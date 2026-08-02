# Settled ground for the 2026-08-02 gauge_vfe_rg deep review

Every item below has already been verified or adjudicated by a prior pass. **Do not re-raise
any of it as a finding** unless the manuscript text touching it has changed since the recorded
revision, in which case say so explicitly and give the diff.

Sources: `.verification/ledger.json` (rev 593dc990), `.verification/pass2-ledger.json`
(rev f568b7b1), `.verification/local-global-rg-ledger.json` (rev e4377537),
`.verification/pullback-geometry-ledger.json` (rev 43eb7e74), and
`manuscripts/gauge_vfe_rg/appendix_claim_ledger.tex`.

## Verified — pass 1 (`ledger.json`)

- **R01** At `A=0` the proposed fixed ray is a singular PSD operator ray, not a normalized
  Gaussian/ELBO law on the declared full Lebesgue space.
- **R02** With the declared right action and quotient convention (`u_i = sigma_0 U_i`), the
  j-to-i associated-fiber transition is `U_i^{-1} U_j`, **not** `U_i U_j^{-1}`.
- **R03** At the `A=0` ray the pencil `(L, Lambda) = (L, L)` is singular; `det(L - d Lambda)` is
  identically zero, and after quotienting the regular spectrum is all one.
- **R04** A finite generalized spectrum is atomic and cannot carry an ordinary low-`d` spectral
  density or exponent without a declared thermodynamic limiting measure.
- **R05** The sum-only coupling map is not primitive on the full product PSD cone for `K > 1`
  because it preserves proper common-range faces.
- **R06** The projection characterization is factor-local and incompatible with nonidentity
  invertible gains; the assembled global interaction family can contain nonprojection gains
  through cancellation.
- **R07** The unrestricted matrix-weighted interaction family is not closed under Kron
  reduction (exact SPD three-node `K=2` counterexample).
- **R08** The selected-observation pointwise posterior and ELBO depend on the chosen density or
  conditional version on observation-null slices.
- **R09** The cyclic no-go is valid for the flat unanchored reciprocal pair, not for all
  anchored globally normalized cyclic Gaussian models.
- **R10** Component preservation alone does not prove attraction, uniqueness of a reached fixed
  point, scheme independence, or absence of observable-class variation.
- **R11** Open 2.32 has a counterexample: unequal local frame-induced connections can give zero
  curvature for every subordinate partition on a one-dimensional abelian base.
- **R12** The displayed exact Gaussian-star coordinate iteration is a strict linear contraction,
  hence has a unique fixed mean.
- **R13** Support on a proper closed subset of posterior support does not by itself imply
  failure of absolute continuity or infinite reverse KL.
- **R14** For the displayed scalar normalizer contribution, identity is a strict local maximum;
  the manuscript's claimed isolated force direction is reversed.
- **R16** A pointwise graph coboundary at one common context does not supply the smooth Cech
  zero-cochain on all overlaps needed to infer global bundle triviality.
- **R17** Proposition 2.31 constructs an averaged connection and gives a sufficient flatness
  condition, but does not prove nontrivial curvature or holonomy.
- **R18** The artifact did not satisfy its own epistemic-status / numerical-reproducibility
  contract; five status registers were clipped in the compiled PDF. (Re-check only whether the
  *current* build still clips; do not re-derive the finding.)
- **R19** Proposition 5.2's prose reverses the named free-energy comparison though its displayed
  total-correlation proof has the correct sign.
- **R20** Proposition 3.9's density criterion is applied to a subspace-supported law outside its
  common-domination hypotheses.
- **R21** Nonconstant dependence of a joint `P_Q` on `Q` does not force the observation evidence
  to vary, nor entail Proposition 4.5's stated ELBO consequences.
- **R15** `INCONCLUSIVE` — whether the fixed-point interpretation can be validated as a
  falsifiable physical law. Open, not a defect.

## Verified — pass 2 (`pass2-ledger.json`)

- **FINAL-01** One common principal `G`-bundle induces belief and model associated bundles
  through possibly inequivalent representations, with correctly typed separate local frames and
  connections, opposite-direction cross-bundle morphisms, relative-frame data, and induced
  parallel transports. This construction is settled.
- **FINAL-02** The general renormalization theory is a typed changing-space categorical cocycle
  with one common principal bundle and two associated statistical bundles per level,
  representation-compatible scale maps, and cross-scale defects; it precedes rather than depends
  on the multivariate-Gaussian realization.
- **FINAL-03** The BKS discussion correctly limits Bayesian renormalization to its regular
  asymptotic information-geometric setting and claims no unproved opposite-flow theorem.
- **FINAL-04** The network-RG, graph-ML, connection/sheaf, Wishart, and matrix-Gamma references
  are represented only for the guarantees their primary sources supply.
- **FINAL-05 / FINAL-06** The verification suite recorded 29 passing checks and the build was
  clean. (Re-run rather than re-derive if you need current status.)
- **FINAL-07** `INCONCLUSIVE` — the framework is not established as a physical law for a
  specified empirical system. Open, not a defect.
- **FINAL-08** **REFUTED** — two independent principal bundles are *not* mathematically required
  to represent separate belief and model frames over one base with one group `G`. Do not argue
  that the single-bundle construction is an error.

## Verified — local/collective ELBO and agent-network RG (`local-global-rg-ledger.json`)

- **LG-1** For every finite standard-Borel agent hypergraph meeting the displayed normalization
  and positive-evidence hypotheses, the fixed interaction joint has an exact collective ELBO,
  and every agent or block has an exact conditional ELBO whose unilateral differences equal the
  collective VFE differences.
