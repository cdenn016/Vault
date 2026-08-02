# Lens review — information geometry

**Scope.** `08_infogeometry.tex`, `05d_relational_inference.tex`, with `05c_pullback_geometry.tex`
consulted for the Fisher/Amari tensor construction. Settled ground (`00-settled-ground.md`,
incl. PB-1/PB-2/PB-3, R01–R21, FINAL-01–08) and every obligation the manuscript's own
`appendix_claim_ledger.tex` declares OPEN or CONJECTURE are treated as out of scope.

**Method.** Every load-bearing identity in both chapters was recomputed independently — exact
symbolic (sympy, rational and free-symbol) plus deterministic numerics
(`C:/Python314/python.exe`, numpy/scipy/mpmath). Scripts live in the session scratchpad
(`ig1.py`–`ig5.py`). Residuals are reported for each. The manuscript's own verification suite was
re-run/inspected: `verification/current-results.json` reports `overall_status: PASS`, 29/29 checks,
including `CHK-IG-EXPECTATION-METRIC`, `CHK-IG-PULLBACK-PUSHFORWARD`, `CHK-GENERALIZED-SPECTRUM`.

---

## Verified clean (recomputed, no finding)

These are recorded so the coordinator knows they were tested and survived.

| Claim | Route | Residual |
|---|---|---|
| `eq:ig-lognormalizer`, `eq:ig-natural`, `eq:ig-expectation` — τ = ∇_ηA = (μ, M₂) in the Frobenius-paired symmetric chart | exact rational sympy, n=1,2,3 | **0** (exact) |
| `eq:ig-fisher-hessian`, `eq:ig-dual-inverse` — g_η = Cov(T(Y)), g_τ = g_η⁻¹; blocks of g_η⁻¹ vs `eq:ig-meanblock`/`eq:ig-crossblock`/½Tr(ΛAΛB) | exact rational sympy, n=1,2,3 | **0** (exact) |
| Conjugate potential A\*(τ) = negative differential entropy (08:55) | numeric n=3 | 4.4e-16 |
| `prop:ig-fisher-moment-chart` u᷉ᵀΛv + ½Tr(ΛAΛB) | KL quadratic limit, mpmath dps=50 | O(ε) truncation, rel. err 2.37e-5 → 2.37e-7 as ε: 1e-5 → 1e-7 (clean first-order scaling) |
| `prop:ig-fisher-expectation-chart` all three blocks | (a) free-symbol sympy n=2 (μ free, Λ general symmetric); (b) KL quadratic limit | (a) **exactly 0**; (b) same clean scaling. Negative control (moment-chart Λ used in the expectation chart) mis-predicts by 88% |
| `cor:ig-mean-block-discrepancy` spectrum {1+μᵀΛμ ×(n−1), 1+2μᵀΛμ ×1}, g_[μμ] ⪰ Λ | numeric n=3 | 7.1e-15; min eig(g_[μμ]−Λ) = 41.6 > 0 |
| `prop:ig-pullback-vs-pushforward` Schur identity + Loewner order + Λ-orthogonal equality control | numeric n=6, k=2 | 1.5e-14; equality control (range(B) Λ-invariant) 9.9e-15 |
| `prop:ig-generalized-spectrum-invariance`, localization interval [0,1], difference form | numeric N=4, K=2 | difference-form residual **0**; spectrum ⊂ [0,1] |
| `prop:ig-frame-dependent-spectra-determinants` (i) and (ii) | numeric n=5, k=2 | 8.9e-16 both |
| `thm:hist-fisher-clock-invariance` and `eq:hist-vfe-clock-rate`/`-unit-tangent`/`-dissipation-per-length` | analytic re-derivation | correct |
| `thm:hist-record-clock-contraction` — score projection, conditional-variance defect, integrated contraction | explicit 2-D Gaussian family + parameter-independent Gaussian channel; plus 4e6-sample Monte Carlo | ν_X²−ν_Y² = 0.3368666906 vs E Var(ℓ^X\|Y) = 0.3368666906, **residual 3.9e-16**; MC E[ℓ^Xℓ^Y]=1.20715 vs E[(ℓ^Y)²]=1.20674 (projection); L_F(P^Y)=2.6245 ≤ L_F(P^X)=3.3328 |
| `eq:hist-parameter-dependent-channel-score` + Bernoulli σ(λ) witness | analytic + numeric | fine speed 0, output Fisher σ(1−σ)=0.2403 > 0 |
| `eq:hist-normalized-form-curvature` dα_F = N⁻²dN∧dF and `eq:hist-nonexact-clock-example` (x²−y²)/(x²+y²)^{3/2} | exact sympy | **residual 0** both |
| `prop:hist-scalar-mobility-orbit`, `eq:hist-anisotropic-orbit-change`, `eq:hist-natural-gradient-nongeodesic` | numeric | 3.3e-16 |
| `prop:hist-semidefinite-gradient-obstruction` (G = dx², F = y / F = x) | analytic | correct |
| `eq:hist-finite-length-infinite-parameter` (∫₀^∞ e^{-t}dt = 1) | analytic | correct |
| `thm:hist-global-clock-exactness` (exact ⟺ closed + zero periods; dT/dτ=1; ker dT = U_F^⊥) | analytic | correct |
| `prop:hist-oriented-semiconjugacy` σ_Q(t) = ∫₀ᵗa(Φ_s Q)ds | analytic | correct |
| `prop:pb-kl-divergence-jets` (05c) — mixed 2-jet = Fisher, Γ_𝒟 − Γ\*_𝒟 = E[ℓℓℓ] | exact sympy on the 1-D normal location-scale family, all 8 index triples | Fisher = diag(σ⁻², 2) ✓; **0 mismatches** |
| `sec:cg-gaussian-fixed-relaxation` natural-gradient identification asserted at 08:335–338 and 08:348–350 | checked against **Amari 1998** definition (preconditioning by the inverse Fisher matrix of the family being updated) | Fisher of {N(z,R⁻¹)} in the mean chart z is R (`prop:ig-fisher-moment-chart` mean block); F⁻¹∇E = R⁻¹Lz identical to the flow to **0.000e+00**; dissipation identity dE/dt = −żᵀRż = −zᵀLR⁻¹Lz reproduced to 10 digits. **The ESTABLISHED tag is earned; the terminology matches Amari's definition.** |
| Recognition-vs-model Fisher trap | audited | **not silently violated.** 08 §`sec:ig-typing` types four distinct spaces, tags the transfer `\status{OPEN}` (08:238), and the ledger carries "Information-geometric transfer (open)". 05d keeps `g_b^F` and `g_m^F` typed separately with declared positive weights (`eq:hist-pointwise-clock-speed`, `eq:hist-finite-design-clock-speed`) and `prop:pb-product-radical` correctly refuses a cross tensor. |
| Citations `Cencov1982`, `Le2017`, `Petz1996`, `Amari1998`, `AmariNagaoka2000`, `Brown1986`, `Lauritzen1996`, `HornJohnson2013` | bib + source check | all resolve and support their sentences. Lê 2017's abstract does say "Under the assumption of strong continuity of an information metric we prove the uniqueness of the Fisher metric", matching 08:315. Petz's classification by operator monotone functions is correctly stated. |

