---
type: paper
title: The Impact of Positional Encoding on Length Generalization in Transformers
aliases:
  - "Kazemnejad et al. 2023 — NoPE"
  - "Positional Encoding and Length Generalization"
authors:
  - Amirhossein Kazemnejad
  - Inkit Padhi
  - Karthikeyan Natesan Ramamurthy
  - Payel Das
  - Siva Reddy
year: 2023
arxiv: 2305.19466
url: https://arxiv.org/abs/2305.19466
tags:
  - cluster/attention
  - cluster/methodology
  - project/transformer
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# The Impact of Positional Encoding on Length Generalization in Transformers

> [!info] Citation
> Kazemnejad, A., Padhi, I., Natesan Ramamurthy, K., Das, P., & Reddy, S. (2023). The Impact of Positional Encoding on Length Generalization in Transformers. Advances in Neural Information Processing Systems 36 (NeurIPS 2023). arXiv:2305.19466.

## TL;DR

Length generalization — training a transformer on sequences up to some length and asking it to keep working on strictly longer ones — is widely assumed to hinge on the choice of positional encoding, yet the field had no controlled head-to-head comparison. This paper supplies one, evaluating five schemes (absolute position embeddings, T5's relative bias, ALiBi, rotary embeddings (RoPE), and no positional encoding at all) on a battery of reasoning and mathematical tasks under a decoder-only, causally-masked architecture. The central and counterintuitive finding is that the explicit encodings most used in practice — ALiBi, RoPE, and absolute embeddings — are *not* well suited to length generalization on these downstream tasks, while **NoPE (no positional encoding)** matches or beats them at zero extra cost. The authors back this with a theoretical result that a causally-masked transformer with no positional inputs can nonetheless represent both absolute and relative position internally, and an empirical probe showing that when trained with SGD the NoPE model spontaneously develops attention patterns resembling T5's relative scheme. They also report that scratchpad/chain-of-thought formatting is not a universal remedy: whether it helps depends sharply on its format.

## Problem & setting

The self-attention operation is permutation-equivariant, so a transformer must be told where each token sits. Practitioners inject this through a positional encoding, and a folk hierarchy had emerged — relative schemes (T5, ALiBi, RoPE) are believed to extrapolate to unseen lengths better than learned absolute embeddings. The setting here is *length generalization* in the strict sense: train on instances with at most $L_{\text{train}}$ tokens, then evaluate on instances longer than anything seen in training, measuring whether accuracy survives the extrapolation. Prior art (Press et al.'s ALiBi, Su et al.'s RoPE, Raffel et al.'s T5 relative bias) each motivated a particular encoding partly by appeal to extrapolation, but those claims were made on language-modeling perplexity rather than on algorithmic tasks with a clean correct/incorrect signal, and rarely against each other under a fixed architecture and training budget. The paper's contribution is the controlled comparison plus a hypothesis the prior work did not entertain: that for a decoder-only model the right amount of positional encoding might be none.

## Method

The experimental method is a matched sweep. The same decoder-only transformer backbone is trained five times, differing only in the positional-encoding module: learned absolute embeddings added to the token embeddings; the T5 relative scheme, which adds a learned scalar bias $b_{i-j}$ (bucketed by signed offset) to the pre-softmax attention logits; ALiBi, which adds a fixed head-specific linear penalty $-m_h\,|i-j|$ to those logits; RoPE, which rotates the query and key vectors of position $i$ by a position-dependent angle so that $\langle R_i q,\, R_j k\rangle$ depends only on the relative offset $i-j$; and NoPE, which injects nothing and relies on the architecture alone.

The conceptual core is the NoPE construction. Because the decoder uses a causal mask, the attention at position $i$ can only see positions $\le i$. The paper argues this is enough for the network to recover position without any explicit signal: a head whose values are constant and whose attention is (approximately) uniform over the visible prefix returns a quantity that scales with the count of attended tokens, i.e. with the absolute index $i$; once an absolute index is available at each position, the difference of two positions yields relative offset. Schematically, if a head attends uniformly to the $i$ visible tokens carrying value $v$, its output is $\tfrac{1}{i}\sum_{j\le i} v = v$ but the normalizer $i$ itself is exposed through the softmax, so absolute position is representable, and from it relative position $i-j$ follows by subtraction in a later layer. The claim is therefore that NoPE's hypothesis class *contains* both absolute and relative encodings rather than lacking positional capacity. Empirically the authors then probe the learned NoPE attention and report it resolves, under SGD, to patterns most similar to the T5 relative scheme.

## Key results

The headline empirical result is a reordering of the folk hierarchy: on the reasoning and mathematical tasks studied, NoPE generalizes to longer sequences at least as well as, and often better than, the explicit encodings, while ALiBi, RoPE, and absolute embeddings each underperform expectations set by their language-modeling reputations. The theoretical result is the representability statement — a causally-masked transformer without positional inputs can express both absolute and relative position — which converts NoPE from an apparent ablation into a principled design. The mechanistic probe supplies the third leg: the trained NoPE model behaves like a relative encoder, which both explains its competitiveness and suggests that explicit relative schemes are, on these tasks, an unnecessary inductive constraint. A secondary but practically important finding concerns scratchpads: chain-of-thought-style intermediate-work formatting does not uniformly rescue length generalization, and its *format* (how the intermediate state is written out) materially changes the outcome. The evidence is strongest as a comparative, controlled benchmark on algorithmic tasks; it is weaker as a claim about open-ended natural-language modeling, which the study does not target, and the specific ranking among the explicit schemes should be read as task-dependent rather than universal.

## Relevance to this research

This paper is the external, falsifiable baseline against which the VFE transformer's treatment of position must be judged. The program stacks several positional kernels — RoPE rotation of the belief means, an ALiBi-style distance penalty, T5 relative buckets (the `t5_relative_bias` prior with its optional learnable per-bucket table), and a gauge-composed `phi` transport — and the open question is whether these are complementary, redundant, or actively destructive when composed. Kazemnejad et al. show that on length-generalization tasks the individual explicit schemes can each be a liability and that *removing* positional encoding is a serious competitor, which directly challenges any assumption that more positional machinery is monotonically better; it argues for an ablation in which the program's positional stack is tested against a NoPE-like configuration and against each kernel in isolation. The NoPE representability argument also has a sharp methodological consequence for the program's gauge-equivariance story: because a causally-masked attention block can synthesize absolute position from the attention normalizer alone, claims that the architecture is positionally agnostic or strictly gauge-equivariant must account for this implicit channel rather than assuming position enters only through the named encodings. See [[Attention mechanisms — theory and positional structure]] for where the program's stacked kernels are catalogued.

## Cross-links

- Concepts / Themes: [[Attention mechanisms — theory and positional structure]]

## BibTeX

```bibtex
@inproceedings{kazemnejad2023positional,
  author    = {Kazemnejad, Amirhossein and Padhi, Inkit and Natesan Ramamurthy, Karthikeyan and Das, Payel and Reddy, Siva},
  title     = {The Impact of Positional Encoding on Length Generalization in Transformers},
  booktitle = {Advances in Neural Information Processing Systems 36 (NeurIPS 2023)},
  year      = {2023},
  eprint    = {2305.19466},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url       = {https://arxiv.org/abs/2305.19466}
}
```
