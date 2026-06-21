---
type: concept
title: Belief inertia
aliases:
  - Epistemic inertia
  - Cognitive momentum
  - Epistemic momentum
  - Belief momentum
tags:
  - cluster/multi-agent
  - cluster/vfe
  - cluster/info-geometry
  - cluster/social-physics
  - project/multi-agent
  - project/social-physics
status: draft
created: 2026-06-18
updated: 2026-06-19
---

# Belief inertia

## Definition

**Belief inertia** is the proposal that a belief, modeled as a point on a statistical manifold, possesses an *inertial mass* proportional to the agent's total precision, so that confident beliefs resist change and, once in motion, tend to continue along their trajectory. The mechanism augments the standard first-order (dissipative) picture of belief updating with a second-order **Hamiltonian** term: instead of pure gradient descent on [[Variational free energy]], beliefs obey an equation of motion of damped-oscillator form

$$
M_i\,\ddot{\mu}_i + \gamma_i\,\dot{\mu}_i + \nabla_{\mu_i}\mathcal{F} = 0,
$$

where $\mu_i$ is agent $i$'s mean belief, $\mathcal{F}$ is the multi-agent free energy, $\gamma_i>0$ is a damping coefficient, and $M_i$ is the **epistemic mass** tensor. The mass is identified with the Hessian of the free energy (a total precision matrix); see [[Mass as Fisher information]]. The associated **cognitive momentum** is $\pi_i = M_i\,\dot{\mu}_i$.

The construction is grounded in the manuscript [[belief-inertia]] ("The Inertia of Belief"), by R. C. Dennis.

> [!note] Editorial: The manuscript is explicit that the second-order Hamiltonian reading is an *ansatz*, not a consequence of information geometry alone. The Fisher metric supplies curvature (a potential), but "the curvature of a potential does not by itself determine a kinetic term." Overdamped predictions are geometrically necessary; underdamped (inertial, oscillatory) predictions depend on the ansatz.

## Why it matters here

Belief inertia is the dynamical heart of the [[Gauge-Theoretic Multi-Agent VFE Model]]'s sociological face. The same gauge-theoretic, multi-agent free energy that yields attention in the transformer setting ([[Multi-agent variational free energy]], [[gl-k-attention]]) becomes, when read as a *potential* for second-order dynamics, a theory of how opinions move, oscillate, and transfer between agents. It supplies three things distinctive to the model:

