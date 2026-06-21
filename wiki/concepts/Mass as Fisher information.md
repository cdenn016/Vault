---
type: concept
title: "Mass as Fisher information"
aliases:
  - "Hessian mass"
  - "Epistemic mass"
  - "Inertial mass tensor"
  - "Mass-precision correspondence"
tags:
  - cluster/multi-agent
  - cluster/info-geometry
  - cluster/social-physics
  - project/multi-agent
  - project/social-physics
status: draft
created: 2026-06-18
updated: 2026-06-19
---

# Mass as Fisher information

## Definition

In the multi-agent (MAgent) model, the **inertial mass** of a belief is identified with a **total precision (Fisher-type) tensor**: the Hessian of the multi-agent variational free energy with respect to the belief parameters. For agent $i$ holding a Gaussian belief $q_i = \mathcal{N}(\mu_i, \Sigma_i)$ anchored to a prior $p_i$, the effective mass is

$$
M_i = \underbrace{\bar{\Lambda}_{p_i}}_{\text{prior}} + \underbrace{\Lambda_{o_i}}_{\text{observation}} + \underbrace{\sum_k \beta_{ik}\,\tilde{\Lambda}_{q_k}}_{\text{incoming social}} + \underbrace{\sum_j \beta_{ji}\,\Lambda_{q_i}}_{\text{outgoing social}}
$$

Each term is an inverse-covariance (precision) matrix, so the mass is a sum of precisions: prior precision $\bar{\Lambda}_{p_i} = \bar{\Sigma}_{p_i}^{-1}$, observation precision $\Lambda_{o_i} = R_i^{-1}$, the attention-weighted transported precisions of neighbours $\tilde{\Lambda}_{q_k} = (\Omega_{ik}\Sigma_{q_k}\Omega_{ik}^\top)^{-1}$, and the recoil precision an agent accumulates from being attended to. The slogan in the code is direct: "Mass = precision: rocks are certain (high $\Lambda$), thus massive, thus hard to move."

This page documents the [[Gauge-Theoretic Multi-Agent VFE Model]] construction. It is the author's own work; every formula below is grounded in [[belief-inertia]] (`belief_inertia.tex`) and the implementation in `gauge_agent/mass.py`.

## Why it matters here

A standard active-inference agent ([[parr-2022-active-inference]], [[friston-2017-active-inference-process-theory|friston-2017-active-inference-process]]) updates beliefs by pure gradient descent on [[Variational free energy]] — a first-order, dissipative flow with no momentum. The MAgent model instead reads the curvature of the free-energy landscape as an **inertial mass tensor**, equipping belief space with kinetic energy $T = \tfrac12 \dot{\mu}^\top M \dot{\mu}$ and a Hamiltonian dynamics ([[Hamiltonian belief dynamics]]). Mass-as-Fisher-information is the bridge that turns the gauge-theoretic VFE functional into a second-order theory and gives the model [[Belief inertia]].

This identification does the following load-bearing work in the model:

- **It makes precision the source of stubbornness.** A confident belief (large $\Lambda$) is heavy and resists change; an uncertain belief is light and updates readily. This recovers confirmation bias and belief perseverance as geometric consequences of inertia rather than as irrationality.
- **It makes inertia social.** The two social terms couple an agent's mass to the precision of its neighbours via the attention weights $\beta_{ij}$, so a cluster of mutually-attending confident agents becomes collectively rigid, and *exerting* influence (being attended to) also costs flexibility through the outgoing/recoil term.
- **It supplies the overdamped/underdamped split.** In the overdamped limit the dynamics reduce to ordinary Bayesian free-energy descent, recovering classical opinion-dynamics models ([[degroot-1974-consensus]], [[friedkin1990-social-influence-opinions|friedkin-johnsen-1990]], [[hegselmann-2002-opinion|hegselmann-krause-2002]]); the underdamped regime predicts oscillation, overshoot, and resonance.

## Details

### The Hessian construction

The complete multi-agent free energy decomposes into complexity, accuracy, and consensus terms,

$$
\mathcal{F} = \sum_i D_{\mathrm{KL}}(q_i \| p_i) \;-\; \sum_i \mathbb{E}_{q_i}[\log p(o_i\mid c_i)] \;+\; \sum_{i,k} \beta_{ik}\, D_{\mathrm{KL}}(q_i \| \Omega_{ik}\cdot q_k),
$$

where $\Omega_{ik} = e^{\phi_i}e^{-\phi_k}$ is a [[Gauge transformation]] that parallel-transports neighbour $k$'s belief into agent $i$'s reference frame ([[Agents as fibre-bundle sections]], [[Parallel transport]]), and $\beta_{ik}$ is the softmax [[Precision weighting]] attention. Writing the full state vector $\xi = (\mu_1,\dots,\mu_N,\Sigma_1,\dots,\Sigma_N)$, the mass matrix is the Hessian

