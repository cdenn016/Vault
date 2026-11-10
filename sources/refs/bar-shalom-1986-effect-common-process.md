---
type: reference
title: "The Effect of the Common Process Noise on the Two-Sensor Fused-Track Covariance"
aliases: ["barshalom1986effect"]
authors: ["Yaakov Bar-Shalom", "Leon Campo"]
year: 1986
venue: "IEEE Transactions on Aerospace and Electronic Systems"
doi: "10.1109/TAES.1986.310815"
url: "https://doi.org/10.1109/TAES.1986.310815"
tags: [cluster/multi-agent, project/multi-agent, field/statistics]
created: 2026-11-10
updated: 2026-11-10
---
# The Effect of the Common Process Noise on the Two-Sensor Fused-Track Covariance

> [!info] Citation
> Bar-Shalom, Y., Campo, L. (1986). *The Effect of the Common Process Noise on the Two-Sensor Fused-Track Covariance*. IEEE Transactions on Aerospace and Electronic Systems, AES-22(6), 803-805. [DOI](https://doi.org/10.1109/TAES.1986.310815)

No local copy: no open-access file passed validation on November 10, 2026. Reading basis: abstract and manuscript reading record.

## TL;DR

A short note on how common process noise affects the fusion of state estimates of one target from two sensors that each run their own tracking subsystem.

## Problem & setting

The problem arises in a multisensor environment where each sensor has its own tracking subsystem, so that the estimates fused are dependent through the shared process noise.

## Key results

For an alpha-beta tracking filter, the abstract states that over a wide range of process-noise variance the uncertainty area of the fused estimate is about 70 percent of the single-sensor area, against 50 percent if the dependence is ignored. Only the abstract was read.

## Relevance to this research

The manuscript cites this note for cross-covariance-aware track fusion: the update with a likelihood that accounts for the correlation between sender and receiver errors. It is also cited, with [[bar-shalom-1981-track-track-correlation]], for calibrated updates under correlated messages and as an instance of the classical double counting of common information, which the manuscript contrasts with its ladder from literal reading to exact fusion. Related pages: [[Conservative information fusion]], [[Gaussian Belief Propagation]], [[Decentralized Bayesian inference]], [[Kalman filter]].

## Cross-links

[[Collective agents literature map]]; [[Conservative information fusion]]; [[Gaussian Belief Propagation]]; [[Decentralized Bayesian inference]]; [[Kalman filter]]; [[bar-shalom-1981-track-track-correlation]].

## BibTeX

```bibtex
@article{barshalom1986effect,
  author  = {Bar-Shalom, Yaakov and Campo, Leon},
  title   = {The Effect of the Common Process Noise on the Two-Sensor Fused-Track Covariance},
  journal = {IEEE Transactions on Aerospace and Electronic Systems},
  volume  = {AES-22},
  number  = {6},
  pages   = {803--805},
  year    = {1986},
  doi     = {10.1109/TAES.1986.310815}
}
```
