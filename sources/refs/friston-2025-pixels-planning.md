---
type: reference
title: "From pixels to planning: scale-free active inference"
aliases: ["Friston 2025 pixels to planning source"]
authors: ["Karl Friston", "Conor Heins", "Tim Verbelen", "Lancelot Da Costa", "Tommaso Salvatori", "Dimitrije Markovic", "Alexander Tschantz", "Magnus Koudahl", "Christopher Buckley", "Thomas Parr"]
year: 2025
url: "https://doi.org/10.3389/fnetp.2025.1521963"
tags: [cluster/multi-agent, cluster/vfe, project/multi-agent, field/neuroscience]
created: 2026-09-26
---

# From pixels to planning: scale-free active inference

## Citation and archive

Karl Friston and colleagues (2025). *From pixels to planning: scale-free active inference*. Frontiers in Network Physiology 5, 1521963. Published June 18, 2025. [Primary publisher record](https://doi.org/10.3389/fnetp.2025.1521963), [local complete publisher PDF](../pdfs/friston-2025-pixels-planning.pdf). The PDF was downloaded from the publisher on September 26, 2026; SHA-256: `9e8dd1c17c3071e46a2e395395674e5f62096b6c151cfd574a98ba0c7d617f1d`.

## Construction supported by the source

The paper constructs hierarchical discrete generative models with latent states and paths. Its selected graphical architecture gives upper states responsibility for lower initial states and paths. Figure 3 and the accompanying discussion on pages 7–9 impose a single parent for each lower state/path and exclude shared children among same-level parent factors. Equation 11 displays this declared hierarchy of grouped likelihood mappings. This is a model-family restriction that supports the stated conditional-independence organization, not a theorem selecting every admissible decomposition from an unrestricted VFE.

Algorithm 1 on page 15 explicitly starts from prescribed spatial blocks and video-frame groups, applies SVD and quantization, accumulates unique block instances and transitions, then partitions temporal blocks and infers initial states and paths. Its pseudocode was checked against the rendered PDF because text extraction omits the algorithm body. Pages 15–16 explain that grouping two lower transitions per higher update supplies the timescale separation. The construction learns conditional structure and parameters within this organization; it does not derive its grouping rule or physical time calibration without additional choices.

The no-shared-child statement is about the latent graphical model. Footnote 7 on page 8 explicitly permits overlapping Gaussian-weighted image patches for SVD preprocessing. Consequently, this source cannot be used to claim that all overlapping observations, or all base-manifold overlaps in PIFB2, are incompatible with hierarchical inference.

## Equation 10 qualification

Equation 10 on page 8 motivates SVD compression through marginal entropy and an approximately Gaussian empirical distribution. Its discussion treats a deterministic delta conditional as having zero conditional entropy. For continuous variables, a deterministic conditional is singular and its differential entropy is not a finite zero. An unconstrained linear scaling also makes the Gaussian output differential entropy unbounded. Therefore this ingestion does not adopt Equation 10 as a general mutual-information maximization theorem. A valid finite statement needs explicit finite quantization or positive observation noise and a rank/scale or orthonormality constraint. The grouping and algorithmic claims above do not depend on accepting that informal entropy argument.

## Relevance and remaining obligation

For [[PIFB2 refactor foundations September 2026]], this source supplies an active-inference precedent for learned hierarchical state/path models. The relevant comparison is between an explicitly supplied grouping and time-blocking architecture and a derivation that selects those operators within a normalized agent theory. The paper does not establish physical spacetime, physical inertia, or a general obstruction to local-section overlap. See [[Meta-agents and hierarchical emergence]], [[Generative model]], and [[Multi-agent variational free energy]].

## BibTeX

```bibtex
@article{Friston2025PixelsPlanning,
  author = {Friston, Karl and Heins, Conor and Verbelen, Tim and Da Costa, Lancelot and Salvatori, Tommaso and Markovic, Dimitrije and Tschantz, Alexander and Koudahl, Magnus and Buckley, Christopher and Parr, Thomas},
  title = {From pixels to planning: scale-free active inference},
  journal = {Frontiers in Network Physiology},
  volume = {5},
  pages = {1521963},
  year = {2025},
  doi = {10.3389/fnetp.2025.1521963},
  url = {https://www.frontiersin.org/journals/network-physiology/articles/10.3389/fnetp.2025.1521963/full}
}
```
