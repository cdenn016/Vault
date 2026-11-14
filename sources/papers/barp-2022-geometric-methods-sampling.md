---
type: paper
title: "Geometric Methods for Sampling, Optimisation, Inference and Adaptive Agents"
aliases: ["Barp et al. 2022 geometric methods sampling"]
authors: ["Alessandro Barp", "Lancelot Da Costa", "Guilherme França", "Karl Friston", "Mark Girolami", "Michael I. Jordan", "Grigorios A. Pavliotis"]
year: 2022
venue: "Handbook of Statistics vol. 46 (Geometry and Statistics), pp. 21-78, Elsevier"
arxiv: "2203.10592"
doi: "10.1016/bs.host.2022.03.005"
url: "https://arxiv.org/abs/2203.10592"
version: "arXiv:2203.10592v3 [stat.ML], dated 25 July 2022 on the first page; 42 pages (32 of text with table of contents, 10 of references). The title on this version uses the British spelling 'Optimisation'. It is the preprint of the chapter in Handbook of Statistics vol. 46, pp. 21-78 (Elsevier, 2022); the journal pagination does not appear on the PDF."
tags: [cluster/info-geometry, cluster/vfe, project/multi-agent, field/statistics, field/mathematics, field/cs-ml]
created: 2026-11-13
updated: 2026-11-13
---

# Geometric Methods for Sampling, Optimisation, Inference and Adaptive Agents

> [!info] Citation
> Alessandro Barp, Lancelot Da Costa, Guilherme França, Karl Friston, Mark Girolami, Michael I. Jordan, Grigorios A. Pavliotis (2022). *Geometric Methods for Sampling, Optimisation, Inference and Adaptive Agents*. Handbook of Statistics vol. 46 (Geometry and Statistics), pp. 21-78, Elsevier. [arXiv:2203.10592](https://arxiv.org/abs/2203.10592) [DOI](https://doi.org/10.1016/bs.host.2022.03.005)

[Local PDF](../pdfs/barp-2022-geometric-methods-sampling.pdf), 42 pages; retrieved November 13, 2026. Version read: arXiv:2203.10592v3 [stat.ML], dated 25 July 2022 on the first page; 42 pages (32 of text with table of contents, 10 of references). The title on this version uses the British spelling 'Optimisation'. It is the preprint of the chapter in Handbook of Statistics vol. 46, pp. 21-78 (Elsevier, 2022); the journal pagination does not appear on the PDF. Reading basis: Read in full from the extracted text: pages 1 to 32 (abstract, Sections 1 to 5, acknowledgements). The reference list on pages 33 to 42 was not read apart from spot checks of entries [81], [112], [115], [125], [226] and [230]. The first reader worked from the extracted text and did not see the typeset pages. The equations I report, (3), (6), (8), (9), (13), (28), (31), (34), (35), (39), (42) and the EFE identity, are those whose extracted text is unambiguous; equation (27), the rate table (11) and the generator formula (37) were legible only in part and are not reported in symbols. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, page-005, page-007, page-008, page-009, page-012, page-013, page-014, page-015, page-022, page-026, page-027, page-028). Confirmed against those pages: (3), (6), (7), (8), (9), (13), (15)-(17) in structure, (19), (25), (27) as printed, (28), (30), (31), (32), (34), (35), (39), (EFE), (AIF), (42); Definition 5.1 (precise agent: P(pi | s) Dirac); footnote 10 and ref [230] (Samuel Tenka, personal communication); Figure 1 (SO(n), n = 500, spherical spin glass, p. 12); Figure 4 T-maze on p. 31. Title, seven authors, arXiv:2203.10592v3 [stat.ML], 25 Jul 2022 confirmed on page 1.

## TL;DR

The chapter is a conceptual survey showing that accelerated optimization, sampling, kernel-based inference and active-inference agents rest on shared geometric structures: bracket vector fields and Poisson geometry for dissipative Hamiltonian flows, the complete family of measure-preserving diffusions with its symmetric (reversible) and antisymmetric (irreversible) parts, Stein operators built from the same brackets, and an expected free energy that is the negative log probability of a decision. It states results and refers to the cited literature for proofs.

## Problem & setting

The authors ask which geometric structures underlie four problems that are usually treated separately: minimizing a function $V$ on a manifold, drawing samples from a target measure $\rho$, fitting a statistical model to a target by minimizing a discrepancy, and making decisions under uncertainty. The standing assumptions are smoothness of $V$ and of the target density, with convexity or strong convexity of $V$ where convergence rates are quoted. The chapter builds on geometric numerical integration (splitting methods, symplectic integrators, shadow Hamiltonians), on the continuous-time view of accelerated gradient methods as dissipative Hamiltonian systems (França, Jordan and Vidal; França, Barp, Girolami and Jordan), on the Jordan, Kinderlehrer and Otto picture of sampling as gradient flow in Wasserstein space, on the complete recipe of Ma, Chen and Fox and its manifold form by Barp, Takao, Betancourt, Arnaudon and Girolami for measure-preserving diffusions, on Hamiltonian Monte Carlo, on reproducing kernel Hilbert spaces and Stein's method, and on the discrete-state active inference literature. The authors say explicitly that the exposition is conceptual and that technical statements are in the references.

