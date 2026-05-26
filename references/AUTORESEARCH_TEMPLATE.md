# AUTOMATED AUTORESEARCH TASK

This file is the persistent control document for an automated Codex autoresearch loop. If the network disconnects, Codex restarts, or chat context is lost, resume by reading this file first and continue from the latest `Experiment Log` entry.

## Automation Status

- Mode: automated iterative deep learning experiment loop, with human-bounded scope.
- Work directory: `<ABSOLUTE_PROJECT_RUN_DIRECTORY>`
- Project: `<PROJECT_NAME>`
- User task: `<TASK>`
- Primary metric: `<METRIC>`
- Metric direction: `<higher-is-better | lower-is-better>`
- Current best reference: `<BEST_RESULT>`
- Target result/effect: `<TARGET>`
- Active run command: `<COMMAND>`
- Active log file: `<LOG_PATH>`
- Reusable terminal: `<tmux | other | none>`
- tmux target: `<SESSION>`
- Available GPUs: `<GPU_IDS>`
- Current experiment: `<EXPERIMENT_NAME>`
- Current status: `<planning | ready | running | keep | discard | crash>`

## Research Policy

- Prefer official GitHub implementations when papers, methods, or repositories are referenced.
- If official GitHub is unavailable, use primary sources such as the paper, project page, or official documentation.
- Ideas should aim for top-conference-level novelty, comparable in ambition to NeurIPS, ICLR, CVPR, or AAAI standards.
- Novelty does not require broad code changes. It requires a clear mechanism, a reason it could generalize, and a testable hypothesis.
- Adapt only the relevant idea into the allowed edit surface.
- Do not change evaluation, data, baseline scripts, or unrelated training logic unless explicitly approved.
- Each experiment should have one main idea so the result is interpretable.

## User Constraints

- Allowed edit files:
  - `<file>`
- Allowed edit regions:
  - `<function/loss/module/code block>`
- Forbidden files:
  - `<file>`
- Forbidden behavior:
  - changing validation metric
  - changing dataset split
  - changing unrelated hyperparameters
  - overwriting user changes
- Runtime budget per experiment: `<TIME>`
- Resource limits: `<GPU/MEMORY/CPU>`
- Notes from user:
  - `<NOTES>`

## Resume Protocol

When resuming or continuing this task:

1. Read this file from top to bottom.
2. Check whether the current run is still active.
3. If using tmux:

```bash
tmux capture-pane -t <SESSION> -p -S -80
```

4. Check the active log:

```bash
tail -n 120 <LOG_PATH>
```

5. Extract latest and best validation metrics.
6. Compare the result with the current best reference.
7. Update the `Experiment Log`:
   - `keep` if the metric improves enough to justify complexity.
   - `discard` if the metric is worse, equal with more complexity, unstable, or violates constraints.
   - `crash` if the run fails for a reason inherent to the idea.
   - `running` if the job is still active.
8. If the result is `discard`, remove or supersede only the failed experiment's allowed-scope change.
9. If the result is `keep`, update the best reference and record why the change is worth keeping.
10. Ask whether new papers or GitHub repositories should be added as references for the next iteration.
11. Propose the next single experiment with a novelty statement.
12. Before editing or launching, update this file with experiment name, hypothesis, code scope, run command, log file, and launch time.
13. Run syntax, import, or smoke checks when feasible.
14. Launch the next run.

Do not rely on chat memory for decisions. Treat this file as the source of truth for automation state.

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

Command:

```bash
<COMMAND>
```

If multiple commands are required, create or record a unified runner:

```bash
sh <RUNNER_SCRIPT>
```

Environment:

```text
<ENVIRONMENT_NOTES>
```

GPU setting:

```text
<GPU_IDS_AND_HOW_USED>
```

## Metric Definition

- Primary metric:
- Direction:
- Current best:
- Target:
- Validation frequency:
- Log parsing rule:
- Secondary metrics:

## Current Code Path

Describe the exact code path being optimized.

```python
<KEY_CODE_SNIPPET>
```

## Innovation Boundary

Future experiments should not be limited to tiny parameter tweaks unless the tweak tests a larger mechanism. Ideas should be bold enough to be described as a research contribution, while staying inside the allowed edit surface.

Allowed ideas:

- official GitHub implementation adaptations
- top-conference-level loss redesigns
- uncertainty-aware objectives
- curriculum schedules
- teacher-student consistency mechanisms
- contrastive or representation-learning additions
- boundary-aware, foreground-aware, class-balance-aware, or data-quality-aware weighting
- robustness, calibration, or self-training mechanisms
- architecture-local modules if the allowed edit surface includes model code

Forbidden without explicit approval:

- changing validation metric code
- changing dataset splits or labels
- changing unrelated training hyperparameters
- changing shell scripts unless approved
- changing optimizer/scheduler unless approved
- editing outside the allowed files/regions

## Code Change History

This section summarizes all code changes made so far. Use it as the quick recovery record after disconnects.

### Original State

- `<WHAT_THE_ORIGINAL_CODE_DID>`

### Experiment 1: `<NAME>`

- Status: `<ready | running | keep | discard | crash>`
- Novelty target: top-conference-level mechanism, not routine tuning.
- Novelty statement:
  - `<WHY_THIS_IDEA_IS_CONCEPTUALLY_NEW_OR_INTERESTING>`
- Hypothesis:
  - `<TESTABLE_HYPOTHESIS>`
- References:
  - Paper/project:
  - Official GitHub:
  - Files/functions consulted:
- Files changed:
  - `<FILE>`
- Exact code region:
  - `<FUNCTION_OR_LINES>`
- Implementation:
  - `<SUMMARY>`
- Validation:
  - launch time:
  - command:
  - log:
  - best metric:
  - latest/final metric:
- Decision:
  - `<keep | discard | crash | running>`
- Rationale:
  - `<WHY>`

## Current Experiment Plan

Experiment name: `<NAME>`

Novelty level:
- Target: NeurIPS/ICLR/CVPR/AAAI-style research contribution.
- Statement: `<MECHANISM_AND_WHY_IT_IS_NONTRIVIAL>`

Reference:
- Paper/site:
- Official GitHub:
- Code consulted:

Hypothesis:
`<HYPOTHESIS>`

Allowed code change:
- `<FILES_AND_REGIONS>`

Implementation plan:
- `<STEP>`

Validation plan:
- Run command:
- Log:
- Metric:
- Expected signal:
- Failure rule:

## Experiment Log

| Date | Experiment | Novelty statement | Command | Result | Decision | Notes |
|---|---|---|---|---|---|---|
| `<DATE>` | baseline | reference state | `<COMMAND>` | `<METRIC>` | reference | `<NOTES>` |
