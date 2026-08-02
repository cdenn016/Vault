---
type: manuscript
title: "Gauge-Covariant Variational Free Energy and Renormalization: 2026-08-01 Pullback Geometry and Timeless Inference Record"
aliases:
  - "Gauge VFE RG pullback geometry record"
  - "Timeless inference record"
  - "Covariant informational pullback record"
authors:
  - Robert C. Dennis
year: 2026
status: in preparation
tags:
  - cluster/vfe
  - cluster/multi-agent
  - cluster/gauge-theory
  - cluster/info-geometry
  - project/multi-agent
  - project/transformer
  - field/mathematics
  - field/statistics
created: 2026-08-01
updated: 2026-08-01
---

# Gauge-Covariant Variational Free Energy and Renormalization: 2026-08-01 Pullback Geometry and Timeless Inference Record

## Scope and immutable provenance

This immutable record binds the pullback-geometry and timeless-inference construction in
`manuscripts/gauge_vfe_rg` to the evidence-gated working-tree snapshot
`git:43eb7e74942a61d7874c271a4be57ab3c94722a4:sha256:374710962a6d5ad312fb0c5938ca300308d5ff85d56df6e0dab1e7432ca2fbb9`
on branch `codex/gauge-vfe-rg-pullback-geometry-20260801`. This identifier is a verified,
uncommitted working-tree revision based on Research commit `43eb7e7`; it is not presented as a
publication commit.

The load-bearing files at verification time had these SHA-256 hashes:

- `05c_pullback_geometry.tex`: `4C241C1A810DA739732E7201B6BC51FE1412D4FC00761B8019AD38A4B673A8E3`
- `05d_relational_inference.tex`: `6DF55B6C7F98EA0C0A3F959BE1BFC0988FD4667D315E5C10F8711495A2E0B61A`
- `main.pdf`: `83B1D9B92F1CBBD9385E0B965448CEFDF561021F8EE72763BF4BE7FC0FAC01DE`
- construction and adversarial-verification report: `EB4B51F6C7B5BB201010E72BBDAEC92245952B6212ADF1DFB0E5254B0ED7961F`
- final-verification report: `E3E214944205BE85A91034007D7EF7BA7C8513970CF33D7F71DD1C366F440C69`

The generated manuscript, *Gauge-Covariant Variational Free Energy and Renormalization:
Covariant Information Geometry, Timeless Inference Histories, Local--Collective Bounds, and Exact
Effective Scale Theory*, compiled to 215 pages (1,365,110 bytes) with no undefined references,
undefined citations, duplicate labels, or fatal TeX errors. The repository verifier reported 29
PASS, 0 FAIL, and 0 INCONCLUSIVE. The evidence ledger closed PB-1 through PB-4 as
`EVIDENCE_VERIFIED`. These checks verify the conditional mathematical construction and its artifact;
they do not turn its explicit hypotheses into canonical physical structure.

## The fixed-base distinction

For either the belief or model associated bundle

$$
\varpi_x:\mathcal E_x\longrightarrow\mathcal C,
\qquad V\mathcal E_x=\ker T\varpi_x,
$$

a statistical law at one context $c\in\mathcal C$ is a point of the fiber $(\mathcal E_x)_c$.
A change from a law $A$ to a law $B$ is therefore additional path data,

$$
\Gamma:J\longrightarrow(\mathcal E_x)_c,
\qquad \Gamma(\lambda_0)=A,
\qquad \Gamma(\lambda_1)=B.
$$

Because $\varpi_x\circ\Gamma=c$, every tangent is intrinsically vertical:
$T\varpi_x(\dot\Gamma)=0$. No connection is needed to say this. The endpoints alone do not select
a path, an orientation, or a duration, and the parameter $\lambda$ is disposable bookkeeping rather
than primitive time.

For an arbitrary total-space curve with nonconstant base projection
$\gamma=\varpi_x\circ\Gamma$, a chosen connection gives the relative decomposition

$$
\dot\Gamma=H^\omega_\Gamma\dot\gamma+\operatorname{ver}^{\omega}\dot\Gamma.
$$

A base curve is simply a curve in the fixed manifold $\mathcal C$; a connection is needed to choose
its horizontal lift and to compare fibers. A curve with nonzero base velocity and nonzero covariant
vertical velocity is mixed relative to that connection.

An update of a spatially extended agent is different again: it is a curve of sections $r\mapsto s_r$.
Writing $\Sigma(r,c)=s_r(c)$ gives $\varpi_x\Sigma(r,c)=c$, hence
$\partial_r\Sigma(r,c)$ is vertical for every fixed $c$. The base remains fixed and timeless while
the statistical section changes.

## Covariant informational pullbacks

