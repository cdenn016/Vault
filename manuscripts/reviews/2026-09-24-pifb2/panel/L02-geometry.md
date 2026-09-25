# L02 panel report: differential geometry (Riemannian geometry, SPD manifolds, pullback metrics)

**Lens:** L02, differential geometry. **Model:** Claude Opus 5.5 (`claude-opus-5-5`), investigator only (no adjudication).
**Target:** `Research/manuscripts/PIFB2.tex` (SHA-256 `f80e6dab…080ec4`, per BRIEF).
**Lines read in full:** 136-235, 296-366, 420-519, 940-1005, 1325-1533, 1860-2070, 2320-2355, 2592-2663. Theory context read: `Theory/b02_base_direction_geometry.tex` 1-250 and `Theory/g05_fisher_geometry.tex` 49-100. Prior reviews checked for overlap: `docs/reviews/2026-09-13-program-review-next-phase/pifb-geometry-review.md` (grep), `docs/reviews/2026-09-23-theory-streamlining-review/findings/C1-pifb2-program-alignment.md` (node table N12, N18, N19).
**Executed (bare `python`, float64 NumPy/SciPy, SymPy 1.14; all run in seconds):**
`scripts/L02_fisher_curvature.py` (Fisher metric jet, full Riemann tensor of the K=1 and K=2 Gaussian Fisher manifolds), `scripts/L02_pullback.py` (R² Gaussian pullback, rank, frame and gauge behavior, combined-tensor signature), `scripts/L02_retraction.py` (SPD exponential map, natural gradient, BCH, frame pullback metric), `scripts/L02_hessian_blocks.py` (two-agent GL(2) Hessian blocks, chart dependence of the coordinate Hessian, the alpha* thresholds).
**Primary source checked:** Skovgaard 1984 (Scand. J. Stat. 11:211-223) was not retrievable in full text; its positive-curvature result is confirmed secondarily by Nielsen 2023 (PMLR 221, "Fisher-Rao and pullback Hilbert cone distances on the multivariate Gaussian"), which states that the Gaussian manifold "is not a NPC manifold when d>1 since some sectional curvatures can be positive (Skovgaard, 1984)", and independently by my direct computation below. The locator inside Skovgaard's paper is not pinned.

## Findings (ranked)

### L02-1: The regulator obstruction is attached to the wrong object; the implemented Fisher pullback already has a regulator-free gauge-invariant form
**Location:** PIFB2.tex:2017 and 2022-2026 (`prop:regulator_obstruction`), 1874-1877 (`eq:induced_metric_full`), 1882, 194, 2042.
**Severity:** high
**Evidence:** Line 2017 says the direct average of the agents' metrics "fails the gauge test", and line 2022 says the Haar-averaged consensus metric is "the framework's only candidate gauge-invariant geometric observable". The obstruction proof at line 2024 uses only the transformation of the horizontal block, `A -> g^{-1}Ag + g^{-1}dg`. The implemented metric is the score-only block (line 1877), and that block behaves differently. I ran `L02_pullback.py` on a K=3 section over R² with Regime-I frames `U(c)=exp(phi(c))`:
- Under the proposition's own action, local right translation `U_i -> U_i h(c)`, the beliefs `q_i` and the links `Omega_ij` are untouched, so the score-only pullback of `q_i` is unchanged by construction. Only `tr(A_mu A_nu)` moves (relative change 2.27).
- Under the lattice action of line 341, `U_i -> g_i(c) U_i` with `q_i -> rho(g_i(c)) q_i`, the ordinary fixed-gauge pullback changes by a relative 0.99. The frame-stripped pullback does not change: it is the pullback of `qhat_i = rho(U_i^{-1}) q_i`, which is the covariant derivative `D q_i = dq_i - rho_*(dU_i U_i^{-1}) q_i` taken with the agent's own Regime-I connection. Its residual is 1.29e-11. The same tensor is invariant under the global right redundancy with residual 1.18e-11.
- Under the lattice action, `tr(AA)` changes by a relative 3.79. The manuscript is right that this block is not invariant.

