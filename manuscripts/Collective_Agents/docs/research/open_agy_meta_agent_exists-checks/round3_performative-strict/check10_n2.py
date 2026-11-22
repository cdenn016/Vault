r"""check10: n = 2 blocks (not covered by Theorem O when loadings differ).  A = 2 relaying members on component 0 acting
on component 0 (or on a renewed component 2) with loadings kappa_1, kappa_2; B = 2 members on component 1, no acts.
Declared expectation BEFORE running: same-sign unequal loadings give r_full(A) <= r_eff(A) in every diffusive draw (the
static argument (c1-c2)^2 < (c1+c2)^2 <= ... suggests it; unproved dynamically); opposite-sign loadings with relays:
no prediction (escape possible when r_eff(A) is small)."""
import numpy as np, lgx
rng = np.random.default_rng(5)
for label, opp in (("same-sign", False), ("opposite-sign", True)):
    up, nd, nn, worst = 0, 0, 0, -np.inf
    for _ in range(300):
        F = rng.uniform(0.3, 0.95, 2); Qw = rng.uniform(0.01, 0.2, 2)
        R, Rc = rng.uniform(0.3, 3), rng.uniform(0.05, 3.0)
        k1, k2 = rng.uniform(0.05, 1.0, 2)
        if opp: k2 = -k2
        Z = int(rng.integers(0, 2)) * 2
        Fw = np.zeros((3, 3)); Fw[0, 0], Fw[1, 1] = F
        ag = [{"k": 0, "R": R, "senders": [1], "kappa": k1, "Z": Z, "beta": 0.5, "sa2": 0.01, "readacts": []},
              {"k": 0, "R": R, "senders": [0], "kappa": k2, "Z": Z, "beta": 0.5, "sa2": 0.01, "readacts": []},
              {"k": 1, "R": R, "senders": [3], "kappa": 0.0, "Z": -1, "beta": 0.0, "sa2": 0.0, "readacts": []},
              {"k": 1, "R": R, "senders": [2], "kappa": 0.0, "Z": -1, "beta": 0.0, "sa2": 0.0, "readacts": []}]
        sp = {"Fw": Fw, "Qw": list(Qw) + [0.05], "Rc": Rc, "qc": 0.0, "agents": ag}
        try:
            if max(abs(np.linalg.eigvals(lgx.build(sp)["A"]))) >= 0.995: continue
        except Exception: continue
        nn += 1
        Pf = np.linalg.inv(lgx.sigma_c(sp, "full", 40)); Pe = np.linalg.inv(lgx.sigma_private(sp, "eff"))
        if lgx.diffusivity(Pf)["diffusive"]:
            nd += 1
            g = lgx.contrast(Pf, [0, 1])["r"] / lgx.contrast(Pe, [0, 1])["r"] - 1
            worst = max(worst, g); up += g > 1e-9
    print(f"{label}: draws {nn}, diffusive {nd}, r_full > r_eff in {up}, max relative gain {worst:.3e}")
