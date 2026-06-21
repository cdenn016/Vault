---
type: paper
title: "A Duet for One"
aliases:
  - "Friston Frith 2015"
  - "Duet for One"
authors:
  - Friston, Karl
  - Frith, Christopher
year: 2015
arxiv: null
url: https://doi.org/10.1016/j.concog.2014.12.003
tags:
  - cluster/vfe
  - project/multi-agent
  - field/neuroscience
  - field/psychology
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# A Duet for One

> [!info] Citation
> Friston, K. & Frith, C. (2015). "A Duet for One." *Consciousness and Cognition*, 36, 390–405. https://doi.org/10.1016/j.concog.2014.12.003

## TL;DR
This paper formalises communication between two agents as mutual active inference under a shared generative model. The key finding is that the infinite regress of "I model you modelling me modelling you..." dissolves when both agents possess the same generative model, giving rise to generalised synchrony — a mathematical form of shared narrative. Simulations of birdsong duets demonstrate that identical synchronisation of internal dynamical states emerges automatically when two predictive coding systems are coupled through sensory exchange, without either agent explicitly representing the other's beliefs.

## Problem & setting
A longstanding puzzle in social neuroscience is how agents infer the mental states of others (theory of mind). Modelling another agent who is itself modelling you creates an apparently infinite regress. The paper asks whether this regress can be resolved within the active inference / predictive coding framework, and what the mechanism of communication actually is at the computational level.

## Method
The framework is active (Bayesian) inference: agents minimise variational free energy (surprise) by updating beliefs about hidden states and by acting to fulfil descending proprioceptive predictions. A hierarchical generative model is constructed from two coupled Lorenz attractors driving a synthetic syrinx to produce birdsong. The critical technical device is **sensory attenuation** — transiently reducing the precision (inverse variance) of auditory prediction errors to permit open-loop motor control during articulation — so an agent can either listen (high auditory precision, low proprioceptive precision) or speak (reversed), but not both simultaneously. Two such synthetic birds are then coupled: each alternately sings and listens. Generalised synchrony is measured by plotting the hidden-state trajectories of both agents against each other.

The free energy in this setting follows the standard form: minimising $F = D_{\mathrm{KL}}[q(x) \| p(x)] - \mathbb{E}_q[\log p(y | x)]$, where $q$ encodes posterior beliefs about hidden states $x$ given sensory observations $y$. Precision weighting enters as the inverse covariance of prediction errors, and sensory attenuation is implemented by reducing that weighting on auditory channels during action epochs.

## Key results
- When two birds share the same generative model and can hear each other, **identical generalised synchrony** emerges rapidly (within one exchange epoch) from random initial conditions. The synchronisation manifold collapses to the identity line in state space.
- When they cannot hear each other, chaotic divergence prevents synchronisation, confirming the causal role of sensory exchange rather than structural similarity alone.
- Successful articulation requires sensory attenuation: running without attenuation destroys the hierarchical dynamics of the higher vocal centre, producing incoherent output — offering a formal account of why one cannot speak and listen simultaneously.
- The shared narrative is amodal and **without agency**: the hidden states driving the duet transcend which bird is currently singing; agency is a contextual factor determined by precision fluctuations, not by the hidden states themselves.
- This yields a predictive-coding account of the hermeneutic circle in communication, resolving theory of mind via model-sharing rather than explicit other-modelling.

## Relevance to this research
This paper is directly relevant to the **multi-agent VFE / active inference** arm of the research program. Several connections are precise:

**Shared generative model as the resolution of mutual-modelling regress.** The paper's main claim — that agents sharing a generative model avoid infinite regress through generalised synchrony — is a single-level version of the hierarchical model-coupling at the heart of the MAgent framework. In the multi-agent VFE model, individual belief states $(mu_i, \Sigma_i)$ are coupled through attention weights $\beta_{ij}$ that include a VFE-minimising coupling term $\sum_{ij} \beta_{ij} \mathrm{KL}(q_i \| \Omega_{ij} q_j)$; Friston and Frith's result suggests this coupling, when the agents' priors $p_i$ are identical, will drive the system toward synchronised belief states rather than divergent ones.

**Precision weighting and sensory attenuation.** The paper's precision machinery maps cleanly onto the $\lambda_\alpha$ and $\beta_{ij}$ weighting parameters in the VFE free energy. Sensory attenuation — modulating the gain on prediction error channels — is structurally equivalent to modulating $\lambda_\alpha$ (the weight on the self-coupling KL term) or adjusting the attention entropy temperature $\tau$. This connection is worth making explicit in the multi-agent manuscript.

**Generalised synchrony as collective belief convergence.** The identical-synchrony outcome in simulations is a special case of the belief-alignment behaviour the multi-agent VFE model predicts under strong inter-agent coupling. The Lorenz-attractor model provides an intuitive concrete instance of how chaotic individual dynamics are tamed by coupling, relevant to the multi-agent model's claims about collective consensus formation.

**Active inference and action as belief enactment.** The proprioceptive-prediction / motor-control picture (action enacts descending predictions, minimising proprioceptive prediction error) is the single-agent active inference substrate on which multi-agent coupling is layered. Understanding this paper clarifies the distinction between perceptual and active inference modes that the MAgent architecture implicitly inherits.

The paper does not address gauge equivariance, SPD geometry, or the GL(K) attention formalism, so it is not directly relevant to the VFE transformer (GL(K)) manuscript.

## Cross-links
- Concepts: [[Active Inference]], [[Predictive Coding]], [[Variational Free Energy]], [[Generalised Synchrony]], [[Precision Weighting]], [[Theory of Mind]], [[Sensory Attenuation]]
- Related sources: [[rao-1999-predictive-coding]], [[heins-2024-surprise-minimization]], [[albarracin-2022-epistemic-communities]]
- Manuscript/Project: [[MAgent Model]], [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{FristonFrith2015duet,
  author  = {Friston, Karl and Frith, Christopher},
  title   = {A Duet for One},
  journal = {Consciousness and Cognition},
  year    = {2015},
  volume  = {36},
  pages   = {390--405},
  doi     = {10.1016/j.concog.2014.12.003},
}
```