Under either local action, then, the Fisher block has a form that is invariant with no orbit average. The non-invariance, and hence the need for a regulator, belongs only to the optional horizontal trace block. The Theory already proves the general statement: `Theory/b02_base_direction_geometry.tex`, `thm:pb-pullback-gauge-invariance`, shows that covariant pullbacks are passively gauge invariant and connection-relative.

The compact-group argument at line 2024 is also imprecise. With a finite agent set or a lattice, the local gauge group is `G^N`, which is compact when G is, so the Haar average of any continuous integrand is finite. The divergence appears only in the continuum limit, because `g^{-1}dg` built from independent Haar variables at lattice spacing `eps` scales as `1/eps`. The correct reason is that `Map(C,G)` is infinite-dimensional and not locally compact, so it has no Haar measure. It is not that the Lie algebra "carries no normalizable uniform measure".

The same point settles line 1882: `G_i^{(p)}` "inherits its profile from the parent's belief" through `p_i = Omega_{i,I}[q_I]` only for the covariant pullback. For the ordinary pullback, a c-dependent `Omega_{i,I}` adds frame-gradient terms, which is the 0.99 relative change above.
**Fix:** Define `nabla^{(i)}` in `eq:induced_metric_full` as the Regime-I covariant derivative `D q_i = dq_i - rho_*(dU_i U_i^{-1}) q_i` and cite `thm:pb-pullback-gauge-invariance`. Restrict `prop:regulator_obstruction` to the horizontal trace block, give "`Map(C,G)` is not locally compact (continuum limit)" as the reason, and replace "only candidate gauge-invariant geometric observable" with: "the presence-weighted average of covariant Fisher pullbacks is gauge invariant without averaging, but it is relative to the agents' connections. The Haar-average obstruction concerns only the optional frame-twist block."
**Falsifies:** A demonstration that the lattice action intended at line 341 does not act on `q_i` by `rho(g_i)`, or that the frame-stripped pullback changes under it. The script's (d) line would then show an O(1) change.
**Status:** The proposition is labeled a "Level-2 mathematical fact" (line 2022). Its conclusion is correct for the trace block (P), but as stated for "the consensus metric" it is over-scoped: status inflation from a block-specific result to the whole observable.

### L02-2: The combined tensor adds an indefinite trace block to the PSD Fisher block with no coupling constant, so its signature depends on an arbitrary normalization
**Location:** PIFB2.tex:1874 (`eq:induced_metric_full`), 1896, 1960, 1969-1975 (`prop:4d_signature`).
**Severity:** medium
**Evidence:** `G^{(q)} = tr(A_mu A_nu) + E[score x score]` sums a form that is dimensionless per coordinate² (its scale set by the normalization of the generator T) and a Fisher form in nats per coordinate². Line 1960 concedes that "the ±2 coefficients are artifacts of the unnormalized T", which is harmless for the trace block alone but not inside the sum. In `L02_pullback.py` (e), with a Fisher time entry of 0.9 and `dpsi_tau = 0.6`, the combined `G_tt` is +0.54, +0.18, and -0.54 for `tr(S^2) = -1, -2, -4`. The time direction is timelike only for the largest normalization. Both signature propositions are statements about the trace block by itself (1933-1938, 1968-1972), yet line 1896 calls "`G_i^{(q)}, G_i^{(p)}`" positive semidefinite, while line 1874 uses the same symbol for the indefinite sum. The Theory makes the analogous point for two Fisher channels: a joint geometry needs declared positive weights, and "unit weights are a specialization" (`hyp:pb-weighted-product-geometry`, `eq:pb-weighted-channel-pullback`).
**Fix:** Write `G^{(q)}_i = kappa tr(A A) + h^{omega}_{q_i}` with an explicit declared constant `kappa`. Reserve `G^{(q)}` for the PSD Fisher block and give the combined tensor its own symbol. State that the Lorentzian propositions concern `kappa tr(A A)` alone, and that the combined tensor is Lorentzian at a point only if `2 kappa (d_tau psi_tau)^2 > h_tautau` and the spatial block stays positive.
**Falsifies:** A normalization principle in the manuscript that fixes `kappa` relative to the Fisher block, for example from the free energy.
**Status:** The signature propositions are P for the trace block (D under the listed postulates). Carrying them over to "the induced metric" is inflation.

