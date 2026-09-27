---
type: reference
title: "Artificial versus Substantial Gauge Symmetries: A Criterion and an Application to the Electroweak Model"
aliases:
  - "François 2019 artificial vs substantial gauge symmetries"
  - "Artificial vs Substantial Gauge Symmetries"
  - "Francois2019Artificial"
authors:
  - Jordan François
year: 2019
arxiv: "1801.00678"
doi: 10.1086/703571
url: https://arxiv.org/abs/1801.00678
tags:
  - cluster/gauge-theory
  - project/transformer
  - field/philosophy
  - field/physics
created: 2026-09-23
updated: 2026-09-23
---

# Artificial versus Substantial Gauge Symmetries: A Criterion and an Application to the Electroweak Model

> [!info] Citation
> Jordan François (2019). "Artificial versus Substantial Gauge Symmetries: A Criterion and an Application to the Electroweak Model." *Philosophy of Science* **86**(3), 472–496. DOI: [10.1086/703571](https://doi.org/10.1086/703571). Preprint: [arXiv:1801.00678](https://arxiv.org/abs/1801.00678) (v4 read).

## TL;DR

François turns the generalized Kretschmann objection, that any theory can be given a gauge symmetry, into an operational test built on the dressing field method. If a local dressing field can be built from the fields of a gauge theory, the theory can be rewritten in local gauge-invariant composite variables at no cost, and its gauge symmetry is artificial. If only non-local dressing fields exist, the symmetry is substantial.

## What it establishes

Section 2 summarizes the dressing field method of [[fournel-2014-gauge-invariant-composite-fields]]. A field $u$ with the transformation law $u^\gamma=\gamma^{-1}u$ under a normal subgroup $J$ of the gauge group yields composite fields $A^u=u^{-1}Au+u^{-1}du$ and $\varphi^u=\rho(u^{-1})\varphi$ that are $J$-invariant, and the Lagrangian rewritten in them is an $H/J$ gauge theory. The paper stresses that this change of variables is not a gauge transformation, because $u$ is not an element of the gauge group. Section 2.2 shows that the $U(1)$ symmetry of the Stueckelberg model is compensated by the Stueckelberg field, itself an abelian dressing field, so that the dressed Lagrangian is the Proca Lagrangian. It then states the criterion (C1): "A local dressing field in a gauge theory signals that its gauge symmetry is artificial." Its complement (C2) holds that a symmetry admitting only non-local dressing fields, such as Dirac's dressed electron, is substantial.

The same section applies the criteria to scalar versus spinor electrodynamics and the Aharonov–Bohm effect, to general relativity, where the tetrad is a local dressing field for local Lorentz symmetry unless spinor matter obstructs it, and to massive gravity, where the vielbein clock field transforms as $e\mapsto eG$ under coordinate changes and $u=e^{-1}$ is a local dressing field. Section 3 applies the method to the electroweak model and argues that spontaneous symmetry breaking is superfluous to the theory's empirical success.

## Relevance to this research

The September 2026 v2 revision of the GL(K) attention manuscript (`manuscripts/GL(K)_attention_v2.tex`) uses criterion (C1) to classify its learned per-token frames $U_i$ as a local dressing field. Under a passive frame change the frames transform as $U_i\mapsto g_iU_i$, and the reference moments $\xi_i=U_i^{-1}\mu_i$ are the dressed variables. The manuscript's passive $\mathrm{GL}(K)$ covariance is therefore artificial in François's sense and constrains none of the learned interface maps ($S_Q$, $S_K$, $T$, $O$). The criterion answers the objection surveyed in [[norton-1993-general-covariance]]. The synthesis is on [[Dressing field method]], [[GL(K) gauge-equivariant attention]], and [[Gauge transformation]].

> [!note] Editorial: Among François's examples, the massive-gravity vielbein is the closest formal analogue of the learned frames. Like $U_i\mapsto g_iU_i$, it is a frame-valued field transformed by one-sided multiplication ($e\mapsto eG$), and a local dressing field is read off from it directly: $u=e^{-1}$ there, and $u=U_i$ here once the gauge parameter is identified as $\gamma=g_i^{-1}$ in the convention $u^\gamma=\gamma^{-1}u$.

## Local full text

The arXiv v4 PDF is stored at `sources/pdfs/Francois2019Artificial.pdf` ([local PDF](../pdfs/Francois2019Artificial.pdf)). Source: [arXiv:1801.00678](https://arxiv.org/pdf/1801.00678). SHA-256: `71526320d91afaf213a0c7774648ad68381d9370d6c168fae2c9508b14b43d57`.

## BibTeX

```bibtex
@article{Francois2019Artificial,
  author = {Fran{\c{c}}ois, Jordan},
  title = {Artificial versus Substantial Gauge Symmetries: A Criterion and an Application to the Electroweak Model},
  journal = {Philosophy of Science},
  volume = {86},
  number = {3},
  pages = {472--496},
  year = {2019},
  doi = {10.1086/703571},
  eprint = {1801.00678},
  archivePrefix = {arXiv}
}
```
