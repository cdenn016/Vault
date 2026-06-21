---
type: paper
title: "Belief traps: Tackling the inertia of harmful beliefs"
aliases:
  - "Scheffer 2022"
  - "Belief Traps"
authors:
  - Scheffer, Marten
  - Borsboom, Denny
  - Nieuwenhuis, Sander
  - Westley, Frances
year: 2022
arxiv: null
url: https://doi.org/10.1073/pnas.2203149119
tags:
  - cluster/social-physics/social-influence
  - project/social-physics
  - field/psychology
  - field/sociology
  - field/neuroscience
  - field/biology
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Belief traps: Tackling the inertia of harmful beliefs

> [!info] Citation
> Scheffer, M., Borsboom, D., Nieuwenhuis, S., & Westley, F. (2022). "Belief traps: Tackling the inertia of harmful beliefs." *PNAS* 119(32), e2203149119. https://doi.org/10.1073/pnas.2203149119

## TL;DR
This paper presents a cross-disciplinary framework explaining why beliefs resist change even under counterevidence, unifying neurobiological attractor dynamics, psychological confirmation bias, cognitive dissonance, and social network contagion into a single "belief trap" model. The key insight is that self-amplifying feedbacks at every level — neural, cognitive, and social — create hysteresis, so that beliefs function as attractors in a dynamical system with tipping points. The paper argues that reducing dichotomous (black-and-white) thinking and addressing the social stressors that promote it (poverty, inequality, polarization) is the most effective generic approach to preventing harmful rigid beliefs.

## Problem & setting
Many beliefs — pathological (phobias, delusions, depression), social (racial prejudice, vaccine refusal, conspiracy theories), and political (post-truth dynamics) — persist despite abundant counterevidence. Existing interventions (better information, media campaigns, workplace diversity training) often fail. The problem spans neuroscience, psychiatry, and social science, but these disciplines have studied belief resilience in isolation without a unifying model. The paper asks: what determines the resilience of a belief, and how can that resilience be reduced?

## Method
The authors develop a graphical dynamical-systems model of confirmation bias. Belief strength is a sigmoidal (potentially black-and-white) function of perceived evidence, while perceived evidence is itself colored by the existing belief — creating a mutual feedback loop. When plotted together, the system can exhibit multiple stable equilibria (belief and disbelief attractors) separated by an unstable repellor, producing hysteresis over a range of objective evidence between two tipping points T1 and T2. The basin of attraction around each attractor quantifies resilience; sustained counterevidence shrinks the basin until a tipping point is crossed.

This framework is then extended qualitatively to two higher organizational levels: (1) cognitive coherence networks, where abandoning one belief risks destabilizing an internally consistent worldview (cognitive dissonance), and (2) social networks, where homophily and mutual contagion within echo chambers amplify belief resilience at the group level. At the neural level, the model maps onto winner-take-all attractor dynamics driven by recurrent excitatory connections and mutual inhibition between competing neural pools, with Hebbian learning gradually deepening the attractor landscape over time.

## Key results
The model predicts that belief resilience is governed primarily by two parameters: (1) the steepness of the sigmoidal belief response (degree of black-and-white thinking) and (2) the strength of confirmation bias. Both must exceed a threshold for multiple stable attractors to exist; below the threshold, belief changes smoothly with evidence. Stress amplifies winner-take-all neural competition, thereby promoting dichotomous thinking and making belief traps more likely — consistent with observations that conspiracy theories and psychiatric disorders spike during societal crises. Sustained (not one-shot) exposure to counterevidence is required to erode resilience, analogous to synaptic unlearning. Institutional rational override (cognitive behavioral therapy for pathological beliefs; structural societal mixing for prejudices) provides the sustained counterevidence needed to cross the tipping point. The most generic intervention, however, is upstream: reducing social stress through policies addressing poverty, inequality, and conflict, including proposals like universal basic income, may prevent rigid belief formation more effectively than targeting specific beliefs after the fact.

## Relevance to this research
The dynamical-systems vocabulary used here — attractors, basins of attraction, hysteresis, tipping points, contagion in networks — maps directly onto the mathematical machinery of the VFE framework. Belief states as attractors of a confirmation-bias feedback loop are formally analogous to the VFE-minimizing belief states (mu, Sigma) that settle into local minima of the free energy landscape; the hysteresis corresponds to the multi-modal posteriors that arise when the prior-to-likelihood balance crosses a phase-transition threshold. The social-contagion dynamics described (homophily driving convergence within subgroups, echo chambers sustaining divergent attractor states across subgroups) are precisely the phenomena targeted by the multi-agent active inference / social-physics extension of the VFE transformer. The stress-driven amplification of black-and-white thinking corresponds to a sharpened softmax (low temperature tau) in the attention distribution, which concentrates beta_ij on fewer neighbors and reduces belief diversity — connecting to the attention entropy term in the canonical free energy. The paper also provides empirical grounding for why opinion polarization is a stable two-attractor phenomenon rather than a continuous distribution, supporting the modeling choice of bistable social dynamics in the multi-agent model. The framework for destabilizing harmful beliefs through rational override is conceptually related to active inference's directed policy selection that minimizes expected free energy.

## Cross-links
- Concepts: [[Belief Dynamics]], [[Attractor Networks]], [[Belief perseverance and confirmation bias|Confirmation Bias]], [[Threshold models and complex contagion|Social Contagion]], [[Opinion Dynamics]], [[Free-energy principle active inference|Free Energy Principle]]
- Related sources: [[deffuant2000-bounded-confidence|deffuant-2000-mixing-beliefs]], [[hegselmann-2002-opinion|hegselmann-2002-opinion-dynamics]], [[parr-2022-active-inference|friston-2022-active-inference]]
- Manuscript/Project: [[VFE Transformer Program]], [[Gauge-Theoretic Multi-Agent VFE Model|MAgent Model]]

## BibTeX
```bibtex
@article{scheffer2022,
  author  = {Scheffer, Marten and Borsboom, Denny and Nieuwenhuis, Sander and Westley, Frances},
  title   = {Belief traps: {T}ackling the inertia of harmful beliefs},
  journal = {Proceedings of the National Academy of Sciences},
  year    = {2022},
  volume  = {119},
  number  = {32},
  pages   = {e2203149119},
  doi     = {10.1073/pnas.2203149119},
}
```
