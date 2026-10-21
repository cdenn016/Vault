---
type: concept
title: Meta-agents and hierarchical emergence
aliases:
  - Meta-agent formation
  - Hierarchical emergence
  - Species-gated condensation
  - Soft condensation
tags:
  - cluster/multi-agent
  - cluster/vfe
  - cluster/social-physics
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-10-20
---

# Meta-agents and hierarchical emergence

## Definition

A **meta-agent** is a full agent in its own right — a section carrying Gaussian beliefs $(q_I, p_I, s_I, r_I)$ with belief and model gauge frames $(\Omega_I, \tilde\Omega_I)$ — that is *constructed* from a cluster $I$ of constituent agents once those agents reach sufficient epistemic coherence. **Hierarchical emergence** is the process by which clusters condense into meta-agents at a higher scale, the meta-agents' collective beliefs feed back down as priors, and the construction repeats scale by scale to build a tower.

The framework distinguishes two orthogonal kinds of alignment (`hierarchical_emergence.py`, module docstring):

- **Model alignment** $(s_i \leftrightarrow s_j)$ defines **species** — agents sharing a generative model, i.e. the same ontology/way of parsing reality. This is *structural* and *slow* (evolutionary timescale, $\varepsilon \ll 1$ in the dynamics).
- **Belief alignment** $(q_i \leftrightarrow q_j)$ defines **meta-agents / coalitions** — agents agreeing on what is happening *now*. This is *dynamic* and *fast* (perceptual timescale).

The selection rule is that **species gates meta-agent formation**: you can only coordinate (form a coalition) with agents that share your model. As an order-parameter field over the base manifold,

$$
W_{i\alpha}(x) = S_{i\sigma(\alpha)}(x)\cdot C_{i\alpha}(x),
$$

with $S$ the slow species gate (from model alignment) and $C$ the fast coalition membership (from belief alignment). The code likens this to Cooper pairing: condensation requires matching quantum numbers (species) before pairing (meta-agent formation) can occur ([[bcs-1957-theory-of-superconductivity]]).

**The hierarchical information budget.** A meta-agent's state update *consumes* the full
bandwidth of its constituents (pooling is constituent-only) while its own emission is far
smaller.
The neuroscience anchor is
[[zheng-meister-2025-unbearable-slowness]] ($10^9$ bits/s in, ~10 bits/s out); the senses in
which a higher level nonetheless "has more" — synergistic readout of joint statistics
([[Partial information decomposition]]) and interventional causal emergence
([[hoel-2013-causal-emergence]]) — are compatible with, not exceptions to, the DPI.

## Definitional hierarchy in the source manuscript

[[participatory-it-from-bit]] characterizes a meta-agent through a constructive state definition,
a free-energy-improvement criterion, and a consensus detector.

- **Definition (what a meta-agent *is*).** The gauge-covariant forward-KL **barycenter** of the transported constituents, $q_I^* = \arg\min_{q_I}\sum_i w_i^I\mathrm{KL}(\Omega_{Ii}q_i\|q_I) + \lambda\mathrm{KL}(q_I\|p_I)$, with the Karcher / first-order-BCH gauge frame. This is the one meta-agent object that is at once a genuine variational minimizer and provably gauge-covariant: the coarse-graining map satisfies $\mathcal{R}_s(h\cdot X)=h\cdot\mathcal{R}_s(X)$.
- **Licensing (*when* one forms).** The free-energy-improvement criterion $\mathcal{F}^*[\text{parent}] + C(I) < \mathcal{F}^*[\text{constituents}]$, itself the $\Delta_I>0$ special case of an MDL/Bayesian retention rule.
- **Computational surrogate.** The Gibbs consensus detector $\Gamma = PC_qC_s>\Gamma_{\min}$ described above, which selects candidate clusters for the criterion.
- **Foils.** Perfect (pointwise) consensus and epistemic death (complete informational alignment after transport) are the pathological limit, not the formation target.

## 2026-07-11 executable-status correction

The PIFB2 code-concordance review found three limits on the reached meta-agent construction. First, the checked-in Gibbs detector inherits $\tau_q=\tau_s=14$ from `kl_threshold=14` rather than using the manuscript's reference $\tau_q=0.05$. At membership threshold $1/2$, the resulting belief pass band is $14\log 2\approx9.704$ nats rather than $0.05\log 2\approx0.035$ nats. The active `covariance_collapse="moment"` pool omits between-child mean dispersion, so the small-temperature argument does not control that truncation on the reviewed arm. A matching implementation must use and verify the stated temperature or retain dispersion in the covariance collapse.

