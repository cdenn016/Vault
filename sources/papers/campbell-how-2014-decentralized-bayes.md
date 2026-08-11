---
type: paper
title: "Approximate Decentralized Bayesian Inference"
aliases:
  - "Campbell and How 2014 decentralized Bayes"
authors:
  - Campbell, Trevor
  - How, Jonathan P.
year: 2014
arxiv: 1403.7471
url: https://www.auai.org/uai2014/proceedings/individuals/182.pdf
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
  - field/statistics
  - field/cs-ml
created: 2026-08-10
---

# Approximate Decentralized Bayesian Inference

> [!info] Citation
> Trevor Campbell and Jonathan P. How (2014). "Approximate Decentralized Bayesian Inference." *Proceedings of the Thirtieth Conference on Uncertainty in Artificial Intelligence (UAI 2014)*, 102--111. arXiv: [1403.7471](https://arxiv.org/abs/1403.7471). [Official proceedings PDF](https://www.auai.org/uai2014/proceedings/individuals/182.pdf).

## TL;DR

Decentralized agents cannot in general multiply independently fitted approximate posteriors and expect a faithful approximation to the batch posterior. Variational factorization can destroy parameter dependencies, and separate fits can choose incompatible representatives of a permutation-symmetric model. Campbell and How repair the latter failure by optimizing the alignment of local posterior components before combining them.

## Problem & setting

The data are conditionally independent across agents given shared global parameters. Each agent performs local approximate Bayesian inference, communicates its approximate posterior rather than its raw observations, and must combine posteriors received from a changing subset of peers. A shared prior must be divided out when local posteriors are multiplied, and approximation-specific information loss remains even after that accounting is correct.

## Method

For exponential-family variational approximations, products and prior correction can be performed in natural-parameter space. The paper isolates a more subtle obstruction in mixture models: local inference chooses one of several equivalent label permutations, so componentwise multiplication without alignment can combine unrelated components. It symmetrizes the local approximations over the relevant permutation group and derives an additional optimization that selects compatible permutations during fusion.

## Key results

Synthetic and real-data experiments show that naive posterior multiplication can be badly wrong when local approximations break model symmetries. The proposed alignment step improves predictive performance while retaining decentralized computation and posterior-level communication. The result is an approximate algorithm under its exponential-family, conditional-independence, shared-prior, and known-symmetry assumptions; it is not an identity for arbitrary local posterior families.

## Relevance to this research

This paper is the primary algorithmic source for [[Decentralized Bayesian inference]]. MultiAgentELBO currently evaluates one exact finite joint law and its ELBO; that centralized oracle does not itself specify what agents transmit or how separately optimized approximations should be reconciled. A future decentralized layer should compare fused local approximations with that oracle and include a permutation-alignment negative control. Gauge-frame alignment and mixture-label alignment are distinct group actions and must not be identified without a typed construction.

## Cross-links

- Concepts: [[Decentralized Bayesian inference]], [[Communication-constrained inference]], [[Variational free energy]]
- Related sources: [[duchi-2014-distributed-estimation]], [[battistelli-chisci-2014-kl-density-consensus]]

## BibTeX

```bibtex
@inproceedings{CampbellHow2014,
  author    = {Campbell, Trevor and How, Jonathan P.},
  title     = {Approximate Decentralized Bayesian Inference},
  booktitle = {Proceedings of the Thirtieth Conference on Uncertainty in Artificial Intelligence},
  pages     = {102--111},
  year      = {2014},
  publisher = {AUAI Press},
  eprint    = {1403.7471},
  archivePrefix = {arXiv}
}
```
