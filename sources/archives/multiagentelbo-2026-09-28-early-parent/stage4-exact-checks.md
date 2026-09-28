# Stage 4 exact and numerical checks: early first-contrast activation

Date: 2026-09-28. Author model: Claude Opus 5.5 (`claude-opus-5-5`). Verifier model: Claude
Fable 5.1 (`claude-fable-5-1`), verdict VALID_WITH_MINOR_ISSUES on the computations and their
reading, recorded in `stage4-crossmodel-exact-checks.md`. The three exposition fixes listed in that
report were applied afterwards by Claude Opus 5.5 and have not been re-verified.
Scope: fixed base point `c_*`, the four-cycle of `def:rg-formation-cycle-experiment` with
`T = eps^8`, no base transport, no stochastic simulation. The vault was read, not edited.

## Reproduction

The scripts and their executed outputs are in
`docs/derivations/2026-09-26-selection-to-formation/stage4-evidence/`. Both ran with the CPU
interpreter `C:\Python314\python.exe` (sympy 1.14.0, mpmath 1.3.0), from inside that folder.

    python stage4_cycle_exact.py  > stage4_cycle_exact_output.txt   # exit 0, 124/124 exact checks PASS
    python stage4_numeric.py      > stage4_numeric_output.txt       # exit 0, also writes stage4_numeric_output.json

`stage4_cycle_exact.py` works over sympy with `T > 0` symbolic and asserts every identity.
`stage4_numeric.py` uses mpmath at 150 significant digits. It computes the Gaussian forgetting
curve two ways: a block closed form, and a full 12-dimensional Gaussian conditioning through a
numerical eigendecomposition of `A_M`. The second computation checks the implementation of the
block reduction, namely that `A_M` is block diagonal on `W_M + Z_M` and that `P_Z x_circ = 0` in
floating point; it is a code-path consistency check and says nothing about the surrogate's
relevance to the conditioned law.

## Task 1: exact construction (all identities hold exactly, both matchings)

Coordinates are `x = (k_0..k_3, m_0..m_3, w_0..w_3)`, with edge `e_i` running from `i` to `i+1`
and `r^b_i = k_{i+1} - k_i - w_i`, `r^m_i = m_{i+1} - m_i - w_i`. For `S^(0) = (1,0,3,2)`, the
selected edges are `e_0, e_2` and the exterior edges are `e_1, e_3`. For `S^(1) = (3,2,1,0)`,
the selected edges are `e_1, e_3` and the exterior edges are `e_0, e_2`. Every edge has the Gram
matrix `[[3,1],[1,3]]`. The Hessian of `V_S`, computed from its definition with each matched
edge counted from both ends, equals `H_M = 2 sum_g (a^b_g a^b_g^T + a^m_g a^m_g^T)`. Its rank is
4, so its kernel has dimension 8.

The four normals `n^+_g = (a^b_g + a^m_g)/(2 sqrt2)` and `n^-_g = (a^b_g - a^m_g)/2` are
orthonormal, with `H_M n^+ = 8 n^+`, `H_M n^- = 4 n^-`, `R_ev n^+ = 0`, and
`R_ev n^- = 4 n^-`, where `R_ev = 2 D^T D`. Take `Z_M = span{(n^+_e - n^+_f)/sqrt2, n^-_e, n^-_f}`
and `W_M = Z_M^perp`. Then `dim W_M = 9`, both `H_M` and `Omega = I + R_ev` preserve `W_M` and
`Z_M` (`W^T H Z = W^T Omega Z = 0`), and `K_M = H_M + T Omega` restricted to `Z_M` is
`diag(8+T, 4+5T, 4+5T)` in that basis. The full characteristic polynomial is
`(l-T)^6 (l-5T)^2 (l-4-5T)^2 (l-8-T)^2`. `W_M` contains `ker H_M` and the fast common normal
`u_+ = (n^+_e + n^+_f)/sqrt2`, with `K_M u_+ = (8+T) u_+`.

The hidden projection of `+x_circ` and of `-x_circ` is zero for both matchings. The loop
covector annihilates `Z_M` and pairs to `-1/sqrt2` with each `n^+`. Each exterior common
residual `(r^b_g + r^m_g)/2` annihilates `Z_M`. Each cost satisfies
`D_g = ((r^b+r^m)/2)^2 + ((r^b-r^m)/2)^2`, which gives the inequality used in part (d).

The center-path formula holds. With `p = sum_sel (a^b + a^m)`, the vector `x_circ + p/4` lies in
`ker H_M`, `H_M p = 8p`, and `R_ev x_circ = R_ev p = 0`. The path
`xbar(t) = e^{-Tt}[x_circ + (1 - e^{-8t}) p/4]` solves `xbar' = -K_M xbar` from `x_circ`. Along
it, every selected residual equals `-e^{-(8+T)t}` and every exterior residual equals
`e^{-Tt}(-3/2 + e^{-8t}/2)`, in both channels. The path also satisfies `kbar = mbar`,
`z_+ = -e^{-(8+T)t}`, and hidden coordinates identically zero.

