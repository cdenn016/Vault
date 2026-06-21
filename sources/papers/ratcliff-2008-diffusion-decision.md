---
type: paper
title: "The Diffusion Decision Model: Theory and Data for Two-Choice Decision Tasks"
aliases:
  - "Ratcliff 2008"
  - "DDM"
authors:
  - Ratcliff, Roger
  - McKoon, Gail
year: 2008
arxiv: null
url: https://doi.org/10.1162/neco.2008.12-06-420
tags:
  - cluster/social-physics/opinion-dynamics
  - project/multi-agent
  - field/psychology
  - field/neuroscience
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# The Diffusion Decision Model: Theory and Data for Two-Choice Decision Tasks

> [!info] Citation
> Ratcliff, R., & McKoon, G. (2008). "The Diffusion Decision Model: Theory and Data for Two-Choice Decision Tasks." *Neural Computation*, 20, 873–922.

## TL;DR
The diffusion decision model (DDM) is a process model of simple two-choice decisions in which a noisy accumulator drifts between two absorbing boundaries; the first-passage time and the boundary hit jointly determine the RT distribution and accuracy. The paper reviews how the model's four main components — drift rate (evidence quality), boundary separation (decision criterion), starting point (prior bias), and nondecision time — each map onto separable experimental manipulations, and demonstrates this decomposition on a coherent-motion discrimination task with human observers. Applications to aging and neurophysiology are also reviewed.

## Problem & setting
Sequential sampling models had been developed (Ratcliff 1978; Laming 1968; Stone 1960) to explain why reaction time distributions in two-choice tasks are positively skewed, why error RTs can be slower or faster than correct RTs depending on instructions, and why accuracy and RT trade off in the specific way they do. Prior models addressed only mean RT or only accuracy; the DDM simultaneously accounts for the full RT distribution for both correct and error responses across experimental conditions. The review paper systematically tests the model against three experimental manipulations (stimulus difficulty, speed-accuracy instructions, and stimulus proportion/prior probability) and examines how each engages a specific subset of model parameters.

## Method
The diffusion process is a continuous-time Wiener process with drift:

$$dx = v\,dt + s\,dW$$

where $v$ is the drift rate, $s$ the within-trial noise (scaling parameter, typically fixed), and $W$ standard Brownian motion. The process starts at $z$ (uniformly distributed over $[z - s_z/2, z + s_z/2]$ across trials) and terminates at the first passage to either boundary $a$ (correct) or $0$ (error). Drift rate itself varies across trials with standard deviation $\eta$ (Gaussian). The nondecision component $T_{er}$ (encoding plus response execution) is uniformly distributed with range $s_t$. The seven free parameters are $\{v, a, z, T_{er}, \eta, s_z, s_t\}$. Model fitting uses a chi-square method on quantile RTs (.1, .3, .5, .7, .9) for correct and error responses, minimized via SIMPLEX. Contaminant responses are handled by an explicit mixture parameter $p_o$. The key diagnostic display is the quantile probability plot — RT quantiles on the $y$-axis versus response proportion on the $x$-axis — which simultaneously represents accuracy and the full RT distribution shape for every condition.

## Key results
Experiment 1 (motion coherence manipulation) showed that drift rate varies with coherence level while boundary separation and nondecision time remain constant, producing the characteristic pattern that .9 quantile RTs increase much more than .1 quantile RTs across difficulty levels (ratio approximately 4:1). Experiment 2 (speed-accuracy instructions) showed that only boundary separation changes between the two instruction regimes, with both leading edge and tail shifting in roughly a 2:1 ratio. Experiment 3 (stimulus proportion manipulation) dissociated starting-point shifts (affecting both leading edge and tail) from drift-criterion shifts (affecting mainly the tail), mirroring signal-detection theory's criterion versus $d'$ distinction. Across-trial drift variability $\eta$ is necessary and sufficient to produce errors slower than correct responses; starting-point variability $s_z$ is necessary and sufficient to produce errors faster than correct responses; and both together explain the full range of observed correct-error RT asymmetries.

## Relevance to this research
The DDM provides a principled stochastic-process account of evidence accumulation and boundary absorption that is mathematically closely related to the VFE framework's belief-update dynamics. In the VFE transformer, beliefs $(mu, \Sigma)$ evolve by minimizing free energy; the drift rate $v$ in the DDM maps conceptually onto the precision-weighted prediction error that drives VFE gradient descent, while the boundary separation $a$ maps onto the confidence threshold implicit in the agent's prior $\alpha$ parameter. More directly, the starting-point bias (prior over responses) is analogous to the initial belief state $\mu_0$ in the VFE active-inference setting, and across-trial drift variability $\eta$ corresponds to hyperprior uncertainty over the precision of sensory evidence. In the multi-agent extension, individual agents accumulating evidence toward categorical decisions under social influence instantiates opinion-dynamics as a network of coupled DDMs — connecting to the social-physics cluster. The paper's treatment of error-RT asymmetries via variability at two timescales (within-trial noise vs. across-trial parameter variability) is directly relevant to any VFE model that must account for both mean behavior and full distributional signatures.

## Cross-links
- Concepts: [[Sequential Sampling Models]], [[Evidence Accumulation]], [[Reaction Time Distributions]], [[Speed-Accuracy Tradeoff]]
- Related sources: [[gold-2001-neural-basis-decision]], [[bogacz-2006-physics-optimal-decision]]
- Manuscript/Project: [[VFE Transformer Program]], [[Collective active inference|Multi-Agent Active Inference]]

## BibTeX
```bibtex
@article{Ratcliff2008,
  author  = {Ratcliff, Roger and McKoon, Gail},
  title   = {The Diffusion Decision Model: Theory and Data for Two-Choice Decision Tasks},
  journal = {Neural Computation},
  year    = {2008},
  volume  = {20},
  pages   = {873--922},
  doi     = {10.1162/neco.2008.12-06-420},
}
```
