# Machine Learning Engineering Plugin

MLE workflow skills for diagnosing and improving training systems across model,
data, runtime, hardware, and distributed-synchronization boundaries.

## Skills

- `distributed-training-stability-engineering`: diagnose scale-out regressions,
  stragglers, tail-latency spikes, data-pipeline stalls, and deterministic
  performance fixes in synchronous distributed training.

## Workflow Preferences

- Treat large-scale training performance as a distributed reliability problem,
  not only an average-throughput problem.
- Establish the synchronization domain, collect per-rank evidence, and use a
  scale-aware spike budget before choosing an optimization.
- Preserve data ordering, sample coverage, numerical behavior, and checkpoint
  correctness while changing the pipeline.
- Prefer reversible, measurable changes that convert random interference into a
  predictable cost.