### L02-3: The "mass matrix" is a coordinate Hessian, which is not a tensor away from critical points; the kinetic-metric postulate does not specify a connection
**Location:** PIFB2.tex:1402 ("defines a configuration-space metric on belief space"), 1445-1449, 1521-1526 (postulate, `eq:full_kinetic`).
**Severity:** medium
**Evidence:** The second variation is taken in the flat affine chart of `Sym(K)` (line 1447). Such a Hessian is chart-independent only at critical points of `F`. The postulate evaluates it "at consensus" (`mu_i = tilde mu_k`, `Sigma_i = Omega Sigma_k Omega^T`), which is not a critical point whenever the prior shadow or sensory terms are off target. In `L02_hessian_blocks.py`, for `f(Sigma) = KL(N(0,Sigma)||N(0,Sigma_p)) + ½ tr(Lambda_o Sigma)`, the second variation along the same tangent vectors agrees in the `Sigma` and `Lambda = Sigma^{-1}` charts at the critical point (relative difference 6.1e-7, finite-difference level) and differs at a non-critical point (0.3297 versus 0.4922, relative 0.49). The flat-chart Hessian and the Riemannian Hessian of the Fisher/AIRM metric that the paper uses for natural gradients differ by a Christoffel-times-gradient term, and the implementation parameterizes by Cholesky factors, which is a third chart. The Hessian is also not a metric off consensus: the manuscript itself records a negative-semidefinite `-tau^{-1} Cov` correction (line 1413) and a rank-one negative prior term (line 1510).
**Fix:** Either impose the postulate only at critical points of `F` (full stationarity, not only consensus) or define `M` as the covariant Hessian of a declared connection, naturally the Fisher Levi-Civita connection. Replace "defines a configuration-space metric" with "defines a symmetric bilinear form, positive definite at the reciprocal-consensus critical point".
**Falsifies:** A statement in the text that "consensus" includes stationarity of the prior and sensory terms, or an explicit connection choice elsewhere.
**Status:** The block formulas are P (verified below). The metric reading is a postulate (F4) and is correctly fenced, but its chart dependence is unstated.

### L02-4: The gauge-sector kinetic metric `G_phi = G_pull` is flat and not invariant under the declared gauge redundancy; "gauge-group curvature" is metric-dependent
**Location:** PIFB2.tex:1526, `eq:pullback_metric` (984-995), 429 (gauge-group curvature).
**Severity:** medium
**Evidence:** Line 1526 takes `G_phi` from `eq:pullback_metric`, the pullback of the flat ambient Frobenius metric through `exp`. It is not left-trivialized, although line 1526 calls it "left-trivialized". Since `exp` is a local diffeomorphism where `dexp^L` is regular, `(gl(K), G_pull)` is locally isometric to flat `R^{K²}`, so its Riemann tensor vanishes (a derivation: a pullback of a flat metric by a local diffeomorphism is flat). The kinetic term `½ G_pull(phi_dot, phi_dot) = ½ ||U_dot||_F^2` is not invariant under the manuscript's global redundancy `U -> U g` (line 341). In `L02_retraction.py` (10), `||U_dot g||^2 / ||U_dot||^2 = 5.795` for a random `g` in GL(3), and exactly 1 for orthogonal `g`. It is not left invariant either. This is expected, since GL⁺(K) has no bi-invariant Riemannian metric (Milnor 1976, Lemma 7.5), but line 1526 does not record it. Line 429 treats "the structure group G" as "a curved manifold" and says group curvature "determines how gauge transformations compose". Composition is governed by noncommutativity, which is metric-free. The Riemannian curvature of GL(K) depends on the chosen metric: zero for `G_pull`, and mixed sign for left-invariant metrics (Milnor 1976). The SO(3) ≅ RP³ remark holds for the bi-invariant metric and does not transfer to the canonical GL(K).
**Fix:** At line 1526 state that `G_pull` is flat and breaks the right-translation redundancy for non-orthogonal `g`, so `eq:full_kinetic` is frame-dependent in its gauge sector. At line 429 separate noncommutativity from curvature and name the metric whenever a group curvature is claimed.
**Falsifies:** A demonstration that `½||U_dot||_F^2` is invariant under `U -> U g` for non-orthogonal `g`. The script shows it is not.
**Status:** The line-429 curvature paragraph is S presented as structure. The `G_pull` construction itself is P (verified below).

