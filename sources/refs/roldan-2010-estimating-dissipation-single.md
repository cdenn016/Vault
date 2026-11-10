---
type: reference
title: "Estimating Dissipation from Single Stationary Trajectories"
aliases: ["roldan2010estimating"]
authors: ["Édgar Roldán", "Juan M. R. Parrondo"]
year: 2010
venue: "Physical Review Letters"
doi: "10.1103/PhysRevLett.105.150607"
arxiv: "1004.2831"
url: "https://doi.org/10.1103/PhysRevLett.105.150607"
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/physics]
created: 2026-11-10
updated: 2026-11-10
---

# Estimating Dissipation from Single Stationary Trajectories

> [!info] Citation
> Roldán, É., Parrondo, J. M. R. (2010). *Estimating Dissipation from Single Stationary Trajectories*. Physical Review Letters, 105, 150607. [DOI](https://doi.org/10.1103/PhysRevLett.105.150607), [arXiv](https://arxiv.org/abs/1004.2831)

[Local PDF](../pdfs/roldan-2010-estimating-dissipation-single.pdf), 4 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages and manuscript reading record.

## TL;DR

The time-reversal asymmetry of a stationary time series carries information about the entropy production of the mechanism that generated it, even without knowledge of that mechanism. The authors build estimators of entropy production that can detect nonequilibrium processes when no flows are measurable.

## Problem & setting

The introduction recalls that the mean entropy production of a process driven by an external agent equals the relative entropy between the forward and backward path distributions, a relation derived for Hamiltonian and Langevin dynamics. For a nonequilibrium stationary state, the entropy production rate is $k$ times the long-time limit of $D/t$, where $D$ is the relative entropy between the probability of a trajectory and that of its time reverse. The setting is a stationary trajectory, so no reversal of driving is needed, and the practical problem is to estimate the rate from partial information such as a non-invertible function of the phase-space coordinates.

## Method

The Letter uses the relative entropy computed on partial information, and builds estimators from the time-reversal asymmetry of the observed series. The reading record adds that the bound on entropy production, from below, is $k_{\mathrm B}$ times the relative-entropy rate between an observed stationary series and its time reverse, and that a flashing ratchet in the fast-switching limit is the example of a series that hides dissipation.

## Key results

The abstract-level claim, supported by the first pages, is that the estimators detect nonequilibrium processes even without measurable flows. Details of the estimators beyond the first page were not read for this note.

## Relevance to this research

The manuscript cites the paper for the use of the rate $\lim_n D_n/n$ of the relative entropy between a stationary series and its reverse as a dissipation bound, alongside two earlier results that link dissipated work to forward-backward relative entropy. It supports the manuscript's thermodynamic accounting of communication; related vault pages are [[Stochastic Thermodynamics]], [[Nonequilibrium steady state]] and [[Information is Physical]].

## Cross-links

[[Collective agents literature map]]; [[Stochastic Thermodynamics]]; [[Nonequilibrium steady state]]; [[Information is Physical]]; [[sagawa-2009-minimal-energy-cost]].

## BibTeX

```bibtex
@article{roldan2010estimating,
  author  = {Rold{\'a}n, {\'E}dgar and Parrondo, Juan M. R.},
  title   = {Estimating Dissipation from Single Stationary Trajectories},
  journal = {Physical Review Letters},
  volume  = {105},
  pages   = {150607},
  year    = {2010},
  doi     = {10.1103/PhysRevLett.105.150607},
  eprint  = {1004.2831},
  archiveprefix = {arXiv}
}
```
