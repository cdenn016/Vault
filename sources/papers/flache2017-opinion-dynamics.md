---
type: paper
title: "Models of Social Influence: Towards the Next Frontiers"
aliases:
  - "Flache 2017"
  - "Flache et al 2017"
authors:
  - Flache, Andreas
  - Mäs, Michael
  - Feliciani, Thomas
  - Chattoe-Brown, Edmund
  - Deffuant, Guillaume
  - Huet, Sylvie
  - Lorenz, Jan
year: 2017
arxiv: null
url: https://doi.org/10.18564/jasss.3521
tags:
  - cluster/social-physics/opinion-dynamics
  - cluster/social-physics/social-influence
  - project/social-physics
  - field/sociology
  - field/physics
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Models of Social Influence: Towards the Next Frontiers

> [!info] Citation
> Flache, A., Mäs, M., Feliciani, T., Chattoe-Brown, E., Deffuant, G., Huet, S., & Lorenz, J. (2017). "Models of Social Influence: Towards the Next Frontiers." *Journal of Artificial Societies and Social Simulation*, 20(4) 2. https://doi.org/10.18564/jasss.3521

## TL;DR
This is a comprehensive review of agent-based models of social influence dynamics, organising the literature into three canonical classes: assimilative influence (always-converging averaging), similarity-biased influence (bounded confidence), and repulsive influence (differentiation from dissimilar others). It argues that persistent opinion diversity, clustering, and bi-polarization each require specific micro-level mechanisms, and identifies two urgent frontiers: better theoretical integration across model classes and far more rigorous empirical calibration and validation.

## Problem & setting
Axelrod's (1997) question — why does not all opinion diversity disappear if social influence reduces differences between people? — motivates this work. Early linear averaging models (DeGroot, French, Harary) predict universal consensus in connected networks, contradicting empirical observations of persistent clustering, fragmentation, and polarization. The review asks which formal ingredients generate which macro-level outcomes (consensus, clustering, bi-polarization, extremization), and what conditions make each outcome fragile or robust.

## Method
The authors categorize the literature into three ideal-typical model classes and present illustrative continuous-opinion update equations for each.

**Class 1 — Assimilative influence** (classical averaging):
$$o_{i,t+1} = o_{i,t} + \mu \sum_j w_{ij}(o_{j,t} - o_{i,t})$$
Fixed weights $w_{ij}$; leads to consensus in any connected network.

**Class 2 — Similarity-biased influence** (bounded confidence, Deffuant et al. 2000; Hegselmann & Krause 2002):
$$o_{i,t+1} = o_{i,t} + f_w(o_{i,t}, o_{j,t})(o_{j,t} - o_{i,t}), \quad f_w = \mu \cdot \mathbf{1}[|o_i - o_j| \leq \epsilon]$$
Influence only within confidence threshold $\epsilon$; generates persistent opinion clusters if $\epsilon$ is sufficiently small.

**Class 3 — Repulsive influence** (Jager & Amblard 2005 type):
$$f_w(o_i, o_j) = \mu(1 - 2|o_j - o_i|)$$
Weights become negative for large disagreement, implementing opinion differentiation; generates bi-polarization with opinions exceeding initial extremes.

Axelrod's (1997) nominal cultural dissemination model and Mark's (1998) symbolic interactionism model are treated as nominal-opinion analogues of Class 2. Repulsive nominal models (Macy et al. 2003; Mark 2003) complete Class 3. The review discusses noise sensitivity, network topology effects, and heterogeneous confidence levels (extremist–moderate mixtures) across all three classes.

## Key results
The three model classes yield qualitatively distinct collective outcomes. Assimilative models inevitably produce consensus in connected networks; diversity requires disconnected components or stubbornness (Friedkin & Johnsen). Similarity-biased models produce opinion clustering when $\epsilon$ is small, but fragmentation is fragile to noise (Mäs et al. 2010; Klemm et al. 2003) and cannot generate opinions more extreme than initial extremists. Repulsive models produce bi-polarization with maximally diverging factions and opinions beyond the initial range, offering a formal account of Abelson's "bimodal cleavage" question. A heterogeneous bounded-confidence population (extremists with small $\epsilon$ mixed with moderates) can drive the entire moderate population to a single extreme — "single extreme convergence" — even with symmetric initial extremism. Across all classes, network density and confidence thresholds are the primary modulators of consensus vs. fragmentation; noise typically destroys diversity but at intermediate rates can sustain it.

## Relevance to this research
The multi-agent VFE/active-inference framework operates on belief distributions (Gaussian tuples $(\mu, \Sigma)$) coupled by attention weights $\beta_{ij}$ that are themselves derived from VFE minimization. The three influence-model classes map naturally onto regimes of the VFE belief-coupling term $\sum_{ij} \beta_{ij} \text{KL}(q_i \| \Omega_{ij} q_j)$: assimilative influence corresponds to fixed uniform $\beta_{ij}$ with symmetric transport $\Omega_{ij}$; similarity-biased influence to attention weights that become negligible when beliefs are far apart (the bounded-confidence analogue is a KL threshold gating $\beta_{ij} \to 0$); repulsive influence has no direct VFE analogue but could arise from anti-aligned gauge transport. The social-physics polarization literature thus provides qualitative benchmarks and mechanisms against which multi-agent VFE collective dynamics (consensus, clustering, bi-polarization) can be compared and validated. The review's critique of insufficient empirical calibration resonates with the VFE program's need to ground free-energy minimization in observable collective behaviour.

## Cross-links
- Concepts: [[Opinion Dynamics]], [[Social Influence]], [[Belief Propagation]], [[Multi-Agent Active Inference]]
- Related sources: [[axelrod1997-culture]], [[deffuant2000-mixing]], [[hegselmann2002-opinion]]
- Manuscript/Project: [[VFE Transformer Program]], [[MAgent Model]]

## BibTeX
```bibtex
@article{flache2017,
  author  = {Flache, Andreas and M\"{a}s, Michael and Feliciani, Thomas and Chattoe-Brown, Edmund and Deffuant, Guillaume and Huet, Sylvie and Lorenz, Jan},
  title   = {Models of Social Influence: Towards the Next Frontiers},
  journal = {Journal of Artificial Societies and Social Simulation},
  year    = {2017},
  volume  = {20},
  number  = {4},
  pages   = {2},
  doi     = {10.18564/jasss.3521},
  url     = {http://jasss.soc.surrey.ac.uk/20/4/2.html},
}
```
