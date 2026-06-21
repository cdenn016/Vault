---
type: paper
title: "The Markov blankets of life: autonomy, active inference and the free energy principle"
aliases:
  - "Kirchhoff 2018"
  - "Markov blankets of life"
authors:
  - Kirchhoff, Michael
  - Parr, Thomas
  - Palacios, Ensor
  - Friston, Karl
  - Kiverstein, Julian
year: 2018
arxiv: null
url: https://doi.org/10.1098/rsif.2017.0792
tags:
  - cluster/vfe
  - cluster/participatory/philosophy-of-mind
  - project/multi-agent
  - field/neuroscience
  - field/biology
  - field/philosophy
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# The Markov blankets of life: autonomy, active inference and the free energy principle

> [!info] Citation
> Kirchhoff M, Parr T, Palacios E, Friston K, Kiverstein J. (2018). "The Markov blankets of life: autonomy, active inference and the free energy principle." J. R. Soc. Interface 15: 20170792. https://doi.org/10.1098/rsif.2017.0792

## TL;DR
This paper argues that the autonomous organization of all biological systems — from single cells to Homo sapiens — can be understood in terms of hierarchically nested Markov blankets operating under the free energy principle. A Markov blanket defines a statistical boundary separating a system's internal states from external states, and its presence induces active inference: the tendency to minimize variational free energy, which upper-bounds surprise. The central contribution is the concept of "ensemble Markov blankets" (blankets of blankets), showing that collectives of Markov-blanketed subsystems self-assemble into superordinate systems that themselves possess a Markov blanket, with autonomous organization extending all the way down to organelles and all the way out to environmental elements.

## Problem & setting
The paper addresses how biological systems maintain coherent autonomous identity despite comprising nested subsystems, and how their organizational boundaries need not coincide with biophysical boundaries. Prior work by Friston and others established the free energy principle and active inference for individual organisms; this paper extends those ideas to *hierarchical ensembles* of Markov-blanketed systems. The central puzzle is avoiding over-broadness: any coupled dynamical system (e.g., Huygens' coupled pendulums) has a Markov blanket and thus technically engages in "active inference" — yet pendulums are not autonomous organisms. The paper resolves this by distinguishing *mere active inference* from *adaptive active inference*.

## Method
The framework builds on the statistical definition of a Markov blanket from Pearl (1988): a set of nodes that renders a target node conditionally independent of all other nodes. In the free energy setting the blanket comprises sensory and active states, with internal states (beliefs) and external states (environment) conditionally independent given blanket states. Variational free energy is defined as:

$$F(s, a, r) = -\ln p(s, a \mid m) + D_\mathrm{KL}[q(w \mid r) \,\|\, p(w \mid s, a)]$$

where $s$ = sensory states, $a$ = active states, $r$ = internal states, $m$ = generative model, and $q(w|r)$ is the variational density over hidden causes $w$. Because $D_\mathrm{KL} \geq 0$, free energy upper-bounds surprise $-\ln p(s,a|m)$; minimizing $F$ therefore minimizes (time-averaged) entropy (shown via Jensen's inequality in the appendix). The paper distinguishes: (1) *mere active inference* — generalized synchrony induced by any Markov blanket (e.g., coupled pendulums); (2) *adaptive active inference* — action selection guided by a temporally deep generative model that infers probabilistic future states and minimizes *expected* free energy. Only the latter confers genuine autonomy. Ensemble (nested) Markov blankets are then formed by showing that the statistical partitioning rule is recursive: slow macroscale dynamics emerge from microscale fast dynamics (synergetics / slaving principle), and a superordinate Markov blanket encodes the order parameter of the collective.

## Key results
The paper establishes three main claims. First, any living system necessarily possesses a Markov blanket, because without one it cannot be distinguished from its environment and ceases to exist. Second, the boundaries of autonomous systems need not be co-extensive with biophysical organism boundaries: they can extend outward to incorporate environmental elements (water boatman's plastron air bubble) or vary across a life cycle (caterpillar-pupa-butterfly metamorphosis). Third, autonomous systems are hierarchically composed of Markov blankets of Markov blankets spanning all scales (DNA, organelles, cells, tissues, organs, organisms, social systems, ecosystems), with the ensemble's self-evidencing dynamics realised by the inter-level slaving of fast microscale to slow macroscale dynamics, recapitulating the same statistical form at each level.

## Relevance to this research
This paper is foundational background for the multi-agent active inference architecture in the VFE transformer program. The hierarchical Markov blanket structure maps directly onto the VFE free energy hierarchy (h → s → p → q → observations): each level of the hierarchy corresponds to a Markov-blanketed system whose internal states are beliefs and whose active/sensory states mediate coupling to adjacent levels. The ensemble Markov blanket construction provides a principled theoretical justification for multi-agent belief coupling via GL(K)-transported KL divergences: each agent has its own Markov blanket, and the coupled-agent system forms a higher-order blanket whose free energy is the sum of pairwise KL terms in the canonical F. The distinction between mere and adaptive active inference informs what "autonomy" means for an agent node in the multi-agent graph. The autopoietic framing (operational closure, sense making) connects to the participatory realism / PIFB manuscript, where Markov blankets are reinterpreted as quantum reference frames that enact the system's classical reality.

## Cross-links
- Concepts: [[Markov Blanket]], [[Free Energy Principle]], [[Active Inference]], [[Variational Free Energy]], [[Predictive Coding]]
- Related sources: [[friston-2010-free-energy-unified]], [[ramstead-2018-answering-schrodinger]], [[parr-friston-2019-generalised]]
- Manuscript/Project: [[VFE Transformer Program]], [[MAgent Model]], [[PIFB]]

## BibTeX
```bibtex
@article{KirchhoffParrPalaciosFristonKiverstein2018,
  author  = {Kirchhoff, Michael and Parr, Thomas and Palacios, Ensor and Friston, Karl and Kiverstein, Julian},
  title   = {The {Markov} blankets of life: autonomy, active inference and the free energy principle},
  journal = {Journal of the Royal Society Interface},
  year    = {2018},
  volume  = {15},
  pages   = {20170792},
  doi     = {10.1098/rsif.2017.0792},
}
```
