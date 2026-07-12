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
updated: 2026-07-11
---

# Gauge-Theoretic Multi-Agent VFE Model

## Goal

The Gauge-Theoretic Multi-Agent VFE Model (codebase `MAgent_Model`) builds and studies a population of interacting agents whose collective dynamics *is* variational inference. Each agent is a smooth section of two associated fibre bundles over a base manifold, carrying Gaussian beliefs on a belief fibre and a model fibre, each equipped with a $GL(K)$ gauge frame. The population descends a single shared objective — a [[Multi-agent variational free energy]] — and the resulting trajectories recover, generalize, and extend classical consensus and opinion-dynamics models on the social-science side while behaving as a genuine dynamical system (oscillation, momentum, resonance) on the physics side.

This is the continuous-time, multi-agent, dynamical-systems instantiation of the same theory that the [[VFE Transformer Program]] instantiates as a language model. Both rest on $GL(K)$ gauge-transported KL divergence between Gaussian "agents" and both minimize a variational free energy; the transformer reads tokens as agents in a forward pass, while this project lets agents-as-bundle-sections evolve in real time under explicit dynamics. The framework is the author's own, developed in the manuscripts [[participatory-it-from-bit]] and [[gl-k-attention]], and is the computational realization of a participatory "it from bit" program ([[wheeler-1990-it-from-bit]]).

## Architecture / approach

The implementation is grounded throughout in manuscript line citations; the structures below are read from the repository's `README.md`, the `gauge_agent.full_vfe` docstring, and the single `CONFIG` dict in `run_experiment.py`.

**Agents as bundle sections.** Each agent is a section of two associated fibre bundles over a base manifold, formalizing [[Agents as fibre-bundle sections]]. An agent carries *four* Gaussian distributions, not one: a belief $q_i = \mathcal{N}(\mu_q, \Sigma_q)$ ("what I think is happening"), a belief prior $p_i$ ("what I expected"), a model belief $s_i$ ("what I think my model is"), and a model prior $r_i$ ("what I expected my model to be"). The belief and model fibres each carry an independent $GL(K)$ gauge frame, with frame change being a [[Gauge transformation]] and inter-agent comparison performed by [[Parallel transport]] of one agent's belief into another's frame via $\Omega_{ij} = \Omega_i \Omega_j^{-1}$ (and an *independent* model-fibre transport $\tilde{\Omega}_{ij}$). The bundle-theoretic substrate — connections, parallel transport, curvature, [[Holonomy]] — follows the standard differential-geometric machinery ([[kobayashi-nomizu-1963-foundations]], [[nakahara-2003-geometry-topology-physics]], [[baez-muniain-1994-gauge-fields]], [[frankel-2011-geometry-of-physics]]), with the non-abelian gauge principle itself in the tradition of [[yang-mills-1954]]. Each agent's spatial support is a function $\chi_i(c)$ over the base manifold, which for sampled populations becomes a smoothed geodesic ball.

**The multi-agent VFE.** The `FullVFE` functional is the canonical five-term boxed equation of the manuscript, integrated over the base manifold against the support $\chi_i$ and the volume form $\sqrt{|g|}$:

$$
\mathcal{F} = \sum_i \!\int_C\! \chi_i\, \alpha_i\, \mathrm{KL}(q_i \| p_i)
+ \sum_i \!\int_C\! \chi_i\, \tilde\alpha_i\, \mathrm{KL}(s_i \| r_i)
+ \sum_{ij} \!\int_C\! \chi_{ij}\, \beta_{ij}\, \mathrm{KL}(q_i \| \Omega_{ij}[q_j])
+ \sum_{ij} \!\int_C\! \chi_{ij}\, \gamma_{ij}\, \mathrm{KL}(s_i \| \tilde\Omega_{ij}[s_j])
- \sum_i \!\int_C\! \chi_i\, \mathbb{E}_{q_i}[\log p(o\,|\,q_i)]
$$

