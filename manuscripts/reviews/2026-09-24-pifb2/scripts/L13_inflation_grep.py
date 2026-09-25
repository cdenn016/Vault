"""L13: extract status-inflation verb hits from PIFB2.tex with short context windows."""
import re, sys, collections
P = r"C:/Users/chris and christine/Desktop/Research/manuscripts/PIFB2.tex"
pat = re.compile(r"\b(prov(e|es|ed|en)|establish\w*|reveal\w*|demonstrat\w*|shows? that|deriv\w*|realiz\w*|resolv\w*|explain\w*|predict\w*|settl\w*)\b", re.I)
lines = open(P, encoding="utf-8").read().split("\n")
lo = int(sys.argv[1]) if len(sys.argv) > 1 else 1
hi = int(sys.argv[2]) if len(sys.argv) > 2 else len(lines)
filt = sys.argv[3] if len(sys.argv) > 3 else None
cnt = collections.Counter()
for n, L in enumerate(lines, 1):
    if not (lo <= n <= hi):
        continue
    for m in pat.finditer(L):
        w = m.group(0).lower()
        cnt[re.sub(r"(s|es|ed|ing|ion|ions|ly)$", "", w)[:8]] += 1
        if filt and not re.search(filt, w, re.I):
            continue
        a, b = max(0, m.start() - 110), min(len(L), m.end() + 70)
        print(f"{n}: ...{L[a:b]}...")
print("COUNTS", dict(cnt), file=sys.stderr)
