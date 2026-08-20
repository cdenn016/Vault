---
type: concept
title: "Bayesian mechanics"
aliases:
  - "Physics of beliefs"
  - "Physics of and by beliefs"
  - "Bayesian mechanics of stationary processes"
  - "Multi-agent Bayesian mechanics"
tags:
  - cluster/vfe
  - cluster/participatory
  - project/multi-agent
  - project/transformer
status: draft
created: 2026-06-19
updated: 2026-08-20
---

# Bayesian mechanics

## Definition

**Bayesian mechanics** is the program — consolidated under that name in [[ramstead-2023-bayesian-mechanics|Ramstead et al. 2023]] and given its technical core in [[dacosta-2021-bayesian-mechanics|Da Costa et al. 2021]] — that treats certain physical systems as *literally doing inference*. A system whose state space partitions into internal $\mu$, external $\eta$, and blanket (sensory + active) states with the conditional independence $\mu \perp\!\!\!\perp \eta \mid b$ of a [[Markov blanket interpretation debate|Markov blanket]] is shown, at non-equilibrium steady state, to have internal states that *parametrize a probability density over external states*. A synchronization (or "bold") map $\sigma: \mu \mapsto \eta(\mu)$ sends the most likely internal state to a posterior over external causes, so the internal dynamics can be read as minimizing [[Variational free energy]]. Ramstead et al. capture the dual claim in their subtitle, "a physics *of and by* beliefs": physics *of* beliefs because internal dynamics are lawful, physics *by* beliefs because those same dynamics realise approximate Bayesian inference. The construction is geometric: starting from the stationary Fokker–Planck density and its Helmholtz decomposition into dissipative (gradient) and solenoidal (divergence-free) parts, free-energy descent becomes a Riemannian gradient flow tied to the [[Fisher information metric]] and [[Natural gradient]] descent. The field thus organises around three pillars — *partition* (Markov blanket), *map* (synchronization), and *flow* (free-energy gradient on a statistical manifold).

## Why it matters here

Bayesian mechanics is a principal single-system precursor to the [[Gauge-Theoretic Multi-Agent VFE Model]], not yet a theorem that the latter formally generalizes. The shared move is that internal states parametrize probability laws over external or latent states, so information geometry can describe inferential motion. Gauge-VFE adds agent-indexed statistical fibers, explicit inter-agent transport, correlated population recognition, and declared multiscale coarse channels.

The additional Bayesian-mechanics obligations are not inherited from those objects. Da Costa et al. construct one particular-state partition, one Markov blanket, a synchronization map, and a stationary stochastic flow. The current Gauge-VFE theory does not derive individual or group blankets, nonequilibrium steady state, ergodicity, compatible individual and group synchronization maps, or physical time. Its relation to Bayesian mechanics is therefore a proposed gauge-covariant multi-agent extension program rather than a completed multi-agent Bayesian mechanics.

The Helmholtz or solenoidal sector remains a dynamical precursor to the project's [[Hamiltonian belief dynamics]] and [[Belief inertia]], not a consequence of fixed-joint ELBO algebra. The [[participatory-it-from-bit]] pullback construction pursues the inference-as-geometry stance by inducing base-manifold tensors from belief fields. [[sengupta-2016-neuronal-gauge|Sengupta et al. 2016]] and [[sengupta2017gauge|Sengupta & Friston 2017]] supply the gauge-axis precursor; PIFB makes the group, connection, and transport more explicit while retaining the missing stochastic-mechanics bridge as open.

## Details

The lineage runs from [[friston-2019-particular-physics|Friston 2019]] ("a free energy principle for a particular physics") through [[parr-2020-markov-blankets-thermodynamics|Parr et al. 2020]], which grounds the partition thermodynamically, to the Da Costa stationary-process formalism and the Ramstead review. [[friston-2023-fep-simpler]] restates the principle in its leanest form. [[sakthivadivel2022-bayesian-mechanics-geometry|sakthivadivel-2022-geometry-bayesian-mechanics]] supplies the explicit information geometry of the synchronization map and steady-state flow, and [[friston-2008-dem]] (DEM) is the earlier generalized-coordinates inference engine on which the dynamical reading rests. Two formulations coexist: *mode-tracking* (steady-state, most-likely internal state) versus *path-tracking* (path-integral over trajectories), each carrying its own assumptions — non-equilibrium steady state, conditional independence, ergodicity. Those assumptions are precisely what the [[Markov blanket interpretation debate]] (Bruineberg, Aguilera, Biehl) contests, distinguishing literal from merely instrumental blankets; PIFB must engage that debate when it claims its agents *are* inferential particles rather than convenient descriptions.

