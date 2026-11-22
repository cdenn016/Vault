r"""Counterexample computations for Theorem O and Proposition D (memoryless Setting G instances).

World eta in R^m:  eta_{t+1} = F eta_t + sum_j Bcol_j a_{j,t} + w_t,  w ~ N(0, qw I).
Acts:              a_{j,t} = sum_l G[j,l] xi_{l,t}            (Gamma = 0; private-noise loading G)
Agent i (scalar contrast coordinate = prior error about h_i^T eta_{t+1}):
                   mu_{i,t+1} = h_i^T F eta_t + sum_l E[i,l] xi_{l,t},   e_i = mu_{i,t+1} - h_i^T eta_{t+1}.
Private process:   z_{t+1} = E xi_t (scalar per agent, S = I).
Sigma^c is computed DIRECTLY as Cov(e_{tau+1} | eta_{0..T+1}) (not through Lemma M).
N_eff: the act term in eta is replaced by an independent forcing with the act law.
Contrast per def:col-contrast; baseline per def:col-baseline clause (c) with mean coupling and
uniform mean leak (no declared geometry, no declared mechanism), sup over sizes 2..N.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
from itertools import combinations

T, tau = 6, 3

def sigma_c(F, Bcols, G, E, hs, qw, null):
    m = F.shape[0]
    N, nxi = E.shape
    na = G.shape[0]
    # noise layout: eta0 (m) | w_t (m) | xi_t (nxi) | forcing_t (na)
    blocks = [m] + [m, nxi, na] * (T + 1)
    Ntot = sum(blocks)
    def sel(t, kind):
        start = m + t * (m + nxi + na) + {"w": 0, "xi": m, "fo": m + nxi}[kind]
        size = {"w": m, "xi": nxi, "fo": na}[kind]
        M = np.zeros((size, Ntot)); M[:, start:start + size] = np.eye(size)
        return M
    eta = [np.hstack([np.eye(m), np.zeros((m, Ntot - m))])]
    mus = []
    Bmat = np.column_stack(Bcols)            # m x na
    Va = G @ G.T                             # act covariance (xi ~ N(0,I))
    La = np.linalg.cholesky(Va + 1e-300 * np.eye(na)) if np.all(np.linalg.eigvalsh(Va) > 0) else None
    for t in range(T + 1):
        xi = sel(t, "xi"); w = np.sqrt(qw) * sel(t, "w")
        a = G @ xi
        if null:
            forcing = La @ sel(t, "fo")      # independent, same law as the act
            eta_next = F @ eta[t] + Bmat @ forcing + w
        else:
            eta_next = F @ eta[t] + Bmat @ a + w
        mu = np.vstack([hs[i] @ F @ eta[t] + E[i] @ xi for i in range(N)])
        mus.append(mu)
        eta.append(eta_next)
    e = mus[tau] - np.vstack([hs[i] @ eta[tau + 1] for i in range(N)])
    Ly = np.vstack(eta)
    Sxx = e @ e.T; Sxy = e @ Ly.T; Syy = Ly @ Ly.T
    return Sxx - Sxy @ np.linalg.solve(Syy, Sxy.T)

def is_diffusive(Pi, tol=1e-10):
    off = Pi - np.diag(np.diag(Pi))
    return bool(np.all(off <= tol) and np.all(Pi.sum(1) >= -tol))

def rates(Pi, C):
    N = Pi.shape[0]
    C = list(C); n = len(C)
    eps = Pi.sum(1)
    a = -(Pi - np.diag(np.diag(Pi)))
    LC = np.zeros((n, n))
    for x, i in enumerate(C):
        for y, j in enumerate(C):
            if i != j:
                LC[x, y] = -a[i, j]; LC[x, x] += a[i, j]
    Q = np.diag(eps[C]) + LC
    U = np.linalg.svd(np.ones((n, 1)))[0][:, 1:]          # basis of 1^perp
    xin = np.min(np.linalg.eigvalsh(U.T @ Q @ U))
    phi = np.zeros(N); phi[C] = 1 / np.sqrt(n)
    xout = phi @ Pi @ phi
    return xin, xout, xin / xout, eps[C]

def baseline_c(Pi):
    N = Pi.shape[0]
    a = -(Pi - np.diag(np.diag(Pi)))
    abar = a[np.triu_indices(N, 1)].mean()
    ebar = Pi.sum(1).mean()
    Phom = ebar * np.eye(N) + abar * (N * np.eye(N) - np.ones((N, N)))
    return max(rates(Phom, range(k))[2] for k in range(2, N + 1)), abar, ebar

def report(name, F, Bcols, G, E, hs, qw, C, r0=None):
    print(f"===== {name} =====")
    print("Cov(z) = E E^T =\n", np.round(E @ E.T, 6))
    print("Cov(z_{t+1}, xi_t) = E =\n", np.round(E, 6))
    out = {}
    for null in (False, True):
        S = sigma_c(F, Bcols, G, E, hs, qw, null)
        Pi = np.linalg.inv(S)
        tag = "N_eff" if null else "full"
        dif = is_diffusive(Pi)
        xin, xout, r, epsC = rates(Pi, C)
        rb, abar, ebar = baseline_c(Pi)
        print(f"[{tag}] Sigma^c =\n{np.round(S, 6)}\n[{tag}] Pi^c =\n{np.round(Pi, 6)}")
        print(f"[{tag}] diffusive={dif}  xi_in(C)={xin:.6f} xi_out(C)={xout:.6f} r(C)={r:.6f} "
              f"leaks on C={np.round(epsC, 6)} baseline(c)={rb:.6f} (abar={abar:.6f}, ebar={ebar:.6f})")
        if r0 is not None:
            coll = (r >= r0) and (r0 > max(epsC.max() / epsC.mean(), rb))
            print(f"[{tag}] collective at r0={r0}: {coll}")
        out[tag] = (S, Pi, r)
    return out

F1 = np.array([[0.5]])
h1 = [np.array([1.0])]

# --- Theorem O, literal (O2): z_1 = xi_1, z_2 = -xi_2 (member 2's own-act effect model has the wrong sign),
#     acts a_i = xi_i with true effect +1 each; tilde-y loads (1,1) on xi_C, nothing on z  => W = {0}.
E = np.diag([1.0, -1.0]); G = np.eye(2)
report("Thm O counterexample, V = C (n=2)", F1, [np.array([1.0]), np.array([1.0])], G, E, h1 * 2, 1.0, [0, 1])
# identity check at the failing step: Cov(u_f,t+1, tilde-y_t) vs (h0-h1)(kappa^T f)
f = np.array([1, -1]) / np.sqrt(2); kappa = np.array([1.0, 1.0])
print("noise identity: LHS Cov(f^T z_{t+1}, kappa^T xi_t) =", f @ E @ kappa,
      "  RHS (h0-h1)(kappa^T f) with h0=E[0,0], h1=E[0,1]:", (E[0, 0] - E[0, 1]) * (kappa @ f))

# same with three isolated non-acting agents (O1 holds), level r0 = 2
E5 = np.diag([1.0, -1.0, 1.0, 1.0, 1.0]); G5 = np.hstack([np.eye(2), np.zeros((2, 3))])
report("Thm O counterexample, V = C + 3 isolated (N=5)", F1, [np.array([1.0]), np.array([1.0])],
       G5, E5, h1 * 5, 1.0, [0, 1], r0=2.0)

# --- Theorem O, strengthened (O2'): jointly equivariant relay E = [[p,q],[q,p]], equal act loading -g on
#     own sensing noise; two isolated agents. Shows the baseline moves under N_eff.
p, q = (np.sqrt(5) + 1) / 2, (np.sqrt(5) - 1) / 2; g = np.sqrt(0.75)
E4 = np.zeros((4, 4)); E4[:2, :2] = [[p, q], [q, p]]; E4[2, 2] = E4[3, 3] = 1.0
G4 = np.hstack([-g * np.eye(2), np.zeros((2, 2))])
report("Thm O strengthened hypotheses, baseline shift (N=4)", F1, [np.array([1.0]), np.array([1.0])],
       G4, E4, h1 * 4, 1.0, [0, 1], r0=1.3)

# --- Proposition D (a): uncorrelated, interchangeable private law, opposite act gains on own sensing noise
#     (agents' priors ignore acts): z_i = F*xi_i... here E = diag(0.5,0.5), acts a = (+g, -g) xi.
Ed = 0.5 * np.eye(2); Gd = np.diag([1.0, -1.0])
outa = report("Prop D (a): opposite-sign loadings", F1, [np.array([1.0]), np.array([1.0])], Gd, Ed, h1 * 2, 1.0, [0, 1])
# --- Proposition D (b): two world components, member i acts on and tracks component i, true effect model
F2 = 0.5 * np.eye(2)
outb = report("Prop D (b): separate components", F2, [np.array([1.0, 0.0]), np.array([0.0, 1.0])],
              np.eye(2), np.eye(2), [np.array([1.0, 0.0]), np.array([0.0, 1.0])], 1.0, [0, 1])
for nm, o in (("(a)", outa), ("(b)", outb)):
    S, Pi, _ = o["full"]
    corr = o["N_eff"][0] - S          # = K K^T by Lemma M
    print(f"Prop D {nm}: correction KK^T =\n{np.round(corr, 6)}  Sigma^c_12 = {S[0,1]:.6f}, "
          f"-|k_1|^2 = {-corr[0,0]:.6f}, k_1.k_2 = {corr[0,1]:.6f}")
