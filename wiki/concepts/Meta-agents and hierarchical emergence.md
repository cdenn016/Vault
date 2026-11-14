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
updated: 2026-11-14
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

## Gaussian template banks as meta-agents, October 24, 2026

A learned Gaussian template bank in the vfe3 block MLP can be read as a population of parents. The EM M-step of a template, given responsibilities $w_{ia}$ and component posteriors $\mathcal N(m_{ia},P_{ia})$, is the forward-KL barycenter $\arg\min_q\sum_iw_{ia}\mathrm{KL}(\mathcal N(m_{ia},P_{ia})\Vert q)$ with between-child dispersion retained, the definition above at $\lambda=0$; the top-down step is the template acting as each token's prior. The closest published precedents run both directions inside a forward pass: parents fitted to children's votes by EM ([[hinton-2018-matrix-capsules-em-routing]]) and slots competing for inputs ([[locatello-2020-slot-attention]]). A causal in-context version, needed for a language model, would update the parent from the prefix only, by the sequential rule of [[broderick-2013-streaming-variational-bayes]], keeping a fast weight memory of sufficient statistics ([[schlag-2021-fast-weight-programmers]]).

> [!note] Editorial: The barycenter identity was checked numerically in the 2026-10-24 session (single-threaded numpy, two dimensions). The vfe3 bank is currently refit only across the training corpus, so it is a corpus-level population of parents rather than meta-agents formed from the current population. The separate model frame used on this page comes from the earlier participatory framework; MAgent Theory 2.0 (`01_foundations.tex`, presentation-and-probability section) uses one structure-group element for both sectors and does not admit independent model frames.

## Sources

- [[participatory-it-from-bit]] — source manuscript: gauge-covariant multi-agent variational inference on a $GL(K)$-bundle, with the Ouroboros meta-agent emergence simulation that this construction implements.
- [[degroot-1974-consensus]], [[friedkin1990-social-influence-opinions|friedkin-johnsen-1990]], [[hegselmann-2002-opinion|hegselmann-krause-2002]] — consensus and bounded-confidence opinion dynamics that the belief-coherence clustering generalizes.
- [[wilson-1975-renormalization-group]], [[galam-2008-sociophysics]] — coarse-graining / hierarchical-aggregation precedents for the species-gated condensation and culture-closure test.
- [[moakher-2005-geometric-mean]], [[karcher-1977-center-of-mass]] — affine-invariant SPD geometric mean and the Riemannian center of mass that the covariance-sandwich barycenter realizes on the belief manifold.
- [[dietrich-list-2016-opinion-pooling]], [[genest-zidek-1986-pooling]] — probabilistic opinion-pooling theory (linear vs logarithmic pools) the gauge-covariant moment averaging generalizes.
- [[waade-2025-as-one-and-many]] — collective active inference treating a group as a single agent, the active-inference framing of the meta-agent / top-down feedback loop.
- [[newman-girvan-2004-community-structure]] — modularity-based community detection, the graph-theoretic precedent for the pair-edge `find_clusters` consensus-graph scheme.
- [[hinton-2018-matrix-capsules-em-routing]], [[locatello-2020-slot-attention]] — EM-style parent formation (capsules) and slot competition inside a forward pass, precedents for templates as meta-agents.
- [[broderick-2013-streaming-variational-bayes]], [[schlag-2021-fast-weight-programmers]] — sequential posterior updating and fast weight memories for causal in-context parents.
- [[geshkovski-2023-mathematical-transformers]] — clustering/condensation dynamics of tokens in transformers, a mathematical analogue of the meta-agent condensation phase transition.
- [[simon-1962-architecture-complexity]], [[maynard-smith-1995-major-transitions]] — staged assembly through stable subassemblies as the canonical account of why hierarchies exist.
- [[zhou-2005-discrete-hierarchy-group-sizes]], [[palla-2007-social-group-evolution]] — empirical layering (branching ratio near three) and accretion dynamics of human groups.
- [[smoluchowski-1916-coagulation]] — binary-merger kinetics, the physics prototype of staged aggregation.
- [[mengistu-2016-evolutionary-origins-hierarchy]] — connection costs as the driver of evolved hierarchy, the external evidence that priced formation produces structure.
- [[heins-2026-collective-sensing-bayesian-inference]] — commuting criterion between physical evolution and belief update under a fixed coarse-graining map (formulated, not tested).
- [[baltieri-2025-bayesian-internal-model-principle]] — a dynamics-preserving surjection gives the coarse system a consistent possibilistic belief about the fine one (proved, discrete deterministic case).
- [[sakthivadivel-2022-weak-markov-blankets]] — blankets that hold at one scale or timescale and fail at another (informal).
- [[sandved-smith-2024-metacognitive-particles]] — inward nesting of particles holding beliefs about beliefs; conjectured unrepresented innermost level.
- [[ueltzhoffer-2021-thermodynamic-efficiency-dissipative]] — hierarchy of dissipative structures with rising efficiency constraints (heuristic argument).
- [[rosas-2026-symmetry-hierarchical-emergence]] (symmetry-derived closed levels and abstract beliefs; read from the arXiv preprint)

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

