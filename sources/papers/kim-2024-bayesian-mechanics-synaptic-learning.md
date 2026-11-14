---
type: paper
title: "Bayesian Mechanics of Synaptic Learning Under the Free-Energy Principle"
aliases: ["Kim 2024 bayesian mechanics synaptic learning"]
authors: ["Chang Sub Kim"]
year: 2024
venue: "Entropy 26(11), 984"
arxiv: "2410.02972"
doi: "10.3390/e26110984"
url: "https://arxiv.org/abs/2410.02972"
version: "arXiv:2410.02972v1 [q-bio.NC], 3 October 2024, as stamped on page 1, with the title printed as 'Bayesian Mechanics of Synaptic Learning under the Free Energy Principle' (no hyphen). The Entropy version of record (26(11), 984) was not the PDF read."
tags: [cluster/vfe, project/multi-agent, field/neuroscience, field/physics]
created: 2026-11-13
updated: 2026-11-13
---

# Bayesian Mechanics of Synaptic Learning Under the Free-Energy Principle

> [!info] Citation
> Chang Sub Kim (2024). *Bayesian Mechanics of Synaptic Learning Under the Free-Energy Principle*. Entropy 26(11), 984. [arXiv:2410.02972](https://arxiv.org/abs/2410.02972) [DOI](https://doi.org/10.3390/e26110984)

[Local PDF](../pdfs/kim-2024-bayesian-mechanics-synaptic-learning.pdf), 20 pages; retrieved November 13, 2026. Version read: arXiv:2410.02972v1 [q-bio.NC], 3 October 2024, as stamped on page 1, with the title printed as 'Bayesian Mechanics of Synaptic Learning under the Free Energy Principle' (no hyphen). The Entropy version of record (26(11), 984) was not the PDF read. Reading basis: The first reader worked from the extracted text and did not see the typeset pages. I read all 20 pages of the text in full, including figure captions, Table 1 and the reference list. No equation was checked against a PDF page. The extraction renders the mathematics with substituted glyphs but legibly. I verified by hand that eqs. (23) to (26) follow from the Hamiltonian of eq. (16) with eqs. (19) and (20), that the matrix of eq. (28) and the fixed point of eq. (31) follow from them, and I computed the eigenvalue structure and fixed-point values for the Table 1 parameters, which is the basis of the discrepancy reported under limits. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, page-005, page-006, page-007, page-008, page-009, page-010, page-011, page-012, page-013, page-014, page-015, page-016). Confirmed against those pages: (2), (3), (4), (5), (6), (7), (8), (9), (10), (11), (12), (13), (14), (15), (16), (17), (18), (19), (20), (21), (22), (23), (24), (25), (26), (27), (28), (29), (30), (31); Table 1 values; fixed points (w_eq, mu_eq) = (-1.0, 0.1) and (-2.0, 0.0) (p. 13); inputs s = 5, 5 cos t + eta, and 5 e^{-t/5} cos t + eta (Figs. 3 to 6). Title page confirmed: arXiv:2410.02972v1 [q-bio.NC], 3 Oct 2024, title 'Bayesian Mechanics of Synaptic Learning under the Free Energy Principle', single author.

## TL;DR

The paper applies the author's least-action formulation to a single synapse. The postsynaptic activity $\mu$ and the synaptic weight $w$ are both treated as dynamical variables with Langevin generative models, their Onsager-Machlup path densities supply the prior and likelihood of the Laplace-encoded free energy, and that free energy is then itself an action whose Hamilton equations couple $\mu$, $w$ and two prediction-error momenta under a time-dependent presynaptic input. A linear Hebbian model is integrated numerically for static, sinusoidal and decaying inputs.

## Problem & setting

