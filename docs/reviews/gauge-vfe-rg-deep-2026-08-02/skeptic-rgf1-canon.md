# Adversarial skeptic C — external-literature audit of RG-F1

**Angle.** Does the primary literature support RG-F1? Every load-bearing claim below is sourced to a
primary paper (URL given) or to an executed computation, never to the manuscript or to `lens-rg.md`.

**Target.** `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex:756-777`
(`eq:rg-linearized-action` and the classification sentence), tagged `\status{ESTABLISHED}` at
`07b:777` and re-asserted in `cor:rg-complete-analytic-tier` (`07b:866-871`).

---

## VERDICT

**SURVIVES-AT-LOWER-SEVERITY.**

Downgrade **CRITICAL → MEDIUM-HIGH**, and rename the finding. The correct finding is *not* "the
relevant branch is empty"; it is:

> **The manuscript never declares the norm on its action space, and the entire content of its
> relevant/marginal/irrelevant trichotomy depends on that undeclared choice. On every norm dominated
> by `L^∞` or `L^p(π_*)` the classification is vacuous (all `y_a ≤ 0`); on the natural weighted
> Banach spaces the operator has unbounded spectral radius and the classification is ill-posed; and
> in neither case are these the coordinates in which the literature defines relevance, because the
> extensive/coupling structure that carries the volume factor is never declared.**

Per-claim adjudication:

| Sub-claim | Verdict |
|---|---|
| (a) unital averaging ⟹ spectral radius 1 ⟹ relevance impossible | **REFUTED as stated.** Explicit counterexample constructed below inside the manuscript's own hypotheses. Survives only in the restricted form "no eigenoperator in `L^∞` or `L^p(π_*)` is relevant." |
| (b) relevant mode is extensive, eigenvalue carries a volume factor, `b^{1-n/2}` at the Gaussian/CLT fixed point | **CONFIRMED verbatim** by Jona-Lasinio (2001) eqs. (2.14) and (5.11), and by Fisher (1998) eqs. (43), (45)-(48). |
| (c) every manuscript exponent is short by exactly `+1` | **PARTIALLY CONFIRMED.** Arithmetic correct in the manuscript's own `α`-stable sector; but the manuscript computes no exponent anywhere, so the claim is counterfactual, and the general deficit is `d`, not `1`. |
| (d) `JonaLasinio2001` is the construction the manuscript needs | **CONFIRMED and UNDERSTATED.** It supplies more than RG-F1 claims. |
| Brief's key check: did the finding conflate averaging with block+rescale? | **NO — the conflation hypothesis is refuted.** Verified by construction and numerically. |

---

## 1. The brief's most important check: no conflation occurred

The hypothesis was that RG-F1 mistook the bare averaging step for the full RG map (block + rescale).
It did not, and I can show this constructively rather than by argument.

`eq:rg-measure-pair-map` (`07b:613-617`) puts the identification/rescaling `I_b` **inside**
`K_b = C_b I_b` and applies it to measures. So the derivative at a fixed pair is the conditional
expectation of the *composite* map. Two facts follow:

1. **Algebraically.** If `I_b` contains a deterministic dilation `S`, then
   `d(S_# m)/d(S_# ρ) = (dm/dρ)∘S^{-1}`, so the composite derivative is a Markov operator composed
   with a relabeling — still positive, still unital. A uniform mass factor cancels in the
   Radon–Nikodym ratio.
2. **Numerically.** I inserted arbitrary dilations `c ∈ {0.5, 1, 2, 7.3}` and arbitrary uniform mass
   factors `{0.37, 1, 12}` into `I_b` and re-measured unitality of `D_H R_b^H`:
   `max|rowsum − 1| ≤ 1.11e-15` in all twelve combinations.

I then built a concrete instance satisfying **every** declared hypothesis of chapter 7b, in which the
rescaling is unambiguously present, and which *is* the block-sum RG:

