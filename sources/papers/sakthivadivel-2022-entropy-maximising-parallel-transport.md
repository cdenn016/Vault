---
type: paper
title: "Entropy-Maximising Diffusions Satisfy a Parallel Transport Law"
aliases: ["Sakthivadivel 2022 entropy maximising parallel transport"]
authors: ["Dalton A. R. Sakthivadivel"]
year: 2022
venue: "arXiv preprint (math-ph)"
arxiv: "2203.08119"
doi: "10.48550/arXiv.2203.08119"
url: "https://arxiv.org/abs/2203.08119"
version: "arXiv:2203.08119v3 [math-ph], 4 January 2023 (document dated 5th January 2023); 17 pages. No journal reference on the PDF."
tags: [cluster/gauge-theory, cluster/vfe, cluster/info-geometry, project/multi-agent, field/mathematics, field/physics, field/statistics]
created: 2026-11-13
updated: 2026-11-13
---

# Entropy-Maximising Diffusions Satisfy a Parallel Transport Law

> [!info] Citation
> Dalton A. R. Sakthivadivel (2022). *Entropy-Maximising Diffusions Satisfy a Parallel Transport Law*. arXiv preprint (math-ph). [arXiv:2203.08119](https://arxiv.org/abs/2203.08119)

[Local PDF](../pdfs/sakthivadivel-2022-entropy-maximising-parallel-transport.pdf), 17 pages; retrieved November 13, 2026. Version read: arXiv:2203.08119v3 [math-ph], 4 January 2023 (document dated 5th January 2023); 17 pages. No journal reference on the PDF. Reading basis: The first reader worked from the extracted text and did not see the typeset pages. The note rests on the extracted text. Pages 1 to 15 were read in full: abstract, Sections 1 to 5, Definitions 1 to 3, Theorems 1 to 3, Propositions 1 to 4, Corollaries 1 and 2, Remarks 1 and 2, and Example 1. The reference list on pages 15 to 17 was skimmed. Equations (1) to (5) and the unnumbered displays reported below were legible in the extracted text; the final transport expression in the proof of Proposition 3 was ambiguous. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, page-004, page-005, page-006, page-007, page-008, page-009, page-010, page-011, page-012, page-013, page-014, page-015). Confirmed against those pages: (1) ds^i_j(T) = -omega^i_j(T)s; (2) constrained entropy action; (3) -ln p = lambda J; (4) d_i p = -lambda d_i J p; (5) Lagrangian (-ln p - lambda J)e^{-lambda J'}p; Theorem 2 transformation p -> e^{-lambda J'}p with lambda J -> lambda J' + lambda J; Proposition 2 pullback A + g^{-1}dg with A = 0 and e^{-J}d e^{J} = d_i J dx^i; transport tra = exp{-int phi*A} (p. 12); Example 1 components (2x,2y), A_i -> A_i + d_i J, level sets x^2+y^2=c, Gaussian Z^{-1}exp{-x^2-y^2}. Title page: v3, 4 Jan 2023, dated 5th January 2023, MSC printed as Primary 60510 (typo in the paper itself).

## TL;DR

The paper recasts constrained maximum entropy for a stationary diffusion as a gauge theory on a principal bundle over state space whose structure group is the positive reals: the constraint function $J$ supplies an exact, flat connection $dJ$, and the maximum-entropy density $p = e^{-\lambda J}$ is a covariantly constant section of the associated line bundle. Its main theorem states that a scalar field is the stationary solution of a Fokker-Planck equation in a scalar potential if and only if parallel transport exists in that bundle.

## Problem & setting

The paper asks why constrained entropy maximization produces exponential-form densities and how this variational method of inference relates to solving the stationary Fokker-Planck equation without integrating it. The setting is a smooth manifold $X$ taken as the state space of a stationary stochastic process with density $p(x)$, constraint functions $J_k$ with prescribed expectations, and Lagrange multipliers treated as arbitrary degrees of freedom. The author builds on Jaynes's maximum entropy principle, on the results of Jordan, Kinderlehrer and Otto and of Markowich and Villani that the Fokker-Planck equation is the gradient flow of a free energy (constrained entropy) functional, and on standard principal-bundle gauge theory (Bleecker, Nakahara). Earlier appearances of gauge symmetry and parallel transport in inference (Amari 2001, Sengupta and Friston 2017) and in statistical physics (Polettini 2012) are acknowledged in Remark 1; the author distinguishes them as concerning flows, whereas this paper concerns covariance with constraints at the point of maximum entropy. Standing restrictions are stationarity, a gradient (potential) drift and holonomic constraints.

