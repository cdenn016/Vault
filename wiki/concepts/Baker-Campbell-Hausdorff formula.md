---
type: concept
title: Baker-Campbell-Hausdorff formula
aliases:
  - BCH
  - BCH formula
  - Baker-Campbell-Hausdorff
  - Baker–Campbell–Hausdorff
  - Baker–Campbell–Hausdorff formula
tags:
  - cluster/gauge-theory
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-06-18
updated: 2026-07-10
---

# Baker-Campbell-Hausdorff formula

## Definition

The **Baker–Campbell–Hausdorff (BCH) formula** is a local/formal logarithm of a product of exponentials. It does not require or imply that the exponential map is onto the entire group. [[gl-k-attention-2026-07-09-review-revision]]

$$
Z = \log\big(\exp X \exp Y\big) = X + Y + \tfrac12[X,Y] + \tfrac1{12}\big([X,[X,Y]] - [Y,[X,Y]]\big) - \tfrac1{24}[Y,[X,[X,Y]]] + \cdots
$$

The remarkable structural fact — **Lie's theorem** in its BCH form — is that every term of $Z$ can be written using only the bracket $[\cdot,\cdot]$, with rational coefficients that are *universal*: they depend on neither the particular algebra nor the particular $X, Y$, only on their formal commutator structure. No products of $X$ and $Y$ outside of brackets ever appear. The first correction $\tfrac12[X,Y]$ already carries the whole moral of the formula: it is exactly the noncommutativity of the group, lifted into the algebra. If $X$ and $Y$ commute, so that $[X,Y]=0$, every bracket term vanishes and the series collapses to the elementary $Z = X+Y$, recovering the scalar law $e^{x}e^{y}=e^{x+y}$.

## Why it matters here

The VFE transformer parameterizes its gauge degrees of freedom **in the Lie
algebra, not in the group**. Its gauge group is the block general-linear group
GL($k$) (`gauge_group: block_glk`), and a represented gauge element is generated
from $\phi \in \mathfrak{gl}(k)$ by $g=\exp(\phi)$. This is an algebra-first
parameterization, not a claim that every GL($k$) element has a real logarithm or
that exp and log are globally inverse. Locally, combining represented elements
$\exp(\phi_1)\exp(\phi_2)$ can be expressed by a BCH algebra coordinate $Z$
before exponentiation or another group-valued retraction.

The configuration uses BCH twice. In `phi_retract_mode: bch`, it updates the
stored algebra coordinate by a truncated approximation to
$\log(\exp(\phi)\exp(\Delta\phi))$. BCH itself maps two algebra elements to a
new algebra coordinate; the group element is obtained only after exponentiation
or a separately specified group-valued retraction. Calling the whole update a
retraction requires the first-order retraction conditions of
[[absil-2008-optimization-matrix-manifolds]] and is not implied by the name
“BCH.” In `pos_phi_compose: bch`, order-four BCH similarly composes learned
positional generators locally in algebra coordinates.

Small configured scales motivate finite BCH truncation but do not certify its error on realized updates; the truncated operation remains approximate. [[gl-k-attention-2026-07-09-review-revision]]

## Details

**Convergence and exactness.** As a formal series BCH always exists, but its *numerical* convergence requires $X$ and $Y$ to be sufficiently small — concretely, the series converges when $\|X\|+\|Y\|$ is below a bound depending on the algebra (for matrices, a bound around $\log 2$ in operator norm is a standard sufficient condition). Two regimes make truncation exact rather than approximate. In a **nilpotent** Lie algebra the iterated brackets eventually vanish identically, so the series terminates and BCH is an exact finite polynomial — no truncation error at all. More generally, when $X$ and $Y$ are themselves small, the *tail* past a given order is bounded by the next power of $\|X\|+\|Y\|$, which is the situation the model engineers with its small `phi_scale` and `pos_phi_scale`.

**Truncation order versus accuracy and cost.** Finite-order BCH discards higher commutators and is approximate outside terminating cases such as nilpotent algebras. The previous $10^{-7}$–$10^{-5}$ estimate was not verified for the realized matrices and is withdrawn. [[gl-k-attention-2026-07-09-review-revision]]

**The commutator as a generic noncommutativity correction.** Group commutators can encode curvature for a general connection. In realized Regime I, however, $\Omega_{ij}=U_iU_j^{-1}$ telescopes exactly even when the $U_i$ do not commute, so BCH commutators do not generate model holonomy. [[gl-k-attention-2026-07-09-review-revision]]

**The dual Zassenhaus formula.** BCH *merges* two exponentials into one; its dual, the **Zassenhaus formula**, *splits* one exponential of a sum into an ordered product,

