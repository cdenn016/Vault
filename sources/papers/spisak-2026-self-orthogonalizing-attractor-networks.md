---
type: paper
title: "Self-orthogonalizing attractor neural networks emerging from the free energy principle"
aliases: ["Spisak and Friston 2026 self orthogonalizing attractor networks"]
authors: ["Tamas Spisak", "Karl Friston"]
year: 2026
venue: "Neurocomputing (2026), article 133472"
arxiv: "2505.22749"
doi: "10.1016/j.neucom.2026.133472"
url: "https://arxiv.org/abs/2505.22749"
version: "arXiv:2505.22749v2 [q-bio.NC], stamped 21 May 2026, with the manuscript date line 'Sunday 8th March, 2026' on the title page; 35 pages (main text pp. 1 to 22, references pp. 23 to 27, appendices pp. 28 to 35). The Neurocomputing version of record was not the PDF read."
tags: [cluster/vfe, project/multi-agent, field/cs-ml, field/neuroscience, field/physics]
created: 2026-11-13
updated: 2026-11-13
---

# Self-orthogonalizing attractor neural networks emerging from the free energy principle

> [!info] Citation
> Tamas Spisak, Karl Friston (2026). *Self-orthogonalizing attractor neural networks emerging from the free energy principle*. Neurocomputing (2026), article 133472. [arXiv:2505.22749](https://arxiv.org/abs/2505.22749) [DOI](https://doi.org/10.1016/j.neucom.2026.133472)

[Local PDF](../pdfs/spisak-2026-self-orthogonalizing-attractor-networks.pdf), 35 pages; retrieved November 13, 2026. Version read: arXiv:2505.22749v2 [q-bio.NC], stamped 21 May 2026, with the manuscript date line 'Sunday 8th March, 2026' on the title page; 35 pages (main text pp. 1 to 22, references pp. 23 to 27, appendices pp. 28 to 35). The Neurocomputing version of record was not the PDF read. Reading basis: The first reader worked from the extracted text and did not see the typeset pages. I read pages 1 to 22 (main text and figure captions) in full and Appendices 1 to 9 on pages 28 to 34 in full; of the comparison table on page 35 I saw only the first rows, and of the reference list (pp. 23 to 27) only the first page and a half. No equation was checked against a PDF page. Equations (1) to (25) and the appendix formulas are legible in the extraction after reassembling line-broken fragments; I verified by hand that $d\psi/d\theta = \coth\theta - 1/\theta$, that eq. (18) follows from eq. (17), and that the conditionals of eq. (12) are those of the joint law in eq. (20) for symmetric couplings. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, page-004, page-005, page-006, page-007, page-008, page-009, page-010, page-011, page-012, page-013, page-014, page-016, page-017, page-021, page-022, page-030). Confirmed against those pages: (1), (2), (3), (4), (5), (6), (7), (8), (11), (12), (13), (14), (15), (16), (17), (18), (19), (20), (21), (22), (23), (24), (25); the Appendix 5 stationarity argument (p. 30). Simulation numbers confirmed: 25 nodes, r = 0.77 to -0.19, 380 runs, 1787 test digits, iT 0.1 to 0.5 for retrieval and iT < 0.1 for generalization, iT 0.17 and evidence level 11 for Simulation 4, 0.14N, N = 4096 with 400 faces. Title page confirmed: arXiv:2505.22749v2 [q-bio.NC], 21 May 2026, date line 'Sunday 8th March, 2026', authors Tamas Spisak and Karl Friston.

## TL;DR

The paper builds a recurrent attractor network from a recursive (deep) particular partition: each node is a subparticle whose internal state follows a continuous Bernoulli law, coupled to the others through deterministic blanket states that scale a neighbor's state by a weight. Minimizing a local variational free energy at each node gives a stochastic update with a Langevin-function sigmoid and a local rule for the weights of the form observed correlation minus predicted correlation. The authors argue, and show in simulations, that the learned attractors become approximately orthogonal, that symmetric couplings give a Boltzmann-like stationary law with Gibbs-sampling inference at the network scale, and that sequential input produces asymmetric couplings read as solenoidal flow at a nonequilibrium steady state.

## Problem & setting

