r"""Numerical checks for Item_2_link_dynamics.tex (float64, tiny sizes, single thread).

Tangent communication model: contents y_i in R^K, receiver-owned dictionary generators omega_e
(edge e = (sender j, receiver i)), comparison records o_e = T_e (y_i - y_j - omega_e c_i) + eps.
Each block prints a residual, a dimension or a spectrum. Agreement supports the statements at the
tested instances; the proofs are in the document.
"""
import numpy as np
from scipy.linalg import expm, null_space

rng = np.random.default_rng(20261023)


def spd(n):
    a = rng.standard_normal((n, n))
    return a @ a.T + n * np.eye(n)


def kap(c):
    r"""Matrix of omega -> omega c on row-major vec(omega)."""
    return np.kron(np.eye(len(c)), c[None, :])


def blockdiag(blocks):
    out = np.zeros((sum(b.shape[0] for b in blocks), sum(b.shape[1] for b in blocks))); r = c = 0
    for b in blocks:
        out[r:r + b.shape[0], c:c + b.shape[1]] = b; r += b.shape[0]; c += b.shape[1]
    return out


class Tangent:
    def __init__(self, K, nA, edges, codes, R, c, m, P, s2, lam, loops, G=None, wstar=None, o=None):
        self.K, self.nA, self.edges, self.mm = K, nA, edges, K * K
        self.codes, self.R, self.c, self.m, self.P = codes, R, c, m, P
        self.s2, self.lam, self.loops = s2, lam, loops
        nE = len(edges)
        self.G = G if G is not None else [np.zeros((self.mm, self.mm)) for _ in edges]
        self.wstar = wstar if wstar is not None else [np.zeros(self.mm) for _ in edges]
        self.o = o if o is not None else [np.zeros(codes[e].shape[0]) for e in range(nE)]
        self.n = nA * K + nE * self.mm
        self.yi = [np.arange(i * K, (i + 1) * K) for i in range(nA)]
        off = nA * K
        self.wi = [np.arange(off + e * self.mm, off + (e + 1) * self.mm) for e in range(nE)]
        self.owned = [[e for e, (j, h) in enumerate(edges) if h == i] for i in range(nA)]
        self.own = [np.concatenate([self.yi[i]] + [self.wi[e] for e in self.owned[i]]) for i in range(nA)]

    def Lrec(self, e):
        j, i = self.edges[e]
        T = self.codes[e]
        L = np.zeros((T.shape[0], self.n))
        L[:, self.yi[i]] += T
        L[:, self.yi[j]] -= T
        L[:, self.wi[e]] -= T @ kap(self.c[i])
        return L

    def Bloop(self, g):
        B = np.zeros((self.mm, self.n))
        for e in self.loops[g]:
            B[:, self.wi[e]] += np.eye(self.mm)
        return B

    def _local(self, H, b, i, edges_here):
        ix = self.yi[i]
        H[np.ix_(ix, ix)] += self.P[i]; b[ix] += self.P[i] @ self.m[i]
        for e in edges_here:
            wx = self.wi[e]
            H[np.ix_(wx, wx)] += np.eye(self.mm) / self.s2 + self.G[e]
            b[wx] += self.G[e] @ self.wstar[e]

    def global_quad(self):
        H = np.zeros((self.n, self.n)); b = np.zeros(self.n)
        for i in range(self.nA):
            self._local(H, b, i, self.owned[i])
        for e in range(len(self.edges)):
            L = self.Lrec(e); Ri = np.linalg.inv(self.R[e])
            H += L.T @ Ri @ L; b += L.T @ Ri @ self.o[e]
        for g in range(len(self.loops)):
            B = self.Bloop(g); H += self.lam * B.T @ B
        return H, b

    def agent_quad(self, i, Sig, V, mode):
        H = np.zeros((self.n, self.n)); b = np.zeros(self.n)
        self._local(H, b, i, self.owned[i])
        for e in self.owned[i]:
            j = self.edges[e][0]; T = self.codes[e]
            Rt = self.R[e] + (T @ Sig[j] @ T.T if mode == "law" else 0.0)
            L = self.Lrec(e); Ri = np.linalg.inv(Rt)
            H += L.T @ Ri @ L; b += L.T @ Ri @ self.o[e]
        for g, gam in enumerate(self.loops):
            if not any(e in self.owned[i] for e in gam):
                continue
            Om = self.lam * np.eye(self.mm)
            if mode == "law":
                Vs = sum((V[f] for f in gam if f not in self.owned[i]), np.zeros((self.mm, self.mm)))
                Om = np.linalg.inv(np.eye(self.mm) / self.lam + Vs)
            B = self.Bloop(g); H += B.T @ Om @ B
        return H, b

    def per_agent(self, mode, iters=2000):
        nE = len(self.edges)
        Sig = [np.zeros((self.K, self.K)) for _ in range(self.nA)]
        V = [np.zeros((self.mm, self.mm)) for _ in range(nE)]
        for it in range(iters):
            newS, newV = list(Sig), list(V)
            for i in range(self.nA):
                H, _ = self.agent_quad(i, Sig, V, mode); ow = self.own[i]
                C = np.linalg.inv(H[np.ix_(ow, ow)])
                newS[i] = C[:self.K, :self.K]; k = self.K
                for e in self.owned[i]:
                    newV[e] = C[k:k + self.mm, k:k + self.mm]; k += self.mm
            delta = max(np.abs(a - b_).max() for a, b_ in zip(newS + newV, Sig + V))
            Sig, V = newS, newV
            if delta < 1e-13:
                break
        Hpa = np.zeros((self.n, self.n)); gpa = np.zeros(self.n); Ab = np.zeros((self.n, self.n))
        for i in range(self.nA):
            H, b = self.agent_quad(i, Sig, V, mode); ow = self.own[i]
            Hpa[ow, :] = H[ow, :]; gpa[ow] = b[ow]; Ab[np.ix_(ow, ow)] = H[np.ix_(ow, ow)]
        return Hpa, gpa, Ab, Sig, V, it