The selected-cost decomposition holds as a polynomial identity in `x`, with normalization
exactly as stated. Put `z_+ = u_+.x`, `z_1 = ((n^+_e - n^+_f)/sqrt2).x`, `z_2 = n^-_e.x`, and
`z_3 = n^-_f.x`. Then `D_e = (z_+ + z_1)^2 + z_2^2` and `D_f = (z_+ - z_1)^2 + z_3^2`. At the
residual level, `r^b_e = z_+ + z_1 + z_2`, `r^m_e = z_+ + z_1 - z_2`, `r^b_f = z_+ - z_1 + z_3`,
and `r^m_f = z_+ - z_1 - z_3`. Every selected residual covector annihilates `ker H_M`. The
Gaussian identity behind the hazard bound was checked by completing the square. The two factors
`1/(1 - 2 sigma^2/T)` are `(8+T)/(6+T)` and `(4+5T)/(2+5T)`. Both decrease in `T`, with values
`4/3` and `2` at `T = 0`. This confirms the factors `sqrt(4/3)` and `sqrt2` and the exponent
bound `4 z_+^2/(3T)`.

One structural fact not stated in the sources also comes out of the exact computation. The
exterior half-difference `(r^b_g - r^m_g)/2` has `Z_M`-components `(0, -1/2, -1/2)`, so each
exterior belief residual carries the hidden term `-(z_2 + z_3)/2`. Together with the internal
identities above, this shows that both the internal and the boundary clauses of the contrast
event read hidden coordinates. So the contrast event `E_T` is not measurable with respect to the
retained path.

## Task 2: Gaussian-surrogate forgetting curve

The held-`M` OU process `dX = -A_M X dt + sqrt(2T) dW`, with `A_M = K_M`, starts from
`N(x_circ, s^2 I)`. Hidden and retained coordinates stay independent because `A_M` is block
diagonal in `W_M + Z_M` and `P_Z x_circ = 0`. The mean discarded conditional relative entropy
against `N(0, T K_Z^{-1})` is therefore
`H(t) = sum_k (1/2)[u_k - log(1+u_k)]` with `u_k = e^{-2 lambda_k t}(s^2 lambda_k/T - 1)`.
The generic 12-dimensional computation agrees with this closed form to relative difference
below `4e-70` at every tabulated point (largest `3.3e-70`). This agreement is a code-path
consistency statement about the block reduction, not evidence that the surrogate describes the
law conditioned on the prefix or on `E_T`. Selected rows follow, with `L = log(1/eps)` and
`H` in nats; the complete table is in `stage4_numeric_output.txt`.

| eps | s | H(L/4) | H(L/2) | H(L/2+1) | H(L) | H(2L)=H(t_eps) | T H/e^{-8t} at L/2 |
|---|---|---|---|---|---|---|---|
| 1e-2 | rho/sqrt48 | 8.33e6 | 826.6 | 0.0330 | 3.47e-11 | 3.47e-43 | 8.27e-6 |
| 1e-2 | rho | 4.00e8 | 3.999e4 | 10.75 | 8.00e-8 | 8.0e-40 | 4.00e-4 |
| 1e-3 | rho/sqrt48 | 8.33e12 | 8.33e6 | 2788 | 3.47e-11 | 3.47e-59 | 8.33e-6 |
| 1e-4 | rho/sqrt48 | 8.33e18 | 8.33e10 | 2.80e7 | 3.47e-11 | 3.47e-75 | 8.33e-6 |
| 1e-4 | rho | 4.0e20 | 4.0e12 | 1.34e9 | 8.00e-8 | 8.0e-72 | 4.00e-4 |

Before the threshold, `T H / e^{-8t}` sits on the plateau `s^2(4+5T)`, which equals
`8.33e-6` for `s = rho/sqrt48` and `4e-4` for `s = rho`. In that regime `H` grows like
`s^2 e^{-8t}/T`, which is of order `T^{-1/2}` at `t = L/2`. `H = 1` is reached at
`t - L = -1.557, -1.403, -1.073` for `s = rho/sqrt48, rho/sqrt14, rho`, independently of
`eps`. The leading-order threshold is `t = L + (1/8)log(4 s^2)`, which gives `-1.462, -1.308,
-0.978`. Past the threshold the curve decays as `8 s^4 e^{-16(t-L)}`. Consequently `H(L+c)` does
not depend on `eps`; for example `H(L) = 8 s^4 = 3.47e-11` for `s = rho/sqrt48`. A vanishing
bound at fixed `s` therefore needs `t - L -> infinity`, which is the `log(1/eps) + omega(1)`
requirement. At `t_eps = 2L` the surrogate equals `8 s^4 eps^16`. This is 20 to 23 orders of
magnitude below `eta_eps = 4.5e-20` at `eps = 1e-2`: the proof's convexity bound is linear in
`e^{-8t}` (the mean-shift, or Dirac-seed, worst case), while a Gaussian mixture over `z_0` is
quadratic.

