---
type: paper
title: "Social Learning Strategies"
aliases: ["Laland 2004", "Who/when/what social learning taxonomy"]
authors: ["Laland K. N."]
year: 2004
url: https://doi.org/10.3758/BF03196002
tags: [cluster/social-physics, project/social-physics, field/psychology, field/biology, cluster/social-physics/evolutionary-and-cultural]
created: 2026-06-19
updated: 2026-06-19
---

# Social Learning Strategies

> [!info] Citation
> Laland, K. N. (2004). "Social learning strategies." *Learning & Behavior* **32**(1), 4–14. DOI: [10.3758/BF03196002](https://doi.org/10.3758/BF03196002).

## TL;DR
A short, agenda-setting review arguing that social learning is not indiscriminate imitation but is governed by *strategies* — evolved, conditional rules specifying when an individual should copy others and whom it should copy. Laland organizes these rules into two questions, "when to copy" and "who to copy," and surveys the theoretical and empirical evidence for specific strategies such as copy-when-asocial-learning-is-costly, copy-when-uncertain, copy-when-dissatisfied, copy-the-majority, copy-successful-individuals, and copy-kin. The framing reorients cultural-evolution research toward the decision rules that filter social information.

## What it establishes
The paper's lasting contribution is a taxonomy of conditional copying policies rather than a single equation. Under "when," the central strategies are state- and uncertainty-dependent: an agent leans on social information when individual (asocial) learning is expensive or unreliable, when it is itself uncertain, or when its current behavior is yielding poor payoffs. Under "who," the strategies bias the *source* of information: copy the majority (frequency dependence, hence conformity), copy successful or high-payoff individuals (payoff bias), copy older or more experienced models, or copy kin. The key claim is that selectivity beats indiscriminate copying, because unconditional imitation can propagate outdated or maladaptive information; the value of social learning depends on deploying it under the right conditions and toward the right models.

## Relevance to this research
This taxonomy is the conceptual specification of the coupling/attention kernel in a multi-agent belief model: it enumerates which neighbors an agent should weight and under what precision/uncertainty conditions. The "copy-when-uncertain" strategy maps directly onto precision-weighted updating — an agent with broad covariance $\Sigma_i$ (low confidence) should place more weight on transported neighbor beliefs — which is exactly the behavior a VFE coupling $\beta_{ij}\,\mathrm{KL}(q_i\,\|\,\Omega_{ij}[q_j])$ produces when the gain is modulated by relative precision. "Copy-the-majority" supplies the conformist nonlinearity and "copy-successful" the payoff/prestige asymmetry that a heterogeneous $\beta_{ij}$ must represent. The relevance is strong and specificational: this is the menu of behaviors the attention weights and precision-weighted gain ought to recover. See [[Cultural evolution and social learning]].

Concept links: [[Cultural evolution and social learning]], [[Multi-agent variational free energy]], [[Fisher information metric]], [[Social influence and conformity]].

## Cross-links
- Concept: [[Cultural evolution and social learning]]
- Related sources: [[rendell-2010-why-copy-others]], [[rendell-2011-cognitive-culture]], [[henrich-gilwhite-2001-evolution-of-prestige]]

## BibTeX
```bibtex
@article{laland2004social,
  author  = {Laland, Kevin N.},
  title   = {Social learning strategies},
  journal = {Learning \& Behavior},
  volume  = {32},
  number  = {1},
  pages   = {4--14},
  year    = {2004},
  doi     = {10.3758/BF03196002}
}
```
