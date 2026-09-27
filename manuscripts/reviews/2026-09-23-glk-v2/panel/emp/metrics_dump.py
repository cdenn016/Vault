import csv, sys, math
path = sys.argv[1]
cols = sys.argv[2].split(",")
every = int(sys.argv[3]) if len(sys.argv) > 3 else 1
with open(path, newline="") as f:
    r = list(csv.DictReader(f))
print("rows", len(r))
print("\t".join(cols))
for k, row in enumerate(r):
    if k % every and k != len(r) - 1:
        continue
    out = []
    for c in cols:
        v = row.get(c, "NA")
        try:
            fv = float(v)
            out.append(f"{fv:.6g}")
        except Exception:
            out.append(str(v))
    print("\t".join(out))
