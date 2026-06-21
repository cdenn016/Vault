---
type: project
title: "SocialPhysics"
aliases:
  - "Social Physics"
  - "Social Physics Program"
  - "Sociophysics VFE"
  - "Belief Dynamics Program"
tags:
  - cluster/social-physics
  - cluster/vfe
  - cluster/multi-agent
  - project/social-physics
status: draft
created: 2026-06-19
updated: 2026-06-19
---

# SocialPhysics

## Goal

SocialPhysics studies how the collective dynamics of opinion, belief, and consensus emerge from a single physical principle: variational free energy minimization run over a population of agents whose beliefs live on statistical manifolds. The program's wager is that the classical models of sociophysics and opinion dynamics — averaging toward consensus, anchoring to an initial conviction, refusing to listen past a confidence threshold, hardening into echo chambers — are not independent phenomenological constructions but limiting cases of one information-geometric variational law with $GL(K)$ gauge-transported KL coupling $\mathrm{KL}(q_i \| \Omega_{ij}[q_j])$. Where it departs from the existing literature is in taking the geometry seriously enough to ask what happens at *second* order: reading the Fisher/precision tensor as an inertial mass gives belief a momentum, and momentum predicts behavior — oscillation, overshoot, resonance, and momentum transfer between agents — that the standard first-order (overdamped) models structurally cannot produce.

This is the social-science and dynamical-systems face of the author's broader gauge-theoretic VFE research program. Its founding manuscript is [[belief-inertia]] ("The Inertia of Belief", Robert C. Dennis), and the dynamics it proposes are implemented in the [[Gauge-Theoretic Multi-Agent VFE Model]] codebase, which carries the Hamiltonian integrator.

## Theoretical core

Each agent carries a Gaussian belief $q_i = \mathcal{N}(\mu_i, \Sigma_i)$ and is treated as a section of a fibre bundle, with comparison between agents performed by [[Parallel transport]] of one belief into another's gauge frame via $\Omega_{ij} = e^{\phi_i} e^{-\phi_j}$ (see [[Agents as fibre-bundle sections]], [[Gauge transformation]]). The population descends a [[Multi-agent variational free energy]] in which inter-agent disagreement is the gauge-transported divergence $\mathrm{KL}(q_i \| \Omega_{ij}[q_j])$, weighted by softmax attention coefficients $\beta_{ij}$. The geometry is not optional: by the Čencov–Chentsov theorem the [[Fisher information metric]] is the unique Riemannian metric (up to scaling) invariant under sufficient statistics, and it supplies a stiffness tensor — the curvature of the free-energy landscape — so that confident beliefs resist change while uncertain beliefs update readily. This [[Precision weighting]] is what makes belief inertia geometrically necessary rather than postulated.

The novel physics enters with the Hessian of the free energy, which decomposes into a four-term inertial mass
$$ M_i = \bar{\Lambda}_{p_i} + \Lambda_{o_i} + \sum_k \beta_{ik}\tilde{\Lambda}_{q_k} + \sum_j \beta_{ji}\Lambda_{q_i}, $$
combining prior precision, observation precision, incoming social precision, and a novel "recoil" outgoing-social term $\sum_j \beta_{ji}\Lambda_{q_i}$ by which influencing others costs an agent its own epistemic flexibility. See [[Mass as Fisher information]].

## The two regimes

The framework lives on a single dynamics toggle separating an overdamped and an underdamped regime, governed by the damped-oscillator equation of motion $M_i\ddot{\mu}_i + \gamma_i\dot{\mu}_i + \nabla_{\mu_i}\mathcal{F} = 0$, with the damping $\gamma$ identified as the inverse variational-inference learning rate and the regime fixed by the discriminant $\gamma^2 - 4KM$.

The **overdamped regime** is first-order gradient flow on the free energy — the standard Bayesian descent limit. Here the dynamics reduce to the [[Free-energy principle active inference]] / predictive-coding update, and this is where the classical opinion-dynamics models are recovered. These derivations depend only on gradient flow and are presented as geometrically necessary, not as resting on any additional assumption.

The **underdamped regime** is the novel contribution and rests on a [[Hamiltonian belief dynamics]] *ansatz*: reading the precision tensor as an inertial mass rather than only a stiffness. This is flagged explicitly in [[belief-inertia]] as an assumption beyond information geometry, since the curvature of a potential does not by itself fix a kinetic term. Granting the ansatz, belief acquires momentum and the model predicts attitude oscillation, overshoot past the equilibrium opinion, displacement resonance under periodic forcing, and momentum transfer between coupled agents — the phenomena absent from first-order dissipative treatments. See [[Belief inertia]].

## Classical models recovered as limiting cases

