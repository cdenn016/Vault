r"""C12: agency bound when habits are E^a (x) E^s and G_C depends on the slot profile only.
Own check: random joint laws P(a, s) of two members (attention option a_i in {0..2}, slot s_i in {0,1}),
class = { E^a (x) P^s_g : P^s_g(s) prop. to E^s(s) exp(-gamma_C G_C(s)) } over random G_C and gamma_C >= 0, plus
the superset { E^a (x) Q : Q any law on slot profiles } whose infimum is KL_a + I(a;s) in closed form.
"""
import itertools

import numpy as np
from scipy.optimize import minimize_scalar

rng = np.random.default_rng(3)


def kl(p, q):
    m = p > 0
    return float(np.sum(p[m] * np.log(p[m] / q[m])))


na, ns_ = 9, 4  # joint attention profiles (3x3), joint slot profiles (2x2)
viol = 0; viol2 = 0; ctrl = 0; idgap = 0.0; ratio_viol = 0; tot = 300; maxgap = -np.inf
for _ in range(tot):
    P = rng.dirichlet(np.ones(na * ns_) * rng.choice([0.2, 1.0, 5.0])).reshape(na, ns_)
    Ea_i = [rng.dirichlet(np.ones(3)) for _ in range(2)]
    Es_i = [rng.dirichlet(np.ones(2)) for _ in range(2)]
    Ea = np.outer(Ea_i[0], Ea_i[1]).ravel(); Es = np.outer(Es_i[0], Es_i[1]).ravel()
    E = np.outer(Ea, Es)
    Pa = P.sum(1); Ps = P.sum(0)
    KLa = kl(Pa, Ea)
    KLsa = sum(Pa[a] * kl(P[a] / Pa[a], Es) for a in range(na) if Pa[a] > 0)
    den = kl(P.ravel(), E.ravel())
    assert abs(den - (KLa + KLsa)) < 1e-10
    bound = KLsa / den
    Imi = kl(P.ravel(), np.outer(Pa, Ps).ravel())
    # class: one random G_C on slot profiles, gamma_C >= 0 optimized (contains the habit-only model)
    G = rng.normal(size=ns_)

    def obj(gam):
        w = Es * np.exp(-gam * G); w /= w.sum()
        return kl(P.ravel(), np.outer(Ea, w).ravel())

    res = minimize_scalar(obj, bounds=(0, 200), method="bounded")
    inf_class = min(res.fun, obj(0.0))
    index = 1 - inf_class / den
    viol += index > bound + 1e-9
    maxgap = max(maxgap, index - bound)
    # superset: any Q on slots; infimum attained at Q = P_s: KL_a + I(a;s)
    inf_sup = kl(P.ravel(), np.outer(Ea, Ps).ravel())
    idgap = max(idgap, abs(inf_sup - (KLa + Imi)))
    index_sup = 1 - inf_sup / den
    viol += index_sup > bound + 1e-9
    # ratio identity: index_sup / bound = KL(P_s||E^s) / (I + KL(P_s||E^s)) <= slot-marginal index (=1 for the superset)
    ratio_viol += abs(index_sup / bound - kl(Ps, Es) / (Imi + kl(Ps, Es))) > 1e-9
    # second part: KL_{s|a} <= sum_i max ln(1/E^s_i)
    cap = sum(np.log(1 / e.min()) for e in Es_i)
    viol2 += KLsa > cap + 1e-12
    # negative control: models allowed to tilt attention (Q any law on (a,s) product a (x) s) can exceed the bound
    inf_tilt = kl(P.ravel(), np.outer(Pa, Ps).ravel())
    ctrl += (1 - inf_tilt / den) > bound + 1e-9
print(f"bound index <= KL_s|a/(KL_a+KL_s|a): violations {viol}/{2 * tot} (class and superset); max(index - bound) in the one-G class = {maxgap:.2e}")
print(f"superset infimum == KL_a + I(a;s): max error {idgap:.1e}; ratio identity violations {ratio_viol}/{tot}")
print(f"KL_s|a <= sum_i max ln(1/E^s_i): violations {viol2}/{tot}")
print(f"negative control (attention tilts allowed): bound exceeded in {ctrl}/{tot}")

# planted error: the superseded second part, KL_{s|a} <= sum_i ln|A_i|, fails for non-uniform slot habits
Pa = np.array([0.8, 0.1, 0.1]); Ea = np.ones(3) / 3
Es = np.array([1 - 1e-4, 1e-4]); Ps = np.array([1e-4, 1 - 1e-4])
KLa = kl(Pa, Ea); KLsa = kl(Ps, Es)
idx = KLsa / (KLa + KLsa)
print(f"superseded bound, one member: KL_a={KLa:.4f}, KL_s|a={KLsa:.4f}, index (class containing E^a (x) P_s)={idx:.4f}; "
      f"ln|A|={np.log(2):.4f} < A0/(1-A0) KL_a={0.9 / 0.1 * KLa:.4f} although index >= 0.9; repaired cap ln(1/min E^s)={np.log(1e4):.4f}")
# I* arithmetic quoted in the note
print(f"I* arithmetic: 0.13345/(16.6321+0.13345) = {0.13345 / (16.6321 + 0.13345):.5f} (note: index 0.008)")