- **LG-2** Every standard-Borel observation kernel has an equivalent environment-node message
  realization; the normalized latent-source attention joint yields the stated categorical
  KL-energy ELBO sector without inserting a live recognition law into the generative target.
- **RG-1** Pushing the reference law and evidence-weighted submeasure through one common Markov
  coarse channel gives an exact coarse VFE identity, regular fine-meta bridge kernels, and exact
  finite-network closure when the effective state admits generated hyperedges.
- **RG-2** Under the displayed equivariance, integrability, positivity,
  lumpability-or-path-space, and semigroup hypotheses, the construction supplies composable
  gauge-covariant cross-scale operators, exact meta-attention, reference-dependent action and
  attention beta functions, and exhaustive invariant measures.

## Verified — pullback geometry and timeless inference (`pullback-geometry-ledger.json`)

- **PB-1** Under the displayed regular statistical-model, represented-`G`-invariance, section,
  and chosen-connection hypotheses, the covariant vertical first jet induces global
  passive-gauge-invariant but connection-relative Fisher and Amari tensors on the base, with the
  stated rank, radical, and vector-bundle quotient structure.
- **PB-2** A law history over one fixed base point is intrinsically vertical and a section
  history is pointwise vertical; under the displayed joint-law lift, support, regular-metric,
  and differentiability hypotheses, VFE selects an oriented unparameterized natural-gradient
  orbit and Fisher arclength supplies reparameterization-invariant duration.
- **PB-3** Under the displayed related-section, horizontal-compatibility, and normalized
  parameter-independent Markov hypotheses, fine and meta covariant first jets obey the exact
  naturality-or-mismatch formula, and perceived Fisher geometry contracts with a
  positive-semidefinite conditional-covariance defect.
- **PB-4** The integrated artifact built to a 215-page PDF with no unresolved references,
  citations, duplicate labels, or fatal errors.

## Declared-open obligations — `appendix_claim_ledger.tex`

The manuscript already carries its own open-obligation ledger and tags claims with
`\status{...}`. **An obligation the manuscript itself declares OPEN or CONJECTURE is not a
finding.** Reporting "the continuum limit is unproved" or "physical-time identification is
unproved" when the appendix already says so is noise. These are declared open and out of scope:

continuum law theory; regular frame-coordinate quotient; optimization/projection convergence;
joint-law lift; global relational information clock; partition selection and experiment-level
recovery; infinite-volume RG limit; two-index limits and universality; the Bayesian-RG bridge;
fine-coarse history semiconjugacy; scalarized attraction (conjecture); admissible cone
classification; nonflat-link compression; intrinsic scale selection; information-geometric
transfer; stochastic inverse RG; update robustness; operational base holonomy (conjecture);
graph-to-base identification; canonical nondegenerate pullback geometry; physical-time
identification; physical-law identification.

**What IS in scope:** a claim tagged `\status{ESTABLISHED}` or stated as a theorem/proposition
whose proof is wrong, circular, incomplete, or whose hypotheses do not support the stated
conclusion; a definition used before it is given; a symbol that is never defined; an internal
inconsistency between chapters; a citation that does not support the sentence citing it; and
status inflation, where prose asserts more than the tagged status licenses.

## Carried-over candidate findings from the interrupted 2026-08-02 session

These three were logged as confirmed before the session died. Treat them as **unverified
candidates**, not established. My own re-read suggests at least two are weaker than reported.
Adjudicate them on the current text.

1. **`\mathcal L^{\rm ext}` undefined** — `06_general_coarsegraining.tex:209,213` use
   `\bar{\mathcal L}^{\rm ext}` and `\mathcal L^{\rm ext}` inside
   `eq:cg-elbo-monotone`. A whole-manuscript grep finds no other occurrence of the symbol and no
   definition. Determine whether "extended ELBO" is defined anywhere (possibly under another
   glyph in `05_elbo.tex` or `03_probability.tex`); if it is defined elsewhere, this is a missing
   cross-reference, and if it is not, it is an undefined load-bearing symbol.
2. **Per-agent VFE decomposition / total-correlation factorization** —
   `05b_local_collective_elbo.tex:292-315`. The prior session claimed a missing factorization
   hypothesis. Note that the text *does* condition on `P_0 = \bigotimes_i \rho_i`, defines
   `TC(Q)` at `eq:obs-total-correlation`, and states the ledger `eq:obs-global-ledger`. Verify
   the chain-rule identity `KL(Q || ⊗ρ_i) = TC(Q) + Σ_i KL(Q_i || ρ_i)` and check whether the
   `Q_i` are the marginals of `Q` throughout. Report only a real gap.
3. **`R_b, R_m` transformation direction** — `02_geometry.tex:361-365`,
   `eq:geo-defect-gauge-laws`. Introduced as "the represented coordinate changes" with no stated
   direction. Note that `eq:geo-local-reframing` (02:154-158) changes coordinates by
   `\widehat\rho(a_i)^{-1}`, whereas `04_generative.tex:280-285` fixes `k' = R^b k` with
   `R = \rho_b(g)` and section rechoice `u' = u (g)^{-1}` — which is self-consistent. Decide
   whether `eq:geo-defect-gauge-laws` is actually wrong under any reading, or whether this is a
   local expository ambiguity resolved only in a later chapter. The prior session also asserted
   that Chapter 7b uses the opposite convention; note that `07b` uses `\mathcal R_b` for the
   **block-`b` renormalization operator**, a different symbol from `R_b`, so check whether that
   claim was a symbol confusion — and if so, whether the `R_b` / `\mathcal R_b` collision is
   itself worth a notation finding.
