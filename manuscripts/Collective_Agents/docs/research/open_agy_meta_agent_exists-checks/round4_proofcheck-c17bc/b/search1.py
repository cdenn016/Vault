"""Random search over instances satisfying every hypothesis of C17b.

Construction (process-law reading of O2'): A, E and the noise factor intertwine the S_n action
P_sigma (x) I on C with the identity on V\\C, so the law of the processes (z, xi) is invariant.
O1 is imposed exactly by tuning one cross-noise parameter per outside agent (Sigma_z is affine in it).
O3: every C-loading of y is kappa^(r) (x) pattern with kappa^(r) in span{1} + W, dim W <= n-2.
Noises v = B nu + w independent of xi (convention). Filters: Pi_eff diffusive; second part also Pi^c diffusive.
Usage: python search1.py <mode> <seed> <count>; mode in {ok, barely, fullW}.
fullW violates O3 (dim W = n-1) as a negative control."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

mode = sys.argv[1] if len(sys.argv) > 1 else "ok"
seed = int(sys.argv[2]) if len(sys.argv) > 2 else 0
count = int(sys.argv[3]) if len(sys.argv) > 3 else 1500
rng = np.random.default_rng(seed)


def blockrow_ones(n, X):  # kron(ones(1,n), X)
    return np.kron(np.ones((1, n)), X)


def blockcol_ones(n, X):  # kron(ones(n,1), X)
    return np.kron(np.ones((n, 1)), X)


def gen():
    n = int(rng.choice([2, 3, 4]))
    d = int(rng.choice([1, 2])); dx = int(rng.choice([1, 2]))
    nout = int(rng.choice([0, 1, 2])); do = int(rng.choice([1, 2])); dxo = 1
    coupled = bool(rng.random() < 0.6)
    # --- dynamics and noise, intertwining structure
    A_CC = comm(n, rng.normal(size=(d, d)), rng.normal(size=(d, d)) * rng.uniform(0, 0.6))
    E_CC = comm(n, rng.normal(size=(d, dx)), rng.normal(size=(d, dx)) * rng.uniform(0, 0.6))
    B_CC = comm(n, rng.normal(size=(dx, dx)), rng.normal(size=(dx, dx)) * rng.uniform(0, 1.5))
    no, nxo = nout * do, nout * dxo
    A_oo = rng.normal(size=(no, no)); E_oo = rng.normal(size=(no, nxo)); B_oo = rng.normal(size=(nxo, nxo))
    c = 1.0 if coupled else 0.0
    A_Co = c * blockcol_ones(n, rng.normal(size=(d, no))) * 0.5
    A_oC = c * np.vstack([blockrow_ones(n, rng.normal(size=(do, d))) for _ in range(nout)]) * 0.5 if nout else np.zeros((0, n * d))
    E_Co = c * blockcol_ones(n, rng.normal(size=(d, nxo))) * 0.5
    E_oC = c * np.vstack([blockrow_ones(n, rng.normal(size=(do, dx))) for _ in range(nout)]) * 0.5 if nout else np.zeros((0, n * dx))
    B_Co = c * blockcol_ones(n, rng.normal(size=(dx, nxo))) * 0.5
    B_oC = c * np.vstack([blockrow_ones(n, rng.normal(size=(dxo, dx))) for _ in range(nout)]) * 0.5 if nout else np.zeros((0, n * dx))
    A = np.block([[A_CC, A_Co], [A_oC, A_oo]]) if nout else A_CC
    E = np.block([[E_CC, E_Co], [E_oC, E_oo]]) if nout else E_CC
    Bf = np.block([[B_CC, B_Co], [B_oC, B_oo]]) if nout else B_CC
    A = A * rng.uniform(0.2, 0.9) / max(abs(np.linalg.eigvals(A)))
    Q0 = Bf @ Bf.T
    nzC, nxC = n * d, n * dx
    s = rng.normal(size=d); so = rng.normal(size=do)
    S = np.zeros((n + nout, nzC + no))
    S[:n, :nzC] = np.kron(np.eye(n), s[None, :])
    for k in range(nout):
        S[n + k, nzC + k * do: nzC + (k + 1) * do] = so
    # --- impose O1: Cov(s^T z_1, so^T z_ok) = 0 by tuning t_k in Q(t) = Q0 + sum t_k X_k
    Q = Q0
    if mode == "noO1":
        if nout == 0 or not coupled:
            return None
    if nout and mode != "noO1":
        Xs = []
        for k in range(nout):
            X = np.zeros_like(Q0)
            u = blockcol_ones(n, rng.normal(size=(dx, dxo)))
            X[:nxC, nxC + k * dxo: nxC + (k + 1) * dxo] = u
            X = X + X.T
            Xs.append(X)
        def cross(Qm):
            Sz = lyap(A, E @ Qm @ E.T)
            Se = S @ Sz @ S.T
            return Se[0, n:].copy()
        c0 = cross(Q0)
        J = np.column_stack([cross(Q0 + Xs[k]) - c0 for k in range(nout)])
        t = np.linalg.solve(J, -c0)
        Q = Q0 + sum(t[k] * Xs[k] for k in range(nout))
        if np.linalg.eigvalsh(Q).min() < -1e-10:
            return None
    # --- observation y = G z + H xi + v, C-loadings kappa^(r) (x) pattern
    p = int(rng.choice([1, 2, 3]))
    if mode in ("ok", "noO1"):
        w = int(rng.integers(0, n - 1))
    elif mode == "barely":
        w = n - 2
    else:  # fullW: violates O3
        w = n - 1
    PD = np.eye(n) - np.ones((n, n)) / n
    Wb = np.linalg.qr(PD @ rng.normal(size=(n, w)))[0][:, :w] if w > 0 else np.zeros((n, 0))
    R = int(rng.integers(1, 4))
    G_C = np.zeros((p, nzC)); H_C = np.zeros((p, nxC))
    for r in range(R):
        kap = rng.normal() * np.ones(n) + (Wb @ rng.normal(size=w) if w else 0.0)
        G_C += np.outer(rng.normal(size=p), np.kron(kap, rng.normal(size=d)))
        H_C += np.outer(rng.normal(size=p), np.kron(kap, rng.normal(size=dx))) * rng.uniform(0, 1)
    G = np.hstack([G_C, rng.normal(size=(p, no)) * rng.uniform(0, 1)]) if nout else G_C
    H = np.hstack([H_C, rng.normal(size=(p, nxo)) * rng.uniform(0, 1)]) if nout else H_C
    Br = rng.normal(size=(p, p))
    Rv = (Br @ Br.T + 0.05 * np.eye(p)) * 10 ** rng.uniform(-1.5, 2.5)
    return dict(n=n, d=d, dx=dx, nout=nout, do=do, A=A, E=E, Q=Q, G=G, H=H, Rv=Rv, S=S, Wb=Wb, w=w, coupled=coupled)


t0 = time.time()
stats = dict(gen=0, valid=0, eff_diff=0, both_diff=0, viol_r=0, viol_xout=0, viol_xin=0)
worst = dict(eig_res=0.0, eig_res_eff=0.0, xin_eff_vs_1a=0.0, O1=0.0, ident=0.0, rel_r_excess=-np.inf,
             xout_gap_min=np.inf, xin_excess=-np.inf, sz_quad=0.0)
example = None
while stats["gen"] < count and time.time() - t0 < 25:
    inst = gen()
    stats["gen"] += 1
    if inst is None:
        continue
    A, E, Q, G, H, Rv, S = (inst[k] for k in ("A", "E", "Q", "G", "H", "Rv", "S"))
    n, nout = inst["n"], inst["nout"]
    Sz = lyap(A, E @ Q @ E.T)
    err, Szq, im = smoother_cov(A, E, Q, G, H, Rv, M=1024)
    worst["sz_quad"] = max(worst["sz_quad"], np.abs(Szq - Sz).max() / np.abs(Sz).max())
    Sc = S @ err @ S.T; Se = S @ Sz @ S.T
    Sc = (Sc + Sc.T) / 2; Se = (Se + Se.T) / 2
    if np.linalg.eigvalsh(Sc).min() <= 1e-10 * np.abs(Se).max():
        continue
    stats["valid"] += 1
    Pc = np.linalg.inv(Sc); Pe = np.linalg.inv(Se)
    C = list(range(n))
    worst["O1"] = max(worst["O1"], np.abs(Se[:n, n:]).max() / np.abs(Se).max() if nout else 0.0)
    # f in D_C perp W
    PD = np.eye(n) - np.ones((n, n)) / n
    M = np.column_stack([np.ones(n), inst["Wb"]])
    Uq = np.linalg.qr(np.column_stack([M, np.eye(n)]))[0]
    Fbasis = Uq[:, M.shape[1]:n]  # orthonormal basis of (span{1} + W)^perp
    if Fbasis.shape[1] == 0:
        f = None
    else:
        f = np.zeros(n + nout); f[:n] = Fbasis[:, 0]
        alpha = f @ Se @ f
        sc_ = np.abs(Se).max()
        worst["eig_res"] = max(worst["eig_res"], np.abs(Sc @ f - alpha * f).max() / sc_)
        worst["eig_res_eff"] = max(worst["eig_res_eff"], np.abs(Se @ f - alpha * f).max() / sc_)
        worst["cond_max"] = max(worst.get("cond_max", 0.0), np.linalg.cond(Sc))
    if not is_diffusive(Pe):
        continue
    stats["eff_diff"] += 1
    xin_e, xout_e, id_e, _, _ = rates(Pe, C)
    if f is not None:
        worst["xin_eff_vs_1a"] = max(worst["xin_eff_vs_1a"], abs(xin_e - 1 / alpha) * alpha)
    xout = np.ones(n) @ Pc[:n, :n] @ np.ones(n) / n
    if xout < xout_e * (1 - 1e-9):
        stats["viol_xout"] += 1
    worst["xout_gap_min"] = min(worst["xout_gap_min"], (xout - xout_e) / xout_e)
    if not is_diffusive(Pc):
        continue
    stats["both_diff"] += 1
    key = f"bd_n{n}_out{nout}_{'cpl' if inst['coupled'] and nout else 'dec'}_w{inst['w']}_d{inst['d']}"
    stats[key] = stats.get(key, 0) + 1
    xin, xout2, idc, _, _ = rates(Pc, C)
    worst["ident"] = max(worst["ident"], idc, id_e)
    r, r_e = xin / xout, xin_e / xout_e
    rel = (r - r_e) / r_e
    if rel > worst["rel_r_excess"]:
        worst["rel_r_excess"] = rel
        example = dict(n=n, d=inst["d"], dx=inst["dx"], nout=nout, w=inst["w"], coupled=inst["coupled"],
                       r=r, r_eff=r_e, xin=xin, xin_eff=xin_e, xout=xout2, xout_eff=xout_e)
    if rel > 1e-8:
        stats["viol_r"] += 1
    if f is not None and xin > (1 / alpha) * (1 + 1e-8):
        stats["viol_xin"] += 1
        print("  xin>1/alpha flagged: rel excess", (xin - 1 / alpha) * alpha, " cond(Sc)", np.linalg.cond(Sc), " alpha/max|Se|", alpha / np.abs(Se).max())
    if f is not None:
        worst["xin_excess"] = max(worst["xin_excess"], (xin - 1 / alpha) * alpha)

print(f"mode={mode} seed={seed} elapsed={time.time()-t0:.1f}s")
print("counts:", stats)
for k, v in worst.items():
    print(f"  {k}: {v:.3e}")
print("instance attaining max (r - r_eff)/r_eff among admissible:", example)
