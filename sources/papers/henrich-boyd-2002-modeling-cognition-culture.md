---
type: paper
title: "On Modeling Cognition and Culture: Why Cultural Evolution Does Not Require Replication of Representations"
aliases: ["Henrich & Boyd 2002", "Attractors and replication of representations"]
authors: ["Henrich J.", "Boyd R."]
year: 2002
url: https://doi.org/10.1163/156853702320281836
tags: [cluster/social-physics, cluster/vfe, project/social-physics, field/biology, field/psychology, cluster/social-physics/evolutionary-and-cultural]
created: 2026-06-19
updated: 2026-06-19
---

# On Modeling Cognition and Culture: Why Cultural Evolution Does Not Require Replication of Representations

> [!info] Citation
> Henrich, J., & Boyd, R. (2002). "On modeling cognition and culture: Why cultural evolution does not require replication of representations." *Journal of Cognition and Culture* **2**(2), 87–112. DOI: [10.1163/156853702320281836](https://doi.org/10.1163/156853702320281836).

## TL;DR
A formal reconciliation of the selectionist (Boyd–Richerson, Cavalli-Sforza–Feldman) and cultural-attraction (Sperber) accounts of cultural evolution. Henrich and Boyd show with an explicit model that faithful copying of mental representations is *not* required for stable, cumulative culture: even when individual transmission is low-fidelity and learners reconstruct rather than replicate, population-level cultural traditions persist because inductive biases ("attractors") pull each reconstruction toward shared cognitive targets. The two frameworks are therefore complementary rather than opposed, differing in the relative strength of selective transmission versus reconstructive attraction.

## What it establishes
The model represents a cultural variant as a continuous value that each learner infers from a noisy observation of a model plus the pull of a cognitive attractor. With weak attractors, transmission-and-selection forces dominate and the standard biased-transmission dynamics apply; with *strong* attractors, the reconstruction step dominates and the population concentrates on the attractor regardless of what was observed. The decisive formal result is a limit: as attractor strength grows, the continuous-representation model *reduces to a discrete replicator model* in which a small number of attractor states behave like faithfully replicated discrete variants. Thus discrete "memes" can be an emergent description of an underlying continuous, reconstructive, attractor-biased process — cultural inertia at the population level survives arbitrarily lossy copying at the individual level.

## Relevance to this research
This is the cleanest formal bridge in the batch to the VFE belief-recreation picture: beliefs are reconstructed each transmission step under attractors (priors), not copied verbatim, which is exactly how the gauge-theoretic functional treats an agent's posterior — pulled toward a prior attractor during free-energy minimization rather than transmitted intact. The reduction-to-replicator-under-strong-attractors result is a direct analog of how strong prior coupling (large $\alpha$ in the self-coupling term $\alpha\,\mathrm{KL}(q_i\,\|\,p_i)$) collapses the continuous belief dynamics toward a small set of fixed attractor states, recovering discrete consensus from continuous Gaussian beliefs. This is strong, machinery-level relevance to the belief-inertia premise and to why the program flags both an overdamped (selection-dominated) and an attractor-dominated regime. See [[Belief inertia]].

Concept links: [[Belief inertia]], [[Cultural evolution and social learning]], [[Multi-agent variational free energy]], [[Renormalization-group flow of beliefs]].

## Cross-links
- Concept: [[Cultural evolution and social learning]]
- Related sources: [[sperber-1996-explaining-culture]], [[cavalli-sforza-feldman-1981-cultural-transmission]], [[henrich-boyd-1998-conformist-transmission]]

## BibTeX
```bibtex
@article{henrich2002modeling,
  author  = {Henrich, Joseph and Boyd, Robert},
  title   = {On modeling cognition and culture: Why cultural evolution does not require replication of representations},
  journal = {Journal of Cognition and Culture},
  volume  = {2},
  number  = {2},
  pages   = {87--112},
  year    = {2002},
  doi     = {10.1163/156853702320281836}
}
```
