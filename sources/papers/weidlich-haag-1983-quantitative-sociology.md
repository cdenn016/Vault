---
type: reference
title: "Concepts and Models of a Quantitative Sociology: The Dynamics of Interacting Populations"
aliases: ["Weidlich & Haag 1983", "Concepts and Models of a Quantitative Sociology"]
authors: ["Weidlich W.", "Haag G."]
year: 1983
url: https://doi.org/10.1007/978-3-642-81789-2
tags: [cluster/social-physics, project/social-physics, field/physics, field/sociology, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# Concepts and Models of a Quantitative Sociology: The Dynamics of Interacting Populations

> [!info] Citation
> Weidlich, W. & Haag, G. (1983). *Concepts and Models of a Quantitative Sociology: The Dynamics of Interacting Populations*. Springer Series in Synergetics, Vol. 14. DOI: [10.1007/978-3-642-81789-2](https://doi.org/10.1007/978-3-642-81789-2).

## TL;DR
The founding monograph of quantitative sociology, predating and providing the detailed machinery later summarized in Weidlich's 1991 *Physics Reports* review. It models opinion and attitude change in interacting populations by partitioning agents among discrete attitudes, defining individual probabilistic transition rates between attitudes (driven by trend parameters and pairwise coupling), and writing the master equation for the probability distribution over the resulting population configuration. Drift and diffusion approximations reduce this to Fokker-Planck and deterministic mean-value equations, and the worked models exhibit order-disorder transitions directly analogous to ferromagnetism.

## What it establishes
For a population distributed over attitudes with configuration $\mathbf{n}=(n_+, n_-)$ (e.g. two opposing opinions), individual switching rates $w_{\pm\mp}$ depend on a preference parameter $\delta$ and a coupling $\kappa$ measuring conformity pressure. The configuration probability $P(\mathbf{n},t)$ obeys the master equation, and the mean opinion fraction $x = (n_+ - n_-)/N$ satisfies a deterministic equation of motion of the schematic mean-field form
$$ \dot{x} = -\,\partial_x V(x), \qquad V(x) \sim -\tfrac{\kappa}{2}\,x^2 + \ldots, $$
with an effective potential $V$ whose shape changes from single-well (consensus impossible, disordered coexistence) to double-well (two stable polarized states) as the coupling $\kappa$ crosses a critical value — the social analogue of the magnetic order-disorder transition with $x$ as the order parameter. Fluctuations around these states are captured by the Fokker-Planck reduction.

## Relevance to this research
This is the original detailed master-equation source — transition rates, configuration space, Fokker-Planck reduction — whose moves the program's thermodynamic-limit and [[Meta-entropy]] arguments echo when they pass from a finite belief population to a continuum description. The explicit **opinion-as-Ising-spin** mapping, with a conformity coupling driving a single-well-to-double-well bifurcation of an order parameter, is the deep statistical-mechanics ancestor of the gauge-VFE consensus/polarization phase structure: the program's attention coupling $\beta_{ij}$ plays the role of Weidlich and Haag's $\kappa$, and the consensus-versus-polarization split is their order-disorder transition in modern dress. Honestly this is genealogy, not shared machinery: the state space is discrete attitude counts and the coupling is a scalar conformity pressure, with no Gaussian beliefs, no gauge transport, and no inertial second-order dynamics. It is the primary-source root that Weidlich (1991) reviews and that the program inherits conceptually.

## Cross-links
- Concept: [[Sociodynamics and synergetics]]
- Related sources: [[weidlich-1991-physics-social-science]], [[helbing-2010-quantitative-sociodynamics]]

## BibTeX
```bibtex
@book{weidlich1983concepts,
  author    = {Weidlich, Wolfgang and Haag, G\"{u}nter},
  title     = {Concepts and Models of a Quantitative Sociology: The Dynamics of Interacting Populations},
  series    = {Springer Series in Synergetics},
  volume    = {14},
  publisher = {Springer},
  year      = {1983},
  doi       = {10.1007/978-3-642-81789-2}
}
```
