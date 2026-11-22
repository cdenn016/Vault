r"""Check 4: route (b) across collectives (cross reading vs collider) and route (d) (acts on an
unsensed world component).  Also cross-validates pcg.build against check3.build_spliced.

Declared expectations:
 (V)  pcg.build and check3.build_spliced give the same Sigma^c (rel. diff <= 1e-10) on two cases.
 (B)  Two EFE-consistent firms (phi_k > 0) on one price, every member also reads every member of the
      other firm with relay noise Rc_x: for large Rc_x the cross entries are > 0 (collider dominates,
      non-diffusive); below some Rc_x they become < 0 (shared sources dominate) and Pi^c can be diffusive;
      contrast of each firm falls as Rc_x falls.  We report whether each firm is a collective against the
      exchangeable mean-coupling baseline (def:col-baseline (c), mean coupling, uniform leak = mean leak).
 (D1) Two niches sensing exogenous components S_A, S_B, each acting only on its own unsensed component
      P_A, P_B: cross entries = 0, diffusive, contrast below the no-act value (collider only).
 (D2) Both niches acting on one unsensed component P: cross entries > 0 (sign rule with phi_k = F_S > 0),
      non-diffusive.
"""
import numpy as np
from pc import world_conditional_cov, diffusivity, contrast
from pcg import build
from check3_sign_rule import build_spliced


def mean_coupling_baseline(Pi):
    N = Pi.shape[0]
    a = -(Pi - np.diag(np.diag(Pi)))
    abar = a[np.triu_indices(N, 1)].mean()
    epsbar = Pi.sum(axis=1).mean()
    return 1 + N * abar / epsbar  # whole exchangeable population attains the sup (uniform leak)


def two_firm_spec(n, F, Q, R, Rc, Rcx, b, g, mu=1.0, cross=True):
    N = 2 * n
    C1 = list(range(n)); C2 = list(range(n, N))
    firm = [0] * n + [1] * n
    reads, Rcd = [], {}
    for i in range(N):
        own = [j for j in (C1 if firm[i] == 0 else C2) if j != i]
        oth = (C2 if firm[i] == 0 else C1) if cross else []
        reads.append(own + oth)
        for j in own:
            Rcd[(i, j)] = Rc
        for j in oth:
            Rcd[(i, j)] = Rcx
    known = [set(C1) if firm[i] == 0 else set(C2) for i in range(N)]
    return C1, C2, {"F": [F], "Qw": [Q], "comp": [0] * N, "R": [R] * N, "reads": reads, "Rc": Rcd,
                    "act": [0] * N, "g": [g] * N, "b": b, "known": known, "mu": [mu] * N}


if __name__ == "__main__":
    F, Q, R, b = 0.9, 0.05, 1.0, 0.2
    n = 4
    print("== (V) cross-validation of builders ==")
    for (Rc, g1, g2, mu1, mu2) in [(1.0, 0.3, 0.3, 1, 1), (0.02, 1.5, 0.2, 0, 0)]:
        A1, Q1, C1, C2 = build_spliced(n, n, F, Q, R, Rc, b, g1, g2, mu1, mu2)
        S1 = world_conditional_cov(A1, Q1, [0], list(range(1, 2 * n + 1)), 100)
        _, _, sp = two_firm_spec(n, F, Q, R, Rc, 1.0, b, 0.0, cross=False)
        sp["g"] = [g1] * n + [g2] * n; sp["mu"] = [mu1] * n + [mu2] * n
        m = build(sp)
        S2 = world_conditional_cov(m["A"], m["Qx"], m["iw"], m["ia"], 100)
        print("  case Rc=%.2f g=(%.2f,%.2f) mu=(%d,%d): rel diff %.2e" % (Rc, g1, g2, mu1, mu2, np.max(np.abs(S1 - S2)) / np.max(np.abs(S1))))

    print("== (B) two EFE-consistent firms with cross reading, g=0.15, mu=1, Rc=0.2 ==")
    phi = F - b * 0.15 * 2 * n
    print("  phi_k = F - b g (n1+n2) = %.3f > 0" % phi)
    for Rcx in [1e6, 1e3, 300.0, 100.0, 30.0, 10.0, 3.0, 1.0]:
        C1, C2, sp = two_firm_spec(n, F, Q, R, 0.2, Rcx, b, 0.15, mu=1.0)
        m = build(sp)
        Sc = world_conditional_cov(m["A"], m["Qx"], m["iw"], m["ia"], 120)
        Pi = np.linalg.inv(Sc)
        cross = Pi[np.ix_(C1, C2)]
        dif = diffusivity(Pi)
        s = "  Rcx=%-8g cross in [%+.4e, %+.4e] diffusive=%s" % (Rcx, cross.min(), cross.max(), dif["diffusive"])
        if dif["diffusive"]:
            c1 = contrast(Pi, C1); base = mean_coupling_baseline(Pi)
            s += "  r(C1)=%.4f cut=%.4f  r(V)=%.4f  rbar_hom(mean coupling)=%.4f  collective=%s" % (
                c1["r"], c1["cut"], contrast(Pi, C1 + C2)["r"], base, c1["r"] > base)
        print(s)

    print("== (D1) niches act on their own unsensed components ==")
    # components: 0 = S_A, 1 = S_B, 2 = P_A, 3 = P_B
    for g in [0.0, 0.15, 0.5]:
        N = 2 * n; C1 = list(range(n)); C2 = list(range(n, N))
        comp = [0] * n + [1] * n
        reads = [[j for j in (C1 if i < n else C2) if j != i] for i in range(N)]
        Rcd = {(i, j): 0.2 for i in range(N) for j in reads[i]}
        sp = {"F": [F, F, 0.8, 0.8], "Qw": [Q, Q, Q, Q], "comp": comp, "R": [R] * N, "reads": reads, "Rc": Rcd,
              "act": [2] * n + [3] * n, "g": [g] * N, "b": b, "known": [set() for _ in range(N)], "mu": [0.0] * N}
        m = build(sp)
        Sc = world_conditional_cov(m["A"], m["Qx"], m["iw"], m["ia"], 120)
        Pi = np.linalg.inv(Sc); dif = diffusivity(Pi)
        cross = Pi[np.ix_(C1, C2)]
        s = "  g=%.2f max|cross|=%.2e diffusive=%s" % (g, np.abs(cross).max(), dif["diffusive"])
        if dif["diffusive"]:
            s += "  r(C1)=%.4f" % contrast(Pi, C1)["r"]
        print(s)
    print("== (D2) both niches act on one unsensed component P ==")
    for g in [0.05, 0.15, 0.5]:
        N = 2 * n; C1 = list(range(n)); C2 = list(range(n, N))
        comp = [0] * n + [1] * n
        reads = [[j for j in (C1 if i < n else C2) if j != i] for i in range(N)]
        Rcd = {(i, j): 0.2 for i in range(N) for j in reads[i]}
        sp = {"F": [F, F, 0.8], "Qw": [Q, Q, Q], "comp": comp, "R": [R] * N, "reads": reads, "Rc": Rcd,
              "act": [2] * N, "g": [g] * N, "b": b, "known": [set() for _ in range(N)], "mu": [0.0] * N}
        m = build(sp)
        Sc = world_conditional_cov(m["A"], m["Qx"], m["iw"], m["ia"], 120)
        Pi = np.linalg.inv(Sc); dif = diffusivity(Pi)
        cross = Pi[np.ix_(C1, C2)]
        print("  g=%.2f cross in [%+.3e, %+.3e] diffusive=%s" % (g, cross.min(), cross.max(), dif["diffusive"]))
