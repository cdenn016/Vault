---
type: paper
title: "Perseverance of Social Theories: The Role of Explanation in the Persistence of Discredited Information"
aliases:
  - "Anderson 1980"
  - "Belief Perseverance"
authors:
  - Anderson, Craig A.
  - Lepper, Mark R.
  - Ross, Lee
year: 1980
arxiv: null
url: null
tags:
  - cluster/social-physics/social-influence
  - project/social-physics
  - field/psychology
  - field/sociology
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Perseverance of Social Theories: The Role of Explanation in the Persistence of Discredited Information

> [!info] Citation
> Anderson, C. A., Lepper, M. R., & Ross, L. (1980). "Perseverance of Social Theories: The Role of Explanation in the Persistence of Discredited Information." *Journal of Personality and Social Psychology*, 39(6), 1037–1049.

## TL;DR
Social theories — beliefs about empirical relationships between variables — persist even after the evidence that generated them has been completely and explicitly discredited. Two experiments demonstrate that this "theory perseverance" effect is substantially amplified when subjects are asked to formulate a causal explanation for the theory, because such explanations become autonomous of the original data and continue to imply the theory's correctness.

## Problem & setting
Prior research (Ross, Lepper, & Hubbard, 1975) showed that specific personal impressions can survive complete invalidation of the evidence on which they were based. The present work asks whether the same phenomenon extends to more abstract social theories (beliefs about relationships among variables), and specifically probes the cognitive mechanism — causal explanation generation — that may mediate perseverance. Subjects in both studies had minimal, objectively inadequate initial evidence (two case studies) and underwent thorough debriefing procedures that explicitly revealed the fictional nature of the original data.

## Method
Both experiments used a debriefing paradigm with Stanford undergraduates. Subjects were shown fabricated case studies suggesting either a positive or negative relationship between a trainee firefighter's risk preference (as measured by a Risky-Conservative Choice Test) and subsequent occupational success. In Experiment 1 (N = 70), all subjects wrote a causal explanation of the apparent relationship before being debriefed; the quality (general causal principle vs. case-specific restatement) of these explanations was correlated with post-debriefing belief perseverance. In Experiment 2 (N = 62), the presence or absence of the explanation task was experimentally manipulated in a 2 (positive vs. negative relationship) × 3 (no debrief / debrief without explanation / debrief with prior explanation) design. Dependent measures assessed perceived criterion validity, generalization to new cases, and generalization to new test items; composite Z-scores were the primary outcome.

## Key results
Experiment 1: Subjects in debriefed conditions continued to endorse theories consistent with their initially induced beliefs even after full discrediting; the Relationship × Debriefing interaction was non-significant (F(1,63) = 1.59), indicating that debriefing produced only a minimal reduction in belief strength. An internal analysis found a significant point-biserial correlation (r = .44, p < .0005) between the presence of a general explanatory principle in subjects' explanations and post-debriefing perseverance. Experiment 2 confirmed perseverance in both explanation and no-explanation debriefed conditions (both significant at p < .001) while showing that explanation significantly enhanced perseverance relative to debriefing without explanation (Explanation × Relationship interaction: F(1,54) = 7.86, p < .01). Importantly, perseverance was observed even in the absence of explicit explanation instructions, ruling out explanation as a necessary precondition while establishing it as a significant amplifier.

## Relevance to this research
This paper is directly relevant to the social-influence dynamics modeled in the multi-agent VFE framework. In that framework, agents update beliefs through a variational free-energy objective that weights incoming evidence against prior expectations; the "theory perseverance" phenomenon can be interpreted as a high prior strength or low likelihood sensitivity that resists Bayesian updating even when the likelihood term is explicitly nullified. The causal explanation mechanism maps onto the generation of internal generative models (causal scripts) that, once instantiated, continue to contribute to the prior belief distribution independently of the originating evidence — an analog of the divergence term KL(q || p) maintaining a mode near the initially induced belief even after the evidence likelihood has collapsed. The findings also bear on opinion dynamics and social contagion: they show that the mechanism by which inter-agent influence propagates (explanation/narrative generation) substantially modulates resistance to subsequent counter-evidence, which is a key consideration for equilibrium and convergence properties in multi-agent active inference models. The debriefing paradigm's partial effectiveness (beliefs shift but not to baseline) parallels the bounded rationality and prior stickiness one would expect from agents minimizing VFE under non-flat priors.

## Cross-links
- Concepts: [[Belief Updating]], [[Social Influence]], [[Causal Explanation]], [[Bayesian Inference]]
- Related sources: [[ross1975perseverance]], [[lord1979biased-assimilation]]
- Manuscript/Project: [[VFE Transformer Program]], [[MAgent Model]]

## BibTeX
```bibtex
@article{anderson1980perseverance,
  author  = {Anderson, Craig A. and Lepper, Mark R. and Ross, Lee},
  title   = {Perseverance of Social Theories: The Role of Explanation in the Persistence of Discredited Information},
  journal = {Journal of Personality and Social Psychology},
  year    = {1980},
  volume  = {39},
  number  = {6},
  pages   = {1037--1049},
}
```
