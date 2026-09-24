"""L16: label/reference/citation integrity for PIFB2.tex (read-only)."""
import re
import collections

TEX = r"C:/Users/chris and christine/Desktop/Research/manuscripts/PIFB2.tex"
BIB = r"C:/Users/chris and christine/Desktop/Research/manuscripts/references.bib"
src = open(TEX, encoding="utf-8").read()
lines = src.split("\n")


def strip(l: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", l)


clean = [strip(l) for l in lines]
labels = collections.defaultdict(list)
refs = collections.defaultdict(list)
cites = collections.defaultdict(list)
envstack: list = []
labkind: dict = {}
last_sec = "?"
KINDS = ("equation", "align", "gather", "multline", "eqnarray", "theorem", "lemma",
         "proposition", "corollary", "definition", "remark", "postulate", "assumption",
         "figure", "table")
pat = re.compile(r"\\(begin|end)\{([a-zA-Z*]+)\}|\\(section|subsection|subsubsection|paragraph|part)\*?\{|\\label\{([^}]+)\}")
for n, l in enumerate(clean, 1):
    for m in pat.finditer(l):
        if m.group(1) == "begin":
            envstack.append(m.group(2))
        elif m.group(1) == "end":
            if envstack and envstack[-1] == m.group(2):
                envstack.pop()
        elif m.group(3):
            last_sec = m.group(3)
        elif m.group(4):
            lab = m.group(4)
            labels[lab].append(n)
            k = None
            for e in reversed(envstack):
                if e.rstrip("*") in KINDS:
                    k = e.rstrip("*")
                    break
            labkind[lab] = k if k else last_sec
    for m in re.finditer(r"\\(eqref|ref|autoref|cref|Cref|pageref)\{([^}]+)\}", l):
        for key in m.group(2).split(","):
            refs[key.strip()].append((n, m.group(1), l[max(0, m.start() - 30):m.start()]))
    for m in re.finditer(r"\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]+)\}", l):
        for key in m.group(1).split(","):
            cites[key.strip()].append(n)

print("labels:", len(labels), " distinct refs:", len(refs), " ref occurrences:",
      sum(len(v) for v in refs.values()), " distinct cites:", len(cites))
print("envstack at EOF:", envstack)
print("\n== multiply defined labels ==")
for k, v in labels.items():
    if len(v) > 1:
        print(k, v)
print("\n== refs to missing labels ==")
for k, v in refs.items():
    if k not in labels:
        print(k, [x[0] for x in v])
print("\n== labels never referenced ==")
unref = [k for k in labels if k not in refs]
bykind = collections.defaultdict(list)
for k in unref:
    bykind[labkind.get(k)].append((labels[k][0], k))
for kk, vv in sorted(bykind.items(), key=lambda t: str(t[0])):
    print(f"[{kk}] {len(vv)}:", ", ".join(f"{k}@{n}" for n, k in sorted(vv)))
print("total unreferenced:", len(unref), "of", len(labels))

print("\n== kind mismatches (word before ref vs label kind) ==")
EQ = {"equation", "align", "gather", "multline", "eqnarray"}
SEC = {"section", "subsection", "subsubsection", "paragraph", "part"}
word2kinds = {
    "theorem": {"theorem"}, "lemma": {"lemma"}, "proposition": {"proposition"},
    "corollary": {"corollary"}, "definition": {"definition"}, "remark": {"remark"},
    "postulate": {"postulate"}, "assumption": {"assumption"},
    "section": SEC, "sec.": SEC, "appendix": SEC, "part": SEC,
    "equation": EQ, "eq.": EQ, "eqs.": EQ, "figure": {"figure"}, "fig.": {"figure"},
    "table": {"table"},
}
plural = {"sections": "section", "theorems": "theorem", "equations": "equation",
          "appendices": "appendix", "propositions": "proposition", "lemmas": "lemma",
          "definitions": "definition", "remarks": "remark", "postulates": "postulate",
          "corollaries": "corollary", "figures": "figure", "tables": "table",
          "assumptions": "assumption"}
for k, v in refs.items():
    if k not in labels:
        continue
    kind = labkind.get(k)
    for n, cmd, pre in v:
        w = re.findall(r"([A-Za-z.]+)[~ ]*\(?$", pre.rstrip())
        if cmd == "eqref" and kind not in EQ:
            print(f"line {n}: eqref{{{k}}} to non-equation [{kind}]")
        if not w:
            continue
        word = w[-1].lower()
        word = plural.get(word, word)
        if word in word2kinds and kind not in word2kinds[word]:
            print(f"line {n}: '{w[-1]} ref{{{k}}}' but label is in [{kind}] (label line {labels[k][0]})")

print("\n== label prefix vs kind ==")
pref = {"eq": EQ, "thm": {"theorem"}, "lem": {"lemma"}, "prop": {"proposition"},
        "cor": {"corollary"}, "def": {"definition"}, "rem": {"remark"}, "sec": SEC,
        "fig": {"figure"}, "tab": {"table"}, "app": SEC, "post": {"postulate"},
        "ass": {"assumption"}}
for k in labels:
    p = k.split(":")[0]
    if p in pref and labkind.get(k) not in pref[p]:
        print(f"{k}@{labels[k][0]} is in [{labkind.get(k)}]")
print("labels without a prefix:", [k for k in labels if ":" not in k])

print("\n== citations ==")
bib = open(BIB, encoding="utf-8").read()
bibkeys = re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bib)
dup = [k for k, c in collections.Counter(bibkeys).items() if c > 1]
bibset = set(bibkeys)
missing = {k: v for k, v in cites.items() if k not in bibset}
print("distinct cited keys:", len(cites), " missing from bib:", missing)
print("duplicate bib keys in references.bib:", dup[:30])
stems = collections.defaultdict(list)
for k in cites:
    stems[re.sub(r"[^a-z]", "", k.lower())[:10]].append(k)
print("cited keys sharing a 10-letter stem:", [v for v in stems.values() if len(v) > 1])
