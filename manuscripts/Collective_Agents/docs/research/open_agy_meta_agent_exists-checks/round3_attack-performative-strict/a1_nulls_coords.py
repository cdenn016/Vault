r"""a1: deciding contrast numbers of the CCP with my own code, the deletion and
freezing nulls the candidate did not compute (N_fr, N_rn), and the
every-selector-constant test for the 'own' and the common coordinates.

Declared expectations (before running):
 E1 'own': r(pair) = 4.3336, mean-coupling baseline 3.2224, N_eff = N_hab = 1.8093,
    N_lp = 1.2397 (candidate's numbers) to 4 decimals.
 E2 N_fr with fresh receiver channel noise equals N_lp exactly (same private inputs).
 E3 N_fr with frozen relay (no private relay input) and N_rn variants: contrast
    stays below the window's lower edge 3.2224 (my static-collider estimate caps a
    relay-free pair near r < 3).  If any variant reaches >= 3.2224 the
    every-selector-constant reading fails; if >= 3.75 the declared level fails.
 E4 common coordinate at 45 deg: N_eff (about 5.26) lies INSIDE the window
    (4.576, 6.364], so under the every-selector-constant reading the sum
    coordinate does NOT differ from N_eff at levels r0 in (4.576, 5.261].
 E5 NEGATIVE CONTROL that must fail the differ test: N_eff evaluated with the
    collider ON (i.e. the full model itself) selects the same partition at every r0.
"""
import numpy as np
from ccp_lib import *

np.set_printoptions(precision=6, suppress=True)
p = default_params()
filt = member_filters(p)


def cond_cov(p, filt, mode, T, own_var=None, collider=True, L=60):
    A, B, C, Dm, qv = private_system(p, filt, mode, own_var=own_var, collider=collider)
    if not collider:
        return T @ stationary_cov(A, B, qv) @ T.T
    return window_condition(A, B, C, Dm, qv, T, L=L)


def every_constant(full, nulls, rbar_full, ngrid=400):
    """For r0 on a fine grid in the admissible window (rbar, r_pair], compare the
    selected partition of the full model with each null's, both with the medium
    held fixed (R3) and with the null's own mean-coupling medium."""
    Pi_f = population_from_pair(full)
    rp = rates(Pi_f, (0, 1))[2]
    grid = np.linspace(rbar_full, rp, ngrid + 2)[1:]
    res = {}
    for name, S in nulls.items():
        Pi_n = population_from_pair(S)
        if not is_diffusive(Pi_n):
            res[name] = "null not diffusive"
            continue
        rb_own = baseline_mean_coupling(Pi_n)[0]
        same_fixed = [r0 for r0 in grid if selected_partition(Pi_n, r0, rbar_full) == selected_partition(Pi_f, r0, rbar_full)]
        same_own = [r0 for r0 in grid if selected_partition(Pi_n, r0, rb_own) == selected_partition(Pi_f, r0, rbar_full)]
        res[name] = (len(same_fixed), len(same_own), len(grid),
                     (min(same_fixed), max(same_fixed)) if same_fixed else None)
    return res


T = coord_map("own")
full = cond_cov(p, filt, "full", T)
out = summarize_pair(full, "full")
print("FULL own: Sigma^c=\n", full)
print("  Pi pair block=\n", out["Pi2"], "\n  diffusive", out["diffusive"],
      "r(pair)=%.5f rbar=%.5f others_max=%.5f" % (out["r_pair"], out["rbar"], out["r_others_max"]))
rbar = out["rbar"]
Pi_f = population_from_pair(full)
eps = Pi_f.sum(1)
print("  leaks", eps, " leak ratio in pair", eps[:2].max() / eps[:2].mean())

