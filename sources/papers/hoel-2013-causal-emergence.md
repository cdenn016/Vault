---
type: paper
title: "Quantifying causal emergence shows that macro can beat micro"
aliases:
  - "Hoel 2013 causal emergence"
  - "causal emergence"
  - "macro can beat micro"
authors:
  - Hoel, Erik P.
  - Albantakis, Larissa
  - Tononi, Giulio
year: 2013
url: https://www.pnas.org/doi/10.1073/pnas.1314922110
tags:
  - cluster/participatory/consciousness
  - cluster/multi-agent
  - project/multi-agent
  - field/neuroscience
  - field/philosophy
created: 2026-08-18
---

# Quantifying causal emergence shows that macro can beat micro

> [!info] Citation
> Erik P. Hoel, Larissa Albantakis, and Giulio Tononi (2013). "Quantifying causal emergence
> shows that macro can beat micro." *PNAS* 110(49):19790–19795.
> doi: [10.1073/pnas.1314922110](https://doi.org/10.1073/pnas.1314922110).

## TL;DR

Coarse-grained (macro) causal models of a system can carry strictly higher *effective
information* (EI) than the micro model that fully specifies them: when micro dynamics are noisy
or degenerate, an appropriately chosen macro partition yields more deterministic, less
degenerate transition structure, and EI — measured with interventional (maximum-entropy
perturbation) distributions — peaks at the macro scale. The authors define causal emergence as
this supersession of macro over micro.

## Key results

EI depends on determinism, degeneracy, and state-space size; toy Markov systems exhibit macro
partitions whose EI exceeds the micro EI even though macro is a deterministic function of
micro. The construction does not violate the data processing inequality: EI is computed under
interventions (do-distributions), not under the pushforward of observational micro data, so
"macro beats micro" is a statement about the quality of a causal channel at a description
scale, not about extracting more observational information than the micro state carries.

## Relevance to this research

This is the one rigorous published sense in which "higher levels carry more information," and
its precise scope matters for the program: in the gauge-theoretic laboratory, observational
boundary information strictly contracts under blocking ([[Data processing inequality]],
measured retention 2–7%), while the regenerated coarse theory can still be the better *causal*
description of level dynamics — the two claims are compatible because they use different
distributions. A candidate future measurement: EI of the coarse regenerated step against the
fine step, which would make the causal-emergence claim internal and testable rather than an
analogy. Connects to [[Meta-agents and hierarchical emergence]] and the Tononi lineage already
in the vault ([[tononi-2004-integrated-information]]).

## Cross-links

- Concepts: [[Data processing inequality]], [[Meta-agents and hierarchical emergence]], [[Coarse Graining]]
- Related sources: [[tononi-2004-integrated-information]], [[zheng-meister-2025-unbearable-slowness]], [[2026-08-18-minfo-information-retention]]

## BibTeX

```bibtex
@article{HoelAlbantakisTononi2013,
  author  = {Hoel, Erik P. and Albantakis, Larissa and Tononi, Giulio},
  title   = {Quantifying causal emergence shows that macro can beat micro},
  journal = {Proceedings of the National Academy of Sciences},
  volume  = {110},
  number  = {49},
  pages   = {19790--19795},
  year    = {2013},
  doi     = {10.1073/pnas.1314922110}
}
```
