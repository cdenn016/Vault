---
type: reference
title: "Dissipation: The Phase-Space Perspective"
aliases: ["kawai2007dissipation"]
authors: ["R. Kawai", "J. M. R. Parrondo", "C. Van den Broeck"]
year: 2007
venue: "Physical Review Letters"
doi: "10.1103/PhysRevLett.98.080602"
arxiv: "cond-mat/0701397"
url: "https://doi.org/10.1103/PhysRevLett.98.080602"
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/physics]
created: 2026-11-10
updated: 2026-11-10
---
# Dissipation: The Phase-Space Perspective

> [!info] Citation
> Kawai, R., Parrondo, J. M. R., Van den Broeck, C. (2007). *Dissipation: The Phase-Space Perspective*. Physical Review Letters, 98, 080602. [DOI](https://doi.org/10.1103/PhysRevLett.98.080602), [arXiv](https://arxiv.org/abs/cond-mat/0701397)

[Local PDF](../pdfs/kawai-2007-dissipation-phase-space.pdf), 4 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

For a Hamiltonian system driven between two canonical equilibrium states, the average dissipated work equals $kT$ times the relative entropy between the phase-space densities of the forward and time-reversed protocols, taken at the same intermediate time.

## Problem & setting

The system is isolated during the protocol and starts in canonical equilibrium at temperature $T$. A control parameter is varied by an external agent, and the time-reversed protocol starts from equilibrium at the final parameter value. The question is an exact microscopic expression for dissipation, which depends on the protocol and can be far from the quasi-static limit.

## Method

The derivation refines the Jarzynski-Crooks work theorem, using the one-to-one correspondence between a forward phase-space trajectory and its time-reversed partner and conservation of total energy to write the work along a trajectory through a given phase point.

## Key results

The authors state the identity $\langle W_{\mathrm{diss}}\rangle=\langle W\rangle-\Delta F=kT\,D(\rho\Vert\tilde\rho)$, valid at any intermediate time, and say it implies inequalities tighter than the second law that include the Landauer principle as a special case.

## Relevance to this research

The manuscript cites the result in its discussion of thermodynamic cost, noting that it concerns a Hamiltonian system between two equilibrium states and is not a statement about stationary path laws. The manuscript uses path relative entropy as a property of the path law and does not adopt the physical identification without a bath premise. See [[Stochastic Thermodynamics]], [[Nonequilibrium steady state]] and [[Data processing inequality]].

## Cross-links

[[Collective agents literature map]]; [[Stochastic Thermodynamics]]; [[Nonequilibrium steady state]].

## BibTeX

```bibtex
@article{kawai2007dissipation,
  author  = {Kawai, R. and Parrondo, J. M. R. and Van den Broeck, C.},
  title   = {Dissipation: The Phase-Space Perspective},
  journal = {Physical Review Letters},
  volume  = {98},
  pages   = {080602},
  year    = {2007},
  doi     = {10.1103/PhysRevLett.98.080602},
  eprint  = {cond-mat/0701397},
  archiveprefix = {arXiv}
}
```
