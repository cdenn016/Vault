---
type: paper
title: "Cognitive Culture: Theoretical and Empirical Insights into Social Learning Strategies"
aliases: ["Rendell et al. 2011", "Cognitive culture review"]
authors: ["Rendell L.", "Fogarty L.", "Hoppitt W. J. E.", "Morgan T. J. H.", "Webster M. M.", "Laland K. N."]
year: 2011
url: https://doi.org/10.1016/j.tics.2010.12.002
tags: [cluster/social-physics, project/social-physics, field/psychology, field/biology, cluster/social-physics/evolutionary-and-cultural]
created: 2026-06-19
updated: 2026-06-19
---

# Cognitive Culture: Theoretical and Empirical Insights into Social Learning Strategies

> [!info] Citation
> Rendell, L., Fogarty, L., Hoppitt, W. J. E., Morgan, T. J. H., Webster, M. M., & Laland, K. N. (2011). "Cognitive culture: Theoretical and empirical insights into social learning strategies." *Trends in Cognitive Sciences* **15**(2), 68–76. DOI: [10.1016/j.tics.2010.12.002](https://doi.org/10.1016/j.tics.2010.12.002).

## TL;DR
A review that places social-learning strategies within a cognitive, decision-theoretic framework and synthesizes the model predictions of cultural-evolution theory with the accumulating experimental evidence from humans and other animals. The authors organize the literature around the now-standard "when" (e.g., copy-when-uncertain, copy-when-asocial-learning-is-costly, copy-when-dissatisfied) and "who" (copy-the-majority, copy-successful, copy-older/experienced) strategy questions, and assess where experiments confirm, refine, or complicate the theoretically predicted strategies.

## What it establishes
The review's contribution is integrative: it ties social-learning-strategy theory to a cost/benefit, uncertainty-driven account of when an individual should rely on social rather than asocial information, and it audits this account against controlled experiments. It documents robust support for state-dependent reliance on social information (uncertainty and the cost of individual learning reliably increase copying), partial and context-dependent support for frequency-dependent conformity, and evidence for payoff- and model-based biases, while flagging methodological gaps in isolating any single strategy. The framing treats the learner as a boundedly rational decision-maker selecting among information sources, rather than as a passive imitator.

## Relevance to this research
This is the authoritative review tying social-learning-strategy theory to decision-theoretic, uncertainty-driven accounts of when to copy — the same logic that, in the VFE setting, makes attention weights a function of relative belief precision and disagreement. The empirical regularity that uncertainty and high asocial-learning cost increase reliance on social information is direct support for treating social learning as Bayesian / precision-weighted belief updating, which is exactly the behavior the coupling term $\beta_{ij}\,\mathrm{KL}(q_i\,\|\,\Omega_{ij}[q_j])$ produces when the gain scales with the agent's own posterior uncertainty $\Sigma_i$. Strong, synthesis-level support for the program's premise that the attention kernel should be precision- and disagreement-modulated rather than fixed. See [[Cultural evolution and social learning]].

Concept links: [[Cultural evolution and social learning]], [[Multi-agent variational free energy]], [[Fisher information metric]], [[Collective active inference]].

## Cross-links
- Concept: [[Cultural evolution and social learning]]
- Related sources: [[laland-2004-social-learning-strategies]], [[rendell-2010-why-copy-others]], [[mesoudi-2011-cultural-evolution]]

## BibTeX
```bibtex
@article{rendell2011cognitive,
  author  = {Rendell, L. and Fogarty, L. and Hoppitt, W. J. E. and Morgan, T. J. H. and Webster, M. M. and Laland, K. N.},
  title   = {Cognitive culture: Theoretical and empirical insights into social learning strategies},
  journal = {Trends in Cognitive Sciences},
  volume  = {15},
  number  = {2},
  pages   = {68--76},
  year    = {2011},
  doi     = {10.1016/j.tics.2010.12.002}
}
```
