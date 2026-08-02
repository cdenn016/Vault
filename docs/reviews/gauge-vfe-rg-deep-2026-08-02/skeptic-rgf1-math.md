# Adversarial skeptic A — RG-F1, mathematical angle

**Question put to me.** Is RG-F1 mathematically wrong?
**Target.** `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex:756-777`.
**Finding attacked.** `docs/reviews/gauge-vfe-rg-deep-2026-08-02/lens-rg.md:45-165`.

## VERDICT

**REFUTED as stated.** The CRITICAL headline — "the `y_a > 0` branch of the
classification is EMPTY", "the object it constructs provably has none of them" — is
false. I exhibit an explicit `(K_b, ρ_*, H_*, φ)` satisfying **every** hypothesis
`07b` attaches to the linearization, with `φ` inside the manuscript's **own declared
perturbation class** as literally written at `07b:756-759`, for which

```
D_H R_b^H [φ] = 2 φ        exactly,     b = 2,     y = log|λ|/log b = +1.0
```

This is precisely falsification condition (c) that RG-F1 itself states at
`lens-rg.md:163-165` and reports it could not construct, and it simultaneously
satisfies falsification condition (a).

**Residual that survives, renamed and re-scored: `RG-F1'` — MEDIUM, well-posedness,
not emptiness.** The manuscript never says whether the integrability in its
perturbation class is *conditional* or *unconditional*, and the answer to "is the
relevant branch inhabited?" flips on that single undeclared word. Both branches are
provable. That ambiguity — not a provably empty case — is the defect.

Everything RG-F1 recomputed is arithmetically correct. Its error is a **quantifier
error**: it proves `|λ| ≤ 1` on `L^∞` and on every `L^p(π_*)`, then asserts it for
"the declared class", which the manuscript declares to be strictly larger.

---

## 1. What I could not break (RG-F1 is right about these)

Recomputed independently, script
`.../scratchpad/rgf1_attack.py` (`C:/Python314/python.exe`, numpy 2.4.4, sympy 1.14.0,
seed 20260802).

| RG-F1 sub-claim | My residual | Status |
|---|---|---|
| `D_H R_b^H[φ](z) = E_{Π_*(dy\|z)}φ` is the *bare* conditional expectation — no Jacobian, no leftover normalizer | derived below from `07b:105-109`, exact | **correct** |
| Positivity + unitality `T1 = 1`; row sums exactly `1` | `[1. 1. 1. 1. 1. 1.]` | **correct** |
| Additive homogeneity `R[H+c] = R[H]+c` | `6.66e-16` | **correct** |
| Crandall–Tartar: `R_b^H` sup-norm nonexpansive | `max(‖R[H₁]−R[H₂]‖_∞ − ‖H₁−H₂‖_∞) = −2.88e-3 ≤ 0` over 20 000 pairs | **correct** |
| Finite-dimensional spectral radius exactly `1` | `1.000000000000004` over 300 random fixed pairs | **correct** |
| `L^p(π_*)` contraction for `p = 1, 2, 4` | `4.4e-16`, `−5.1e-2`, `−1.7e-1` (all `≤ 0`) | **correct** |
| Hermite identity `E[He_n(Y₁)\|Z=z] = b^{−n/2}He_n(z)` | sympy **exactly 0** for `b ∈ {2,3,4}`, `n ∈ {1..4}` | **correct** |
| `JonaLasinio2001` in `references.bib:1103`, cited nowhere | grep: 1 bib hit, 0 `.tex` hits | **correct** |

**The escape hatches the brief asked me to test all fail.** I checked each:

