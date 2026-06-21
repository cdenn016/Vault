---
type: paper
title: "Social physics"
aliases: ["Jusup et al. 2022", "Social physics (Physics Reports review)"]
authors: ["Jusup M.", "Holme P.", "Kanazawa K.", "Takayasu M.", "Romić I.", "Wang Z.", "Geček S.", "Lipić T.", "Podobnik B.", "Wang L.", "Luo W.", "Klanjšček T.", "Fan J.", "Boccaletti S.", "Perc M."]
year: 2022
arxiv: 2110.01866
url: https://doi.org/10.1016/j.physrep.2021.10.005
tags: [cluster/social-physics, cluster/social-physics/opinion-dynamics, cluster/social-physics/networks-and-contagion, project/social-physics, field/physics, field/sociology, field/economics, field/cs-ml]
created: 2026-06-20
updated: 2026-06-20
---

# Social physics

> [!info] Citation
> Jusup, M., Holme, P., Kanazawa, K., Takayasu, M., Romić, I., Wang, Z., Geček, S., Lipić, T., Podobnik, B., Wang, L., Luo, W., Klanjšček, T., Fan, J., Boccaletti, S. & Perc, M. (2022). *Social physics*. Physics Reports **948**, 1–148. arXiv:[2110.01866](https://arxiv.org/abs/2110.01866). DOI: [10.1016/j.physrep.2021.10.005](https://doi.org/10.1016/j.physrep.2021.10.005).

## TL;DR
A sweeping, book-length *Physics Reports* survey of **social physics** — the use of statistical-physics methods to study collective human phenomena. It is the most current panoramic map of the whole field, organized into two halves: topics at the heart of modern societies (urban dynamics and traffic, financial markets, cooperation, social-network structure, and the integration of intelligent machines) and topics framed as threats (crime, mass migration, epidemics, environmental and climate challenges). For each it reviews the canonical models, the empirical regularities (scaling laws, phase transitions, criticality), and open directions. Its value to the program is as an orientation atlas: it situates the [[SocialPhysics]] belief-dynamics work within the broadest possible picture of physics-of-society and supplies a single authoritative entry point to the surrounding literature.

## Problem & setting
The review's thesis is methodological: a great range of societal phenomena yield to the same toolkit physicists built for many-body systems — master equations, mean-field and kinetic descriptions, scaling and renormalization, network science, agent-based simulation, and the search for universality and criticality. It traces the lineage from Quetelet's "social physics" and the 19th-century statistical tradition through Schelling, Galam, Weidlich's [[Sociodynamics and synergetics|synergetics]], and the modern explosion catalogued by [[castellano-2009-statistical-physics-social-dynamics|castellano-fortunato-loreto-2009-social-dynamics]]. It builds on, and updates, the standard reviews — the statistical-physics-of-social-dynamics canon, the [[galam-2008-sociophysics|Galam sociophysics]] lineage, and the cooperation review [[perc-jordan-rand-wang-boccaletti-szolnoki-2017-statistical-physics-cooperation]] — folding them into one frame.

## Method
The survey is organized by domain rather than by mathematical technique, but the same machinery recurs throughout: power-law / scaling analysis (city size and growth, market fluctuations), [[Network structure — small-world and scale-free|complex-network]] structure and dynamics, [[Evolutionary game theory and cooperation|evolutionary-game]] models of cooperation on graphs, [[Kinetic theory of opinion dynamics|kinetic / agent-based]] models of opinion and behavior, epidemic-spreading and [[Threshold models and complex contagion|contagion]] models, and data-driven empirical validation against large behavioral datasets. A distinctive late section treats the **integration of intelligent machines** (algorithms, bots, recommender systems) into human social networks as a new force reshaping collective dynamics — the social-physics framing of human–AI hybrid systems.

## Key results
This is a review, so its "results" are syntheses: that urban scaling, market criticality, cooperation on networks, and opinion polarization are each well captured by statistical-physics models with measurable universal features; that network topology is decisive across all of them; and that the field has matured from toy analogy to a quantitative, data-validated discipline. It closes optimistically — "the future for social physics is bright" — while stressing the need for genuine interdisciplinary dialogue rather than physicists colonizing other fields.

## Relevance to this research
This is the broadest external context map for the [[SocialPhysics]] program, and it sets the bar the program must clear to claim novelty. Three points of contact matter. First, the review confirms that the program's strategy — write a microscopic interaction rule, coarse-grain to collective behavior, look for universality — *is* the social-physics method, so the [[Multi-agent variational free energy]] functional sits squarely inside this tradition rather than beside it. Second, almost every model the review catalogs is **first-order** (rate rules, gradient-like relaxation, memoryless updates); the program's distinctive bet, the **underdamped / inertial** belief dynamics of [[belief-inertia]] with [[Mass as Fisher information|mass from Fisher information]], is precisely the second-order extension this entire landscape structurally lacks, which is exactly how the [[Statistical physics of social systems and collective behavior]] theme positions it. Third, the review's emphasis on network structure and on human–machine hybrid systems aligns with reading the attention weights $\beta_{ij}$ as a learned interaction graph and with the program's multi-scale [[Ouroboros multi-scale dynamics|Ouroboros]] / [[Meta-agents and hierarchical emergence|meta-agent]] coarse-graining. Honestly, this is positioning and vocabulary, not machinery: it offers no gauge structure and no inertial dynamics, but it is the single best citation for "here is the whole field the program is trying to subsume."

## Cross-links
- Concepts: [[Sociophysics]], [[Opinion dynamics]], [[Network structure — small-world and scale-free]], [[Evolutionary game theory and cooperation]], [[Synchronization and the Kuramoto model]], [[Threshold models and complex contagion]]
- Theme: [[Statistical physics of social systems and collective behavior]]
- Project: [[SocialPhysics]]
- Related sources: [[castellano-2009-statistical-physics-social-dynamics|castellano-fortunato-loreto-2009-social-dynamics]], [[galam-2008-sociophysics]], [[perc-jordan-rand-wang-boccaletti-szolnoki-2017-statistical-physics-cooperation]], [[noorazar-2020-opinion-dynamics-survey]], [[helbing-2010-quantitative-sociodynamics]]

## BibTeX
```bibtex
@article{jusup2022social,
  author  = {Jusup, Marko and Holme, Petter and Kanazawa, Kiyoshi and Takayasu, Misako and Romi\'{c}, Ivan and Wang, Zhen and Ge\v{c}ek, Sun\v{c}ana and Lipi\'{c}, Tomislav and Podobnik, Boris and Wang, Lin and Luo, Wei and Klanj\v{s}\v{c}ek, Tin and Fan, Jingfang and Boccaletti, Stefano and Perc, Matja\v{z}},
  title   = {Social physics},
  journal = {Physics Reports},
  volume  = {948},
  pages   = {1--148},
  year    = {2022},
  doi     = {10.1016/j.physrep.2021.10.005}
}
```
