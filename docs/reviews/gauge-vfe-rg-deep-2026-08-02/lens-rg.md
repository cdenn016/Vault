# Lens review — renormalization group / statistical field theory

Reviewer lens: RG. Artifact: `manuscripts/gauge_vfe_rg/` at working-tree revision of 2026-08-02
(`07_general_renormalization.tex`, `07b_agent_network_rg.tex`, `10_renormalization.tex` as read).
Settled ground (`00-settled-ground.md`) honored: R01–R21, FINAL-01…08, LG-1/2, RG-1/2, PB-1…4 and
every `appendix_claim_ledger.tex` OPEN/CONJECTURE item are treated as out of scope. In particular
this review does **not** re-raise the infinite-volume limit, two-index limits/universality, the
Bayesian-RG bridge, scalarized attraction, or "composition holds under the displayed semigroup
hypothesis" (RG-2). It attacks the hypotheses those entries rest on and the steps between them.

Recomputation script: `C:/Users/CHRISA~1/AppData/Local/Temp/claude/C--Users-chris-and-christine-Desktop-Research/21b92b09-6f32-47fa-8f90-6f5faa59e5a3/scratchpad/rg_checks.py` and `C:/Users/CHRISA~1/AppData/Local/Temp/claude/C--Users-chris-and-christine-Desktop-Research/21b92b09-6f32-47fa-8f90-6f5faa59e5a3/scratchpad/ref_change.py`
(`C:/Python314/python.exe`, numpy 2.4.4 / sympy 1.14.0, seed 20260802). Every residual quoted below
is machine output, not recollection.

---

## 0. What recomputed clean (adversarial baseline)

Before the findings, the negative result: I tried to break the following and could not. These are
correct as written and are **not** findings.

| Claim | Location | Residual |
|---|---|---|
| Hard aggregation: `S^T Λ S` equals the parameter formula | `10:31-42` `eq:grg-aggregation` | `3.55e-15` |
| Aggregation semigroup `A_{S2}A_{S1} = A_{S1S2}` | `10:49-59` | `3.55e-15` |
| Equal-block spectral bounds `bλ_min ≤ λ_min(S^TΛS) ≤ λ_max(S^TΛS) ≤ bλ_max` | `10:85-101` | holds (2.22 ≤ 2.32; 33.21 ≤ 44.39) |
| Homogeneous complete graph `A↦bA`, `W↦b²W`; sector gap `1/b` | `10:144-149`, `10:270-280` | `0.0`, `1.78e-15` |
| `D_H R_b^H[φ] = E_{Π_*}[φ | Z=z]` (first variation) | `07b:761-762` | `1.25e-10` (central difference) |
| `D_H² R_b^H[φ,φ] = −Var_{Π_*}(φ)` (second variation) | `07b:764-766` | `4.86e-08` (second difference) |
| Ising-star cubic coefficient `2 sech²(h₀)tanh(h₀)J₁J₂J₃ + O(J⁵)` | `07b:180-190` | sympy difference **exactly 0**; `t⁴` coefficient **exactly 0** |
| Replicator beta `β̇_J = β_J(u_J − Σβ_K u_K)` with the displayed `u_J` | `07b:697-702` | sympy residual **exactly 0** for all `J` |
| Möbius inversion `H = Σ_A Φ_A` | `07b:157-168` | `2.22e-15` |
| Nested compositions `C^{12}C^{01}=C^{02}`, `P^{01}P^{12}=P^{02}`, `CP=I` | `07b:320-332` | `2.2e-16`, `4.97e-14`, `1.78e-15` |
| Mori–Zwanzig memory operators `CTQ(QTQ)^n QTP` + initial-noise term | `07b:577-597` | rederived symbolically; formula exact |
| `β̇_{IJ}=(η̇_{IJ}−β_{IJ}α̇_I)/α_I`; log-sum-exp `π^c_J e^{−E^c_J/τ}=Σ_{j∈J}π_j e^{−E_j/τ}` | `07b:689-692`, `07b:444-450` | exact |
| Mass-pencil transfer `d=λ/(λ+a)`, counting transfer, `Λ≻0` criterion | `10:337-361`, `10:314-330` | exact |
| `β'(g') = (1/c)Df(g)β(g)`; heat/entropy `−dS/dlog t = t²Var_t(λ) → α` | `07:396-402`, `07:468-483` | rederived; exact |
| Alternating-cocycle counterexample `BA = [[3,2],[4,3]]`, Perron ray `[1,√2]`, odd ray `A[1,√2]` distinct | `07:365-380` | verified |

So the manuscript's *algebra* is sound. The findings below are structural: they concern what the
constructed objects can and cannot be, not arithmetic slips.

---

## FINDING RG-F1 — **CRITICAL** — the linearized RG operator is a unital averaging operator, so the "relevant" branch of the exponent classification is empty

**Claim under review.** `07b:756-777` (`eq:rg-linearized-action` and the sentence following it):
after giving `D_H R_b^H|_{(H_*,ρ_*)}[φ](z) = E_{Π_*(dy|z)}φ(Y)`, the text states

> "On an infinite-dimensional Banach or Hilbert action space, growth is classified by the full
> spectrum and spectral radius of this derivative… For an isolated eigenoperator satisfying
> `D_H R_b^H[ψ_a] = λ_a ψ_a`, the exponent `y_a = log|λ_a|/log b` is relevant, marginal, or
> irrelevant according as it is positive, zero, or negative"

**Location.** `07b_agent_network_rg.tex:756-777`; corollary hypothesis at `07b:866-868`; the
declared perturbation class ("bounded perturbations `φ ∈ L^∞` (or, more generally, perturbations
with conditional exponential integrability…)") at `07b:756-759`.

**Severity.** critical.

**Status.** `\status{ESTABLISHED}` at `07b:777` and again inside
`cor:rg-complete-analytic-tier` (`07b:871`). **Prose inflates**: the three-way classification and
the phrase "growth is classified by the full spectrum and spectral radius" assert that the
`y_a > 0` branch is inhabited. It is not.

**Evidence (recomputation).**

1. *Unconditional structural fact.* For **any** nonnegative kernel `K_b` (Markov or not) and any
   `H_*` with `0 < L^c_*(z) < ∞` (the manuscript's own
   `eq:rg-linearization-positive-likelihood`, `07b:749-754`), the displayed derivative is
   ```
   D_H R_b^H[φ](z) = ∫ φ(y) Π_*(dy|z),   Π_*(dy|z) = e^{−H_*(y)}Λ_z(dy) / ∫e^{−H_*}dΛ_z
   ```
   with `Π_*(·|z)` a **probability measure** for every `z`. Hence the operator is positive and
   **unital**: `D_H R_b^H[1] = 1`. Equivalently — and this is the same fact one line up —
   `R_b^H[H+c] = R_b^H[H] + c` for every constant `c`, which follows immediately from
   `e^{−(H+c)}ρ = e^{−c}(e^{−H}ρ)` and cancellation of `e^{−c}` in the Radon–Nikodym ratio.
   Verified: `||R[H+1.7] − R[H] − 1.7||_∞ = 4.44e-16` (check F).
