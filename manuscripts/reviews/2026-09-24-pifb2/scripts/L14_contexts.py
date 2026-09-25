"""L14: print the sentence around each use of selected citation keys in PIFB2.tex."""
import re
import sys
from pathlib import Path

TEX = Path(r"C:/Users/chris and christine/Desktop/Research/manuscripts/PIFB2.tex")
lines = TEX.read_text(encoding="utf-8").splitlines()
keys = sys.argv[1:]
for i, line in enumerate(lines, 1):
    for k in keys:
        for m in re.finditer(r"\\cite[a-z]*\*?(?:\[[^\]]*\])*\{[^}]*\b" + re.escape(k) + r"\b[^}]*\}", line):
            a = max(line.rfind(". ", 0, m.start()), 0)
            b = line.find(". ", m.end())
            b = len(line) if b < 0 else b + 1
            a2 = max(line.rfind(". ", 0, max(a - 1, 0)), 0) if m.start() - a < 60 else a
            print(f"[{k}] L{i}: {line[a2:b].strip()}\n")
