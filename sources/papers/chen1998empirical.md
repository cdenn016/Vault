---
type: paper
title: "An Empirical Study of Smoothing Techniques for Language Modeling"
aliases:
  - "Chen 1998"
  - "Kneser-Ney smoothing survey"
authors:
  - Chen, Stanley F.
  - Goodman, Joshua
year: 1998
arxiv: null
url: http://nrs.harvard.edu/urn-3:HUL.InstRepos:25104739
tags:
  - cluster/info-geometry
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# An Empirical Study of Smoothing Techniques for Language Modeling

> [!info] Citation
> Chen, Stanley F. and Goodman, Joshua (1998). "An Empirical Study of Smoothing Techniques for Language Modeling." Harvard Computer Science Group Technical Report TR-10-98. http://nrs.harvard.edu/urn-3:HUL.InstRepos:25104739

## TL;DR
This paper provides a comprehensive tutorial on n-gram language models and an extensive empirical comparison of smoothing techniques including Jelinek-Mercer, Katz, Witten-Bell, absolute discounting, and Kneser-Ney smoothing. The authors introduce a novel modification of Kneser-Ney smoothing (interpolated Kneser-Ney) that consistently outperforms all other evaluated algorithms across training set sizes, corpora, and n-gram orders. They also demonstrate that improved language model smoothing leads to measurable gains in downstream speech recognition word-error rate.

## Problem & setting
Maximum-likelihood n-gram models assign zero probability to unseen word sequences, catastrophically degrading performance on held-out data and downstream tasks such as speech recognition, OCR, and machine translation. Prior comparative work evaluated at most two smoothing methods on one or two corpora with a single training size, making it impossible to gauge relative algorithm performance across conditions. This paper fills that gap with systematic experiments varying training data size, corpus type (Brown vs. Wall Street Journal), count cutoffs, and n-gram order (bigram vs. trigram).

## Method
The paper surveys and implements seven smoothing families: (1) additive smoothing (Lidstone/Jeffreys, pretend each n-gram occurs delta more times); (2) Good-Turing estimation (corrected count r* = (r+1) n_{r+1}/n_r, where n_r is the number of n-grams with exactly r counts); (3) Jelinek-Mercer interpolation (recursive linear blend of higher- and lower-order ML models with lambda parameters tied into count-bucketed partitions and estimated via deleted interpolation or held-out EM); (4) Katz smoothing (Good-Turing-derived discount ratios d_r applied to nonzero counts for r <= k, with residual mass redistributed via the lower-order ML distribution); (5) Witten-Bell smoothing (a Jelinek-Mercer instance with the backoff weight set to N_{1+}(h) / (N_{1+}(h) + total_count(h)), the count of unique word types following history h); (6) absolute discounting (subtract fixed D from all nonzero counts, redistribute to lower-order model, D = n_1/(n_1 + 2*n_2)); and (7) Kneser-Ney smoothing, which modifies the lower-order distribution to reflect not unigram frequency but the number of distinct contexts a word completes. The novel interpolated Kneser-Ney variant maintains the full Kneser-Ney modified lower-order distribution at each recursion level rather than only at the lowest level. Performance is measured by cross-entropy H_p(T) = -(1/W_T) log_2 p(T) on held-out test data; perplexity is 2^{H_p(T)}.

## Key results
Interpolated Kneser-Ney smoothing consistently outperforms all other evaluated methods across training sizes and corpora. Katz smoothing outperforms Jelinek-Mercer on large training sets but Jelinek-Mercer is superior on small sets — contradicting Katz's original single-corpus conclusion. Kneser-Ney is especially superior for low-count n-grams, while Katz performs comparably for high-count n-grams. Witten-Bell smoothing shows mediocre performance relative to the best methods. Better smoothing yields up to 1% absolute improvement in speech recognition word-error rate. The bucket scheme for Jelinek-Mercer (bucketing by average counts per nonzero element rather than total counts) yields better performance. Suboptimal parameter selection can significantly degrade performance, underscoring the importance of careful tuning.

## Relevance to this research
This paper is primarily background reference for language modeling rather than directly connected to the gauge-theoretic VFE transformer. Its relevance is indirect: the probabilistic model-combination ideas in Jelinek-Mercer and Kneser-Ney smoothing are conceptually related to belief interpolation and hierarchical prior structures in VFE (the VFE hierarchy h → s → p → q mirrors the recursive interpolation of lower-order models as fallbacks for higher-order ones). The discounting and redistribution mechanisms in Katz and absolute discounting resemble mass-conservation arguments in belief update and free-energy minimization. The cross-entropy evaluation metric is the standard information-theoretic quantity that grounds VFE: H_p(T) = -E_q[log p] appears as the likelihood term in variational free energy. Otherwise the paper has no direct connection to GL(K) gauge-equivariant attention, SPD belief geometry, active inference, or social opinion dynamics.

## Cross-links
- Concepts: [[Information Geometry]], [[Variational Free Energy]]
- Related sources: [[kneser-1995-improved-backing-off|kneser1995improved]], [[jelinek-1980-interpolated-estimation|jelinek1980interpolated]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@techreport{chen1998empirical,
  author      = {Chen, Stanley F. and Goodman, Joshua},
  title       = {An Empirical Study of Smoothing Techniques for Language Modeling},
  institution = {Harvard University Computer Science Group},
  year        = {1998},
  number      = {TR-10-98},
  url         = {http://nrs.harvard.edu/urn-3:HUL.InstRepos:25104739},
}
```
