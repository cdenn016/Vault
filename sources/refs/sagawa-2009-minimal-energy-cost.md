---
type: reference
title: "Minimal Energy Cost for Thermodynamic Information Processing: Measurement and Information Erasure"
aliases: ["sagawa2009minimal"]
authors: ["Takahiro Sagawa", "Masahito Ueda"]
year: 2009
venue: "Physical Review Letters"
doi: "10.1103/PhysRevLett.102.250602"
arxiv: "0809.4098"
url: "https://doi.org/10.1103/PhysRevLett.102.250602"
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/physics]
created: 2026-11-10
updated: 2026-11-10
---

# Minimal Energy Cost for Thermodynamic Information Processing: Measurement and Information Erasure

> [!info] Citation
> Sagawa, T., Ueda, M. (2009). *Minimal Energy Cost for Thermodynamic Information Processing: Measurement and Information Erasure*. Physical Review Letters, 102, 250602. [DOI](https://doi.org/10.1103/PhysRevLett.102.250602), [arXiv](https://arxiv.org/abs/0809.4098)

[Local PDF](../pdfs/sagawa-2009-minimal-energy-cost.pdf), 5 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages and manuscript reading record.

## TL;DR

The Letter derives lower bounds on the work needed to measure and to erase information in a memory in contact with a heat bath, and calls the result a second law of information thermodynamics.

## Problem & setting

A memory stores the outcome of a measurement on a thermodynamic system through an isothermal process at temperature $T$. Outcomes label mutually orthogonal subspaces of the memory's Hilbert space, the memory starts in a canonical state with the standard outcome, and it is in contact with a bath. The formulation is quantum but valid in the classical limit. Results are proved rigorously for classical information processing and, for the quantum case, after an additional assumption.

## Method

The bounds follow from the stated measurement and erasure protocol with the memory and bath. The first pages read do not reach the derivation.

## Key results

The abstract states lower bounds on the energy cost of measurement and of erasure. The erasure bound validates Landauer's principle for a symmetric memory and indicates its breakdown in other cases. The manuscript's reading record adds that separate bounds hold for measurement and erasure, and that their sum for an isothermal memory is bounded below by $k_{\mathrm B}T$ times the acquired mutual information.

## Relevance to this research

The manuscript takes the bound on total measurement-plus-erasure work as a stated premise in its thermodynamic cost accounting of a communication register. It records that the hypotheses of the source, a memory with finitely many outcomes, were not checked against registers holding real-valued Gaussian readings. See [[Stochastic Thermodynamics]], [[Information is Physical]] and [[Mutual information]].

## Cross-links

[[Collective agents literature map]]; [[Stochastic Thermodynamics]]; [[Information is Physical]]; [[Mutual information]]; [[roldan-2010-estimating-dissipation-single]].

## BibTeX

```bibtex
@article{sagawa2009minimal,
  author  = {Sagawa, Takahiro and Ueda, Masahito},
  title   = {Minimal Energy Cost for Thermodynamic Information Processing: Measurement and Information Erasure},
  journal = {Physical Review Letters},
  volume  = {102},
  pages   = {250602},
  year    = {2009},
  doi     = {10.1103/PhysRevLett.102.250602},
  eprint  = {0809.4098},
  archiveprefix = {arXiv}
}
```
