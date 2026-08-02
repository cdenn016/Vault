# Referee report — *Gauge-Covariant Variational Free Energy and Renormalization*

Deep multi-agent peer review, 2026-08-02. Branch `review/gauge-vfe-rg-deep-2026-08-02`.
Artifact: `manuscripts/gauge_vfe_rg/` at `9ea9969`, 215-page build, 24 chapter files.

Nine expert lenses (gauge theory; differential geometry and SPD; information geometry;
variational and ELBO; coarse-graining; renormalization group; measure-theoretic probability and
numerics; philosophy of science and claim status; notation, cross-reference, citation, and build
integrity), followed by seven adversarial skeptics on every finding raised at high or critical.
Prior settled ground was loaded first from four verification ledgers and the manuscript's own
open-obligation appendix; nothing already verified was re-litigated.

## Summary

This is a strong, unusually well-fenced manuscript, and the review did not break it. Across seven
lenses that recomputed rather than trusted, roughly sixty load-bearing identities were re-derived
independently and **every one survived**, most to machine precision. The gauge algebra of
Chapter 2, the pullback geometry of Chapter 5c, the information geometry of Chapter 8, the
coarse-graining exactness claims of Chapters 6 and 9, the ELBO machinery of Chapter 5, and
sixteen renormalization identities in Chapters 7, 7b, and 10 all check out. Three lenses returned
no mathematical error at all. The build is clean at 215 pages with zero dangling references, zero
undefined citations, and zero overfull boxes, and prior ledger item R18 is discharged.

The adversarial tier mattered more than usual on this pass. Of nine findings raised at high or
critical severity, **one survives at high, one at medium, four were downgraded to low, and four
were refuted outright**, and the review's only critical finding was refuted by two independent
skeptics while spawning a new medium in its place. Two of the three
findings inherited from the interrupted session also failed to survive: the total-correlation gap
was killed by explicit computation, and the claimed cross-chapter gauge-convention conflict was a
symbol confusion. The panel's raw severities ran hot, and the report below reflects the
adjudicated severities, not the raw ones.

**Recommendation: minor revision.** No result is wrong. The genuine defects are one stale claim
crediting a deleted proposition, one undefined symbol inside an `ESTABLISHED` theorem, a broken
provenance chain in the verification ledger covering the manuscript's newest 1,642 lines, an
undeclared perturbation class whose two readings disagree about whether the RG relevant branch is
inhabited, and a numerically unstable evaluation form in the manuscript's own check suite. Each
has a bounded, mechanical fix.

## Status of findings raised at high or critical

| # | Finding | Raised | Adjudicated | Verdict |
|---|---|---|---|---|
| P-1 | Ch. 12 credits Ch. 2 with a proof that does not exist | high | **high** | survives as stated |
| P-2 | Audit index omits the Ch. 8 monotonicity obligation | high | low | justification refuted |
| N-1 | `\mathcal L^{\rm ext}` undefined in an `ESTABLISHED` theorem | high | **medium** | survives, reasoned down |
| N-3 | Roman `R` overloaded across chapters | high | low | not a mathematical error |
| N-5 | `P_b` bundle vs. precision matrix | high | — | refuted |
| N-6 | `\Theta` carries six meanings | high | — | refuted |
| N-7 | `\mathcal R` carries six meanings | high | — | refuted |
| RG-F1 | The "relevant" branch of the RG classification is empty | critical | — | refuted, 3 of 3, unanimous |
| RG-F1′ | The action-space norm is never declared, so the trichotomy swings between vacuous and unbounded | — | **medium-high** | new; two skeptics converged on it independently |
| RG-F2 | No isolated or hyperbolic RG fixed point | high | — | refuted |
| RG-F3 | The additive constant `c_b` is forced to zero | med-high | — | refuted |
| V1 | Symmetric local objectives *can* sum to the collective VFE | high | — | refuted |
| V2 | `prop:obs-attention-elbo` missing a factorization hypothesis | high | — | refuted |

Every row above is fully adjudicated; all seven skeptic verdicts are in.

## Major comments

### 1. Chapter 12 credits Chapter 2 with a proof that no longer exists (high; essential)

