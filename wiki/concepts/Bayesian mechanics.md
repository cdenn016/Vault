---
type: concept
title: "Bayesian mechanics"
aliases:
  - "Physics of beliefs"
  - "Physics of and by beliefs"
  - "Bayesian mechanics of stationary processes"
tags:
  - cluster/vfe
  - cluster/participatory
  - project/multi-agent
  - project/transformer
status: draft
created: 2026-06-19
updated: 2026-06-19
---

# Bayesian mechanics

## Definition

**Bayesian mechanics** is the program — consolidated under that name in [[ramstead-2023-bayesian-mechanics|Ramstead et al. 2023]] and given its technical core in [[dacosta-2021-bayesian-mechanics|Da Costa et al. 2021]] — that treats certain physical systems as *literally doing inference*. A system whose state space partitions into internal $\mu$, external $\eta$, and blanket (sensory + active) states with the conditional independence $\mu \perp\!\!\!\perp \eta \mid b$ of a [[Markov blanket interpretation debate|Markov blanket]] is shown, at non-equilibrium steady state, to have internal states that *parametrize a probability density over external states*. A synchronization (or "bold") map $\sigma: \mu \mapsto \eta(\mu)$ sends the most likely internal state to a posterior over external causes, so the internal dynamics can be read as minimizing [[Variational free energy]]. Ramstead et al. capture the dual claim in their subtitle, "a physics *of and by* beliefs": physics *of* beliefs because internal dynamics are lawful, physics *by* beliefs because those same dynamics realise approximate Bayesian inference. The construction is geometric: starting from the stationary Fokker–Planck density and its Helmholtz decomposition into dissipative (gradient) and solenoidal (divergence-free) parts, free-energy descent becomes a Riemannian gradient flow tied to the [[Fisher information metric]] and [[Natural gradient]] descent. The field thus organises around three pillars — *partition* (Markov blanket), *map* (synchronization), and *flow* (free-energy gradient on a statistical manifold).

## Why it matters here

Bayesian mechanics is the precise single-agent substrate that the [[Gauge-Theoretic Multi-Agent VFE Model]] generalises. The central PIFB move — that an observer's internal state parametrizes a density over the external world, so what looks like physics is the geometry of inference — *is* the Bayesian-mechanics claim, lifted into a gauge-covariant, multi-agent setting. Where Da Costa et al. fix one Markov blanket and one synchronization map under a single global frame, the manuscript [[participatory-it-from-bit]] stacks many blankets across scales via [[Multi-agent variational free energy]] and [[Ouroboros multi-scale dynamics]], and replaces the single frame with frame-covariant [[Parallel transport]] under a [[Gauge transformation]]. The Helmholtz/solenoidal component, which gives Bayesian mechanics its oscillatory, Hamiltonian-like character rather than pure relaxation, is the steady-state ancestor of the project's [[Hamiltonian belief dynamics]] and [[Belief inertia]]. The "it from bit" pullback construction is exactly this inference-as-geometry stance pushed to the point where a metric on the base manifold is induced from belief fields. Reading Bayesian mechanics as the non-gauge lineage of FEP-as-physics also positions [[sengupta-2016-neuronal-gauge-theory|Sengupta et al. 2016]] and [[sengupta-friston-2017-bayesian-gauge-theory|Sengupta & Friston 2017]] as the *gauge*-axis precursor running alongside it: those two argue that variational inference itself is a gauge theory, and PIFB supplies which group, which connection, and a working gauge-equivariant minimizer.

## Details

