---
type: paper
title: "Particular flows and attracting sets: A comment on 'How particular is the physics of the free energy principle?' by Aguilera, Millidge, Tschantz and Buckley"
aliases: ["Heins 2022 particular flows attracting sets"]
authors: ["Conor Heins"]
year: 2022
venue: "Physics of Life Reviews 42, 43-48"
arxiv: "2205.09595"
doi: "10.1016/j.plrev.2022.06.003"
url: "https://arxiv.org/abs/2205.09595"
version: "arXiv:2205.09595v1 [q-bio.NC], stamped 19 May 2022, with the title-page date printed as May 20, 2022; 9 pages. The journal version of record (Physics of Life Reviews 42, 43-48) was not the version read."
tags: [cluster/vfe, project/multi-agent, field/neuroscience, field/physics]
created: 2026-11-13
updated: 2026-11-13
---

# Particular flows and attracting sets: A comment on "How particular is the physics of the free energy principle?" by Aguilera, Millidge, Tschantz and Buckley

> [!info] Citation
> Conor Heins (2022). *Particular flows and attracting sets: A comment on "How particular is the physics of the free energy principle?" by Aguilera, Millidge, Tschantz and Buckley*. Physics of Life Reviews 42, 43-48. [arXiv:2205.09595](https://arxiv.org/abs/2205.09595) [DOI](https://doi.org/10.1016/j.plrev.2022.06.003)

[Local PDF](../pdfs/heins-2022-particular-flows-attracting-sets.pdf), 9 pages; retrieved November 13, 2026. Version read: arXiv:2205.09595v1 [q-bio.NC], stamped 19 May 2022, with the title-page date printed as May 20, 2022; 9 pages. The journal version of record (Physics of Life Reviews 42, 43-48) was not the version read. Reading basis: The first reader worked from the extracted text and did not see the typeset pages. I read all 9 pages in full against both the rendered pages and the extracted text, including Figure 1 and its caption on page 6. Equations (1) to (10) were checked against the rendered pages 2, 4 and 5. Numerical values quoted from Figure 1 were read off the plot by eye. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001 through page-008). Confirmed against those pages: (1), the blanket condition p(mu, eta | b) = p(mu|b) p(eta|b), (2), (3), (4), (5) as printed (vector order (mu, b, eta) with noise (omega_eta, omega_b, omega_mu)), (6), (7) rows (0,gamma,0), (-gamma,0,-lambda), (0,lambda,0) with gamma = Q_{eta b} and lambda = -Q_{b mu}, (8) Pi tridiagonal (2,1,0;1,2,1;0,1,2) and Gamma = 2I, (9) with -(Gamma+Q) = (-2,-gamma,0; gamma,-2,lambda; 0,-lambda,-2), (10), and the attracting-set definition on page 5. Figure 1: the angle rises from 0 to about 1.4 rad at gamma near 0.9 with lambda = 1.0, and the angle is identically 0 in the bottom row with gamma = 0. The eta range [-15, 15] is confirmed. The printed 'Pi x = grad_x ln p(x)' sign is confirmed on page 5. Hand checks: at gamma = 0 the attracting line is mu = -b/2, equal to the conditional mode; the eta-averaged particular flow is -(Gamma+Q)_{(b,mu)} applied to grad(-ln p(b,mu)), with Schur-complement precision (3/2, 1; 1, 2). Both confirm the note. Title page: arXiv:2205.09595v1 [q-bio.NC] 19 May 2022, date May 20, 2022, 9 pages.

## TL;DR

Heins studies a three-dimensional linear diffusion with a Markov blanket in its Gaussian steady state and asks how solenoidal coupling changes the set toward which internal and blanket (particular) states are attracted. By numerical demonstration in one parameterized example, solenoidal coupling between external and blanket states rotates this attracting set away from the line of conditional modes, while solenoidal coupling between blanket and internal states leaves it aligned. He concludes that the inference reading of the particular flow holds for a wider class of couplings than the target article allowed, and at arbitrary points of state space.