### L02-5: "Nothing on the base but induced geometry" is contradicted by the background density, the chart metric used for the sectors, and dim C = 2
**Location:** PIFB2.tex:146-153, 429, 508-509, 2033-2035, 2042.
**Severity:** medium
**Evidence:** Line 2042 says "the base manifold C carries no intrinsic metric, distance, or temporal direction, all such structure being induced by agent beliefs". The construction nonetheless uses a background density (every `int ... dc` in the functional, line 940), a background metric `g_0` for the sector decomposition (line 2033 takes "`g_0` to be the flat background chart metric"), periodic boundary conditions, and a metric-dependent smoothing penalty `||grad phi||^2` (line 958). The Theory records that a scalar gauged energy "would further require a base cometric, a base density" (`b02`, lines 29-31). By the rank theorem (verified below), `rank G_i(c) = rank dsigma_i(c) <= dim C`. On the only instantiated base, `C = R^2` (line 434), at most two sector eigenvalues are nonzero, so the hypothesis `|D_obs| = 4` with `|D_obs| << |D_subthresh| << |D_internal|` (lines 2033-2035) cannot be realized there.
**Fix:** Replace line 2042's absolute claim with: "C carries a background density and a fiducial chart metric used for integration and sector thresholds; the metrics that represent perceived geometry are the induced pullbacks." State in the sector section that the hierarchy requires `dim C >= 4` (and much larger for the stated hierarchy) and is not realizable on the working base.
**Falsifies:** A reformulation in which the functional, the sectors, and the smoothing term use only induced structures, for example the density of `G_i` itself, which is degenerate where `dsigma_i` has a kernel.
**Status:** S. The "no view from nowhere" statement is interpretive and inflated relative to the construction.

### L02-6: Line 1472 reintroduces a reciprocity condition for block symmetry that lines 1439 and 1532 correctly deny, and names an impossible case
**Location:** PIFB2.tex:1472 (after `eq:mass_sigma_offdiagonal`), compared with 1439 and 1532.
**Severity:** low
**Evidence:** Line 1472 reads "when `beta_ik != beta_ki` or `Omega_ik != (Omega_ki)^{-1}`, the off-diagonal block is non-symmetric and the inertia-tensor reading is recovered only in the reciprocal limit". Lines 1439 and 1532 state that the block-transpose identity holds for any `beta` by Schwarz symmetry, and that "reciprocity is not what makes it symmetric". My finite-difference check uses `beta_12 = 0.7` and `beta_21 = 0.4`. It reproduces the boxed off-diagonal blocks (below), and the resulting Hessian is block-transpose symmetric. Under the cocycle `Omega_ki = Omega_ik^{-1}` identically, so the second clause never occurs in Regime I.
**Fix:** Delete the sentence, or replace it with: "The individual block `[M_SS]_ik` need not be symmetric; the assembled Hessian satisfies `[M]_ik = [M]_ki^T` for all `beta`."
**Falsifies:** A reading of "non-symmetric" that refers to something other than the Schwarz identity. No such reading is stated.
**Status:** D. Internal inconsistency, not status inflation.

