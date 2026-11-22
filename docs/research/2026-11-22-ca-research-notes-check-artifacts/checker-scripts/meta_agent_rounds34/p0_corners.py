"""P0: the exactly computed clauses at the 128 corners of the +-5% box, own engine."""
import io, contextlib, itertools
import numpy as np
with contextlib.redirect_stdout(io.StringIO()):
    import p0_rebuild as eng

def ric(own_var, msg_vars):
    H = np.array([[1.0, 0.0]] + [[0.0, 1.0]] * len(msg_vars))
    Rm = np.diag([own_var] + list(msg_vars))
    P = np.eye(2)
    for _ in range(5000):
        K = P @ H.T @ np.linalg.inv(H @ P @ H.T + Rm)
        Pn = eng.A2 @ (np.eye(2) - K @ H) @ P @ eng.A2.T + eng.QM
        done = np.max(np.abs(Pn - P)) < 1e-15
        P = Pn
        if done: break
    K = P @ H.T @ np.linalg.inv(H @ P @ H.T + Rm)
    return P, K, H
eng.riccati = ric
base = dict(F=0.9, Q=0.05, R=1.0, RS=0.01, RC=0.002, QC=1e-4, GAM=40.0)
A = (1, 2, 3, 4); allS = ((0,),) * 4
rows = []
for signs in itertools.product((-1, 1), repeat=7):
    p = {k: v * (1 + 0.05 * s) for (k, v), s in zip(base.items(), signs)}
    eng.F, eng.Q, eng.R, eng.QC = p['F'], p['Q'], p['R'], p['QC']
    eng.A2 = np.array([[p['F'], 0.0], [1.0, 0.0]])
    eng.QM = np.diag([p['Q'], 0.0]) + p['QC'] * np.eye(2)
    S, filt = eng.sigma_c(allS, rs=p['RS'], rc=p['RC'])
    Pi = np.linalg.inv(S)
    rA = eng.contrast(Pi, A)
    oth = max(eng.contrast(Pi, C) for C in eng.regions() if C != A)
    offs = [-Pi[i, j] for i in range(5) for j in range(i + 1, 5)]
    b1 = 1 + 5 * np.mean(offs) / Pi.sum(1).mean()
    vb = np.mean(np.diag(S)); ob = (S.sum() - np.trace(S)) / 20
    b2 = 1 + 5 * ob / (vb - ob)
    Pm, Km, Hm = filt[1]
    def info(mv):
        H = np.array([[1.0, 0.0]] + [[0.0, 1.0]] * len(mv)); Rm = np.diag([p['R']] + mv)
        return 0.5 * (np.linalg.slogdet(H @ Pm @ H.T + Rm)[1] - np.linalg.slogdet(Rm)[1])
    IS, I0, Im = info([p['RS'] + p['RC']]), info([]), info([p['R'] + p['RC']])
    pnot = (np.exp(p['GAM'] * (I0 - IS)) + 3 * np.exp(p['GAM'] * (Im - IS)))
    rows.append((rA, max(b1, b2), oth, eng.diffusive(Pi), pnot))
r = np.array([[x[0], x[1], x[2], x[4]] for x in rows])
print("corners: %d, all diffusive: %s" % (len(rows), all(x[3] for x in rows)))
print("r(A) in [%.4f, %.4f]; larger baseline max %.4f; other regions max %.4f; min margin r(A)-baseline %.4f"
      % (r[:, 0].min(), r[:, 0].max(), r[:, 1].max(), r[:, 2].max(), (r[:, 0] - r[:, 1]).min()))
print("r0 = 4.5 admissible at every corner: %s; largest P(member does not read S) %.2e"
      % (bool((r[:, 1] < 4.5).all() and (r[:, 0] >= 4.5).all()), r[:, 3].max()))
