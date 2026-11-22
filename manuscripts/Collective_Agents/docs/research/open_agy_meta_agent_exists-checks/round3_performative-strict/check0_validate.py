r"""check0: validation of lgx.py against round-1 attack A8 (attack-performative/a8_out.txt).

Population PN under literal one-round latency: two niches of four, F=0.9, Q=0.05, R=1, Rc=0.2, qc=0, all-to-all raw
relays inside each niche; acts u_j = -g m^+_{j,0}, b=0.2, members of a niche read the niche's realized total act
(known input).  Declared expectations BEFORE running:
  E1  no acts:          r(A) = 7.425938 (a8: 7.425938377967279), to 1e-5 relative;
  E2  acts g = 0.05:    r(A) = 6.169015 (a8: 6.169015190410915), to 1e-4 relative (a8 used a one-sided window);
  E3  Lemma M identification: the N_eff world-conditional covariance computed by window conditioning equals the
      stationary covariance of the private-noise response (Lyapunov) to 1e-9;
  E4  Lemma M inequality: Sigma_full <= Sigma_eff in Loewner order (smallest eigenvalue of the gap >= -1e-10);
  NEG1 (must fail E1's value): Rc = 1e6 gives r(A) within 1e-3 of 1 (no relay information);
  NEG2 (must violate E4's reversed order): Sigma_eff <= Sigma_full fails (gap has a negative eigenvalue < -1e-6).
"""
import numpy as np
import lgx

F, Q, R, b = 0.9, 0.05, 1.0, 0.2


def pn_spec(g: float, Rc: float = 0.2, qc: float = 0.0) -> dict:
    ag = []
    for i in range(8):
        k = 0 if i < 4 else 1
        mates = [j for j in range(8) if j != i and (j < 4) == (i < 4)]
        niche = [j for j in range(8) if (j < 4) == (i < 4)]
        ag.append({"k": k, "R": R, "senders": mates, "kappa": g if g else 0.0, "Z": k if g else -1, "beta": b,
                   "sa2": 0.0, "readacts": niche if g else []})
    return {"Fw": np.diag([F, F]), "Qw": [Q, Q], "Rc": Rc, "qc": qc, "agents": ag}


def rA(S: np.ndarray) -> float:
    return lgx.contrast(np.linalg.inv(S), range(4))["r"]


if __name__ == "__main__":
    for L in (40, 80):
        S0 = lgx.sigma_c(pn_spec(0.0), "full", L)
        print(f"E1 L={L}: r(A) no acts = {rA(S0):.9f}  (expect 7.425938)")
    for L in (40, 80):
        S1 = lgx.sigma_c(pn_spec(0.05), "full", L)
        print(f"E2 L={L}: r(A) acts g=0.05 = {rA(S1):.9f}  (expect 6.169015)")
    Seff_w = lgx.sigma_c(pn_spec(0.05), "eff", 80)
    Seff_p = lgx.sigma_private(pn_spec(0.05), "eff")
    print(f"E3: max|Sigma_eff(window) - Sigma_private| = {np.max(np.abs(Seff_w - Seff_p)):.3e}")
    print(f"    r(A) under N_eff = {rA(Seff_w):.6f};  r(A) full = {rA(S1):.6f}")
    print(f"E4: min eig(Sigma_eff - Sigma_full) = {lgx.loewner_gap(Seff_w, S1):.3e}")
    print(f"NEG2: min eig(Sigma_full - Sigma_eff) = {lgx.loewner_gap(S1, Seff_w):.3e}  (must be < -1e-6)")
    Sneg = lgx.sigma_c(pn_spec(0.0, Rc=1e6), "full", 40)
    print(f"NEG1: Rc=1e6 r(A) = {rA(Sneg):.6f}  (must be within 1e-3 of 1)")
