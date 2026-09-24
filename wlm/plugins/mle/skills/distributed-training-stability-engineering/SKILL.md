---
name: distributed-training-stability-engineering
description: "Diagnoses and stabilizes large-scale synchronous ML training when scale-out exposes stragglers, tail-latency spikes, data-pipeline stalls, or throughput collapse. Use for evidence-led performance and reliability work across ranks, hosts, storage, CPU, GPU, NCCL collectives, data loaders, runtime, and synchronization boundaries. Not for model-quality tuning or generic single-GPU benchmarking."
---

# Distributed Training Stability Engineering

Treat synchronous distributed training as a reliability problem, not only an
average-throughput problem. The useful result is a measured explanation of
which rank or pipeline stage sets the global step time, a scale-aware fix, and
proof that the fix improves the target topology without changing data or model
semantics.

## Operating model

For a synchronized step, the slowest participating rank controls completion:

```text
cluster_step_time = max(rank_step_time_1, ..., rank_step_time_N)
```

If a rank has an independent per-step spike probability `p`, the probability
that at least one of `N` synchronized participants spikes is:

```text
cluster_spike_probability = 1 - (1 - p)^N
```

Use the actual synchronization domain for `N` (ranks, GPUs, or another
collective participant set), and state the independence approximation. If the
allowed cluster spike probability is `q`, the implied local target is:

```text
p <= 1 - (1 - q)^(1/N)
```

These equations are planning tools, not universal thresholds. Calculate the
target from the workload's scale and reliability budget rather than importing a
fixed number such as 0.5% into every training job.

Separate mean savings from tail cost. A loader or preprocessing change that
saves a few milliseconds on an isolated host can lose at scale if it increases
rare stalls. Compare the full step-time distribution, spike rate, and worst
rank, not only the mean.

## Workflow

### 1. Establish the topology and success gates

Record the training revision, framework/runtime versions, node and GPU count,
rank-to-host mapping, collective used, batch and sequence semantics, storage
layout, and target scale. Define success gates before changing code:

- local spike definition and acceptable `p`
- cluster P95/P99/max step time and observed spike rate
- throughput at the target scale
- data ordering, sample coverage, loss, and checkpoint correctness
- memory headroom and recovery behavior after a long run

Measure enough steps to catch rare events. Keep per-rank records for data,
forward, backward, communication, barrier, and total step time, and retain rank
IDs and timestamps for every outlier.

### 2. Prove or exclude a communication bottleneck

Benchmark the relevant collectives with the repository's supported tool (for
example, `nccl-tests` for NCCL) and compare bus bandwidth and latency across
hosts. A slowdown after scale-out does not by itself make the network the
bottleneck. If the collective is healthy and rank distributions are consistent,
move the investigation to rank-local work and synchronization amplification.

Use controlled isolation experiments:

1. Replace the real input path with fixed or fake data while preserving the
   model and collective shape. Stable timing points to the data/input path.
2. A/B synchronous and asynchronous input delivery at the same scale. Compare
   tail distributions, not just average `data_time`.
3. Run a short single-host baseline, then a small multi-host baseline, then the
   target topology. Keep seeds, data slices, batch shape, and run length fixed.

### 3. Measure without changing the system

Instrumentation can itself cause the stall. Keep `torch.cuda.synchronize()` and
`dist.barrier()` out of per-step hot paths, even to make timings look precise: a
barrier turns one rank's delay into everyone's delay, and
synchronization-heavy profilers can create the very tail they are supposed to
measure.

Use a no-op or low-interference profiler for normal runs. Reserve exact GPU
timing and forced synchronization for short profiling sessions, and label those
results as instrumented. For straggler detection, collect kernel/CUDA API or
host traces when available and compare ranks with robust statistics such as
median absolute deviation (MAD) or interquartile range (IQR). Report the
outlier rank, operation, duration, and reproduction window.

### 4. Trace the complete input-to-step pipeline

Follow one sample or batch from storage to the synchronized step. Check each
domain separately:

- **Storage:** cache/readahead settings, cold reads, metadata or LMDB lookup
  outliers, retries, and corrupted/dirty samples. Measure per-sample latency;
  batch averages hide one cold read that stalls the whole rank.
- **Data semantics:** keep temporally dependent frames or clips on the same
  rank and preserve their order. A sample-level random sampler can silently
  break sequence models while making timing look healthy.
- **CPU preprocessing:** GIL-bound Python work, worker oversubscription,
  context switching, CPU affinity, NUMA locality, memory bandwidth, and dense
  transforms such as color conversion or resize.
- **Host/GPU transfer:** H2D and D2H traffic, PCIe/NVLink contention, pinned
  memory allocation, and CUDA-context lock contention between loader threads
  and kernel launches.
- **Memory:** host allocator pauses, CUDA allocator fragmentation, dynamic
  shapes, transient allocation peaks, and insufficient headroom.
- **Runtime:** automatic GC, allocator background decay, periodic logging,
  plotting, checkpoint serialization, and other work that lands on the hot
  path.
- **Hardware/rank health:** persistent slow kernels, clocks, thermals, ECC or
  fabric errors, and nodes whose latency distribution is shifted rather than
  merely noisy.

### 5. Convert random interference into a budgeted cost

Prefer changes that make latency predictable while preserving correctness:

- remove redundant global barriers and reduce hot-path logging
- bind workers to the appropriate CPU/NUMA domain and tune worker count from
  measurements, not folklore
- prewarm storage caches or reuse a known-good sample instead of performing an
  unbounded random retry
- preallocate and reuse pinned buffers when shapes permit it
- move dense, embarrassingly parallel preprocessing to a separate CUDA stream
  only after checking transfer and compute contention
- schedule expensive maintenance at a fixed interval or off the hot path
- make GC or allocator reclamation explicit and infrequent only when a measured
  pause justifies it, and keep a memory-safety and leak check

Runtime-specific settings such as
`PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` or
`TCMALLOC_RELEASE_RATE=0` are hypotheses to test, not portable defaults. Check
framework, allocator, driver, and container versions before enabling them.

### 6. Evaluate asynchronous loaders as a scale-dependent tradeoff

An asynchronous or triple-buffered loader can hide CPU work and H2D latency,
but it may also contend for PCIe/NVLink bandwidth, DRAM bandwidth, NUMA memory,
or the process-wide CUDA context lock. For each A/B run, record:

- mean and tail `data_time`, forward time, and total step time
- local spike probability before and after
- predicted and observed cluster spike probability at the target `N`
- GPU idle time, transfer volume, CPU utilization by core, and memory headroom

Enable the asynchronous path only when its net benefit remains positive at the
target scale. A deterministic fixed cost is often preferable to a smaller mean
with a larger random tail.

## Verification and handoff

For every proposed fix, keep a small experiment table with the baseline, one
change, topology, run length, local and cluster tail metrics, correctness
checks, and rollback condition. Re-run at one host, a representative multi-host
size, and the target size. Verify that:

- the intended outlier or pipeline stage changed, rather than the delay merely
  moving elsewhere
- the collective remains healthy and no rank is silently dropped
- sequence order, sample coverage, loss behavior, and checkpoints are intact
- P95/P99/max and spike probability improve without unacceptable mean or
  memory regressions
- long-running behavior stays stable after caches warm and periodic work fires

Report confirmed evidence, remaining hypotheses, and the next measurement. The
target distributed run is the proof boundary: a clean single-host run or a
"command succeeded" signal does not establish scale-out readiness.

## Anti-patterns

- Averaging away the slowest rank, or relying only on aggregate GPU
  utilization.
- Assuming more workers, asynchronous loading, or GPU preprocessing is faster
  without a target-scale A/B measurement.
- Adding barriers or forced synchronization during steady-state training to
  make dashboards easier to read.
- Disabling GC, allocator cleanup, retries, or safety checks blindly.
- Treating a fixed threshold, vendor tool, or one article's topology as a
  universal contract.
- Changing sampler semantics, data order, or retry behavior while claiming a
  pure performance result.
