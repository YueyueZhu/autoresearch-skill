---
name: autoresearch
description: Use when running automated or semi-automated deep learning research loops: interview the user for the project directory, task, metric, run command, GPUs, tmux preference, and allowed edit surface; create and maintain AUTORESEARCH.md as a persistent recovery ledger; prioritize official GitHub implementations for paper-inspired ideas; propose top-conference-level novel experiments; run fixed-budget training jobs; parse logs; and keep or discard changes by validation metrics.
metadata:
  source: https://github.com/karpathy/autoresearch
---

# Autoresearch

This skill adapts the `karpathy/autoresearch` idea into a general deep learning workflow. It is for iterative model, loss, trainer, or data-pipeline experiments where Codex records context, proposes one clear research idea, edits only approved code, launches a bounded run, parses metrics, and decides whether to keep or discard the change.

## Core Rule

`AUTORESEARCH.md` is the source of truth. Create it in the user's project run directory before any code change. If the network disconnects or Codex restarts, resume by reading this file first.

Use the full template in `references/AUTORESEARCH_TEMPLATE.md` when creating or refreshing the file.

## Startup Interview

Before starting automation, ask for the required context. Use `references/INTERVIEW_QUESTIONS.md` for the full checklist.

Required answers:

1. Deep learning work directory.
2. Task, primary metric, metric direction, current best result, and target result.
3. Whether papers or repositories should be added as references before each iteration.
4. Exact run command or files to run. If there are multiple commands, offer to create a unified `.sh` script.
5. Whether to run in a reusable terminal. Default: tmux.
6. Exact files, functions, losses, modules, or code regions that may be modified.
7. Available GPU IDs and whether the run command may be updated to use them.
8. Runtime budget and stopping criteria for each experiment.

If the user already provided some answers, do not ask again. Summarize the known context and ask only for missing or risky details.

## Research Standard

Ideas should aim beyond routine tuning. Each proposed experiment must include a novelty statement and should target the conceptual standard of top ML/CV venues such as NeurIPS, ICLR, CVPR, or AAAI.

This does not mean every experiment must be large or risky. It means the idea should be framed as a research contribution: a clear mechanism, a reason it could generalize, and a testable hypothesis. Prefer ideas inspired by official GitHub implementations of relevant papers, then adapt only the relevant mechanism into the approved edit surface.

Avoid spending long runs on trivial threshold tweaks unless they are part of a larger, documented research hypothesis.

## Workflow

1. Read or create `AUTORESEARCH.md`.
2. Inspect only the needed project files: entrypoint, run scripts, trainer, loss, model, config, metric code, and active logs.
3. Record allowed and forbidden edit surfaces.
4. Propose one experiment with:
   - name
   - hypothesis
   - novelty level
   - references, especially official GitHub sources
   - exact code scope
   - validation metric and stopping rule
5. Update `AUTORESEARCH.md` before editing.
6. Edit only the approved code region.
7. Run syntax, import, or smoke checks when feasible.
8. Launch the run. Default tmux command:

```bash
tmux send-keys -t <session> '<run command>' C-m
```

9. Monitor tmux/logs enough to confirm the run started.
10. On resume, parse the latest and best metric from logs.
11. Mark the experiment:
    - `keep`: improves the primary metric enough to justify complexity.
    - `discard`: worse, equal with more complexity, unstable, or violates constraints.
    - `crash`: failed because of the idea or irrecoverable runtime issue.
    - `running`: still active.
12. Record every decision in `AUTORESEARCH.md`.

For detailed iteration rules, read `references/ITERATION_PROTOCOL.md`.

## Safety

- Never change data loading, evaluation metrics, baseline scripts, or unrelated files unless the user explicitly approves.
- Never overwrite unrelated user changes.
- Before reverting an experiment, inspect the diff and ensure only the experiment's changes are affected.
- Ask before destructive commands.
- If a referenced paper, project, package, or rule may have changed, verify with official or primary sources when network/tools are available.

## Log Parsing

Adapt parsing to the project. Record both latest and best metric when available. Use `references/LOG_PARSING_GUIDE.md` for common patterns.

## Recovery Message

When finishing setup or launching a long run, tell the user:

```text
If this session disconnects, resume with:
Read <workdir>/AUTORESEARCH.md and continue the automated autoresearch task.
```

## Optional Scripts

Use bundled scripts when helpful:

- `scripts/init_autoresearch.py`: generate a starter `AUTORESEARCH.md`.
- `scripts/append_experiment.py`: append a concise experiment-log row.
