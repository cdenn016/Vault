r"""a4: my own open-neighborhood scan of the CCP ('own' coordinate), Latin
hypercube over 9 parameters INCLUDING rho (the candidate's box fixed rho), at
half-widths 1% and 5%.  At each point: r(pair), mean-coupling baseline, every
deletion/freezing null I computed in a1 (max over them, every-constant test:
max null < baseline), input-free d_M, alpha_I (prior average and posterior
average), agency (avg posterior belief).

Declared expectations (before running):
 E1 +-1%: a common level r0 = 3.75 works at every point (window intersection
    contains 3.75), every-constant test holds everywhere, d_M < 0.02, alpha_I
    (prior avg) < 0.05, agency (avg posterior) >= 0.25 everywhere.
 E2 +-5%: the common level may fail; agency (margin 0.015 at the center) may
    drop below 0.25 at some points; alpha_I (posterior average, margin 0.005)
    may exceed 0.05 at some points.
 E3 NEGATIVE CONTROL: at the center, setting Rc = 1e6 (relays useless) must
    empty the window or put N_eff above the lower edge (the relays create the
    base correlation the collider amplifies).
"""
import sys
import numpy as np
from ccp_lib import *
from ccp_full import *

T = coord_map("own")


def point(p):
    filt = member_filters(p)
    out = {}
    A, B, C, Dm, qv = private_system(p, filt, "full")
    Sf = window_condition(A, B, C, Dm, qv, T, L=60)
    o = summarize_pair(Sf)
    if not o["diffusive"]:
        return None
    out["r"] = o["r_pair"]; out["rbar"] = o["rbar"]; out["others"] = o["r_others_max"]
    nulls = {}
    nulls["eff"] = T @ stationary_cov(A, B, qv) @ T.T
    A2, B2, C2, D2_, q2 = private_system(p, filt, "lp")
    nulls["lp"] = window_condition(A2, B2, C2, D2_, q2, T, L=60)
    pm = dict(p); pm["Rc"] = p["Q"] / (1 - p["F"] ** 2) + p["R"] + p["Rc"]
    A3, B3, C3, D3, q3 = private_system(pm, filt, "lp")
    nulls["lpm"] = window_condition(A3, B3, C3, D3, q3, T, L=60)
    A4, B4, C4, D4, q4 = private_system(p, filt, "frozen")
    nulls["frz"] = window_condition(A4, B4, C4, D4, q4, T, L=60)
    f1 = member_filters(p, relay=False)
    A5, B5, C5, D5, q5 = private_system(p, f1, "none")
    nulls["rn1"] = window_condition(A5, B5, C5, D5, q5, T, L=60)
    f2 = member_filters(p, relay=False, own_R=p["R"] / 2)
    A6, B6, C6, D6, q6 = private_system(p, f2, "none", own_var=p["R"] / 2)
    nulls["rn2"] = window_condition(A6, B6, C6, D6, q6, T, L=60)
    mx = -np.inf
    for k, S in nulls.items():
        on = summarize_pair(S)
        val = on["r_pair"] if on["diffusive"] else np.inf
        out["null_" + k] = val
        mx = max(mx, val)
    out["maxnull"] = mx
    m = full_model(p)
    out["dM"] = dM_inputfree_prior_avg(m)
    out["aI_prior"] = alpha_I_prior_avg(m)
    out["aI_post"] = alpha_I_post_avg(m)
    out["agency"] = agency_index(m, belief="avg_post")
    return out


p0 = default_params()
keys = ["F", "Q", "rho", "R", "Rc", "qc", "kappa", "s2", "QZ"]
c = point(p0)
print("center:", {k: round(v, 5) for k, v in c.items()})
pn = dict(p0); pn["Rc"] = 1e6
cn = point(pn)
print("E3 negative control Rc=1e6:", {k: round(v, 4) for k, v in cn.items()} if cn else "non-diffusive")


def lhs(n, d, rng):
    u = np.zeros((n, d))
    for j in range(d):
        u[:, j] = (rng.permutation(n) + rng.random(n)) / n
    return u


for hw, npts in ((0.01, int(sys.argv[1]) if len(sys.argv) > 1 else 48), (0.05, int(sys.argv[2]) if len(sys.argv) > 2 else 48)):
    rng = np.random.default_rng(int(hw * 1000) + 3)
    U = lhs(npts, len(keys), rng)
    rows = []
    for i in range(npts):
        p = dict(p0)
        for j, k in enumerate(keys):
            p[k] = p0[k] * (1 + hw * (2 * U[i, j] - 1))
        o = point(p)
        rows.append(o)
    ok = [o for o in rows if o is not None]
    lo = max(o["rbar"] for o in ok); hi = min(o["r"] for o in ok)
    print("\nhalf-width %.2f: %d/%d diffusive" % (hw, len(ok), npts))
    print("  common window of levels: (%.4f, %.4f]  nonempty=%s ; r0=3.75 inside: %s" % (lo, hi, lo < hi, lo < 3.75 <= hi))
    print("  every-constant (max null < local baseline) at %d/%d; largest max-null %.4f; smallest local baseline %.4f"
          % (sum(o["maxnull"] < o["rbar"] for o in ok), len(ok), max(o["maxnull"] for o in ok), min(o["rbar"] for o in ok)))
    print("  others max %.4f" % max(o["others"] for o in ok))
    for k, thr, sense in (("dM", 0.02, "<="), ("aI_prior", 0.05, "<="), ("aI_post", 0.05, "<="), ("agency", 0.25, ">=")):
        vals = np.array([o[k] for o in ok])
        npass = np.sum(vals <= thr) if sense == "<=" else np.sum(vals >= thr)
        print("  %-9s range [%.4g, %.4g]; passes %s %.3g at %d/%d" % (k, vals.min(), vals.max(), sense, thr, npass, len(ok)))
