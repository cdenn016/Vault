---
type: paper
title: "REBUS and the Anarchic Brain: Toward a Unified Model of the Brain Action of Psychedelics"
aliases:
  - "Carhart-Harris 2019"
  - "REBUS"
authors:
  - Carhart-Harris, R. L.
  - Friston, K. J.
year: 2019
arxiv: null
url: https://doi.org/10.1124/pr.118.017160
tags:
  - cluster/participatory/consciousness
  - project/multi-agent
  - field/neuroscience
  - field/psychology
  - field/philosophy
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# REBUS and the Anarchic Brain: Toward a Unified Model of the Brain Action of Psychedelics

> [!info] Citation
> Carhart-Harris, R. L. and Friston, K. J. (2019). "REBUS and the Anarchic Brain: Toward a Unified Model of the Brain Action of Psychedelics." *Pharmacological Reviews*, 71(3):316–344. https://doi.org/10.1124/pr.118.017160

## TL;DR
This paper proposes REBUS (Relaxed Beliefs Under pSychedelics), a unified model of psychedelic brain action synthesizing the free-energy principle with the entropic brain hypothesis. Classic psychedelics act via 5-HT2A receptor agonism to relax the precision weighting of high-level priors (beliefs) encoded in spontaneous cortical hierarchies, liberating ascending prediction error from intrinsic sources such as the limbic system. This flattening of the variational free-energy landscape is analogous to simulated annealing, transiently destabilizing entrenched attractor states and enabling revision of pathologically overweighted priors underlying many psychiatric conditions.

## Problem & setting
Prior models of psychedelic action focused on pharmacology (5-HT2AR agonism) or phenomenology in isolation. The entropic brain hypothesis (Carhart-Harris 2014/2018) accounted for increased brain entropy under psychedelics, while the free-energy principle (Friston 2010) provided a unified description of belief updating in hierarchical generative models. The gap was an integrated computational account linking the pharmacological action of psychedelics to hierarchical predictive coding and to therapeutic outcomes. The paper also addresses why psychedelics can produce lasting belief revision while also potentially triggering anxiety, psychosis-like states, or ego dissolution at high doses.

## Method
The paper is a theoretical synthesis with empirical review rather than a primary data study. Its core framework uses hierarchical predictive coding under the free-energy principle: the brain encodes a generative model of causes as descending predictions weighted by precision (inverse variance), which modulate the gain on ascending prediction errors. Psychedelics — acting on deep-layer pyramidal neurons via 5-HT2ARs, particularly in high-level cortex and the default-mode network (DMN) — are proposed to reduce the precision weighting of high-level priors, allowing prediction errors from lower intrinsic systems to propagate upward freely. The resulting state is characterized by decreased alpha and beta oscillatory power, increased functional connectivity entropy, and proximity to criticality. Bayesian model reduction (BMR) is invoked to explain how the transient hot/plastic state can yield lasting pruning of entrenched model parameters after the drug is metabolized. Phenomenological and neuroimaging evidence is assembled to support each component of the model.

## Key results
The REBUS model generates several specific, empirically supported predictions. Psychedelics produce reliable reductions in alpha and beta power in DMN regions (posterior cingulate cortex), and the magnitude of these reductions correlates with subjective ratings of ego dissolution under both psilocybin and LSD. The precision of high-level priors, physiologically encoded by the postsynaptic gain of deep-layer pyramidal cells, is reduced by 5-HT2AR activation, leading to decreased top-down effective connectivity (confirmed by dynamic causal modelling of MEG data under LSD). Behavioral evidence includes blunted mismatch negativity to auditory deviant tones, reduced object completion in Kanizsa paradigms, increased perceptual mixing in binocular rivalry, and reduced social exclusion sensitivity — all interpretable as weakened top-down constraints. The anarchic-brain component — increased bottom-up signaling liberated from intrinsic (limbic) sources — accounts for the emotional and autobiographical richness of psychedelic experiences. Therapeutically, the model predicts that psychedelics can revise pathologically overweighted priors (e.g., negative self-schemas in depression, entrenched phobias) by first relaxing their precision and then enabling updating via sensitized prediction error, potentially explaining post-treatment afterglow periods lasting beyond acute drug effects.

## Relevance to this research
The REBUS model is deeply relevant to the VFE transformer program through several channels. First, it is an explicit application of variational free-energy minimization (the same functional F minimized in the VFE transformer) to biological hierarchical inference, demonstrating how precision (inverse variance) weighting — directly analogous to the sigma terms in belief tuples (mu, Sigma, phi) — governs hierarchical information flow. Second, the concept of flattening the free-energy landscape by relaxing prior precision maps onto the role of lambda_h (hyper-prior coupling) and alpha (self-coupling strength) in the VFE functional: reducing these parameters loosens the anchoring of beliefs to priors, allowing larger belief updates from inter-agent coupling terms. Third, the anarchic brain — increased bottom-up prediction error flow — is structurally analogous to the attention-weighted inter-layer coupling (beta_ij) terms dominating when top-down priors are weakened. Fourth, Bayesian model reduction as a mechanism for lasting prior revision after a plasticity window parallels the role of the prior bank (PriorBank) that stores and refines group-level generative models. Fifth, the paper's treatment of precision as gain on prediction error is the neuroscientific interpretation of the information-geometric role of the precision matrix Sigma in Gaussian belief geometry. Finally, the participatory/consciousness dimension: REBUS frames ego dissolution as the collapse of high-level self-models, connecting to the participatory realism and participatory-it-from-bit themes explored in the PIFB manuscript.

## Cross-links
- Concepts: [[Variational Free Energy]] [[Predictive Coding]] [[Precision Weighting]] [[Active Inference]] [[Entropic Brain]]
- Related sources: [[friston-2010-fep]] [[carhart-harris-2018-entropic-brain]]
- Manuscript/Project: [[VFE Transformer Program]] [[PIFB]]

## BibTeX
```bibtex
@article{CarhartHarrisFriston2019,
  author  = {Carhart-Harris, R. L. and Friston, K. J.},
  title   = {{REBUS} and the Anarchic Brain: Toward a Unified Model of the Brain Action of Psychedelics},
  journal = {Pharmacological Reviews},
  volume  = {71},
  number  = {3},
  pages   = {316--344},
  year    = {2019},
  doi     = {10.1124/pr.118.017160},
}
```
