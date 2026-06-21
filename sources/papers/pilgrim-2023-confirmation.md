---
type: paper
title: "Confirmation bias emerges from an approximation to Bayesian reasoning"
aliases:
  - "Pilgrim 2023"
  - "BIASR model"
authors:
  - Pilgrim, Charlie
  - Sanborn, Adam
  - Malthouse, Eugene
  - Hills, Thomas T.
year: 2023
arxiv: null
url: https://doi.org/10.1016/j.cognition.2023.105693
tags:
  - cluster/social-physics/social-influence
  - cluster/social-physics/opinion-dynamics
  - project/social-physics
  - field/psychology
  - field/statistics
  - field/philosophy
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Confirmation bias emerges from an approximation to Bayesian reasoning

> [!info] Citation
> Pilgrim, C., Sanborn, A., Malthouse, E., & Hills, T. T. (2023). "Confirmation bias emerges from an approximation to Bayesian reasoning." *Cognition*, 245, 105693. https://doi.org/10.1016/j.cognition.2023.105693

## TL;DR
The BIASR model (Bayesian updating with an Independence Approximation and Source Reliability) shows that confirmation bias — defined as searching for and assimilating information that favours prior beliefs — arises naturally from boundedly rational belief updating. When agents jointly track beliefs about a central hypothesis and source reliability, simultaneous Bayesian updating introduces correlations between these beliefs; an independence (mean-field) approximation that discards those correlations introduces a systematic bias that compounds over sequential observations. A single model thereby generates biased evaluation, biased assimilation, attitude polarisation, belief perseverance, and confirmation bias in source selection.

## Problem & setting
Confirmation bias is widely observed yet poorly explained at the information-processing level. Prior models either posit irrationality without principled grounding (e.g., a discount factor on disconfirmatory evidence) or explain individual phenomena in isolation. The paper asks whether confirmation bias can emerge from a principled, boundedly rational approximation to Bayesian inference, using a minimal Bayesian network where evidence $D$ is influenced by both the true hypothesis $H$ and source reliability $R$ — a collider structure $H \to D \leftarrow R$.

## Method
The BIASR model rests on four assumptions: (1) agents maintain and update beliefs about source reliability; (2) updating is simultaneous over $H$ and $R$ using Bayes' rule on the joint $P(H,R|D) \propto P(D|H,R)P(H,R)$; (3) because maintaining the full joint distribution is cognitively intractable (memory scales as $O(k^n)$ with $n$ attributes), agents apply a mean-field independence approximation, factoring $P(H,R) \approx P(H)P(R)$ and forgetting induced correlations between beliefs; (4) data is processed sequentially, so the approximation is re-applied at each step, causing path dependence.

The independence approximation minimises KL divergence between the full joint posterior and the factored approximation — formally a variational mean-field step applied between each sequential update. Information gain from a source is quantified as expected KL divergence between prior and posterior beliefs,
$$E(I_g) = \sum_D P(D) \sum_H P(H|D)\log\frac{P(H|D)}{P(H)}.$$
The model is compared to simple Bayes (no source reliability tracking) and rational Bayesian network updating (full joint maintained) across simulated tasks.

## Key results
Under the BIASR model, five empirical phenomena are reproduced: (1) biased evaluation — confirmatory sources are judged more reliable than disconfirmatory ones ($P(R|\mathbf{D}_\text{for}) > P(R|\mathbf{D}_\text{against})$); (2) biased assimilation — belief in the hypothesis is updated more strongly than under rational updating for both confirmatory and disconfirmatory evidence; (3) attitude polarisation — agents who share identical source-reliability priors but differ only in hypothesis priors diverge after seeing the same data; (4) belief perseverance — early data has disproportionate influence, so beliefs formed on confirmatory evidence resist later disconfirmation; (5) source selection bias — the expected information gain from confirmatory sources is rated much higher under BIASR than under rational updating. Empirical alignment is demonstrated via simulation replications of Redlawsk (2002) and Carlson et al. (2006), where confirmation bias is stronger when information is processed sequentially (on-line) versus all at once (memory-based), consistent with the path-dependence prediction.

## Relevance to this research
The BIASR model is a concrete instantiation of variational mean-field approximation applied to sequential Bayesian belief updating, directly mirroring the mathematics at the core of the VFE framework. The independence approximation $P(H,R) \approx P(H)P(R)$ is precisely the factored (mean-field) variational family used in variational inference, and the paper explicitly frames this as minimising KL divergence from the true joint — the variational free energy perspective. The compounding of small approximation errors over sequential observations parallels how iterated VFE minimisation can accumulate policy-shaping biases in multi-agent active inference. The collider Bayesian network structure ($H \to D \leftarrow R$) is conceptually related to the observation-likelihood term in the VFE free-energy functional where observations are explained by both latent state beliefs and model (prior/source) reliability. The attitude polarisation result connects to social-physics models of opinion dynamics: agents with shared auxiliary priors can diverge when their central priors differ, a mechanism relevant to multi-agent belief coupling in the GL(K) attention framework. The information-gain formulation as expected KL divergence relates to the attention-entropy and belief-coupling terms in the VFE functional. The paper also provides a normative grounding for why boundedly rational agents would adopt mean-field approximations — directly relevant to justifying the independence assumptions implicit in factored VFE updates across agent layers.

## Cross-links
- Concepts: [[Variational Inference]], [[Mean Field Approximation]], [[KL Divergence]], [[Bounded Rationality]], [[Bayesian Inference]]
- Related sources: [[Social Opinion Dynamics]], [[Active Inference]]
- Manuscript/Project: [[VFE Transformer Program]], [[PIFB]]

## BibTeX
```bibtex
@article{Pilgrim2023confirmation,
  author  = {Pilgrim, Charlie and Sanborn, Adam and Malthouse, Eugene and Hills, Thomas T.},
  title   = {Confirmation bias emerges from an approximation to {Bayesian} reasoning},
  journal = {Cognition},
  volume  = {245},
  pages   = {105693},
  year    = {2024},
  note    = {Received 2023},
  doi     = {10.1016/j.cognition.2023.105693},
}
```
