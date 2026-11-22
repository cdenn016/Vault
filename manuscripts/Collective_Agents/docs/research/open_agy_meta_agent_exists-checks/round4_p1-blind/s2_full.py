"""Items 2, 4, 5, 6 at the base point (Monte Carlo over attention paths, noises integrated exactly).

Expectations (before running): members' Var ~0.0075, member-member cov ~0.004, S-member ~6.5e-4
(already seen in the timing probe at B=400); diffusive precision; r(A) a few percent above the
deletion value 5.38; mechanism medium baseline near 1; Cov(e_i,e_j|eta,v_S) small positive;
Markov defect 1e-3..1e-1 nats; inference KL ~1e-2 nats.
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
B, TB, TA, G = 6000, 100, 300, 30


def fmt(v, s):
    return f"{v:.6g} +- {s:.2g}"


# ------------------------------------------------------------------ item 2: full model
m = L.Model(p, kind="pop", att="efe", content="full")
r = L.simulate(m, B=B, T_burn=TB, T_avg=TA, seed=20261122, G=G, do_union=True, do_memory=True)
print(f"[full model run: B={B}, burn {TB}, average {TA}, groups {G}; {time.time()-t0:.1f}s]")
Sg = L.group_sigmas(r)
S, Sse = L.jackknife(lambda X: X, Sg)
print("=== Item 2: Sigma^c (second-moment convention), agents ordered (S,1,2,3,4) ===")
print(S)
print("jackknife SE:\n", Sse)
print("attention law (Rao-Blackwellized MC, member 1):", r["att_prob"][0])
print("attention law averaged over members: {S}=%.6f {S,m}=%.6f(each) nonS total=%.3e" % (
    r["att_prob"][:, 1].mean(), r["att_prob"][:, 5:8].mean(), r["att_prob"][:, [0, 2, 3, 4, 8, 9, 10]].sum(1).mean()))
print("max non-S probability over all draws:", r["max_nonS"], " union kS!=4 events:", r["nU_bad"])

an = L.analyze_sigma(S)


def st(f):
    return L.jackknife(lambda X: f(L.analyze_sigma(X)), Sg)


Pi, Pise = st(lambda a: a["Pi"])
print("Pi:\n", Pi, "\nSE:\n", Pise)
mo, mose = st(lambda a: a["maxoff"])
mr, mrse = st(lambda a: a["minrow"])
print("diffusive:", an["diffusive"], " largest off-diagonal:", fmt(mo, mose), " smallest row sum:", fmt(mr, mrse))
aa, aase = st(lambda a: a["a"])
ee, eese = st(lambda a: a["eps"])
print("couplings a_ij:\n", aa, "\nSE:\n", aase)
print("leaks eps:", ee, "\nSE:", eese)
rA, rAse = st(lambda a: a["rA"])
print("r(A) =", fmt(rA, rAse))
regs = L.regions(5)
rall, rallse = L.jackknife(lambda X: np.array([L.analyze_sigma(X)["r_all"][C] for C in regs]), Sg)
print("contrast of every region (agent 0 = S):")
order = np.argsort(-rall)
for i in order:
    print(f"   {str(regs[i]):18s} r = {rall[i]:.6f} +- {rallse[i]:.2g}")
bm, bmse = st(lambda a: a["baseline_mean"])
ab, abse = st(lambda a: a["abar"])
eb, ebse = st(lambda a: a["ebar"])
het, hetse = st(lambda a: a["hetA"])
print("mean coupling abar =", fmt(ab, abse), " mean leak =", fmt(eb, ebse))
print("mean-coupling baseline (sup over regions of the comparison medium) =", fmt(bm, bmse),
      " check 1+5abar/ebar =", 1 + 5 * ab / eb)
print("leak heterogeneity on A eps_max/eps_bar =", fmt(het, hetse))
xin, xinse = L.jackknife(lambda X: L.contrast_from_precision(np.linalg.inv(X), (1, 2, 3, 4))["xin"], Sg)
xout, xoutse = L.jackknife(lambda X: L.contrast_from_precision(np.linalg.inv(X), (1, 2, 3, 4))["xout"], Sg)
print("x_in(A) =", fmt(xin, xinse), " x_out(A) =", fmt(xout, xoutse))
out["item2"] = dict(Sigma=S.tolist(), Sigma_se=Sse.tolist(), Pi=Pi.tolist(), Pi_se=Pise.tolist(),
                    maxoff=[mo, mose], minrow=[mr, mrse], a=aa.tolist(), a_se=aase.tolist(),
                    eps=ee.tolist(), eps_se=eese.tolist(), rA=[rA, rAse],
                    regions={str(regs[i]): [rall[i], rallse[i]] for i in range(len(regs))},
                    baseline_mean=[bm, bmse], abar=[ab, abse], ebar=[eb, ebse], hetA=[het, hetse],
                    xin=[xin, xinse], xout=[xout, xoutse],
                    att_prob_member_avg=r["att_prob"].mean(0).tolist())

# ------------------------------------------------------------------ item 6: inference
print("\n=== Item 6: inference clause (union model = exact filter on all members' own sensors and"
      " source messages, no q_c) ===")
aU = r["accU"]
cnt = aU["cnt"]


def kl_stats(acc):
    mm = {k: acc[k].sum() / acc["cnt"].sum() for k in acc}
    vstar = 1 / mm["1/PU"]
    fwd_best = 0.5 * (mm["d2/PU"] - np.log(vstar) + mm["lnPU"])
    fwd_claim = 0.5 * (mm["v/PU"] + mm["d2/PU"] - 1 - mm["ln(v/PU)"])
    rev_best = 0.5 * (np.log(mm["PU+d2"]) - mm["lnPU"])
    rev_claim = 0.5 * (mm["PU/v"] + mm["d2/v"] - 1 + mm["ln(v/PU)"])
    return np.array([fwd_best, fwd_claim, rev_best, rev_claim, mm["d2"], mm["PU"], mm["v"], vstar])


accg = np.stack([np.stack([aU[k] for k in aU]) for _ in [0]])[0]  # (K,G)
keys = list(aU.keys())


def kl_from_groups(Xg):
    return kl_stats({k: Xg[i] for i, k in enumerate(keys)})


# jackknife over groups on sums
vals = kl_from_groups(accg)
loo = np.array([kl_from_groups(np.delete(accg, g, 1)) for g in range(G)])
se = np.sqrt((G - 1) / G * ((loo - loo.mean(0)) ** 2).sum(0))
labs = ["KL(q_y||p_U), best constant v", "KL(q_y||p_U), claimed prior variance",
        "KL(p_U||q_y), best constant v", "KL(p_U||q_y), claimed prior variance",
        "E[(y-m^U)^2]", "P^U (union predictive variance of eta_t)", "E[claimed prior variance]",
        "best constant v (forward)"]
for l_, v_, s_ in zip(labs, vals, se):
    print(f"   {l_:45s} {v_:.8g} +- {s_:.2g}")
out["item6"] = {l_: [float(v_), float(s_)] for l_, v_, s_ in zip(labs, vals, se)}

# ------------------------------------------------------------------ item 5: memory
print("\n=== Item 5: memory clause (input-conditional; noise-driven part; q_c scale drops out) ===")
I2, I1, Dcl = r["I2"], r["I1"], r["Dcl"]
m2 = I2.mean(0)
s2 = I2.std(0) / np.sqrt(B)
tsup = int(np.argmax(m2))
print("(ii) deterministic start: path-average I(y_{t+1};y_{0:t-1}|y_t) at t=0..12:", m2[:13])
print("     sup_t of path-average = %.6g +- %.2g at t=%d; value at t=%d: %.6g" % (m2[tsup], s2[tsup], tsup,
                                                                                  TB + TA - 1, m2[-1]))
m1 = I1.mean(0)
s1 = I1.std(0) / np.sqrt(B)
tsup1 = int(np.argmax(m1))
print("(i) stationary initial law: path-average vs history length 0..12:", m1[:13])
print("     sup over history length = %.6g +- %.2g at length %d; value at length %d: %.6g" % (
    m1[tsup1], s1[tsup1], tsup1, TA - 1, m1[-1]))
# spread over blanket paths at a fixed late time
late2 = I2[:, -1]
late1 = I1[:, -1]
q = [0.0, 0.05, 0.5, 0.95, 1.0]
print("     spread over paths at the last round, (ii): std %.4g, quantiles %s" % (late2.std(), np.quantile(late2, q)))
print("     spread over paths at the last round, (i):  std %.4g, quantiles %s" % (late1.std(), np.quantile(late1, q)))
sup_path2 = I2[:, TB:].max(1)
print("     per-path sup over rounds %d..%d (ii): mean %.4g, std %.4g, max %.4g" % (TB, TB + TA - 1, sup_path2.mean(),
                                                                                  sup_path2.std(), sup_path2.max()))
dc = Dcl[:, TB:].mean()
dcse = Dcl[:, TB:].mean(1).std() / np.sqrt(B)
dcm = Dcl.mean(0)
print("closure defect I(y_{t+1};x_t|y_t,x_B): stationary path/time average = %.6g +- %.2g;"
      " per-round std over paths %.4g; deterministic start t=0..6: %s" % (dc, dcse, Dcl[:, -1].std(), dcm[:7]))
out["item5"] = dict(det_sup=[float(m2[tsup]), float(s2[tsup]), tsup], det_last=float(m2[-1]),
                    stat_sup=[float(m1[tsup1]), float(s1[tsup1]), tsup1], stat_last=float(m1[-1]),
                    spread_det_last=dict(std=float(late2.std()), q=np.quantile(late2, q).tolist()),
                    spread_stat_last=dict(std=float(late1.std()), q=np.quantile(late1, q).tolist()),
                    per_path_sup_det=dict(mean=float(sup_path2.mean()), std=float(sup_path2.std()),
                                          max=float(sup_path2.max())),
                    closure=[float(dc), float(dcse)], closure_det_first=dcm[:7].tolist(),
                    det_curve=m2[:40].tolist(), stat_curve=m1[:40].tolist())

# ------------------------------------------------------------------ item 4: interaction given (eta, v_S)
print("\n=== Item 4: Cov(e_i,e_j | eta, v_S) for members ===")
mc = L.Model(p, kind="pop", att="efe", content="full", condS=True)
rc = L.simulate(mc, B=B, T_burn=TB, T_avg=TA, seed=777, G=G)
Sgc = L.group_sigmas(rc)


def pairstats(X):
    C = X[1:, 1:]
    iu = np.triu_indices(4, 1)
    cov = C[iu].mean()
    d = np.sqrt(np.diag(C))
    corr = (C / np.outer(d, d))[iu].mean()
    return np.array([cov, corr, np.diag(C).mean()])


v4, s4 = L.jackknife(pairstats, Sgc)
Sc, Scse = L.jackknife(lambda X: X, Sgc)
print("Cov(e|eta,v_S):\n", Sc, "\nSE:\n", Scse)
print("member pair covariance (avg over 6 pairs) = %.6g +- %.2g; correlation = %.6g +- %.2g; member var = %.6g" % (
    v4[0], s4[0], v4[1], s4[1], v4[2]))
out["item4"] = dict(Sigma=Sc.tolist(), Sigma_se=Scse.tolist(), cov=[v4[0], s4[0]], corr=[v4[1], s4[1]],
                    var=[v4[2], s4[2]])

# ------------------------------------------------------------------ medium generated by the mechanism
print("\n=== Mechanism medium: five agents of the members' type, gamma=40 ===")
mm_ = L.Model(p, kind="medium", att="efe", content="full")
rm = L.simulate(mm_, B=B, T_burn=TB, T_avg=TA, seed=4242, G=G)
Sgm = L.group_sigmas(rm)
Sm, Smse = L.jackknife(lambda X: X, Sgm)
print("Sigma^c medium:\n", Sm, "\nSE:\n", Smse)
print("medium attention law (avg over agents): ", rm["att_prob"].mean(0))
anm = L.analyze_sigma(Sm)
print("medium (unsymmetrized) diffusive:", anm["diffusive"], " maxoff", anm["maxoff"], " minrow", anm["minrow"])
ex, exse = L.jackknife(lambda X: np.array([L.exchangeable_baseline(X)[k] for k in ("a", "eps", "sup")]), Sgm)
exb = L.exchangeable_baseline(Sm)
print("medium (exchangeable-symmetrized): coupling a = %.6g +- %.2g, leak = %.6g +- %.2g, sup contrast = %.6g +- %.2g"
      " attained at %s" % (ex[0], exse[0], ex[1], exse[1], ex[2], exse[2], exb["argsup"]))
print("   sup contrast by region size:", exb["by_size"])
supu, supuse = L.jackknife(lambda X: max(L.analyze_sigma(X)["r_all"].values()), Sgm)
print("   unsymmetrized sup over regions: %.6g +- %.2g" % (supu, supuse))
out["medium"] = dict(Sigma=Sm.tolist(), Sigma_se=Smse.tolist(), a=[ex[0], exse[0]], eps=[ex[1], exse[1]],
                     sup=[ex[2], exse[2]], argsup=list(exb["argsup"]), by_size=exb["by_size"],
                     sup_unsym=[supu, supuse], att=rm["att_prob"].mean(0).tolist(),
                     diffusive_unsym=anm["diffusive"])

with open(os.path.join(HERE, "s2_full_output.json"), "w") as f:
    json.dump(out, f, indent=1, default=float)
print("\nwall time %.1f s" % (time.time() - t0))