In the overdamped limit the same VFE functional reproduces the canonical sociophysics models. DeGroot social learning ([[degroot-1974-consensus]]) emerges as precision-weighted averaging toward consensus; Friedkin–Johnsen opinion dynamics ([[friedkin1990-social-influence-opinions|friedkin-johnsen-1990]], [[friedkin-johnsen-2011-social-influence-network]]) as the same flow with a persistent anchor to the initial conviction (the prior term); bounded-confidence dynamics ([[hegselmann-2002-opinion|hegselmann-krause-2002]], [[deffuant2000-bounded-confidence|deffuant-2000-bounded-confidence]]) as a soft finite-temperature analog of the hard confidence threshold, with the softmax attention $\beta_{ij}$ playing the role of the bounded-confidence kernel; echo-chamber formation and polarization ([[Echo chambers and polarization]]) as the self-reinforcing drift that the state-dependent self-coupling $\alpha_i^*(c) = c_0/(b_0 + \mathrm{KL}(q_i\|p_i))$ produces; Social Impact Theory ([[latane1981psychology|latane-1981-social-impact]]) as the precision-weighted aggregation of social forcing; and diffusion of innovations ([[rogers-2003-diffusion-of-innovations]]) as belief spreading through the coupling network. Consensus and polarization are thereby unified as two boundary conditions of one principle rather than two mechanisms. The broader sociophysics tradition this sits within is surveyed in [[castellano-2009-statistical-physics-social-dynamics|castellano-fortunato-loreto-2009-social-dynamics]], [[galam-2008-sociophysics]], and [[flache-2017-social-influence-models]]; confirmation bias ([[nickerson-1998-confirmation-bias]]) and belief perseverance ([[anderson1980-belief-perseverance|anderson-1980-belief-perseverance]]) are recast as geometric consequences of epistemic inertia rather than irrationality.

## Relation to the sibling projects

SocialPhysics shares its entire mathematical substrate — the [[Multi-agent variational free energy]] functional and the $GL(K)$ gauge core — with the [[Gauge-Theoretic Multi-Agent VFE Model]], which is where the dynamics actually run: the MAgent codebase carries the symplectic Hamiltonian integrator (`dynamics.dynamics = hamiltonian`) that realizes the underdamped regime, alongside the natural-gradient overdamped path. SocialPhysics is the social-physics reading of that machinery, picking out the opinion-dynamics interpretation and the falsifiable second-order predictions. It is a sibling to the [[VFE Transformer Program]], the language-model instantiation of the same theory; the three projects differ only in what the agents *are* (opinions, persistent bundle sections, tokens) and what the dynamics *mean*.

## Manuscripts

- [[belief-inertia]] — the founding and flagship manuscript: classical sociology models as overdamped limits of multi-agent VFE, the four-term Hessian mass, and the Hamiltonian belief-momentum extension.
- [[meta-entropy-manuscript]] — supplies the thermodynamic-limit bridge ([[Meta-entropy]], Kac-normalized extensivity) connecting the discrete population to a continuum.
- [[participatory-it-from-bit]] — the gauge substrate from which the state-dependent self-coupling weight and the $GL(K)$ transport are imported.
- [[gl-k-attention]] — the shared gauge-attention derivation linking opinion coupling to transformer attention.

## Concepts

[[Opinion dynamics]] · [[Bounded confidence]] · [[Sociophysics]] · [[Echo chambers and polarization]] · [[Belief perseverance and confirmation bias]] · [[Belief inertia]] · [[Mass as Fisher information]] · [[Hamiltonian belief dynamics]] · [[Multi-agent variational free energy]] · [[Fisher information metric]] · [[Variational free energy]] · [[Natural gradient]] · [[Precision weighting]] · [[Gauge transformation]] · [[Parallel transport]] · [[Holonomy]] · [[Agents as fibre-bundle sections]] · [[Renormalization-group flow of beliefs]] · [[Meta-agents and hierarchical emergence]] · [[Participatory realism (it from bit)]]

## Deep literature neighborhood

The broad statistical-physics-of-social-systems literature this program sits within is synthesized in the theme [[Statistical physics of social systems and collective behavior]], which frames each strand by its relation to the belief-inertia functional (recovered in the overdamped limit, extended by the underdamped momentum ansatz, or adjacent context). It is organized into these concept pages:

- **Opinion-dynamics models** — [[Opinion dynamics]] · [[Voter model]] · [[Discrete spin and majority-rule models of opinion]] · [[Axelrod model of cultural dissemination]] · [[Bounded confidence]]
- **Continuum & kinetic theory** — [[Kinetic theory of opinion dynamics]] · [[Sociodynamics and synergetics]] · [[Mean-field games and continuum limits]]
- **Networks & contagion** — [[Network structure — small-world and scale-free]] · [[Threshold models and complex contagion]] · [[Information cascades and herding]] · [[Schelling segregation and tipping points]]
- **Collective motion & synchronization** — [[Collective motion and flocking]] · [[Synchronization and the Kuramoto model]]
- **Behavioral & evolutionary foundations** — [[Social influence and conformity]] · [[Cultural evolution and social learning]] · [[Evolutionary game theory and cooperation]] · [[Replicator dynamics]]
- **Empirical polarization** — [[Echo chambers and polarization]]