2. *Numerical confirmation of unitality and of the spectrum.* Finite common space `n = 6`, random
   Markov `K_b`, invariant `ρ_*` (invariance residual `1.94e-16`):
   ```
   row sums of D_H R^H  = [1. 1. 1. 1. 1. 1.]
   eigenvalues          = −0.2704, −0.0342, 0.0443±0.1451i, 0.2003, 1.0000
   spectral radius      = 1.0000000000000002
   y_a = log|λ|/log 2   = [0.000, −1.887, −2.320, −2.721, −2.721, −4.872]
   ```
   Exactly one exponent is zero (the constants), every other is strictly negative, **none is
   positive**.
3. *Global, not just local.* `R_b^H` is order preserving (`H₁ ≤ H₂ ⟹ e^{−H₁} ≥ e^{−H₂} ⟹
   E[e^{−H₁}|Z] ≥ E[e^{−H₂}|Z] ⟹ R[H₁] ≤ R[H₂]`) and additively homogeneous. By Crandall–Tartar
   (order preserving + additively homogeneous ⟹ sup-norm nonexpansive) the *whole flow*, not just
   its linearization, is a nonexpansion. Verified over 4000 random pairs:
   `max(||R[H₁]−R[H₂]||_∞ − ||H₁−H₂||_∞) = 0.0` (attained, never positive).
4. *So no admissible eigenoperator can be relevant.* On `L^∞` (the declared class),
   `||D_H R_b^H||_{∞→∞} = 1`, hence every eigenvalue satisfies `|λ_a| ≤ 1` and `y_a ≤ 0`. If
   `K_b` is Markov (which the chapter requires elsewhere — see RG-F4), then at a fixed pair
   `π_* = m_*/Z(o)` is invariant for the reverse kernel `Π_*(dy|z)` (I verified `π_* K_b = π_*`
   follows from `m_* K_b = m_*` and mass conservation), so `D_H R_b^H` is a Markov operator with
   invariant probability `π_*`, is an `L^p(π_*)` contraction for every `p ∈ [1,∞]` by Jensen, and
   the bound `|λ_a| ≤ 1` extends to every eigenoperator in any `L^p(π_*)`.
5. *The manuscript's own worked sector demonstrates what is lost.* At `07b:783-787` the text
   offers the strictly `α`-stable baseline with block statistic `b^{−1/α}Σ_{i=1}^b Y_i` as an
   exact fixed pair (correct; I verified it is a genuine instance of `eq:rg-kernel-semigroup`).
   This is the textbook Gaussian/stable fixed point, whose linearization has the *relevant*
   direction `y = 1/α > 0` (the field/magnetization direction) and a marginal direction at the
   second Hermite mode. Monte Carlo, 4·10⁶ samples, on the exact identity
   `E[He_n(Y₁)|Z=z] = b^{−n/2}He_n(z)`:
   ```
   b=2, n=1 : MC 0.7047 vs a^n He_n(1)=0.7071   λ_extensive = b·a^n = 1.4142  y = +0.500
   b=2, n=2 : MC −0.0046 vs 0.0000              λ_extensive = 1.0000          y =  0.000
   b=2, n=3 : MC −0.7157 vs −0.7071             λ_extensive = 0.7071          y = −0.500
   b=4, n=1 : MC 0.5040  vs 0.5000              λ_extensive = 2.0000          y = +0.500
   b=4, n=2 : MC 0.0013  vs 0.0000              λ_extensive = 1.0000          y =  0.000
   ```
   The relevant eigenvalue `b^{1−n/2}` appears **only** for the *extensive* perturbation
   `φ = Σ_{i=1}^b He_n(y_i)`. On the common space required to make `K_b` an endomorphism (the
   infinite sequence space), that `φ` does not converge, so it is not in `L^∞`, not in any
   `L^p(π_*)`, and not "conditionally exponentially integrable" — it is not a function at all.
   On the finite system the operator is not an endomorphism, so "eigenvalue" is undefined. Either
   way `eq:rg-linearized-action` cannot see `y = +1/2`, and instead assigns the same Hermite mode
   `λ = b^{−n/2}`, i.e. `y = −n/2`: **every exponent is off by exactly `+1` (the volume factor),
   and the two physically decisive directions (field, relevant; mass, marginal) are both
   misclassified as irrelevant.**
6. *Consistency cross-check with `07:407-418`.* `eq:rg-projective-dimensions` defines
   `y_a = log|μ_a/μ_0|/log b`. The two chapters' `y_a` agree here only because RG-F1 forces
   `μ_0 = 1` (the constants). So the ch-7 convention *already* encodes the conclusion: at a
   normalized fixed point of a positive map all transverse exponents are `≤ 0`.

**Why this is not merely pedantic.** The framework's RG step is, by
`thm:rg-exact-coarse-vfe` and its own summary at `07b:801-806`, a monotone information-destroying
channel. A monotone information-destroying semigroup on normalized measures is purely IR-attracting
by construction. Wilsonian relevance is *not* a property of that semigroup; it is a property of the
induced map on **coupling densities per unit volume**, which is where the extensivity factor lives.
The chapter names relevance, marginality, criticality, and scaling exponents, and tags the naming
`ESTABLISHED`, while the object it constructs provably has none of them.

**Fix.**
1. State the structural theorem explicitly: *`R_b^H` is order preserving and additively
   homogeneous, hence sup-norm nonexpansive; `D_H R_b^H` is a positive unital operator with
   spectral radius exactly 1; consequently no bounded eigenoperator is relevant and `λ = 1` (the
   constants) is always an eigenvalue.* This is a genuine, provable, `ESTABLISHED`-grade result and
   it is more informative than the current sentence.
2. Move the relevant/marginal/irrelevant classification to the **coupling coordinates** the
   manuscript already has. With `H = Σ_A g_A ψ_A` (`eq:rg-component-beta`, `07b:671-682`) built on
   the Möbius potentials (`eq:rg-mobius-potentials`, `07b:157-168`), classify the spectrum of
   `M_{AB} = ⟨ψ*_A , E_{Π_*}[ψ_B | Z=·]⟩`. Because the coefficient functionals `ψ*_A` are not
   norm-compatible with `L^∞`, `M` can and does have `|λ| > 1`; that is where `y_a > 0` lives.