### L02-7: The R2 example's reading ("confident regions appear larger") needs a spatially varying sigma, which adds a term
**Location:** PIFB2.tex:1888-1890.
**Severity:** low
**Evidence:** The reduction `G = sigma^{-2} dmu.dmu` holds for constant sigma, and I verified it to 9.2e-16. "Confident regions appear larger and uncertain regions smaller" presupposes a varying `sigma(c)`, and then `Sigma = sigma^2 I` contributes `(1/2) tr(Sigma^{-1} dSigma Sigma^{-1} dSigma) = 2 K_q (dsigma x dsigma)/sigma^2`. The correct statement is `G = sigma^{-2}(dmu.dmu + 2 K_q dsigma x dsigma)`. With constant sigma the rescaling is global, and no region is larger than another.
**Fix:** Write the variable-sigma form, and say that `sigma^{-2}` acts as a conformal factor on the mean term plus an extra uncertainty-gradient term.
**Falsifies:** Nothing in the constant case; the finding concerns only the interpretive sentence.
**Status:** P for the formula; the interpretive sentence is S.

### L02-8: The "operational" observable-sector pencil is under-specified and generically singular
**Location:** PIFB2.tex:2033 (definition via `G_i v = lambda J^{(o)} v`).
**Severity:** low
**Evidence:** `J^{(o)}` is "the pullback along the section of the Fisher information of the likelihood `p(o|x)`". That Fisher information is a metric on the latent x-space, not on the belief fiber, so a map from C to x-space must be declared. The natural choice through `mu_i(c)` gives, for the Gaussian likelihood of line 1333, `J^{(o)} = dmu^T Lambda_o dmu`. This form is blind to covariance variation and is degenerate wherever `dmu_i` has a kernel, while `G_i` generally is not. The pencil then has infinite generalized eigenvalues, so "lambda of order one" does not define a subspace. This is an analytic observation; I did not script it.
**Fix:** Declare the map (for example `mu_i`), require `J^{(o)} > 0` on `T_cC`, or define the sectors on `ker J^{(o)}` and its complement separately.
**Falsifies:** A construction in which `J^{(o)}` is the pullback of a fiber-level tensor that is positive definite on `im dsigma_i`.
**Status:** The text calls it "a definition, not a new postulate". It is an incomplete definition.

### L02-9: Absolute value is not an admissible positive map for the Cholesky diagonal
**Location:** PIFB2.tex:2660.
**Severity:** low
**Evidence:** Line 2660 says "reparameterizing the diagonal through a positive map (softplus or absolute value) so that ... the realized diagonal entries cannot cross zero", and later "the map `L -> LL^T` is a diffeomorphism onto the SPD cone, so ... share stationary points". Softplus is a diffeomorphism from R onto the positive half-line, so both claims hold for it. The absolute value vanishes at 0, so `Sigma` can become singular. It is not differentiable at 0, and it is two-to-one, so the stored-parameter-to-SPD map is not a diffeomorphism. Stationary points of the parameter objective then include `Sigma` on the boundary, and duplicate interior points.
**Fix:** Drop "or absolute value", or state that the stationarity equivalence holds only for a diffeomorphic positive map such as softplus or exp.
**Falsifies:** A demonstration that the implementation never reaches zero there, which would still leave the diffeomorphism claim false.
**Status:** D, a minor misstatement.

### L02-10: Bookkeeping slips in the SPD gauge-covariance paragraph and the kinetic form
**Location:** PIFB2.tex:2328, 1523.
**Severity:** low
**Evidence:** (1) Line 2328 says the covector and vector laws "coincide if and only if g is orthogonal, ... the compact restriction `g in SO(K_q)`". The correct group is O(K_q). (2) The same paragraph attributes the "bilinear form `Sigma(.)Sigma`" to the metric `g(U,V) = tr(Sigma^{-1} U Sigma^{-1} V)` while using `2 Sigma(.)Sigma`. `L02_retraction.py` (8) confirms that `2 Sigma grad Sigma` is the Riemannian gradient for the Fisher normalization `(1/2) tr(...)` (residual -1.9e-9) and `Sigma grad Sigma` for `tr(...)` (residual -1.9e-9), and that mixing the two leaves an O(1) error (-0.67 against 1.345). The two statements in the paragraph are individually right but paired with different normalizations. (3) At line 1523, `(1/2) tr[M_SS[Sigma_dot, Sigma_dot]]` takes the trace of a scalar.
**Fix:** Change SO to O. Say "`2 Sigma(.)Sigma` is the gradient for the Fisher member `a = 1/2, b = 0`". Write `(1/2) M_SS[Sigma_dot, Sigma_dot]`.
**Falsifies:** None needed; these are typographical-level corrections.
**Status:** P content, sloppy notation.

