---
type: paper
title: "Functorial Statistical Physics: Feynman--Kac Formulae and Information Geometries"
aliases: ["Sakthivadivel 2022 functorial statistical physics"]
authors: ["Dalton A. R. Sakthivadivel"]
year: 2022
venue: "arXiv preprint (math-ph; cross-listed cond-mat.stat-mech, math.AT, math.PR)"
arxiv: "2212.13618"
doi: "10.48550/arXiv.2212.13618"
url: "https://arxiv.org/abs/2212.13618"
version: "arXiv:2212.13618v1 [math-ph], 27 December 2022 (document dated 29th December 2022); 9 pages (8 of text plus references)."
tags: [cluster/info-geometry, project/multi-agent, field/mathematics, field/physics, field/statistics]
created: 2026-11-13
updated: 2026-11-13
---

# Functorial Statistical Physics: Feynman--Kac Formulae and Information Geometries

> [!info] Citation
> Dalton A. R. Sakthivadivel (2022). *Functorial Statistical Physics: Feynman--Kac Formulae and Information Geometries*. arXiv preprint (math-ph; cross-listed cond-mat.stat-mech, math.AT, math.PR). [arXiv:2212.13618](https://arxiv.org/abs/2212.13618)

[Local PDF](../pdfs/sakthivadivel-2022-functorial-statistical-physics.pdf), 9 pages; retrieved November 13, 2026. Version read: arXiv:2212.13618v1 [math-ph], 27 December 2022 (document dated 29th December 2022); 9 pages (8 of text plus references). Reading basis: The first reader worked from the extracted text and did not see the typeset pages. The note rests on the extracted text, read in full for all 9 pages, including the statements and proofs of Propositions 1 to 3, Lemmas 1 and 2, Theorems 1 to 3, Corollaries 1 and 2 and Remarks 1 to 3. Equations (1) to (4) were legible; the commutative triangle in the proof of Proposition 2 was garbled and was reconstructed from the surrounding sentence. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, page-002, page-003, page-004, page-005, page-006, page-007, page-008, page-009). Confirmed against those pages: (1) dY_t = -b dt + sqrt(2 lambda) dW_t (as printed); (2) dY^i = b_i dt + sigma_ik dW^k; Feynman-Kac p(q,t) = E_pi[p(Y_T,T) | Y_t = q_t]; Proposition 1 F(x) = exp{-x.J(q)} and F_* = F o phi; (3) dF_* : T^0_inf X -> rho A with A = m(q,t)d_q + s(q,t)d_qq; Proposition 3 F_* : Gamma(X) -> rho P; Theorem 1 (m_t,s_t) -> FK(m_t,s_t) = p(q,t); (4) <x|P_t p|x'> = E[p_ss(q; x(t,t'))]; Theorem 3 kernel composition e^{-lambda_f J(t_f)} o ... o e^{-lambda_1 J(t_1)}. Title page: v1, 27 Dec 2022, dated 29th December 2022.

## TL;DR

A short announcement claiming that the Feynman-Kac formula is a functor from paths in a parameter space (the moments of a diffusion) to paths of densities on a statistical manifold, that the statistical manifold is thereby a sheaf over the parameter space, and that the composition law of this functor, read as the sewing law of functorial field theory, extends to Jaynes's maximum caliber for processes not driven by Wiener noise. The proofs are brief, and the abstract itself calls the last step a partial formalization.

## Problem & setting

The paper sets out to formalize the working practice, in information geometry and time-dependent statistical physics, of computing with parameters (moments or sufficient statistics) in place of densities, and to extend path-measure methods beyond Wiener-driven diffusions. The setting is a finite-dimensional manifold $X$ globally equivalent to $\mathbb{R}^d$ serving as parameter space, dynamical systems regarded as one-parameter groups of local diffeomorphisms and hence as categories, and a statistical manifold $S_M$ of exponential-form densities $\exp\{-\lambda\cdot J(q)\}$ on a manifold $M$, with fixed $J$ and uniquely determined parameters. The stochastic input is an Itô diffusion whose Kolmogorov backward equation is solved by the Feynman-Kac formula. Prior work drawn on includes statistical manifolds (Lauritzen; Pistone and Rogantin; Amari), Dynkin's formula, jet groupoids and Atiyah Lie algebroids, diffeological spaces, functorial field theory after Atiyah, Segal and Kontsevich in Schreiber's presentation and its Riemannian variants, and maximum caliber (Jaynes 1985; Pressé et al. 2013).

