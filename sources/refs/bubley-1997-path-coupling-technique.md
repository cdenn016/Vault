---
type: reference
title: "Path coupling: A technique for proving rapid mixing in Markov chains"
aliases: ["bubley1997path"]
authors: ["R. Bubley", "M. Dyer"]
year: 1997
venue: "Proceedings 38th Annual Symposium on Foundations of Computer Science"
doi: "10.1109/SFCS.1997.646111"
url: "https://doi.org/10.1109/SFCS.1997.646111"
tags: [cluster/multi-agent, project/multi-agent, field/cs-ml, field/mathematics]
created: 2026-11-10
updated: 2026-11-10
---

# Path coupling: A technique for proving rapid mixing in Markov chains

> [!info] Citation
> Bubley, R., Dyer, M. (1997). *Path coupling: A technique for proving rapid mixing in Markov chains*. Proceedings 38th Annual Symposium on Foundations of Computer Science, 223-231. [DOI](https://doi.org/10.1109/SFCS.1997.646111)

No local copy: no open-access file passed validation on November 10, 2026. Reading basis: abstract and manuscript reading record.

## TL;DR

A conference paper introducing path coupling, a variant of the coupling technique for bounding the mixing rates of Markov chains used in Markov chain Monte Carlo.

## Problem & setting

According to the abstract, approximating #P-hard counting problems by Markov chain Monte Carlo rests on bounding the mixing rates of the chains involved, and earlier coupling arguments needed detailed combinatorial insight into each problem.

## Method

The abstract describes path coupling as a way to reduce the combinatorial difficulty of coupling proofs and to give simpler convergence proofs than standard coupling.

## Key results

The abstract states that the method is applied to graph colouring, TWICE-SAT, the antiferromagnetic Potts model and the hard-core lattice gas, giving either new rapid-mixing proofs or simplifications of existing ones.

## Relevance to this research

The collective-agents manuscript cites this paper for the attribution of the path-coupling argument, which it writes out in its own proof of a contraction bound for a Wasserstein distance on member-change paths. The reading record states that the paper was not read, so the attribution rests on the abstract and the bibliographic record. The link to the vault is mixing of the stochastic dynamics that a collective's members follow, see [[Markov chain Monte Carlo]], [[Multi-agent variational free energy]] and [[Collective active inference]].

## Cross-links

[[Collective agents literature map]]; [[Markov chain Monte Carlo]]; [[Multi-agent variational free energy]]; [[Collective active inference]].

## BibTeX

```bibtex
@inproceedings{bubley1997path,
  author    = {Bubley, R. and Dyer, M.},
  title     = {Path coupling: A technique for proving rapid mixing in {Markov} chains},
  booktitle = {Proceedings 38th Annual Symposium on Foundations of Computer Science},
  pages     = {223--231},
  publisher = {IEEE Computer Society},
  year      = {1997},
  doi       = {10.1109/SFCS.1997.646111}
}
```