## Verified, no defect (ledger candidates)

Each item gives the location, the method, the residual against its baseline, and the script.

- **Fisher metric and the 1/2 covariance factor** (lines 167-186, 945, 2621-2635). The KL second-order jet at a random K=2 point satisfies `KL(theta||theta+hv)/h^2 -> (1/2) g(v,v)`, with relative error 1.95e-3 at h=1e-3, decreasing linearly with h, which is the expected O(h) term. With factor 1 on the covariance block the error is 0.277. The operator inverse `2 Sigma X Sigma` is correct, and the vech remark is correct. `L02_fisher_curvature.py` (a), `L02_retraction.py` (8).
- **Gaussian Fisher curvature** (lines 429, 462). The full Riemann tensor was computed symbolically.
  - K=1: curvature -0.5, exactly.
  - K=2, pure-mean plane: +0.25 at `Sigma = I` and also at a non-identity `Sigma` (homogeneity), matching line 429's "+1/4". The same value follows from the Gauss equation with second fundamental form `II(e_a, e_b) = -(1/2)(E_ab + E_ba)`.
  - K=2, covariance-only planes: maximum over 2000 random planes -7.6e-9 at `Sigma = I` and -1.7e-7 at the second point (0 up to rounding), consistent with the totally geodesic, nonpositively curved SPD slice.
  - Random planes range over [-0.914, +0.260], so the curvature is of mixed sign for `K_q >= 2`.
  - The "location-scale with fixed correlation" family has intrinsic metric `(dmu^T R^{-1} dmu + 2K dsigma^2)/sigma^2`, which is hyperbolic with curvature `-1/(2K)` (analytic).
  - The Skovgaard attribution is consistent with Nielsen 2023. Note that +1/4 is not the supremum: mixed planes reach about 0.26. The text does not claim a supremum.
  - Script: `L02_fisher_curvature.py` (b, c).
- **Congruence isometry of the fiber metric and associated-bundle isometry** (lines 229, 468-504). A constant `g in GL(3)` leaves the pullback metric unchanged (relative 5.6e-12). The AIRM distance is congruence-invariant (relative 6.1e-16). Scripts: `L02_pullback.py` (c), `L02_retraction.py` (7).
- **R2 Gaussian pullback formula** (line 1888). The closed form agrees with the independently computed KL-jet Hessian along the section to relative 7.3e-8. The eigenvalues are positive (5.74 and 29.74) for a full-rank section. `L02_pullback.py` (a).
- **Degeneracy and rank of the pullback** (lines 1890, 2033-2037). For a section factoring through `x + y`, the eigenvalues are {-1.8e-15, 34.8} and `G(1,-1) = 1.3e-10`, so `rank G = rank dsigma`, the kernel equals `ker dsigma`, and G is PSD. This matches the Theory's `thm:pb-pullback-rank-quotient`. The isotropic constant case agrees to 9.2e-16. The arithmetic `dim B = 768*771/2 = 296,064` is correct. `L02_pullback.py` (b).
- **Fisher pullbacks cannot be indefinite** (line 1896). They are expectations of squared scores; every eigenvalue computed was nonnegative up to rounding. The indefinite form enters only through the trace block (lines 1900 and 1904 say so correctly). On `gl(K,R)`, the trace form is negative definite on `so(K)` and positive definite on the symmetric complement (analytic, and consistent with the ledger). The PD route is ruled out cleanly for the Fisher block alone. See L02-2 for the combined tensor.
- **SPD exponential retraction** (lines 2330-2349). All checks in `L02_retraction.py` (1-6):
  - Positive definiteness for large steps: `lambda_min` is 1.76, 0.355, and 1.38 at t = 1, 10, 50, while the additive step reaches -49.1.
  - `R_S(0) = S` to 2.1e-15, and `dR_S(0) = id` to 7.0e-10 (central finite difference).
  - The eigendecomposition form equals the square-root form to 3.1e-16.
  - Congruence equivariance holds to 1.5e-15.
  - Geodesic property: `d(S, R_S(tD)) / (t ||D||_S) = 1.000000000000` for t = 0.3, 1, 3.
  - Log round trip to 1.8e-14 (cond(S) = 30, eps = 2.2e-16).
  - It is the Riemannian exponential map, a valid first-order (indeed exact-geodesic) retraction, as claimed.
