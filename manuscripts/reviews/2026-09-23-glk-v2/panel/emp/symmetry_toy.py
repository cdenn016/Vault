# Tiny CPU check: (i) Noether identities for the GL(r) comparison symmetry and GL(s) content symmetry;
# (ii) AdamW (wd=0) vs SGD drift along the flat orbit of a routing loss built from the projected
# Gaussian KL (same formula as eq. projected_full_kl). Dimensions are single digits.
import math, torch
torch.set_num_threads(1); torch.manual_seed(0)
dt = torch.float64
K, r, s, N = 6, 3, 3, 7

def spd(n):
    A = torch.randn(n, n, dtype=dt); return A @ A.T + n * torch.eye(n, dtype=dt)
xi = torch.randn(N, K, dtype=dt); C = torch.stack([spd(K) for _ in range(N)])

def kl_matrix(SQ, SK):
    a = xi @ SQ.T; bk = xi @ SK.T
    VQ = SQ @ C @ SQ.T; VK = SK @ C @ SK.T          # (N,r,r)
    P = torch.linalg.inv(VK)
    D = torch.empty(N, N, dtype=dt)
    for i in range(N):
        for j in range(N):
            d = a[i] - bk[j]
            D[i, j] = 0.5 * (torch.trace(P[j] @ VQ[i]) + d @ P[j] @ d - r + torch.logdet(VK[j]) - torch.logdet(VQ[i]))
    return D

target = torch.softmax(torch.randn(N, N, dtype=dt), -1)
mask = torch.tril(torch.ones(N, N, dtype=torch.bool))
def loss_fn(SQ, SK, T, O, y):
    D = kl_matrix(SQ, SK)
    logits = (-D / math.sqrt(r)).masked_fill(~mask, float("-inf"))
    beta = torch.softmax(logits, -1)
    route = -(target * torch.log(beta.clamp_min(1e-300))).masked_fill(~mask, 0).sum()
    m = beta @ (xi @ T.T @ O.T)                    # content through O T only
    return route + ((m - y) ** 2).sum() * 1e-3

SQ = torch.randn(r, K, dtype=dt, requires_grad=True); SK = torch.randn(r, K, dtype=dt, requires_grad=True)
T = torch.randn(s, K, dtype=dt, requires_grad=True); O = torch.randn(K, s, dtype=dt, requires_grad=True)
y = torch.randn(N, K, dtype=dt)
L = loss_fn(SQ, SK, T, O, y); gQ, gK, gT, gO = torch.autograd.grad(L, (SQ, SK, T, O))
print("GL(r) invariance of D: max|D(A SQ, A SK) - D| =",
      float((kl_matrix(torch.randn(r, r, dtype=dt) @ SQ.detach() * 0 + (lambda A: A @ SQ.detach())(torch.eye(r, dtype=dt) * 3.0 + torch.randn(r, r, dtype=dt)), (lambda A: A @ SK.detach())(torch.eye(r, dtype=dt) * 3.0 + torch.randn(r, r, dtype=dt))) - kl_matrix(SQ.detach(), SK.detach())).abs().max()) if False else "see below")
A = torch.eye(r, dtype=dt) * 2.0 + 0.5 * torch.randn(r, r, dtype=dt)
print("GL(r) invariance residual max|D(A SQ, A SK) - D(SQ, SK)| =", float((kl_matrix(A @ SQ.detach(), A @ SK.detach()) - kl_matrix(SQ.detach(), SK.detach())).abs().max()))
print("Noether GL(r): ||gQ SQ^T + gK SK^T||_F =", float((gQ @ SQ.detach().T + gK @ SK.detach().T).norm()), " (scale ||gQ||*||SQ|| =", float(gQ.norm() * SQ.norm()), ")")
print("Noether GL(s): ||T gT^T - gO^T O||_F =", float((T.detach() @ gT.T - gO.T @ O.detach()).norm()), " (scale", float(gT.norm() * T.norm()), ")")

def run(opt_name, steps=4000, lr=0.01):
    torch.manual_seed(1)
    ps = [torch.randn(r, K, dtype=dt), torch.randn(r, K, dtype=dt), torch.randn(s, K, dtype=dt), torch.randn(K, s, dtype=dt)]
    # orthonormal-row start for the comparison maps, as in the archived initialization
    ps[0] = torch.linalg.qr(ps[0].T).Q.T.contiguous(); ps[1] = torch.linalg.qr(ps[1].T).Q.T.contiguous()
    ps = [p.requires_grad_(True) for p in ps]
    opt = torch.optim.AdamW(ps, lr=lr, weight_decay=0.0) if opt_name == "adamw" else torch.optim.SGD(ps, lr=lr)
    M0 = (ps[0] @ ps[0].T + ps[1] @ ps[1].T).detach(); B0 = (ps[2] @ ps[2].T - ps[3].T @ ps[3]).detach()
    hist = []
    for t in range(steps + 1):
        if t % (steps // 4) == 0:
            M = (ps[0] @ ps[0].T + ps[1] @ ps[1].T).detach(); Bb = (ps[2] @ ps[2].T - ps[3].T @ ps[3]).detach()
            hist.append((t, float(loss_fn(*ps, y)), float(torch.trace(M)), float((M - M0).norm()), float((Bb - B0).norm()),
                         float((ps[3] @ ps[2]).detach().norm())))
        opt.zero_grad(); l = loss_fn(*ps, y); l.backward(); opt.step()
    return hist
for name in ("sgd", "adamw"):
    for row in run(name):
        print(name, "step %5d loss %.5f tr(SQSQ^T+SKSK^T) %.3f |dM| %.3e |d(TT^T-O^TO)| %.3e ||OT|| %.3f" % row)