A selected principal connection induces an Ehresmann splitting and the covariant vertical first jet

$$
D^{\omega_x}s=\operatorname{ver}^{\omega_x}\circ Ts.
$$

If the statistical fiber carries its Fisher metric $g_x^F$ and Amari--Chentsov tensor $T_x^A$, the
agent induces the base tensors

$$
h_{s,x}^{\omega_x}(X,Y)
=g_x^F(D^{\omega_x}sX,D^{\omega_x}sY),
$$

$$
c_{s,x}^{\omega_x}(X,Y,Z)
=T_x^A(D^{\omega_x}sX,D^{\omega_x}sY,D^{\omega_x}sZ).
$$

Under the stated equivariance hypotheses these tensors are global and invariant under passive gauge
changes. They are nevertheless connection-relative. If $\omega'=\omega+a$ and the induced vertical
correction is $R_a$, then $D^{\omega'}sX=D^\omega sX+R_a(X)$, so the perceived Fisher tensor acquires
two linear cross terms and the quadratic term $g^F(R_aX,R_aY)$. Bundle geometry alone does not choose
one perceived base geometry.

Where $g_x^F$ is positive definite,

$$
\operatorname{rad}h_s^\omega=\ker D^\omega s,
\qquad
\operatorname{rank}h_s^\omega=\operatorname{rank}D^\omega s.
$$

The result is therefore generally a positive-semidefinite tensor, not automatically a Riemannian
metric. Constant rank gives a metric vector-bundle quotient
$T\mathcal C/\operatorname{rad}h_s^\omega$. A quotient manifold additionally needs an involutive
radical distribution, a regular leaf space, and basicness of the tensor along the leaves. The
manuscript retains explicit counterexamples showing that none of these stronger conclusions is
automatic.

## Exact local and collective VFE histories

A belief section and a model section specify marginals, not their joint dependence. An exact VFE
history therefore requires a declared conditional or full-law space $\mathfrak R_B$, configuration
map $\pi_i^{\mathrm{conf}}$, and right-inverse lift

$$
\iota_i:\mathcal Q_i\longrightarrow\mathfrak R_B,
\qquad
\pi_i^{\mathrm{conf}}\circ\iota_i=\operatorname{id}_{\mathcal Q_i}.
$$

The lift must reproduce the displayed configuration and carry any correlation or copula data. At a
fixed outside marginal, the correct local coordinate potential is the outside-averaged conditional
VFE

$$
\overline{\mathcal F}_{B,o}(Q_i)
=\mathbb E_{Q_{B^c}}
\left[\mathcal F_{B,o}(r_B^{Q_i};Y_{B^c})\right].
$$

Under the stated support, positive-evidence, finiteness, integrability, and dominated-differentiation
hypotheses,

$$
\mathcal F_o(Q_{B^c}r_B^{Q_i})
=C(Q_{B^c})+\overline{\mathcal F}_{B,o}(Q_i).
$$

Thus the restricted collective functional and the averaged local functional have the same
differential and, with the same block metric, the same natural-gradient ray. A single realized
conditional VFE at one blanket value need not have that gradient. The exact recognition metric is
the joint-law pullback $\mathsf G_i^F=\iota_i^*G_{\mathfrak R_B}^F$; a sum of marginal Fisher metrics
is exact only after block orthogonality or fixed dependence is separately proved.

VFE decrease alone does not select a unique curve or speed. On a regular metric inference space the
positive ray

$$
\dot Q=-v\,\operatorname{grad}^F\mathcal F_i,
\qquad v>0,
$$

selects an oriented unparameterized orbit. Positive scalar mobility changes only its parameterization;
anisotropic mobility generally changes its path. Natural-gradient trajectories are not generally
geodesics.

### Observation--interaction kernel equivalence

An **operational environment node** is a standard-Borel state space with a normalized state law and
a measurable message kernel; the definition does not assume biological agency, autonomy, or
self-modeling. By the randomization lemma, every normalized standard-Borel observation kernel
$K(do\mid y)$ admits a message realization

$$
U\sim\operatorname{Unif}[0,1],
\qquad
O=F(Y,U),
\qquad
\Pr(F(y,U)\in A)=K(A\mid y).
$$

Conversely, marginalizing an environment state and its message policy gives a normalized observation
kernel. The probability theory can therefore be presented entirely as interactions among agent and
environment nodes when all data and exogenous noise are represented at the boundary. This does not
remove observations from the ELBO: realized messages remain the records on which it conditions. Nor
does it prove that every boundary node is an agent in the stronger ontological sense. Persistent
state, action, a Markov blanket, or a local VFE are additional agency hypotheses.

## Emergent information duration, not primitive time

Once an oriented orbit is selected, its Fisher length

$$
L_F[Q]=\int\sqrt{\mathsf G_i^F(\dot Q,\dot Q)}\,d\lambda
$$

is invariant under orientation-preserving reparameterization. Fisher arclength $\tau$ gives the
representative equations

$$
\frac{dQ}{d\tau}
=-\frac{\operatorname{grad}^F\mathcal F_i}
{\|\operatorname{grad}^F\mathcal F_i\|_F},
\qquad
\frac{d\mathcal F_i}{d\tau}
=-\|\operatorname{grad}^F\mathcal F_i\|_F.
$$

Orientation comes from descent and duration from distinguishability length. This is an agent-relative
information duration on the realized history, not physical time or a global synchronized clock. It
can stall at critical or null segments. A scalar clock on a region exists only when the normalized
VFE one-form is exact, including vanishing periods.

## Meta-agent and cross-scale geometry

Let a bundle morphism $\Psi:\mathcal E\to\bar{\mathcal E}$ cover a base coarse map
$f:\mathcal C\to\bar{\mathcal C}$. If the fine and coarse sections are related,
$\Psi\circ s=\bar s\circ f$, and the morphism preserves horizontal lifts, then

$$
D^{\bar\omega}\bar s\circ Tf=T^V\Psi\circ D^\omega s.
$$

Without those hypotheses the exact formula retains a vertical mismatch term. When the fiber map is
also a normalized, parameter-independent Markov channel, Fisher data processing defines the vertical
defect

$$
\Delta_F^\Psi
=g^F-(T^V\Psi)^*\bar g^F\succeq0,
$$

whose value is the conditional covariance of the fine score. Its pullback to the fine base is the
distinct base defect

$$
\delta_\Psi
=(D^\omega s)^*\Delta_F^\Psi
=h_s^\omega-f^*h_{\bar s}^{\bar\omega}\succeq0.
$$

The vertical defects compose across two scales as

$$
\Delta_F^{\Psi_{12}\circ\Psi_{01}}
=\Delta_F^{\Psi_{01}}+(T^V\Psi_{01})^*\Delta_F^{\Psi_{12}}.
$$

Under related sections and compatible connections, the corresponding typed base identity is
$\delta_{02}=\delta_{01}+f_{01}^*\delta_{12}$.

This contraction compares a fine path with its own pushforward. It does not compare independently
recomputed fine and meta-agent VFE flows; that stronger relation requires oriented vector-field
semiconjugacy. A beta function for perceived geometry is defined only after the levelwise tensors are
transported to a declared common reference space. RG depth is a scale coordinate, not inference
duration.

## Exact closure boundary

The construction establishes conditional mathematical closure for covariant pullbacks, fixed-base
vertical histories, exact local--collective VFE coordinates, agent-relative Fisher duration, and
cross-scale Markov contraction. It does not claim a canonical connection, automatic nondegeneracy,
automatic existence of a joint-law lift, an automatic smooth quotient of an infinite-dimensional
section space, Lorentzian signature, physical time, or a global clock. It also does not certify that
the older MAgent barycenter or exploratory `renormalization.py` pipeline realizes the hypotheses of
the new abstract coarse theory.

## Relevance to this research

This record supplies the rigorous mathematical layer behind the program's earlier pullback and
multi-scale intuitions. It identifies the precise sense in which an agent can perceive geometry on a
fixed contextual base, separates passive gauge invariance from dependence on a chosen connection,
and states exactly what must commute for a meta-agent to inherit that geometry. It also resolves the
time-language ambiguity: belief/model change may carry an oriented, reparameterization-invariant
information duration without promoting the base manifold or an external parameter to physical time.

## Related

[[Agents as fibre-bundle sections|Agents as fiber-bundle sections]] · [[Fisher information metric]] ·
[[Statistical manifold]] · [[Multi-agent variational free energy]] ·
[[Meta-agents and hierarchical emergence]] · [[Renormalization-group flow of beliefs]] ·
[[Participatory realism (it from bit)]] · [[Information geometry and natural gradient]] ·
[[Emergent spacetime and holography]] · [[Gauge-Theoretic Multi-Agent VFE Model]]

## Sources

The primary source is the verified working-tree snapshot of
`manuscripts/gauge_vfe_rg`, especially Chapters 5c and 5d, the general coarse-map and
renormalization chapters, and the two dated verification reports under
`docs/reviews/gauge-vfe-rg-pullback-geometry-2026-08-01/`. The construction uses standard bundle and
information-geometric results already represented in this vault by [[kobayashi-nomizu-1963-foundations]],
[[amari-2000-methods-information-geometry]], [[cencov-1982-statistical-decision-rules]], and
[[ay-2017-information-geometry]].