`12_philosophy.tex:100-102` states that "The geometry chapter proves that curved and flat averaged
connections are mathematically possible." Chapter 2 proves no such thing. The string `averag` does
not occur anywhere in `02_geometry.tex`, and that chapter's single mention of curvature, at
`02:369`, says the opposite: the connections "are chosen data; no curvature or transport is
inferred from the agent frames." Searches for `partition of unity`, `subordinate`, and
`convex combination` return zero matches manuscript-wide.

The sentence was true when it was written. `git show 96b7b5f` removed the section "An induced
connection from the frames" together with Definitions and Propositions 2.29 through 2.32, and the
deleted Proposition 2.32, then tagged `ESTABLISHED`, delivered both halves with explicit
witnesses: a flat average on the real line, and `a = -y\,dx` on `R × (0,1)` with `F = dx ∧ dy ≠ 0`
and nontrivial holonomy. The claim in Chapter 12 was orphaned by that deletion and never updated.
The deletion left further debris: `02_geometry.tex:264` carries a `\label{sec:geo-induced-connection}`
that no `\ref` in the manuscript resolves to.

A second defect compounds the first. Under `SPEC.md` §2.1 the `\status{CONJECTURE}` tag at
`12:100` governs the preceding sentence, so the claim at `12:100-102` carries no status tag at
all, and `SPEC.md:74` states that "A claim with no status is a defect."

Mitigating: `appendix_claim_ledger.tex:144-148` states the same conjecture without the
averaged-connection premise, so nothing downstream depends on the false sentence.

**Fix.** Either restore the deleted Proposition 2.32 or rewrite `12:100-102` to drop the appeal to
a Chapter 2 result, and give the surviving claim its own status tag. Delete the orphan label at
`02:264`. This is the one finding in the review that a reader could act on and be misled by.

### 2. The verification ledger for the newest chapters cannot be audited (high; essential)

All four claims `PB-1` through `PB-4` in `.verification/pullback-geometry-ledger.json` record
`artifact_revision: git:43eb7e74`, and their evidence entries cite
`05c_pullback_geometry.tex:20-566`, `05c_pullback_geometry.tex:574-849`, and
`05d_relational_inference.tex:13-626`. Neither file existed at that revision. `git ls-tree 43eb7e7`
returns empty for both paths, and `git log --diff-filter=A` shows both were first added one commit
later, in `0af1cbd`.

Under the project's own evidence-gating rule, that evidence is fresh only for the recorded
artifact revision, so as recorded these four `EVIDENCE_VERIFIED` claims have an invalid provenance
chain. The verification was in all likelihood performed correctly against the working tree, and
this pass's geometry and information-geometry lenses independently recomputed much of the same
material and found it sound. But on the record, the manuscript's newest 1,642 lines — the
pullback-geometry and relational-inference chapters, the least-swept surface in the document — are
not covered by an auditable closure record.

**Fix.** Re-anchor the ledger to `0af1cbd` or later and re-run the checks, so the recorded
revision actually contains the cited evidence.

### 3. `\mathcal L^{\rm ext}` is undefined inside an `ESTABLISHED` theorem (medium)

The symbol occurs exactly twice in the entire manuscript, at `06_general_coarsegraining.tex:209`
and `:213`, both inside `eq:cg-elbo-monotone` in `thm:cg-evidence-preserving-channel`, which
carries `\status{ESTABLISHED}`. It is defined nowhere, under any glyph, and appears in neither
`SPEC.md` nor `appendix_notation.tex`. The prose "extended ELBOs" at `:207` is its only gloss.

Two independent lenses and one skeptic reached different severities, and the reasoned middle is
medium. In its favor as a minor item: the displayed line is arithmetically self-contained, the
theorem is referenced zero times elsewhere, and the inequality is correct under both plausible
readings, which were verified to agree to `2.2e-16`. Against: under the density reading the
theorem is missing a coarse reference measure and a coarse hypothesis (H4), so the repair has real
mathematical content rather than being a gloss. The nearest neighboring symbol,
`\widetilde{\mathcal L}` at `05_elbo.tex:54`, is the pseudo-ELBO the manuscript explicitly warns
is *not* a bound, which is precisely the wrong thing for a reader to land on.

**Fix.** Promote the prose at `05_elbo.tex:458` to a tagged definition of the canonical
relative-log extension and cross-reference it from `06:207`. Do **not** simply drop the superscript
in favor of the `\Lelbo` macro: that silently imports hypothesis (H4), which the theorem does not
assume. The same statement is already written correctly with defined symbols at
`07_restrictions.tex:302-305`; use that as the model.

