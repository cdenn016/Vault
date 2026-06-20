---
type: paper
title: "Opinions and Social Pressure"
aliases: ["Asch 1955", "Asch conformity experiments"]
authors: ["Asch S. E."]
year: 1955
url: https://doi.org/10.1038/scientificamerican1155-31
tags: [cluster/social-physics, project/social-physics, field/psychology, cluster/social-physics/social-influence]
created: 2026-06-19
updated: 2026-06-19
---

# Opinions and Social Pressure

> [!info] Citation
> Solomon E. Asch (1955). *Opinions and social pressure*. Scientific American, 193(5), 31–35 (companion: 1951 chapter "Effects of group pressure upon the modification and distortion of judgments" in H. Guetzkow, ed., *Groups, Leadership and Men*, Carnegie Press). DOI: 10.1038/scientificamerican1155-31.

## TL;DR
Asch's line-judgment paradigm is the canonical demonstration that a unanimous but incorrect majority can drive a substantial fraction of people to publicly endorse a manifestly wrong perceptual judgment. A naive participant, seated among confederates who unanimously give the same wrong answer on an unambiguous task (matching a target line to one of three comparison lines), conforms on roughly a third of critical trials, and about three-quarters of participants conform at least once. The experiments isolate the power of social pressure from genuine perceptual ambiguity, since the correct answer is obvious in control conditions where participants err under 1% of the time.

## What it establishes
The central finding is that public conformity emerges even when private perception is clear, and that conformity depends sharply on the *unanimity* and *size* of the opposing majority. Conformity rises as the majority grows from one to three or four confederates and then plateaus; a single dissenting ally who breaks unanimity collapses conformity dramatically, restoring near-independent responding. Asch interprets the responses as a mixture of distortion of judgment, distortion of action (knowing the right answer but going along publicly), and, more rarely, distortion of perception. If we write an individual's expressed judgment as a compromise between a private perceptual estimate $o_i$ and the social signal from the majority $\bar{x}_{-i}$, the experiment shows the social term can dominate even when the perceptual evidence is high-precision and unambiguous.

## Relevance to this research
This is the empirical anchor for the claim that the social-coupling term in the VFE functional must be strong enough to override the observation-likelihood term — that $\beta_{ij}\,\mathrm{KL}(q_i \,\|\, \Omega_{ij} q_j)$ coupling can dominate $\mathbb{E}_q[\log p(o\mid x)]$ even when the likelihood is sharp. It grounds the human-behavior phenomenology the overdamped flow is meant to reproduce and directly motivates the conformity and echo-chamber regimes: a unanimous neighborhood collapses an agent's belief toward the consensus, while a single dissenting neighbor (an alternative coupling target) restores independence. The unanimity/ally effect is a concrete falsifiable prediction for the coupling graph's topology. See [[Social influence and conformity]], [[Echo chambers and polarization]], and [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Social influence and conformity]]
- Related sources: [[deutsch-gerard-1955-normative-informational-influence]], [[bond-smith-1996-culture-and-conformity]], [[sherif-1936-psychology-social-norms]]

## BibTeX
```bibtex
@article{asch1955opinions,
  author  = {Asch, Solomon E.},
  title   = {Opinions and Social Pressure},
  journal = {Scientific American},
  year    = {1955},
  volume  = {193},
  number  = {5},
  pages   = {31--35},
  doi     = {10.1038/scientificamerican1155-31}
}
```