## Method

Section 2 builds flows from bracket vector fields $X^B_f = B^{ij}\partial_i f \partial_j$ (3): an antisymmetric $B$ conserves $f$ and a negative semidefinite $B$ dissipates it. The working example is the conformal Hamiltonian system with $H(q,p) = \tfrac12 p_i g^{ij} p_j + V(q)$ (6) and equations of motion $\dot q^i = g^{ij}p_j$, $\dot p_i = -\partial V/\partial q^i - \gamma(t)p_i$ (8), for which $dH/dt = -\gamma(t) p_i g^{ij} p_j \le 0$ (9). A change of variables gives the time-dependent Hamiltonian $H(t,q,p) = \tfrac12 e^{-\eta(t)} p_i g^{ij} p_j + e^{\eta(t)}V(q)$ with $\eta = \int\gamma dt$ (13), and adding time and a conjugate momentum $u$ yields a conservative system in $\mathbb{R}^{2d+2}$ (15) to (17) (symplectification), to which symplectic integrators apply. Section 2.6 takes the free energy $F[\mu] = E_\mu[H] - \beta^{-1}S[\mu]$ (28), equal to $\mathrm{KL}[\mu \mid \rho]$ up to scale and an additive constant, and shows that the flow generated on the space of measures by the bracket (7) is the Fokker-Planck equation of the underdamped Langevin diffusion $dq_t = p_t dt$, $dp_t = -\partial_q V(q_t)dt - \gamma p_t dt + \sqrt{2\gamma\beta^{-1}}dw_t$ (31). Section 3 states the family of $\rho$-preserving diffusions on a manifold, $dx_t = \mathrm{curl}_\rho(A)dt + \tfrac12 \mathrm{div}_\rho(Y_i)Y_i dt + Y_i \circ dw^i_t$ (34), and its Euclidean form $dx_t = -(A+S)(x_t)\partial V(x_t)dt + \partial\cdot(A+S)(x_t)dt + \sqrt{2S(x_t)}dw_t$ (35), with $S$ symmetric, $A$ antisymmetric and $V = -\log\rho$. Section 4 defines the canonical Stein operator $\mathcal{S}_\mu = \mathrm{div}_\mu$ and the bracket form $\mathcal{S}^{S+A}_\mu(f) = \mathrm{div}_\mu(X^S_f) + \mathrm{curl}_\mu(A)(f)$ (39). Section 5 partitions a process into external, observable and autonomous paths $x = (s,o,a)$, defines a precise agent by $P(\pi \mid s)$ being a Dirac measure (Definition 5.1), and derives $-\log P(a_{>t} \mid \pi_{\le t}) = E_{P(s,o \mid a_{>t},\pi_{\le t})}[\log P(s \mid a_{>t},\pi_{\le t}) - \log P(s,o \mid \pi_{\le t})]$ (EFE), with active inference defined as minimizing this quantity over $a_{>t}$ (AIF).

## Key results

Nothing in the chapter is proved in full; results are stated or sketched with citations. Stated with a sketch from the Baker-Campbell-Hausdorff expansion (1), (4), (5): splitting integrators for Poisson systems exactly conserve a shadow function close to the Hamiltonian (Section 2.2, pp. 5-6). Stated from the cited work [9], [10]: a symplectic integrator of order $r$ applied to the symplectified system reproduces the continuum convergence rate, $V(q_k) - V^\star = V(q(t_k)) - V^\star + O(e^{-\eta(t_k)}\delta t^r)$ (19, p. 9); explicit schemes are the dissipative leapfrog (20), a Lie-group version (23) and a dissipative RATTLE scheme for constraints (24) (pp. 10-11). Argued informally: the high-friction limit $\gamma \to \infty$ of (8) is first-order gradient flow, and correspondingly overdamped Langevin (32) is the gradient flow of the free energy while underdamped Langevin is its conformal Hamiltonian counterpart (Sections 2.5 and 2.6, pp. 11-13). Shown by one simulation, quoted from [10]: on $SO(n)$ with $n = 500$ for a spherical spin glass energy, method (23) in the underdamped regime converges faster than in the overdamped regime, where it tracks Riemannian gradient descent (Figure 1, p. 12). Asserted with citations: (34) and (35) exhaust the measure-preserving diffusions up to a topological obstruction; such a diffusion is non-reversible exactly when $A \not\equiv 0$; removing irreversibility worsens the spectral gap and asymptotic variance; for strongly convex $V$ the optimal reversible geometry is $g = \partial^2 V$ (Section 3.1, pp. 14-15). Section 3.2 (pp. 16-19) attributes the success of Hamiltonian Monte Carlo to preservation of a reference measure, a conserved shadow Hamiltonian and tractable splittings, and says, hedged with 'seems', that the symplectic bracket is the only unimodular Poisson bracket available on general manifolds. Section 4 (pp. 19-25) characterizes test functions of zero mean on a connected manifold as divergences of compactly supported vector fields, reads kernel Stein discrepancy as a maximum mean discrepancy, obtains generalized score matching (41), and gives information tensors for natural gradient descent on these discrepancies. Section 5 derives the EFE identity (p. 27) and its decompositions into risk plus ambiguity (42, p. 28) and extrinsic plus intrinsic value (p. 29), and illustrates the algorithm (43) to (46) on a T-maze (Figure 4, p. 31).