## Problem & setting

Aguilera et al. argued, for Ornstein-Uhlenbeck processes, that the marginal flow of internal states does not follow variational free energy gradients evaluated at the conditional mode except under restrictive conditions on solenoidal coupling. Heins accepts that statement and shifts attention from the marginal flow at the conditional mode to the flow of particular states $(\mu, b)$ at arbitrary points. The setting is an Ito diffusion $\dot{x} = f(x) + \omega$ for $x = (\eta, b, \mu)$ with independent Wiener increments (1), a steady state in which $b$ is a Markov blanket, $p(\mu, \eta \mid b) = p(\mu \mid b) p(\eta \mid b)$, conditional modes $\boldsymbol{\mu}(b) = \arg\max p(\mu \mid b)$ and $\boldsymbol{\eta}(b) = \arg\max p(\eta \mid b)$ (2), and marginal flows defined as averages of $f$ over $p(\eta, \mu \mid b)$ (3). Following the earlier literature it assumes no solenoidal coupling between internal and external states. It builds on Friston (2019), Parr et al. (2020), Da Costa et al. (2021) and work on nonreversible acceleration of diffusions.

## Method

The linear system $f(x) = \mathbf{J} x$ (5) is assumed to have a Jacobian whose spectrum has negative real parts, so that a Gaussian nonequilibrium steady state $p(x) = \mathcal{N}(x; 0, \Pi^{-1})$ exists. The flow is written in Helmholtz form $\mathbf{J} x = -(\Gamma + Q) \nabla_x \ln p(x)$ (6), with $\Gamma$ the positive-definite diffusion tensor and $Q = -Q^{\top}$ the solenoidal matrix. With $Q_{\eta\mu} = 0$ the solenoidal matrix has two parameters: $Q(\gamma, \lambda)$ has rows $(0, \gamma, 0)$, $(-\gamma, 0, -\lambda)$ and $(0, \lambda, 0)$ (7), where $\gamma = Q_{\eta b}$ couples external and blanket states and $\lambda = -Q_{b\mu}$ couples blanket and internal states. All demonstrations fix the precision $\Pi$ to the tridiagonal matrix with rows $(2,1,0)$, $(1,2,1)$, $(0,1,2)$ and set $\Gamma = 2I$ (8); the zeros $\Pi_{\mu\eta} = \Pi_{\eta\mu} = 0$ encode the blanket independently of $Q$. The flow is then the matrix product $-(\Gamma + Q) \Pi x$ (9). The object studied is the attracting set of the particular flow, defined on page 5 as $\{(\mu, b) : f_{\mu,b}(x) = 0 \text{ for some external state } \eta\}$, computed over $\eta \in [-15, 15]$ and compared with the line $\{(b, \boldsymbol{\mu}(b))\}$ on which the free energy of particular states $F(\mu, b)$ is minimized (Figure 1, page 6).

## Key results

The results are numerical demonstrations in the single example (8), shown in Figure 1 and discussed on pages 5 to 7; no general theorem is stated. With $\lambda$ fixed at 1.0, increasing $\gamma$ rotates the attracting set of particular states away from the line of conditional modes, the angle rising from zero at $\gamma = 0$ to about 1.4 radians near $\gamma = 0.9$ as read from the plot (top row), and for $\gamma \neq 0$ the paper writes $f_\mu(\mu, b, \eta) \not\propto -\nabla_{\boldsymbol{\mu}(b)} F(\boldsymbol{\mu}(b), b)$ and $\not\propto -\nabla_\mu F(\mu, b)$ (10). The rotation comes with a contraction of the attracting set's extent over the same range of $\eta$, which the author relates to nonreversible acceleration of convergence. With $\gamma = 0$, varying $\lambda$ leaves the attracting set aligned with the line of conditional modes at every tested value (bottom row). From this the paper concludes that in these systems the only constraint needed for internal states to minimize free energy is $Q_{\eta b} = 0$, and it disputes the target article's claim that only block-diagonal solenoidal coupling sustains free-energy-minimizing marginal flows. Page 5 observes that any nonzero $\gamma$ or $\lambda$ produces at least unidirectional Jacobian coupling between internal and external states despite the blanket. Page 7 states, as a suspicion, that alignment persists whenever solenoidal coupling is absent between autonomous and non-autonomous states and unconstrained within each subset. My hand check from (9) with $\gamma = 0$ gives the attracting line $\mu = -b/2 = \boldsymbol{\mu}(b)$ for every $\lambda$, in agreement with the bottom row.

