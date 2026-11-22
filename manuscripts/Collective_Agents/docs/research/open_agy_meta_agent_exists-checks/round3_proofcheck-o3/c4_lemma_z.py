r"""Fresh-context check of C4 (Lemma Z).

Claim: if Pi is PD and diffusive (off-diagonals <= 0, row sums >= 0), then
Sigma = Pi^{-1} satisfies
  Z1  Sigma >= 0 entrywise,
  Z2  Sigma_ij > 0 iff i, j lie in one component of the coupling graph {a_ij > 0},
  Z3  Sigma_ij Sigma_jk <= Sigma_ik Sigma_jj for distinct i, j, k,
  Z4  every principal submatrix of Sigma has a Z-matrix inverse.

Declared expectations (before running):
  A. PD diffusive draws (with several components): 0 violations of Z1-Z4.
  B. PD Z-matrices with some NEGATIVE row sums: 0 violations of Z1-Z4
     (the proof never uses row sums; C3a and C5(b) rely on this strengthening).
  C. Negative control, PD matrices with at least one positive off-diagonal entry:
     Z4 fails for S = V in every draw (by construction), and Z1 or Z3 fails in a
     positive fraction of draws.
  D. Negative control, random Wishart covariances: Z3 fails in a positive fraction.
"""
import itertools
import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np

rng = np.random.default_rng(20261121)
TOL = 1e-12


def components(adj: np.ndarray) -> list[set[int]]:
    n = adj.shape[0]
    seen, comps = set(), []
    for s in range(n):
        if s in seen:
            continue
        stack, comp = [s], set()
        while stack:
            v = stack.pop()
            if v in comp:
                continue
            comp.add(v)
            stack.extend(int(w) for w in np.nonzero(adj[v])[0] if w not in comp)
        seen |= comp
        comps.append(comp)
    return comps


def check_z(Pi: np.ndarray) -> dict[str, int]:
    n = Pi.shape[0]
    Sig = np.linalg.inv(Pi)
    scale = np.max(np.abs(Sig))
    out = {"Z1": 0, "Z2": 0, "Z3": 0, "Z4": 0}
    if np.min(Sig) < -TOL * scale:
        out["Z1"] = 1
    adj = (-Pi > TOL * np.max(np.abs(Pi))) & ~np.eye(n, dtype=bool)
    comp_of = {}
    for c_idx, comp in enumerate(components(adj)):
        for v in comp:
            comp_of[v] = c_idx
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            same = comp_of[i] == comp_of[j]
            pos = Sig[i, j] > 1e-10 * scale
            if same != pos:
                out["Z2"] = 1
    for i, j, k in itertools.permutations(range(n), 3):
        if Sig[i, j] * Sig[j, k] > Sig[i, k] * Sig[j, j] + TOL * scale**2:
            out["Z3"] = 1
            break
    for r in range(2, n + 1):
        for S in itertools.combinations(range(n), r):
            S = list(S)
            M = np.linalg.inv(Sig[np.ix_(S, S)])
            off = M - np.diag(np.diag(M))
            if np.max(off) > 1e-9 * np.max(np.abs(M)):
                out["Z4"] = 1
                break
        if out["Z4"]:
            break
    return out


def draw_diffusive(n: int) -> np.ndarray:
    # random block structure (1-3 components), random sparse couplings inside blocks
    ncomp = rng.integers(1, 4)
    labels = rng.integers(0, ncomp, size=n)
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            if labels[i] == labels[j] and rng.random() < 0.7:
                A[i, j] = A[j, i] = rng.exponential(1.0)
    eps = rng.exponential(0.3, size=n) * (rng.random(n) < 0.6)
    # every connected component of the coupling graph needs a positive leak for PD
    for comp in components(A > 0):
        idx = np.array(sorted(comp))
        if np.all(eps[idx] == 0):
            eps[rng.choice(idx)] = rng.exponential(0.3) + 0.01
    L = np.diag(A.sum(1)) - A
    Pi = np.diag(eps) + L
    return Pi


def draw_pd_z_negative_rowsum(n: int) -> np.ndarray:
    B = rng.exponential(1.0, size=(n, n)) * (rng.random((n, n)) < 0.6)
    B = (B + B.T) / 2
    np.fill_diagonal(B, rng.exponential(1.0, size=n))
    lam = np.max(np.linalg.eigvalsh(B))
    s = lam * (1 + 0.05 * rng.random()) + 1e-3
    Pi = s * np.eye(n) - B
    return Pi


def draw_pd_non_z(n: int) -> np.ndarray:
    while True:
        Pi = draw_diffusive(n)
        i, j = rng.choice(n, size=2, replace=False)
        Pi[i, j] = Pi[j, i] = abs(Pi[i, j]) + rng.exponential(0.5) + 0.05
        if np.min(np.linalg.eigvalsh(Pi)) > 1e-6:
            return Pi


n = 6
ndraw = 300
res = {}
for name, gen in [("A_diffusive", draw_diffusive), ("B_PDZ_negrow", draw_pd_z_negative_rowsum), ("C_nonZ", draw_pd_non_z)]:
    counts = {"Z1": 0, "Z2": 0, "Z3": 0, "Z4": 0, "Z1orZ3": 0}
    negrows = 0
    for _ in range(ndraw):
        Pi = gen(n)
        assert np.min(np.linalg.eigvalsh(Pi)) > 0
        if np.min(Pi.sum(1)) < -1e-12:
            negrows += 1
        o = check_z(Pi)
        for k in o:
            counts[k] += o[k]
        counts["Z1orZ3"] += int(o["Z1"] or o["Z3"])
    res[name] = (counts, negrows)
    print(f"{name}: draws={ndraw}, draws with a negative row sum={negrows}, violations={counts}")

# D: Wishart covariances
z3_fail = 0
for _ in range(ndraw):
    X = rng.standard_normal((n, n + 2))
    Sig = X @ X.T
    for i, j, k in itertools.permutations(range(n), 3):
        if Sig[i, j] * Sig[j, k] > Sig[i, k] * Sig[j, j] + 1e-12:
            z3_fail += 1
            break
print(f"D_wishart: Z3 violated in {z3_fail}/{ndraw}")

ok = (sum(v for k, v in res["A_diffusive"][0].items() if k != "Z1orZ3") == 0
      and sum(v for k, v in res["B_PDZ_negrow"][0].items() if k != "Z1orZ3") == 0
      and res["B_PDZ_negrow"][1] > 0
      and res["C_nonZ"][0]["Z4"] == ndraw and res["C_nonZ"][0]["Z1orZ3"] > 0 and z3_fail > 0)
print("EXPECTATIONS MET:", ok)
