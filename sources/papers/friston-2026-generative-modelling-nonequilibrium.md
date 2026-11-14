---
type: paper
title: "A framework for the use of generative modelling in non-equilibrium statistical mechanics"
aliases: ["Friston et al. 2026 generative modelling nonequilibrium"]
authors: ["Karl J. Friston", "Maxwell J. D. Ramstead", "Dalton A. R. Sakthivadivel"]
year: 2026
venue: "Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences 482(2330), article 20250538"
arxiv: "2406.11630"
doi: "10.1098/rspa.2025.0538"
url: "https://arxiv.org/abs/2406.11630"
version: "arXiv:2406.11630v5 [cond-mat.stat-mech], stamped 22 Dec 2025, title page dated 23rd December 2025, 31 pages. This is the preprint, not the Proceedings of the Royal Society A version of record."
tags: [cluster/vfe, cluster/participatory, cluster/participatory/philosophy-of-mind, project/multi-agent, field/physics, field/philosophy, field/statistics, field/biology]
created: 2026-11-13
updated: 2026-11-13
---

# A framework for the use of generative modelling in non-equilibrium statistical mechanics

> [!info] Citation
> Karl J. Friston, Maxwell J. D. Ramstead, Dalton A. R. Sakthivadivel (2026). *A framework for the use of generative modelling in non-equilibrium statistical mechanics*. Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences 482(2330), article 20250538. [arXiv:2406.11630](https://arxiv.org/abs/2406.11630) [DOI](https://doi.org/10.1098/rspa.2025.0538)

[Local PDF](../pdfs/friston-2026-generative-modelling-nonequilibrium.pdf), 31 pages; retrieved November 13, 2026. Version read: arXiv:2406.11630v5 [cond-mat.stat-mech], stamped 22 Dec 2025, title page dated 23rd December 2025, 31 pages. This is the preprint, not the Proceedings of the Royal Society A version of record. Reading basis: I read the extracted text of all 31 pages in full (pages 1 to 28 of main text; the reference list on pages 28 to 31 was skimmed). The first reader worked from the extracted text and did not see the typeset pages. I additionally viewed pages 6 to 9 of the PDF in the browser pane at low resolution (about 320 pixels page width), which was enough to confirm the layout and the leading signs of Eqs. (2.1.1), (2.1.2) and (2.1.3) but not fine subscripts. Equations in Sections 3.1 and 3.2 are reported from the text only. Figures were not inspected beyond their captions and extracted axis labels. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, 006, 007, 008, 009, 011, 012, 013, 014, 015, 016, 017, 018, 019, 020, 021, 022, 023, 027). Confirmed against those pages: (2.1.1) including the existence condition with [Q+Gamma]^{-1} and 2Gamma = DD^T; (2.1.2); (2.1.3) as printed (leading minus, no dt), and the unnumbered display after it on p. 8; (3.1.1); (3.1.2) first line f_mu = D mu - grad eps . Pi^(1) eps - Pi^(2) mu; signaling kernel with positive exponent e^{|psi_xi - psi_xj|} (p. 11); generative chain s|eta, eta|a, a|mu (p. 16); Q and Gamma parametrization (p. 17, no mu-eta entry); (3.2.1); steady-state marginal p*(s,a,mu) = (1/2pi) N(a; A cos mu, sigma_a^2) N(s; a, sigma_s^2+sigma_eta^2) and the ribbon in S^1 x R^2 (pp. 17-18); v_post, m_post, q(eta; mu, tau^2) = N(eta; A cos mu, tau^2) and the collected free energy (p. 18); (3.2.2). Title, authors, arXiv v5 stamp 22 Dec 2025 and 'Dated: 23rd December 2025' confirmed on p. 1. N = 200 confirmed in Figs. 6 and 7. The note's sign observation on (2.1.3) is correct: (2.1.1) gives -(Q-Gamma) grad log p = +(Q-Gamma) grad(-log p), so with F bounding -log p the consistent form is +(Q-Gamma) grad F, as (3.1.2) has. Prefactors e^{-16} and e^{-2} for Pi^(1) and Pi^(2) confirmed (p. 12).

## TL;DR

The paper restates the free energy principle as a modeling method for coupled subsystems: given a steady-state density with a Markov blanket and a Helmholtz-type decomposition of the drift, the flow of a particle's states can be rewritten as a flow on variational free energy by adding a KL term that is stipulated to vanish. Two constructed simulations (eight-cell morphogenesis and a phase-coding periodically firing cell) illustrate the recipe, and the authors state that these are constructions and not independent empirical tests. The philosophical sections argue that the inferential reading is an as-if description supplied by the modeler, so the map-territory objection does not apply to the formalism as such.

## Problem & setting

