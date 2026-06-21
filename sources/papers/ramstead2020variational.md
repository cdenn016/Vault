---
type: paper
title: "Variational ecology and the physics of sentient systems"
aliases:
  - "Ramstead 2019"
  - "Variational Ecology"
  - "VE"
authors:
  - Ramstead, Maxwell J.D.
  - Constant, Axel
  - Badcock, Paul B.
  - Friston, Karl J.
year: 2019
arxiv: null
url: https://doi.org/10.1016/j.plrev.2018.12.002
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/neuroscience
  - field/biology
  - field/philosophy
  - field/physics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Variational ecology and the physics of sentient systems

> [!info] Citation
> Ramstead, M.J.D., Constant, A., Badcock, P.B., & Friston, K.J. (2019). "Variational ecology and the physics of sentient systems." *Physics of Life Reviews*, 31, 188–205. https://doi.org/10.1016/j.plrev.2018.12.002

## TL;DR
This review extends the free energy principle (FEP) and variational neuroethology (VNE) to large-scale organism–niche ensembles via the variational approach to niche construction (VANC) and the skilled intentionality framework (SIF). The resulting framework, termed variational ecology (VE), explains how ecological niches inherit statistical robustness from the collective active inference of their denizens, enabling a physics of sentient systems that spans cells to societies.

## Problem & setting
Variational neuroethology had provided a principled multiscale ontology for living systems using recursively nested Markov blankets (MBs), but lacked a principled method for individuating and drawing MBs at scales beyond the single organism — for social ensembles, ecosystems, or cultural collectives. Critics (Bruineberg & Hesp; Kirmayer) argued that the MB formalism, defined through conditional independencies of weakly mixing random dynamical systems, may not transfer to large-scale ensembles that are too transient or loosely coupled. The paper addresses how to extend VFE minimisation to organism–niche coupled dynamics at these broader scales.

## Method
The paper synthesises three frameworks. VNE uses the FEP with Tinbergen's four levels of biological explanation to recursively nest MBs (blankets of blankets), where order parameters at each scale correspond to slow eigenmodes of lower-scale blanket-state Jacobians. The VANC recasts developmental niche construction (DNC) as the joint ontogenetic optimisation of niche and agent ensemble, and selective niche construction (SNC) as Bayesian model selection; agents collectively offload expected-free-energy computation to unambiguous epistemic resources embedded in the niche. The SIF defines affordances as expected-free-energy gradients over the organism's action repertoire, providing the mechanism by which the niche acquires MB structure — its sensory states are the solicitations that engage agents, its active states are the affordances it offers, and its internal states are the physical structures modified through dense histories of active inference. Variational ecology (VE) integrates all three, positing that an ecological niche possesses a statistical MB in virtue of these affordance-based relations, and that the total free energy of an ensemble is extensive (additive over agents sharing the same generative model).

## Key results
The paper's key theoretical results are the following. First, the extensivity of variational free energy over agent ensembles allows the total free energy of a collective to be decomposed as a sum of individual free energies, enabling joint optimisation at the population level. Second, affordances, recast as expected-free-energy gradients under the VANC/SIF combination, function as the MB surface of the niche: solicitations constitute sensory states of the niche, while the niche's capacity to offer varied engagement possibilities constitutes its active states. Third, the internal states of the niche — physical structures modified by recurrent action — encode organism-specific causal regularities about group behaviour and shared intentionality, not merely generic environmental changes. Fourth, the recursive application of this construction yields a multiscale hierarchy in which each scale's dynamics constrain the scale below via probability gradients, and free energy minimisation at each level dissolves those gradients in a form of cross-scale circular causality homologous to synergetics' enslaving principle.

## Relevance to this research
This paper is directly relevant to the multi-agent extension of the VFE transformer program. The extensivity of variational free energy over agent ensembles is the justification for summing individual agent free energies in the MAgent_Model, and the recursive MB nesting underpins the multi-scale belief-coupling architecture. The coupling term in the VFE free energy functional — $\sum_{ij} \beta_{ij} \mathrm{KL}(q_i \| \Omega_{ij} q_j)$ — is a formal realisation of the pairwise belief coupling that VE describes informally between agents sharing a niche. The gauge transport $\Omega_{ij}$ in the GL(K)-equivariant attention corresponds to the statistical structure of niche-mediated coupling among agents' internal states. The paper also provides conceptual grounding for the social-physics extension, since VE's physics of interacting minds directly motivates modelling social opinion dynamics as active inference over shared niches with affordance-structured interactions.

## Cross-links
- Concepts: [[Free Energy Principle]], [[Active Inference]], [[Markov Blanket]], [[Variational Free Energy]], [[Niche Construction]]
- Related sources: [[friston2019free]], [[ramstead2018answering]], [[constant2018variational]]
- Manuscript/Project: [[VFE Transformer Program]], [[MAgent Model]]

## BibTeX
```bibtex
@article{ramstead2020variational,
  author  = {Ramstead, Maxwell J.D. and Constant, Axel and Badcock, Paul B. and Friston, Karl J.},
  title   = {Variational ecology and the physics of sentient systems},
  journal = {Physics of Life Reviews},
  volume  = {31},
  pages   = {188--205},
  year    = {2019},
  doi     = {10.1016/j.plrev.2018.12.002},
}
```
