---
type: paper
title: "Bayesian mechanics of perceptual inference and motor control in the brain"
aliases: ["Kim 2021 bayesian mechanics perceptual inference"]
authors: ["Chang Sub Kim"]
year: 2021
venue: "Biological Cybernetics 115(1), 87-102"
arxiv: "2008.09927"
doi: "10.1007/s00422-021-00859-9"
url: "https://arxiv.org/abs/2008.09927"
version: "arXiv:2008.09927v3 [q-bio.NC], 21 January 2021, as stamped on page 1; the acknowledgments state that it is the post-peer-review, pre-copyedit version of the article published in Biological Cybernetics (doi 10.1007/s00422-021-00859-9). The journal version of record was not the PDF read."
tags: [cluster/vfe, project/multi-agent, field/neuroscience, field/physics]
created: 2026-11-13
updated: 2026-11-13
---

# Bayesian mechanics of perceptual inference and motor control in the brain

> [!info] Citation
> Chang Sub Kim (2021). *Bayesian mechanics of perceptual inference and motor control in the brain*. Biological Cybernetics 115(1), 87-102. [arXiv:2008.09927](https://arxiv.org/abs/2008.09927) [DOI](https://doi.org/10.1007/s00422-021-00859-9)

[Local PDF](../pdfs/kim-2021-bayesian-mechanics-perceptual-inference.pdf), 28 pages; retrieved November 13, 2026. Version read: arXiv:2008.09927v3 [q-bio.NC], 21 January 2021, as stamped on page 1; the acknowledgments state that it is the post-peer-review, pre-copyedit version of the article published in Biological Cybernetics (doi 10.1007/s00422-021-00859-9). The journal version of record was not the PDF read. Reading basis: The first reader worked from the extracted text and did not see the typeset pages. I read pages 1 to 25 (all sections, figure captions and the acknowledgment) in full; of the reference list on pages 25 to 28 I saw only the first page and a few entries found by search. No equation was checked against a PDF page. The extraction renders the mathematics with substituted glyphs but legibly; I re-derived by hand the Legendre transform from eq. (11) to eqs. (13) to (16), the Hamilton equations (17) and (18), the linear system (28) to (32), the determinant of the relaxation matrix and the reported fixed point, and report where the printed text and my derivation differ. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, page-003, page-008, page-010, page-011, page-012, page-013, page-014, page-016, page-017, page-018, page-019, page-020, page-021, page-022, page-023, page-024, page-025). Confirmed against those pages: (1), (3), (5), (6), (7), (9), (10), (11), (12), (13), (14), (15), (16), (17), (18), (19), (20), (21), (22), (23), (26), (27), (28), (29), (30), (31), (32), (33); Det(R) = -(1+beta)^2 + (gamma^2 - 1) m_z/m_w (p. 18); parameter values sigma_w = 1.0, sigma_z = 10, phi = -2.8, m_w = 4.6, m_z = 0.1 m_w, alpha = -0.60, beta = -0.28, gamma = -2.8 (kappa = 10) (p. 19); fixed points (-65.6, -306) and (20, 0) (p. 19); p_eq ≈ 8.0 (p. 21). Title page confirmed: arXiv:2008.09927v3 [q-bio.NC], 21 Jan 2021, single author Chang Sub Kim. The post-peer-review statement is on p. 25.

## TL;DR

The paper recasts continuous-state free energy minimization as a least-action problem: the Laplace-encoded free energy of a one-variable generative model with white noise is taken as a Lagrangian in $(\mu, \dot{\mu})$, its time integral as the action, and a Legendre transformation gives Hamilton's equations for the brain state $\mu$ and a conjugate momentum that is a precision-weighted prediction error. Sensory prediction errors enter as time-dependent driving terms, which the author reads as motor signals. For a linear model the flow has a traceless relaxation matrix, so the solutions are saddles or centers; oscillatory solutions are found numerically only in a narrow parameter window that requires a negative covariance between the two generative noises and an added tuning parameter.

## Problem & setting

