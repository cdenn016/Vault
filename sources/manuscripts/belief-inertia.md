---
type: manuscript
title: "The Inertia of Belief"
aliases:
  - The Inertia of Belief
authors:
  - Robert C. Dennis
year: 2025
status: in preparation
tags:
  - cluster/multi-agent
  - project/multi-agent
  - project/social-physics
created: 2026-06-18
updated: 2026-06-18
---

# The Inertia of Belief

> [!info] Manuscript
> Source file: `belief_inertia.tex` (Manuscripts-Theory).
> Status: **in preparation**. Single-author manuscript by Robert C. Dennis. Companion to the [[VFE Transformer Program]] and the [[Gauge-Theoretic Multi-Agent VFE Model]].

## Abstract

The manuscript presents a unified information-geometric framework from which several foundational sociological models emerge as limiting cases: DeGroot social learning, Friedkin–Johnsen opinion dynamics, bounded-confidence models, echo-chamber formation, and Social Impact Theory all arise from variational free energy minimization on statistical manifolds under appropriate parameter regimes. Consensus and polarization are presented not as separate phenomena but as manifestations of a single information-geometric principle under different boundary conditions, with bounded-confidence dynamics recovered as a soft finite-temperature analog rather than an exact hard-threshold limit.

The framework's deeper claim explains why phenomenological mass/spring models of belief dynamics have been empirically successful. The [[Fisher information metric]], which by the Čencov–Chentsov theorem is the unique Riemannian metric (up to positive scaling) on statistical manifolds invariant under sufficient statistics, naturally supplies a stiffness tensor — the curvature of the free-energy landscape — so that confident beliefs resist change while uncertain beliefs update readily. Reading this same precision tensor as an *inertial mass* (rather than only a stiffness) is explicitly flagged as a **Hamiltonian ansatz**, not a consequence of information geometry alone, since the curvature of a potential does not by itself fix a kinetic term. Under this ansatz, precision plays the role of epistemic inertia ([[Mass as Fisher information]]); the dynamics reduce to standard Bayesian free-energy descent in the overdamped limit while predicting oscillation, overshooting, and resonance in the underdamped regime. Confirmation bias and belief perseverance are reframed as geometric consequences of [[Belief inertia]] rather than irrationality.

## Core contributions

The introduction states three primary contributions:

1. **Second-order belief dynamics with a mass tensor.** The Hessian of the multi-agent variational free energy supplies a natural inertial mass
   $$ M_i = \bar{\Lambda}_{p_i} + \Lambda_{o_i} + \sum_k \beta_{ik}\tilde{\Lambda}_{q_k} + \sum_j \beta_{ji}\Lambda_{q_i}, $$
   combining prior precision, observation precision, and incoming/outgoing social precision. Multi-agent coupling takes the form $D_{\mathrm{KL}}(q_i \| \Omega_{ij}\cdot q_j)$, penalizing disagreement after gauge transport $\Omega_{ij}=e^{\phi_i}e^{-\phi_j}$ into a common reference frame ([[Multi-agent variational free energy]], [[Agents as fibre-bundle sections]]).
2. **Classical sociological models as limiting cases.** DeGroot, Friedkin–Johnsen, bounded confidence, echo chambers, and Social Impact Theory are all derived from the overdamped limit of the same VFE functional. These derivations depend only on gradient flow, *not* on the inertial ansatz.
3. **Unification of psychological phenomena.** Attitude oscillation in persuasion, perceptual aftereffects/adaptation overshoot, momentum in economic expectations, confirmation bias, and belief perseverance are recast as consequences of epistemic inertia in different parameter regimes, yielding testable predictions (precision-scaled relaxation times, resonance frequencies, stopping distances) absent from first-order dissipative treatments.

## Key results / theorems

