r"""Attack A1-A3 on the performative niche candidate PN (g = 0.05, F = 0.9, Q = 0.05, R = 1, Rc = 0.2, b = 0.2, n = 4).

Declared expectations (written before running):
 (A1) Base mode (investigator's filters, U as known input): windowed Pi^c of one niche is diffusive and compound
      symmetric, r = closed form 24.4989 to <= 1e-6 relative; at g = 0 it is 28.5.  NEG: the closed form at
      g = 0.06 differs from the g = 0.05 window value by more than 1e-2 (the check can fail).
 (A2) N_ex applicability.  prop:fw-performative(b) (s02_framework.tex:96-104): an act set from beliefs is also a
      message.  Expectation: in the base process the member's estimate has MSE P^+ = 0.0832..., while the exact
      conditional variance of eta_t given the member's own information set (private data to t, U to t-1) and,
      separately, given that set plus U(t), is strictly smaller.  NEG control: at g = 0 (U == 0) the exact
      conditional variance equals the filter's MSE (to 1e-9), so the test can fail.
 (A3) Exact-fusion null N_ex (members condition exactly on all their data, U included): Pi^c of the niche;
      expectation: diffusive by exchangeability; contrast unknown in advance (heuristic: above 24.5).  NEG control:
      exact mode at g = 0 must reproduce the no-act value 28.5 (to 1e-4).
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import time
import numpy as np
from win import build, world_conditional, contrast_block, closed_form

F, Q, R, Rc, b, n = 0.9, 0.05, 1.0, 0.2, 0.2, 4
T, TS = 70, 40

if __name__ == "__main__":
    t0 = time.time()
    print("== A1 base-mode reconstruction ==")
    for g in [0.05, 0.0]:
        mod = build(F, Q, R, Rc, b, g, T, mode="base")
        S = world_conditional(mod, TS)
        Pi = np.linalg.inv(S)
        c = contrast_block(Pi)
        cf = closed_form(n, F, Q, R, Rc, b, g)
        print("  g=%.2f window r=%.8f closed form %.8f rel.diff %.2e | diffusive=%s max_off=%.4e min_row=%.4e cs_dev=%.1e" % (
            g, c["r"], cf, abs(c["r"] - cf) / cf, c["diffusive"], c["max_off"], c["min_row"], c["cs_dev"]))
        if g == 0.05:
            r_base = c["r"]
            print("  alpha=%.6e v=%.6e" % (1 / c["xin"], 1 / c["xout"]))
    print("  NEG: closed form at g=0.06 = %.6f vs window at g=0.05 %.6f (must differ by > 1e-2)" % (
        closed_form(n, F, Q, R, Rc, b, 0.06), r_base))

    print("== A2 is the public act informative to a base-mode member? ==")
    for g in [0.05, 0.0]:
        mod = build(F, Q, R, Rc, b, g, 60, mode="base", probe_t=40)
        p = mod["probe"]
        print("  g=%.2f MSE(member m^+)=%.8f  claimed P^+=%.8f  Var(eta_t|info set: private to t, U to t-1)=%.8f  "
              "Var(eta_t|info set + U(t))=%.8f" % (g, p["mse_member_estimate"], p["Pp_claimed"], p["var_given_info_set"],
                                                    p["var_given_info_set_plus_U_t"]))

    print("== A3 exact-fusion null ==")
    for g in [0.0, 0.05]:
        mod = build(F, Q, R, Rc, b, g, T, mode="exact")
        S = world_conditional(mod, TS)
        Pi = np.linalg.inv(S)
        c = contrast_block(Pi)
        Mp = mod["Mp"][TS]
        eta_t = mod["eta"][TS]
        mse = np.mean([float((Mp[i] - eta_t) @ (Mp[i] - eta_t)) for i in range(n)])
        print("  exact g=%.2f: r=%.6f diffusive=%s max_off=%.4e min_row=%.4e cs_dev=%.1e  MSE(m^+)=%.6f" % (
            g, c["r"], c["diffusive"], c["max_off"], c["min_row"], c["cs_dev"], mse))
        print("     Sigma^c diag %.6e off %.6e" % (np.mean(np.diag(S)), (S.sum() - np.trace(S)) / (n * (n - 1))))
    # window-convergence check for the exact mode
    mod = build(F, Q, R, Rc, b, 0.05, 80, mode="exact")
    c2 = contrast_block(np.linalg.inv(world_conditional(mod, 48)))
    print("  exact g=0.05 window check (T=80, t*=48): r=%.6f" % c2["r"])
    print("elapsed %.1f s" % (time.time() - t0))
