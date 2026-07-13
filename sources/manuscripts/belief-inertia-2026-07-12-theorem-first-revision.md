---
type: manuscript
title: "The Inertia of Belief: 2026-07-12 Theorem-First Revision Record"
aliases:
  - "Belief-inertia theorem-first revision record"
  - "Theorem-first belief-inertia revision"
authors:
  - Robert C. Dennis
year: 2026
status: in preparation
tags:
  - cluster/social-physics
  - cluster/social-physics/opinion-dynamics
  - cluster/multi-agent
  - cluster/vfe
  - cluster/gauge-theory
  - cluster/info-geometry
  - cluster/attention
  - project/social-physics
  - project/multi-agent
  - field/physics
  - field/mathematics
  - field/sociology
  - field/cs-ml
created: 2026-07-12
updated: 2026-07-12
---

# The Inertia of Belief: 2026-07-12 Theorem-First Revision Record

## Scope and provenance

This immutable record banks the theorem-first revision of `manuscripts/belief_inertia.tex` on branch `codex/belief-inertia-ultradeep-review-20260712`. The literature lock, manuscript revision, and symbolic regression span commits `5533b27c8afc57ff41fcd199afa69fa04839624a` through `f5b0bffc2c980a5f5c2c0cc74d179b18d804eca3`; the manuscript rewrite itself spans `8c1574278320466dae31b139d1d7013e721cb498` through `8ba7d095214f8cac3f3eb3bba7ea2c889c414c6d`. The revised title is *The Inertia of Belief: Gauge-Covariant Variational Free Energy for Social Dynamics*.

The revision was motivated by the [ultradeep peer review](../../docs/reviews/2026-07-12-belief-inertia-ultradeep-peer-review.md), is checked by the [exact symbolic regression](../../docs/reviews/2026-07-12-belief-inertia-symbolic-checks.py), and is reconciled with the durable [[verified-ledger|verification ledger]]. The historical source note [[belief-inertia]] remains unchanged and records the earlier manuscript state; this dated note supersedes its synthesis claims where the two differ.

## Primary contribution after revision

The paper's primary result is an engineered, gauge-covariant population consensus energy for Gaussian beliefs in heterogeneous local frames. Entropy-retaining row optimization gives Gibbs attention and the reduced log-partition objective. At frozen optimal attention and local gauge consensus, the loss Hessian has a four-part mean-sector diagonal block: prior, sensory, incoming relational, and outgoing relational or recoil stiffness. Fisher--Rao natural-gradient flow is the primary first-order dynamics. Belief inertia is retained only as an explicit, conditional kinetic-metric postulate layered on that stiffness theorem.

This positioning distinguishes the work from the direct mechanics comparators [[martins-2015-opinion-particles]], [[chirco-2022-statistical-bundle-dynamics]], [[girolami-calderhead-2011-riemann-hmc]], [[leok-zhang-2017-information-geometric-mechanics]], and [[pistone-2018-statistical-bundle-lagrangian]]. The residual novelty is not mechanics on probability spaces by itself; it is the combination of gauge-transported Gaussian KL consensus, optimized attention, four-part local relational stiffness, and a separately declared kinetic interpretation.

## Mathematical corrections

The authoritative population objective retains the categorical relative-entropy term,

$$
\mathcal F_{\mathrm{full}}
=\sum_i\mathrm{KL}(q_i\|p_i)
-\sum_i\mathbb E_{q_i}\log p(o_i\mid c_i)
+\sum_{ij}\left[
\beta_{ij}E_{ij}
+\tau\beta_{ij}\log\frac{\beta_{ij}}{\pi_{ij}}
\right],
$$

