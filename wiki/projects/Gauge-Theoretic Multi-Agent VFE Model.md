---
type: project
title: "Gauge-Theoretic Multi-Agent VFE Model"
aliases:
  - "MAgent"
  - "MAgent_Model"
  - "Gauge Agent"
  - "MAgent Model"
tags:
  - cluster/multi-agent
  - cluster/gauge-theory
  - cluster/vfe
  - cluster/participatory
  - project/multi-agent
status: draft
created: 2026-06-18
updated: 2026-08-16
---

# Gauge-Theoretic Multi-Agent VFE Model

## Goal

The Gauge-Theoretic Multi-Agent VFE Model studies populations of paired belief/model law sections
carried by associated bundles with local gauge frames. Gaussians are the principal computational
realization, not the theory-level ontology. Inter-agent comparisons use gauge transport before
divergence is measured. The canonical coupling is an engineered [[Multi-agent variational free energy]]
with entropy-retaining attention. Fisher--Rao natural-gradient flow and conditional action or
Hamiltonian branches require separately declared dynamical structure.

The project is the continuous-time multi-agent sibling of the [[VFE Transformer Program]]. Its broader mathematical framework is developed in [[participatory-it-from-bit]], while the focused social-dynamics status is recorded in [[belief-inertia-2026-07-12-theorem-first-revision]].

## Current primary focus: recursive graph renormalization

