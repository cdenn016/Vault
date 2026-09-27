import re, collections, json
BS = chr(92)
base = r"C:/Users/chris and christine/Desktop/Research/manuscripts/"
docs = {'main': 'GL(K)_attention_v2.tex', 'supp': 'GL(K)_supplementary_v2.tex'}
lab = collections.defaultdict(list)
refs = collections.defaultdict(list)
cites = collections.defaultdict(list)
text = {}
re_label = re.compile(re.escape(BS) + r'label\{([^}]*)\}')
re_ref = re.compile(re.escape(BS) + r'(eqref|ref|autoref|cref|Cref|pageref)\{([^}]*)\}')
re_cite = re.compile(re.escape(BS) + r'(cite[tp]?\*?|citealp|citeauthor|citeyear|nocite)(\[[^\]]*\])?(\[[^\]]*\])?\{([^}]*)\}')
for d, f in docs.items():
    L = open(base + f, encoding='utf-8').read().split('\n')
    text[d] = L
    for n, line in enumerate(L, 1):
        if line.strip().startswith('%'):
            continue
        for m in re_label.finditer(line):
            lab[m.group(1)].append((d, n))
        for m in re_ref.finditer(line):
            for k in m.group(2).split(','):
                refs[k.strip()].append((d, n, m.group(1)))
        for m in re_cite.finditer(line):
            for k in m.group(4).split(','):
                cites[k.strip()].append((d, n, m.group(1), (m.group(2) or '') + (m.group(3) or '')))
print("=== LABELS (defined) ===")
for k, v in sorted(lab.items(), key=lambda kv: (kv[1][0][0], kv[1][0][1])):
    r = refs.get(k, [])
    print(f"{k:45s} def={v[0][0]}:{v[0][1]} nrefs={len(r)} at={[(x[0], x[1], x[2]) for x in r]}")
print("\n=== MULTIPLY-DEFINED LABELS ===")
for k, v in lab.items():
    if len(v) > 1:
        print(k, v)
print("\n=== REFS TO UNDEFINED LABELS ===")
for k, v in refs.items():
    if k not in lab:
        print(k, v)
print("\n=== CROSS-DOC REFS ===")
for k, v in refs.items():
    if k in lab:
        dd = lab[k][0][0]
        for x in v:
            if x[0] != dd:
                print(f"{x[0]}:{x[1]} ({x[2]}) refs {k} defined in {dd}:{lab[k][0][1]}")
print("\n=== UNUSED LABELS ===")
for k, v in lab.items():
    if k not in refs:
        print(k, v)
print("\n=== ADJACENT DOUBLE LABELS (same object) ===")
for d in docs:
    L = text[d]
    for n, line in enumerate(L, 1):
        if line.count(BS + 'label') > 1:
            print(d, n, line.strip()[:120])
        if (BS + 'label') in line and n < len(L) and (BS + 'label') in L[n]:
            print(d, n, '&', n + 1, line.strip()[:70], '|', L[n].strip()[:70])
print("\n=== CITES ===")
for d in docs:
    ks = sorted(set(k for k, v in cites.items() for x in v if x[0] == d))
    print(d, len(ks), ks)
for k, v in sorted(cites.items()):
    print(k, v)
json.dump({k: v for k, v in cites.items()}, open('cites.json', 'w'), indent=1)