nulls = {}
nulls["N_eff"] = cond_cov(p, filt, "full", T, collider=False)
nulls["N_hab"] = nulls["N_eff"]  # acts from habits carry no private information
nulls["N_lp(Rc)"] = cond_cov(p, filt, "lp", T)
p_m = dict(p); p_m["Rc"] = p["Q"] / (1 - p["F"] ** 2) + p["R"] + p["Rc"]
nulls["N_lp(matched var)"] = cond_cov(p_m, filt, "lp", T)
nulls["N_fr(fresh nu)"] = cond_cov(p, filt, "lp", T)
nulls["N_fr(frozen)"] = cond_cov(p, filt, "frozen", T)
f1 = member_filters(p, relay=False)
nulls["N_rn(own only, R)"] = cond_cov(p, f1, "none", T)
f2 = member_filters(p, relay=False, own_R=p["R"] / 2)
nulls["N_rn(own twice, R/2)"] = cond_cov(p, f2, "none", T, own_var=p["R"] / 2)
for name, S in nulls.items():
    o = summarize_pair(S, name)
    if o["diffusive"]:
        print("%-22s diffusive  r(pair)=%.5f  own-medium rbar=%.5f  Pi2=%s" % (name, o["r_pair"], o["rbar"], np.round(o["Pi2"].ravel(), 3)))
    else:
        print("%-22s NOT diffusive Pi2=%s" % (name, np.round(o["Pi2"].ravel(), 3)))

print("\nEvery-selector-constant test ('own'): (#same partition with medium fixed, #same with null's own medium, #grid, range)")
for k, v in every_constant(full, nulls, rbar).items():
    print("  %-22s %s" % (k, v))
print("NEGATIVE CONTROL (full model as its own null):", every_constant(full, {"full": full}, rbar))

print("\nCoordinate scan (common coordinate cos(th) e^a + sin(th) e^b for both members)")
print(" th   r(pair)  rbar   r_eff  r_lp   declared-level window   every-constant (N_eff < rbar and N_lp < rbar)")
for th in [0, 15, 30, 35, 40, 45, 50, 55, 60, 90, 135]:
    Tth = coord_map(("dir", th))
    Sf = cond_cov(p, filt, "full", Tth)
    of = summarize_pair(Sf)
    Se = cond_cov(p, filt, "full", Tth, collider=False)
    oe = summarize_pair(Se)
    Sl = cond_cov(p, filt, "lp", Tth)
    ol = summarize_pair(Sl)
    rl = ol["r_pair"] if ol["diffusive"] else float("nan")
    lo = max(of["rbar"], oe["r_pair"], rl if ol["diffusive"] else -np.inf)
    decl = "(%.3f, %.3f]" % (lo, of["r_pair"]) if lo < of["r_pair"] else "empty"
    ec = (oe["r_pair"] < of["rbar"]) and (ol["diffusive"] and rl < of["rbar"])
    print("%4d  %.4f  %.4f  %.4f  %s  %-22s %s" % (th, of["r_pair"], of["rbar"], oe["r_pair"],
          ("%.4f" % rl) if ol["diffusive"] else "nondiff", decl, ec))
for nm in ["a", "b"]:
    Tn = coord_map(nm)
    of = summarize_pair(cond_cov(p, filt, "full", Tn))
    oe = summarize_pair(cond_cov(p, filt, "full", Tn, collider=False))
    print("coord %s: r(pair)=%.4f rbar=%.4f N_eff=%.4f" % (nm, of["r_pair"], of["rbar"], oe["r_pair"]))

# Kronecker test: is the vector world-conditional covariance of the members'
# current errors of the form Sigma^sc (x) I_2 ?
Tv = np.zeros((4, NX)); Tv[0, 0] = 1; Tv[1, 1] = 1; Tv[2, 4] = 1; Tv[3, 5] = 1
Sv = cond_cov(p, filt, "full", Tv)
print("\nvector Sigma^c of (e_b^a, e_b^b, e_s^a, e_s^b):\n", Sv)
blk = [[Sv[2*i:2*i+2, 2*j:2*j+2] for j in range(2)] for i in range(2)]
dev = max(np.max(np.abs(blk[i][j] - np.trace(blk[i][j]) / 2 * np.eye(2))) for i in range(2) for j in range(2))
print("max deviation of 2x2 agent blocks from scalar*I_2:", dev, "(Kronecker form needs 0)")
