---
type: reference
title: "Signal propagation and noisy circuits"
aliases: ["evans1999signal"]
authors: ["W. S. Evans", "L. J. Schulman"]
year: 1999
venue: "IEEE Transactions on Information Theory"
doi: "10.1109/18.796377"
url: "https://doi.org/10.1109/18.796377"
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/cs-ml, field/statistics]
created: 2026-11-10
updated: 2026-11-10
---
# Signal propagation and noisy circuits

> [!info] Citation
> Evans, W. S., Schulman, L. J. (1999). *Signal propagation and noisy circuits*. IEEE Transactions on Information Theory 45(7), 2367-2373. [DOI](https://doi.org/10.1109/18.796377)

No local copy: no open-access file passed validation on November 10, 2026. Reading basis: abstract and manuscript reading record.

## TL;DR

The paper bounds how fast the information carried by a signal decays as it crosses a noisy channel, and uses the bound to prove depth lower bounds for reliable computation in von Neumann's noisy circuit model.

## Problem & setting

Information decays when a signal is corrupted by random noise, whether in transmission over a channel or in a noisy component doing computation. In the circuit model each component fails independently with a fixed probability, while the output must be correct with high probability.

## Key results

The abstract reports a tight bound on the rate of information loss across a noisy channel. From it the authors derive a lower bound on the multiplicative increase in circuit depth needed for reliable computation, and an upper bound on the noise level at which reliable computation remains possible.

## Relevance to this research

The manuscript cites the paper as the precursor of a bound on information flow in Bayesian networks by site percolation due to Polyanskiy and Wu (2017). The reading record says only the bibliographic data were verified. The paper relates to [[Data processing inequality]], [[Channel Capacity]] and [[Mutual information]].

## Cross-links

[[Collective agents literature map]]; [[Data processing inequality]]; [[Channel Capacity]]; [[Mutual information]]; [[evans-2000-broadcasting-trees-ising]].

## BibTeX

```bibtex
@article{evans1999signal,
  author  = {Evans, W. S. and Schulman, L. J.},
  title   = {Signal propagation and noisy circuits},
  journal = {IEEE Transactions on Information Theory},
  volume  = {45},
  number  = {7},
  pages   = {2367--2373},
  year    = {1999},
  doi     = {10.1109/18.796377}
}
```