> Common standard-Borel space `Y = ℝ`. `K_b(y,dz) =` law of `Z = b^{-1/2}(y + Y_2 + … + Y_b)` with
> `Y_i` iid `N(0,1)` — that is, the block sum `C_b` followed by the `b^{-1/2}` rescale `I_b`. This is
> the Mehler/Ornstein–Uhlenbeck kernel with correlation `r = b^{-1/2}`.

Measured: Markov to `2.2e-16`; `ρ_* K_b = ρ_*` for `ρ_* = N(0,1)` to `4.2e-17`; the semigroup
`K_2 K_2 = K_4` of `eq:rg-kernel-semigroup` to `1.1e-15`. `H_* = 0` is a fixed action. Then

```
b=2:  D_H R^H unital to 8.9e-16, positive, spectral radius 1.0000000000000004
      eigenvalues   1, 0.7071, 0.5, 0.3536, 0.25, 0.1768, 0.125   ( = b^{-n/2} )
      manuscript y  0, -0.5, -1.0, -1.5, -2.0, -2.5, -3.0         ( = -n/2 )
      Wilson    y   1.0, 0.5, 0.0, -0.5, -1.0, -1.5, -2.0         ( = 1-n/2 )
b=4:  identical exponents; spectral radius 1.0000000000000002
```

So the deficit of exactly one is reproduced in a realization where block *and* rescale are both
inside the map. RG-F1 did not confuse the two steps.

---

## 2. Sub-claim (b) — CONFIRMED verbatim by primary sources

### 2.1 Jona-Lasinio 2001 states the exact spectrum RG-F1 claims

`arXiv:cond-mat/0009219`, published as Phys. Rep. **352** (2001) 439–458.
<https://arxiv.org/abs/cond-mat/0009219>

Section II, block-sum RG for the CLT. Eq. (2.13) gives the linearized operator
`(Lh)(x) = 2π^{-1/2}∫dy e^{-y²} h(y + x2^{-1/2})`, and then, verbatim:

> "The eigenvalues of `L` are
> `λ_k = 2^{1−k/2}`  (2.14)
> and the eigenfunctions the Hermite polynomials."

That is `b^{1−k/2}` at `b = 2` — RG-F1's claimed eigenvalue, in the canonical source, as a displayed
equation. Jona-Lasinio also fixes the trichotomy in the same place: "upon iteration of the RG
transformation they will contract to zero exponentially as the corresponding eigenvalues are `< 1`",
and in §III "for `2 > c > 2^{1/2}` the eigenvalues `λ_0` and `λ_1` are `> 1`."

### 2.2 The volume factor is written explicitly, *inside a conditional expectation*

This is the decisive corroboration, because it concerns the same operator the manuscript uses.
Jona-Lasinio §V, self-similar random fields on `ℤ^d`:

> `ξ^n_j = (R_{α,n} ξ)_j = n^{−dα/2} Σ_{s∈V^n_j} ξ_s`  (5.1)

with `V^n_j` a block of `n^d` sites — an **extensive** sum. He then writes, for a deformation
`P_G(1+h)`:

> `R*_{α,n} P_G h = E(h|{ξ^n_j}) R*_{α,n} P_G = E(h|{ξ^n_j}) P_G({ξ^n_j})`  (5.10)
> "The conditional expectation on the right hand side of (5.10) will be called **the linearization
> of the RG at the fixed point `P_G`**."

That is exactly `eq:rg-linearized-action`: `D_H R_b^H[φ](z) = E_{Π_*(dy|z)}φ(Y)`. Same object, same
name. And its eigenvalue equation is

> `E(H_k|{ξ^n_j}) = n^{[k(α/2−1)+1]d} H_k({ξ^n_j})`  (5.11)

