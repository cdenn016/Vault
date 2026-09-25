r"""G1 check (b): eq:dispersion_drop_bound (PIFB2.tex 1620-1625) with non-uniform coherence weights.

Bound:  || sum_i w_i (mu_i - mubar)(mu_i - mubar)^T ||_op  <=  max_j lambda_max(S_j) * eps_w,
        eps_w = sum_{i,j} w_i w_j KL(q_i || q_j)   (laws already in the parent frame; Regime I cocycle).
Text claim (1625): inside the detector pass band (Gamma = P C_q C_s > 0.5, C_q = exp(-mean KL / tau),
tau = 0.05) the right side is at most tau log 2 * max lambda (= 0.035 max lambda). The pass band bounds the
UNWEIGHTED mean KL (1/|I|^2) sum_{i,j} KL.
 (i)  the bound itself, arbitrary normalized weights (random instances);
 (ii) batched random search (K=2, n=3..6) for pass-band instances whose actual dropped spread exceeds
      0.035 max lambda, with the implementation's self-consistent weights w_i = chi_i exp(-KL(q_i||qbar))
      iterated from the uniform-weight start; chi = 1 and chi free in [0,1];
 (iii) explicit large-n instance (one outlier) at the outlier-captured fixed point of the bistable weight map.
"""
import numpy as np
rng = np.random.default_rng(7)
tau = 0.05; band = tau*np.log(2)

def spd_batch(B, n, K, scale):
    A = rng.standard_normal((B, n, K, K))*scale[:, None, None, None]; A = (A + np.swapaxes(A, -1, -2))/2
    lam, V = np.linalg.eigh(A); return (V*np.exp(lam)[..., None, :])@np.swapaxes(V, -1, -2)

def kl_pair(m1, S1, m2, S2):
    K = m1.shape[-1]; S2i = np.linalg.inv(S2); d = (m2 - m1)[..., None]
    tr = np.einsum('...ij,...ji->...', S2i, S1); quad = (np.swapaxes(d, -1, -2)@S2i@d)[..., 0, 0]
    return 0.5*(tr + quad - K + np.linalg.slogdet(S2)[1] - np.linalg.slogdet(S1)[1])

def evaluate(mus, Ss, chi, iters=300):
    B, n, K = mus.shape
    KL = kl_pair(mus[:, :, None, :], Ss[:, :, None], mus[:, None, :, :], Ss[:, None])  # (B,n,n) KL(q_i||q_j)
    w = chi/chi.sum(1, keepdims=True)
    for _ in range(iters):
        mb = np.einsum('bi,bik->bk', w, mus); Sb = np.einsum('bi,bikl->bkl', w, Ss)
        k = kl_pair(mus, Ss, mb[:, None, :], Sb[:, None])
        w = chi*np.exp(-(k - k.min(1, keepdims=True))); w /= w.sum(1, keepdims=True)
    mean_kl = KL.sum((1, 2))/n**2; Gamma = chi.mean(1)*np.exp(-mean_kl/tau)
    mb = np.einsum('bi,bik->bk', w, mus); d = mus - mb[:, None, :]
    spread = np.einsum('bi,bik,bil->bkl', w, d, d); lhs = np.linalg.eigvalsh(spread)[:, -1]
    lmax = np.linalg.eigvalsh(Ss)[..., -1].max(1); eps_w = np.einsum('bi,bij,bj->b', w, KL, w)
    return dict(Gamma=Gamma, mean_kl=mean_kl, eps_w=eps_w, lhs=lhs, lmax=lmax, w=w)

# (i) bound with arbitrary weights
B = 20000; worst = np.inf
for n in (2, 3, 5):
    for K in (1, 2, 3):
        mus = rng.standard_normal((B, n, K))*rng.uniform(0.01, 2, (B, 1, 1)); Ss = spd_batch(B, n, K, rng.uniform(0, 1.5, B))
        w = rng.dirichlet(np.ones(n)*0.5, B)
        KL = kl_pair(mus[:, :, None, :], Ss[:, :, None], mus[:, None, :, :], Ss[:, None])
        mb = np.einsum('bi,bik->bk', w, mus); d = mus - mb[:, None, :]
        lhs = np.linalg.eigvalsh(np.einsum('bi,bik,bil->bkl', w, d, d))[:, -1]
        rhs = np.linalg.eigvalsh(Ss)[..., -1].max(1)*np.einsum('bi,bij,bj->b', w, KL, w)
        worst = min(worst, ((rhs - lhs)/rhs).min())
print(f"(i) bound on 180000 random instances (n in 2,3,5; K in 1,2,3; arbitrary weights): min (rhs-lhs)/rhs = {worst:.3e}")

# (ii) pass-band random search with self-consistent weights
for chi_mode in ("chi=1", "chi free"):
    for n in (3, 4, 5, 6):
        B = 40000; K = 2
        mus = rng.standard_normal((B, n, K))*rng.uniform(0.005, 0.4, (B, 1, 1))
        Ss = spd_batch(B, n, K, rng.uniform(0, 0.6, B))
        chi = np.ones((B, n)) if chi_mode == "chi=1" else rng.uniform(0, 1, (B, n))**rng.uniform(0.1, 1, (B, 1))
        r = evaluate(mus, Ss, chi)
        ok = r['Gamma'] > 0.5
        ratio = np.where(ok, r['lhs']/(band*r['lmax']), 0)
        ratio_w = np.where(ok, r['eps_w']/r['mean_kl'], 0)
        j = np.argmax(ratio)
        print(f"(ii) {chi_mode:8s} n={n}: admitted {ok.sum():5d}/{B}; max spread/(0.035 lmax) = {ratio.max():.4f}; "
              f"max eps_w/mean KL = {ratio_w.max():.3f}; at argmax: Gamma={r['Gamma'][j]:.3f}, mean KL={r['mean_kl'][j]:.4f}, eps_w={r['eps_w'][j]:.4f}")

# (iii) explicit large-n instance
n, D = 1000, 5.0
mus = np.zeros((1, n, 2)); mus[0, 0, 0] = D; Ss = np.broadcast_to(np.eye(2), (1, n, 2, 2)).copy(); chi = np.ones((1, n))
mean_kl = 2*(n - 1)*(D*D/2)/n**2
for start in ("uniform", "outlier"):
    mb = np.array([D/n, 0.0]) if start == "uniform" else np.array([D, 0.0])
    for _ in range(2000):
        k = 0.5*((mus[0] - mb)**2).sum(1); w = np.exp(-(k - k.min())); w /= w.sum(); mb = w@mus[0]
    d = mus[0] - mb; lhs = np.linalg.eigvalsh((w[:, None, None]*np.einsum('ik,il->ikl', d, d)).sum(0))[-1]
    print(f"(iii) n={n}, one outlier at D={D}, identity covariances: mean KL={mean_kl:.5f} < {band:.5f}, Gamma={np.exp(-mean_kl/tau):.3f}; "
          f"start {start}: mubar={mb[0]:.4f}, ||spread||_op={lhs:.4f} vs claimed cap {band:.4f} (ratio {lhs/band:.1f})")
