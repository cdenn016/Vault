r"""Deciding script D7c: 2^(8-4) resolution-IV fractional factorial on B_delta (delta = 1%), real protocol, r(A) with
16 pairs per point; plus the two gradient corners under the frozen protocol (40 pairs).
Generators E = BCD, F = ACD, G = ABC, H = ABD over the factors (F, Q, R, Rc, Rs, psi, gamma, qc).
Declared expectations: all 16 values inside [8.19, 8.67] up to Monte Carlo error (0.02), hence inside [7.9, 9.05);
the first-order model predicts each point within 0.05; frozen corners within 0.05 of the real ones.
NEGATIVE CONTROL: the first-order prediction with the gradient's sign flipped mispredicts by more than 0.2 at some
design point (the gradient carries information).
"""
import itertools, time
import numpy as np
from lib3 import sigma_c
from instance3 import PAR, T, BURN, EVERY, R0

t0 = time.time()
grad = np.load("d7a_grad.npy", allow_pickle=True).item()
names = ["F", "Q", "R", "Rc", "Rs", "psi", "gamma", "qc"]
r0c = 8.4311
rows = []
for a, b, c, d in itertools.product((-1, 1), repeat=4):
    lv = [a, b, c, d, b * c * d, a * c * d, a * b * c, a * b * d]
    kw = {nm: getattr(PAR, nm) * (1 + 0.01 * s) for nm, s in zip(names, lv)}
    r = sigma_c(PAR.with_(**kw), 16, T, BURN, EVERY, seed=7201)["r"]
    pred = r0c + 0.01 * sum(grad[nm] * s for nm, s in zip(names, lv))
    bad = r0c - 0.01 * sum(grad[nm] * s for nm, s in zip(names, lv))
    rows.append((lv, r, pred, bad))
    print(f"{lv}: r(A) {r:.4f}  first-order {pred:.4f}  (flipped-sign model {bad:.4f})", flush=True)
rs = np.array([x[1] for x in rows]); er = np.array([x[1] - x[2] for x in rows]); eb = np.array([x[1] - x[3] for x in rows])
print(f"design: min {rs.min():.4f} max {rs.max():.4f}; all in [7.9, 9.05): {bool(np.all((rs >= R0) & (rs < 9.05)))}; "
      f"max |r - first order| {np.abs(er).max():.4f}; NEG flipped-sign max error {np.abs(eb).max():.4f}  "
      f"({time.time()-t0:.0f}s)", flush=True)
for lab, sg in (("lower", -1), ("upper", +1)):
    kw = {nm: getattr(PAR, nm) * (1 + sg * 0.01 * np.sign(g)) for nm, g in grad.items()}
    f = sigma_c(PAR.with_(proto="frozen", **kw), 40, T, BURN, EVERY, seed=7202)
    print(f"frozen {lab} corner: r(A) {f['r']:.4f} +/- {f['se_r']:.4f}; in [7.9, 9.05): {R0 <= f['r'] < 9.05}  "
          f"({time.time()-t0:.0f}s)", flush=True)
print(f"total {time.time()-t0:.0f}s")