def sheaf_h0(edges, codes, nV, Kd):
    rows = []
    for (tail, head), Te in zip(edges, codes):
        Rw = np.zeros((Te.shape[0], nV * Kd))
        Rw[:, head * Kd:(head + 1) * Kd] += Te
        Rw[:, tail * Kd:(tail + 1) * Kd] -= Te
        rows.append(Rw)
    return nV * Kd - np.linalg.matrix_rank(np.vstack(rows), tol=1e-9)


cx_edges = [(1, 0), (0, 1), (2, 1), (1, 2), (0, 2), (2, 0)]
cx_loops = [[0, 1], [2, 3], [4, 5], [1, 3, 5], [4, 2, 0]]


def complete_model(K, rank, lam=2.0, s2=1.0, g=0.0, Rscale=1.0, seed_codes=None):
    senders = [rng.standard_normal((rank, K)) for _ in range(3)]
    codes = [senders[t] for (t, h) in cx_edges]
    R = [Rscale * spd(rank) / rank for _ in cx_edges]
    Mref = spd(K) / K
    G = [g * np.kron(T.T @ np.linalg.inv(Rr) @ T, Mref) for T, Rr in zip(codes, R)]
    wstar = [0.2 * rng.standard_normal(K * K) for _ in cx_edges]
    mod = Tangent(K, 3, cx_edges, codes, R, [rng.standard_normal(K) for _ in range(3)],
                  [rng.standard_normal(K) for _ in range(3)], [spd(K) / K for _ in range(3)],
                  s2, lam, cx_loops, G=G, wstar=wstar, o=[0.3 * rng.standard_normal(rank) for _ in cx_edges])
    return mod, senders


