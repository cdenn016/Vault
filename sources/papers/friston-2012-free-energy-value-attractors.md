---
type: paper
title: "Free Energy, Value, and Attractors"
aliases: ["Friston and Ao 2012 free energy value attractors"]
authors: ["Karl Friston", "Ping Ao"]
year: 2012
venue: "Computational and Mathematical Methods in Medicine 2012:937860"
doi: "10.1155/2012/937860"
url: "https://doi.org/10.1155/2012/937860"
version: "Journal version of record as printed on the title page: Computational and Mathematical Methods in Medicine, Volume 2012, Article ID 937860, 27 pages, doi:10.1155/2012/937860 (Hindawi; received 23 August 2011, accepted 7 September 2011; copyright 2012 K. Friston and P. Ao)."
tags: [cluster/vfe, project/multi-agent, field/neuroscience, field/physics, field/cs-ml]
created: 2026-11-13
updated: 2026-11-13
---

# Free Energy, Value, and Attractors

> [!info] Citation
> Karl Friston, Ping Ao (2012). *Free Energy, Value, and Attractors*. Computational and Mathematical Methods in Medicine 2012:937860. [DOI](https://doi.org/10.1155/2012/937860)

[Local PDF](../pdfs/friston-2012-free-energy-value-attractors.pdf), 27 pages; retrieved November 13, 2026. Version read: Journal version of record as printed on the title page: Computational and Mathematical Methods in Medicine, Volume 2012, Article ID 937860, 27 pages, doi:10.1155/2012/937860 (Hindawi; received 23 August 2011, accepted 7 September 2011; copyright 2012 K. Friston and P. Ao). Reading basis: The first reader worked from the extracted text and did not see the typeset pages. I relied on the extracted text file. From that text I read pages 1 to 21 in full (Sections 1 to 8, all figure captions), Appendices A to E in full (pages 21 to 23), and skimmed Appendices F to H (pages 23 to 24). The reference list (pages 24 to 27) was only spot-checked for the Ao, Kwon and Yuan entries. The extracted equations of this paper are mostly legible line by line; the equations I report (1 to 8, 10, 12, 16 to 21, 23, 27, 30 to 32, and Lemmas A.1, B.1, D.1) are those whose text form is unambiguous, with one caveat: the extraction drops the tilde that marks generalized coordinates, so I write states without tildes. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, 005, 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 021, 022). Confirmed against those pages: Eqs. 1, 2, 3 (a = u + omega_u), 4, 5, 6, 7, 8, 10, 12, 16, 17, 18, 19, 20, 21, 23, 25, 27, 30, 31, 32; Lemma A.1 (A.1), Lemma B.1 (B.2), Lemma D.1 (D.1); generalized-filtering parameter equation on page 9 (ddot mu_theta = -d_theta F - kappa mu'_theta); Figure 4 diffusion Gamma = (1/64) I. Title page metadata (vol. 2012, Article ID 937860, 27 pages, received 23 Aug 2011, accepted 7 Sep 2011, copyright 2012) confirmed.

## TL;DR

Friston and Ao describe an agent as an ergodic random dynamical system whose expected flow (the "policy") decomposes as $f=(\Gamma+Q)\nabla V$, where value $V=\ln p$ is the log of the ergodic density and $Q$ is antisymmetric. Because a value function fixes only the curl-free part of the flow, optimal control and reinforcement learning specify fixed-point policies only; the paper proposes instead that policies are prior beliefs about motion, constrained by a cost function through the divergence of the flow and realized by active inference, and illustrates this on the mountain-car problem.

## Problem & setting

The paper asks whether reward or cost functions are necessary to explain adaptive behavior, given that the free energy account has action and internal states minimize sensory surprise without any reward signal. The standing assumptions are as follows. The states split four ways into external (hidden) states, sensory states, action and internal states, with sensory states and action forming a Markov blanket; this partition is stipulated through a graphical model (Section 2.1, Figure 1) and is not derived from dynamics. The macroscopic states obey a Langevin equation written in generalized coordinates of motion, with fluctuations that are Wiener processes on the generalized states (Eqs. 1 to 4). The ensemble density is ergodic in the sense of an invariant measure, which the authors equate with the existence of a pullback random attractor (Section 2.3, citing Crauel and Flandoli). The work builds on Friston's free energy principle and generalized filtering, on Ao's potential construction for stochastic differential equations (Ao 2004; Kwon, Ao and Thouless 2005; Yuan et al.), on Haken's slaving principle for macroscopic order parameters, and on the optimal control and reinforcement-learning literature (Hamilton-Jacobi-Bellman equation, temporal difference and Q-learning).

## Method

The agent is described by coupled equations for hidden states and sensations, $\dot x = f(x,a,\theta)+\omega_a$ and $s = g(x,a,\theta)+\omega_s$ (Eq. 1), with action and internal states following a generalized gradient descent on free energy, $\dot a = -\partial_a F(s,\mu)$ and $\dot\mu = D\mu - \partial_\mu F(s,\mu)$ (Eqs. 2 and 12). Writing action as a state-dependent control plus a fluctuation, $a = u(x)+\omega_u$ (Eq. 3), yields an autonomous controlled flow $f(x,u)$, called the policy, whose ensemble density obeys the Fokker-Planck equation $\dot p = \Lambda p := \nabla\cdot\Gamma\nabla p - \nabla\cdot(fp)$ (Eq. 4), with $\Gamma$ half the covariance of the fluctuations. The ergodic density $p(x\mid m)$ is the zero eigenfunction of $\Lambda$, and its entropy is the long-run time average of surprise $L(x) = -\ln p(x\mid m)$ (Eq. 5). Action is posited to minimize this entropy, $a^* = \arg\min_a H(X\mid m)$ (Eq. 7), which it can do only through sensory entropy (Eq. 8) and therefore through the bound $F = L(s) + D_{KL}(q(\vartheta)\Vert p(\vartheta\mid s,m))$ (Eq. 10). The central object is the decomposition of the policy, $f = \Gamma\cdot\nabla V + \nabla\times W$ (Eq. 16), put in Ao's standard form $f = (\Gamma+Q)\nabla V$ with $Q = -Q^T$ (Eq. 17), for which $p = \exp(V)$ solves $\Lambda p = 0$ (Eq. 18) and $\dot V = \nabla V\cdot\Gamma\cdot\nabla V \ge 0$ along the flow (Eq. 19). Optimal control instead defines value as the negative expected path integral of cost, which gives $c(x) = f\cdot\nabla V + \nabla\cdot\Gamma\cdot\nabla V$ (Eq. 23) and, in the deterministic limit, the Hamilton-Jacobi-Bellman equation $\max_u f(x,u)\cdot\nabla V(x) = c(x)$ (Eq. 27). Section 6 constrains the flow directly: stationarity gives $p = (\nabla\cdot\Gamma\nabla p - f\cdot\nabla p)/\nabla\cdot f$ (Eq. 30), peaks of $p$ require $\nabla\cdot f<0$ (Eq. 31), and the flow $f = (x', c(x)x' - \partial_x\varphi)$ has $\nabla\cdot f = c$ (Eq. 32), so that cost acts as negative friction.

## Key results

Proved, at the level of short lemmas in the appendices: Lemma D.1 (page 22) shows that for $f=(\Gamma+Q)\nabla V$ with constant antisymmetric $Q$ the density $p=\exp(V)$ is stationary, since $Q\nabla V$ is divergence-free and orthogonal to $\nabla V$; the main-text version is Eq. 18 (page 10), and Eq. 19 states that value is a Lyapunov function of the expected flow. Lemma A.1 (page 21) splits entropy production into a flow term and a non-negative dispersion term $\int \nabla p\cdot\Gamma\cdot\nabla p/p\ dx$ (also Eq. 6, page 7). Lemma B.1 (page 21) bounds hidden-state entropy by sensory entropy, $H(S\mid m)\ge H(X\mid m)+\ln|\partial g/\partial x|$, for a diffeomorphic sensory map with uniform sensitivity. Appendix E (pages 22 to 23) derives cost as the expected rate of change of value (Eq. 23), from which maxima of the ergodic density lie only where $c(x)\le 0$ (Eq. 25, page 12).

Worked examples: with $L=\varphi(x)+\frac{1}{2}x'^2$ and the canonical $2\times 2$ antisymmetric $Q$, the conservative flow $f=-Q\nabla L$ is Newtonian motion in a potential (Eq. 20, page 11), and adding $\Gamma=\mathrm{diag}(0,\gamma)$ produces a friction term $-\gamma x'$ (Eq. 21).

Argued informally: that value functions are an incomplete specification of policies because $Q$ (or $W$) is left free, so optimal control reaches only fixed-point attractors (Sections 4.2 and 5.2, pages 11 to 13); that policies are empirical priors, $f(x,u)=f(x,\mu_\theta)$, on the assumption that action cancels on average the difference between actual and predicted flow (Section 3.2, pages 9 to 10); and that cost functions act as priors (Section 7.2, citing the complete class theorem).

Shown by simulation: emergence and loss of macroscopic order in sixteen coupled Lorenz oscillators (Figures 2 and 3, pages 4 to 5); numerically computed value and cost functions of a Lorenz system from a discretized Fokker-Planck operator with $\Gamma=(1/64)I$ (Figure 4, page 14); active-inference solution of the mountain-car problem from a divergence-based cost with no value learning (Figures 5 to 7, pages 16 to 18); and itinerant, heteroclinic behavior when cost depends on a satiety state (Figure 8, page 19).

## Limits

The authors state that the first term of Eq. 16 is curl-free only for isotropic diffusion, that Lemma D.1 ignores state dependence of $Q$ (deferring to Ao 2008), that negative divergence does not guarantee an attracting fixed point, that the divergence-based scheme is less efficient at minimizing the path integral of cost, and that learning of the potential $\varphi$ is assumed already done. My observations: the Markov blanket is posited, not derived. Eq. 8 asserts equality of two minimizers, while Appendix B proves only an entropy inequality. Appendix A assumes "without loss of generality" a diffeomorphism making the diffusion tensor isotropic, which is not justified in the text. Eq. 9 passes from stationarity of the time-integrated surprise to pointwise minimization, which presumes surprise depends on action only instantaneously. The sentence on page 15 that negative divergence implies all Lyapunov exponents are negative is false as stated, since divergence is their sum.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The paper matters for the vault mainly as the place where the Ao decomposition $f=(\Gamma+Q)\nabla V$ is attached to the free energy principle, and so as the origin of the dissipative and solenoidal split that later Bayesian mechanics rests on. Its bearing on Hamiltonian belief dynamics is moderate and interpretive: the conservative sector $Q\nabla V$ with canonical $Q$ reproduces Newtonian motion with surprise in the role of an energy function, and friction appears as the dissipative response to fluctuations in velocity. These are statements about physical states in state space, with unit mass, and say nothing about motion of belief parameters on a statistical manifold or about a Fisher-information mass. One formal analog is closer: generalized filtering treats slowly changing parameters by a damped second-order equation, $\ddot\mu_\theta=-\partial_\theta F-\kappa\mu_\theta'$, which has the form of inertial belief dynamics with damping set by a prior precision. The paper also poses a challenge that any free-energy-first construction inherits: a stationary density (or a scalar potential) does not determine the dynamics, because $Q$ is free. There is no Fisher metric, no transport between agents, and no multi-agent or coarse-graining content beyond the mean-field oscillator illustration; those links are weak.

## Cross-links

Concepts: [[Bayesian mechanics]]; [[Nonequilibrium steady state]]; [[Markov Blanket]]; [[Active Inference]]; [[Variational free energy]]; [[Hamiltonian belief dynamics]]; [[Belief inertia]]; [[Generalised coordinates of motion]].

Related sources: [[friston-2009-reinforcement-active-inference]]; [[friston-2010-free-energy-principle]]; [[friston-2008-dem]]; [[friston-2013-life-as-we-know-it]]; [[friston-2019-particular-physics]]; [[haken-1983-synergetics-introduction]]; [[kappen-2012-optimal-control-inference]]; [[friston-2012-fep-biological-systems]]; [[feng-2011-potential-flux-decomposition]]; [[dacosta-2023-entropy-production-stationary-diffusions]].

## BibTeX

```bibtex
@article{friston2012attractors,
  author  = {Friston, Karl and Ao, Ping},
  title   = {Free Energy, Value, and Attractors},
  journal = {Computational and Mathematical Methods in Medicine},
  volume  = {2012},
  pages   = {937860},
  year    = {2012},
  doi     = {10.1155/2012/937860}
}
```