3. Declare the extensivity/self-similarity structure that makes `ψ_A` comparable across scales
   (per-site or per-volume normalization). Without it "block factor `b`" cannot convert an operator
   eigenvalue into a scaling dimension.
4. Resolve the symbol clash `ψ_A` (Schauder basis of the action space, `07b:672`) vs `ψ_a`
   ("eigenoperator", `07b:771`) — the clash is a symptom of exactly this conflation.
5. `JonaLasinio2001` ("Renormalization group and probability theory", Phys. Rep. 352:439–458) is
   **already in `references.bib:1103` and never cited anywhere in the manuscript**. It is the
   canonical source for precisely this construction (block-sum RG on laws, Gaussian fixed point,
   eigenvalues of the linearized RG and critical indices). Citing it would have exposed the gap.

**Falsifies.** This finding is wrong if (a) the manuscript declares an action space whose norm is
*not* dominated by `L^∞` or `L^p(π_*)` and proves `D_H R_b^H` bounded there with spectral radius
`> 1` — it declares no norm at all; or (b) `R_b^H` is not the map at
`eq:rg-reference-dependent-action-map` but something with an unbounded multiplicative factor, which
is the "followed by the declared rescaling" clause (see RG-F4, where that clause is shown to be
either redundant or a double count); or (c) a concrete `(K_b, ρ_*, H_*, ψ_a)` with `|λ_a| > 1` and
`ψ_a` in a declared class is exhibited. I could not construct (c), and the argument in (1) shows it
cannot exist for bounded `ψ_a`.

---

## FINDING RG-F2 — **HIGH** — fixed-point dichotomy: an ergodic rescaled kernel admits only constant actions; a nonconstant action forces non-isolated, non-hyperbolic fixed points

**Claim under review.** `thm:rg-fixed-point-equations`, `07b:712-747`, titled "Exhaustive
fixed-point equations", and its illustrative sectors at `07b:779-799`.

**Location.** `07b:712-747` (`eq:rg-fixed-measure-pair`, `eq:rg-fixed-action`), `07b:779-790`.

**Severity.** high.

**Status.** `\status{ESTABLISHED}`. **Prose inflates** via "Exhaustive" and via presenting a menu of
"exact sectors [that] illustrate them" without noting that every one of them has a constant `H_*` or
a degenerate channel — because nothing else is possible.

**Evidence (recomputation and proof).**

*Theorem (mine).* Let `K_b` be Markov on a common standard Borel space, `ρ_*` a probability with
`ρ_* K_b = ρ_*`, and `m_* = e^{−H_*}ρ_*` with `0 < Z = m_*(Y) < ∞` (the "positive finite evidence"
hypothesis of `thm:rg-complete-effective-theory`, `07b:817`) and `H_*` finite-valued `ρ_*`-a.e.
(the declared action Banach space, `07b:749-750`). Then:

- **(i)** `m_*/Z` is a `K_b`-invariant probability. If `ρ_*` is the *unique* `K_b`-invariant
  probability, then `m_*/Z = ρ_*`, so `H_* = −log Z` is a.e. constant.
- **(ii)** Hence a nonconstant finite-valued `H_*` forces `π_* = m_*/Z` to be non-ergodic for
  `K_b`. (If `π_*` were ergodic, then since `π_* ≪ ρ_*` and both are invariant, `π_*` is an ergodic
  component of `ρ_*`, so `dπ_*/dρ_* = 1/c` on `supp π_*` and `0` off it, i.e. `H_* = +∞` on a set
  of positive `ρ_*`-measure — contradicting finite-valuedness.)
- **(iii)** Therefore the invariant probabilities dominated by `ρ_*` form a simplex of dimension
  `≥ 1`, every point of which is another fixed pair with finite-valued action: **no nontrivial
  fixed point of this RG is isolated**, and the tangent direction along that simplex is a
  `λ = 1` eigenvector of `D_H R_b^H`, so **`λ = 1` has multiplicity ≥ 2 and no fixed point is
  hyperbolic**.

Numerical confirmation (checks D, D2):
```
irreducible K_b (n=6):  dim of invariant-measure space = 1
                        ||m_*/Z − ρ_*||_max = 0.0
                        H_* = [0,0,0,0,0,0]   spread = 0.0
                        ||R^H[H_*] − H_*|| = 0.0             (constant action, trivially fixed)

reducible K_b (two classes):
  θ=0.25  H_* = [ 0.6931 0.6931 0.6931 −0.4055 −0.4055 −0.4055]  ||R^H[H_*]−H_*|| = 3.33e-16
  θ=0.50  H_* = [ 0 0 0 0 0 0 ]                                  ||R^H[H_*]−H_*|| = 0.00e+00
  θ=0.75  H_* = [−0.4055 −0.4055 −0.4055 0.6931 0.6931 0.6931]   ||R^H[H_*]−H_*|| = 1.67e-16
  ||ρ_* K_b − ρ_*|| = 5.55e-17  for all θ
  eigenvalues of D_H R^H at the θ=0.25 fixed point:
      0.0280±0.0879i, 0.0759±0.0638i, 1.0000, 1.0000
  multiplicity of λ = 1 : 2
```
A one-parameter family of exact fixed pairs, each with residual `< 4e-16`, and a doubled marginal
eigenvalue. Exactly as predicted.

*Cross-check against the manuscript's own list* (`07b:781-790`): "The identity channel fixes every
law" — maximally non-ergodic, every `H_*` fixed, infinite-dimensional simplex, all directions
marginal. "A terminal channel followed by its one-point identification" — `H_*` constant. "Strictly
`α`-stable baseline **with constant likelihood `m_o = Z(o)ρ`**" — `H_*` constant by fiat. **The
manuscript exhibits no example of a nontrivial fixed point with nonconstant finite action and a
nondegenerate channel, and by (i)–(ii) none can exist unless `K_b` is reducible.**

**Fix.** State the dichotomy as a proposition immediately after `thm:rg-fixed-point-equations`:
either `K_b` is uniquely ergodic and the only fixed theory is `H_* = const` (the trivial/infrared
theory), or `K_b` is reducible and the fixed set is a simplex on which `D_H R_b^H` has `λ = 1` with
multiplicity equal to the number of ergodic components. Then say explicitly that nontrivial critical
fixed points require either the per-volume/projective sector (see RG-F3) or the infinite-volume
setting, which the ledger already declares OPEN — so the finite theory's `ESTABLISHED` fixed-point
statement is a statement about trivial and degenerate fixed points only. Also drop "Exhaustive" from
the theorem title: the proof (`07b:740-747`) is a restatement of the definition of invariance plus a
one-line Radon–Nikodym equivalence, and the paragraph at `07b:779-780` already disclaims
enumeration.