### 4. The manuscript's own gap computation is numerically unstable (medium)

The displayed evaluation form of `eq:restrict-determinant-gap` and `eq:restrict-refinement`, which
is implemented verbatim as `factorization_gap` at `verification/run_checks.py:1277`, is
cancellation-prone. An executed sweep returned a **negative** gap on 833 of 3138 draws, worst
`-2.30e-03`, at condition number `1e14` with `ε ≤ 1e-8`. A negative gap means a computed
`ℒ*_𝔅` exceeds `log p_θ(o|X)`, violating the bound the quantity is meant to certify. The
equivalent Schur and `log1p` form returned zero negatives over the same sweep. Compounding this,
the check `CHK-CG-FACTOR-GAP` applies an absolute threshold of `1e-12` to a quantity whose
roundoff scales with `|log det|`, and the suite's single draw sits at condition number `29.58`, so
the failing regime is never exercised.

**Fix.** Replace the displayed evaluation form with the Schur/`log1p` form and make the tolerance
relative.

### 5. The verification manifest does not bind the sources it certifies (medium)

Re-running `run_checks.py` rewrote 28 manifest entries across 14 `.tex` files while every check
result and line number stayed byte-identical: the committed manifest had gone stale against the
August 1 edits and nothing detected it. `run_checks.py` recomputes and overwrites the source hashes
without ever comparing them, and records neither a timestamp nor a git revision, so the freshness
contract stated at `appendix_numerical_provenance.tex:41-47` is unenforceable as written. This is
the same class of defect as comment 2 and has the same consequence: a provenance record that
cannot fail is not a provenance record.

**Fix.** Add a `--verify` mode that compares rather than overwrites, and record
`run_timestamp_utc` and `git_rev` in the results file.

Note that running the suite during this review modified the tracked file
`verification/current-results.json`, which is what the runner does by design. The diff is purely
source hashes and byte counts updating to match current sources, leaving it more accurate than the
committed copy. It has been left modified and uncommitted for the author to decide on.

### 6. Positive-definiteness is asserted but not established (medium)

`06_gaussian.tex:323` states that "Positive definiteness is proved by
`prop:gauss-interaction-energy-kernel`." That proposition proves `Λ ⪰ 0` together with an
if-and-only-if criterion, not definiteness. The supporting `prop:gauss-interaction-nonempty` at
`:308` hypothesizes "a proper prior of precision `A_i ⪰ 0`", which is self-contradictory, since a
singular precision is improper, and concludes only membership in `𝓘(V)`. Taking `A_i = 0`, which
the stated hypothesis admits, yields `λ_min(Λ) = -9.5e-16` with nullity exactly `K`, the consensus
subspace, so the constructed witness need not be a density at all, while `eq:gauss-density`
requires `J ∈ 𝕊ⁿ₊₊`. The consequence is that `𝓘(V) ∩ 𝕊^{NK}₊₊ ≠ ∅` is never established even
though `hyp:gauss-global-interaction` needs it.

**Fix.** Two lines: require `A_i ≻ 0` in the nonemptiness proposition, and restate `:323` as
semidefiniteness plus the criterion.

### 7. Campbell 1986 is misattributed (medium)

`08_infogeometry.tex:315`, tagged `ESTABLISHED`, states that Chentsov uniqueness up to scale
extends to non-normalized measures "due to Campbell1986". Campbell's actual theorem gives
`⟨X_i, X_j⟩ = A(|x|) + δ_ij |x| B(|x|)/x_i` with `A` and `B` arbitrary smooth functions of the
total mass: a two-function family, not a scale. This is corroborated by the manuscript's own
`Ay2015` citation, Main Theorem 2.10(2). The correction runs in favor of the section's thesis, so
fixing it strengthens §8.4 rather than weakening it.

### 8. Measure-theoretic hypotheses that are used but not stated (medium)