The **`+1` inside the bracket, multiplied by `d`, is the volume factor `n^d`** — printed, in the
canonical reference, inside the eigenvalue of a conditional-expectation operator. Setting `α = 1`
(the CLT case, per Jona-Lasinio's own §V discussion) and `d = 1` reproduces (2.14) exactly; I
verified the algebraic identity `[k(α/2−1)+1]d = 1 − k/2` for `k = 0…5` at `α=1, d=1`. The `H_k` are
"appropriate infinite dimensional generalizations of Hermite polynomials" — extensive field
functionals, not bounded functions.

### 2.3 Fisher (1998) states the same structure in the Wilsonian language

Rev. Mod. Phys. **70**, 653 (1998).
<https://link.aps.org/doi/10.1103/RevModPhys.70.653>
(full text: <https://harvest.aps.org/v2/journals/articles/10.1103/RevModPhys.70.653/fulltext>)

- Extensivity: "A physical system of interest is then specified by its Hamiltonian `H[{s_x}]` … which
  is usually just **a spatially uniform sum of local operators**."
- Linearization, eq. (45): `R_b[H̄* + gQ] = H̄* + g L_b Q + o(g)`.
- Eigenoperators, eq. (47): `L_b Q_k = Λ_k(b) Q_k`, with `Λ_k(b) = b^{λ_k}`, and the parenthetical
  "eigenoperators, say `Q_k` (**which will be 'partial Hamiltonians'**)" — i.e. themselves extensive.
- Eq. (48): `H̄ ≈ H̄* + Σ_k g_k Q_k`, where "the expansion coefficient `g_k` then represents the
  thermodynamic field **conjugate to** the 'critical operator' `Q_k`", and "under renormalization
  each `g_k` varies simply as `g_k(l) ≈ b^{λ_k l} g_k(0)`."
- Trichotomy: "the sign of a given `φ_j` and, hence, of the corresponding `λ_j` determines the
  relevance (for `λ_j > 0`), marginality (for `λ_j = 0`), or irrelevance (for `λ_j < 0`)."
- The volume factor appears explicitly in the free-energy flow, eq. (43):
  `f(t,h,…) ≡ f[H̄] = b^{−dl} f[H̄(l)]`, and in hyperscaling, eq. (50): `2 − α = d/λ_1`.

So relevance in the literature is a statement about the **conjugate coupling `g_k`**, on a space of
**extensive partial Hamiltonians**, with `d` present. RG-F1's fix #2 (classify the spectrum in
coupling coordinates) is what the literature actually does.

### 2.4 The rigorous literature says the infinite-volume Hamiltonian is not a function

van Enter, Fernández & Sokal, J. Stat. Phys. **72** (1993) 879; `arXiv:hep-lat/9210032`.
<https://arxiv.org/abs/hep-lat/9210032>

Abstract, verbatim:

> "we show that the RG map, **defined on a suitable space of interactions (= formal Hamiltonians)**,
> is always single-valued and Lipschitz continuous on its domain of definition."

§2.2, verbatim:

> "the Hamiltonian `H(ω)` for an infinite-volume system is **an ill-defined object**. Therefore we
> must proceed more cautiously. We define first the concept of an *interaction*, which corresponds
> roughly to the idea of a 'formal Hamiltonian' or a 'set of coupling constants'. … The (meaningless)
> Hamiltonian of an infinite-volume system is written formally as a **sum of terms corresponding to
> various finite subsets of the lattice**."

Definition 2.1: "An interaction … is a family `Φ = (Φ_A)_{A∈S}` of functions `Φ_A : Ω → ℝ`."

This is the same indexing as the manuscript's own Möbius potentials `Φ_A` (`07b:157-168`,
`eq:rg-mobius-potentials`). The manuscript already possesses the coordinates in which relevance is
defined; it performs its spectral analysis in the wrong ones.

### 2.5 The `α`-stable exponent `y = 1/α`

