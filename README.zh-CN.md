# Autoresearch Skill

<p align="center">
  <img src="./f17748cf3cd7c1bec26293dc1e40ec32455173280.gif@480w_480h.webp" alt="Maodie meme cat" width="280">
</p>

<h2 align="center">哈基米爱科研</h2>


`autoresearch` is a Codex skill for running automated or semi-automated deep learning research loops.

It is designed for long experiments where one run may take hours, the network may disconnect, and the agent must remember exactly what it changed, why it changed it, how the experiment was launched, and whether the result should be kept or discarded.

The central idea is simple:

> Create an `AUTORESEARCH.md` file inside the project run directory and treat it as the persistent source of truth for the whole research loop.

## What This Skill Is For

Use this skill when you want Codex to help improve a deep learning project through iterative experiments, such as:

- improving segmentation Dice or IoU
- improving classification accuracy, F1, or AUC
- reducing validation loss or perplexity
- redesigning a loss function
- testing a semi-supervised, weakly supervised, or self-supervised idea
- adapting ideas from papers or GitHub repositories into your own training code
- running long experiments in tmux and resuming after interruptions

The skill is not tied to any specific framework. It can be adapted to PyTorch, MONAI, TensorFlow, JAX, Lightning, custom trainers, shell scripts, or ordinary Python training entrypoints.

## Core Behavior

When triggered, the skill guides Codex to:

1. Ask for the deep learning project run directory.
2. Ask for the task, metric, current best result, and target result.
3. Ask whether each iteration should consider new papers or GitHub repositories.
4. Prefer official GitHub implementations when a paper or method is referenced.
5. Ask which command, Python file, or shell script should run the experiment.
6. Offer to create a unified `.sh` runner when multiple commands are needed.
7. Ask whether to use a reusable terminal, defaulting to tmux.
8. Ask which files, functions, losses, modules, or code regions may be modified.
9. Ask which GPU IDs are available.
10. Create or update `AUTORESEARCH.md`.
11. Propose one experiment at a time.
12. Require every idea to include a top-conference-level novelty statement, targeting the ambition of NeurIPS, ICLR, CVPR, or AAAI-style work.
13. Modify only the approved code surface.
14. Launch the run, monitor logs, parse metrics, and record results.
15. Mark each experiment as `keep`, `discard`, `crash`, or `running`.

## Why `AUTORESEARCH.md` Matters

Deep learning experiments are easy to lose track of. A useful run may take 4 to 7 hours. A network interruption can erase chat context. A failed idea may be repeated accidentally if the decision is not recorded.

`AUTORESEARCH.md` solves this by recording:

- project directory
- task and metric
- best known reference result
- target result
- run command
- tmux session
- log file
- available GPUs
- allowed edit surface
- forbidden changes
- files already read
- current code path
- experiment hypothesis
- novelty statement
- paper or GitHub references
- exact code changes
- launch time
- best and latest metrics
- keep/discard/crash decision

If a session disconnects, resume with:

```text
Read /path/to/project/AUTORESEARCH.md and continue the automated autoresearch task.
```

## Research Standard

This skill asks Codex to avoid shallow trial-and-error whenever possible.

Each experiment should have one main research idea and a clear novelty statement. The goal is not merely to tweak a threshold, but to propose a mechanism that could plausibly become a meaningful contribution, such as:

- uncertainty-aware consistency learning
- dynamic curriculum schedules
- teacher-student disagreement modeling
- topology-aware or boundary-aware losses
- class-imbalance-aware pseudo-label filtering
- contrastive objectives for representation alignment
- confidence calibration inside weak supervision
- robust training under noisy labels or mixed samples

Small changes are allowed only when they test a larger mechanism.

## Repository Layout

```text
autoresearch-skill/
├── SKILL.md
├── README.md
├── README.zh-CN.md
├── references/
│   ├── AUTORESEARCH_TEMPLATE.md
│   ├── INTERVIEW_QUESTIONS.md
│   ├── ITERATION_PROTOCOL.md
│   └── LOG_PARSING_GUIDE.md
└── scripts/
    ├── init_autoresearch.py
    └── append_experiment.py
```

## Files

- `SKILL.md`: Codex-facing instructions for the skill.
- `references/AUTORESEARCH_TEMPLATE.md`: full template for the persistent control document.
- `references/INTERVIEW_QUESTIONS.md`: required startup questions.
- `references/ITERATION_PROTOCOL.md`: keep/discard loop and experiment protocol.
- `references/LOG_PARSING_GUIDE.md`: common metric parsing patterns.
- `scripts/init_autoresearch.py`: helper script for creating a starter `AUTORESEARCH.md`.
- `scripts/append_experiment.py`: helper script for appending experiment-log rows.

## Prompt Template

Copy and adapt this prompt when starting a new project:

```text
Use the autoresearch skill for this deep learning project.

Work directory:
/absolute/path/to/my/project

Task:
Improve <metric or behavior>. Prioritize ideas that could be novel enough for NeurIPS, ICLR, CVPR, or AAAI. If I provide a paper or method, first look for the official GitHub implementation and adapt only the relevant idea.

Metric:
Primary metric is <metric_name>, and <higher/lower> is better.
Current best result is <current_best>.
Target result is <target_result>.

Run command:
<python train.py ... or sh train.sh>

Log file:
/absolute/path/to/log.txt

Terminal:
Use tmux by default. tmux session is <session_name_or_id>.

GPU:
Available GPU IDs are <gpu_ids>.

Allowed edit surface:
Only modify <file/function/loss/module/code region>.

Forbidden changes:
Do not change <dataset/evaluation metric/model/shell args/optimizer/etc.>.

Automation:
Create AUTORESEARCH.md in the work directory before changing code. Record all context, hypotheses, code changes, logs, metrics, and keep/discard decisions there. If the session disconnects, resume by reading AUTORESEARCH.md.
```

## Minimal Example

```text
Use the autoresearch skill.
Work directory: /home/user/projects/segmentation-exp
Task: improve validation mdice. Current best is 0.824, target is above 0.83.
Metric: mdice, higher is better.
Run command: sh train.sh.
Log file: /home/user/projects/segmentation-exp/train.log.
Use tmux session 0.
Available GPUs: 0,1.
Only modify losses.py, specifically consistency_loss().
Before each iteration, ask me whether I have a paper or GitHub repository to add.
```

## Installation

Copy this folder into your Codex skills directory:

```bash
cp -a autoresearch-skill ~/.codex/skills/autoresearch
```

Then start a new Codex request that mentions `autoresearch`.

## Notes

This repository packages a local Codex skill. The workflow is inspired by `karpathy/autoresearch`, but generalized for arbitrary deep learning projects.