The question is which attractor networks follow from the free energy principle without inference and learning rules being imposed by design, and in particular how a network can come to be, and stay, an attractor network through its own dynamics, which the authors call adaptive self-organization. The starting point is the particular partition of a random dynamical system into external, sensory, active and internal states with sparse coupling and independent fluctuations, the conditional independence $\eta \perp \mu \mid s, a$ (eq. 1), and the cited consequence $\dot{\mu} = -\nabla_\mu F(s, a, \mu)$ with $F = E_{q_\mu(\eta)}[\ln q_\mu(\eta) - \ln p(s, a, \eta)]$ (eqs. 2 and 3), taken from Friston et al. (2023) and the path-integral paper and not re-derived. The authors treat this partition as universal for persistent systems and apply it recursively, following Friston (2019) and Palacios et al. (2020). The specific model then rests on a chosen parametrization: continuous Bernoulli internal states, Dirac-delta blanket states (which makes the subparticles conservative particles in the sense of Friston et al. 2023), and additive combination of evidence. Hopfield networks and Boltzmann machines, the projector (pseudo-inverse) networks of Personnaz et al. and of Kanter and Sompolinsky, unlearning rules, Sanger's rule and predictive coding networks supply the comparison class.

## Method

The internal states $\mu$ of a macro-scale particle are covered by overlapping subparticles $\pi_i$ with internal states $\sigma_i$ and pairwise blanket states satisfying $a_{ji} = s_{ij}$, so that $\sigma_i \perp \sigma_j \mid a_{ij}, s_{ij}$ (eq. 4). The parametrization is $p(\sigma_i) \propto e^{b_i \sigma_i}$ on $\sigma_i \in [-1, 1]$ (eq. 5), $p(s_{ij} \mid \sigma_j) = \delta(s_{ij} - J_{ij}\sigma_j)$ and $p(a_{ij} \mid \sigma_i) = \delta(a_{ij} - J_{ji}\sigma_i)$ (eqs. 6 and 7), and $p(\sigma_i \mid s_{ij}) \propto e^{(b_i + s_{ij})\sigma_i}$ (eq. 8). Marginalizing the blanket gives $p(\sigma_i \mid \sigma_j) \propto e^{(b_i + J_{ij}\sigma_j)\sigma_i}$ (eq. 11) and, with all neighbors, the local evidence $\theta_i = b_i + \sum_{j \neq i} J_{ij}\sigma_j$ (eq. 12). The local free energy is $F_i[q_i] = E_{q_i}[-\log p(\sigma_i \mid \theta_i)] - H[q_i] = \psi(\theta_i) - \theta_i E_{q_i}[\sigma_i] - H[q_i]$ with $\psi(\theta) = \log(2\sinh\theta/\theta)$ (eqs. 13 and 14). Its minimizer is $q_i^*(\sigma_i) \propto \exp(\theta_i\sigma_i)$ on $[-1, 1]$ (eq. 15), with mean $E_q[\sigma_i] = L(\theta_i)$, where $L(\theta) = \coth\theta - 1/\theta$ is the Langevin function (eq. 16, Appendix 4). For learning, a point estimate of $\sigma_i$ gives $F_i(\theta_i; \sigma_i) = \psi(\theta_i) - \theta_i\sigma_i$ (eq. 17), $dF_i/dJ_{ij} = (L(\theta_i) - \sigma_i)\sigma_j$ (eq. 18) and the rule $\Delta J_{ij} \propto \sigma_i\sigma_j - L(b_i + \sum_{k \neq i} J_{ik}\sigma_k)\sigma_j$ (eq. 19). At the network scale the weights define a prior $p(\sigma) \propto \exp\{\sum_i b_i^{base}\sigma_i + \frac{1}{2}\sum_{ij} J_{ij}\sigma_i\sigma_j\}$ (eq. 20), bias shifts $\delta b_i$ define a likelihood $p(s \mid \sigma) \propto \exp(\sum_i \delta b_i\sigma_i)$ (eq. 21), and the posterior has the same form with total biases (eq. 22). The coupling matrix is split as $J = J^{\dagger} + J^{-}$ into symmetric and antisymmetric parts (Sect. 2.8). The simulations add an inverse temperature and a learning rate.

## Key results

