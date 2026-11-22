r"""Check 2: two collectives on one conditioned world variable (collider) vs routes (a) and (c).

Population: scalar world eta (F, Q); firms C1 = {0..n1-1}, C2 = {n1..n1+n2-1}; all members sense eta
(noise R_i); members relay raw observations to their own firm only (all-to-all inside the firm, noise Rc);
each member reads its own firm's realized acts exactly and models the other firm's acts as -g_j m_i^+.
Acts u_j = -g_j m_j^+ enter eta with loading b.

Declared expectations:
 (E1) Both firms acting (g1, g2 > 0), no cross channels: every C1-C2 entry of Pi^c is > 0
      (collider), so Pi^c is not diffusive, at every g tested.
 (E2) As g -> 0 (g1 = g2 = g), the largest C1-C2 entry scales as g^2 (first-order collider).
 (E3) Route (a): only C1 acts (g2 = 0): all C1-C2 entries vanish (conditional independence), to
      round-off; diffusivity then is decided inside C1 alone.
 (E4) Route (c), one delegate per firm (one actor in each firm): C1-C2 entries between the delegates
      positive -> non-diffusive.  One delegate in C1 only: C1-C2 entries vanish.
 Negative control (N1): b = 0 (acts without effect): all C1-C2 entries vanish.
"""
import numpy as np
from pc import build_population, world_conditional_cov, diffusivity, contrast


def spec_two(n1, n2, F, Q, R, Rc, b, g, known_own=True):
    N = n1 + n2
    C1 = list(range(n1)); C2 = list(range(n1, N))
    firm = [0] * n1 + [1] * n2
    reads = [[j for j in (C1 if firm[i] == 0 else C2) if j != i] for i in range(N)]
    known = [set(C1) if firm[i] == 0 else set(C2) for i in range(N)] if known_own else [set() for _ in range(N)]
    return {"F": [F], "Qw": [Q], "comp": [0] * N, "R": list(R), "reads": reads, "Rc": Rc,
            "act_comp": [0] * N, "g": list(g), "b": b, "known": known, "model_unknown": True}, C1, C2


def analyze(spec, C1, C2, L=120):
    mod = build_population(spec)
    Sc = world_conditional_cov(mod["A"], mod["Qx"], mod["iw"], mod["ia"], L)
    Pi = np.linalg.inv(Sc)
    cross = Pi[np.ix_(C1, C2)]
    w1 = Pi[np.ix_(C1, C1)] - np.diag(np.diag(Pi[np.ix_(C1, C1)]))
    dif = diffusivity(Pi)
    return Pi, cross, w1, dif


if __name__ == "__main__":
    F, Q, b = 0.9, 0.05, 0.2
    n1 = n2 = 4
    R = [1.0] * 8
    Rc = 1.0
    print("== E1/E2: both firms act, homogeneous R, no cross channels ==")
    prev = None
    for g in [0.0, 0.005, 0.01, 0.02, 0.05, 0.15, 0.3]:
        spec, C1, C2 = spec_two(n1, n2, F, Q, R, Rc, b, [g] * 8)
        Pi, cross, w1, dif = analyze(spec, C1, C2)
        line = "g=%.3f  cross min=%.4e max=%.4e  within-C1 offdiag max=%.4e  diffusive=%s" % (
            g, cross.min(), cross.max(), w1.max(), dif["diffusive"])
        if g > 0:
            line += "  cross/g^2=%.5f" % (cross.max() / g ** 2)
        print(line)
    print("== heterogeneous sensing noise (0.5,1,2,4 | 1,1,2,2), g=0.15 ==")
    spec, C1, C2 = spec_two(4, 4, F, Q, [0.5, 1, 2, 4, 1, 1, 2, 2], Rc, b, [0.15] * 8)
    Pi, cross, w1, dif = analyze(spec, C1, C2)
    print("cross min=%.4e max=%.4e within-C1 offdiag max=%.4e diffusive=%s" % (cross.min(), cross.max(), w1.max(), dif["diffusive"]))
    print(np.array2string(Pi, precision=4, max_line_width=200))
    print("== E3: route (a), only C1 acts ==")
    for g in [0.05, 0.15, 0.3]:
        spec, C1, C2 = spec_two(n1, n2, F, Q, R, Rc, b, [g] * 4 + [0.0] * 4)
        Pi, cross, w1, dif = analyze(spec, C1, C2)
        c = contrast(Pi, C1)["r"] if dif["diffusive"] else float("nan")
        print("g=%.3f  max|cross|=%.3e  within-C1 offdiag max=%.4e  diffusive=%s  r(C1)=%.5f" % (
            g, np.abs(cross).max(), w1.max(), dif["diffusive"], c))
    print("== E4: route (c) delegates ==")
    for g in [0.05, 0.15, 0.3]:
        gv = [0.0] * 8; gv[0] = g * 4; gv[4] = g * 4
        spec, C1, C2 = spec_two(n1, n2, F, Q, R, Rc, b, gv)
        Pi, cross, w1, dif = analyze(spec, C1, C2)
        print("two delegates g_D=%.2f: cross[0,4]=%.4e  cross max=%.4e min=%.4e  diffusive=%s" % (
            g * 4, Pi[0, 4], cross.max(), cross.min(), dif["diffusive"]))
        gv = [0.0] * 8; gv[0] = g * 4
        spec, C1, C2 = spec_two(n1, n2, F, Q, R, Rc, b, gv)
        Pi, cross, w1, dif = analyze(spec, C1, C2)
        c = contrast(Pi, C1)["r"] if dif["diffusive"] else float("nan")
        print("one delegate in C1 g_D=%.2f: max|cross|=%.3e  within-C1 offdiag max=%.4e  diffusive=%s  r(C1)=%.5f" % (
            g * 4, np.abs(cross).max(), w1.max(), dif["diffusive"], c))
        print("   within-C1 block of Pi:", np.array2string(Pi[np.ix_(C1, C1)], precision=4, max_line_width=200))
    print("== N1: negative control b = 0 ==")
    spec, C1, C2 = spec_two(n1, n2, F, Q, R, Rc, 0.0, [0.3] * 8)
    Pi, cross, w1, dif = analyze(spec, C1, C2)
    print("b=0: max|cross|=%.3e diffusive=%s" % (np.abs(cross).max(), dif["diffusive"]))