## Method

Section 2 recalls a principal $G$-bundle $P \to X$ with connection one-form $\omega$, an associated vector bundle $E = P \times_G F$, and the parallel-section condition $(d + \omega)s = 0$, written for matrix Lie algebras as $ds^i_j(T) = -\omega^i_j(T)s$ (eq. 1). Section 3 defines the constrained Shannon entropy as an action (Definition 2, eq. 2), $$S[p;J] = -\int_X \ln\{p(x)\}p(x)dx - \sum_k \lambda_k\left(\int_X J_k(x)p(x)dx - C_k\right),$$ whose Euler-Lagrange equation is given as $-\ln\{p(x)\} = \lambda J(x)$ (eq. 3), that is $p = \exp\{-\lambda J\}$. Section 4 differentiates this to obtain $\partial_i p(x) = -\lambda\partial_i J(x)p(x)$ (eq. 4) and reads it as eq. (1) with connection $dJ$. The bundle is then constructed. Definition 3 introduces the abelian Lie group $\mathrm{Exp}^\times$ of elements $e^q$ with $q \in \mathbb{R}$, in bijection with $\mathbb{R}_{>0}$ and with Lie algebra $\mathbb{R}$. Proposition 1 builds a principal $\mathrm{Exp}^\times$-bundle with local section $\sigma : x \mapsto (x, e^{J(x)})$ and an associated real line bundle $E$ with section $s : x \mapsto (x, p(x))$. Proposition 2 takes the pullback connection $\sigma^*\omega = A + g^{-1}dg$ with $A = 0$, so that $e^{-J}de^{J} = \partial_i J dx^i$; the gauge field is the Maurer-Cartan form of $e^J$, namely $dJ$. A change of constraint acts by $p \mapsto e^{-\lambda J'}p$ together with $\lambda J \mapsto \lambda J' + \lambda J$ (Theorem 2), and in Example 1 as $A_i \mapsto A_i + \partial_i J$. Parallel transport of a point along a path $\varphi$ is $\mathrm{tra} = \exp\{-\int_{[0,1]}\varphi^*A\}$ (Proposition 3).

## Key results

Theorem 1 (p. 8) states that parallel transport occurs at the maximum-entropy density, since eq. (4) is the parallel-transport equation for the connection $dJ$ and integrates to eq. (3); the proof is a short calculation, and the author describes the statement as naive until $J$ is shown to be a connection on a bundle to which $p$ lifts (Remark 1 and the following paragraph, p. 8). Theorem 2 (p. 9) states that the maximum-entropy action is gauge invariant: under $p \mapsto e^{-\lambda J'}p$ and $\lambda J \mapsto \lambda J' + \lambda J$ the Lagrangian reduces to $(-\ln\{p\} - \lambda J)e^{-\lambda J'}p$ (eq. 5), whose stationarity condition is again eq. (3). Propositions 1 and 2 (pp. 10 to 11) construct the principal and associated bundles and identify the components of $\nabla J$ as the gauge field. Corollary 1 (p. 11) states that both bundles are flat and admit a covariantly constant section because $dJ$ is exact; Corollary 2 states that the level sets $J(x) = c$ are integral curves of $\ker(\sigma^*\omega)$. Proposition 3 (p. 12) is stated as yielding $\exp\{J(x)\}$ for the transport map, while its proof concludes that endpoints of horizontal lifts are given by $\exp\{-\lambda J(x)\}$; statement and proof disagree in sign and factor. Example 1 (p. 13) works the quadratic constraint on $\mathbb{R}^2$, with connection components $(2x, 2y)$, circular level sets $x^2 + y^2 = c$ and the Gaussian $Z^{-1}\exp\{-x^2 - y^2\}$. Theorem 3 (p. 13), the stated main result, asserts that $p(x)$ is the stationary solution to some Fokker-Planck equation (in the proof, one in a scalar potential $J$) if and only if parallel transport solutions exist in that geometry; the proof assembles the earlier statements and imports the equivalence between stationary Fokker-Planck solutions and stationary points of a free energy functional from the cited functional-analytic literature. Proposition 4 (p. 14) states that maximizing likelihood is a charged flow, meaning that a flow crossing level sets has a vertical component; the argument is informal. Section 5 (pp. 14 to 15) names the construction a constraint geometry and suggests, without proof, that the horizontal-vertical splitting reinterprets the gradient-plus-circulation decompositions of Graham, Ao, Qian and Friston, deferring the account to forthcoming work. All results are analytic; there are no simulations.

## Limits

The author restricts the construction to stationary processes and to a density built over state space, and leaves flows on a statistical manifold, nonequilibrium steady states with fluxes and time-dependent statistical mechanics to future work (Remark 1 and Section 5). The connection $dJ$ is exact, so the bundle is abelian and flat and every holonomy is trivial; the construction therefore covers gradient drift only. Observations of this reader: Theorem 2 shows that the transformed action has the same stationarity equation in the original variable, which is a change-of-variables statement and is weaker than invariance of the value of $S$; the Euler-Lagrange step absorbs the additive constant from differentiating $p\ln p$ without comment; once the connection is fixed as $dJ$, the equivalence in Theorem 3 adds no analytic content beyond the cited results; and Definition 3 calls $\mathrm{Exp}^\times$ a subgroup of $(\mathbb{R},+)$ where it is its image under the exponential map.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> This is the construction in the Bayesian mechanics lineage that comes closest to a bundle with a connection, and its correspondence with the vault's model is interpretive, not exact. Here the base is the state space of one system, the fiber over a state is the real line of density values, the structure group is the abelian group of positive rescalings, and the connection is exact. In the gauge-theoretic multi-agent model the fibers are statistical manifolds of Gaussian beliefs, the group is nonabelian, and transport acts between agents. What the paper would supply is a precise statement of the trivial sector: reweighting a density by $e^{-\lambda J'}$, a change of reference potential, is a gauge transformation, and an equilibrium density is a horizontal section of a flat line bundle. It also marks a boundary that a non-flat inter-agent connection has to cross, since nothing in this paper produces curvature or holonomy; the papers by Polettini and by Feng and Wang in this batch show that curvature of an analogous abelian connection is the signature of broken detailed balance. The link to transport between agents is weak; the link to the reference-measure gauge freedom of a single belief is moderate.

## Cross-links

Concepts: [[Maximum entropy]]; [[Parallel transport]]; [[Gauge Theory]]; [[Gauge transformation]]; [[Fibre Bundle]]; [[Bayesian mechanics]]; [[Nonequilibrium steady state]]; [[Holonomy]].

Related sources: [[sakthivadivel2022-bayesian-mechanics-geometry]]; [[sengupta2017gauge]]; [[sengupta-2016-neuronal-gauge]]; [[jaynes-1957-information-statistical-mechanics]]; [[friston-2019-particular-physics]]; [[nakahara-2003-geometry-topology-physics]]; [[polettini-2012-nonequilibrium-thermodynamics-gauge]]; [[feng-2011-potential-flux-decomposition]]; [[barp-2021-measure-preserving-diffusions]]; [[barp-2022-geometric-methods-sampling]].

## BibTeX

```bibtex
@misc{sakthivadivel2022entropy,
  author = {Sakthivadivel, Dalton A. R.},
  title = {Entropy-Maximising Diffusions Satisfy a Parallel Transport Law},
  year = {2022},
  eprint = {2203.08119},
  archivePrefix = {arXiv},
  primaryClass = {math-ph},
  doi = {10.48550/arXiv.2203.08119},
  note = {arXiv v3, 4 January 2023; earlier versions circulated as "A constraint geometry for inference and integration"}
}
```