Also dropped after adversarial test, and **not** reported:

* The discrepancy scalar μᵀΛμ (08:150) *is* invariant under the declared block reframing group
  `eq:ig-reframing` (μ ↦ Tμ, Λ ↦ T^{-⊤}ΛT^{-1}), so §8.3's own prohibition is not violated. It is
  translation-dependent, but translations are not in the declared group.
* `eq:hist-exact-fisher-lift`'s possible degeneracy in the two-channel (belief + model) setting is
  covered verbatim by the ledger's declared-open **"Joint-law lift"** item ("nondegeneracy of its
  Fisher pullback … must be proved for each declared recognition family"). Out of scope.
* The design clock `eq:hist-finite-design-clock-speed` is not positive definite on the full section
  space — the manuscript says so itself in the same paragraph.

---

## Findings

### F-IG-1 — Campbell 1986 does not extend Chentsov's uniqueness-up-to-scale to non-normalized measures

* **Claim.** "On a finite sample space the Fisher metric is, up to a positive scale, the unique
  Riemannian metric invariant under Markov morphisms; this is Chentsov's theorem \citep{Cencov1982},
  **with the extension to non-normalized measures due to \citet{Campbell1986}**."
* **Location.** `08_infogeometry.tex:315` (§`sec:ig-notclaimed`, first sentence-group).
* **Severity.** medium
* **Status.** `\status{ESTABLISHED}` on the whole clause. Prose inflates: the ESTABLISHED tag is
  attached to a compound sentence whose second half the cited source contradicts.
