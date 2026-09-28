# Stage 4 cross-model check of the exact and numerical evidence

Date: 2026-09-28. Author model: Claude Opus 5.5 (`claude-opus-5-5`). Verifier model: Claude
Fable 5.1 (`claude-fable-5-1`). The cross-model condition is satisfied. Object under review:
`stage4-exact-checks.md` and the scripts and outputs in `stage4-evidence/`. Scope: the fixed
base point `c_*`, the four-cycle of `def:rg-formation-cycle-experiment` at `T = eps^8`, no base
transport, no Lean, no stochastic simulation. The vault was read, not edited.

Verdict on the computational evidence: VALID_WITH_MINOR_ISSUES. Every exact identity and every
numerical value that I recomputed independently agrees with the author's, and the author's
scripts reproduce their stored outputs byte for byte. The minor issues are matters of
exposition in the summary, listed in the last section; none changes a number or an identity.
This verdict covers the computations and the summary's reading of them. It does not certify
the three mathematical obligations of the stage (the event-specific hidden-information bound,
the following-window coupling, and the mobility question), which the author's own PARTIAL
verdict leaves open and which remain open here.

## What I ran

The independent scripts were written from the theory sources alone, namely
`c13_formation.tex` (`def:rg-formation-cycle-experiment`, lines 1187 to 1232, and
`prop:rg-formation-endogenous-cycle`), `ca_formation_proofs.tex` (matching sector, lines 1858
to 1891, and the episode paragraph through line 1939), and the contrast-event clause of
`prop:phil-seeded-contrast-formation` in `c14_interpretation.tex` (lines 189 to 197). I read
the author's `stage4_cycle_exact.py` and `stage4_numeric.py` only after my own scripts had run.
All runs used the CPU interpreter `C:\Python314\python.exe` (CPython 3.14.4, sympy 1.14.0,
mpmath 1.3.0). Files, all under
`docs/derivations/2026-09-26-selection-to-formation/stage4-evidence/fable-recheck/`:

    fable_recheck_exact.py            sympy, symbolic T > 0, both matchings; exit 0, 148/148 checks PASS
    fable_recheck_exact_output.txt    its output
    fable_recheck_numeric.py          mpmath at 110 digits; exit 0
    fable_recheck_numeric_output.txt  its output
    fable_recheck_numeric_output.json the H(t) table as data
    rerun/rerun-log.txt               provenance of the rerun of the author's scripts, with sha256 of every file
    rerun/rerun_cycle_exact_output.txt, rerun/rerun_numeric_output.txt, rerun/stage4_numeric_output.json

The rerun executed copies of the author's two scripts from `rerun/` (the copies were deleted
afterwards; their hashes are in the log). Both exited 0, and `diff` against the stored
`stage4_cycle_exact_output.txt`, `stage4_numeric_output.txt`, and `stage4_numeric_output.json`
reported no difference. The stored outputs are therefore what the stored scripts produce on this
host.

## Independent exact reconstruction

The construction was rebuilt from the definition. With `x = (k_0..k_3, m_0..m_3, w_0..w_3)`,
`a^b_i` and `a^m_i` the covectors of `r^b_i = k_{i+1} - k_i - w_i` and
`r^m_i = m_{i+1} - m_i - w_i`, `V_S = sum_i D_{e(i,S_i)}`, `D x = k - m`, `R_ev = 2 D^T D`, and
`K_M = Hess(V_M) + T(I + R_ev)`, the following hold as symbolic identities in `T` for both
`S^(0) = (1,0,3,2)` (selected edges `e_0, e_2`) and `S^(1) = (3,2,1,0)` (selected `e_1, e_3`).

