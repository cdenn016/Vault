"""Assemble the remediated PIFB2 chunks, build a scratch copy, and report integrity checks.

Usage: python assemble_and_check.py [--no-build]
Writes remediation/PIFB2.assembled.tex and remediation/check-report.md; never touches manuscripts/PIFB2.tex.
"""
import io, json, os, re, shutil, subprocess, sys

REM = os.path.dirname(os.path.abspath(__file__))
MS = os.path.abspath(os.path.join(REM, "..", "..", ".."))  # .../Research/manuscripts
SCRATCH = r"C:\Users\CHRISA~1\AppData\Local\Temp\claude\C--Users-chris-and-christine-Desktop-MultiAgentELBO\6de05277-e025-4e08-a760-fbde64e948d5\scratchpad\pifb2-remediation-build"

man = json.load(open(os.path.join(REM, "chunks", "manifest.json")))
order = sorted(man["chunks"], key=lambda k: man["chunks"][k][0])
parts = []
for cid in order:
    t = io.open(os.path.join(REM, "chunks", cid + ".tex"), encoding="utf-8", newline="").read()
    parts.append(t if t.endswith("\n") else t + "\n")
out = "".join(parts)
io.open(os.path.join(REM, "PIFB2.assembled.tex"), "w", encoding="utf-8", newline="").write(out)
text = out.replace("\r\n", "\n")
lines = text.split("\n")

rep = []
rep.append(f"# Check report\n\nAssembled from {len(order)} chunks: {len(lines)} lines, {len(re.findall(r'\\S+', text))} whitespace words.\n")

labels = re.findall(r"\\label\{([^}]*)\}", text)
dup = sorted({l for l in labels if labels.count(l) > 1})
refs = re.findall(r"\\(?:eq)?ref\{([^}]*)\}|\\cref\{([^}]*)\}|\\autoref\{([^}]*)\}", text)
refset = set()
for g in refs:
    for x in g:
        for y in x.split(","):
            if y.strip():
                refset.add(y.strip())
undef = sorted(r for r in refset if r not in set(labels))
rep.append(f"## Labels\n\n{len(labels)} labels; duplicates: {dup or 'none'}\n\nReferences to undefined labels ({len(undef)}): {undef}\n")

bib = io.open(os.path.join(MS, "references.bib"), encoding="utf-8").read()
bibkeys = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bib))
cites = set()
for m in re.finditer(r"\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}", text):
    for k in m.group(1).split(","):
        if k.strip():
            cites.add(k.strip())
missing = sorted(k for k in cites if k not in bibkeys)
rep.append(f"## Citations\n\n{len(cites)} distinct keys cited; missing from references.bib ({len(missing)}): {missing}\n")

def hits(pattern, flags=0, cap=60):
    res = []
    for i, ln in enumerate(lines, 1):
        if ln.lstrip().startswith("%"):
            continue
        for m in re.finditer(pattern, ln, flags):
            res.append(f"{i}: …{ln[max(0, m.start()-60):m.end()+60]}…")
    return res

checks = {
    "banned words": r"key insight|crucially|critically|notably|importantly|it's worth noting|it is worth noting|fundamentally|leverages|underscores",
    "spacing macros": r"\\[;,!](?![a-zA-Z])",
    "Level taxonomy": r"Level[~ -]?[123]\b|Level-3",
    "fence register": r"\bfence\b|\(F[1-6][;)]|\bF[1-6]\b",
    "realiz* near Wheeler": r"realiz\w*",
    "RG / renormalization": r"\bRG\b|renormali[sz]\w*",
    "transformer": r"[Tt]ransformer|WikiText|RoPE|ALiBi|softmax attention",
    "texttt": r"\\texttt",
    "scale superscript (s)": r"\^\{\(s\)\}|\^\{\(s\+1\)\}|\\mathcal\{R\}_s\b",
    "UK spellings": r"\b\w+(?:isation|ised|ising|our(?:s)?\b|ogue)\b",
    "horizontal rules": r"\\hrule|\\rule\{\\textwidth\}",
}
rep.append("## Pattern checks (non-comment lines)\n")
for name, pat in checks.items():
    h = hits(pat, re.I if name in ("banned words",) else 0)
    if name == "UK spellings":
        h = [x for x in h if not re.search(r"\b(?:our|four|hour|your|pour|tour|flour|sour)\b", x.split(":", 1)[1], re.I) or re.search(r"(isation|ised|ising|ogue|colour|behaviour|favour|neighbour|labour|honour|centre|modelling)", x, re.I)]
    rep.append(f"### {name}: {len(h)}\n")
    rep.extend(h[:40])
    rep.append("")

if "--no-build" not in sys.argv:
    if os.path.isdir(SCRATCH):
        shutil.rmtree(SCRATCH)
    os.makedirs(os.path.join(SCRATCH, "figures"))
    shutil.copy(os.path.join(REM, "PIFB2.assembled.tex"), os.path.join(SCRATCH, "PIFB2.tex"))
    shutil.copy(os.path.join(MS, "references.bib"), SCRATCH)
    for f in os.listdir(os.path.join(MS, "figures")):
        if f.startswith("pifb2"):
            shutil.copy(os.path.join(MS, "figures", f), os.path.join(SCRATCH, "figures"))
    for f in os.listdir(MS):
        if f.endswith(".sty"):
            shutil.copy(os.path.join(MS, f), SCRATCH)
    p = subprocess.run(["latexmk", "-pdf", "-interaction=nonstopmode", "PIFB2.tex"], cwd=SCRATCH, capture_output=True, text=True, timeout=900)
    log = io.open(os.path.join(SCRATCH, "PIFB2.log"), encoding="latin-1").read() if os.path.exists(os.path.join(SCRATCH, "PIFB2.log")) else ""
    errs = re.findall(r"^! .*", log, re.M)
    und_ref = sorted(set(re.findall(r"Reference `([^']*)' on page", log)))
    und_cit = sorted(set(re.findall(r"Citation `([^']*)' on page", log)))
    pages = re.findall(r"Output written on PIFB2\.pdf \((\d+) pages", log)
    rep.append(f"## Build\n\nlatexmk exit {p.returncode}; pages {pages[-1] if pages else 'none'}; errors {len(errs)}: {errs[:10]}\n\nundefined references {len(und_ref)}: {und_ref}\n\nundefined citations {len(und_cit)}: {und_cit}\n\noverfull boxes: {len(re.findall('Overfull', log))}; underfull: {len(re.findall('Underfull', log))}\n\nScratch build: {SCRATCH}\n")

io.open(os.path.join(REM, "check-report.md"), "w", encoding="utf-8").write("\n".join(rep) + "\n")
print("\n".join(rep[:12]))
print("... full report in check-report.md")
