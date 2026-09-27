---
type: reference
title: "Probabilistic Inference for Solving Discrete and Continuous State Markov Decision Processes"
aliases:
  - "Toussaint and Storkey 2006"
  - "Probabilistic Inference for Solving Discrete and Continuous State Markov Decision Processes"
  - "ToussaintStorkey2006"
authors:
  - Marc Toussaint
  - Amos Storkey
year: 2006
doi: 10.1145/1143844.1143963
url: https://homepages.inf.ed.ac.uk/amos/publications/ToussaintStorkey2006ProbabilisticInferenceSolvingMDPs.pdf
tags:
  - cluster/vfe
  - project/transformer
  - field/cs-ml
  - field/statistics
created: 2026-09-23
updated: 2026-09-23
---

# Probabilistic Inference for Solving Discrete and Continuous State Markov Decision Processes

> [!info] Citation
> Marc Toussaint and Amos Storkey (2006). "Probabilistic Inference for Solving Discrete and Continuous State Markov Decision Processes." *Proceedings of the 23rd International Conference on Machine Learning* (ICML 2006), 945–952. DOI: [10.1145/1143844.1143963](https://doi.org/10.1145/1143844.1143963). No arXiv version; the author-hosted camera-ready copy was read.

## TL;DR

Solving a Markov decision process is recast exactly as likelihood maximization in a latent-variable model. Rewards are binary observed variables, the MDP is replaced by a mixture of finite-time MDPs with a geometric prior over the horizon, and the likelihood of observing a reward is proportional to the expected discounted return. EM then computes optimal policies, and any inference method can be used in the E-step.

## What it establishes

Section 2 defines the dynamic Bayesian network of a time-unbounded MDP and takes the reward variable to be binary, $r_t\in\{0,1\}$. A footnote justifies this: binary reward variables suffice to associate arbitrary reward expectations in $[0,1]$ with states and actions, which is the general case up to rescaling. Section 3 introduces a mixture of finite-time MDPs, each emitting a reward only at its final step, with time prior $P(T)=\gamma^T(1-\gamma)$. With this prior the likelihood $P(r=1\mid x_0;\pi)$ is proportional to the expected discounted future return, and Theorem 3.1 states that maximizing it is equivalent to solving the MDP, without fixing a total time in advance. Section 4 gives the EM algorithm, whose E-step runs synchronized forward and backward propagation over all horizons at once and yields posteriors over the horizon $T$. Section 5 relates the algorithm to policy iteration. Sections 6 and 7 demonstrate exact inference on a discrete maze and Gaussian belief-state propagation (with the unscented transform) on a continuous stochastic optimal-control problem.

## Relevance to this research

The September 2026 v2 revision of the GL(K) attention manuscript cites this paper, with [[levine-2018-control-as-inference]] and [[kappen-2012-optimal-control-inference]], for the binary-observation device. A binary variable whose conditional probability encodes a score lets one condition on "success" and read the resulting posterior as the solution of an optimization. In the manuscript the variable is a compatibility record with $P(o=1\mid J=j)=\exp(-D_{ij}/\tau)$, which makes Gibbs routing the exact source-label posterior at every temperature. See [[GL(K) gauge-equivariant attention]].

## Local full text

No arXiv copy exists. The camera-ready PDF hosted on Amos Storkey's University of Edinburgh homepage is stored at `sources/pdfs/ToussaintStorkey2006.pdf` ([local PDF](../pdfs/ToussaintStorkey2006.pdf)). Source: [author copy](https://homepages.inf.ed.ac.uk/amos/publications/ToussaintStorkey2006ProbabilisticInferenceSolvingMDPs.pdf). SHA-256: `b162a073dbfd37b12d789b2022284122116114609797a992f832231076f2a76f`.

## BibTeX

```bibtex
@inproceedings{ToussaintStorkey2006,
  author = {Toussaint, Marc and Storkey, Amos},
  title = {Probabilistic Inference for Solving Discrete and Continuous State {M}arkov Decision Processes},
  booktitle = {Proceedings of the 23rd International Conference on Machine Learning},
  pages = {945--952},
  year = {2006},
  doi = {10.1145/1143844.1143963}
}
```