The lineage runs from [[friston-2019-particular-physics|Friston 2019]] ("a free energy principle for a particular physics") through [[parr-2020-markov-blankets-thermodynamics|Parr et al. 2020]], which grounds the partition thermodynamically, to the Da Costa stationary-process formalism and the Ramstead review. [[friston-2023-fep-simpler]] restates the principle in its leanest form. [[sakthivadivel-2022-geometry-bayesian-mechanics]] supplies the explicit information geometry of the synchronization map and steady-state flow, and [[friston-2008-dem]] (DEM) is the earlier generalized-coordinates inference engine on which the dynamical reading rests. Two formulations coexist: *mode-tracking* (steady-state, most-likely internal state) versus *path-tracking* (path-integral over trajectories), each carrying its own assumptions — non-equilibrium steady state, conditional independence, ergodicity. Those assumptions are precisely what the [[Markov blanket interpretation debate]] (Bruineberg, Aguilera, Biehl) contests, distinguishing literal from merely instrumental blankets; PIFB must engage that debate when it claims its agents *are* inferential particles rather than convenient descriptions.

The "physics-by-beliefs" half of the claim only has teeth if the underlying inference is itself well-founded, and Bayesian mechanics inherits this from variational Bayes. The free energy the internal states descend is the same negative evidence lower bound (ELBO) that grounds modern variational inference ([[blei-2017-variational-inference]]), and the synchronization-map reading — internal states *parametrize* a variational density $q_\mu(\eta)$ — is the amortized / structured-posterior idea that hierarchical latent-variable models exploit, e.g. the ladder VAE's top-down precision-weighted refinement ([[sonderby-2016-ladder-vae]]). The factorised, locally-coupled form a blanketed system imposes on its beliefs is also exactly the product-of-experts trick, where a joint density is built by multiplying many simple expert distributions ([[hinton-2002-poe]]) — a useful lens on how nested blankets compose beliefs across scales. A coherence guarantee comes from generalized Bayes ([[bissiri-holmes-walker-2016-general-bayes]]): minimising expected loss plus a KL-to-prior penalty is the *unique* rational belief update, so the free-energy E-step is legitimate inference rather than ad hoc energy descent, with precision playing the role of a learning-rate / temperature (a *tempered* free energy). This decision-theoretic footing matters when the inference is not a textbook likelihood update — which is generically the case for blanketed steady-state systems.

## Sources

- [[dacosta-2021-bayesian-mechanics]] — technical core: synchronization map, Helmholtz decomposition, geometric free-energy descent for stationary processes.
- [[ramstead-2023-bayesian-mechanics]] — definitive review; partition/map/flow schema and the "physics of and by beliefs" phrasing.
- [[friston-2019-particular-physics]] — the founding "free energy principle for a particular physics" statement.
- [[parr-2020-markov-blankets-thermodynamics]] — thermodynamic grounding of the Markov-blanket partition.
- [[friston-2023-fep-simpler]] — leanest restatement of the principle.
- [[sakthivadivel-2022-geometry-bayesian-mechanics]] — information geometry of the synchronization map and steady-state flow.
- [[sengupta-2016-neuronal-gauge-theory]] — named gauge-axis precursor: free-energy minimization as gauge-covariant dynamics.
- [[sengupta-friston-2017-bayesian-gauge-theory]] — technical follow-up: approximate Bayesian inference as a gauge theory.
- [[friston-2008-dem]] — DEM, the generalized-coordinates inference engine underlying the dynamical reading.
- [[blei-2017-variational-inference]] — the ELBO / variational-Bayes machinery the free-energy descent instantiates.
- [[sonderby-2016-ladder-vae]] — hierarchical, precision-weighted variational posterior; the synchronization-map idea in deep-learning form.
- [[hinton-2002-poe]] — product-of-experts factorisation, a lens on how nested-blanket beliefs compose.
- [[bissiri-holmes-walker-2016-general-bayes]] — generalized (Gibbs) Bayes: the free-energy E-step as the unique coherent, tempered belief update.
- [[participatory-it-from-bit]] — the manuscript that gauges and stacks this substrate.

## See also

- [[Free-energy principle active inference]]
- [[Markov blanket interpretation debate]]
- [[Participatory realism (it from bit)]]
- [[Fisher information metric]]
- [[Multi-agent variational free energy]]
- [[Variational free energy]]
- [[Natural gradient]]
- [[Hamiltonian belief dynamics]]
- [[Belief inertia]]
- [[Ouroboros multi-scale dynamics]]