## Limits

The author restricts the analysis to linear diffusions in one three-dimensional example with fixed $\Pi$ and $\Gamma$, assumes $Q_{\eta\mu} = 0$, and labels the extension to particular partitions with autonomous states a suspicion. My observations: alignment of a zero set with the line of conditional modes is weaker than proportionality of the flow to a free energy gradient, and the paper gives no formula for the sense in which particular states point along gradients of $F(\mu, b)$. By my hand calculation from (9) with $\gamma = 0$, the average of the particular flow over $p(\eta \mid b)$ equals $-(\Gamma + Q)$ restricted to $(b, \mu)$ applied to the gradient of $-\ln p(b, \mu)$, a gradient mixed with a solenoidal rotation, which is the form in Da Costa et al. (2021). The text sets $\Pi x = \nabla_x \ln p(x)$, which has the opposite sign for a zero-mean Gaussian, and the coordinate ordering differs between the declared $x = (\eta, b, \mu)$ and the vectors printed in (5) and (9).

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The paper sits in the regime that Gaussian beliefs occupy: a Gaussian steady state whose blanket is a zero block of the precision matrix, with the flow split into a dissipative part and a conservative solenoidal part. What it would supply is a concrete sorting of conservative couplings by whether they preserve the free-energy-descent reading: solenoidal mixing among a system's own internal and blanket states leaves the attracting set on the free energy minimum, while solenoidal coupling between the blanket and the outside rotates it away. For Hamiltonian belief dynamics that suggests, by analogy, that conservative terms internal to an agent are compatible with an inference reading and that conservative terms across the boundary are the ones to scrutinize. The correspondence is interpretive: $Q$ here is a constant skew matrix on a flat space of physical states in one numerical example, not a symplectic structure on a belief manifold, and the paper contains no metric, connection or transport. The remark that solenoidal flow induces Jacobian coupling between internal and external states despite the blanket is a caution against reading blankets off the couplings between agents. The strength of the link is moderate.

## Cross-links

Concepts: [[Bayesian mechanics]]; [[Markov blanket interpretation debate]]; [[Markov Blanket]]; [[Nonequilibrium steady state]]; [[Hamiltonian belief dynamics]]; [[Gaussian Beliefs]]; [[Variational free energy]].

Related sources: [[aguilera-2022-particular-physics]]; [[heins-2022-sparse-coupling-markov]]; [[dacosta-2021-bayesian-mechanics]]; [[friston-2019-particular-physics]]; [[parr-2020-markov-blankets-thermodynamics]]; [[friston-2021-stochastic-chaos-markov]]; [[friston-2023-fep-simpler]]; [[biehl-2021-technical-critique]]; [[friston-2021-interesting-observations-fep]]; [[barp-2022-geometric-methods-sampling]]; [[ramstead-2022-notation-minima-comment]]; [[sakthivadivel-2022-regarding-flows-fep]].

## BibTeX

```bibtex
@article{heins2022particular,
  author = {Heins, Conor},
  title = {Particular flows and attracting sets: A comment on ``{H}ow particular is the physics of the free energy principle?'' by {A}guilera, {M}illidge, {T}schantz and {B}uckley},
  journal = {Physics of Life Reviews},
  volume = {42},
  pages = {43--48},
  year = {2022},
  doi = {10.1016/j.plrev.2022.06.003},
  eprint = {2205.09595},
  archivePrefix = {arXiv},
  primaryClass = {q-bio.NC}
}
```