The five terms are, in order, belief self-consistency, model self-consistency (ontology held against its own prior), belief alignment across agents, model alignment across agents (ontology *sharing*), and the observation/likelihood term, plus a precision regularizer $R(\alpha)$. The inter-agent coupling weights are attention coefficients $\beta_{ij} = \mathrm{softmax}(-\mathrm{KL}(q_i \| \Omega_{ij}[q_j]) / \tau)$ for beliefs and $\gamma_{ij}$ for models — this is the gauge-transported, KL-based attention shared with [[gl-k-attention]]. The precision $\alpha_i(x) = c_0 / (b_0 + \mathrm{KL}(q_i \| p_i))$ is state-dependent and pointwise, realizing [[Precision weighting]] / [[Prediction error]] gating through a closed-form log-barrier ($R(\alpha) = b_0 \alpha - c_0 \log \alpha$) that keeps $\alpha > 0$ and finite. Optional extensions in the functional include a gauge-smoothness term, a Yang-Mills $\mathrm{tr}(F_{\mu\nu}F^{\mu\nu})$ term, and multi-generation hyperpriors. KL is the default divergence, with a Rényi/alpha family available ([[Renyi divergence]], [[Alpha-divergence]]). The construction sits on information geometry's invariant foundations — the Fisher-Rao/Chentsov metric being the unique invariant choice ([[cencov-1982-statistical-decision-rules]], [[ay-2017-information-geometry]], [[amari-2016-information-geometry-applications]]) — and generalizes the single-agent active-inference VFE substrate ([[parr-2022-active-inference]], [[friston-2017-active-inference-process-theory|friston-2017-active-inference-process]], [[ramstead-2019-enactive-inference|ramstead-2019-variational-neuroethology]]) to the multi-agent, gauge-theoretic setting. See [[Fisher information metric]] and [[Variational free energy]].

**The dynamics toggle.** The integrator is selected by a single config field, `dynamics.dynamics`:

| Setting | Integrator | Regime |
| --- | --- | --- |
| `natural_gradient` (default) | First-order, Fisher-preconditioned descent | Overdamped |
| `hamiltonian` | Second-order symplectic leapfrog | Conservative / underdamped |

The natural-gradient path is overdamped flow preconditioned by the inverse [[Fisher information metric]] (the [[Natural gradient]]), guarded by gauge-aware trust regions (a per-step KL bound on $\mu$, an SPD-Fisher bound on $\Sigma$, and a spectral-norm bound on the Lie-algebra $\Omega$ step). The Hamiltonian path is symplectic leapfrog in which the precision/Fisher tensor doubles as an inertial *mass*, giving rise to [[Hamiltonian belief dynamics]], [[Belief inertia]], and the identification of [[Mass as Fisher information]]. The entropic-inference precedent for "belief dynamics as inference" is Caticha's program ([[caticha-2019-entropic-dynamics-qm|caticha-2019-entropic-dynamics]]); the coordinate-ascent / EM reading of the overdamped descent connects to [[dempster-1977-em-algorithm|dempster-1977-em]].

**The run modes.** `CONFIG['mode']` selects the class of experiment:

| `mode` | What it exercises | Concept |
| --- | --- | --- |
| `basic` | Flat, single-scale dynamics (natural-gradient or Hamiltonian) | — |
| `ouroboros` | Multi-scale tower with bottom-up formation, opt-in top-down writes, and multi-generation hyperpriors | [[Ouroboros multi-scale dynamics]] |
| `hierarchy` | Species × coalition gated soft membership and condensation into meta-agents | [[Meta-agents and hierarchical emergence]] |
| `rg` | Renormalization-group flow with KL-proximity blocking | [[Renormalization-group flow of beliefs]] |

The `ouroboros` mode provides the machinery for a self-referential, multi-scale loop. On the reviewed `779f96f` configuration it executes bottom-up tower formation while both top-down shadow-write flags are disabled, so full bidirectional feedback remains an opt-in branch. The `hierarchy` mode detects consensus and condenses sub-populations into emergent meta-agents whose footprint $M_\alpha(x) = \sum_i W[i,\alpha,x]\chi_i(x)$ can be visualized, and the `rg` mode coarse-grains beliefs scale by scale in the manner of Wilson's renormalization group ([[wilson-1975-renormalization-group]]). [[participatory-it-from-bit-2026-07-11-code-concordance-review]]

## Relation to the transformer

This project and the [[VFE Transformer Program]] are sibling instantiations of one theory. Both define agents as Gaussian distributions on a statistical fibre bundle with $GL(K)$ gauge frames, both compute inter-agent coupling as the softmax of a gauge-transported KL divergence, and both minimize a variational free energy over those beliefs. The shared "[[gl-k-attention|attention as gauge-theoretic variational inference]]" core is what makes them two faces of the same construction: in the flat-bundle, isotropic-Gaussian limit the gauge-transported KL-consensus problem reduces to standard scaled dot-product attention.

The difference is the instantiation. The transformer is the **language** instantiation: agents are tokens, "time" is the discrete forward pass, and the model is validated as a working language model (per [[gl-k-attention]] and [[participatory-it-from-bit]]). This project is the **continuous-time multi-agent dynamical** instantiation: agents are persistent bundle sections evolving under explicit overdamped or Hamiltonian dynamics, exposing phenomena — momentum, oscillation, resonance, multi-scale emergence, RG flow — that a single forward pass cannot. The thermodynamic-limit bridge between the discrete transformer and the continuum population is developed in [[meta-entropy-manuscript]].