The Gram matrix of every edge is `[[3,1],[1,3]]` and the two selected edges have disjoint
supports. The Hessian of `V_S` computed by `sympy.hessian` from the definition, in which each
matched edge is counted from both ends, equals `2 sum_g (a^b_g a^b_g^T + a^m_g a^m_g^T)`, of rank
4 with an eight-dimensional kernel. The four normals `n^+_g = (a^b_g + a^m_g)/(2 sqrt2)` and
`n^-_g = (a^b_g - a^m_g)/2` are orthonormal with `H_M n^+ = 8 n^+`, `H_M n^- = 4 n^-`,
`R_ev n^+ = 0`, `R_ev n^- = 4 n^-`, and `R_ev` preserves `ker H_M`. With
`Z_M = span{u_1 = (n^+_e - n^+_f)/sqrt2, n^-_e, n^-_f}` and `W_M = Z_M^perp`, `dim W_M = 9`,
`W^T H_M Z = 0`, `W^T (I + R_ev) Z = 0`, `K_M Z = Z diag(8+T, 4+5T, 4+5T)`, and the physical
matrix `H_M + T I` restricts to `diag(8+T, 4+T, 4+T)`. `W_M` contains `ker H_M` and
`u_+ = (n^+_e + n^+_f)/sqrt2`, with `K_M u_+ = (8+T) u_+`. The characteristic polynomial of
`K_M`, computed by `Matrix.charpoly`, is `(l-T)^6 (l-5T)^2 (l-4-5T)^2 (l-8-T)^2`; the two `5T`
eigenvalues are carried by `(e_i + e_{i+1}, -(e_i + e_{i+1}), 0)` for the two matched pairs, which
lie in `ker H_M` and in the range of `D^T`.

The hidden eigenvalues of `K_M` are `8+T, 4+5T, 4+5T`. The hidden projection `Z^T(+-x_circ)` is
`(0,0,0)` for both signs and both matchings, while `u_+ . x_circ = -1`. The loop covector
`(0,0,1_4)` has `Z_M` components `(0,0,0)` and pairs to `-1/sqrt2` with each selected `n^+`. Each
exterior common residual covector `(a^b_g + a^m_g)/2` has `Z_M` components `(0,0,0)`, and each
exterior half-difference `(a^b_g - a^m_g)/2` has `Z_M` components `(0, -1/2, -1/2)`, so the
exterior belief residual `r^b_g` carries the hidden term `-(z_2 + z_3)/2` and the exterior model
residual carries `+(z_2 + z_3)/2`, on both exterior edges.

The center path `xbar(t) = e^{-Tt}[x_circ + (1 - e^{-8t}) p/4]` satisfies `xbar' = -K_M xbar`
and `xbar(0) = x_circ`, with `H_M(x_circ + p/4) = 0`, `H_M p = 8p`, `R_ev x_circ = R_ev p = 0`,
selected residuals `-e^{-(8+T)t}`, exterior residuals `e^{-Tt}(-3/2 + e^{-8t}/2)`, `kbar = mbar`,
`z_+ = -e^{-(8+T)t}`, and hidden coordinates zero. The polynomial identities
`D_e = (z_+ + z_1)^2 + z_2^2`, `D_f = (z_+ - z_1)^2 + z_3^2`, `r^b_e = z_+ + z_1 + z_2`,
`r^m_e = z_+ + z_1 - z_2`, `r^b_f = z_+ - z_1 + z_3`, `r^m_f = z_+ - z_1 - z_3` hold, every
selected residual covector annihilates `ker H_M`, and the hazard factors
`1/(1 - 2 sigma^2/T)` with `sigma^2 = T/lambda` are `(8+T)/(6+T)` and `(4+5T)/(2+5T)`, decreasing
in `T` with values `4/3` and `2` at `T = 0`.

Every item in the author's Task 1 list is therefore confirmed by an independent computation,
including the new fact about the exterior half-difference.

## Independent numerical reconstruction