- **Mass-as-Fisher-information derivation.** The free-energy Hessian decomposes into four precision contributions — prior, observation, incoming social, outgoing social — each derived term by term. The author carefully distinguishes this "Hessian mass" from the intrinsic Fisher–Rao metric (the two coincide only at $q=p$). The **outgoing social term** $\sum_j \beta_{ji}\Lambda_{q_i}$ is the novel "recoil" mass: influencing others costs epistemic flexibility.
- **State-dependent self-coupling.** Promoting the self-coupling weight to a per-agent variational precision $\alpha_i^*(c) = c_0/(b_0 + D_{\mathrm{KL}}(q_i\|p_i))$ (MAP under a Gamma prior) rescales the prior block of the mass; it predicts *weaker* prior anchoring where belief has drifted furthest (self-reinforcing drift). A regime-of-validity analysis gives the negative rank-one correction and the bound $D_{\mathrm{KL}}=b_0$ beyond which the inertial reading fails.
- **Hamiltonian / damped-oscillator dynamics.** Equation of motion $M_i\ddot{\mu}_i + \gamma_i\dot{\mu}_i + \nabla_{\mu_i}\mathcal{F}=0$, with $\gamma$ identified as the inverse VI learning rate. Three regimes (over/critically/under-damped) via the discriminant $\gamma^2-4KM$ ([[Hamiltonian belief dynamics]]).
- **Quantitative predictions.** Overshoot $d_{\text{overshoot}} = |\dot{\mu}|\sqrt{M/K}$ (square-root law); natural frequency $\omega=\sqrt{K/M-\gamma^2/4M^2}$; displacement-resonance peak $\omega_{\text{res}}=\sqrt{K/M-\gamma^2/2M^2}$; envelope decay $\tau_{\mathrm{env}}=2M/\gamma$; coasting relaxation $\tau_{\mathrm{relax}}=M/\gamma$.
- **Fisher arc-length "clock."** $d\ell=\sqrt{d\mu^\top\Sigma^{-1}d\mu}$ as an information-theoretic time, with high-precision agents accumulating arc-length faster (analogy to proper time, explicitly *not* a claim of Lorentzian structure).
- **Multi-agent momentum transfer.** Coupled equations of motion, a momentum current $J_{k\to i}$ with continuity equation, and conservation only under reciprocal symmetric coupling (broken by row-normalized softmax attention, priors, and damping).
- **Numerical verification (Table of self-consistency).** Symplectic integration reproduces closed-form predictions: stopping-distance scaling $d\propto\Lambda$ ($R^2=1.000$), decay-time scaling $\tau_{\mathrm{relax}}\propto\Lambda$ ($R^2=1.000$), underdamped frequency exact, resonance frequency $<1.1\%$. The author stresses these establish *integrator/internal consistency*, not empirical validation.
- **One empirical comparison (helicopter task).** Fitting to McGuire et al. (2014) data yields damping ratios near critical ($\zeta=0.91\pm0.12$); the delta rule (zero-momentum limit) wins by BIC for 31/32 participants, consistent with the prediction that high-noise/volatile tasks sit near critical damping where the framework reduces to first-order updating.
- **Gauge curvature / epistemic frustration (future-work program).** The vertex-cocycle transport $\Omega_{ij}=e^{\phi_i}e^{-\phi_j}$ is *pure gauge*: its [[Holonomy]] around any loop is identically $I$ by Maurer–Cartan. Nontrivial holonomy ("intransitive understanding," spin-glass-like frustration energy, persistent disagreement under apparent consensus) requires an edge-local link variable $\Omega_{ij}=U_i e^{\delta_{ij}}U_j^{-1}$; these predictions are flagged as belonging to that extension, not the flat model studied here.

> [!note] Editorial: The author is unusually explicit about epistemic status — the overdamped/gradient-flow results (classical-model limits, $d\propto\Lambda$) are presented as geometrically necessary, while the underdamped/Hamiltonian results (oscillation, resonance, $\sqrt{M/K}$ overshoot) are flagged as resting on the ansatz and as not yet empirically validated. The $\sqrt{M/K}$ overshoot law is explicitly noted as *not* yet simulated.

## Relevance to the program

This manuscript is the dynamical / multi-agent pillar of the gauge-theoretic VFE program. It builds directly on the same [[Multi-agent variational free energy]] functional and gauge structure used in the [[Gauge-Theoretic Multi-Agent VFE Model]], and it reuses the $\mathrm{GL}(d)$/[[Gauge transformation]] transport, softmax attention as VFE minimizer, and [[Agents as fibre-bundle sections]] picture from the companion attention work [[gl-k-attention]]. Specific concept links:

- [[Belief inertia]] — the central object: precision-as-inertia.
- [[Mass as Fisher information]] — the four-term Hessian mass derivation.
- [[Hamiltonian belief dynamics]] — the second-order equation of motion and oscillator regimes.
- [[Fisher information metric]] / [[Precision weighting]] / [[Variational free energy]] — the geometric and inferential substrate.
- [[Holonomy]] / [[Parallel transport]] / [[Gauge transformation]] — the social-frame transport and the pure-gauge/edge-local distinction.
- [[Renormalization-group flow of beliefs]] / [[Meta-agents and hierarchical emergence]] — flagged in "Hierarchical Extensions" as forthcoming coarse-graining into informational meta-agents (links to [[meta-entropy-manuscript]]).
- [[Participatory realism (it from bit)]] / [[participatory-it-from-bit]] — the state-dependent self-coupling weight is imported from that companion framework.
- Methods: [[Free-energy principle active inference]], [[Predictive coding network]] (the overdamped limit recovers their first-order dynamics); [[Gauge equivariant CNN]] cited as motivation for retaining gauge structure.
- Projects: [[VFE Transformer Program]], [[Gauge-Theoretic Multi-Agent VFE Model]].

## References cited

Resolved from `references.bib` in the same folder. Keys present in the program registry are wikilinked to their source notes.