- *"Maybe the derivative is not the bare averaging operator — watch for a Jacobian,
  a normalizer, or a ρ-dependence."* No. `eq:rg-conditional-partition` (`07b:105-109`)
  gives `exp[−H_o^c(z)] = ∫ exp[−H_o(y)] R_ρ(z,dy)`, so
  `R_b^H[H;ρ](z) = −log E_ρ[e^{−H(Y)} | Z = z]`. Differentiating,
  `D_H R^H[φ] = E[φ e^{−H_*}|Z] / E[e^{−H_*}|Z] = E_{Π_*}φ`. The `log` and the ratio
  produce exactly the exponentially tilted reverse conditional and nothing else; the
  `ρ`-dependence is entirely absorbed into `Π_*`. Unitality is unavoidable.
- *"Maybe the exponents come from the beta function, not the map."* They do not —
  `07b:771-772` reads `D_H R_b^H[ψ_a] = λ_a ψ_a`, the map. And it makes no difference:
  `D_H 𝔅_b^H = (D_H R_b^H − I)/log b` has the same eigenvectors, and
  `μ = (λ−1)/log b > 0 ⟺ λ > 1`. Verified (check 9).
- *"Maybe a mass-scaling `I_b` breaks unitality."* A uniform factor cancels in
  numerator and denominator of `eq:rg-reference-dependent-action-map`; a state-dependent
  one is reabsorbed into `Π_*` and the operator stays normalized.

So RG-F1's *machinery* is sound. It breaks at the quantifier.

---

## 2. The counterexample

### 2.1 Construction

Common standard-Borel state space `S = ℕ₀`, `p = 1/2`.

**Reverse conditional (the operator the manuscript linearizes).** Let `U` be the
advance-or-reset Markov kernel

```
U(i, i+1) = p ,        U(i, 0) = 1 − p ,        π_i = (1−p) p^i .
```

**Coarse channel.** Let `K := Û`, the `π`-reversal of `U`:

```
K(i, i−1) = 1   (i ≥ 1) ,      K(0, j) = (1−p) p^j .
```

Exact checks (`Fraction` arithmetic, no floats):

```
Σ_i π_i = 1                                                   (sympy)
(π K)(j) = π_j        for j = 0 … 23                          exact, 0 violations
π(y) K(y,z) = π(z) U(z,y)   for all y,z ≤ 23                  exact, 0 violations
```

**Fixed pair.** `ρ_* = π`, `H_* ≡ 0`, `m_* = e^{−H_*}ρ_* = π`. Then
`R_b(ρ_*, m_*) = (π K, π K) = (π, π)` — a normalized fixed theory in the exact sense of
`eq:rg-fixed-measure-pair` (`07b:714-717`), with `c_b = 0`. Directly verified from the
manuscript's definition:

```
max_z | R_b^H[H_*; ρ_*](z) − H_*(z) |  =  0.0     (z = 0 … 12)
```

Because `H_* ≡ 0`, the reverse conditional of the fixed pair is exactly `U`, so
`D_H R_b^H = U` acting on functions.

**Blocking ratio.** `b = 2`, with `K_{2^m} := K^m`, so `eq:rg-kernel-semigroup`
`K_{b₁b₂} = K_{b₁}K_{b₂}` holds identically. The choice `b = 2` is not arbitrary: the
step destroys `H(Y|Z) = −[p log p + (1−p)log(1−p)] = 0.693147 nats = exactly 1.0000
bits`, so this is a genuinely lossy coarse channel with information blocking ratio 2,
and `thm:rg-exact-coarse-vfe` applies non-trivially.

**The relevant perturbation.**

```
φ(i) = 1/3 + (2/3)·4^i        φ(0..7) = 1, 3, 11, 43, 171, 683, 2731, 10923
```

Exact rational check over `i = 0 … 23`:  `max |Uφ − 2φ| = 0` (**exactly zero**, `Fraction`).

### 2.2 Every hypothesis `07b` imposes is met