Second, the current frame pool is not defined on every frame the active updates admit. Bounded products of real exponentials can reach well-conditioned elements of $\mathrm{GL}^+(K)$ without a real logarithm, while meta-agent formation calls `matrix_log_principal` unconditionally. The hierarchy therefore needs a log-safe invariant domain, a restricted group closed under the selected chart, or a log-free group barycenter. Third, an existing higher scale is not reconciled with later detector partitions: membership, parent maps, and lineage persist after one-shot formation. A persistence window is consequently not an independent stability test until the runtime supports replacement, retirement, and time-indexed membership.

## Why it matters here

This is the layer of the [[Gauge-Theoretic Multi-Agent VFE Model]] that turns a flat population of [[Agents as fibre-bundle sections]] into a genuine *hierarchy*. The base layers supply [[Multi-agent variational free energy]] dynamics among peers; this construction (Layer 6/7 in the module map: `meta_agents.py` and `hierarchical_emergence.py`) is what lets the model build new scales rather than only updating beliefs at one scale. It is the mechanism behind the `'hierarchy'` preset (species × coalition gated soft membership + condensation) and underpins the `'ouroboros'` multi-scale tower, where meta-agent formation and top-down feedback close the participatory loop ([[participatory-it-from-bit]]).

Formation is also a *staged* process in every empirical and theoretical tradition that has
looked: assembly through stable subassemblies outpaces all-at-once assembly
([[simon-1962-architecture-complexity]]), evolution's major transitions always combine
previously stabilized units ([[maynard-smith-1995-major-transitions]]), real social groups grow
by accretion with size-dependent persistence ([[palla-2007-social-group-evolution]]) and layer
into a discrete hierarchy with branching ratio near three
([[zhou-2005-discrete-hierarchy-group-sizes]]), and connection costs are what drive evolved
networks to become hierarchical at all ([[mengistu-2016-evolutionary-origins-hierarchy]]) —
resonant with this construction's priced formation (retention charge, Wilson term, partition
prior).

It also connects the project to social and statistical physics. The consensus/condensation picture sits alongside opinion-dynamics consensus models ([[degroot-1974-consensus]], [[friedkin1990-social-influence-opinions|friedkin-johnsen-1990]], [[hegselmann-2002-opinion|hegselmann-krause-2002]]). The covariance-sandwich barycenter is a geometric (KL/transport-aware) opinion pool ([[Collective active inference]], [[dietrich-list-2016-opinion-pooling]], [[genest-zidek-1986-pooling]]), and the cluster-acceptance test is a model-selection question — when does collapsing a block to one meta-agent pay for its description length? ([[MDL and BIC model selection]], [[Community detection and modularity]]).

## Details

### Consensus detection (Gibbs cluster scalar)

A meta-agent is licensed when a cluster's **consensus score** $\Gamma(I,x)\in[0,1]$ exceeds a threshold. The canonical (manuscript-conformant) form in `ConsensusDetector` is a product of three bounded factors:

$$
C_q(I,x) = \exp\Big[-\tfrac{1}{\tau_q |I|^2}\sum_{i,j\in I}\mathrm{KL}\big(q_i \| \Omega_{ij} q_j\big)\Big],
\quad
C_s(I,x) = \exp\big[-V_s(I,x)/\tau_s\big],
$$
$$
P(I,x) = \tfrac{1}{|I|}\sum_{i\in I}\chi_i(x),
\qquad
\Gamma(I,x) = P \cdot C_q \cdot C_s .
$$

Here $C_q$ measures belief coherence, $C_s$ model coherence, and $P$ the **presence** (mean support $\chi_i$). The divergences are computed *after gauge transport* — $\mathrm{KL}(q_i \| \Omega_{ij} q_j)$ uses the belief frame $\Omega_{ij}$, and the model term uses its own frame $\tilde\Omega_{ij}$. The diagonal $\mathrm{KL}(q_i\|q_i)=0$ terms are kept in the $|I|^{-2}$ average. A cluster is accepted when $\Gamma > \Gamma_{\min}$ and $|I|\ge N_{\min}$.