Conventional continuous-state implementations of the free energy principle minimize the instantaneous free energy by gradient descent in generalized coordinates of motion, with a separate gradient rule $\dot{a} = -\nabla_a F$ for action (eq. 3). The author argues (Sect. 2, pp. 5 to 9) that higher-order generalized states have no dynamical status in Newtonian mechanics, that the motor variable has no equation of motion in that scheme, and that a physically principled process theory should minimize the time-integrated bound $\int dt \{-\ln p(\varphi)\} \leq \int dt F[q(\vartheta), p(\varphi, \vartheta)]$ (eq. 1). The paper extends Kim (2018, Neural Computation), which treated passive perception of static inputs, to nonstationary inputs produced by the agent's own movement. The standing assumptions are a fixed-form Gaussian recognition density (Laplace approximation) so that only the mean $\mu$ matters, a single brain variable, Gaussian white noise in both generative equations with stationary variances, and a statistical coupling between the two noises. Motor inference is not modeled: the motor variable is latent and acts only through the time dependence of the sensory input, which the author calls semi-active inference. The mathematical review by Buckley, Kim, McGregor and Seth (2017) supplies the baseline formulation and the agent model.

## Method

I write the sensory input as $\varphi$ and the noise covariance as $\phi$. The generative model is $\dot{\mu} = f(\mu) + w$ (eq. 5) and $\varphi(a) = g(\mu) + z$ (eq. 6), with $(w, z)$ jointly Gaussian with variances $\sigma_w$, $\sigma_z$ and covariance $\phi(t) = \langle w(0) z(t) \rangle$ (defined below eq. 7). With $\rho = \phi / \sqrt{\sigma_w \sigma_z}$ (eq. 9) and $m_i = 1/(\sigma_i (1 - \rho^2))$ (eq. 10), the Laplace-encoded free energy $F = -\ln p(\varphi, \mu)$ gives the informational Lagrangian $L = \frac{1}{2} m_w (\dot{\mu} - f)^2 + \frac{1}{2} m_z (\varphi - g)^2 - \sqrt{m_w m_z} \rho (\dot{\mu} - f)(\varphi - g)$ (eq. 11) and the action $S[\mu(t)] = \int F dt$ (eq. 12). The conjugate momentum is $p = \partial L / \partial \dot{\mu} = m_w (\dot{\mu} - f) - \sqrt{m_w m_z} \rho (\varphi - g)$ (eq. 13), and the Hamiltonian is $H = T + V$ with $T = \frac{p^2}{2 m_w} + (\rho \sqrt{m_z / m_w} (\varphi - g) + f) p$ and $V = \frac{1}{2} m_z (\rho^2 - 1)(\varphi - g)^2$ (eqs. 14 to 16); my hand derivation from eq. 11 agrees. Hamilton's equations are stated as $\dot{\mu} = \frac{1}{m_w} p + f(\mu) + \alpha \Delta_\varphi$ (eq. 17) and $\dot{p} = -(\partial_\mu f - \beta \partial_\mu g) p - (1 - \gamma^2) \partial_\mu g \Delta_\varphi$ (eq. 18), with $\alpha = \rho / \sqrt{m_z m_w}$, $\beta = m_z \alpha$, $\gamma = \rho \sqrt{\kappa}$ (eq. 19) and $\Delta_\varphi = m_z (\varphi(a) - g(\mu))$ (eq. 20). The precisions $m_w$ and $m_z$ are called neural inertial masses, explicitly as a metaphor. A multivariate Lagrangian under an independent-particle approximation is given in eq. 23. The worked model takes $g(\mu) = \mu$ and $f(\mu) = -(\mu - \vartheta_d)$ (eqs. 26 and 27), where $\vartheta_d$ is a prior belief, which makes the system linear, $\dot{\Psi} + R \Psi = S$ for $\Psi = (\mu, p)^T$ (eqs. 30 to 32).

## Key results

Derived results are the Hamiltonian form of recognition dynamics (eqs. 17 and 18, p. 12), in which the momentum is a combined prediction error on the state rate and the sensory input, and the driving terms $C_\mu = \alpha \Delta_\varphi$ and $C_p = -(1 - \gamma^2) \partial_\mu g \Delta_\varphi$ (eqs. 21 and 22) that the author identifies with motor signals, noting a resemblance to Hamilton-Jacobi-Bellman motor-control dynamics, with $p$ read as a costate, without carrying out the minimization over controls. For the linear model the relaxation matrix (eq. 31) has zero trace and $\det R = -(1 + \beta)^2 + (\gamma^2 - 1) m_z / m_w$, so its eigenvalues are $\pm \lambda$ (p. 18). Argued analytically: with zero noise covariance the eigenvalues are real and the solution unstable; with covariance retained and suitable parameters they are purely imaginary, $\pm i\omega$, and the fixed point $\Psi_{eq} = R^{-1} S$ (eq. 33) is a center. Shown numerically (pp. 19 to 24, Figs. 2 to 7) with $\sigma_w = 1$, $\sigma_z = 10$, $\phi = -2.8$, giving $m_w = 4.6$, $m_z = 0.1 m_w$, $\alpha = -0.60$, $\beta = -0.28$ and $\gamma = -2.8$ at $\kappa = 10$: for static input $\varphi = 4$ and prior $\vartheta_d = 20$ the orbits circle the fixed point $(\mu_{eq}, p_{eq}) = (-65.6, -306)$, which the author notes does not match the sensory cause; for input equal to the prior the fixed point is $(20, 0)$; with movement-generated nonstationary input the state settles into a stationary oscillation about a value close to but not equal to the prior, with $p_{eq}$ about 8.0. The author reports that stable trajectories exist only in a narrow window of $\sigma_w$, $\sigma_z$ and $\phi$ and that only negative covariance gave stable solutions (pp. 19 and 22), both as numerical observations. The summary on pp. 22 to 23 calls the oscillations limit cycles that constitute the brain's nonequilibrium resting states.

