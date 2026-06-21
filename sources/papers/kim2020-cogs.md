---
type: paper
title: "COGS: A Compositional Generalization Challenge Based on Semantic Interpretation"
aliases:
  - "Kim 2020"
  - "COGS"
authors:
  - Kim, Najoung
  - Linzen, Tal
year: 2020
arxiv: "2010.05465"
url: https://arxiv.org/abs/2010.05465
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/psychology
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# COGS: A Compositional Generalization Challenge Based on Semantic Interpretation

> [!info] Citation
> Kim, Najoung and Linzen, Tal (2020). "COGS: A Compositional Generalization Challenge Based on Semantic Interpretation." arXiv:2010.05465 [cs.CL].

## TL;DR
COGS is a synthetic semantic parsing dataset designed to evaluate compositional generalization in neural language models. It maps English sentences to logical forms and contains a held-out generalization set that requires out-of-distribution generalization via systematic compositional principles. Both Transformers and LSTMs achieve near-perfect in-distribution accuracy (96–99%) but poor generalization accuracy (16–35%), with high sensitivity to random seed, demonstrating that standard NLP architectures lack robust compositional generalization capacity.

## Problem & setting
Standard neural sequence-to-sequence models perform well in-distribution but fail to generalize compositionally — that is, they cannot reliably interpret novel combinations of familiar primitives and structures, even when humans find such combinations trivially inferrable. Prior benchmarks like SCAN (Lake and Baroni, 2018) used only simple synthetic navigation commands and could not probe the full range of natural-language grammatical abstractions. COGS addresses this by grounding compositional generalization in formal English semantics (lambda-calculus-based logical forms), covering a broader set of syntactic constructions including argument structure alternations, recursive embedding, and modifier placement.

## Method
The dataset is generated from a Probabilistic Context-Free Grammar (PCFG) over a fragment of English covering approximately 70–80% of naturally-occurring English sentence types. Logical forms follow a Neo-Davidsonian event semantics adapted from Reddy et al. (2017), with indexed Skolem constants grounded to word positions to reduce the out-of-vocabulary label problem. The training and generalization sets are constructed to differ systematically: the generalization set contains five categories of novel combinations — (1) novel combinations of familiar primitives and grammatical roles (e.g., a noun seen only as subject appearing as object), (2) novel combinations of modified phrases and grammatical roles, (3) deeper recursive nesting (depth 3–12 vs. 0–2 in training), (4) verb argument structure alternations (active/passive, transitive/intransitive, dative alternation), and (5) verb class sensitivity (unaccusative vs. unergative). The training set has 24,155 examples and the generalization set 21,000. Transformer (9.5M params, 2 encoder/decoder layers, 4 heads) and LSTM (bidirectional and unidirectional, 10–11M params) models are evaluated in an encoder-decoder sequence-to-sequence framework without any pretraining.

## Key results
In-distribution test accuracy was 96–99% for all three architectures, with negligible variance across random seeds. Generalization accuracy was 35% for Transformer, 32% for unidirectional LSTM, and only 16% for bidirectional LSTM, all with standard deviation of 6–8% across seeds. Structural generalization (novel combinations of familiar syntactic structures, deeper recursion, modifier role shifts) was dramatically harder than lexical generalization (familiar primitives in familiar structures but unseen role assignments): structural cases produced near-zero accuracy across all models. Active-to-passive was the one exception for Transformers, achieving near-100% accuracy; LSTMs made structurally correct errors on that case while Transformers made fewer but more idiosyncratic structural errors. Increasing model size fivefold did not help generalization, and sometimes hurt it. Increasing primitive exposure examples from 1 to 100 substantially improved lexical generalization (Transformer rose from 35% to 63%) but did not help structural generalization.

## Relevance to this research
COGS is not directly about variational free energy or gauge-equivariant attention, but it is relevant to the VFE transformer research program in several ways. First, the Transformer architecture evaluated in COGS (Vaswani et al., 2017) is precisely the architecture the VFE transformer is designed to replace or reinterpret through iterative VFE minimization over Gaussian belief tuples. COGS results provide a concrete empirical data point about where standard softmax-attention Transformers fail: they lack structural compositionality, which in the VFE framework may be related to the absence of geometry-aware belief transport. Second, the compositionality problem — whether a model's representations combine in a principled, structure-sensitive way — is analogous to the gauge-equivariance requirement in GL(K) attention: both demand that the model respect certain structural symmetries (grammatical role structure vs. gauge group action) when generalizing to unseen inputs. Third, the failure of scale to fix generalization aligns with the VFE program's thesis that architectural inductive bias (here, gauge-equivariant belief transport) matters more than parameter count. The paper is a useful external baseline motivating why attention mechanisms need richer structural priors.

## Cross-links
- Concepts: [[Compositionality]], [[Attention Mechanism]], [[Sequence-to-Sequence Models]]
- Related sources: [[vaswani2017attention]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{kim2020cogs,
  author  = {Kim, Najoung and Linzen, Tal},
  title   = {{COGS}: A Compositional Generalization Challenge Based on Semantic Interpretation},
  journal = {arXiv preprint arXiv:2010.05465},
  year    = {2020},
  url     = {https://arxiv.org/abs/2010.05465},
}
```