# (1) Interpretation gauge: records see (y, omega) only through T_e(y_i - y_j - omega_e c_i).
mod, senders = complete_model(2, 1)
Lall = np.vstack([mod.Lrec(e) for e in range(6)])
ker = null_space(Lall)
dy = rng.standard_normal(3 * 2)
x = np.zeros(mod.n); x[:6] = dy
for e, (j, i) in enumerate(cx_edges):
    c = mod.c[i]
    x[mod.wi[e]] = np.outer(dy[2 * i:2 * i + 2] - dy[2 * j:2 * j + 2], c).flatten() / (c @ c)
print("(1a) |records of the constructed gauge displacement| =", np.abs(Lall @ x).max(),
      " dim gauge =", ker.shape[1], " rank of its belief projection =", np.linalg.matrix_rank(ker[:6], tol=1e-9), "of 6")
Zs = [null_space(np.kron(T.T @ T, np.eye(2))) for T in mod.codes]
basis = blockdiag([np.eye(6)] + Zs)
k2 = null_space(Lall @ basis)
print("(1b) dictionaries fixed modulo N: belief part of the gauge has dim", np.linalg.matrix_rank((basis @ k2)[:6], tol=1e-9),
      " code-sheaf dim H0 =", sheaf_h0(cx_edges, mod.codes, 3, 2))

# (2) Persuasion, counter-persuasion and reinterpretation for one record, both pictures.
K = 3
T = rng.standard_normal((2, K)); Rr = spd(2) / 2
P0, P1 = spd(K) / K, spd(K) / K
c0 = rng.standard_normal(K); s2 = 0.7
one = Tangent(K, 2, [(1, 0)], [T], [Rr], [c0, rng.standard_normal(K)], [rng.standard_normal(K), rng.standard_normal(K)],
              [P0, P1], s2, 0.0, [], o=[rng.standard_normal(2)])
H, b = one.global_quad(); mu = np.linalg.solve(H, b)
r = one.o[0] - T @ (one.m[0] - one.m[1])
C = np.linalg.inv(P0) + np.linalg.inv(P1) + s2 * (c0 @ c0) * np.eye(K)
S = T @ C @ T.T + Rr
dy0 = np.linalg.inv(P0) @ T.T @ np.linalg.solve(S, r)
dy1 = -np.linalg.inv(P1) @ T.T @ np.linalg.solve(S, r)
kdw = -s2 * (c0 @ c0) * T.T @ np.linalg.solve(S, r)
print("(2a) global: |dy_i - formula|, |dy_j - formula|, |omega c - formula| =",
      np.abs(mu[one.yi[0]] - one.m[0] - dy0).max(), np.abs(mu[one.yi[1]] - one.m[1] - dy1).max(),
      np.abs(kap(c0) @ mu[one.wi[0]] - kdw).max())
Sig1 = np.linalg.inv(P1)
Ha, ba = one.agent_quad(0, [None, Sig1], [None], "law")
ow = one.own[0]; rest = np.setdiff1d(np.arange(one.n), ow)
xr = np.zeros(one.n); xr[one.yi[1]] = one.m[1]
xa = np.linalg.solve(Ha[np.ix_(ow, ow)], ba[ow] - Ha[np.ix_(ow, rest)] @ xr[rest])
Sp = T @ (np.linalg.inv(P0) + s2 * (c0 @ c0) * np.eye(K)) @ T.T + Rr + T @ Sig1 @ T.T
print("(2b) per-agent: |dy_i - formula|, |omega c - formula| =",
      np.abs(xa[:K] - one.m[0] - np.linalg.inv(P0) @ T.T @ np.linalg.solve(Sp, r)).max(),
      np.abs(kap(c0) @ xa[K:] + s2 * (c0 @ c0) * T.T @ np.linalg.solve(Sp, r)).max())

