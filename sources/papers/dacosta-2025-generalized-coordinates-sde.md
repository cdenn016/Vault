---
type: paper
title: "A Theory of Generalized Coordinates for Stochastic Differential Equations"
aliases: ["Costa et al. 2025 generalized coordinates sde"]
authors: ["Lancelot Da Costa", "Nathaël Da Costa", "Conor Heins", "Johan Medrano", "Grigorios A. Pavliotis", "Thomas Parr", "Ajith Anil Meera", "Karl Friston"]
year: 2025
venue: "Studies in Applied Mathematics 154(5), e70062"
arxiv: "2409.15532"
doi: "10.1111/sapm.70062"
url: "https://arxiv.org/abs/2409.15532"
version: "arXiv:2409.15532v3 [math.PR]; the date stamp in the extracted first page reads 1 Jun 2026. 49 pages (41 of text, then bibliography and a two-part appendix). The title on this version uses the British spelling: 'A theory of generalised coordinates for stochastic differential equations'. The journal version of record is Studies in Applied Mathematics 154(5), e70062 (2025) per the manifest; no journal pagination appears on this PDF."
tags: [cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-11-13
updated: 2026-11-13
---

# A Theory of Generalized Coordinates for Stochastic Differential Equations

> [!info] Citation
> Lancelot Da Costa, Nathaël Da Costa, Conor Heins, Johan Medrano, Grigorios A. Pavliotis, Thomas Parr, Ajith Anil Meera, Karl Friston (2025). *A Theory of Generalized Coordinates for Stochastic Differential Equations*. Studies in Applied Mathematics 154(5), e70062. [arXiv:2409.15532](https://arxiv.org/abs/2409.15532) [DOI](https://doi.org/10.1111/sapm.70062)

[Local PDF](../pdfs/dacosta-2025-generalized-coordinates-sde.pdf), 49 pages; retrieved November 13, 2026. Version read: arXiv:2409.15532v3 [math.PR]; the date stamp in the extracted first page reads 1 Jun 2026. 49 pages (41 of text, then bibliography and a two-part appendix). The title on this version uses the British spelling: 'A theory of generalised coordinates for stochastic differential equations'. The journal version of record is Studies in Applied Mathematics 154(5), e70062 (2025) per the manifest; no journal pagination appears on this PDF. Reading basis: Read in full from the extracted text: pages 1 to 41 (abstract, introduction, Chapters 1 to 4, software note). The bibliography on pages 42 to 47 was spot-checked only (entries [4] to [11], [39], [40]). Appendix A.1 (notation) and A.2 (Lemma A.2.1 and its proof, pages 48 to 49) were not read beyond the opening of the statement. Proofs in Chapters 1 and 2 were read. The first reader worked from the extracted text and did not see the typeset pages. Matrix displays for $\mathbf{D}$, $\mathbf{D}'$ and the covariance (2.6), (2.7) were legible in structure but are described in words. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, page-007, page-008, page-009, page-010, page-011, page-017, page-018, page-021, page-022, page-024, page-025, page-029, page-031, page-032, page-033, page-034, page-035). Confirmed against those pages: (1.5), (1.6), (1.10), (1.12), (1.13) structure of D and D', (1.14), (1.17), (1.19), (2.1), (2.2), (2.6), (2.7), (2.16), (2.19), (2.20), (2.25), (2.29), (2.32), (2.34), (2.37), (3.3), (3.10), (3.12), (3.14), (3.21), (3.23), (3.26), (3.30), (3.31), (3.33). Statements checked: Theorem 1.2.2 (p. 10), Theorem 1.2.4 (p. 11), Example 1.2.5, Lemma 2.1.1 with Remark 2.1.2 (p. 17), Propositions 2.2.1, 2.2.3, 2.2.5 (locally uniform on (-R/lambda, R/lambda), lambda = max(1, ||A||_inf, ||A^T||_inf)), Theorem 2.2.10 under Assumptions 2.2.4 and 2.2.9 (p. 23); N = 4 in text p. 29 vs N + 1 = 4 in Figure 3.4 caption p. 31; 'third order optimisation scheme' and underdamped Langevin comparison p. 34; 'not been bench-marked' p. 38. Title page: 'A theory of generalised coordinates for stochastic differential equations', eight authors in the stated order, stamp arXiv:2409.15532v3 [math.PR] 1 Jun 2026.

## TL;DR

The paper gives a pathwise theory of generalized coordinates of motion for stochastic differential equations with additive, temporally correlated noise: the solution is represented by its Taylor coefficients at a time point, which evolve under a linear shift, and the representation is exact when flow and noise are analytic. It solves the linear equation driven by analytic stationary Gaussian noise in closed form, writes the path-integral Lagrangian in these coordinates, and derives generalized Bayesian filtering as a gradient flow on a Laplace free energy.

## Problem & setting

The problem is to analyze and simulate equations $\frac{d}{dt}x_t = f(x_t) + w_t$ whose noise has temporal correlations, so that the solution is not Markov. The standing assumptions are additive noise, a deterministic initial condition, a flow $f$ and noise sample paths that are $(N-1)$ times continuously differentiable (Assumption 1.1.1), and for most of Chapter 2 a mean-zero stationary Gaussian process with sufficiently regular autocovariance (Assumptions 2.1.5, 2.2.2, 2.2.4, 2.2.9). The paper positions itself against three existing approaches: stochastic integration with respect to semimartingales, rough path theory, and Markovian realization by white-noise equations in an extended state space, which Stratonovich already noted is accurate only on time scales long compared with the correlation time. It formalizes a device that originated in dynamic expectation maximization and generalized filtering for neuroimaging time series (Friston and colleagues, 2008 to 2010) and that was later used in path-based derivations of the free energy principle. It draws on the Picard-Lindelöf and Cauchy-Kovalevskaya theorems, on the Wong-Zakai approximation theorems, and on sample-path regularity results for Gaussian processes.

## Method

Differentiating the equation in time relates the serial derivatives of the solution at $t=0$ (1.3). The space of generalized coordinates of order $n$ is $\mathbb{G}^{d,n} \cong \mathbb{R}^{d(n+1)}$ (1.5). The generalized flow $\mathbf{f}$ stacks functions $f^{(n)}$ defined by $f^{(n)}(x_t, \dots, \tfrac{d^n}{dt^n}x_t) = \tfrac{d^n}{dt^n}f(x_t)$ (1.6, Definition 1.1.2); the local linear approximation (Approximation 1.1.3) drops derivatives of $f$ above first order, leaving rows $\nabla f(z^{(0)})z^{(n)}$ (1.10). The generalized process is the solution of the Cauchy problem $\frac{d}{dt}\mathbf{x}_t = \mathbf{D}\mathbf{x}_t$, $\mathbf{D}'\mathbf{x}_0 = \mathbf{f}(\mathbf{x}_0) + \mathbf{w}_0$, $x^{(0)}_0 = z$ (1.12), where $\mathbf{D}$ is the block shift sending each order of motion to the next, so that $\mathbf{x}_t = \exp(t\mathbf{D})\mathbf{x}_0$ is a moving Taylor polynomial (1.14). For stationary noise with autocovariance $\kappa(h) = E[w_t w_{t+h}^\top]$ (2.1), the generalized fluctuations satisfy $E[w^{(n)}_t w^{(m)\top}_{t+h}] = (-1)^n\kappa^{(n+m)}(h)$ (2.2), which gives an equal-time covariance $\Sigma$ with a checkerboard pattern of even derivatives of $\kappa$ at zero (2.7). The Lagrangian on generalized states is $\mathcal{L}(\mathbf{x}_0) = (\mathbf{D}'\mathbf{x}_0 - \mathbf{f}(\mathbf{x}_0))^\top(2\Sigma)^{-1}(\mathbf{D}'\mathbf{x}_0 - \mathbf{f}(\mathbf{x}_0))$, equal to $-\log p(\mathbf{x}_0)$ up to a constant (2.32); states embed into paths by $\eta: z \mapsto (t \mapsto \exp(t\mathbf{D})z)$ (2.29) and the action is $\mathcal{L}\circ\eta^{-1}$ (2.34). Generalized filtering uses the generative model $p(\mathbf{y}_t \mid \mathbf{x}_t) = \mathcal{N}(\mathbf{y}_t; \mathbf{g}(\mathbf{x}_t), \Sigma^z)$, $p(\mathbf{x}_t) = \mathcal{N}(\mathbf{D}'\mathbf{x}_t - \mathbf{f}(\mathbf{x}_t); 0, \Sigma^w)$ (3.10), the variational free energy $F(q; \mathbf{y}_t) = E_q[\log q(\mathbf{x}_t) - \log p(\mathbf{y}_t, \mathbf{x}_t)]$ (3.12), a Gaussian posterior with $\Sigma^* = (\nabla^2_\mu V)^{-1}$ under the Laplace approximation (3.21), and the mean flow $\dot\mu_t = \mathbf{D}\mu_t - \lambda\nabla_\mu V(\mathbf{y}_t, \mu_t) - \tfrac{\lambda}{2}\nabla_\mu\log\det\nabla^2_\mu V(\mathbf{y}_t, \mu_t)$ (3.23), with $V = -\log p(\mathbf{y}_t, \mathbf{x}_t)$ (3.14) and $\lambda > 0$ a hyperparameter.

## Key results

Proved: Theorem 1.2.2 (p. 10) gives a unique local $C^N$ solution for each noise path, with Taylor error $o_\omega(|t|^N)$ (1.17). Theorem 1.2.4 (p. 11), a special case of Cauchy-Kovalevskaya, gives an analytic solution when $f$ and the noise path are analytic, so that with $N = \infty$ the zeroth generalized coordinate equals the solution on $(-R_\omega, R_\omega)$ (1.19); Example 1.2.5 shows the radius can be arbitrarily small even for entire coefficients. Lemma 1.3.2 and Theorem 1.3.4 (pp. 13-14) show that white noise convolved with a Gaussian has a power series representation and almost surely entire sample paths; Proposition 1.3.8 (p. 15) shows that the Gaussian convolution of any integrable noise path is entire. Lemma 2.1.1 (p. 17) is derived formally and made rigorous for Gaussian processes under Assumption 2.1.5 through Propositions 2.1.6 and 2.1.7 (p. 19), which rely on a cited regularity result; Theorem 2.1.9 (p. 20) gives $\mathbf{w}_t \sim \mathcal{N}(0, \Sigma)$ for all $t$. For the linear equation $\dot x_t = Ax_t + w_t$, Proposition 2.2.1 (p. 21) gives mean and autocovariance at finite order (2.16), Propositions 2.2.3 and 2.2.5 give the limits $e^{At}x_0$ (2.19) and (2.20) with locally uniform convergence on $(-R/\lambda, R/\lambda)$, $\lambda = \max(1, \|A\|_\infty, \|A^\top\|_\infty)$, and Theorem 2.2.10 (p. 23) identifies the unique solution as the Gaussian process with these statistics under Assumptions 2.2.4 and 2.2.9. Formal: the density obeys the Liouville equation $\partial_t\rho_t(z) = -\nabla\rho_t(z)\cdot\mathbf{D}z$ (2.25), stated as formal for $N = \infty$; the path of least action solves $\mathbf{D}'\bar{\mathbf{x}}_0 = \mathbf{f}(\bar{\mathbf{x}}_0)$ (2.37). Derived algebraically: the filtering equations (3.26), and under the local linear approximation $\nabla^3_\mu V \equiv 0$ (3.30), so the Laplace free energy is exact and the flow reduces to $\dot\mu_t = \mathbf{D}\mu_t - \lambda\nabla_\mu V$ (3.33); a footnote identifies the scheme without parameter inference with dynamic expectation maximization. Shown by simulation: zigzag integration is accurate on short intervals for linear, Lotka-Volterra and Lorenz systems and the linearized variant stays accurate longer (Figures 3.1 to 3.3); the flow $\dot{\bar{\mathbf{x}}}_t = \mathbf{D}\bar{\mathbf{x}}_t - \lambda\nabla\mathcal{L}(\bar{\mathbf{x}}_t)$ (3.3) approaches the noise-free path as $\lambda$ grows for a two-dimensional linear system (Figure 3.4); a filter with $N = M = 5$ reconstructs a partially observed Lorenz system (Figure 3.5).

## Limits

The authors state that faithfulness under the local linear approximation for nonlinear flows is not established (Remark 1.2.1), that the radius of validity is expected to shrink to zero in the rough-noise limit so that the Wong-Zakai route to diffusions needs rate estimates not supplied here, that multiplicative noise, multiscale equations and non-stationary noise are left to future work, that whether an analytic autocovariance implies almost surely analytic sample paths is unknown to them (hence the separate Assumption 2.2.9), and that the non-linearized filter has not been benchmarked against the linearized one. My observations: the claims that (3.3) converges to the most likely path and that the filter mean (3.23) tracks the posterior mode are supported by intuition and one simulation each, with no convergence theorem; the role of $\lambda$ is heuristic; the text gives the order for Figure 3.4 as $N = 4$ in one place and $N + 1 = 4$ in the caption; two cited steps rest on online forum posts.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The paper bears on the Gaussian-belief and belief-dynamics objects of the program, and not on its gauge structure. Generalized filtering is a concrete case of a Gaussian belief $q = \mathcal{N}(\mu, \Sigma)$ whose covariance is the inverse Hessian of an energy and whose mean follows a free-energy gradient plus a kinematic term $\mathbf{D}\mu$ that carries velocity, acceleration and higher orders of motion. The authors themselves compare this to underdamped Langevin dynamics and call it a higher-order optimization scheme. Reading the $\mathbf{D}$ term as belief inertia or as a Hamiltonian structure is interpretive: $\mathbf{D}$ is a nilpotent shift with no symplectic form and no mass matrix, and the descent uses a Euclidean gradient with a scalar rate, not a Fisher-metric natural gradient. What the paper would supply is the rigorous footing for path-based Bayesian mechanics, where states and paths are identified through the embedding (2.29) and the Lagrangian (2.32) replaces a stationary density, together with precise validity conditions (analyticity, local-in-time exactness). It contains nothing on Markov blankets, on several agents, on transport between agents or on coarse-graining. The link is moderate for temporal depth of single-agent Gaussian beliefs and weak elsewhere.

## Cross-links

Concepts: [[Generalised coordinates of motion]]; [[Laplace approximation]]; [[Variational free energy]]; [[Gaussian process]]; [[Gaussian Beliefs]]; [[Kalman filter]]; [[Bayesian mechanics]]; [[Belief dynamics]].

Related sources: [[friston-2008-dem]]; [[parr-friston-2019-generalised]]; [[friston-2023-path-integrals-particular]]; [[friston-2023-fep-simpler]]; [[kalman-1960-approach-linear-filtering]]; [[pavliotis-2008-multiscale-methods-averaging]]; [[barp-2022-geometric-methods-sampling]].

## BibTeX

```bibtex
@article{dacosta2025generalized,
  author  = {Da Costa, Lancelot and Da Costa, Nathaël and Heins, Conor and Medrano, Johan and Pavliotis, Grigorios A. and Parr, Thomas and Anil Meera, Ajith and Friston, Karl},
  title   = {A Theory of Generalized Coordinates for Stochastic Differential Equations},
  journal = {Studies in Applied Mathematics},
  volume  = {154},
  number  = {5},
  pages   = {e70062},
  year    = {2025},
  doi     = {10.1111/sapm.70062},
  eprint  = {2409.15532},
  archivePrefix = {arXiv},
  primaryClass  = {math.PR}
}
```
