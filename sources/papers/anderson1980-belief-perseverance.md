---
type: paper
title: "Perseverance of Social Theories: The Role of Explanation in the Persistence of Discredited Information"
aliases:
  - Anderson 1980
  - belief perseverance
  - anderson1980perseverance
  - anderson-1980-belief-perseverance
  - Anderson Lepper Ross 1980
  - Perseverance of Social Theories
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
> Anderson, C. A., Lepper, M. R., & Ross, L. (1980). "Perseverance of Social Theories: The Role of Explanation in the Persistence of Discredited Information." *Journal of Personality and Social Psychology*, 39(6), 1037–1049. DOI: [10.1037/h0077720](https://doi.org/10.1037/h0077720).

## TL;DR
Two experiments using a debriefing paradigm demonstrate that social theories formed on minimal evidence survive complete invalidation of the formative data. The effect is substantially amplified when subjects are first asked to generate a causal explanation for the observed relationship, because the explanation becomes cognitively autonomous of the original (now-discredited) evidence base.

## Problem & setting
Prior work had shown that specific personal impressions (e.g., perceived ability) can persist after the evidence underlying them is discredited (Ross, Lepper, & Hubbard, 1975). This paper extends the phenomenon to more abstract social theories about empirical relationships between variables, asking: (1) do theories persevere even when the initiating data set is minimal and explicitly refuted, and (2) does the cognitive act of formulating a causal explanation mediate perseverance? Stanford undergraduates were given fictitious case-study evidence for either a positive or negative relationship between firefighter success and risk preference, then thoroughly debriefed about the data's fictional nature.

## Method
Experiment 1 (N = 70): 2 × 2 factorial (Positive vs. Negative relationship × Debriefing vs. No Debriefing) plus a no-information control. All experimental subjects provided a written causal explanation before debriefing. Post-debriefing beliefs were assessed via perceived criterion validity of the risk-preference scale, generalization to new cases, and generalization to new test items; these three measures were highly intercorrelated (average r ≈ 0.73) and combined into a composite Z-score.

Experiment 2 (N = 62): Six conditions crossing relationship direction (positive/negative) with three explanation × debriefing combinations (no-debriefing/no-explanation; debriefing/no-explanation; debriefing/explanation), allowing direct causal isolation of the explanation manipulation.

## Key results
In Experiment 1, debriefed subjects retained beliefs nearly as strong as non-debriefed subjects: the Relationship × Debriefing interaction was non-significant, F(1,63) = 1.59. The internal analysis revealed a highly significant point-biserial correlation (r = 0.44, p < 0.0005) between the presence of a generalized explanatory principle in the subject's written account and the degree of post-debriefing belief perseverance. In Experiment 2, theory perseverance occurred even in the debriefing/no-explanation condition (Relationship × Debriefing interaction significant, F(1,54) = 23.31, p < 0.001), and explicit explanation significantly enhanced perseverance beyond this baseline (Explanation × Relationship interaction, F(1,54) = 7.86, p < 0.05). Subjects exposed to opposing fictional data sets were equally easily induced to adopt and retain conceptually opposite beliefs, ruling out the possibility that perseverance reflects a normatively defensible prior.

> [!note] Editorial — verified statistic
> The Experiment-2 Explanation × Relationship interaction is reported in the original article as **F(1,54) = 7.86, p < .05** (the duplicate notes that disagreed — p < .01 vs p < .05 — are resolved in favour of **p < .05**). Confirmed against the primary source: Anderson, Lepper & Ross (1980), *JPSP* 39(6), 1037–1049, p. 1046, where the same paragraph states all component effects were significant at p < .05 and renders the F = 23.31 Relationship × Debriefing interaction at p < .001. Full text: author's copy at craiganderson.org (80ALR.PDF).

## Relevance to this research
This paper is directly relevant to the social-physics and opinion-dynamics components of the VFE multi-agent framework. In the gauge-theoretic VFE / active-inference setting, agents maintain belief distributions q_i over latent states; the belief-perseverance phenomenon maps onto the stability of local minima in the variational free energy landscape — once a causal explanation is encoded as a generative model structure (the "prior" p_i in the VFE), it persists as a self-reinforcing attractor even when the original sensory evidence is removed. The finding that explanation-generation mediates perseverance suggests that the depth of generative-model elaboration (analogous to the number of hierarchical layers or the specificity of prior structure in a predictive coding hierarchy) predicts resistance to belief revision. For social-influence and opinion-dynamics modeling this is a key empirical regularity: belief states do not simply track evidence but are stabilized by the internal generative structure the agent has constructed, which is exactly the kind of dynamics the multi-agent VFE coupling terms (beta_ij KL divergences) need to reproduce. The paper also anticipates the "consider-the-opposite" debiasing technique, which maps onto the meta-cognitive free-energy regulation proposed in the participatory-realism thread.

## Cross-links
- Concepts: [[Belief Perseverance]], [[Causal Explanation]], [[Social Influence]], [[Opinion Dynamics]]
- Related sources: [[ross1975-perseverance]], [[lord1979-biased-assimilation]]
- Manuscript/Project: [[VFE Transformer Program]], [[MAgent Model]]

## BibTeX
```bibtex
@article{anderson1980,
  author  = {Anderson, Craig A. and Lepper, Mark R. and Ross, Lee},
  title   = {Perseverance of Social Theories: The Role of Explanation in the Persistence of Discredited Information},
  journal = {Journal of Personality and Social Psychology},
  year    = {1980},
  volume  = {39},
  number  = {6},
  pages   = {1037--1049},
  doi     = {10.1037/h0077720},
}
```