# (3) Grounding closes reinterpretation at rate 1/g.
Mg = spd(K) / K
for g in (1e1, 1e3, 1e5):
    one.G = [g * np.kron(T.T @ np.linalg.inv(Rr) @ T, Mg)]
    H, b = one.global_quad(); mu = np.linalg.solve(H, b)
    print("(3) g =", g, ": |T omega c| =", np.abs(T @ kap(c0) @ mu[one.wi[0]]).max(),
          " g |T omega c| =", g * np.abs(T @ kap(c0) @ mu[one.wi[0]]).max())
one.G = [np.zeros((K * K, K * K))]

# (4) Global agent-factorized flow: real spectrum, exact means, monotone free energy.
mod, _ = complete_model(2, 1)
J, eta = mod.global_quad()
D = blockdiag([J[np.ix_(ow, ow)] for ow in mod.own])
perm = np.concatenate(mod.own)
Jp, Dp = J[np.ix_(perm, perm)], D[np.ix_(perm, perm)]
ev = np.linalg.eigvals(-np.linalg.solve(Dp, Jp))
mu_star = np.linalg.solve(J, eta)
mu0 = rng.standard_normal(mod.n)
Fvals = []
for t in np.linspace(0, 20, 41):
    mut = mu_star + expm(-np.linalg.solve(D, J) * t) @ (mu0 - mu_star)
    Fvals.append(0.5 * (mut - mu_star) @ J @ (mut - mu_star))
print("(4) global: max |Im eig| =", np.abs(ev.imag).max(), " max Re eig =", ev.real.max(),
      " F monotone:", bool(np.all(np.diff(Fvals) <= 1e-12)), " |mu(20) - mu*| =", np.abs(mut - mu_star).max())

# (5) Per-agent flows (plug-in and law), compared with the global flow.
for mode in ("plug", "law"):
    Hpa, gpa, Ab, Sg, Vv, it = mod.per_agent(mode)
    ev = np.linalg.eigvals(-np.linalg.solve(Ab, Hpa))
    mu_pa = np.linalg.solve(Hpa, gpa)
    print("(5)", mode, ": cov iterations", it, " |H - H^T| =", np.abs(Hpa - Hpa.T).max(),
          " max |Im eig| =", np.abs(ev.imag).max(), " max Re eig =", ev.real.max(),
          " |mu_pa - mu_global| =", np.abs(mu_pa - mu_star).max())

# (6) Plug-in rows: dictionary rows equal the global rows; content rows lack exactly the sender terms.
Hpa, gpa, Ab, _, _, _ = mod.per_agent("plug")
wrows = np.concatenate(mod.wi)
diff = J - Hpa
send = np.zeros_like(J); sendb = np.zeros_like(eta)
for e, (j, i) in enumerate(cx_edges):
    L = mod.Lrec(e); Ri = np.linalg.inv(mod.R[e])
    send[mod.yi[j], :] += (L.T @ Ri @ L)[mod.yi[j], :]
    sendb[mod.yi[j]] += (L.T @ Ri @ mod.o[e])[mod.yi[j]]
print("(6) |dictionary rows J - H_pa| =", np.abs(diff[wrows]).max(),
      " |content rows (J - H_pa) - sender terms| =", np.abs(diff - send).max(), np.abs((eta - gpa) - sendb).max())

# (7) Directed ring, K = 1: per-agent spectrum -(1 - zeta w) with w = q s / (p s + p q c^2 + q s).
p, q, s, cc = 1.3, 2.1, 0.8, 0.9
ring = Tangent(1, 3, [(1, 0), (2, 1), (0, 2)], [np.ones((1, 1))] * 3, [np.eye(1) / q] * 3,
               [np.array([cc])] * 3, [np.array([v]) for v in (0.5, -0.2, 1.0)], [p * np.eye(1)] * 3,
               1.0 / s, 0.0, [], o=[np.zeros(1)] * 3)
