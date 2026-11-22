r"""O6 check A (exact algebra): the scalar Riccati map of instance I* and its contraction constants.

Objects (record C11; lib.py of round2_epistemic_persistent, functions Pminus and posterior):
  prior covariance of x_{t+1} = (eta_{t+1}, eta_t) from the posterior variance p of eta_t:
      P^-(p) = [[F^2 p + Q + qc, F p], [F p, p + qc]] = p u u^T + Qt,  u = (F, 1)^T,  Qt = diag(Q + qc, qc);
  update with observation precision D = diag(a, b) on (eta_t, eta_{t-1}),
      a = 1/R + (open slots read)/Rs,  b = (relays read)/(R + Rc);
  scalar Riccati map g(p; a, b) = [((P^-)^{-1} + D)^{-1}]_{00};
  closed-loop error matrix of the exact filter M = A_F (I - K H) = A_F (I + P^- D)^{-1},  A_F = [[F, 0], [1, 0]].

Claims to verify (declared before running; all must print PASS):
  S1  g(p) = (c1 p + c0)/(d1 p + d0) with c1 = F^2 + b K1, c0 = Qp (1 + b qc), d1 = a F^2 + b + a b K1,
      d0 = (1 + a Qp)(1 + b qc), where Qp = Q + qc and K1 = F^2 qc + Qp  (a Moebius map with positive coefficients);
  S2  c1 d0 - c0 d1 = F^2 (1 + b qc)^2, hence g'(p) = F^2 (1 + b qc)^2/(d1 p + d0)^2 <= F^2/(1 + a Qp)^2;
  S3  M = u v^T is rank one and the scalar closed-loop factor lambda = v^T u = F (1 + b qc)/(d1 p + d0) > 0,
      with lambda^2 = g'(p); hence products M_k...M_1 = u (prod_{j>=2} lambda_j) v_1^T;
  N1  numerical: closed forms equal lib.posterior / direct linear algebra to relative 1e-12 at 2000 random points;
  N2  on the I* policy set (a = 1/R + n/Rs, n = 0..4; b = m/(R+Rc), m = 0..3) and p in [0, 0.2], the largest
      g'(p) is below rho_bar = (F/(1 + Qp/R))^2 = 0.7346 and the largest lambda is below lambda_bar = 0.8571.
NEGATIVE CONTROLS (must print FAIL-as-expected):
  X1  a perturbed closed form (qc dropped from d0) disagrees with lib.posterior by more than 1e-6 relative;
  X2  without a structural own sensor and with F = 1.2 (a = 0 allowed), sup g' > 1: no uniform contraction.
"""
import os
import sys
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[_v] = "1"
LIB = r"C:/Users/chris and christine/Desktop/Research/manuscripts/Collective_Agents/docs/research/open_agy_meta_agent_exists-checks/round2_epistemic_persistent"
sys.path.insert(0, LIB)
import numpy as np
import sympy as sp
from lib import Par, Pminus, posterior

F, Q, qc, p, a, b = sp.symbols("F Q q_c p a b", positive=True)
Qp = Q + qc
Pm = sp.Matrix([[F**2 * p + Qp, F * p], [F * p, p + qc]])
D = sp.diag(a, b)
Pplus = (Pm.inv() + D).inv()
g = sp.simplify(Pplus[0, 0])
K1 = F**2 * qc + Qp
c1, c0 = F**2 + b * K1, Qp * (1 + b * qc)
d1, d0 = a * F**2 + b + a * b * K1, (1 + a * Qp) * (1 + b * qc)
ok_S1 = sp.simplify(g - (c1 * p + c0) / (d1 * p + d0)) == 0
print(f"S1 Moebius form of g: {'PASS' if ok_S1 else 'FAIL'}")
ok_S2a = sp.expand(c1 * d0 - c0 * d1 - F**2 * (1 + b * qc)**2) == 0
gp = sp.simplify(sp.diff(g, p))
ok_S2b = sp.simplify(gp - F**2 * (1 + b * qc)**2 / (d1 * p + d0)**2) == 0
print(f"S2 determinant c1 d0 - c0 d1 = F^2 (1 + b qc)^2: {'PASS' if ok_S2a else 'FAIL'}; "
      f"g'(p) formula: {'PASS' if ok_S2b else 'FAIL'}")
u = sp.Matrix([F, 1])
AF = sp.Matrix([[F, 0], [1, 0]])
Minv = (sp.eye(2) + Pm * D).inv()
M = AF * Minv
v = Minv[0, :].T
ok_rank1 = sp.simplify(M - u * v.T) == sp.zeros(2, 2)
lam = sp.simplify((v.T * u)[0, 0])
ok_lam = sp.simplify(lam - F * (1 + b * qc) / (d1 * p + d0)) == 0
ok_lam2 = sp.simplify(lam**2 - gp) == 0
# exact-filter identity used in the text: (I - K H) = P^+ (P^-)^{-1} = (I + P^- D)^{-1}
ok_IKH = sp.simplify(Pplus * Pm.inv() - Minv) == sp.zeros(2, 2)
# P^-(p) = p u u^T + Qt
ok_Pm = sp.simplify(Pm - (p * u * u.T + sp.diag(Qp, qc))) == sp.zeros(2, 2)
print(f"S3 M = u v^T: {'PASS' if ok_rank1 else 'FAIL'}; lambda = F(1+b qc)/(d1 p + d0): {'PASS' if ok_lam else 'FAIL'}; "
      f"lambda^2 = g': {'PASS' if ok_lam2 else 'FAIL'}; (I-KH) = (I+P^-D)^-1: {'PASS' if ok_IKH else 'FAIL'}; "
      f"P^- = p u u^T + Qt: {'PASS' if ok_Pm else 'FAIL'}")

