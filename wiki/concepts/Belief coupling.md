---
type: concept
title: "Belief coupling"
aliases:
  - "beliefcoupling"
  - "Belief Coupling"
  - "Gauge-transported KL coupling"
tags:
  - cluster/multi-agent
  - cluster/social-physics/opinion-dynamics
  - cluster/vfe
  - project/multi-agent
  - project/social-physics
status: draft
created: 2026-06-21
updated: 2026-07-13
---

# Belief coupling

**Belief coupling** is the inter-agent interaction term by which one agent's belief is
pulled toward another's. In the gauge-theoretic [[Multi-agent variational free energy]] (VFE)
model it takes the specific form of an **attention-weighted, gauge-transported Kullback–Leibler
(KL) divergence**,

$$
\sum_{k}\,\beta_{ik}\;D_{\mathrm{KL}}\!\big(q_i \,\big\|\, \Omega_{ik}[q_k]\big),
$$

summed over the neighbors $k$ of agent $i$. It is the term that makes the model genuinely
*multi-agent* rather than a stack of independent active-inference agents. It supplies a
consensus interaction and a candidate input to coarse-graining, but polarization and
[[Meta-agents and hierarchical emergence|meta-agent]] emergence require separate results and
cannot be read off from this term alone. This page collects the definition, its classical
comparisons, and its role in collective dynamics.

## Definition

Each agent $i$ carries a Gaussian belief $q_i = \mathcal{N}(\mu_i, \Sigma_i)$ over a latent
code $k_i \in \mathbb{R}^K$, realised as a section of a statistical fiber bundle
([[Agents as fibre-bundle sections]]). Two beliefs cannot be compared naively, because each
lives in its own local $\mathrm{GL}(K)$ **gauge frame**: there is no global coordinate system
in which $\mu_i$ and $\mu_k$ are directly commensurable. The model therefore compares them only
after **gauge transport** — the [[Parallel transport]] of $q_k$ into $i$'s frame through the
transporter

$$
\Omega_{ik} = \Omega_i\,\Omega_k^{-1} = \exp(\phi_i)\exp(-\phi_k) \in \mathrm{GL}(K),
$$

where $\Omega_i = \exp(\phi_i)$ is the local frame of agent $i$ (the $e^{\phi}$ parameterization
restricts to the identity component $\det\Omega > 0$). The notation $\Omega_{ik}[q_k]$ denotes
the *pushforward* of the Gaussian $q_k$ under this linear map, $\Omega_{ik}[q_k] =
\mathcal{N}(\Omega_{ik}\mu_k,\ \Omega_{ik}\Sigma_k\Omega_{ik}^\top)$.

The pairwise interaction energy is then the transported divergence
$E_{ik} = D_{\mathrm{KL}}(q_i\|\Omega_{ik}[q_k])$, and the **coupling term** in the free
energy is the attention-weighted, entropy-regularized sum (term T3 of the canonical functional
in [[Multi-agent variational free energy]]):

$$
\mathcal{F}_{\text{couple}}
= \sum_{i,k}\Big[\beta_{ik}D_{\mathrm{KL}}\big(q_i\|\Omega_{ik}[q_k]\big)
   + \tau\beta_{ik}\log(\beta_{ik}/\pi_{ik})\Big],
\qquad
\beta_{ik} = \operatorname*{softmax}_{k}\Big(-\tfrac{E_{ik}}{\kappa\sqrt{K}} + \log\pi_{ik}\Big).
$$

Here $\beta_{ik}$ is the **attention weight** — a normalized coupling strength that *itself*
depends on the divergence: pairs that already disagree strongly (large $E_{ik}$) couple weakly,
pairs that nearly agree couple strongly. The weight is not a free parameter but the stationary
minimizer of the bracket: the relative-entropy term $\tau\beta\log(\beta/\pi)$ is what makes the
softmax the actual free-energy minimizer rather than an imposed choice, so that
$\min_\beta \mathcal{F}_{\text{couple}} = -\tau\log\sum_k\pi_{ik}\exp(-E_{ik}/\tau)$
([[Multi-agent variational free energy]]). The prior $\pi_{ik}$ is a non-uniform attention
prior (causal masks, positional biases) and $\kappa\sqrt{K}$ is the
[[Precision weighting|precision-temperature]] scale.

### Gauge invariance makes the comparison well-posed

