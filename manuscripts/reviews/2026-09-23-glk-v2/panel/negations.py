"""Sentence-level count of negated / scope-disclaiming sentences in the main text and supplement."""
import re, collections
BS = chr(92)
E = re.escape
base = r"C:/Users/chris and christine/Desktop/Research/manuscripts/"
docs = {'main': 'GL(K)_attention_v2.tex', 'supp': 'GL(K)_supplementary_v2.tex'}
neg = re.compile(r"\b(not|no|neither|nor|never|cannot|none)\b", re.I)
disc_verbs = re.compile(r"\b(not|no|neither|nor|cannot)\b[^.]{0,80}\b(establish|imply|implies|identify|identifies|require|requires|select|selects|determine|determines|claim|claimed|supply|supplies|derive|derived|equal|prove|proves|extend|force|forces|recover|replace|mean|make|makes|remove|removes|exhaust|guarantee|assumed|isolate|provide|propagate)\w*", re.I)
for d, f in docs.items():
    src = open(base + f, encoding='utf-8').read()
    src = re.sub(r'(?<!\\)%.*', '', src)
    body = src.split(BS + 'begin{document}', 1)[1]
    body = re.sub(E(BS) + r'begin\{(tikzpicture|table|algorithm|figure)\}.*?' + E(BS) + r'end\{\1\}', ' ', body, flags=re.S)
    parts = re.split('(' + E(BS) + r'(?:section|subsection|subsubsection)\*?\{[^}]*\})', body)
    cur = 'front'
    tot_s = tot_n = tot_d = 0
    rows = []
    for p in parts:
        m = re.match(E(BS) + r'(section|subsection|subsubsection)\*?\{([^}]*)\}', p)
        if m:
            cur = m.group(2)
            continue
        t = re.sub(E(BS) + r'begin\{(equation|align)\*?\}.*?' + E(BS) + r'end\{\1\*?\}', ' EQ. ', p, flags=re.S)
        t = re.sub(E(BS) + r'\(.*?' + E(BS) + r'\)', ' M ', t, flags=re.S)
        t = re.sub(r'\$[^$]*\$', ' M ', t)
        t = re.sub(E(BS) + r'(cite[tp]?|ref|eqref|label)(\[[^\]]*\])*\{[^}]*\}', ' R ', t)
        t = re.sub(E(BS) + r'[A-Za-z]+\*?', ' ', t)
        t = re.sub(r'(et al|Eq|Eqs|Sec|Secs|App|Fig|i\.e|e\.g)\.', r'\1', t)
        sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', t) if len(s.split()) >= 4]
        n = sum(1 for s in sents if neg.search(s))
        dd = sum(1 for s in sents if disc_verbs.search(s))
        tot_s += len(sents); tot_n += n; tot_d += dd
        if sents:
            rows.append((cur, len(sents), n, dd))
    print(f"== {d}: sentences={tot_s}, with negation={tot_n} ({100*tot_n/tot_s:.0f}%), negated scope-disclaimers={tot_d} ({100*tot_d/tot_s:.0f}%)")
    for r in rows:
        print(f"   {r[1]:3d} sent  {r[2]:3d} neg ({100*r[2]/r[1]:3.0f}%)  {r[3]:3d} disclaim  {r[0][:70]}")
