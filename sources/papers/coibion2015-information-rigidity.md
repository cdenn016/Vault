---
type: paper
title: "Information Rigidity and the Expectations Formation Process: A Simple Framework and New Facts"
aliases:
  - "Coibion 2010"
  - "Coibion Gorodnichenko FIRE"
authors:
  - Coibion, Olivier
  - Gorodnichenko, Yuriy
year: 2010
arxiv: null
url: http://www.nber.org/papers/w16537
tags:
  - cluster/social-physics/social-influence
  - project/social-physics
  - field/economics
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Information Rigidity and the Expectations Formation Process: A Simple Framework and New Facts

> [!info] Citation
> Coibion, Olivier and Gorodnichenko, Yuriy (2010). "Information Rigidity and the Expectations Formation Process: A Simple Framework and New Facts." NBER Working Paper No. 16537. http://www.nber.org/papers/w16537.

## TL;DR
This paper proposes a novel test of full-information rational expectations (FIRE) grounded in two theoretical models of informational rigidities — sticky information (Mankiw-Reis) and imperfect information (Kalman-filter signal extraction). The central insight is that under either model, the ex post mean forecast error is linearly predicted by the ex ante mean forecast revision, with a coefficient that maps one-to-one into the underlying degree of information rigidity. Applying this framework to U.S. and cross-country professional forecaster survey data, the authors find pervasive and economically significant informational rigidities, with implied information-update durations of six to seven months, and document state-dependence in the expectations formation process.

## Problem & setting
Standard tests of FIRE (regressing forecast errors on lagged variables) suffer from data-mining concerns, provide no guidance about which alternative model best describes departures from the null, and do not quantify the economic significance of those departures. Prior empirical work on informational frictions was either restricted to inflation forecasts or required structural shock identification. The authors seek a parsimonious, theoretically motivated specification applicable across agents, variables, and countries that simultaneously tests FIRE and recovers a structural measure of information rigidity.

## Method
Both the sticky-information model and the Kalman-filter imperfect-information model yield the same reduced-form prediction. Let $\bar{F}_t x_{t+h}$ denote the mean forecast across agents and $\bar{F}_{t-1} x_{t+h}$ the previous period's mean. The key regression is

$$x_{t+h} - \bar{F}_t x_{t+h} = \alpha + \beta (\bar{F}_t x_{t+h} - \bar{F}_{t-1} x_{t+h}) + \varepsilon_t,$$

where under FIRE $\beta = 0$, while under informational rigidities $\beta = \lambda/(1-\lambda) > 0$ (sticky information, $\lambda$ = probability of not updating) or $\beta = (1-G)/G > 0$ (imperfect information, $G$ = Kalman gain). The coefficient $\beta$ thus serves as a structural identifier of rigidity magnitude under either model. The approach is applied to the U.S. Survey of Professional Forecasters (1969–2010, inflation and four other macro variables), Consensus Economics cross-country data (G-7 and additional countries, 1989–), consumers, and financial market participants.

## Key results
Estimating the baseline specification on U.S. inflation SPF data yields $\hat{\beta} = 1.23$ (s.e. 0.50), strongly rejecting FIRE in the direction predicted by informational-rigidity models. The implied structural parameters are $\hat{\lambda} \approx 0.55$ (sticky information: average update every 6–7 months) or Kalman gain $G < 0.5$ (imperfect information: less than half the weight placed on new information). Pooling across macro variables and forecasting horizons sharpens rejection. Cross-country Consensus Economics data yield nearly identical $\hat{\beta}$. The degree of information rigidity varies systematically across variables in a manner consistent with imperfect-information (persistence and signal-noise ratio predict cross-sectional variation in $\hat{\beta}$, accounting for 20–30% of variance), favoring imperfect-information over sticky-information as the better model. Time-variation analysis reveals that information rigidity fell during high-volatility 1970s–early 1980s and has risen since the Great Moderation, consistent with rational inattention under reduced macroeconomic volatility. Recessions and highly visible shocks (9/11) exhibit state-dependence: rigidity decreases sharply after large salient events.

## Relevance to this research
This paper is relevant to the VFE transformer and multi-agent active inference program primarily through the Kalman-filter signal extraction framework. The imperfect-information Kalman gain $G$ is structurally analogous to the belief-update weighting in variational free energy minimization: agents performing Bayesian updating under precision-weighted prediction errors correspond directly to the signal extraction agents here, and the "degree of information rigidity" $(1-G)/G$ parallels the ratio of prior precision to likelihood precision in the VFE E-step. The framework for measuring departures from full-information updating across a population of agents also connects to multi-agent active inference, where heterogeneous precision (attention weights $\beta_{ij}$) governs how strongly each agent updates beliefs toward neighbors. The state-dependence results (rigidity falls under large shocks) mirror attention sharpening under high prediction error in the VFE formulation. For the social-physics / opinion-dynamics thread, this paper provides an empirically grounded macro-level instance of collective belief inertia modulated by environmental volatility — directly analogous to how opinion clusters persist under low social noise and dissolve under high-salience shocks.

## Cross-links
- Concepts: [[Kalman Filter]], [[Variational Free Energy]], [[Predictive Coding]], [[Information Rigidity]], [[Rational Inattention]]
- Related sources: [[mankiw2002-sticky-information]], [[woodford2001-imperfect-information]], [[sims2003-rational-inattention]]
- Manuscript/Project: [[VFE Transformer Program]], [[Multi-Agent Active Inference]]

## BibTeX
```bibtex
@techreport{coibion2015,
  author      = {Coibion, Olivier and Gorodnichenko, Yuriy},
  title       = {Information Rigidity and the Expectations Formation Process: A Simple Framework and New Facts},
  institution = {National Bureau of Economic Research},
  year        = {2010},
  type        = {Working Paper},
  number      = {16537},
  url         = {http://www.nber.org/papers/w16537},
}
```