Two items in Chapter 3. First, `prop:prob-kernel-integration-measurability` at `03:166-177`,
tagged `ESTABLISHED`, contains an unproved clause: the lemma is stated for *probability* kernels
and its Dynkin proof uses finiteness, while `eq:prob-evidence` integrates against the σ-finite and
infinite `ν^Y_D`; separately, joint measurability of a *version* of the density is an uncited
distinct fact. A counterexample is on file: the constant kernel `Unif[0,1]` with version
`p(o|X) = 1 + 1_N(X) 1_{\{X\}}(o)` for non-Borel `N` is a valid density for every `X` yet is not
`ℬ⊗ℬ`-measurable. The prose at `03:177` inflates this to "discharged here rather than assumed".

Second, `def:prob-reference-measures` at `03:71-79` builds the mixed-coordinate reference measure
from the coordinate's law, so it depends on `(θ, X)`, while `eq:prob-generative-density`,
`05_elbo.tex:129`, and `eq:restrict-cross-model` all presume a single `(θ, X)`-free `ν`. Witness:
`μ_θ = ½δ_θ + ½N(0,1)` admits no σ-finite common dominating measure, and the resulting "evidence
difference" at `o = 0`, `θ ∈ {0,1}` is `0.9189`, a number with no likelihood-ratio meaning.

### 9. Gauge-lens medium items (medium)

Three from Chapter 2 and its neighbors, none affecting a result. `R_b, R_m` are introduced at
`02:361` as "the represented coordinate changes" with no direction given, and the law is correct
only under the convention fixed two chapters later at `04:280-285`; the formula that would
disambiguate, `R_i^b = ρ_b(g_i)`, sits 300 lines later at `02:661` with the channel index moved
from subscript to superscript. Separately, `p_{θ'} = |det R|^{-1} p_θ(R^{-1}y')` requires
`R_# ν^Y_D = |det R|^{-1} ν^Y_D`, which fails on Chapter 3's own mixed continuous-plus-atomic
reference measure, though the measure-level conclusion survives. And the text describes "the full
residual group" as the stabilizer of the shared-link constraints, but that set is not closed under
multiplication; an explicit `GL(2,R)` counterexample gives a design-dependent product.

### 10. The RG action-space norm is never declared (medium-high)

`07b:756-759` declares the perturbation class as `L^∞` "or, more generally, perturbations with
*conditional* exponential integrability". Those two readings are not equivalent, and they disagree
about whether the relevant branch of the trichotomy at `07b:771-774` is inhabited.

Under the conditional reading, which is what the text says, the branch is inhabited. An explicit
witness is on file: on `S = ℕ₀` with `p = 1/2`, the advance-or-reset kernel `K(i, i-1) = 1` for
`i ≥ 1` and `K(0, j) = (1-p)p^j`, with `ρ_* = m_* = π_i = (1-p)p^i` and `H_* ≡ 0`. All identities
hold exactly in rational arithmetic (`πK = π`, reversal identity with zero violations,
fixed-action residual exactly `0.0`). The perturbation `φ(i) = 1/3 + (2/3)·4^i` satisfies
`max|Uφ - 2φ| = 0` exactly, giving `D_H R_b^H[φ] = 2φ` and, at `b = 2`, the exponent
`y = log 2 / log 2 = +1`: relevant. The choice `b = 2` is principled, since the step destroys
`H(Y|Z) = 0.693147` nats, exactly one bit, and the semigroup holds with `y = +1` at `b = 2, 4, 8`
alike. The perturbation is admissible because `Π_*(·|z)` has two-point support, so its conditional
moment generating function is finite for every real `t`. A weighted space `c_0(w)` with `w = 5^i`
gives spectral radius `2.5`.

Under the unconditional evidence-mass reading, `φ ∈ L¹(π_*)` and Jensen forces `|λ| ≤ 1`, so the
branch is empty. The witness above has one-sided finite evidence mass only.

A second structural point falls out and is worth stating in the text: for a positive unital
operator on an action lattice with quasi-interior constants, `r(T) > 1` forces `r(T) = r_ess(T)`,
verified here at `r = r_ess = 2.5` with point spectrum an open disk. Relevance therefore never
arises from an isolated eigenoperator. `07b:768-770` already routes growth to the continuous and
residual spectrum and `07b:774-776` fences generalized eigenspaces, so the manuscript's own
hedging is what makes the classification survivable.

