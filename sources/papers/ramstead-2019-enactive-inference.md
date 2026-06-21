---
type: paper
title: "A tale of two densities: active inference is enactive inference"
aliases:
  - "Ramstead 2019"
  - "enactive inference"
  - "ramstead-2019-variational-neuroethology"
  - "Ramstead et al. 2019"
  - "Variational neuroethology"
authors:
  - Ramstead, Maxwell JD
  - Kirchhoff, Michael D
  - Friston, Karl J
year: 2019
arxiv: null
url: https://doi.org/10.1177/1059712319862774
tags:
  - cluster/participatory/philosophy-of-mind
  - project/multi-agent
  - field/neuroscience
  - field/philosophy
  - field/biology
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# A tale of two densities: active inference is enactive inference

> [!info] Citation
> Ramstead, M. J. D., Kirchhoff, M. D., & Friston, K. J. (2019). "A tale of two densities: active inference is enactive inference." *Adaptive Behavior*, 28(4), 225–239. DOI: 10.1177/1059712319862774

## TL;DR

This paper clarifies the interpretation of generative models and recognition densities within the free-energy principle (FEP) and active inference, arguing against a prevailing structural representationalist reading. The authors propose an "enactive inference" interpretation in which the generative model is not a brain-encoded structural representation but rather a control system that is entailed by the adaptive dynamics of an organism, while the recognition density is what the organism literally embodies. The distinction dissolves the conflation of active inference with predictive coding and the Bayesian brain by centering the circular causality between action and perception.

## Problem & setting

The paper targets a systematic misrepresentation in the FEP literature: the conflation of active inference with brain-centred Bayesian theories (predictive coding, prediction error minimisation) which treat generative models as structural representations — internal neural structures whose statistical properties mirror the causal structure of the environment. Drawing on Kiefer & Hohwy (2018, 2019), Gadziejewski (2016), and others as their target, the authors ask whether generative models and recognition densities, as they actually appear in the FEP mathematical framework, warrant the representationalist gloss.

## Method

The argument is philosophical and information-theoretic rather than empirical, grounded in the formal apparatus of active inference. Key constructs introduced or clarified include:

- **Markov blankets**: a partition of states into internal, external, sensory, and active, defining system identity and shielding internal from external states.
- **Variational free energy**: $F(Q) = \mathbb{E}_Q[\ln Q(s) - \ln P(s, o)]$, which upper-bounds surprise ($-\ln P(o)$); minimisation yields the recognition density $Q(s) \approx P(s|o)$.
- **Expected free energy** $G$: the policy-conditioned free energy over future states, whose minimisation drives action selection.
- The **generative model** $P(o,s,\pi)$ is presented as a Bayesian network (A, B, C, D, H matrices for likelihood, transitions, preferences, initial states, and ambiguity) and as a Forney factor graph supporting belief propagation.

The authors distinguish the generative model (a stipulative probabilistic structure that is *entailed* by dynamics, never physically instantiated as such) from the recognition density (the approximate posterior parameterised by internal states, which the organism *embodies*). Invoking the good regulator theorem (Conant & Ashby, 1970), they cast the generative model as a control system — structurally isomorphic to the generative process in order to regulate the organism's behaviour, not to represent the world.

## Key results

The paper's central philosophical finding is that representationalists commit a category error: the structures encoding exploitable structural similarities to the environment are the internal states (the recognition density), not the generative model. The generative model does not encode anything; it is realised by the statistical relations between states and is enacted through adaptive behaviour. Specific conclusions are:

1. The generative model is entailed by the organism's dynamics and functions as a control system that selects action policies by inducing free energy gradients.
2. The recognition density is embodied by internal states whose sufficient statistics (expectations and precisions) parameterise an approximate posterior.
3. Active inference generalises predictive inference: perception is *one moment* of policy selection, not an independent process; action and perception are circularly causal.
4. Structural representationalism is vindicated only at the level of the recognition density (internal states encode exploitable environmental structure), but this vindication is accomplished through enactivist resources — these structures are established and maintained through active inference (action).

## Relevance to this research

This paper is directly relevant to the multi-agent active inference program underpinning the VFE transformer. Its formal articulation of the generative/recognition density distinction maps precisely onto the VFE hierarchy $h \to s \to p \to q \to o$: the hyper-prior $h$ and model-level density $s$ play roles analogous to the enacted generative model, while the belief tuple $(μ, Σ, φ)$ at the $q$ level is the embodied recognition density whose sufficient statistics the E-step updates. The Markov blanket formalism underpins the agent-environment boundary implicit in the GL(K) attention architecture, where each token maintains an internal belief state isolated from external tokens except through the sensory/active interface encoded by gauge-transported attention weights $\Omega_{ij}$. The paper's insistence that the generative model is a control system (not a representational mirror) aligns with the VFE transformer's design philosophy: free-energy minimisation drives policy-like attention allocation, not feature matching. The action-perception cycle described here foreshadows multi-scale active inference in the multi-agent model, where model-level beliefs $s_i$ couple via meta-attention $\gamma_{ij}$ in the same circular causal structure.

## Cross-links
- Concepts: [[Free-energy principle active inference|Free Energy Principle]], [[Active Inference]], [[Markov Blanket]], [[Variational Free Energy]], [[Recognition Density]]
- Related sources: [[friston-2010-free-energy-principle|friston-2010-free-energy]], [[ramstead-2018-answering-schrodinger]], [[kirchhoff-2018-markov-blankets-of-life]]
- Manuscript/Project: [[VFE Transformer Program]], [[Gauge-Theoretic Multi-Agent VFE Model|MAgent Model]]

## BibTeX
```bibtex
@article{Ramstead2019,
  author  = {Ramstead, Maxwell J. D. and Kirchhoff, Michael D. and Friston, Karl J.},
  title   = {A tale of two densities: active inference is enactive inference},
  journal = {Adaptive Behavior},
  year    = {2019},
  volume  = {28},
  number  = {4},
  pages   = {225--239},
  doi     = {10.1177/1059712319862774},
}
```
