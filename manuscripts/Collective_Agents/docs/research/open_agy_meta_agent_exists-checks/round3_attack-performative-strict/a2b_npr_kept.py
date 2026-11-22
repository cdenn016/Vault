r"""a2b: annealed N_pr under the kept-gain convention (4-agent joint system).

Members 0=b1, 1=s1, 2=b2, 3=s2. Each round each member reads one partner drawn
uniformly from the other three and applies its full-model steady-state gains to
it (relay row of H unchanged).  The private part of a relay read by j from
partner p is v_p(t-1) + nu_j(t).

Declared expectations (before running):
 E1 NEGATIVE CONTROL: partners fixed to mates reproduces the block-diagonal full
    model, r(pair) = 4.3336, cross-firm block 0.
 E2 kept-gain annealed: cross-firm covariances appear.  I expect at least one
    positive off-diagonal precision entry (non-diffusive), as for the TDF.
"""
import sys
import numpy as np
from ccp_lib import *

np.set_printoptions(precision=5, suppress=True, linewidth=150)
p = default_params()
Phi, Qw, Gm = world_mats(p)
filt = member_filters(p)
kap = p["kappa"]
role = ["b", "s", "b", "s"]
mate = [1, 0, 3, 2]
firm = [0, 0, 1, 1]
OWNC = {"b": 0, "s": 1}
NXa, NXIa = 20, 30   # state: z(16), vlag(4); noise: v(4), nu(4), c(16), eps(4), wZ(2)


def zsl(j):
    return slice(4 * j, 4 * j + 4)


def step_mats(partner):
    A = np.zeros((NXa, NXa)); B = np.zeros((NXa, NXIa))
    Cm = np.zeros((2, NXa)); Dm = np.zeros((2, NXIa))
    for j in range(4):
        K, H = filt[role[j]]["K"], filt[role[j]]["H"]
        M = np.eye(4) - K @ H
        ZpS = np.zeros((4, NXa)); ZpS[:, zsl(j)] = M
        ZpX = np.zeros((4, NXIa))
        ZpX[:, j] += K[:, 0]                  # own sensing noise v_j(t)
        ZpS[:, 16 + partner[j]] += K[:, 1]    # v_partner(t-1)
        ZpX[:, 4 + j] += K[:, 1]              # receiver channel noise nu_j(t)
        A[zsl(j)] = Phi @ ZpS
        B[zsl(j)] = Phi @ ZpX
        B[zsl(j), 8 + 4 * j: 12 + 4 * j] += np.eye(4)   # computation noise
        f = firm[j]
        Cm[f] += -kap * D @ ZpS
        Dm[f] += -kap * D @ ZpX
        Dm[f, 24 + j] += 1.0                  # act noise
    for j in range(4):
        B[16 + j, j] = 1.0                    # vlag_j(t+1) = v_j(t)
    Dm[0, 28] += 1.0; Dm[1, 29] += 1.0        # w^Z per firm
    return A, B, Cm, Dm


qv = np.zeros(NXIa)
qv[0:4] = p["R"]; qv[4:8] = p["Rc"]; qv[8:24] = p["qc"]; qv[24:28] = p["s2"]; qv[28:30] = p["QZ"]
Tsel = np.zeros((4, NXa))
for j in range(4):
    Tsel[j, 4 * j + OWNC[role[j]]] = 1.0

# initial covariance: stationary law with mates fixed
A_m, B_m, _, _ = step_mats(mate)
S0 = solve_discrete_lyapunov(A_m, B_m @ np.diag(qv) @ B_m.T)


def window(partners, L, Lr):
    nsteps = L + Lr + 1
    dimU = NXa + NXIa * nsteps
    coefS = np.zeros((NXa, dimU)); coefS[:, :NXa] = np.eye(NXa)
    O = np.zeros((2 * nsteps, dimU))
    tgt = None
    for k in range(nsteps):
        if k == L:
            tgt = Tsel @ coefS
        A, B, Cm, Dm = step_mats(partners[k])
        cx = np.zeros((NXIa, dimU)); cx[:, NXa + k * NXIa: NXa + (k + 1) * NXIa] = np.eye(NXIa)
        O[2 * k: 2 * k + 2] = Cm @ coefS + Dm @ cx
        coefS = A @ coefS + B @ cx
    dg = np.tile(qv, nsteps)

    def cov(X, Y):
        return X[:, :NXa] @ S0 @ Y[:, :NXa].T + (X[:, NXa:] * dg) @ Y[:, NXa:].T
    Soo = cov(O, O); Sto = cov(tgt, O); Stt = cov(tgt, tgt)
    return Stt - Sto @ np.linalg.solve(Soo, Sto.T)


def contrast_report(Sig, tag):
    Pi = np.linalg.inv(Sig)
    off = Pi - np.diag(np.diag(Pi))
    print(tag, "Pi=\n", Pi)
    print("  max off-diagonal %.4f, min row sum %.4f, diffusive %s" % (off.max(), Pi.sum(1).min(), is_diffusive(Pi)))
    if is_diffusive(Pi):
        for C in all_regions(4):
            print("   r%s = %.4f" % (C, rates(Pi, C)[2]))


L = Lr = 50
nsteps = L + Lr + 1
Sfix = window([mate] * nsteps, L, Lr)
print("E1 mates fixed: Sigma=\n", Sfix)
contrast_report(Sfix, "E1")

rng = np.random.default_rng(7)
nseq = int(sys.argv[1]) if len(sys.argv) > 1 else 200
acc = []
for k in range(nseq):
    parts = []
    for t in range(nsteps):
        parts.append([rng.choice([q for q in range(4) if q != j]) for j in range(4)])
    acc.append(window(parts, L, Lr))
acc = np.array(acc)
W = acc.mean(0)
print("\nkept-gain annealed W (n=%d):\n" % nseq, W, "\nSE:\n", acc.std(0) / np.sqrt(nseq))
contrast_report(W, "kept-gain")
for h, sl in (("first half", slice(0, nseq // 2)), ("second half", slice(nseq // 2, nseq))):
    Pi = np.linalg.inv(acc[sl].mean(0))
    off = Pi - np.diag(np.diag(Pi))
    print("  %s: max off-diag %.4f, min row sum %.4f" % (h, off.max(), Pi.sum(1).min()))