## Persistence and composition in Fields's work

Fields and Levin's account of objects and processes emphasizes that recognizing persistence needs a stable boundary criterion and memory. Their discussion of records as interpretative interactions is useful for specifying what a parent must retain. The conscious-agent network paper builds memory and combination through declared kernels, while the perceptual-network study distinguishes stable collective dynamics from autonomous embodiment. These are constructive and conceptual predecessors whose supplied ingredients must remain explicit. [[fields-2025-thoughts-and-thinkers-on-the-complementarity-between-objects-and-processes]], [[fields-2018-conscious-agent-networks-formal-analysis-and-application-to-cognition]], [[prentner-2019-using-ai-methods-to-evaluate-a-minimal-model-for-perception]]

> [!note] Editorial: What transfers
> Semantic composition, a stable attractor, and a normalized predictive parent are different mathematical claims. The source papers can inform the interface and retention questions without establishing a general formation theorem for the current gauge-VFE model. [[Chris Fields and physics as communication]] keeps the comparison tied to each paper's assumptions.

## Collective agents references, November 10, 2026

[[Collective agents literature map]] groups the references ingested on November 10, 2026. Its sections on closure, lumpability and model reduction and on organizations, markets and teams as information processors hold the sources closest to this page, among them [[barnett-2023-dynamical-independence-discovering]], [[shalizi-2025-what-macrostate-subjective]], [[courtois-1977-decomposability-queueing-computer]] and [[list-2011-group-agency-possibility]].

## Error terms for an approximately closed meta-agent, November 11, 2026

The constructions on this page say when a parent exists and what it retains; they do not say how wrong a parent's belief is when the summary it models is not closed. [[Approximate meta-agent theorem]] collects the first such statements, from [[dennis-2026-collective-agents-approximate-meta-agent]], in a linear-Gaussian model of communicating agents: a bound, with no smallness condition, on the excess relative entropy of a collective that filters a non-closed coarse exterior with a Markov model; an assembled theorem in which the coarse blanket and the closure of the coarse internal state stay exact while the abstract physics, the belief and the joint act carry error terms; and a bound on the memory of the average of members that fuse literally, whose closure defect in information form has a floor that mixing does not lower. These statements concern that model and transfer to the gauge-VFE meta-agent only as a template for what an error analysis must contain.

## Error terms without exact blanket conditions and for literal members, November 11, 2026

The statements of the preceding section keep the blanket conditions exact and give members that fuse literally a bound on memory only. [[dennis-2026-collective-agents-approximate-blanket-conditions]] removes both restrictions in the same linear-Gaussian model. When the conditions that make the coarse sensory state and the coarse act a blanket fail, a parent still has an exactly closed coarse internal state and an exact group posterior over acts, provided the members run a consensus filter on shared declared models. Its belief is measured against what the members' channels jointly determine about the exterior, and it pays for the defects of its declared dynamics and observation model and for whatever its coarse sensory state discards. The last cost is specific to a parent: when only the weights of the summary are wrong, the other models are declared truthfully and the collective reads its sensors through the summary alone, a summary that is not sufficient for the members' channels sets a term that no declared input matrix removes. For members that fuse literally, the belief carried by their average has an exact excess relative entropy, the inefficiency of the average as an estimator plus the price of a miscalibrated claimed variance, and the autocorrelation of the error of their average departs from a geometric sequence by an amount bounded through the dispersions of the update when the exterior is held fixed. [[Approximate meta-agent theorem]] gives the statements and the list of what remains open; the caveat on transfer to the gauge-VFE meta-agent stated in the preceding section applies unchanged.

## Consensus, relays and elimination across levels, November 11, 2026

Four statements of [[dennis-2026-collective-agents-renormalization-results]] concern what passes between the levels of a hierarchy of collectives in the linear-Gaussian model of the collective-agents manuscript. A hierarchy that pools information contributions with finitely many consensus rounds per level miscounts each agent's contribution by a factor whose error compounds multiplicatively over the levels, with an attained bound ([[Decentralized Bayesian inference]]). The content shared along a relay of codes has an effective rank that falls with hop distance when the codes share a direction and need not fall monotonically when they do not, and a meta-level hop that averages its members' projections first raises the rank and then lowers it with depth ([[Effective rank along relays]]). Eliminating the internal states of members without memory has an error of first order in the ratio of timescales, with a proved coefficient under stated hypotheses ([[Coarse Graining]]). Decimating the nearest-neighbor lattice medium in two or more dimensions generates couplings of unbounded range that decay exponentially at a proved rate ([[Renormalization group flow]]). As with [[Approximate meta-agent theorem]], these statements concern that model, and they bear on the gauge-VFE meta-agent as examples of what a theory of levels has to quantify.

## Criteria and templates for emergent levels from the Bayesian mechanics batch, November 13, 2026

