"""L17: word counts of PIFB2.tex by part, section, and subsection.

Two counts per unit:
  raw   = whitespace-split tokens of the LaTeX source (matches `wc -w` in total)
  prose = tokens after stripping comments, display/inline math, and LaTeX commands
          (a rough estimate of the words a reader reads as text)
Also counts displayed equations, theorem-like environments, and fence/status markers.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

PATH = Path(r"C:/Users/chris and christine/Desktop/Research/manuscripts/PIFB2.tex")
lines = PATH.read_text(encoding="utf-8").splitlines()

HEAD = re.compile(r"^\s*\\(part|section|subsection|appendix)\*?(?:\{(.*?)\})?")


def prose_words(text: str) -> int:
    t = re.sub(r"(?<!\\)%.*", "", text)
    t = re.sub(r"\\begin\{(equation|align|gather|multline|eqnarray)\*?\}.*?\\end\{\1\*?\}", " ", t, flags=re.S)
    t = re.sub(r"\\\[.*?\\\]", " ", t, flags=re.S)
    t = re.sub(r"\$\$.*?\$\$", " ", t, flags=re.S)
    t = re.sub(r"\$[^$]*\$", " MATH ", t)
    t = re.sub(r"\\(label|ref|eqref|cite|citep|citet|begin|end)\{[^}]*\}", " ", t)
    t = re.sub(r"\\[A-Za-z]+\*?", " ", t)
    t = re.sub(r"[{}~\\]", " ", t)
    return len([w for w in t.split() if re.search(r"[A-Za-z]", w)])


units: list[tuple[int, str, str]] = []  # (line, level, title)
for i, ln in enumerate(lines, 1):
    m = HEAD.match(ln)
    if m and "\\ref" not in ln[: m.end()]:
        units.append((i, m.group(1), (m.group(2) or "").strip()))

# boundaries
rows = []
for k, (ln, lvl, title) in enumerate(units):
    end = units[k + 1][0] - 1 if k + 1 < len(units) else len(lines)
    body = "\n".join(lines[ln - 1 : end])
    rows.append((ln, end, lvl, title, len(body.split()), prose_words(body)))

pre = "\n".join(lines[: units[0][0] - 1])
print(f"front matter 1-{units[0][0]-1}: raw={len(pre.split())} prose={prose_words(pre)}")
tot_raw = len(pre.split())
for ln, end, lvl, title, raw, pw in rows:
    tot_raw += raw
    ind = {"part": "", "appendix": "", "section": "  ", "subsection": "      "}[lvl]
    print(f"{ind}{lvl[:3]} {ln:4d}-{end:4d} raw={raw:6d} prose={pw:6d}  {title[:80]}")
print("total raw", tot_raw, "wc-equivalent", len("\n".join(lines).split()))

# Aggregate at section level (section + its subsections)
print("\n== section-level aggregates (section incl. subsections) ==")
sec_rows = []
cur = None
for ln, end, lvl, title, raw, pw in rows:
    if lvl in ("section", "part", "appendix"):
        cur = [ln, end, lvl, title, raw, pw]
        sec_rows.append(cur)
    else:
        cur[1] = end
        cur[4] += raw
        cur[5] += pw
for ln, end, lvl, title, raw, pw in sec_rows:
    print(f"{lvl[:3]} {ln:4d}-{end:4d} raw={raw:6d} prose={pw:6d} {title[:70]}")

# Block aggregates matching the brief's map
blocks = {
    "Front+abstract (1-72)": (1, 72),
    "Intro+epistemic+related (73-135)": (73, 135),
    "Part I single-scale core (136-1005)": (136, 1005),
    "Transformer recovery + WikiText (1006-1324)": (1006, 1324),
    "Mass section (1325-1532)": (1325, 1532),
    "Coarse-graining I-IV (1533-1731)": (1533, 1731),
    "Prospective validation+discussion+conclusion I (1732-1809)": (1732, 1809),
    "Part II (1810-2159)": (1810, 2159),
    "Methods and statements (2160-2211)": (2160, 2211),
    "Appendices A-I + notation (2212-3956)": (2212, 3956),
}
print("\n== block aggregates ==")
for name, (a, b) in blocks.items():
    body = "\n".join(lines[a - 1 : b])
    print(f"{name:60s} raw={len(body.split()):6d} prose={prose_words(body):6d}")

# Counts of environments and fence vocabulary
full = "\n".join(lines)
envs = {e: len(re.findall(r"\\begin\{" + e + r"\*?\}", full)) for e in
        ["equation", "align", "theorem", "proposition", "lemma", "corollary", "definition", "postulate", "remark", "assumption", "figure", "table"]}
print("\nenvironments:", envs)
vocab = ["Level-1", "Level-2", "Level-3", "Level~1", "Level~2", "Level~3", "not a derivation", "ansatz", "postulate", "heuristic",
         "interpretive", "speculative", "conjecture", "not claimed", "does not", "rather than", "F1", "F2", "F3", "F4", "F5", "F6",
         "transformer", "attention", "WikiText", "Wheeler", "it from bit", "participatory", "Lahav", "consciousness", "neural", "LLM",
         "codebase", "repository", "GitHub", "Zenodo", "companion", "simulation", "2026", "Claude"]
for v in vocab:
    print(f"  {v!r}: {len(re.findall(re.escape(v), full, flags=re.I if v.islower() else 0))}")
