---
type: paper
title: "Continuous Opinion Dynamics Under Bounded Confidence: A Survey"
aliases:
  - "Lorenz 2007"
  - "Bounded-confidence survey"
  - "lorenz-2007-continuous-opinion-dynamics"
  - "lorenz2007-continuous-opinion-dynamics"
authors: ["Lorenz J."]
year: 2007
url: https://doi.org/10.1142/S0129183107011789
tags: [cluster/social-physics, project/social-physics, field/physics, field/sociology, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# Continuous Opinion Dynamics Under Bounded Confidence: A Survey

> [!info] Citation
> Lorenz, J. (2007). *Continuous Opinion Dynamics Under Bounded Confidence: A Survey*. International Journal of Modern Physics C 18(12), 1819-1838. DOI: [10.1142/S0129183107011789](https://doi.org/10.1142/S0129183107011789). arXiv:0708.3293.

## TL;DR
Lorenz provides the authoritative consolidation of the bounded-confidence family of continuous opinion-dynamics models, unifying the two dominant variants — Hegselmann-Krause (HK) and Deffuant-Weisbuch (DW) — under a common framework. The core mechanism in both is the confidence threshold $\varepsilon$: an agent is influenced only by other agents whose opinions lie within distance $\varepsilon$ of its own; opinions outside that window are simply ignored. The survey catalogues the resulting phenomenology — convergence to consensus, splitting into a finite number of opinion clusters, or fragmentation — and how it depends systematically on $\varepsilon$, the update scheme, and the population structure.

## What it establishes
In the Hegselmann-Krause model agents update synchronously to the average of all opinions within their confidence interval,
$$ x_i(t+1) = \frac{1}{|I_i(t)|}\sum_{j \in I_i(t)} x_j(t), \qquad I_i(t) = \{ j : |x_i(t) - x_j(t)| \le \varepsilon \}, $$
whereas Deffuant-Weisbuch uses random pairwise meetings with a partial relaxation toward each other when within $\varepsilon$. The survey's organizing empirical law is the relation between the confidence bound and the number of surviving opinion clusters: large $\varepsilon$ yields a single consensus, decreasing $\varepsilon$ produces an increasing number of distinct clusters (roughly $\sim 1/(2\varepsilon)$ for HK on a uniform initial distribution), and very small $\varepsilon$ gives fragmentation into many isolated views. Lorenz frames both models as positive linear (averaging) systems with state-dependent, opinion-gated coupling, which is what gives confidence dynamics their characteristic cluster-counting behaviour.

## Relevance to this research
This is the reference survey for the bounded-confidence family that belief-inertia explicitly lists among the models recovered in its overdamped limit, and it supplies the consolidated phenomenology — number of clusters as a function of the confidence threshold — that any subsuming VFE functional must match. The confidence window $|x_i - x_j| \le \varepsilon$ is the discrete-cutoff caricature of the smooth attention gate $\beta_{ij} = \mathrm{softmax}(-\mathrm{KL}(q_i\|\Omega_{ij}[q_j])/\tau)$: large transported divergence suppresses coupling continuously where bounded confidence severs it abruptly. The cluster-formation and fragmentation regimes are direct targets for the program's claim to reproduce echo-chamber and polarization outcomes. This is a directly requested authoritative survey and a strong, on-machinery reference. See [[Bounded confidence]], [[Opinion dynamics]], [[Echo chambers and polarization]].

## Cross-links
- Concept: [[Bounded confidence]]
- Related sources: [[noorazar-2020-opinion-dynamics-survey]], [[axelrod-1997-dissemination-of-culture]]

## BibTeX
```bibtex
@article{lorenz2007continuous,
  author  = {Lorenz, Jan},
  title   = {Continuous Opinion Dynamics Under Bounded Confidence: A Survey},
  journal = {International Journal of Modern Physics C},
  year    = {2007},
  volume  = {18},
  number  = {12},
  pages   = {1819--1838},
  doi     = {10.1142/S0129183107011789}
}
```
