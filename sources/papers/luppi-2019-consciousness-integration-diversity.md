---
type: paper
title: "Consciousness-specific dynamic interactions of brain integration and functional diversity"
aliases:
  - Luppi 2019
  - Luppi2021
  - Luppi et al. 2019
  - Luppi (2019) Integration and Diversity
authors:
  - Luppi, Andrea I.
  - Craig, Michael M.
  - Pappas, Ioannis
  - Finoia, Paola
  - Williams, Guy B.
  - Allanson, Judith
  - Pickard, John D.
  - Owen, Adrian M.
  - Naci, Lorina
  - Menon, David K.
  - Stamatakis, Emmanuel A.
year: 2019
arxiv: null
url: https://doi.org/10.1038/s41467-019-12658-9
tags:
  - cluster/participatory/consciousness
  - project/multi-agent
  - field/neuroscience
  - field/physics
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Consciousness-specific dynamic interactions of brain integration and functional diversity

> [!info] Citation
> Luppi, A.I., Craig, M.M., Pappas, I., Finoia, P., Williams, G.B., Allanson, J., Pickard, J.D., Owen, A.M., Naci, L., Menon, D.K., & Stamatakis, E.A. (2019). "Consciousness-specific dynamic interactions of brain integration and functional diversity." *Nature Communications*, 10, 4616. https://doi.org/10.1038/s41467-019-12658-9

> [!note] Editorial (citation disambiguation): The verified primary article is *Nature Communications* **10**:4616 (2019), DOI 10.1038/s41467-019-12658-9. A task-supplied citation listed "Nat. Commun. 12:4427 (2021)"; that is a different/erroneous attribution. The `Luppi2021` alias on this note is misleading and should be reviewed/removed by a human — if the manuscript intends a distinct 2021 Luppi paper, the attribution must be reconfirmed separately.

## TL;DR
This study combines graph-theoretic measures of brain integration with entropy-based measures of functional diversity from resting-state fMRI to identify consciousness-specific patterns. Comparing awake volunteers, propofol-anaesthetised volunteers, and patients with disorders of consciousness (DOC), the authors demonstrate that consciousness specifically requires the interaction of integration and diversity: cortical networks in highly integrated temporal states show reduced functional diversity and compromised informational capacity (small-worldness) during unconsciousness, while thalamo-cortical disconnections emerge during segregated states. Posterior default mode network (DMN) regions, especially posterior cingulate/precuneus, consistently show concurrent reductions in both integrative capacity and temporal entropy across both datasets.

## Problem & setting
Prominent theories of consciousness — Integrated Information Theory (IIT), Global Workspace Theory, and the Entropic Brain Hypothesis — each emphasise different neuro-computational properties: information integration, global broadcasting, and signal diversity (entropy), respectively. Prior work had addressed these separately, leaving unresolved how integration and diversity relate neurobiologically during loss of consciousness, and whether their alterations are consistent across pharmacological (propofol anaesthesia) and pathological (brain injury) routes to unconsciousness. A specific discrepancy existed: DMN connectivity hubs are strongly suppressed by anaesthesia, yet prior reports found DMN entropy minimally affected. The authors set out to reconcile these findings using dynamic functional connectivity to reveal state-specific temporal interactions.

## Method
Resting-state fMRI data from 16 healthy volunteers (awake and under deep propofol anaesthesia, Ramsay score 5) and 22 DOC patients (UWS/MCS from traumatic or hypoxic-ischemic injury) were compared. The analysis had two main spatial and temporal arms.

Spatially, voxelwise intrinsic connectivity contrast (ICC) measured whole-brain integrative capacity:

$$\mathrm{ICC}(i) = \sum_j \left[ r(t_i, t_j) \right]^2$$

and voxelwise sample entropy (SampEn) of BOLD timeseries measured functional diversity:

$$\mathrm{SampEn} = -\log \frac{A}{B}$$

where A is the count of template matches of length m+1 and B of length m (with Chebyshev distance threshold r).

Temporally, dynamic functional connectivity (sliding windows, 22 TR) was used with k-means clustering (k=2) on joint participation-coefficient/within-module-Z-score histograms to partition each subject's time into predominantly integrated and predominantly segregated brain states (following Shine et al. 2016). For each state, small-worldness S = (C/C_rand)/(L/L_rand) and connectivity entropy (normalised Shannon entropy of each ROI's FC distribution) were compared between conscious and unconscious conditions.

