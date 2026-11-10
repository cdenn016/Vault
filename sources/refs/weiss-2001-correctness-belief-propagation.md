---
type: reference
title: "Correctness of Belief Propagation in Gaussian Graphical Models of Arbitrary Topology"
aliases: ["weiss2001correctness"]
authors: ["Yair Weiss", "William T. Freeman"]
year: 2001
venue: "Neural Computation"
doi: "10.1162/089976601750541769"
url: "https://doi.org/10.1162/089976601750541769"
tags: [cluster/multi-agent, cluster/vfe, project/multi-agent, field/cs-ml, field/statistics]
created: 2026-11-10
updated: 2026-11-10
---
# Correctness of Belief Propagation in Gaussian Graphical Models of Arbitrary Topology

> [!info] Citation
> Weiss, Y., Freeman, W. T. (2001). *Correctness of Belief Propagation in Gaussian Graphical Models of Arbitrary Topology*. Neural Computation, 13(10), 2173-2200. [DOI](https://doi.org/10.1162/089976601750541769)

No local copy: no open-access file passed validation on November 10, 2026. Reading basis: abstract.

## TL;DR

An analysis of loopy belief propagation when the graph's nodes are jointly Gaussian, with an analytical relation between true and loopy posteriors, sufficient conditions for convergence, and the result that converged propagation gives correct posterior means on any topology.

## Problem & setting

Belief propagation is guaranteed correct on singly connected graphs, and loopy versions perform well empirically, but the abstract says there had been little theory beyond graphs with a single loop.

## Method

The authors derive a formula relating the true posterior to the one computed by loopy propagation for Gaussian models, and state sufficient conditions for convergence.

## Key results

Per the abstract, when propagation converges the posterior means are correct for all graph topologies. The abstract does not state the same for variances.

## Relevance to this research

The manuscript cites this paper for correct means of Gaussian belief propagation when it converges, alongside the walk-summability result for convergence, and places loopy Gaussian propagation and track fusion, where double counting is classical, as the known end of a ladder from literal reading to exact fusion. See [[Gaussian Belief Propagation]], [[Belief Propagation]], [[Conservative information fusion]] and [[Decentralized Bayesian inference]].

## Cross-links

[[Collective agents literature map]]; [[Gaussian Belief Propagation]]; [[Belief Propagation]]; [[Conservative information fusion]]; [[Decentralized Bayesian inference]].

## BibTeX

```bibtex
@article{weiss2001correctness,
  author  = {Weiss, Yair and Freeman, William T.},
  title   = {Correctness of Belief Propagation in {Gaussian} Graphical Models of Arbitrary Topology},
  journal = {Neural Computation},
  volume  = {13},
  number  = {10},
  pages   = {2173--2200},
  year    = {2001},
  doi     = {10.1162/089976601750541769}
}
```
