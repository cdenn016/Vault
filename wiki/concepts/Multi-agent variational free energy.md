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
updated: 2026-07-09
---

# Multi-agent variational free energy

The **multi-agent variational free energy (VFE)** is the central objective functional of the [[Gauge-Theoretic Multi-Agent VFE Model]]. It generalises the single-agent [[Variational free energy]] of active inference (the [[parr-2022-active-inference]] / [[friston-2017-active-inference-process-theory|friston-2017-active-inference-process]] substrate) to a *population* of agents that are realised as [[Agents as fibre-bundle sections|sections of two associated fibre bundles]], each carrying Gaussian beliefs on a *belief* fibre and a *model* fibre with `GL(K)` [[Gauge transformation|gauge frames]]. The whole framework minimises this one scalar; everything else — attention weights, mass, dynamics, hierarchy — is read off from its structure.

## Definition

Let each agent $i$ carry **four** Gaussian distributions over the latent code $k_i \in \mathbb{R}^K$:

- $q_i = \mathcal{N}(\mu_q, \Sigma_q)$ — belief about the latent state,
- $p_i = \mathcal{N}(\mu_p, \Sigma_p)$ — prior on the latent state,
- $s_i = \mathcal{N}(\mu_s, \Sigma_s)$ — the agent's *model* of reality,
- $r_i = \mathcal{N}(\mu_r, \Sigma_r)$ — prior on that model.

