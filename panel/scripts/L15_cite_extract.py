"""L15: extract citation keys from PIFB2.tex, check they resolve in references.bib,
check for duplicate bib keys, and print bib entries plus citing lines for requested keys."""
import re, sys, collections
T = r"C:/Users/chris and christine/Desktop/Research/manuscripts/PIFB2.tex"
B = r"C:/Users/chris and christine/Desktop/Research/manuscripts/references.bib"
tex = open(T, encoding="utf-8").read().splitlines()
bib = open(B, encoding="utf-8").read()
cite_re = re.compile(r"[\\]cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{([^}]*)\}")
uses = collections.defaultdict(list)
for i, line in enumerate(tex, 1):
    for m in cite_re.finditer(line):
        for k in m.group(1).split(","):
            uses[k.strip()].append(i)
# bib entries
ent_re = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", re.M)
keys = [m.group(2) for m in ent_re.finditer(bib)]
cnt = collections.Counter(keys)
dups = [k for k, c in cnt.items() if c > 1]
lower = collections.Counter(k.lower() for k in keys)
print("cited keys:", len(uses), "bib entries:", len(keys))
print("missing from bib:", sorted(k for k in uses if k not in cnt))
print("duplicate bib keys:", dups)
print("case-collision bib keys:", [k for k, c in lower.items() if c > 1])
def entry(k):
    m = re.search(r"@\w+\s*\{\s*" + re.escape(k) + r"\s*,", bib)
    if not m: return None
    s = m.start(); depth = 0
    for j in range(bib.index("{", s), len(bib)):
        if bib[j] == "{": depth += 1
        elif bib[j] == "}":
            depth -= 1
            if depth == 0: return bib[s:j+1]
if len(sys.argv) > 1:
    for k in sys.argv[1:]:
        print("=" * 10, k, "lines", uses.get(k))
        print(entry(k))
