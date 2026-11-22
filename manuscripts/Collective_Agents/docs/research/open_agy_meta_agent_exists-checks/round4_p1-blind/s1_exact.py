"""Items 1, 3, 9 (exact or deterministic-to-working-precision parts) and an engine validation.

Expectation (stated before running): {S}~0.21, {S,m_k}~0.26 each, non-S sets total ~1e-14;
p({}) under deletion ~1e-15; r(A) without member channels a few percent below the full model;
agency index ~0.995 with gamma_C* ~ 200-250.
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

np.set_printoptions(precision=6, linewidth=150)
t0 = time.time()
p = L.BASE
out = {}

# ---------------- item 1: exact stationary attention law (history chain)
print("=== Item 1: stationary attention law (history-truncated chain, reduced alphabet {S},{S,m}) ===")
prev = None
for Lh in (4, 6, 8, 10, 12, 14):
    ex = L.exact_attention_law(p, L=Lh)
    law5 = ex["law5"]
    if prev is not None:
        print(f"L={Lh:2d} law5={law5} max|diff vs L-2|={np.abs(law5 - prev).max():.2e} nonS={ex['nonS']:.4e}")
    else:
        print(f"L={Lh:2d} law5={law5} nonS={ex['nonS']:.4e}")
    prev = law5
exL = L.exact_attention_law(p, L=14)
law5 = exL["law5"]
full6 = L.exact_attention_law_full(p, L=6)["law5"]
red6 = L.exact_attention_law(p, L=6)["law5"]
print("cross-check full 5-type chain L=6:", full6)
print("reduced chain L=6               :", red6, " max diff", np.abs(full6 - red6).max())
law11 = L.law11_from_types(law5)
for k, v in law11.items():
    print(f"  {k:24s} {v:.10e}")
print("  total over the 11 sets:", L.pbar11(law5).sum())
print("  mean claimed prior variance of eta (next round):", exL["v_prior"], " posterior var of eta_t:", exL["v_post"])
out["item1"] = dict(law5=law5.tolist(), law11={k: float(v) for k, v in law11.items()},
                    nonS=float(law5[:3].sum()), v_prior=exL["v_prior"], v_post=exL["v_post"],
                    full6_minus_red6=float(np.abs(full6 - red6).max()))

# ---------------- item 9: agency index
print("\n=== Item 9: agency index ===")
nonS = float(law5[:3].sum())
for lab, v_eta in (("V = claimed prior var + R_S (primary)", exL["v_prior"]),
                   ("V = posterior var of eta_t + R_S (sensitivity)", exL["v_post"])):
    V = v_eta + p["RS"]
    ag = L.agency_index(law5, nonS, p, V)
    print(lab, f"V={V:.6f}")
    for k, v in ag.items():
        print(f"   {k:14s} {v:.10g}")
    out.setdefault("item9", {})[lab] = {k: float(v) for k, v in ag.items()}
# sensitivity: drop the non-S mass entirely (P(k<4)=0): infimum is the gamma_C->inf limit
print("   gamma_C -> infinity limit with non-S mass set to 0:",
      4 * (L.pbar11(law5)[[7, 8, 9, 10]] / L.pbar11(law5)[[7, 8, 9, 10]].sum() *
           np.log(L.pbar11(law5)[[7, 8, 9, 10]] / L.pbar11(law5)[[7, 8, 9, 10]].sum())).sum() + np.log(256))

# ---------------- item 3: member channels deleted (exact)
print("\n=== Item 3: channels among members deleted (attend {} or {S}) ===")
ex3 = L.exact_fixedS(p)
print("p({}) at the fixed point =", ex3["p_empty"], " info gap I({S})-I({}) =", ex3["dI"], "nats")
print("Lyapunov residual:", ex3["resid"])
S3 = ex3["Sigma"]
print("Sigma^c (exact):\n", S3)
an3 = L.analyze_sigma(S3)
print("Pi:\n", an3["Pi"])
print("diffusive:", an3["diffusive"], " max offdiag:", an3["maxoff"], " min row sum:", an3["minrow"])
print("r(A) =", repr(an3["rA"]), " largest other region:", an3["max_other"], " hetA:", an3["hetA"])
print("couplings a_ij:\n", an3["a"], "\nleaks:", an3["eps"])
print("mean-coupling baseline:", an3["baseline_mean"])
out["item3"] = dict(p_empty=float(ex3["p_empty"]), dI=float(ex3["dI"]), Sigma=S3.tolist(),
                    Pi=an3["Pi"].tolist(), rA=float(an3["rA"]), diffusive=an3["diffusive"],
                    maxoff=float(an3["maxoff"]), minrow=float(an3["minrow"]),
                    max_other=[list(an3["max_other"][0]), float(an3["max_other"][1])],
                    baseline_mean=float(an3["baseline_mean"]), hetA=float(an3["hetA"]))

# item 4 part: deletion -> conditional covariance given (eta, v_S) exactly zero among members
ex3c = L.exact_fixedS(p, condS=True)
S3c = ex3c["Sigma"]
print("\nItem 4 under deletion: Cov(e|eta,v_S) (exact):\n", S3c)
print("max |offdiag among members| =", np.abs(S3c[1:, 1:] - np.diag(np.diag(S3c[1:, 1:]))).max())
out["item4_deleted"] = dict(Sigma=S3c.tolist(),
                            max_off_members=float(np.abs(S3c[1:, 1:] - np.diag(np.diag(S3c[1:, 1:]))).max()))

# ---------------- engine validation: fixed-{S} engine vs Lyapunov
print("\n=== Engine validation: Rao-Blackwellized engine in fixed-{S} mode vs exact Lyapunov ===")
m = L.Model(p, att="fixedS")
r = L.simulate(m, B=200, T_burn=200, T_avg=50, seed=7, G=20)
Se = L.group_sigmas(r).mean(0)
print("engine Sigma:\n", Se)
print("max |engine - exact| =", np.abs(Se - S3).max(), " (relative", np.abs(Se - S3).max() / np.abs(S3).max(), ")")
out["validation_fixedS_maxabs"] = float(np.abs(Se - S3).max())
mc = L.Model(p, att="fixedS", condS=True)
rc = L.simulate(mc, B=200, T_burn=200, T_avg=50, seed=8, G=20)
Sec = L.group_sigmas(rc).mean(0)
print("engine Cov(e|eta,v_S) fixed-{S}:\n", Sec, "\nmax |engine-exact|", np.abs(Sec - S3c).max())
out["validation_fixedS_condS_maxabs"] = float(np.abs(Sec - S3c).max())

with open(os.path.join(HERE, "s1_exact_output.json"), "w") as f:
    json.dump(out, f, indent=1)
print("\nwall time %.1f s" % (time.time() - t0))