$$
\mathbf{M} = \frac{\partial^2 \mathcal{F}}{\partial\xi\,\partial\xi^\top}.
$$

The four contributions to the mean-sector block follow by direct differentiation:

1. **Prior precision.** $\dfrac{\partial^2}{\partial\mu_i\partial\mu_i^\top} D_{\mathrm{KL}}(q_i\|p_i) = \bar{\Sigma}_{p_i}^{-1} \equiv \bar{\Lambda}_{p_i}$.
2. **Observation precision.** For $p(o_i\mid c_i)=\mathcal{N}(o_i\mid c_i, R_i)$, the accuracy term contributes $R_i^{-1} \equiv \Lambda_{o_i}$ — precise sensors anchor beliefs.
3. **Incoming social precision.** With attention frozen, $\dfrac{\partial^2}{\partial\mu_i\partial\mu_i^\top}\sum_k \beta_{ik} D_{\mathrm{KL}}(q_i\|\Omega_{ik}\cdot q_k) = \sum_k \beta_{ik}\,\tilde{\Lambda}_{q_k}$, the transported precision $\tilde{\Lambda}_{q_k} = \Omega_{ik}^{-\top}\Lambda_{q_k}\Omega_{ik}^{-1}$.
4. **Outgoing/recoil precision.** Agent $i$ also appears in its neighbours' consensus terms, contributing $\sum_j \beta_{ji}\,\Lambda_{q_i}$.

### Hessian mass vs. Fisher–Rao metric

The manuscript is careful that this **Hessian mass is not the intrinsic Fisher–Rao metric** $\mathcal{I}(\theta) = \mathrm{Cov}_q[(\nabla\log q)(\nabla\log q)^\top]$, which depends only on $q$ itself ([[Fisher information metric]]). The Hessian of $D_{\mathrm{KL}}(q\|p)$ in the parameters of $q$ yields the *reference* distribution's precision $\Lambda_p$, not the Fisher information of $q$; the two coincide only at the critical point $q = p$. Both nonetheless reduce to a precision matrix for Gaussians, which is why the "mass = total Fisher information" reading holds. Reading a physical inertia off the Fisher tensor places the construction in the lineage of [[Physics from Fisher information]], where Frieden's extreme-physical-information principle ([[frieden-1998-physics-fisher]]) and Reginatto's reconstruction of the Schrödinger equation from a Fisher-information term ([[reginatto-1998-fisher-quantum]]) derive dynamical laws from the same statistical-estimation quantity. The deeper justification for treating this precision tensor as the canonical geometric object is the Čencov–Chentsov uniqueness theorem ([[cencov-1982-statistical-decision-rules]]): the Fisher metric is, up to a positive scalar, the unique Riemannian metric on statistical manifolds invariant under sufficient statistics ([[ay-2017-information-geometry]], [[amari-2016-information-geometry-applications]]).

### The Hamiltonian as ansatz

> [!note] Editorial:
> The manuscript flags an important caveat that should not be elided. Information geometry supplies the *stiffness* (the curvature of the potential), but it does **not** by itself supply a kinetic term: "the curvature of a potential does not by itself determine a kinetic term." Reading the same precision tensor as an *inertial mass* is therefore a Hamiltonian **ansatz**, not a consequence of the Fisher geometry alone. The overdamped predictions are geometrically necessary; the underdamped (oscillatory) predictions depend on the ansatz and their empirical adequacy remains to be established.

### Consequences

Because mass is a sum of independent precisions, the model reads each term as a distinct psychological inertia: **prior inertia** (cost of leaving deep expectations), **sensory inertia** (high-fidelity observation anchors belief — so experts become *harder* to move, not easier), **incoming social inertia** (being pulled toward confident neighbours), and **outgoing/recoil inertia** (influence is "paid for in epistemic rigidity"). Multiplying mass by belief velocity gives the cognitive momentum $\pi_i = M_i \dot{\mu}_i$; for an isotropic isolated agent this collapses to $\pi_i = \sigma_i^{-2}\dot{\mu}_i = \Lambda_i \dot{\mu}_i$.

### Mean-field validity and adaptive precision

The mass is evaluated under **frozen (mean-field) attention**: $\beta_{ik}$ in fact depends on $\mu_i$ through the softmax, so the full Hessian carries extra terms that vanish exactly at consensus and are $O(1)$ off-equilibrium. The mass is therefore exact at consensus and an approximation otherwise. A state-dependent generalization promotes the prior weight to $\alpha_i^*(c) = c_0/(b_0 + D_{\mathrm{KL}}(q_i\|p_i))$ (a Gamma-MAP self-coupling), rescaling only the prior block:

$$
M_i = \alpha_i^*\,\bar{\Lambda}_{p_i} + \Lambda_{o_i} + \sum_k \beta_{ik}\tilde{\Lambda}_{q_k} + \sum_j \beta_{ji}\Lambda_{q_i}.
$$

