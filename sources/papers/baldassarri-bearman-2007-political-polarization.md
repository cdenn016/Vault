---
type: paper
title: "Dynamics of Political Polarization"
aliases: ["Baldassarri & Bearman 2007", "Dynamics of Political Polarization"]
authors: ["Baldassarri D.", "Bearman P."]
year: 2007
url: https://doi.org/10.1177/000312240707200507
tags: [cluster/social-physics, project/social-physics, field/sociology, field/physics, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# Dynamics of Political Polarization

> [!info] Citation
> Baldassarri, D., & Bearman, P. (2007). *Dynamics of Political Polarization*. American Sociological Review 72(5):784-811. DOI: [10.1177/000312240707200507](https://doi.org/10.1177/000312240707200507).

## TL;DR
A formal agent-based model of interpersonal influence over multiple simultaneous issue positions, designed to resolve the apparent paradoxes of polarization: why aggregate attitude polarization is empirically rare even though local interaction networks become homogeneous and the population exhibits macro-level heterogeneity. By letting agents discuss several issues and selectively interact based on overall agreement, the model reproduces "takeoff" dynamics on a few salient issues, the formation of locally homogeneous discussion networks, and the coexistence of global stability with local sorting.

## What it establishes
Each agent $i$ holds a vector of issue opinions $\mathbf{x}_i\in\mathbb{R}^d$ and interacts with others with a probability that increases in their overall similarity. Interaction updates opinions toward the partner on the discussed issue, while interaction propensity is gated by agreement across the whole vector. This coupling of multi-issue opinion with similarity-biased tie selection produces three regularities simultaneously: most issues stay unpolarized, a few "take off" toward bimodality, and discussion partners grow more alike than the population at large. The model thus explains how interpersonal influence yields local homogeneity and issue-specific extremization without requiring global polarization — the "absence/presence paradox."

## Relevance to this research
This is the closest sociological precursor to the program's multi-agent dynamical framing: an explicit agent-based influence model over multi-dimensional belief vectors, exactly the structure the VFE functional generalizes when it promotes each $\mathbf{x}_i$ to a Gaussian belief $q_i=\mathcal{N}(\mu_i,\Sigma_i)$ on a statistical manifold and replaces ad hoc similarity gating with attention-weighted gauge-transported KL coupling $\beta_{ij}\,\mathrm{KL}(q_i\,\|\,\Omega_{ij}[q_j])$. Its central quantitative target — local network homogeneity coexisting with limited global polarization on most issues — is a non-trivial pattern the VFE flow should be shown to reproduce. Strong: it is the substantive opinion-dynamics model the program subsumes, not just thematic context.

## Cross-links
- Concept: [[Opinion dynamics]]
- Related: [[Multi-agent variational free energy]], [[Echo chambers and polarization]], [[Sociophysics]]
- Related sources: [[dimaggio-evans-bryson-1996-attitude-polarization]], [[sunstein-2002-law-of-group-polarization]], [[conover-2011-political-polarization-twitter]]

## BibTeX
```bibtex
@article{baldassarri2007dynamics,
  author  = {Baldassarri, Delia and Bearman, Peter},
  title   = {Dynamics of Political Polarization},
  journal = {American Sociological Review},
  volume  = {72},
  number  = {5},
  pages   = {784--811},
  year    = {2007},
  doi     = {10.1177/000312240707200507}
}
```