The question is how synaptic learning can be written as inference under the free energy principle when inputs are nonstationary. The author holds (Sect. 3.3) that gradient descent on a free energy surface is not legitimate when that surface changes in time with the input, and that generalized coordinates of motion lack a Newtonian basis, so Hamilton's principle should replace both. The setting is a single synaptic assembly (Sect. 2): a prescribed presynaptic signal $s(t)$, a postsynaptic variable and a weight, with hidden stochastic variables $\tilde{\vartheta} = \{M, W\}$ represented by the means $\tilde{\mu} = \{\mu, w\}$ of a Gaussian recognition density (eq. 4). The bound is $-\ln p(s) \leq F(\mu, w, s)$ with Laplace-encoded free energy $F(\mu, w \mid s) = -\ln p(w \mid \mu, s) p(\mu, s)$ (eqs. 6 and 7). The standing assumptions are overdamped Langevin dynamics with additive Gaussian white noise for both variables, local thermal equilibrium at body temperature with noise strength fixed by a fluctuation-dissipation relation $\sigma_\mu^2 = 2\gamma_\mu^{-1} k_B T$ (eq. 10), and the Ito convention. The paper continues Kim (2018), Kim (2021) and Kim (2023, Interface Focus), in which the action was the time integral of the free energy under an ergodic assumption.

## Method