## Manuscripts

- [[participatory-it-from-bit-2026-07-11-code-concordance-review]] — major-revision code-concordance record for the PIFB2 repository mirror and executable MAgent baseline at `779f96f`; the review is commit-scoped and does not claim exhaustive coverage of the differing Research-vault WIP.

- [[participatory-it-from-bit]] — the primary manuscript this codebase implements: a gauge-covariant multi-agent variational-inference framework on a principal $GL(K)$-bundle, recovering transformer attention as a gauge-fixed isotropic-Gaussian limit and including the Ouroboros meta-agent emergence simulation that the `ouroboros` mode runs.
- [[belief-inertia]] — the [[Belief inertia]] / [[Mass as Fisher information]] result: the Fisher-information precision tensor doubles as an inertial mass, recovering DeGroot, Friedkin-Johnsen, and bounded-confidence opinion dynamics in the overdamped limit and predicting oscillation, overshoot, resonance, and social momentum transfer in the underdamped Hamiltonian regime.
- [[meta-entropy-manuscript]] — the configurational [[Meta-entropy]] $S_{\mathrm{meta}} = \log W$ counting belief configurations at fixed free energy, fixed by the Fisher-Rao volume and rendered extensive via Kac normalization, supplying the thermodynamic-limit bridge for the gauge-theoretic free-energy transformer.
- [[gl-k-attention]] — the [[Multi-agent variational free energy]] / gauge-attention derivation shared with the transformer: attention as the softmax of a gauge-transported KL divergence between Gaussian agents.

## Applications

**Physics.** The Hamiltonian regime is exercised on a multi-agent oscillator (the `hamiltonian_oscillator` preset) and on a photon-style minimal-coupling construction (see [[Non-flat connection and the photon analogy]]), where the complex / Lorentzian gauge module and lattice gauge field (plaquette holonomy, Yang-Mills) come into play. A 2026-06-18 audit found this sector to be the gauge-covariant half of the photon picture — a genuine non-flat connection with a Yang-Mills kinetic term wired into the free energy, fixing the gauge-covariance break that the sibling [[VFE Transformer Program]]'s `regime_ii` carries. The open second half — the minimal-coupling belief vertex (`lambda_belief_neighbor`) that lets the connection do covariant-derivative work *on* the beliefs — was then implemented the same day (`gauge_agent/belief_neighbor.py`) and wired to the *same* lattice connection the Yang-Mills term penalizes (the `belief_neighbor_from_lattice` toggle reindexes the `LatticeGaugeField` twists into the vertex's base links), so MAgent now realizes both halves of the photon; the term is default-off and opt-in. The current `ym_bounded=True` and `ym_action_form="frobenius"` defaults select the nonnegative plaquette deficit $\sum_\square\lVert W(\square)-I\rVert_F^2$. This term is smooth at flatness and detects unipotent shear, but it is a frame-metric penalty invariant only under orthogonal vertex reframing, not a full-$\mathrm{GL}(K)$ conjugation-invariant action. The opt-in spectral form $\sum_k|\lambda_k(W)-1|$ is a conjugation-invariant semisimple diagnostic, but it vanishes on nonidentity unipotent holonomy and has unstable gradients when eigenvalues coalesce. The connection's edge twists are optimized in the M-step with a bounded Lie-group retraction. See [[Non-flat connection and the photon analogy]]. These connect to the participatory-physics cluster: entropic dynamics ([[caticha-2019-entropic-dynamics-qm|caticha-2019-entropic-dynamics]]), QBism ([[fuchs2014-qbism-locality|fuchs-2014-qbism]]), relational quantum mechanics ([[rovelli-1996-relational-qm]]), evolution-without-evolution ([[page-wootters-1983]]), entanglement-built spacetime ([[VanRaamsdonk-2010-spacetime-entanglement|vanraamsdonk-2010-entanglement-spacetime]]), decoherence/einselection ([[zurek-2003-einselection|zurek-2003-decoherence]]), and the participatory ontology of [[wheeler-1990-it-from-bit]] via [[Participatory realism (it from bit)]].

