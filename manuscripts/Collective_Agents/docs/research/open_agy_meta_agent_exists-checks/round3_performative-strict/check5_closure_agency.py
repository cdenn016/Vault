r"""check5: closure (memory and inference) and agency index of the TDF instance (kappa* = 0.68, Rc = 0.1).

Closure (def:agy-closure, 05_agency.tex:13-24).  eta_C = (eta^{3f}_t, eta^{3f+1}_t), the exterior variables the
members sense (05_agency.tex:11); declared coarse variable y = (ybar_B, ybar_S), the department averages of the
members' prior means of their component: the pooled statistic of the members' beliefs about eta_C, one coordinate per
exterior variable.  The departments are independent and identical, so both clauses are twice a department's value.
  Memory: interior x = (m^-_{b1}, m^-_{b2}) given the blanket path (own sensors and the relayed sensings),
  x' = A_int x + n, A_int = blockdiag(A_F (I - K H)), n = A_F K_rel nu + qc noise; d_M from the autocovariance of
  ybar (Toeplitz conditioning on L = 400 lags); d_cl from eq:agy-closure-defect.
  Inference: union model = exact centralized filter of eta from both members' own sensors (no relays, the round-2
  convention); alpha_I = 1/2 E[(ybar - u)^2] / U per department (KL(encoded || union predictive), best constant
  encoding variance, which equals U here).
Agency (def:agy-agency-index, 05_agency.tex:240-246; acts by def:agy-joint-acts, s05_agency.tex:146-159, extended to
continuous Gaussian acts as in rounds 1-2).  Instance act parameters: beta = 1, h = 1, Lam = 1, gamma = 68,
habits N(0, sE2) with sE2 = 1/32, so s2 = 1/(1/sE2 + gamma Lam beta^2) = 0.01 and kappa = gamma Lam beta h s2 = 0.68.
  Actual law at a decision state (declaration D2): independent u_j ~ N(mu_j, s2), mu_j = -kappa sigma_j m^+_{j,0}.
  Class: belief = pooled (department averages), preference N(0, 1/Lam) on eta^Z', true effects, habits fixed at
  N(0, sE2) per member, gamma_C in [0, inf).  Decision states: 300 joint states of firm 0 drawn from the stationary law
  of the members' posterior means (seed 7), equal weights.
Declared expectations BEFORE running:
  E1 d_M per department below 1e-3 (the department average misses only the lag coordinate); d_M <= d_cl;
  E2 alpha_I per department of order 1e-2 to 5e-2 (one-round latency, two members);
  E3 agency index strictly between 0 and 1 (the group model explains the common part of the act shifts, not the
     split between departments nor the members' individual variance shrinkage);
  CTRL+ if the actual law is replaced by the group posterior at gamma_C = gamma (same class), index = 1;
  CTRL- if members acted by habit (mu = 0, variance sE2) the denominator vanishes (index 1 by definition, reported
     as degenerate, not used).
"""
import numpy as np
from scipy.optimize import minimize_scalar
import lgx
from tdf import tdf_spec, groups

F, Q, R, Rc, qc = 0.9, 0.05, 1.0, 0.1, 1e-4
KAP = 0.68
gamma, Lam, beta, h, sE2 = 68.0, 1.0, 1.0, 1.0, 1.0 / 32.0
s2 = 1.0 / (1.0 / sE2 + gamma * Lam * beta ** 2)
assert abs(gamma * Lam * beta * h * s2 - KAP) < 1e-12 and abs(s2 - 0.01) < 1e-12

spec = tdf_spec(2, 2, Rc=Rc, qc=qc, kappa=KAP, sa2=s2)
mod = lgx.build(spec, "full")
Kg = mod["gains"][0]["K"]
AF = np.array([[F, 0.0], [1.0, 0.0]])
H = np.array([[1.0, 0.0], [0.0, 1.0]])