The construction is only meaningful because the transported KL is **gauge-invariant**: for
Gaussians $P,Q$ and any $\Omega \in \mathrm{GL}(K)$,
$D_{\mathrm{KL}}(\Omega_* P \,\|\, \Omega_* Q) = D_{\mathrm{KL}}(P \,\|\, Q)$ — the $(\det\Omega)^2$
Jacobian factors cancel identically. This is the $\mathrm{GL}(K)$ Gauge-Invariance Theorem of
[[gl-k-attention|the GL(K) attention manuscript]], which extends to *all* $f$-divergences
(transport need only satisfy $\det\Omega_{ik}\neq 0$). Consequently $E_{ik}$ measures intrinsic
disagreement between $q_i$ and $q_k$, independent of the arbitrary local frames — the coupling
respects the gauge symmetry of the bundle ([[Gauge transformation]]). A related identity,
$\Omega_{ik}\Omega_{km}\Omega_{mi}=I$ for the vertex-frame transporters, means the coupling
operates in a flat-bundle regime with vanishing reconstructed [[Holonomy]] (Regime I);
promoting it to non-trivial holonomy is reserved for the companion edge-relaxed extension.

> [!note] Editorial: The prompt's index convention is $i,k$ (used here); the manuscripts write
> the same term with indices $i,j$ as $\beta_{ij}\,D_{\mathrm{KL}}(q_i\|\Omega_{ij}[q_j])$. They
> are identical — only the dummy summation label differs.

## Classical comparisons and restricted reductions

The gauge-transported KL coupling shares structures with several established interaction
rules, but the current theorem proves only a narrow first-order subclass. The comparisons
below separate that result from soft analogies and covariance-fusion calculations.

### Bounded-confidence / opinion-dynamics limit

Replace each Gaussian belief by its mean, set $\Omega_{ik}=I$, and hold a common covariance
fixed. The transported KL then becomes a squared Euclidean discrepancy, and finite-temperature
attention becomes a smooth similarity-decreasing gate. This is a **soft analog** of bounded
confidence, not the hard Deffuant–Weisbuch update or a Hegselmann–Krause ball average
([[deffuant2000-bounded-confidence]], [[Bounded confidence]]).

For fixed symmetric row-stochastic influence, the primary unweighted product Fisher flow gives
continuous-time DeGroot up to one global rate scale. For a nonuniform reversible matrix, matching
the standard transient requires $G_\rho=\sigma^{-2}(D_\rho\otimes I)$ or agent-specific rates
$\eta_i\propto\rho_i^{-1}$; the primary flow retains $D_\rho$. Adding persistent anchors to the
reversible scalar energy gives a restricted [[friedkin1990-social-influence-opinions|Friedkin–Johnsen]]
stationary equilibrium independently of the positive flow metric, but matching its standard
transient has the same weighted-metric or rate requirement. General directed DeGroot and
Friedkin–Johnsen iterations are not derived. Susceptibility is an anchoring parameter, not a
geometric identity with [[Belief inertia]] or [[Mass as Fisher information]].

### Products-of-experts limit

The *other* limit fuses beliefs rather than averaging opinions. When the alignment term
dominates (small temperature $\tau$ and self-coupling), the belief that minimizes the coupling
sum is the one that is simultaneously close to all of its transported neighbours — and for
Gaussian experts this minimizer is the **product of Gaussians**, which is itself Gaussian with
precision equal to the *sum* of the (transported) neighbour precisions,

$$
\Sigma_i^{-1} \;\approx\; \big\langle (\Omega_{ik}\Sigma_k\Omega_{ik}^\top)^{-1} \big\rangle_{\beta}.
$$

This "add the precisions" fusion is exactly the **product of experts (PoE)** of
[[hinton-2002-products-of-experts]] — equivalently logarithmic opinion pooling
([[Probabilistic opinion pooling]]) — recovered here as the covariance fixed point of the VFE
coupling (App. B of [[gl-k-attention]]). Where bounded confidence *averages* means, PoE
*multiplies* distributions: each expert acts as a soft constraint, and the product is sharp
wherever the experts agree. The softmax normalization of attention plays the role of the PoE
partition function. The two limits are the two faces of belief coupling — first-moment
consensus (bounded confidence) and second-moment fusion (products of experts) — both contained
in the single transported-KL term.

> [!note] Editorial: The two limits are not interchangeable. The meta-agent coarse-graining
> ([[Meta-agents and hierarchical emergence]]) deliberately *rejects* the PoE/product fusion for
> a constituent covariances, using instead a gauge-covariant **sandwich average** (a linear
> pool) to avoid the over-sharpening "veto" pathology a product imposes when many constituents
> are combined. PoE governs the within-agent precision fixed point; linear pooling governs the
> across-scale aggregation. See [[hinton-2002-products-of-experts]] and [[Probabilistic opinion pooling]].

