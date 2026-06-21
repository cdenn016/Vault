---
type: paper
title: "Topological synchronization of chaotic systems"
aliases:
  - "Lahav 2022"
  - "Topological Synchronization"
authors:
  - Lahav, Nir
  - Sendiña-Nadal, Irene
  - Hens, Chittaranjan
  - Ksherim, Baruch
  - Barzel, Baruch
  - Cohen, Reuven
  - Boccaletti, Stefano
year: 2022
arxiv: null
url: https://doi.org/10.1038/s41598-022-06262-z
tags:
  - cluster/social-physics/networks-and-contagion
  - project/social-physics
  - field/physics
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Topological synchronization of chaotic systems

> [!info] Citation
> Lahav, N., Sendiña-Nadal, I., Hens, C., Ksherim, B., Barzel, B., Cohen, R., & Boccaletti, S. (2022). "Topological synchronization of chaotic systems." *Scientific Reports* 12, 2508. https://doi.org/10.1038/s41598-022-06262-z

## TL;DR
This paper introduces topological synchronization as a microscopic, topology-level description of chaotic synchronization, shifting the descriptive level from Lyapunov spectra (macroscopic) to the multifractal structure of strange attractors. The central finding is a universal "zipper effect": as coupling strength increases between mismatched chaotic oscillators, topological synchronization initiates in the sparse (low-probability) regions of the attractor — captured by negative-$q$ generalized dimensions $D_q$ — and progressively zips toward the dense regions (positive $q$) until complete synchronization is achieved. This zipper effect is demonstrated to be a robust trait of chaotic synchronization across continuous systems (Rössler), discrete maps (logistic), high-mismatch class III systems, and high-dimensional systems (Mackey–Glass delay equations).

## Problem & setting
Classical characterizations of chaotic synchronization rely on macroscopic indicators such as the Lyapunov exponent spectrum, or on mesoscopic unstable periodic orbit analysis. These descriptions miss the continuous, gradual, microscopic process by which two strange attractors align their topological structure. The paper addresses this gap by asking: what is the microscopic geometry of the transition from non-synchrony to complete synchrony in coupled chaotic systems?

Prior work (Lahav et al., Phys. Rev. E 98, 052204, 2018) introduced topological synchronization for standard attractors; the present paper extends this to the full multifractal regime using Rényi generalized dimensions.

## Method
The central mathematical tool is the Rényi generalized dimension,

$$D_q = \lim_{l \to 0} \frac{1}{q-1} \frac{\ln\!\left(\sum_i p_i^q\right)}{\ln(1/l)},$$

where $p_i$ is the probability of a trajectory point falling in sphere $i$ of radius $l$, and $q \in \mathbb{R}$ parametrizes which scaling laws are probed: $D_0$ is the box-counting (Hausdorff) dimension, $D_1$ the information dimension, $D_2$ the correlation dimension; $D_{-\infty}$ isolates rare sparse-attractor scaling laws (low occupation probability) and $D_{+\infty}$ isolates rare dense-attractor laws (high occupation probability).

Topological synchronization is declared complete when

$$\Delta D_q = \sup_q \left|D_q^{(1)} - D_q^{(2)}\right| \to 0.$$

Master–slave configurations of Rössler oscillators (slightly and highly mismatched), logistic maps, and Mackey–Glass delay equations are studied by computing $D_q(q)$ curves as a function of coupling strength and monitoring their convergence.

## Key results
Across all studied systems, topological synchronization exhibits the same zipper effect: synchronization of $D_q$ for $q \leq 0$ (sparse attractor regions) precedes and drives synchronization for $q > 0$ (dense regions). Specific quantitative milestones for the logistic map: $\Delta D_{q<0} \to 0$ at coupling $k \approx 0.33$, while $\Delta D_{q>0} \to 0$ only at $k \approx 0.9$ (full synchronization). For the high-mismatch Rössler class III system (where synchronization is confined to a finite coupling window $\sigma \in [3, 7]$), the zipper effect is approximate but present, and a reverse zipper effect appears at de-synchronization ($\sigma > 7$): dense regions desynchronize first, sparse regions last. For the infinite-dimensional Mackey–Glass system, the negative-$D_q$ part synchronizes around $\sigma \approx 0.5$ and the positive part follows to reach near-complete synchronization at $\sigma \approx 2$.

## Relevance to this research
The connection to the core VFE / GL(K) program is indirect but potentially meaningful in two directions. First, the multifractal convergence framing — where two systems become informationally equivalent region by region, starting from their rarest configurations — is structurally analogous to how belief distributions $q_i$ and $q_j$ are coupled through the KL divergence terms $\beta_{ij} \operatorname{KL}(q_i \| \Omega_{ij} q_j)$ in the VFE functional: the transport $\Omega_{ij}$ aligns distributions gradually as coupling $\beta_{ij}$ increases. Second, the Rényi generalized dimension at parameter $q$ is mathematically related to Rényi divergences of order $q$, which generalize the KL divergence (order 1) used throughout the VFE framework — the $q$-parametric family of dimensions here parallels the $\alpha$-divergence family in the codebase's f-divergence registry. The zipper effect may also be relevant to multi-agent active inference: in networks of coupled agents, belief alignment might preferentially stabilize low-entropy (sparse) belief regions before high-entropy (dense) ones. The paper's treatment of synchronization in high-dimensional and high-mismatch systems offers qualitative intuition for robustness of belief coupling across heterogeneous agents.

## Cross-links
- Concepts: [[Chaotic Synchronization]], [[Multifractal Geometry]], [[Renyi Divergence]]
- Related sources: [[lahav-2018-microscopic-sync]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{LahavTopologicalSync2022,
  author  = {Lahav, Nir and Sendiña-Nadal, Irene and Hens, Chittaranjan and Ksherim, Baruch and Barzel, Baruch and Cohen, Reuven and Boccaletti, Stefano},
  title   = {Topological synchronization of chaotic systems},
  journal = {Scientific Reports},
  volume  = {12},
  pages   = {2508},
  year    = {2022},
  doi     = {10.1038/s41598-022-06262-z},
}
```
