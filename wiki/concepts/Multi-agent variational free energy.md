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
updated: 2026-08-01
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

> [!important] An exact lift exists on an enlarged inventory (2026-07-27)
> The qualifier "on the original agent-state variables" is load-bearing, and dropping it changes the
> verdict. If the latent inventory is **enlarged by a declared source label** $j_i$, then under a
> topologically ordered source mask the divergence-scored row is the *exact* CAVI coordinate of a
> fixed normalized joint, with the sender mean free throughout and the link noise tied as
> $R_{ij}=\Omega_{ij}\Sigma_j\Omega_{ij}^\top$
> ([[magent-exact-elbo-whitepaper-2026-07-27-attention-derivation]]). This is a *lift*, not an
> equality of functionals on the original variables, so it does not contradict the moving-peer
> obstruction. Two costs are real: the mask is a **normalization requirement** (under the cocycle
> $\Omega_{ij}=U_iU_j^{-1}$ a reciprocal pair has singular assembled precision and infinite mass), and
> a nonunit $\tau$ additionally requires a tempered model carrying a per-source
> $-\tfrac12(1-1/\tau)\log\det(\Omega_{ij}\Sigma_j\Omega_{ij}^\top)$ logit.
>
> Those two costs are **the same cost**
> ([[magent-exact-elbo-whitepaper-2026-07-27-link-covariance-tie]]). Source-freeness as an identity in
> the free sender mean forces $R_{ij}=\tau\Omega_{ij}\Sigma_j\Omega_{ij}^\top$ and then $\tau=1$, so
> the tie and the unit temperature are one hypothesis and the lift does not reach the deployed
> $\tau=\kappa\sqrt K$. The tie is a declared postulate: the unique M-step optimum is
> $\Sigma_i+S_{ij}+\Delta_{ij}\Delta_{ij}^\top$, which exceeds it by a positive-definite amount, and a
> correlated pair recognition factor buys stationarity or the divergence-scored row but never both.

The same construction reads the **self term and the peer terms as competing slots of one simplex**. A
distinguished label slot with $p(y_i\mid j_i=\varnothing)=p_i(y_i)$ contributes
$D_{\mathrm{KL}}(q_i\Vert p_i)+H(q_i)$, so moving $T_1$ inside the attention row costs exactly one
belief entropy per slot. That is the generative-side reading of the observations-as-agent-couplings
parsimony question, reached independently of the direct computation.

[[magent-exact-elbo-whitepaper-2026-07-19-continuum-finite-remediation]] supplies the corrected obstruction. It works on the fine site-factorized family and sums iterated derivatives from separate site-local paths, yielding a positive weighted variance while every fixed-joint negative ELBO gives zero on the corresponding paths. The result excludes the coarser cross-design families, restricted families without the needed tangents, auxiliary-variable lifts, and the reduced functional after substituting state-dependent optimized attention. Its continuum corollary is conditional and does not construct a probability law on section space or a finite-to-continuum limit.

[[vfe-population-generative-status-2026-07-12]] remains the immutable earlier record of the equilibrium-frozen auxiliary source model and a belief-configuration Gibbs lift when its partition function is finite. Its older obstruction account is refined by the site-local theorem above rather than silently rewritten.

## Exact local--collective histories and their geometry

A pair of displayed belief/model marginals does not determine a joint recognition law. The exact
history construction therefore declares a configuration map and a full-law lift

$$
\pi_i^{\mathrm{conf}}:\mathfrak R_B\to\mathcal Q_i,
\qquad
\iota_i:\mathcal Q_i\to\mathfrak R_B,
\qquad
\pi_i^{\mathrm{conf}}\circ\iota_i=\operatorname{id}.
$$

The right-inverse condition is load-bearing: the lifted conditional or full law must reproduce the
agent's displayed configuration and carry any required correlation or copula data. Smoothness alone
does not make a map a lift. The exact recognition Fisher metric is
$\mathsf G_i^F=\iota_i^*G_{\mathfrak R_B}^F$; adding marginal Fisher metrics is exact only when block
orthogonality or fixed dependence has separately been established.

At fixed outside marginal, the coordinate-local objective that matches the restricted collective VFE
is the outside-averaged conditional functional

$$
\overline{\mathcal F}_{B,o}(Q_i)
=\mathbb E_{Q_{B^c}}
\left[\mathcal F_{B,o}(r_B^{Q_i};Y_{B^c})\right].
$$

Under the stated support, positive conditional-evidence, finiteness, integrability, and dominated-
differentiation hypotheses,

$$
\mathcal F_o(Q_{B^c}r_B^{Q_i})
=C(Q_{B^c})+\overline{\mathcal F}_{B,o}(Q_i).
$$

The two differentials and their natural-gradient rays then agree under the same block metric. A
single conditional VFE evaluated at one realized blanket value need not have the collective coordinate
gradient.

The observation--interaction equivalence is exact at the kernel level. By the randomization lemma,
every normalized standard-Borel observation kernel $K(do\mid y)$ can be realized as a message
$O=F(Y,U)$ from an operational environment node with $U\sim\operatorname{Unif}[0,1]$; conversely,
marginalizing an environment state and message policy produces a normalized observation kernel. This
gives an operationally agent-and-environment-node-only presentation when all data and exogenous noise
are boundary messages. It does **not** erase observations from the ELBO: the realized messages remain
its conditioning records. It also does not make every random seed or boundary node an autonomous
agent; persistent state, a Markov blanket, action, or its own local VFE are additional agency
hypotheses. [[gauge-vfe-rg-pullback-geometry-2026-08-01]]

VFE descent supplies orientation only after a metric or mobility is declared. The ray
$\dot Q=-v\,\operatorname{grad}^F\mathcal F_i$ with $v>0$ selects an oriented unparameterized orbit;
positive scalar mobility changes its parameterization, while anisotropic mobility can change the path.
Fisher arclength can then measure agent-relative information duration, but it is not imposed physical
time.

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

- [[gauge-vfe-rg-pullback-geometry-2026-08-01]] -- exact full-law lift, outside-averaged local VFE, local--collective differential identity, and timeless orbit geometry.

- [[magent-exact-elbo-whitepaper-2026-07-19-continuum-finite-remediation]] -- corrected fine-family/site-local obstruction, response identity, and conditional continuum corollary.
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