* **Evidence (primary source, retrieved and text-extracted myself from the AMS PDF,
  Proc. AMS 98(1) 1986, p. 137, §4 "Characterization theorem"):**

  > "**Theorem.** Let ⟨ , ⟩_m be a Riemannian metric on R₊^m for m ∈ {2,3,…}. Let this sequence of
  > metrics have the property that every congruent embedding by a Markov mapping is an isometry.
  > Then
  > (6)  ⟨X_i, X_j⟩_m(x) = A(|x|) + δ_ij |x| B(|x|)/x_i,
  > where |x| = Σ x_i, δ_ij is the Kronecker delta, and **A and B are C^∞ functions on R₊ satisfying
  > B(a) > 0 and A(a) + B(a) > 0 for all a > 0.** Conversely, if A and B are C^∞ functions on R₊
  > satisfying B(a) > 0, A(a)+B(a) > 0, then (6) defines a sequence of Riemannian metrics under which
  > every congruent embedding by a Markov mapping is an isometry."

  Campbell's abstract likewise frames the paper as extending the *characterization* to the cone, not
  the uniqueness: "In Čencov's theorem, the underlying differentiable manifold is the probability
  simplex Σxᵢ = 1, xᵢ > 0. … In the present paper Čencov's result is extended to the positive cone."

  So on the cone of non-normalized measures the invariant metrics are a **two-arbitrary-function
  family**, not a one-parameter scaling of the Fisher metric. Uniqueness up to a positive scale is
  recovered only on the simplex, where |x| = 1 and Σvᵢ = 0 kill the A-term and freeze B(1) to a
  constant.

  Independently corroborated by a source the manuscript itself cites, `Ay2015`
  (Ay–Jost–Lê–Schwachhöfer, PTRF 162, arXiv:1207.6736), Main Theorem 2.10(2): for a *local
  statistical continuous quadratic form field* invariant under sufficient statistics on
  non-normalized measures, "there are continuous functions f, d : ℝ → ℝ such that
  F(x) = f(∫_Ω dp(x)) g^F(x) + d(∫_Ω dp(x)) A(x)²" — again two free functions of the total mass.

* **Fix.** Replace the clause with, e.g.: "…this is Chentsov's theorem \citep{Cencov1982}. On the
  cone of non-normalized measures the invariant metrics form a strictly larger family,
  ⟨X_i,X_j⟩ = A(|x|) + δ_ij|x|B(|x|)/x_i with A, B free functions of the total mass
  \citep{Campbell1986}, so uniqueness up to a positive scale is a property of the normalized
  simplex, not of the cone."
* **Falsifies.** Nothing in the manuscript's own mathematics. It falsifies only the ESTABLISHED
  status of the sentence as written. **Directionally this error works against the manuscript's own
  thesis**: §`sec:ig-notclaimed` exists to argue that the classical uniqueness results are *too weak*
  to force the Fisher choice, and the misstatement makes them look stronger. Correcting it
  strengthens the section.

