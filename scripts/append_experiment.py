#!/usr/bin/env python3
"""Append a row to AUTORESEARCH.md's Experiment Log table."""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("md_path")
    parser.add_argument("--date", required=True)
    parser.add_argument("--experiment", required=True)
    parser.add_argument("--novelty", required=True)
    parser.add_argument("--command", required=True)
    parser.add_argument("--result", required=True)
    parser.add_argument("--decision", required=True)
    parser.add_argument("--notes", default="")
    args = parser.parse_args()

    path = Path(args.md_path).expanduser().resolve()
    row = (
        f"| {args.date} | {args.experiment} | {args.novelty} | "
        f"`{args.command}` | {args.result} | {args.decision} | {args.notes} |\n"
    )
    with path.open("a", encoding="utf-8") as f:
        f.write(row)
    print(path)


if __name__ == "__main__":
    main()