I did not find a literature statement in the manuscript's exact parameterization, so I proved it. For
`Z = b^{-1/α}Σ_{i=1}^b Y_i` (the manuscript's own `07b:783-784`), the identity `Σ_i Y_i = b^{1/α}Z`
is deterministic, so `E[Σ_i Y_i | Z=z] = b^{1/α} z` **exactly**; numerically
`max|Σ_i Y_i − b^{1/α}Z| = 9.1e-13` over 2·10^5 draws at `α=1.5, b=8` (floating point only). Hence the
coupling conjugate to the extensive magnetization flows with `λ = b^{1/α}`, `y = 1/α`. Consistency:
`y = d − Δ` with `d = 1` gives `Δ = 1 − 1/α`, and at `α = 2` this returns `Δ = 1/2` and `y = 1/2`,
matching the Hermite `n = 1` mode. Jona-Lasinio's (5.11) at `k = 1` is the same statement in his
conjugate parameterization (`n^{dα/2}` = the reciprocal of his normalization `n^{−dα/2}`), so the
mechanism is corroborated even though the symbol `α` denotes different quantities in the two
conventions. RG-F1's `y = 1/α` is correct.

### 2.6 Independent recomputation of RG-F1's arithmetic

Mehler identity, Monte Carlo `N = 4·10^6`, regression coefficient of `He_n(Y_1)` on `He_n(Z)`:

```
b=2  n=1 0.70719 / 0.70711   n=2 0.50047 / 0.50000   n=3 0.35466 / 0.35355
b=4  n=1 0.50015 / 0.50000   n=2 0.25021 / 0.25000   n=3 0.12523 / 0.12500
b=8  n=1 0.35395 / 0.35355   n=2 0.12495 / 0.12500   n=3 0.04450 / 0.04419
```
(MC / theory `b^{-n/2}`). Extensive vs intensive deficit `= log b / log b = +1.0` for every
`(b, n)` tested. RG-F1's numbers reproduce.

---

## 3. Sub-claim (a) — REFUTED as stated

RG-F1's headline is that the `y_a > 0` branch is **empty** and the classification therefore vacuous.
That is false. I constructed the object RG-F1's own falsifier (c) says it could not construct:

> "(c) a concrete `(K_b, ρ_*, H_*, ψ_a)` with `|λ_a| > 1` and `ψ_a` in a declared class is exhibited.
> **I could not construct (c)**, and the argument in (1) shows it cannot exist for bounded `ψ_a`."
> — `lens-rg.md:163-165`

Take the instance of §1 above (`Y = ℝ`, `K_b` = block-sum-plus-rescale = Mehler with `r = b^{-1/2}`,
`ρ_* = N(0,1)`, `H_* = 0`; Markov, invariant, exact semigroup, `eq:rg-linearization-positive-likelihood`
holds with `L^c_*(z) ≡ 1`). Set

```
ψ(y) = e^{y²/2}   ( = √(2π) / γ(y), the reciprocal Gaussian density )
```

Then, in closed form and confirmed to 40 significant digits,

```
D_H R_b^H[ψ](z) = E[e^{Y²/2} | Z=z]  =  (1/r) e^{z²/2}  =  b^{1/2} ψ(z)
```

Symbolic check (sympy): `E[e^{Y²/2}|Z=z] − (1/r)e^{z²/2} = 0` for `r > 0`. Numeric check (mpmath,
40 dps), relative error vs `b^{1/2}e^{z²/2}`:

```
b=2  z=-2.30 3.4e-41   z=0 1.1e-41   z=0.90 2.3e-41   z=2.30 3.4e-41
b=4  z=-2.30 0.0       z=0 0.0       z=0.90 0.0       z=2.30 0.0
b=8  z=-2.30 3.4e-41   z=0 1.1e-41   z=0.90 2.3e-41   z=2.30 3.4e-41
```

So `λ = b^{1/2}` and `y_a = log|λ|/log b = +1/2 > 0` — a **relevant** eigenoperator of the
manuscript's own linearized RG.

**It sits in a legitimate declared Banach space.** Let `B = {φ : ‖φ‖_B := sup_y |φ(y)| e^{-y²/2} < ∞}`.
Then `‖D_H R_b^H φ‖_B ≤ ‖φ‖_B sup_z e^{-z²/2}(1/r)e^{z²/2} = b^{1/2}‖φ‖_B`, attained at `ψ` (with
`‖ψ‖_B = 1`). So the operator is **bounded on `B` with norm exactly `b^{1/2}`, and its spectral
radius is at least `b^{1/2} > 1`.** This is precisely RG-F1's falsifier (a): "an action space whose
norm is not dominated by `L^∞` or `L^p(π_*)` [on which the operator is] bounded … with spectral
radius `> 1`."

**It satisfies the manuscript's other side conditions.** `H_* + εψ` is finite-valued everywhere, so
it lies in a finite-valued action space (`07b:749-750`). `e^{-εψ}ρ_*` is a positive measure with
`0 < Z < ∞` for `ε > 0`, so `thm:rg-complete-effective-theory`'s positive-finite-evidence hypothesis
(`07b:817`) holds. `span{ψ}` is invariant under `R_b^H` at first order, so
`eq:rg-discrete-beta-functional`'s "declared vector space of finite-valued actions closed under this
map" (`07b:633-635`) is satisfiable on it.

**The pathology is worse than a single relevant mode.** The family `φ_m(y) = y^m e^{y²/2}` is
triangular under the operator with diagonal `r^{-(m+1)} = b^{(m+1)/2}`:

```
b=4:  m=0 λ=2, y=+0.5 | m=1 λ=4, y=+1.0 | m=2 λ=8, y=+1.5 | m=3 λ=16, y=+2.0 | …
```

Spectral radius `= +∞` on the polynomially weighted extension. So the manuscript's sentence "growth
is classified by the full spectrum and spectral radius of this derivative" is not merely vacuous — it
is **ill-posed** until a norm is declared, and swings between "all exponents `≤ 0`" and "unbounded
spectrum" depending on a choice the manuscript never makes.

### 3.1 Why RG-F1 missed this, and what it means for its evidence

RG-F1's numerical evidence (its item 2) is a **finite** `n = 6` state space. On a finite state space
every function is bounded, so `L^∞` is everything and unitality trivially caps the spectrum. The
method was structurally incapable of finding its own falsifier. The phenomenon requires a
non-compact state space — which is exactly what the manuscript's own `α`-stable sector at
`07b:783-787` supplies.

### 3.2 What of claim (a) does survive

The restricted statement holds and is provable:

- `D_H R_b^H` is positive and unital, so `‖·‖_{∞→∞} = 1`, so `r(T)|_{L^∞} = 1` exactly (the constants
  are an eigenvector). Verified: `max|rowsum − 1| ≤ 8.9e-16`, spectral radius `1.0000000000000004`.
- At a fixed pair `π_*` is `K_b`-invariant, so Jensen gives an `L^p(π_*)` contraction for every
  `p ∈ [1,∞]`, so any eigenoperator in `L^1(π_*)` has `|λ| ≤ 1`.
- The manuscript's *licensed perturbation class* — "`φ ∈ L^∞` (or … conditional exponential
  integrability in a neighborhood of zero **and the first two required moments**)" (`07b:756-759`) —
  forces at most quadratic growth (a cubic already fails conditional exponential integrability at
  both tails), hence lies inside `L^2(π_*)`. On that class RG-F1's conclusion is airtight, and my
  counterexample `ψ = e^{y²/2}` is correctly excluded: `E[e^{θψ(Y)}|Z] = ∞` for every `θ > 0`.

