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
  - cluster/participatory/consciousness
  - cluster/multi-agent
  - project/multi-agent
  - field/neuroscience
  - field/physics
  - field/psychology
  - field/philosophy
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# A Duet for One

> [!info] Citation
> Friston, K., & Frith, C. (2015). "A Duet for One." *Consciousness and Cognition*, 36, 390–405. https://doi.org/10.1016/j.concog.2014.12.003

## TL;DR
Friston and Frith show that the infinite regress in modelling another agent who is simultaneously modelling you dissolves if both agents share the same generative model. Treating communication as active inference under a shared narrative, they demonstrate via birdsong simulations that coupling two predictive-coding schemes through sensory exchange produces generalised (identical) synchronisation of internal brain states, which they identify as the formal signature of communication. The mechanism hinges on sensory attenuation: agents must alternate between attending to sensations (listening) and attenuating sensory input (speaking), making turn-taking an emergent property of precision control.

## Problem & setting
Theory of mind traditionally poses an infinite regress: inferring another agent who is simultaneously inferring you. Standard Bayesian brain accounts do not resolve this regress. Prior work on active inference had treated perception and action as minimisation of variational free energy, but had not extended this to multi-agent communication. The paper asks whether a formal, generative-model-based account of communication can emerge from first principles of active inference, without positing explicit theory-of-mind computations.

## Method
The authors use hierarchical generalised predictive coding (DEM/spm_ADEM scheme) with Lorenz-attractor-based generative models of birdsong. The key equations are the generalised gradient descent on free energy:

$$\dot{\tilde{\mu}}(t) = D\tilde{\mu}(t) - \partial_{\tilde{\mu}} F(\tilde{s}, \tilde{\mu})$$

where $\tilde{\mu}$ are generalised posterior expectations over hidden states, $\tilde{s}$ generalised sensory inputs, and $D$ is the shift operator returning generalised motion. The hierarchical generative model has two Lorenz attractors (fast: ~100 ms, slow: ~seconds) controlling syrinx frequency and amplitude. Precision parameters (log-precision of proprioceptive vs. exteroceptive prediction errors) are toggled to switch a bird between singing mode (high proprioceptive precision, attenuated auditory precision) and listening mode (low proprioceptive precision, high auditory precision). Two such birds are coupled by making each hear the other's output. Generalised synchrony is quantified by inspecting the synchronisation manifold (a 1-D attractor in the joint state space when birds are coupled).

## Key results
Simulations show three main findings. First, a bird cannot sing a well-formed song while simultaneously attending to its own auditory feedback (sensorimotor delays produce perpetual prediction errors that destroy attractor dynamics); sensory attenuation of the auditory channel is necessary and sufficient to restore coherent song. Second, two birds with the same generative model but different initial conditions fail to synchronise when they cannot hear each other (chaotic divergence), but synchronise almost immediately once within earshot, with identical synchrony at both hierarchical levels. Third, the mathematics of the free energy principle guarantee this: any measure-preserving coupled dynamical system with a Markov blanket possesses a random dynamical attractor (the synchronisation manifold), and minimising free energy reduces the measure of this attractor, making generalised synchrony inevitable. Theory of mind reduces to inferring which state one would need to be in to produce the observed sensory consequences — agency is contextualised by fluctuations in sensory attenuation, not encoded in the shared hidden states themselves.

## Relevance to this research
This paper is a direct precursor to the multi-agent active-inference framework in the VFE research program. Several connections are specific. The shared-generative-model resolution of the infinite-regress problem maps onto the multi-agent VFE architecture, where agents sharing the same belief geometry (GL(K) gauge structure, SPD priors) can synchronise without explicit other-modelling. The precision-weighted prediction-error message passing is the neuroscience counterpart to the VFE free-energy functional's attention weights $\beta_{ij}$ (belief coupling) and the KL divergence terms governing agent-to-model alignment. Sensory attenuation as a precision toggle is structurally analogous to the attention temperature $\tau = \kappa\sqrt{d}$ controlling how sharply the softmax $\beta$ concentrates. The generalised synchrony result supports the broader claim in the multi-agent program that FEP-coupled agents converge to shared representations under iterated VFE minimisation. The Markov blanket argument for inevitable synchrony is the dynamical-systems underpinning of why gauge-equivariant coupling should yield coherent multi-agent equilibria.

## Cross-links
- Concepts: [[Active Inference]], [[Predictive Coding]], [[Free Energy Principle]], [[Markov Blanket]], [[Generalised Synchrony]], [[Sensory Attenuation]]
- Related sources: [[friston-2006-free-energy]], [[friston-2010-generalised-filtering]], [[feldman-friston-2010-attention]]
- Manuscript/Project: [[VFE Transformer Program]], [[MAgent Model]]

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