The generative equations are $d\mu/dt = f(\mu, \theta) + \xi$ (eq. 8) and $dw/dt = h(w, \theta) + \chi$ (eq. 12) with delta-correlated noises of strengths $\sigma_\mu^2$ and $\sigma_w^2$. Discretizing in the Ito convention and taking the continuum limit gives the Onsager-Machlup path density $p(\mu, \theta) \sim \exp\{-\frac{1}{2\sigma_\mu^2}\int_0^t dt' (d\mu/dt' - f(\mu, \theta(t')))^2\}$ (eq. 11) and the analogous likelihood for $w$ (eq. 13). Setting $\theta = s$ and inserting both into eq. 7 gives $F = \int_0^t L dt'$ (eq. 14) with $L = \frac{1}{2\sigma_\mu^2}(\dot{\mu} - f(\mu, w; s))^2 + \frac{1}{2\sigma_w^2}(\dot{w} - h(\mu, w, s))^2$ (eq. 15). The free energy is thus identified with an action, $S = F$, and $\delta F = 0$ with Hamilton's principle. The Legendre transform gives $H = \frac{p_\mu^2}{2 m_\mu} + \frac{p_w^2}{2 m_w} + p_\mu f(\mu, w; s) + p_w h(w, \mu; s)$ (eq. 16), with $m_\mu = 1/\sigma_\mu^2$ and $m_w = 1/\sigma_w^2$ (eq. 18) and momenta $p_\mu = m_\mu(\dot{\mu} - f)$ and $p_w = m_w(\dot{w} - h)$ (eqs. 21 and 22). The model functions are $f = -\gamma_\mu(\mu - \mu_d) + w s$ (eq. 19) and $h = -\gamma_w(w - w_d) + s\mu$ (eq. 20), the last term being Hebb's rule. Hamilton's equations are $\dot{\mu} = p_\mu/m_\mu - \gamma_\mu(\mu - \mu_d) + w s$, $\dot{w} = p_w/m_w - \gamma_w(w - w_d) + s\mu$, $\dot{p}_\mu = \gamma_\mu p_\mu - s p_w$ and $\dot{p}_w = \gamma_w p_w - s p_\mu$ (eqs. 23 to 26), which I checked by differentiating eq. 16. In matrix form $\dot{\Psi} = R\Psi + I$ for $\Psi = (\mu, w, p_\mu, p_w)^T$ (eqs. 27 to 29).

## Key results

Derived: the four coupled equations of the synaptic Bayesian mechanics (eqs. 23 to 26, p. 11); the vanishing trace of $R$ (p. 13), used by the author as a numerical consistency check; the formal solution (eq. 30); and, for constant or saturating input $s_\infty$, the fixed point with $\mu_{eq} = (\mu_d + s_\infty w_d/\gamma_\mu)/(1 - s_\infty^2/\gamma_\mu\gamma_w)$, $w_{eq} = (w_d + s_\infty \mu_d/\gamma_w)/(1 - s_\infty^2/\gamma_\mu\gamma_w)$ and zero momenta (eq. 31). The momenta are interpreted as the prediction errors of predictive coding and the precisions as neural masses, as a metaphor (pp. 10 to 11). Shown numerically (Sect. 6, pp. 13 to 16) with $m_\mu = 5$, $m_w = 0.5$, $\gamma_\mu = 1$, $\gamma_w = 0.1$ and $(\mu_d, w_d) = (5, 5)$ or $(10, 0)$ (Table 1): for static input $s = 5$ the weight and activity are reported to approach $(w_{eq}, \mu_{eq}) = (-1.0, 0.1)$ and $(-2.0, 0.0)$ with transient oscillation, attributed to imaginary eigenvalues of $R$ (Fig. 3), and to spiral into the origin when $\mu_d = w_d = 0$ (Fig. 4); for $s(t) = 5\cos t + \eta$ the outputs keep oscillating (Fig. 5); for $s(t) = 5 e^{-t/5}\cos t + \eta$ the trajectory approaches the origin (Fig. 6). The momenta are not plotted because they stay near zero. Asserted in the discussion (Sect. 7): that removing the ergodic assumption and generalized coordinates makes the scheme more physically grounded than earlier ones, that the Laplace-encoded free energy underlies the $L_2$ losses of machine learning, and that the trajectories are learned without supervision. No comparison with data or with a gradient-descent baseline is made.

## Limits

Stated limits: white noise only, although brain signals are colored (p. 9); a single synapse with a prescribed presynaptic input; linear model functions; path densities obtained under a local-equilibrium assumption. My observations: with the Hebbian sign of eq. 20 the state block of $R$ in eq. 28 is the symmetric matrix with rows $(-\gamma_\mu, s)$ and $(s, -\gamma_w)$, whose eigenvalues are real, and for $s = 5$ its determinant $\gamma_\mu\gamma_w - s^2$ is negative, so the printed equations give a saddle and cannot produce the reported spirals; the reported values, including the positive $\mu_{eq} = 0.1$, match the anti-Hebbian sign $h = -\gamma_w(w - w_d) - s\mu$ by my hand calculation. The momentum block is the negative of the state block, so every decaying state mode is paired with a growing momentum mode, and the plotted trajectories with zero momentum are the noise-free drift $\dot{\mu} = f$, $\dot{w} = h$ of the generative model.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The paper informs the Hamiltonian belief dynamics and belief inertia objects, and to a lesser degree the treatment of learning alongside inference. It puts fast states and slow parameters under one action, with the mass of each coordinate equal to the precision of its generative noise, $m = 1/\sigma^2$, and through eq. 10 ties that precision to temperature and friction, $m_\mu = \gamma_\mu/(2 k_B T)$. As in the 2021 paper, the precision equals the Fisher information of a Gaussian location parameter, so a reading of mass as Fisher information agrees in value; this is an editorial comparison, and the paper calls the mass a metaphor. The identification of the free energy with a path action built from Onsager-Machlup densities is a path-space formulation that sits closer to a variational principle over trajectories than to a steady-state blanket argument. The link to the multi-agent and gauge structure is weak: one synapse, flat coordinates, no covariance dynamics, no transport. What it would challenge is the sufficiency of conservative dynamics. The extremals with zero momentum reduce to the prior drift and nonzero momentum is unstable, so the Hamiltonian sector by itself adds no inferential content in the worked example.

## Cross-links

Concepts: [[Hamiltonian belief dynamics]]; [[Belief inertia]]; [[Mass as Fisher information]]; [[Bayesian mechanics]]; [[Laplace approximation]]; [[Predictive Coding]]; [[Prediction error]]; [[Process-space variational inference]].

Related sources: [[buckley-2017-fep-mathematical-review]]; [[friston-2023-fep-simpler]]; [[aguilera-2022-particular-physics]]; [[friston-2008-dem]]; [[rao-1999-predictive-coding]]; [[dacosta-2020-discrete-state-synthesis]]; [[kim-2021-bayesian-mechanics-perceptual-inference]]; [[isomura-2023-bayesian-mechanics-self-organising]].

## BibTeX

```bibtex
@article{kim2024bayesian,
  title = {Bayesian Mechanics of Synaptic Learning Under the Free-Energy Principle},
  author = {Kim, Chang Sub},
  journal = {Entropy},
  volume = {26},
  number = {11},
  pages = {984},
  year = {2024},
  doi = {10.3390/e26110984},
  eprint = {2410.02972},
  archivePrefix = {arXiv},
  primaryClass = {q-bio.NC}
}
```