A code comment records the *reason* the Gibbs exponential is used rather than a $1-\mathrm{KL}$ surrogate: the surrogate would be signed and could give a misleadingly positive product from two negative factors, whereas $\exp[-V/\tau]\in(0,1]$ cannot. `find_clusters` is a two-stage scheme: build a pair-edge graph from $\Gamma(\{i,j\},x)>\Gamma_{\min}$, take connected components of size $\ge N_{\min}$ as candidates, then re-score each full cluster and accept iff $\sup_x \Gamma(I,x) > \Gamma_{\min}$. An opt-in `'kl_bar'` mode instead connects agents whose joint symmetric mean post-transport KL falls below a raw threshold.

### Meta-agent construction (covariance-sandwich barycenter)

Given an accepted cluster, `MetaAgentFormation.form_meta_agent` builds the parent by gauge-covariant averaging. Every constituent moment is first transported into a reference frame ($\Omega_{ij}=\Omega_{\mathrm{ref}}\Omega_j^{-1}$), then pooled:

$$
\bar\mu_I(x) = \frac{\sum_i w_i(x)\Omega_{I,i}[\mu_i^{(s)}](x)}{\sum_i w_i(x)},
\qquad
\bar\Sigma_I(x) = \frac{\sum_i w_i(x)\Omega_{I,i}[\Sigma_i^{(s)}](x)\Omega_{I,i}^{\top}}{\sum_i w_i(x)},
$$

with **saddle-point coherence weights**

$$
w_i(x) = \chi_i(x)\exp\big[-\mathrm{KL}\big(q_i^{(s)} \| \bar q_I^{(s)}\big)\big],
$$

solved by fixed-point iteration (the parent estimate from the previous sweep enters the weights at the current step). Both fibers run this independently. Two design choices are explicit in the code: (i) under the high-coherence assumption the dispersion term is dropped, and (ii) the manuscript *rejects* the precision-weighted product-of-experts form — `covariance_pool` (the sandwich above) is canonical, while `precision_pool` ($\Lambda_\alpha=\sum_i w_i\Omega\Lambda_i\Omega^\top$, variance-shrinking "consensus sharpening") is kept only for callers who explicitly want that semantics and has no runtime caller. The contrast is sharp: identical constituents give $\Sigma_\alpha=\Sigma_i$ under the sandwich but $\Sigma_i/N$ under product-of-experts.

The meta-agent's **gauge frames** are a Lie-algebra-additive (first-order [[Baker-Campbell-Hausdorff formula]]) average of the constituent frames,

$$
\phi_I = \sum_i w_i\phi_i,\quad \phi_i=\log\Omega_i,\qquad \Omega_I=\exp(\phi_I),
$$

which is the first-order BCH approximation of the group-valued Karcher barycenter on the non-compact $GL^+(K)$ frame group. The covariance-sandwich pooling is the gauge-covariant analogue of the affine-invariant SPD geometric mean ([[Symmetric spaces and the SPD cone]], [[moakher-2005-geometric-mean]]), itself an instance of the Riemannian center of mass ([[karcher-1977-center-of-mass]]). The comments note $GL^+(K)$ has no bi-invariant metric (so this is an approximation, exact for commuting frames), guaranteed to land in $GL^+(K)$ because $\det(\exp M)=\exp(\mathrm{tr}M)>0$, and restoring the strict-consensus invariant (identical inputs $\to$ identical output) and inverse cancellation. Pooled moments are then re-expressed from the reference frame into the BCH meta-frame via $T=\Omega_{\mathrm{avg}}\Omega_{\mathrm{ref}}^{-1}$ so the stored $(\mu_I,\Omega_I)$ pair is internally consistent (KL is gauge-invariant, so weights are unchanged). The meta-agent's **support** is the no-transport coherence-weighted presence $\chi_\alpha(x)=\sum_i w_i\chi_i(x)/\sum_i w_i$ (fiber rotations do not act on the base-grid scalar $\chi$). On a lattice base, a coarse-grained connection $V_\alpha$ is pooled by the same BCH rule applied to the *bare* edge twists. Coarse-graining is intentionally non-differentiable (`@torch.no_grad()` + `.data.copy_`): meta-agent moments are independently optimized leaves, so pooling is an empirical-Bayes value injection, not a gradient path.

### Top-down feedback (closing the loop)