**Falsifies.** Wrong if `K_b` is not required to be mass-preserving (see RG-F4: `I_b`'s type is
never declared) — but a non-mass-preserving `K_b` breaks `ρ_* K_b = ρ_*` for a probability
reference, which is `eq:rg-fixed-action`'s first component; or if `H_*` is allowed to be
extended-valued, which `07b:749-750` explicitly forbids at a fixed pair; or if a concrete
uniquely-ergodic `K_b` with nonconstant finite `H_*` is exhibited, which (i) forbids.

---

## FINDING RG-F3 — **MEDIUM-HIGH** — the additive normalizer `c_b` is forced to zero under the chapter's own hypotheses, and when nonzero obeys an unstated cocycle

**Claim under review.** `eq:rg-fixed-action-ray`, `07b:728-735`:

> "If the evidence mass is discarded and actions are considered only projectively, the weaker
> fixed-ray equation is `R_b^H[H_*;ρ_*] = H_* + c_b`. It represents the normalized pair in
> `eq:rg-fixed-measure-pair` only when the reference is also invariant and normalization fixes
> `c_b = 0`."

**Location.** `07b:726-735`; interacting with `eq:rg-discrete-beta-functional` at `07b:636-639`
and with `07b:640-643` ("If the evidence mass is deliberately forgotten and finite unnormalized
actions are quotiented by additive constants, the same formula is interpreted in that quotient").

**Severity.** medium-high.

**Status.** `\status{ESTABLISHED}` (`07b:738`). **Prose inflates**: calling the ray equation
"weaker" and listing "normalization fixes `c_b = 0`" as a *side condition* alongside reference
invariance, when it is a *consequence* of reference invariance plus the chapter's standing
finite-evidence hypothesis.

**Evidence (recomputation).** With `K_b` Markov, total mass is conserved:
`‖m_* K_b‖ = ‖m_*‖ = Z`. If `ρ_* K_b = ρ_*` and `R_b^H[H_*;ρ_*] = H_* + c_b`, then
`d(m_* K_b)/dρ_* = e^{−H_*−c_b}`, i.e. `m_* K_b = e^{−c_b} m_*`, so `Z = e^{−c_b} Z`. Since
`thm:rg-complete-effective-theory` (`07b:817`) requires **positive finite evidence**,
`0 < Z < ∞`, hence `c_b = 0` necessarily. Numerical confirmation (check E):
```
mass of m_*: 1.0     mass of m_* K_b: 1.0
c_b = 0.0 : ||R^H[H_*] − (H_* + c_b)||_max = 3.33e-16     (satisfied)
c_b = 0.3 : ||R^H[H_*] − (H_* + c_b)||_max = 3.00e-01     (no solution)
```
So the "weaker fixed-ray equation" is **not weaker**: it has exactly the same solution set as
`eq:rg-fixed-action` under the chapter's own standing hypotheses. A nonzero `c_b` requires
`Z ∈ {0, ∞}`, i.e. a non-normalizable effective theory, which is precisely the infinite-volume /
free-energy-density sector the ledger declares OPEN.

**Second, unstated constraint.** `R_b^H` composes: I verified symbolically that
`R^H_{b₂}[R^H_{b₁}[H;ρ]; ρK_{b₁}] = R^H_{b₁b₂}[H;ρ]` whenever `K_{b₁}K_{b₂} = K_{b₁b₂}`
(`eq:rg-kernel-semigroup`). At a fixed ray with invariant reference this forces
`c_{b₁b₂} = c_{b₁} + c_{b₂}`, i.e. `c_b = γ log b` for a single constant `γ`. That cocycle
condition is nowhere stated, yet `eq:rg-fixed-action-ray` quantifies over "every declared `b`"
(`07b:717`). The constant `γ` is exactly the nonvanishing free-energy-density beta of the discarded
mass — the one genuinely interesting object in the ray sector, and it is not named.

**Third: symbol collision.** `c_b` in `eq:rg-fixed-action-ray` (`07b:730`, the additive action
normalizer) collides head-on with `c_b` in `10_renormalization.tex:160` ("If a typical coarse cut
contains `c_b ≍ b^s` fine edges"), where it is the number of fine edges in a coarse cut. Two RG
chapters, same glyph with subscript `b`, incompatible meanings. See RG-F7.

**Fix.** Replace the sentence at `07b:732-735` with: *"Under the chapter's standing hypotheses —
Markov `K_b`, invariant probability reference, and positive finite evidence — mass conservation
forces `c_b = 0`, so the ray equation is not weaker. A nonzero `c_b` requires infinite or vanishing
evidence mass, and then the semigroup forces `c_{b₁b₂} = c_{b₁} + c_{b₂}`, i.e. `c_b = γ log b`
for a declared free-energy-density constant `γ`, whose discrete beta is the constant `γ`."*
Rename one of the two `c_b`'s.

**Falsifies.** Wrong if `K_b` may lose or gain mass — which requires `I_b` to be non-Markov and
breaks `eq:rg-fixed-action`'s first component (see RG-F4); or if the "declared canonical
identifications" (`07b:606-608`) are permitted to rescale total mass, in which case say so, because
a *uniform* mass factor cancels identically in `eq:rg-reference-dependent-action-map` (numerator and
denominator scale together) and therefore still cannot produce `c_b ≠ 0`.

---

## FINDING RG-F4 — **MEDIUM** — `I_b` is never typed, and the order of "push then Radon–Nikodym" vs "Radon–Nikodym then identify" is stated three different ways

**Claim under review.** Three mutually inconsistent placements of the identification/rescaling `I_b`.

**Locations.**
1. `07b:605-617`: "a declared rescaling/identification kernel `I_b` that returns the target to a
   common measurable state space. Define the typed rescaled kernel `K_b = C_b I_b`" and
   `R_b(ρ, m_o) = ((ρC_b)I_b, (m_oC_b)I_b) = (ρK_b, m_oK_b)` — **`I_b` inside, applied to
   measures, before any Radon–Nikodym derivative.**
2. `fig:rg-exact-measure-flow`, `07b:527-550`: the diagram routes
   `coarse law → (Radon–Nikodym) → H^c_o → (identification I_b) → rescaled common space`
   — **`I_b` applied to the action, after the Radon–Nikodym derivative.**
3. `07b:766-767`: the first and second variations are "followed by the declared rescaling" —
   **`I_b` applied a second time, after a derivative of a map that already contains it.**

**Severity.** medium.

**Status.** `eq:rg-measure-pair-map` is inside a paragraph tagged `\status{ESTABLISHED}`
(`07b:624`); `eq:rg-linearized-action` is `\status{ESTABLISHED}` (`07b:777`).

**Evidence.** The two orders coincide **iff** `I_b` is a deterministic bijection: if `I_b = φ_#`
then `d(φ_#m)/d(φ_#ρ) = (dm/dρ)∘φ^{−1}`, so pushing then differentiating equals differentiating
then relabeling. For any genuinely randomizing or non-injective `I_b` — and the text calls it a
*kernel* — order (1) produces `−log E[e^{−H^c}|·]`, a strictly further-averaged (hence
strictly larger by Jensen) action than order (2). The two definitions give different `H`, different
`𝔅_b^H`, different fixed points, and different `λ_a`. Additionally `I_b` is never declared Markov,
sub-Markov, or mass-scaling; `appendix_notation.tex:139-142` types only the generic `K` as
"normalized, parameter-independent Markov kernel" and does not list `I_b`, `C_b`, `K_b`, `R_b`,
`R_b^ρ`, `R_b^H`, or `𝔅_b^H` at all (see RG-F7). Everything in RG-F2 and RG-F3 depends on which
answer is intended.

**Fix.** Add one line to `sec:rg-beta-function`: *"`I_b` is a Markov kernel; consequently `K_b` is
Markov and preserves total mass."* Then correct the figure (identification acts on the measure pair,
before the Radon–Nikodym derivative) and delete "followed by the declared rescaling" at `07b:766`
(it is already inside `K_b`). If instead `I_b` is meant to act on the action *after* the
Radon–Nikodym derivative, then `eq:rg-measure-pair-map` is the equation that must change, and
`R_b^H` must be redefined.

**Falsifies.** Wrong if `I_b` is somewhere declared to be a deterministic isomorphism — I could not
find such a declaration in `07`, `07b`, `10`, or `appendix_notation.tex`; `07:35-38` offers *either*
re-embeddings `ȷ_ℓ` *or* isomorphisms `I_ℓ` and says "Only the isomorphism option supplies the
inverse", which suggests isomorphism is intended at ch-7 level, but `07b` calls `I_b` a kernel and
never repeats the restriction.

---

## FINDING RG-F5 — **MEDIUM** — the reference-dependence of the beta functional is named but its transformation law is never derived, so no scheme-covariant object is defined

**Claim under review.** `eq:rg-reference-dependent-action-map` (`07b:626-632`) and
`eq:rg-discrete-beta-functional` (`07b:636-647`), together with the scheme-dependence section
`sec:rg-scheme-dependence` (`07:394-425`).

**Severity.** medium.

**Status.** `\status{ESTABLISHED}` (`07b:647`); `07:402` `\status{ESTABLISHED}` for
`eq:rg-beta-change`.

**Evidence (recomputation).** The map is explicitly called *reference dependent* and retains `ρ` as
an argument, but the manuscript never says how it transforms when the reference is changed. It does
transform, exactly and simply. Writing `ρ' = e^{−Δ}ρ` for the same evidence submeasure (so
`H' = H − Δ`):
```
R_b^H[H − Δ ; e^{−Δ}ρ] = R_b^H[H ; ρ] − R_b^H[Δ ; ρ]        residual 3.33e-16
𝔅_b^H[H';ρ'] = 𝔅_b^H[H;ρ] − 𝔅_b^H[Δ;ρ]                      residual 6.66e-16
```
(check `C:/Users/CHRISA~1/AppData/Local/Temp/claude/C--Users-chris-and-christine-Desktop-Research/21b92b09-6f32-47fa-8f90-6f5faa59e5a3/scratchpad/ref_change.py`). So the beta functional is covariant with an **inhomogeneous term**
`−𝔅_b^H[Δ;ρ]`, which is itself a beta functional. This is the direct analogue of
`eq:rg-beta-change` in the *reference* direction, and it is the reason a "reference-dependent beta
function" is not by itself a diagnostic: two admissible references give beta functionals differing
by an arbitrary nonzero functional. `sec:rg-scheme-dependence` (`07:394-425`) covers only
coupling reparameterization `g' = f(g)` and scale change `t' = ct`; the reference direction — the
one `07b` actually parameterizes — is absent from the scheme-dependence analysis entirely, and the
"candidate cross-scheme quantities" list at `07:420-425` therefore omits the invariance that
`07b`'s beta most needs.

**Fix.** Display the transformation law above right after `eq:rg-discrete-beta-functional`, tag it
`ESTABLISHED` (it is a two-line proof), and extend the `07:420-425` candidate-invariants list to
state which candidates survive a change of reference. Note explicitly that only *differences* of
beta functionals at a common reference, or the fixed-point set itself, are reference independent.

**Falsifies.** Wrong if the "declared reference trajectory" (`07b:643`) is somewhere argued to be
canonical, removing the freedom. It is not: `07b:626` explicitly retains `ρ` as a free argument, and
`07b:861` lists "a declared reference trajectory" as a supplied hypothesis of the corollary.

---

## FINDING RG-F6 — **MEDIUM** — the Mori–Zwanzig "exactly when" is a false biconditional; explicit counterexample

**Claim under review.** `07b:588-590`: "Autonomous resolved dynamics on an admitted initial class
holds **exactly when** all the relevant memory and noise operators vanish there."

**Location.** `07b:577-597`.

**Severity.** medium.

**Status.** `\status{ESTABLISHED}` (`07b:597`).

**Evidence (counterexample, check H).** Take the 2-state linear tier
```
T = [[0.3, 0.5],
     [0.4, 0.2]],       C = [1 0],  P = [1 0]^T,   ||CP − I|| = 0.0
Π = P C,  Q = I − Π
```
and admit the invariant class spanned by the eigenvector `x₀ = (1, 0.8)` with eigenvalue
`μ = 0.7`. Then
```
resolved trajectory  x̂ = 1.0, 0.7, 0.49, 0.343, 0.2401, 0.16807, 0.117649
ratios x̂_{k+1}/x̂_k  = 0.7, 0.7, 0.7, 0.7, 0.7      -> exactly autonomous
memory operator n=0:  C T Q Q T P = 0.2   (nonzero)
initial-noise n=0:    C T Q Q x₀   = 0.4   (nonzero)
Galerkin operator     C T P        = 0.3  != μ = 0.7
```
The resolved dynamics is exactly autonomous and first order on the admitted class, while the `n=0`
memory operator and the initial-noise term are both nonzero **on that class**. Necessity fails.
Under the narrower reading ("autonomous *with the Galerkin operator* `CTP`") necessity also fails,
because `C T v_k = 0` for all `k` can hold by cancellation between the memory sum and the noise
term without any individual operator vanishing.

**Fix.** Replace "exactly when" with "if" and add the necessity condition: *necessity holds when the
admitted class and its resolved images span, i.e. when `{Q x₀ : x₀ ∈ class}` spans `ran Q` and
`{x̂_k}` spans the resolved space.* Alternatively state it as: vanishing of the memory and noise
operators is sufficient for autonomy with the Galerkin operator, and necessary only modulo the
annihilator of the admitted class. Cite Nakajima/Zwanzig/Mori — `eq:rg-memory-operators` is the
standard discrete Nakajima–Zwanzig decomposition and carries no citation.

**Falsifies.** Wrong if "admitted initial class" is implicitly required to span the full state space.
`07b:590-597` only says "For a general admitted initial class one must additionally require …
throughout that class", which does not impose spanning; a one-dimensional invariant class is
plainly admitted by that wording.

---

## FINDING RG-F7 — **MEDIUM** — the RG operator tier is absent from the "Typed Notation Contract" and collides with five other uses of `R`/`c`

**Claim under review.** `appendix_notation.tex` announces itself as "a type checker" (`:4`).

**Severity.** medium (low mathematically, high for readability of exactly the chapters under review).

**Status.** untagged appendix; the collisions live inside `ESTABLISHED` material.

**Evidence.**

- **`R_b` collision (the item flagged as carried-over candidate #3).** `02_geometry.tex:361-365`
  introduces `R_b, R_m` as "the represented coordinate changes" in `eq:geo-defect-gauge-laws`;
  `07b:614-772` uses `\mathcal R_b`, `\mathcal R_b^ρ`, `\mathcal R_b^H` for the block-`b`
  renormalization operator and its components. **Confirmed: these are different symbols
  (`R_b` vs `\mathcal R_b`), so the prior session's claim that "Chapter 7b uses the opposite
  convention" was a symbol confusion.** But the collision is real as a *reading* hazard: in the same
  document `R` denotes (i) the ch-2 represented coordinate change `R_b, R_m`; (ii) the ch-7b reverse
  conditional `R_ρ(z,dy)` (`07b:104`) and full reverse kernel `R_o(z,dy)` (`07b:201`); (iii) the
  ch-7b linear representation `R_x : G → GL(V_x)` (`07b:301`); (iv) the ch-10 positive reference
  form `R ≻ 0` (`10:338`); (v) the general refinement kernel `R` (`07:502`,
  `appendix_notation.tex:175`); and (vi) the RG operator `\mathcal R_b`. Note in particular that
  `\mathcal R_b^ρ` (RG map, reference component, `07b:619`) and `R_ρ` (reverse conditional kernel,
  `07b:104`) differ only by calligraphy and sub/superscript position, and both appear in the same
  chapter, both applied to the same measure `ρ`.
- **`c_b` collision.** `07b:730` (additive action normalizer) vs `10:160` (number of fine edges in a
  coarse cut). Two RG chapters. Verified by grep: these are the only two occurrences of `c_b` in the
  manuscript, and they mean different things.
- **`ρ` triple use.** `ρ` = reference probability measure (`07b`, ch 6, `appendix_notation:161`);
  `\widehat ρ_{ℓ,x}` = representation on laws (`07:70`, `appendix_notation:31`); `ρ_a = μ_a/μ_0` =
  projective eigenvalue ratio (`07:411`). All three appear within chapters 7/7b.
- **`ψ_A` vs `ψ_a`.** Schauder basis of the action space (`07b:672`) vs "eigenoperator"
  (`07b:771`) — see RG-F1, where distinguishing them is the fix.
- **`\mathcal A` triple use.** Generator adjoint `\mathcal A^*` (`07b:653`), aggregation map
  `\mathcal A_S` (`10:33`), within-connection defect `\mathbf A^Φ` (`07:227`).
- **Absent from the notation contract.** `appendix_notation.tex` lists `C_{ℓk}`, `c_ℓ`, `Q,R`,
  `\mathsf C,\mathsf P`, `(ρ,m_o)`, `α_i,β_{ij},η_{ij}` — and **none of** `C_b`, `I_b`, `K_b`,
  `\mathcal R_b`, `\mathcal R_b^ρ`, `\mathcal R_b^H`, `𝔅_b^H`, `c_b`, `y_a`, `λ_a`, `b`. The RG
  operator tier — the subject of the chapter titled "The RG transformation and beta functions" — is
  entirely missing from the appendix that claims to type check the manuscript.

**Fix.** Add an RG block to `appendix_notation.tex` typing `C_b` (Markov coarse channel), `I_b`
(identification kernel — and *say whether it is Markov*, RG-F4), `K_b = C_b I_b`, `\mathcal R_b`
(measure-pair RG), `\mathcal R_b^H` (reference-dependent action map, with its prohibited
identification with the ch-2 `R_b`), `𝔅_b^H`, and `b`. Rename `c_b` in one chapter. Consider
`\mathsf R_ρ` or `\Pi_ρ` for the reverse conditional to separate it from `\mathcal R_b^ρ`.

**Falsifies.** Nothing mathematical; this is a notation finding, reported because the review brief
asked for it and because RG-F1/F4 are made materially harder to detect by the missing type
declarations.

---

## FINDING RG-F8 — **LOW-MEDIUM** — `b` is never declared to be a linear or a volume ratio, so `y_a` cannot be matched against the heat/IDS exponent the manuscript proposes as a cross-scheme invariant

**Claim under review.** `07:420-425`: "Candidate cross-scheme quantities include … projective
eigenvalue ratios, dimensionless amplitude ratios, and matched spectral or heat exponents."

**Location.** `07:407-425` (`eq:rg-projective-dimensions`), `07:468-483`
(`eq:rg-heat-susceptibility`), `07b:771-773`, `10:375-396` (`eq:grg-ids`).

**Severity.** low-medium.

**Status.** `\status{ESTABLISHED}` on `eq:rg-projective-dimensions` and
`eq:rg-heat-susceptibility`; `\status{HYPOTHESIS}` on the candidate-invariants sentence.

**Evidence.** `y_a = log|ρ_a|/log b` and `y_a = log|λ_a|/log b` are normalized by "the declared
block factor `b`". Everywhere `b` is instantiated it is a **cardinality**: `10:144` "equal blocks of
size `b`" (nodes per cluster), `10:31-42` (nodes per cluster), `07b:783` (`b` summands),
`07:448-453` (`b` path vertices). The spectral exponent `α` in `eq:rg-heat-susceptibility` and
`eq:grg-ids` is instead defined by `N(λ) − N(0) ∼ cλ^α`, a **length-based** exponent (`α = d_s/2`).
Matching a volume-normalized `y_a` against a length-normalized `α` requires a declared dimension `d`
with `b_volume = b_linear^d`. That relation is never declared, and for the complete graph
(`10:144-165`) it does not exist. So "matched spectral or heat exponents" is not yet a well-posed
comparison. Concretely: the dense MVG sector has `y_self = −1` per *volume*-doubling
(`eq:grg-sector-gap` gives ratio `1/b`), and the chain has `y_self = +1 − s = +1` by the same
convention (`10:157-165`, correct arithmetic, verified) — but neither number is comparable to a
spectral dimension without `d`.

**Fix.** Declare once, in `sec:rg-scheme-dependence`, whether `b` is the linear or the volume
rescaling factor, and state the conversion `y^{linear} = d · y^{volume}` needed before any
comparison with `α`. One sentence.

**Falsifies.** Wrong if the manuscript intends `y_a` purely as an internal label with no comparison
to spectral exponents — but `07:420-425` explicitly proposes matching them, and `10:390-396` repeats
the proposal.

---

## FINDING RG-F9 — **LOW** — the Möbius "exact closure" is a tautology and carries no bound on the surviving interaction order

**Claim under review.** `07b:169-171`: "Thus the full hypergraph family is exactly closed."

**Location.** `07b:155-178`; used in `thm:rg-complete-effective-theory`'s proof at `07b:839`
("Mobius inversion or the retained top-order factor closes the hypergraph").

**Severity.** low.

**Status.** `\status{ESTABLISHED}`. Correct, but "closure" is doing rhetorical work.

**Evidence.** I verified `Σ_{A⊆P} Φ_A(z_A) = H(z)` for a **uniformly random array** `H` on
`3^4` states: residual `2.22e-15`. The identity holds for *every* function on a finite product,
with no structure whatsoever. It is Möbius inversion on the Boolean lattice, not an RG statement.
The RG content of "closure" is a bound on the number of nonvanishing potentials or on their decay,
and the manuscript's own Ising-star computation (`07b:180-190`, verified exactly) shows that no such
bound holds. `07b:645-647` does say the right thing ("A beta function on a truncated coupling vector
exists only after invariance of that finite family is proved"), so this is an internal tension, not
an error.

**Fix.** Change "the full hypergraph family is exactly closed" to "the full hypergraph family is
trivially closed: every finite-valued action equals the sum of its Möbius potentials, so closure
here is a change of coordinates rather than a bound on interaction order". The section title
"Exact closure generates hyperedges" is fine; the closure-theorem proof line at `07b:839` should
point at the truncation residual rather than at closure.

**Falsifies.** Nothing; the identity is true. The finding is about status of the word "closed".

---

## FINDING RG-F10 — **LOW** — three uncited canonical results and one Abelian/Tauberian mislabel

**Locations and evidence.**

1. **Strong lumpability**, `07b:564-575`: "a coarse first-order kernel `T^c` exists for every
   initial law **exactly under** strong lumpability". Correct — this is the Kemeny–Snell theorem
   (*Finite Markov Chains*, §6.3) — but it is stated with no citation. Grep confirms no
   `Kemeny` entry in `references.bib` and no `\citep` on that paragraph, while comparable
   `ESTABLISHED` statements elsewhere in the chapter do carry citations.
2. **Nakajima–Zwanzig / Mori memory expansion**, `eq:rg-memory-operators`, `07b:577-597`: exact and
   correctly derived (I rederived it: `v_k = (QTQ)^k v₀ + Σ_n (QTQ)^n QTP x̂_{k−1−n}`,
   `x̂_{k+1} = CTP x̂_k + CTQ(QTQ)^k Q x₀ + Σ_n CTQ(QTQ)^n QTP x̂_{k−1−n}`), but uncited.
3. **`JonaLasinio2001` is in `references.bib:1103` and never cited anywhere.** It is the canonical
   probabilistic-RG reference for exactly the construction in `sec:rg-fixed-points` — the block-sum
   transformation on laws, the stable/Gaussian fixed point, and "eigenvalues of the linearized RG
   and critical indices". See RG-F1.
4. **Abelian mislabeled as Tauberian**, `07:468-472`: "If an infinite-volume integrated density
   satisfies `N(λ) − N(0) ∼ cλ^α` and **a Tauberian hypothesis** supplies the corresponding heat
   asymptotic…". The direction IDS ⟹ heat trace is the **Abelian** half of Karamata's theorem and
   needs no extra hypothesis beyond convergence of the transform; the Tauberian half is the reverse
   implication. The displayed conclusion `Z(t) ∼ cΓ(α+1)t^{−α}` and
   `−dS/d log t = t²Var_t(λ) → α` are both correct (I rederived: `S = log Z + t⟨λ⟩`,
   `dS/dt = −t Var_t`, `⟨λ⟩ = α/t`, `Var = α/t²`).

**Severity.** low. **Status.** all in `ESTABLISHED` paragraphs.

**Fix.** Add Kemeny–Snell and a Zwanzig/Mori reference; cite `JonaLasinio2001` at
`eq:rg-linearized-action`; change "Tauberian" to "Abelian (Karamata)" at `07:469`.

---

## FINDING RG-F11 — **LOW** — "compatible nested forests" is a spurious hypothesis for the measure-pair composition

**Claim under review.** `07b:621-624`: "Equation `eq:rg-kernel-semigroup`, **together with
compatible nested forests**, makes `R_{b₁b₂} = R_{b₂}R_{b₁}`."

**Severity.** low. **Status.** `\status{ESTABLISHED}`.

**Evidence.** `R_b(ρ, m_o) = (ρK_b, m_oK_b)` (`eq:rg-measure-pair-map`) depends on `K_b` alone.
Composition follows from `eq:rg-kernel-semigroup` by associativity of the right action of kernels on
measures, with the order reversal `R_{b₁b₂} = R_{b₂}R_{b₁}` correct as printed. The rooted/nested
forest condition is `eq:rg-linear-nested-compatibility` (`07b:320-332`), which governs the **linear
feature tier** `C_x, P_x` — a different tier, correctly separated everywhere else in the chapter
(e.g. `07b:350-356`, `07b:857-860`). Importing it into the measure-tier statement blurs exactly the
tier discipline the chapter is built on.

Related and also low: `eq:rg-linearization-positive-likelihood` (`07b:749-754`) is redundant *at a
fixed pair*, since the fixed-point equation gives `L^c_*(z) = e^{−H_*(z)}`, and finiteness of `H_*`
is already required by membership in the declared action Banach space one line earlier.

**Fix.** Delete "together with compatible nested forests" from `07b:622`, or move the sentence to
the linear-tier paragraph where the forests actually matter.

**Falsifies.** Wrong if `C_b` is somewhere *defined* through the rooted forests. It is not:
`eq:rg-coarse-channel` (`07b:20-23`) defines `C` as an arbitrary Markov kernel that does not read
`Q_o`.

---

## Answers to the specific questions in the brief

**Semigroup/cocycle property — proved or assumed?** Assumed, in both chapters, and in two different
ways. In ch 7, `eq:rg-scale-diagram` builds `C_{kr}C_{ℓk} = C_{ℓr}` into the *definition* of the
state functor, so the composition of `\widehat{\mathcal R}_ℓ = I_{ℓ+1}C_{ℓ,ℓ+1}I_ℓ^{−1}` is
vacuously true (I checked: the `I_ℓ^{−1}I_ℓ` telescoping gives it immediately). In ch 7b,
`eq:rg-kernel-semigroup` is a declared compatibility hypothesis. **Nowhere is the semigroup property
derived for a concrete blocking-plus-rescaling scheme.** RG-2 settles the conditional reading, so
this is reported only as context. The one instantiation that does satisfy it is the `α`-stable
block-sum map at `07b:783-787`, and the manuscript does not point this out — worth adding, because
it shows the hypothesis is not vacuous.

**Blocking schemes and scheme independence.** Correctly and honestly handled at `07:394-425` for
coupling reparameterization and scale change; **absent for reference change**, which is the
parameter `07b` actually carries (RG-F5).

**Fixed points and what "fixed point" means with `+c_b`.** See RG-F2 and RG-F3: `c_b` is forced to
zero; nontrivial fixed points require a reducible `K_b` and are then non-isolated and non-hyperbolic.

**Linearization and scaling exponents.** The first and second variations are correct
(residuals `1.25e-10`, `4.86e-08`). The exponent classification built on them is vacuous on the
relevant branch (RG-F1).

**Beta functions and reference dependence.** Both discrete and continuous betas are correct
(`Ḣ_t = −A*(r e^{−H})/(r e^{−H}) + A*r/r` rederived exactly; the replicator form has sympy
residual exactly 0). The transformation law under reference change is missing (RG-F5).

**Relevant/irrelevant/marginal classification — is the spectrum genuinely computed?** No. It is
never computed anywhere in the manuscript, for any sector. `10:270-280` computes the only concrete
spectrum (`b²` and `b`, ratio `1/b`, verified) and does not convert it to `y_a`;
`05a_expfamily.tex:266` explicitly defers the mass-sector classification as `\status{OPEN}`.
`07b:771-776` supplies vocabulary without a single instance.

**Invariant measures and exhaustiveness.** The `α`-stable / `b`-semistable discussion at
`07b:783-790` is correct and appropriately hedged (semistable laws do provide extra fixed points at
one fixed integer `b`; invariance over all `b` with the usual centering recovers strict stability).
The exhaustiveness that is *missing* is RG-F2's dichotomy.

**The additive normalizer.** RG-F3.

**Is finite-network exactness being silently extended to asymptotic statements?** Not in the way I
expected: the manuscript is explicit and repeated (`07:427-466`, `10:375-396`, `07b:881-896`) that
the two-index limits are open, and `prop:rg-noncommuting-limits` is a correct explicit warning
(`N(λ) − N(0) ≍ λ^{1/2}` for the infinite path vs `δ₀` on the diagonal — verified). The silent
extension is the *opposite* one and is RG-F1/RG-F2: **asymptotic RG vocabulary (relevance,
criticality, scaling exponents, universality classes) is attached to a finite exact construction in
which those phenomena provably cannot occur.**

**`\mathcal R_b` vs `R_b` notation collision.** Confirmed real, and confirmed that the prior
session's "opposite convention in chapter 7b" claim was a symbol confusion. Reported as RG-F7 with
four further collisions in the same tier.

---

## Adversarial self-tests I ran against my own findings

- **RG-F1.** Tried to defeat it by letting `I_b` be non-Markov or mass-scaling. A *uniform* mass
  factor cancels in `eq:rg-reference-dependent-action-map` (numerator and denominator both scale),
  and a *state-dependent* one still leaves the derivative a normalized average, hence still unital.
  Tried an unbounded eigenfunction: with `K_b` Markov, `π_*` is invariant for the reverse kernel, so
  Jensen gives `L^p(π_*)` contraction for every `p`, and an eigenfunction outside every `L^p(π_*)`
  makes `E[ψ|Z]` undefined. Tried the manuscript's own stable sector: the relevant mode exists but
  is extensive and therefore outside every declared class — which is the finding, not a refutation.
- **RG-F2.** Tried to find a uniquely ergodic `K_b` with nonconstant finite `H_*`: impossible by the
  two-line argument, confirmed numerically (`||m_*/Z − ρ_*|| = 0.0`). Tried extended-valued `H_*`:
  excluded by `07b:749-750`. Tried a non-probability reference: excluded by
  `eq:rg-fixed-action`'s first component.
- **RG-F3.** Tried `Z = ∞`: excluded by the closure theorem's "positive finite evidence". Tried a
  mass-scaling `I_b`: cancels identically, verified by inspection of the ratio.
- **RG-F6.** Checked whether the counterexample class is "admitted": the text imposes no spanning
  condition, so a one-dimensional invariant class is admitted. Also checked the narrow reading
  (autonomy specifically with `CTP`): necessity still fails by cancellation.
- **RG-F5.** Checked that the transformation law is not stated elsewhere (grep on `reference` in
  `07`, `07b`); it is not.
- **Discarded candidates** (tested, found sound, not reported): the exactness of
  `thm:rg-exact-coarse-vfe` (settled as RG-1 anyway); associativity of meta-attention under nested
  partitions (holds by the tower property since `Y → Z₁ → Z₂` is Markov); the evidence-weighted
  receiver posterior `α'_i = a_{i|I}c_i Z_i / W_I` (rederived from the declared augmented joint,
  correct); `C_x P_x = I` and the passive covariance laws (residuals `≤ 5e-14`); the aggregation
  semigroup and the `1/b` sector gap; `prop:rg-contraction-no-fixed-ray`; every ch-10 pencil
  proposition.

## Files

- Findings: this file.
- Recomputation: `C:/Users/CHRISA~1/AppData/Local/Temp/claude/C--Users-chris-and-christine-Desktop-Research/21b92b09-6f32-47fa-8f90-6f5faa59e5a3/scratchpad/rg_checks.py` (checks A–L) and `C:/Users/CHRISA~1/AppData/Local/Temp/claude/C--Users-chris-and-christine-Desktop-Research/21b92b09-6f32-47fa-8f90-6f5faa59e5a3/scratchpad/ref_change.py`.
  Interpreter `C:/Python314/python.exe` (CPU torch irrelevant here; numpy/sympy only).
