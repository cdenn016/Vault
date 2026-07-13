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
updated: 2026-07-13
---

# Gauge-Theoretic Multi-Agent VFE Model

## Goal

The Gauge-Theoretic Multi-Agent VFE Model (`MAgent_Model`) studies populations of Gaussian belief and model states carried by associated fibers with local $GL(K)$ frames. Inter-agent comparisons use gauge transport before divergence is measured. The canonical coupling is an engineered [[Multi-agent variational free energy]] with entropy-retaining attention. The primary belief dynamics are Fisher--Rao natural-gradient flow; a Hamiltonian path is a separate conditional kinetic extension.

The project is the continuous-time multi-agent sibling of the [[VFE Transformer Program]]. Its broader mathematical framework is developed in [[participatory-it-from-bit]], while the focused social-dynamics status is recorded in [[belief-inertia-2026-07-12-theorem-first-revision]].

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

The entropy-suppressed scalar $\sum_j\beta_{ij}^*E_{ij}$ is a different objective with a covariance response. A rowwise source-mixture interpretation requires an explicit source-independence assumption, and the full population functional is not one fixed mean-field ELBO over the original agent states. [[vfe-population-generative-status-2026-07-12]] gives the exact obstruction and the permitted auxiliary/configuration-space constructions.

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

Under the primary unweighted product Fisher metric, the revised social theory derives continuous-time DeGroot only for fixed symmetric coupling. Nonuniform reversible DeGroot requires an additional $\rho$-weighted product metric, a fixed-label joint family, or equivalent agent-specific rates; the restricted anchored Friedkin--Johnsen equilibrium inherits that scope. Gibbs attention is a soft bounded-confidence analog. Positive finite-temperature attractive attention yields metastable clustering in the stated unanchored, symmetric reciprocal two-cluster reduction, not exact stable polarization. Social Impact Theory remains interpretive, and diffusion requires an explicit adoption state and hazard.

The direct comparison set includes [[martins-2015-opinion-particles]], [[nevin-mandell-atak-1983-behavioral-momentum]], [[xue-hirche-cao-2020-opinion-port-hamiltonian]], [[baumann-sokolov-tyloo-2020-second-order-consensus]], [[bass-1969-product-growth]], and [[sampson-porter-restrepo-2025-oscillatory-opinion]]. Oscillation or resonance alone does not identify the proposed kinetic mechanism.

## Status and next steps

No new empirical validation is claimed by the theorem-first revision. The next social tests must separately estimate or manipulate Fisher geometry, restoring stiffness, any kinetic metric, damping, source selection, and slow explanatory states. The broader project should also resolve the open code-concordance findings before treating participatory or hierarchical claims as runtime-validated.

## Cross-links

**Sibling projects:** [[SocialPhysics]] · [[VFE Transformer Program]]

**Key concepts:** [[Agents as fibre-bundle sections|Agents as fiber-bundle sections]] · [[Multi-agent variational free energy]] · [[Belief inertia]] · [[Mass as Fisher information]] · [[Hamiltonian belief dynamics]] · [[Natural gradient]] · [[Fisher information metric]] · [[Ouroboros multi-scale dynamics]] · [[Meta-agents and hierarchical emergence]] · [[Renormalization-group flow of beliefs]] · [[Holonomy]]

**Manuscripts:** [[participatory-it-from-bit]] · [[belief-inertia-2026-07-12-theorem-first-revision]] · [[belief-inertia]] · [[meta-entropy-manuscript]] · [[gl-k-attention]]
