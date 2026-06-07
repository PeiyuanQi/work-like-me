#!/usr/bin/env python3
"""
The Simulacrum - A long-running agent that replicates the user.

This agent:
- Loads skills from every group under wlm/plugins
- Uses ~/.wlm/memory/ for persistent memory
- Runs continuously, processing tasks from a queue or stdin
- Supports headless mode with file-based message queue
"""

import os
import sys
import json
import logging
import asyncio
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional

import anyio
from claude_agent_sdk import (
    ClaudeAgentOptions,
    query,
    ClaudeSDKClient,
    ResultMessage,
    SystemMessage,
)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("simulacrum")


# Paths - go up from the-simulacrum/src to the repo root
WORK_LIKE_ME_ROOT = Path(__file__).parent.parent.parent
WLMSKILLS_DIR = WORK_LIKE_ME_ROOT / "wlm" / "plugins"
MEMORY_DIR = Path.home() / ".wlm" / "memory"

# Config files
LOCAL_ENV = Path(__file__).parent.parent / ".env"
GLOBAL_ENV = Path.home() / ".wlm" / "simulacrum.env"

# SOUL files - natural language
LOCAL_SOUL = Path(__file__).parent.parent / "SOUL.md"
GLOBAL_SOUL = Path.home() / ".wlm" / "SOUL.md"

# Headless mode config
QUEUE_DIR = Path.home() / ".wlm" / "queue"


def load_config() -> dict:
    """Load configuration from .env file."""
    import os

    config = {
        "mode": "interactive",
        "queue_dir": str(QUEUE_DIR),
        "model": "claude-opus-4-6",
        "max_turns": 50,
        "permission_mode": "acceptEdits",
    }

    # Try local .env first, then global
    env_file = None
    if LOCAL_ENV.exists():
        env_file = LOCAL_ENV
        logger.info(f"Loading config from local: {LOCAL_ENV}")
    elif GLOBAL_ENV.exists():
        env_file = GLOBAL_ENV
        logger.info(f"Loading config from global: {GLOBAL_ENV}")

    if env_file:
        # Parse .env format
        for line in env_file.read_text().split("\n"):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()

    return config


def get_communication_config() -> dict:
    """Get communication configuration."""
    return load_config()


def get_soul_file() -> Optional[Path]:
    """Get the SOUL.md file (local takes precedence)."""
    if LOCAL_SOUL.exists():
        logger.info(f"Loading SOUL from local: {LOCAL_SOUL}")
        return LOCAL_SOUL
    if GLOBAL_SOUL.exists():
        logger.info(f"Loading SOUL from global: {GLOBAL_SOUL}")
        return GLOBAL_SOUL
    logger.warning("No SOUL.md found")
    return None


def load_skill_directories() -> list[Path]:
    """Load skill directories from wlm plugins."""
    skills = []

    if not WLMSKILLS_DIR.exists():
        return skills

    for plugin_dir in sorted(WLMSKILLS_DIR.iterdir()):
        plugin_skills = plugin_dir / "skills"
        if not plugin_skills.exists():
            continue
        for skill_dir in sorted(plugin_skills.iterdir()):
            if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                skills.append(skill_dir)

    return skills


def load_skill_content(skill_dir: Path) -> dict:
    """Load skill content from SKILL.md file."""
    skill_file = skill_dir / "SKILL.md"

    if not skill_file.exists():
        return {"name": skill_dir.name, "content": ""}

    content = skill_file.read_text()

    # Extract skill name from first heading
    lines = content.strip().split("\n")
    name = skill_dir.name
    for line in lines:
        if line.startswith("# "):
            name = line[2:].strip()
            break

    return {
        "name": name,
        "content": content,
        "path": str(skill_dir)
    }


def build_system_prompt() -> str:
    """Build the system prompt with loaded skills."""
    skills = load_skill_directories()
    skill_contents = [load_skill_content(s) for s in skills]

    # Load SOUL.md as natural language context
    soul_text = ""
    soul_file = get_soul_file()
    if soul_file:
        soul_text = soul_file.read_text()

    # Build memory context
    memory_context = ""
    if MEMORY_DIR.exists():
        memory_files = list(MEMORY_DIR.rglob("*.md"))
        if memory_files:
            memory_context = "\n\n## Memory Files\n"
            for mf in memory_files[:10]:  # Limit to 10 files
                memory_context += f"\n### {mf.relative_to(MEMORY_DIR)}\n{mf.read_text()[:1000]}\n"

    # Use system prompt from SOUL - it must exist
    if not soul_text:
        raise ValueError("SOUL.md not found. Please create SOUL.md in the simulacrum directory or at ~/.wlm/SOUL.md")

    prompt = f"""# The Simulacrum

{soul_text}

## Available Memory

The user's memory is stored at: {MEMORY_DIR}

{memory_context}

## Available Skills

You have access to skills from the following categories:

"""

    for skill in skill_contents:
        prompt += f"\n### {skill['name']}\n"
        prompt += f"Location: {skill['path']}\n"
        # Include first part of skill content
        content_lines = skill['content'].split("\n")[:50]
        prompt += "\n".join(content_lines)
        if len(skill['content'].split("\n")) > 50:
            prompt += "\n... (see full skill file for details)"

    prompt += """

## Operating Principles

1. First Principle Thinking - always start from fundamentals
2. Use skills when they match the task
3. Update memory after significant learnings
4. Ask for clarification when needed
5. Be proactive but don't overstep

## Tools

You have access to:
- Read, Write, Edit - file operations
- Bash - shell commands
- Glob, Grep - search
- WebSearch, WebFetch - web access
- Agent - spawn subagents

When you need to use a skill:
1. Read the SKILL.md file for that skill
2. Follow the steps outlined in the skill
3. Report results back

"""

    return prompt