A second skeptic reached the same conclusion from an unrelated construction, which is why this
is recorded at medium-high rather than medium. In a Mehler realization satisfying every hypothesis
of Chapter 7b — common space `R`, Markov `K_b` as block-sum plus rescale with `r = b^{-1/2}`,
invariant `ρ_* = N(0,1)`, exact semigroup `K_2 K_2 = K_4` to `1.1e-15`, `H_* = 0` — the function
`ψ(y) = e^{y²/2}` gives `D_H R_b^H[ψ](z) = b^{1/2} e^{z²/2}` (exact by sympy; relative error
`3.4e-41` at 40 digits), hence `y_a = +1/2 > 0`. On the Banach space where it lives the operator is
bounded with norm exactly `b^{1/2}`; but `φ_m = y^m e^{y²/2}` is triangular with diagonal
`b^{(m+1)/2}`, so on that space the spectral radius is `+∞`. Two independent constructions, one on
the naturals and one on the line, therefore put the trichotomy on either side of well-posedness
depending on a norm the manuscript never fixes. Under the licensed class the manuscript does name
elsewhere — "two required moments", forcing at most quadratic growth and hence `⊂ L²(π_*)` —
Jensen closes it and the branch is empty.

**Fix.** Declare the action-space norm the trichotomy is stated over. Note that simply asserting
spectral radius one, as the refuted finding proposed, would enter the manuscript as a **false
theorem** unless "bounded, in the declared class" is attached. Also state the
`r(T) = r_ess(T)` consequence, so the reader knows relevance here is not an isolated-eigenvalue
phenomenon.

### 11. `JonaLasinio2001` is uncited and supplies two results the manuscript flags as missing (medium)

The entry sits at `references.bib:1103` with zero citations anywhere in the manuscript, and three
of this pass's agents independently arrived at it. Jona-Lasinio 2001 (arXiv:cond-mat/0009219) is
the canonical treatment of the renormalization-group reading of the central limit theorem: eq.
(2.14) gives the eigenvalues `λ_k = 2^{1-k/2}` with Hermite eigenfunctions, and eq. (5.10) names
the conditional expectation as "the linearization of the RG at the fixed point", which is exactly
the operator of `07b:756-777`. Beyond corroboration it supplies two things the manuscript is
missing: eq. (7.4), the generalized eigenvalue between two tangent spaces, which resolves the
non-endomorphism problem the trichotomy runs into; and eq. (7.5),
`λ_k(m, R*P) λ_k(n, P) = λ_k(mn, P)`, the reference-direction cocycle that this review's RG lens
separately reported as absent. Citing it closes two open items at once.

## Minor comments

Recorded in full in the per-lens files. The larger clusters: `h_i` versus `h_i^x` collide and the
`Θ`-law is displayed twice with opposite-sided inverses without reconciliation
(`lens-gauge.md`, G4); `B`, `B_⊥`, `G`, `Q`, and `\operatorname{pdet}` are used in Chapter 9 but
defined only elsewhere or not at all (`lens-coarsegraining.md`, CG-2, CG-3);
`thm:cg-evidence-preserving-channel` names "does not read `Q_o`" as its hypothesis when the display
needs `K(x, 𝖸) = 1`, which sub-Markov kernels break immediately (CG-4);
`cor:cg-compact-holonomy-barycenter` needs `\overline{\mathcal H}`, since finitely generated
represented holonomy of a finite graph is generically non-closed (CG-7); the entire RG operator
tier is absent from `appendix_notation.tex` (`lens-rg.md`, RG-F7); Kemeny–Snell for the lumpability
biconditional and Nakajima–Zwanzig for `eq:rg-memory-operators` are uncited, and an Abelian theorem
is labeled Tauberian at `07:469` (RG-F10/F11); Chapter 11 points the cut-closure condition at
Chapter 10 when it lives at `eq:cg-cut-excess` in Chapter 9 (`lens-philosophy.md`, P-7);
`esfeld2008moderate` is cited for a radical structural-realist thesis its authors explicitly
disavow (P-3), and van Fraassen 1980 for an eliminative parsimony rule constructive empiricism does
not endorse (P-4); `main.tex:21` advertises the keyword `emergent time`, which `12:45-51`
explicitly disclaims (P-10); the double status tags on single paragraphs at `01:102`, `01:114`, and
`06:180` (P-11).

