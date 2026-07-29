---
type: paper
title: "Network renormalization"
aliases:
  - "Gabrielli, Garlaschelli, Patil & Serrano 2025"
  - "Network Renormalization review"
authors:
  - Gabrielli, Andrea
  - Garlaschelli, Diego
  - Patil, Subodh P.
  - Serrano, M. Ángeles
year: 2025
arxiv: "2412.12988"
url: https://doi.org/10.1038/s42254-025-00817-5
tags:
  - cluster/multi-agent
  - cluster/social-physics/networks-and-contagion
  - cluster/info-geometry
  - project/multi-agent
  - project/social-physics
  - field/physics
  - field/mathematics
  - field/cs-ml
status: stable
created: 2026-07-28
updated: 2026-07-28
---

# Network renormalization

> [!info] Citation
> Gabrielli, A., Garlaschelli, D., Patil, S. P., & Serrano, M. Á. (2025). "Network renormalization." *Nature Reviews Physics* **7**(4), 203–219. DOI: [10.1038/s42254-025-00817-5](https://doi.org/10.1038/s42254-025-00817-5). Preprint: [arXiv:2412.12988](https://arxiv.org/abs/2412.12988).

## TL;DR

A review of how the renormalization group survives the loss of the things it was built on — homogeneity, symmetry, geometry, locality — when the substrate is a heterogeneous network. It organizes renormalization into three steps (define coarse variables, marginalize fine detail, renormalize parameters) and surveys three frameworks that each attack a different step: **geometric renormalization** (GR) supplies the blocks from a latent hyperbolic embedding, **Laplacian renormalization** (LRG) supplies them spectrally via diffusion in $k$-space, and the **multiscale model** (MSM) is agnostic about blocks entirely and instead identifies the unique connection-probability functional form invariant under *every* possible aggregation. The closing open problems are the identification of intrinsic resolution scales, the *simultaneous* renormalization of topology and of dynamics running on it, generalized criticality, and an information-geometric account of parameter relevance.

## Problem & setting

Traditional RG relies on a lattice: a metric, translational symmetry, local interactions, a momentum space. Real networks have none of these — irregular degree distributions, small-world path lengths, no translational symmetry, and coarse-graining partitions that are arbitrary rather than canonical. Worse, the resolution at which a network's nodes are defined is usually an artifact of data collection, not an intrinsic scale of the system. The review's organizing question is what "changing the scale" can mean under those conditions.

## Method

**The three-step program.** Levels are indexed by $\ell$, with a partition $\mathbf\Omega_\ell$ mapping $N_\ell$ nodes onto $N_{\ell+1}$ block nodes. The canonical binary coarse-graining is the "at least one link" (OR) rule

$$a^{(\ell+1)}_{IJ} = 1 - \prod_{i\in I}\prod_{j\in J}\big(1 - a^{(\ell)}_{ij}\big),$$

with a generic $\mathcal G$ for weighted graphs. Step (iii) is the flow of couplings.

**Geometric renormalization (GR).** Nodes live on the $\mathbb S^1$ similarity circle with hidden degree $\kappa_i$; connection probability $p_{ij} = (1+\chi_{ij})^{-1}$, $\chi_{ij} = (R_0\Delta\theta_{ij})^\beta / (\hat\mu_0\kappa_i\kappa_j)^{\max(1,\beta)}$. Blocks are contiguous angular sectors of $r$ nodes; the hidden variable $z_i = \kappa_i^{\max(1,\beta)}$ is **additive** and the angle renormalizes as a $z$-weighted barycenter, with $R_{\ell+1}=R_\ell/r^\ell$, $\hat\mu_{\ell+1}=\hat\mu_\ell/r^{\min(1,\beta)}$ and $\beta$ scale-invariant. Mean degree flows as $\langle k\rangle_{\ell+1} = r^\nu\langle k\rangle_\ell$; the genuinely self-similar flow is the marginal line $\nu = 0$. See [[garciaperez-2018-multiscale]].

**Laplacian renormalization (LRG).** With $L = \mathrm{diag}(k) - A$ and diffusion propagator $\mathbf K(\tau) = e^{-\tau L}$, define a Gibbs density matrix $\rho(\tau) = e^{-\tau L}/Z(\tau)$ in which $L$ is the Hamiltonian and $\tau$ the inverse temperature. Its von Neumann entropy $S(\tau)$ and **entropic susceptibility**

$$C(\tau) = -\frac{dS(\tau)}{d\log\tau}$$

detect scales: peaks of $C$ mark topological transitions, and a network is topologically scale-invariant iff the spectral density obeys $\omega(\lambda)\sim\lambda^{d_s/2-1}$, equivalently $C(\tau) = d_s/2$ constant. Coarse-graining integrates out fast modes ($\lambda\ge\lambda^*=1/\tau^*$) and rescales time, $\mathbf L^{(\ell+1)} = \tau^*\mathbf L^{(\ell)}_{\rm red}$. See [[villegas-2023-laplacian-renormalization-group]].

**Multiscale model (MSM).** The strongest of the three because it is a uniqueness result. See [[garuccio-2023-multiscale-network-renormalization]]: the *only* connection probability whose functional form is invariant under **all** partitions is $p_{ij} = 1 - e^{-\delta x_i x_j f(d_{ij})}$, with fitness $x$ additive, dyadic attribute $d$ renormalizing as a fitness-weighted $f$-mean, and $\delta$ exactly scale-invariant; the partition function $\mathcal Z(\delta)$ is exactly invariant along the flow.

## Key results

| | Geometric (GR) | Laplacian (LRG) | Multiscale (MSM) |
|---|---|---|---|
| Analogue | Kadanoff real-space | Wilson momentum-space | Lévy stability / exact fixed point |
| RG scale | block size $r$ | diffusion time $\tau$, cutoff $\lambda^*=1/\tau^*$ | none — *any* partition |
| Blocks | assumed (latent $\mathbb H^2$ coordinates) | derived (diffusion-equivalence cells) | agnostic |
| Fixed-point invariance | $p_{ij}$ form preserved, same $\beta$; self-similar at $\nu=0$ | $C(\tau)=d_s/2$ constant | exact form-invariance of $P(\mathbf A\vert\mathbf\Theta)$ under all partitions |
| Required input | hyperbolic embedding | full Laplacian spectrum | an additive node attribute |
| Invertible? | yes (branching growth), needs stable $\rho(z)$ | no — fast modes discarded | yes, exactly, in the annealed $\alpha$-stable variant |

The sharpest general lesson carried by this literature is a *failure* taxonomy: the configuration model, degree-corrected SBM and preferential attachment are not renormalizable because their defining quantity is the node degree, and renormalizability is additivity of the defining parameter. Correspondingly, **scale-free** (power-law degrees) and **scale-invariant** (renormalizable) are different and largely orthogonal properties.

> [!warning] Attribution correction — the failure-taxonomy quote belongs to MSM, not to this review.
> An earlier version of this note put the sentence *"is neither preserved nor additively transformed upon renormalization"* in the review's mouth. That passage does not appear in this review at all. It comes from a different paper, [[garuccio-2023-multiscale-network-renormalization]] — Garuccio, Lalli & Garlaschelli, "Multiscale network renormalization: scale-invariance without geometry," [arXiv:2009.11024](https://arxiv.org/abs/2009.11024), §II.6 — where the text reads, verbatim: *"However the degrees, even when power-law distributed, cannot be renormalized exactly because they are neither preserved or additively transformed upon renormalization. The non-scale-invariance of the CM, (dc)SBM and PA models originates precisely from the fact that their defining quantities are the node degrees."* Three things were wrong beyond the attribution: the conjunction is **"or"**, not "nor"; the subject is plural (*"the degrees … they are"*), not the singular "their defining quantity"; and the quoted form spliced these two consecutive sentences into one. The "or"/"nor" discrepancy is between the arXiv rendering, which reads "or", and any copyedit in the published version — the Phys. Rev. Research **5**, 043101 (2023) text was not reachable for checking, so treat "or" as the verifiable reading.

## Open problems (§6)

1. **Intrinsic vs. observational resolution.** The node-level resolution of most empirical networks is a data-collection artifact; whether the system has *intrinsic* scales must be decided independently. LRG's $C(\tau)$ peaks are the review's main instrument; MSM's partition-agnosticism is the complementary answer.
2. **Renormalizing dynamics together with topology** — "the lack of structural homogeneity in real-world networks and their coarse-grained versions implies a **coupling** between the renormalization of the dynamical process and that of the topology." Prior work is confined to regular and fractal substrates.
3. **Generalized criticality** — heterogeneity may produce not a single transition but an entire region of parameters where criticality appears progressively in partial sub-networks, "somewhat similar to Griffiths phases."
4. **Parameter (ir)relevance: an information-theoretic perspective** — a named subsection arguing that power-counting relevance should be replaced, for arbitrary systems without a microscopic model, by Fisher information and information geometry, illustrated by a figure showing an exponential eigenvalue hierarchy in the Fisher matrices of 30 trained MNIST classifiers.

> [!warning] "Parameter (ir)relevance" is a promissory note, not a result.
> An earlier version of this note called the passage *truncated mid-argument*. That was a fetch artifact, not a property of the paper: the arXiv v1 HTML carries the argument to completion. What is mechanically confirmed is that the passage contains **zero equations** — no `<math>` elements and no `ltx_equation` blocks across its 9,941-character span. It is prose, and it derives nothing; what is verifiable is the argument's direction and its Figure 4 (Fisher eigenvalue hierarchy of trained networks). Cite it as an open direction the review names, not as a derivation. It is nonetheless the explicit bridge to [[berman-2023-bayesian-renormalization]], which executes exactly this program on the model-space side: the review cites BKS (arXiv:2305.10491) as reference **[201]** at the very sentence about reimagining "statistical (Bayesian) inference and renormalization in a unified framework of parameter flow," so the two literatures are joined by a direct citation rather than only by our synthesis.
> **Citation form.** The arXiv version carries no numbered subsections in §6, so cite this as `Gabrielli et al. (2025), §6, "Parameter (ir)relevance: an information-theoretic perspective"` rather than "§6.4".

## Relevance to this research

**Open problem 2 is the MAgent problem.** MAgent is a dynamical process (belief updating) on a network (the interaction graph) in which both must be coarse-grained together — with the additional complication that in the Gaussian case the process and the topology share a single operator. The review's own survey of prior work on coupled renormalization covers only regular and fractal substrates, so a heterogeneous gauge-carrying belief network is uncovered ground.

**MSM is the general form of the white paper's tying proposition.** The MAgent exact-ELBO chapter proves the five-term interaction family closed under $0/1$ congruence $\Lambda_c = S^\top\Lambda S$, with the derived rule that the coarse pair weight is *exactly the sum of the fine weights on cut edges*. MSM's fitness additivity is the same principle in the Bernoulli setting, and MSM's failure taxonomy is the general statement of why MAgent's Schur-complement route breaks the interaction form while its congruence route does not. The white paper leaves open *"whether an aggregating map that integrates rather than identifies can preserve the family."*

> [!note] Editorial: the theorem this suggests. MSM proves **uniqueness** where the white paper proves only **closure**. The MAgent analogue would be: *block-diagonal PSD self terms plus a PSD-matrix-weighted graph Laplacian is the unique family of Gaussian interaction precisions closed under $0/1$ congruence for every partition.* This is not covered by MSM (Bernoulli, scalar) nor by the Kron-reduction literature (Doerfler–Bullo, Loukas: scalar-weighted), so the matrix-weighted case is open in **both** literatures. That is the correct basis for a novelty claim and is defensible.

**LRG supplies the intrinsic scale MAgent lacks**, executably. The Ouroboros investigation found no timescale separation in the tower and refuted both proposed slowdown mechanisms; `gauge_agent/renormalization.py` blocks by KL-proximity agglomeration, a heuristic with no principled stopping rule. Running $\rho(\tau) = e^{-\tau\Lambda}/Z$ on the population precision gives $S(\tau)$, $C(\tau)$, and — via the diffusion-equivalence rule — the blocking partition for free. On a planted two-scale test the susceptibility peaks recovered the planted weight ratio (47.8 against 50) and the cells recovered the planted partition exactly (co-membership agreement 1.0000). Caveat: LRG's $\tau$ is a diffusion time and needs zero row sums, whereas MAgent's $\Lambda$ carries self terms and so generates a *killed* diffusion; declare whether the pure Laplacian part or the full precision is meant.

**The α-stable route is a third option for the tower.** MSM's annealed variant draws the additive parameter from an $\alpha$-stable law; infinite divisibility then permits indefinite *fine*-graining, so the flow "defines not only a semi-group proceeding bottom-up, but also a **group** proceeding in both directions." García-Pérez's branching growth needs the same property for the same reason — two independent literatures converging on *bidirectionality requires stability under summation*. Since MAgent's additive parameter is a PSD precision, the analogue is an infinitely divisible law on $\mathrm{Sym}_+(K)$. This is a third possibility beyond the Ouroboros verdict's "declared top prior or truncated tower," and as far as I can find it is unexplored.

Full development in the MAgent repo at `docs/derivations/2026-07-28-renormalization-literature-application.md`, with oracle `verification/rg_literature_probe.py`.

## Cross-links

- Concepts: [[Renormalization group flow]], [[Renormalization-group flow of beliefs]], [[Coarse Graining]], [[Graph Laplacian]], [[Community detection and modularity]], [[Critical Phenomena]], [[Meta-agents and hierarchical emergence]], [[Ouroboros multi-scale dynamics]], [[Fisher information metric]]
- Related sources: [[villegas-2023-laplacian-renormalization-group]], [[garuccio-2023-multiscale-network-renormalization]], [[garciaperez-2018-multiscale]], [[serrano-2008-self-similarity]], [[boettcher2012renormalization]], [[berman-2023-bayesian-renormalization]], [[beny-osborne-2015-info-geometric-rg]], [[wilson-1971-rg-critical-phenomena]]
- Manuscript/Project: [[participatory-it-from-bit]], [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@article{gabrielli2025network,
  author        = {Gabrielli, Andrea and Garlaschelli, Diego and Patil, Subodh P. and Serrano, M. {\'A}ngeles},
  title         = {Network renormalization},
  journal       = {Nature Reviews Physics},
  volume        = {7},
  number        = {4},
  pages         = {203--219},
  year          = {2025},
  doi           = {10.1038/s42254-025-00817-5},
  eprint        = {2412.12988},
  archivePrefix = {arXiv},
  primaryClass  = {physics.soc-ph},
}
```
