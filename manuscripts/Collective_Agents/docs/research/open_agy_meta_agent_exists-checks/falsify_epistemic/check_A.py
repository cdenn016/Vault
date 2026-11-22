"""Check A: blind recomputation at the declared instance, with expected outcomes stated first.

Expected (investigator's values): P(S)=[.0059,.095,.331,.4051,.1629]; alpha=0.015111, beta=0.200540; r(A)=54.0861;
other regions <= 2.8599, mixed <= 1; mechanism medium sup 18.5982 (whole medium); mean-coupling 46.5024;
Agency 0.999891 (gamma_C 4.192); alpha_I (encoded N(ybar,Pbar)) 0.007655; N_hab 4.3523; N_pr annealed 4.1399.
"""
import os
for k in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[k] = "1"
import math
import numpy as np
from fx import *

n, N, kappa = 4, 8, 3
P0, Rs, Rc, gam, s2 = 1.0, 1.0, 0.1, 4.0, 1e-3
out = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(line)
    out.append(line)


# ---- slot law from the (P4) chain built from members' own EFEs (P2: hear all open co-members) ----
Gfull = lambda i, x, So: finfo(x / Rs + So / (Rs + Rc), P0)
profs, law, db = stationary_chain(n, Gfull, gam)
d = [finfo(1 / Rs + k / (Rs + Rc), P0) - finfo(k / (Rs + Rc), P0) for k in range(n)]
g = np.concatenate([[0.0], np.cumsum(d)])
gibbs = np.exp(-gam * g[profs.sum(1)])
gibbs /= gibbs.sum()
say("A0 expect chain = Gibbs exp(-gamma g(S)) and detailed balance ~1e-16:", np.abs(law - gibbs).max(), db)
Gneg = lambda i, x, So: finfo(x * [1.0, 1.3, 0.8, 1.0][i] / Rs + So / (Rs + Rc), P0)
_, _, dbn = stationary_chain(n, Gneg, gam)
say("A0 negative control (heterogeneous own precision) expect detailed balance violated (>1e-6):", dbn)
say("A0 P(S=0..4):", np.round([law[profs.sum(1) == k].sum() for k in range(n + 1)], 4))

# ---- full model Sigma^c ----
SA = sigma_c(n, law, N - 1, kappa, np.inf, P0, Rs, Rc, s2)
SA_nm = sigma_c(n, law, N - 1, kappa, np.inf, P0, Rs, Rc, s2, mean_term=False)
alpha, beta = SA[0, 0] - SA[0, 1], SA[0, 1]
say("B  alpha", alpha, "beta", beta, "| beta without mean term", SA_nm[0, 1], "| exch spread",
    np.ptp(np.diag(SA)), np.ptp(SA[~np.eye(n, dtype=bool)]))
Pi = np.linalg.inv(blockdiag(SA, SA))
dif, offmax = is_diffusive(Pi)
say("B  diffusive", dif, "max offdiag", offmax, "| leak", Pi.sum(1)[0], "| coupling", -Pi[0, 1], "| cross", Pi[0, n])
regs = {C: contrast(Pi, C) for C in all_regions(N)}
rA = regs[tuple(range(n))]
oth = [r for C, r in regs.items() if C not in (tuple(range(n)), tuple(range(n, N)))]
mixed = [r for C, r in regs.items() if min(C) < n <= max(C)]
say("B  r(A)", rA, "1+n beta/alpha", 1 + n * beta / alpha, "| max other region", max(oth), "| max mixed", max(mixed))

# ---- negative control: an independent-noise block (beta=0) must give r = 1 ----
Pc = np.linalg.inv(np.eye(4) * 0.3)
say("B  control beta=0 block: r", contrast(Pc, range(4)), "(expect 1)")

# ---- Monte Carlo check of Sigma^c (independent seed) ----
rng = np.random.default_rng(424242)
T = 300000
kk = rng.choice(len(profs), size=T, p=law)
p = profs[kk].astype(float)
eta = rng.normal(0, math.sqrt(P0), T)
v = rng.normal(0, math.sqrt(Rs), (T, n))
s = eta[:, None] + v
e = np.zeros((T, n))
invL = np.zeros((T, n))
for i in range(n):
    So = p.sum(1) - p[:, i]
    Lam = 1 / P0 + p[:, i] / Rs + So / (Rs + Rc)
    tot = p[:, i] * s[:, i] / Rs
    for j in range(n):
        if j != i:
            tot = tot + p[:, j] * (s[:, j] + rng.normal(0, math.sqrt(Rc), T)) / (Rs + Rc)
    e[:, i] = tot / Lam + rng.normal(0, math.sqrt(s2), T) - eta
    invL[:, i] = 1 / Lam