| Manuscript hypothesis | Location | Counterexample |
|---|---|---|
| `b > 1` blocking ratio | `07b:602` | `b = 2` |
| `K_b = C_b I_b` Markov on a common measurable space | `07b:604-616` | `K` on `ℕ₀` |
| `K_{b₁b₂} = K_{b₁}K_{b₂}` | `eq:rg-kernel-semigroup`, `07b:607-610` | `K_{2^m} = K^m` |
| `C` an arbitrary Markov kernel not reading `Q_o` | `eq:rg-coarse-channel`, `07b:20-23` | yes |
| `R_b(ρ_*,m_*) = (ρ_*,m_*)` | `eq:rg-fixed-measure-pair`, `07b:714-717` | residual `0.0` |
| `H_*` in the finite-valued action Banach space | `07b:749-750` | `H_* = 0` |
| `0 < L_*^c(z) < ∞` | `eq:rg-linearization-positive-likelihood`, `07b:751-754` | `L_*^c ≡ 1` |
| perturbation class | `07b:756-759`, restated `07b:866-868` | see §2.3 |
| positive finite evidence `0 < Z < ∞` | `thm:rg-complete-effective-theory`, `07b:817` | `Z = 1` |

### 2.3 `φ` is inside the manuscript's declared class — the load-bearing point

`07b:756-759` reads, verbatim:

> "For bounded perturbations `φ ∈ L^∞` (**or, more generally, perturbations with
> conditional exponential integrability in a neighborhood of zero and the first two
> required moments**)"

`Π_*(·|z) = U(z,·)` is supported on the **two points** `{z+1, 0}`. Therefore

```
E[ e^{t φ(Y)} | Z = z ] = p e^{t φ(z+1)} + (1−p) e^{t φ(0)}   <  ∞
```

for **every real `t`** and every `z` — not merely a neighborhood of zero. Both
"required moments" are the conditional ones appearing in the two displayed formulas,
and both are finite:
`E[φ|Z=z] = 2φ(z)`, `E[φ²|Z=z] = pφ(z+1)² + (1−p)φ(0)²`.

`φ ∉ L^∞` and `φ ∉ L^p(π_*)` for any `p` — as it must not be (§4):

```
Σ_{i≤5}  π_i|φ_i| = 21.33
Σ_{i≤20} π_i|φ_i| = 6.99e5
Σ_{i≤59} π_i|φ_i| = 3.84e17        →  E_π|φ| = +∞
```

### 2.4 The derivative, computed from the manuscript's definition

Not from `U` — from `R_b^H[H;ρ](z) = −log[ Σ_y ρ(y)e^{−H(y)}K(y,z) ] / [ Σ_y ρ(y)K(y,z) ]`,
which for this `K` has exactly two terms and needs no truncation. Central difference:

```
   z |   D_H R^H[φ](z)   |      2·φ(z)       |  abs err
   0 |      1.999999999780 |      2.000000000000 | 2.20e-10
   1 |      6.000000000227 |      6.000000000000 | 2.27e-10
   2 |     22.000000002738 |     22.000000000000 | 2.74e-09
   3 |     86.000000013339 |     86.000000000000 | 1.33e-08
   5 |   1365.999999845097 |   1366.000000000000 | 1.55e-07
   7 |  21845.999996119830 |  21846.000000000000 | 3.88e-06
```

The manuscript's **second** variation also holds on this unbounded `φ`:

```
   z |  D² (finite diff)  |  −Var_{Π_*}φ      | abs err
   0 |      −1.0000000827 |     −1.0000000000 | 8.3e-08
   2 |    −441.0000233990 |   −441.0000000000 | 2.3e-05
   4 | −116281.0056609786 |−116281.0000000000 | 5.7e-03
```

`λ = 2`, `b = 2`, `y = log 2 / log 2 = **+1.0 > 0** — RELEVANT`.

### 2.5 Scale consistency along the declared semigroup

The exponent is not an artifact of one `b`. Reversal is an anti-automorphism
(`‖reversal(K²) − U²‖_max = 0.0` on 400 states), so `Π_*^{(b)} = U^m` for `b = 2^m`:

