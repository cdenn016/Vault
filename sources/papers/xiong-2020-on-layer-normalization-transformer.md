---
type: paper
title: On Layer Normalization in the Transformer Architecture
aliases:
  - "Xiong et al. 2020 — On Layer Normalization in the Transformer"
  - "Pre-LN vs Post-LN"
authors:
  - Xiong R.
  - Yang Y.
  - He D.
  - Zheng K.
  - Zheng S.
  - Xing C.
  - Zhang H.
  - Lan Y.
  - Wang L.
  - Liu T.-Y.
year: 2020
arxiv: "2002.04745"
url: https://arxiv.org/abs/2002.04745
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
created: 2026-06-20
updated: 2026-06-20
---

# On Layer Normalization in the Transformer Architecture

> [!info] Citation
> Ruibin Xiong, Yunchang Yang, Di He, Kai Zheng, Shuxin Zheng, Chen Xing, Huishuai Zhang, Yanyan Lan, Liwei Wang, and Tie-Yan Liu (2020). *On Layer Normalization in the Transformer Architecture.* ICML 2020 (PMLR vol. 119), pp. 10524–10533. arXiv:[2002.04745](https://arxiv.org/abs/2002.04745).

## TL;DR

Xiong and colleagues give a mean-field gradient analysis that explains *why* the original Transformer is so brittle to train and how a one-line change to where layer normalization sits fixes it. In the original **Post-LN** placement — normalization applied *after* the residual addition, $x_{\ell+1} = \mathrm{LN}(x_\ell + \mathrm{SubLayer}(x_\ell))$ — the expected gradient of the parameters near the output layer scales with depth at initialization, so the loss surface near the start of training is steep and a large learning rate diverges; this is precisely why the canonical recipe needs a **learning-rate warm-up** stage. Moving normalization *inside* the residual branch — **Pre-LN**, $x_{\ell+1} = x_\ell + \mathrm{SubLayer}(\mathrm{LN}(x_\ell))$ — makes the expected gradients well-scaled and depth-independent at initialization. The practical payoff is that Pre-LN Transformers train **stably without warm-up**, tolerate larger learning rates, and reach comparable quality with markedly less tuning. The paper is the reference that turned "where does the LayerNorm go" from folklore into a gradient-flow argument, and it is why nearly every modern large model is Pre-LN.

## Problem & setting

The Transformer of [[vaswani-2017-attention]] is, in practice, finicky: training diverges unless the optimizer is eased in with a warm-up schedule that ramps the learning rate from near zero, and the final result is sensitive to the warm-up length and peak rate. These knobs cost compute and tuning effort, yet the original paper offered no first-principles account of why they are needed. The authors localize the cause to the placement of the residual layer normalization. The original architecture is **Post-LN**: each sublayer's output is added to its input and the *sum* is then normalized, so the normalization sits on the residual highway itself. The competing **Pre-LN** variant normalizes the input *before* it enters the sublayer and leaves the residual path un-normalized, so the identity shortcut runs clean from input to output. The question is which placement yields gradients that a first-order optimizer can follow from a standard random initialization, and the setting is the usual supervised sequence-transduction and language-model training regimes (machine translation, BERT-style pretraining).

## Method

The analysis is a mean-field / expected-gradient calculation at initialization. Treating the weights as random and propagating second moments through the stack, the authors compute how the magnitude of the gradient with respect to parameters in each layer depends on the network depth $L$. For **Post-LN**, the expected gradient norm at the layers near the output is large — it does not stay $O(1)$ as depth grows — so at step zero the parameters closest to the loss receive outsized updates; a large global learning rate then overshoots and the run diverges, which is exactly the regime warm-up was introduced to tame. For **Pre-LN**, the same calculation shows the expected gradients are bounded independently of depth, because the un-normalized residual path keeps the forward signal and its backward gradient on a stable scale. The structural reason is that in Pre-LN the identity branch carries the signal undisturbed and the LayerNorm only rescales what is *fed into* the sublayer, whereas in Post-LN every residual sum is re-normalized, repeatedly rescaling the very pathway gradients must travel. The claims are stated as scaling results on the expected gradient and corroborated empirically by measuring gradient magnitudes across layers at initialization.

## Key results

- **Post-LN gradients blow up near the output at initialization.** The expected gradient of the output-adjacent parameters grows with depth, theoretically explaining the divergence that warm-up exists to prevent. Pre-LN gradients are, by contrast, well-scaled and depth-stable.
- **Pre-LN removes the warm-up requirement.** Pre-LN Transformers train stably from a large learning rate with no warm-up stage, whereas the same configuration destabilizes Post-LN.
- **Less tuning, less time, comparable quality.** Across machine translation (IWSLT/WMT) and unsupervised pretraining (BERT), Pre-LN reaches results comparable to the warm-up-tuned Post-LN baseline while needing fewer hyperparameters and less training time.
- **Diagnosis, not just a swap.** The contribution is the gradient-flow *explanation* tying a known training pathology to a specific architectural choice, which is why the result generalized far beyond the exact models tested.

## Relevance to this research

The why for this note is that the Pre-LN versus Post-LN gradient analysis is the canonical account of how normalization *placement* governs transformer training stability, and that question maps onto the residual-temperature and normalization-placement design choices discussed in the GL(K) attention manuscript — which is why both the gauge-theory audit lens and the transformer-ML review lens (`audit-transformer-ml`, `debate-expert-transformer-ml`) cite it. The connections are specific but interpretive.

- **Residual scale as a free temperature.** The Pre-LN insight is that what travels the residual highway must be kept on a stable scale, and that the LayerNorm acts as a learned rescaling gate on the sublayer input rather than on the highway itself. In the VFE transformer the analogous degree of freedom is the *residual temperature* and the precision-weighting that sets how strongly each belief update is admitted; this paper is the cleanest demonstration that getting that scale wrong is a depth-amplified gradient pathology, not a cosmetic detail. See [[VFE Transformer Program]].
- **Normalization placement in a no-NN model.** The model is no-NN and does not contain a literal LayerNorm module; its native analogue of normalization is the Gaussian belief precision (the inverse covariance $\Sigma^{-1}$) that re-weights tokens by inferred confidence, in the spirit of [[Precision weighting]]. This paper sharpens the question of *where* in the iterative VFE update a normalization-like rescaling should act so that the per-layer transport stays well-conditioned across depth — the same depth-stability concern, reframed for belief transport rather than backprop through residual blocks.
- **A backprop-flow result for a model that is permitted backprop.** The program forbids neural-network layers but does permit backprop to compute VFE gradients for its learned-scalar toggles. To the extent those toggles are trained through a deep stack of transport steps, the depth-scaling lesson here — keep the expected gradient $O(1)$ in depth or pay with instability — is the relevant warning, even though the architecture being differentiated is geometric rather than an MLP stack.

> [!note] Editorial: The links to residual temperature, precision-weighting, and belief-transport conditioning are bridges this research program draws; the paper itself is strictly about LayerNorm placement in a standard MLP-and-attention Transformer trained by backprop, and proves a scaling statement about expected gradients at initialization rather than a claim about Gaussian-belief models. Its sibling primitive note [[ba-2016-layer-normalization]] (Layer Normalization) is being catalogued alongside this one in the same ingest batch.

## Cross-links

- Concepts: [[Mechanistic interpretability of attention]]
- Theme: [[Attention mechanisms — theory and positional structure]]
- Related sources: [[vaswani-2017-attention]], [[dong-2021-rank-collapse]], [[geshkovski-2023-mathematical-transformers]]
- Project: [[VFE Transformer Program]]

## BibTeX

```bibtex
@inproceedings{xiong2020layernorm,
  title     = {On Layer Normalization in the Transformer Architecture},
  author    = {Xiong, Ruibin and Yang, Yunchang and He, Di and Zheng, Kai and
               Zheng, Shuxin and Xing, Chen and Zhang, Huishuai and Lan, Yanyan and
               Wang, Liwei and Liu, Tie-Yan},
  booktitle = {Proceedings of the 37th International Conference on Machine Learning (ICML)},
  series    = {Proceedings of Machine Learning Research},
  volume    = {119},
  pages     = {10524--10533},
  year      = {2020},
  eprint    = {2002.04745},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url       = {https://arxiv.org/abs/2002.04745}
}
```