So the real defect is a **scope mismatch inside `07b:756-777`**: sentence one names a perturbation
class licensing the variation formula; sentence two takes the spectrum on "an infinite-dimensional
Banach or Hilbert action space" that is never identified with that class and never normed. Under one
reading the trichotomy is vacuous; under the other it is unbounded. That is a real `ESTABLISHED`-tag
defect — but it is a scope/declaration defect, not the vacuity theorem RG-F1 asserts.

---

## 4. Sub-claim (c) — PARTIALLY CONFIRMED

"Every exponent the manuscript computes is short by exactly `+1`" fails on two counts.

1. **The manuscript computes no exponents.** `lens-rg.md:645-648` says so itself: "It is never
   computed anywhere in the manuscript, for any sector." The claim is therefore counterfactual —
   about what the formula *would* give — and should be stated that way.
2. **The deficit is `d`, not `1`.** Jona-Lasinio (5.11) puts the volume factor at `n^{+1·d}`; Fisher
   (43) at `b^{-dl}`. The deficit is `1` only when `b` is the volume/count ratio (`b^d` with the
   linear factor absorbed). In the manuscript's own `α`-stable sector `b` *is* the summand count
   (`07b:783-784`, `Σ_{i=1}^b Y_i`), so `+1` is right there — but `10:144` and `07:448-453` also use
   `b` as a cardinality while `eq:rg-heat-susceptibility` uses a length-based exponent, which is
   RG-F8's own open point. RG-F1's `+1` silently assumes what RG-F8 says is undeclared.

