import csv, math, sys
rows = list(csv.DictReader(open(sys.argv[1], newline="")))
last = rows[-1]
for k, v in last.items():
    if k.startswith("val_") or k.startswith("phi_chart") or k in ("relational_score_klmax_frac",):
        print(k, "=", v)
def f(r, k):
    try: return float(r[k])
    except Exception: return float("nan")
spe = 57050
print("--- train_ce around epoch boundaries (mean of logged minibatches within +-12000 steps)")
for e in (1, 2, 3, 4):
    b = e * spe
    pre = [f(r, "train_ce") for r in rows if b - 12000 <= f(r, "step") < b]
    post = [f(r, "train_ce") for r in rows if b <= f(r, "step") < b + 12000]
    sd = lambda xs: (sum((x - sum(xs)/len(xs))**2 for x in xs) / (len(xs) - 1)) ** 0.5
    print("epoch %d boundary %d: pre mean %.3f (n=%d, sd %.3f) post mean %.3f (n=%d, sd %.3f)" % (e, b, sum(pre)/len(pre), len(pre), sd(pre), sum(post)/len(post), len(post), sd(post)))
