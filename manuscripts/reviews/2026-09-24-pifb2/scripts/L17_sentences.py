"""L17: sentence-length statistics of PIFB2 prose (math stripped), by block.

Reports median and 90th-percentile sentence length in words and the share of sentences over 50 words.
Math is replaced by a single token so formulas do not inflate counts.
"""
from __future__ import annotations

import re
import statistics
from pathlib import Path

L = Path(r"C:/Users/chris and christine/Desktop/Research/manuscripts/PIFB2.tex").read_text(encoding="utf-8").splitlines()


def clean(t: str) -> str:
    t = re.sub(r"(?<!\\)%.*", "", t)
    t = re.sub(r"\\begin\{(equation|align|gather)\*?\}.*?\\end\{\1\*?\}", " EQ. ", t, flags=re.S)
    t = re.sub(r"\$[^$]*\$", " X ", t)
    t = re.sub(r"~?\\(eqref|ref|cite|label)\{[^}]*\}", " R ", t)
    t = re.sub(r"\\(emph|textbf|textit)\{([^}]*)\}", r"\2", t)
    t = re.sub(r"\\[A-Za-z]+\*?(\[[^\]]*\])?(\{[^}]*\})?", " ", t)
    t = re.sub(r"\b(e\.g|i\.e|cf|Eq|Eqs|Sec|Fig|al)\.", r"\1", t)
    return t


blocks = [("Abstract", 59, 63), ("Intro", 73, 93), ("Epistemic", 94, 127), ("Part I body", 136, 1807),
          ("Part II", 1810, 2159), ("Appendices", 2212, 3941)]
for name, a, b in blocks:
    t = clean("\n".join(L[a - 1 : b]))
    sents = [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z])", t) if len(s.split()) >= 3]
    lens = sorted(len(s.split()) for s in sents)
    p90 = lens[int(0.9 * (len(lens) - 1))]
    over50 = sum(1 for x in lens if x > 50) / len(lens)
    print(f"{name:12s} n={len(lens):5d} median={statistics.median(lens):5.1f} p90={p90:4d} max={lens[-1]:4d} share>50w={over50:.2f}")
