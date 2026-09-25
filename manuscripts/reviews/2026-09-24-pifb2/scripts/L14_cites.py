"""L14: extract every citation key from PIFB2.tex, resolve against references.bib,
report missing and duplicate keys, and dump a key table (with bib metadata and
PIFB2 line numbers) to L14_cites.json.  Also checks which candidate prior-art
works are present in the bib (by title/author substring)."""
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(r"C:/Users/chris and christine/Desktop/Research/manuscripts")
TEX = ROOT / "PIFB2.tex"
BIB = ROOT / "references.bib"
OUT = ROOT / "reviews/2026-09-24-pifb2/scripts/L14_cites.json"

tex_lines = TEX.read_text(encoding="utf-8").splitlines()
cite_re = re.compile(r"\\(?:cite|citep|citet|citealp|citeauthor|citeyear|parencite|textcite)\*?(?:\[[^\]]*\]){0,2}\{([^}]*)\}")
uses: dict[str, list[int]] = defaultdict(list)
for i, line in enumerate(tex_lines, 1):
    s = line.split("%")[0] if not line.lstrip().startswith("%") else ""
    # keep escaped \% ; crude comment strip
    s = re.sub(r"(?<!\\)%.*", "", line)
    for m in cite_re.finditer(s):
        for k in m.group(1).split(","):
            k = k.strip()
            if k:
                uses[k].append(i)

bib_text = BIB.read_text(encoding="utf-8")
entry_re = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", re.M)
starts = [(m.start(), m.group(1).lower(), m.group(2)) for m in entry_re.finditer(bib_text)]
entries: dict[str, list[dict]] = defaultdict(list)
for idx, (pos, typ, key) in enumerate(starts):
    end = starts[idx + 1][0] if idx + 1 < len(starts) else len(bib_text)
    body = bib_text[pos:end]
    fields = {}
    for f in ("author", "title", "year", "journal", "booktitle", "volume", "pages", "doi", "publisher", "eprint", "number"):
        mm = re.search(r"\b" + f + r"\s*=\s*[{\"](.*?)[}\"]\s*,?\s*\n", body, re.S | re.I)
        if mm:
            fields[f] = re.sub(r"\s+", " ", mm.group(1)).strip()
    entries[key].append({"type": typ, **fields, "bibline": bib_text[:pos].count("\n") + 1})
if typ == "string":
    pass

cited = sorted(uses)
missing = [k for k in cited if k not in entries]
dup_bib = {k: [e["bibline"] for e in v] for k, v in entries.items() if len(v) > 1 and k.lower() not in ("string", "comment", "preamble")}
dup_cited = {k: v for k, v in dup_bib.items() if k in uses}
# case-insensitive collisions
lower = defaultdict(list)
for k in entries:
    lower[k.lower()].append(k)
case_coll = {k: v for k, v in lower.items() if len(v) > 1}

table = []
for k in cited:
    e = entries.get(k, [{}])[0]
    table.append({"key": k, "pifb2_lines": uses[k], "resolved": k in entries, **{f: e.get(f) for f in ("type", "author", "title", "year", "journal", "booktitle", "volume", "pages", "doi", "bibline")}})

candidates = {
    "Wilson 1974 confinement": r"Confinement of quarks",
    "Beny-Osborne 2015 info-geometric RG": r"(information[- ]geometric approach to the renormali|Renormali[sz]ation group flow as optimal|Information geometric approach to the renormalisation)",
    "Machta et al 2013 parameter space compression": r"Parameter space compression",
    "Mehta-Schwab 2014 exact mapping VRG-DL": r"exact mapping between the variational renormali",
    "Berman et al 2023 Bayesian renormalization": r"Bayesian renormali",
    "Cohen et al 2019 gauge-equivariant CNN": r"Gauge equivariant convolutional",
    "Fields-Friston-Glazebrook-Levin 2022 FEP quantum": r"free energy principle for generic quantum",
    "Ramstead et al 2023 Bayesian mechanics": r"(On Bayesian mechanics|Bayesian mechanics)",
    "Yedidia-Freeman-Weiss 2005 region free energies": r"Constructing free[- ]energy approximations",
    "Wheeler 1990 it from bit": r"Information, physics, quantum",
    "Wilson 1971 RG I/II": r"Renormalization group and critical phenomena",
    "Wilson-Kogut 1975": r"renormalization group and the .?epsilon",
    "Koch-Janusz Ringel 2018 mutual information RG": r"Mutual information, neural networks and the renormali",
    "Kobayashi-Nomizu": r"Foundations of Differential Geometry",
    "Fuchs QBism participatory": r"(participatory realism|QBism)",
    "Rovelli relational QM": r"Relational quantum mechanics",
    "Caticha entropic dynamics": r"(Entropic dynamics|entropic inference)",
    "Frieden EPI": r"(Physics from Fisher|Fisher information)",
    "Brody-Hughston": r"(geometric quantum mechanics|Geometrization of statistical)",
    "Kikuchi 1951 CVM": r"cluster variation",
    "Bronstein et al 2021 GDL": r"Geometric deep learning",
}
found = {}
for label, pat in candidates.items():
    hits = []
    for k, v in entries.items():
        t = (v[0].get("title") or "")
        if re.search(pat, t, re.I):
            hits.append({"key": k, "title": t, "year": v[0].get("year"), "cited_in_pifb2": k in uses})
    found[label] = hits

res = {"n_cite_commands_keys": len(cited), "n_uses": sum(len(v) for v in uses.values()),
       "missing": missing, "duplicate_bib_keys_all": dup_bib, "duplicate_bib_keys_cited": dup_cited,
       "case_collisions": case_coll, "table": table, "prior_art_candidates": found}
OUT.write_text(json.dumps(res, indent=1), encoding="utf-8")
print("distinct cited keys:", len(cited), " total uses:", res["n_uses"])
print("missing:", missing)
print("duplicate bib keys (all):", dup_bib)
print("duplicate bib keys cited:", dup_cited)
print("case collisions:", case_coll)
for t in table:
    print(f'{t["key"]:40s} L{t["pifb2_lines"][:6]} | {t.get("year")} | {(t.get("author") or "")[:50]} | {(t.get("title") or "")[:70]} | {t.get("journal") or t.get("booktitle") or ""} {t.get("volume") or ""} {t.get("pages") or ""} doi={t.get("doi")}')
print("\nPRIOR ART CANDIDATES")
for k, v in found.items():
    print(k, "->", v)