Hpa, gpa, Ab, _, _, _ = ring.per_agent("plug")
ev = np.sort_complex(np.linalg.eigvals(-np.linalg.solve(Ab, Hpa)))
w = q * s / (p * s + p * q * cc ** 2 + q * s)
pred = np.sort_complex(np.array([-1, -1, -1] + [-(1 - z * w) for z in np.exp(2j * np.pi * np.arange(3) / 3)]))
Jr, er = ring.global_quad()
Dr = blockdiag([Jr[np.ix_(ow, ow)] for ow in ring.own])
print("(7) ring: |eig - prediction| =", np.abs(ev - pred).max(), " w =", w, " rigid-dictionary w =", q / (p + q),
      " global max |Im eig| =", np.abs(np.linalg.eigvals(-np.linalg.solve(Dr, Jr)).imag).max())

# (8) Grounded limit: beliefs converge to known-dictionary consensus in each picture.
mod, _ = complete_model(2, 1, g=1.0)
base_G = [G.copy() for G in mod.G]


def known_dictionary(mod, mode):
    r"""Belief means with dictionaries fixed at the grounded centers."""
    K, nA = mod.K, mod.nA
    off = [mod.o[e] + mod.codes[e] @ kap(mod.c[i]) @ mod.wstar[e] for e, (j, i) in enumerate(mod.edges)]
    Sig = [np.zeros((K, K))] * nA
    for _ in range(2000):
        A = [mod.P[i] + sum((mod.codes[e].T @ np.linalg.inv(mod.R[e] + (mod.codes[e] @ Sig[j] @ mod.codes[e].T if mode == "law" else 0))
                             @ mod.codes[e] for e, (j, h) in enumerate(mod.edges) if h == i), np.zeros((K, K))) for i in range(nA)]
        newS = [np.linalg.inv(a) for a in A]
        if max(np.abs(a - b_).max() for a, b_ in zip(newS, Sig)) < 1e-14:
            break
        Sig = newS
    H = np.zeros((nA * K, nA * K)); b = np.zeros(nA * K)
    for i in range(nA):
        H[i * K:(i + 1) * K, i * K:(i + 1) * K] += mod.P[i]; b[i * K:(i + 1) * K] += mod.P[i] @ mod.m[i]
    for e, (j, i) in enumerate(mod.edges):
        T = mod.codes[e]
        Rt = mod.R[e] + (T @ Sig[j] @ T.T if mode == "law" else 0)
        L = np.zeros((T.shape[0], nA * K)); L[:, i * K:(i + 1) * K] += T; L[:, j * K:(j + 1) * K] -= T
        Ri = np.linalg.inv(Rt)
        if mode == "global":
            H += L.T @ Ri @ L; b += L.T @ Ri @ off[e]
        else:
            H[i * K:(i + 1) * K] += (L.T @ Ri @ L)[i * K:(i + 1) * K]; b[i * K:(i + 1) * K] += (L.T @ Ri @ off[e])[i * K:(i + 1) * K]
    return np.linalg.solve(H, b)


yG, yP, yL = known_dictionary(mod, "global"), known_dictionary(mod, "plug"), known_dictionary(mod, "law")
Pid = [np.eye(4) - null_space(G) @ null_space(G).T for G in base_G]
for g in (1e3, 1e5):
    mod.G = [g * G for G in base_G]
    J, eta = mod.global_quad(); muG = np.linalg.solve(J, eta)
    Hpa, gpa, Ab, _, _, _ = mod.per_agent("plug"); muP = np.linalg.solve(Hpa, gpa)
    Hpa, gpa, Ab, _, _, _ = mod.per_agent("law"); muL = np.linalg.solve(Hpa, gpa)
    idg = max(np.abs(Pid[e] @ (muG[mod.wi[e]] - mod.wstar[e])).max() for e in range(6))
    idp = max(np.abs(Pid[e] @ (muP[mod.wi[e]] - mod.wstar[e])).max() for e in range(6))
    print("(8) g =", g, ": |y - known|: global", np.abs(muG[:6] - yG).max(), " plug-in", np.abs(muP[:6] - yP).max(),
          " law", np.abs(muL[:6] - yL).max(), " |identified omega - centre|: global", idg, " plug-in", idp)
