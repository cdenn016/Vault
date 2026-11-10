---
type: reference
title: "Renormalising Generative Models for Active Inference: Foundations, Derivations, and Verification"
aliases: ["zaghw2026renormalising"]
authors: ["Karim Zaghw", "Andrew Pashea", "Marc Pritsch", "Wouter Nuijten", "Karl Friston", "Lancelot Da Costa"]
year: 2026
arxiv: "2608.09512"
url: "https://arxiv.org/abs/2608.09512"
tags: [cluster/multi-agent, cluster/vfe, project/multi-agent, field/cs-ml, field/neuroscience]
created: 2026-11-10
updated: 2026-11-10
---
# Renormalising Generative Models for Active Inference: Foundations, Derivations, and Verification

> [!info] Citation
> Zaghw, K., Pashea, A., Pritsch, M., Nuijten, W., Friston, K., Da Costa, L. (2026). *Renormalising Generative Models for Active Inference: Foundations, Derivations, and Verification*. arXiv preprint. [arXiv](https://arxiv.org/abs/2608.09512)

[Local PDF](../pdfs/zaghw-2026-renormalising-generative-models.pdf), 25 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages. The extract covers the abstract, the introduction and the model and structure-learning sections.

## TL;DR

A self-contained, derivation-oriented account of renormalising generative models (RGMs) for discrete active inference, with an open verified implementation. It reconstructs the hierarchy, the belief and action updates, and the passing of information between levels.

## Problem & setting

Discrete active-inference models become hard to use at scale because states, transitions and policies multiply. RGMs compose the same discrete model across spatial and temporal scales. The paper says the original exposition is compact and the reference implementation is embedded in specialized software, so many algorithmic details are implicit.

## Method

Each level has hidden states, paths, likelihoods, transitions and empirical-prior mappings. Lower-level episodes are summarized upward, and higher-level beliefs return downward as empirical priors. Updates use variational message passing with Dirichlet-categorical conjugacy, and planning scores paths by expected free energy. The paper describes fast structure learning as the renormalization operator: it groups sites by mutual information through a spectral relaxation, turns recurring local patterns into coarse states, and passes state and path summaries upward. It states which steps the published equations and the implementation treat differently, such as expected-log messages versus log posterior-predictive probabilities.

## Key results

The contribution is expository and implementational: a derivation, an open implementation, and explicit statements of where the equations and executable routines differ. The extract contains no error bound for the coarse-graining.

## Relevance to this research

The manuscript lists this paper among later works it has not read, in two places: the open question of error bounds for adiabatic reductions in active-inference renormalization, and the statement that its search for such a bound does not cover this paper. The present note is the first reading of the paper's opening sections, and the extract found no error bound, which does not settle the question for the rest of the paper. See [[Active Inference]], [[Hierarchical generative model]], [[Coarse Graining]] and [[Renormalization group flow]].

## Cross-links

[[Collective agents literature map]]; [[Active Inference]]; [[Hierarchical generative model]]; [[Coarse Graining]]; [[Renormalization group flow]].

## BibTeX

```bibtex
@misc{zaghw2026renormalising,
  author        = {Zaghw, Karim and Pashea, Andrew and Pritsch, Marc and Nuijten, Wouter and Friston, Karl and Da Costa, Lancelot},
  title         = {Renormalising Generative Models for Active Inference: Foundations, Derivations, and Verification},
  year          = {2026},
  eprint        = {2608.09512},
  archivePrefix = {arXiv}
}
```
