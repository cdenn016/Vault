"""Second formulation (brute-force replicas with sampled noises), the negative control, and memory
sensitivity to the reading of the initial laws.

Expectations (before running):
 (a) shared-world brute-force replicas reproduce the Rao-Blackwellized Sigma^c of s2 within ~3 SE;
 (b) NEGATIVE CONTROL, independent world paths in the two replicas: the estimator returns the
     unconditional covariance, every entry inflated by the world common mode (>= Q = 0.05 since
     e(t) loads on -w_{t-1} with coefficient one); the leaks collapse by a factor ~1+c*sum(eps)
     (~20) and the whole population V becomes the highest-contrast region, far above r(A);
 (c) brute-force Cov(e_i,e_j|eta,v_S) ~ 3.8e-5 (weak check, SE ~1e-5);
 (d) memory: the stationary limit ~0.0257 nats does not depend on the initial-law reading; the
     transient peak at t=2 from the deterministic start depends on the initial covariance P0.
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


def bruteforce(p, B, TB, TA, seed, share_world=True, share_vS=False):
    """Two replicas; independent attention, private noises; world shared or not."""
    rng = np.random.default_rng(seed)
    m = L.Model(p)
    N, A, Rs, wmsg = m.N, m.A, m.Rs, m.wmsg
    F, Q, Rc, qc, gam = p["F"], p["Q"], p["Rc"], p["qc"], p["gamma"]
    recv = np.array(m.receivers)
    s0 = Q / (1 - F ** 2)
    eta = [rng.normal(0, np.sqrt(s0), B)]
    eta.append(eta[0] if share_world else rng.normal(0, np.sqrt(s0), B))
    P0 = L.world_cov(p)
    st = []
    for r in range(2):
        st.append(dict(mean=np.zeros((B, N, 2)), Pm=np.broadcast_to(P0, (B, N, 2, 2)).copy(),
                       read=np.zeros((B, N, N)), sprev=np.zeros((B, N))))
    D_sum = np.zeros((N, N))
    E_sum = [np.zeros((N, N)), np.zeros((N, N))]
    n = 0
    for t in range(TB + TA):
        w = [rng.normal(0, np.sqrt(Q), B)]
        w.append(w[0] if share_world else rng.normal(0, np.sqrt(Q), B))
        vS = rng.normal(0, np.sqrt(Rs[0]), B)
        es = []
        for r in range(2):
            S_ = st[r]
            et = S_["mean"][:, :, 0] - eta[r][:, None]
            es.append(et)
            v = rng.normal(size=(B, N)) * np.sqrt(Rs)[None, :]
            if share_vS:
                v[:, 0] = vS
            s = eta[r][:, None] + v
            nu = rng.normal(size=(B, N, N)) * np.sqrt(Rc)
            y = S_["sprev"][:, None, :] + nu  # message from j to a
            invPm = L.inv2(S_["Pm"])
            Lam = invPm.copy()
            Lam[..., 0, 0] += 1 / Rs
            Lam[..., 1, 1] += S_["read"] @ wmsg
            Pp = L.inv2(Lam)
            mm = S_["mean"]
            innov0 = (s - mm[:, :, 0]) / Rs[None, :]
            innov1 = (S_["read"] * wmsg[None, None, :] * (y - mm[:, :, 1][:, :, None])).sum(-1)
            mp = mm + Pp[..., :, 0] * innov0[..., None] + Pp[..., :, 1] * innov1[..., None]
            S_["mean"] = mp @ A.T + rng.normal(size=(B, N, 2)) * np.sqrt(qc)
            S_["sprev"] = s
            Pmn = A @ Pp @ A.T + m.Qx
            Ln = L.inv2(Pmn)
            ld = np.log(Pmn[..., 0, 0] * Pmn[..., 1, 1] - Pmn[..., 0, 1] ** 2)
            a_ = Ln[:, recv, 0, 0] + 1 / Rs[recv][None, :]
            det = a_[..., None] * (Ln[:, recv, 1, 1][..., None] + m.sig[None]) - Ln[:, recv, 0, 1][..., None] ** 2
            logit = gam * 0.5 * (ld[:, recv, None] + np.log(det))
            k = np.argmax(logit + rng.gumbel(size=logit.shape), -1)
            rn = np.zeros((B, N, N))
            for ri, a in enumerate(recv):
                rn[:, a, :] = m.Ind[ri][k[:, ri]]
            S_["read"] = rn
            S_["Pm"] = Pmn
        if t >= TB:
            D = es[0] - es[1]
            D_sum += D.T @ D
            for r in range(2):
                E_sum[r] += es[r].T @ es[r]
            n += B
        eta[0] = F * eta[0] + w[0]
        eta[1] = eta[0] if share_world else F * eta[1] + w[1]
    return 0.5 * D_sum / n, (E_sum[0] + E_sum[1]) / (2 * n)


ref = np.array(json.load(open(os.path.join(HERE, "s2_full_output.json")))["item2"]["Sigma"])

# ---- (a) second formulation: brute-force shared-world replicas, 4 independent batches for SE
ests = []
for b in range(4):
    Sb, Eb = bruteforce(p, B=2000, TB=60, TA=150, seed=900 + b, share_world=True)
    ests.append(Sb)
ests = np.array(ests)
Sbf = ests.mean(0)
Sbf_se = ests.std(0, ddof=1) / 2
print("=== (a) brute-force shared-world replicas: (1/2)E[(e1-e2)(e1-e2)^T] ===")
print(Sbf, "\nSE (4 batches):\n", Sbf_se)
print("Rao-Blackwellized Sigma^c (s2):\n", ref)
z = (Sbf - ref) / Sbf_se
print("z-scores:\n", z)
an_bf = L.analyze_sigma(Sbf)
print("brute-force r(A) = %.4f (RB: 5.37234)" % an_bf["rA"])
rAs = [L.analyze_sigma(X)["rA"] for X in ests]
print("brute-force r(A) per batch:", rAs, " SE", np.std(rAs, ddof=1) / 2)
out["bruteforce"] = dict(Sigma=Sbf.tolist(), se=Sbf_se.tolist(), maxabsz=float(np.abs(z).max()),
                         rA=float(an_bf["rA"]), rA_se=float(np.std(rAs, ddof=1) / 2))
print("[%.1fs]" % (time.time() - t0))

# ---- (b) negative control: independent world paths in the two replicas
Snc, Enc = bruteforce(p, B=2000, TB=60, TA=150, seed=950, share_world=False)
print("\n=== (b) NEGATIVE CONTROL: independent world paths ===")
print("replica estimator:\n", Snc)
print("one-replica second moment E[e e^T] (unconditional):\n", Enc)
an_nc = L.analyze_sigma(Snc)
print("diffusive:", an_nc["diffusive"], " maxoff", an_nc["maxoff"], " minrow", an_nc["minrow"])
print("leaks:", an_nc["eps"], "\nr(A) = %.4f ; whole population r(V) = %.4f ; largest other region %s" % (
    an_nc["rA"], an_nc["r_all"][(0, 1, 2, 3, 4)], an_nc["max_other"]))
out["negative_control"] = dict(Sigma=Snc.tolist(), diffusive=an_nc["diffusive"], eps=an_nc["eps"].tolist(),
                               rA=float(an_nc["rA"]), rV=float(an_nc["r_all"][(0, 1, 2, 3, 4)]),
                               max_other=[list(an_nc["max_other"][0]), float(an_nc["max_other"][1])])
print("[%.1fs]" % (time.time() - t0))

# ---- (c) brute-force check of item 4 (replicas share eta and v_S)
c4 = []
for b in range(3):
    Sb, _ = bruteforce(p, B=2000, TB=60, TA=150, seed=970 + b, share_world=True, share_vS=True)
    iu = np.triu_indices(4, 1)
    c4.append(Sb[1:, 1:][iu].mean())
print("\n=== (c) brute-force Cov(e_i,e_j|eta,v_S), avg over member pairs: %.3g +- %.2g (RB: 3.78e-5)" % (
    np.mean(c4), np.std(c4, ddof=1) / np.sqrt(3)))
out["bruteforce_item4"] = [float(np.mean(c4)), float(np.std(c4, ddof=1) / np.sqrt(3))]
print("[%.1fs]" % (time.time() - t0))


# ---- (d) memory sensitivity to the initial law readings
def member_AT(p, B, T, seed, P0):
    rng = np.random.default_rng(seed)
    m = L.Model(p)
    N, A, Rs, wmsg = m.N, m.A, m.Rs, m.wmsg
    recv = np.array(m.receivers)
    Pm = np.broadcast_to(P0, (B, N, 2, 2)).copy()
    read = np.zeros((B, N, N))
    AT = np.zeros((B, T, 4, 2, 2))
    for t in range(T):
        invPm = L.inv2(Pm)
        Lam = invPm.copy()
        Lam[..., 0, 0] += 1 / Rs
        Lam[..., 1, 1] += read @ wmsg
        Pp = L.inv2(Lam)
        AT[:, t] = (A @ (Pp @ invPm))[:, 1:5]
        Pmn = A @ Pp @ A.T + m.Qx
        Ln = L.inv2(Pmn)
        ld = np.log(Pmn[..., 0, 0] * Pmn[..., 1, 1] - Pmn[..., 0, 1] ** 2)
        a_ = Ln[:, recv, 0, 0] + 1 / Rs[recv][None, :]
        det = a_[..., None] * (Ln[:, recv, 1, 1][..., None] + m.sig[None]) - Ln[:, recv, 0, 1][..., None] ** 2
        logit = p["gamma"] * 0.5 * (ld[:, recv, None] + np.log(det))
        k = np.argmax(logit + rng.gumbel(size=logit.shape), -1)
        rn = np.zeros((B, N, N))
        for ri, a in enumerate(recv):
            rn[:, a, :] = m.Ind[ri][k[:, ri]]
        read, Pm = rn, Pmn
    return AT


def mem_curve(AT, t_start, Sx0):
    """I(y_{t+1}; y_{t_start:t-1} | y_t) along each path for t >= t_start, initial covariance Sx0."""
    B, T = AT.shape[:2]
    Pv = np.zeros(8)
    Pv[[0, 2, 4, 6]] = 0.25
    Sx = np.broadcast_to(Sx0, (B, 8, 8)).copy() if Sx0.ndim == 2 else Sx0.copy()
    Sf = Sx.copy()
    I = np.zeros((B, T - t_start))
    eye = np.eye(8)
    for t in range(t_start, T):
        At = np.zeros((B, 8, 8))
        for mm in range(4):
            At[:, 2 * mm:2 * mm + 2, 2 * mm:2 * mm + 2] = AT[:, t, mm]
        VY0 = np.einsum("i,bij,j->b", Pv, Sx, Pv)
        cov = np.einsum("i,bij,j->b", Pv, At @ Sx, Pv)
        Sxn = At @ Sx @ At.transpose(0, 2, 1) + eye
        VY1 = np.einsum("i,bij,j->b", Pv, Sxn, Pv)
        Vc = np.where(VY0 > 1e-300, VY1 - cov ** 2 / np.where(VY0 > 1e-300, VY0, 1), VY1)
        sP = Sf @ Pv
        s = sP @ Pv
        upd = np.where((s > 1e-300)[:, None, None], Sf - sP[:, :, None] * sP[:, None, :] /
                       np.where(s > 1e-300, s, 1)[:, None, None], Sf)
        Sf = At @ upd @ At.transpose(0, 2, 1) + eye
        Vf = np.einsum("i,bij,j->b", Pv, Sf, Pv)
        I[:, t - t_start] = 0.5 * np.log(Vc / Vf)
        Sx = Sxn
    return I


print("\n=== (d) memory: sensitivity to the initial-law readings ===")
Bm, Tm, Tb = 2000, 120, 60
P0w = L.world_cov(p)
P0s = L.exact_fixedS(p)["PmM"]  # members' stationary prior covariance under {S}
res_d = {}
for lab, P0 in (("deterministic start, P0 = world stationary covariance (primary)", P0w),
                ("deterministic start, P0 = members' {S}-stationary prior covariance", P0s)):
    AT = member_AT(p, Bm, Tm, 31, P0)
    I = mem_curve(AT, 0, np.zeros((8, 8)))
    mI = I.mean(0)
    k = int(np.argmax(mI))
    print(f"{lab}: path-avg t=0..6 {np.round(mI[:7], 6)}, sup={mI[k]:.6f} at t={k}, late={mI[-1]:.6f}")
    res_d[lab] = dict(curve=mI[:10].tolist(), sup=float(mI[k]), tsup=k, late=float(mI[-1]))
# stationary initial law: path-conditional versus moment-matched
AT = member_AT(p, Bm, Tm, 32, P0w)
Pv = np.zeros(8)
Sx = np.zeros((Bm, 8, 8))
for t in range(Tb):
    At = np.zeros((Bm, 8, 8))
    for mm in range(4):
        At[:, 2 * mm:2 * mm + 2, 2 * mm:2 * mm + 2] = AT[:, t, mm]
    Sx = At @ Sx @ At.transpose(0, 2, 1) + np.eye(8)
I_pc = mem_curve(AT, Tb, Sx)
I_mm = mem_curve(AT, Tb, Sx.mean(0))
for lab, I in (("stationary law, path-conditional (primary)", I_pc), ("stationary law, moment-matched Gaussian", I_mm)):
    mI = I.mean(0)
    k = int(np.argmax(mI))
    print(f"{lab}: path-avg by history length 0..6 {np.round(mI[:7], 6)}, sup={mI[k]:.6f} at {k}, late={mI[-1]:.6f}")
    res_d[lab] = dict(curve=mI[:10].tolist(), sup=float(mI[k]), tsup=k, late=float(mI[-1]))
out["memory_sensitivity"] = res_d

with open(os.path.join(HERE, "s4_checks_output.json"), "w") as f:
    json.dump(out, f, indent=1, default=float)
print("\nwall time %.1f s" % (time.time() - t0))
