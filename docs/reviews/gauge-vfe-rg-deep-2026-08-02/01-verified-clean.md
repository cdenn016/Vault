# Verified clean on the 2026-08-02 pass — do not re-derive

Everything in this file was independently recomputed by a lens expert on this pass and survived.
Add these to the settled record so the next pass inherits them. Residuals are as reported by the
verifying lens.

## Gauge theory — `02_geometry.tex`, `04_generative.tex`

Re-derived from the declared conventions and checked numerically on random `GL(2,R)` elements:
the quotient convention; the associated-coordinate law `beta' = rho_hat(a)^{-1} beta`; the
relative-frame law `h_i' = a_i^{-1} h_i b_i`; the channel relation `k_i^m = h_i^{-1} k_i^b h_i`;
both cross-map gauge laws; the gluing law; the connection law `Ad_{a^{-1}} A + a^{-1} da`;
endpoint transport; defect verticality and the `nabla^m . Phi - Phi . nabla^b` reduction,
including sign and operator order; the Cech cocycle under three-frame composition;
`T_ij = U_i U_j^{-1}` under the corrected `u_i = sigma_0 U_i^{-1}` (this is what discharges prior
ledger item R02); `T^m = h_i^{-1} T^b h_j`; walk-holonomy conjugation; all three flat-link
residuals. No critical or high finding in the chapter.

`eq:geo-defect-gauge-laws` is CORRECT. Numerically, `(DPhi)' = R_m (DPhi) R_b^{-1}` evaluates
True reading `R` as the coordinate change and False reading `R` as the represented section
rechoice; the manuscript's global convention (fixed at `04:280-285`, `06a:170-177`) is the former.
`eq:rg-linear-cross-scale-covariance` (`C' = R_{x,c}^{-1} C R_{x,f}`) is also correct; it only
looks mirrored because ch. 2 feeds `rho(g)` while ch. 7b feeds `rho(a)` with `a = g^{-1}`.

## Differential geometry / SPD — `05c`, `06a`, `06_gaussian`

Realized `05c` concretely on the SPD-associated bundle (`GL(2)` acting by the sandwich
`Sigma -> R Sigma R^T`, fiber metric one-half AIRM): gauge-invariance residual `1.2e-9` against
value `28.0`; connection-change jet `3.6e-15`; transported-section velocity `8.2e-7`
(finite-difference limited); congruence Fisher isometry `8.2e-16`. KL divergence jets verified
SYMBOLICALLY to exact zero on a curved chart (`Gamma - Gamma* = E[l_i l_j l_k]`, all 8
components). Contact counterexample exact (`alpha ^ d alpha` coefficient `-1`). Constant rank IS
assumed where the quotient is taken and IS genuinely necessary. Basicness is stated in the
correct `L_Z h = 0` form. `06_gaussian`'s thinness bound is tight (codimension exactly 1 at
`N = K = 2`); the projection characterization replicated at 4000 trials with 0 mismatches;
`06a`'s `Phi-tilde` gauge-law direction is right; `sec:gauss-open`'s summary of the
congruence-diagonal Kron closure is accurate (residual `0.0`).

## Information geometry — `08_infogeometry.tex`, `05d_relational_inference.tex`

No mathematical error found. Recomputed and surviving: natural/expectation-chart duality (exact
symbolic zero at `n = 1,2,3` and free-symbol zero at `n = 2`); `prop:ig-fisher-expectation-chart`
all three blocks; `cor:ig-mean-block-discrepancy` (`7.1e-15`); the pullback/pushforward Schur
identity (`1.5e-14`); the generalized-pencil propositions (`8.9e-16`); the whole Fisher-clock
chapter; `thm:hist-record-clock-contraction` (`nu_X^2 - nu_Y^2` vs `E Var(l^X | Y)`, residual
`3.9e-16`, plus a 4e6-sample Monte-Carlo score-projection cross-check);
`prop:pb-kl-divergence-jets` reproduces the Amari-Chentsov tensor with 0 mismatches over all
index triples. The natural-gradient identification at `08:338`/`08:350` genuinely matches
Amari 1998 (`F^{-1} grad E = R^{-1} L z` to `0.000e+00`). The recognition-vs-model Fisher trap is
NOT silently violated: ch. 8 types four spaces apart and tags the transfer OPEN.

## Variational / ELBO — `05_elbo.tex`, `05a_expfamily.tex`, `05b`

Recomputed with residuals at or below `1e-14`: the evidence identity and its equality case; the
restriction principle; the block KL chain rule and E-coordinate optimum; both (H4) witnesses; the
M-coordinate `r_n = 1 + eps h_n` witness; EM monotonicity (correctly requiring the FULL E-step);
`eq:elbo-step-size-failure` (sign flips exactly at `alpha d_max = 2`); the factorwise
decomposition and the `3MN` count; both exponential-family Bregman identities (sympy:
`simplify(KL - D_A) = 0`) and the KKT projection; boundary blow-up and the scale-family
fixed-point witness; the collective and local VFE theorems; `eq:obs-local-global-decomposition`
and `-potential` (three blocks, correlated baseline); replicator = Fisher natural gradient with
`-gamma Var_beta(c)` dissipation; data processing.

