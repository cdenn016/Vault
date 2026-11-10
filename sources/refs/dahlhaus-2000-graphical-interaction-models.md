---
type: reference
title: "Graphical interaction models for multivariate time series"
aliases: ["dahlhaus2000graphical"]
authors: ["Rainer Dahlhaus"]
year: 2000
venue: "Metrika"
doi: "10.1007/s001840000055"
url: "https://doi.org/10.1007/s001840000055"
tags: [cluster/multi-agent, project/multi-agent, field/statistics, field/mathematics]
created: 2026-11-10
updated: 2026-11-10
---
# Graphical interaction models for multivariate time series

> [!info] Citation
> Dahlhaus, R. (2000). *Graphical interaction models for multivariate time series*. Metrika, 51(2), 157-172. [DOI](https://doi.org/10.1007/s001840000055)

[Local PDF](../pdfs/dahlhaus-2000-graphical-interaction-models.pdf), 21 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages and manuscript reading record.

## TL;DR

The paper extends undirected conditional-independence graphs from multivariate data to multivariate time series, with edges identified by partial spectral coherence.

## Problem & setting

A graph's vertices are the components of the series, and its edges encode the partial correlation structure of two components given the others. For Gaussian series the graph is a conditional independence graph. For non-Gaussian series it is called a partial correlation graph.

## Method

The paper defines a partial correlation graph for time series and uses the partial spectral coherence between two components, given the rest, to identify edges. It proves a property of the inverse of the spectral matrix that helps identify the graph and a separation theorem equivalent to the global Markov property. Multivariate autoregressive processes serve as an example, and an air pollution data set is analyzed.

## Key results

The text extract is garbled (words split across lines), but the introduction and the outline of the paper are legible and support the description above. No numerical findings were taken from it.

## Relevance to this research

The Collective Agents manuscript cites the paper as a source of exact stationary blanket-type structure for graphical models of stationary Gaussian processes, in a list of items it does not claim as new. The manuscript's reading record states that the statement was known through the restatement in a later paper, not from this text. It connects to [[Markov Blanket]], [[Markov blanket interpretation debate]] and [[Gaussian State Space Model]].

## Cross-links

[[Collective agents literature map]]; [[Markov Blanket]]; [[Markov blanket interpretation debate]]; [[Gaussian State Space Model]].

## BibTeX

```bibtex
@article{dahlhaus2000graphical,
  author  = {Dahlhaus, Rainer},
  title   = {Graphical interaction models for multivariate time series},
  journal = {Metrika},
  volume  = {51},
  number  = {2},
  pages   = {157--172},
  year    = {2000},
  doi     = {10.1007/s001840000055}
}
```