Housekeeping: `main.log`, `main.aux`, and `main.toc` are stale, dating from a July 29 249-page
build with 126 overfull boxes, and will mislead a future reviewer; refresh or gitignore them. Ten
status tags hyphenate across line breaks (`[ESTAB-`/`LISHED]`), cosmetic only, fixable with
`\mbox{[#1]}` at `main.tex:104`.

## What the review could not break

Recorded in full in `01-verified-clean.md` and worth reading before the next pass, since it is the
larger half of this review's output. Highlights: the gauge algebra of Chapter 2 re-derived from
declared conventions and checked numerically, including the cocycle under three-frame composition
and the transport direction that discharges prior ledger item R02; Chapter 5c realized concretely
on the SPD bundle with gauge-invariance residual `1.2e-9` against value `28.0` and congruence
Fisher isometry `8.2e-16`; the KL divergence jets verified symbolically to exact zero on a curved
chart across all eight components; `thm:hist-record-clock-contraction` at residual `3.9e-16` with a
four-million-sample Monte-Carlo cross-check; the Amari–Chentsov tensor reproduced with zero
mismatches over all index triples; sixteen RG identities including the Ising-star cubic coefficient
exactly zero by symbolic computation; refinement monotonicity exhaustive over all 52 partitions of
five coordinates and all 358 refinement pairs with zero violations; and 118 coarse-graining checks
at worst residual `1.1e-14`.

Four hypotheses were confirmed load-bearing by counterexample, which is worth recording so nobody
proposes weakening them: parameter-dependent `K_θ` drives the coarse Fisher information to 400
against a fine value of `0.25`; sub-Markov `K` reverses the ELBO ordering at every scale `≤ 0.5`;
non-lumpable `K` breaks Bayes recovery at `5.2e-2`; failed diagonal affinity breaks
`thm:cg-graph-exponential-closure`.

The falsifiability posture is exemplary and should not be softened: the manuscript states it has no
discriminating prediction, classifies its only available test as internal, and locates empirical
risk in the added cross-scale hypothesis rather than in the theorems.

## Adjudicated rejections — do not re-raise

- **Total-correlation factorization gap** at `05b:292-315`. `eq:obs-global-ledger` is exact
  (residual `-1.11e-16`) and unconditionally valid in `[0, ∞]` given `Q ≪ P_0 = ⊗ρ_i`, since
  `Q ≪ ⊗Q_i` follows and each KL's negative part is bounded by `1/e`. No missing hypothesis.
- **Cross-chapter gauge-convention conflict** between `02:361-365` and Chapter 7b. A symbol
  confusion: `\mathcal R_b` in 7b is the block-`b` renormalization operator with `b` a blocking
  ratio, a different glyph from `R_b`. Both `eq:geo-defect-gauge-laws` and
  `eq:rg-linear-cross-scale-covariance` are correct; they differ only because Chapter 2 feeds
  `ρ(g)` and Chapter 7b feeds `ρ(a)` with `a = g^{-1}`.
- **`P_b`, `\Theta`, and `\mathcal R` symbol collisions** as defects. `appendix_notation.tex:4-8`
  promises only that superscripts `b`/`m` denote channels; it never promises glyph uniqueness, and
  its closing paragraphs show the declared discipline is controlled reuse with a non-identification
  clause, which the chapters apply in situ at each flagged site.
- **RG-F2, no isolated or hyperbolic fixed point.** "hyperbolic", "ergodic", "irreducible", and
  "reducible" have zero occurrences manuscript-wide; both horns sit inside declared hypotheses.
  "Exhaustive" modifies the fixed-point equations, and the biconditional at `07b:719` tested clean
  on 2000 random draws with zero disagreements.
- **RG-F3, `c_b` forced to zero.** `07b:734` already states "normalization fixes `c_b = 0`" and
  `07b:745-746` gives the mechanism. In the declared sector where mass is discarded
  (`07b:726`, `:641-643`) the ray equation is genuinely weaker, with an explicit witness.
- **P-2's justification**, that the RG has no established arrow. Refuted by
  `thm:rg-exact-coarse-vfe` (`07b:34-57`, `ESTABLISHED`), restated at `07b:801-806`. The Chapter 8
  OPEN is scoped to the deterministic Galerkin aggregation map, not the Markov coarse channel.
