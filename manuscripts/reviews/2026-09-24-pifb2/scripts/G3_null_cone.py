r"""G3: pointwise check that a null cone fixes a Lorentzian metric up to a factor (PIFB2.tex:1980).

Claim at 1980: "The cone fixes g only up to a conformal factor". Pointwise this is the
linear-algebra lemma: if a symmetric bilinear form q vanishes on every null vector of
eta = diag(-c^2, 1, ..., 1), then q = lambda * eta. We impose q(v, v) = 0 on sampled null
vectors v = (1/c, n), |n| = 1, and compute the null space of the resulting linear system in
the n(n+1)/2 components of q. A one-dimensional null space spanned by eta confirms the
lemma. (The global statement, that the causal order fixes the conformal class, is the
Hawking-King-McCarthy / Malament theorem proposed as a citation by L15-2.)
"""
from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(1)
    c = 1.7
    for dim in (2, 3, 4, 5):
        iu = np.triu_indices(dim)
        rows = []
        for _ in range(4 * dim * dim):
            n = rng.standard_normal(dim - 1)
            n /= np.linalg.norm(n)
            v = np.concatenate([[1.0 / c], n]) * rng.uniform(0.5, 2.0)
            M = np.outer(v, v)
            M = M + M.T - np.diag(np.diag(M))  # coefficient of q_ab (a<=b) in q(v,v)
            rows.append(M[iu])
        A = np.array(rows)
        _, s, Vt = np.linalg.svd(A)
        null_dim = int(np.sum(s < 1e-10 * s[0]))
        q = np.zeros((dim, dim))
        q[iu] = Vt[-1]
        q = q + q.T - np.diag(np.diag(q))
        eta = np.diag([-(c**2)] + [1.0] * (dim - 1))
        lam = q[1, 1]
        resid = np.linalg.norm(q / lam - eta)
        print(f"dim={dim}: null-space dimension={null_dim}, smallest s={s[-1]:.2e}, next={s[-2]:.2e}, ||q/lambda - eta||={resid:.2e}")


if __name__ == "__main__":
    main()