```
 m=1  b=2 : U^m φ = 2^m φ, rel err 0.000e+00 ;  y = log(2^m)/log b = 1.000000
 m=2  b=4 : rel err 0.000e+00                 ;  y = 1.000000
 m=3  b=8 : rel err 0.000e+00                 ;  y = 1.000000
```

### 2.6 A declared Banach action space that hosts it — falsification condition (a)

RG-F1's condition (a) asks for "an action space whose norm is not dominated by `L^∞`
or `L^p(π_*)`" on which `D_H R_b^H` is bounded with spectral radius `> 1`. Take

```
c₀(w),   w(i) = 5^i ,   ‖ψ‖_w = sup_i |ψ(i)|/w(i) ,   ψ(i)/w(i) → 0.
```

This is precisely the standard weighted-sup (`V`-norm) space of Markov-chain theory,
and it is exactly the object `07b:671-673` asks for — "a declared Banach action space
with a Schauder basis `{ψ_A}` and continuous coordinate functionals `{ψ_A^*}`" — since
`c₀(w)` has the unit-vector Schauder basis with continuous coordinate functionals.

```
‖φ‖_w  = 1                        (φ(i)/w(i) = (2/3)(4/5)^i → 0, so φ ∈ c₀(w))
‖D_H R^H‖_{c₀(w)→c₀(w)} = 3.0     (bounded)
spectral radius on c₀(w) = p·θ = 2.5 > 1
```

`c₀(w)` is also closed under the *nonlinear* map, which `07b:633-635` demands
(computed in log space, no overflow):

```
 H = 0          ‖H‖_w =      0 → ‖R^H[H]‖_w =      0
 H = +0.3 φ     ‖H‖_w =    0.3 → ‖R^H[H]‖_w = 0.5557   (tail 1.4e-105 → 0)
 H = −0.3 φ     ‖H‖_w =    0.3 → ‖R^H[H]‖_w = 0.6443   (tail 2.3e-15  → 0)
 H = −1.0 φ     ‖H‖_w =      1 → ‖R^H[H]‖_w =  2.434   (tail 7.8e-15  → 0)
 H = 2 sin(i)   ‖H‖_w = 0.3366 → ‖R^H[H]‖_w = 0.5227   (tail 2.6e-106 → 0)
```

Both falsification conditions RG-F1 wrote for itself are therefore satisfied.

---

## 3. Where RG-F1's numerics were structurally incapable of seeing this

RG-F1's decisive evidence (`lens-rg.md:79-93`) is a **finite** `n = 6` state space plus
a 4000-pair sup-norm sweep. On a finite space every function is bounded, so
`L^∞` = all functions and the experiment can only ever sample the `L^∞` sector, where
the conclusion is true and forced. The sup-norm sweep tests nonexpansiveness *in the
sup norm*, which constrains nothing about an eigenvector of infinite sup norm. Neither
computation can bear on the "more generally" clause, and the finding treats them as if
they do. I reproduced both (`ρ(T) = 0.9999999999999993`, row sums `1`, nonexpansiveness
`≤ 0`) and they are correct and irrelevant to the claim they are cited for.

---

## 4. What genuinely survives, and its correct severity

### 4.1 The real defect is an undeclared word, not an empty branch

Both readings of `07b:756-759` are provable, and they give **opposite** answers:

| Reading | Statement | Verdict on the relevant branch |
|---|---|---|
| **(A) conditional** — what the text literally says | `E_{Π_*(dy\|z)}[e^{tφ}] < ∞` for `\|t\| < δ`, a.e. `z` | **inhabited**: `λ = 2`, `y = +1` (§2) |
| **(B) unconditional** — evidence-mass integrability | `∫ e^{tφ} dm_* < ∞` on a two-sided neighborhood of 0 | **empty**: `\|λ\| ≤ 1` provably |

Proof of (B), which is the sharp form of RG-F1's own insight and which I grant:
two-sided `∫e^{tφ}dm_* < ∞` ⟹ `φ ∈ L¹(π_*)`; `π_*` is `Π_*`-invariant (I verified
`π U = π` exactly); Jensen and invariance give
`∫|φ|dπ_* = ∫T|φ|dπ_* ≥ ∫|Tφ|dπ_* = |λ|∫|φ|dπ_*`, so `|λ| ≤ 1`.

