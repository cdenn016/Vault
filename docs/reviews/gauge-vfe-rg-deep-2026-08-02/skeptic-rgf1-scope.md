# Adversarial skeptic B — scope adjudication of RG-F1

**Target of the finding.** `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex:756-777`
(`eq:rg-linearized-action` and the classification sentence at `:771-774`).

**Angle.** Reachability within the claim's stated scope. I assume RG-F1's algebra is correct:
`D_H\mathcal R_b^H` is a positive unital averaging operator, spectral radius exactly 1, so no
bounded eigenoperator has `y_a > 0`. I attack only whether that is a *defect* the manuscript
commits, and whether it is reachable given the settled ledger and the manuscript's own declared
obligations.

**Verdict: REFUTED as stated and as a defect.** The residue is real but is an enhancement plus one
LOW tagging item, not a CRITICAL finding. Details and decisive text below.

---

## 1. Text freshness — the settled-ground exception does not apply

The lines under attack have not moved since the commit that produced the RG-2 verification.

```
$ git diff --stat a997a60 HEAD -- manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex
 1 file changed, 9 insertions(+), 6 deletions(-)
```

The entire diff is confined to `07b:549-562` (the path-space section heading and its first
paragraph). Lines `749-806` are byte-identical to the verified revision. So `00-settled-ground.md:3-5`
("Do not re-raise … unless the manuscript text touching it has changed") is in force, and RG-F1
gets no freshness exemption.

`a997a60` is the commit that added `07b`; the ledger's recorded `artifact_revision`
`git:e4377537e2ef2c0b7d23e17157ee041d0a0d9e95` resolves to `e437753`, the commit immediately
*preceding* it (the base revision at which verification started).

## 2. Settled-ledger collision with RG-2 — partial, and RG-F1 does not contradict it

RG-2's verified statement (`.verification/local-global-rg-ledger.json`, `EVIDENCE_VERIFIED`,
severity high) reads:

> "Under the displayed equivariance, integrability, positivity, lumpability-or-path-space, and
> semigroup hypotheses, the construction supplies composable gauge-covariant cross-scale operators,
> exact meta-attention, reference-dependent action and attention beta functions, and exhaustive
> invariant measure-pair fixed-point equations."

The *statement* does not mention linearization or exponent classification. But its evidence range
does: `RG-2-e1 = manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex:243-804`, which contains
`756-777` outright. And the closure report the ledger points at is explicit:

- `docs/reviews/gauge-vfe-rg-local-global-rg-2026-08-01/02-construction-and-adversarial-verification.md:190`
  — "Linearization is valid on the positive finite coarse-likelihood domain; infinite-dimensional
  scaling uses the full spectrum and spectral radius, with eigenoperators only for point spectrum."
- `…:209` — "Round-four closure verdicts were PASS after repair for: … positive-likelihood
  linearization; weak-lumpability qualification; **full-spectrum scaling**; and the finite
  arbitrary-graph closure theorem."
- `…:203` — the adversarial candidate set included "The strongest covariance, **averaging**, memory,
  moving-reference, or fixed-point objection."

So the lines were inside a verified, adversarially-tested range, and an averaging objection was on
the docket.

That said, RG-F1 does **not** contradict RG-2. RG-F1 concedes the derivative formula is exact
(`lens-rg.md:28-29`, residuals `1.25e-10` and `4.86e-08`), and it does not dispute that the full
spectrum is the right object. It adds a *new theorem about the same operator*. A strengthening is
not a contradiction. The collision is therefore not fatal on its own — but it does raise the bar:
a finding on lines already PASSed for "full-spectrum scaling" must show the manuscript asserts
something false, not merely that it omits something true.

## 3. The manuscript does not assert the relevant branch is occupied — this is the decisive point

Verbatim, `07b:768-777`:

> "On an infinite-dimensional Banach or Hilbert action space, growth is classified by the full
> spectrum and spectral radius of this derivative, including continuous and residual spectrum. For
> an isolated eigenoperator satisfying `D_H\mathcal R_b^H[\psi_a] = \lambda_a\psi_a`, the exponent
> `y_a=\log|\lambda_a|/\log b` is relevant, marginal, or irrelevant according as it is positive,
> zero, or negative; the sign or complex phase is retained. Generalized eigenspaces are used only
> in finite dimensions or for isolated point spectrum with the requisite spectral projections."

Four sentences, parsed:

| Sentence | Logical form | Does it assert `y_a>0` exists? |
|---|---|---|
| Two variations (`:760-767`) | proved identity | no — and RG-F1 verifies it |
| "growth is classified by the full spectrum … including continuous and residual spectrum" | a **restriction**: do not read growth off eigenvalues alone in infinite dimensions | no |
| "For an isolated eigenoperator satisfying …, the exponent … is relevant, marginal, or irrelevant according as it is positive, zero, or negative" | conditional naming convention; "according as" is definitional grammar; no existential quantifier | **no** |
| "Generalized eigenspaces are used only in finite dimensions or for isolated point spectrum …" | a **restriction** | no |

Three of the four are restrictive cautions and the fourth is a naming convention. The passage
defines a trichotomy and asserts nothing about which cases occur. RG-F1's own severity rationale
(`lens-rg.md:62-64`) claims the text "assert[s] that the `y_a > 0` branch is inhabited." It does
not, and no reading of the printed grammar produces that assertion.

**Corroboration 1 — the one place the trichotomy is applied to a concrete object is tagged OPEN.**
`05a_expfamily.tex:264-267`:

> "The pin changes the family, may change the fixed set, and introduces a parameter whose removal
> need not commute with the long-scale limit. Whether the mass sector is relevant, marginal, or
> irrelevant is an open spectral question for the declared scale map. `\status{OPEN}`"

restated in the manuscript's own ledger at `appendix_claim_ledger.tex:28-34`: "determine whether a
positive mass pin is relevant, marginal, or irrelevant under that map. `\status{OPEN}`".

**Corroboration 2 — the classification is never used.** A whole-manuscript grep finds `y_a` at
exactly two locations (`07:412`, `07b:772`) and `\lambda_a` at exactly one (`07b:772`). No exponent
is computed anywhere, for any sector — which `lens-rg.md:645-650` itself concedes. The two
downstream references to `eq:rg-linearized-action` are `07b:805` (a hedge, quoted below) and
`07b:866-868` (a corollary hypothesis naming the admissible perturbation class). Nothing in the
manuscript depends on a relevant direction existing. A vocabulary defined once and applied zero
times cannot carry CRITICAL severity.

**Corroboration 3 — the surrounding prose deflates, it does not inflate.** `07b:801-806`:

> "Along every exact coarse path, `eq:rg-vfe-chain-rule` makes the recognition gap nonincreasing and
> the ELBO nondecreasing at fixed evidence. This monotone flow is information loss under resolution,
> **not a proof of approach to a nontrivial critical fixed point.** Attraction requires spectral
> control of `eq:rg-linearized-action` on the declared common space."

and `07b:779-780`: "The equations characterize all fixed points without claiming that every model
class admits a closed-form enumeration."

The manuscript states, on the page RG-F1 attacks, that its flow is not a proof of approach to a
critical fixed point, and it names spectral control of the very equation in question as the missing
ingredient. RG-F1's theorem *supplies* that spectral control. That is the manuscript asking for the
result, not concealing it.

## 4. The "asymptotic vocabulary attached where the phenomena cannot occur" charge is overstated

Actual counts across the manuscript:

- **"criticality":** zero occurrences.
- **"critical fixed point":** one occurrence, `07b:804`, inside a disclaimer.
- **"universality":** zero occurrences in `07b`. In `07` it appears at `07:420-425` under
  `\status{HYPOTHESIS}` ("Their existence, convergence, and completeness must be proved in the
  chosen realization. Universality is a statement about basins and invariant observables, not
  algebraic closure alone.") and at `07:585-586` ("Fixed points, universality, and continuum laws
  are meaningful only after these types and limits have been declared."). In `10` it appears at
  `10:391`, immediately after `\status{OPEN}` at `10:389`, inside a negative statement ("Equality
  of one exponent is not equality of universality classes").
- **"relevant/marginal/irrelevant" as an RG classification:** two occurrences, `07b:772-773` (the
  definition) and `appendix_claim_ledger.tex:33` (an `\status{OPEN}` item).
- **Finite-graph exponents are explicitly refused:** `10:383-389` — "A cumulative exponent
  `N(t)-N(0)\sim Ct^\alpha` is meaningful only after proving convergence `N_n\to N` in a stated
  mode. **A fixed finite graph has an atomic measure, so a density exponent is not defined there.**
  … `\status{OPEN}`".

Status-tag census in the three RG chapters:

| File | ESTABLISHED | DEFINITION | HYPOTHESIS | OPEN | NOT-CLAIMED | CONJECTURE |
|---|---|---|---|---|---|---|
| `07_general_renormalization.tex` | 14 | 8 | 3 | 4 | 1 | 0 |
| `07b_agent_network_rg.tex` | 36 | 0 | 0 | 0 | 0 | 0 |
| `10_renormalization.tex` | 18 | 2 | 0 | 5 | 1 | 1 |

Every claim in chapters 7 and 10 that touches exponents, universality, or thermodynamic limits
carries `OPEN` or `HYPOTHESIS`. Chapter 7b carries no non-`ESTABLISHED` tags at all, but it defers
its infinite-volume obligations in prose and by cross-reference at `07b:894-896`: "Existence and
uniqueness of a thermodynamic DLR state, convergence of free-energy densities, and interchange of
volume and RG limits remain the separate open obligations recorded in `\Cref{app:claim-ledger}`."

## 5. Declared open obligations already fence the substance

`appendix_claim_ledger.tex:66-71`, **Infinite-volume RG limit (open)** — this is exactly where
RG-F1's own counterexample places the missing relevant direction. RG-F1 item 5
(`lens-rg.md:115-118`) states that the relevant eigenvalue `b^{1-n/2}` appears "only for the
*extensive* perturbation `\varphi=\sum_{i=1}^b He_n(y_i)`", and that "On the common space required to
make `K_b` an endomorphism (the infinite sequence space), that `\varphi` does not converge." That is
the infinite-volume sector, declared OPEN.

`appendix_claim_ledger.tex:73-77`, **Two-index limits and universality (open)** — "A finite
congruence identity or one matched exponent is insufficient." This fences exponent matching and
universality, which is the second half of RG-F1's consequence paragraph.

Settled ground **R04** (`00-settled-ground.md:20-21`, pass-1 `EVIDENCE_VERIFIED`) — "A finite
generalized spectrum is atomic and cannot carry an ordinary low-`d` spectral density or exponent
without a declared thermodynamic limiting measure." The general proposition "a finite construction
cannot exhibit asymptotic scaling phenomena" is already adjudicated and already answered by the
manuscript at `10:385`.

Per `00-settled-ground.md:118-120`, "An obligation the manuscript itself declares OPEN or CONJECTURE
is not a finding." RG-F1's consequence claim restates three disclosed limitations.

## 6. The status tag does not support the severity

`SPEC.md:66-72` defines the register. `ESTABLISHED` = "Proved here, or a standard result cited to a
source that has been checked." `DEFINITION` = "A declared type, construction, or convention. Nothing
is being proved and the text says so."

The `\status{ESTABLISHED}` at `07b:777` governs a paragraph whose load-bearing content is the two
variations, and those are proved — the proof is at `07b:873-879` ("dominated differentiation under
the conditional partition gives the first two variations") and RG-F1 independently confirms them.
The trichotomy appendage is a convention and should carry `DEFINITION`. That is a real mistag, and
it is LOW: it is one instance of a chapter-wide pattern (7b has 36 `ESTABLISHED` and zero
`DEFINITION` tags), not a claim of a proof that does not exist.

The in-scope list at `00-settled-ground.md:131-135` admits six categories. RG-F1 as stated matches
none of them:

| In-scope category | RG-F1? |
|---|---|
| proof wrong, circular, or incomplete | no — the proof is of the two variations, and it holds |
| hypotheses do not support the stated conclusion | no — the conclusion is a naming convention |
| definition used before it is given | no |
| symbol never defined | no (the `\psi_A`/`\psi_a` clash is RG-F7, LOW) |
| internal inconsistency between chapters | no — RG-F1 item 6 shows `07:410-414` and `07b:772` *agree*, and gives the reason |
| status inflation, prose asserts more than the tag licenses | **no — the prose asserts less**, see §3 |

## 7. One point I checked that would have saved the finding, and did not

RG-F1 item 6 (`lens-rg.md:124-127`) notes that `eq:rg-projective-dimensions` (`07:410-414`) defines
`y_a=\log|\mu_a/\mu_0|/\log b` — a *projective* exponent, quotiented by the radial eigenvalue —
whereas `07b:772` uses the absolute `\log|\lambda_a|/\log b`. I looked for an internal
inconsistency there. There is none, and the reason cuts against the finding: `07:407-418` sets the
convention "For a differentiable homogeneous positive endomorphism at a fixed ray, let `\mu_0` be
the radial eigenvalue … They are invariant under smooth coordinate conjugacy at the ray **once
gauge, normalization, and other redundant directions have been quotiented**." Quotienting the
radial/normalization direction of a positive homogeneous map is precisely the standard handling of
the unitality RG-F1 identifies. The manuscript's ch-7 convention already encodes it — as RG-F1
itself observes ("So the ch-7 convention *already* encodes the conclusion"). A convention that
already encodes the conclusion is not blind to it.

`eq:rg-projective-dimensions` is defined once and cross-referenced nowhere, so no downstream claim
rides on either definition.

## 8. What should survive, and where it belongs

Not zero. Two items, both non-critical:

1. **Missing structural theorem (enhancement, LOW, not a defect).** `\mathcal R_b^H` is order
   preserving and additively homogeneous, hence sup-norm nonexpansive (Crandall–Tartar);
   `D_H\mathcal R_b^H` is positive and unital with spectral radius exactly 1 and always carries the
   eigenvalue 1 on constants. The manuscript should state this, because `07b:805` explicitly names
   "spectral control of `eq:rg-linearized-action` on the declared common space" as what attraction
   requires and then does not supply it. This is the manuscript understating what its own
   construction proves — an omission of a true result, which is not among the six in-scope defect
   categories.
2. **Definitional mistag (LOW).** The trichotomy at `07b:771-774` is a `DEFINITION` carrying
   `ESTABLISHED`. Fold into a chapter-7b tagging note, alongside the `\psi_A`/`\psi_a` clash already
   filed as RG-F7.

Neither justifies "the classification is provably empty, therefore CRITICAL." Both are worth a
paragraph of revision.

## 9. Verdict

**REFUTED** as stated and at the stated severity.

- The algebra is granted and is not in dispute.
- The manuscript nowhere asserts the `y_a>0` branch is inhabited; it defines a trichotomy and
  applies it to nothing (`07b:771-774`), and the single applied instance is tagged `\status{OPEN}`
  (`05a:266`, `appendix_claim_ledger.tex:33`).
- The "prose inflates" charge is contradicted by `07b:801-806`, `07:585-586`, and `10:383-389`.
- "Criticality" and "universality" appear zero times in chapter 7b; elsewhere they are `HYPOTHESIS`,
  `OPEN`, or negations.
- The consequence claim restates the disclosed obligations at `appendix_claim_ledger.tex:66-71` and
  `:73-77` and duplicates settled `R04`.
- `y_a` is never computed and never used downstream, so nothing in the artifact depends on the
  branch being inhabited.

Re-file the salvageable content as a LOW-severity enhancement (state the unitality/nonexpansiveness
theorem, which answers the question `07b:805` poses) plus a LOW tagging item. Drop the CRITICAL
finding.