## Limits

Stated limits: white noise only, with no treatment of temporal correlations; one brain variable; motor inference and expected free energy not included; the noise covariance has no empirical support and was introduced to obtain stable solutions (p. 25); the parameter window for stability is narrow. My observations: differentiating eqs. 14 to 16 gives the coefficient $(1 - \rho^2)$ in the momentum equation, so $\gamma = \rho\sqrt{\kappa}$ with $\kappa \neq 1$ (introduced as a tuning parameter for stability) alters Hamilton's equations by hand, and at $\kappa = 1$ the determinant is nonpositive for every admissible $\rho$, so the unmodified linear flow is a saddle. The closed orbits around a center form a family indexed by the initial condition (Fig. 2 shows three) and are not isolated attracting limit cycles. The equations are integrated as an initial-value problem with a freely chosen initial momentum, and no endpoint or transversality condition is discussed, so which extremal counts as the inference is left open.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> Among this batch the paper is the closest precedent for Hamiltonian belief dynamics and belief inertia. The precision of the generative noise acts as an inertial mass, $m_w = 1/(\sigma_w(1 - \rho^2))$, and the conjugate momentum is a precision-weighted prediction error. For a Gaussian location family the Fisher information matrix is the inverse covariance $\Sigma^{-1}$, so the paper's mass coincides in value with a mass defined as Fisher information; the paper does not make that identification, calls the mass a metaphor, and the agreement holds for this Gaussian case, where $m_w$ is the $ww$ entry of $\Sigma^{-1}$ for any $\rho$. The construction differs from a kinetic term placed on a statistical manifold: the velocity enters because the prior is a dynamical model, the Laplace step discards covariance dynamics, and there is one agent with a flat one-dimensional belief coordinate, so nothing here touches fibers, transport or the Fisher metric as a geometry. Its value to the program is as much cautionary as supportive. A purely conservative flow obtained from a free energy action has eigenvalues in opposite-sign pairs, cannot relax to a posterior, and in this paper needed correlated noise and a hand-tuned parameter to give bounded motion, which bears on how dissipation would have to be supplied alongside any Hamiltonian sector.

## Cross-links

Concepts: [[Hamiltonian belief dynamics]]; [[Belief inertia]]; [[Mass as Fisher information]]; [[Bayesian mechanics]]; [[Laplace approximation]]; [[Generalised coordinates of motion]]; [[Prediction error]]; [[Active Inference]].

Related sources: [[buckley-2017-fep-mathematical-review]]; [[friston-2008-dem]]; [[sengupta-2016-neuronal-gauge]]; [[sengupta2017gauge]]; [[friston-2019-particular-physics]]; [[parr-2020-markov-blankets-thermodynamics]]; [[amari-1998-natural-gradient]]; [[bogacz-2017-free-energy-tutorial]]; [[kim-2024-bayesian-mechanics-synaptic-learning]]; [[friston-2012-free-energy-value-attractors]]; [[dacosta-2025-generalized-coordinates-sde]].

## BibTeX

```bibtex
@article{kim2021bayesian,
  title = {Bayesian mechanics of perceptual inference and motor control in the brain},
  author = {Kim, Chang Sub},
  journal = {Biological Cybernetics},
  volume = {115},
  number = {1},
  pages = {87--102},
  year = {2021},
  doi = {10.1007/s00422-021-00859-9},
  eprint = {2008.09927},
  archivePrefix = {arXiv},
  primaryClass = {q-bio.NC}
}
```
