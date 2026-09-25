"""L09: reconstruct the PIFB2 WikiText-103 aggregate means and SDs from the vector
content of figures/pifb2_scaling.pdf (the bundled CSV named in the manuscript is
absent from every available artifact), then (i) refit PPL = a K^b + c, (ii) test the
nested b = -1 restriction on aggregate means, (iii) recompute the p-value of
F(1,8) = 9.73 requested by the panel, (iv) leave-one-K-out range of b, (v) SD-weighted
fit, (vi) profile of b vs c coupling."""
import re, zlib, numpy as np
from scipy.optimize import curve_fit
from scipy import stats

PDF = r"C:/Users/chris and christine/Desktop/Research/manuscripts/figures/pifb2_scaling.pdf"
d = open(PDF, "rb").read()
t = zlib.decompress(next(re.finditer(rb"stream\r?\n(.*?)endstream", d, re.S)).group(1)).decode("latin1").replace("\x00", "")
L = t.split("\n")

# y calibration from tick marks: (pdf_y, value)
ticks = [(float(m.group(1)), None) for m in []]
ytick = {}
for i, l in enumerate(L):
    m = re.match(r"33\.672115 ([\d.]+) m$", l)
    if m and L[i + 1].startswith("30.672115"):
        ytick[float(m.group(1))] = None
yt = sorted(ytick)
vals = [80, 100, 120, 140, 160, 180, 200, 220]
A = np.polyfit(yt, vals, 1)
ymap = lambda y: np.polyval(A, y)
# x calibration
xt = [43.459735, 79.051082, 114.642428, 150.233774, 185.82512, 239.21214]
B = np.polyfit(xt, [10, 30, 50, 70, 90, 120], 1)
xmap = lambda x: np.polyval(B, x)

def markers(name):
    x = y = 0.0; out = []
    for l in L:
        m = re.match(r"1 0 0 1 ([-\d.]+) ([-\d.]+) cm /%s Do" % name, l)
        if m:
            x += float(m.group(1)); y += float(m.group(2)); out.append((x, y))
    return np.array(out)
M2 = markers("M2"); lo = markers("M0"); hi = markers("M1")
K = np.round(xmap(M2[:, 0])).astype(int)
mean = ymap(M2[:, 1]); sd = (ymap(hi[:, 1]) - ymap(lo[:, 1])) / 2
n = np.array([2 if k == 90 else 3 for k in K])
print("calibration residual y:", np.max(np.abs(ymap(np.array(yt)) - vals)))
print("K   mean     sd")
for k, m_, s_ in zip(K, mean, sd): print(f"{k:4d} {m_:8.3f} {s_:7.3f}")

f = lambda k, a, b, c: a * k**b + c
p, cov = curve_fit(f, K, mean, p0=[1800, -1, 60], maxfev=20000)
res = mean - f(K, *p); rss3 = np.sum(res**2)
r2 = 1 - rss3 / np.sum((mean - mean.mean())**2)
print("\nunweighted 3-param fit a,b,c =", p, " R2 =", r2, " RSS =", rss3)
print("manuscript: a=1805.5529 b=-1.048919 c=61.1699 R2=0.99981995")
print("asymptotic (Wald) SE from 3-param fit:", np.sqrt(np.diag(cov)))
print("corr(b,c) =", cov[1, 2] / np.sqrt(cov[1, 1] * cov[2, 2]))
print("PPL(120) point =", mean[K == 120][0])

g = lambda k, a, c: a / k + c
q, _ = curve_fit(g, K, mean, p0=[1800, 60])
rss2 = np.sum((mean - g(K, *q))**2)
F = (rss2 - rss3) / (rss3 / (len(K) - 3))
print("\nnested b=-1 fit a,c =", q, " RSS2 =", rss2)
print(f"F(1,{len(K)-3}) = {F:.3f}, p = {stats.f.sf(F, 1, len(K)-3):.4g}")
print("requested check: p(F(1,8) >= 9.73) =", stats.f.sf(9.73, 1, 8))

# SD-weighted (by SE) fit
se = sd / np.sqrt(n)
pw, covw = curve_fit(f, K, mean, p0=p, sigma=se, absolute_sigma=True, maxfev=20000)
chi2 = np.sum(((mean - f(K, *pw)) / se)**2)
print("\nSE-weighted fit a,b,c =", pw, " SE(b) =", np.sqrt(covw[1, 1]), " chi2/dof =", chi2 / 8)

# leave-one-K-out
bs = []
for j in range(len(K)):
    msk = np.arange(len(K)) != j
    pj, _ = curve_fit(f, K[msk], mean[msk], p0=p, maxfev=20000); bs.append((K[j], pj[1], pj[2]))
print("\nleave-one-K-out (K dropped, b, c):")
for r in bs: print(f"  {r[0]:4d} {r[1]:8.4f} {r[2]:8.3f}")
print("LOKO b range:", min(r[1] for r in bs), max(r[1] for r in bs))

# fit on K<=80 only (common optimization regime claimed at line 126)
m80 = K <= 80
p80, c80 = curve_fit(f, K[m80], mean[m80], p0=p, maxfev=20000)
print("\nK<=80 only fit a,b,c =", p80, " SE:", np.sqrt(np.diag(c80)))

# parametric bootstrap over seeds using stored SDs (seed-level resampling proxy)
rng = np.random.default_rng(0); bb = []
for _ in range(2000):
    y = mean + rng.standard_normal(len(K)) * se
    try:
        pb, _ = curve_fit(f, K, y, p0=p, maxfev=5000); bb.append(pb[1])
    except RuntimeError: pass
bb = np.array(bb)
print("\nparametric seed bootstrap b: 2.5/50/97.5% =", np.percentile(bb, [2.5, 50, 97.5]), " n =", len(bb))

print("\nresiduals (mean - fit) and residual/SE:")
for k, r, s in zip(K, res, se): print(f"  {k:4d} {r:7.3f} {r/s:7.2f}")
print("residual SD sqrt(RSS/8) =", np.sqrt(rss3 / 8))
# token arithmetic claimed at PIFB2.tex:126
for steps, tps in [(30000, 4096), (60000, 2048), (22500, 122880000 / 22500)]:
    print(f"steps {steps} x tokens/step {tps:.2f} = {steps*tps:,.0f}")
