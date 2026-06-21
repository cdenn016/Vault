---
type: paper
title: "Unifying Theories of Psychedelic Drug Effects"
aliases:
  - "Swanson 2018"
  - "Unifying Theories Psychedelics"
authors:
  - Swanson, Link R.
year: 2018
arxiv: null
url: https://doi.org/10.3389/fphar.2018.00172
tags:
  - cluster/participatory/consciousness
  - cluster/participatory/philosophy-of-mind
  - project/multi-agent
  - field/neuroscience
  - field/philosophy
  - field/psychology
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Unifying Theories of Psychedelic Drug Effects

> [!info] Citation
> Swanson LR (2018). "Unifying Theories of Psychedelic Drug Effects." *Frontiers in Pharmacology* 9:172. https://doi.org/10.3389/fphar.2018.00172

## TL;DR
A comprehensive review of theories of psychedelic drug effects spanning 125 years of research, from 19th-century model psychoses and filtration theories through 21st-century cognitive neuroscience frameworks (entropic brain theory, integrated information theory, and predictive processing). The author identifies an abstract unifying principle across all frameworks: psychedelics perturb neurobiological constraint mechanisms that normally suppress entropy and restrict the range of perception, cognition, emotion, and self-experience. The paper argues that making psychedelic drug effects a testing ground for theories of brain function is a powerful strategy for developing and evaluating unifying theories of consciousness.

## Problem & setting
The field lacks a unifying theory of psychedelic drug effects that can simultaneously account for (1) the broad diversity of subjective effects across perceptual, emotional, cognitive, and self-related domains; (2) the multi-level pharmaco-neurophysiological causal chain from receptor agonism to phenomenology; (3) the relationship between psychedelic effects and symptoms of psychosis; and (4) the clinical mechanisms of psychedelic-assisted therapies. Five explicit explanatory gaps are identified. Prior theories — model psychoses, filtration theory, psychoanalytic theory — each partially address these gaps but lack a formalized quantitative framework. Recent neuroimaging data reveals systematic neurophysiological correlates (desynchronization of oscillatory power, disintegration of the default mode network, expanded repertoire of functional connectivity) that demand a principled theoretical account.

## Method
Narrative review of theoretical frameworks across three historical waves of psychedelic science. For each theory the author identifies (a) core principles, (b) which of the five explanatory gaps it addresses, and (c) how it relates to recurring abstract features. The four recurring theoretical features extracted are: (1) psychedelics inhibit a brain mechanism that normally constrains mental processes; (2) this mechanism can become pathological in either direction (too much or too little constraint); (3) psychedelic effects and psychotic symptoms share a common substrate of unconstrained processing; (4) therapeutic utility derives from temporary removal of pathological constraints. Modern theories are assessed for how they formalize these abstract principles quantitatively.

The three 21st-century frameworks reviewed are:

**Entropic Brain Theory (EBT; Carhart-Harris et al., 2014)**: Characterizes psychedelic effects via information-theoretic entropy. Brain dynamics in normal waking life are "near-critical but sub-critical," poised between order and disorder. Psychedelics elevate entropy, expanding the repertoire of functional connectivity motifs. The DMN (default mode network) functions as an entropy-suppression and ego-sustaining mechanism; its pharmacological disintegration under psychedelics permits primary-process, high-entropy dynamics to emerge. EBT recasts Freudian primary/secondary process distinction and Huxley's cerebral reducing valve in quantitative terms.

**Integrated Information Theory (IIT; Gallimore, 2015 building on Tononi)**: Formalizes the entropy-flexibility trade-off in terms of cause-effect information (phi). Psychedelic dissolution of DMN-TPN anticorrelation expands the cause-effect repertoire of neural mechanisms toward the unconstrained repertoire of all possible states, increasing flexibility while decreasing cause-effect information and predictive precision.

