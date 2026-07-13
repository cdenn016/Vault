---
type: paper
title: "Opinion Behavior Analysis in Social Networks Under the Influence of Coopetitive Media"
aliases:
  - "Coopetitive-media opinion dynamics (Xue et al. 2020)"
authors:
  - Dong Xue
  - Sandra Hirche
  - Ming Cao
year: 2020
doi: 10.1109/TNSE.2019.2894565
url: https://doi.org/10.1109/TNSE.2019.2894565
tags:
  - cluster/social-physics
  - cluster/social-physics/opinion-dynamics
  - cluster/multi-agent
  - project/social-physics
  - project/multi-agent
  - field/cs-ml
  - field/sociology
created: 2026-07-12
---

# Opinion Behavior Analysis in Social Networks Under the Influence of Coopetitive Media

> [!info] Citation
> Dong Xue, Sandra Hirche, and Ming Cao (2020). “Opinion Behavior Analysis in Social Networks Under the Influence of Coopetitive Media.” *IEEE Transactions on Network Science and Engineering* 7(3), 961–974. DOI: [10.1109/TNSE.2019.2894565](https://doi.org/10.1109/TNSE.2019.2894565).

## TL;DR

Xue, Hirche, and Cao model opinion formation under interpersonal influence and media organizations that may cooperate or compete. Their community-aware, bias-sensitive network model is analyzed using port-Hamiltonian systems and passivity. Because it already applies Hamiltonian-system machinery to opinion dynamics, it is an essential comparator against any broad claim that Hamiltonian opinion modeling is new.

## Problem & setting

The paper studies how public opinions evolve when individuals communicate over a social network and also receive messages from multiple media actors. The media relationships are “coopetitive,” mixing cooperation and competition, and individuals may have personalized biases. The research question concerns long-run outcomes such as consensus, polarization, neutrality, and the influence of coordinated media coalitions.

## Method

The authors introduce a mathematical opinion-diffusion model that incorporates community structure, peer interactions, media exposure, and individual biases. They express the dynamics in port-Hamiltonian form and use the passivity of individual self-dynamics to establish convergence properties. The formulation is then used to analyze steering conditions and the balance between interpersonal communication and media contact.

## Key results

The port-Hamiltonian representation supports long-run analysis of opinion evolution and conditions for steering populations toward consensus, polarity, or neutrality. The paper also examines how an autocratic media coalition can emerge independently of public views and how the relative strengths of peer communication and media exposure shape the outcome. These results concern a specific controlled network model rather than a universal kinetic law for beliefs.

## Relevance to this research

This source prevents novelty claims based merely on introducing Hamiltonian language into [[Opinion dynamics]]. A defensible contribution for [[Hamiltonian belief dynamics]] must identify the mechanism absent here: gauge-transported VFE coupling, optimized attention, the four-part local stiffness, and the explicit kinetic metric on probabilistic beliefs. Xue, Hirche, and Cao also provide a useful systems-and-control comparator for analyzing dissipation and external social forcing without conflating passivity with Fisher-Rao mass.

## Cross-links

The paper connects [[Opinion dynamics]], [[Sociophysics]], [[Hamiltonian belief dynamics]], [[Belief inertia]], and [[Echo chambers and polarization]]. Its multi-agent port-Hamiltonian perspective is also relevant to [[Statistical physics of social systems and collective behavior]] and to comparisons between network control, media forcing, and variational belief coupling.

## BibTeX

```bibtex
@article{XueHircheCao2020,
  author  = {Xue, Dong and Hirche, Sandra and Cao, Ming},
  title   = {Opinion Behavior Analysis in Social Networks Under the Influence of Coopetitive Media},
  journal = {IEEE Transactions on Network Science and Engineering},
  volume  = {7},
  number  = {3},
  pages   = {961--974},
  year    = {2020},
  doi     = {10.1109/TNSE.2019.2894565}
}
```
