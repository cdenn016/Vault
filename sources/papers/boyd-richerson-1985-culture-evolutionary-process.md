---
type: reference
title: "Culture and the Evolutionary Process"
aliases: ["Boyd & Richerson 1985", "Dual-inheritance theory (Boyd & Richerson)"]
authors: ["Boyd R.", "Richerson P. J."]
year: 1985
tags: [cluster/social-physics, project/social-physics, field/biology, field/sociology, field/psychology, cluster/social-physics/evolutionary-and-cultural]
created: 2026-06-19
updated: 2026-06-19
---

# Culture and the Evolutionary Process

> [!info] Citation
> Boyd, R., & Richerson, P. J. (1985). *Culture and the Evolutionary Process*. University of Chicago Press, Chicago. ISBN 978-0-226-06933-3.

## TL;DR
The founding theoretical statement of dual-inheritance (gene–culture coevolution) theory cast in explicit recursion-equation models. Boyd and Richerson treat culture as a second inheritance system carried by socially transmitted information and ask, for each plausible psychology of social learning, what population-level dynamics it produces. Their central contribution is a taxonomy of *transmission biases* — the decision rules by which a naive learner chooses which cultural variant to adopt — and a demonstration, via formal models borrowed from quantitative population genetics, that these biases are themselves adaptive and generate distinctive macro-dynamics (cumulative adaptation, stable group differences, maladaptive runaway).

## What it establishes
The book classifies social learning into three families of bias. *Direct (content) bias*: the learner evaluates variants on their intrinsic merit and preferentially adopts the more attractive one. *Indirect (model-based) bias*: the learner copies whoever displays a marker of success or prestige rather than evaluating the trait itself. *Frequency-dependent bias*, of which the canonical case is **conformist transmission**: the probability of adopting a variant is a nonlinear, sigmoidal function of its frequency in the sampled population, so common variants are adopted at greater-than-proportional rate. If $p$ is the frequency of a variant among the $n$ models an individual samples, an unbiased (DeGroot-like) learner adopts it with probability $p$, whereas a conformist learner adopts it with probability
$$
p' = p + D\,p(1-p)(2p-1),
$$
with conformity strength $D>0$, which has unstable interior and stable fixity at $p=0,1$. This nonlinearity is what distinguishes genuine social influence from linear averaging. The biased-transmission recursions, combined with natural selection on the cultural variants and on the learning psychology itself, give a complete dynamical system for cultural change.

## Relevance to this research
The conformist / prestige / content-bias typology is exactly the menu of update rules a population-level VFE model of belief must be able to reproduce, and conformist bias in particular is the frequency-dependent nonlinearity that separates real social influence from the linear DeGroot averaging recovered in the overdamped limit of the belief-inertia functional. In the SocialPhysics program the pairwise gauge-transported coupling $\beta_{ij}\,\mathrm{KL}(q_i\,\|\,\Omega_{ij}[q_j])$ is the individual-level mechanism whose population aggregate should, under different attention/coupling kernels, generate these biases — uniform coupling giving averaging, status-weighted $\beta_{ij}$ giving prestige bias, and a majority-amplifying weighting giving the conformist sigmoid. The relevance is foundational rather than literal: this is the canonical specification of what the dynamics must reproduce, not machinery the equations import. See [[Cultural evolution and social learning]].

Concept links: [[Cultural evolution and social learning]], [[Opinion dynamics]], [[Multi-agent variational free energy]], [[Echo chambers and polarization]].

## Cross-links
- Concept: [[Cultural evolution and social learning]]
- Related sources: [[cavalli-sforza-feldman-1981-cultural-transmission]], [[richerson-boyd-2005-not-by-genes-alone]], [[henrich-boyd-1998-conformist-transmission]]

## BibTeX
```bibtex
@book{boyd1985culture,
  author    = {Boyd, Robert and Richerson, Peter J.},
  title     = {Culture and the Evolutionary Process},
  publisher = {University of Chicago Press},
  address   = {Chicago},
  year      = {1985},
  isbn      = {978-0-226-06933-3}
}
```