---

### F-IG-2 — "It is false in the expectation chart" is stronger than §8.2's own concession; the orthogonal-quotient mean sector in that chart is *exactly* Λ

* **Claim.** "It is often asserted that the mean sector of the Fisher metric of a Gaussian family
  *is* the precision. The assertion is true … in the moment chart. **It is false in the expectation
  chart**, which is the chart the exponential-family duality of Section~\ref{sec:ig-expfam} actually
  delivers." And: "The discrepancy … is unbounded. It is not a normalization constant and it does not
  disappear in any limit that keeps the mean away from the origin."
* **Location.** `08_infogeometry.tex:76` and `08_infogeometry.tex:150`; in tension with the chapter's
  own `08_infogeometry.tex:154`.
* **Severity.** medium
* **Status.** The headline paragraph carries no tag; the "chart discipline" box at `08:157` is
  `\status{ESTABLISHED}` and is correct as stated (it compares *restriction* mean blocks). The
  inflation is in the framing at :76 / :150.
* **Evidence (my recomputation).** "The mean sector" of a metric admits exactly two invariant
  readings — restriction to the mean coordinate directions, and the metric induced on the quotient
  by the second-moment directions (equivalently, the restriction to their metric-orthogonal
  complement). The chapter itself says so at :154 and concludes "Absent a declared splitting, 'the
  mean sector' in that chart names no unique object." But it never computes the second reading.
  The second reading is the Schur complement of the expectation-chart metric with respect to the
  M₂ block, and

  ```
  g_[μμ] − g_[μM₂] (g_[M₂M₂])⁻¹ g_[M₂μ]  =  ((g_τ⁻¹)_{μμ})⁻¹  =  (Cov_q(Y))⁻¹  =  Λ    exactly.
  ```

  Numerically (`ig4.py`, CHK K), for random Λ ≻ 0 and random μ:

  | n | ‖Schur(g_τ / M₂-block) − Λ‖_F | ‖g_[μμ] − Λ‖_F (restriction reading) |
  |---|---|---|
  | 2 | 1.34e-15 | 9.2956 |
  | 3 | 2.70e-14 | 118.6016 |
  | 4 | 3.93e-14 | 241.8986 |

  So in the expectation chart the *restriction* mean block is not Λ (correct, and the chapter proves
  it), while the *quotient* mean block is Λ to machine precision. The flat "It is false in the
  expectation chart" therefore asserts more than the chapter's own :154 licenses, and it is false
  under one of the two admissible readings — indeed under the reading that is chart-covariant.
* **Fix.** (i) Soften :76 to "It is false for the restriction reading in the expectation chart, and
  the phrase is ambiguous there." (ii) Add the Schur identity as a corollary to
  `prop:ig-fisher-expectation-chart`: *the metric induced on the quotient by the second-moment
  directions is exactly Λ, because ((g_τ)⁻¹)_{μμ} = (g_η)_{hh} = Cov_q(Y) = Λ⁻¹.* This is a
  one-line proof from `eq:ig-dual-inverse` and it is the single most decision-relevant fact for a
  reader trying to obey the chapter's chart discipline. (iii) Then :150's "unbounded … does not
  disappear" becomes precise: it is the *restriction*-reading discrepancy that is unbounded.
* **Falsifies.** Nothing proved. It falsifies the unqualified framing, and it exposes a material
  omission in a chapter whose stated purpose is to prevent exactly this ambiguity.

---

### F-IG-3 — `prop:ig-generalized-spectrum-localization`'s kernel-dimension clause uses a Laplacian hypothesis it does not state

* **Claim.** "*If in addition L ⪰ 0 and A = Λ − L ⪰ 0, then every generalized eigenvalue of
  \eqref{eq:ig-pencil} lies in [0,1]. The value 0 is attained exactly on ker L, **whose dimension is
  at least K because every configuration constant across agents lies in it**, and the value 1 exactly
  on ker A.*"
