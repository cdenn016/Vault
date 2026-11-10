---
type: reference
title: "Belief Sharing: A Blessing or a Curse"
aliases: ["catal2025belief"]
authors: ["Ozan Çatal", "Toon Van de Maele", "Riddhi J. Pitliya", "Mahault Albarracin", "Candice Pattisapu", "Tim Verbelen"]
year: 2025
venue: "Active Inference: 5th International Workshop, IWAI 2024, Oxford, UK, September 9–11, 2024, Revised Selected Papers"
doi: "10.1007/978-3-031-77138-5_8"
arxiv: "2407.02465"
url: "https://doi.org/10.1007/978-3-031-77138-5_8"
tags: [cluster/multi-agent, cluster/vfe, project/multi-agent, field/cs-ml, field/neuroscience]
created: 2026-11-10
updated: 2026-11-10
---
# Belief Sharing: A Blessing or a Curse

> [!info] Citation
> Çatal, O., Van de Maele, T., Pitliya, R. J., Albarracin, M., Pattisapu, C., Verbelen, T. (2025). *Belief Sharing: A Blessing or a Curse*. In Active Inference: 5th International Workshop, IWAI 2024, Oxford, UK, September 9-11, 2024, Revised Selected Papers (Communications in Computer and Information Science, vol. 2193), pp. 121-133. Springer, Cham. [DOI](https://doi.org/10.1007/978-3-031-77138-5_8), [arXiv](https://arxiv.org/abs/2407.02465)

[Local PDF](../pdfs/catal-2025-belief-sharing-blessing.pdf), 13 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper models communication between active-inference agents as belief sharing, in which one agent's beliefs become an observation modality for another. It argues that sharing posterior beliefs naively produces echo chambers and self-doubt, and proposes sharing likelihood information instead.

## Problem & setting

Under active inference, agents minimize variational free energy with respect to a generative model, and communication at the lowest level is cast as turning one agent's beliefs into data for another. The paper states that how best to turn beliefs into observations is open.

## Method

The authors summarize the active-inference model (a POMDP-style generative model, variational free energy, and expected free energy for planning) and use it to model communication between agents. They contrast naive sharing of posteriors with an alternative in which the shared quantity is likelihood information, so that another agent's observations count as additional independent evidence. The introduction lists an analysis of the failure modes, the likelihood-sharing proposal, and validation by simulations in collaborative tasks; the simulation details were not read.

## Key results

The paper reports, as its contributions, that naive posterior sharing leads agents to reinforce each other's biases (echo chambers) and to discount their own observations in favor of shared but incorrect beliefs (self-doubt), and that sharing likelihoods mitigates both. The evidence read here is the abstract and introduction, so the strength of the simulation support is not assessed.

## Relevance to this research

The manuscript cites the paper as a related active-inference model of communication. It reads a partner's belief taken as an observation as literal reading in its own taxonomy of interpretation levels, and says the paper shows this produces echo chambers that sharing likelihoods removes. The manuscript identifies this as the double counting of one of its hypotheses, in a discrete model. The manuscript says it knew the paper through its abstract and secondary accounts. See [[Active inference communication and collective boundaries]], [[Echo chambers and polarization]], [[Collective active inference]] and [[Active Inference]].

## Cross-links

[[Collective agents literature map]]; [[Active inference communication and collective boundaries]]; [[Echo chambers and polarization]]; [[Collective active inference]]; [[Active Inference]].

## BibTeX

```bibtex
@incollection{catal2025belief,
  author        = {{\c{C}}atal, Ozan and Van de Maele, Toon and Pitliya, Riddhi J. and Albarracin, Mahault and Pattisapu, Candice and Verbelen, Tim},
  title         = {Belief Sharing: A Blessing or a Curse},
  booktitle     = {Active Inference: 5th International Workshop, {IWAI} 2024, Oxford, UK, September 9--11, 2024, Revised Selected Papers},
  series        = {Communications in Computer and Information Science},
  volume        = {2193},
  pages         = {121--133},
  publisher     = {Springer},
  address       = {Cham},
  year          = {2025},
  doi           = {10.1007/978-3-031-77138-5_8},
  eprint        = {2407.02465},
  archivePrefix = {arXiv}
}
```