Honesty about my counterexample under (B): the perturbed evidence mass
`Z(ε) = ∫e^{−εφ}dπ` is finite only **one-sidedly**:

```
 ε ≥ 0 :  Z = 0.3596 (ε=0.5), 0.7702 (ε=0.05), 1 (ε=0)   finite
 ε < 0 :  +INFINITE
```

So `φ` is admissible under reading (A) two-sidedly and under reading (B) only from the
right. By the theorem above **no** perturbation is two-sidedly (B)-admissible and
relevant — that class is genuinely closed. RG-F1 is therefore correct *conditional on a
reading the manuscript does not state*, and wrong under the reading the manuscript does
state.

That is a **MEDIUM** clarity/well-posedness finding: *declare the norm and say whether
the integrability is conditional or unconditional; the answer to "does this RG have
relevant directions?" flips on it.* It is not CRITICAL, it is not "a provably
unreachable case", and it does not license "the object it constructs provably has none
of them" (`lens-rg.md:135`).

### 4.2 The `isolated` qualifier — a narrower true residual

`07b:771` says "For an **isolated** eigenoperator". My `λ = 2` is in the point
spectrum but is **not** isolated: on `c₀(w)` the eigenfunction
`ψ_λ(i) = (1−p)/(λ−p) + [(λ−1)/(λ−p)](λ/p)^i` lies in the space iff `|λ| < pθ = 2.5`,
so the point spectrum is an open disk. Verified at 60 digits (mpmath):

```
 λ = 2.0    rel resid 0.000e+00   ‖v‖_w = 1        y = +1.0000
 λ = 2.4    rel resid 1.83e-61    ‖v‖_w = 1        y = +1.2630
 λ = 1+1i   rel resid 1.39e-61    ‖v‖_w = 1        y = +0.5000
 λ = −1.8   rel resid 1.46e-61    ‖v‖_w = 1        y = +0.8480
 λ = 0.25   rel resid 0.000e+00   ‖v‖_w = 1        y = −2.0000
 λ = 2.6    rel resid 2.36e-61    ‖v‖_w diverges   (correctly outside)
 ‖S^n‖_w^{1/n} = 2.500000 for n = 1,2,4,8,16      (r_ess = r = 2.5)
```

This is not an accident. **Structural theorem (mine).** Let `X` be a Banach lattice of
actions in which the constants `1` are quasi-interior (true for `L^∞`, every
`L^p(π_*)`, and `c₀(w)` — the ideal generated by `1` is `L^∞`, dense in `c₀(w)`), and
let `T = D_H R_b^H` be positive and unital (`T1 = 1`, from `07b:761-762`). If
`r(T) > r_ess(T)`, then `r(T)` is a pole of the resolvent with positive residue, so
there is `0 ≤ μ ∈ X*`, `μ ≠ 0`, with `T*μ = r(T)μ` [Schaefer, *Banach Lattices and
Positive Operators*, Ch. V; Nussbaum 1981]. Then
`μ(1) = μ(T1) = (T*μ)(1) = r(T)μ(1)`, so `r(T) ≠ 1` forces `μ(1) = 0`; quasi-interiority
of `1` and `μ ≥ 0` then force `μ = 0`. Contradiction. Hence

> **`r(T) > 1` implies `r(T) = r_ess(T)`.** Relevant directions, when they exist, live in
> the essential/continuous spectrum and are never isolated eigenoperators with spectral
> projections. In finite dimensions `r_ess = 0`, which is exactly why RG-F1's `n = 6`
> experiment returns `1` and must.

The counterexample realizes this precisely: `r(T) = r_ess(T) = 2.5`.

