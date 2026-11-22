"""C20(ii),(iv): the 6^4 fixed two-partner patterns of the variant P1, with my own engine."""
import io, contextlib, itertools
import numpy as np
with contextlib.redirect_stdout(io.StringIO()):
    import p0_rebuild as eng

_cache = {}
def _ric(own_var, msg_vars):
    key = (own_var, tuple(msg_vars))
    if key not in _cache:
        H = np.array([[1.0, 0.0]] + [[0.0, 1.0]] * len(msg_vars))
        Rm = np.diag([own_var] + list(msg_vars))
        P = np.eye(2)
        for _ in range(3000):
            K = P @ H.T @ np.linalg.inv(H @ P @ H.T + Rm)
            Pn = eng.A2 @ (np.eye(2) - K @ H) @ P @ eng.A2.T + eng.QM
            done = np.max(np.abs(Pn - P)) < 1e-15
            P = Pn
            if done: break
        K = P @ H.T @ np.linalg.inv(H @ P @ H.T + Rm)
        _cache[key] = (P, K, H)
    return _cache[key]
eng.riccati = _ric
A = (1, 2, 3, 4)
pairs = lambda i: list(itertools.combinations([j for j in range(5) if j != i], 2))
nd = 0; rA = []; selA = 0; best = []; mi_ge = 0; mi_max = (0, None); sub_ge = 0; ties = 0; nd_mi_max = 0
for pat in itertools.product(*[pairs(i) for i in range(1, 5)]):
    S, _ = eng.sigma_c(pat)
    Pi = np.linalg.inv(S)
    m4 = max(eng.multiinfo(S, C) for C in itertools.combinations(range(5), 4))
    if m4 >= 0.663833: mi_ge += 1
    if m4 > mi_max[0]: mi_max = (m4, pat)
    sv = eng.substitute(S)
    if sv >= 1.5 - 1e-9: sub_ge += 1
    if abs(sv - 1.5) < 1e-9: ties += 1
    if eng.diffusive(Pi):
        nd += 1
        rs = {C: eng.contrast(Pi, C) for C in eng.regions()}
        best.append(max(rs.values()))
        if [C for C, r in rs.items() if r >= 4.45] == [A]:
            selA += 1; rA.append(rs[A])
    else:
        nd_mi_max = max(nd_mi_max, m4)
print("diffusive %d of 1296; select exactly {A} at 4.45: %d; r(A) on those: min %.4f max %.4f, distinct %s"
      % (nd, selA, min(rA), max(rA), sorted(set(np.round(rA, 4)))))
print("largest regional contrast over diffusive patterns %.4f; count >= 5.3723: %d" % (max(best), sum(b >= 5.3723 for b in best)))
print("multi-info: patterns >= 0.663833: %d; max %.6f at %s; max over non-diffusive %.6f" % (mi_ge, mi_max[0], mi_max[1], nd_mi_max))
print("substitute selector >= 3/2: %d (exact ties %d)" % (sub_ge, ties))
