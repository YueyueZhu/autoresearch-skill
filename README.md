# Autoresearch Skill

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/9/9b/Mao_Tse_Tung.jpg" alt="Mao Zedong portrait" width="260">
</p>

<h2 align="center">世界是你们滴</h2>

<p align="center">
  Image source: <a href="https://commons.wikimedia.org/wiki/File:Mao_Tse_Tung.jpg">Wikimedia Commons, Mao Tse Tung.jpg</a>.
</p>

Autoresearch is a Codex skill for automated and semi-automated deep learning research loops.

It creates and maintains an `AUTORESEARCH.md` control document inside your project directory, then uses that document to preserve context across long runs, network interruptions, and Codex restarts.

## What It Does

- Interviews the user for the deep learning work directory, task, metric, run command, GPUs, tmux preference, and allowed edit surface.
- Creates a persistent `AUTORESEARCH.md` recovery ledger.
- Prioritizes official GitHub implementations when papers or repositories are referenced.
- Requires each idea to include a top-conference-level novelty statement, targeting NeurIPS, ICLR, CVPR, or AAAI-style research ambition.
- Edits only approved files or code regions.
- Runs fixed-budget experiments, preferably in tmux.
- Parses logs for latest and best metrics.
- Marks experiments as `keep`, `discard`, `crash`, or `running`.
- Records every hypothesis, code change, result, and decision.

## Typical Prompt

```text
Use the autoresearch skill for this deep learning project.
Work directory: /path/to/project
Task: improve validation Dice.
Metric: mdice, higher is better.
Current best: 0.824.
Run command: sh train.sh.
Use tmux session 0.
Allowed edit surface: only loss.py, function consistency_loss().
Available GPUs: 0,1.
```

## Recovery

If the session disconnects, resume with:

```text
Read /path/to/project/AUTORESEARCH.md and continue the automated autoresearch task.
```

## Files

- `SKILL.md`: Codex-facing skill instructions.
- `references/AUTORESEARCH_TEMPLATE.md`: full persistent control-document template.
- `references/INTERVIEW_QUESTIONS.md`: startup checklist.
- `references/ITERATION_PROTOCOL.md`: experiment loop protocol.
- `references/LOG_PARSING_GUIDE.md`: metric parsing guide.
- `scripts/init_autoresearch.py`: optional helper to create a starter `AUTORESEARCH.md`.
- `scripts/append_experiment.py`: optional helper to append experiment-log rows.

## Scope

This skill is designed for deep learning workflows such as segmentation, classification, detection, language modeling, medical imaging, self-supervised learning, and semi-supervised learning.

It is not tied to the original `karpathy/autoresearch` repository. It adapts the workflow to arbitrary local projects.
