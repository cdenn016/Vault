---
type: reference
title: "What Type of Inference is Active Inference?"
aliases: ["nuijten2026type"]
authors: ["Wouter W. L. Nuijten", "Mykola Lukashchuk", "Thijs van de Laar", "Bert de Vries"]
year: 2026
venue: "Proceedings of the 42nd Conference on Uncertainty in Artificial Intelligence (UAI 2026)"
arxiv: "2606.04935"
url: "https://arxiv.org/abs/2606.04935"
tags: [cluster/vfe, cluster/multi-agent, project/multi-agent, field/cs-ml, field/statistics]
created: 2026-11-10
updated: 2026-11-10
---
# What Type of Inference is Active Inference?

> [!info] Citation
> Nuijten, W. W. L., Lukashchuk, M., van de Laar, T., de Vries, B. (2026). *What Type of Inference is Active Inference?*. Proceedings of the 42nd Conference on Uncertainty in Artificial Intelligence (UAI 2026), PMLR 337, 5003-5039. [arXiv](https://arxiv.org/abs/2606.04935)

[Local PDF](../pdfs/nuijten-2026-what-type-inference.pdf), 37 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper shows that the variational free energy of a generative model augmented with epistemic priors equals the free energy of the predictive model plus entropy-correction terms, and that expected-free-energy planning needs these epistemic corrections together with a planning correction.

## Problem & setting

Active inference unifies goal-directed and information-seeking behavior through the expected free energy (EFE). Earlier work, cited in the introduction, wrote EFE minimization as variational free energy (VFE) minimization on a model with epistemic priors, which places it inside a marginal variational objective but does not yet give planning over policies. Planning-as-inference methods, by contrast, lack an explicit epistemic drive.

## Method

The authors prove the decomposition of the augmented-model VFE and combine two entropy corrections: the epistemic corrections from earlier work by the same group and a planning correction from other work, which turns marginal inference into policy optimization. They derive a message-passing scheme, with simpler ablations, in which each added entropy term induces a channel reparameterization that resolves the circularity of posterior-dependent epistemic priors.

## Key results

The paper gives a full variational characterization of EFE-based planning and states which corrections cross-entropy planning and full EFE planning need. In three grid-world experiments, the authors report that full EFE planning outperforms ablations that omit either correction.

## Relevance to this research

The manuscript cites this paper in its open-problems section, noting that the authors leave a convergence theory for their channel updates open, alongside a distinction among formulations of the expected free energy made by other authors. The manuscript's reading record confirms bibliographic data only and says the paper was not read. The topic connects to [[Expected Free Energy]], [[Variational free energy]], [[Belief Propagation]] and [[Active Inference]].

## Cross-links

[[Collective agents literature map]]; [[Expected Free Energy]]; [[Variational free energy]]; [[Belief Propagation]]; [[Active Inference]].

## BibTeX

```bibtex
@inproceedings{nuijten2026type,
  author        = {Nuijten, Wouter W. L. and Lukashchuk, Mykola and van de Laar, Thijs and de Vries, Bert},
  title         = {What Type of Inference is Active Inference?},
  booktitle     = {Proceedings of the 42nd Conference on Uncertainty in Artificial Intelligence ({UAI} 2026)},
  series        = {Proceedings of Machine Learning Research},
  volume        = {337},
  pages         = {5003--5039},
  publisher     = {PMLR},
  year          = {2026},
  url           = {https://proceedings.mlr.press/v337/nuijten26a.html},
  eprint        = {2606.04935},
  archivePrefix = {arXiv}
}
```
