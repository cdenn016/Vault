---
type: paper
title: "Analytic and Clustering Properties of Thermodynamic Functions and Distribution Functions for Classical Lattice and Continuum Systems"
aliases: ["Lebowitz and Penrose 1968", "Lebowitz-Penrose analyticity"]
authors: ["J. L. Lebowitz", "O. Penrose"]
year: 1968
arxiv:
url: "https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-11/issue-2/Analytic-and-clustering-properties-of-thermodynamic-functions-and-distribution-functions/cmp/1103841197.full"
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/physics, field/mathematics]
created: 2026-10-12
---

# Analytic and Clustering Properties of Thermodynamic Functions and Distribution Functions for Classical Lattice and Continuum Systems

> [!info] Citation
> Lebowitz, J. L. and Penrose, O. (1968). *Analytic and clustering properties of thermodynamic functions and distribution functions for classical lattice and continuum systems*. Communications in Mathematical Physics 11(2), 99–124. doi:10.1007/BF01645899. Free copy on Project Euclid (cmp/1103841197); local PDF `sources/pdfs/LebowitzPenrose1968.pdf` (2,357,211 bytes, SHA-256 `fe979d3cfccec13919d3bc58a1e573f6e37eafc92ee7daf94ab25c4f0fb019bd`, not tracked in Git). Read on October 12, 2026 from the PDF's text layer: the abstract, Sections I to IV in full (pp. 99–109), and the opening of Section V.

## TL;DR

For the Ising spin system with purely ferromagnetic pair interactions in a field $H$ (equivalently a lattice gas with attractive interactions), the infinite-volume free energy per site and the distribution functions are analytic in the two variables $\beta$ and $H$ jointly whenever $\beta>0$ and $H$ is not a limit point of zeros of the grand partition function, which by the Lee–Yang circle theorem holds whenever $\operatorname{Re}H\neq0$. In the authors' words for the pressure (end of Section IV, p. 109), for an Ising ferromagnet "a sufficient condition is simply that the magnetic field should not vanish". Ursell functions decay exponentially in the separation when $\operatorname{Re}H\neq0$ and the interaction has finite range.

## Problem & setting

Mayer and Ruelle had shown analyticity of the pressure and distribution functions in the fugacity $z$ (and in $\beta$ jointly) inside a small-fugacity disk. Lee and Yang showed that for the Ising ferromagnet the zeros of the partition function in the variable $\zeta=e^{-2mH\beta}$ lie on the unit circle, which gives analyticity in $H$ at fixed $\beta$ away from $H=0$. Analyticity in $z$ at fixed real $\beta$ does not by itself give joint analyticity; the paper's example on p. 101 is a series analytic in $z$ for real $\beta$ whose sum is not analytic in $\beta$. The interaction is a two-body potential satisfying Ruelle's stability and regularity conditions; the infinite-volume limit lets the boundary recede to infinity.

## Method

The core is a lemma in Section III (pp. 104–107): if $F(\beta,z)$ is jointly analytic near $S\times C$ (a complex neighborhood of an interval $I$ times a small disk $C$, from the Mayer expansion), analytic in $z$ on a closed region $K$ for each fixed real $\beta\in I$, and uniformly bounded on $I\times K$, then $F$ is jointly analytic on $I\times K^\circ$. Section IV applies it to $F=\exp(\beta p(\beta,z))$ under condition (36): a bounded simply connected region $J$ containing $0$ and $z_0$ whose closed subregions are free of zeros of the grand partition function for all large volumes and all $\beta\in I$. For the ferromagnet, Lee–Yang supplies $J$ as the open unit disk in $\zeta$ (and $|\zeta|>1$ by field reversal), and the bound (40) gives condition (23).

## Key results

Section IV: $p(\beta,z)$ is jointly analytic wherever (36) holds; for the Ising ferromagnet this means for every $\beta>0$ and every nonzero real field, and the energy and specific heat per unit volume are analytic under the same conditions. Sections V and VI extend joint analyticity to the distribution functions (for the ferromagnet and for nonnegative potentials below the Mayer radius); Sections VII and VIII give clustering of Ursell functions, with $|u_s|\le C\exp[(-2\beta m|\operatorname{Re}H|+\varepsilon)\Lambda_s/\lambda]$ for interactions of range $\lambda$. A phase transition as $\beta$ varies at fixed $H$ can occur only at a limit point of Lee–Yang zeros, hence only at $\operatorname{Re}H=0$.

## Relevance to this research

The October 12 review of the MultiAgentELBO theory found that the native free model of Supplement B (`def:rg-pressure-native`) is exactly a nearest-neighbor ferromagnetic Ising model on the $(L-1)\times(L-1)$ plaquette grid, with coupling $\tfrac12\log(1/b)$ and fields $\tfrac12\log t+\tfrac n2\log b$, which are negative for $0<b,t<1$ ([[multiagentelbo-2026-10-12-theory-review-remediation]], `rem:rg-pressure-native-ising`). The bulk field is therefore nonzero on all of $(0,1)^2$, and since $(b,t)\mapsto$ (coupling, bulk field) is a real-analytic diffeomorphism onto an open subset of (positive coupling, negative field), while the paper's variables $(\beta,H)$ for a fixed coupling shape reach every such pair through $(\beta J_0,\beta H)$, this paper's Section IV gives real-analyticity of the native infinite-volume pressure in $(b,t)$ on the whole square, not only on the domain $12t<1$ where Supplement B proves $C^4$. The remark currently claims no analyticity consequence, because this paper had not been read. Before the manuscript cites it, two hypotheses need a line of argument: that the native pressure differs from the Ising pressure only by real-analytic terms in $(b,t)$, and that the site-dependent boundary fields (the $n$ in the field) do not affect the bulk limit, which is the boundary point the authors flag on p. 108. The paper bears on the B = 1 thermodynamic Fisher statements of Supplement B, whose Fisher metric is the Hessian of the pressure ([[Renormalization group flow]]).

## Cross-links
- Concepts: [[Renormalization group flow]], [[Fisher information metric]]
- Related sources: [[multiagentelbo-2026-10-12-theory-review-remediation]]

## BibTeX
```bibtex
@article{LebowitzPenrose1968,
  author  = {Lebowitz, Joel L. and Penrose, Oliver},
  title   = {Analytic and clustering properties of thermodynamic functions and distribution functions for classical lattice and continuum systems},
  journal = {Communications in Mathematical Physics},
  volume  = {11},
  number  = {2},
  pages   = {99--124},
  year    = {1968},
  doi     = {10.1007/BF01645899}
}
```