- **V1, symmetric local objectives summing to the collective VFE.** The counting-number arithmetic
  replicates (`Σ_i F_i - F_o = 2.22e-16`) but the witness is not in the class: `05b:311-313` fixes
  it one sentence earlier with "counts factor `a` **exactly** `|∂a|` times", restated at
  `05b:282-285`, `appendix_notation.tex:153-156`, and `01:83-84`, all reading *incident*. A
  structure theorem settles it: any `{F_i}` with `Σ F_i = F_o` and `∂_i F_i = ∂_i F_o` satisfies
  `F_i = F_o + h_i(η_{-i})`, so every witness contains the whole collective VFE and no local
  witness exists under any weight rule. The witness also sums correctly only on the product slice
  (off it, `Σ_i F_i - F_o = -TC(Q) = -0.5048`), and on the unilateral move the theorem quantifies
  over it fails derivative matching by `0.0205` where the manuscript's outside-averaged local VFE
  matches to `5.6e-12`. The Yedidia–Freeman–Weiss canon does not fit either: regions must contain
  the factors they count, and region-based free energies are approximations.
- **V2, a missing factorization hypothesis in `prop:obs-attention-elbo`.** The algebra replicates
  (residual equals `E_{Q_Y}[TC(Q_{J|Y})]` to `3.9e-16`) but violates a stated hypothesis.
  `11:207` glosses the family as "factorizing over `b` and the constituents", `05b:423-425`
  declares it a product family with block-diagonal Fisher metric "including categorical blocks
  when present", and Blei–Kucukelbir–McAuliffe §2.3 defines mean-field as mutual independence.
  Under mean-field `TC = 0`, so there is no substitution and no inconsistency with `05:350`.

## Open at time of writing

**RG-F1 is refuted unanimously**, three skeptics to zero. All seven skeptic verdicts for this
pass are now in and nothing is outstanding. The three refutations are independent and reach the
same place by different routes.

The scope skeptic found that `07b:771-774` is a conditional naming convention with no existential
quantifier, the one applied instance is tagged OPEN at `05a:264-267`, `07b:801-806` explicitly
denies approach to a critical fixed point, "criticality" occurs zero times manuscript-wide, and
`y_a` is computed nowhere, so nothing downstream depends on the branch.

The mathematics skeptic went further and falsified RG-F1's central claim outright, by meeting the
finding's own stated falsification condition: it constructed a concrete kernel with `|lambda| = 2`
and an admissible perturbation, so the relevant branch is inhabited under the reading the text
actually declares. RG-F1's numerics were correct but structurally blind, since on a finite space
every function is bounded, and its quotation of the declared class as `L^inf` was a misquote of
`07b:756-759`. Two subsidiary claims are also wrong: "every exponent short by exactly +1" holds
only in the alpha-stable sector, and its `mu_0 = 1` contradicts `10:271-272`, which has
`mu_0 = b^2`.

What survives is major comment 10 above, a well-posedness gap at medium, plus two low items: state
the spectral-radius-one and Crandall-Tartar nonexpansiveness result that `07b:805` asks for, and
retag the trichotomy from `ESTABLISHED` to `DEFINITION` per `SPEC.md:67`.

V1 and V2 also returned **refuted** and are recorded under adjudicated rejections above.

The literature skeptic refuted sub-claim (a) the same way the mathematics skeptic did, by explicit
construction on a different space, and confirmed against primary sources that relevance in the
canon is a property of the conjugate coupling carrying a volume factor `d` (Fisher, RMP 70, 653,
eqs. 43 and 45-48; van Enter-Fernandez-Sokal on interaction spaces). It also corrected the refuted
finding's arithmetic a second way: the deficit is `d`, not `1`, since `+1` presumes `b` is the
volume ratio, which the RG lens separately reports as undeclared. Its verdict was
survives-at-lower-severity under a rename, which is comment 10 above.

## Artifacts

Per-lens findings and skeptic adjudications are in this directory: `00-settled-ground.md`,
`01-verified-clean.md`, `lens-gauge.md`, `lens-geometry.md`, `lens-infogeo.md`,
`lens-variational-elbo.md`, `lens-coarsegraining.md`, `lens-rg.md`,
`lens-probability-numerics.md`, `lens-philosophy.md`, `lens-integrity.md`,
`skeptic-philosophy.md`, `skeptic-notation.md`, `skeptic-rgf1-scope.md`, `skeptic-rgf2-f3.md`,
and the three pending skeptic files named above.