* **Location.** `08_infogeometry.tex:283–287` (statement and proof).
* **Severity.** low
* **Status.** `\status{ESTABLISHED}`. The [0,1] localization and both endpoint characterizations are
  correct under the stated hypotheses; only the dim ≥ K clause is under-hypothesized.
* **Evidence.** The proposition's hypotheses are those inherited from
  `prop:ig-generalized-spectrum-invariance` (Λ ≻ 0, L = Lᵀ) plus L ⪰ 0 and A = Λ − L ⪰ 0. Nothing in
  that list forces L to be a matrix-weighted Laplacian. Witness satisfying every stated hypothesis:
  L = diag(1,2,3) ⪰ 0, A = I₃ ⪰ 0, Λ = diag(2,3,4) ≻ 0 — then **dim ker L = 0**, which is < K for
  every K ≥ 1. The proof silently imports the difference form
  xᵀLx = Σ_{i<j}(x_i − x_j)ᵀW_{ij}(x_i − x_j), which is declared only in the surrounding §8.3 prose
  (`08:259`, "where L is the Laplacian part of the interaction precision") and in `08:67–71`.
  I verified the difference form itself holds exactly for the declared family (residual 0.0e+00,
  N=4, K=2) and that dim ker L = K = 2 there.
* **Fix.** Add "and L is the matrix-weighted Laplacian of `eq:cg-interaction-family` with
  W_{ij} = W_{ji} ⪰ 0" to the proposition's hypotheses, or scope the kernel clause: "if in addition
  L is the interaction Laplacian, then dim ker L ≥ K."
* **Falsifies.** The literal universal reading of the proposition. It does not falsify any downstream
  use, because §8.3 always supplies the Laplacian structure.

---

### F-IG-4 — §8.4 invokes `eq:ig-restriction-marginal` for an aggregation operator whose columns are not orthonormal; the displayed Schur identity fails there

* **Claim.** "The theorem does not cover the aggregation operation of the following chapters, because
  by \Cref{prop:ig-pullback-vs-pushforward} the coarse operator is a restriction … **the two differ
  by the positive semidefinite Schur term in \eqref{eq:ig-restriction-marginal}**, and the restriction
  is the larger of the two in the Loewner order."
* **Location.** `08_infogeometry.tex:325–331`, invoking `prop:ig-pullback-vs-pushforward`
  (`08:222–233`, hypothesis "*let B ∈ R^{n×k} have orthonormal columns*") against the aggregation
  operator of `09_coarsegraining.tex:43–53`, where `eq:cg-aggregation-matrix` states explicitly
  **SᵀS = diag(n_I) ⊗ I_K**, i.e. the columns are orthogonal but *not* normalized.
* **Severity.** low
* **Status.** `\status{ESTABLISHED}`. The qualitative conclusion survives; the cited identity does
  not apply verbatim.
* **Evidence (`ig4.py` CHK M, `ig5.py` CHK Q).** With Λ ≻ 0 on R⁶ and S the piecewise-constant
  prolongator for two blocks of three:

  ```
  ‖[SᵀΛS − (SᵀΛ⁻¹S)⁻¹] − (SᵀΛS_⊥)(S_⊥ᵀΛS_⊥)⁻¹(S_⊥ᵀΛS)‖_F  =  31.058     (identity FAILS)
  same quantity with B = S·diag(n_I)^{-1/2}                    =  5.87e-15  (identity holds)
  ```

  The reason is that congruence by the normalizer does not commute with inversion: writing S = BD
  with D = diag(√n_I) ⊗ I_K, the restriction scales as D(BᵀΛB)D while the marginal precision scales
  as D⁻¹(BᵀΛ⁻¹B)⁻¹D⁻¹. The correct general Loewner statement for full-column-rank S is

  ```
  SᵀΛS  ⪰  (SᵀS)(SᵀΛ⁻¹S)⁻¹(SᵀS),
  ```

  verified PSD over 200 random draws (worst min-eigenvalue 0.0137 > 0), which reduces to
  `eq:ig-restriction-marginal` exactly when SᵀS = I. Equivalently, the Markov readout realizing the
  pushforward is the block *average* S⁺ = (SᵀS)⁻¹Sᵀ, not Sᵀ.
