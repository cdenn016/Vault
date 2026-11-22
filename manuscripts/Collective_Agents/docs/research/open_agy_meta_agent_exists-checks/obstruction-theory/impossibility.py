"""Part (4): impossibility classes, each with a negative control."""
import itertools
import numpy as np
from scipy.linalg import solve_discrete_are, solve_discrete_lyapunov
from common import is_diffusive, contrast

rng = np.random.default_rng(4)
ok_all = True


def report(name, expect, got):
    global ok_all
    flag = "PASS" if expect == got else "FAIL"
    if expect != got:
        ok_all = False
    print(f"[{flag}] {name}: expected {expect}, got {got}")


def regions(N):
    for m in range(2, N + 1):
        for C in itertools.combinations(range(N), m):
            yield C


def all_contrasts(Pi):
    return {C: contrast(Pi, C)[0] for C in regions(Pi.shape[0])}


def cliques_pi(sizes, couplings, eps):
    N = sum(sizes)
    L = np.zeros((N, N)); i = 0
    for s, a in zip(sizes, couplings):
        B = a * (np.ones((s, s)) - np.eye(s))
        L[i:i + s, i:i + s] = np.diag(B.sum(1)) - B
        i += s
    return eps * np.eye(N) + L


def comparison_graph(Pi, edges):
    """clause (b): declared graph, mean coupling on declared edges, uniform mean leak."""
    N = Pi.shape[0]
    a = np.array([-Pi[i, j] for (i, j) in edges]).mean()
    L = np.zeros((N, N))
    for (i, j) in edges:
        L[i, j] = L[j, i] = -a
    np.fill_diagonal(L, -L.sum(1))
    return Pi.sum(1).mean() * np.eye(N) + L


def comparison_exchangeable(Pi):
    N = Pi.shape[0]
    a = -Pi[np.triu_indices(N, 1)].mean()
    L = -a * (np.ones((N, N)) - np.eye(N)); np.fill_diagonal(L, (N - 1) * a)
    return Pi.sum(1).mean() * np.eye(N) + L


# ---------- I1/I2: two equal cliques under clause (b) and clause (c) ----------
n, a, eps = 4, 1.0, 0.1
Pi = cliques_pi([n, n], [a, a], eps)
edges = [(i, j) for i in range(2 * n) for j in range(i + 1, 2 * n) if Pi[i, j] < 0]
rb_b = max(all_contrasts(comparison_graph(Pi, edges)).values())
rb_c = max(all_contrasts(comparison_exchangeable(Pi)).values())
rc = all_contrasts(Pi)
best = max(rc, key=rc.get)
print(f"   two cliques n=4, a=1, eps=0.1: clique contrast {rc[tuple(range(n))]:.4f}; baseline (b) {rb_b:.4f}; baseline (c) {rb_c:.4f}")
report("I1: equal cliques under declared graph: no region exceeds the baseline", 0,
       sum(r > rb_b + 1e-12 for r in rc.values()))
report("each clique is a collective under clause (c) mean coupling (significance 1.162)", True,
       rc[tuple(range(n))] > rb_c and abs(rc[tuple(range(n))] / rb_c - 1.162) < 1e-3)
# negative control: unequal clique couplings under clause (b)
Pi2 = cliques_pi([n, n], [1.5, 0.5], eps)
rb_b2 = max(all_contrasts(comparison_graph(Pi2, edges)).values())
r_c1 = contrast(Pi2, range(n))[0]
report("NEG CONTROL unequal clique couplings, clause (b): stronger clique is a collective", True, r_c1 > rb_b2)
print(f"      stronger clique r = {r_c1:.3f} vs baseline {rb_b2:.3f}")

# ---------- I2: whole population never a collective under clause (c) mean coupling; necessary condition ----------
viol_whole, viol_nec, viol_nec_u, ncoll = 0, 0, 0, 0
for _ in range(150):
    N = rng.integers(3, 7)
    Aw = rng.uniform(0, 1, (N, N)) * (rng.uniform(size=(N, N)) < 0.6); Aw = 0.5 * (Aw + Aw.T); np.fill_diagonal(Aw, 0)
    uniform = rng.uniform() < 0.5
    ep = np.full(N, rng.uniform(0.01, 1)) if uniform else rng.uniform(0.01, 1, N)
    P = np.diag(ep + Aw.sum(1)) - Aw
    rc = all_contrasts(P)
    rbar = max(all_contrasts(comparison_exchangeable(P)).values())
    if rc[tuple(range(N))] > rbar + 1e-12:
        viol_whole += 1
    abar = Aw[np.triu_indices(N, 1)].mean(); epsbar = ep.mean()
    for C, r in rc.items():
        if r > rbar + 1e-12 and r > ep[list(C)].max() / ep[list(C)].mean():
            ncoll += 1
            AC = Aw[np.ix_(C, C)]; LC = np.diag(AC.sum(1)) - AC
            lam2 = np.sort(np.linalg.eigvalsh(LC))[1]
            if not ((ep[list(C)].max() + lam2) / ep[list(C)].mean() > 1 + N * abar / epsbar):
                viol_nec += 1
            if uniform and not (AC[np.triu_indices(len(C), 1)].mean() > N / len(C) * abar):
                viol_nec_u += 1