**Predictive Processing (PP; Friston FEP, Clark, Hohwy)**: The brain is a hierarchical generative model continuously minimizing prediction error (variational free energy). Normal perception is "controlled hallucination" where top-down priors constrain bottom-up sensory evidence. Psychedelics, via 5-HT2A agonism and hyperexcitation of layer V pyramidal neurons, perturb hierarchically linked priors in internal generative models, causing endogenous simulations to "run wild." Active inference — the FEP principle by which the agent selectively samples sensory input consistent with its priors — also becomes perturbed, potentially explaining why psychedelics manifest both inner (hallucinatory) and outer (perceptual intensification) phenomena simultaneously. Multiple PP-based mechanistic variants are canvassed: hyperactivation of top-down signals, reduced higher-cortical suppression, disrupted multisensory integration, and distorted bottom-up signals with compensatory top-down enhancement.

## Key results
The review does not report original empirical data but synthesizes the following findings as the current consensus: (1) 5-HT2A receptor agonism is necessary (though not sufficient) for classic psychedelic effects, established by ketanserin blockade studies; (2) psychedelics consistently reduce oscillatory power across broad frequency bands, particularly in alpha-band activity correlated with visual effects and ego dissolution; (3) fMRI studies show decreased DMN intrinsic functional connectivity, increased between-network functional connectivity, and markedly expanded repertoire of neurophysiological states under LSD, psilocybin, and ayahuasca; (4) ego dissolution, correlated with alpha-power reductions in cingulate and parahippocampal regions, predicts positive clinical outcomes in therapeutic settings; (5) long-term personality trait changes (increased openness) and cognitive flexibility improvements persist for weeks after a single session. The central theoretical conclusion is that no currently existing theory constitutes a full "unifying theory" by Morrison's criteria (formalized framework plus unifying principles), but the predictive processing / FEP framework is the most promising candidate for providing such formalization.

## Relevance to this research
The predictive processing discussion is directly relevant to the VFE transformer's theoretical foundations. Swanson's review explicitly frames psychedelic disruption of priors through Friston's free energy principle, active inference, and hierarchical generative models — the same theoretical architecture that motivates the GL(K) gauge-equivariant attention and variational free energy minimization in this codebase. Specifically: (a) the hierarchy "h → s → p → q → observations" in the VFE transformer is precisely the multi-level "priors on priors" (hyperpriors) structure that Swanson, following Tenenbaum et al. and Friston et al., identifies as critical for tractable Bayesian inference; (b) the lambda_h * KL(s_i || h) hyper-prior coupling term in the VFE free energy functional enforces the "hyperpriors" that Swanson identifies as allowing the system to "rule out large swaths of possibilities"; (c) entropic brain theory's characterization of the DMN as an entropy-suppression mechanism analogizes to the VFE model's self-coupling term alpha * KL(q_i || p_i), which tethers beliefs to priors and constrains the belief distribution. The paper also connects to PIFB (participatory it-from-bit) themes: Huxley's question of whether psychedelics manifest "more of mind" or "more of world" maps directly onto the participatory realism debate about whether the observer's generative model partially constitutes reality. Swanson's resolution via active inference — that the mind-manifesting and world-manifesting interpretations are reconcilable because models shape sensory sampling — is structurally parallel to the participatory ontology explored in the PIFB manuscript.

## Cross-links
- Concepts: [[Predictive Processing]], [[Free Energy Principle]], [[Active Inference]], [[Entropic Brain Theory]], [[Default Mode Network]], [[Ego Dissolution]], [[Consciousness]]
- Related sources: [[friston-2010-free-energy]] [[carhart-harris-2014-entropic-brain]] [[tononi-2004-iit]]
- Manuscript/Project: [[VFE Transformer Program]], [[PIFB]]

## BibTeX
```bibtex
@article{Swanson2018,
  author  = {Swanson, Link R.},
  title   = {Unifying Theories of Psychedelic Drug Effects},
  journal = {Frontiers in Pharmacology},
  volume  = {9},
  pages   = {172},
  year    = {2018},
  doi     = {10.3389/fphar.2018.00172},
}
```
