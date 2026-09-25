"""L16: print context windows around a regex on given PIFB2.tex lines.

Usage: python L16_ctx.py <regex> <line> [<line> ...]   (regex is a Python regex; width 70)
"""
import re
import sys

TEX = r"C:/Users/chris and christine/Desktop/Research/manuscripts/PIFB2.tex"
lines = open(TEX, encoding="utf-8").read().split("\n")
rx = re.compile(sys.argv[1].replace("@", "\\\\"))  # '@' stands for a literal backslash
W = 70
for a in sys.argv[2:]:
    if "-" in a:
        lo, hi = map(int, a.split("-"))
    else:
        lo = hi = int(a)
    for n in range(lo, hi + 1):
        l = lines[n - 1]
        for m in list(rx.finditer(l))[:4]:
            print(f"{n}: ...{l[max(0, m.start() - W):m.end() + W]}...")