**Social science.** The overdamped regime is the home of opinion dynamics. As established in [[belief-inertia]], the natural-gradient flow recovers DeGroot consensus ([[degroot-1974-consensus]]), the Friedkin-Johnsen anchored-influence model ([[friedkin1990-social-influence-opinions|friedkin-johnsen-1990]]), and bounded-confidence dynamics ([[deffuant2000-bounded-confidence|deffuant-2000-bounded-confidence]], [[hegselmann-2002-opinion|hegselmann-krause-2002]]), within a sociophysics tradition ([[galam-2008-sociophysics]]). The underdamped Hamiltonian regime adds genuinely dynamical predictions — opinion oscillation, overshoot, resonance, and momentum transfer — absent from the classical averaging models. Consciousness-adjacent participatory framings ([[seth-2021-being-you]], [[tononi-2016-iit]]) motivate the self-modeling agent.

## Status & next steps

The July 11 code-concordance review supersedes the earlier all-clear status for claims that join [[participatory-it-from-bit|PIFB2]] to the reached MAgent runtime. It adjudicated five High, six Medium, and one Low finding at baseline `779f96f`. The load-bearing corrections concern common-right frame-update equivariance, closure of hierarchical pooling on the real-log domain, the detector-temperature and covariance-collapse pairing, disabled belief-shadow propagation, and one-shot lineage persistence. The recommendation is major revision before presenting the manuscript as a code-backed Methods paper. [[participatory-it-from-bit-2026-07-11-code-concordance-review]]

Per the repository `README.md`, the codebase is at a hardened, click-to-run stage:

- Earlier formal audits closed their recorded blockers and follow-up majors; the July 11 review identified a separate set of manuscript-to-runtime defects that remains open.
- 83 numerical asserts pin manuscript-canonical equations (70 blocker + 7 numerical-monitor + 6 manifold-visualization).
- Single click-to-run entry point (`run_experiment.py`) with four modes and a full artifact pipeline (metrics, rotating checkpoints, publication figures, verifier report).
- Real-time numerical-health monitor with KL, SPD, and spectral trust-region guards on the natural-gradient path (AUDIT6-8).

> [!note] Editorial: The README lists dormant / architectural follow-ups in `PURIFICATION_PLAN.md` but does not enumerate quantitative experimental results in the file read; specific run outputs (loss curves, emergence statistics) are not quoted here because they are not present in the grounding files.

Next steps, in rough priority order:

1. Settle one frame-space contract across the symmetry statement, metric, regularizer, update, and admitted subgroup, then make hierarchical pooling closed on that domain without an unconditional real logarithm.
2. Pair detector temperature with a covariance collapse that has the claimed error control, and make belief/model shadows, T2, and T6 a non-duplicative executable contract.
3. Add dynamic membership or declare a one-shot genealogy; implement the stated nonequilibrium statistic, time-dependent forcing, tower-aware recording, lineage events, and cryptographic provenance before running the prospective validation.
4. After those corrections, persist representative mode artifacts, quantify the [[belief-inertia]] predictions against classical baselines, and tighten the [[meta-entropy-manuscript]] thermodynamic-limit correspondence.

## Cross-links

**Sibling project:** [[VFE Transformer Program]]

**Key concepts:** [[Agents as fibre-bundle sections]] · [[Multi-agent variational free energy]] · [[Belief inertia]] · [[Mass as Fisher information]] · [[Hamiltonian belief dynamics]] · [[Ouroboros multi-scale dynamics]] · [[Meta-agents and hierarchical emergence]] · [[Renormalization-group flow of beliefs]] · [[Meta-entropy]] · [[Participatory realism (it from bit)]] · [[Gauge transformation]] · [[Parallel transport]] · [[Holonomy]] · [[Non-flat connection and the photon analogy]] · [[Natural gradient]] · [[Fisher information metric]] · [[Precision weighting]] · [[Variational free energy]]

**Manuscripts:** [[participatory-it-from-bit]] · [[participatory-it-from-bit-2026-07-11-code-concordance-review]] · [[belief-inertia]] · [[meta-entropy-manuscript]] · [[gl-k-attention]]

**Key sources:** [[parr-2022-active-inference]] · [[friston-2017-active-inference-process-theory|friston-2017-active-inference-process]] · [[caticha-2019-entropic-dynamics-qm|caticha-2019-entropic-dynamics]] · [[cencov-1982-statistical-decision-rules]] · [[amari-2016-information-geometry-applications]] · [[yang-mills-1954]] · [[nakahara-2003-geometry-topology-physics]] · [[wheeler-1990-it-from-bit]] · [[degroot-1974-consensus]] · [[friedkin1990-social-influence-opinions|friedkin-johnsen-1990]] · [[hegselmann-2002-opinion|hegselmann-krause-2002]] · [[wilson-1975-renormalization-group]]