**And the manuscript already anticipates it.** `07b:768-770` reads "growth is classified
by the full spectrum and spectral radius of this derivative, **including continuous and
residual spectrum**", and `07b:774-776` restricts generalized eigenspaces to "finite
dimensions or … isolated point spectrum with the requisite spectral projections". The
sentence RG-F1 quotes as inflated is the one that correctly routes relevance to the
continuous spectrum. What survives is at most: *add one clause saying the `y_a > 0`
case of the isolated-eigenoperator sentence is empty on any action lattice with
quasi-interior constants, and that relevance therefore lives in the preceding sentence's
continuous spectrum.* **LOW**, and it is an addition, not a correction.

### 4.3 The "off by exactly +1" arithmetic — half right

I verified the Hermite half symbolically: `E[He_n(Y₁)|Z=z] = b^{−n/2}He_n(z)` (sympy
residual **exactly 0** for `b ∈ {2,3,4}`, `n ∈ {1..4}`), so `y_op = −n/2`,
`y_ext = 1 − n/2`, difference `= +1` exactly, checked for `n ∈ {1,2,3,5}`,
`b ∈ {2,4,8}` to `< 1e-13`. **Correct — inside the `α`-stable block-sum sector.**

As a general claim about the manuscript's exponents it is **false**. My counterexample
has `λ = 2` with no block sum, no extensive perturbation, and no volume factor
anywhere; there is no "+1" to restore. "Every exponent is short by exactly +1, the
volume factor" (`lens-rg.md:120-123`) generalizes one sector to the whole construction.

### 4.4 The chapter-7 cross-check (RG-F1 point 6) is wrong on its stated reason

`lens-rg.md:124-127` claims the two chapters' `y_a` "agree here only because RG-F1
forces `μ₀ = 1` (the constants)". `eq:rg-projective-dimensions` (`07:407-414`) is for a
**homogeneous positive endomorphism at a fixed ray**, unnormalized, where `μ₀` is the
radial eigenvalue and is generically not 1: the manuscript's own worked case at
`10:271-272` has `μ₀ = b²` (coupling sector) and `μ_a = b` (self sector), ratio `1/b`
(`eq:grg-sector-gap`, `10:274-277`). Dividing by `μ₀` is exactly how chapter 7 removes
the radial/extensive direction that RG-F1 says is missing. So chapter 7 does not
"already encode the conclusion"; it is the projective tier RG-F1's own fix #2 asks to be
added, and it is already there.

(A *different* and better-targeted finding is available at `07:407-414`: for a positive
homogeneous endomorphism at an **interior** fixed ray, the differential is nonnegative
with strictly positive eigenvector `x_*`, so Perron–Frobenius gives `μ₀ = r(D)`, hence
`|ρ_a| ≤ 1` and `y_a ≤ 0` there too. That is a real observation about `07:407-414`, it
is not what RG-F1 says, and it does not transfer to `07b:756-777`.)

---

## 5. Disposition of RG-F1 as filed

| RG-F1 element | `lens-rg.md` line | Disposition |
|---|---|---|
| Severity **critical** | `:59` | **refuted** — downgrade to medium |
| "the `y_a > 0` branch … is EMPTY" | `:45`, `:64` | **refuted** — explicit `λ = 2`, `y = +1` |
| "no admissible eigenoperator can be relevant" | `:94-100` | **refuted** — proved only for `L^∞`, `L^p(π_*)` |
| "On `L^∞` (the declared class)" | `:95` | **misquote** — `07b:756-759` declares a strictly larger class |
| "Prose inflates" / status inflation | `:61-64` | **refuted** — a trichotomy is a definition; `07b:768-770` and `07b:774-776` already fence it |
| "the object it constructs provably has none of them" | `:135` | **refuted** |
| "every exponent is off by exactly +1" | `:120-123` | **half** — true in the stable sector, false in general |
| ch-7 cross-check, "`μ₀ = 1`" | `:124-127` | **refuted** — `μ₀ = b²` at `10:271` |
| unitality, Crandall–Tartar, `L^p(π_*)` bound, finite-dim `ρ = 1` | `:68-100` | **all correct** |
| "the spectrum is never computed anywhere for any sector" | `:645-649` | **correct**, and is the honest finding here |
| `JonaLasinio2001` uncited | `:153-156` | **correct** (`references.bib:1103`, 0 `.tex` citations) |
| Fix #2 (move classification to coupling coordinates) | `:144-147` | **already present** at `07:407-414` / `10:271-277`; reduces to a missing cross-reference |
| Fix #4 (`ψ_A` vs `ψ_a` clash) | `:151-152` | **correct**, independent of the rest |