print("    limits differ: |global - plug-in| =", np.abs(yG - yP).max(), " |global - law| =", np.abs(yG - yL).max())

# (9) Dictionaries only, grounded limit: loop filling under the three recognitions.
def dictionary_only(edges, loops, K, rank, lam, g, s2=1.0):
    nA = 1 + max(max(e) for e in edges)
    senders = [rng.standard_normal((rank, K)) for _ in range(nA)]
    codes = [senders[t] for (t, h) in edges]
    Mref = spd(K) / K
    G = [g * np.kron(T.T @ T, Mref) for T in codes]
    a_pot = 0.2 * rng.standard_normal((nA, K * K))
    wstar = [a_pot[h] - a_pot[t] for (t, h) in edges]          # flat truth
    return Tangent(K, nA, edges, codes, [1e30 * np.eye(rank) for _ in edges], [rng.standard_normal(K) for _ in range(nA)],
                   [np.zeros(K) for _ in range(nA)], [np.eye(K) for _ in range(nA)], s2, lam, loops, G=G, wstar=wstar)


def filling_report(name, mod):
    J, eta = mod.global_quad()
    wix = np.concatenate(mod.wi)
    Zs = [null_space(G) for G in mod.G]
    Zb = blockdiag(Zs)
    mu = np.linalg.solve(J, eta)[wix]
    Cfull = np.linalg.inv(J)
    Hpa, gpa, _, _, Vlaw, it = mod.per_agent("law")
    mu_law = np.linalg.solve(Hpa, gpa)[wix]
    wst = np.concatenate(mod.wstar)
    joint = np.linalg.eigvalsh(Zb.T @ Cfull[np.ix_(wix, wix)] @ Zb) / mod.s2

    def marg(blocks):
        return np.sort(np.concatenate([np.linalg.eigvalsh(Z.T @ C @ Z) for Z, C in zip(Zs, blocks)]) / mod.s2)[::-1]

    ex = marg([Cfull[np.ix_(w, w)] for w in mod.wi])
    mf = marg([np.linalg.inv(J[np.ix_(w, w)]) for w in mod.wi])
    lw = marg(Vlaw)
    print("(9)", name, ": dim N =", Zb.shape[1], " joint exact eigenvalues > 0.75 s2:", int(np.sum(joint > 0.75)))
    print("     largest per-edge marginal variances / s2: exact", np.round(ex[:4], 3), " receiver-factorized",
          np.round(mf[:4], 4), " per-agent law", np.round(lw[:4], 3), " (iterations", it, ")")
    print("     invisible-part mean error: exact", np.abs(Zb.T @ (mu - wst)).max(), " per-agent law",
          np.abs(Zb.T @ (mu_law - wst)).max(), " truth size", np.abs(Zb.T @ wst).max())


filling_report("complete exchange", dictionary_only(cx_edges, cx_loops, 3, 1, 1e3, 1e5))
filling_report("directed triangle", dictionary_only([(0, 1), (1, 2), (2, 0)], [[0, 1, 2]], 3, 1, 1e3, 1e5))
filling_report("reciprocal pair", dictionary_only([(1, 0), (0, 1)], [[0, 1]], 3, 1, 1e3, 1e5))

# (10) One unread coordinate per edge around a loop of length l: exact, factorized and law-level variances.
s2, lam = 1.0, 1e6
for l in (2, 3, 4):
    exact = s2 * (1 + (l - 1) * lam * s2) / (1 + l * lam * s2)
    mf = 1.0 / (1.0 / s2 + lam)
    v = s2
    for _ in range(100000):
        v_new = 1.0 / (1.0 / s2 + 1.0 / (1.0 / lam + (l - 1) * v))
        if abs(v_new - v) < 1e-15:
            break
        v = v_new
    Cl = np.linalg.inv(np.eye(l) / s2 + lam * np.ones((l, l)))
    pred = s2 * (l - 2) / (l - 1) if l > 2 else np.sqrt(s2 / lam)
    print("(10) l =", l, ": exact marginal", exact, "(matrix", Cl[0, 0], ") factorized", mf, " law", v, " law asymptote", pred)