The paper asks how open, coupled, nonequilibrium systems can be modeled tractably, and whether describing a physical object as inferring its environment reifies the scientist's model, the objection raised against the free energy principle by Bruineberg and colleagues and by van Es, following Cartwright. The standing assumptions are a joint system with external, blanket and internal states $(\eta, b, \mu)$ whose steady-state density $p(\eta, b, \mu)$ makes $\mu$ conditionally independent of $\eta$ given $b$; an Itô diffusion with a nonequilibrium steady-state density that admits the decomposition of Ao and of Ma, Chen and Fox; a Laplace assumption under which the mode equals the expectation and the posterior is locally Gaussian (or, more generally, a maximum-entropy Gibbs form); and the existence of a synchronization map $\sigma$ with $\sigma(\hat\mu_b) = \hat\eta_b$, taken from Lemma 4.3 of Sakthivadivel's geometry paper. It builds on Friston 2019, Da Costa et al. 2021, Ramstead et al. 2023, Parr et al. 2020, generalized filtering (Friston et al. 2010), and the authors' earlier preprint on the map-territory fallacy (arXiv:2208.06924), which the acknowledgements say this paper develops more fully. Path-space formulations are mentioned and set aside.

## Method

Section 2.1 starts from an Itô diffusion $dX_t = f(X_t)dt + D(X_t)dW_t$ with nonequilibrium steady-state density $p^*$ and rewrites it as Eq. (2.1.1), $dX_t = -(Q(X_t) - \Gamma(X_t))\nabla_x \log p^*(X_t)dt + D(X_t)dW_t$, with $Q$ skew-symmetric, $\Gamma$ positive semidefinite and $2\Gamma = DD^\top$. The decomposition is said to hold whenever some $Q$ satisfies $\nabla \times [Q(x) + \Gamma(x)]^{-1} f(x) = 0$ and $\Gamma$ is divergence free. Under the Laplace assumption the internal mode $\hat\mu_b = \arg\max \log p(\mu, b)$ is mapped by $\sigma$ to the parameter $\hat\eta_b$ of a variational density $q(\eta; \hat\eta_b)$. The free energy is Eq. (2.1.2), $F(\mu,b) = D_{KL}(q(\eta;\sigma(\mu)) \| p(\eta|b)) - \log p(\mu,b) \geq -\log p(\mu,b)$, and the internal flow is rewritten as Eq. (2.1.3), printed as $d\mu_t = -(Q-\Gamma)\nabla_\mu F(\mu,b) + dW_t$. Section 3.1 applies this in generalized coordinates $\tilde\psi = [\psi, \psi', \psi'', \ldots]$ to eight cells, each with a softmax generative mapping from beliefs about its identity to expected position, signal expression and sensed concentration, prediction errors $\varepsilon_i = s_i - g(\psi)_i$, and drifts given by Eq. (3.1.2), for example $f_{\tilde\mu} = D\tilde\mu - \nabla_{\tilde\mu}\tilde\varepsilon_i \cdot \Pi^{(1)}\tilde\varepsilon_i - \Pi^{(2)}\tilde\mu$. Section 3.2 builds a four-variable system $(\mu, s, a, \eta)$ from the chain $s|\eta \sim N(\eta,\sigma_s^2)$, $\eta|a \sim N(a,\sigma_\eta^2)$, $a|\mu \sim N(A\cos\mu,\sigma_a^2)$ with a uniform prior on the phase $\mu$, constant $\Gamma = \mathrm{diag}(\gamma_\mu,\gamma_s,\gamma_a,\gamma_\eta)$ and a constant $Q$ with entries $q_{\mu s}$, $q_{\mu a}$, $q_{a\eta}$ and no $\mu$-$\eta$ entry. The exact posterior is $p(\eta|s,a) = N(m_{post}, v_{post})$ with $v_{post} = (1/\sigma_s^2 + 1/\sigma_\eta^2)^{-1}$ and $m_{post} = v_{post}(s/\sigma_s^2 + a/\sigma_\eta^2)$, the variational density is $q(\eta;\mu,\tau^2) = N(\eta; A\cos\mu, \tau^2)$, and $F(s,a,\mu) = \tfrac{1}{2}[\log(v_{post}/\tau^2) + (\tau^2 + (A\cos\mu - m_{post})^2)/v_{post} - 1] - \log p(s,a,\mu)$. Flows on $L = -\log p$ (Eq. 3.2.1) and on $F$ (Eq. 3.2.2) are simulated and compared. Sections 4 and 5 are philosophical argument.

## Key results

The paper contains no theorem or proposition environments. Section 2.1 (pp. 5 to 8) argues informally that, given a Markov blanket and the decomposition (2.1.1), the dynamics of a particle can be written as a gradient flow on variational free energy, with exact agreement where the KL term vanishes; the vanishing is stipulated, on the ground that the system is at its average state on average, and the authors call the result an approximate description of all Markov-blanketed systems. Section 2.2 (pp. 8 to 10) asserts that $F$ is a Lyapunov function for the (deterministic) flow, citing Freidlin and Wentzell and the bound (2.1.2), without proof. Section 3.1 (pp. 11 to 16) reports a simulation in the DEM toolbox of SPM12, following Friston, Levin, Sengupta and Pezzulo (2015): eight cells with two-dimensional positions and four-dimensional signaling profiles migrate and differentiate toward a prescribed head, body and tail morphology while free energy, after a brief initial rise to about $-240$, decreases to below $-340$ over the roughly 30 time units shown (Fig. 2b). Section 3.2 (pp. 14 to 22) derives the steady-state marginal $p^*(s,a,\mu) \propto \frac{1}{2\pi}N(a; A\cos\mu,\sigma_a^2)N(s; a,\sigma_s^2+\sigma_\eta^2)$, a ribbon in $S^1 \times \mathbb{R}^2$ along which the solenoidal flow circulates, and shows by simulation that trajectories of $\mu$ and $a$ under (3.2.1) and (3.2.2) agree closely (Figs. 4 and 5, described qualitatively, no error metric), that the sample mean of the KL term over $N = 200$ trajectories falls from about 13 to a plateau near 1 (Fig. 6; the text calls this a tendency toward zero), and that free energy falls faster and lower under the flow on $F$ (Fig. 7). Section 3.3 (pp. 19 to 23) states the central contribution as constructive: whenever the decomposition and a blanket exist, generative models and variational densities can be built so that the dynamics descend a free energy; the examples are said not to be independent empirical tests, and a bottom-up test from an independently specified Langevin model is left as future work. Sections 4 to 6 (pp. 23 to 28) argue that the generative model is the modeler's map of the joint system while the variational density is the map attributed to the particle, so the two are not conflated; the authors add that models built with the principle can still be reified. The claim on p. 27 that any modeling process consistent with physics must conform to the principle is asserted.

## Limits

The authors state that both examples were engineered top-down with a prescribed steady state and constant $Q$ and $\Gamma$, that the adiabatic approximation of Section 3.1 excludes modeling migration as a function of action, that Section 3.2 has no hierarchical states or generalized coordinates, and that path-space versions are not treated. My observations: Eq. (2.1.3) and the display after it carry a leading minus sign and omit $dt$, which is inconsistent with (2.1.1) and with (3.1.2) if $F$ bounds $-\log p$ from above; agreement of the two flows needs the gradient of the KL term to vanish along the flow, which is stronger than the KL term being small at the mode and is stipulated; the existence condition is printed with $[Q+\Gamma]^{-1}$ while the flow uses $Q-\Gamma$; the signaling kernel in Section 3.1 is described as exponential decay but printed with a positive exponent.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The paper bears mainly on how claims about agents should be phrased. The lineage's most recent statement treats inference by a physical system as a modeler's description that is conditional on a blanket and on a drift decomposition, and it calls its own demonstrations constructions. For a gauge-theoretic multi-agent free energy model this supports presenting agents with Gaussian beliefs on statistical fibers as a modeling ansatz whose blanket and steady-state premises are assumed, in line with the boundary already drawn on the Bayesian mechanics page. The morphogenesis example is the nearest contact with the multi-agent side: every cell carries the same generative model of a target configuration and infers its own place through a shared signaling field. That is a common-prior picture with no transport between agents' belief frames and no demonstrated group-level blanket, so any correspondence with coarse-graining to meta-agents is interpretive. Section 3.2 uses a Gaussian variational density with a Kalman-form posterior, which matches the Gaussian-belief setting exactly but only for a scalar state. The paper says nothing about connections, holonomy, or the Fisher metric beyond passing mentions of a manifold of probability distributions and of a neural manifold. The link is strong for interpretation and scope and weak for geometry.

## Cross-links

Concepts: [[Bayesian mechanics]]; [[Markov blanket interpretation debate]]; [[Markov Blanket]]; [[Nonequilibrium steady state]]; [[Variational free energy]]; [[Generative model]]; [[Laplace approximation]]; [[Collective active inference]].

Related sources: [[ramstead-2023-bayesian-mechanics]]; [[dacosta-2021-bayesian-mechanics]]; [[sakthivadivel2022-bayesian-mechanics-geometry]]; [[friston-2023-path-integrals-particular]]; [[bruineberg-2022-emperors-markov-blankets]]; [[parr-2020-markov-blankets-thermodynamics]]; [[sakthivadivel-2023-worked-example-classical-objects]]; [[dacosta-2023-entropy-production-stationary-diffusions]].

## BibTeX

```bibtex
@article{friston2026generative,
  author = {Friston, Karl J. and Ramstead, Maxwell J. D. and Sakthivadivel, Dalton A. R.},
  title = {A framework for the use of generative modelling in non-equilibrium statistical mechanics},
  journal = {Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences},
  volume = {482},
  number = {2330},
  pages = {20250538},
  year = {2026},
  doi = {10.1098/rspa.2025.0538},
  eprint = {2406.11630},
  archivePrefix = {arXiv},
  primaryClass = {cond-mat.stat-mech},
  note = {Read as arXiv v5, 22 December 2025}
}
```