The "physics-by-beliefs" half of the claim only has teeth if the underlying inference is itself well-founded, and Bayesian mechanics inherits this from variational Bayes. The free energy the internal states descend is the same negative evidence lower bound (ELBO) that grounds modern variational inference ([[blei-2017-variational-inference]]), and the synchronization-map reading — internal states *parametrize* a variational density $q_\mu(\eta)$ — is the amortized / structured-posterior idea that hierarchical latent-variable models exploit, e.g. the ladder VAE's top-down precision-weighted refinement ([[sonderby-2016-ladder-vae]]). The factorised, locally-coupled form a blanketed system imposes on its beliefs is also exactly the product-of-experts trick, where a joint density is built by multiplying many simple expert distributions ([[hinton-2002-products-of-experts|hinton-2002-poe]]) — a useful lens on how nested blankets compose beliefs across scales. A coherence guarantee comes from generalized Bayes ([[bissiri-2016-general-bayesian-updating|bissiri-holmes-walker-2016-general-bayes]]): minimising expected loss plus a KL-to-prior penalty is the *unique* rational belief update, so the free-energy E-step is legitimate inference rather than ad hoc energy descent, with precision playing the role of a learning-rate / temperature (a *tempered* free energy). This decision-theoretic footing matters when the inference is not a textbook likelihood update — which is generically the case for blanketed steady-state systems.

## Multi-agent boundary (2026-08-20)

The established Bayesian-mechanics results treat one particular-state partition, one blanket, and one synchronization map, even when the state vectors are high-dimensional. Da Costa et al. identify partitioning the external space into several systems that are themselves Markov blankets as a possible extension, not as a completed interacting-blanket theorem. [[palacios-2020-hierarchical-markov-blankets]] is the nearest constructive result: suitably equipped microscopic blankets form a macroscopic blanket in simulation, while the paper rejects automatic emergence for arbitrary coupling. [[waade-2025-as-one-and-many]] and [[maisto-2025-flock-joint-agency]] likewise treat group agency as conditional on a demonstrated group-level blanket.

A multi-agent Bayesian-mechanics claim therefore owes more than coupled free-energy descent. It must specify the individual and group partitions, establish the required stationary or nonequilibrium steady-state assumptions and conditional independences, construct the individual and group synchronization maps, and prove their compatibility under composition or coarse-graining. A composite vector-valued internal state presents no dimensional obstacle, but it does not by itself induce individual blankets or reciprocal agent-wise maps. [[heins-2023-spin-glass-active-inference]] is an exact collective special case under restrictive assumptions, not a general Bayesian-mechanics extension.

## Sources

- [[dacosta-2021-bayesian-mechanics]] — technical core: synchronization map, Helmholtz decomposition, geometric free-energy descent for stationary processes.
- [[ramstead-2023-bayesian-mechanics]] — definitive review; partition/map/flow schema and the "physics of and by beliefs" phrasing.
- [[friston-2019-particular-physics]] — the founding "free energy principle for a particular physics" statement.
- [[parr-2020-markov-blankets-thermodynamics]] — thermodynamic grounding of the Markov-blanket partition.
- [[friston-2023-fep-simpler]] — leanest restatement of the principle.
- [[sakthivadivel2022-bayesian-mechanics-geometry|sakthivadivel-2022-geometry-bayesian-mechanics]] — information geometry of the synchronization map and steady-state flow.
- [[sengupta-2016-neuronal-gauge|sengupta-2016-neuronal-gauge-theory]] — named gauge-axis precursor: free-energy minimization as gauge-covariant dynamics.
- [[sengupta2017gauge|sengupta-friston-2017-bayesian-gauge-theory]] — technical follow-up: approximate Bayesian inference as a gauge theory.
- [[friston-2008-dem]] — DEM, the generalized-coordinates inference engine underlying the dynamical reading.
- [[blei-2017-variational-inference]] — the ELBO / variational-Bayes machinery the free-energy descent instantiates.
- [[sonderby-2016-ladder-vae]] — hierarchical, precision-weighted variational posterior; the synchronization-map idea in deep-learning form.
- [[hinton-2002-products-of-experts|hinton-2002-poe]] — product-of-experts factorisation, a lens on how nested-blanket beliefs compose.
- [[bissiri-2016-general-bayesian-updating|bissiri-holmes-walker-2016-general-bayes]] — generalized (Gibbs) Bayes: the free-energy E-step as the unique coherent, tempered belief update.
- [[palacios-2020-hierarchical-markov-blankets]] — conditional hierarchical Markov-blanket construction and its non-automatic-emergence boundary.
- [[heins-2023-spin-glass-active-inference]] — exact but narrow collective active-inference equivalence.
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

## Related sources (ingested 2026-06-20)

- [[friston-2016-active-inference-learning]] — Active-inference treatment of learning as free-energy minimization over time;