# (11) Stability of the per-agent mean flow over random instances.
worst = -np.inf; worst_im = 0.0
for trial in range(40):
    mod_r, _ = complete_model(2, 1 + trial % 2, lam=float(rng.uniform(0, 3)), s2=float(rng.uniform(0.3, 2)))
    for mode in ("plug", "law"):
        Hpa, gpa, Ab, _, _, _ = mod_r.per_agent(mode)
        ev = np.linalg.eigvals(-np.linalg.solve(Ab, Hpa))
        worst = max(worst, ev.real.max()); worst_im = max(worst_im, np.abs(ev.imag).max())
print("(11) 40 random complete exchanges, both modes: largest real part", worst, " largest imaginary part", worst_im)

# (12) Tangent reciprocal potential: its mean part is the global energy with record noise S_{j,e} / beta_e
# and registered value zero, so links receive no reciprocal force.
import copy
from scipy.optimize import brentq


def kl_gauss(m1, S1, m2, S2):
    r"""KL(N(m1,S1) || N(m2,S2))."""
    S2i = np.linalg.inv(S2); d = m2 - m1
    return 0.5 * (np.trace(S2i @ S1) - len(m1) + d @ S2i @ d + np.linalg.slogdet(S2)[1] - np.linalg.slogdet(S1)[1])


def edge_cost(mod, e, x, Sig, V):
    j, i = mod.edges[e]; T = mod.codes[e]; Kp = kap(mod.c[i])
    Si = T @ Sig[i] @ T.T + mod.R[e]; Sj = T @ Sig[j] @ T.T + mod.R[e]
    rec = T @ (x[mod.yi[i]] - Kp @ x[mod.wi[e]])
    return kl_gauss(rec, Si, T @ x[mod.yi[j]], Sj) + 0.5 * np.trace(np.linalg.solve(Sj, T @ Kp @ V[e] @ Kp.T @ T.T))


def potential(mod, x, Sig, V, beta):
    tot = sum(kl_gauss(x[mod.yi[i]], Sig[i], mod.m[i], np.linalg.inv(mod.P[i])) for i in range(mod.nA))
    tot += sum(beta[e] * edge_cost(mod, e, x, Sig, V) for e in range(len(mod.edges)))
    Lam = sum((mod.lam * mod.Bloop(g).T @ mod.Bloop(g) for g in range(len(mod.loops))), np.zeros((mod.n, mod.n)))
    tot += 0.5 * x @ Lam @ x
    for e in range(len(mod.edges)):
        a = x[mod.wi[e]]; Lee = Lam[np.ix_(mod.wi[e], mod.wi[e])] + np.eye(mod.mm) / mod.s2
        tot += 0.5 * a @ a / mod.s2 + 0.5 * (a - mod.wstar[e]) @ mod.G[e] @ (a - mod.wstar[e])
        tot += 0.5 * np.trace((Lee + mod.G[e]) @ V[e]) - 0.5 * np.linalg.slogdet(V[e])[1]
    return tot


mod, _ = complete_model(2, 1, lam=1.5, g=2.0)
Sig = [spd(2) / 4 for _ in range(3)]
V = [spd(4) / 8 for _ in range(6)]
beta = rng.uniform(0.3, 1.0, 6)
modS = copy.copy(mod)
modS.R = [(mod.codes[e] @ Sig[j] @ mod.codes[e].T + mod.R[e]) / beta[e] for e, (j, i) in enumerate(mod.edges)]
modS.o = [np.zeros(1) for _ in mod.edges]
JS, etaS = modS.global_quad()
x0 = 0.3 * rng.standard_normal(mod.n)
h = 1e-6
fd = np.array([(potential(mod, x0 + h * np.eye(mod.n)[k], Sig, V, beta) - potential(mod, x0 - h * np.eye(mod.n)[k], Sig, V, beta)) / (2 * h)
               for k in range(mod.n)])
