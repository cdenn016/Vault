---
type: paper
title: "Exposure to opposing views on social media can increase political polarization"
aliases: ["Bail et al. 2018", "Exposure to opposing views (Twitter bot experiment)"]
authors: ["Bail C. A.", "Argyle L. P.", "Brown T. W.", "Bumpus J. P.", "Chen H.", "Hunzaker M. B. F.", "Lee J.", "Mann M.", "Merhout F.", "Volfovsky A."]
year: 2018
url: https://doi.org/10.1073/pnas.1804840115
tags: [cluster/social-physics, project/social-physics, field/sociology, field/psychology, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# Exposure to opposing views on social media can increase political polarization

> [!info] Citation
> Bail, C. A., Argyle, L. P., Brown, T. W., Bumpus, J. P., Chen, H., Hunzaker, M. B. F., Lee, J., Mann, M., Merhout, F., & Volfovsky, A. (2018). *Exposure to opposing views on social media can increase political polarization*. Proceedings of the National Academy of Sciences (PNAS) 115(37):9216-9221. DOI: [10.1073/pnas.1804840115](https://doi.org/10.1073/pnas.1804840115).

## TL;DR
A preregistered randomized field experiment that paid Democratic and Republican Twitter users to follow a bot retweeting messages from elected officials, opinion leaders, and organizations of the opposing party for one month. Rather than moderating attitudes as the naive contact hypothesis would predict, sustained exposure to the other side hardened them: Republicans who followed a liberal bot became substantially more conservative, and Democrats who followed a conservative bot became marginally (non-significantly) more liberal. The study is a clean causal demonstration that cross-cutting exposure can backfire.

## What it establishes
The design isolates the causal effect of cross-ideological exposure by random assignment, with attitudes measured on a multi-item liberal-conservative scale before and after treatment. Letting $\Delta\theta_i$ be the post-minus-pre shift in agent $i$'s issue position and $x$ the (oppositely signed) signal injected by the bot, the contact hypothesis predicts $\operatorname{sign}(\Delta\theta_i)=\operatorname{sign}(x-\theta_i)$ (movement toward the source). The experiment instead found $\operatorname{sign}(\Delta\theta_i)=-\operatorname{sign}(x-\theta_i)$ for Republicans — a backlash, or boomerang, response in which the perturbation amplifies rather than reduces the pre-existing displacement, with a monotone dose-response in self-reported bot engagement.

## Relevance to this research
This is a strong, direct empirical test of the inertia thesis. A first-order DeGroot/Friedkin-Johnsen averaging flow is contractive — any cross-cutting signal must pull a belief toward the source — so it structurally cannot produce backlash. The program's underdamped (inertial) regime, $M\ddot{\mu}+\gamma\dot{\mu}+\nabla F=0$, can: belief momentum and overshoot, plus identity-driven repulsive coupling in which the attention weight $\beta_{ij}$ on a dissonant neighbor becomes negative or the effective transported divergence is maximized rather than minimized, predict amplified displacement under perturbation. Honestly, the paper supplies a phenomenon the program must explain, not machinery it uses; reproducing this boomerang qualitatively would be a real, falsifiable win for the underdamped ansatz over overdamped opinion dynamics.

## Cross-links
- Concept: [[Echo chambers and polarization]]
- Related: [[Belief inertia]], [[Hamiltonian belief dynamics]], [[Opinion dynamics]]
- Related sources: [[guess-2023-feed-algorithms-election]], [[bakshy-2015-ideological-diversity-facebook]], [[sunstein-2002-law-of-group-polarization]]

## BibTeX
```bibtex
@article{bail2018exposure,
  author  = {Bail, Christopher A. and Argyle, Lisa P. and Brown, Taylor W. and Bumpus, John P. and Chen, Haohan and Hunzaker, M. B. Fallin and Lee, Jaemin and Mann, Marcus and Merhout, Friedolin and Volfovsky, Alexander},
  title   = {Exposure to opposing views on social media can increase political polarization},
  journal = {Proceedings of the National Academy of Sciences},
  volume  = {115},
  number  = {37},
  pages   = {9216--9221},
  year    = {2018},
  doi     = {10.1073/pnas.1804840115}
}
```
