---
type: paper
title: "Whence the Expected Free Energy?"
aliases:
  - "Millidge et al. 2021 Whence EFE"
authors:
  - Beren Millidge
  - Alexander Tschantz
  - Christopher L. Buckley
year: 2021
arxiv: 2004.08128
url: https://doi.org/10.1162/neco_a_01354
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/neuroscience
  - field/cs-ml
created: 2026-08-10
---

# Whence the Expected Free Energy?

> [!info] Citation
> Millidge, B., Tschantz, A., & Buckley, C. L. (2021). Whence the Expected Free Energy? *Neural Computation*, 33(2), 447-482. https://doi.org/10.1162/neco_a_01354

## TL;DR

Millidge, Tschantz, and Buckley critically examine the mathematical relationship between expected free energy (EFE) and present-time variational free energy (VFE). They argue that EFE is not obtained merely by evaluating VFE in the future: a natural candidate future-VFE objective can discourage exploration. They propose the free energy of the expected future (FEEF) as an alternative objective with an epistemic component and an explicit divergence between predicted and desired futures.

## Problem & setting

EFE is widely used for active-inference policy selection because common decompositions combine preference satisfaction with information gain. The paper asks where that functional comes from, whether it is mandated by ordinary free-energy minimization, and which assumptions are needed to recover its exploratory term.

## Method

The authors compare candidate future objectives algebraically. They analyze how expectations over predicted outcomes, biased preference models, approximate posteriors, and likelihood terms change the resulting extrinsic and intrinsic components. They then define FEEF as a KL divergence between predicted and desired future joint laws.

## Key results

The analysis shows that exploration does not follow simply from carrying present VFE forward in time. Under an approximately correct posterior, FEEF and EFE share an intrinsic information-seeking term, while their extrinsic terms differ. FEEF reduces to a present-time VFE construction under additional conditions described by the authors. This is a proposed critical reconstruction, not a universal refutation of every EFE convention or an empirical comparison across all active-inference agents.

## Relevance to this research

The paper supplies necessary counterevidence for [[Expected Free Energy]]. EFE's epistemic/pragmatic and risk/ambiguity forms should be stated with their generative-model, preference, factorization, and posterior-approximation assumptions rather than called an assumption-free continuation of VFE. It also prevents an attention score or collective finite ELBO from being relabeled as an active-policy objective by analogy alone. The current MultiAgentELBO code has no EFE policy-selection layer.

## Cross-links

- Concepts: [[Expected Free Energy]], [[Active Inference]], [[Variational free energy]], [[Collective active inference]]
- Related sources: [[parr-friston-2019-generalised]], [[smith-2022-active-inference-tutorial]]

## BibTeX

```bibtex
@article{millidge2021whenceefe,
  author  = {Millidge, Beren and Tschantz, Alexander and Buckley, Christopher L.},
  title   = {Whence the Expected Free Energy?},
  journal = {Neural Computation},
  volume  = {33},
  number  = {2},
  pages   = {447--482},
  year    = {2021},
  doi     = {10.1162/neco_a_01354}
}
```
