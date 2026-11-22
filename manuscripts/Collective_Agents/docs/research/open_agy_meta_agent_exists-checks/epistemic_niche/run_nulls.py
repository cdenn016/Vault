"""Deciding script 2: the null family of tab:agy-nulls at the declared instance, and the partner-randomization test."""
import itertools, math
import numpy as np
from core import *

n, N, kappa = 4, 8, 3
P0, s, c, gam, s2 = 1.0, 1.0, 0.1, 4.0, 1e-3
R0 = 36.0                      # declared level, inside the (c)-mechanism window (18.598, 54.086]
NNULL, ALPHA = 999, 0.01
rng = np.random.default_rng(7)
law, _ = deliberation_law(n, n - 1, P0, s, c, gam)
profs = profiles(n)
out = []
def say(*a):
    line = " ".join(str(x) for x in a); print(line); out.append(line)

def att_full(i, p):
    return [(tuple(j for j in range(n) if j != i), 1.0)]

def att_random(i, p):          # uniform kappa-subset of the N-1 others, restricted to co-members
    lst = []
    for r in range(0, min(kappa, n - 1) + 1):
        if kappa - r > N - n: continue
        pr = math.comb(N - n, kappa - r) / math.comb(N - 1, kappa)
        lst += [(U, pr) for U in itertools.combinations([j for j in range(n) if j != i], r)]
    return lst

def summarize(SAa, SBb, tag):
    Pi = np.linalg.inv(block_diag(SAa, SBb)); d = diffusive(Pi)
    if not d[0]:
        say(tag, "non-diffusive (max offdiag %.3g): contrast undefined, no region selected" % d[1]); return None
    regs = region_contrasts(Pi); Cm = max(regs, key=regs.get)
    say(tag, "| r(A)", round(regs[tuple(range(n))], 4), "| max region contrast", round(regs[Cm], 4), "at", Cm,
        "| selected at r0:", [C for C, r in regs.items() if r >= R0])
    return regs

S0 = None
say("expect: every type-D null below r0 =", R0, "(full model r(A)=54.086)")
full = summarize(SA := sigma_c_enum(n, law, att_full, P0, s, c, s2), SA, "FULL")
S0 = min(full[tuple(range(n))], full[tuple(range(n, N))]); S0p = max(full.values())

uni = np.full(2 ** n, 2.0 ** -n)
Sh = sigma_c_enum(n, uni, att_random, P0, s, c, s2); summarize(Sh, Sh, "N_hab (slots and attention from uniform habits)")
Shs = sigma_c_enum(n, uni, att_full, P0, s, c, s2); summarize(Shs, Shs, "diagnostic: slots from habits, attention kept")
for nm, L in [("P^inf (declared)", law), ("all open", np.eye(2 ** n)[-1]), ("uniform", uni)]:
    Sp = sigma_c_enum(n, L, att_random, P0, s, c, s2); summarize(Sp, Sp, "N_pr annealed, slot law " + nm)

# deletion nulls: every inter-agent channel (messages and announced intentions) delivers pure noise;
# members fuse n-1 noise 'readings' with the kept precision; policies independent (marginals of P^inf).
pm = law @ profs                                   # marginal open probabilities
def sigma_deleted(noise_var):
    Sg = np.zeros((n, n)); EC = np.zeros(n); ECC = np.zeros((n, n))
    for k, p in enumerate(profs):
        w = np.prod(np.where(p == 1, pm, 1 - pm))
        P = 1 / (1 / P0 + p / s + (n - 1) / (s + c))
        Sg += w * np.diag(P ** 2 * (p / s + (n - 1) * noise_var / (s + c) ** 2))
        coef = P * p / s - 1.0; EC += w * coef; ECC += w * np.outer(coef, coef)
    return Sg + (ECC - np.outer(EC, EC)) * P0 + s2 * np.eye(n)
