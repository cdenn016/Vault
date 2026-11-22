r"""Check 1: deciding quantities of the pure audience (instance P0, declared in aud.py: F=0.9, Q=0.05, R=1, RS=0.01,
Rc=0.002, qc=1e-4, n=4, kmsg=1, gamma=40, psi=0).

Computed: exact full-model Sigma^c and Pi^c (EFE attention is 'read the source' with probability 1 - O(1e-14) at the
stationary decision state; the deterministic pattern is used and the deviation probability reported); all region
contrasts; whether the source joins the selected block; the clause (c) mean-coupling baseline; the type-D nulls
N_hab (gamma = 0) and N_pr (partners redrawn uniformly every round) by exact pair algebra over Monte Carlo policy
paths (second-moment convention); N_lp / N_rn / N_fr by the dead-channel check (proved diagonal).

Declared expectations before running:
  full model: diffusive; r(A) = 5.3849; best other region r(A u {S}) = 2.326; baseline 3.817;
  N_hab: r(A) between 1.2 and 2.0, every region below 3.0; N_pr: r(A) between 1.2 and 2.2, every region below 3.0;
  dead channels (N_lp): off-diagonal Sigma^c entries within 3 SE of 0, r <= 1 up to noise.
NEGATIVE CONTROL: the null pipeline applied to the full model's own paths ('full' mode through the Monte Carlo
pair algebra) must reproduce r(A) = 5.385 within 3 SE (so the pipeline can return a high value).
"""
import time
import numpy as np
from aud import Par, riccati_fixed, b_of, stationary_fixed, coords, diffusive, contrast, region_table, \
    mean_coupling_baseline, type_law, sigma_mc, symmetrize_audience

t0 = time.time()
par = Par()
A = tuple(range(1, par.N))


def summarize_Pi(Sc, label):
    Pi = np.linalg.inv(Sc)
    dif = diffusive(Pi)
    tab = region_table(Pi) if dif[0] else {}
    rA = tab.get(A, float("nan"))
    best = max(((v, k) for k, v in tab.items()), default=(float("nan"), None))
    best_other = max(((v, k) for k, v in tab.items() if k != A), default=(float("nan"), None))
    print(f"[{label}] diffusive {dif[0]} (max off-diag {dif[1]:.3e}, min row sum {dif[2]:.3e}); r(A) {rA:.4f}; "
          f"best region {best[0]:.4f} {best[1]}; best other {best_other[0]:.4f} {best_other[1]}")
    return Pi, tab


# ---------------- full model (exact) ----------------
Pm_S, _ = riccati_fixed(par, 1.0 / par.RS, 0.0)
Pm_A, _ = riccati_fixed(par, 1.0 / par.R, b_of(par, 1, 0))
ty, p, G, mult = type_law(par, Pm_A)
pdev = 1 - sum(pp for (s, m), pp in zip(ty, p) if s == 1)
print(f"decision state P^- (audience) = {np.round(Pm_A, 6).tolist()}; source P^- = {np.round(Pm_S, 6).tolist()}")
print(f"EFE by type {dict(zip(ty, np.round(G, 6)))}; P(not reading the source) per member-round = {pdev:.3e}")
Pm = np.array([Pm_S] + [Pm_A] * par.n)
S, _, _ = stationary_fixed(par, [tuple()] + [(0,)] * par.n, Pm)
Sc = coords(par, S)
Pi, tab = summarize_Pi(Sc, "full, exact")
print("Pi^c full:", np.round(Pi, 4).tolist())
eps = Pi.sum(1)
a = -(Pi - np.diag(np.diag(Pi)))
print(f"couplings: audience pair {a[1,2]:.4f}, source-audience {a[0,1]:.4f}; leaks: source {eps[0]:.4f}, audience {eps[1]:.4f}")
cutA = a[1:, 0].sum()
print(f"cut(A) = {cutA:.4f}; xi_out(A) = {Pi[1:,1:].sum()/par.n:.4f}; r(A) = {tab[A]:.6f}; r(A u S) = {tab[tuple(range(par.N))]:.6f}")
mb = mean_coupling_baseline(Pi)
print(f"mean-coupling baseline {mb[0]:.6f} (abar {mb[1]:.4f}, epsbar {mb[2]:.4f}); window ({mb[0]:.4f}, {tab[A]:.4f}]")
print(f"leak heterogeneity on A: {eps[1:].max()/eps[1:].mean():.6f}")

# ---------------- negative control: the Monte Carlo pipeline on the full model ----------------
fx = sigma_mc(par, "full", npairs=40, T=200, burn=60, every=2, seed=101)
Sf = symmetrize_audience(fx["S"])
Pif, tabf = summarize_Pi(Sf, "NEG full via MC pipeline")
print(f"   attention deviation rate in sampled paths {fx['dev_rate']:.2e}")

# ---------------- nulls ----------------
for mode, label in (("hab", "N_hab (gamma=0)"), ("pr", "N_pr (redrawn every round)")):
    x = sigma_mc(par, mode, npairs=200, T=300, burn=80, every=2, seed=hash(mode) % 1000)
    Ss = np.array([symmetrize_audience(s) for s in x["S_pairs"]])
    Sm = Ss.mean(0)
    Pin, tabn = summarize_Pi(Sm, label)
    # standard error of r(A) by batching pairs into 20 batches
    rb = []
    for bi in range(20):
        Sb = Ss[bi::20].mean(0)
        try:
            rb.append(contrast(np.linalg.inv(Sb), A))
        except Exception:
            pass
    rb = np.array(rb)
    mix = Sm - symmetrize_audience(x["Priv"])
    print(f"   r(A) batches: mean {rb.mean():.4f} sd/sqrt(20) {rb.std(ddof=1)/np.sqrt(len(rb)):.4f}; "
          f"mixture part of cov(i,j): {mix[1,2]:.3e} (cov(i,j) {Sm[1,2]:.4e}); attention deviation rate {x['dev_rate']:.3f}")
    print(f"   Sigma^c null [varS, cov(S,i), var i, cov(i,j)] = {[round(v, 7) for v in (Sm[0,0], Sm[0,1], Sm[1,1], Sm[1,2])]}")

# ---------------- deletion null N_lp (channels deliver pure noise, attention pattern kept) ----------------
x = sigma_mc(par, "fixedS", npairs=40, T=200, burn=60, every=2, seed=7, dead=True)
Sd = symmetrize_audience(x["S"])
print(f"[N_lp dead channels] cov(S,i) {Sd[0,1]:.3e}, cov(i,j) {Sd[1,2]:.3e} (exact algebra: zero by construction); "
      f"r(A) = {contrast(np.linalg.inv(Sd), A):.6f}")
print(f"({time.time() - t0:.0f}s)")
