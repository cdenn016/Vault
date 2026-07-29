---
type: paper
title: "Multiscale network renormalization: scale-invariance without geometry"
aliases:
  - "Garuccio, Lalli & Garlaschelli 2023"
  - "Multiscale model"
  - "MSM"
  - "Aggregation-invariant random graphs"
authors:
  - Garuccio, Elena
  - Lalli, Margherita
  - Garlaschelli, Diego
year: 2023
arxiv: "2009.11024"
url: https://doi.org/10.1103/PhysRevResearch.5.043101
tags:
  - cluster/multi-agent
  - cluster/social-physics/networks-and-contagion
  - project/multi-agent
  - project/social-physics
  - field/physics
  - field/mathematics
status: stable
created: 2026-07-28
updated: 2026-07-28
---

# Multiscale network renormalization: scale-invariance without geometry

> [!info] Citation
> Garuccio, E., Lalli, M., & Garlaschelli, D. (2023). "Multiscale network renormalization: Scale-invariance without geometry." *Physical Review Research* **5**(4), 043101. DOI: [10.1103/PhysRevResearch.5.043101](https://doi.org/10.1103/PhysRevResearch.5.043101). Preprint: [arXiv:2009.11024](https://arxiv.org/abs/2009.11024) (2020).

## TL;DR

Instead of choosing a coarse-graining and asking what it does to a model, this paper inverts the question: which random-graph model is form-invariant under **every** node partition at once? The answer is a uniqueness theorem. Under the "at least one link" coarse-graining rule the only connection probability preserved by all aggregations is $p_{ij} = 1 - e^{-\delta x_i x_j f(d_{ij})}$, with node fitness $x_i$ **additive** under aggregation, dyadic attribute $d_{ij}$ renormalizing as a fitness-weighted $f$-mean, and the density parameter $\delta$ exactly invariant — the partition function itself takes the same value at every level. The construction is the graph analogue of Lévy-stable random variables: laws that survive being combined. Its sharpest corollary is a demarcation — **scale-free** and **scale-invariant** are different, largely orthogonal properties — and a failure taxonomy explaining exactly which standard models are non-renormalizable and why.

## Problem & setting

Every network renormalization scheme before this one had to *choose* the blocks: geometric proximity, diffusion equivalence, box covering. But in most empirical networks the node-level resolution is an artifact of data collection, so a scheme whose answer depends on the partition is reporting an artifact. The authors ask for form-invariance under arbitrary partitions, and under arbitrary *compositions* of partitions, which turns coarse-graining into a semigroup constraint on the model family rather than an operation applied to one model.

## Method

Edge-independent random graphs $P(\mathbf A|\mathbf\Theta) = \prod_{ij} p_{ij}^{a_{ij}}(1-p_{ij})^{1-a_{ij}}$, coarse-grained by

$$a^{(\ell+1)}_{IJ} = 1 - \prod_{i\in I}\prod_{j\in J}(1 - a^{(\ell)}_{ij}).$$

Consistency is a marginalization requirement: the distribution induced on $\mathbf A^{(\ell+1)}$ by pushing $P_\ell$ through this map must be the *same functional form* with only transformed parameters, for every partition. The mechanism forcing the answer is that $1 - e^{-\theta}$ is the probability of at least one event in a Poisson variable of mean $\theta$, so the OR rule composes multiplicatively in $e^{-\theta}$; additivity of $\theta$ over the block product then forces the product-of-additive-fitnesses structure. The unique fixed point is

$$p_{ij} = 1 - e^{-\delta x_i x_j f(d_{ij})}\quad (i\neq j),\qquad
x_I = \sum_{i\in I} x_i,\qquad
d_{IJ} = f^{-1}\!\left(\frac{\sum_{i\in I}\sum_{j\in J} x_i x_j f(d_{ij})}{\sum_{i\in I}\sum_{j\in J} x_i x_j}\right),$$

with $\delta$ scale-invariant. Writing $\mathcal H^{(\ell)}_{\rm eff} = -\sum_{i\le j} a_{ij}\log[p_{ij}/(1-p_{ij})]$ gives $\mathcal Z(\delta) = \exp[\tfrac12\sum_{ij} x_i x_j f(d_{ij})]$, whose value is the same at every level — the exact fixed-point certificate.

**Annealed $\alpha$-stable variant.** Requiring aggregation invariance of the *fitness distribution* as well forces the fitness to be $\alpha$-stable; positivity forces $\alpha\in(0,1)$, hence a diverging mean. Because $\alpha$-stable laws are infinitely divisible, nodes can be split indefinitely into sub-nodes with i.i.d. fitness, so **the flow becomes a group rather than a semigroup** — fine-graining as well as coarse-graining.

## Key results

The expected degree distribution of the annealed model has a universal $k^{-2}$ power-law tail *irrespective of $\alpha$*, becoming a pure power law at aggregation levels with $\delta\sim N_\ell^{-1/\alpha}$ and acquiring a density-dependent cutoff for coarser aggregations. The model reproduces decaying assortativity, vanishing global clustering, and — notably — **non-vanishing local clustering in the sparse regime without any geometry**, which no other sparse edge-independent model achieves without metric distances. The quenched variant is applied empirically to a multiscale model of the International Trade Network valid across hierarchical geographic partitions.

The failure taxonomy is the result with the widest reach. The configuration model and the degree-corrected SBM fail because the degrees "are neither preserved or additively transformed upon renormalization" (§II.6 — the arXiv rendering reads "or", not "nor"; the published Phys. Rev. Research text was not reachable to check for a copyedit); preferential attachment fails because node identity is set by entry time rather than by an additive attribute. Hence: "the non-scale-invariance of the CM, (dc)SBM and PA models originates precisely from the fact that their defining quantities are the node degrees," and scale-invariance "is not due to the scale-free property."

## Relevance to this research

**This is the general form of the MAgent white paper's tying proposition.** Chapter 8a proves the five-term interaction family closed under $0/1$ congruence $\Lambda_c = S^\top\Lambda S$, with off-diagonal blocks $-\sum_{i\in I, j\in J} W_{ij}$ and diagonal blocks $\sum_{i\in I}A_i + \sum_{\rm cut} W_{ij}$: **the coarse coupling is the sum of the fine couplings on cut edges.** That is MSM's additivity structure with the scalar fitness replaced by a PSD matrix weight. Both families close for the same reason — the defining parameter is additive under aggregation — and MSM's failure taxonomy is the general statement of why the Schur-complement (marginalization) route breaks the interaction form while the congruence (tying) route does not.

> [!note] Editorial: the open theorem this suggests. MSM proves **uniqueness**; Chapter 8a proves only **closure**, and explicitly records as open *"whether an aggregating map that integrates rather than identifies can preserve the family."* The MAgent analogue of MSM's theorem would be: *block-diagonal PSD self terms plus a PSD-matrix-weighted graph Laplacian is the unique family of Gaussian interaction precisions closed under $0/1$ congruence for every partition.* MSM's proof strategy — impose invariance under *all* partitions and read off the functional form — is the route. Nothing in the network-RG literature covers Gaussian matrix-weighted precisions, and the Kron-reduction results the white paper cites (Doerfler–Bullo Lemma 2; Loukas Prop. 2.2) are explicitly scalar-weighted, so the matrix-weighted case is open in both literatures.

**The $\alpha$-stable variant is a third option for the Ouroboros tower.** That investigation's verdict is that what survives the refuted apex closure is "a declared top prior or a truncated tower." MSM offers a third: make the flow a two-sided *group* by drawing the additive parameter from an infinitely divisible law. MAgent's additive parameter is a PSD precision, so the analogue is an infinitely divisible law on $\mathrm{Sym}_+(K)$ — matrix-Gamma / Wishart-type. García-Pérez's geometric branching growth requires stability under summation for the same reason, so two independent literatures converge on *bidirectionality requires stability under summation*. Whether this makes MAgent's precision-addition rule invertible is, as far as I can find, unexplored; the Gindikin-set restrictions on Wishart degrees of freedom make it a real question rather than a formality.

**A demarcation the program should adopt.** MSM's separation of *scale-free* from *scale-invariant* maps directly onto the calibration already recorded on [[Renormalization-group flow of beliefs]]: measuring power laws in a belief population is not evidence that the population is renormalizable. The two properties are largely orthogonal, and the manuscripts should say so.

## Cross-links

- Concepts: [[Renormalization group flow]], [[Renormalization-group flow of beliefs]], [[Coarse Graining]], [[Critical Phenomena]], [[Meta-agents and hierarchical emergence]], [[Ouroboros multi-scale dynamics]], [[Community detection and modularity]]
- Related sources: [[gabrielli-2025-network-renormalization]], [[villegas-2023-laplacian-renormalization-group]], [[garciaperez-2018-multiscale]], [[serrano-2008-self-similarity]], [[berman-2023-bayesian-renormalization]]
- Manuscript/Project: [[Gauge-Theoretic Multi-Agent VFE Model]], [[participatory-it-from-bit]]

## BibTeX

```bibtex
@article{garuccio2023multiscale,
  author        = {Garuccio, Elena and Lalli, Margherita and Garlaschelli, Diego},
  title         = {Multiscale network renormalization: Scale-invariance without geometry},
  journal       = {Physical Review Research},
  volume        = {5},
  number        = {4},
  pages         = {043101},
  year          = {2023},
  doi           = {10.1103/PhysRevResearch.5.043101},
  eprint        = {2009.11024},
  archivePrefix = {arXiv},
  primaryClass  = {physics.soc-ph},
}
```