print("(12) |grad of the reciprocal potential in the means - (J^S x - eta^S)| =", np.abs(fd - (JS @ x0 - etaS)).max(),
      " gradient size", np.abs(fd).max())

# (13) Reciprocal mean flow at frozen covariances, and the rows compared with the per-agent law-level model.
Mmet = blockdiag(Sig + V)
ev = np.linalg.eigvals(-Mmet @ JS)
print("(13) reciprocal flow: max |Im eig| =", np.abs(ev.imag).max(), " max Re eig =", ev.real.max())
mod1 = copy.copy(mod); mod1.o = [np.zeros(1) for _ in mod.edges]
mod1S = copy.copy(mod1)
mod1S.R = [mod.codes[e] @ Sig[j] @ mod.codes[e].T + mod.R[e] for e, (j, i) in enumerate(mod.edges)]
J1S, eta1S = mod1S.global_quad()
worst_rows = 0.0
for i in range(3):
    Hi, bi = mod1.agent_quad(i, Sig, V, "law")
    send = np.zeros_like(J1S)
    for e, (j, k) in enumerate(mod.edges):
        if j == i:
            L = mod1S.Lrec(e); send += L.T @ np.linalg.solve(mod1S.R[e], L)
    worst_rows = max(worst_rows, np.abs((J1S - send)[mod.yi[i]] - Hi[mod.yi[i]]).max())
print("     |content rows of J^S minus sender terms - per-agent law-level content rows| =", worst_rows)

# (14) Source-role force on a sender's covariance: moment matching including the coded disagreement.
K = 3
T = rng.standard_normal((2, K)); Rr = spd(2) / 2; c0 = rng.standard_normal(K)
one = Tangent(K, 2, [(1, 0)], [T], [Rr], [c0, rng.standard_normal(K)], [np.zeros(K)] * 2, [np.eye(K)] * 2, 1.0, 0.0, [])
Sg = [spd(K) / 3, spd(K) / 3]; Vv = [spd(K * K) / 10]
xx = rng.standard_normal(one.n)
d = T @ (xx[one.yi[0]] - xx[one.yi[1]] - kap(c0) @ xx[one.wi[0]])
Sj = T @ Sg[1] @ T.T + Rr; Sk = T @ Sg[0] @ T.T + Rr
Sji = np.linalg.inv(Sj)
grad_formula = 0.5 * T.T @ (Sji - Sji @ (Sk + np.outer(d, d) + T @ kap(c0) @ Vv[0] @ kap(c0).T @ T.T) @ Sji) @ T
Edir = rng.standard_normal((K, K)); Edir = Edir + Edir.T
num = (edge_cost(one, 0, xx, [Sg[0], Sg[1] + h * Edir], Vv) - edge_cost(one, 0, xx, [Sg[0], Sg[1] - h * Edir], Vv)) / (2 * h)
print("(14) sender-covariance derivative: |numeric - trace(formula E)| =", abs(num - np.trace(grad_formula @ Edir)))
p_j, Rs, vk = 1.0, 0.5, 0.3
for d2 in (0.0, 1.0, 4.0):
    f = lambda v: p_j - 1 / v + 1 / (v + Rs) - (vk + Rs + d2) / (v + Rs) ** 2
    v_star = brentq(f, 1e-6, 1e3)
    fprime = (f(v_star + 1e-7) - f(v_star - 1e-7)) / 2e-7
    print("     scalar sender: d^2 =", d2, " stationary variance", v_star, " f'(v*) =", fprime)
