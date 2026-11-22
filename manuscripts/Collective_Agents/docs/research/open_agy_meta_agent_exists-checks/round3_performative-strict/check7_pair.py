r"""check7: the pure-collider pair (TDF with one-agent departments, no message channel anywhere).

Population: two firms, each = {b, s}; b senses eta^{3f}, s senses eta^{3f+1} (R = 1, F = 0.9, Q = 0.05); both regulate
the renewed outcome eta^{3f+2} = h (eta^{3f} - eta^{3f+1}) + beta (u_b + u_s) + w^Z with the D2 act rule
(gamma = 68, Lam = 1, beta = h = 1, sE2 = 1/32, s2 = 0.01, kappa = 0.68), QZ = 0.05, qc = 1e-4.
Declared expectations BEFORE running:
  E1 full Pi diffusive; r(pair) > 1; window (rbar, r(pair)] nonempty under clause (c) mean coupling (N = 4);
  E2 N_eff and N_hab: Pi diagonal on each pair, r(pair) = 1 exactly (up to 1e-12), nothing selected;
  E3 memory: each member's eta_t-coordinate prior mean is an exact AR(1) given its input, d_M = 0 (<= 1e-12);
  E4 inference: alpha_I of order qc / U (computation noise only), below 1e-3;
  E5 agency index in (0, 1);
  E6 every inter-agent message channel is absent, so N_lp, N_rn, N_fr, N_pr, N_inf are inapplicable (no
     computation: the interventions leave the model unchanged); Omega_int(C | zeta_{V\C}) = 0 exactly by causal
     separation (prop:agy-nulls-vanish(a), 05_agency.tex:311).
  NEG kappa = 0: r(pair) = 1.
"""
import numpy as np
from scipy.optimize import minimize_scalar
import lgx
from tdf import tdf_spec, groups

F, Q, R, qc, QZ = 0.9, 0.05, 1.0, 1e-4, 0.05
gamma, Lam, beta, h, sE2 = 68.0, 1.0, 1.0, 1.0, 1.0 / 32.0
s2 = 1.0 / (1.0 / sE2 + gamma * Lam * beta ** 2)
KAP = gamma * Lam * beta * h * s2
G = groups(1, 2)