Beliefs are compared across agents by **gauge transport** through the `GL(K)` frames: $\Omega_{ij} = \Omega_i\,\Omega_j^{-1}$ on the belief fibre and an *independent* $\tilde\Omega_{ij} = \tilde\Omega_i\,\tilde\Omega_j^{-1}$ on the model fibre. The canonical functional (the manuscript's Eq. 24, implemented in `free_energy.py`) is the five-term form

$$
S[\{q_i\},\{p_i\},\{s_i\},\{r_i\},\{\Omega_i\},\{\tilde\Omega_i\}]
= \underbrace{\sum_i \int \chi_i\, D_{\mathrm{KL}}(q_i\|p_i)\,dc}_{\text{T1: belief self-consistency}}
+ \underbrace{\lambda_h \sum_i \int \chi_i\, D_{\mathrm{KL}}(s_i\|r_i)\,dc}_{\text{T2: model self-consistency}}
$$
$$
+ \underbrace{\sum_{ij}\int \chi_{ij}\big[\beta_{ij}D_{\mathrm{KL}}(q_i\|\Omega_{ij}[q_j]) + \tau\beta_{ij}\log(\beta_{ij}/\pi_{ij})\big]dc}_{\text{T3: belief alignment}}
+ \underbrace{\sum_{ij}\int \chi_{ij}\big[\gamma_{ij}D_{\mathrm{KL}}(s_i\|\tilde\Omega_{ij}[s_j]) + \tau\gamma_{ij}\log(\gamma_{ij}/\pi^{(s)}_{ij})\big]dc}_{\text{T4: model alignment}}
$$
$$
- \underbrace{\sum_i \int \chi_i\, \mathbb{E}_{q_i}[\log p(o\mid q_i)]\,dc}_{\text{T5: observation}} .
$$

Here $\chi_i(c)$ is agent $i$'s spatial support function over the base manifold, $\chi_{ij}=\chi_i\chi_j$ is the pairwise overlap, $d\mu(c) = \sqrt{|g|}\,d^{n}c$ carries the volume form, and the attention weights are softmaxes of the (transported) [[Prediction error|alignment energies]]:

$$
\beta_{ij} = \mathrm{softmax}_j\Big(-\tfrac{D_{\mathrm{KL}}(q_i\|\Omega_{ij}[q_j])}{\kappa\sqrt{K}} + \log\pi_{ij}\Big), \qquad
\gamma_{ij} = \mathrm{softmax}_j\Big(-\tfrac{D_{\mathrm{KL}}(s_i\|\tilde\Omega_{ij}[s_j])}{\kappa\sqrt{K}} + \log\pi^{(s)}_{ij}\Big).
$$

The crucial point recorded in both files is that $s_i \ne p_i$: an agent separately represents *what it thinks is happening* ($q_i$), *what it expected* ($p_i$), *what it thinks its model is* ($s_i$), and *what it expected its model to be* ($r_i$). T4 aligns the model fibre $s_i$ across agents — this is the framework's notion of **ontology sharing** ("what makes science possible — agents must agree not just on beliefs but on the MODEL itself").

## Why it matters here

This functional is the object the entire [[Gauge-Theoretic Multi-Agent VFE Model]] minimises; it is what makes the model *multi-agent* rather than a stack of independent active-inference agents, placing it within the wider programme of [[Collective active inference]]. Three roles:

1. **Coupling through transport.** T3 and T4 compare beliefs after transport. The Regime-I vertex cocycle forces trivial loop holonomy but permits nonidentity pairwise transport. Only the shared-frame or edge-independent constant reduction gives identity transport, whose isotropic score is identity-bilinear plus a key-norm bias; arbitrary learned QK structure is not recovered from transport. [[gl-k-attention-2026-07-09-review-revision]]

2. **Attention is emergent, not assumed.** The entropy term makes softmax the conditional row minimizer for fixed energies. It does not make a one-step belief update an argmin or CAVI step. The canonical and entropy-suppressed belief vector fields agree exactly only when the softmax energy-gradient covariance gap vanishes; joint canonical stationarity alone is insufficient. [[gl-k-attention-2026-07-09-review-revision]]

3. **It is the potential for the dynamics.** Its gradient drives the [[Natural gradient]] flow (`NaturalGradientDynamics`) in the overdamped regime and acts as the potential energy $V$ in the [[Hamiltonian belief dynamics]] regime, where the [[Mass as Fisher information|Fisher precision tensor supplies the inertial mass]] — the [[belief-inertia]] story.

## Details

**State-dependent precision (adaptive $\alpha$).** Beyond the bare five-term form, `FullVFE` weights the self-consistency terms by a *context-dependent precision field* $\alpha_i(x)$ ([[Precision weighting]]) derived from a log-barrier regulariser (Section 2.11.2):

$$
\alpha_i^\*(x) = \frac{c_0}{b_0 + D_{\mathrm{KL}}(q_i(x)\|p_i(x))}, \qquad
R(\alpha) = b_0\,\alpha - c_0\log\alpha .
$$

T1 then reads $\int \chi_i\,\alpha_i(x)\,D_{\mathrm{KL}}(q_i\|p_i)\,dc$, and the bracket $[\alpha\cdot\mathrm{KL} + R(\alpha)]$ is added as a *single unit*. The closed-form optimum $\alpha^\*=c_0/(b_0+\mathrm{KL})$ means agents *near* their prior trust it more (high $\alpha$) and agents *far* from it loosen it (low $\alpha$). The per-agent $b_0, c_0$ (and $\tilde b_0, \tilde c_0$ for the model fibre) live on the model fibre as a slowly-evolving "genotype": specialists carry high $c_0/b_0$, generalists low. A subtle gradient identity is pinned in the code: because $R$ is the Legendre dual of $\alpha\cdot\mathrm{KL}$, the $\partial\alpha/\partial\theta\cdot\mathrm{KL}$ piece is exactly cancelled by $R'(\alpha)\,\partial\alpha/\partial\theta$, so the coefficient on $\partial\mathrm{KL}/\partial\theta$ collapses to the *envelope* result $\alpha^\*$ rather than a naive product-rule expression.

**Generalised divergence.** Every divergence dispatches through a single Rényi $\alpha$-order knob (`divergence_alpha`): $\alpha=1$ short-circuits to the canonical Gaussian [[Variational free energy|KL]], while $\alpha\ne1$ invokes the closed-form Gaussian [[Renyi divergence|Rényi $\alpha$-divergence]] (manuscript §"Generalisation to Rényi $\alpha$-divergence"). This makes T1–T4 and the hyperprior a one-parameter family ([[Alpha-divergence]]).

**Optional extensions.** Off by default ($\lambda=0$), `FullVFE.forward` can add:

- **T6 hyperpriors** — $\sum_i\sum_{k=1}^{D}\rho^k\int\chi_i\,D_\alpha(s_i\|\tilde\Omega_{i,A_k}[s_{A_k}])\,dc$, a multi-scale *model-fibre* chain pulling each agent toward its transported ancestors at generational depth $1\!\ldots\!D$ with exponentially decaying weight $\rho^k$. This is the cross-scale coupling supplied by the Ouroboros tower; gradients are kept live so the variational signal flows top-down into ancestors ([[Meta-agents and hierarchical emergence]], [[Ouroboros multi-scale dynamics]]).
- **R1 gauge smoothness** — $\lambda_\varphi\sum_i\int\|A_\mu\|_F^2\sqrt{|g|}\,dc$ on the connection one-form $A_\mu = U^{-1}\partial_\mu U$, a weak gauge-aware [[Parallel transport]] smoothness prior.
- **R2 Yang–Mills** — $\lambda_F\int\mathrm{tr}(F_{\mu\nu}F^{\mu\nu})\sqrt{|g|}\,dc$, the strictly gauge-invariant curvature penalty ([[Holonomy]]) computed from lattice-gauge plaquettes ([[yang-mills-1954]]).

**Bundle assembly.** `FullVFE.forward` caches one snapshot of the $(\mu,\Sigma)$ state for the four fibres, computes the pairwise transported KL fields $E_{ij}$ (chunked over the agent axis to bound memory), forms $\beta/\gamma$, and assembles
$$
\text{total} = \lambda_{\text{self}}(T1 + R_\alpha) + \lambda_h(T2 + \tilde R_\alpha) + \lambda_{\text{belief}}T3 + \lambda_{\text{model}}T4 + \lambda_{\text{obs}}T5 \;(+\,\lambda_{\text{hyper}}T6 + \lambda_{\text{smooth}}R1 + \lambda_{\text{ym}}R2).
$$
The self-diagonal of $E$ is zeroed (self-KL is owned by T1/T2, not the alignment terms), and a detached per-agent partition $F_{\text{per agent}}$ is returned for diagnostics, with the field-level $R1, R2, T6$ tracked as a global residual so the per-agent curves reconcile to `total`.

> [!note] Editorial: A consequence noted in `full_vfe.py` is that the entropy-corrected $F^\*$ is *unbounded below in $\tau$*, so the softmax temperature $\kappa$ should be set as a precision hyperprior rather than learned by gradient descent (learnable $\kappa$ is disabled by default and warns).

## In this work

- **Code.** Two implementations: `gauge_agent/free_energy.py` holds the simplified five-term `FreeEnergyFunctional` (used by `ouroboros.py`, `mass.py`, `renormalization.py`, `manifold_system.py`), and `gauge_agent/full_vfe.py` holds `FullVFE` — the full functional with adaptive precision, T6 hyperpriors, and the R1/R2 extensions — plus `HierarchicalVFE`, which sums per-scale VFE over the Ouroboros tower and wires the ancestor maps for T6. `FullVFE.forward` corresponds to the manuscript's canonical free energy (README line citation 1232).
- **Manuscript.** Developed in [[participatory-it-from-bit]] (Sections 2.10–2.11, Eq. 24); the single-agent substrate it generalises is [[parr-2022-active-inference]] / [[friston-2017-active-inference-process-theory|friston-2017-active-inference-process]] / [[ramstead-2019-enactive-inference|ramstead-2019-variational-neuroethology]]. Its [[Mass as Fisher information|inertial-mass]] and Hamiltonian extensions are the subject of [[belief-inertia]]; its thermodynamic-limit / counting-measure treatment (configurational [[meta-entropy-manuscript]]) is [[meta-entropy-manuscript]]; the attention recovery and `GL(K)` validation are [[gl-k-attention]].
- **Where it plugs in.** The functional is the potential minimised by `NaturalGradientDynamics` and `HamiltonianDynamics`; its attention weights $\beta,\gamma$ are the model's [[Attention mechanisms — theory and positional structure|attention mechanism]]; its T6 chain and the soft-membership pooling drive [[Belief inertia]]-aware [[Meta-agents and hierarchical emergence|meta-agent emergence]] and the [[Renormalization-group flow of beliefs|RG flow of beliefs]].

## Sources

- [[participatory-it-from-bit]] — primary manuscript developing the framework and Eq. 24.
- [[belief-inertia]] — Fisher-precision-as-mass and the Hamiltonian regime built on this functional.
- [[meta-entropy-manuscript]] — configurational meta-entropy / thermodynamic limit of the gauge-theoretic VFE.
- [[gl-k-attention]] — attention recovered from the gauge-transported KL alignment terms.
- [[parr-2022-active-inference]], [[friston-2017-active-inference-process-theory|friston-2017-active-inference-process]], [[ramstead-2019-enactive-inference|ramstead-2019-variational-neuroethology]] — single-agent VFE substrate.
- [[dempster-1977-em-algorithm|dempster-1977-em]] — the E/M alternation underlying the precision (genotype) vs. belief timescale split.
- [[heins-2024-surprise-minimization]] — surprise minimisation in multi-agent / collective active inference.
- [[friston-2024-federated-inference]] — federated inference and belief sharing across coupled agents.
- [[hinton-2002-products-of-experts|hinton-2002-poe]] — products of experts as a precursor to multiplicative belief combination.
- [[blei-2017-variational-inference]] — variational inference review framing the KL objective minimised here.
- [[bissiri-2016-general-bayesian-updating|bissiri-holmes-walker-2016-general-bayes]] — general Bayesian updating via loss-based KL minimisation.
- [[genest-zidek-1986-pooling]] — logarithmic and linear opinion pooling, the classical belief-aggregation theory behind T3/T4.
- [[nishimori-2001-spin-glasses-information]] — statistical mechanics of inference: the disorder-averaged free energy as the right object for Bayes-optimal collective behavior, with the Nishimori line as the matched-prior condition derived from a gauge symmetry.

## See also

- [[Variational free energy]] — the single-agent objective this generalises.
- [[Agents as fibre-bundle sections]] — how the four distributions and `GL(K)` frames are carried.
- [[Gauge transformation]] · [[Parallel transport]] · [[Holonomy]] — the transport machinery in T3/T4/T6.
- [[Precision weighting]] · [[Alpha-divergence]] · [[Renyi divergence]] — the adaptive-$\alpha$ and divergence generalisations.
- [[Natural gradient]] · [[Hamiltonian belief dynamics]] · [[Mass as Fisher information]] — the dynamics that minimise it.
- [[Meta-agents and hierarchical emergence]] · [[Ouroboros multi-scale dynamics]] · [[Renormalization-group flow of beliefs]] — the multi-scale structure of T6.
- [[Evidence lower bound (ELBO)]] — the variational-bound reading of each KL term.
- [[Collective active inference]] — the broader programme of many agents minimising shared/coupled free energy.
- [[Information bottleneck]] — the rate–distortion reading of the compression–alignment trade-off in the KL terms.
