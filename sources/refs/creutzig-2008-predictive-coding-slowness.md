---
type: reference
title: "Predictive Coding and the Slowness Principle: An Information-Theoretic Approach"
aliases: ["creutzig2008predictive"]
authors: ["Felix Creutzig", "Henning Sprekeler"]
year: 2008
venue: "Neural Computation"
doi: "10.1162/neco.2008.01-07-455"
url: "https://doi.org/10.1162/neco.2008.01-07-455"
tags: [cluster/multi-agent, cluster/vfe, cluster/info-geometry, project/multi-agent, field/neuroscience, field/statistics]
created: 2026-11-10
updated: 2026-11-10
---
# Predictive Coding and the Slowness Principle: An Information-Theoretic Approach

> [!info] Citation
> Creutzig, F., Sprekeler, H. (2008). *Predictive Coding and the Slowness Principle: An Information-Theoretic Approach*. Neural Computation, 20(4), 1026-1041. [DOI](https://doi.org/10.1162/neco.2008.01-07-455)

No local copy: no open-access file passed validation on November 10, 2026. Reading basis: abstract and manuscript reading record.

## TL;DR

The paper relates two principles of sensory coding, predictive coding and slowness, by stating an information-bottleneck objective for temporally local predictive coding and showing that linear slow feature analysis is a variant of it.

## Problem & setting

Predictive coding holds that sensory systems encode information about future inputs. Slow feature analysis extracts slowly varying components from quickly varying signals. The paper asks how these two principles are related.

## Method

The authors use the information bottleneck method to write an information-theoretic objective for temporally local predictive coding.

## Key results

The abstract states that the linear case of slow feature analysis can be read as a variant of predictive coding that maximizes the mutual information between the current output and the input at the next time step. The authors conclude that the two principles are closely related.

## Relevance to this research

The Collective Agents manuscript cites the paper as a precedent for selecting slow features by a predictive-information criterion at one time step, and says what its own construction adds is at most the dependence on horizon and control. The manuscript's reading record states that the paper was read only through its abstract. It connects to [[Predictive Coding]], [[Information bottleneck]] and [[Mutual information]].

## Cross-links

[[Collective agents literature map]]; [[Predictive Coding]]; [[Information bottleneck]]; [[Mutual information]]; [[creutzig-2009-past-future-information]].

## BibTeX

```bibtex
@article{creutzig2008predictive,
  author  = {Creutzig, Felix and Sprekeler, Henning},
  title   = {Predictive Coding and the Slowness Principle: An Information-Theoretic Approach},
  journal = {Neural Computation},
  volume  = {20},
  number  = {4},
  pages   = {1026--1041},
  year    = {2008},
  doi     = {10.1162/neco.2008.01-07-455}
}
```