with $E_{ij}=\mathrm{KL}(q_i\|\Omega_{ij\#}q_j)$. The source-mixture reading is fenced by an explicit rowwise source-independence assumption. Eliminating the attention row gives

$$
\mathcal F_{i,\mathrm{red}}=-\tau\log Z_i,
\qquad
d\mathcal F_{i,\mathrm{red}}=\sum_j\beta_{ij}^*dE_{ij}.
$$

The entropy-suppressed scalar $S_i=\sum_j\beta_{ij}^*E_{ij}$ is a different objective whose differential contains $-\tau^{-1}\operatorname{Cov}_{\beta_i^*}(E_{ij},dE_{ij})$; that response has no universal homophily sign.

The revision separates three geometries: the intrinsic Fisher metric $G(q)$, the coordinate loss Hessian or local stiffness $H_F(x)$, and a separately chosen positive kinetic metric $M(x)$. Chentsov's theorem selects $G$, not the total free-energy Hessian. The kinetic choice is a postulate, and the same-functional choice is degenerate:

$$
H_Fv=\omega^2Mv,
\qquad M=H_F
\quad\Longrightarrow\quad
\omega^2=1
$$

up to the declared scale. Nontrivial oscillator predictions therefore require operationally independent kinetic and restoring tensors. For coupled kinetic geometry, the canonical momentum is $\pi_i=\sum_kM_{ik}\dot\mu_k$; the local form $\pi_i=M_i\dot\mu_i$ is reserved for an explicit block-diagonal approximation.

Fixed asymmetric attention remains conservative when all receiver and sender derivatives of the scalar potential are retained. Nonconservative behavior requires a declared detached/receiver-only truncation, explicit time dependence, damping, or external forcing. The complete adaptive-prior sector is $\alpha_iD_i+b_0\alpha_i-c_0\log\alpha_i$. Its envelope force coefficient $c_0/(b_0+D_i)$ differs from the derivative $b_0c_0/(b_0+D_i)^2$ of the bare product $\alpha_i^*D_i$.

## Social-claim adjudication

The first-order social theory now derives only the symmetric or reversible continuous-time DeGroot subclass and a restricted anchored Friedkin--Johnsen equilibrium. Heterogeneous susceptibility requires agent-indexed anchor precision or coupling. Gibbs attention is a finite-temperature, similarity-decreasing analog of bounded confidence, not an exact Hegselmann--Krause ball average.

Purely attractive finite-temperature attention has a positive cross-cluster tail, so separated clusters in the stated unanchored, symmetric reciprocal reduction are metastable and continue to merge. Exact persistent polarization requires extra structure such as severed support, persistent anchors with a proved separated equilibrium, signed influence, or active confirmation-biased sampling. [[albarracin-2022-epistemic-communities]] supplies the active-sampling comparator; it is not identified with passive attractive attention.

Social Impact Theory is interpretive because row normalization does not reproduce Latan\'e's number law. Diffusion and adopter-category claims are removed; a future diffusion theory needs an adoption state, hazard, irreversibility rule, and a population equation such as [[bass-1969-product-growth]]. Similarity weighting supports only selective exposure conditional on the kernel. Stiffness or a chosen kinetic metric can support revision-latency hypotheses, but explanatory perseverance requires an explicit slow state. The outgoing relational term is contemporaneous curvature, not accumulated social memory.

The direct social and dynamics comparators are [[nevin-mandell-atak-1983-behavioral-momentum]], [[xue-hirche-cao-2020-opinion-port-hamiltonian]], [[baumann-sokolov-tyloo-2020-second-order-consensus]], [[bass-1969-product-growth]], and [[sampson-porter-restrepo-2025-oscillatory-opinion]]. In particular, oscillation alone does not identify kinetic inertia because group-opinion feedback and time-dependent network coupling supply alternative mechanisms.

## Relationship to PIFB2

The revision inherits the entropy-retaining population objective, source-independence fence, optimized-attention envelope calculation, and Fisher natural-gradient path from [[participatory-it-from-bit]]. It does not edit `manuscripts/PIFB2.tex` or import PIFB2's broader participatory-physics scope. PIFB2 remains the mathematical comparator; this manuscript specializes the shared formalism to mathematical sociophysics and makes the kinetic extension conditional.

## Source hashes

- Revised `manuscripts/belief_inertia.tex`: SHA-256 `537EF4233E6F5AB9ED04FAAB1F5FACA0F2F588CC7543660E1F4A313F1EE990EF`.
- Shared `manuscripts/references.bib`: SHA-256 `CE8F668CD95BA5B6334717424E0F49559583E9D9BE7E7D72276FBB199F4F96D4`.
- Protected comparator `manuscripts/PIFB2.tex`: SHA-256 `50F382C51BFAC8B8841A4FE6AFF2887CE05D3D47DD905C6D20A91A688152D81B`.
- Protected historical note `sources/manuscripts/belief-inertia.md`: SHA-256 `ADD9AA3AE8497AE9DB28FB66B07F55C56DBB80F8601726160BDBE0DC5DCB5E92`.
- Ultradeep peer review: SHA-256 `2D5D5694A08DA334DF89E44C9AEC5DD1B935ED386D097FE2CF31176C81D5F1DE`.
- Symbolic regression: SHA-256 `258951A75AF7B2F59A6D13A862A1A499040F1622DA8E512E1BAFD09CA08C46F6`.

## Relevance to this research

This record is the corrected provenance source for [[Belief inertia]], [[Mass as Fisher information]], [[Hamiltonian belief dynamics]], [[Multi-agent variational free energy]], [[Echo chambers and polarization]], [[Belief perseverance and confirmation bias]], [[Sociophysics]], [[Statistical physics of social systems and collective behavior]], [[SocialPhysics]], and [[Gauge-Theoretic Multi-Agent VFE Model]]. It fixes the proof-status boundary between primary Fisher flow, local loss stiffness, and optional kinetic mechanics while preserving the old manuscript note as immutable history.
