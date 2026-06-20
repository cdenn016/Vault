---
type: reference
title: "Information Geometry"
aliases: ["Ay 2017", "Ay-Jost-Le-Schwachhofer 2017"]
authors: ["Nihat Ay", "Jürgen Jost", "Hông Vân Lê", "Lorenz Schwachhöfer"]
year: 2017
tags: [cluster/info-geometry, project/transformer, project/multi-agent, field/mathematics, field/statistics]
created: 2026-06-18
updated: 2026-06-18
---

# Information Geometry

> [!info] Citation
> Ay, N., Jost, J., Lê, H. V., & Schwachhöfer, L. (2017). *Information Geometry*. Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge / A Series of Modern Surveys in Mathematics, vol. 64. Springer International Publishing. ~400 pp.

## TL;DR

A research monograph giving a rigorous, measure-theoretic foundation for information geometry. It builds the subject around *parametrized measure models* — families of (possibly infinite-dimensional) probability or finite measures — and derives the [[Fisher information metric]] and the Amari–Chentsov tensor as the canonical invariant structures on such families, characterized by their invariance under sufficient statistics (the Chentsov-type uniqueness theorem). It then develops the dual-affine ($\alpha$-)connections, divergences, and the geometry of exponential and mixture families on a single unified footing.

## What it establishes

- **Parametrized measure models as the basic object.** Rather than starting from a finite-dimensional parameter manifold, the book defines geometric structures directly on spaces of measures, allowing both finite- and infinite-dimensional models and treating the embedding into the space of (signed) measures intrinsically.
- **Invariant tensors via congruent Markov morphisms.** The [[Fisher information metric]] and the Amari–Chentsov $3$-tensor are shown to be (up to scale) the unique $2$- and $3$-tensors invariant under congruent embeddings / sufficient statistics — the modern measure-theoretic form of Chentsov's theorem (cf. [[cencov-1982-statistical-decision-rules]]).
- **Dual structure and $\alpha$-connections.** Construction of the dually flat geometry, the family of torsion-free $\alpha$-connections, and the associated divergences, including the canonical / Bregman divergence on dually flat spaces and its relation to the [[Alpha-divergence]] and [[Renyi divergence]] families.
- **Exponential and mixture families.** Treatment of $e$- and $m$-geodesics, dual flatness, projection theorems, and the Pythagorean relation for divergences.
- **Functional-analytic rigor.** Complete proofs with the necessary measure theory, Riemannian/Banach geometry, and treatment of the singular and infinite-dimensional cases, distinguishing it from the more applied surveys (cf. [[amari-2016-information-geometry-applications]], [[amari-2000-methods-information-geometry]]).

## Why the project cites it

This monograph is the geometric backbone for the project's claim that belief space is a Riemannian manifold whose metric is statistical, not arbitrary. The themes [[Information geometry and natural gradient]] and (for the covariance sector) [[SPD-manifold geometry and Riemannian optimization]] rest on the invariance results established here.

- **Fisher metric as the canonical belief-space metric.** The uniqueness of the [[Fisher information metric]] under sufficient statistics justifies using it — and not an ad hoc metric — to measure distances between agents' beliefs and to define the [[Natural gradient]] descent that underlies the model's update dynamics. This is the precise sense in which the project treats [[Mass as Fisher information]]: the inertial/metric weight on a belief coordinate is the Fisher information, an object whose canonical status this book secures.
- **Divergences for variational objectives.** The $\alpha$-connection / divergence machinery grounds the project's use of the [[Variational free energy]] objective and its [[Alpha-divergence]] and [[Renyi divergence]] generalizations; the dually flat structure is exactly the setting in which KL minimization (the [[Evidence lower bound (ELBO)]] gap) becomes an orthogonal-projection problem.
- **Geometry that meshes with gauge structure.** Because the project models [[Agents as fibre-bundle sections]] and reasons about [[Parallel transport]] and [[Holonomy]] of beliefs, it needs the statistical metric to be an honest Riemannian object on the fibre. This book supplies that object and its invariance properties, letting the [[Gauge equivariance and geometric deep learning]] and information-geometry pictures be glued along the Fisher metric.
- **Precision weighting and predictive coding.** The Fisher metric's identification with inverse-variance / precision connects directly to [[Precision weighting]] of [[Prediction error]] in the [[Free-energy principle active inference]] formulation the project builds on.

> [!note] Editorial: This note draws on the standard content of the monograph rather than a local copy of the text; specific page or theorem numbers should be verified against the book before being cited in a manuscript.

## BibTeX

```bibtex
@book{ay2017information,
  author    = {Ay, Nihat and Jost, J\"urgen and L\^e, H\^ong V\^an and Schwachh\"ofer, Lorenz},
  title     = {Information Geometry},
  series    = {Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge / A Series of Modern Surveys in Mathematics},
  volume    = {64},
  publisher = {Springer International Publishing},
  address   = {Cham},
  year      = {2017},
  doi       = {10.1007/978-3-319-56478-4},
  isbn      = {978-3-319-56477-7}
}
```
