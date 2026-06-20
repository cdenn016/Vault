---
type: paper
title: "Pathological Outcomes of Observational Learning"
aliases: ["Smith & Sorensen 2000", "Pathological outcomes of observational learning"]
authors: ["Smith L.", "Sorensen P."]
year: 2000
url: https://doi.org/10.1111/1468-0262.00113
tags: [cluster/social-physics, project/social-physics, field/economics, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# Pathological Outcomes of Observational Learning

> [!info] Citation
> Smith, L., & Sorensen, P. (2000). *Pathological Outcomes of Observational Learning*. Econometrica, 68(2), 371-398. DOI: [10.1111/1468-0262.00113](https://doi.org/10.1111/1468-0262.00113).

## TL;DR
Smith and Sorensen give the rigorous, general-signal treatment of sequential observational learning that subsumes and sharpens the 1992 cascade models. By allowing **heterogeneous preferences** and **general signal distributions**, they show the standard cascade story is a special case and uncover two distinct pathologies. First, they carefully separate the notions of a **herd** (everyone eventually takes the same action) from an **informational cascade** (private signals stop affecting actions): the two coincide in the simple binary model but generally do not. Second, with heterogeneous types they exhibit **confounded learning**, where the public belief converges but to a state in which different types optimally take different actions, so the action history can no longer disentangle the truth and learning permanently stalls short of full information. They pin down exactly when society herds on the wrong action: this happens precisely when private **signals have uniformly bounded strength**, whereas unbounded (arbitrarily informative) signals guarantee eventual correct learning.

## What it establishes
The framework is a sequential Bayesian game with a continuum of possible private beliefs. The decisive condition is the **boundedness of beliefs**:

$$\text{bounded private signals} \;\Rightarrow\; \text{positive-probability wrong herd}, \qquad \text{unbounded signals} \;\Rightarrow\; \text{asymptotic correct learning}.$$

With bounded signals there always exists a threshold of public confidence beyond which no admissible private signal can overturn the herd, so society can lock onto the wrong action forever; with unbounded signals, arbitrarily strong contrarian signals keep arriving and eventually correct any wrong herd. The **herd vs. cascade** decoupling shows actions can converge while beliefs still move (a herd without a cascade) and that the cascade concept is the special degenerate limit. **Confounded learning** with heterogeneous preferences is the most striking pathology: the social belief settles at a point where the mixed actions of different types are uninformative, freezing aggregation. These results are the definitive characterization of *when and how* social learning fails.

## Relevance to this research
This paper sharpens cascade theory into a precise statement of *when* social learning stalls or converges to the wrong consensus, which is the rigorous form of the failure mode the program's self-coupling $\alpha$ (signal strength) is meant to guard against — making it a strong, theoretically deep reference. Smith and Sorensen's bounded-versus-unbounded-signal dichotomy maps onto the relative weight of the self-coupling term $\alpha\,\mathrm{KL}(q_i\|p_i)$ against the neighbor-coupling term in the VFE functional: "bounded signal strength" is the regime where each agent's own evidence (carried by $\alpha$ and the likelihood) can be permanently outvoted by the transported neighbor consensus, so the population can lock onto a wrong attractor, exactly the wrong-herd pathology. Their herd/cascade distinction is also a useful conceptual discipline for the program, which should be careful to distinguish "all beliefs converge" (a herd) from "self-evidence stops mattering" (a cascade). The correspondence is structural and benchmark-level, not an identity: their model is one-shot Bayesian and discrete-action, the program's is continuous variational flow.

See [[Information cascades and herding]], [[Multi-agent variational free energy]], [[Belief inertia]], [[Opinion dynamics]].

## Cross-links
- Concept: [[Information cascades and herding]]
- Related sources: [[banerjee-1992-herd-behavior]], [[bikhchandani-hirshleifer-welch-1992-informational-cascades]], [[acemoglu-dahleh-lobel-ozdaglar-2011-bayesian-learning-networks]]

## BibTeX
```bibtex
@article{smith2000pathological,
  author  = {Smith, Lones and Sorensen, Peter},
  title   = {Pathological Outcomes of Observational Learning},
  journal = {Econometrica},
  year    = {2000},
  volume  = {68},
  number  = {2},
  pages   = {371--398},
  doi     = {10.1111/1468-0262.00113}
}
```