Letting $\alpha_i^*$ co-move with the belief inside the second variation adds a *negative* rank-one correction $-\tfrac{(\alpha_i^*)^2}{c_0}(\bar{\Lambda}_{p_i}\Delta\mu_i)(\bar{\Lambda}_{p_i}\Delta\mu_i)^\top$ that can make the mass indefinite; the model adopts the detached, quasi-static convention to keep the kinetic energy bounded below.

## In this work

- **Manuscript.** [[belief-inertia]] develops the construction in full: the section "Mass as Fisher Information: The Complete Derivation" gives the four-term Hessian, the boxed mass formula $M_i = \bar{\Lambda}_{p_i} + \Lambda_{o_i} + \sum_k \beta_{ik}\tilde{\Lambda}_{q_k} + \sum_j \beta_{ji}\Lambda_{q_i}$, the Hessian-vs-Fisher-Rao distinction, the "Hamiltonian as ansatz" caveat, and the state-dependent self-coupling generalization. The mass feeds the Fisher arc-length clock, the kinetic energy $T = \tfrac12\dot{\mu}^\top M\dot{\mu}$, and the overshoot law $d_{\text{overshoot}} = |\dot{\mu}_i|\sqrt{M_i/K_i}$.
- **Code.** `gauge_agent/mass.py` implements the tensor. The `MassMatrix` module computes `effective_mass_diagonal` (the four-term Eq. 37 diagonal), `off_diagonal_mass` / `full_block` (the full $N\!\cdot\!K \times N\!\cdot\!K$ mean-sector block with the contravariant $\Omega^{-\top}\Lambda\,\Omega^{-1}$ transport), `full_block_gridded` (per-base-point mass), `kinetic_energy`, `scalar_mass` (= $\mathrm{tr}(M_i)$), and the covariance-sector mass $[M_{\Sigma\Sigma}]_{ii} = \tfrac12(\Lambda_{q_i}\!\otimes\!\Lambda_{q_i})\,f_i$ with $f_i = 1 + \sum_k\beta_{ik} + \sum_j\beta_{ji}$. Precisions and gauge frames are read with `.detach()` / `.omega.data` because the mass is a frozen preconditioner under the envelope convention. The opt-in `adaptive_precision` flag rescales only the prior block by $\alpha_i^*$. `InformationGeometricMass.mass_precision_correlation` validates the mass–precision correspondence (separating the honest *relational* statistic from the self-correlated total). `ouroboros_effective_mass` exposes a distinct timescale-separation inertia $M_{\text{eff}} = 2/(\varepsilon\eta^2\Lambda_m)$ for the [[Ouroboros multi-scale dynamics]] convention — kept independent from the Hessian/spring-constant object.
- **Related model concepts.** The mass is the backbone of [[Belief inertia]] and [[Hamiltonian belief dynamics]]; it is built from gauge transport of beliefs ([[Agents as fibre-bundle sections]]) and the softmax attention of [[Multi-agent variational free energy]]. The companion [[meta-entropy-manuscript]] manuscript and the [[gl-k-attention]] / [[participatory-it-from-bit]] line carry the same $\mathrm{GL}(K)$ gauge and precision-weighting machinery.

## Sources

- [[belief-inertia]] — *The Inertia of Belief*: the manuscript that derives the Hessian mass, the four-term precision formula, and the Hamiltonian belief dynamics.
- [[cencov-1982-statistical-decision-rules]] — Čencov/Chentsov uniqueness theorem grounding the Fisher metric as the canonical invariant structure.
- [[amari-2016-information-geometry-applications]], [[ay-2017-information-geometry]] — information-geometric foundations for the Fisher metric and precision tensors.
- [[parr-2022-active-inference]], [[friston-2017-active-inference-process-theory|friston-2017-active-inference-process]] — the single-agent VFE / active-inference substrate the model generalizes (and whose purely dissipative dynamics it extends to second order).
- [[degroot-1974-consensus]], [[friedkin1990-social-influence-opinions|friedkin-johnsen-1990]], [[hegselmann-2002-opinion|hegselmann-krause-2002]] — classical opinion-dynamics models recovered in the overdamped (massless-flow) limit.
- [[frieden-1998-physics-fisher]], [[reginatto-1998-fisher-quantum]] — deriving physical dynamics from Fisher information (extreme physical information; Schrödinger equation from a Fisher term), the broader programme that reading mass off the precision tensor belongs to.

## See also

- [[Belief inertia]]
- [[Hamiltonian belief dynamics]]
- [[Fisher information metric]]
- [[Physics from Fisher information]]
- [[Precision weighting]]
- [[Multi-agent variational free energy]]
- [[Agents as fibre-bundle sections]]
- [[Natural gradient]]
- [[Variational free energy]]
- [[Ouroboros multi-scale dynamics]]
- [[Gauge-Theoretic Multi-Agent VFE Model]]