> [!note] Editorial (author-specified focus, 2026-08-16). At one fixed contextual point $c_*$, begin
> with scale-0 agents connected by the directed belief-attention weights $\beta_{ij}$ and
> model-attention weights $\gamma_{ij}$. These two row-normalized layers, together with their
> gauge transports and transported belief/model divergences, define an informational network even
> though there is no physical length or momentum. Small $\beta_{ij}$ or $\gamma_{ij}$ means weak
> directed proximity; $1/\beta_{ij}$ has the intended monotonic interpretation but is not generally
> a metric, while $-\tau\log(\beta_{ij}/\pi_{ij})$ recovers the corresponding transported energy up
> to a receiver-row constant. The primary problem is to prove when joint VFE descent yields stable
> two-channel blocks, when each block admits a holonomy-blind parent satisfying $h_\#Q_I=Q_I$ or
> instead must retain holonomy data, how $\beta$, $\gamma$, and the gauge transports descend to the
> quotient graph, and when the construction recurses to higher scales. See
> [[Renormalization-group flow of beliefs#Primary fixed-point graph-RG problem (2026-08-16)]].

The scale in this problem is organizational resolution on a directed multiplex graph. It is not
assumed to be spatial. The desired hierarchy is also not guaranteed by the current descent equations:
a selector, persistence or time-scale-separation theorem, quotient-closure result, and composable or
nested partition rule remain required. The holonomy condition is central on cyclic blocks but does
not itself choose those blocks.

This focus is separate from the water-like fluid/diffusion limit, the infinite-volume Gibbs/DLR
limit with free-energy-density convergence, and a continuous RG-scale semigroup. Those are three
additional and mutually non-equivalent obligations; none is a substitute for the finite recursive
graph-RG construction.

## Continuum theory and finite realizations

The theory-level agents are distribution-valued sections over a continuous contextual base. A finite experimental design supplies practical probability laws and CAVI factors, but section sampling and finite marginalization are distinct maps: sampled values of supplied sections equal posterior coordinate marginals only under an explicit compatibility hypothesis. The finite recognition law neither determines a unique off-design section nor constructs a probability law on the space of sections. A finite design is therefore not automatically a lattice gauge theory. That stronger construction requires a declared interaction complex, separately declared group-valued link variables on oriented edges, and declared two-cells or plaquettes. [[magent-exact-elbo-whitepaper-2026-07-19-continuum-finite-remediation]] records the exact types and the remaining continuum-limit obligations.

## Agent-only ontology and physicalization program (2026-08-13)

The intended ontology takes
$z_i=(q_i,s_i)\in\Gamma(\mathcal E_b\times_{\mathcal C}\mathcal E_m|_{\mathcal C_i})$
as the primitive state-bearing content of agent $i$. "Agent-only" means only agents bear state; it
does not yet reconstruct the contextual base, bundle, gauge action, incidence, normalized
interaction-record kernels, or variational rule. Observations are endogenous records of scoped
interactions rather than an extra physical substance; an operational environment-node presentation
does not by itself prove autonomy or agency for every boundary node. A full finite recognition law may carry
dependence absent from its displayed marginal sections, so an exact section-level VFE additionally
requires a declared lift to the joint-law space.

Apparent history is a curve in section/configuration space over a fixed, potentially timeless base.
A VFE selects an oriented orbit only after a metric or mobility is declared; its Fisher length is
information duration rather than physical time. Stationary-action, Hamiltonian, and quantum-phase
branches require their own additional structures.

The physicalization target is a typed family of natural gauge-invariant maps from relational section
data modulo gauge to candidate observables. The established example
$h_s^\omega=(D^\omega s)^*g^F$ is a connection-relative positive-semidefinite semigeometry. Shared
physical geometry still needs a collective or joint-law section, connection and channel choices,
nondegeneracy or quotient control, and an inter-agent agreement theorem. Physical dimensions may be
modeled as type lines and units as perspective-relative bases, but information is dimensionless: an
information-to-action scale and any identification involving $\hbar$ remain open bridge data, not a
derived pullback identity. [[multiagentelbo-agent-only-ontology-2026-08-13]]

## Covariant pullback geometry and timeless inference

The general theory now distinguishes three objects that older project prose sometimes merged. A law
change at one context is a vertical curve in one statistical fiber. A spatially extended agent update
is a curve of sections whose evaluation at every fixed context is vertical. A total-space curve over a
moving base path admits horizontal/vertical components only after a connection is selected. The base
$\mathcal C$ itself can remain fixed and timeless throughout.

For a belief or model section $s$, the connection-relative covariant first jet
$D^\omega s=\operatorname{ver}^\omega\circ Ts$ pulls the fiber Fisher metric back to the perceived
base semimetric $h_s^\omega=(D^\omega s)^*g^F$. It is passive-gauge invariant under the theorem's
hypotheses, but neither connection independent nor automatically nondegenerate. VFE natural-gradient
descent can select an oriented unparameterized inference orbit, after which Fisher arclength supplies
agent-relative information duration rather than imposed physical time.

At the meta-agent level, first-jet naturality requires related fine/coarse sections and a
connection-compatible bundle morphism. Markov Fisher contraction additionally requires a normalized,
parameter-independent channel. These are conditional mathematical results; they do not by themselves
certify the current runtime barycenter, hierarchy, or exploratory RG pipeline.
[[gauge-vfe-rg-pullback-geometry-2026-08-01]]

## Finite conditional theory closure (2026-08-08)

The general finite theory is now terminally closed for arbitrary admitted standard-Borel agent
networks and finite composable scale sequences. It includes common-channel evidence preservation,
conditional log-Laplace actions, DQM/Fisher contraction, exact local/block VFE coordinates, the
complete finite interaction representation and retained residual, posterior meta-agent bridges,
marked-event attention, covariant pullback anomalies, information duration, nonautonomous
derivative cocycles, and reference-typed beta and fixed-object data.

This is a conditional mathematical framework, not runtime certification. Applying it to MAgent
still requires explicit principal scale maps, target product references, exact recognition lifts,
configuration manifolds and coarse maps, related sections, objective and metric compatibility,
comparison isomorphisms, and any claimed natural-gradient semiconjugacy. It does not establish
automatic sparse closure, physical time, universality, or an infinite-volume limit.
[[gauge-vfe-rg-terminal-theory-closure-2026-08-08]]

## Agent and transport architecture

Each agent carries belief $q_i$, belief prior $p_i$, model state $s_i$, and model prior $r_i$. Belief and model channels can carry independent frames. A belief edge compares

$$
E_{ij}=D_{\mathrm{KL}}(q_i\|\Omega_{ij\#}q_j),
\qquad
\Omega_{ij}=U_iU_j^{-1},
$$

with a parallel construction for the model channel. Vertex transport is flat: loop products telescope to the identity. Edge-local links and nontrivial [[Holonomy]] are optional extensions and must not be attributed to the flat baseline.

## Canonical objective and attention

For each channel, the canonical attention row retains both expected edge energy and categorical relative entropy:

$$
\sum_j\left[
\beta_{ij}E_{ij}
+\tau\beta_{ij}\log\frac{\beta_{ij}}{\pi_{ij}}
\right].
$$

Optimizing the row gives

$$
\beta_{ij}^*=\frac{\pi_{ij}e^{-E_{ij}/\tau}}{Z_i},
\qquad
\mathcal F_{i,\mathrm{red}}=-\tau\log Z_i,
\qquad
d\mathcal F_{i,\mathrm{red}}=\sum_j\beta_{ij}^*dE_{ij}.
$$

The entropy-suppressed scalar $\sum_j\beta_{ij}^*E_{ij}$ is a different objective with a covariance response. A rowwise source-mixture interpretation requires an explicit source-independence assumption, and the full population functional is not one fixed mean-field ELBO over the original agent states. [[magent-exact-elbo-whitepaper-2026-07-19-continuum-finite-remediation]] gives the corrected fine-family, site-local obstruction and its conditional continuum corollary; [[vfe-population-generative-status-2026-07-12]] retains the earlier auxiliary and configuration-space constructions.

**The attention row now has an exact lift (2026-07-27).** On the inventory enlarged by a declared
source label, and under a topologically ordered source mask, $\beta^*$ above is the exact CAVI
coordinate of a fixed normalized joint rather than an engineered simplex value, with the sender mean
free and the link noise tied as $R_{ij}=\Omega_{ij}\Sigma_j\Omega_{ij}^\top$
([[magent-exact-elbo-whitepaper-2026-07-27-attention-derivation]]). Two findings bear directly on this
project rather than on the transformer. First, the ordered mask is a **normalization requirement**:
under the cocycle transport $\Omega_{ij}=U_iU_j^{-1}$ a reciprocal pair has singular assembled
precision and infinite mass, so a bidirectional source relation — which is the natural multi-agent
setting — cannot be lifted directly. Adding the $T_1$ self-prior anchor restores definiteness but
yields a label-dependent partition function that does not separate across rows (spread 1.76 nats at
$N=3$). Second, a nonunit $\tau$ requires a tempered model whose normalizer adds a per-source
$-\tfrac12(1-1/\tau)\log\det(\Omega_{ij}\Sigma_j\Omega_{ij}^\top)$ logit, absent from the deployed
row; at $\tau=\sqrt7$ the two rows differ by 0.069 in total variation.

**The tie is a postulate, and it is the temperature (2026-07-27).**
[[magent-exact-elbo-whitepaper-2026-07-27-link-covariance-tie]] grades the remaining hypothesis and
collapses those two findings into one. Source-freeness of the offset, as an identity in the free sender
mean, forces $R_{ij}=\tau\Omega_{ij}\Sigma_j\Omega_{ij}^\top$ and then forces $\tau=1$, so the lift
covers the unit-temperature row and not the deployed $\tau=\kappa\sqrt K$. The tie is not an M-step
fixed point — the unique optimum is $\Sigma_i+S_{ij}+\Delta_{ij}\Delta_{ij}^\top$, exceeding it by a
positive-definite amount, with the forgone bound exactly a Stein loss — so it stands as a declared
constrained-covariance postulate. Three consequences bear on this project specifically. A correlated
pair recognition family, the natural next relaxation and one this project is already planning, buys
stationarity or the divergence-scored row but never both, so it should be pursued on its own merits
rather than as a repair. The ordered mask survives the non-flat toggle, because
`gauge_agent/non_flat_connection.py` builds $V_{ji}=V_{ij}^{-1}$ and so preserves
$\Omega_{ij}\Omega_{ji}=I$ even at large 3-cycle [[Holonomy|holonomy]]; the mask tracks edge
reciprocity, not flatness, and escaping it means surrendering edge reversibility. And the tie does not
mean what it appears to: the link predictive is $2S_{ij}$, not the transported belief.

For adaptive prior precision, the complete sector is $\alpha_iD_i+b_0\alpha_i-c_0\log\alpha_i$. The optimized envelope coefficient $c_0/(b_0+D_i)$ differs from the derivative $b_0c_0/(b_0+D_i)^2$ of the bare product $\alpha_i^*D_i$.

## Primary and conditional dynamics

The primary Gaussian belief update is

$$
\dot\mu_i=-\eta_\mu\Sigma_i\nabla_{\mu_i}\mathcal F,
\qquad
\dot\Sigma_i=-2\eta_\Sigma\Sigma_i
(\nabla_{\Sigma_i}\mathcal F)\Sigma_i.
$$

This is Fisher--Rao [[Natural gradient|natural-gradient]] flow. The intrinsic Fisher metric $G$, loss Hessian/local stiffness $H_F$, and any positive kinetic metric $M$ are separate.

At frozen optimized attention and local consensus, the mean-sector $H_F$ separates into prior, sensory, incoming relational, and outgoing relational/recoil stiffness. The outgoing block is contemporaneous sender-role curvature. It is not accumulated memory or inertia by itself.

The optional Hamiltonian integrator requires a declared kinetic metric. If the same equilibrium Hessian supplies both mass and restoring force, $M=H_F$ makes the generalized spectrum $\omega^2=1$ up to scale. Nontrivial modal predictions require independently identified kinetic and restoring tensors. For coupled $M$, momentum is $\pi_i=\sum_kM_{ik}\dot\mu_k$. Fixed asymmetric attention remains conservative when both sender and receiver derivatives of the scalar potential are retained; detached receiver-only updates are a different truncation.

## Run modes and code scope

The repository exposes `basic`, `ouroboros`, `hierarchy`, and `rg` modes. Natural-gradient and Hamiltonian integrators are selected independently from the run mode. The Ouroboros, meta-agent, renormalization, nonflat-connection, reflection, and Yang--Mills paths remain opt-in project extensions with their own code-concordance limits. The July 11 review [[participatory-it-from-bit-2026-07-11-code-concordance-review]] remains the governing record for frame-update equivariance, real-log-domain closure, detector-temperature/covariance consistency, belief shadows, lineage persistence, nonequilibrium observables, and provenance.

## Social-science scope

Under the primary unweighted product Fisher metric, the revised social theory derives continuous-time DeGroot only for fixed symmetric coupling. Matching a standard nonuniform reversible transient requires an additional $\rho$-weighted product metric, a fixed-label joint family, or equivalent agent-specific rates. The restricted anchored Friedkin--Johnsen stationary equilibrium is independent of the positive flow metric; only its standard transient retains that requirement. Gibbs attention is a soft bounded-confidence analog. Positive finite-temperature attractive attention yields metastable clustering in the stated unanchored, symmetric reciprocal two-cluster reduction, not exact stable polarization. Social Impact Theory remains interpretive, and diffusion requires an explicit adoption state and hazard.

The direct comparison set includes [[martins-2015-opinion-particles]], [[nevin-mandell-atak-1983-behavioral-momentum]], [[xue-hirche-cao-2020-opinion-port-hamiltonian]], [[baumann-sokolov-tyloo-2020-second-order-consensus]], [[bass-1969-product-growth]], and [[sampson-porter-restrepo-2025-oscillatory-opinion]]. Oscillation or resonance alone does not identify the proposed kinetic mechanism.

## Literature-backed extension map (2026-08-10)

The source-backed gap review [[multiagentelbo-literature-gap-review-2026-08-10]] separates four
extension layers that older project language sometimes blended:

1. **Inference approximation.** [[Process-space variational inference]], [[Belief Propagation]],
   [[Gaussian Belief Propagation]], and [[Approximate Bayesian inference]] specify process-level,
   constrained-Bethe, walk-summable Gaussian, copula, and covariance-safe baselines. The present
   code remains the exact finite oracle; locally consistent pseudomarginals are not its exact global
   recognition law.
2. **Gauge, recovery, and quotient geometry.** [[Statistical experiment comparison and deficiency]],
   [[Graph synchronization and connection Laplacians]], [[Singular statistical models]], and
   [[Quotient Bayesian learning]] provide external comparison theorems. Graphical-model gauge
    reparameterization is not automatically passive principal-bundle gauge, and compact
    connection-Laplacian guarantees do not automatically extend to noncompact `GL^+(2)`.
3. **Communication and collective epistemics.** [[Decentralized Bayesian inference]],
   [[Communication-constrained inference]], [[Conservative information fusion]],
   [[Non-Bayesian social learning]], and [[Common knowledge and Bayesian agreement]] distinguish
   posterior approximation, density consensus, information recycling, bit budgets, network
   learning, common priors, and common knowledge. None follows from an attractive VFE interaction
   energy alone.
4. **Population and higher-order limits.** [[Graphon limits of agent networks]],
   [[Propagation of chaos]], [[O-information]], and [[Partial information decomposition]] supply
   stochastic-limit and diagnostic routes. They require declared indexed models and estimator or
   axiom choices; deterministic graph limits, graphon diffusions, games, O-information, and PID are
   not interchangeable.

[[Expected Free Energy]] and [[Collective active inference]] now carry the corresponding
derivational and aggregate-objective counterevidence. Active-policy selection remains outside the
current code scope. The literature sharpens the open continuum, DLR, regular-quotient,
experiment-recovery, intrinsic-partition, and Oseledets obligations; it does not close them by
citation.

## Status and next steps

The finite conditional theorem itself is complete. The next theory-to-model step is a minimal
two-scale finite instantiation that supplies the application data above and measures the exact
retained residual and semiconjugacy defect before any universality or thermodynamic-limit program is
attempted. [[gauge-vfe-rg-terminal-theory-closure-2026-08-08]]

No new empirical validation is claimed by the theorem-first revision. The next social tests must separately estimate or manipulate Fisher geometry, restoring stiffness, any kinetic metric, damping, source selection, and slow explanatory states. The broader project should also resolve the open code-concordance findings before treating participatory or hierarchical claims as runtime-validated.

## Cross-links

**Revision record:** [[magent-exact-elbo-whitepaper-2026-07-19-continuum-finite-remediation]]

**Sibling projects:** [[SocialPhysics]] · [[VFE Transformer Program]]

**Reference curriculum:** [[Gauge VFE ELBO curriculum]]

**Research method:** [[Rigorous theory search]] — the contract, proof-portfolio, dependency,
effective-theory, adversarial-reconstruction, and oracle-erasure protocol for new mathematical
constructions in this project

**Key concepts:** [[Agents as fibre-bundle sections|Agents as fiber-bundle sections]] · [[Multi-agent variational free energy]] · [[Belief inertia]] · [[Mass as Fisher information]] · [[Hamiltonian belief dynamics]] · [[Natural gradient]] · [[Fisher information metric]] · [[Ouroboros multi-scale dynamics]] · [[Meta-agents and hierarchical emergence]] · [[Renormalization-group flow of beliefs]] · [[Holonomy]]

**Manuscripts:** [[gauge-vfe-rg-terminal-theory-closure-2026-08-08]] · [[gauge-vfe-rg-pullback-geometry-2026-08-01]] · [[participatory-it-from-bit]] · [[belief-inertia-2026-07-13-final-review-closure]] · [[belief-inertia-2026-07-13-final-verification-addendum]] · [[belief-inertia-2026-07-12-theorem-first-revision]] · [[belief-inertia]] · [[meta-entropy-manuscript]] · [[gl-k-attention]]