## Role in consensus and meta-agent formation

Belief coupling supplies attractive interaction in the program. Because $\beta_{ik}$ is a
function of the divergence it weights, nearby agents can interact more strongly than distant
agents. Under the stated connected, positive, finite-temperature, symmetric reciprocal
two-cluster reduction, however, separated clusters are metastable and continue to contract;
stable fragmentation is not derived ([[deffuant2000-bounded-confidence]]). A tightly coupled group of
agents whose beliefs have aligned (modulo their gauge frames) behaves as a single coarse belief
— a **meta-agent** — at the next scale ([[Meta-agents and hierarchical emergence]]). The
emergent meta-agent's transporter is the inter-cluster average $\Omega_{AB} = (|A||B|)^{-1}
\sum_{i\in A, k\in B}\Omega_{ik}$, and its covariance is the equal-weight mixture moment
$\Sigma_A = \langle\Sigma_i\rangle + \mathrm{Var}_A(\mu)$ — both read directly off the coupling
structure. Iterating this gives the cross-scale tower of the
[[Renormalization-group flow of beliefs]], in which the coupling strength is one of the
RG couplings. For Regime-I vertex variables, equal-weight blocking gives RMS fluctuations
proportional to $n^{-1/2}$ and $y_2=-1/2$. The $n^{-1}$ rate belongs to a separate enlarged
independent-edge ensemble and is not established by the data-dependent Regime-II parameterization.
[[gl-k-attention-2026-07-09-review-revision]]

Two further connections make the term load-bearing:

- **Attention uses this coupling.** The Regime-I cocycle forces trivial loop holonomy but does not
  force pairwise identity transport. In the shared-frame or edge-independent constant reduction,
  $\Omega_{ik}=I$. Its isotropic transported-KL score is identity-bilinear plus a key-norm bias; an
  arbitrary learned QK bilinear form is a separate structural map. [[gl-k-attention-2026-07-09-review-revision]]

- **Coupling vs. inertia.** The coupling term supplies a restoring force. The intrinsic
  [[Fisher information metric]], the loss stiffness, and any kinetic metric are distinct
  ([[Mass as Fisher information]]). At fixed Fisher geometry and learning rate, larger positive
  first-order stiffness speeds relaxation; slower revision requires an independent mobility,
  damping, kinetic, or slow-state mechanism. Friedkin–Johnsen susceptibility is represented by
  explicit anchoring, not by identifying stiffness or Fisher geometry with inertia
  ([[friedkin1990-social-influence-opinions]]).

## Relevance to this research

Belief coupling is the program's inter-agent interaction and a common comparison point for
**attention**, restricted **consensus**, and proposed **hierarchical emergence**. It does not by
itself derive bounded-confidence fragmentation, cascades, polarization, or meta-agent closure.
It connects the social-physics lineage — Deffuant–Weisbuch bounded confidence
([[deffuant2000-bounded-confidence]]), Friedkin–Johnsen social influence
([[friedkin1990-social-influence-opinions]]), DeGroot averaging
([[degroot-1974-consensus]]) — with the machine-learning lineage of products of experts
([[hinton-2002-products-of-experts]]) and transformer attention
([[gl-k-attention]]), but with the proof-status distinctions stated above rather than as
unqualified limits of one gauge-covariant divergence.
This dual heritage is why the concept sits in both the
[[Gauge-Theoretic Multi-Agent VFE Model]] and the [[SocialPhysics]] projects.

## Related

[[Multi-agent variational free energy]] · [[gl-k-attention|GL(K) attention manuscript]] ·
[[Meta-agents and hierarchical emergence]] · [[Belief inertia]] · [[Mass as Fisher information]] ·
[[Bounded confidence]] · [[Opinion dynamics]] · [[Probabilistic opinion pooling]] ·
[[Renormalization-group flow of beliefs]] · [[Gauge transformation]] · [[Parallel transport]] ·
[[Holonomy]] · [[Agents as fibre-bundle sections]] · [[Precision weighting]] ·
[[Fisher information metric]] · [[Hamiltonian belief dynamics]]

## Sources

[[deffuant2000-bounded-confidence]] · [[friedkin1990-social-influence-opinions]] ·
[[hinton-2002-products-of-experts]] · [[degroot-1974-consensus]] · [[gl-k-attention]]