`TopDownFeedback.propagate_prior` writes the meta-agent's collective belief back into the constituents' *priors* on both fibers:

$$
p_i^{(s)}(x) = \Omega_{i,I}\big[q_I^{(s+1)}\big](x),
\qquad
r_i^{(s)}(x) = \tilde\Omega_{i,I}\big[s_I^{(s+1)}\big](x),
$$

with $\Omega_{i,I}=\Omega_i\Omega_I^{-1}$ (and the model analogue), a blend factor, and a `safe_inv` guard because the BCH-mean frame can be near-singular. This is the participatory step: the emergent collective becomes the prior that constrains its own constituents.

### Soft hierarchical emergence (species × coalition fields)

The differentiable path replaces hard clusters with **field-valued soft membership** over the base manifold. With sigmoid gates,

$$
S_{i\sigma}(x) = \sigma\Big(-\frac{\mathrm{KL}\big(s_i \| \tilde\Omega_{i\sigma}[s_\sigma]\big)}{\tau_{\text{species}}}\Big)\chi_i(x),
\qquad
C_{i\alpha}(x) = \sigma\Big(-\frac{\mathrm{KL}\big(q_i \| \Omega_{i\alpha}[q_\alpha]\big)}{\tau_{\text{belief}}}\Big)\chi_i(x),
$$

with $\tau_{\text{species}}$ large (loose model match) and $\tau_{\text{belief}}$ small (tight belief match), and $W_{i\alpha}=S_{i\alpha}\cdot C_{i\alpha}$. Because both gates carry $\chi_i$, `GatedMembership.compute` divides one $\chi_i$ back out so support is counted once. The **emergent shape** of a meta-agent is

$$
\chi_\alpha(x) = \sum_{i<j} W_{i\alpha}(x)W_{j\alpha}(x) = \tfrac12\Big[\big(\textstyle\sum_i W_{i\alpha}\big)^2 - \sum_i W_{i\alpha}^2\Big],
$$

the `'pairwise'` second-moment form (default), which is identically zero unless at least two constituents overlap at $x$ — confining emergence to true agent–agent overlap regions; a legacy `'sum'` mode gives the unconstrained $\sum_i W_{i\alpha}$. Bottom-up pooling (`_pool_into_parents`) uses the same manuscript covariance-sandwich `covariance_pool` as the hard path; a differentiable `CrossScaleVFE` couples scales through a membership-weighted top-down KL $\sum_{i,\alpha}\int_C W_{i\alpha}(x)[\mathrm{KL}(p_i\|\Omega_{i\alpha}q_\alpha)+\mathrm{KL}(r_i\|\tilde\Omega_{i\alpha}s_\alpha)]dx$.

### Condensation as a phase transition

`CondensationDiagnostics` supplies order parameters. The per-meta-agent **condensation order parameter** is the membership-weighted model-mean variance

$$
\Psi_\alpha = \frac{1}{Z_\alpha}\sum_i w_{i\alpha}\big\|\tilde\Omega_{\alpha i}[s_i]-\bar s_\alpha\big\|^2,
$$

small $\Psi_\alpha$ meaning condensed (agents agree, "like Cooper pairs"), large meaning uncondensed ("like free electrons"); metas with fewer than two participants are undefined and report zero. The macroscopic order parameter is the **condensation fraction** $f\in[0,1]$ — the share of (participating) meta-agents below a threshold — running from $f=0$ (paramagnetic / no emergence) through partial condensation to $f=1$ (fully ordered hierarchy).

## In this work

These mechanisms live in two Layer-6/7 modules of `MAgent_Model`:

- `gauge_agent/meta_agents.py` — `ConsensusDetector` (Gibbs $\Gamma$, `find_clusters`), `MetaAgentFormation.form_meta_agent` (covariance-sandwich barycenter, saddle-point weights, BCH frame mean), and `TopDownFeedback.propagate_prior`. The README maps `MetaAgentFormation.form_meta_agent` to the manuscript meta-agent saddle-point (line 1907) and `TopDownFeedback.propagate_prior` to top-down propagation (line 1965).
- `gauge_agent/hierarchical_emergence.py` — `SpeciesDetector`, `CoalitionDetector`, `GatedMembership`/`SoftMembership` (the $W=S\cdot C$ fields), `covariance_pool` vs `precision_pool`, `CondensationDiagnostics` (order parameter and condensation fraction), `CrossScaleVFE`, and the full `HierarchicalEmergence` tower.

