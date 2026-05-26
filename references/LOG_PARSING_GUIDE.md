# Log Parsing Guide

Adapt parsing to the target project. Always record:

- latest metric
- best metric if logged
- iteration/epoch
- launch time used to separate old runs from new runs
- whether higher or lower is better

## Common Metric Patterns

Segmentation:

```text
mdice: 0.824
miou: 0.729
dice: 0.824
iou: 0.729
```

Classification:

```text
acc: 0.91
accuracy: 91.0
auc: 0.94
f1: 0.88
val_loss: 0.31
```

Language modeling:

```text
val_loss: 2.31
perplexity: 10.1
val_bpb: 1.04
```

Detection:

```text
mAP: 0.42
AP50: 0.61
AP75: 0.45
```

## Suggested Commands

Use `tail` for recent logs:

```bash
tail -n 120 <LOG_PATH>
```

Use `rg` for metric lines:

```bash
rg "best|latest|test|val|mdice|dice|miou|iou|acc|auc|loss|mAP|val_bpb" <LOG_PATH>
```

When the same log appends multiple runs, use launch time or the most recent training header to identify the active run.

## Decision Notes

Record both:

- best result: useful for judging peak potential
- final/latest result: useful for judging stability

If best improves but final collapses, mark the decision carefully. It may suggest a follow-up idea about stabilization, early stopping, regularization, or curriculum scheduling.
