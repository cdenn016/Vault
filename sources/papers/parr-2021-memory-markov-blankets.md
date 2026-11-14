---
type: paper
title: "Memory and Markov Blankets"
aliases: ["Parr et al. 2021 memory markov blankets"]
authors: ["Thomas Parr", "Lancelot Da Costa", "Conor Heins", "Maxwell James D. Ramstead", "Karl J. Friston"]
year: 2021
venue: "Entropy 23(9):1105"
doi: "10.3390/e23091105"
url: "https://doi.org/10.3390/e23091105"
version: "Journal version of record: Entropy 2021, 23, 1105 (MDPI, open access, CC BY), received 10 July 2021, accepted 22 August 2021, published 25 August 2021, 23 pages."
tags: [cluster/vfe, cluster/info-geometry, project/multi-agent, field/neuroscience, field/physics, field/statistics]
created: 2026-11-13
updated: 2026-11-13
---

# Memory and Markov Blankets

> [!info] Citation
> Thomas Parr, Lancelot Da Costa, Conor Heins, Maxwell James D. Ramstead, Karl J. Friston (2021). *Memory and Markov Blankets*. Entropy 23(9):1105. [DOI](https://doi.org/10.3390/e23091105)

[Local PDF](../pdfs/parr-2021-memory-markov-blankets.pdf), 23 pages; retrieved November 13, 2026. Version read: Journal version of record: Entropy 2021, 23, 1105 (MDPI, open access, CC BY), received 10 July 2021, accepted 22 August 2021, published 25 August 2021, 23 pages. Reading basis: I read the extracted text of pages 1 to 21 in full (the reference list on pages 21 to 23 was skimmed). The first reader worked from the extracted text and did not see the typeset pages. I viewed pages 1 and 3 to 10 in the browser pane at low resolution (about 320 pixels page width), which confirmed the placement and line structure of Eqs. (1) to (4), (6), (7), (9), (10), (11) and (12) and of Table 1 but not fine subscripts. Eqs. (1) to (8), (11) and (13) to (16) are legible in the extracted text. I checked by hand that Eq. (11) follows from Eq. (6) with $\Phi = \Sigma^{-1}$, including the expanded $\mu\eta$ component, and that the variances in Eq. (13) and the reported sample correlations are consistent with the Table 1 parameters. Eqs. (9), (10), (12) and Table 3 are partly garbled in the text and are described in words. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, 003, 004, 005, 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016, 017, 018). Confirmed against those pages: (1); (2) Fokker-Planck form; (3) first two lines (the note omits the third line, div div(Q p_inf) = 0, which is acceptable); (4); (5) with Pi_eta mu = 0; Table 1 (theta = 0; Q = [[0,-theta,0],[theta,0,-theta],[0,theta,0]]; Pi = (1/kappa)[[2,kappa^{1/2},0],[kappa^{1/2},2kappa,kappa^{1/2}],[0,kappa^{1/2},2]], which confirms the drafter's reconstruction; Gamma = (1/4)diag(gamma,1,gamma)); (6); (7) as a vectorized linear system; (9) conditional MI via the Schur complement Upsilon; (10) information length via sqrt(2 D_KL); (11) Phi-dot = Pi(Gamma-Q)^T Phi + Phi(Gamma-Q)Pi - 2 Phi Gamma Phi and the expanded mu-eta component; (12) three labeled groups; (13) Sigma_mu = Sigma_eta = 3kappa/4, Sigma_b|mu = Sigma_b|eta = 2/3 (also checked by inverting Pi: det = 4, (M^{-1})_mu mu = 3/4); (14), (15), (16). Masthead confirmed on p. 1 (Entropy 2021, 23, 1105; received 10 July, accepted 22 August, published 25 August 2021; CC BY). Correlations -0.53, -0.55, 0.37, 512 runs, x = (1,1,1), tau = 16 (pp. 5-6); e^4 blanket precision (p. 10); sweep ranges 1/4 to 2 (Figs. 3-5); categorical tau = 2 (Fig. 6); 'changing theta does little' (p. 17); limitations in Section 7.3 confirmed.

## TL;DR

The paper argues that a Markov blanket defined on a steady-state density constrains only that density: once a past blanket state is conditioned upon, the evolving density is away from steady state, and internal and external states can be conditionally dependent given the current blanket state until the initial condition is forgotten. It demonstrates this in a three-variable Ornstein-Uhlenbeck example and in a categorical master-equation example, and it proposes conditional mutual information, an information-length difference, and Jacobian time constants as measures of memory, examined by parameter sweeps.

## Problem & setting

The apparent paradox is that if every dependence between internal states $\mu$ and external states $\eta$ is mediated by the blanket $b$, then internal states could hold no information about external states beyond what the current blanket state carries, which would rule out memory (for example delay-period neural activity after a stimulus is removed). The standing assumptions are a random dynamical system $\dot x = f(x) + \omega(x)$ for $x = (\mu, b, \eta)$ with Gaussian white fluctuations of covariance $2\Gamma$; a steady-state density that exists and factorizes as $p(\mu,\eta|b) = p(\mu|b)p(\eta|b)$; solenoidal and diffusion matrices $Q$ and $\Gamma$ that are constant; and a Laplace assumption (quadratic potential), under which flows are linear and the Itô, Stratonovich and A-type conventions coincide. Each of $\mu$, $b$, $\eta$ is one-dimensional in the examples. The paper builds on Parr, Da Costa and Friston 2020, Friston 2019, Da Costa et al. 2021, the Laplace population dynamics of Marreiros et al. 2009, the information length of Kim and of Crooks, and the decomposition of discrete Markov processes by Ao, Chen and Shi 2013. The acknowledgements credit conversations with Biehl, Rosas and Virgo as motivation.

## Method

The density dynamics are the Fokker-Planck equation of Eq. (2), $\partial_\tau p(x,\tau) = \nabla_x\cdot(\nabla_x\cdot(\Gamma(x)p(x,\tau))) - \nabla_x\cdot(f(x)p(x,\tau))$, whose stationary solution gives Eq. (3), $f(x) = (Q(x) - \Gamma(x))\nabla_x\Im(x) + \nabla_x\cdot(\Gamma(x) + Q(x))$ with $p(x,\infty) \propto e^{-\Im(x)}$. The central statement is Eq. (4), $p(\eta,\mu,b) = \lim_{\tau\to\infty}p(\eta,\mu,b,\tau|b_0)$: the blanket factorization holds for the left side and need not hold for the density conditioned on an initial blanket state $b_0$ at finite $\tau$. The example uses the quadratic potential of Eq. (5), $\Im(x) = \tfrac{1}{2}(x-\vartheta)\cdot\Pi(x-\vartheta)$ with $\Pi_{\eta\mu} = 0$, and Table 1 parameters $\vartheta = 0$, $Q$ antisymmetric with entries $\pm\theta$ coupling $\mu$ to $b$ and $b$ to $\eta$, $\Gamma = \tfrac{1}{4}\mathrm{diag}(\gamma, 1, \gamma)$, and a precision $\Pi$ parameterized by $\kappa$. Under these assumptions Eq. (6) gives $p(x,\tau) = N(\xi,\Sigma)$ with $\dot\xi = -(\Gamma - Q)\Pi(\xi - \vartheta)$ and $\dot\Sigma = 2\Gamma - \Sigma\Pi(\Gamma - Q)^T - (\Gamma - Q)\Pi\Sigma$, vectorized as a linear system in Eq. (7). Memory is measured by the conditional mutual information $I[p(\mu,\tau|b);p(\eta,\tau|b)] = D_{KL}[p(\mu,\eta,\tau|b) \| p(\mu,\tau|b)p(\eta,\tau|b)]$, evaluated in closed form from the Schur complement of $\Sigma_{bb}$ (Eq. 9); by the difference in information length, accumulated as the square root of twice the KL divergence between successive densities, between the joint density and the blanket marginal (Eq. 10); and by reciprocals of the real parts of the eigenvalues of the covariance Jacobian. For the precision $\Phi = \Sigma^{-1}$, Eq. (11) gives $\dot\Phi = \Pi(\Gamma - Q)^T\Phi + \Phi(\Gamma - Q)\Pi - 2\Phi\Gamma\Phi$. The categorical analogue (Eqs. 14 to 16) is the master equation $\mathrm{vec}(\dot s(\tau)) = L\mathrm{vec}(s(\tau))$ with $L = \Omega\Lambda$, $\Lambda = \mathrm{diag}(\mathrm{vec}(s(\infty)))^{-1}$, $s_{\mu\eta b}(\infty) = s_{\mu|b}(\infty)s_{\eta|b}(\infty)s_b(\infty)$, $\Omega = Q - \Gamma$, $\Gamma = -\tfrac{1}{2}(\Omega + \Omega^T)$ and $Q = \tfrac{1}{2}(\Omega - \Omega^T)$.

## Key results

The paper states no theorems. Section 2 (pp. 3 to 4) argues from Eq. (4) that densities relaxing toward a steady-state density with a Markov blanket are not themselves subject to the blanket condition, so the blanket does not preclude memory. Section 3 (pp. 5 to 7) shows this numerically: 512 stochastic runs from $x = (1,1,1)$ to $\tau = 16$ give sample correlations of $-0.53$ (internal and blanket), $-0.55$ (external and blanket) and $0.37$ (internal and external) although the last pair is conditionally independent at steady state, and integration of Eq. (7) shows the element $\Phi_{\mu\eta}$ becoming transiently nonzero and decaying to zero (Fig. 2). Section 5 (pp. 9 to 14) expands the $\mu\eta$ component of Eq. (11) into dissipation by internal and external states, dissipation by blanket states, and solenoidal coupling to blanket states (Eq. 12). From it the authors read that a conditional dependence can be induced only through blanket dissipation or solenoidal coupling to the blanket, that internal and external dissipation act only once the dependence exists, and that the solenoidal terms cancel at steady state. Sweeps of $\gamma$, $\theta$ and $\kappa$ from $1/4$ to $2$, starting from the steady-state density with blanket precision raised to $e^4$, show by simulation that larger $\gamma$ gives faster forgetting without changing the period of synchronization and desynchronization (Fig. 3); that larger $\theta$ lengthens the information length with only a small decrease in time constants, while weaker solenoidal coupling gives longer but later and smaller peaks (Fig. 4); and that $\kappa$ scales the marginal variances $\Sigma_\mu = \Sigma_\eta = 3\kappa/4$ while $\Sigma_{b|\mu} = \Sigma_{b|\eta} = 2/3$ stays fixed (Eq. 13), with time constants growing with marginal variance and a tight steady state producing an early, high and short-lived mutual-information peak (Fig. 5). Section 6 (pp. 14 to 18) repeats the analysis for a categorical system simulated to $\tau = 2$: transient conditional dependencies again appear, and changing $\theta$ does little. Section 7 relates the time constants to short-term and long-term memory; that discussion is interpretive.

## Limits

The authors state that the simulations are proofs of principle and not exhaustive, that only linear flows of the sufficient statistics are treated, that each component is one-dimensional (so no intrinsic dynamics within a component, no separation of timescales among internal states, no split of the blanket into active and sensory states), that the quantitative results are specific to the chosen Ornstein-Uhlenbeck process, and that the categorical analogy with the solenoidal and dissipative split is inexact. My observations: the central claim is an argument from the meaning of conditioning and comes with no stated conditions or rates; the initial condition of the parameter sweeps is a Gaussian with sharpened blanket precision, not conditioning on a point value of $b_0$; and the result grants that conditional independence given only the current blanket state fails after an observation, which is the situation the time-unrolled blanket commentary by Virgo, Rosas and Biehl describes.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The paper separates two objects that a multi-agent free energy model also has to keep apart: the stationary joint law, in which a blanket is a zero pattern in the precision matrix, and the transient law after an observation, in which that zero fills in. For Gaussian beliefs the statement is exact. Eq. (11) is a matrix Riccati flow for the precision on the cone of symmetric positive definite matrices, and its $\mu\eta$ component shows that cross-blanket precision is generated only through the blanket's own diffusion and its solenoidal coupling. This bears on how a blanket of an individual or of a collective should be stated, namely as a property of the stationary density that is violated on relaxation timescales, and it supplies candidate measures (conditional mutual information, information length under the Fisher metric) of how far a proposed boundary is from a blanket at a given time, which is relevant to coarse-graining toward meta-agents. Any relation to belief inertia is interpretive: the time constants here come from overdamped linear relaxation with solenoidal rotation, and the model has no mass term or second-order dynamics. The paper contains no transport or gauge structure. The link is moderate overall and exact within the linear-Gaussian case.

## Cross-links

Concepts: [[Markov Blanket]]; [[Bayesian mechanics]]; [[Nonequilibrium steady state]]; [[Mutual information]]; [[Information Geometry]]; [[Laplace approximation]]; [[Markov blanket interpretation debate]]; [[Hamiltonian belief dynamics]].

Related sources: [[parr-2020-markov-blankets-thermodynamics]]; [[dacosta-2021-bayesian-mechanics]]; [[friston-2019-particular-physics]]; [[friston-2021-stochastic-chaos-markov]]; [[friston-2021-parcels-particles-markov]]; [[crooks-2007-thermodynamic-length]]; [[virgo-2022-sensorimotor-history-markov-blankets]]; [[barp-2021-measure-preserving-diffusions]]; [[dacosta-2021-neural-dynamics-active-inference]].

## BibTeX

```bibtex
@article{parr2021memory,
  author = {Parr, Thomas and Da Costa, Lancelot and Heins, Conor and Ramstead, Maxwell James D. and Friston, Karl J.},
  title = {Memory and {M}arkov Blankets},
  journal = {Entropy},
  volume = {23},
  number = {9},
  pages = {1105},
  year = {2021},
  doi = {10.3390/e23091105}
}
```
