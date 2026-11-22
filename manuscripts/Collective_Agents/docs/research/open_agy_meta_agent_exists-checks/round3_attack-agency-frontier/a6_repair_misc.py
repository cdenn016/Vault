r"""Attack run a6: (1) a repair of the literal-eta_C failure: a pragmatic cost c_o on reading a non-member's relay
(members and group share it, def:agy-group-model "each slot's pragmatic term being that of the member j who controls
it"), with calibrated V_o = 1.263; supports {0, mate, o1, o2} (D1') and {mate, o1, o2} (D1'').  Index only; the
other clauses of D1'/D1'' are NOT re-verified here (the mechanism medium would need the cost declared for an
exchangeable population).
Declared expectations: D1' index -> 1 - 2 ln 2 / (2 ln 4 + 16 ln 2) = 0.9 (mate vs empty set unexplained);
D1'' index -> 1 (every departure from habits explained by costs).
(2) N_ex with computation noise removed (qc = 0): r(A) (survival needs r >= 3.7 and the same partition).
(3) N_pr and N_hab re-run with fresh seeds and larger batches (the a2 N_pr differed from the candidate by 2.2 SE).
NEGATIVE CONTROL: c_o = 0 must reproduce the a4 literal value (index 0 at V_o = 1.263)."""
import itertools
import time
import numpy as np
from scipy.optimize import minimize_scalar
from mylib import Par, steady, gains, efe, lbin, sigma_c_pattern, contrast, mc

t0 = time.time()
par = Par()
m = par.m
Pm = steady(par, 1, 0)
_, _, _, _, Pp = gains(par, Pm, 1, 0)
vstar = Pp[0, 0]
lb = lbin(m)
Vo = 1.263


def index_literal(sets, co, Vo=Vo):
    cset = {"0": 0, "mate": 1, "o1": 0, "o2": 0}
    cost = {"0": 0.0, "mate": 0.0, "o1": co, "o2": co}
    S = len(sets)
    lw = np.array([[lb[k] - par.gamma * (efe(par, Pm, cset[s], k) + cost[s]) for k in range(m + 1)] for s in sets])
    lw -= lw.max(); Pk = np.exp(lw); Pk /= Pk.sum(); pa = Pk.sum(1)
    KLa1 = sum(pa[i] * np.log(S * pa[i]) for i in range(S) if pa[i] > 0)
    KLs1 = sum(pa[i] * (Pk[i, k] / pa[i]) * (np.log(Pk[i, k] / pa[i]) - lb[k] + m * np.log(2.0))
               for i in range(S) for k in range(m + 1) if Pk[i, k] > 0)
    den = 2 * (KLa1 + KLs1)
    pairs = list(itertools.product(range(S), range(S)))
    Iatt = np.zeros((S, S)); Catt = np.zeros((S, S))
    for (i, j) in pairs:
        for o in ("o1", "o2"):
            no = (sets[i] == o) + (sets[j] == o)
            if no:
                Iatt[i, j] += 0.5 * np.log1p(no * Vo / par.Rc)
        Catt[i, j] = cost[sets[i]] + cost[sets[j]]
    Ks = np.arange(2 * m + 1); lb2 = lbin(2 * m)

    def mis(g):
        GA = -Iatt + Catt
        la = -np.log(S * S) - g * GA; la -= np.logaddexp.reduce(la.ravel())
        GC = -0.5 * np.log1p(Ks * vstar / par.Rs) + par.psi * Ks
        lZ = np.logaddexp.reduce(lb2 - 2 * m * np.log(2.0) - g * GC)
        tot = 0.0
        for (i, j) in pairs:
            w = pa[i] * pa[j]
            if w <= 0:
                continue
            tot += w * (np.log(w) - la[i, j])
            p1 = Pk[i] / pa[i]; p2 = Pk[j] / pa[j]
            for k1 in range(m + 1):
                for k2 in range(m + 1):
                    ww = p1[k1] * p2[k2]
                    if ww > 0:
                        tot += w * ww * (np.log(p1[k1]) - lb[k1] + np.log(p2[k2]) - lb[k2]
                                         + 2 * m * np.log(2.0) + g * GC[k1 + k2] + lZ)
        return tot
    r = minimize_scalar(lambda z: mis(np.exp(z)), bounds=(-12, 8), method="bounded", options=dict(xatol=1e-9))
    f = min(float(r.fun), mis(0.0))
    return 1 - f / den, float(np.exp(r.x)), 1 - pa[sets.index("mate")]


print("NEG c_o = 0, D1 support:", index_literal(["0", "mate", "o1", "o2"], 0.0))
for co in (1.0, 2.0, 4.0):
    print(f"c_o = {co}: D1' (0,mate,o1,o2) index/gamma*/P(not mate) {index_literal(['0', 'mate', 'o1', 'o2'], co)}; "
          f"D1'' (mate,o1,o2) {index_literal(['mate', 'o1', 'o2'], co)}")
print(f"({time.time() - t0:.1f}s)")
# (2) N_ex with qc = 0
Sc, _ = sigma_c_pattern(par.w(qc=0.0), [1, 0, 3, 2], [0, 0, 0, 0])
print(f"N_ex variant qc = 0: r(A) {contrast(np.linalg.inv(Sc), (0, 1)):.6f} (survival needs >= 3.7)")
# (3) fresh seeds
o = mc(par, "pr", B=6000, T=600, burn=150, seed=91)
print(f"N_pr (every round), fresh seed: r {o['r']:.4f} +- {o['se']:.4f}  ({time.time() - t0:.1f}s)")
o = mc(par, "hab", B=6000, T=600, burn=150, seed=92)
print(f"N_hab, fresh seed: r {o['r']:.4f} +- {o['se']:.4f}  ({time.time() - t0:.1f}s)")
o = mc(par, "full", B=6000, T=600, burn=150, seed=93)
print(f"full model, fresh seed: r {o['r']:.4f} +- {o['se']:.4f} (exact 4.345220)  ({time.time() - t0:.1f}s)")