if __name__ == "__main__":
    for kap in (0.0, KAP, 2 * KAP):
        sp = tdf_spec(1, 2, kappa=kap, sa2=s2, qc=qc, QZ=QZ)
        Pf = np.linalg.inv(lgx.sigma_c(sp, "full", 60))
        Pe = np.linalg.inv(lgx.sigma_private(sp, "eff"))
        Ph = np.linalg.inv(lgx.sigma_c(sp, "hab", 60))
        df = lgx.diffusivity(Pf)
        rP = lgx.contrast(Pf, G["C0"])["r"]
        rb = lgx.baseline_mean_coupling(Pf)
        others = [(round(r, 4), C) for r, C, _ in lgx.all_regions(Pf, top=0) if C not in (G["C0"], G["C1"])][:2]
        print(f"kappa={kap:.3f}: full diffusive={df['diffusive']}; r(pair)={rP:.5f}; rbar={rb:.5f}; "
              f"window=({max(rb, others[0][0]):.5f}, {rP:.5f}]; next regions {others}")
        print(f"   Pi(full) firm 0: {np.array2string(Pf[:2, :2], precision=4)}")
        print(f"   N_eff r(pair)={lgx.contrast(Pe, G['C0'])['r']:.12f}, offdiag {Pe[0, 1]:.2e}; "
              f"N_hab r(pair)={lgx.contrast(Ph, G['C0'])['r']:.12f}")
        if kap > 0:
            mid = 0.5 * (max(rb, others[0][0]) + rP)
            print(f"   selected at r0={mid:.4f}: full {lgx.selected(Pf, mid, rb)}; N_eff {lgx.selected(Pe, mid, rb)}; "
                  f"N_hab {lgx.selected(Ph, mid, rb)}")
    # memory and inference for one member (no relays): scalar filter on (eta_t, eta_{t-1}) with own sensor only
    sp = tdf_spec(1, 2, kappa=KAP, sa2=s2, qc=qc, QZ=QZ)
    mod = lgx.build(sp, "full")
    Kg = mod["gains"][0]["K"]          # 2 x 1
    Pm = mod["gains"][0]["P"]
    AF = np.array([[F, 0.0], [1.0, 0.0]])
    Ai = AF @ (np.eye(2) - Kg @ np.array([[1.0, 0.0]]))
    print(f"[memory] interior matrix A_F(I-KH) = {np.array2string(Ai, precision=5)}; first row only reads the first "
          f"coordinate: |A_01| = {abs(Ai[0, 1]):.1e}, so m^-_0 is an exact AR(1) given the input and d_M = 0")
    # inference: union predictive for eta_t from this member's own sensor without computation noise
    PU = Q
    for _ in range(100000):
        Pp = 1.0 / (1.0 / PU + 1.0 / R)
        PUn = F * F * Pp + Q
        if abs(PUn - PU) < 1e-16:
            break
        PU = PUn
    KU = Pp / R
    k0 = Kg[0, 0]
    # E(y - u)^2: y_{t+1} = F(1-k0) y + F k0 s + qcn ; u_{t+1} = F(1-KU) u + F KU s ; d = y - u
    # d_{t+1} = F(1-k0) d + F(KU - k0)(u - s) ... compute via a 3-state stationary system (eta, y, u)
    A = np.array([[F, 0, 0], [F * k0, F * (1 - k0), 0], [F * KU, 0, F * (1 - KU)]])
    Gm = np.array([[np.sqrt(Q), 0, 0], [0, F * k0 * np.sqrt(R), np.sqrt(qc)], [0, F * KU * np.sqrt(R), 0]])
    S = lgx.stat_cov(A, Gm @ Gm.T)
    dv = np.array([0, 1, -1])
    msd = float(dv @ S @ dv)
    print(f"[inference] member gain k0={k0:.6f} vs union gain {KU:.6f}; E(y-u)^2={msd:.3e}; alpha_I per member = "
          f"{0.5 * msd / PU:.3e}; pair = {msd / PU:.3e}")
    # agency (D2) for firm 0, decision states from the stationary law of the two members' act means
    C0 = list(G["C0"])
    P = lgx.stat_cov(mod["A"], mod["Qx"])
    Ux = mod["Ux"][C0]; Un = mod["Un"][C0].copy(); Un[:, mod["n_a"]] = 0.0
    Cmu = Ux @ P @ Ux.T + (Un * mod["sd"] ** 2) @ Un.T
    MU = np.random.default_rng(7).multivariate_normal(np.zeros(2), 0.5 * (Cmu + Cmu.T), size=300)
    sig = np.array([1.0, -1.0]); n = 2

    def kl(m1, S1, m2, S2):
        S2i = np.linalg.inv(S2); dm = m2 - m1
        return 0.5 * (np.trace(S2i @ S1) + dm @ S2i @ dm - len(m1) + np.log(np.linalg.det(S2) / np.linalg.det(S1)))

    def group(gC, zC):
        Gam = np.eye(n) / sE2 + gC * Lam * beta ** 2 * np.ones((n, n)); Si = np.linalg.inv(Gam)
        return -gC * Lam * beta * zC * Si @ np.ones(n), Si

    zC = lambda mu: h * ((-mu / (KAP * sig))[0] - (-mu / (KAP * sig))[1])
    den = sum(kl(mu, s2 * np.eye(n), np.zeros(n), sE2 * np.eye(n)) for mu in MU)
    f = lambda lg: sum(kl(mu, s2 * np.eye(n), *group(np.exp(lg), zC(mu))) for mu in MU)
    grid = np.linspace(-8, 10, 73); vals = [f(x) for x in grid]; j = int(np.argmin(vals))
    res = minimize_scalar(f, bracket=(grid[j - 1], grid[j], grid[j + 1]))
    print(f"[agency] pair, D2: index = {1 - min(res.fun, vals[j]) / den:.4f} (best gamma_C {np.exp(res.x):.3f}); "
          f"mean KL(P||E) = {den / len(MU):.3f} nats")
