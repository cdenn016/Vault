r"""check1: randomized checks of the obstruction theorems O1 and O2 (proved by hand; numerics guard the algebra).

Population: niche A (component 0, n_A members, common R_A, all-to-all relays) and niche B (component 1, n_B members,
all-to-all relays), literal latency, exact filters, random F, Q, R, Rc, qc.  C = A.

Families and declared expectations BEFORE running:
  O1 (symmetric act loadings on A; A's members may read A's total realized act, with act noise; B acts on its own
      component, on A's component (with either sign) or not at all; no relay between A and B):
      E-O1: in every draw with a diffusive full precision, r_full(A) <= r_eff(A) (tolerance 1e-9 relative);
            the disagreement eigenvalue of Sigma on D_A is the same in both laws; Sigma_full is exchangeable on A.
  O2 (heterogeneous, mixed-sign act loadings kappa_i on A's component, A's members do not read acts, n_A >= 3):
      E-O2: in every diffusive draw, r_full(A) <= r_eff(A).
  NEG-a (must escape): n_A = 2 with opposite-sign loadings and no relay at all: r_full(A) > r_eff(A) = 1 in every
      diffusive draw with kappa != 0.
  NEG-b (must escape in some draws): C = two departments of two (components 0 and 1, relays only inside a department)
      acting on a third component with opposite-sign loadings: r_full(C) > r_eff(C) in some draws.
  EXP-c (exploratory, no expectation): decoupling, A and B on the same component with complete bipartite relays
      between them, both acting with one sign; report how often r_full(A) > r_eff(A).
"""
import numpy as np
import lgx

rng = np.random.default_rng(20261121)


def niche_agents(n, k, R, senders_fn, kappa, Z, beta, sa2, readacts):
    return [{"k": k, "R": R, "senders": senders_fn(i), "kappa": kappa[i], "Z": Z, "beta": beta, "sa2": sa2,
             "readacts": readacts} for i in range(n)]


def eval_C(spec, C, L=40):
    Sf = lgx.sigma_c(spec, "full", L)
    Se = lgx.sigma_private(spec, "eff")
    Pf, Pe = np.linalg.inv(Sf), np.linalg.inv(Se)
    df, de = lgx.diffusivity(Pf), lgx.diffusivity(Pe)
    rf = lgx.contrast(Pf, C)["r"] if df["diffusive"] else np.nan
    re = lgx.contrast(Pe, C)["r"] if de["diffusive"] else np.nan
    return Sf, Se, df, de, rf, re


def stable(spec):
    try:
        m = lgx.build(spec, "full")
        return max(abs(np.linalg.eigvals(m["A"]))) < 0.995
    except Exception:
        return False