The held OU process from `N(x_circ, s^2 I)` has hidden marginal `N(0, C(t))` with
`C_k = s^2 e^{-2 lambda_k t} + (T/lambda_k)(1 - e^{-2 lambda_k t})`, and the mean discarded
conditional relative entropy against `kappa = N(0, T K_Z^{-1})` is
`H(t) = sum_k (1/2)[u_k - log(1+u_k)]`, `u_k = e^{-2 lambda_k t}(s^2 lambda_k/T - 1)`. I evaluated
this with `mpmath.log1p` at 110 digits, and separately by a second formulation that propagates
the full 12-dimensional mean and covariance with `mpmath.expm`, rotates to an explicit
orthonormal `(W|Z)` basis built by Gram-Schmidt, conditions `z` on `y`, and averages the
Gaussian relative entropy over `y`. At `eps = 1e-2` the two agree to relative difference between
`1e-102` and `1e-69`, the cross covariance `S_zy` is below `1e-116` in magnitude, and the
hidden mean is exactly zero. The values at the two requested times and the other tabulated
points are, in nats,

| eps | s | H(L/2+1) mine | author | H(2L) = H(t_eps) mine | author |
|---|---|---|---|---|---|
| 1e-2 | rho/sqrt48 | 0.0330420248 | 0.033042025 | 3.47222222e-43 | 3.4722222e-43 |
| 1e-2 | rho/sqrt14 | 0.286303826 | 0.28630383 | 4.08163265e-42 | 4.0816327e-42 |
| 1e-2 | rho | 10.749992657 | 10.749993 | 8.0e-40 | 8.0e-40 |

with `L = log(1/eps) = 4.60517`, `L/2 + 1 = 3.302585`, `2L = 9.210340`. The remaining entries of
the author's Task 2 table (`L/4`, `L/2`, `L`, `2L+1`, and `eps = 1e-3, 1e-4`) also agree to every
printed digit; for example `H(L/4) = 8334147.02`, `H(L/2) = 826.6067`, and
`H(L) = 3.47220293e-11` at `eps = 1e-2`, `s = rho/sqrt48`. The plateau `T H/e^{-8t}` equals
`s^2(4+5T)` before the threshold (`8.333e-6` and `4.0e-4`), `H = 1` occurs at
`t - L = -1.5573678, -1.4033499, -1.0734677` for the three scales independently of `eps`, and
`H(L) = 3.4722029e-11` against the asymptote `8 s^4 = 3.4722222e-11`, `H(2L) = 8 s^4 eps^16`
exactly to the printed digits. The Task 3 crossing times (center `1.15129`, hidden `rho/4` alone
`0.804719`, superposed worst sign `1.18246`, ball with the `eps^2/8` margin `1.29596` at
`eps = 1e-2`, and the corresponding values at `1e-3` and `1e-4`), the margins
`L/2 + 1 - tau = 1.0066, 1.1158, 1.1179` for the ball worst case, the Dirac-seed hidden relative
entropies `3267.84`, `5.15972e8`, `6.68787e12` with `eps^4` multiples `3.27e-5`, `5.16e-4`,
`6.69e-4` against `2e^{-8} = 6.709e-4`, and the surrogate at `tau` (`2170.88`, `3.43982e8`,
`4.45858e12`) all agree with the author's Task 3. The Task 4 constants at `eps = 1e-2`
(`p = 7.52788e-3`, `eta = 4.5e-20`, `h_b = 4.43043e-2`, `(eta + h_b)/(1-p) = 4.46404e-2`,
`log10(4 sqrt(8/3) e^{-1/T}) = 0.81504 - 4.3429448190325183e15`, row ratio `1.2274` linear and
`1.2150` exponential on `[0, t*]`, `13.778` on `[0, 2/eps]`) agree, as do the `1e-3` and `1e-4`
rows.

## Reading of the theory