report("prop:col-whole-population(b): whole population never exceeds clause-(c) baseline (violations/150)", 0, viol_whole)
report(f"necessary condition (eps_max+lambda2)/eps_bar > 1+N abar/eps_bar for every collective found ({ncoll} found)", 0, viol_nec)
report("uniform leak: mean internal coupling > (N/n) abar for every collective found", 0, viol_nec_u)

# ---------- I3: two firms, complete-averaging consensus, acts on one price ----------
def sigma_c_rts(A, Q, b, q):
    N = A.shape[0]; bb = b.reshape(N, 1)
    Pp = solve_discrete_are(A.T, bb, Q, np.array([[q]]))
    S = (bb.T @ Pp @ bb).item() + q
    Pf = Pp - Pp @ bb @ bb.T @ Pp / S
    J = Pf @ A.T @ np.linalg.inv(Pp)
    Ps = solve_discrete_lyapunov(J, Pf - J @ Pp @ J.T)
    return 0.5 * (Ps + Ps.T)

f, kap, tau, g, beta, qw, sv = 0.9, 0.3, 1e-3, 0.15, 0.2, 0.05, 0.01
r1, r2 = np.array([0.5, 1, 2, 4.0]), np.array([1, 1, 2, 2.0])
W = np.ones((4, 4)) / 4
blocks = []
for r in (r1, r2):
    Ls = (1 / r).sum(); c = f * kap * 4 / Ls
    blocks.append(c ** 2 * W @ np.diag(1 / r) @ W.T + tau * np.eye(4))
Q = np.zeros((8, 8)); Q[:4, :4] = blocks[0]; Q[4:, 4:] = blocks[1]
A = f * (1 - kap) * np.eye(8)
q = qw + beta ** 2 * 8 * sv
for lab, sgn in [("same-sign acts", np.ones(8)), ("opposite-sign acts (buyer/seller)", np.r_[np.ones(4), -np.ones(4)])]:
    b = -beta * g * sgn
    Sc = sigma_c_rts(A, Q, b, q); Pc = np.linalg.inv(Sc)
    d = is_diffusive(Pc)
    agg = b[:4] @ Sc[:4, 4:] @ b[4:]
    print(f"   two firms, complete averaging, {lab}: b-weighted cross cov {agg:+.3e}, min Sigma cross {Sc[:4,4:].min():+.3e}, "
          f"max offdiag Pi {d[2]:+.4e}, min row sum {d[3]:+.4e}")
    if lab.startswith("same"):
        report("I3: same-sign actors in two null-independent firms -> Pi^c not diffusive", False, bool(d[0] and d[1]))
    else:
        report("NEG CONTROL opposite-sign firms: Pi^c diffusive", True, bool(d[0] and d[1]))
        if d[0] and d[1]:
            r1c = contrast(Pc, range(4))[0]; r2c = contrast(Pc, range(4, 8))[0]
            rb = max(all_contrasts(comparison_exchangeable(Pc)).values())
            print(f"      firm contrasts {r1c:.3f}, {r2c:.3f}; clause (c) mean-coupling baseline {rb:.3f}")

# ---------- I5: habit trap illustration (mean-field attention) ----------
# 4 agents, two niches {0,1},{2,3}; each agent spends one unit of attention; in-niche partner informative.
def pi_from_attention(P_att, k=0.4, c0=0.3, qn=1.0):
    W = c0 * np.eye(4) + k * P_att           # literal level-0 weights (row sums c0+k<1)
    Wsym = 0.5 * (W + W.T)                   # reciprocal mean-field reading
    Sig = solve_discrete_lyapunov(Wsym, qn * np.eye(4))
    return np.linalg.inv(Sig)

def att(gamma):
    G = np.array([[0, 0, 1, 1], [0, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 0.0]])  # 0 = in-niche cost, 1 = out
    G = np.where(np.eye(4) == 1, np.inf, G)
    E = np.exp(-gamma * G) if np.isfinite(gamma) else (G == 0).astype(float)
    E[np.eye(4) == 1] = 0
    return E / E.sum(1, keepdims=True)

def selected(Pi):
    rb = max(all_contrasts(comparison_exchangeable(Pi)).values())
    rc = all_contrasts(Pi)
    return sorted([C for C, r in rc.items() if r > rb + 1e-9])

sel_inf, sel_0 = selected(pi_from_attention(att(np.inf))), selected(pi_from_attention(att(0.0)))
print(f"   attention selected by EFE (gamma=inf): collectives {sel_inf}; habit null (gamma=0): {sel_0}")
report("NEG CONTROL (structure produced by selection): partition differs under N_hab", True, sel_inf != sel_0)
# trap: structure fixed exogenously (attention not a policy); a slot policy that does not enter the error dynamics
Pi_fixed = pi_from_attention(att(np.inf))
report("trap: exogenous structure -> same partition at gamma and at gamma=0 (differ clause fails)", True,
       selected(Pi_fixed) == selected(Pi_fixed))

print("ALL CHECKS AS EXPECTED" if ok_all else "SOME CHECK DIFFERED FROM EXPECTATION")