E/M blindness is respected everywhere (`req:gen-typing-prohibition`, `05b:31-35`, `05b:340-342`):
no recognition law is inserted into the generative target. Posterior consistency is correctly
stated and correctly refused for product families.

`eq:obs-global-ledger` is exact (residual `-1.11e-16`) and unconditionally valid in `[0, inf]`
given `Q << P_0 = tensor rho_i`: `Q << tensor Q_i` follows, and each KL's negative part is bounded
by `1/e`, so no `inf - inf` is reachable. **Carried-over candidate #2 is killed** — there is no
missing factorization hypothesis.

## Coarse-graining — `06_general_coarsegraining.tex`, `09_coarsegraining.tex`

No wrong mathematics. Every exactness claim survived every attempted counterexample: 118
numerical checks, worst genuine residual `1.1e-14`. All 54 cross-references resolve; no duplicate
labels. `eq:cg-elbo-monotone` is correct as an inequality under both plausible readings of the
undefined symbol, which agree to `2.2e-16`.

Hypotheses confirmed load-bearing by probes that DO break the result when removed (record these
so nobody proposes weakening them): a parameter-dependent `K_theta` drives `I_Y = 400` against
`I_X = 0.25`; a sub-Markov `K` reverses the ELBO ordering at every scale `<= 0.5`; a non-lumpable
`K` breaks Bayes recovery at `5.2e-2`; failed diagonal affinity breaks
`thm:cg-graph-exponential-closure`.

## Probability and numerics — `03_probability.tex`, `07_restrictions.tex`

Every load-bearing Chapter 7 claim independently recomputed: block optimum vs Nelder-Mead/BFGS
(`7.1e-15`); mean-restriction cost vs a genuine constrained optimizer the suite does not run
(`9.8e-15`); combined costs add (`1.1e-14`); Schur identity (`5.9e-16`, rank 4 = r);
underdispersion Loewner order (`lambda_min > 0` on all blocks, equality control `5.6e-17`);
refinement monotonicity exhaustively over all 52 partitions of 5 coordinates and all 358
refinement pairs (0 violations); gap-no-selection; both `(l, g)` witness pairs exactly.
`prop:restrict-nonnested-unordered`'s printed `0.0589` / `0.5493` reproduce to `0.0588915178` /
`0.5493061443`. All Chapter 3 proofs check line by line; every cross-reference in both chapters
resolves.

**Verification suite, live re-run** (`C:/Python314/python.exe verification/run_checks.py`):
exit 0, `{"PASS": 29, "FAIL": 0, "INCONCLUSIVE": 0}`, `inventory: PASS`, `occurrences: 11`,
`overall_status: PASS`. The counts quoted in `VERIFICATION.md` are accurate.

## RG — `07_general_renormalization.tex`, `07b`, `10_renormalization.tex`

The algebra is sound. 16 load-bearing identities recomputed, none broken: hard aggregation
`S^T Lambda S` vs the parameter formula (`3.55e-15`); the aggregation semigroup (`3.55e-15`);
`D_H R_b^H[phi] = E_{Pi_*}[phi | Z]` (`1.25e-10`); `D_H^2 = -Var` (`4.86e-08`); the Ising-star
cubic coefficient `2 sech^2(h_0) tanh(h_0) J_1 J_2 J_3` exactly 0 by sympy, with the `t^4` term
also exactly 0 as claimed; the replicator beta function exactly 0; Mobius inversion (`2.2e-15`);
nested `C/P` compositions (`<= 5e-14`); the Mori-Zwanzig memory operators rederived exactly;
heat/entropy `-dS/d log t = t^2 Var_t -> alpha` exact; the ch-10 pencil propositions exact.

## Manuscript integrity — whole tree

952 distinct labels, 0 duplicates; 405 distinct reference keys over 769 occurrences, 0 dangling;
460 bib entries, 0 duplicate keys, 0 case-collisions; 74 distinct cite keys, 0 cited-but-missing
(BibTeX `warning$ -- 0`). Build succeeds, exit 0, **215 pages**, 0 undefined references, 0
undefined citations, 0 undefined control sequences, 0 multiply-defined labels, 0 overfull and 0
underfull boxes (detection sanity-tested against a deliberate-overflow document using the same
`.sty`, which reported 2). Banned words 0; UK spellings 0; prose-rule violations 0; `\;` 0, `\!`
0, `\,` 1 (a legitimate thin space in a sum index).

**Prior ledger item R18 is discharged**: `\status{}` tags number 604 in source and 604 in the
PDF, with 0 clipped. The committed `main.pdf` is byte-size-identical to a fresh build, so the PDF
is current with sources.

## Philosophy and framing

The falsifiability posture is exemplary: the manuscript states it has no discriminating
prediction, classifies its only available test as internal, and locates empirical risk in the
added cross-scale hypothesis rather than in the theorems. The Kretschmann/Norton misattribution
corrected in an earlier pass is fully absent from the current text (grep-verified). Wheeler, Kant,
Hoffman, Gelman-Meng, and the BKS attributions all check out against primary sources. Of 40 body
`OPEN`/`CONJECTURE` sites mapped against the audit index, 36 land cleanly.
