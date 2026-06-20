---
type: paper
title: "On a Kinetic Model for a Simple Market Economy"
aliases: ["Cordier, Pareschi & Toscani 2005", "Kinetic Model for a Simple Market Economy"]
authors: ["Cordier S.", "Pareschi L.", "Toscani G."]
year: 2005
url: https://doi.org/10.1007/s10955-005-5456-0
tags: [cluster/social-physics, project/social-physics, field/physics, field/economics, field/mathematics, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# On a Kinetic Model for a Simple Market Economy

> [!info] Citation
> Cordier, S., Pareschi, L. & Toscani, G. (2005). *On a Kinetic Model for a Simple Market Economy*. Journal of Statistical Physics **120**(1–2), 253–277. DOI: [10.1007/s10955-005-5456-0](https://doi.org/10.1007/s10955-005-5456-0).

## TL;DR
The methodological parent of Toscani's opinion kinetics, applied to **wealth** rather than belief. Agents exchange money through conservative binary trades that, on average, preserve total wealth but include a stochastic (risky-investment) component. Writing a Boltzmann-type equation for the wealth density and passing to a quasi-invariant (grazing) trade limit, the authors derive a Fokker-Planck equation whose stationary distribution exhibits a **Pareto power-law tail** — the heavy-tailed wealth distribution observed empirically — arising endogenously from conservative, noisy binary exchanges.

## What it establishes
For wealth $v\ge 0$, a binary trade $(v, w)$ produces post-trade wealths
$$ v' = (1-\gamma)\,v + \gamma\,w + \eta\,v, \qquad w' = (1-\gamma)\,w + \gamma\,v + \tilde\eta\,w, $$
where $\gamma$ is the saving propensity and $\eta,\tilde\eta$ are centered random multipliers modeling the risk of market investment. Total wealth is conserved in the mean. The density $f(v,t)$ obeys a Boltzmann equation, and the grazing limit yields the Fokker-Planck equation
$$ \partial_t f = \tfrac{1}{2}\,\partial_v^2\!\big[ v^2 f \big] + \partial_v\!\big[ (v - m)\, f \big], $$
whose steady state is an inverse-Gamma distribution with an algebraic (Pareto) tail $f(v)\sim v^{-(1+\mu)}$, the exponent $\mu$ set by the ratio of saving to risk. This established the now-standard pairwise-interaction-plus-grazing-limit recipe that the opinion kinetics later inherited.

## Relevance to this research
This is the methodological parent of Toscani's opinion kinetics: the identical pairwise-interaction-plus-grazing-limit recipe that the opinion (and hence the program-adjacent) models inherit, here proven out on wealth exchange. Its enduring lesson for the program is that **heavy-tailed, non-Gaussian stationary distributions emerge naturally from conservative noisy binary interactions** — directly relevant if the program's belief distributions ever leave the Gaussian family and develop fat tails under repeated stochastic interaction, where a single Gaussian $q_i = N(\mu_i,\Sigma_i)$ would no longer be a faithful summary. Honestly this is adjacent: it concerns wealth, not belief, and carries no gauge or information-geometric structure, so it serves the program as a cautionary and methodological reference about stationary-distribution shape rather than as a piece of the VFE functional.

## Cross-links
- Concept: [[Kinetic theory of opinion dynamics]]
- Related sources: [[toscani-2006-kinetic-opinion]], [[pareschi-toscani-2013-interacting-multiagent]]

## BibTeX
```bibtex
@article{cordier2005kinetic,
  author  = {Cordier, St\'{e}phane and Pareschi, Lorenzo and Toscani, Giuseppe},
  title   = {On a Kinetic Model for a Simple Market Economy},
  journal = {Journal of Statistical Physics},
  volume  = {120},
  number  = {1--2},
  pages   = {253--277},
  year    = {2005},
  doi     = {10.1007/s10955-005-5456-0}
}
```
