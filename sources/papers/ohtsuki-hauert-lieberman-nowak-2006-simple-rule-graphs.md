---
type: paper
title: "A Simple Rule for the Evolution of Cooperation on Graphs and Social Networks"
aliases: ["Ohtsuki et al. 2006", "b/c > k rule for cooperation"]
authors: ["Ohtsuki H.", "Hauert C.", "Lieberman E.", "Nowak M. A."]
year: 2006
url: https://doi.org/10.1038/nature04605
tags: [cluster/social-physics, project/social-physics, field/biology, field/mathematics, field/physics, cluster/social-physics/evolutionary-and-cultural]
created: 2026-06-19
updated: 2026-06-19
---

# A Simple Rule for the Evolution of Cooperation on Graphs and Social Networks

> [!info] Citation
> Ohtsuki, H., Hauert, C., Lieberman, E., & Nowak, M. A. (2006). *A Simple Rule for the Evolution of Cooperation on Graphs and Social Networks*. Nature 441(7092):502–505. DOI: [10.1038/nature04605](https://doi.org/10.1038/nature04605).

## TL;DR
This paper derives a remarkably simple closed-form condition for when natural selection favors cooperation in a graph-structured population. Studying the prisoner's dilemma (benefit $b$, cost $c$) on a regular graph of degree $k$ under standard update rules, the authors show via pair-approximation and exact simulation that cooperators are favored over defectors when the benefit-to-cost ratio exceeds the average number of neighbors. This unifies the inclusive-fitness (kin-selection) and evolutionary-graph-theory traditions: network reciprocity is shown to obey a Hamilton-rule-like inequality in which the graph degree plays the role of an inverse relatedness.

## What it establishes
The central result is the condition
$$\frac{b}{c} > k,$$
where $b$ is the benefit a cooperator confers on a neighbor, $c$ is the cost of cooperating, and $k$ is the (average) degree of the interaction graph, valid for $k \ll N$ under death-birth updating. Sparser, more locally clustered graphs (small $k$) make cooperation easier; dense, well-mixed graphs (large $k$) make it harder, recovering the no-cooperation result of the mean-field limit. The rule provides an analytic bridge between network topology and the viability of cooperative outcomes.

## Relevance to this research
This provides a closed-form structural condition ($b/c > k$) linking network connectivity to the viability of cooperation — exactly the kind of analytic structure-to-outcome map the program seeks for belief coupling on its agent graph. It is a strong, concretely citable result tying graph degree to collective cooperative outcomes: the program's coupling weights and graph degree play an analogous role in deciding whether locally coupled agents drift toward shared (cooperative/consensual) configurations or fragment. The dynamics are death-birth strategy updates rather than VFE flow, so the result is a structural template the program can aspire to derive in its own setting rather than a shared equation. See [[Evolutionary game theory and cooperation]], [[Community detection and modularity]], and [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Evolutionary game theory and cooperation]]
- Related sources: [[lieberman-hauert-nowak-2005-evolutionary-dynamics-on-graphs]], [[nowak-2006-five-rules-cooperation]], [[santos-pacheco-2005-scale-free-cooperation]]

## BibTeX
```bibtex
@article{ohtsuki2006simple,
  author  = {Ohtsuki, Hisashi and Hauert, Christoph and Lieberman, Erez and Nowak, Martin A.},
  title   = {A Simple Rule for the Evolution of Cooperation on Graphs and Social Networks},
  journal = {Nature},
  volume  = {441},
  number  = {7092},
  pages   = {502--505},
  year    = {2006},
  doi     = {10.1038/nature04605}
}
```