## Limits

The authors state that the exposition is conceptual and defer technical conditions to the references (for example footnote 4 omits Lipschitz conditions behind (18) and (19), and footnote 5 restricts results to suitable step sizes). They note that no general guideline exists for optimizing irreversibility in nonlinear diffusions, that discretization can affect ergodicity, change the amount of irreversibility and bias the invariant measure, and that active inference has not been scaled like reinforcement learning. Footnote 10 says the vanishing of the term that yields (EFE) is shown only for countable path spaces, by personal communication [230], with the general case presumed. My observations: the precise-agent hypothesis (deterministic agent given the environment) carries the whole derivation of (EFE) and excludes agents with intrinsic noise; the uniqueness claim for the symplectic bracket is not established in the text; equation (27), printed on p. 12 without a minus sign, gives a dissipative term of opposite sign to the Fokker-Planck equation the paper derives from it on p. 13, so (27) carries a sign or transpose slip in its dissipative part.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The chapter bears most directly on Hamiltonian belief dynamics and belief inertia. Its conformal Hamiltonian system, with a kinetic metric $g$ acting as a mass matrix, a friction $\gamma$, and gradient flow recovered at high friction, is the standard template for a second-order belief dynamic whose overdamped limit is a (natural) gradient descent, and the free-energy reading of underdamped Langevin in Section 2.6 places that template on a space of probability measures. The correspondence with a belief dynamic on Gaussian statistical fibers is interpretive: the paper works with a constant metric in (6), treats manifolds by reference to [10], and never takes the Fisher metric as the kinetic metric except in the remark on Riemannian Hamiltonian Monte Carlo. The symmetric plus antisymmetric decomposition (35) is the same split that Bayesian mechanics uses for dissipative and solenoidal flow, so the paper would supply the clean statement of that split and its manifold form (34). The geometric integrators for Lie groups and for the positive-definite cone are of practical interest for group-valued and covariance-valued variables. The chapter has no conditional-independence (Markov blanket) condition, no transport between agents, no gauge connection and no coarse-graining; its agent section is single-agent. The link is strong for the Hamiltonian and natural-gradient objects and absent for the gauge and multi-agent ones.

## Cross-links

Concepts: [[Hamiltonian belief dynamics]]; [[Symplectic geometry]]; [[Hamiltonian Monte Carlo]]; [[Natural gradient]]; [[Expected Free Energy]]; [[Active Inference]]; [[Bayesian mechanics]]; [[Baker-Campbell-Hausdorff formula]].

Related sources: [[neal-2011-mcmc-hamiltonian]]; [[girolami-calderhead-2011-riemann-hmc]]; [[wibisono-2016-variational-accelerated]]; [[amari-1998-natural-gradient]]; [[dacosta-2020-discrete-state-synthesis]]; [[friston-2023-fep-simpler]]; [[barp-2021-measure-preserving-diffusions]]; [[dacosta-2023-entropy-production-stationary-diffusions]].

## BibTeX

```bibtex
@incollection{barp2022geometric,
  author    = {Barp, Alessandro and Da Costa, Lancelot and Fran{\c{c}}a, Guilherme and Friston, Karl and Girolami, Mark and Jordan, Michael I. and Pavliotis, Grigorios A.},
  title     = {Geometric Methods for Sampling, Optimisation, Inference and Adaptive Agents},
  booktitle = {Geometry and Statistics},
  series    = {Handbook of Statistics},
  volume    = {46},
  pages     = {21--78},
  publisher = {Elsevier},
  year      = {2022},
  doi       = {10.1016/bs.host.2022.03.005},
  eprint    = {2203.10592},
  archivePrefix = {arXiv},
  primaryClass  = {stat.ML}
}
```
