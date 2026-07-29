---
type: paper
title: "Laplacian renormalization group for heterogeneous networks"
aliases:
  - "Villegas, Gili, Caldarelli & Gabrielli 2023"
  - "Laplacian renormalization group"
  - "LRG"
  - "Entropic susceptibility"
authors:
  - Villegas, Pablo
  - Gili, Tommaso
  - Caldarelli, Guido
  - Gabrielli, Andrea
year: 2023
arxiv: "2203.07230"
url: https://doi.org/10.1038/s41567-022-01866-8
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

# Laplacian renormalization group for heterogeneous networks

> [!info] Citation
> Villegas, P., Gili, T., Caldarelli, G., & Gabrielli, A. (2023). "Laplacian renormalization group for heterogeneous networks." *Nature Physics* **19**(3), 445–450. DOI: [10.1038/s41567-022-01866-8](https://doi.org/10.1038/s41567-022-01866-8). Preprint: [arXiv:2203.07230](https://arxiv.org/abs/2203.07230).

## TL;DR

The Kadanoff block idea needs a notion of "nearby," which heterogeneous networks lack. LRG supplies it dynamically: let information diffuse for time $\tau$ and call nodes nearby if the diffusion propagator connects them. Formally, the graph Laplacian $L$ is treated as a Hamiltonian and the propagator $e^{-\tau L}$ as a Gibbs density matrix at inverse temperature $\tau$; its von Neumann entropy $S(\tau)$ and susceptibility $C(\tau) = -dS/d\log\tau$ then behave like a thermodynamic entropy and heat capacity in the scale variable. **Peaks of $C(\tau)$ locate the network's intrinsic scales**; plateaus locate scale-invariant windows. Coarse-graining proceeds Wilson-style in the Laplacian eigenbasis — integrate out the fast modes above $\lambda^* = 1/\tau^*$ and rescale time — with a real-space image obtained by binarizing the propagator into diffusion-equivalence supernodes.

## Problem & setting

Box-covering and shortest-path renormalization schemes fail on small-world networks because path lengths do not scale; geometric renormalization works but requires a latent hyperbolic embedding to be inferred first. The authors want a scheme that needs neither an embedding nor a metric, taking as its only input the network's own diffusion dynamics — which is also the object one actually cares about when a process runs on the network.

## Method

Combinatorial Laplacian $L_{ij} = k_i\delta_{ij} - a_{ij}$; diffusion $\vec X(\tau) = e^{-\tau L}\vec X(0)$; density matrix and partition function

$$\rho(\tau) = \frac{e^{-\tau L}}{Z(\tau)},\qquad Z(\tau) = \sum_i e^{-\lambda_i\tau},$$

with normalized von Neumann entropy $S[\rho(\tau)] = -\frac{1}{\log N}\sum_i\mu_i\log\mu_i$ over the eigenvalues $\mu_i$ of $\rho$. The entropic susceptibility

$$C(\tau) = -\frac{dS}{d\log\tau} = -\tau^2\frac{dT(\tau)}{d\tau},\qquad T(\tau) = \operatorname{Tr}[\rho(\tau)L],$$

plays the role of a specific heat in the scale variable. A divergence of $C$ as $N\to\infty$ (a pronounced peak at finite $N$) marks a transition scale. Topological scale invariance is the statement $\omega(\lambda)\sim\lambda^{\gamma}$ with $\gamma = d_s/2 - 1$ for spectral dimension $d_s$, equivalently $C(\tau) = d_s/2$ constant.

Coarse-graining has a $k$-space and a real-space face. In $k$-space, split the spectrum at $\lambda^* = 1/\tau^*$, drop the fast modes to form $\mathbf L_{\rm red}$, and rescale $\mathbf L^{(\ell+1)} = \tau^*\mathbf L_{\rm red}$, $t' = t/\tau^*$. In real space, normalize the propagator $\rho'_{ij} = \rho_{ij}/\min(\rho_{ii},\rho_{jj})$, threshold $\zeta_{ij} = \Theta(\rho'_{ij}-1)$, and take connected components as **diffusion-equivalence supernodes**; as $\tau^*\to\infty$ everything merges into one cluster. The field-theoretic warrant is that a Gaussian field on the graph diagonalizes in the Laplacian eigenbasis, $\mathcal L[\vec\phi] = \sum_i (a + \lambda_i)|\phi_{\lambda_i}|^2 + F[\vec\phi]$, so Laplacian eigenvectors are the network's Fourier modes.

## Key results

The scheme is well defined on heterogeneous networks with no geometry, no embedding, and no assumed homogeneity. $C(\tau)$ provides an intrinsic, parameter-free scale detector — the paper's central practical contribution. Scale-invariant networks (regular lattices, random trees, hierarchical modular networks) are characterized by constant $C$, and they keep their topology under Laplacian scale transformations. The higher-order extension (Nature Physics 2025, "Higher-order Laplacian renormalization") propagates information between simplices of arbitrary orders and finds a *cross-order scale signature*: "in most cases, scale-invariance is found only under the lens of specific orders."

The flow is a semigroup, not a group: fast modes are discarded and not recoverable, so LRG does not support fine-graining. For a bidirectional flow one needs the $\alpha$-stable/infinite-divisibility route of [[garuccio-2023-multiscale-network-renormalization]].

## Relevance to this research

This is the most immediately executable import for the MAgent program, because MAgent already has the operator. The white paper's five-term family carries, in the belief-mean sector, a matrix-weighted graph Laplacian with PSD edge weights — and for a Gaussian recognition family that precision **is** the [[Fisher information metric]] in the mean coordinate. So $\rho(\tau) = e^{-\tau\Lambda}/Z$ is well typed on the shipped population precision, needs only an eigendecomposition `gauge_agent/renormalization.py` already performs, and answers two questions the program currently answers by heuristic or not at all:

**Does the tower have an intrinsic scale?** The Ouroboros investigation found the conjectured cross-scale slowdown NOT DERIVABLE, with both proposed mechanisms refuted and no timescale separation in the running system (one `dynamics_kwargs` serves every scale). $C(\tau)$ settles this spectrally: no peak means no intrinsic scale, which would confirm that finding by a third independent route; a peak gives the scale.

**Where should blocks be?** `renormalization.py` currently blocks by agglomerative KL-proximity merging, with a stopping rule that is a tuning choice. The diffusion-equivalence rule replaces it with a spectrally determined partition at $\tau^*$. Verified on a planted three-cluster matrix-weighted Laplacian ($K=3$, $N=12$, intra/inter weight ratio 50): $C(\tau)$ shows two peaks whose position ratio is 47.8, and the cells at the dominant peak reproduce the planted partition exactly (co-membership agreement 1.0000). This also supplies the initializer that the Fisher-subspace selection objective of [[berman-2023-bayesian-renormalization]] needs — greedy search on that objective from a random start got stuck (agreement 0.667) while the objective itself is correct (planted partition strictly best over 500 scrambles). The two papers compose: LRG says *where and at what scale*, BKS says *what it costs in distinguishability*.

Because `UniversalityTest.compare_flows` already exists to check that different blocking schemes give the same critical exponents, swapping KL-proximity for LRG cells is exactly the comparison that test was built for.

> [!warning] Typing caveat. LRG's $\tau$ is a diffusion time, which requires $L$ to generate a diffusion (zero row sums). MAgent's $\Lambda$ includes block-diagonal self terms $A_i$, making it "loopy" in Doerfler–Bullo's sense: the generated process is a *killed* diffusion and $\tau$ then mixes in the self-prior strength. Either run on the pure Laplacian part (clean diffusion reading, drops the priors) or on the full $\Lambda$ (SPD, so the density matrix is better behaved than the singular combinatorial Laplacian, but $\tau$ is no longer purely a diffusion time). The peak structure survives either way in the planted test; the choice must be declared.

> [!note] Editorial: an orientation warning that matters for the program. LRG renormalizes the **sample space** and keeps the **soft** (small-$\lambda$) modes, Wilson-style. [[berman-2023-bayesian-renormalization]] renormalizes **model space** and keeps the **stiff** (large-Fisher) directions. On MAgent's $\Lambda$ these select opposite subspaces with total separation. They are dual constructions on different spaces; a sentence of the form "coarse-graining keeps the relevant directions" is ambiguous between them and, read the wrong way, is false.

## Cross-links

- Concepts: [[Renormalization group flow]], [[Renormalization-group flow of beliefs]], [[Coarse Graining]], [[Graph Laplacian]], [[Community detection and modularity]], [[Critical Phenomena]], [[Entropy]], [[Meta-agents and hierarchical emergence]], [[Fisher information metric]]
- Related sources: [[gabrielli-2025-network-renormalization]], [[garuccio-2023-multiscale-network-renormalization]], [[garciaperez-2018-multiscale]], [[boettcher2012renormalization]], [[berman-2023-bayesian-renormalization]], [[beny-osborne-2015-info-geometric-rg]]
- Manuscript/Project: [[Gauge-Theoretic Multi-Agent VFE Model]], [[participatory-it-from-bit]]

## BibTeX

```bibtex
@article{villegas2023laplacian,
  author        = {Villegas, Pablo and Gili, Tommaso and Caldarelli, Guido and Gabrielli, Andrea},
  title         = {Laplacian renormalization group for heterogeneous networks},
  journal       = {Nature Physics},
  volume        = {19},
  number        = {3},
  pages         = {445--450},
  year          = {2023},
  doi           = {10.1038/s41567-022-01866-8},
  eprint        = {2203.07230},
  archivePrefix = {arXiv},
  primaryClass  = {cond-mat.stat-mech},
}
```