The author's threshold reading matches the source. The contrast event of
`prop:phil-seeded-contrast-formation` asks, on a duration-one interval inside `[0, 2/eps]`,
for internal belief and model transported relative entropies at most `eps^4 = sqrt T` and
exterior belief relative entropies above `1/2`. With `KL(q^b_{i+1} || Theta_# q^b_i) = (r^b)^2/2`
and `KL(q^m_{i+1} || Theta_# q^m_i) = (r^m)^2/(2 sigma_ev^2) = (r^m)^2`, these are
`|r^b| <= sqrt2 eps^2`, `|r^m| <= eps^2`, and `|r^b_ext| > 1`, as the author states, and the model
clause binds. The author's `tau = t_int + 1` is the completion of the first duration-one
qualifying interval in the noise-free flow, which is the right object for the event's infimum
of qualifying completion times. The identification of `kappa` with `N(0, T K_Z^{-1})` is correct
because `q^*` on the matching sheet is `N(0, T K_M^{-1})` with `K_M` block diagonal on
`W_M + Z_M`.

The lower-bound argument in Task 2 is sound as stated. For the joint law `q_t` of `(y, z)`,
`E_y KL(q_t(z|y) || kappa) = KL(q_t || q_{t,Y} x kappa) >= KL(q_{t,Z} || kappa)` by the chain rule
and marginalization, and `KL(q_{t,Z} || kappa) >= E_{q_{t,Z}} log(dN(m,C)/dkappa) = KL(N(m,C) || kappa)`
by the Donsker and Varadhan variational formula with the quadratic test function, whose
`q`-expectation depends only on the first two moments. For the held process without proposals
the hidden moments evolve autonomously, so `H(t)` bounds the discarded conditional information
of the unconditioned held law from any initial law with hidden mean zero and hidden covariance
`s^2 I`; the uniform ball gives `s^2 = rho^2/14`. The bound says nothing about the law
conditioned on the prefix event or on `E_T`, which the author states.

## Minor issues in the summary

None of these affects a number or an identity.

First, the summary's sentence that `E_T` is not measurable with respect to the retained path is a
correct pathwise statement, since `r^b_e`, `r^m_e`, and both exterior residuals are affine in
the hidden coordinates with nonzero coefficients. The final paragraph's reading that a
conditional-information bound at early activation therefore fails structurally does not follow
from non-measurability alone; an event can depend on hidden coordinates while the conditional
hidden law on the event stays close to `kappa`. The author labels this a reading rather than a
proof, and the Task 3 Dirac-seed and surrogate values are the actual quantitative evidence for
large hidden information at `tau`; the wording should point to those values rather than to
measurability.

Second, the "independent 12-dimensional Gaussian conditioning" checks the implementation of
the block reduction (that `A_M` is block diagonal on `W_M + Z_M` and `P_Z x_circ = 0` in floating
point), not the surrogate's relevance to the conditioned law. My `expm`-based formulation is
the same kind of check. Agreement at `1e-70` is a code-path consistency statement.

Third, the summary reports `(eta + h_b)/(1 - p_tilde)` with `p_tilde = 73728 eps^4 t* + 5 t* e^{-1/T}`,
whereas the theory's `bar eta_eps` uses `p_eps` with the coefficient `4`. The two are equal to
all printed digits because `e^{-1/T}` underflows, and the author's own script prints both; the
summary should say which one it tabulates.

## Scope and what remains

The computations support the stage's Task 1 identities exactly and the Task 2 to Task 4 numbers
to the printed precision, in the noise-free or Gaussian-surrogate settings the author declares.
The unresolved obligation is unchanged: an event-specific hidden-information bound for the
seeded early prefix, conditioned on the prefix and on `E_T` rather than for the unconditioned
held law, together with the following-window coupling and the mobility question at
`eps_L = T^{1/8}`. The computed evidence points the other way for early activation, since the
surrogate lower bound at `tau` is of order `T^{-1/2}` for every hidden second moment
considered, but a lower bound on a surrogate of the unconditioned law is not a counterexample
for the conditioned law. The next step that would change the answer is a computation of the
hidden conditional moments given the prefix event `A_t` on the Gaussian sheet, which is a
conditioning on a tube event and is not closed form; a Monte Carlo estimate at `eps = 1e-2`
would be the smallest executable version.
