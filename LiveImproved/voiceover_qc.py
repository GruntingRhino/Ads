#!/usr/bin/env python3
"""Heuristic voiceover QA for LiveImproved ad scripts.

Checks for:
- pronunciation risks (POV, LiveImproved, acronyms)
- pacing issues (too-long sentences)
- emotional cadence (pauses, short fragments, variation)
- generic marketing language

Usage:
  python voiceover_qc.py
  python voiceover_qc.py /path/to/voiceover.txt
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
from pathlib import Path

PRONUNCIATION_REPLACEMENTS = {
    "POV": "P. O. V.",
    "LiveImproved": "Live Improved",
    "AI": "A. I.",
}


def score_text(text: str):
    issues = []
    t = text.strip()

    # pronunciation risks
    if re.search(r"\bPOV\b", t):
        issues.append(("pronunciation", "Spell POV as P. O. V. when spoken."))
    if re.search(r"\bLiveImproved\b", t):
        issues.append(("pronunciation", "Speak LiveImproved as Live Improved."))
    if re.search(r"\bAI\b", t):
        issues.append(("pronunciation", "Spell AI as A. I. when you want emphasis."))

    # pacing / cadence
    sentences = [s.strip() for s in re.split(r"[.!?]+\s*", t) if s.strip()]
    avg_words = sum(len(s.split()) for s in sentences) / max(1, len(sentences))
    if avg_words > 18:
        issues.append(("pacing", f"Average sentence length is high ({avg_words:.1f} words)."))
    if t.count("...") < 1 and t.count("—") < 1:
        issues.append(("emotion", "Add pauses (ellipsis or em dash) to create better cadence."))
    short_sentences = [s for s in sentences if len(s.split()) <= 4]
    if len(short_sentences) < 2:
        issues.append(("variation", "Add a few short punchy fragments for pitch/tempo variation."))

    # genericness / marketing fluff
    generic_phrases = [
        r"change your life",
        r"unlock your potential",
        r"best version of you",
        r"take control",
        r"game changer",
    ]
    for pat in generic_phrases:
        if re.search(pat, t, re.I):
            issues.append(("generic", f"Avoid generic phrase matched by /{pat}/."))

    score = 100
    weights = {"pronunciation": 20, "pacing": 10, "emotion": 8, "variation": 6, "generic": 8}
    for kind, _ in issues:
        score -= weights.get(kind, 5)
    return max(score, 0), issues, len(sentences), round(avg_words, 1)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", help="voiceover text files or folders")
    args = parser.parse_args()

    files = []
    if args.paths:
        for p in args.paths:
            path = Path(p)
            if path.is_dir():
                files.extend(sorted(path.glob("*/voiceover.txt")))
            else:
                files.append(path)
    else:
        files = [Path(p) for p in sorted(glob.glob("*/voiceover.txt"))]

    rows = []
    for path in files:
        if not path.exists():
            continue
        text = read_text(path)
        score, issues, nsent, avg = score_text(text)
        rows.append({
            "path": str(path),
            "score": score,
            "sentences": nsent,
            "avg_sentence_words": avg,
            "issues": issues,
            "text": text,
        })

    print(json.dumps(rows, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