def family_O1(ndraw):
    viol, ndiff, nn, maxdev_alpha, maxdev_exch = 0, 0, 0, 0.0, 0.0
    worst = -np.inf
    for _ in range(ndraw):
        nA, nB = rng.integers(3, 5), rng.integers(2, 5)
        F = rng.uniform(0.3, 0.95, 2); Qw = rng.uniform(0.01, 0.2, 2)
        RA, RB, Rc = rng.uniform(0.3, 3), rng.uniform(0.3, 3), rng.uniform(0.05, 1.0)
        qc = rng.choice([0.0, 1e-4])
        gA = rng.uniform(-0.4, 0.4); bA = rng.uniform(0.1, 0.5)
        sa2A = rng.choice([0.0, rng.uniform(0, 0.05)])
        readA = bool(rng.integers(0, 2))
        A_idx = list(range(nA)); B_idx = list(range(nA, nA + nB))
        agA = niche_agents(nA, 0, RA, lambda i: [j for j in A_idx if j != i], [gA] * nA, 0, bA, sa2A,
                           A_idx if readA else [])
        ZB = int(rng.choice([-1, 1, 0]))
        gB = rng.uniform(-0.4, 0.4); bB = rng.uniform(0.1, 0.5)
        readB = A_idx if False else (B_idx if (ZB == 1 and rng.integers(0, 2)) else [])
        agB = niche_agents(nB, 1, RB, lambda i: [j for j in B_idx if j != i + nA], [gB] * nB, ZB, bB,
                           rng.choice([0.0, 0.02]), readB)
        spec = {"Fw": np.diag(F), "Qw": Qw, "Rc": Rc, "qc": qc, "agents": agA + agB}
        if not stable(spec):
            continue
        nn += 1
        Sf, Se, df, de, rf, re = eval_C(spec, A_idx)
        # exchangeability and disagreement eigenvalue on D_A
        SA_f, SA_e = Sf[np.ix_(A_idx, A_idx)], Se[np.ix_(A_idx, A_idx)]
        offs = SA_f[~np.eye(nA, dtype=bool)]
        maxdev_exch = max(maxdev_exch, (offs.max() - offs.min()) / SA_f.diagonal().mean())
        al_f = np.mean(SA_f.diagonal()) - np.mean(offs)
        offe = SA_e[~np.eye(nA, dtype=bool)]
        al_e = np.mean(SA_e.diagonal()) - np.mean(offe)
        maxdev_alpha = max(maxdev_alpha, abs(al_f - al_e) / al_e)
        if df["diffusive"]:
            ndiff += 1
            gap = (rf - re) / re
            worst = max(worst, gap)
            if gap > 1e-9:
                viol += 1
    print(f"O1: draws={nn}, diffusive={ndiff}, violations of r_full<=r_eff: {viol}, max (r_f-r_e)/r_e = {worst:.3e}")
    print(f"    max rel. deviation of disagreement eigenvalue (full vs eff) = {maxdev_alpha:.2e}; "
          f"max off-diagonal spread of Sigma_full on A = {maxdev_exch:.2e}")


def family_O2(ndraw):
    viol, ndiff, nn = 0, 0, 0
    worst = -np.inf
    for _ in range(ndraw):
        nA, nB = rng.integers(3, 6), rng.integers(2, 4)
        F = rng.uniform(0.3, 0.95, 2); Qw = rng.uniform(0.01, 0.2, 2)
        RA, RB, Rc = rng.uniform(0.3, 3), rng.uniform(0.3, 3), rng.uniform(0.05, 1.0)
        qc = rng.choice([0.0, 1e-4])
        A_idx = list(range(nA)); B_idx = list(range(nA, nA + nB))
        kap = rng.uniform(-1.0, 1.0, nA)
        bA = rng.uniform(0.1, 0.8)
        agA = niche_agents(nA, 0, RA, lambda i: [j for j in A_idx if j != i], kap, 0, bA,
                           rng.choice([0.0, 0.02]), [])
        agB = niche_agents(nB, 1, RB, lambda i: [j for j in B_idx if j != i + nA], [rng.uniform(-.3, .3)] * nB,
                           int(rng.choice([-1, 1])), 0.3, 0.0, [])
        spec = {"Fw": np.diag(F), "Qw": Qw, "Rc": Rc, "qc": qc, "agents": agA + agB}
        if not stable(spec):
            continue
        nn += 1
        Sf, Se, df, de, rf, re = eval_C(spec, A_idx)
        if df["diffusive"]:
            ndiff += 1
            gap = (rf - re) / re
            worst = max(worst, gap)
            if gap > 1e-9:
                viol += 1
    print(f"O2: draws={nn}, diffusive={ndiff}, violations of r_full<=r_eff: {viol}, max (r_f-r_e)/r_e = {worst:.3e}")


def neg_a(ndraw):
    esc, ndiff, nn = 0, 0, 0
    for _ in range(ndraw):
        F = rng.uniform(0.3, 0.95, 3); Qw = rng.uniform(0.01, 0.2, 3)
        R = rng.uniform(0.3, 3)
        kap = rng.uniform(0.2, 1.0)
        b = rng.uniform(0.2, 1.0)
        Fw = np.diag(F); Fw[2, 2] = 0.0
        ag = [{"k": 0, "R": R, "senders": [], "kappa": kap, "Z": 2, "beta": b, "sa2": 0.01, "readacts": []},
              {"k": 1, "R": R, "senders": [], "kappa": -kap, "Z": 2, "beta": b, "sa2": 0.01, "readacts": []}]
        spec = {"Fw": Fw, "Qw": Qw, "Rc": 0.1, "qc": 0.0, "agents": ag}
        nn += 1
        Sf, Se, df, de, rf, re = eval_C(spec, [0, 1])
        if df["diffusive"]:
            ndiff += 1
            esc += int(rf > re + 1e-9)
    print(f"NEG-a (pair, opposite signs, no relay): draws={nn}, diffusive={ndiff}, r_full>r_eff in {esc}")