async def run_agent_task(prompt: str, options: ClaudeAgentOptions):
    """Run a single task with the agent."""
    logger.info(f"Running task: {prompt[:100]}...")

    try:
        async for message in query(prompt=prompt, options=options):
            if isinstance(message, ResultMessage):
                logger.info(f"Task completed: {message.result[:200]}...")
                return message.result
            elif isinstance(message, SystemMessage):
                if hasattr(message, 'session_id'):
                    logger.info(f"Session started: {message.session_id}")

        return "No result returned"
    except Exception as e:
        logger.error(f"Error running task: {e}")
        return f"Error: {str(e)}"


async def interactive_mode(options: ClaudeAgentOptions):
    """Run in interactive mode, reading from stdin."""
    logger.info("Starting Simulacrum in interactive mode")
    logger.info(f"Memory: {MEMORY_DIR}")
    logger.info(f"Skills loaded: {len(load_skill_directories())}")
    logger.info("Enter tasks (Ctrl+C to exit, 'quit' to exit)")

    while True:
        try:
            task = input("> ")
            if task.lower() in ("quit", "exit", "q"):
                logger.info("Shutting down...")
                break

            if not task.strip():
                continue

            result = await run_agent_task(task, options)
            logger.info(f"Result: {result[:200]}...")

        except KeyboardInterrupt:
            logger.info("Shutting down...")
            break
        except EOFError:
            break


async def batch_mode(options: ClaudeAgentOptions, tasks: list[str]):
    """Run a batch of tasks."""
    for i, task in enumerate(tasks, 1):
        logger.info(f"Running task {i}/{len(tasks)}")
        result = await run_agent_task(task, options)
        logger.info(f"Task {i} completed: {result[:200]}...")


async def headless_mode(options: ClaudeAgentOptions):
    """Run in headless mode - process tasks from queue directory."""
    logger.info("Starting Simulacrum in headless mode")
    logger.info(f"Queue: {QUEUE_DIR}")
    logger.info(f"Memory: {MEMORY_DIR}")
    logger.info(f"Skills: {len(load_skill_directories())}")
    logger.info("Waiting for tasks...")

    # Ensure queue directory exists
    QUEUE_DIR.mkdir(parents=True, exist_ok=True)

    # Track processed tasks
    processed_file = QUEUE_DIR / ".processed"

    def get_processed_ids() -> set:
        if processed_file.exists():
            return set(processed_file.read_text().strip().split("\n"))
        return set()

    def mark_processed(task_id: str):
        processed = get_processed_ids()
        processed.add(task_id)
        processed_file.write_text("\n".join(processed))

    while True:
        try:
            # Find pending tasks
            pending = sorted(QUEUE_DIR.glob("task-*.json"))
            processed = get_processed_ids()

            for task_file in pending:
                task_id = task_file.stem
                if task_id in processed:
                    continue

                # Read task
                try:
                    task_data = json.loads(task_file.read_text())
                    user_prompt = task_data.get("prompt", "")
                    task_type = task_data.get("type", "default")
                except Exception as e:
                    logger.error(f"Error reading task {task_file}: {e}")
                    continue

                logger.info(f"Processing task: {task_id} - {user_prompt[:50]}...")
                logger.info(f"[TASK] {task_id}: {user_prompt[:50]}...")

                # Run task
                result = await run_agent_task(user_prompt, options)

                # Write result
                result_file = QUEUE_DIR / f"{task_id}.result.json"
                result_file.write_text(json.dumps({
                    "task_id": task_id,
                    "status": "completed",
                    "result": result,
                }))

                # Mark as processed
                mark_processed(task_id)
                logger.info(f"Task completed: {task_id}")

            # Sleep before next poll
            await asyncio.sleep(2)

        except KeyboardInterrupt:
            logger.info("Shutting down...")
            break
        except Exception as e:
            logger.error(f"Error in headless loop: {e}")
            await asyncio.sleep(5)


async def main():
    """Main entry point."""
    # Load SOUL for configuration
    soul = load_soul()
    communication = get_communication_config()

    # Check for headless mode
    headless = "--headless" in sys.argv or communication.get("mode") == "headless"

    # Build system prompt with skills
    system_prompt = build_system_prompt()

    # Configure agent options
    options = ClaudeAgentOptions(
        cwd=str(WORK_LIKE_ME_ROOT),
        system_prompt=system_prompt,
        allowed_tools=[
            "Read", "Write", "Edit", "Bash", "Glob", "Grep",
            "WebSearch", "WebFetch", "Agent"
        ],
        permission_mode="acceptEdits",
        max_turns=50,
    )

    # Parse remaining arguments
    args = [a for a in sys.argv[1:] if a != "--headless"]

    if headless:
        print_server_log(f"Starting Simulacrum in headless mode")
        print_server_log(f"Memory: {MEMORY_DIR}")
        print_server_log(f"Queue: {QUEUE_DIR}")
        await headless_mode(options)
    elif len(args) > 0:
        # Batch mode - tasks passed as arguments
        tasks = args
        await batch_mode(options, tasks)
    else:
        # Interactive mode
        await interactive_mode(options)


if __name__ == "__main__":
    anyio.run(main)
