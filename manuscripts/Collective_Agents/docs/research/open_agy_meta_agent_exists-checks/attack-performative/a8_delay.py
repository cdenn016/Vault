r"""Attack A8: PN under the literal one-round channel latency of def:fw-system (02_framework.tex:15).

A relay of s_j(t-1) is read at round t: y_ij(t) = eta_{t-1} + v_j(t-1) + nu_ij(t).  Each member runs the exact
time-varying Kalman filter on x_t = (eta_t, eta_{t-1}) with the public act as known input (the investigator's member
model).  Error rows over standardized noises are propagated exactly; Pi^c is the inverse of the second moment of
Cov(e(t*) | eta path) over attention sequences (exact for fixed attention and for no-act nulls; P(a|eta) ~ P(a) with
acts).  Computes PN (fixed attention on niche-mates), the annealed habit null (uniform 3 of 7, no acts), the annealed
partner-randomization null (uniform 3 of 7, acts kept) and the mechanism baseline M1 (8 agents, one component, 3
uniformly random partners, acts).

Declared expectations: PN at delay 1 reproduces r(A) = 6.169015 of a5 (validation; NEG: the same code with the relay
read at delay 0 must give 24.498926); the every-constant differ clause against N_hab holds under latency iff
M1_delay > N_hab_delay (no prediction made).
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np

F, Q, R, Rc, b = 0.9, 0.05, 1.0, 0.2, 0.2


def run(mode: str, g: float, nsamp: int, delay: int = 1, T: int = 60, ts: int = 45, seed: int = 0) -> float:
    rng = np.random.default_rng(seed)
    N = 8
    if mode == "M1":
        comp = [0] * 8
        members = list(range(8))
    else:
        comp = [0] * 4 + [1] * 4
        members = list(range(4))
    pairs = [(i, j) for i in range(N) for j in range(N) if i != j]
    pidx = {p: q for q, p in enumerate(pairs)}
    per = 1 + N + len(pairs)
    NT = 1 + per * T
    sig0 = np.sqrt(Q / (1 - F * F))
    A = np.array([[F, 0.0], [1.0, 0.0]])
    covs, Ks_list, Seta_list = [], [], []
    for s in range(nsamp):
        eta = np.zeros((T + 1, NT)); eta[0, 0] = sig0
        # prior error rows of x_t = (eta_t, eta_{t-1}) for each member; start: estimate 0, eta_{-1} ~ treat as eta_0/F
        err = {i: np.zeros((2, NT)) for i in members}
        P = {i: np.diag([Q / (1 - F * F), Q / (1 - F * F)]) for i in members}
        etam1 = np.zeros(NT); etam1[0] = sig0  # crude eta_{-1} := eta_0 (start transient only)
        for i in members:
            err[i][0] = -eta[0]; err[i][1] = -etam1
        Erows = None
        prev_v = None
        for t in range(T):
            base = 1 + per * t
            if t == ts:
                Erows = np.array([err[i][0] for i in members])
            vrow = lambda k: (base + 1 + k)
            post = {}
            for i in members:
                if mode == "fixed":
                    part = [j for j in members if j != i]
                else:
                    others = [j for j in range(N) if j != i]
                    part = list(rng.choice(others, size=3, replace=False))
                inf = [j for j in part if comp[j] == comp[i]]
                Hs, Rs, noise_rows = [], [], []
                # own sensing of eta_t
                Hs.append([1.0, 0.0]); Rs.append(R)
                nr = np.zeros(NT); nr[vrow(i)] = np.sqrt(R); noise_rows.append(nr)
                for j in inf:
                    if delay == 1:
                        if t == 0:
                            continue
                        Hs.append([0.0, 1.0]); Rs.append(R + Rc)
                        nr = np.zeros(NT); nr[1 + per * (t - 1) + 1 + j] = np.sqrt(R)
                    else:
                        Hs.append([1.0, 0.0]); Rs.append(R + Rc)
                        nr = np.zeros(NT); nr[vrow(j)] = np.sqrt(R)
                    nr[base + 1 + N + pidx[(i, j)]] = np.sqrt(Rc)
                    noise_rows.append(nr)
                H = np.array(Hs); Rm = np.diag(Rs)
                S = H @ P[i] @ H.T + Rm
                K = P[i] @ H.T @ np.linalg.inv(S)
                Pp = (np.eye(2) - K @ H) @ P[i]
                # posterior error: (I - K H) err + K * noise
                e_post = (np.eye(2) - K @ H) @ err[i] + K @ np.array(noise_rows)
                post[i] = e_post
                P[i] = A @ Pp @ A.T + np.diag([Q, 0.0])
            U = -g * sum(eta[t] + post[i][0] for i in members)
            eta[t + 1] = F * eta[t] + b * U
            eta[t + 1][base] += np.sqrt(Q)
            for i in members:
                # predicted error of (eta_{t+1}, eta_t): A e_post - (w_t, 0); acts are known inputs and cancel
                new = A @ post[i]
                new[0][base] -= np.sqrt(Q)
                err[i] = new
        Hm = eta
        G = Hm @ Hm.T
        C_eh = Erows @ Hm.T
        Ka = np.linalg.solve(G, C_eh.T).T
        covs.append(Erows @ Erows.T - Ka @ C_eh.T)
        Ks_list.append(Ka); Seta_list.append(G)
    S_eta = np.mean(Seta_list, axis=0)
    Kbar = np.mean(Ks_list, axis=0)
    mix = np.mean([K @ S_eta @ K.T for K in Ks_list], axis=0) - Kbar @ S_eta @ Kbar.T
    Sig = np.mean(covs, axis=0) + mix
    n = len(members)
    diag = np.mean(np.diag(Sig)); off = (Sig.sum() - np.trace(Sig)) / (n * (n - 1))
    Pi = np.linalg.inv(0.5 * (Sig + Sig.T))
    offd = Pi - np.diag(np.diag(Pi))
    return (diag - off + n * off) / (diag - off), float(offd.max()), float(Pi.sum(axis=1).min())


if __name__ == "__main__":
    print("PN delay 0 (NEG/validation, expect 24.498926):", run("fixed", 0.05, 1, delay=0))
    print("PN delay 1 (expect 6.169015):", run("fixed", 0.05, 1, delay=1))
    print("PN delay 1, no acts:", run("fixed", 0.0, 1, delay=1))
    print("N_hab annealed delay 1 (no acts):", run("hab", 0.0, 600, delay=1, seed=1))
    print("N_pr annealed delay 1 (acts g=0.05):", run("hab", 0.05, 600, delay=1, seed=2))
    print("M1 delay 1 (acts g=0.05):", run("M1", 0.05, 150, delay=1, seed=3))
    print("M1 delay 1 (no acts):", run("M1", 0.0, 150, delay=1, seed=4))
