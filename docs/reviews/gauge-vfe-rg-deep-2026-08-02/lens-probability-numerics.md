# Lens review — measure-theoretic probability and numerical analysis

Scope: `03_probability.tex`, `07_restrictions.tex`, `appendix_numerical_provenance.tex`,
`verification/`. Everything in `00-settled-ground.md` (R01–R21, FINAL-01–08, LG/RG/PB, and the
manuscript's own declared-open ledger) is treated as out of scope and is not re-raised.

Environment for every recomputation below: `C:\Python314\python.exe` 3.14.4, numpy 2.4.4,
scipy 1.17.1, Windows-10-10.0.19045, fp64 (53-bit mantissa, eps = 2.220446049250313e-16).

---

## 0. Verification suite — actual current machine output

Declared run from `appendix_numerical_provenance.tex:24-27`, executed verbatim from the repository
root:

```
$ "C:/Python314/python.exe" manuscripts/gauge_vfe_rg/verification/run_checks.py
{"checks": {"FAIL": 0, "INCONCLUSIVE": 0, "PASS": 29},
 "dispositions": {"keep_exact": 9, "remove": 0, "retain_as_inconclusive": 0,
                  "rewrite_to_current_check": 0},
 "inventory": "PASS", "occurrences": 11,
 "output": "...\\manuscripts\\gauge_vfe_rg\\verification\\current-results.json",
 "overall_status": "PASS"}
exit 0
```

`current-results.json` `summary` after the run:
`total_NUMERICAL_occurrences: 11`, `literal_status_macro_occurrences: 11`,
`bare_status_table_entries: 0`, `substantive_claims: 9`, `taxonomy_entries: 1`,
`duplicate_register_entries: 1`, `checks {PASS: 29, FAIL: 0, INCONCLUSIVE: 0}`,
`current_protocol_claims_pass: 9`, `current_protocol_claims_inconclusive: 0`.

These match the counts quoted in `verification/VERIFICATION.md:6-10` (11 tokens = 9 + 1 + 1) and
`VERIFICATION.md:55` (29 checks). **The quoted numbers are currently accurate.** The declared run
command works verbatim. (Finding N3 below concerns the *staleness* of the committed artifact, not
these counts.)

---

## Findings

### P1 — `prop:prob-kernel-integration-measurability` proves its first sentence and not its second

- **Claim / location.** `03_probability.tex:166-177`, `prop:prob-kernel-integration-measurability`,
  `eq:prob-kernel-integration`. The proposition body reads: "Then `x ↦ ∫_F f(x,y) κ(x,dy)` is
  `𝓔`-measurable. **Consequently `X ↦ p_θ(o|X)` and the `Q_X`-expectations appearing in the bound of
  Chapter 5 are measurable in `(o,X)`** whenever their integrands are jointly measurable."
- **Severity.** medium
- **Status.** `\status{ESTABLISHED}` (03:172). Prose inflates: 03:177 says "an implicit use of an
  unproved measurability claim is a gap. It is discharged here rather than assumed." The
  "Consequently" clause is *inside* the ESTABLISHED statement and the proof (03:175) never touches
  it.
- **Evidence.** Two independent defects.

  **(a) The proved lemma does not cover the integral it is applied to.** The proposition is stated
  for a *probability* kernel `κ`, and its Dynkin proof uses finiteness explicitly ("`𝒟` … is closed
  under proper differences **because `κ(x,·)` is a finite measure**"). But `eq:prob-evidence`
  integrates against `ν^Y_D`, which by `def:prob-reference-measures` is σ-finite and (in the Gaussian
  realization, Lebesgue on `∏ ℝ^K × ℝ^{d_m}`) infinite. A constant kernel `κ(x,·) = ν^Y_D` is not a
  probability kernel, so `prop:prob-kernel-integration-measurability` does not apply to
  `eq:prob-evidence`. The correct instrument is Tonelli for σ-finite measures — which the chapter
  does invoke correctly one section earlier (03:137) but only for *fixed* `(θ,X)`.

  **(b) Joint measurability of the density is version-dependent and is not supplied.**
  `def:prob-normalized-kernels` (03:115) itself insists densities are determined only up to
  reference-null sets. A statement that `(o,X) ↦ p_θ(o|X)` is measurable is therefore a statement
  about a *selected version*, and arbitrary per-`X` selection destroys it. Explicit counterexample,
  entirely inside the chapter's own typing:

  > Let `𝖷 = [0,1]` with `ℬ`, let the observation space be `𝖮 = [0,1]` with `ℬ` and reference
  > `ν^O = λ`, and let `P(·|X) = Unif[0,1]` for every `X` — a probability kernel, measurable in `X`,
  > dominated by `λ`. Pick `N ⊆ [0,1]` non-Borel and set
  > `p(o|X) := 1 + 1_N(X)·1_{\{X\}}(o)`.
  > For each fixed `X` this is a legitimate density version: `∫_A p(o|X) λ(do) = λ(A) + λ(A∩{X}) =
  > λ(A) = P(A|X)`. Yet `{(o,X) : p(o|X) ≠ 1} = {(x,x) : x ∈ N}`, and since `x ↦ (x,x)` is a Borel
  > isomorphism of `[0,1]` onto the closed diagonal `Δ ⊆ [0,1]²`, that set is Borel iff `N` is.
  > Hence `(o,X) ↦ p(o|X)` is **not** `ℬ⊗ℬ`-measurable, and `prop:prob-kernel-integration-measurability`
  > as stated gives no grounds to exclude this version.

  The conclusion is nonetheless *true* under the standard dominated-kernel lemma (a kernel dominated
  by a fixed σ-finite measure admits a jointly measurable density version) — but that lemma is
  neither stated nor cited anywhere in the chapter, and the chapter cites `\citep{Kallenberg2021}`
  only for "the full development of kernels and their integrals".

  This is load-bearing by the manuscript's own words: 03:177 ("used implicitly whenever one writes an
  expectation over configurations") and 03:65 (configuration priors and configuration recognition
  kernels), and again 05_elbo.tex:186 which explicitly contemplates "jointly measurable pointwise
  density and conditional versions declared as part of the parameterized model".
- **Fix.** Split the proposition. Keep the Dynkin lemma as proved. Add a second, separately cited
  statement: *for a kernel `P_θ(·|X)` dominated by a fixed σ-finite `ν`, there exists a jointly
  `𝒳⊗𝒪_D⊗𝒴_D`-measurable version of `p_θ(o,y|X)`; that version is declared as model data, and then
  Tonelli for σ-finite measures gives joint measurability of `p_θ(o|X)` in `(o,X)`.* Same declaration
  for `q_X(y|o)`. Do not derive it from `eq:prob-kernel-integration`.
- **Falsifies.** Nothing downstream is false; the ELBO measurability that Chapters 5–11 rely on
  survives once the lemma is cited. What is falsified is the chapter's claim to have *discharged*
  this measurability obligation.

---

### P2 — the mixed-coordinate reference measure is a function of `(θ,X)`, but every cross-parameter evidence comparison presumes it is not

- **Claim / location.** `def:prob-reference-measures`, `03_probability.tex:71-79`:
  "Each mixed real coordinate carries the measure declared in
  `\Cref{prop:prob-mixed-coordinate-dominating-measure}`." That proposition (03:87-93) constructs
  `ν = λ + Σ_{x∈A} δ_x` where `A` is *the atom set of `μ`* — and `μ` is the coordinate's law, hence a
  function of `(θ,X)`. Yet `eq:prob-reference-measures`, `eq:prob-generative-density` and
  `eq:prob-evidence` write `ν^O_D`, `ν^Y_D` with no `(θ,X)` index.
- **Severity.** medium
- **Status.** `def:prob-reference-measures` is `\status{DEFINITION}` (03:79);
  `prop:prob-mixed-coordinate-dominating-measure` is `\status{ESTABLISHED}` (03:93) **and is correct
  as stated** — I verified its proof line by line (σ-finiteness via `ℝ = ⋃_n([-n,n]\A) ∪ ⋃_{x∈A}{x}`
  with `ν([-n,n]\A) ≤ 2n` and `ν({x}) = 1`; absolute continuity from `ν(B)=0 ⟹ λ(B)=0 ∧ B∩A=∅`).
  The defect is in the *use*: a hypothesis (θ-free reference) is used but not stated. Prose inflation
  is at 03:4 — the chapter's opening claims this ordering "is what makes the exact evidence bound of
  Chapter 5 an identity rather than an inequality with hidden exceptions."
- **Evidence — explicit counterexample.** One mixed real observation coordinate, one-parameter
  family:

  > `μ_θ = ½ δ_θ + ½ 𝒩(0,1)`, `θ ∈ ℝ`. Each `μ_θ` has no singular continuous part, so
  > `prop:prob-mixed-coordinate-dominating-measure` applies and returns `ν_θ = λ + δ_θ`.
  > *No σ-finite measure dominates the whole family.* Suppose `μ_θ ≪ ν` for every `θ`. Since
  > `μ_θ({θ}) = ½ > 0`, necessarily `ν({θ}) > 0` for every `θ ∈ ℝ`. A σ-finite measure has at most
  > countably many atoms (each set of finite measure contains at most countably many atoms of
  > positive mass, and there are countably many such sets), so `ν` is not σ-finite. Contradiction.

  Consequence: `p_θ(o|X) = dP^O_{θ,X}/dν_θ` and `p_{θ'}(o|X) = dP^O_{θ',X}/dν_{θ'}` are derivatives
  against *different* measures. Concretely at `o = 0` with `θ = 0, θ' = 1`:
  `p_0(0) = μ_0({0})/ν_0({0}) = ½`, `p_1(0) = ½φ(0) ≈ 0.19947`, so
  `log p_0(0) − log p_1(0) ≈ 0.9189` — a number with no likelihood-ratio meaning.

  This is used downstream in results tagged ESTABLISHED:
  - `07_restrictions.tex:262-268`, `eq:restrict-cross-model`, which calls
    `[log p_θ(o|X) − log p_{θ'}(o|X)]` "an evidence difference, a model-comparison quantity"
    (`prop:restrict-unrelated-joint-elbo`, `\status{ESTABLISHED}` at 07:268);
  - `05_elbo.tex:129`, "the parameter subscript is restored as `ℒ_ϑ` whenever two parameter values
    are compared."
- **Fix.** Add one sentence to `def:prob-reference-measures`: *the component reference measures are
  declared once, before and independently of `θ` and `X`; for a mixed coordinate the atom set `A` is
  part of that declaration and is required to contain the atoms of `μ^{θ,X}` for every admissible
  `(θ,X)`.* Then add a remark that this is a genuine restriction — families with moving atoms admit
  no common σ-finite dominating measure, exactly as the singular-continuous exclusion at 03:98 is
  already flagged as "a real restriction".
- **Falsifies.** Only the general-theory tier. All of Part II (Gaussian realization) uses Lebesgue
  coordinates only, where `ν` is manifestly `(θ,X)`-free, so no worked result is wrong.

---

### P3 — `def:prob-reference-measures` permits a non-σ-finite component, contradicting 03:82 and 03:121

- **Claim / location.** `03_probability.tex:72`: "Each discrete coordinate carries its power-set
  sigma-algebra and counting base measure." No countability requirement. Compare 03:82
  ("Sigma-finiteness of every component **is required** and is not decoration") and 03:121 ("This
  holds for the finite products of Euclidean and **countable** discrete fibers").
- **Severity.** low
- **Status.** `\status{DEFINITION}` (03:79). The word "countable" is present at 03:121 and absent
  from the definition that 03:121 depends on.
- **Evidence.** Take one discrete fiber `𝖮_{i,a} = [0,1]` with `2^{[0,1]}` and counting measure `#`.
  Then, in order:
  1. `#` is not σ-finite, so the product `ν^O_D ⊗ ν^Y_D` in `eq:prob-generative-density` is not
     uniquely determined by its values on rectangles, and the equation has no unique referent.
  2. The Tonelli step at 03:137 fails. Classical witness (Sierpiński; Folland, *Real Analysis* 2nd
     ed. Ex. 2.46; Rudin, *RCA* 8.9(c)): with `E = ([0,1], 2^{[0,1]}, #)` and
     `F = ([0,1], ℬ, λ)`, the diagonal `Δ = {(o,y) : o = y}` is closed in `[0,1]²` hence lies in
     `ℬ⊗ℬ ⊆ 2^{[0,1]}⊗ℬ`, yet
     `∫_E(∫_F 1_Δ dλ) d# = ∫_E 0 d# = 0` while `∫_F(∫_E 1_Δ d#) dλ = ∫_F 1 dλ = 1`.
     So `o ↦ ∫ p_θ(o,y|X) ν^Y_D(dy)` is not guaranteed to be a density of `P^O_{θ,X}` w.r.t. `ν^O_D`,
     which is precisely what 03:137 asserts.
  3. `(𝖸_D, 𝒴_D)` is then not standard Borel (the power set of an uncountable set is not countably
     generated), so the regular-conditional convention at 03:121 loses both existence and the
     a.s.-uniqueness at 03:135.
- **Fix.** "Each **at most countable** discrete coordinate carries its power-set sigma-algebra and
  counting base measure." One word.
- **Falsifies.** Nothing in the worked construction; this is a hypothesis-hygiene defect in a chapter
  whose stated purpose is hypothesis hygiene.

---

### P4 — Chapter 7 argues pointwise at a fixed `o` without the version declaration Chapter 3 requires

- **Claim / location.** `07_restrictions.tex:137-148`
  (`prop:restrict-conditional-precision-observation-free`, proof: "Read the exponent of the joint
  density as a function of `y` at fixed `o`") and `07_restrictions.tex:295-311` (the data-processing
  paragraph, which identifies the coarse conditional with `P_o K`).
- **Severity.** low
- **Status.** both `\status{ESTABLISHED}` (07:145, 07:311). Note that
  `prop:restrict-unrelated-joint-elbo` (07:259-261) *does* carry the qualifier — "Assume the selected
  `o` belongs to the regular-observation set of each joint, or that pointwise versions have been
  declared for both" — so the omission in the neighbouring results is an internal inconsistency, not
  a global oversight.
- **Evidence.**
  - For `prop:restrict-conditional-precision-observation-free` the pointwise reading is *repairable
    and true*: a nondegenerate joint Gaussian has an everywhere-positive continuous density, the
    evidence `p(o) > 0` for every `o`, and the density-ratio conditional of `eq:prob-rcp-density` is
    then defined and correct at every `o`. But 03:161 states that an "everywhere pointwise statement
    … requires a particular jointly measurable density, evidence representative, and
    regular-conditional version to be declared as part of the model data", and Chapter 7 never makes
    that declaration.
  - For the data-processing display, `o ↦ P_o K` is *a* version of the RCP of
    `P̄ = (id_O ⊗ K)_\# P` (checked: `P̄(A×B) = ∫_A (P_oK)(B) P^O(do)` by Tonelli), but it need not
    agree at a given `o` with the version selected by `eq:prob-rcp-density` applied to `P̄`. The
    displayed inequality is therefore a `P^O`-a.e. statement, not a pointwise one at "the selected
    `o`".
  - A third, smaller gap in the same chapter: nothing verifies that every member of
    `𝒬_𝔅` (`eq:restrict-block-family`) and `𝒬_B` (`eq:restrict-mean-family`) lies in the domain of
    `hyp:prob-regular-observation` before `eq:restrict-exact-identity` is applied to them. They do —
    nondegenerate Gaussians are mutually absolutely continuous and have finite log-moments — but the
    step is silent.
- **Fix.** One sentence at the head of `sec:restrict-observation`: *throughout this chapter the
  continuous everywhere-positive Gaussian density and the corresponding everywhere-defined
  conditional are the declared versions*, plus "for `P^O`-almost every `o`" on the data-processing
  display, plus one line verifying `𝒬_𝔅, 𝒬_B ⊆ dom(hyp:prob-regular-observation)`.
- **Falsifies.** No stated conclusion.

---

### N1 — the displayed determinant gap is evaluated in a cancellation-prone form; in fp64 it goes negative, violating the theorem's own inequality

- **Claim / location.** `eq:restrict-determinant-gap` (`07_restrictions.tex:92-98`),
  `eq:restrict-block-min-kl` (07:102-106), `eq:restrict-refinement` (07:221-228). All display the gap
  as `½[Σ_b log det J_bb − log det J] ≥ 0`. `verification/run_checks.py:1277-1288`
  (`factorization_gap`) implements exactly this form with `slogdet`.
- **Severity.** medium (numerical, not mathematical — the theorem is correct; I verified its proof
  and recomputed it, see §Recomputations)
- **Status.** `\status{ESTABLISHED}` (07:98, 07:229). No prose inflation; the theorem is true. What
  is missing is any statement that the displayed form is not the form to evaluate.
- **Evidence — executed sweep.** 6+6 block sizes, `J = [[A, C],[Cᵀ, D]]` with `A, D` spectrally
  conditioned to `κ` and `C = ε·randn·√λ_max(A)`, 300 SPD draws per cell, fp64,
  `numpy.linalg.slogdet`. Columns: number of draws whose *computed* gap is negative, and the most
  negative value.

  | κ(J) | ε | draws | neg (naive form) | worst naive | neg (stable form) | max abs difference |
  |---|---|---|---|---|---|---|
  | 1e4 | 1e-8 | 300 | 5 | -1.81e-13 | 0 | 4.12e-13 |
  | 1e4 | 1e-9 | 300 | 125 | -1.71e-13 | 0 | 1.77e-13 |
  | 1e8 | 1e-8 | 300 | 24 | -1.89e-09 | 0 | 3.27e-09 |
  | 1e8 | 1e-9 | 300 | 137 | -1.73e-09 | 0 | 1.74e-09 |
  | 1e12 | 1e-8 | 300 | 44 | -1.69e-05 | 0 | 4.36e-05 |
  | 1e12 | 1e-9 | 300 | 153 | -2.65e-05 | 0 | 2.66e-05 |
  | 1e14 | 1e-8 | 300 | 30 | **-2.30e-03** | 0 | 2.98e-03 |
  | 1e14 | 1e-9 | 300 | 142 | -2.04e-03 | 0 | 2.06e-03 |
  | 1e14 | 1e-10 | 300 | 141 | -1.57e-03 | 0 | 1.57e-03 |

  A separate scalar witness isolates the mechanism cleanly. For `J = [[1, ε],[ε, 1]]` with two
  singleton blocks, the true gap is `-½log(1-ε²) ≈ ε²/2`:

  | ε | true gap | fp64 `Σ log det J_bb − log det J` form |
  |---|---|---|
  | 1e-6 | 5.000000e-13 | 4.999889e-13 |
  | 1e-7 | 5.000000e-15 | 4.996004e-15 |
  | 1e-8 | 5.000000e-17 | 5.551115e-17 |
  | 3e-9 | 4.500000e-18 | **0.000000e+00** |
  | 1e-9 | 5.000000e-19 | **0.000000e+00** |

  Consequences that touch stated results:
  1. A numerically computed `ℒ*_𝔅` can *exceed* `log p_θ(o|X)` — the ELBO can appear above the
     evidence purely from roundoff, by up to 2.3e-3 in the tested regime.
  2. The equality condition of `thm:restrict-determinant-gap` ("equality if and only if `J_bc = 0`")
     and of `prop:restrict-refinement-monotonicity` ("vanishing exactly when `J_bb` is block
     diagonal") are not numerically decidable: coupling at `ε ≲ 1e-8` is indistinguishable from exact
     decoupling in fp64.
  3. `open:restrict-intrinsic-criterion` (07:313-327) asks for a functional over the partition
     lattice. Any implementation of such a search that scores partitions by the displayed gap has an
     fp64 noise floor of the magnitudes tabulated above, which exceeds the true gap for weak coupling.
  4. `CHK-CG-FACTOR-GAP` (`run_checks.py:1291`) tests `monotonicity` with
     `monotonicity_absolute: 1.0e-12` — an *absolute* threshold on a quantity whose roundoff scales
     with `|log det|`. Current observed `nested_partition_gaps` are `[1.3085, 1.2940, 1.2793,
     1.1634, 1.1483, 0.0]` on a `random_spd(rng, 8, 1.0)` draw, so the tolerance is never exercised;
     the sweep above shows it would fail on roundoff, not mathematics, at `κ ≳ 1e12`.
- **Fix.** Add a numerical remark to `sec:restrict-block` giving the algebraically equivalent stable
  form. For two blocks, `det J = det A · det(D − CᵀA⁻¹C)`, hence
  `gap = -½ log det(I − W)`, `W = D^{-1/2} CᵀA^{-1} C D^{-1/2} ⪰ 0`, evaluated as
  `-½ Σ_i log1p(-w_i)` on the eigenvalues `w_i` of `W`; inductively for more blocks. Verified above:
  this form returned a negative value in **0 of 3000+ draws** across the whole sweep, and agrees with
  the naive form to within the naive form's own error. Switch `factorization_gap` to it and make
  `monotonicity_absolute` relative.
- **Falsifies.** Nothing in the mathematics. Falsifies the implicit claim, carried by
  `appendix_numerical_provenance.tex:32-39` ("current deterministic, double-precision CPU
  implementations satisfy their declared finite checks"), that the encoded endpoints are robust
  outside the well-conditioned draws the suite happens to use.

---

### N2 — `CHK-RESTRICTION-SCHUR`'s positive-semidefiniteness threshold is absolute where the quantity's scale is `‖J‖`

- **Claim / location.** `07_restrictions.tex:200` ("The deterministic replacement check
  `CHK-RESTRICTION-SCHUR` independently reconstructs the block-inversion and constrained-optimization
  endpoints and includes the orthogonal equality control"),
  `prop:restrict-marginal-vs-restricted-precision` / `eq:restrict-marginal-vs-restricted` (07:181-198),
  implementation `run_checks.py:387-420`.
- **Severity.** low
- **Status.** `\status{NUMERICAL}` (07:200) for the check sentence; `\status{ESTABLISHED}` (07:189)
  for the proposition. **I adversarially tested and then withdrew** a stronger version of this
  finding: I initially judged `closed_cost == direct_cost` circular, since both derive from the same
  formula. It is not. Substituting the restricted precision `B_⊥ᵀJB_⊥` for the marginal precision
  `(B_⊥ᵀJ⁻¹B_⊥)⁻¹` — the exact substitution 07:199-200 warns against — breaks *both* tested
  conditions: `|closed − direct| = 4.81e+01` (vs 4.44e-15 for the correct matrix) and feasibility
  `‖B_⊥ᵀμ*‖ = 4.34e+00` (vs 3.89e-16). The check does discriminate. The residual finding is only
  about tolerance scaling.
- **Evidence.** Sweep over `κ(J) ∈ {1e2, …, 1e16}`, `n = 9`, `r = 4`, fp64:

  | κ(J) | rel. Frobenius residual of `eq:restrict-marginal-vs-restricted` | min eig(gap) | max eig(gap) | numerical rank | passes suite's `1e-11` relative tol | passes suite's `-1e-10` absolute PSD tol |
  |---|---|---|---|---|---|---|
  | 1e2 | 1.57e-15 | -9.48e-15 | 5.02e+01 | 4 | yes | yes |
  | 1e6 | 3.61e-14 | 2.60e-10 | 8.55e+05 | 4 | yes | yes |
  | 1e10 | 5.08e-13 | 2.05e-07 | 8.41e+09 | 4 | yes | yes |
  | 1e12 | 1.09e-12 | 1.50e-05 | 2.96e+11 | 4 | yes | yes |
  | 1e14 | 6.16e-12 | **-5.88e-04** | 5.98e+13 | 4 | **yes** | **NO** |
  | 1e16 | 1.71e-12 | 2.27e-01 | 6.73e+15 | 4 | yes | yes |

  At `κ = 1e14` the min eigenvalue is `-5.88e-04` — but relative to `λ_max = 5.98e13` that is
  `-9.8e-18 ≈ -eps/2`, i.e. pure roundoff. The identity residual (relative) passes at 6.16e-12 while
  the PSD control (absolute) fails by seven orders of magnitude. The two tolerances in the same check
  scale differently. The suite's actual draw is `random_spd(rng, 9, 0.5)` with `κ(J) = 29.58`,
  `λ_min = 0.9245`, so nothing near this regime is exercised; recorded observed values are
  `schur_identity_relative_residual: 7.43e-16`, `gap_minimum_eigenvalue: 4.03e-16`.
- **Fix.** Replace `gap_eig.min() >= -1.0e-10` by `gap_eig.min() >= -1.0e-12 * max(gap_eig.max(),
  ‖J‖₂)`, and either add an ill-conditioned draw or state in `claims.json` that the endpoint is
  certified only for `κ(J) = O(10)`.
- **Falsifies.** Nothing in `prop:restrict-marginal-vs-restricted-precision`, which I recomputed and
  which holds exactly (see §Recomputations).

---

### N3 — the committed results artifact did not bind the committed sources, and nothing can detect that

- **Claim / location.** `appendix_numerical_provenance.tex:41-47`: "The result artifact records
  interpreter and dependency versions and **binds the discovered manuscript sources and verification
  protocol by SHA-256. Any source, protocol, input, dependency, or environment change requires a new
  run before the numerical evidence is current.**" `verification/VERIFICATION.md:46-51`.
- **Severity.** medium (reproducibility statement)
- **Status.** untagged prose in the provenance appendix; the whole `\status{NUMERICAL}` class rests
  on it.
- **Evidence.** Running the declared command rewrote the committed
  `verification/current-results.json`:

  ```
  $ git diff --stat manuscripts/gauge_vfe_rg/verification/
   .../verification/current-results.json | 56 +++++++++++-----------
   1 file changed, 28 insertions(+), 28 deletions(-)
  ```

  All 28 changed pairs are `byte_count` / `sha256` entries inside `inventory_manifest.tex_sources`,
  covering 14 files: `01_introduction`, `02_geometry`, `05b_local_collective_elbo`,
  `05c_pullback_geometry`, `05d_relational_inference`, `06_general_coarsegraining`,
  `07_general_renormalization`, `07b_agent_network_rg`, `08_infogeometry`, `09_coarsegraining`,
  `12_philosophy`, `appendix_claim_ledger`, `appendix_notation`, `main`. Example:
  `01_introduction.tex` recorded `byte_count 11181 / sha 5a7c671c…`; the file in the tree is
  `11224 / 2237a429…`. Every `checks[*]` result, every `source_line` and every disposition was
  byte-identical before and after — so the *results* were current while the *binding* was not.

  Two structural reasons this cannot be caught:
  1. `run_checks.py` recomputes `inventory_manifest` from disk on every run
     (`main()`, `run_checks.py:2279-2292`) and writes it out. It never compares against the
     previously stored manifest. The only CLI flag is `--output` (`parse_args`,
     `run_checks.py:2261-2269`). A stale committed artifact therefore always "passes".
  2. The artifact records no run timestamp and no git revision — `environment` holds only
     `python`, `python_executable`, `platform`, `machine`, `numpy`, `scipy`, `sympy`, `float_info`.
     Staleness is undetectable from the artifact alone.
- **Fix.** Add `--verify` (recompute the manifest, diff it against the stored one, exit nonzero on
  any difference) and wire it into the build; add `run_timestamp_utc` and `git_rev` (plus dirty-tree
  flag) to `environment`. Then the appendix's freshness sentence becomes a mechanically enforced
  contract instead of a stated intention.
- **Falsifies.** Not the check results — the current run is `PASS 29 / FAIL 0 / INCONCLUSIVE 0`.
  It falsifies the appendix's implicit claim that the SHA-256 binding makes the numerical evidence
  self-certifying against source drift.

---

### N4 — typo, `eq:prob-generative-density`

`03_probability.tex:107` writes `P_\theta(do,dY\given X) = p_\theta(o,y\given X)\nu^{O}_{D}(do)\nu^{Y}_{D}(dy)`
— capital `dY` on the left, lowercase `y`/`dy` on the right. Severity low, `\status{DEFINITION}`.
Fix: `dy`.

---

## Recomputations (everything load-bearing in Chapter 7, recomputed from scratch)

All independent of `run_checks.py`; fp64; scripts under the session scratchpad.

| Claim | Location | Independent check | Result |
|---|---|---|---|
| `prop:restrict-nonnested-unordered` displayed numbers | 07:242 | closed form at `(a,b)=(0.8,0.2)` | `0.0588915178` and `0.5493061443` — manuscript's `0.0589`/`0.5493` **confirmed**; exchanged at `(0.2,0.8)` **confirmed**; `det J = 0.32`, `κ(J) = 10.40` |
| `thm:restrict-exact-block-optimum` | 07:54-63 | Nelder-Mead + BFGS over `(μ_Q, {chol C_b})`, `n=9`, blocks 4/3/2, 6 restarts | numeric min KL `1.888277650420` vs closed `1.888277650420`, diff **7.1e-15**; `‖μ_num − μ‖_∞ = 2.6e-08`; `‖C_num − J_bb^{-1}‖_F/‖J_bb^{-1}‖_F ∈ {2.8e-08, 4.7e-08, 2.6e-08}` |
| `thm:restrict-determinant-gap` | 07:90-98 | same run | closed-form gap equals numerically minimized KL to 7.1e-15 |
| `prop:restrict-optimum-vs-marginal` | 07:116-122 | `λ_min((J^{-1})_bb − J_bb^{-1})` for 3 blocks, `κ(J)=65.4` | `1.21e-02`, `7.43e-03`, `3.60e-02` — all `> 0`, Loewner order **confirmed**; block-diagonal equality control: max abs difference `5.6e-17` |
| `prop:restrict-mean-cost` | 07:158-173 | L-BFGS-B + BFGS over `(α ∈ ℝ^r, chol C_Q ∈ ℝ^{n(n+1)/2})`, 4 restarts — a genuine optimizer, which the suite does not run | numeric min `6.925441470681` vs closed `6.925441470681`, diff **9.8e-15**; `‖B_⊥ᵀμ*‖ = 3.3e-16`; `‖μ_num − μ*‖_∞ = 3.9e-08` |
| `prop:restrict-marginal-vs-restricted-precision` | 07:181-189 | Schur identity, spectrum, rank | rel. residual **5.9e-16**; gap eigenvalues `[9.4e-16, 0.4416, 1.8535, 4.6243, 14.794]`; numerical rank 4 = `r` |
| wrong-matrix control (the substitution 07:199 forbids) | 07:199-200 | substitute `B_⊥ᵀJB_⊥` for `(B_⊥ᵀJ^{-1}B_⊥)^{-1}` | cost `18.078` vs correct `4.965`; overstates by `13.11`; feasibility residual `4.34` — the manuscript's warning is quantitatively right |
| `cor:restrict-combined-costs-add` | 07:202-209 | joint numeric minimization over both restrictions | numeric `8.8137191211` vs closed `8.8137191211`, diff **1.1e-14** |
| `prop:restrict-refinement-monotonicity` | 07:219-229 | exhaustive: all 52 partitions of 5 coordinates, all 358 refinement pairs | 0 violations; min difference `0.0` (attained at `p2 = p1`); trivial-partition gap `0.0`; lattice maximum `1.035477` at the all-singleton partition |
| `prop:restrict-gap-no-selection` | 07:249-250 | same lattice enumeration | gap minimized at the one-block partition, value `0.0` — **confirmed** |
| `prop:restrict-unrelated-joint-elbo` witness | 07:271-293 | exact evaluation of both parameter pairs | `(-1,0)`: mass `1.000000000000`, `log Ev = -1`, `KL = 0`, `ELBO* = -1`; `(0,2)`: `log Ev = 0`, `KL = 2`, `ELBO* = -2` → `ELBO₁ > ELBO₂` while `ℓ₁ < ℓ₂` **confirmed**. `(0,1)` vs `(-2,0)`: `ELBO* = -1` vs `-2` with `g₁ = 1 > g₂ = 0` **confirmed** |
| `CHK-RESTRICTION-SCHUR` endpoint | `run_checks.py:387` | reproduced the suite's own `closed_cost` by regenerating its exact rng stream | `4.9645321953` — matches recorded `closed_cost: 4.964532195333737` |

Proofs I checked line by line and found correct: `prop:prob-mixed-coordinate-dominating-measure`
(03:96), `prop:prob-density-absolute-continuity` (03:212), `prop:prob-marginals-do-not-determine-joint`
(03:264), `prop:prob-compatibility-nonidentifiability` (03:291), the `O^reg` / `eq:prob-rcp-density`
construction (03:137-150, including that `Π(o,·)` is a probability measure for each `o ∈ O^reg`, that
`o ↦ Π(o,B)` is measurable, and that `P(A×B) = ∫_A Π(o,B) P^O(do)`), the version counterexample at
03:151-161, `prop:restrict-gaussian-reverse-kl`, `thm:restrict-exact-block-optimum`,
`thm:restrict-determinant-gap` (both lemmas and the induction),
`prop:restrict-conditional-precision-observation-free`, `prop:restrict-mean-cost`,
`cor:restrict-mean-cost-data` (the "if and only if `B_⊥ᵀJ^{-1}𝒥_{Yo} = 0`" is correct because
`(B_⊥ᵀJ^{-1}B_⊥)^{-1} ≻ 0`), `prop:restrict-marginal-vs-restricted-precision`,
`cor:restrict-combined-costs-add`, `prop:restrict-refinement-monotonicity`,
`prop:restrict-unrelated-joint-elbo`, and the data-processing display at 07:301-306.

Cross-reference audit of both chapters: every `\Cref`/`\eqref` target in `03_probability.tex` and
`07_restrictions.tex` resolves to a definition in the source tree (`prop:restrict-principle` →
`05_elbo.tex:213`; `eq:restrict-exact-identity` → `05_elbo.tex:210`; `eq:restrict-sup-identity` →
`05_elbo.tex:220`; `prop:gauss-conditional-precision` → `06_gaussian.tex:56`;
`def:geo-principal-systems` → `02_geometry.tex:40`; `def:geo-graph-links` → `02_geometry.tex:527`).
No undefined symbol found in either chapter.

## Things I checked and deliberately do **not** report

- The `\mathcal L^{\rm ext}` carry-over candidate is in `06_general_coarsegraining.tex`, outside my
  chapters.
- The a.e.-`o` qualifier for optimization over an uncountable parameter space is **already handled**
  explicitly at `05_elbo.tex:186` ("An optimization over an uncountable parameter space requires
  either a common full-measure set proved for that family or jointly measurable pointwise density and
  conditional versions declared as part of the parameterized model"). Not a finding.
- The standard-Borel hypothesis at 03:121 is, in the dominated setting the manuscript actually uses,
  redundant for *existence* of the RCP (the density construction at 03:137-150 supplies one directly)
  and is needed only for the a.s.-*uniqueness* at 03:135, which requires the σ-algebra to be
  countably generated. Stating the stronger hypothesis is harmless, so this is a note, not a finding.
- R08, R13 and R20 (version dependence of the pointwise posterior; proper-support subsets;
  `prop:prob-density-absolute-continuity` misapplication) are settled ground, and 03:151-161 and
  03:214-221 now handle all three correctly in the current text.
