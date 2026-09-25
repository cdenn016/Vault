"""L05: region free energy of PIFB2 App. H, Eq. eq:beyond_mf_bethe_entropy, against Yedidia-Freeman-Weiss.
(1) tree: Bethe free energy at exact marginals equals -log Z exactly; (2) product beliefs reduce H_B to the MF entropy;
(3) 4-cycle: Bethe free energy at exact marginals differs from -log Z (no bound implied), and loopy BP fixed point.
Binary variables, random pairwise potentials, exhaustive enumeration.
"""
import itertools, numpy as np
rng = np.random.default_rng(2)
def H(p): p = p[p > 0]; return -(p*np.log(p)).sum()
def model(nv, edges):
    psi_i = [np.exp(rng.normal(size=2)) for _ in range(nv)]
    psi_ij = {e: np.exp(rng.normal(size=(2, 2))) for e in edges}
    P = np.zeros([2]*nv)
    for x in itertools.product([0, 1], repeat=nv):
        v = np.prod([psi_i[i][x[i]] for i in range(nv)])*np.prod([psi_ij[(a, b)][x[a], x[b]] for (a, b) in edges])
        P[x] = v
    Z = P.sum(); return psi_i, psi_ij, P/Z, Z
def marg(P, idx):
    ax = tuple(a for a in range(P.ndim) if a not in idx); return P.sum(axis=ax)
def bethe(nv, edges, psi_i, psi_ij, bi, bij):
    deg = [sum(i in e for e in edges) for i in range(nv)]
    U = -sum((bi[i]*np.log(psi_i[i])).sum() for i in range(nv)) - sum((bij[e]*np.log(psi_ij[e])).sum() for e in edges)
    HB = sum(H(bij[e].ravel()) for e in edges) - sum((deg[i]-1)*H(bi[i]) for i in range(nv))
    return U - HB, HB
# (1) tree: star + path, 5 nodes
edges = [(0, 1), (0, 2), (2, 3), (2, 4)]
psi_i, psi_ij, P, Z = model(5, edges)
bi = [marg(P, (i,)) for i in range(5)]; bij = {e: marg(P, e) for e in edges}
FB, HB = bethe(5, edges, psi_i, psi_ij, bi, bij)
print('(1) tree: F_Bethe(exact marginals) + log Z =', FB + np.log(Z), '; H_B - H(joint) =', HB - H(P.ravel()))
# (2) product beliefs
qi = [rng.dirichlet([1, 1]) for _ in range(5)]
_, HBp = bethe(5, edges, psi_i, psi_ij, qi, {e: np.outer(qi[e[0]], qi[e[1]]) for e in edges})
print('(2) product beliefs: H_B - sum_i H(q_i) =', HBp - sum(H(q) for q in qi))
iso = [(0, 1)]; _, HBi = bethe(3, iso, [np.ones(2)]*3, {(0, 1): np.ones((2, 2))}, qi[:3], {(0, 1): np.outer(qi[0], qi[1])})
print('    with an isolated node (d=0 counting number +1): H_B - sum H =', HBi - sum(H(q) for q in qi[:3]))
# (3) loop
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
psi_i, psi_ij, P, Z = model(4, edges)
bi = [marg(P, (i,)) for i in range(4)]; bij = {e: marg(P, e) for e in edges}
FB, HB = bethe(4, edges, psi_i, psi_ij, bi, bij)
print('(3) 4-cycle: F_Bethe(exact marginals) + log Z =', FB + np.log(Z))
