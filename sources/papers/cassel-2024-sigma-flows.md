---
type: paper
title: Sigma Flows for Image and Data Labeling and Learning Structured Prediction
aliases:
  - Cassel 2024 sigma flows
authors:
  - Cassel, Jonas
  - Boll, Bastian
  - Petra, Stefania
  - Albers, Peter
  - Schnörr, Christoph
year: 2024
arxiv: "2408.15946"
url: https://arxiv.org/abs/2408.15946
doi: 10.1007/s10851-025-01270-w
tags:
  - cluster/info-geometry
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/mathematics
  - field/cs-ml
status: stable
created: 2026-08-12
updated: 2026-08-12
---

# Sigma Flows for Image and Data Labeling and Learning Structured Prediction

> [!info] Citation
> Jonas Cassel, Bastian Boll, Stefania Petra, Peter Albers and Christoph Schnörr. "Sigma Flows for Image and Data Labeling and Learning Structured Prediction." *Journal of Mathematical Imaging and Vision* (2025). [doi:10.1007/s10851-025-01270-w](https://doi.org/10.1007/s10851-025-01270-w); preprint [arXiv:2408.15946](https://arxiv.org/abs/2408.15946) (v1 dated 29 August 2024, 51 pp.; primary class math.DS, cross-listed cs.CV, cs.LG). Funded by DFG grant SCHN 457/17-2 within priority programme SPP 2298 "Theoretical Foundations of Deep Learning" and by DFG Excellence Strategy EXC 2181/1 – 390900948 (Heidelberg STRUCTURES Excellence Cluster).

## TL;DR

The **sigma flow** is a geometric PDE whose solution is a [[Harmonic map]] from a compact Riemannian *domain* manifold $(M,h)$ into a *statistical* target manifold — the relative interior of the probability simplex $(\mathring\triangle_c,\mathfrak g)$ carrying the [[Fisher information metric|Fisher-Rao metric]]. It is the Riemannian gradient flow of the corresponding harmonic (Dirichlet) energy, and it merges two prior lines: the Laplace-Beltrami / Beltrami-flow framework of Sochen-Kimmel-Malladi and the authors' own [[Assignment flow]] programme. The distinguishing ingredient is that the *domain* metric $h_t=\mathcal O(\mathfrak S_t)$ is itself a function of the evolving state, which is what makes the model learnable: parametrising $\mathcal O$ by a network turns geometric integration of the flow into a neural-ODE-style architecture. The paper proves a **Lyapunov decrease** and explicitly defers **existence and global convergence** to future work.

## Problem & setting

Assignment flows label metric data on graphs by evolving points of a product of probability simplices under the Fisher-Rao metric; the Beltrami / Laplace-Beltrami framework denoises and enhances images by harmonic-map gradient flows between Riemannian manifolds. Neither on its own gives a *continuous-domain* labeling model with a learnable geometry. The authors take the target manifold of the harmonic-map problem to be the statistical manifold of the assignment-flow approach, thereby extending assignment flows from graphs to a continuous domain manifold and extending the Beltrami framework from Euclidean feature targets to a [[Statistical manifold]].

Standing assumptions (§1.3): $(M,h)$ is a **compact, oriented, connected Riemannian manifold without boundary** and maps are smooth, $f\in C^\infty(M,N)$; for images $M=\mathbb T^2$ (the image domain extended by a constant margin, doubly-periodic boundary conditions) with $h$ induced by data. Compactness is used only to invoke standard spectral facts about the Laplace-Beltrami operator, which are the basis of the Lyapunov argument.

The paper is candid about where it sits relative to harmonic-map theory. Existence results in the literature assume a closed target with **nonpositive** sectional curvature (via convexity of the energy), or a complete target with a positive upper curvature bound for the Dirichlet problem, or Łojasiewicz-Simon machinery on a closed target. §1.3 states verbatim that "our scenario violates basic assumptions made in the literature above ($N$ is open with positive sectional curvature, non-metric affine connection) and generalizes the basic harmonic map problem to sigma models", and therefore that the authors "leave the problem of existence and global convergence … of the gradient flow for future work and solely focus on *geometric* aspects in this paper."

## Method

**Harmonic energy on the simplex.** For $\mathfrak P:M\to\mathring\triangle_c$ the harmonic energy is evaluated in the two dually flat affine coordinate systems of information geometry — the natural/exponential coordinates $\vartheta^i$ and the expectation/mixture coordinates $\mathfrak p_i$ (Prop. 4.1) — and its first variation gives the tension field $\tau(\mathfrak P;\mathfrak g,h)$ in closed coordinate form (Props. 4.2, 4.3).

**Regularised Fisher-Rao metric.** The Fisher-Rao metric $\mathfrak g_{ij}=p_i\delta_{ij}-p_ip_j$ degenerates on paths approaching the simplex boundary, so the paper works with $\mathfrak g_\varepsilon:=\mathfrak g+\varepsilon\mathbb I$, $0<\varepsilon\ll 1$ (Remark 4.4). Because the target is a Hessian manifold, the Christoffel symbols are unchanged by the shift, $(\Gamma_\varepsilon)_{ijk}=\Gamma_{ijk}=\tfrac12\mathfrak d_i\mathfrak d_j\mathfrak d_k\psi$ (Prop. 4.5).

**The flow (Def. 4.6).** With $T,\varepsilon>0$ fixed,
$$\partial_t\mathfrak S_t=\tau(\mathfrak S_t;\mathfrak g_\varepsilon,h_t),\qquad h_t=\mathcal O(\mathfrak S_t),\qquad \mathfrak S_0=\mathfrak P,$$
where $\mathcal O$ maps states to positive-definite symmetric $2$-tensors subject to a *uniform positive definiteness* criterion $\mathcal O(\mathfrak P)\succeq C(\mathcal O)\mathbb I$. In coordinates (Prop. 4.7, $\varepsilon=0$):
$$\partial_t\vartheta^i=\tfrac12\big(\Delta_{h_t}\vartheta^i+\mathfrak g^{ij}\Delta_{h_t}\mathfrak p_j\big),\qquad \partial_t\mathfrak p_i=\tfrac12\big(\mathfrak g_{ij}\Delta_{h_t}\vartheta^j+\Delta_{h_t}\mathfrak p_i\big).$$
The two-stage parametrisation $\mathfrak S_t\xrightarrow{\ \mathcal O\ }h_t\xrightarrow{\ \Delta_{h_t}\ }\tau\xrightarrow{\ \int dt\ }\mathfrak S_t$ is the learnable object: a low-dimensional, time-variant parametrisation of $\mathcal O$ already yields strong adaptivity, and taking $h$ fixed and state-independent recovers established PDE models (Beltrami flow, anisotropic diffusion) as special cases.

The paper further introduces a **sigma-$\alpha$ flow** relative to the $\alpha$-connections of information geometry (§4.3) and an **entropic** harmonic energy with an entropic potential driving convergence to the simplex boundary, i.e. to integral labelings (§4.4); it compares the model to the continuum limit of the discrete S-flow (§4.5) and gives a tangent-space parametrisation for implementation (§4.6). The name "sigma flow" is chosen for the analogy with the **sigma models** of mathematical physics.

## Key results

- **A Lyapunov functional, not an existence theorem.** Prop. 4.10: with $\varphi$ the negative entropy on $\mathring\triangle_c$, the functional $\Phi(\mathfrak P)=\int_M\big(\varphi(\mathfrak P)+\tfrac\varepsilon2\delta_{ij}\vartheta^i\vartheta^j\big)$ is a Lyapunov functional for the sigma flow provided $\varepsilon+c_1=\beta>0$, where $c_1$ comes from the uniform two-sided bound $c_2\mathbb I\succeq\mathcal B(\theta)\succeq c_1\mathbb I$ on $\mathcal B_{ij}=\mathfrak g_{ij}+\tfrac12\mathfrak d_k\mathfrak g_{ij}\theta^k$ (Lemma 4.9, constants depending only on the number of labels). The proof shows $\Phi$ is bounded below, continuous, differentiable and monotonically decreasing, using the spectrum of $\Delta_h$ (Lemma 4.8) and the uniform lower bound on $h$ from (4.26).
- **Existence and global convergence are explicitly open** (§1.3, quoted above). The result is a decrease/stability statement about smooth solutions, not a well-posedness theorem, and the paper flags exactly which standard hypotheses its setting violates: open target, positive sectional curvature, non-metric affine connection.
- **Experiments are proof-of-concept.** §5 reports implementation details, comparison to the discrete S-flow model, a synthetic convergence benchmark, an expressivity study, and learning the prediction of labelings through a time-variant domain metric. No benchmark-leading claim is made.
- **Structural similarity to transformers** is asserted and discussed in §5.3: geometric integration of the sigma flow generates a layered network, and the authors point out structural parallels to transformer architectures as motivation for geometric design principles in scientific machine learning. This is presented as a structural observation, not a derivation of attention.
- The paper answers a question posed by Uohashi (2014) on finding applications of non-trivial harmonic maps relative to the $\alpha$-connections; note that while the target $(N,\mathfrak g)$ is a Hessian manifold, the learned domain $(M,h)$ generally is not.

> [!note] Reading scope
> The full arXiv text was read through §4.2 (definition of the flow, Props. 4.1-4.10 and their proofs); the HTML retrieval truncated thereafter. §§4.3-6 (sigma-$\alpha$ flow, entropic potential, continuum-limit comparison, experiments, transformer comparison, conclusion) are summarised from the paper's own abstract, table of contents and §1.3-§1.4 roadmap, and are marked as such above.

## Relevance to this research

This is the closest published relative of the **Dirichlet / harmonic-map sector** of the vault's own bundle programme, and it is worth being precise about the overlap and the gap.

**What coincides.** The owner's construction ([[participatory-it-from-bit]], `PIFB2.tex`) attaches statistical manifolds with the Fisher-Rao metric as fibres and lets the resulting fields vary over a base manifold of contexts; the sigma flow is exactly the gradient flow of the harmonic energy of a map from a Riemannian base into a Fisher-Rao statistical manifold. If one trivialises the owner's associated bundle $\mathcal E\to\mathcal C$ (single global frame, transport $\Omega_{ij}=I$), a section is just a map $\mathcal C\to\mathcal B$ and the covariant Dirichlet term degenerates to precisely this harmonic energy. The sigma flow is therefore best read as the **flat, ungauged special case** of the owner's Dirichlet sector, worked out in full analytic detail.

**What is absent here.** There is **no bundle, no structure group, no principal connection, no curvature term, and no notion of gauge covariance** in this paper. The target statistical manifold is one fixed manifold shared by every point of $M$, not a fibre transported by a connection; there is no analogue of the owner's $\Omega_{ij}=e^{\phi_i}e^{-\phi_j}$, no analogue of the Regime-I/Regime-II distinction over whether the connection is frame-derived (flat by Maurer-Cartan) or an independent field, and no Yang-Mills or Wilson-type curvature penalty. The gauge half of the owner's construction is supplied instead by the same group's later papers [[cassel-2025-bundle-scale-spaces]] and [[cassel-2025-yang-mills-data]], which do not carry the Fisher-Rao fibre.

**What can be imported rather than re-derived.** (i) The closed coordinate expressions for the harmonic energy and tension field on the simplex in dual affine coordinates. (ii) The $\varepsilon$-regularisation $\mathfrak g_\varepsilon=\mathfrak g+\varepsilon\mathbb I$ as a principled fix for Fisher-Rao degeneracy at the boundary, together with the observation that Hessian structure leaves the Christoffel symbols untouched. (iii) The **Lyapunov construction** — negative entropy plus an $\varepsilon$-quadratic, monotone under a uniform positive-definiteness assumption on the domain metric plus the two-sided bound on $\mathcal B(\theta)$ — is a template for a descent statement about a covariant Dirichlet term, since nothing in it uses flatness of the target's affine connection. (iv) The **state-dependent, learnable domain metric** $h_t=\mathcal O(\mathfrak S_t)$ is a design idea directly comparable to the belief-conditioned coupling of [[gl-k-attention]].

**What the paper concedes and the owner should not overclaim from.** The absence of an existence or global-convergence theorem is stated by the authors themselves, and the obstruction they name — an open target of positive sectional curvature with a non-metric affine connection — applies *a fortiori* to the owner's Gaussian fibres, whose Fisher-Rao sectional curvature is of mixed sign (`PIFB2.tex`, four-curvatures discussion). Any well-posedness claim for a covariant Dirichlet term in the owner's functional therefore cannot cite this paper as precedent; it must be proved, and the standard harmonic-map toolbox is not directly available.

## Cross-links

- Concepts: [[Harmonic map]], [[Sigma flow]], [[Assignment flow]], [[Fisher information metric]], [[Statistical manifold]], [[Information Geometry]], [[Natural gradient]], [[Fibre Bundle|associated bundle]], [[Agents as fibre-bundle sections]]
- Themes / methods: [[Information geometry and natural gradient]], [[Gauge equivariance and geometric deep learning]]
- Related sources: [[cassel-2025-bundle-scale-spaces]], [[cassel-2025-yang-mills-data]], [[gonzalez-alvarado-2025-patch-assignment]], [[amari-2000-methods-information-geometry]], [[vaswani-2017-attention]], [[participatory-it-from-bit]], [[gl-k-attention]]

## BibTeX

```bibtex
@article{cassel2024sigma,
  author        = {Cassel, Jonas and Boll, Bastian and Petra, Stefania and Albers, Peter and Schn{\"o}rr, Christoph},
  title         = {Sigma Flows for Image and Data Labeling and Learning Structured Prediction},
  journal       = {Journal of Mathematical Imaging and Vision},
  year          = {2025},
  doi           = {10.1007/s10851-025-01270-w},
  eprint        = {2408.15946},
  archivePrefix = {arXiv},
  primaryClass  = {math.DS}
}
```