hbar = invL.mean(0) / P0
M2 = e.T @ e / T - P0 * np.outer(hbar, hbar)
se = np.std(e[:, 0] * e[:, 1]) / math.sqrt(T)
say("B  MC beta", M2[0, 1], "exact", beta, "z", (M2[0, 1] - beta) / se, "| control (no mean term) z",
    (M2[0, 1] - SA_nm[0, 1]) / se)

# ---- comparison media ----
Gmed = lambda i, x, So: finfo(x / Rs + min(kappa, So) / (Rs + Rc), P0)
profN, lawN, _ = stationary_chain(N, Gmed, gam)
SH = sigma_c(N, lawN, N - 1, kappa, np.inf, P0, Rs, Rc, s2)
PiH = np.linalg.inv(SH)
regH = {C: contrast(PiH, C) for C in all_regions(N)}
say("C  mechanism medium (capped EFE): diffusive", is_diffusive(PiH)[0], "sup", max(regH.values()),
    "size of argmax", len(max(regH, key=regH.get)), "| mean S", (lawN * profN.sum(1)).sum())
Gmed2 = lambda i, x, So: finfo(x / Rs + So / (Rs + Rc), P0)
profN2, lawN2, _ = stationary_chain(N, Gmed2, gam)
SH2 = sigma_c(N, lawN2, N - 1, kappa, np.inf, P0, Rs, Rc, s2)
PiH2 = np.linalg.inv(SH2)
say("C  medium with literal (P2) slot EFE (expects all opened slots): diffusive", is_diffusive(PiH2)[0], "sup",
    max(contrast(PiH2, C) for C in all_regions(N)), "| mean S", (lawN2 * profN2.sum(1)).sum())
A_ = -(Pi - np.diag(np.diag(Pi)))
abar = A_[np.triu_indices(N, 1)].mean()
ebar = Pi.sum(1).mean()
say("C  mean-coupling baseline", 1 + N * abar / ebar, "| window (c)-mean", (1 + N * abar / ebar, rA))
# leak replaced by population mean leak in the mechanism medium (alternative literal reading of the preamble)
aH = -PiH[0, 1]
say("C  mechanism couplings with population mean leak:", 1 + N * aH / ebar, "| medium own leak", PiH.sum(1)[0])

# ---- nulls ----
uni = np.full(2 ** n, 2.0 ** -n)
Sh = sigma_c(n, uni, N - 1, kappa, 0.0, P0, Rs, Rc, s2)
say("D  N_hab r(A)", contrast(np.linalg.inv(blockdiag(Sh, Sh)), range(n)), "diffusive",
    is_diffusive(np.linalg.inv(blockdiag(Sh, Sh)))[0])
Sp = sigma_c(n, law, N - 1, kappa, 0.0, P0, Rs, Rc, s2)
say("D  N_pr annealed (slot law kept) r(A)", contrast(np.linalg.inv(blockdiag(Sp, Sp)), range(n)))
Shk = sigma_c(n, uni, N - 1, kappa, np.inf, P0, Rs, Rc, s2)
say("D  diagnostic: habit slots, attention kept r(A)", contrast(np.linalg.inv(blockdiag(Shk, Shk)), range(n)))

# ---- agency ----
ag, gC, num, den = agency(law, profs, P0, Rs)
say("E  Agency", ag, "gamma_C", gC, "KLmin", num, "KL(P||E)", den)

# ---- inference closure ----
def infer_terms(p):
    S = p.sum()
    Lam = 1 / P0 + p / Rs + (S - p) / (Rs + Rc)
    Ps = 1 / (1 / P0 + S / Rs)
    ceta = np.mean((p / Rs + (S - p) / (Rs + Rc)) / Lam) - Ps * S / Rs
    var = ceta ** 2 * P0
    for k in range(n):
        if p[k]:
            cm = np.mean([(1 / (Lam[i] * Rs) if i == k else 1 / (Lam[i] * (Rs + Rc))) for i in range(n)]) - Ps / Rs
            var += cm ** 2 * Rs
    for i in range(n):
        var += (S - p[i]) * (1 / (n * Lam[i] * (Rs + Rc))) ** 2 * Rc
    var += s2 / n
    return np.mean(1 / Lam), Ps, var


KLp = 0.0
EinvPs = 0.0
rows = []
for k, p in enumerate(profs):
    Pb, Ps, var = infer_terms(p)
    KLp += law[k] * 0.5 * (Pb / Ps - 1 - math.log(Pb / Ps) + var / Ps)
    EinvPs += law[k] / Ps
    rows.append((law[k], Ps, var))
V = 1 / EinvPs
KLc = sum(w * 0.5 * (V / Ps - 1 - math.log(V / Ps) + var / Ps) for w, Ps, var in rows)
say("F  alpha_I encoded N(ybar, Pbar(pi))", KLp, "| constant-variance encoding (best V =", V, "):", KLc)
open("check_A_out.txt", "w").write("\n".join(out) + "\n")
