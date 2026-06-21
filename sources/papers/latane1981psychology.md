---
type: paper
title: "The Psychology of Social Impact"
aliases:
  - "Latane 1981"
  - "Social Impact Theory"
  - "SIT"
authors:
  - Latane, Bibb
year: 1981
arxiv: null
url: https://doi.org/10.1037/0003-066X.36.4.343
tags:
  - cluster/social-physics/social-influence
  - project/social-physics
  - field/psychology
  - field/sociology
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# The Psychology of Social Impact

> [!info] Citation
> Latane, B. (1981). "The Psychology of Social Impact." *American Psychologist*, 36(4), 343–356. https://doi.org/10.1037/0003-066X.36.4.343

## TL;DR
Latane proposes a formal theory of social impact specifying how other persons affect an individual through three principles: impact as a multiplicative function of source strength, immediacy, and number (I = f(SIN)); a psychosocial power law I = sN^t with t < 1 (diminishing marginal returns of additional people); and division of impact when multiple people share a target role, yielding I = sN^{-t}. The theory is validated across ten empirical domains spanning conformity, stage fright, bystander inhibition, tipping, and crowding in rats.

## Problem & setting
The paper addresses the lack of a unified quantitative framework for the diverse ways that people affect one another — conformity, social facilitation, diffusion of responsibility, social loafing, and related phenomena. Prior work (Asch on conformity, Darley–Latane on bystander intervention) had identified these effects but lacked a common mathematical structure. Latane draws on earlier quantitative social science by Dodd, Stewart, Zipf, Lewin, and Stevens to synthesize a single theory.

## Method
The theory rests on an analogy between social forces and physical forces (light, gravity, magnetism) operating in a social force field. Three formal principles are stated:

**Principle 1 — Multiplication of impact:** When N sources of strength S and immediacy I act on a target,
$$I = f(S \cdot I \cdot N).$$

**Principle 2 — Psychosocial law:** Impact follows a power function of the number of sources,
$$I = s N^t, \quad t < 1,$$
so each additional person contributes less than the previous (marginal diminishing returns, analogous to Stevens's psychophysical power law $\psi = K\phi^\beta$).

**Principle 3 — Division of impact:** When multiple people stand together as co-targets of an external force,
$$I = s / N^t \equiv s N^{-t}, \quad t < 1,$$
so the per-person impact decreases as the group grows.

Power functions are tested by logarithmic linearization (log I = log s + t log N) with standard regression, giving exact estimates of the exponent t and goodness-of-fit r^2. Ten empirical applications are reviewed, each fitting the predicted inverse or direct power function.

## Key results
Across ten domains the data are consistent with a power law with exponent t < 1:

- Conformity (Gerard et al. 1968): I = 14 N^{0.46}, r^2 = .80 (conformity grows as square root of majority size).
- Crowd imitation / gawking (Milgram et al. 1969): exponent ≈ 0.24, r^2 = .90 (fourth root).
- Stage fright (Latane & Harkins 1976): exponent ≈ 0.52 (square root of audience size); multiplicative with audience status, no interaction in log units.
- News interest (Bassett & Latane): I grows as N^{0.5}, r^2 = .99 (square root of persons involved).
- Bystander inhibition (Darley & Latane 1968): helping speed decreases as cube root of bystanders believed present.
- Elevator helping (Latane & Dabbs 1975): individual help rate = 48 N^{-0.5}, r^2 = .94 (inverse square root).
- Tipping (Freeman et al. 1975): tip percentage = s N^{-0.2} (inverse fifth root of party size).
- Billy Graham inquiries (Wilson 1970): percent inquiring = s N^{-0.3} (inverse cube root of crowd size), r^2 not stated but clearly decreasing.
- Social loafing / shouting (Latane, Williams & Harkins 1979): individual effort = s N^{-1/6} (inverse sixth root of pseudogroup size).
- Crowding in rats (Latane, Cappell & Joy 1970): sociability ∝ N^{-1/3} (inverse cube root).

The finding that the sign of the exponent (positive vs. negative) is determined by whether the individual is source-side target or co-target, and that |t| < 1 consistently, is the central empirical contribution.

## Relevance to this research
Social Impact Theory is a foundational quantitative model for social influence that feeds directly into the social-physics stream of the VFE/MAgent research program in several ways.

**Formal connection to the VFE attention mechanism.** The attention weights beta_{ij} in the GL(K) free energy aggregate social force across agents j acting on agent i, and the attention-entropy term tau * sum_{ij} beta_{ij} log(beta_{ij}/pi_{ij}) regularises this aggregation. The psychosocial law's diminishing marginal returns (I = sN^t, t < 1) is structurally analogous to the concavity that the entropic softmax introduces: in both cases, the incremental influence of an additional agent is sub-linear. Latane's multiplicative principle (I ∝ S · I · N) maps to the multiplicative factorisation of attention (strength, proximity/immediacy, count) implicit in the dot-product softmax kernel.

**Division of impact and diffusion of responsibility.** When multiple agents share a target (Principle 3, I = sN^{-t}), the per-agent impact is reduced — exactly the social-loafing and diffusion-of-responsibility mechanism. In the multi-agent VFE model this manifests as: when many agents share a common observation, the likelihood gradient is divided among them, reducing each agent's individual update. The negative-exponent regime maps onto the shared-target coupling in the model-level (gamma_{ij}) or observation-likelihood terms.

**Social-physics bridge to opinion dynamics.** SIT is an upstream empirical foundation for bounded-confidence opinion-dynamics models (Hegselmann–Krause, Deffuant) and Latane's own later Dynamic Social Impact Theory (1996), which is a direct precursor to the collective belief updating treated in the MAgent / social-physics manuscripts. The power-law scaling across ten domains provides empirical grounding for why opinion-field models use sub-linear influence kernels.

**Participatory / observer-dependence angle.** Latane notes the theory does not explain mechanisms, only aggregate laws — an epistemological humility parallel to the participatory realism stance in the PIFB manuscript, where observer-relative coarse-graining produces emergent social structure without requiring a microscopic mechanistic account.

## Cross-links
- Concepts: [[Social Influence]], [[Opinion Dynamics]], [[Power Law]], [[Diffusion of Responsibility]], [[Social Loafing]]
- Related sources: [[hegselmann2002opinion]], [[deffuant2000mixing]], [[latane1996dynamic]]
- Manuscript/Project: [[MAgent Model]], [[PIFB]], [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{latane1981psychology,
  author  = {Latane, Bibb},
  title   = {The Psychology of Social Impact},
  journal = {American Psychologist},
  year    = {1981},
  volume  = {36},
  number  = {4},
  pages   = {343--356},
  doi     = {10.1037/0003-066X.36.4.343},
}
```