This neighborhood was ingested as 122 source notes spanning the discrete opinion models (DeGroot, voter, Sznajd, Galam, Axelrod), kinetic/continuum theory (Toscani, Pareschi, Weidlich, Helbing, mean-field games), network science (Watts–Strogatz, Barabási–Albert, Granovetter), synchronization and flocking (Kuramoto, Vicsek, Cucker–Smale), the social psychology of influence (French, Asch, Festinger, Sherif), information cascades (Bikhchandani–Hirshleifer–Welch, Banerjee), evolutionary cooperation (Axelrod, Nowak), cultural evolution (Boyd–Richerson, Henrich), and empirical polarization (Del Vicario, Cinelli, Bail). The full catalog is in [[index|the index]]; the synchronization, Kuramoto, and Cucker–Smale strands are the closest physical precedents for the underdamped [[Hamiltonian belief dynamics]] regime, while the kinetic and mean-field-game limits are the natural continuum home for [[Meta-entropy]] and the thermodynamic-limit bridge.

## Key sources

**Classic opinion dynamics / sociophysics:** [[degroot-1974-consensus]] · [[friedkin1990-social-influence-opinions|friedkin-johnsen-1990]] · [[friedkin-johnsen-2011-social-influence-network]] · [[hegselmann-2002-opinion|hegselmann-krause-2002]] · [[deffuant2000-bounded-confidence|deffuant-2000-bounded-confidence]] · [[galam-2008-sociophysics]] · [[castellano-2009-statistical-physics-social-dynamics|castellano-fortunato-loreto-2009-social-dynamics]] · [[latane1981psychology|latane-1981-social-impact]] · [[rogers-2003-diffusion-of-innovations]] · [[flache-2017-social-influence-models]]

**Psychology of belief:** [[nickerson-1998-confirmation-bias]] · [[anderson1980-belief-perseverance|anderson-1980-belief-perseverance]] · [[kaplowitz-fink-1992-attitude-change]]

**Dynamics / statistical physics:** [[strogatz-2015-nonlinear-dynamics]] · [[sornette-2006-critical-phenomena]] · [[mezard-parisi-virasoro-1987-spin-glass]]

**Collective inference:** [[heins-2024-surprise-minimization]] · [[friston-2024-federated-inference]] · [[waade-2025-as-one-and-many]] · [[albarracin-2022-epistemic-communities]] · [[Collective active inference]]

**Geometry / inference substrate:** [[Free-energy principle active inference]] · [[Fisher information metric]] · [[Natural gradient]]

## Status & next steps

The overdamped results — recovery of DeGroot, Friedkin–Johnsen, bounded confidence, echo chambers, and Social Impact Theory — are the settled, geometrically necessary core. The underdamped Hamiltonian regime is the program's falsifiable, not-yet-validated frontier: it rests on the mass ansatz and makes sharp predictions that have yet to be tested empirically. The distinctive quantitative claims are the natural and resonance frequencies $\omega = \sqrt{K/M - \gamma^2/4M^2}$ and $\omega_{\text{res}} = \sqrt{K/M - \gamma^2/2M^2}$, the square-root overshoot law $d_{\text{overshoot}} = |\dot{\mu}|\sqrt{M/K}$ (which the manuscript notes has not yet even been simulated), and momentum transfer between coupled agents with a conserved current under reciprocal symmetric coupling. Symplectic integration in the manuscript confirms internal/integrator consistency (stopping-distance and decay-time scaling $\propto \Lambda$ at $R^2 = 1.000$, resonance frequency within $1.1\%$), but these establish self-consistency, not empirical truth.

Only one empirical comparison exists so far: a fit to the McGuire et al. (2014) helicopter task, which lands near critical damping ($\zeta = 0.91 \pm 0.12$) with the zero-momentum delta rule winning by BIC for 31 of 32 participants — consistent with the prediction that high-noise, volatile tasks sit near critical damping where the framework collapses back to first-order updating. The open frontier is therefore to find a low-noise, stable-environment paradigm where the underdamped predictions (oscillation, overshoot, resonance) would be visible and to test them directly. A second forward direction is the gauge-curvature extension: the vertex-cocycle transport $\Omega_{ij} = e^{\phi_i}e^{-\phi_j}$ is pure gauge with trivial [[Holonomy]], so nontrivial epistemic frustration (persistent disagreement under apparent consensus, spin-glass-like structure) requires the edge-local link variable $\Omega_{ij} = U_i e^{\delta_{ij}} U_j^{-1}$ flagged in [[belief-inertia]] as future work.

## Cross-links

**Sibling projects:** [[Gauge-Theoretic Multi-Agent VFE Model]] · [[VFE Transformer Program]]

**Manuscripts:** [[belief-inertia]] · [[meta-entropy-manuscript]] · [[participatory-it-from-bit]] · [[gl-k-attention]]

**Key concepts:** [[Belief inertia]] · [[Mass as Fisher information]] · [[Hamiltonian belief dynamics]] · [[Opinion dynamics]] · [[Bounded confidence]] · [[Sociophysics]] · [[Echo chambers and polarization]] · [[Belief perseverance and confirmation bias]] · [[Multi-agent variational free energy]] · [[Fisher information metric]]