- [[friston-2010-free-energy-principle|Friston (2010), The free-energy principle: a unified brain theory?]]
- Clark (2013), Whatever next? Predictive brains, situated agents, and the future of cognitive science
- Jaynes (2003), Probability Theory: The Logic of Science
- Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo (2016), Active inference and learning
- Hohwy (2013), The Predictive Mind
- [[millidge-2020-pc-approximates-backprop|Millidge, Seth & Buckley (2021), Predictive coding: a theoretical and experimental review]]
- [[amari-2016-information-geometry-applications|Amari (2016), Information Geometry and Its Applications]]
- Friston (2008), Hierarchical models in the brain
- [[bogacz-2017-free-energy-tutorial|Bogacz (2017), A tutorial on the free-energy framework for modelling perception and learning]]
- Castellano, Fortunato & Loreto (2009), Statistical physics of social dynamics
- [[galam-2008-sociophysics|Galam (2012), Sociophysics: A Physicist's Modeling of Psycho-political Phenomena]]
- [[hegselmann-krause-2002|Hegselmann & Krause (2002), Opinion dynamics and bounded confidence: models, analysis and simulation]] (cited as both `hegselmann2002opinion` and `hegselmann2002`)
- Busemeyer & Bruza (2012), Quantum Models of Cognition and Decision
- Kahneman (2011), Thinking, Fast and Slow
- Nielsen (2020), Elementary Differential Geometry
- [[degroot-1974-consensus|DeGroot (1974), Reaching a consensus]]
- [[friedkin-johnsen-1990|Friedkin & Johnsen (1990), Social influence and opinions]]
- [[deffuant-2000-bounded-confidence|Deffuant, Neau, Amblard & Weisbuch (2000), Mixing beliefs among interacting agents]]
- Kaplowitz & Fink (1992), Dynamics of attitude change
- Fink, Kaplowitz & Hubbard (2002), Oscillation in beliefs and decisions
- Webster (2015), Visual adaptation
- Coibion & Gorodnichenko (2015), Information rigidity and the expectations formation process
- Nickerson (1998), Confirmation bias: a ubiquitous phenomenon in many guises (keys `nickerson1998confirmation` and `nickerson1998`)
- Anderson, Lepper & Ross (1980), Perseverance of social theories (keys `anderson1980perseverance` and `anderson1980`)
- [[parr-2022-active-inference|Parr, Pezzulo & Friston (2022), Active Inference: The Free Energy Principle in Mind, Brain, and Behavior]]
- Arnold (1989), Mathematical Methods of Classical Mechanics
- Holmes (2012), Introduction to Perturbation Methods
- Olver (1993), Applications of Lie Groups to Differential Equations
- [[wilson-1975-renormalization-group|Wilson & Kogut (1975), The renormalization group and the ε expansion]]
- Goldenfeld (1992), Lectures on Phase Transitions and the Renormalization Group
- Strogatz (2015), Nonlinear Dynamics and Chaos
- Sornette (2006), Critical Phenomena in Natural Sciences
- [[gl-k-attention|Dennis (2025), Implementing Attention and Transformers without Neural Networks: Validation of Gauge-Theoretic Transformers]] (`Dennis2025trans`)
- Adams (1918), The Education of Henry Adams
- [[cencov-1982-statistical-decision-rules|Čencov (1982), Statistical Decision Rules and Optimal Inference]]
- [[participatory-it-from-bit|Dennis (2025), A Theoretical and Computational Implementation of a Participatory "It From Bit" Universe]] (`Dennis2025it`)
- Eagly & Chaiken (1993), The Psychology of Attitudes
- Lewandowsky, Ecker, Seifert, Schwarz & Cook (2012), Misinformation and its correction: continued influence and successful debiasing
- McGuire, Nassar, Gold & Kable (2014), Functionally dissociable influences on learning rate in a dynamic environment
- Kaplowitz, Fink & Bauer (1983), A dynamic model of the effect of discrepant information on unidimensional attitude change
- Friedkin & Johnsen (2011), Social Influence Network Theory
- Flache, Mäs, Feliciani, Chattoe-Brown, Deffuant, Huet & Lorenz (2017), Models of social influence: towards the next frontiers
- Ross, Lepper & Hubbard (1975), Perseverance in self-perception and social perception
- Bishop (2006), Pattern Recognition and Machine Learning
- Solzhenitsyn (1973), The Gulag Archipelago

> [!note] Editorial: The following keys are cited in `belief_inertia.tex` but were **not found** in `references.bib`, so author/year/title could not be resolved: `latane1981psychology` (Social Impact Theory), `cohen2019gauge` (gauge-equivariant CNNs), `he2025cask` (gauge-covariant transformers), `rogers2003diffusion`, `diakonikolas2021momentum`, `daSilva2023confirmation`, `mezard1987spin`. These should be added to the bibliography.