---

## 5. Sub-claim (d) — CONFIRMED, and RG-F1 undersells it

`references.bib:1103` is `@article{JonaLasinio2001}`, Phys. Rep. 352:439–458, "Renormalization group
and probability theory". Verified against the primary record: the arXiv preprint is
`cond-mat/0009219`, DOI `10.1016/S0370-1573(01)00042-4`, matching volume and pages
(<https://arxiv.org/abs/cond-mat/0009219>). A grep over `manuscripts/gauge_vfe_rg/` for
`JonaLasinio|Jona-Lasinio|Jona` returns **no matches** — RG-F1's "present but never cited" is
confirmed.

Beyond RG-F1's claim, the paper also supplies two things chapter 7b needs and lacks:

1. **The two-space eigenvalue formalism that resolves the endomorphism problem.** §VII interprets the
   conditional expectation "as a linear transformation from the linear space tangent to `P` to the
   linear space tangent to `R*_{α,n}P`" and defines a **generalized** eigenvalue equation
   `E_P(H^P_k|{ξ^n_j}) = λ_k(n,P) H^{R*_{α,n}P}_k({ξ^n_j})` (7.4). This is the correct replacement for
   `eq:rg-linearized-action`'s ordinary `D_H R_b^H[ψ_a] = λ_a ψ_a` on one undeclared space.
2. **A cocycle law for the reference-dependent eigenvalues.** Eq. (7.5):
   `λ_k(m, R*_{α,n}P) λ_k(n,P) = λ_k(mn, P)`. This is the reference-direction transformation law that
   RG-F5 correctly reports as missing from `eq:rg-discrete-beta-functional`, and it is in the same
   uncited paper. It also matches `07b:624`'s own "typed cocycle rather than an autonomous semigroup".

Jona-Lasinio §II further remarks that "the Gaussian is an example of what is called in probability
theory a stable distribution. These are distributions which are fixed points of convolution equations
and, with the exception of the Gaussian, have infinite variance" — directly on `07b:783-790`.

---

## 6. Recommended replacement for RG-F1

Retitle: **"The action-space norm is never declared, so the exponent classification has no determinate
content; the extensivity that carries Wilsonian relevance is absent."** Severity MEDIUM-HIGH.

Fixes, revised from RG-F1's:

1. **Do not** state RG-F1's fix #1 as written. "`D_H R_b^H` is a positive unital operator with
   spectral radius exactly 1, consequently no eigenoperator is relevant" is false without the
   qualifier. State instead: *`R_b^H` is order preserving and additively homogeneous, hence sup-norm
   nonexpansive; `D_H R_b^H` is positive and unital, hence has `L^∞` operator norm 1 and, at a fixed
   pair, is an `L^p(π_*)` contraction for every `p`. Therefore every eigenoperator in the declared
   perturbation class of `07b:756-759` has `|λ_a| ≤ 1` and `y_a ≤ 0`.* Then note that on weighted
   spaces outside that class the spectral radius can be `+∞` (`ψ_m(y) = y^m e^{y²/2}`,
   `λ_m = b^{(m+1)/2}` for the Gaussian block-sum realization), so the space **must** be declared.
2. Keep RG-F1's fix #2 (classify in the coupling coordinates `M_{AB} = ⟨ψ*_A, E_{Π_*}[ψ_B|Z=·]⟩`) and
   cite van Enter–Fernández–Sokal for the reason: the RG map is properly defined on a space of
   interactions `Φ = (Φ_A)`, which the manuscript already has at `eq:rg-mobius-potentials`.
3. Keep fix #3 (declare the extensivity/per-volume normalization) and cite Jona-Lasinio (5.1),
   (5.10), (5.11) plus Fisher (43), (45)–(48). State the deficit as `d`, not `1`, and cross-reference
   RG-F8 on whether `b` is linear or volume.
4. Keep fix #4 (`ψ_A` vs `ψ_a` symbol clash).
5. Cite `JonaLasinio2001` at `eq:rg-linearized-action` **and** at `eq:rg-discrete-beta-functional`
   (for the §VII cocycle, which is RG-F5's missing law).

---

## 7. Sources

- G. Jona-Lasinio, *Renormalization group and probability theory*, Phys. Rep. **352** (2001) 439–458;
  `arXiv:cond-mat/0009219`. <https://arxiv.org/abs/cond-mat/0009219> — eqs. (2.13), (2.14), (5.1),
  (5.10), (5.11), (7.4), (7.5).
- M. E. Fisher, *Renormalization group theory: Its basis and formulation in statistical physics*,
  Rev. Mod. Phys. **70** (1998) 653. <https://link.aps.org/doi/10.1103/RevModPhys.70.653>;
  full text <https://harvest.aps.org/v2/journals/articles/10.1103/RevModPhys.70.653/fulltext> —
  eqs. (23), (24), (43), (45), (47), (48), (50).
- A. C. D. van Enter, R. Fernández, A. D. Sokal, *Regularity properties and pathologies of
  position-space renormalization-group transformations*, J. Stat. Phys. **72** (1993) 879;
  `arXiv:hep-lat/9210032`. <https://arxiv.org/abs/hep-lat/9210032> — abstract; §2.2; Definition 2.1.

## 8. Executed verification

Interpreter `C:/Python314/python.exe` (numpy 2.4.4, sympy 1.14.0, mpmath, pypdf); no torch, no CUDA
claim. Scratchpad:
`C:/Users/CHRISA~1/AppData/Local/Temp/claude/C--Users-chris-and-christine-Desktop-Research/21b92b09-6f32-47fa-8f90-6f5faa59e5a3/scratchpad/`
(`jona.txt`, `fisher.txt`, `vefs.txt` are the extracted primary-source texts).

Checks run: Mehler conditional-expectation identity (MC, `N = 4·10^6`); extensive-vs-intensive
deficit table; Jona-Lasinio (5.11) reduction to `b^{1−k/2}`; `α`-stable identity
`Σ_i Y_i = b^{1/α}Z`; construction and validation of the Mehler realization (Markov `2.2e-16`,
invariance `4.2e-17`, semigroup `1.1e-15`, unitality `8.9e-16`, spectral radius `1.0000000000000004`,
Hermite spectrum `b^{-n/2}`); unitality under twelve dilation/mass insertions
(`max|rowsum−1| ≤ 1.11e-15`); symbolic and 40-dps numeric confirmation of
`D_H R_b^H[e^{y²/2}] = b^{1/2}e^{y²/2}`; triangular family `y^m e^{y²/2}` with
`λ_m = b^{(m+1)/2}`; grep for `JonaLasinio|Jona-Lasinio|Jona` over `manuscripts/gauge_vfe_rg/`
(no matches).
