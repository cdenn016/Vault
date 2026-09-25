"""L16: house-style mechanics for PIFB2.tex (read-only counts with line numbers)."""
import re
import collections

TEX = r"C:/Users/chris and christine/Desktop/Research/manuscripts/PIFB2.tex"
lines = open(TEX, encoding="utf-8").read().split("\n")


def strip(l: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", l)


clean = [strip(l) for l in lines]
BANNED = ["key insight", "crucially", "critically", "notably", "importantly",
          "it's worth noting", "it is worth noting", "fundamentally", "leverages",
          "leverage", "leveraging", "underscores", "underscore"]
print("== banned words (case-insensitive, whole word) ==")
for w in BANNED:
    hits = [n for n, l in enumerate(clean, 1) if re.search(r"\b" + re.escape(w) + r"\b", l, re.I)]
    cnt = sum(len(re.findall(r"\b" + re.escape(w) + r"\b", l, re.I)) for l in clean)
    if cnt:
        print(f"{w!r}: {cnt} at lines {hits}")

print("\n== horizontal rules ==")
for n, l in enumerate(clean, 1):
    s = l.strip()
    if re.fullmatch(r"-{3,}", s) or re.search(r"\\(hrule|rule\{\\(line|text)width\}|noindent\\rule)", l):
        print(n, s[:80])
dash3 = [n for n, l in enumerate(clean, 1) if re.search(r"(?<!-)---(?!-)", l)]
print("em-dash '---' occurrences in text lines:", len(dash3), dash3[:40])
dash2 = sum(len(re.findall(r"(?<![-!])--(?!-)", l)) for l in clean)
print("en-dash '--' occurrences:", dash2)

print("\n== LaTeX spacing macros ==")
for mac, rx in [(r"\;", r"\\;"), (r"\,", r"\\,"), (r"\!", r"\\!"), (r"\:", r"\\:"),
                (r"\quad", r"\\quad\b"), (r"\qquad", r"\\qquad\b")]:
    hits = [n for n, l in enumerate(clean, 1) if re.search(rx, l)]
    cnt = sum(len(re.findall(rx, l)) for l in clean)
    print(f"{mac}: {cnt} occurrences on {len(hits)} lines; first lines {hits[:25]}")

print("\n== UK spellings ==")
UK = {
    r"\b\w*isation\w*\b": "-isation", r"\b(?!(?:rise|wise|precise|concise|exercise|advertise|comprise|compromise|surprise|expertise|enterprise|franchise|revise|supervise|televise|improvise|premise|chastise|excise|despise|devise|disguise|incise|merchandise|promise|raise|praise|noise|poise|cruise|bruise|guise|otherwise|likewise|clockwise|pairwise|stepwise|elementwise|coordinatewise|entrywise|pointwise|blockwise|rowwise|columnwise|componentwise|edgewise|agentwise|piecewise|channelwise|clusterwise|nodewise|scalewise|sitewise|termwise|layerwise|headwise|tokenwise|samplewise|batchwise|dimensionwise|groupwise|linewise|leafwise|arise|arises|arising|arisen|rises|rising|raises|raised|raising|promises|promised|premises|revised|revises|revising|exercises|exercised|comprises|comprised|comprising|surprising|surprised|surprisingly|devised|advertised|disguised|noisy|noiseless))\w*[^aeiou\W]ise[sd]?\b": "-ise",
    r"\b\w*ising\b": "-ising",
    r"\b(colour|behaviour|favour|honour|labour|neighbour|flavour|harbour|rumour|vapour|vigour|humour)\w*\b": "-our",
    r"\b(centre|fibre|metre|litre|theatre|calibre|spectre|sombre)s?\b": "-re",
    r"\bmodell(ing|ed|er)\b": "modelling", r"\blabell(ing|ed)\b": "labelling",
    r"\btravell(ing|ed)\b": "travelling", r"\bsignall(ing|ed)\b": "signalling",
    r"\b(analyse|analysed|analysing|catalyse|paralyse)\b": "-yse",
    r"\b(defence|licence|offence)\b": "-ence", r"\bwhilst\b": "whilst", r"\bamongst\b": "amongst",
    r"\bgrey\b": "grey", r"\bprogramme\b": "programme", r"\bartefact\w*\b": "artefact",
    r"\bcounsell\w*\b": "counsel", r"\bfulfil\b": "fulfil", r"\benrol\b": "enrol",
    r"\bsceptic\w*\b": "sceptic", r"\baluminium\b": "aluminium",
}
tot = 0
for rx, name in UK.items():
    found = collections.defaultdict(list)
    for n, l in enumerate(clean, 1):
        for m in re.finditer(rx, l, re.I):
            found[m.group(0).lower()].append(n)
    for word, ns in found.items():
        tot += len(ns)
        print(f"{name}: {word!r} x{len(ns)} lines {ns[:12]}")
print("UK spelling hits total:", tot)

print("\n== notational variants (counts; first lines) ==")
VAR = {
    "KL macro": r"\\KL(?![A-Za-z])", "mathrm KL": r"(?<!D_\{)\\mathrm\{KL\}", "D_{mathrm KL}": r"D_\{\\mathrm\{KL\}\}",
    "operatorname KL": r"\\operatorname\{KL\}", "text KL": r"\\text\{KL\}",
    "mathrm tr": r"\\mathrm\{tr\}", "operatorname tr": r"\\operatorname\{tr\}", "Tr": r"\\(mathrm|operatorname)\{Tr\}",
    "^top": r"\^\{?\\top\}?", "^T": r"\^\{?T\}?(?![A-Za-z])", "^{-T}": r"\^\{-T\}", "^{-top}": r"\^\{-\\top\}",
    "mathrm softmax": r"\\mathrm\{softmax\}", "softmax macro": r"\\softmax(?![A-Za-z])",
    "operatorname softmax": r"\\operatorname\{softmax\}", "text softmax": r"\\text\{softmax\}",
    "mathrm d (differential)": r"\\mathrm\{d\}", "E_nu / mathbb E": r"\\mathbb\{E\}",
    "GL(K_q) plain": r"\\mathrm\{GL\}\(K_q\)", "GL(K_q,R)": r"\\mathrm\{GL\}\(K_q, ?\\mathbb\{R\}\)",
    "GL^+": r"\\mathrm\{GL\}\^\+",
}
for name, rx in VAR.items():
    hits = [n for n, l in enumerate(clean, 1) if re.search(rx, l)]
    cnt = sum(len(re.findall(rx, l)) for l in clean)
    print(f"{name}: {cnt} on {len(hits)} lines; first {hits[:10]}")

print("\n== figure / table / abstract counts ==")
body = "\n".join(clean)
print("figure envs:", len(re.findall(r"\\begin\{figure\*?\}", body)),
      " tikzpicture:", len(re.findall(r"\\begin\{tikzpicture\}", body)),
      " includegraphics:", len(re.findall(r"\\includegraphics", body)),
      " table envs:", len(re.findall(r"\\begin\{table\*?\}", body)),
      " tabular(x):", len(re.findall(r"\\begin\{tabularx?\}", body)))
ab = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", body, re.S).group(1)
txt = re.sub(r"\\(cite|ref|eqref)\{[^}]*\}", "X", ab)
txt = re.sub(r"\$[^$]*\$", "X", txt)
txt = re.sub(r"\\[A-Za-z]+", " ", txt)
print("abstract words (math spans counted as one word):", len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-.]*", txt)),
      " characters:", len(ab))
print("numbered theorem-like envs:", {e: len(re.findall(r"\\begin\{" + e + r"\}", body)) for e in
      ["theorem", "lemma", "proposition", "corollary", "definition", "remark", "postulate", "assumption"]})
print("sections:", len(re.findall(r"\\section\{", body)), " subsections:", len(re.findall(r"\\subsection\{", body)))
print("itemize/enumerate/description:", len(re.findall(r"\\begin\{(itemize|enumerate|description)\}", body)))
print("texttt occurrences (code paths):", len(re.findall(r"\\texttt\{", body)))
