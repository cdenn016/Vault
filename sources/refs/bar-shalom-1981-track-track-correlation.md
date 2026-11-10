---
type: reference
title: "On the track-to-track correlation problem"
aliases: ["barshalom1981track"]
authors: ["Y. Bar-Shalom"]
year: 1981
venue: "IEEE Transactions on Automatic Control"
doi: "10.1109/TAC.1981.1102635"
url: "https://doi.org/10.1109/TAC.1981.1102635"
tags: [cluster/multi-agent, project/multi-agent, field/statistics]
created: 2026-11-10
updated: 2026-11-10
---
# On the track-to-track correlation problem

> [!info] Citation
> Bar-Shalom, Y. (1981). *On the track-to-track correlation problem*. IEEE Transactions on Automatic Control, 26(2), 571-572. [DOI](https://doi.org/10.1109/TAC.1981.1102635)

No local copy: no open-access file passed validation on November 10, 2026. Reading basis: abstract and manuscript reading record.

## TL;DR

A two-page note on testing whether two tracks represent the same target, which presents a test that accounts for correlation between the two tracks' state estimates.

## Problem & setting

According to the abstract, earlier literature assumed that the estimates of one target's state from two track files are uncorrelated.

## Key results

The abstract states that a test including the correlation is presented. The manuscript's record says only the abstract and the bibliographic record were read.

## Relevance to this research

The manuscript cites the note, together with [[bar-shalom-1986-effect-common-process]], for the calibrated update of a receiver that gets a message whose error is correlated with its own, which is track-to-track fusion. The gain that minimizes the posterior covariance and the cost of ignoring correlation are worked out in the manuscript's supplement, not taken from this note. The link is to double counting of common information, as in [[Conservative information fusion]], [[Decentralized Bayesian inference]], [[Kalman filter]] and [[Belief Propagation]].

## Cross-links

[[Collective agents literature map]]; [[Conservative information fusion]]; [[Decentralized Bayesian inference]]; [[Kalman filter]]; [[bar-shalom-1986-effect-common-process]].

## BibTeX

```bibtex
@article{barshalom1981track,
  author  = {Bar-Shalom, Y.},
  title   = {On the track-to-track correlation problem},
  journal = {IEEE Transactions on Automatic Control},
  volume  = {26},
  number  = {2},
  pages   = {571--572},
  year    = {1981},
  doi     = {10.1109/TAC.1981.1102635}
}
```
