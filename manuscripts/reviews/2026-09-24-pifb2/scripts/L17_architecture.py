"""L17: architectural diagnostics for PIFB2.tex.

1. Abstract word count and Wheeler/it-from-bit mentions in abstract, intro, conclusions.
2. Distribution of thesis vocabulary (Wheeler, it from bit, participatory) versus ML vocabulary
   (transformer, attention, WikiText, token, softmax) over the brief's block map.
3. Fence and repeated-disclaimer phrases: counts and line numbers.
4. Implementation/provenance vocabulary by block (reference implementation, checked-in, texttt,
   repository, CUDA, seed, configuration).
5. Hedge density: 'rather than', 'not a derivation', 'is not', 'does not' per 1000 words by block.
"""
from __future__ import annotations

import re
from pathlib import Path

PATH = Path(r"C:/Users/chris and christine/Desktop/Research/manuscripts/PIFB2.tex")
L = PATH.read_text(encoding="utf-8").splitlines()


def span(a: int, b: int) -> str:
    return "\n".join(L[a - 1 : b])


def cnt(pat: str, text: str, flags: int = re.I) -> int:
    return len(re.findall(pat, text, flags))


abstract = span(59, 63)
print("abstract raw words:", len(abstract.split()))
for p in ["Wheeler", r"it from bit", "participat", "transformer|attention", "WikiText", "implementation"]:
    print(f"  abstract {p!r}: {cnt(p, abstract)}")
print("keywords line:", L[65][:200])

blocks = [
    ("Abstract 58-72", 58, 72), ("Intro 73-93", 73, 93), ("Epistemic+scope 94-127", 94, 127),
    ("Related 128-135", 128, 135), ("One rung 136-515", 136, 515), ("Free energy 516-734", 516, 734),
    ("Precision/env 735-928", 735, 928), ("Timescales 929-1005", 929, 1005),
    ("Transformer 1006-1303", 1006, 1303), ("WikiText 1304-1324", 1304, 1324), ("Mass 1325-1532", 1325, 1532),
    ("CG I 1533-1661", 1533, 1661), ("CG II-IV 1662-1731", 1662, 1731), ("Prosp.val 1732-1750", 1732, 1750),
    ("Discussion 1751-1801", 1751, 1801), ("Concl I 1802-1807", 1802, 1807), ("Part II 1808-2151", 1808, 2151),
    ("Concl 2152-2159", 2152, 2159), ("Methods+stmts 2160-2211", 2160, 2211), ("App A 2212-2515", 2212, 2515),
    ("App B rock 2516-2591", 2516, 2591), ("App C-E 2592-2955", 2592, 2955), ("App F 2956-3161", 2956, 3161),
    ("App G 3162-3412", 3162, 3412), ("App H 3413-3568", 3413, 3568), ("App I 3569-3941", 3569, 3941),
]
thesis = r"Wheeler|it from bit|participat"
ml = r"transformer|attention|WikiText|token|softmax|language model|perplexity|RoPE|ALiBi"
impl = r"reference implementation|checked-in|\\texttt|repository|CUDA|codebase|autograd|config"
hedge = r"rather than|not a derivation|is not |does not |are not |not claimed|remains open|is open"
print("\nblock                     words  thesis  ml   impl  hedge  hedge/1kw")
tot_thesis = 0
for name, a, b in blocks:
    t = span(a, b)
    w = len(t.split())
    th, m, im, h = cnt(thesis, t), cnt(ml, t), cnt(impl, t), cnt(hedge, t)
    tot_thesis += th
    print(f"{name:25s} {w:6d} {th:6d} {m:5d} {im:5d} {h:6d} {1000*h/max(w,1):8.1f}")
full = "\n".join(L)
print("total thesis-term hits", cnt(thesis, full), " ml-term hits", cnt(ml, full), " impl hits", cnt(impl, full))

print("\nWheeler line numbers:", [i for i, l in enumerate(L, 1) if "Wheeler" in l])
print("'it from bit' line numbers:", [i for i, l in enumerate(L, 1) if re.search("it from bit", l, re.I)])

phrases = {
    "fence F": r"fence~?F\d",
    "recovery in a limit": r"recovery in a limit",
    "not a derivation": r"not a derivation",
    "Level-3": r"Level[-~]3",
    "regulator (F3 theme)": r"regulator",
    "kinetic-metric postulate (F4 theme)": r"kinetic-metric postulate",
    "prospective (F2 theme)": r"prospective",
    "unavailable (F2/F6 theme)": r"unavailable",
    "separately introduced (bilinear M)": r"separately introduced",
    "abelian-exact": r"abelian-exact",
    "Regime~II": r"Regime[~ ]II",
    "Section~\\ref{sec:epistemic_status}": r"Section~\\ref\{sec:epistemic_status\}",
    "tiered falsifiability": r"tiered falsifiab",
}
print("\nrepeated-disclaimer phrases:")
for k, p in phrases.items():
    lines = [i for i, l in enumerate(L, 1) if re.search(p, l)]
    print(f"  {k:40s} hits={cnt(p, full, 0):4d} lines={len(lines):3d} first={lines[:12]}")

# Sentences restating the attention-recovery fence (M, limit, not derivation) outside the home section
fence1 = [i for i, l in enumerate(L, 1) if re.search(r"recover", l) and re.search(r"limit", l) and re.search(r"derivation|derived", l)]
print("\nlines restating F1 (recover+limit+derivation):", fence1, "count", len(fence1))

# Long lines (paragraph-per-line) count and top by words
wl = sorted(((len(l.split()), i) for i, l in enumerate(L, 1)), reverse=True)[:12]
print("\nlongest source lines (words, line):", wl)
print("lines > 400 words:", sum(1 for l in L if len(l.split()) > 400))
