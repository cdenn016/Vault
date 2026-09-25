"""L04: PIFB2 line 678. Source-label model with Gaussian link y_i | y_j, J=j ~ N(Omega_j y_j, L_j),
mean-field q_i=N(mu_i,Sigma_i), q_j=N(mu_j,Sigma_j). Coordinate update log beta_j = log pi_j + E_q log N(y_i; Omega_j y_j, L_j).
Claim: matching -KL(q_i||Omega_j q_j)/tau as an identity in the sender mean forces L_j = tau A_j (A_j = Omega_j Sigma_j Omega_j^T),
and then the residual j-dependent logit is -(1/2)(1 - 1/tau) log|A_j|, vanishing for all A_j only at tau = 1."""
import numpy as np
rng = np.random.default_rng(1)
K = 3
def spd(): M = rng.normal(size=(K, K)); return M@M.T + 0.5*np.eye(K)
mu_i = rng.normal(size=K); S_i = spd()
def kl(m0, S0, m1, S1):
    S1i = np.linalg.inv(S1); d = m1 - m0
    return 0.5*(np.trace(S1i@S0) + d@S1i@d - K + np.log(np.linalg.det(S1)/np.linalg.det(S0)))
def exp_loglik(mu_j, S_j, Om, L):
    A = Om@S_j@Om.T; Li = np.linalg.inv(L); r = mu_i - Om@mu_j
    return -0.5*(r@Li@r + np.trace(Li@S_i) + np.trace(Li@A)) - 0.5*np.log(np.linalg.det(2*np.pi*L))
for tau in (1.0, 0.7, 2.3):
    rows = []
    for j in range(4):
        mu_j = rng.normal(size=K); S_j = spd(); Om = rng.normal(size=(K, K)) + 2*np.eye(K)
        A = Om@S_j@Om.T
        coord = exp_loglik(mu_j, S_j, Om, tau*A)
        score = -kl(mu_i, S_i, Om@mu_j, A)/tau
        pred_extra = -0.5*(1 - 1/tau)*np.log(np.linalg.det(A))
        rows.append(coord - score - pred_extra)
    rows = np.array(rows)
    print(f'tau={tau}: coord - score - predicted logdet logit, per source (should be j-independent):', np.round(rows, 12), ' spread=', f'{np.ptp(rows):.2e}')