# ---------------------------------------------------------------- memory
Ai = AF @ (np.eye(2) - Kg @ H)
Qi = Rc * AF @ np.outer(Kg[:, 1], Kg[:, 1]) @ AF.T + qc * np.eye(2)
Aint = np.kron(np.eye(2), Ai)
Qn = np.kron(np.eye(2), Qi)
Sx = lgx.stat_cov(Aint, Qn)
Py = np.array([[0.5, 0.0, 0.5, 0.0]])
Lg = 400
acov = [(Py @ np.linalg.matrix_power(Aint, k) @ Sx @ Py.T).item() for k in range(Lg + 2)]
T = np.array([[acov[abs(a - b)] for b in range(Lg + 1)] for a in range(Lg + 1)])
c = np.array(acov[1:Lg + 2])[::-1]          # Cov(y_{t+1}, y_{t-L..t}) ordered oldest..newest
v_inf = acov[0] - c @ np.linalg.solve(T, c)
v_one = acov[0] - acov[1] ** 2 / acov[0]
dM = 0.5 * np.log(v_one / v_inf)
PS = Py @ Sx
Sxy = Sx - PS.T @ PS / (PS @ Py.T).item()
dcl = 0.5 * np.log(1 + (Py @ Aint @ Sxy @ Aint.T @ Py.T).item() / (Py @ Qn @ Py.T).item())
print(f"[memory] per department: d_M = {dM:.3e}, d_cl = {dcl:.3e}; firm (two independent departments): "
      f"d_M = {2 * dM:.3e}, d_cl = {2 * dcl:.3e}")

# ---------------------------------------------------------------- inference
# union scalar filter with two sensors per round
PU = Q
for _ in range(100000):
    Pp = 1.0 / (1.0 / PU + 2.0 / R)
    PUn = F * F * Pp + Q
    if abs(PUn - PU) < 1e-16:
        break
    PU = PUn
KU = Pp / R
# joint state: eta_t, eta_{t-1}, m1 (2), m2 (2), v1(t-1), v2(t-1), u(t); noises w, v1, v2, nu12, nu21, qc x4
d, p = 9, 9
A = np.zeros((d, d)); G = np.zeros((d, p))
A[0, 0] = F; G[0, 0] = np.sqrt(Q)
A[1, 0] = 1.0
for i, (mi, vi, vj, nui, qi) in enumerate([((2, 3), 6, 7, 3, 5), ((4, 5), 7, 6, 4, 7)]):
    # innovations: s_i - m_{i,0} = eta_t + v_i(t) - m_{i,0};  y - m_{i,1} = eta_{t-1} + v_j(t-1) + nu - m_{i,1}
    Mx = np.zeros((2, d)); Mn = np.zeros((2, p))
    Mx[:, list(mi)] = np.eye(2)
    ox = np.zeros((2, d)); on = np.zeros((2, p))
    ox[0, 0] = 1.0; on[0, 1 + i] = np.sqrt(R)
    ox[1, 1] = 1.0; ox[1, vj] = 1.0; on[1, nui] = np.sqrt(Rc)
    post_x = Mx + Kg @ (ox - H @ Mx)
    post_n = Kg @ on
    A[list(mi)] = AF @ post_x
    G[list(mi)] = AF @ post_n
    G[mi[0], qi] += np.sqrt(qc); G[mi[1], qi + 1] += np.sqrt(qc)
    G[vi, 1 + i] = np.sqrt(R)
# union: u(t+1) = F (u + KU (s1 + s2 - 2u))
A[8, 8] = F * (1 - 2 * KU); A[8, 0] = F * 2 * KU
G[8, 1] = F * KU * np.sqrt(R); G[8, 2] = F * KU * np.sqrt(R)
Sj = lgx.stat_cov(A, G @ G.T)
dvec = np.zeros(d); dvec[2] = 0.5; dvec[4] = 0.5; dvec[8] = -1.0
msd = float(dvec @ Sj @ dvec)
aI = 0.5 * msd / PU
ev = np.zeros(d); ev[2] = 0.5; ev[4] = 0.5; ev[0] = -1.0
print(f"[inference] union prior variance U = {PU:.6f}; E(ybar - u)^2 = {msd:.4e}; alpha_I per department = "
      f"{aI:.4e}; firm = {2 * aI:.4e}  (members' mean error var {float(ev @ Sj @ ev):.5f})")