* **Fix.** Either restate `prop:ig-pullback-vs-pushforward` for full-column-rank B with the (BᵀB)
  factors carried, or add one sentence at :331 normalizing S to B = S·diag(n_I)^{-1/2} before the
  identity is invoked. §8.3's own `eq:ig-logdet-law` already carries exactly this kind of Jacobian
  bookkeeping, so the omission here is inconsistent with the chapter's stated discipline.
* **Falsifies.** The literal citation of `eq:ig-restriction-marginal` at :330. It does **not**
  falsify the section's conclusion (the coarse operator is a mean-submodel restriction, not a Markov
  pushforward, and the restriction is Loewner-larger), which I verified holds for the unnormalized S
  as well.

---

### F-IG-5 — `G^F_{\mathfrak R_B}` is used but never defined; the Fisher metric of a family of *conditional* kernels needs a named mixing law

* **Claim.** "If \(\mathsf G_i^F\) is called the exact recognition Fisher metric, also require
  \(\mathsf G_i^F = \iota_i^{*}G_{\mathfrak R_B}^F\) on a nondegenerate tier…"
* **Location.** `05d_relational_inference.tex:260–264` (`eq:hist-exact-fisher-lift`);
  `appendix_notation.tex:116`. A whole-manuscript grep finds `G_{\mathfrak R_B}^F` at exactly these
  two places and nowhere else, with no defining equation.
* **Severity.** low
* **Status.** `\status{HYPOTHESIS}` — so this is a definition gap, not status inflation.
* **Evidence.** `\mathfrak R_B` is declared as "a manifold of admissible **conditional** recognition
  kernels" \(r_B(\cdot\mid b)\). The Fisher metric of a parametrized measure model is defined on a
  *fixed* sample space (Amari & Nagaoka 2000 §2.1; Ay–Jost–Lê–Schwachhöfer 2017 Ch. 3). For a family
  of kernels indexed by the conditioning variable there is no Fisher metric until a law over b is
  named; different mixing laws give different metrics and different radicals. The manuscript's own
  05c `hyp:pb-regular-models` is scrupulous about exactly this (it demands a finite-dimensional
  parametrized-measure model on one sample space).
* **Fix.** One line. The canonical choice is forced by the surrounding hypotheses and should simply
  be written down: since \(Q_{B^c}\) is fixed and \(Q_i\)-independent, the Fisher metric of the joint
  \(Q_{B^c}(db)\,r_B^{Q_i}(dy_B\mid b)\) is exactly
  \(G^F_{\mathfrak R_B}(u,v) = \E_{Q_{B^c}}\bigl[\E_{r_B(\cdot\mid b)}[\ell_u\ell_v]\bigr]\),
  because the outside factor contributes no score. Stating this also makes
  `eq:hist-exact-fisher-lift` checkable rather than nominal.
* **Falsifies.** Nothing proved. It leaves `eq:hist-exact-fisher-lift` — the hypothesis the
  ledger's "Joint-law lift (open)" item is supposed to be *about* — without a determinate right-hand
  side, which weakens that open obligation's own statement.

---

### F-IG-6 — 08's model-space typing sentence omits the input law that the conditional Fisher metric depends on

* **Claim.** "The model parameter space is where θ lives, indexing the generative kernel; **the
  Fisher metric of the likelihood θ ↦ p_θ(o \given X) is a Riemannian metric on that**, and its
  dimension is the dimension of θ."