## 6. Replacement finding I would file instead

> **RG-F1′ — MEDIUM — the perturbation class and the action-space norm are undeclared,
> and the relevant/irrelevant verdict flips on them.**
> `07b:756-759` admits both bounded and "conditionally exponentially integrable"
> perturbations, and `07b:768-771` classifies growth by "the full spectrum and spectral
> radius of this derivative" without declaring a norm. The spectrum of a conditional
> expectation operator is space-dependent: on `L^∞` and on every `L^p(π_*)` it lies in
> the closed unit disk and `y_a ≤ 0` always (Crandall–Tartar plus Jensen; verified,
> §1); on the weighted space `c₀(5^i)` — a legitimate `07b:671-673` Banach space with a
> Schauder basis, closed under `R_b^H` — the same operator has spectral radius `2.5` and
> a relevant eigenvalue `λ = 2`, `y = +1` (§2). Two provable, opposite answers inside one
> undeclared choice.
> **Fix.** (i) Declare the norm. (ii) Say whether "conditional exponential integrability"
> is conditional or unconditional; if unconditional, add the two-line Jensen proof that
> `|λ_a| ≤ 1` and state that the classification is then infrared-only. (iii) Add the
> provable structural clause: `R_b^H` is order preserving and additively homogeneous
> hence sup-norm nonexpansive, `D_H R_b^H` is positive unital, and on any action lattice
> with quasi-interior constants `r > 1` forces `r = r_ess` — so a relevant direction is
> never an isolated eigenoperator, which is why `07b:768-770` must name the continuous
> spectrum. (iv) Cross-reference `eq:rg-projective-dimensions` (`07:410-413`) and
> `eq:grg-sector-gap` (`10:274-277`) as the projective tier where `μ₀ ≠ 1`.
> (v) Cite `JonaLasinio2001`. (vi) Resolve `ψ_A` / `ψ_a`.

## 7. Files

- Scripts (all `C:/Python314/python.exe`, numpy 2.4.4 / sympy 1.14.0 / mpmath dps=60, seed 20260802):
  - `C:/Users/CHRISA~1/AppData/Local/Temp/claude/C--Users-chris-and-christine-Desktop-Research/21b92b09-6f32-47fa-8f90-6f5faa59e5a3/scratchpad/rgf1_attack.py` (checks 0–9)
  - `C:/Users/CHRISA~1/AppData/Local/Temp/claude/C--Users-chris-and-christine-Desktop-Research/21b92b09-6f32-47fa-8f90-6f5faa59e5a3/scratchpad/rgf1_attack2.py` (checks 10–14)
  - `C:/Users/CHRISA~1/AppData/Local/Temp/claude/C--Users-chris-and-christine-Desktop-Research/21b92b09-6f32-47fa-8f90-6f5faa59e5a3/scratchpad/rgf1_spec.py` (check 12b, 60-digit)
  - `C:/Users/CHRISA~1/AppData/Local/Temp/claude/C--Users-chris-and-christine-Desktop-Research/21b92b09-6f32-47fa-8f90-6f5faa59e5a3/scratchpad/rgf1_reading.py` (check 15)
- Settled ground honored: RG-2 (`00-settled-ground.md:93-96`) is not re-litigated; the
  operator construction is taken as given and the attack is on the exponent
  classification built on top of it.