# ---------------------------------------------------------------- agency
C0 = list(groups(2, 2)["C0"])
P = lgx.stat_cov(mod["A"], mod["Qx"])
Ux = mod["Ux"][C0]
Un = mod["Un"][C0].copy()
Un[:, mod["n_a"]] = 0.0
sd = mod["sd"]
Cmu = Ux @ P @ Ux.T + (Un * sd ** 2) @ Un.T
Cmu = 0.5 * (Cmu + Cmu.T)
rng = np.random.default_rng(7)
MU = rng.multivariate_normal(np.zeros(4), Cmu, size=300)
sig = np.array([a["kappa"] for a in spec["agents"]])[C0] / KAP     # +1 on B, -1 on S
n = 4


def zC_of(mu):
    m = -mu / (KAP * sig)                     # members' posterior means
    return h * (m[:2].mean() - m[2:].mean())


def kl_gauss(mu1, S1, mu2, S2):
    k = len(mu1)
    S2i = np.linalg.inv(S2)
    dm = mu2 - mu1
    return 0.5 * (np.trace(S2i @ S1) + dm @ S2i @ dm - k + np.log(np.linalg.det(S2) / np.linalg.det(S1)))


def group(gC, zC):
    Gam = np.eye(n) / sE2 + gC * Lam * beta ** 2 * np.ones((n, n))
    Si = np.linalg.inv(Gam)
    return -gC * Lam * beta * zC * Si @ np.ones(n), Si


def index(MUs, actual_cov):
    den = sum(kl_gauss(mu, actual_cov, np.zeros(n), sE2 * np.eye(n)) for mu in MUs)
    f = lambda lg: sum(kl_gauss(mu, actual_cov, *group(np.exp(lg), zC_of(mu))) for mu in MUs)
    grid = np.linspace(-8, 10, 73)
    vals = [f(x) for x in grid]
    j = int(np.argmin(vals))
    res = minimize_scalar(f, bracket=(grid[max(j - 1, 0)], grid[j], grid[min(j + 1, 72)]))
    num = min(res.fun, vals[j], den)
    return 1 - num / den, float(np.exp(res.x)), den / len(MUs), num / len(MUs)


A_idx, gC_best, den_avg, num_avg = index(MU, s2 * np.eye(n))
print(f"[agency] D2: index = {A_idx:.4f} (best gamma_C = {gC_best:.3f}); mean KL(P||E) = {den_avg:.3f} nats, "
      f"mean KL(P||P_g) = {num_avg:.3f} nats")
# CTRL+: actual law replaced by the class's own group posterior at gamma_C = gamma
MU_g = np.array([group(gamma, zC_of(mu))[0] for mu in MU])
Sg = group(gamma, 0.0)[1]
den = sum(kl_gauss(m, Sg, np.zeros(n), sE2 * np.eye(n)) for m in MU_g)
num = sum(kl_gauss(m, Sg, *group(gamma, zC_of(mu))) for m, mu in zip(MU_g, MU))
print(f"[agency] CTRL+ (actual = group posterior at gamma): index = {1 - num / den:.6f}")
# the D1 alternative (intention sharing + (P4), exact potential game): stationary law = group posterior with tilted
# habits; class with habits fixed cannot represent the tilts
def d1_law(mu):
    m = -mu / (KAP * sig)
    z = h * sig * m
    Gam = np.eye(n) / sE2 + gamma * Lam * beta ** 2 * np.ones((n, n))
    Si = np.linalg.inv(Gam)
    return -gamma * Lam * beta * Si @ z, Si
D1 = [d1_law(mu) for mu in MU]
den = sum(kl_gauss(m, S, np.zeros(n), sE2 * np.eye(n)) for m, S in D1)
f1 = lambda lg: sum(kl_gauss(m, S, *group(np.exp(lg), zC_of(mu))) for (m, S), mu in zip(D1, MU))
grid = np.linspace(-8, 10, 73)
vals = [f1(x) for x in grid]
print(f"[agency] D1 alternative (intention sharing): index = {1 - min(vals) / den:.4f} at gamma_C ~ "
      f"{np.exp(grid[int(np.argmin(vals))]):.2f}; its total act loading per member = "
      f"{gamma * Lam * beta ** 2 * sE2 / (1 + n * gamma * Lam * beta ** 2 * sE2):.4f} vs D2 {KAP:.4f}")