* **Location.** `08_infogeometry.tex:177–181`.
* **Severity.** low
* **Status.** `\status{ESTABLISHED}`.
* **Evidence.** For a *conditional* model p_θ(o | x) there is no single Fisher metric: the
  information matrix is I_r(θ) = E_{X∼r}[ E_{p_θ(·|X)}[∂_θ log p ∂_θ log pᵀ] ], and it depends on the
  input law r — different r give different metrics and can give different ranks. (This is the
  ordinary conditional-Fisher / averaged-Fisher object; Amari 1998 §3 uses exactly this averaging
  when defining the natural gradient for a conditional network model.) The dimension claim is
  correct regardless.
* **Fix.** "…the Fisher metric of the likelihood θ ↦ p_θ(o | X), averaged over a declared input law
  for X, is a Riemannian metric on that…"
* **Falsifies.** Nothing. But it is consequential for the manuscript's own `\status{OPEN}` item at
  `08:238`, which asks for "a check that the resulting parameter-space metric is nondegenerate" —
  nondegeneracy is a property of the pair (θ-parameterization, input law), so the open obligation
  cannot be discharged until the input law is part of the declaration.

---

### F-IG-7 (minor) — factor of two in the KL / mean-sector-Fisher identification

* **Claim.** "…their pairwise KL is **exactly the associated mean-sector Fisher quadratic**; summing
  over edges gives the connection Laplacian form."
* **Location.** `08_infogeometry.tex:189–199`, `\status{ESTABLISHED}`.
* **Severity.** low
* **Evidence.** KL(𝒩(μ_i,Σ) ‖ 𝒩(μ_j,Σ)) = **½**(μ_i − μ_j)ᵀΛ(μ_i − μ_j), while the mean-sector
  Fisher quadratic of `eq:ig-moment-metric` is (μ_i − μ_j)ᵀΛ(μ_i − μ_j). Numerically the ratio is
  0.500000 (n=3, random Λ ≻ 0). The manuscript elsewhere carries the ½ explicitly
  (`eq:pb-transported-divergence-expansion`: 𝒟 = (ε²/2)h(γ̇,γ̇); `eq:cg-fixed-covariance-kl`:
  KL = ½(z−w)ᵀR(z−w)), so "exactly" here is inconsistent with its own convention.
* **Fix.** "…is exactly **one half** the associated mean-sector Fisher quadratic," or write the
  quadratic as ½ g(u,u).
* **Falsifies.** Nothing downstream; the connection-Laplacian conclusion is scale-invariant.

---

## Summary table

| ID | Location | Severity | One line |
|---|---|---|---|
| F-IG-1 | `08:315` | medium | Campbell 1986 gives a two-arbitrary-function family on the cone, not uniqueness up to scale; ESTABLISHED clause contradicted by the cited primary source |
| F-IG-2 | `08:76`, `08:150` vs `08:154` | medium | "False in the expectation chart" overstates; the orthogonal-quotient mean sector there is *exactly* Λ (verified to 3.9e-14) and is never computed |
| F-IG-3 | `08:283–287` | low | `prop:ig-generalized-spectrum-localization`'s dim ker L ≥ K uses an unstated Laplacian hypothesis; explicit witness L=diag(1,2,3), A=I |
| F-IG-4 | `08:325–331` | low | `eq:ig-restriction-marginal` invoked for ch. 9's non-orthonormal aggregation S; Schur identity residual 31.06, correct form carries (SᵀS) factors |
| F-IG-5 | `05d:262` | low | `G^F_{\mathfrak R_B}` never defined; conditional-kernel Fisher metric needs the mixing law (canonically Q_{B^c}) |
| F-IG-6 | `08:177–181` | low | conditional model-space Fisher metric depends on an unnamed input law; matters for the OPEN item at `08:238` |
| F-IG-7 | `08:193` | low | KL equals *one half* the mean-sector Fisher quadratic, not the quadratic itself |

Nothing in either chapter's Gaussian information geometry, dual-affine machinery, natural-gradient
identification, Fisher-arclength construction, or Markov contraction theorem was found to be
mathematically wrong. All seven findings are hypothesis-completeness, citation-support, and
framing defects.
