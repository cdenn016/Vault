---
type: paper
title: "The entropic brain: a theory of conscious states informed by neuroimaging research with psychedelic drugs"
aliases:
  - "Carhart-Harris 2014"
  - "Entropic Brain"
authors:
  - Carhart-Harris, Robin L.
  - Leech, Robert
  - Hellyer, Peter J.
  - Shanahan, Murray
  - Feilding, Amanda
  - Tagliazucchi, Enzo T.
  - Chialvo, Dante R.
  - Nutt, David
year: 2014
arxiv: null
url: https://doi.org/10.3389/fnhum.2014.00020
tags:
  - cluster/participatory/consciousness
  - cluster/participatory/philosophy-of-mind
  - project/multi-agent
  - field/neuroscience
  - field/psychology
  - field/physics
  - field/philosophy
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# The entropic brain: a theory of conscious states informed by neuroimaging research with psychedelic drugs

> [!info] Citation
> Carhart-Harris, R. L., Leech, R., Hellyer, P. J., Shanahan, M., Feilding, A., Tagliazucchi, E. T., Chialvo, D. R., & Nutt, D. (2014). "The entropic brain: a theory of conscious states informed by neuroimaging research with psychedelic drugs." *Frontiers in Human Neuroscience*, 8, Article 20. https://doi.org/10.3389/fnhum.2014.00020

## TL;DR
The paper introduces the "entropic brain hypothesis," which proposes that the quality of any conscious state is determined by measurable entropy in key brain parameters. Using neuroimaging data from psilocybin studies, the authors argue that psychedelic states are high-entropy "primary" states of consciousness characterized by elevated network metastability and Shannon entropy in functional connectivity patterns, while normal adult waking consciousness operates in a slightly sub-critical, entropy-suppressed regime upheld by the default-mode network (DMN). This framework is used to explain therapeutic properties of psychedelics and to integrate psychoanalytic (Freudian ego) concepts with cognitive neuroscience via the free-energy principle.

## Problem & setting
The paper addresses three interrelated questions: how normal adult waking consciousness relates to other states, how the brain maintains its normal waking state, and what happens neurodynamically during altered states such as REM sleep, early psychosis, and psychedelic experience. Prior work had characterized the DMN and self-organized criticality separately; the paper synthesizes these under a unified entropy framework, drawing on fMRI (arterial spin labeling, BOLD), MEG studies with intravenous psilocybin in healthy volunteers, and Friston's free-energy principle. The psychoanalytic concepts of primary and secondary consciousness, the ego, and regression are recast in mechanistic terms compatible with cognitive neuroscience.

## Method
The authors conduct three neuroimaging studies with psilocybin (2 mg i.v.) versus placebo in healthy volunteers (n=15 per study). Study 1 measures cerebral blood flow (CBF) via ASL-fMRI; Study 2 measures BOLD signal changes and resting-state functional connectivity (seed-based RSFC) with mPFC, middle frontal gyrus, and hippocampal seeds; Study 3 uses MEG to measure oscillatory power across frequency bands. To formalize entropy, the time course of intra-network synchrony is discretized into bins and Shannon entropy is computed from the resulting probability distribution over each of nine canonical resting-state networks. A second entropy measure enumerates functional connectivity motifs over a 4-node limbic network (bilateral hippocampi and ACC), computing the entropy of the sequence of motifs under placebo versus psilocybin. Key correlates tested include PCC alpha power versus subjective ego-disintegration ratings (Bonferroni-corrected across 23 items).

## Key results
Psilocybin produced decreases in CBF, BOLD signal, intra-DMN functional connectivity, and oscillatory power localized to high-level association cortices and the DMN; no increases were detected. Network metastability (variance of intra-network synchrony) increased significantly after psilocybin in high-level association networks but not in sensory/motor networks, and Shannon entropy over these networks increased correspondingly. The repertoire of functional connectivity motifs in the hippocampus/ACC network was significantly larger under psilocybin, with some motifs exclusive to the drug condition, and the entropy of the motif sequence was significantly higher than at baseline. PCC alpha power decrease correlated strongly with self-reported ego-disintegration (r explaining ~66% of variance), surviving Bonferroni correction; the only other surviving item was "the experience had a supernatural quality." BOLD signal variance increased selectively in the bilateral hippocampi, suggesting hippocampal uncoupling from the DMN.

## Relevance to this research
The entropic brain framework operationalizes entropy as a direct measure of consciousness quality, connecting information-theoretic entropy to the free-energy principle (Friston 2010) through the identity that free-energy (surprise) averages to entropy (uncertainty). This is directly relevant to the VFE transformer program: the variational free-energy objective minimized in VFE attention is formally the same quantity that Carhart-Harris et al. link to conscious state regulation. The attractor-landscape language (shallower basins in primary states, entrenched basins in depression/OCD) parallels the belief-geometry picture of SPD manifolds and KL divergences between beliefs and priors. The concept that normal cognition operates at slight sub-criticality — tuned to minimize surprise while maintaining flexibility — mirrors the active-inference framing of beliefs organized to minimize expected free energy. The paper's treatment of the ego as self-organized DMN activity suppressing entropy also connects to participatory realism discussions of observer-constituted reality and the role of prior beliefs in shaping perception. Shannon entropy over connectivity motif sequences is a network-level analog of the entropy terms appearing in the VFE free-energy functional (the attention entropy term tau * beta * log(beta/pi)).

## Cross-links
- Concepts: [[Variational Free Energy]], [[Entropy]], [[Self-Organized Criticality]], [[Default Mode Network]], [[Active Inference]]
- Related sources: [[friston-2010-free-energy]], [[tononi-2004-information-integration]]
- Manuscript/Project: [[VFE Transformer Program]], [[PIFB]]

## BibTeX
```bibtex
@article{Carhart-Harris2014,
  author  = {Carhart-Harris, Robin L. and Leech, Robert and Hellyer, Peter J. and Shanahan, Murray and Feilding, Amanda and Tagliazucchi, Enzo T. and Chialvo, Dante R. and Nutt, David},
  title   = {The entropic brain: a theory of conscious states informed by neuroimaging research with psychedelic drugs},
  journal = {Frontiers in Human Neuroscience},
  year    = {2014},
  volume  = {8},
  pages   = {20},
  doi     = {10.3389/fnhum.2014.00020},
}
```