# ---------------- numerical N1 / X1 ----------------
rng = np.random.default_rng(6060)
fg = sp.lambdify((F, Q, qc, p, a, b), (c1 * p + c0) / (d1 * p + d0), "numpy")
fbad = sp.lambdify((F, Q, qc, p, a, b), (c1 * p + c0) / (d1 * p + (1 + a * Qp)), "numpy")
flam = sp.lambdify((F, Q, qc, p, a, b), F * (1 + b * qc) / (d1 * p + d0), "numpy")
err, errbad, errlam = 0.0, 0.0, 0.0
for _ in range(2000):
    Fv, Qv, qcv = rng.uniform(0.1, 0.99), rng.uniform(1e-3, 0.5), 10 ** rng.uniform(-6, -1)
    pv, av, bv = rng.uniform(0, 1), rng.uniform(0.2, 5), rng.uniform(0, 5)
    par = Par(F=Fv, Q=Qv, qc=qcv)
    ref = posterior(Pminus(par, pv), av, bv)[0, 0]
    err = max(err, abs(fg(Fv, Qv, qcv, pv, av, bv) - ref) / ref)
    errbad = max(errbad, abs(fbad(Fv, Qv, qcv, pv, av, bv) - ref) / ref)
    Pmv = Pminus(par, pv)
    Mv = np.array([[Fv, 0], [1, 0]]) @ np.linalg.inv(np.eye(2) + Pmv @ np.diag([av, bv]))
    lam_num = np.trace(Mv)            # rank one: trace = v^T u
    errlam = max(errlam, abs(lam_num - flam(Fv, Qv, qcv, pv, av, bv)) / abs(lam_num))
print(f"N1 closed form vs lib.posterior: max rel err {err:.2e} -> {'PASS' if err < 1e-12 else 'FAIL'}; "
      f"lambda vs trace of direct M: max rel err {errlam:.2e} -> {'PASS' if errlam < 1e-12 else 'FAIL'}")
print(f"X1 perturbed closed form (qc dropped from d0): max rel err {errbad:.2e} -> "
      f"{'FAIL-as-expected' if errbad > 1e-6 else 'UNEXPECTED PASS'}")

# ---------------- N2: contraction constants on the I* policy set ----------------
I = Par(F=0.9, Q=0.05, R=1.0, Rc=0.1, Rs=2.0, Rsh=0.0, psi=0.024, gamma=400.0, qc=1e-4, n=4, n_zero=4, kmsg=3)
fgp = sp.lambdify((F, Q, qc, p, a, b), F**2 * (1 + b * qc)**2 / (d1 * p + d0)**2, "numpy")
ps = np.linspace(0.0, 0.2, 4001)
gmax, lmax = 0.0, 0.0
for nslot in range(5):
    for m in range(4):
        av, bv = 1 / I.R + nslot / I.Rs, m / (I.R + I.Rc)
        gmax = max(gmax, float(np.max(fgp(I.F, I.Q, I.qc, ps, av, bv))))
        lmax = max(lmax, float(np.max(flam(I.F, I.Q, I.qc, ps, av, bv))))
rho_bar = (I.F / (1 + (I.Q + I.qc) / I.R)) ** 2
lam_bar = I.F / (1 + (I.Q + I.qc) / I.R)
print(f"N2 I*: sup g' on policy set x [0,0.2] = {gmax:.6f} (proved bound rho_bar = {rho_bar:.6f}) -> "
      f"{'PASS' if gmax <= rho_bar + 1e-15 else 'FAIL'}; sup lambda = {lmax:.6f} (bound {lam_bar:.6f}) -> "
      f"{'PASS' if lmax <= lam_bar + 1e-15 else 'FAIL'}")
# fixed points and the invariant interval
def fixed(av, bv, x=0.05):
    for _ in range(5000):
        x = float(fg(I.F, I.Q, I.qc, x, av, bv))
    return x
p_hi = fixed(1 / I.R, 0.0)
p_lo = fixed(1 / I.R + I.n / I.Rs, I.kmsg / (I.R + I.Rc))
print(f"    invariant interval J = [p_lo, p_hi] = [{p_lo:.6f}, {p_hi:.6f}]; lambda on J at most "
      f"{max(float(np.max(flam(I.F, I.Q, I.qc, np.linspace(p_lo, p_hi, 2001), 1/I.R + k/I.Rs, m/(I.R+I.Rc)))) for k in range(5) for m in range(4)):.6f}")

# ---------------- X2: negative control, no structural sensor and F > 1 ----------------
Fx = 1.2
gx = max(float(np.max(fgp(Fx, 0.05, 1e-4, ps, 0.0, 0.0))), 0.0)
print(f"X2 F=1.2, a=b=0 allowed: sup g' = {gx:.4f} -> {'FAIL-as-expected (no uniform contraction)' if gx > 1 else 'UNEXPECTED PASS'}")