- **Covector versus vector transformation laws and the GL-invariant metric family** (lines 2322-2328). `g^{-T}(grad S)g^{-1}` and `g(2 Sigma grad S Sigma)g^T` hold (analytic). The family `a tr(S^{-1}U S^{-1}V) + b tr(S^{-1}U) tr(S^{-1}V)` with `a > 0`, `a + Kb > 0` is congruence-invariant and positive definite (analytic: `tr(S^{-1}U)` is invariant, and the value on `U = S` is `K(a + Kb)`). The citation locator in Pennec 2006 was not checked.
- **BCH first correction** (line 2651). `log(e^X e^{-Y}) = X - Y - (1/2)[X,Y] + O(3)`. The residuals after the correction are 2.8e-3, 7.3e-5, and 7.2e-6 at `|phi|` of 0.1, 0.03, and 0.01, cubic scaling as expected. `L02_retraction.py` (9).
- **Frame pullback metric and dexp regularity** (lines 984-999). The trace formula follows from `Dexp_phi[H] = Psi_R(ad_phi)(H) e^phi` (analytic). `G_pull` is positive definite away from the `2 pi i Z` locus: minimum eigenvalue 0.708 at theta = 1 and -8.4e-17 at theta = 2 pi for `phi = theta J`, in agreement with `prop:dexp_regularity`. Line 1004's telescoping `xi = U^{-1} grad_U F` holds when the generator basis spans `gl(K)`; for a subalgebra, `Dexp[v]` is the orthogonal projection of `grad_U F`, a qualifier the text does not state. `L02_retraction.py` (11).
- **Hessian blocks** (lines 1417-1495). Two agents, K=2, general GL(2) transports, `beta_12 = 0.7`, `beta_21 = 0.4`, reciprocal consensus, arbitrary priors and sensory terms. `L02_hessian_blocks.py`:
  - `[M_mumu]_11`: relative error 5.2e-7.
  - `[M_mumu]_12` (`-beta_ik Omega^{-T} Lambda_k - beta_ki Lambda_i Omega_ki^{-1}`): 1.6e-6.
  - `[M_SS]_11` at consensus, `(1/2)(1+sum beta)(Lambda x Lambda)`: 4.6e-6.
  - `[M_SS]_12`, including the transposed sender Kronecker factor in the vec convention: 2.5e-6.
  - The cross block `C^{mu Sigma}` at consensus is 0 (exact in finite differences).
  - The GL-valid identity `Omega_ji^T tilde Lambda_i^{(j)} Omega_ji = Lambda_i` is confirmed through the diagonal block.
- **alpha* rank-one thresholds** (line 1512). Along `Delta mu`, the log-barrier curvature `c_0 log(b_0 + D)` reaches 0 exactly at `D = b_0`. For `c_0 D/(b_0 + D)` it reaches 0 at `D = b_0/3`. Both match the text. `L02_hessian_blocks.py`.

## Physics-audience and standalone notes