## Method

Section 1 fixes notation with two examples. For a drifted Wiener process (eq. 1) and for an Ornstein-Uhlenbeck process, Itô's lemma gives ordinary differential equations for the mean $m(t)$ and variance $s(t)$, so that a trajectory $(m(t), s(t))$ in $\mathbb{R}^2$ determines the density $p(q,t)$. For the general diffusion $dY^i_t = b^i(Y_t,t)dt + \sigma^{ik}(Y_t,t)dW^k_t$ (eq. 2) with a terminal condition, the backward equation is solved by $p(q,t) = E_\pi[p(Y_T,T) \mid Y_t = q_t]$, with $\pi$ the Wiener measure. Section 2 forms the order-zero jet groupoid $\Gamma_0(X)$, whose morphisms are local diffeomorphisms between points of $X$, and the map on objects $F(x) = \exp\{-x\cdot J(q)\}$. Pushing forward gives $F_* : \Gamma_0(X) \to \Gamma_0(S_M)$ with $F_* = F\circ\varphi$ (Proposition 1). Its differential is expressed through a representation $\rho$ of the algebra of generators acting on $S_M$, $dF_* : T^0_{\mathrm{inf}}X \to \rho_A$ (eq. 3), with $A = m(q,t)\partial_q + s(q,t)\partial_{qq}$ (Proposition 2), and is formally integrated to $F_* : \Gamma_0(X) \to \rho_P$, an assignment of parameter paths to actions of Markov kernels $P_t$ (Proposition 3). Precomposition with oppositization gives the presheaf $\tilde F_* : \Gamma_0(X)^{\mathrm{op}} \to \Gamma_0(S_M)$. Section 3 identifies $\Gamma_0(X)$ with a one-dimensional cobordism category and $\Gamma_0(S_M)$ with $\mathrm{Vect}_{\mathrm{isos}}$, and reads kernel composition as the gluing law $\langle x|P_t p|x'\rangle = E[p_{ss}(q; x(t,t'))]$ (eq. 4).

## Key results

Proposition 1 (p. 4): if points of $X$ parameterize points of $S_M$ uniquely, $F_*$ is an isomorphism of groupoids, hence a functor, taking paths of parameters to paths of densities. Proposition 2 (p. 5): when motion on $S_M$ follows the Kolmogorov backward equation, the differential of $F_*$ assigns tangent vectors on $X$ to the action of infinitesimal generators on $S_M$. Proposition 3 (p. 5): a formal integral $F_* : \Gamma_0(X) \to \rho_P$ exists and is a monoidal functor from paths to Markov kernels. Theorem 1 (p. 6): $F_*$ is the Feynman-Kac formula, in the sense $(m_t, s_t) \mapsto \mathrm{FK}(m_t, s_t) = p(q,t)$; the proof invokes Dynkin's formula and Itô's lemma in a few lines. Lemma 1 and Theorem 2 (p. 6): the points and paths of a statistical manifold form a $\Gamma_0(S_M)$-valued presheaf on $\Gamma_0(X)$ that is a sheaf because the groupoids are diffeological spaces, with a corresponding cosheaf in the covariant case; the author remarks that this is nearly a triviality. Corollary 1 (p. 7), stated without proof: with $G = F^{-1}$, adjoint functors $G_*$ and $\tilde G_*$ exist. Lemma 2 and Corollary 2 (pp. 7 to 8): after identifying $\Gamma_0(X)$ with $1\mathrm{Cob}_n$ and $\Gamma_0(S_M)$ with $\mathrm{Vect}_{\mathrm{isos}}$, $F_*$ is a one-dimensional topological field theory, and with a Riemannian structure on $X$ the Feynman-Kac formula is a Riemannian functorial field theory. Theorem 3 (p. 8): through the Atiyah-Kontsevich-Segal gluing axioms, maximum caliber is a functorial Euclidean field theory; the proof composes Gibbs-type kernels $e^{-\lambda_f J(t_f)}\circ\cdots\circ e^{-\lambda_1 J(t_1)}$ and cites the literature for the claim that such a measure maximizes caliber. Remark 2 offers, at the level of a proposal, that practical information geometry is the study of such a field theory. All of this is asserted with proof sketches; nothing beyond the Wiener and Ornstein-Uhlenbeck moments is computed.

## Limits

The paper is an announcement. The abstract describes the caliber result as a partial formalization, and the closing paragraph says the algebraic object behind the caliber functional remains to be formalized. $X$ is taken globally equivalent to $\mathbb{R}^d$ and parameters are assumed unique, so the sheaf-theoretic content is minimal. Observations of this reader: Lemma 2 asserts two equivalences of categories in two sentences and relies on calling $S_M$ a finite-dimensional Hilbert space, which an exponential family is not in general; Proposition 1 obtains the isomorphism directly from the assumed bijectivity of the parameterization; the passage from the two-moment generator $A = m\partial_q + s\partial_{qq}$ to the general diffusion of eq. (2) is not spelled out; and the worked moments of Section 1 show sign and factor inconsistencies on the typeset page, in the mean of eq. (1) against its Fokker-Planck equation and Gaussian solution, and in the stationary Ornstein-Uhlenbeck variance, stated as $b/\lambda$ beside a density with variance $\lambda/b$.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The link to the vault's program is weak to moderate and interpretive. The sheaf here lives over the parameter space of a single system and its gluing is composition in time (Chapman-Kolmogorov read as a sewing law), whereas the multi-agent model needs fibers of beliefs over a base of agents glued by transport across agents; the two uses of sheaf and gluing should not be conflated. What the paper would supply is a functorial statement of something the Gaussian belief fibers rely on implicitly: for an exponential family with unique parameters, the dynamics of the density and the dynamics of its parameters correspond under an isomorphism of path groupoids, with Markov kernels as the image of parameter paths. For Gaussian beliefs with mean and covariance as coordinates this would license computing belief dynamics on the parameter manifold. The maximum-caliber statement bears on path-measure variational formulations, again for one system. Given the brevity of the proofs, the paper is better cited as a pointer than as an established foundation. It says nothing about Markov blankets, agents, connections or coarse-graining.

## Cross-links

Concepts: [[Statistical manifold]]; [[Exponential family]]; [[Information Geometry]]; [[Maximum entropy]]; [[Process-space variational inference]]; [[Sufficient statistics]]; [[Bayesian mechanics]].

Related sources: [[sakthivadivel2022-bayesian-mechanics-geometry]]; [[amari-2016-information-geometry-applications]]; [[pistone-2018-statistical-bundle-lagrangian]]; [[jaynes-1957-information-statistical-mechanics]]; [[fritz-2019-a-synthetic-approach-to-markov-kernels-conditional-independence-and-th]]; [[ramstead-2023-bayesian-mechanics]]; [[sakthivadivel-2023-worked-example-classical-objects]]; [[sakthivadivel-2022-entropy-maximising-parallel-transport]]; [[smithe-2023-compositional-bayesian-brain]].

## BibTeX

```bibtex
@misc{sakthivadivel2022functorial,
  author = {Sakthivadivel, Dalton A. R.},
  title = {Functorial Statistical Physics: {F}eynman--{K}ac Formulae and Information Geometries},
  year = {2022},
  eprint = {2212.13618},
  archivePrefix = {arXiv},
  primaryClass = {math-ph},
  doi = {10.48550/arXiv.2212.13618},
  note = {arXiv v1, 27 December 2022; announcement}
}
```
