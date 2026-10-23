r"""Numerical checks for Item_3_curvature_hierarchy.tex (float64, tiny sizes, single thread).

Tangent communication model of Item 2 with declared parents (meta-agents). Each block prints a residual,
a dimension or a profile; agreement supports the statements at the tested instances only.
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




def code_coboundary(mod):
    r"""delta: y -> (T_e (y_i - y_j))_e, and V: omega -> (T_e kappa_i omega_e)_e, as matrices."""
    rows_d, rows_v = [], []
    for e, (j, i) in enumerate(mod.edges):
        L = mod.Lrec(e)
        rows_d.append(L[:, :mod.nA * mod.K])
        rows_v.append(-L[:, mod.nA * mod.K:])
    return np.vstack(rows_d), np.vstack(rows_v)


def edge_gain(T, R, s2, c):
    r"""F_e = s2 |c|^2 T^T (R + s2 |c|^2 T T^T)^{-1} T."""
    a = s2 * (c @ c)
    return a * T.T @ np.linalg.solve(R + a * T @ T.T, T)


cx_edges = [(1, 0), (0, 1), (2, 1), (1, 2), (0, 2), (2, 0)]
cx_loops = [[0, 1], [2, 3], [4, 5], [1, 3, 5], [4, 2, 0]]

# (1) Matter penalizes curvature: the omega-marginal precision of the global joint.
K = 2
codes = [rng.standard_normal((2, K)) for _ in cx_edges]                  # injective codes
R = [spd(2) / 2 for _ in cx_edges]
c_common = rng.standard_normal(K)
P = [spd(K) / K for _ in range(3)]
mod = Tangent(K, 3, cx_edges, codes, R, [c_common] * 3, [rng.standard_normal(K) for _ in range(3)], P, 0.8, 0.0, [])
J, eta = mod.global_quad()
ny = 3 * K
Jyy, Jyw, Jww = J[:ny, :ny], J[:ny, ny:], J[ny:, ny:]
schur = Jww - Jyw.T @ np.linalg.solve(Jyy, Jyw)
dlt, Vm = code_coboundary(mod)
Rb = blockdiag(R)
Pinv = blockdiag([np.linalg.inv(p) for p in P])
formula = np.eye(Jww.shape[0]) / mod.s2 + Vm.T @ np.linalg.solve(Rb + dlt @ Pinv @ dlt.T, Vm)
print("(1a) |Schur complement - (anchor + V^T (R + delta P^-1 delta^T)^-1 V)| =", np.abs(schur - formula).max())
Ri = np.linalg.inv(Rb)
Hproj = Ri - Ri @ dlt @ np.linalg.pinv(dlt.T @ Ri @ dlt) @ dlt.T @ Ri
for eps in (1e-3, 1e-6):
    mod.P = [eps * np.eye(K)] * 3
    J, eta = mod.global_quad()
    schur = J[ny:, ny:] - J[ny:, :ny] @ np.linalg.solve(J[:ny, :ny], J[:ny, ny:])
    print("(1b) anchors eps =", eps, ": |record part - V^T H1-projection V| =",
          np.abs(schur - np.eye(Jww.shape[0]) / mod.s2 - Vm.T @ Hproj @ Vm).max())
lim = Vm.T @ Hproj @ Vm
nE, mm = len(cx_edges), K * K
print("     rank of the limiting penalty =", np.linalg.matrix_rank(lim, tol=1e-9),
      " predicted (E - V + 1) K =", (nE - 3 + 1) * K)
Bc = np.zeros((len(cx_loops) * K, nE * mm))                              # omega -> (sum_{e in gamma} omega_e c)
for g, gam in enumerate(cx_loops):
    for e in gam:
        Bc[g * K:(g + 1) * K, e * mm:(e + 1) * mm] += kap(c_common)
kerB = null_space(Bc)
print("     |penalty on {loop sums of omega c = 0}| =", np.abs(kerB.T @ lim @ kerB).max(),
      " dim of that set =", kerB.shape[1], " predicted E K^2 - (E - V + 1) K =", nE * mm - (nE - 2) * K)

# (2) Stationary reinterpretation is rank one on the topic: kappa omega_e = F_e Delta_e.
mod.P = P
mod.codes = [rng.standard_normal((1 + e % 2, K)) for e in range(nE)]
mod.R = [spd(mod.codes[e].shape[0]) / 2 for e in range(nE)]
mod.o = [np.zeros(mod.codes[e].shape[0]) for e in range(nE)]
mod.m = [3.0 * rng.standard_normal(K) for _ in range(3)]                  # conflicting anchors
for mode in ("global", "plug", "law"):
    if mode == "global":
        J, eta = mod.global_quad(); x = np.linalg.solve(J, eta); Rt = mod.R
    else:
        Hpa, gpa, _, Sg, _, _ = mod.per_agent(mode); x = np.linalg.solve(Hpa, gpa)
        Rt = [mod.R[e] + (mod.codes[e] @ Sg[j] @ mod.codes[e].T if mode == "law" else 0) for e, (j, i) in enumerate(cx_edges)]
    err, sv2 = 0.0, 0.0
    for e, (j, i) in enumerate(cx_edges):
        w = x[mod.wi[e]].reshape(K, K)
        Dl = x[mod.yi[i]] - x[mod.yi[j]]
        F = edge_gain(mod.codes[e], Rt[e], mod.s2, c_common)
        err = max(err, np.abs(w @ c_common - F @ Dl).max())
        sv2 = max(sv2, np.linalg.svd(w, compute_uv=False)[1])
    print("(2)", mode, ": |kappa omega - F Delta| =", err, " largest second singular value of omega_e =", sv2)

# (3) Holonomy on the topic: sum_e F_e Delta_e; zero for equal gains on a loop, whatever the disagreement.
J, eta = mod.global_quad(); x = np.linalg.solve(J, eta)
for g, gam in enumerate(cx_loops):
    hol = sum(x[mod.wi[e]].reshape(K, K) for e in gam) @ c_common
    pred = sum(edge_gain(mod.codes[e], mod.R[e], mod.s2, c_common) @ (x[mod.yi[cx_edges[e][1]]] - x[mod.yi[cx_edges[e][0]]]) for e in gam)
    if g in (0, 3):
        print("(3) unequal gains, loop", gam, ": |hol c - sum F Delta| =", np.abs(hol - pred).max(), " |hol c| =", np.abs(hol).max())
Tu, Ru = rng.standard_normal((1, K)), spd(1)
mod.codes = [Tu] * nE; mod.R = [Ru] * nE; mod.o = [np.zeros(1)] * nE
J, eta = mod.global_quad(); x = np.linalg.solve(J, eta)
dis = max(np.abs(x[mod.yi[i]] - x[mod.yi[j]]).max() for (j, i) in cx_edges)
hol = max(np.abs(sum(x[mod.wi[e]].reshape(K, K) for e in gam) @ c_common).max() for gam in cx_loops)
print("    equal gains: largest disagreement |Delta| =", dis, " largest |hol c| over the loops =", hol)
e0, e1 = 0, 1                                                             # two-cycle 1->0, 0->1
mod.codes = [Tu] * nE; mod.R = [Ru] * nE; mod.R[e1] = 5.0 * Ru            # unequal record noise on the reverse edge
J, eta = mod.global_quad(); x = np.linalg.solve(J, eta)
hol = (x[mod.wi[e0]] + x[mod.wi[e1]]).reshape(K, K) @ c_common
D0 = x[mod.yi[0]] - x[mod.yi[1]]
pred = (edge_gain(Tu, Ru, mod.s2, c_common) - edge_gain(Tu, 5.0 * Ru, mod.s2, c_common)) @ D0
print("    two-cycle with unequal gains: |hol c - (F_e - F_e') Delta_e| =", np.abs(hol - pred).max(), " |hol c| =", np.abs(hol).max())

# (4) Two clusters with meta-agents: top-down coupling localizes disagreement at the wall.
def two_cluster(tau, bridge_noise=(1.0, 1.0), K=2, seed=7, pin=None):
    rs = np.random.default_rng(seed)
    I, Jc = [0, 1, 2], [3, 4, 5]
    edges, codes_, R_ = [], [], []
    T0 = rs.standard_normal((1, K)); T1 = rs.standard_normal((1, K))
    for grp in (I, Jc):
        for a in grp:
            for b in grp:
                if a != b:
                    edges.append((a, b)); codes_.append(np.vstack([T0, T1])); R_.append(np.eye(2))
    bridges = [(2, 3), (3, 2), (1, 4), (4, 1)]
    for k, (a, b) in enumerate(bridges):
        edges.append((a, b)); codes_.append(np.vstack([T0, T1])); R_.append(bridge_noise[k // 2] * np.eye(2))
    for a in I:
        edges.append((6, a)); codes_.append(np.eye(K)); R_.append(np.eye(K) / max(tau, 1e-12))
    for b in Jc:
        edges.append((7, b)); codes_.append(np.eye(K)); R_.append(np.eye(K) / max(tau, 1e-12))
    u = np.ones(K) / np.sqrt(K)
    m_ = [u + 0.3 * rs.standard_normal(K) for _ in I] + [-u + 0.3 * rs.standard_normal(K) for _ in Jc] + [np.zeros(K)] * 2
    P_ = [np.eye(K)] * 6 + [1e-3 * np.eye(K)] * 2
    c = np.ones(K)
    mdl = Tangent(K, 8, edges, codes_, R_, [c] * 8, m_, P_, 0.5, 0.0, [], o=[np.zeros(r.shape[0]) for r in R_])
    if pin is not None:
        mdl.G = [pin * np.eye(K * K) if (e < 12 or e >= 16) else np.zeros((K * K, K * K)) for e in range(len(edges))]
    return mdl, edges


for pin, label in ((None, "free cluster dictionaries"), (1e6, "pinned cluster dictionaries")):
    print("(4)", label, "- top-down coupling tau: mean |Delta| on internal edges, on bridges")
    for tau in (0.0, 1.0, 10.0, 100.0):
        mdl, edges = two_cluster(tau, pin=pin)
        J, eta = mdl.global_quad(); x = np.linalg.solve(J, eta)
        dl = [np.linalg.norm(x[mdl.yi[i]] - x[mdl.yi[j]]) for (j, i) in edges]
        print("     tau =", tau, ":", np.mean(dl[:12]), np.mean(dl[12:16]))


def wall_curvature(mdl, edges, x):
    loop = [edges.index((2, 3)), edges.index((3, 4)), edges.index((4, 1)), edges.index((1, 2))]
    c = mdl.c[0]
    hol = sum(x[mdl.wi[e]].reshape(mdl.K, mdl.K) for e in loop) @ c
    tc = sum(x[mdl.wi[e]].reshape(mdl.K, mdl.K) for e in (edges.index((2, 3)), edges.index((3, 2)))) @ c
    inner = sum(x[mdl.wi[e]].reshape(mdl.K, mdl.K) for e in (edges.index((0, 1)), edges.index((1, 2)), edges.index((2, 0)))) @ c
    return np.linalg.norm(hol), np.linalg.norm(tc), np.linalg.norm(inner)


for bn, name in (((1.0, 1.0), "equal bridge gains"), ((1.0, 6.0), "unequal bridge gains")):
    mdl, edges = two_cluster(10.0, bn)
    J, eta = mdl.global_quad(); x = np.linalg.solve(J, eta)
    print("     ", name, ": |hol c| on the wall-crossing loop, on a bridge two-cycle, on an internal triangle =", wall_curvature(mdl, edges, x))
    mdl, edges = two_cluster(10.0, bn, pin=1e6)
    J, eta = mdl.global_quad(); x = np.linalg.solve(J, eta)
    JI = [edges.index((3, 2)), edges.index((4, 1))]; IJ = [edges.index((2, 3)), edges.index((1, 4))]
    print("       pinned clusters: |difference of the two J->I bridge dictionaries| =",
          np.abs(x[mdl.wi[JI[0]]] - x[mdl.wi[JI[1]]]).max(), " |omega_(I->J) + omega_(J->I)| max =",
          max(np.abs(x[mdl.wi[a]] + x[mdl.wi[b]]).max() for a in IJ for b in JI), " wall loop |hol c| =", wall_curvature(mdl, edges, x)[0])

# (5) Rigid limit: clusters pinned to their meta-agents give a two-agent tangent model on the parents.
pinned = 1e9
mdl, edges = two_cluster(1.0, (1.0, 6.0), pin=pinned)
br = [12, 13, 14, 15]
K2 = mdl.K
for tau in (1e3, 1e6):
    mdl, edges = two_cluster(tau, (1.0, 6.0), pin=pinned)
    J, eta = mdl.global_quad(); x = np.linalg.solve(J, eta)
    A_edges = [(1, 0) if edges[e][0] in (3, 4, 5) else (0, 1) for e in br]   # (sender, receiver): B=1 sends to A=0
    PA = sum(mdl.P[i] for i in (0, 1, 2, 6)); PB = sum(mdl.P[i] for i in (3, 4, 5, 7))
    mA = np.linalg.solve(PA, sum(mdl.P[i] @ mdl.m[i] for i in (0, 1, 2, 6)))
    mB = np.linalg.solve(PB, sum(mdl.P[i] @ mdl.m[i] for i in (3, 4, 5, 7)))
    meta = Tangent(K2, 2, A_edges, [mdl.codes[e] for e in br], [mdl.R[e] for e in br], [mdl.c[0]] * 2, [mA, mB], [PA, PB],
                   mdl.s2, 0.0, [], o=[np.zeros(2)] * 4)
    Jm, em = meta.global_quad(); xm = np.linalg.solve(Jm, em)
    yA = x[mdl.yi[0]]; yB = x[mdl.yi[3]]
    werr = max(np.abs(x[mdl.wi[e]] - xm[meta.wi[k]]).max() for k, e in enumerate(br))
    print("(5) tau =", tau, ": |cluster I - meta A|, |cluster J - meta B|, |bridge dictionaries - meta dictionaries| =",
          np.abs(yA - xm[meta.yi[0]]).max(), np.abs(yB - xm[meta.yi[1]]).max(), werr)
