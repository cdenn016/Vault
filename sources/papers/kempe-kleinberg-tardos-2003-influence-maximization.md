---
type: inproceedings
title: "Maximizing the Spread of Influence through a Social Network"
aliases: ["Kempe, Kleinberg & Tardos 2003", "Influence maximization"]
authors: ["Kempe D.", "Kleinberg J.", "Tardos E."]
year: 2003
url: https://doi.org/10.1145/956750.956769
tags: [cluster/social-physics, project/social-physics, field/cs-ml, field/sociology, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# Maximizing the Spread of Influence through a Social Network

> [!info] Citation
> Kempe, D., Kleinberg, J., & Tardos, E. (2003). *Maximizing the Spread of Influence through a Social Network*. In Proc. 9th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD '03), 137-146. doi:10.1145/956750.956769.

## TL;DR
Kempe, Kleinberg, and Tardos formalize *influence maximization*: given a diffusion model on a social network and a budget $k$, choose the $k$ seed nodes whose activation maximizes the expected number of eventually-activated nodes. They unify the two dominant operational diffusion models — the Linear Threshold model and the Independent Cascade model — show that under both the expected spread $\sigma(S)$ is a *monotone submodular* set function, and exploit submodularity to prove that the natural greedy algorithm gives a $(1 - 1/e - \varepsilon)$-approximation to the NP-hard optimum. This launched a large algorithmic literature on viral marketing and seeding.

## What it establishes
The core technical result rests on the *triggering-set* equivalence between threshold and cascade dynamics, which lets the expected spread be written as an expectation over reachability in random "live-edge" subgraphs. Because reachability is monotone and submodular and expectation preserves both properties, $\sigma$ is monotone submodular with $\sigma(\emptyset) = 0$. The Nemhauser-Wolsey-Fisher theorem then guarantees that greedily adding the node with the largest marginal gain achieves
$$\sigma(S_{\text{greedy}}) \ge \left(1 - \frac{1}{e}\right)\sigma(S^{*}),$$
within $\varepsilon$ given Monte-Carlo estimation of the marginals. The paper also proves the underlying problem NP-hard, so the constant-factor guarantee is essentially the best one can hope for efficiently.

## Relevance to this research
Influence maximization connects influence-graph topology to *which* seed agents most efficiently steer collective belief — an algorithmic counterpart to the question of which agents dominate consensus formation in the VFE dynamics, and a tool for designing interventions on the coupling graph. The Linear Threshold and Independent Cascade models it formalizes are the diffusion primitives underneath the threshold/contagion line of this batch. The relevance is adjacent algorithmic context: it concerns optimal seeding on a fixed graph rather than the belief-inertia equations of motion or the gauge transport. See [[Network structure — small-world and scale-free]], [[Threshold models and complex contagion]], and [[Opinion dynamics]].

## Cross-links
- Concept: [[Network structure — small-world and scale-free]]
- Related sources: [[watts-2002-global-cascades]], [[granovetter-1978-threshold-models]], [[centola-macy-2007-complex-contagion]]

## BibTeX
```bibtex
@inproceedings{kempe2003influence,
  author    = {Kempe, David and Kleinberg, Jon and Tardos, {\'E}va},
  title     = {Maximizing the Spread of Influence through a Social Network},
  booktitle = {Proceedings of the 9th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD '03)},
  year      = {2003},
  pages     = {137--146},
  doi       = {10.1145/956750.956769}
}
```
