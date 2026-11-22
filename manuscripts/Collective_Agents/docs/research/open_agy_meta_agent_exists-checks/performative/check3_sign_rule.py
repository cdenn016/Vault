r"""Check 3: sign rule for the collider entries between two exchangeable firms.

Claim under test (derived by hand, see report): for two exchangeable firms with all-to-all raw relays
inside each firm, exact-gain filters, deterministic acts u_j = -g_k m_j^+, members reading their own
firm's realized acts and predicting the other firm's act as mu_k * (-g_o n_o m_i^+) (mu_k in {0,1}),
no channel between the firms, the C1-C2 entries of Pi^c all have the sign of phi_1 phi_2, where
phi_k = F - b g_k n_k - mu_k b g_o n_o is firm k's conditional closed-loop coefficient.

Declared expectations:
 (E1) phi_1, phi_2 > 0: cross entries > 0 (non-diffusive).            [C3 regime]
 (E2) phi_1 < 0 < phi_2: cross entries < 0.                           [C3 fails]
 (E3) phi_1, phi_2 < 0: cross entries > 0.                            [negative control for E2]
 (E4) In E2 cases with strong in-firm sharing (small Rc), the whole Pi^c can be diffusive.
 The world must be stable: |F - b(g_1 n_1 + g_2 n_2)| < 1.
"""
import numpy as np
from pc import build_population, world_conditional_cov, diffusivity, contrast


def spec_two(n1, n2, F, Q, R, Rc, b, g1, g2, mu1, mu2):
    N = n1 + n2
    C1 = list(range(n1)); C2 = list(range(n1, N))
    firm = [0] * n1 + [1] * n2
    reads = [[j for j in (C1 if firm[i] == 0 else C2) if j != i] for i in range(N)]
    known = [set(C1) if firm[i] == 0 else set(C2) for i in range(N)]
    return firm, C1, C2, {"F": [F], "Qw": [Q], "comp": [0] * N, "R": [R] * N, "reads": reads, "Rc": Rc,
                          "act_comp": [0] * N, "g": [g1] * n1 + [g2] * n2, "b": b, "known": known}


def build_spliced(n1, n2, F, Q, R, Rc, b, g1, g2, mu1, mu2):
    """Direct construction (no splicing): exchangeable firms, exact formulas."""
    from pc import riccati_scalar
    N = n1 + n2
    firm = [0] * n1 + [1] * n2
    n = [n1, n2]; g = [g1, g2]; mu = [mu1, mu2]
    gains = []
    for k in range(2):
        o = 1 - k
        Feff = F - mu[k] * b * g[o] * n[o]
        Pm, Pp = riccati_scalar(Feff, Q, 1.0 / R + (n[k] - 1) / (R + Rc))
        gains.append((Pp / R, Pp / (R + Rc), Feff))
    # noises: w, v_1..v_N, nu_i (aggregated relay noise of receiver i, variance (n_k-1) Rc)
    d = 1 + N
    nxi = 1 + N + N
    # m^+_i = c_i m_i + (ks + (n-1)kc) eta + ks v_i + kc sum_{j in firm, j!=i} v_j + kc nu_i
    Cm = np.zeros((N, N)); Ceta = np.zeros((N, 1)); D = np.zeros((N, nxi))
    for i in range(N):
        k = firm[i]; ks, kc, _ = gains[k]
        mates = [j for j in range(N) if firm[j] == k and j != i]
        Cm[i, i] = 1 - ks - len(mates) * kc
        Ceta[i, 0] = ks + len(mates) * kc
        D[i, 1 + i] = ks * np.sqrt(R)
        for j in mates:
            D[i, 1 + j] = kc * np.sqrt(R)
        D[i, 1 + N + i] = kc * np.sqrt(len(mates) * Rc)
    gv = np.array([g[firm[i]] for i in range(N)])
    # u = -diag(g) m^+
    A = np.zeros((d, d)); G = np.zeros((d, nxi))
    # eta' = F eta + b sum u + w
    A[0, 0] = F - b * (gv @ Ceta[:, 0])
    A[0, 1:] = -b * (gv @ Cm)
    G[0, 0] = np.sqrt(Q)
    G[0, :] += -b * (gv @ D)
    # m_i' = Feff_i m_i^+ + b * sum_{j in own firm} u_j
    for i in range(N):
        k = firm[i]; Feff = gains[k][2]
        own = [j for j in range(N) if firm[j] == k]
        rowm = Feff * Cm[i] - b * sum(gv[j] * Cm[j] for j in own)
        roweta = Feff * Ceta[i, 0] - b * sum(gv[j] * Ceta[j, 0] for j in own)
        rowG = Feff * D[i] - b * sum(gv[j] * D[j] for j in own)
        A[1 + i, 1:] = rowm; A[1 + i, 0] = roweta; G[1 + i] = rowG
    return A, G @ G.T, list(range(n1)), list(range(n1, N))


if __name__ == "__main__":
    F, Q, R, b = 0.9, 0.05, 1.0, 0.2
    n1 = n2 = 4
    cases = [
        # (label, Rc, g1, g2, mu1, mu2)
        ("E1 both undershoot, ignore", 1.0, 0.3, 0.3, 0, 0),
        ("E1 both model other", 1.0, 0.3, 0.3, 1, 1),
        ("E2 firm1 overshoots, ignore", 1.0, 1.5, 0.2, 0, 0),
        ("E2 firm1 overshoots, ignore, Rc=0.02", 0.02, 1.5, 0.2, 0, 0),
        ("E2 mu1=1 mu2=0, g=0.8 both", 0.02, 0.8, 0.8, 1, 0),
        ("E3 both overshoot, ignore", 1.0, 1.5, 1.5, 0, 0),
        ("E3 both overshoot, ignore, Rc=0.02", 0.02, 1.5, 1.5, 0, 0),
    ]
    for label, Rc, g1, g2, mu1, mu2 in cases:
        A, Qx, C1, C2 = build_spliced(n1, n2, F, Q, R, Rc, b, g1, g2, mu1, mu2)
        phi1 = F - b * g1 * n1 - mu1 * b * g2 * n2
        phi2 = F - b * g2 * n2 - mu2 * b * g1 * n1
        world = F - b * (g1 * n1 + g2 * n2)
        Scs = {}
        for L in (80, 140):
            Scs[L] = world_conditional_cov(A, Qx, [0], list(range(1, 1 + n1 + n2)), L)
        conv = np.max(np.abs(Scs[140] - Scs[80])) / np.max(np.abs(Scs[140]))
        Pi = np.linalg.inv(Scs[140])
        cross = Pi[np.ix_(C1, C2)]
        dif = diffusivity(Pi)
        line = "%-38s phi1=%+.3f phi2=%+.3f world=%+.3f | cross in [%.4e, %.4e] | conv %.1e | diffusive=%s" % (
            label, phi1, phi2, world, cross.min(), cross.max(), conv, dif["diffusive"])
        print(line)
        if dif["diffusive"]:
            r1 = contrast(Pi, C1); r2 = contrast(Pi, C2)
            print("     r(C1)=%.4f (cut %.4f)  r(C2)=%.4f (cut %.4f)  r(V)=%.4f" % (
                r1["r"], r1["cut"], r2["r"], r2["cut"], contrast(Pi, C1 + C2)["r"]))
        else:
            off = Pi - np.diag(np.diag(Pi))
            print("     within-C1 offdiag max %.3e, within-C2 offdiag max %.3e" % (
                off[np.ix_(C1, C1)].max(), off[np.ix_(C2, C2)].max()))
