r"""Check 3: sign of the residual off-diagonal second moment under N_fr with the real-time (P4) scheduler.
Declared expectation: the exact E[Cov(e|eta,pi)] part is diagonal; the policy-mixture part is of order 1e-6 and may
be negative (the shared uniform scheduler makes revision times mutually exclusive); either way no region of the null
reaches contrast 1.1, so the null selects no collective at any admissible r0."""
from lib import sigma_c
from instance import PAR, T, BURN, EVERY
res = sigma_c(PAR, "real_fr", 120, T, BURN, EVERY, seed=4404, dead_var=PAR.Rc)
print(f"N_fr (real-time): alpha={res['alpha']:.7f} beta={res['beta']:.3e} +/- {res['se_beta']:.1e}; "
      f"E[Cov] beta={res['beta_priv']:.1e}; r(A)={res['r']:.5f}")