$$
\exp(X+Y) = \exp(X)\exp(Y)\exp\big(-\tfrac12[X,Y]\big)\exp\big(\tfrac16(2[Y,[X,Y]] + [X,[X,Y]])\big)\cdots,
$$

which is the basis of operator-splitting and Trotter-type schemes. The two formulas are inverse views of the same noncommutativity, and either can serve when an algorithm needs to trade a single exponential for a sequence of cheaper ones or vice versa.

**Relation to the matrix exp/log maps.** Instead of forming
$g_1=\exp(\phi_1)$, $g_2=\exp(\phi_2)$, multiplying, and selecting a local
$\log(g_1g_2)$, truncated BCH approximates that local algebra coordinate from
brackets of $\phi_1$ and $\phi_2$. It does not itself produce a group element,
nor does it define a global logarithm. The canonical survey
[[moler-vanloan-2003-nineteen-dubious-ways]] explains why eigenvalue-based
matrix-exponential methods can fail for non-normal or defective matrices. A
real symmetric $\phi$ is orthogonally diagonalizable and $\exp(\phi)$ is SPD,
but its noncompact spectral range can still cause conditioning, overflow, or
underflow. Scaling and squaring with Padé approximation is analyzed by
[[al-mohy-higham-2009-scaling-squaring-matrix-exp]]. Log-Euclidean SPD geometry
instead composes logarithmic coordinates additively; BCH retains noncommutative
bracket corrections locally.

> [!note] Editorial (2026-07-10): no numerical residual range is asserted without a bound evaluated on the realized matrices; order-four BCH remains a local approximation. [[gl-k-attention-2026-07-09-review-revision]]

## In this work

BCH is the operational glue between the algebra-valued `phi` parameterization and the GL($k$) group it must act through:

- **`phi_retract_mode: bch`** — a truncated BCH update of the stored algebra
  coordinate, approximating the local logarithm of a composed group update.
  Exponentiation or another group-valued map is still required to act on the
  group. General retraction and Riemannian-SGD results apply only after their
  first-order and stochastic assumptions are verified.
- **`pos_phi: learned`, `pos_phi_compose: bch`, `bch_pe_order: 4`** — learned positional gauge transforms are composed in the algebra by an order-4 BCH series, so *relative position is encoded by group composition* rather than by additive sinusoids. Composing positional generators with BCH means the position structure inherits the gauge group's noncommutativity, the gauge-native counterpart to the positional encodings surveyed in [[Attention mechanisms — theory and positional structure]].
- **`phi_scale: 0.06`, `pos_phi_scale: 0.02`** — small configured algebra scales that motivate a local order-4 truncation. The formal discarded tail begins at degree five, but an evaluated remainder bound or residual on the realized updates is required to establish numerical accuracy.

The optional frame conditioner is not a full-$\mathrm{GL}(K)$ invariant or Fisher metric, and BCH truncation does not change that scope. [[gl-k-attention-2026-07-09-review-revision]]

## Sources

- [[finzi-2020-lieconv]] — Lie-algebra (log-coordinate) parameterization with $\exp$ recovery, the template for handling group composition in the algebra.
- [[absil-2008-optimization-matrix-manifolds]] — retractions as first-order surrogates for the geodesic exponential; the conditions a complete BCH-based update must satisfy.
- [[bonnabel-2013-riemannian-sgd]] — Riemannian SGD convergence under stated retraction and stochastic assumptions.
- [[arsigny-2006-log-euclidean]] — the flat, commutative Log-Euclidean alternative that discards the bracket corrections BCH retains.
- [[pennec-2006-affine-invariant-tensor]] — affine-invariant geometry at the curved, bracket-retaining end of the exp/log spectrum.
- [[moler-vanloan-2003-nineteen-dubious-ways]] — canonical survey of matrix-exponential methods, including conditioning and the eigenvalue-method breakdown for non-normal or defective matrices; symmetric $\phi$ is normal and nondefective.
- [[al-mohy-higham-2009-scaling-squaring-matrix-exp]] — scaling and squaring with Padé approximation for matrix exponentials used after algebra-coordinate updates and in gauge transport.

## See also

- [[Gauge transformation]]
- [[Parallel transport]]
- [[Holonomy]]
- [[Killing form]]
- [[Group equivariance]]
- [[Natural gradient]]
- [[LieConv]]
- [[Attention mechanisms — theory and positional structure]]
- [[Gauge equivariance and geometric deep learning]]
- [[SPD-manifold geometry and Riemannian optimization]]