- **A unification of opinion-dynamics models.** In the overdamped limit ($\gamma\to\infty$) the dynamics reduce to preconditioned gradient flow $\dot\mu = -M^{-1}\nabla\mathcal F$, from which DeGroot social learning ([[degroot-1974-consensus]]), Friedkin–Johnsen opinion dynamics ([[friedkin1990-social-influence-opinions|friedkin-johnsen-1990]]), and bounded-confidence models ([[hegselmann-2002-opinion|hegselmann-krause-2002]], [[deffuant2000-bounded-confidence|deffuant-2000-bounded-confidence]]) emerge as limiting cases. Consensus and polarization become two regimes of one functional rather than separate theories.
- **A mechanism for social rigidity.** Because mass is *collective* (it inherits neighbors' precision through attention), the model explains why expertise clusters resist perturbation and why wielding influence costs flexibility — connecting to [[Agents as fibre-bundle sections]] and the gauge-transport coupling $D_{\mathrm{KL}}(q_i\|\Omega_{ij}\cdot q_j)$.
- **Novel, testable dynamics absent from first-order active inference** ([[parr-2022-active-inference]], [[friston-2017-active-inference-process-theory|friston-2017-active-inference-process]]): overshoot, oscillation, resonance, perseverance, and momentum transfer — see [[Hamiltonian belief dynamics]].

## Details

### Epistemic mass as total precision

Writing the multi-agent free energy as complexity + (negative) accuracy + consensus,

$$
\mathcal{F} = \sum_i D_{\mathrm{KL}}(q_i\|p_i) - \sum_i \mathbb{E}_{q_i}[\log p(o_i|c_i)] + \sum_{i,k}\beta_{ik}\,D_{\mathrm{KL}}(q_i\|\Omega_{ik}\cdot q_k),
$$

the mass is defined as the Hessian $\mathbf{M} = \partial^2\mathcal{F}/\partial\xi\,\partial\xi^\top$ with respect to the belief parameters. For Gaussian beliefs this decomposes into four interpretable precision contributions:

$$
M_i = \underbrace{\bar{\Lambda}_{p_i}}_{\text{prior}} + \underbrace{\Lambda_{o_i}}_{\text{observation}} + \underbrace{\sum_k \beta_{ik}\,\tilde{\Lambda}_{q_k}}_{\text{incoming social}} + \underbrace{\sum_j \beta_{ji}\,\Lambda_{q_i}}_{\text{outgoing social}},
$$

where $\bar{\Lambda}_{p_i}=\bar\Sigma_{p_i}^{-1}$ is the prior precision, $\Lambda_{o_i}=R_i^{-1}$ the observation (inverse sensory-noise) precision, $\tilde{\Lambda}_{q_k}=(\Omega_{ik}\Sigma_{q_k}\Omega_{ik}^\top)^{-1}$ a neighbor's precision transported into agent $i$'s frame ([[Parallel transport]], [[Gauge transformation]]), and the *outgoing* term the reciprocal recoil from being attended to. The four parts read as prior inertia, sensory anchoring, incoming social pull, and outgoing recoil. The identification of mass with precision rests on the uniqueness of the [[Fisher information metric]] under sufficient statistics ([[cencov-1982-statistical-decision-rules]]).

> [!note] Editorial: The manuscript carefully distinguishes this "Hessian mass" from the intrinsic Fisher–Rao metric $\mathcal{I}(\theta)$; the two coincide only at the critical point $q=p$. Both reduce to the precision matrix for Gaussians.

### The Fisher arc-length clock and kinetic energy

Time is defined intrinsically as Fisher arc length, $d\ell = \sqrt{d\mu^\top\Sigma^{-1}d\mu}$, so high-precision agents accumulate "cognitive time" faster for the same parametric motion. This metric motivates the kinetic energy $T=\tfrac12\dot\mu^\top M\dot\mu$ that completes the Hamiltonian. To second order, $\mathrm{KL}(q\|q+dq)\approx\tfrac12 d\ell^2$, so the clock measures accumulated information change.

### Damping and the three regimes

The damping $\gamma$ is *not* a new free parameter: in the overdamped limit it is the inverse learning rate of standard variational inference ($\dot\mu = -\gamma^{-1}\nabla\mathcal F$). Linearizing about equilibrium, $M_i\ddot{\delta\mu}+\gamma_i\dot{\delta\mu}+K_i\,\delta\mu=0$, where the **stiffness** $K_i$ is the *evidence* curvature, a different object from the mass $M_i$. The discriminant $\Delta=\gamma_i^2-4K_iM_i$ sorts behavior into overdamped (monotone decay), critically damped (fastest non-oscillatory approach), and underdamped (oscillation/overshoot). Key closed forms:

- Natural frequency: $\omega=\sqrt{K_i/M_i-\gamma_i^2/4M_i^2}$.
- Overshoot distance: $d_{\text{overshoot}}=|\dot\mu_i|\sqrt{M_i/K_i}$, predicting overshoot $\propto\sqrt{\text{precision}}$.
- Displacement resonance peak: $\omega_{\text{res}}=\sqrt{K_i/M_i-\gamma_i^2/2M_i^2}$, with high-mass agents showing *larger* resonant swings ($A_{\max}=(f_0/\gamma_i)\sqrt{M_i/K_i}$).
- Perseverance: underdamped envelope decay $\tau_{\mathrm{env}}=2M_i/\gamma_i$; coasting (continued-influence) time $\tau_{\mathrm{relax}}=M_i/\gamma_i$. Both scale linearly with precision.

### Momentum transfer between agents

Through the attention coupling $\beta_{ij}$, momentum flows between agents. The current from $k$ to $i$ is $J_{k\to i}=\beta_{ik}\tilde{\Lambda}_{q_k}(\tilde\mu_k-\mu_i)$, satisfying a continuity equation. Under symmetric, reciprocal coupling ($\beta_{ik}=\beta_{ki}$, $\Omega_{ik}\Omega_{ki}=I$) with no priors or damping, total momentum is conserved; row-normalized (asymmetric) attention or priors/damping break conservation, dissipating momentum into the prior "environment." This makes influence intrinsically reciprocal: changing another's mind perturbs one's own trajectory.

### Adaptive (state-dependent) self-coupling

When the prior self-coupling weight is promoted to a per-agent variational precision $\alpha_i$ with a Gamma-type regularizer, the stationary value $\alpha_i^*(c)=c_0/(b_0+D_{\mathrm{KL}}(q_i\|p_i))$ rescales only the prior block of the mass, $M_i=\alpha_i^*\bar\Lambda_{p_i}+\dots$. Because $\alpha_i^*$ *decreases* as the belief drifts from its prior, prior anchoring weakens exactly where the belief is most displaced — a self-reinforcing drift rather than added stubbornness.

## In this work

- **Manuscript [[belief-inertia]]** ("The Inertia of Belief") develops the entire construction: the four-part mass formula, the Fisher arc-length clock, the damped-oscillator dynamics, the classical opinion-dynamics limits, and the numerical/empirical validation (symplectic integration reproducing closed-form predictions to $<1\%$; a single empirical comparison on the helicopter task that lands near critical damping, where the framework reduces to a delta rule).
- Tightly coupled wiki concepts: [[Mass as Fisher information]] (the precision-as-mass identification), [[Hamiltonian belief dynamics]] (the full phase-space formulation and predictions), and [[Precision weighting]] (the precision quantities reused as inertia).
- The same multi-agent free energy and gauge-transport coupling appear in the transformer-side manuscripts [[gl-k-attention]] and [[participatory-it-from-bit]], where softmax attention is recovered as a gauge-fixed isotropic-Gaussian limit; belief inertia is the second-order reading of that shared potential. The thermodynamic-limit counting of belief configurations is developed under [[meta-entropy-manuscript]].

## Sources

- [[belief-inertia]] — The Inertia of Belief (primary manuscript; all definitions, the mass formula, dynamics, and validation are taken from this file).
- [[cencov-1982-statistical-decision-rules]] — Čencov/Chentsov uniqueness theorem underwriting precision-as-Fisher-information.
- [[amari-2016-information-geometry-applications]], [[ay-2017-information-geometry]] — information geometry of the statistical manifold.
- [[parr-2022-active-inference]], [[friston-2017-active-inference-process-theory|friston-2017-active-inference-process]] — first-order active-inference substrate that the second-order dynamics extend.
- [[degroot-1974-consensus]], [[friedkin1990-social-influence-opinions|friedkin-johnsen-1990]], [[hegselmann-2002-opinion|hegselmann-krause-2002]], [[deffuant2000-bounded-confidence|deffuant-2000-bounded-confidence]] — classical opinion-dynamics models recovered as overdamped limits.

## See also

- [[Mass as Fisher information]]
- [[Hamiltonian belief dynamics]]
- [[Multi-agent variational free energy]]
- [[Agents as fibre-bundle sections]]
- [[Variational free energy]]
- [[Fisher information metric]]
- [[Natural gradient]]
- [[Precision weighting]]
- [[Parallel transport]]
- [[Gauge transformation]]
- [[Gauge-Theoretic Multi-Agent VFE Model]]
