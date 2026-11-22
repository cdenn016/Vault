"""Items 7 and 8: nulls N_hab, N_pr (with the test of prop:agy-tests(b)), N_lp, N_fr.

Expectations (before running): N_hab and N_pr give r(A) well below 5.37 (members read S w.p. 4/11
and 1/2), diffusive; the N_pr test, if run, gives p=1/1000. N_lp: diagonal Sigma^c, r(A)=1 up to MC
noise. N_fr with private broadcast (sensing) noise: frozen v_S(0) is a common offset of all members,
strong positive member correlations, r(A) large; with frozen broadcast noises conditioned, diagonal.
"""
import os
import sys
import json
import time

for _k in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[_k] = "4"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np  # noqa: E402
import p1lib as L  # noqa: E402

np.set_printoptions(precision=7, linewidth=160)
t0 = time.time()
p = L.BASE
out: dict = {}
regs = L.regions(5)


def report(name, res, extra=""):
    Sg = L.group_sigmas(res)
    S, Sse = L.jackknife(lambda X: X, Sg)
    an = L.analyze_sigma(S)
    rall, rse = L.jackknife(lambda X: np.array([L.analyze_sigma(X)["r_all"][C] for C in regs]), Sg)
    mo, mose = L.jackknife(lambda X: L.analyze_sigma(X)["maxoff"], Sg)
    mr, mrse = L.jackknife(lambda X: L.analyze_sigma(X)["minrow"], Sg)
    iA = regs.index((1, 2, 3, 4))
    imax = int(np.argmax(rall))
    oth = [i for i in range(len(regs)) if i != iA]
    io = oth[int(np.argmax(rall[oth]))]
    print(f"\n=== {name} {extra}===")
    print("Sigma^c:\n", S, "\nSE:\n", Sse)
    print("Pi:\n", an["Pi"])
    print("diffusive:", an["diffusive"], " largest off-diagonal %.6g +- %.2g, smallest row sum %.6g +- %.2g" % (
        mo, mose, mr, mrse))
    print("r(A) = %.6f +- %.2g;  largest regional contrast: %s r=%.6f +- %.2g;  largest other region: %s r=%.6f +- %.2g" % (
        rall[iA], rse[iA], regs[imax], rall[imax], rse[imax], regs[io], rall[io], rse[io]))
    print("attention law (members avg):", res["att_prob"].mean(0))
    return dict(Sigma=S.tolist(), Sigma_se=Sse.tolist(), Pi=an["Pi"].tolist(), diffusive=an["diffusive"],
                maxoff=[mo, mose], minrow=[mr, mrse], rA=[rall[iA], rse[iA]],
                rmax=[str(regs[imax]), rall[imax], rse[imax]], rother=[str(regs[io]), rall[io], rse[io]],
                att=res["att_prob"].mean(0).tolist())


B, TB, TA, G = 3000, 100, 300, 20
r_hab = L.simulate(L.Model(p, att="hab"), B=B, T_burn=TB, T_avg=TA, seed=101, G=G)
out["N_hab"] = report("N_hab (gamma=0, uniform habits over the 11 sets)", r_hab)
print("[%.1fs]" % (time.time() - t0))
r_pr = L.simulate(L.Model(p, att="pr"), B=B, T_burn=TB, T_avg=TA, seed=102, G=G)
out["N_pr"] = report("N_pr (two partners uniformly from the four others, redrawn every round)", r_pr)
print("[%.1fs]" % (time.time() - t0))
r_lp = L.simulate(L.Model(p, att="efe", content="lp"), B=B, T_burn=TB, T_avg=TA, seed=103, G=G)
out["N_lp"] = report("N_lp (channels deliver pure noise N(0,R_j+R_c); attention by EFE unchanged)", r_lp)
print("[%.1fs]" % (time.time() - t0))
r_fr = L.simulate(L.Model(p, att="efe", content="fr"), B=B, T_burn=TB, T_avg=TA, seed=104, G=G)
out["N_fr"] = report("N_fr (others frozen at u_j(0)=s_j(0); sensing noise private, spec convention)", r_fr)
print("[%.1fs]" % (time.time() - t0))
r_fr0 = L.simulate(L.Model(p, att="efe", content="fr", cond_v0=True), B=B, T_burn=TB, T_avg=TA, seed=105, G=G)
out["N_fr_cond_v0"] = report("N_fr with the frozen broadcast noises v_j(0) in the conditioning set (table reading)",
                             r_fr0)
print("[%.1fs]" % (time.time() - t0))

# ---------------- test of prop:agy-tests(b) for N_pr, statistic r(A)
# Declared estimator for one draw: Rao-Blackwellized plug-in Sigma^c from 20 attention paths
# (10 pairs), burn-in 60 rounds, 100 averaged rounds; statistic = r(A) of that estimate.
print("\n=== N_pr test (prop:agy-tests(b)), n_null = 999 ===")
nnull, bpg = 999, 10
rn = L.simulate(L.Model(p, att="pr"), B=2 * nnull * bpg, T_burn=60, T_avg=100, seed=2027, G=nnull)
Sn = L.group_sigmas(rn)
Snull = np.array([L.analyze_sigma(X)["rA"] for X in Sn])
r0 = L.simulate(L.Model(p, att="efe"), B=2 * bpg, T_burn=60, T_avg=100, seed=2028, G=1)
S0 = L.analyze_sigma(L.group_sigmas(r0)[0])["rA"]
pval = (1 + np.sum(Snull >= S0)) / (nnull + 1)
print("S_0 (full model, same estimator) = %.6f" % S0)
print("null draws: mean %.6f, sd %.4g, min %.6f, max %.6f" % (Snull.mean(), Snull.std(), Snull.min(), Snull.max()))
print("p = (1 + #{S_l >= S_0})/(n_null+1) = %.6g" % pval)
out["N_pr_test"] = dict(S0=S0, null_mean=Snull.mean(), null_sd=Snull.std(), null_min=Snull.min(),
                        null_max=Snull.max(), p=pval, n_null=nnull)

with open(os.path.join(HERE, "s3_nulls_output.json"), "w") as f:
    json.dump(out, f, indent=1, default=float)
print("\nwall time %.1f s" % (time.time() - t0))
