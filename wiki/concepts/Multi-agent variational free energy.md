---
type: concept
title: "Multi-agent variational free energy"
aliases:
  - "Multi-agent VFE"
  - "Full VFE"
  - "FullVFE functional"
  - "Five-term variational free energy"
tags:
  - cluster/multi-agent
  - cluster/vfe
  - cluster/gauge-theory
  - cluster/info-geometry
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-07-12
---

# Multi-agent variational free energy

The **multi-agent variational free energy** is the scalar objective used to couple distribution-valued agents after gauge transport into common local frames. The authoritative social-belief sector in [[belief-inertia-2026-07-12-theorem-first-revision]] is entropy-retaining:

$$
\mathcal F_{\mathrm{full}}
=\sum_iD_{\mathrm{KL}}(q_i\|p_i)
-\sum_i\mathbb E_{q_i}\log p(o_i\mid c_i)
+\sum_{ij}\left[
\beta_{ij}E_{ij}
+\tau\beta_{ij}\log\frac{\beta_{ij}}{\pi_{ij}}
\right],
$$

where

$$
E_{ij}=D_{\mathrm{KL}}(q_i\|\Omega_{ij\#}q_j),
\qquad
\Omega_{ij}=U_iU_j^{-1}.
$$

The broader [[Gauge-Theoretic Multi-Agent VFE Model]] contains parallel belief and model channels, with separate transported energies and attention rows. The same rule applies in each channel: the categorical relative-entropy term is part of the canonical scalar and cannot be dropped while retaining canonical-envelope claims.

## Optimized attention

For fixed edge energies, row prior $\pi_i$, and temperature $\tau>0$, the unique row minimizer is

$$
\beta_{ij}^*
=\frac{\pi_{ij}e^{-E_{ij}/\tau}}{Z_i},
\qquad
Z_i=\sum_k\pi_{ik}e^{-E_{ik}/\tau}.
$$

Eliminating the row yields

$$
\mathcal F_{i,\mathrm{red}}=-\tau\log Z_i,
\qquad
d\mathcal F_{i,\mathrm{red}}
=\sum_j\beta_{ij}^*dE_{ij}.
$$

This is the envelope gradient: no extra first-order $d\beta^*$ term remains because the entropy-retaining row has been optimized. The entropy-suppressed scalar

$$
S_i=\sum_j\beta_{ij}^*E_{ij}
$$

is a different objective with differential

$$
dS_i
=\mathbb E_{\beta_i^*}[dE_{ij}]
-\tau^{-1}\operatorname{Cov}_{\beta_i^*}(E_{ij},dE_{ij}).
$$

The covariance response has no universal homophily sign and cannot be substituted into canonical-VFE arguments.

## Source-independence and generative-model status

The social block is an **engineered gauge-covariant consensus energy**. A rowwise source-mixture identity can be written only after the substantive assumption that the transported source templates form an externally supplied candidate family for that row. Even then, the row identity does not make the whole population functional the mean-field ELBO of one fixed joint on the original agent-state variables because the sources are other variational beliefs.

[[vfe-population-generative-status-2026-07-12]] proves the fixed-state mean-field obstruction and records three narrower constructions: the zero-within-scale Gaussian hierarchy, an equilibrium-frozen auxiliary source model, and a belief-configuration Gibbs lift when its partition function is finite. These constructions fence the probabilistic interpretation without weakening the scalar optimization result.

## Primary dynamics

For Gaussian belief coordinates, the primary update is Fisher--Rao natural-gradient flow:

$$
\dot\mu_i=-\eta_\mu\Sigma_i\nabla_{\mu_i}\mathcal F,
\qquad
\dot\Sigma_i=-2\eta_\Sigma\Sigma_i
(\nabla_{\Sigma_i}\mathcal F)\Sigma_i.
$$

This is not obtained by assigning the loss Hessian as a mass and taking a scalar-damping limit. The intrinsic Fisher metric $G$, loss Hessian $H_F$, and any kinetic metric $M$ are distinct objects.

## Local stiffness and conditional kinetics

At frozen optimized attention and local gauge consensus, the mean-sector loss Hessian has prior, sensory, incoming relational, and outgoing relational/recoil contributions. Away from frozen consensus, the reduced row Hessian includes

$$
-\tau^{-1}\operatorname{Cov}_{\beta_i^*}(\nabla E_{ij},\nabla E_{ij}),
$$

so the fully reduced Hessian is not globally identified with an intrinsic positive metric.

[[Belief inertia]] and [[Hamiltonian belief dynamics]] add second-order motion only through a conditional kinetic postulate. If the same local Hessian supplies both $M$ and the restoring tensor, $M=H_F$ makes the generalized spectrum $\omega^2=1$ up to scale. Nontrivial kinetic predictions require an independently specified positive $M$.

Fixed asymmetric attention remains conservative when all receiver and sender derivatives of the scalar edge sum are retained. A receiver-only/detached update is a different, explicitly nonconservative truncation.

## Adaptive prior precision

The complete adaptive sector is

$$
\alpha_iD_i+R(\alpha_i),
\qquad
R(\alpha_i)=b_0\alpha_i-c_0\log\alpha_i,
\qquad
\alpha_i^*=\frac{c_0}{b_0+D_i}.
$$

The optimized envelope force $c_0/(b_0+D_i)$ differs from the derivative $b_0c_0/(b_0+D_i)^2$ of the bare product $\alpha_i^*D_i$. Whenever the adaptive sector is enabled, $R(\alpha_i)$ remains part of the canonical objective.

## Sources

- [[belief-inertia-2026-07-12-theorem-first-revision]] -- entropy-retaining social objective, envelope gradient, Fisher path, and conditional kinetics.
- [[vfe-population-generative-status-2026-07-12]] -- exact generative-model scope and no-go result.
- [[participatory-it-from-bit]] -- broader two-channel multi-agent framework.
- [[gl-k-attention]] and [[gl-k-attention-2026-07-09-review-revision]] -- gauge-attention derivation and corrected canonical-versus-surrogate scope.

## See also

- [[Variational free energy]]
- [[Natural gradient]]
- [[Fisher information metric]]
- [[Belief inertia]]
- [[Mass as Fisher information]]
- [[Hamiltonian belief dynamics]]
- [[Collective active inference]]
- [[Gauge-Theoretic Multi-Agent VFE Model]]