Derived: the local posterior and Langevin update (eqs. 15 and 16; a longer derivation by accuracy and complexity terms in Appendix 6 ends in $b_q = b + \sum_{j \neq i} J_{ij}\sigma_j$) and the learning rule (eq. 19, p. 8). Obtained for symmetric couplings by a factorization argument: the Boltzmann-like stationary law $p(\sigma) \propto \exp\{\sum_i b_i\sigma_i + \sum_{ij} J^{\dagger}_{ij}\sigma_i\sigma_j\}$ (eq. 25, p. 12), from which the local updates are Gibbs sampling of the posterior of eq. 22 and time averages approximate the posterior mean (eq. 23). Appendix 5 shows by a short calculation that $p_s \propto \exp(-U/D)$ is stationary exactly when $\nabla \cdot (R p_s) = 0$; that this holds for blanketed conservative particles is asserted by citation. Argued informally: approximate orthogonality of attractors (Sect. 2.6, pp. 8 to 9), by analogy with Sanger's rule and with unlearning rules that converge to the projector matrix; and preservation of the Boltzmann form under asymmetric couplings (p. 12), which the authors say they argue and for which they defer a rigorous treatment. Shown by simulation: two patterns with correlation 0.77 yield attractors with correlation -0.19 in a 25-node network (Simulation 1); a grid of 380 runs on ten 8 by 8 digits finds retrieval best at inverse temperature 0.1 to 0.5, one-shot generalization to 1787 unseen digits best below 0.1, and three regimes of high, balanced and low complexity, with orthogonality highest in the balanced one (Simulation 2, Fig. 5); a fixed sequence of three digits gives an asymmetric matrix whose symmetric part holds three fixed points and whose free run replays the order (Simulation 3); free running with learning on and zero bias largely preserves couplings and performance (Simulation 4); runtime scales as $O(N^2)$ and retention exceeds the $0.14N$ Hopfield bound (Simulation 5); attractor formation and denoising carry over to 400 face images with $N = 4096$ (Simulation 6). The proposal that the symmetric and antisymmetric parts correspond to variational and expected free energy is offered as a direction for future work.

## Limits

Stated limits (pp. 21 to 22): quadratic memory in $N$; mixing times under asymmetric coupling not characterized; inputs stationary or slowly varying; a single layer only; node-by-node updates are sequential and the parallel schedule used at scale is an approximation; the link between orthogonality and the divergence-free condition is left for future work (p. 12). My observations: eq. 13 is the divergence from $q_i$ to the local conditional, so eq. 15 holds by definition and the content lies in the parametrization of eqs. 5 to 8; eq. 19 is stochastic ascent on the local conditional log-likelihood, that is a pseudo-likelihood rule, a connection the paper does not name; the pairwise term of eq. 25 as printed lacks the factor $\frac{1}{2}$ of eqs. 20 and 22; with Dirac-delta blanket states the conditional independence of eq. 4 holds by construction; no bound on attractor overlap is proved.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The paper informs the collective side of the program. It is a population of blanketed units, each holding a one-parameter exponential-family belief, whose local free energy minimization composes, for symmetric couplings, into an explicit network-scale posterior (eq. 22). That is a concrete case of micro-level inference yielding a macro-level inferring particle, comparable to the exact spin-glass case already in the vault, and it would supply a test bed for claims about coarse-graining to meta-agents. Evidence from neighbors is added in natural parameters, $\theta_i = b_i + \sum_j J_{ij}\sigma_j$, after a deterministic scaling by $J_{ij}$ at the blanket. One can read that scaling as a scalar stand-in for transport between agents, but the reading is interpretive: $J_{ij}$ carries no group structure, is not invertible in general, is learned as a statistical coupling, and no compatibility with the geometry of the belief family is claimed. The split of couplings into a symmetric dissipative part and an antisymmetric solenoidal part parallels a gradient sector plus a conservative sector in belief dynamics, with the caveat that the paper's statement about the stationary law under asymmetric coupling is unproved. Links to the Fisher metric, Gaussian fibers and belief inertia are weak.

## Cross-links

Concepts: [[Attractor networks]]; [[Associative Memory]]; [[Bayesian mechanics]]; [[Markov Blanket]]; [[Nonequilibrium steady state]]; [[Meta-agents and hierarchical emergence]]; [[Collective active inference]]; [[Energy-Based Models]].

Related sources: [[friston-2023-fep-simpler]]; [[friston-2023-path-integrals-particular]]; [[palacios-2020-hierarchical-markov-blankets]]; [[ramstead-2023-bayesian-mechanics]]; [[friston-2019-particular-physics]]; [[hinton-2002-products-of-experts]]; [[hinton-sejnowski-1986-boltzmann]]; [[heins-2023-spin-glass-active-inference]]; [[friston-2012-free-energy-value-attractors]]; [[isomura-2023-bayesian-mechanics-self-organising]].

## BibTeX

```bibtex
@article{spisak2026selforthogonalizing,
  title = {Self-orthogonalizing attractor neural networks emerging from the free energy principle},
  author = {Spisak, Tamas and Friston, Karl},
  journal = {Neurocomputing},
  year = {2026},
  pages = {133472},
  doi = {10.1016/j.neucom.2026.133472},
  eprint = {2505.22749},
  archivePrefix = {arXiv},
  primaryClass = {q-bio.NC},
  note = {Article number 133472; arXiv v2, 21 May 2026}
}
```