It is exercised by the `'hierarchy'` preset (species × coalition gated membership + condensation, manuscript §4.2) and feeds the `'ouroboros'` multi-scale tower (§4.5–4.7). The construction grounds out in the source manuscript [[participatory-it-from-bit]], which develops the participatory "It From Bit" loop the meta-agent / top-down cycle realizes. It composes with the related concepts [[Multi-agent variational free energy]], [[Agents as fibre-bundle sections]], [[Meta-entropy]] (the thermodynamic counting of belief configurations), and [[Ouroboros multi-scale dynamics]]; the Hamiltonian / inertial belief regime is developed in [[Belief inertia]] and [[belief-inertia]].

## Predictive retention criterion for language parents, October 4, 2026

[[dennis-2026-backprop-free-vfe-language-architecture]] gives a causal language-oriented criterion that sharpens the existing operational parent contract. A proposed word, phrase, or idea parent must retain enough of the consumed prefix to predict future tokens at a declared memory budget; internal coherence, sharp membership, or a higher coarse ELBO is insufficient. For a deterministic retained prefix statistic, the excess one-step log loss decomposes into discarded conditional mutual information plus decoder error. The source treats explicit-duration parents, finite grammar/tree hypotheses, and Bayesian context memory as candidate non-neural parent laws. It leaves activation rules, practical retention tests, and semantic composition open, and does not convert finite formation constructions into a general language-hierarchy result.

## Sources

- [[participatory-it-from-bit]] — source manuscript: gauge-covariant multi-agent variational inference on a $GL(K)$-bundle, with the Ouroboros meta-agent emergence simulation that this construction implements.
- [[degroot-1974-consensus]], [[friedkin1990-social-influence-opinions|friedkin-johnsen-1990]], [[hegselmann-2002-opinion|hegselmann-krause-2002]] — consensus and bounded-confidence opinion dynamics that the belief-coherence clustering generalizes.
- [[wilson-1975-renormalization-group]], [[galam-2008-sociophysics]] — coarse-graining / hierarchical-aggregation precedents for the species-gated condensation and culture-closure test.
- [[moakher-2005-geometric-mean]], [[karcher-1977-center-of-mass]] — affine-invariant SPD geometric mean and the Riemannian center of mass that the covariance-sandwich barycenter realizes on the belief manifold.
- [[dietrich-list-2016-opinion-pooling]], [[genest-zidek-1986-pooling]] — probabilistic opinion-pooling theory (linear vs logarithmic pools) the gauge-covariant moment averaging generalizes.
- [[waade-2025-as-one-and-many]] — collective active inference treating a group as a single agent, the active-inference framing of the meta-agent / top-down feedback loop.
- [[newman-girvan-2004-community-structure]] — modularity-based community detection, the graph-theoretic precedent for the pair-edge `find_clusters` consensus-graph scheme.
- [[geshkovski-2023-mathematical-transformers]] — clustering/condensation dynamics of tokens in transformers, a mathematical analogue of the meta-agent condensation phase transition.
- [[simon-1962-architecture-complexity]], [[maynard-smith-1995-major-transitions]] — staged assembly through stable subassemblies as the canonical account of why hierarchies exist.
- [[zhou-2005-discrete-hierarchy-group-sizes]], [[palla-2007-social-group-evolution]] — empirical layering (branching ratio near three) and accretion dynamics of human groups.
- [[smoluchowski-1916-coagulation]] — binary-merger kinetics, the physics prototype of staged aggregation.
- [[mengistu-2016-evolutionary-origins-hierarchy]] — connection costs as the driver of evolved hierarchy, the external evidence that priced formation produces structure.

## See also

- [[Multi-agent variational free energy]]
- [[Agents as fibre-bundle sections]]
- [[Ouroboros multi-scale dynamics]]
- [[Meta-entropy]]
- [[Belief inertia]]
- [[Gauge transformation]]
- [[Parallel transport]]
- [[Baker-Campbell-Hausdorff formula]]
- [[Fisher information metric]]
- [[Precision weighting]]
- [[Community detection and modularity]]
- [[Collective active inference]]
- [[MDL and BIC model selection]]
- [[Symmetric spaces and the SPD cone]]
- [[Gauge-Theoretic Multi-Agent VFE Model]]
