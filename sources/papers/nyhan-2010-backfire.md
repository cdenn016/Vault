---
type: paper
title: "When Corrections Fail: The Persistence of Political Misperceptions"
aliases:
  - "Nyhan 2010"
  - "Backfire Effect"
authors:
  - Nyhan, Brendan
  - Reifler, Jason
year: 2010
arxiv: null
url: https://doi.org/10.1007/s11109-010-9112-2
tags:
  - cluster/social-physics/opinion-dynamics
  - cluster/social-physics/social-influence
  - project/social-physics
  - field/psychology
  - field/sociology
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# When Corrections Fail: The Persistence of Political Misperceptions

> [!info] Citation
> Nyhan, Brendan, and Jason Reifler (2010). "When Corrections Fail: The Persistence of Political Misperceptions." *Political Behavior* 32: 303–330. https://doi.org/10.1007/s11109-010-9112-2

## TL;DR
This paper presents four experiments testing whether factual corrections embedded in realistic mock news articles reduce political misperceptions. Corrections frequently fail to reduce misperceptions among the ideologically committed groups most likely to hold them, and in several cases produce a "backfire effect" in which corrections actually strengthen the misperception among those subjects. The results are interpreted through a motivated reasoning / goal-directed information processing framework.

## Problem & setting
Political misperceptions — false or unsubstantiated beliefs about political facts (e.g., Iraqi WMD stockpiles, tax-cut revenue effects, the scope of stem-cell research policy) — are distinct from simple ignorance and resist standard fact-checking. Prior work tested corrections delivered authoritatively by survey interviewers, not in realistic media contexts. The paper asks whether corrections embedded in news reports, the format citizens actually encounter, can shift factual beliefs, and whether ideology moderates that effect.

## Method
Four between-subjects experiments were conducted in 2005–2006 with undergraduate samples. Participants read mock newspaper articles containing a misleading political claim, randomly assigned to versions with or without an immediately following correction. Dependent variable: agreement with a misperception statement on a 5-point Likert scale. The core regression model is:

Y = b0 + b1·Correction + b2·Ideology + b3·(Correction × Ideology) + b4·Knowledge

where Ideology is a 7-point liberal-to-conservative scale and Knowledge is a 5-item factual quiz. The interaction coefficient b3 tests whether the correction's effectiveness varies by ideology (Hypothesis 1). A positive marginal effect (b1 + b3·Ideology > 0) for the sympathetic ideological subgroup constitutes the backfire prediction (Hypothesis 2b). OLS regression is used throughout; ordered probit results are substantively identical. Topics covered: Iraqi WMD (two iterations), Bush tax cuts and revenue, and the Bush stem cell research "ban."

## Key results
In Study 1 (fall 2005, WMD), the correction × ideology interaction is significant (p < 0.01) and positive: among conservatives, the correction increased belief in Iraqi WMD (raw data show agreement rising from 32% in controls to 64% in the correction condition). Very liberal subjects updated correctly; centrists and moderate liberals were unaffected. In Study 2 (spring 2006), the WMD backfire did not replicate for conservatives — possibly reflecting elite cue shifts by early 2006 — but the interaction structure was again significant. The tax-cut experiment showed corrections failing to move conservative misperceptions and in some specifications producing backfire. The stem cell experiment tested a liberal misperception, finding again that corrections failed for the ideologically sympathetic group. Media source (NYT vs. FoxNews.com) did not significantly moderate correction effects in any experiment. Issue importance moderated backfire on WMD: among conservatives who rated Iraq as the most important issue, the backfire was strongest (three-way interaction p < 0.05).

## Relevance to this research
This paper belongs to the social-physics / opinion-dynamics literature that the VFE multi-agent framework is designed to model. Several connections are worth noting. First, the "backfire effect" is a concrete empirical instance of non-Bayesian belief update: agents with strong priors generate counter-arguments that reinforce, rather than revise, prior beliefs when confronted with disconfirming evidence — directly analogous to the failure of naive free-energy minimization when the agent's prior coupling (alpha·KL(q||p)) dominates the observation likelihood. Second, the ideology-moderated interaction maps cleanly onto the multi-agent attention structure: the coupling weights beta_ij encode who influences whom, and ideologically sorted social networks produce block-diagonal effective coupling — agents within an ideological cluster attend heavily to each other and resist out-cluster information. Third, the motivated reasoning mechanism (counterarguing → attitude bolstering) echoes the tau-scaled attention entropy term in the VFE functional: a high-certainty agent (low tau) concentrates beta on in-group peers, making the observation likelihood term too weak to pull beliefs toward corrective evidence. Quantitative modeling of backfire onset and decay as a function of prior strength and social-network topology is a natural downstream application of the multi-agent VFE framework.

## Cross-links
- Concepts: [[Motivated Reasoning]], [[Belief Updating]], [[Opinion Dynamics]], [[Social Influence]]
- Related sources: [[lord-1979-biased-assimilation]], [[taber-2006-motivated-skepticism]]
- Manuscript/Project: [[VFE Transformer Program]], [[MAgent Model]]

## BibTeX
```bibtex
@article{Nyhan2010,
  author  = {Nyhan, Brendan and Reifler, Jason},
  title   = {When Corrections Fail: The Persistence of Political Misperceptions},
  journal = {Political Behavior},
  year    = {2010},
  volume  = {32},
  pages   = {303--330},
  doi     = {10.1007/s11109-010-9112-2},
}
```
