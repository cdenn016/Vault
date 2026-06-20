---
type: paper
title: Leakage and the reproducibility crisis in machine-learning-based science
aliases:
  - "Kapoor, Narayanan 2023"
  - "Leakage and the Reproducibility Crisis in ML"
authors:
  - Sayash Kapoor
  - Arvind Narayanan
year: 2023
arxiv: 2207.07048
url: https://doi.org/10.1016/j.patter.2023.100804
tags:
  - cluster/methodology
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Leakage and the reproducibility crisis in machine-learning-based science

> [!info] Citation
> Kapoor, S., & Narayanan, A. (2023). Leakage and the reproducibility crisis in machine-learning-based science. Patterns, 4(9), 100804. DOI 10.1016/j.patter.2023.100804. arXiv:2207.07048.

## TL;DR

Across the quantitative sciences, researchers increasingly defend scientific claims by reporting the predictive performance of a machine-learning model, and Kapoor and Narayanan show that a single methodological failure — data leakage, where information that would be unavailable at genuine prediction time contaminates the training procedure — has produced a sprawling, cross-disciplinary reproducibility crisis. Surveying existing reviews, they document leakage in seventeen fields collectively affecting at least 294 papers, many reaching wildly overoptimistic conclusions. Their constructive contribution is twofold: a fine-grained taxonomy of eight types of leakage spanning textbook errors to open research problems, and a standardized reporting instrument, the *model info sheet*, that forces an author to certify, item by item, that none of the eight failure modes is present before a performance claim is published. A reproducibility study of civil war prediction makes the stakes concrete — once leakage is corrected, the complex ML models that were believed to vastly outperform classical logistic regression do not perform substantively better than decades-old regression baselines.

## Problem & setting

The paper restricts its scope precisely: *ML-based science*, meaning research that advances a scientific claim using the measured performance of an ML model as the evidence. This is deliberately distinguished from ML methods research, ML ethics, engineering deployments, and prediction contests, where the epistemic standards and failure modes differ. The motivating observation is a feedback loop of overoptimism: pitfalls in applying ML inflate reported performance, non-replicable findings tend to be cited more than replicable ones, and the inflated results then propagate the predictive paradigm into fields ill-equipped to audit it. The prior art the work builds on is the broader replication crisis in statistics-based science together with scattered, field-specific reports of leakage; the contribution is to unify those reports under one causal mechanism — spurious correlation between outcome and features that does not survive to genuine out-of-sample data — and to give that mechanism an operational, auditable structure.

## Method

The taxonomy organizes the eight leakage types under three top-level causes. The first, **[L1] lack of clean separation of training and test data**, covers four textbook errors: using no held-out test set at all ([L1.1]); performing pre-processing such as imputation or over/under-sampling on the full dataset before splitting ([L1.2]); conducting feature selection on the full dataset ([L1.3]); and duplicate records that place the same instance in both splits ([L1.4]). The second cause, **[L2] the model uses illegitimate features**, has no subcategories because the judgment is irreducibly domain-specific — a feature that is a proxy for the outcome (the canonical example being anti-hypertensive medication as a predictor of hypertension) leaks because it would not be available, or would render the task trivial, at real prediction time. The third cause, **[L3] the test set is not drawn from the distribution of scientific interest**, splits into temporal leakage, where the test set contains data predating the training set for a forward-prediction task ([L3.1]); non-independence between train and test samples, such as multiple observations of the same patient or proteins from one family split across the partition ([L3.2]); and sampling bias in the test distribution, including spatial bias and selection bias that make the evaluation set unrepresentative of the population about which claims are made ([L3.3]). The *model info sheet* operationalizes this taxonomy: rather than leaving leakage detection to chance review, it asks the authors to state, for each category, the precise justification (training/test separation, the legitimacy argument for every feature, the match between the evaluation distribution and the claimed scientific distribution) — a documentation artifact functioning as a pre-registered severe test against each known way the performance number could be an artifact.

## Key results

The central empirical findings are a survey result and a case study. The survey aggregates prior reviews to establish breadth: leakage has been found in seventeen fields, collectively affecting at least 294 papers in the published *Patterns* version (the earlier arXiv preprint reports a higher figure of 329, reflecting a different accounting). The case study supplies depth and the strongest causal demonstration. In civil war prediction, several published papers claimed that complex ML models — random forests, gradient-boosted trees and the like — dramatically outperform traditional logistic regression. Kapoor and Narayanan reproduce these analyses, identify leakage in each, and show that once the errors are corrected the complex models do not perform substantively better than the decades-old regression baselines, with the headline ML-over-LR advantage collapsing. The evidence is strong for the qualitative claim that leakage is widespread and consequential, and the civil war study is a clean falsification of specific superiority claims; the survey counts are best read as a documented lower bound on prevalence rather than an exhaustive census, since they aggregate whatever prior reviews happened to exist.

## Relevance to this research

This paper supplies the concrete severe-test and selection-effect instrument the program needs whenever it claims that the gauge-theoretic VFE transformer beats a vanilla transformer or a VFE_2.0 baseline. A reported advantage is corroboration only if it survives the eight leakage checks; the model info sheet is the auditable form in which to certify that the golden-test parity ablations, the train/test partitioning, and the choice of evaluation distribution did not manufacture the gap. The taxonomy is the empirical, ML-meta counterpart to the philosophy-of-science demarcation question catalogued under [[Structural realism and philosophy of science]] — it converts "is this claim honestly evidenced?" into a finite checklist of selection effects to rule out. It joins Sculley 2015 (hidden technical debt) and Hooker 2020 (the hardware lottery) as the methodological-hygiene layer of the vault, with a sharper warning: the most dangerous leakage here is [L3], distribution mismatch, because a streaming belief-update architecture evaluated on data that shares structure with its training stream can report a generalization advantage that is really non-independence ([L3.2]) or temporal leakage ([L3.1]) rather than a property of the variational mechanism.

## Cross-links

- Concepts / Themes: [[Structural realism and philosophy of science]]
- Project: [[VFE Transformer Program]]

## BibTeX

```bibtex
@article{kapoornarayanan2023leakage,
  author  = {Kapoor, Sayash and Narayanan, Arvind},
  title   = {Leakage and the reproducibility crisis in machine-learning-based science},
  journal = {Patterns},
  volume  = {4},
  number  = {9},
  pages   = {100804},
  year    = {2023},
  doi     = {10.1016/j.patter.2023.100804},
  note    = {arXiv:2207.07048}
}
```
