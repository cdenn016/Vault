---
type: reference
title: "Cultural Transmission and Evolution: A Quantitative Approach"
aliases: ["Cavalli-Sforza & Feldman 1981", "Quantitative theory of cultural transmission"]
authors: ["Cavalli-Sforza L. L.", "Feldman M. W."]
year: 1981
tags: [cluster/social-physics, project/social-physics, field/biology, field/mathematics, field/sociology, cluster/social-physics/evolutionary-and-cultural]
created: 2026-06-19
updated: 2026-06-19
---

# Cultural Transmission and Evolution: A Quantitative Approach

> [!info] Citation
> Cavalli-Sforza, L. L., & Feldman, M. W. (1981). *Cultural Transmission and Evolution: A Quantitative Approach*. Monographs in Population Biology 16, Princeton University Press, Princeton. ISBN 978-0-691-08283-7.

## TL;DR
The founding mathematical theory of cultural transmission. Cavalli-Sforza and Feldman import the formal machinery of population genetics — mutation, selection, migration, and drift — and reinterpret each force as a mode of cultural change, building explicit dynamical models for how a measurable cultural trait spreads through a population over time. By distinguishing the *channels* of transmission (vertical from parents, horizontal among peers, oblique from unrelated elders), they show that the route information takes through a population, not just the trait's content, controls its rate and pattern of diffusion.

## What it establishes
The book formalizes cultural change as a transmission process acting on trait frequencies. For a continuous trait, an offspring value is modeled as a weighted combination of the values of its cultural parents plus noise; for a dichotomous trait with frequency $p_t$, vertical and oblique transmission give linear recursions of the form
$$
p_{t+1} = a\,p_t + b,
$$
whose fixed point and rate of approach depend on the transmission coefficients, while horizontal (contagion-like) transmission yields logistic spread. The authors derive the variance dynamics under blending, the conditions under which a trait reaches fixation or stable polymorphism, and the much slower equilibration of culture relative to biological inheritance because each individual draws on many cultural parents. They give one of the first quantitative accounts of cultural drift and of the interaction between selection on traits and the demographic structure of transmission.

## Relevance to this research
This is the original quantitative-dynamics treatment of belief and trait spread across a population, and it is the direct ancestor of the overdamped opinion-dynamics models the belief-inertia manuscript claims to recover as limiting cases. Its linear blending recursion $p_{t+1}=a p_t + b$ is structurally the population-level analogue of Friedkin–Johnsen averaging, and its transmission operators are precisely the population limit that the pairwise VFE coupling $\mathrm{KL}(q_i\,\|\,\Omega_{ij}[q_j])$ instantiates at the level of individual Gaussian beliefs. The vertical/horizontal/oblique distinction maps onto the structure of the coupling graph and attention kernel in the multi-agent functional. This is genuine machinery-level lineage for the overdamped claim, though the original models are scalar-trait and noise-free whereas the VFE beliefs carry covariance and gauge frames. See [[Cultural evolution and social learning]].

Concept links: [[Cultural evolution and social learning]], [[Opinion dynamics]], [[Multi-agent variational free energy]], [[Renormalization-group flow of beliefs]].

## Cross-links
- Concept: [[Cultural evolution and social learning]]
- Related sources: [[boyd-richerson-1985-culture-evolutionary-process]], [[henrich-boyd-2002-modeling-cognition-culture]], [[mesoudi-2011-cultural-evolution]]

## BibTeX
```bibtex
@book{cavallisforza1981cultural,
  author    = {Cavalli-Sforza, L. L. and Feldman, M. W.},
  title     = {Cultural Transmission and Evolution: A Quantitative Approach},
  series    = {Monographs in Population Biology},
  number    = {16},
  publisher = {Princeton University Press},
  address   = {Princeton},
  year      = {1981},
  isbn      = {978-0-691-08283-7}
}
```
