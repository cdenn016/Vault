"""Tail certificates for the gf:regrouping data (tau^2=1/20): persistence balls."""
from fractions import Fraction as Fr
from certify_gf import Model, mv, mat_inv, sub, name
M = Model(Fr(1), Fr(1, 4), Fr(1, 20), Fr(4))
o = [Fr(x) for x in ("2.9", "3.1", "5.65", "5.85")]; m0 = [Fr(x) for x in (-4, 2, -9, -1)]
sep = (((0, 1), (2, 3)), ((0, 1), (2, 3))); join = (((0, 1), (2, 3)), ((0, 1, 2, 3),))
traj = [m0]
for n in range(6):
    W, _, _ = M.select(traj[-1]); traj.append(M.sweep(W, traj[-1], o))
ms = mv(M.C[join], mv(mat_inv([[M.C[join][i][j] + (M.rho2 if i == j else 0) for j in range(4)] for i in range(4)]), o))
r, P = M.ball_radius(join, ms)
print("full: r_join =", float(r), "binding", name(P), [ (n, float(sum(x*x for x in sub(m, ms))) <= float(r)**2 and sum(x*x for x in sub(m, ms)) <= r*r) for n, m in enumerate(traj)])
lp = [m0]
for n in range(6):
    lp.append([M.a * oi + M.b * M.k * mi for oi, mi in zip(o, lp[-1])])
ko = [M.kappa * x for x in o]
r, P = M.ball_radius(sep, ko)
print("lp: r_sep at kappa o =", float(r), "binding", name(P), [(n, sum(x*x for x in sub(m, ko)) <= r*r) for n, m in enumerate(lp)])
