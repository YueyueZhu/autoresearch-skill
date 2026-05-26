#!/usr/bin/env python3
"""Create a starter AUTORESEARCH.md from simple key=value arguments."""

from __future__ import annotations

import argparse
from pathlib import Path


TEMPLATE = """# AUTOMATED AUTORESEARCH TASK

This file is the persistent control document for an automated Codex autoresearch loop. If the network disconnects, Codex restarts, or chat context is lost, resume by reading this file first and continue from the latest `Experiment Log` entry.

## Automation Status

- Mode: automated iterative deep learning experiment loop, with human-bounded scope.
- Work directory: {workdir}
- Project: {project}
- User task: {task}
- Primary metric: {metric}
- Metric direction: {direction}
- Current best reference: {best}
- Target result/effect: {target}
- Active run command: {command}
- Active log file: {log}
- Reusable terminal: {terminal}
- tmux target: {tmux}
- Available GPUs: {gpus}
- Current experiment: planning
- Current status: planning

## Research Policy

- Prefer official GitHub implementations when papers, methods, or repositories are referenced.
- Ideas should aim for top-conference-level novelty, comparable in ambition to NeurIPS, ICLR, CVPR, or AAAI standards.
- Adapt only the relevant idea into the allowed edit surface.
- Do not change evaluation, data, baseline scripts, or unrelated training logic unless explicitly approved.
- Each experiment should have one main idea so the result is interpretable.

## User Constraints

- Allowed edit files:
  - TBD
- Allowed edit regions:
  - TBD
- Forbidden files:
  - TBD
- Forbidden behavior:
  - changing validation metric code
  - changing dataset split
  - changing unrelated hyperparameters
  - overwriting user changes
- Runtime budget per experiment: TBD
- Resource limits: {gpus}
- Notes from user:
  - TBD

## Resume Protocol

1. Read this file from top to bottom.
2. Check whether the current run is still active.
3. Check tmux if used:

```bash
tmux capture-pane -t {tmux} -p -S -80
```

4. Check the active log:

```bash
tail -n 120 {log}
```

5. Extract latest and best validation metrics.
6. Compare the result with the current best reference.
7. Update the `Experiment Log`.
8. Ask whether new papers or GitHub repositories should be added as references for the next iteration.
9. Propose the next single experiment with a top-conference-level novelty statement.
10. Update this file before editing or launching.

## Files Read

- Entrypoint:
- Run script:
- Config:
- Trainer:
- Loss:
- Model:
- Dataset:
- Evaluation metric:
- Active log:

## Training Entry

```bash
{command}
```

## Metric Definition

- Primary metric: {metric}
- Direction: {direction}
- Current best: {best}
- Target: {target}
- Log parsing rule: TBD

## Current Code Path

```text
TBD
```

## Innovation Boundary

Allowed:
- TBD

Forbidden without explicit approval:
- changing validation metric code
- changing dataset splits or labels
- changing unrelated training hyperparameters
- editing outside the allowed files/regions

## Code Change History

### Original State

- TBD

## Current Experiment Plan

Experiment name: TBD

Novelty level:
- Target: NeurIPS/ICLR/CVPR/AAAI-style research contribution.
- Statement: TBD

Hypothesis:
- TBD

Allowed code change:
- TBD

Validation plan:
- TBD

## Experiment Log

| Date | Experiment | Novelty statement | Command | Result | Decision | Notes |
|---|---|---|---|---|---|---|
| TBD | baseline | reference state | `{command}` | {best} | reference | initialized |
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workdir", required=True)
    parser.add_argument("--project", default="TBD")
    parser.add_argument("--task", default="TBD")
    parser.add_argument("--metric", default="TBD")
    parser.add_argument("--direction", default="TBD")
    parser.add_argument("--best", default="TBD")
    parser.add_argument("--target", default="TBD")
    parser.add_argument("--command", default="TBD")
    parser.add_argument("--log", default="TBD")
    parser.add_argument("--terminal", default="tmux")
    parser.add_argument("--tmux", default="0")
    parser.add_argument("--gpus", default="TBD")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    workdir = Path(args.workdir).expanduser().resolve()
    output = workdir / "AUTORESEARCH.md"
    if output.exists() and not args.force:
        raise SystemExit(f"{output} already exists; pass --force to overwrite")

    output.write_text(TEMPLATE.format(**vars(args)), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
