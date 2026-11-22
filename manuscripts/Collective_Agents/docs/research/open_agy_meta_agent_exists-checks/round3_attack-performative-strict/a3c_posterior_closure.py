r"""a3c: is there a consistent declaration in which the group belief of the
agency class is literally a function of the declared closure coarse variable?
Candidate declaration: closure on the average of the members' current PRIOR
means y(t); agency belief z_C = mean of the members' POSTERIOR z (a function of
posteriors, not of y(t)).  Repair candidate: declare the closure coarse variable
as the average of the members' current POSTERIOR means y+(t) (the internal
state after the round-t update, on which the acts are drawn).

Declared expectations (before running):
 E1 alpha_I of y+(t) against the union-model posterior at t (both own sensors
    up to t) is larger than the prior-average value 0.0317, because each
    member's posterior lacks the mate's round-t reading; I do not know whether
    it exceeds 0.05.
 E2 the input-free memory defect of y+ is small (< 1e-3), as for y.
 E3 NEGATIVE CONTROL: replacing the members' posteriors by the union posterior
    itself gives alpha_I = 0 to 1e-12.
"""
import io, contextlib
import numpy as np
with contextlib.redirect_stdout(io.StringIO()):
    import a3_closure_agency as M

p, NY, NE, SYX = M.p, M.NY, M.NE, M.SYX
E2m = M.E2
KU, PU = M.KU, M.PU
PUp = (np.eye(2) - KU) @ PU                 # union posterior covariance
print("union posterior covariance:\n", PUp)
EbY, EbX = M.Epost["b"]; EsY, EsX = M.Epost["s"]
ieU = M.ieU
# y+ - m_U^+ = 0.5 (e_b^+[cur] + e_s^+[cur]) - e_U^+
r = np.zeros((2, NY + NE))
r[:, :NY] += 0.5 * E2m @ EbY + 0.5 * E2m @ EsY
r[:, NY:] += 0.5 * E2m @ EbX + 0.5 * E2m @ EsX
MU = np.eye(2) - KU
r[:, ieU.start:ieU.stop] += -MU
r[:, NY + 2:NY + 4] += -KU
Cd = r @ SYX @ r.T
print("E1 alpha_I (posterior average vs union posterior, best constant encoding) = %.5f" % (0.5 * np.trace(np.linalg.solve(PUp, Cd))))
# negative control
r0 = np.zeros((2, NY + NE)); r0[:, ieU.start:ieU.stop] = MU; r0[:, NY + 2:NY + 4] = KU
rr = r0 - r0
print("E3 control alpha_I = %.2e" % (0.5 * np.trace(np.linalg.solve(PUp, rr @ SYX @ rr.T))))
# also: union posterior at t vs prior average y(t)  (encoded belief one round stale)
r2 = np.zeros((2, NY + NE)); r2[:, M.ieb] += 0.5 * E2m; r2[:, M.ies] += 0.5 * E2m
r2[:, ieU.start:ieU.stop] += -MU; r2[:, NY + 2:NY + 4] += -KU
print("   alpha_I (prior average y(t) vs union POSTERIOR at t) = %.5f" % (0.5 * np.trace(np.linalg.solve(PUp, r2 @ SYX @ r2.T))))

# E2: input-free memory defect of y+ : internal state = posteriors (8) + relay channel values (2)
Phi = M.Phi
fb, fs = M.filt["b"], M.filt["s"]
Mb = np.eye(4) - fb["K"] @ fb["H"]; Ms = np.eye(4) - fs["K"] @ fs["H"]
# m^+(t+1) = M Phi m^+(t) + M c(t) + K [s(t+1); relay(t+1)] ; relay(t+1) = s_mate(t) + nu(t+1)
# input-free: x = [m_b^+, m_s^+], noise n = [M_b c_b + K_b[:,1] nu_bs ; M_s c_s + K_s[:,1] nu_sb]
Ai = np.zeros((8, 8)); Ai[0:4, 0:4] = Mb @ Phi; Ai[4:8, 4:8] = Ms @ Phi
Bn = np.zeros((8, 10)); Bn[0:4, 0:4] = Mb; Bn[4:8, 4:8] = Ms; Bn[0:4, 8] = fb["K"][:, 1]; Bn[4:8, 9] = fs["K"][:, 1]
Qn = np.diag([p["qc"]] * 8 + [p["Rc"]] * 2)
Si = M.solve_discrete_lyapunov(Ai, Bn @ Qn @ Bn.T)
Py = np.zeros((2, 8)); Py[:, 0:4] = 0.5 * E2m; Py[:, 4:8] = 0.5 * E2m
acf = lambda k: Py @ np.linalg.matrix_power(Ai, k) @ Si @ Py.T
for K in (1, 5, 20, 60):
    print("E2 d_M(y+), input-free, history %2d: %.4e" % (K, M.markov_defect_from_acf(acf, K)))

# E3b (check that can fail): Monte Carlo of Cov(y+ - m_U^+) by simulating the full model
rng = np.random.default_rng(5)
A, B, Qxi = M.A, M.B, M.Qxi
Lq = np.linalg.cholesky(Qxi + 1e-18 * np.eye(NE))
Y = np.zeros(NY); acc = []
for t in range(200000 + 1000):
    xi = Lq @ rng.standard_normal(NE)
    if t >= 1000:
        acc.append(r @ np.concatenate([Y, xi]))
    Y = A @ Y + B @ xi
acc = np.array(acc)
Cmc = np.cov(acc.T)
bs = len(acc) // 100
se = np.array([np.cov(acc[i*bs:(i+1)*bs].T) for i in range(100)]).std(0) / 10
print("E3b MC Cov(y+ - m_U^+) vs exact: z =", ((Cmc - Cd) / se).ravel())
