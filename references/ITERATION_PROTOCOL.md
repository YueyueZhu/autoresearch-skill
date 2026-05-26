# Autoresearch Iteration Protocol

Use this protocol after `AUTORESEARCH.md` exists.

## Before Each Experiment

1. Read `AUTORESEARCH.md`.
2. Inspect tmux/process status and the active log.
3. Decide whether the previous run is `running`, `keep`, `discard`, or `crash`.
4. Update `AUTORESEARCH.md` before making another change.
5. Ask the user whether a new paper, method, or GitHub repository should be added as a reference.
6. If a reference is provided, prioritize official GitHub code and primary sources.
7. Propose one experiment only.

## Experiment Idea Requirements

Each idea must include:

- a short experiment name
- a top-conference-level novelty statement
- a mechanism, not just a parameter tweak
- the exact approved edit surface
- what should improve and why
- what failure would mean
- how the metric will be parsed

Good idea framing:

```text
Novelty statement: Introduce uncertainty-conditioned consistency weighting that distinguishes ambiguous mixed pixels from genuinely hard foreground boundaries, inspired by <official GitHub implementation>, but adapted only inside <allowed loss>.
```

Weak idea framing:

```text
Change threshold from 0.8 to 0.75.
```

A threshold change can be acceptable only if it is part of a documented mechanism such as curriculum expansion, adaptive confidence calibration, or uncertainty-gated sample selection.

## Launching Runs

Default tmux launch:

```bash
tmux send-keys -t <SESSION> '<COMMAND>' C-m
```

If a run uses multiple commands, create or ask to create a runner script:

```bash
sh <RUNNER_SCRIPT>
```

After launch, confirm:

- tmux pane shows the command started
- log file received a new timestamp or header
- no immediate syntax/import/runtime error occurred

## Keep / Discard

Keep if:

- primary metric improves beyond noise
- complexity is justified by improvement
- runtime and memory remain acceptable
- result does not rely on changing forbidden code

Discard if:

- primary metric is worse
- equal metric with higher complexity
- late-training instability makes the result unreliable
- run crashes for idea-related reasons
- change violates allowed edit scope

Crash handling:

- Fix obvious typos or shape errors once if the idea remains valid.
- If the idea itself is incompatible, record `crash` and move on.

## Recovery

If Codex reconnects or the user starts a new session:

```text
Read <workdir>/AUTORESEARCH.md and continue the automated autoresearch task.
```

Then follow the Resume Protocol in the file.