Beyond the surrogate itself, the curve gives a rigorous lower bound. For any joint law,
`E_y KL(q(z|y) || kappa) = KL(q_{YZ} || q_Y x kappa) >= KL(q_Z || kappa)`. By Donsker and
Varadhan with the quadratic test function `log dN(m,C)/dkappa`, this is at least
`KL(N(m,C) || kappa)`, where `m` and `C` are the hidden mean and covariance. The surrogate value
is exactly this quantity for the held law started from any initial law with zero hidden mean and
hidden covariance `s^2 I`. For the uniform law on the ball `|x - x_circ| < rho` in `R^12`, the
hidden covariance is `(rho^2/14) I`, so the `s = rho/sqrt14` rows are lower bounds for the
held process from that law. For `N(m_0, I)` restricted to the ball, the covariance is modified
by the density ratio on the ball; that correction and the prefix conditioning were not computed.

## Task 3: first internal-threshold crossing and the first qualifying completion time

The thresholds are `sqrt T = eps^4`. The belief threshold is `|r^b| <= sqrt2 eps^2` and the model
threshold is `|r^m| <= eps^2`, since `sigma_ev^2 = 1/2`. The model threshold always binds. On
the center path the crossing is at `2L/(8+T)`, about `L/4`. A hidden `n^-` discrepancy of initial
size `delta` alone crosses at `log(delta/eps^2)/(4+5T)`, about `L/2 + (1/4)log delta`. For
`delta = rho/4` the two single mechanisms cross over at `eps` about `1/400`.

| eps | center (model) | hidden rho/4 (model) | binding | superposed worst sign | ball worst, noise margin eps^2/8 | tau: center / rho/4 / ball | L/2+1 |
|---|---|---|---|---|---|---|---|
| 1e-2 | 1.1513 | 0.8047 | center | 1.1825 | 1.2960 | 2.151 / 2.182 / 2.296 | 3.303 |
| 1e-3 | 1.7269 | 1.9560 | hidden | 1.9888 | 2.3381 | 2.727 / 2.989 / 3.338 | 4.454 |
| 1e-4 | 2.3026 | 3.1073 | hidden | 3.1077 | 3.4873 | 3.303 / 4.108 / 4.487 | 5.605 |

The ball worst case is computed as `sup |r^m(t)| = e^{-(8+T)t} + rho sqrt(2e^{-2(8+T)t} +
e^{-2(4+5T)t})`, with the tube margin `sqrt3 delta_eps = eps^2/8` subtracted from the threshold.
The boundary clause `|r_ext| > 1` holds on the center path for all `t > 0`, and on the ball plus
the tube after `t = 0.0044`, so it never binds. The first qualifying completion time is
therefore `tau = t_int + 1`, and on the seed events `tau <= L/2 + 1 - m` with margin
`m = 1.007, 1.116, 1.118` at the three tabulated `eps`; the hidden-binding limit of the margin
is `-(1/4)log rho = 1.151` less the tube shift. Hypothesis H-b's `tau <= L/2 + 1` holds with
margin about one in the noise-free flow with the Chebyshev tube margin. At
`tau`, a Dirac seed `z_2(0) = rho/4` carries hidden relative entropy `3268`, `5.16e8`, and
`6.69e12` at `eps = 1e-2, 1e-3, 1e-4`. Multiplied by `eps^4` this gives `3.3e-5`, `5.2e-4`, and
`6.69e-4`, which approaches `2e^{-8} = 6.71e-4`: when the hidden coordinate binds,
`z_2(tau) = eps^2 e^{-4}` and the relative entropy is `2e^{-8} eps^{-4}`. The Gaussian
surrogate at the same `tau` is `2.2e3`, `3.4e8`, and `4.5e12` for `s = rho/sqrt48`. Early
activation at `tau` therefore carries discarded hidden information of order `T^{-1/2}`, as H-b
predicts.

Task 3b checks which block is first. Along noise-free held paths, which of the two matched pairs
of a seed crosses first is decided by hidden initial data. With `z_+(0) = -1`, the sign of `z_1`
decides when `z_2 = z_3 = 0`, and otherwise the larger of `z_2, z_3` delays its pair. For example,
at `eps = 1e-4`, `z_2(0) = rho/4` gives `t_e = 3.1077` against `t_f = 2.3026`. So on a seed event
the first-block mark `K_T` is, in the noise-free flow, a function of hidden coordinates; this is
the half-space mechanism of `rem:phil-conditioned-hidden-sign`. The illustration is noise-free.
A Chebyshev-tube perturbation of size `eps^2/8` can shift crossing times by about `1/64` to `1/32`, which
exceeds the `z_1`-induced gap of `6e-4`, although typical noise, of order `eps^4`, does not.

