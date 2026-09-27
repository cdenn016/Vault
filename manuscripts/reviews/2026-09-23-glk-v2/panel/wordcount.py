"""Words, displays, and negation/disclaimer counts per (sub)section, from the TeX source."""
import re, collections
BS = chr(92)
base = r"C:/Users/chris and christine/Desktop/Research/manuscripts/"
docs = {'main': 'GL(K)_attention_v2.tex', 'supp': 'GL(K)_supplementary_v2.tex'}
E = re.escape

def strip(src):
    src = re.sub(r'(?<!\\)%.*', '', src)
    src = re.sub(E(BS) + r'begin\{tikzpicture\}.*?' + E(BS) + r'end\{tikzpicture\}', ' ', src, flags=re.S)
    return src

neg_re = re.compile(r"\b(not|no|neither|nor|never|none|cannot|without|unresolved|outside|unless|nor)\b|n't", re.I)
for d, f in docs.items():
    src = strip(open(base + f, encoding='utf-8').read())
    body = src.split(BS + 'begin{document}', 1)[1]
    # split on section commands
    parts = re.split('(' + E(BS) + r'(?:section|subsection|subsubsection|paragraph)\*?\{[^}]*\})', body)
    cur = 'front'
    stats = collections.OrderedDict()
    for p in parts:
        m = re.match(E(BS) + r'(section|subsection|subsubsection|paragraph)\*?\{([^}]*)\}', p)
        if m:
            cur = f"{m.group(1)}: {m.group(2)}"
            stats.setdefault(cur, [0, 0, 0, 0])
            continue
        displays = len(re.findall(E(BS) + r'begin\{(?:equation|align)\*?\}', p))
        t = re.sub(E(BS) + r'begin\{(equation|align)\*?\}.*?' + E(BS) + r'end\{\1\*?\}', ' ', p, flags=re.S)
        t = re.sub(E(BS) + r'begin\{(table|algorithm|figure)\}.*?' + E(BS) + r'end\{\1\}', ' FLOAT ', t, flags=re.S)
        t = re.sub(E(BS) + r'\(.*?' + E(BS) + r'\)', ' M ', t, flags=re.S)
        t = re.sub(r'\$[^$]*\$', ' M ', t)
        t = re.sub(E(BS) + r'(cite[tp]?|ref|eqref|label)(\[[^\]]*\])*\{[^}]*\}', ' R ', t)
        t = re.sub(E(BS) + r'[A-Za-z]+\*?', ' ', t)
        t = re.sub(r'[{}~]', ' ', t)
        words = re.findall(r"[A-Za-z][A-Za-z'\-]*|M|R", t)
        negs = len(neg_re.findall(t))
        s = stats.setdefault(cur, [0, 0, 0, 0])
        s[0] += len(words); s[1] += displays; s[2] += negs
    tot = sum(v[0] for v in stats.values())
    print(f"==== {d}: total words ~{tot}, displays {sum(v[1] for v in stats.values())}, negation tokens {sum(v[2] for v in stats.values())}")
    for k, v in stats.items():
        print(f"{v[0]:6d} words {v[1]:3d} displays {v[2]:4d} neg  ({1000*v[2]/max(v[0],1):5.1f}/kw)  {k}")
