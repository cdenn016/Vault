---
type: paper
title: "An Optimization-centric View on Bayes' Rule: Reviewing and Generalizing Variational Inference"
aliases:
  - "knoblauch-2022-generalized-variational-inference"
  - "Knoblauch2022-generalized-variational-inference"
  - "knoblauch2022generalizedvariationalinference"
authors:
  - "Knoblauch, Jeremias"
  - "Jewson, Jack"
  - "Damoulas, Theodoros"
year: 2022
url: https://jmlr.org/papers/v23/19-1047.html
venue: "Journal of Machine Learning Research"
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/statistics
  - field/cs-ml
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# An Optimization-centric View on Bayes' Rule: Reviewing and Generalizing Variational Inference

> [!info] Citation
> Knoblauch, Jeremias, Jewson, Jack, Damoulas, Theodoros (2022). "An Optimization-centric View on Bayes' Rule: Reviewing and Generalizing Variational Inference." Journal of Machine Learning Research. https://jmlr.org/papers/v23/19-1047.html

## TL;DR
Reframes Bayesian inference as the solution to an optimization problem — the Rule of Three (loss, divergence, feasible set) — yielding Generalized Variational Inference (GVI). By varying the loss, the regularizing divergence, and the variational family, it recovers standard variational Bayes as a special case while enabling robust, prior-misspecification-tolerant, and computationally tractable generalizations.

## Relevance to this research
Generalizes the variational free-energy objective central to the program: it shows the accuracy+complexity (loss+divergence) decomposition is one point in a broad design space, justifying alternative divergences and loss functions (e.g. generalized/Gibbs posteriors) used to motivate the VFE attention and belief-update rules.

## Cross-links
[[Variational free energy]], [[Generalized Bayes]]

## BibTeX
```bibtex
@article{knoblauch2022generalizedvariationalinference,
  title={An Optimization-centric View on Bayes' Rule: Reviewing and Generalizing Variational Inference},
  author={Knoblauch, Jeremias and Jewson, Jack and Damoulas, Theodoros},
  journal={Journal of Machine Learning Research},
  volume={23},
  number={132},
  pages={1--109},
  year={2022}
}
```