for nm, var in [("N_lp/N_rn (noise var P0+s+c)", P0 + s + c), ("N_fr (deterministic frozen content)", 0.0)]:
    Sd = sigma_deleted(var)
    say(nm, "| max |offdiag| of Sigma^c", np.abs(Sd - np.diag(np.diag(Sd))).max(), "| region max contrast",
        max(region_contrasts(np.linalg.inv(block_diag(Sd, Sd))).values()))

# coordinator's symmetric variant: owner also reads through a receiver-specific channel, so the slot noise
# is shared by several receivers and is conditioned on (def:col-world-conditional): only nu remains.
def sym_variant(L):
    # given (eta, v, profile): e_i = P(S)[sum_open (eta+v_j+nu_ij)]/(s+c) - eta; P(S) = (1/P0+S/(s+c))^-1
    Sv = np.zeros((n, n)); EX2 = 0.0; EXeta = 0.0; EXv = np.zeros(n)
    for k, p in enumerate(profs):
        S_ = p.sum(); P = 1 / (1 / P0 + S_ / (s + c))
        Sv += L[k] * np.eye(n) * P ** 2 * S_ * c / (s + c) ** 2
        EX2 += L[k] * P ** 2 * (S_ ** 2 * P0 + S_ * s) / (s + c) ** 2
        EXeta += L[k] * P * S_ / (s + c); EXv += L[k] * P * p / (s + c)
    common = EX2 - (EXeta ** 2 * P0 + np.sum(EXv ** 2) * s)      # E_{eta,v} Var_profile(conditional mean), same for all members
    return Sv + common * np.ones((n, n)) + s2 * np.eye(n), common
for nm, L in [("all-open profile (control, expect r = 1)", np.eye(2 ** n)[-1]), ("profiles from P^inf", law)]:
    Sv, com = sym_variant(L)
    say("symmetric-owner variant (slot noise shared by all readers, conditioned on),", nm, "| common term", com,
        "| r(A)", contrast(np.linalg.inv(block_diag(Sv, Sv)), range(n)))

# quenched partner randomization: n_null independent draws, statistic S = min(r(A), r(B)) (0 if no region selected)
others = lambda i: [j for j in range(N) if j != i]
stats, statsp, nondiff = [], [], 0
for l in range(NNULL):
    T = [rng.choice(others(i), size=kappa, replace=False) for i in range(N)]
    blocks = []
    for base in (0, n):
        U = [tuple(int(j) - base for j in T[base + i] if base <= j < base + n) for i in range(n)]
        blocks.append(sigma_c_enum(n, law, lambda i, p, U=U: [(U[i], 1.0)], P0, s, c, s2))
    Pi = np.linalg.inv(block_diag(*blocks))
    if not diffusive(Pi)[0]:
        nondiff += 1; stats.append(0.0); statsp.append(0.0); continue
    rA_, rB_ = contrast(Pi, range(n)), contrast(Pi, range(n, N))
    stats.append(min(rA_, rB_))
    statsp.append(max(max(contrast(Pi, C) for C in itertools.combinations(range(b, b + n), r))
                      for b in (0, n) for r in range(2, n + 1)))
stats, statsp = np.array(stats), np.array(statsp)
p1 = (1 + np.sum(stats >= S0)) / (NNULL + 1); p2 = (1 + np.sum(statsp >= S0p)) / (NNULL + 1)
say("N_pr quenched: n_null", NNULL, "| non-diffusive draws", nondiff, "| S0", round(S0, 4), "max S_l", round(stats.max(), 4),
    "q95", round(np.quantile(stats, 0.95), 4), "| p", p1, "reject at", ALPHA, ":", p1 <= ALPHA)
say("N_pr quenched, within-niche max-region statistic: S0'", round(S0p, 4), "max", round(statsp.max(), 4), "| p", p2,
    "| draws with any region >= r0:", int(np.sum(statsp >= R0)))
open("nulls_out.txt", "w").write("\n".join(out) + "\n")