## Task 4: constants

The table uses `p_tilde = 73728 eps^4 t* + 5 t* e^{-1/T}`, whose coefficient `5` is justified at the
end of this section. The theory's `bar eta_eps` uses `p_eps = 73728 eps^4 t* + 4 t* e^{-1/T}`
instead. The script prints both, and they agree to every printed digit at all three `eps`
because the term `t* e^{-1/T}` is of order `10^{-4.3e15}` or smaller; the tabulated values
therefore serve for either choice.

| eps | p_tilde | eta_eps | h_b(p_tilde) (nats) | (eta+h_b)/(1-p_tilde) | log10 of 4 sqrt(8/3) e^{-1/T} |
|---|---|---|---|---|---|
| 1e-2 | 7.52788e-3 | 4.5e-20 | 4.43043e-2 | 4.46404e-2 | 0.81504 - 4.3429448190325183e15 |
| 1e-3 | 1.09232e-6 | 4.5e-28 | 1.60868e-5 | 1.60868e-5 | 0.81504 - 4.34e23 |
| 1e-4 | 1.43185e-10 | 4.5e-36 | 3.38874e-9 | 3.38874e-9 | 0.81504 - 4.34e31 |

At `eps = 1e-2`, `t* = 10.21034`. The value `eta_eps` equals the proof's held bound at `t_eps`
exactly. The combined bound `0.0446` at `eps = 1e-2` is dominated by `h_b(p_tilde)` and is not
small at the largest admissible `eps`. The row ratio at mobility `eps` is at most `1.2274` on
`[0, t*]` from the linear bound, or `1.2150` from the exponential form `2e^{eps t} - 1` of the
proof's own bound `|pi - 1/2| <= (1 - e^{-eps t})/2`. On the whole horizon `[0, 2/eps]` it is at
most `2e^2 - 1 = 13.78`, and the linear form is vacuous there. Including the ratio adds `0.0899`
(for `1.23`) or `1.139` (for `13.78`) to the log10 prefactor. This is negligible against
`e^{-1/T}`. Also, `4 x 1.23 = 4.92 <= 5` gives the `5` in `p_tilde`.

Two further numbers bear on the following-window coupling. First, the Chebyshev tube fails with
probability at most `73728 eps^4` per unit time. A window after `t*` with total failure bound
`0.1` therefore has `h = 125` at `eps = 1e-2`, scaling as `eps^{-4} = T^{-1/2}`. Second, the
center-path exterior residual, less `sqrt3(rho + delta_eps)`, stays at least `13/10` until about
`0.130/T` and at least `1` until about `0.388/T`. These are consistent with H-c: windows of
length `o(T^{-1/2})` with the `eps^2` tube, and at most of order `1/T` with an order-one tube.

## What these computations do and do not settle

Everything in Task 1 is exact. The Task 2 values are exact evaluations of a Gaussian surrogate and,
through the Donsker–Varadhan remark, lower bounds for held laws with the stated hidden second
moments. They are not the law conditioned on the prefix or on `E_T`. The Task 3 times are for
the noise-free held flow with a deterministic tube margin, and the activation time `tau` in the
process is a stopping time. None of the checks involves the rows except through the ratio bound,
which stays finite at the original mobility `eps_L = eps = T^{1/8}` over `[0, 2/eps]`.

The numbers are therefore consistent with the following reading, which remains a reading and not
a proof. Deterministic late activation at `theta` in `[t_eps, t*]` gives vanishing hidden
information at `eps_L = T^{1/8}`. Activation at the first qualifying completion time carries
hidden information of order `T^{-1/2}`, a property of the held flow that is independent of the
mobility. The quantitative evidence for this is the Task 3 values at `tau`: the Dirac-seed hidden
relative entropies `3268`, `5.16e8`, and `6.69e12`, and the Gaussian surrogate `2.2e3`, `3.4e8`,
and `4.5e12`, at `eps = 1e-2, 1e-3, 1e-4`. That the contrast event and the first-block mark read
hidden coordinates, so that `E_T` is not measurable with respect to the retained path, does not by
itself imply that a conditional-information bound at early activation fails, since an event can
depend on hidden coordinates while the conditional hidden law on it stays close to `kappa`. The
surrogate values are also lower bounds only for the unconditioned held law, so they are not a
counterexample for the law conditioned on the prefix and on `E_T`; that conditional computation
remains open.
