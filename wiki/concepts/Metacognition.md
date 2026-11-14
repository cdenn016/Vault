---
type: concept
title: "Metacognition"
aliases:
  - "Metacognitive accuracy"
  - "Confidence calibration"
tags:
  - cluster/multi-agent
  - cluster/social-physics
  - project/multi-agent
  - project/social-physics
status: stub
created: 2026-06-21
updated: 2026-11-13
---

# Metacognition

Metacognition is cognition about one's own cognition: the monitoring and evaluation of one's knowledge, performance, and confidence. Poor metacognitive accuracy underlies the Dunning-Kruger effect, where low-skill individuals overestimate their competence because the skills needed to perform a task overlap with those needed to judge performance. In belief-dynamics terms it concerns the calibration of an agent's precision/confidence over its own beliefs.

## Related
[[Belief inertia]], [[Mass as Fisher information]]

## Sources
[[kruger1999-unskilled-unaware]], [[sandved-smith-2024-metacognitive-particles]]

## Metacognitive particles in Bayesian mechanics, November 13, 2026

[[sandved-smith-2024-metacognitive-particles]] defines metacognition in the particular-partition language of [[Bayesian mechanics]]. A particle is cognitive when a map from internal paths to beliefs exists such that the most likely internal path given blanket paths encodes the posterior over external paths; the paper separates this from a particle as such, which only has a [[Markov Blanket|blanket]] over some period. A metacognitive particle is a cognitive particle in which one subset of internal paths, $\mu^{(2)}$, parameterizes posterior beliefs about another subset, $\mu^{(1)}$, and under a mean-field factorization the higher-level belief is a belief about the parameters of a belief. Metacognition is passive when the higher level reads the lower level only through the particle's sensory paths. It is active when an internal blanket with its own sensory and active paths lets the higher level act on the sufficient statistics of the lower-level belief. With a Gaussian lower belief $\mathcal{N}(\eta; m, \Pi)$ the inner particle holds beliefs about the mean and the precision and its active paths can modulate them, which the authors read as mental action and as a proxy for attention ([[Precision weighting]]). Metacognition is comprehensive when the higher level holds beliefs about all sufficient statistics of the lower-level belief, and the paper contrasts this with partial metacognition. For strange nested particles the sense of agency is defined as a joint higher-level belief over lower-level internal and active paths, with strength given by the [[Mutual information|mutual information]] of its eq. 20,

$$
D_{KL}\big[ Q_{\mu^{(2)}}(\mu^{(1)}, a^{(1)}) \| Q_{\mu^{(2)}}(\mu^{(1)}) Q_{\mu^{(2)}}(a^{(1)}) \big].
$$

The contribution is definitional. The paper states no theorem, gives no conditions on the dynamics under which these beliefs exist and runs no simulations. Its finiteness of nesting depth is an informal complexity argument, the innermost level that is never the target of further beliefs is a conjecture, and the prediction that the agency measure correlates with behavior in a control-detection task is untested.

> [!note] Editorial: relation to confidence over one's own beliefs
> The opening description on this page, calibration of an agent's confidence over its own beliefs, corresponds here to the higher level's belief about the lower level's precision $\Pi$. In the gauge-VFE model that would be a belief placed over an agent's fiber coordinates $(\mu, \Sigma)$. The correspondence is an analogy, since the paper has no metric, transport or dynamics for these beliefs.