Network parcellation used 90 AAL ROIs, with graph metrics computed via the Brain Connectivity Toolbox, using modularity maximisation (Louvain algorithm) with a signed-graph formulation.

## Key results
Spatial domain: Reduced ICC and reduced SampEn overlapped in posterior cingulate/precuneus (PCC/PCU), left angular gyrus, and left supramarginal gyrus in both propofol and DOC datasets — identifying these DMN posterior hubs as regions where both integrative capacity and functional diversity are simultaneously compromised during unconsciousness.

Temporal domain (dynamic FC): The predominantly integrated brain state showed significantly reduced small-worldness in both anaesthetised volunteers (M=1.90 vs. 2.15 awake, t(15)=3.01, p=0.010, g=1.03) and DOC patients (M=1.89 vs. 2.15, t(36)=3.41, p=0.002, g=1.10), while the segregated state showed no significant change. Connectivity entropy (normalised Shannon entropy of FC distributions) was also specifically reduced in the integrated state for both anaesthesia (t(15)=2.22, p=0.046) and DOC patients (t(36)=3.43, p=0.002), localised to the DMN. Thalamo-cortical disconnections appeared selectively in the segregated state, while cortico-cortical disruptions were specific to the integrated state. Time spent in the integrated state did not differ between conscious and unconscious conditions, ruling out occupancy as the relevant variable — instead, the quality (small-worldness, entropy) of the integrated state was impaired.

No differences were found between TBI and hypoxic/ischemic subgroups of DOC patients, supporting the generalisability of findings across aetiologies.

## Relevance to this research
This paper provides empirical grounding for several theoretical threads relevant to the VFE / participatory-realism research program. The core finding — that consciousness depends on the dynamic interaction between integration and diversity, specifically during states of high integration — resonates with variational free energy formulations where the quality of belief integration (not just its frequency) determines inference quality. The decomposition into integrated vs. segregated temporal brain states mirrors the distinction between high-coupling (strong β attention weights, low tau) and low-coupling regimes in the VFE attention framework.

The finding that entropy of functional connectivity distributions (Shannon H of each node's FC profile) is selectively reduced in the integrated state connects directly to the role of belief-distribution entropy in the VFE objective — specifically the tau * β_ij * log(β_ij / π_ij) attention-entropy term and the broader KL structure of the free energy functional. Reduced connectivity entropy parallels reduced variational diversity in belief states. The spatial localisation to the DMN posterior hubs (PCC/PCU) as the locus of simultaneous integration-diversity breakdown is consistent with predictive coding accounts (the DMN as the primary site of top-down generative models and self-related priors).

The thalamo-cortical vs. cortico-cortical dissociation across temporal states is relevant to multi-scale or hierarchical VFE architectures: thalamic gating modulates information access in a state-dependent manner, analogous to how hyper-prior level (h → s) coupling in the VFE hierarchy is conditionally active. The paper also provides a concrete empirical example of how graph-theoretic measures of integration/segregation transition correspond to functional state changes — a pattern directly relevant to opinion dynamics and collective integration in multi-agent active inference models where agents transition between more and less integrated network states.

## Cross-links
- Concepts: [[tononi-2004-integrated-information|Integrated Information Theory]] · [[Global neuronal workspace theory|Global Workspace Theory]] · [[Entropy and Consciousness]] · [[Default Mode Network]] · [[Dynamic Functional Connectivity]] · [[Fisher information metric]] · [[Meta-entropy]] · [[Meta-agents and hierarchical emergence]] · [[Ouroboros multi-scale dynamics]] · [[Mathematical consciousness science]]
- Related sources: [[luppi-2021-synergistic-core]] · [[tononi-2004-integrated-information|tononi-2004-information-integration]] · [[tononi-2016-iit]] · [[carhart-harris-2014-entropic-brain]]
- Manuscript/Project: [[participatory-it-from-bit]] · [[VFE Transformer Program]] · [[participatory-it-from-bit|Participatory It-from-Bit]]

## BibTeX
```bibtex
@article{Luppi2019,
  author  = {Luppi, Andrea I. and Craig, Michael M. and Pappas, Ioannis and Finoia, Paola and Williams, Guy B. and Allanson, Judith and Pickard, John D. and Owen, Adrian M. and Naci, Lorina and Menon, David K. and Stamatakis, Emmanuel A.},
  title   = {Consciousness-specific dynamic interactions of brain integration and functional diversity},
  journal = {Nature Communications},
  year    = {2019},
  volume  = {10},
  pages   = {4616},
  doi     = {10.1038/s41467-019-12658-9},
}
```
