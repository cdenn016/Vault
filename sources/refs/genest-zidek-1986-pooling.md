---
type: reference
title: "Combining Probability Distributions: A Critique and an Annotated Bibliography"
aliases:
  - "Genest & Zidek 1986"
  - "Genest-Zidek (1986) Pooling"
authors:
  - Christian Genest
  - James V. Zidek
year: 1986
tags:
  - cluster/social-physics
  - cluster/multi-agent
  - project/multi-agent
  - project/social-physics
  - field/statistics
  - cluster/social-physics/opinion-dynamics
created: 2026-06-19
updated: 2026-06-19
---

# Combining Probability Distributions: A Critique and an Annotated Bibliography

> [!info] Citation
> Genest, C., & Zidek, J. V. (1986). "Combining Probability Distributions: A Critique and an Annotated Bibliography." *Statistical Science* **1**(1), 114–135. DOI: [10.1214/ss/1177013825](https://doi.org/10.1214/ss/1177013825).

## TL;DR

The canonical survey and taxonomy of **opinion pooling** — how to combine several probability distributions over a common space into one. It systematizes the field into the two principal families that still organize the literature: the **linear opinion pool** (a weighted arithmetic average, $p = \sum_i w_i p_i$) and the **logarithmic opinion pool** (a weighted normalized geometric mean, $p \propto \prod_i p_i^{w_i}$), together with the axiomatic properties (marginalization, external Bayesianity, the zero-preservation/veto property, unanimity) that distinguish them. It remains the standard map of which pooling operator satisfies which desideratum.

## What it establishes

Genest & Zidek lay out the axioms a pooling rule might be asked to satisfy and show how they force a family. The **marginalization property** (pooling commutes with computing marginals) characterizes the linear pool; **external Bayesianity** (pooling commutes with Bayesian updating on shared evidence) characterizes the logarithmic pool. Linear pooling preserves unanimous unconditional assignments and is consensus-respecting but is not externally Bayesian; logarithmic pooling is externally Bayesian and zero-preserving (any expert can veto an event by assigning it probability zero) but does not marginalize. The review also surveys supra-Bayesian and weight-elicitation approaches and supplies the annotated bibliography that became the field's reference list.

## Why the project cites it

This is the work [[participatory-it-from-bit]] cites by name (`GenestZidek1986`) to frame its **barycenter / pooling choice**. PIFB invokes the *log-linear pool* explicitly: in the multi-generation hyperprior, the strictly-normalized special case $\lambda_0 = 1-\rho$ enforces $\sum_k \lambda_k = 1$ and "recovers the externally-Bayesian log-linear pool of Genest & Zidek," with the Gaussian pooled precision $\Sigma_\star^{-1} = \sum_k \lambda_k \Sigma_k^{-1}$. The taxonomy is what lets the manuscript state precisely which pooling regime each part of the model uses: the externally-Bayesian logarithmic pool for the discounted-KL ancestral stack, versus the consensus-preserving *linear* (sandwich) average for meta-agent coarse-graining in [[Meta-agents and hierarchical emergence]]. It is the umbrella reference for the more specialized [[bordley-1982-multiplicative-pooling]] (log-pool derivation), [[hinton-2002-products-of-experts|hinton-2002-poe]] (product-of-experts), and [[dietrich-list-2016-opinion-pooling]] (axiomatic adjudication) that the project also cites.

```bibtex
@article{genest1986combining,
  author  = {Genest, Christian and Zidek, James V.},
  title   = {Combining Probability Distributions: A Critique and an Annotated Bibliography},
  journal = {Statistical Science},
  volume  = {1},
  number  = {1},
  pages   = {114--135},
  year    = {1986},
  doi     = {10.1214/ss/1177013825},
  publisher = {Institute of Mathematical Statistics}
}
```