def neg_b(ndraw):
    esc, ndiff, nn, best = 0, 0, 0, 0.0
    for _ in range(ndraw):
        F = rng.uniform(0.5, 0.95); Q = rng.uniform(0.01, 0.2)
        R, Rc = rng.uniform(0.3, 3), rng.uniform(0.05, 1.0)
        kap = rng.uniform(0.2, 1.0); b = rng.uniform(0.2, 1.5)
        Fw = np.diag([F, F, 0.0])
        ag = [{"k": 0, "R": R, "senders": [1], "kappa": kap, "Z": 2, "beta": b, "sa2": 0.01, "readacts": []},
              {"k": 0, "R": R, "senders": [0], "kappa": kap, "Z": 2, "beta": b, "sa2": 0.01, "readacts": []},
              {"k": 1, "R": R, "senders": [3], "kappa": -kap, "Z": 2, "beta": b, "sa2": 0.01, "readacts": []},
              {"k": 1, "R": R, "senders": [2], "kappa": -kap, "Z": 2, "beta": b, "sa2": 0.01, "readacts": []}]
        spec = {"Fw": Fw, "Qw": [Q, Q, 0.05], "Rc": Rc, "qc": 0.0, "agents": ag}
        nn += 1
        Sf, Se, df, de, rf, re = eval_C(spec, [0, 1, 2, 3])
        if df["diffusive"]:
            ndiff += 1
            if rf > re + 1e-9:
                esc += 1
                best = max(best, rf / re)
    print(f"NEG-b (two departments, opposite signs): draws={nn}, diffusive={ndiff}, r_full>r_eff in {esc}, "
          f"max r_full/r_eff = {best:.3f}")


def exp_c(ndraw):
    up, ndiff, nn, best = 0, 0, 0, 0.0
    for _ in range(ndraw):
        nA, nB = 3, 3
        F = rng.uniform(0.5, 0.95); Q = rng.uniform(0.01, 0.2)
        RA, RB = rng.uniform(0.3, 3), rng.uniform(0.3, 3)
        Rc = rng.uniform(0.05, 1.0)
        A_idx, B_idx = [0, 1, 2], [3, 4, 5]
        kA, kB = rng.uniform(0.05, 0.5), rng.uniform(0.05, 1.5)
        b = rng.uniform(0.1, 0.6)
        cross = bool(rng.integers(0, 2))
        agA = [{"k": 0, "R": RA, "senders": [j for j in A_idx if j != i] + (B_idx if cross else []),
                "kappa": kA, "Z": 0, "beta": b, "sa2": 0.0, "readacts": []} for i in A_idx]
        agB = [{"k": 0, "R": RB, "senders": [j for j in B_idx if j != i] + (A_idx if cross else []),
                "kappa": kB, "Z": 0, "beta": b, "sa2": 0.0, "readacts": []} for i in B_idx]
        spec = {"Fw": np.diag([F]), "Qw": [Q], "Rc": Rc, "qc": 0.0, "agents": agA + agB}
        if not stable(spec):
            continue
        nn += 1
        Sf, Se, df, de, rf, re = eval_C(spec, A_idx)
        if df["diffusive"] and de["diffusive"]:
            ndiff += 1
            if rf > re + 1e-9:
                up += 1
                best = max(best, rf / re)
    print(f"EXP-c (decoupling, same sign, bipartite relays in about half the draws): draws={nn}, both diffusive="
          f"{ndiff}, r_full>r_eff in {up}, max ratio {best:.4f}")


if __name__ == "__main__":
    family_O1(200)
    family_O2(200)
    neg_a(60)
    neg_b(80)
    exp_c(150)
