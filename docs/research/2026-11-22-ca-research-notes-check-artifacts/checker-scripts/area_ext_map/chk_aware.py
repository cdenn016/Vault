"""prv_aware M4 instance: d=1, A=Q=P0=H=R=1. Member 1 reports {1,2,3} at t=3 and {4,5,6} at t=6;
member 2's observations at times 1,2 reach the hub at t=7,8. Exact rationals."""
from sympy import Matrix, Rational, zeros
T = 8
# Cov(x_s, x_t) = 1 + min(s,t)  (x_0 var 1, unit process noise)
def cx(s, t): return Rational(1 + min(s, t))
def weights(t, obs):          # obs: list of (member, time); returns row of E[x_t | obs] weights
    n = len(obs)
    C = Matrix(n, n, lambda a, b: cx(obs[a][1], obs[b][1]) + (1 if obs[a] == obs[b] else 0))
    c = Matrix(1, n, lambda _, b: cx(t, obs[b][1]))
    return c * C.inv()
m1 = [(1, s) for s in range(1, 7)]
evals = {3: m1[:3], 4: m1[:3], 5: m1[:3], 6: m1, 7: m1 + [(2, 1)], 8: m1 + [(2, 1), (2, 2)]}
rows = []
for t, obs in evals.items():
    w = weights(t, obs); r = zeros(1, 6)
    for k, o in enumerate(obs):
        if o[0] == 1: r[0, o[1] - 1] = w[0, k]
    rows.append((t, r))
R = Matrix.vstack(*[r for _, r in rows])
print("rank all rows on six observations:", R.rank())
print("r*(W1, evaluations before t=6):", Matrix.vstack(*[r[:, :3] for t, r in rows if t < 6]).rank())
print("r*(W1, all t):", Matrix.vstack(*[r[:, :3] for t, r in rows]).rank())
print("r*(W2, t>=6):", Matrix.vstack(*[r[:, 3:] for t, r in rows if t >= 6]).rank())
# C3 instance: member 1 reports {1,2} at t=2; member 2 reports {1,2,3} at t=3
a = weights(2, [(1, 1), (1, 2)]); b = weights(3, [(1, 1), (1, 2), (2, 1), (2, 2), (2, 3)])
print("C3 rows:", a, b[:, :2], "det", Matrix.vstack(a, b[:, :2]).det())