A physics referee will want the base manifold's status stated once, in operational terms, before any metric is pulled back to it: C is a smooth n-manifold of labels, carrying a declared density and a fiducial chart metric used only for integration, boundary conditions, and thresholds, and no metric that represents perceived geometry. The Kant and Whitehead paragraph at lines 146-153 can stay, but it should follow this sentence, not replace it (see L02-5).

The induced tensors have units of nats per (coordinate unit) squared. To read `G_i` as a candidate spatial metric with ds^2 in length squared, the paper needs a conversion scale `ell^2` per nat. Register entry P7 declines to supply one ("nats are the fundamental units"), which is a coherent position, but then "metric" should be said to mean an information metric, and the Lorentzian propositions should not be described as producing "spacetime" intervals.

The horizontal block has a clean description a physicist will recognize: `tr(A_mu A_nu) = U^*(tr(XY))` is the pullback, along the frame map `U: C -> GL(K)`, of the bi-invariant pseudo-Riemannian metric defined by the Ad-invariant trace form. Saying this once would replace several paragraphs at lines 1872, 1900, and 1904, and it immediately shows why the result is invariant under constant left and right translations but not local ones.

The four-curvatures paragraph (line 429) mixes the Riemannian curvature of the fiber (correct and verified), the noncommutativity of G (not a curvature), the vanishing field strength (correct), and an unspecified base curvature. For a physics venue it should be reduced to the fiber-curvature statement plus a one-line pointer to Regime I flatness (see L02-4).

The mass section (lines 1325-1532) is long for a physics journal. The Hessian blocks are correct (verified), but the O(d)-versus-GL(d) asides are repeated four times and could be condensed into one remark after `eq:precision_transport`.

## Complementarity notes

- **Covariant pullback and its gauge invariance.** PIFB2 should cite `Theory/b02_base_direction_geometry.tex`, `def:pb-informational-pullbacks` and `thm:pb-pullback-gauge-invariance`, at line 1874 and in the consensus-metric section. This resolves L02-1 on the PIFB2 side with no Theory change. The Theory's `prop:pb-pullback-connection-change` gives the exact dependence on the chosen connection, which is what replaces the "frame-dependent" language of line 194.
- **Rank and degeneracy.** Line 1890's full-rank caveat, and the sector statements, should cite `thm:pb-pullback-rank-quotient` (`b02`, `eq:pb-pullback-radical-rank`).
- **Weighting of joint tensors.** L02-2's `kappa` has an exact Theory analog in `hyp:pb-weighted-product-geometry` and `prop:pb-product-radical`, which cover the Fisher-Fisher case. The trace-plus-Fisher case is PIFB2-specific, and the Theory does not treat it. Whether to add it there would be an author decision; PIFB2 can simply declare `kappa`.
- **Fiber metric.** Line 945 and Appendix C can cite `Theory/g05_fisher_geometry.tex`, `prop:ig-fisher-moment-chart` (the same block form, proved with the affine isometry), in place of restating it.
- **Scope gate.** The fix in L02-1 uses only PIFB2's existing Regime-I connection `U^{-1}dU`; no new base-transport construction is needed. The connection-relative development belongs to Theory Supplement B and is deferred there.

## Not covered

- Karcher and BCH frame averaging (lines 1533-1661), including the frame-barycenter uniqueness claims. This is outside the assigned scope, and the relevant trap (GL+(K) inherits no SPD uniqueness) was not checked here.
- Appendix D, covariance dynamics (lines 2662-2891), apart from the retraction.
- I did not read Skovgaard 1984 in full text. The positive-curvature attribution rests on Nielsen 2023 plus my computation, and I have no page locator.
- I did not verify the Pennec 2006 or Bhatia 2007 locators for the two-parameter invariant family.
- The Lorentzian postulate register and GL(2,C) example (lines 1894-2014) were read for the PD-versus-indefinite question only. The complex-route algebra was not re-derived; it belongs to the gauge lens and is covered by the ledger on trace forms.
