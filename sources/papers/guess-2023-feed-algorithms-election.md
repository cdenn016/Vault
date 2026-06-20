---
type: paper
title: "How do social media feed algorithms affect attitudes and behavior in an election campaign?"
aliases: ["Guess et al. 2023", "Chronological vs. algorithmic feed experiment"]
authors: ["Guess A. M.", "Malhotra N.", "Pan J.", "Barbera P.", "Allcott H.", "Brown T.", "Crespo-Tenorio A.", "Dimmery D.", "Freelon D.", "Gentzkow M.", "Gonzalez-Bailon S.", "Kennedy E.", "Kim Y. M.", "Lazer D.", "Moehler D.", "Nyhan B.", "Velasco Rivera C.", "Settle J.", "Thomas D. R.", "Thorson E.", "Tromble R.", "Wilkins A.", "Wojcieszak M.", "Xiong B.", "Kiewiet de Jonge C.", "Franco A.", "Mason W.", "Stroud N. J.", "Tucker J. A."]
year: 2023
url: https://doi.org/10.1126/science.abp9364
tags: [cluster/social-physics, project/social-physics, field/sociology, field/cs-ml, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# How do social media feed algorithms affect attitudes and behavior in an election campaign?

> [!info] Citation
> Guess, A. M., Malhotra, N., Pan, J., Barbera, P., Allcott, H., Brown, T., et al. (2023). *How do social media feed algorithms affect attitudes and behavior in an election campaign?* Science 381(6656):398-404. DOI: [10.1126/science.abp9364](https://doi.org/10.1126/science.abp9364).

## TL;DR
A large, preregistered field experiment (part of the U.S. 2020 Facebook and Instagram Election Study, run in partnership with Meta) that randomly replaced consenting users' algorithmically ranked feeds with a reverse-chronological feed for roughly three months. The intervention sharply changed what users saw — chronological feeds showed more content from ideologically diverse sources and untrusted sources, and reduced time on platform — yet produced no significant change in issue polarization, affective polarization, political knowledge, or other downstream political attitudes. Large changes in exposure did not translate into changes in belief.

## What it establishes
The experiment cleanly separates the exposure channel from the attitude channel. Let $E$ denote the distribution of content a user is exposed to and $\theta$ their measured attitudes; randomizing the ranking algorithm induced a large $\Delta E$ (composition, source diversity, dwell time all shifted substantially) while the estimated treatment effect on $\theta$ was near zero and statistically insignificant across a battery of polarization and knowledge measures. The causal arrow from feed algorithm to exposure is strong; the arrow from exposure to attitudes, over a campaign-length horizon, is not detectable.

## Relevance to this research
A crucial calibration counter-anchor and a direct probe of the inertia thesis. That a large $\Delta E$ moved attitudes negligibly is exactly the belief stickiness the program's inertial (underdamped) dynamics and prior-anchoring (Friedkin-Johnsen-like) self-coupling $\alpha\,\mathrm{KL}(q_i\,\|\,p_i)$ predict: strong attachment to a prior, or large effective inertial mass read off the Fisher/precision tensor, makes the steady state insensitive to bounded changes in the driving signal. It also guards the program against overclaiming algorithmic causation — pairing it with backlash results like Bail et al. forces the model to reproduce both stickiness and overshoot from one functional, a stringent and honest constraint. Strong and recent.

## Cross-links
- Concept: [[Belief inertia]]
- Related: [[Hamiltonian belief dynamics]], [[Fisher information metric]], [[Multi-agent variational free energy]]
- Related sources: [[bail-2018-exposure-opposing-views]], [[bakshy-2015-ideological-diversity-facebook]], [[cinelli-2021-echo-chamber-effect]]

## BibTeX
```bibtex
@article{guess2023feed,
  author  = {Guess, Andrew M. and Malhotra, Neil and Pan, Jennifer and Barbera, Pablo and Allcott, Hunt and Brown, Taylor and Crespo-Tenorio, Adriana and Dimmery, Drew and Freelon, Deen and Gentzkow, Matthew and Gonzalez-Bailon, Sandra and Kennedy, Edward and Kim, Young Mie and Lazer, David and Moehler, Devra and Nyhan, Brendan and Velasco Rivera, Carlos and Settle, Jaime and Thomas, Daniel Robert and Thorson, Emily and Tromble, Rebekah and Wilkins, Arjun and Wojcieszak, Magdalena and Xiong, Beixian and Kiewiet de Jonge, Chad and Franco, Annie and Mason, Winter and Stroud, Natalie Jomini and Tucker, Joshua A.},
  title   = {How do social media feed algorithms affect attitudes and behavior in an election campaign?},
  journal = {Science},
  volume  = {381},
  number  = {6656},
  pages   = {398--404},
  year    = {2023},
  doi     = {10.1126/science.abp9364}
}
```
