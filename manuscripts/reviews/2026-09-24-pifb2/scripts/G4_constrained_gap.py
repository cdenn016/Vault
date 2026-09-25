r"""G4 check (b): constrained weighted gap eq:rg_constrained_gap (PIFB2.tex:3682-3685).

lambda_{I,w} = min_{xi != 0, w^T xi = 0} xi^T L xi / xi^T xi  (L connected graph Laplacian, w >= 0, sum w = 1).
Claims tested:
  (1) interlacing bound  lambda_2 / (n |w|^2) <= lambda_{I,w} <= lambda_2  (derived in the G4 report);
  (2) the ratio can tend to 0 only with n -> infinity (complete graph K_n, w = e_1: ratio exactly 1/n);
  (3) 'reduces to lambda_2 only for uniform weights' is false (P3 with symmetric nonuniform w; star with hub weight);
  (4) determinant bookkeeping for eq:rg_laplace: det(L restricted to w-perp) = det'(L)/(n|w|^2), while the
      coarea fiber integral int exp(-xi^T L xi/2T) delta(w^T xi - y) d xi = sqrt(n) (2 pi T)^{(n-1)/2} det'(L)^{-1/2}
      is independent of w (normal Jacobian 1/|w| cancels the constraint factor).
"""
import numpy as np

rng = np.random.default_rng(1)


def lap(A):
    return np.diag(A.sum(1)) - A


def lam_w(L, w):
    n = len(w)
    Q, _ = np.linalg.qr(np.column_stack([w, np.eye(n)]))
    B = Q[:, 1:n]  # orthonormal basis of w-perp
    return np.linalg.eigvalsh(B.T @ L @ B)[0], B


def graphs(n):
    out = {}
    A = np.ones((n, n)) - np.eye(n); out['complete'] = A
    A = np.zeros((n, n))
    for i in range(n-1):
        A[i, i+1] = A[i+1, i] = 1
    out['path'] = A.copy()
    A[0, n-1] = A[n-1, 0] = 1; out['cycle'] = A
    A = np.zeros((n, n)); A[0, 1:] = A[1:, 0] = 1; out['star(hub=0)'] = A
    return out


worst = 0.0
viol = 0
for trial in range(2000):
    n = rng.integers(2, 9)
    A = rng.uniform(0, 1, (n, n)) * (rng.uniform(size=(n, n)) < 0.6)
    A = np.triu(A, 1); A = A + A.T
    for i in range(n-1):  # ensure connected
        if A[i, i+1] == 0:
            A[i, i+1] = A[i+1, i] = 0.1
    L = lap(A)
    w = rng.dirichlet(np.full(n, rng.choice([0.05, 1.0, 20.0])))
    l2 = np.linalg.eigvalsh(L)[1]
    lw, _ = lam_w(L, w)
    lo = l2/(n*w @ w)
    if lw < lo*(1-1e-10) or lw > l2*(1+1e-10):
        viol += 1
    worst = max(worst, (lo - lw)/l2)
print('(1) random connected graphs n<=8, 2000 trials: bound violations =', viol,
      ' max (lower - lam_w)/lam_2 =', worst)

print('(2) ratio lam_w/lam_2 with fully concentrated w = e_k (node 0; for the star a leaf)')
for n in [3, 5, 10, 20, 40]:
    row = []
    for name, A in graphs(n).items():
        L = lap(A); l2 = np.linalg.eigvalsh(L)[1]
        w1 = np.zeros(n); w1[-1 if name.startswith('star') else 0] = 1.0  # star: leaf; others: node 0
        lw1, _ = lam_w(L, w1)
        row.append(f'{name}:{lw1/l2:.4f}')
    print(f'  n={n:3d}  ' + '  '.join(row) + f'   (1/n = {1/n:.4f})')
n = 6
L = lap(graphs(n)['star(hub=0)']); l2 = np.linalg.eigvalsh(L)[1]
wh = np.zeros(n); wh[0] = 1
print('  star n=6, weight on hub: lam_w/lam_2 =', lam_w(L, wh)[0]/l2)

print('(3) P3 path with symmetric nonuniform weights')
L = lap(graphs(3)['path']); l2 = np.linalg.eigvalsh(L)[1]
for w in [np.array([0.1, 0.8, 0.1]), np.array([0.45, 0.1, 0.45]), np.array([0.2, 0.3, 0.5])]:
    print(f'  w={w}: lam_w={lam_w(L, w)[0]:.12f}  lam_2={l2:.12f}')

print('(4) determinant bookkeeping (K=1)')
for trial in range(3):
    n = 5
    A = rng.uniform(0.2, 1.5, (n, n)); A = np.triu(A, 1); A = A + A.T
    L = lap(A)
    ev = np.linalg.eigvalsh(L); detp = np.prod(ev[1:])
    w = rng.dirichlet(np.ones(n)*0.7)
    _, B = lam_w(L, w)
    dcon = np.linalg.det(B.T @ L @ B)
    print(f'  det(L|w-perp)={dcon:.10f}  det\'(L)/(n|w|^2)={detp/(n*w@w):.10f}')
    # fiber integral via parametrization xi = xi_p + B eta, xi_p = y w/|w|^2; delta(w^T xi - y) -> 1/|w| on fiber
    T, y = 0.3, 0.7
    xp = y*w/(w@w)
    M = B.T @ L @ B
    b = B.T @ L @ xp
    c = xp @ L @ xp
    # int exp(-(eta^T M eta + 2 b^T eta + c)/(2T)) d eta
    val = (2*np.pi*T)**((n-1)/2)/np.sqrt(np.linalg.det(M))*np.exp(-(c - b @ np.linalg.solve(M, b))/(2*T))
    fiber = val/np.sqrt(w @ w)
    target = np.sqrt(n)*(2*np.pi*T)**((n-1)/2)/np.sqrt(detp)
    print(f'     coarea fiber integral={fiber:.10f}  sqrt(n)(2piT)^((n-1)/2) det\'^(-1/2)={target:.10f}'
          f'  rel.resid={abs(fiber-target)/target:.2e}')
