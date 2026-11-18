---
slug: flache-2017-social-influence-models
title: "Models of Social Influence: Towards the Next Frontiers"
aliases:
  - flache2017-opinion-dynamics
  - Flache 2017
  - Flache et al 2017
type: reference
authors:
  - Andreas Flache
  - Michael Mäs
  - Thomas Feliciani
  - Edmund Chattoe-Brown
  - Guillaume Deffuant
  - Sylvie Huet
  - Jan Lorenz
year: 2017
created: 2026-06-19
updated: 2026-06-19
tags:
  - cluster/social-physics
  - cluster/methodology
  - project/social-physics
  - field/sociology
  - field/physics
  - field/cs-ml
  - cluster/social-physics/opinion-dynamics
---

# Models of Social Influence: Towards the Next Frontiers

> [!cite] Citation
> Flache, A., Mäs, M., Feliciani, T., Chattoe-Brown, E., Deffuant, G., Huet, S., & Lorenz, J. (2017). Models of Social Influence: Towards the Next Frontiers. *Journal of Artificial Societies and Social Simulation*, 20(4), 2. DOI: [10.18564/jasss.3521](https://doi.org/10.18564/jasss.3521)

## TL;DR

A state-of-the-art review that maps the landscape of formal, agent-based models of social influence and charts where the field should go next. The authors organise three decades of work around Axelrod's puzzle — if interacting people grow more alike, why do differences not vanish into uniform consensus? — and partition the modelling tradition into three families distinguished by how an agent's opinion responds to the opinions it encounters: **assimilative** influence (agents always move toward those they interact with, as in DeGroot averaging and Friedkin–Johnsen), **similarity-biased** influence (agents adjust only toward sufficiently similar others, the bounded-confidence mechanism of Deffuant and Hegselmann–Krause), and **repulsive** influence (agents move away from dissimilar or disliked others, generating bi-polarization). The review's programmatic claim is that the next frontier is empirical: a generation of data-grounded influence models is needed to address live societal questions, above all the effect of social media and online interaction on opinion polarization.

## What it establishes

The paper's organising contribution is the assimilative / similarity-biased / repulsive taxonomy, which gives a single axis — the sign and conditional structure of the response-to-disagreement function — along which otherwise heterogeneous models can be compared. The three classes are made concrete by illustrative continuous-opinion update equations. **Class 1 — assimilative** (classical averaging, DeGroot/French/Harary): $o_{i,t+1} = o_{i,t} + \mu \sum_j w_{ij}(o_{j,t} - o_{i,t})$ with fixed weights $w_{ij}$, leading to consensus in any connected network. **Class 2 — similarity-biased** (bounded confidence, Deffuant et al. 2000; Hegselmann–Krause 2002): $o_{i,t+1} = o_{i,t} + f_w(o_{i,t}, o_{j,t})(o_{j,t} - o_{i,t})$ with $f_w = \mu \cdot \mathbf{1}[|o_i - o_j| \leq \epsilon]$, influence acting only within the confidence threshold $\epsilon$ and generating persistent clusters when $\epsilon$ is small. **Class 3 — repulsive** (Jager & Amblard 2005 type): $f_w(o_i, o_j) = \mu(1 - 2|o_j - o_i|)$, weights going negative for large disagreement, producing bi-polarization with opinions exceeding the initial extremes (a formal account of Abelson's "bimodal cleavage"). A heterogeneous bounded-confidence population (extremists with small $\epsilon$ mixed with moderates) can drive the entire moderate population to a single extreme — "single extreme convergence." Axelrod's (1997) nominal cultural-dissemination model and Mark's (1998) symbolic-interactionism model are the nominal-opinion analogues of Class 2. Within that frame it shows that consensus, fragmentation (multiple stable clusters), and persistent bi-polarization are not separate phenomena requiring separate models but distinct regimes of one mechanism class, selected by whether influence is unconditionally attractive, attractive-below-threshold, or attractive-near / repulsive-far. The authors trace how each family answers Axelrod's diversity puzzle: assimilative models need structural heterogeneity (network topology, noise, stubborn or zealot agents) to prevent collapse to consensus, similarity-biased models generate diversity endogenously through the confidence threshold, and repulsive models produce diversity through active divergence. The forward-looking half of the review identifies the methodological gap the field must close: most influence models are validated on stylized facts rather than calibrated to data, and the authors argue for empirical grounding — micro-validation of the influence response function, and macro-comparison of simulated against observed opinion distributions — as the precondition for using these models to reason about real polarization dynamics.

## Why the project cites it

The taxonomy connects to project threads on [[Opinion dynamics]], [[Bounded confidence]], [[Echo chambers and polarization]] (the repulsive-influence and similarity-biased families are the literature's account of polarization), and through its emphasis on network structure and clustering to [[Community detection and modularity]] and the Multi-agent variational free energy coupling graph.

## Sources / cross-links

- Concept pages: [[Opinion dynamics]], [[Sociophysics]], [[Bounded confidence]], [[Echo chambers and polarization]], [[Belief perseverance and confirmation bias]]
- Project dynamics shared with the multi-agent model:
- Geometry / method context: [[Fisher information metric]], [[Natural gradient]], [[Gauge transformation]]
- Classical opinion-dynamics sources reviewed here: [[degroot-1974-consensus]], [[friedkin1990-social-influence-opinions|friedkin-johnsen-1990]], [[deffuant2000-bounded-confidence|deffuant-2000-bounded-confidence]], [[hegselmann-2002-opinion|hegselmann-krause-2002]], [[galam-2008-sociophysics]], [[friedkin-johnsen-2011-social-influence-network]], [[axelrod-1997-dissemination-of-culture|axelrod1997-culture]]
- Companion surveys created this build: [[castellano-2009-statistical-physics-social-dynamics|castellano-fortunato-loreto-2009-social-dynamics]], [[rogers-2003-diffusion-of-innovations]]
- Related project pages: Gauge-Theoretic Multi-Agent VFE Model, [[VFE Transformer Program]]

## BibTeX

```bibtex
@article{flache2017social,
  author  = {Flache, Andreas and M{\"a}s, Michael and Feliciani, Thomas and Chattoe-Brown, Edmund and Deffuant, Guillaume and Huet, Sylvie and Lorenz, Jan},
  title   = {Models of Social Influence: Towards the Next Frontiers},
  journal = {Journal of Artificial Societies and Social Simulation},
  volume  = {20},
  number  = {4},
  pages   = {2},
  year    = {2017},
  doi     = {10.18564/jasss.3521}
}
```
