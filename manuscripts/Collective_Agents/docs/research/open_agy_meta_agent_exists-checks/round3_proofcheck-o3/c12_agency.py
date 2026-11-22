r"""Fresh-context check of C12 (agency bound when formation runs through internal attention).

Policies pi_i = (a_i, s_i); product habits E = E^a (x) E^s; admissible class: P_g(a, s) = E^a(a) P^s_g(s),
P^s_g propto E^s exp(-gamma G(s)), G a function of the slot profile, gamma >= 0 (habit-only model included).
Claims:
  B1 Agency <= KL_{s|a}/(KL_a + KL_{s|a}) at each decision state (and the weighted version over states).
  B2 with finite slot sets, KL_{s|a} <= sum_i ln|A_i|, hence Agency >= A0 needs sum_i ln|A_i| >= A0/(1-A0) KL_a.
Declared expectations:
  1. chain rule KL(P||E) = KL_a + KL_{s|a} to 1e-12; numerical infimum over the class (softmax
     optimization) equals the closed form KL_a + I(a;s) to 1e-6; B1 holds in every draw, single and
     weighted.
  2. B2 holds in every draw with UNIFORM slot habits.
Negative controls (must fail):
  N1 class with free attention law (attention tilts allowed): the index exceeds the B1 bound in
     some draws.
  N2 (defect probe for B2) non-uniform slot habits: KL_{s|a} > sum ln|A_i| and an index >= A0 with
     sum ln|A_i| < A0/(1-A0) KL_a.  Expected: B2 fails as stated; the repaired bound
     KL_{s|a} <= sum_i max ln(1/E^s_i) holds.
"""
import itertools
import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(99)
na, ns = 3, 2  # options per member: attention, slot
prof_a = list(itertools.product(range(na), range(na)))
prof_s = list(itertools.product(range(ns), range(ns)))


def kl(p, q):
    m = p > 0
    return float(np.sum(p[m] * np.log(p[m] / q[m])))


def pieces(P, Ea, Es):
    """P: (|a-profiles|, |s-profiles|) joint law."""
    Pa = P.sum(1)
    KLa = kl(Pa, Ea)
    Ps_a = P / Pa[:, None]
    KLsa = float(np.sum(Pa * np.array([kl(Ps_a[i], Es) for i in range(len(Pa))])))
    Ps = P.sum(0)
    I = float(np.sum(Pa * np.array([kl(Ps_a[i], Ps) for i in range(len(Pa))])))
    return KLa, KLsa, I


def prod_habit(per_member):
    return np.array([per_member[0][x] * per_member[1][y] for x, y in itertools.product(range(len(per_member[0])), repeat=2)])


def inf_class_numeric(P, Ea, Es):
    def obj(th):
        logits = np.log(Es) + np.concatenate([[0.0], th])
        q = np.exp(logits - logits.max())
        q /= q.sum()
        Pg = np.outer(Ea, q)
        return kl(P.ravel(), Pg.ravel())
    best = np.inf
    for _ in range(3):
        r = minimize(obj, rng.standard_normal(len(Es) - 1), method="BFGS", options={"gtol": 1e-10})
        best = min(best, r.fun)
    return best


worst_chain = worst_inf = 0.0
b1_viol = n1_exceed = b2_viol = 0
ndraw = 200
for _ in range(ndraw):
    Ea = prod_habit([rng.dirichlet(np.ones(na) * 2), rng.dirichlet(np.ones(na) * 2)]) if rng.random() < 0.5 else np.ones(na * na) / na ** 2
    Es = np.ones(ns * ns) / ns ** 2
    P = rng.dirichlet(np.ones(na * na * ns * ns) * rng.choice([0.2, 1.0, 5.0])).reshape(na * na, ns * ns)
    KLa, KLsa, I = pieces(P, Ea, Es)
    E = np.outer(Ea, Es)
    worst_chain = max(worst_chain, abs(kl(P.ravel(), E.ravel()) - (KLa + KLsa)))
    inf_num = inf_class_numeric(P, Ea, Es)
    worst_inf = max(worst_inf, abs(inf_num - (KLa + I)))
    denom = KLa + KLsa
    index = 1 - inf_num / denom
    bound = KLsa / denom
    b1_viol += int(index > bound + 1e-9)
    n1_exceed += int(1 - I / denom > bound + 1e-9)  # free attention law: inf over products = I(a;s)
    b2_viol += int(KLsa > 2 * np.log(ns) + 1e-12)
print(f"chain rule max error {worst_chain:.2e}; |numeric inf - (KL_a + I)| max {worst_inf:.2e}")
print(f"B1 violations {b1_viol}/{ndraw};  N1 (attention tilts allowed) exceeds bound in {n1_exceed}/{ndraw}")
print(f"B2 (uniform slot habits) violations {b2_viol}/{ndraw}")

# weighted multi-state version
wviol = 0
for _ in range(100):
    X = 3
    w = rng.dirichlet(np.ones(X))
    Ea = np.ones(na * na) / na ** 2
    Es = np.ones(ns * ns) / ns ** 2
    Ps = [rng.dirichlet(np.ones(na * na * ns * ns)).reshape(na * na, ns * ns) for _ in range(X)]
    # one group model shared across states (state-independent class here: same slot law) - numeric inf
    def obj(th):
        logits = np.concatenate([[0.0], th])
        q = np.exp(logits - logits.max()); q /= q.sum()
        return sum(wx * kl(Px.ravel(), np.outer(Ea, q).ravel()) for wx, Px in zip(w, Ps))
    inf = min(minimize(obj, rng.standard_normal(3), method="BFGS").fun for _ in range(2))
    parts = [pieces(Px, Ea, Es) for Px in Ps]
    num = sum(wx * p[1] for wx, p in zip(w, parts))
    den = sum(wx * (p[0] + p[1]) for wx, p in zip(w, parts))
    wviol += int(1 - inf / den > num / den + 1e-9)
print(f"weighted B1 violations {wviol}/100")

# N2: non-uniform slot habits (one member, two slots, for transparency; then two members)
delta = 1e-4
Es1 = np.array([1 - delta, delta])
Ps1 = np.array([1e-4, 1 - 1e-4])
KLs = kl(Ps1, Es1)
print(f"N2 one member: KL(P_s||E^s) = {KLs:.4f} > ln 2 = {np.log(2):.4f}; repaired bound ln(1/min E^s) = {np.log(1/delta):.4f}")
# attention part: 3 options, habit uniform, actual law concentrated -> KL_a
Pa1 = np.array([0.8, 0.1, 0.1])
KLa1 = kl(Pa1, np.ones(3) / 3)
Pjoint = np.outer(Pa1, Ps1)  # slot independent of attention: class contains E^a (x) P_s exactly
Ea1 = np.ones(3) / 3
KLa_, KLsa_, I_ = pieces(Pjoint, Ea1, Es1)
idx = 1 - (KLa_ + I_) / (KLa_ + KLsa_)
A0 = 0.9
print(f"  KL_a = {KLa_:.4f}, KL_s|a = {KLsa_:.4f}, I = {I_:.1e}, index = {idx:.4f} >= A0 = {A0}; "
      f"B2's necessary condition ln|A| = {np.log(2):.4f} >= A0/(1-A0) KL_a = {A0/(1-A0)*KLa_:.4f}? {np.log(2) >= A0/(1-A0)*KLa_}")