Five sources ingested on November 13, 2026 bear on what a claim of an emergent level must show. [[heins-2026-collective-sensing-bayesian-inference]] states in its Appendix B the test that would establish that a collective realizes a group-level inference: for a fixed coarse-graining map $C$, physical evolution $F_y$ and belief update $B_y$, the two should commute within a stated error, $C(F_y(s)) \approx B_y(C(s))$. The paper formulates the test and does not carry it out. [[baltieri-2025-bayesian-internal-model-principle]] proves a discrete, deterministic relative of this square. When an autonomous system $\mathsf{M}$ models $\mathsf{X}$ through a state surjection $\mu_s$ that commutes with the dynamics, updating $\mathsf{M}$ and then taking the fiber $\mu_s^{-1}$ equals taking the fiber and then applying the coarsened dynamics of $\mathsf{X}$ (Proposition IV.2), and the fibers give a consistent possibilistic filtering interpretation (Theorem IV.5) whose beliefs are disjoint sets that ignore observations.

On nesting, [[sakthivadivel-2022-weak-markov-blankets]] describes informally strongly mixing subsystems with very weak blankets that form a cohesive whole at a larger scale, and sketches an adiabatic argument that separation of timescales leaves many zero entries in the solenoidal matrix. [[sandved-smith-2024-metacognitive-particles]] nests inward: a particle inside a particle holds beliefs about the sufficient statistics of the outer level's belief, a definition extended to $N$ levels, with an informal argument that the depth is finite and a conjectured innermost core that is never the target of further beliefs. [[ueltzhoffer-2021-thermodynamic-efficiency-dissipative]] argues heuristically, without simulation of this part, that dissipative structures each feeding on the gradient left by the previous level form a hierarchy in which the minimum viable efficiency rises with level; that paper uses no blankets and makes no inference claim.

> [!note] Editorial: bearing on the gauge-VFE meta-agent
> The commuting condition states what the barycenter construction on this page owes: the pooled parent, evolved by its own update, should agree with the pooling of the evolved constituents within a stated error. Proposition IV.2 is a candidate formal template for that square. The match is an analogy, since its beliefs are possibilistic sets with no Gaussian, Fisher or transport structure. The inward nesting and the dissipative hierarchy are analogies as well.

## Symmetry-derived levels and matching belief hierarchies, November 14, 2026

[[rosas-2026-symmetry-hierarchical-emergence]] adds a mechanism to the criteria collected in the preceding section, in a setting far from this page's construction: finite groups acting on discrete-state, discrete-time Markov processes (version read: the arXiv preprint arXiv:2512.00984v1; the Science Advances text was not available). A Markov kernel that is equivariant under a group $G$ has an informationally closed orbit variable for every subgroup of $G$, and the level of a larger subgroup is closed with respect to the level of a smaller one, so the subgroup lattice supplies a hierarchy of exactly closed levels (its Corollaries 1 and 2). On the observer's side, if the measurement channel and the initial law share the symmetry, the orbit variables of state and measurement form a hidden Markov model, and the belief $b^*_t=p(z_t\mid v_{0:t})$ about a coarse level updates by a Bayesian filter that never consults the finer level (Theorem 2 and Corollary 3). A commuting square of the kind that [[heins-2026-collective-sensing-bayesian-inference]] formulates as a test and [[baltieri-2025-bayesian-internal-model-principle]] proves for possibilistic beliefs appears here between two levels of one observer's probabilistic beliefs, and not between a collective's physical evolution and a belief update: under the condition $I(Z_t;Y_{0:t})=I(Z_t;V_{0:t})$ of Corollary 4, marginalizing the micro-level belief and then updating equals updating and then marginalizing, $b^*_t=P_{\phi_G}b_t$. Without that condition the coarse belief is still the exact posterior given the coarse record, with its own update, and is less informative than the marginal of the fine belief; the paper's Ehrenfest example is of this second kind. The paper presents equivariance as sufficient for such hierarchies and names Markov lumpability as the necessary condition. The statements are given in full on [[Coarse Graining]].

> [!note] Editorial: bearing on the gauge-VFE meta-agent
> The relation is interpretive, and three differences block an exact transfer. First, the paper's coarse-grainings are orbit maps, which are invariant under the group, whereas the barycenter on this page is described as gauge-covariant, transforming with the frames, so the parent is not the orbit variable of the frame group. The symmetry whose orbits resemble pooling is permutation of the members of a cluster; its orbit variable is the multiset of member states, and a barycenter is a coarser function of that multiset which Corollaries 1 and 2 do not cover. Second, the paper assumes a finite group, discrete states, discrete time, a fixed Markov kernel and a fixed group action, whereas the construction here has the continuous non-compact group $GL^+(K)$, Gaussian parameters, and memberships and top-down priors that change when a parent forms. Third, whether the model's update, read as a transition law, is equivariant under any of these actions is not asserted here. What the paper supplies is a pair of exact conditions to aim at: a parent level is closed when it is the orbit variable of a symmetry of the dynamics, and its belief agrees with the marginal of the members' joint belief when the coarse record is sufficient in the sense of Corollary 4. [[Group equivariance]] records what Corollary 2 implies for global and local group actions.
