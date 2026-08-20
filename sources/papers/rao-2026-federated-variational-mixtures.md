---
type: paper
title: "Federated Variational Inference for Bayesian Mixture Models"
aliases:
  - "Rao et al. 2026 federated variational mixtures"
authors:
  - Rao, Jackie
  - Crowe, Francesca L.
  - Marshall, Tom
  - Richardson, Sylvia
  - Kirk, Paul D. W.
year: 2026
arxiv: 2502.12684
url: https://proceedings.mlr.press/v297/rao26a.html
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
  - field/statistics
  - field/cs-ml
created: 2026-08-20
---

# Federated Variational Inference for Bayesian Mixture Models

> [!info] Citation
> Jackie Rao, Francesca L. Crowe, Tom Marshall, Sylvia Richardson, and Paul D. W. Kirk (2026). "Federated Variational Inference for Bayesian Mixture Models." *Proceedings of the Fifth Machine Learning for Health Symposium*, PMLR **297**, 826--863. https://proceedings.mlr.press/v297/rao26a.html. arXiv: [2502.12684](https://arxiv.org/abs/2502.12684).

## TL;DR

A one-shot federated variational method clusters large binary and categorical datasets using local merge/delete moves followed by global merges based on data summaries. It targets privacy-sensitive electronic-health-record applications and makes mixture-label reconciliation part of the variational procedure.

## Problem & setting

Large categorical mixture models are expensive to fit centrally, and health data cannot always be pooled. Independent local clustering creates an additional problem: component labels and even the number of retained clusters can differ across partitions.

## Method

Each data batch is processed in parallel with variational merge/delete moves. A global stage uses summarized local clusters and ELBO-improving merge proposals to construct a population-level mixture without sharing individual observations.

## Key results

Simulations and benchmark experiments compare favorably with clustering alternatives, and the method identifies multimorbidity patterns in British primary-care data. It is a one-shot variational divide-and-conquer method; accepted merge moves improve its stated objective but do not make all local approximations exact.

## Relevance to this research

The paper is a strong test case for discrete quotient structure in [[Decentralized Bayesian inference]]. Component-label alignment is an identifiable permutation problem, while the project's gauge transport is continuous frame alignment. A complete multi-agent implementation may need both and must keep their group actions separate.

## Cross-links

- Concepts: [[Decentralized Bayesian inference]], [[Quotient Bayesian learning]], [[Approximate Bayesian inference]]
- Related sources: [[campbell-how-2014-decentralized-bayes]], [[ashman-2022-partitioned-variational-inference]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@inproceedings{RaoEtAl2026FederatedMixtures,
  author    = {Rao, Jackie and Crowe, Francesca L. and Marshall, Tom and Richardson, Sylvia and Kirk, Paul D. W.},
  title     = {Federated Variational Inference for Bayesian Mixture Models},
  booktitle = {Proceedings of the Fifth Machine Learning for Health Symposium},
  series    = {Proceedings of Machine Learning Research},
  volume    = {297},
  pages     = {826--863},
  year      = {2026},
  publisher = {PMLR},
  eprint    = {2502.12684},
  archivePrefix = {arXiv},
  url       = {https://proceedings.mlr.press/v297/rao26a.html}
}
```
