---
type: paper
title: "Regarding Flows Under the Free Energy Principle: A Comment on 'How Particular is the Physics of the Free Energy Principle?' by Aguilera, Millidge, Tschantz, and Buckley"
aliases: ["Sakthivadivel 2022 regarding flows fep"]
authors: ["Dalton A. R. Sakthivadivel"]
year: 2022
venue: "Physics of Life Reviews 42:25-28"
arxiv: "2205.07793"
doi: "10.1016/j.plrev.2022.05.009"
url: "https://arxiv.org/abs/2205.07793"
version: "arXiv:2205.07793v2 [cond-mat.stat-mech], stamped 1 Jun 2022, with the title-page date printed as 2nd June 2022; 5 pages. The journal version of record (Physics of Life Reviews 42, 25-28) was not the version read."
tags: [cluster/vfe, project/multi-agent, field/physics, field/neuroscience]
created: 2026-11-13
updated: 2026-11-13
---

# Regarding Flows Under the Free Energy Principle: A Comment on "How Particular is the Physics of the Free Energy Principle?" by Aguilera, Millidge, Tschantz, and Buckley

> [!info] Citation
> Dalton A. R. Sakthivadivel (2022). *Regarding Flows Under the Free Energy Principle: A Comment on "How Particular is the Physics of the Free Energy Principle?" by Aguilera, Millidge, Tschantz, and Buckley*. Physics of Life Reviews 42:25-28. [arXiv:2205.07793](https://arxiv.org/abs/2205.07793) [DOI](https://doi.org/10.1016/j.plrev.2022.05.009)

[Local PDF](../pdfs/sakthivadivel-2022-regarding-flows-fep.pdf), 5 pages; retrieved November 13, 2026. Version read: arXiv:2205.07793v2 [cond-mat.stat-mech], stamped 1 Jun 2022, with the title-page date printed as 2nd June 2022; 5 pages. The journal version of record (Physics of Life Reviews 42, 25-28) was not the version read. Reading basis: The first reader worked from the extracted text and did not see the typeset pages. I read all 5 pages in full against both the rendered pages and the extracted text. Equations (1) and (2) and the three unnumbered displays on page 3 were checked against the rendered page. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, page-002, page-003, page-004). Confirmed against those pages: (1) <mu(t)>_omega = int_0^t f_mu(bold mu_s, b) ds; the unnumbered constraint E_{p(gamma)}[gamma] = C(t); the constrained caliber functional; (2) exp{-lambda_{0,...,n}(mu_0,...,mu_n)}; the product exp{-lambda(n)mu(n)} exp{-lambda(n-1)mu(n-1)} ... exp{-lambda(0)mu(0)}. Title page: arXiv:2205.07793v2 [cond-mat.stat-mech] 1 Jun 2022, date 2nd June 2022. The page 4 concession that the critiques are 'mathematically correct', the 'appears to be equivalent' wording, the citations FCS+22, BDCF+22, PGLD13, GDAD20 and the thanks to Friston are confirmed.

## TL;DR

An informal comment on Aguilera et al. that concedes two of their conclusions about linear systems as mathematically correct and argues that they are not fatal to the free energy principle. It conjectures that a path-based formulation, sketched through a constrained maximum caliber argument, restores the content that the density-over-states formulation lacks, and takes the position that the principle is uninformative about linear systems by design.

## Problem & setting

The target paper shows, for linear diffusions, that the absence of solenoidal coupling between external and other states is rare, so sparse coupling is a sufficient and not a necessary sign of being a system, and that marginal flows of internal and external states on free energy and surprisal gradients correlate poorly with the system's dynamics (its Section 3.1, Section 3.2 and Figure 5). The comment accepts both derivations and asks whether they undermine the principle. Its standing premise is that the free energy principle is naturally path-based, with reference to Friston (2019), to the then-preprint The free energy principle made simpler but not too simple, and to Barp et al. (2022), and that nonequilibrium systems are better described by probabilities over trajectories than over states, with reference to Jaynes's principle of maximum caliber, to Presse et al. (2013), to Ghosh et al. (2020) and to the stochastic thermodynamics literature. It thanks Friston for sharing preliminary work that writes the principle in terms of trajectories.

## Method

The comment has no formal construction beyond a maximum caliber sketch on page 3. It first restates the two conclusions of the target paper. Section 2.1 then proposes that the Markov blanket as usually presented is a special case of individuation along the dynamical evolution of a system, expressed as conditional independence of the system's flow from its environment, which should be readable from the Jacobian or from probabilities over system-like trajectories given environmental dynamics, without a density over states. Section 2.2 takes the average trajectory $\langle \mu(t) \rangle_\omega = \int_0^t f_\mu(\boldsymbol{\mu}_s, b) ds$ (1), where the bracket is an expectation over realizations of the noise $\omega$, rewrites it for a sample path $\gamma$ as the constraint $E_{p(\gamma)}[\gamma] = C(t)$, and forms the constrained caliber functional $-\int_\pi \ln\{p(\gamma)\} p(\gamma) d\gamma - \lambda(t) \left( \int_\pi \gamma p(\gamma) d\gamma - C(t) \right)$ over the space of paths $\pi$. Assuming independence across time steps for notational ease, the resulting density $\exp\{-\lambda_{0,\ldots,n}(\mu_0, \ldots, \mu_n)\}$ (2) is written as the product $\exp\{-\lambda(n)\mu(n)\} \exp\{-\lambda(n-1)\mu(n-1)\} \cdots \exp\{-\lambda(0)\mu(0)\}$, each factor read as a belief that has the mode $\boldsymbol{\mu}_t$ as its parameter and sufficient statistic. Mapped into a statistical manifold, the sequence is read as an inference process in which the belief changes at every step.

## Key results

Nothing is proved; the piece calls itself an informal comment and labels its positive claims as conjectures. It concedes (Section 3, page 4) that the two points of critique raised by Aguilera et al. are mathematically correct. It asserts (Section 2, page 2) that path descriptions are superior to state descriptions because maximum caliber is asymptotically maximum entropy, supported by citation only. Section 2.1 (page 2) asserts that sparse coupling should be a special case of path-wise conditional independence and that the stereotyped structure of the Hessian should become unnecessary; no definition or criterion of path-wise independence is given. Section 2.2 (page 3) argues that under linear fluctuations a system dissipates on average to a fixed point $\mu^*$, so it matches a mode without tracking a moving one, and the flow on free energy is trivial; Figure 5 of the target paper is read as showing that the evolution of a few samples is not representative. The maximum caliber density (2) is offered, conjecturally, as a model of a system that infers where the mode will be at a future time step and flows toward it, and the comment says this appears to be equivalent to the formulations of Friston (2019) and Parr et al. (2020). It concludes (page 4) that the state-based formulation assumes an idealized nonequilibrium steady state valid for an ensemble and not for one realization, that only the fluctuations of linear systems carry nontrivial dynamics, and that the principle is most informative for nonlinear or chaotic systems.

## Limits

The author states that the comment is informal, that the path-based resolution is conjectural, and that the equivalence of the caliber construction with earlier formulations only appears to hold. My observations: the functional on page 3 carries a mean constraint and no normalization constraint, and a density of the form $\exp\{-\lambda \mu\}$ on an unbounded state space is not normalizable without a further constraint or a reference measure, so (2) is schematic. The assumed independence across time steps removes the temporal structure that a path formulation is meant to add. No criterion is given for when path-wise independence holds, so the claim that it generalizes sparse coupling cannot be assessed from this text; the author's 2026 preprint in this batch supplies such criteria.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> This comment is a marker of position more than a source of mathematics. It records the point at which a lineage author concedes that the state-density formulation says little about linear systems and moves the content of the blanket to path measures, a move carried out formally in the 2026 preprint in this batch. For the program the relevant challenge is direct: linear couplings with Gaussian stationary beliefs are the regime the comment calls uninformative, where a system matches a fixed mode and does not track a moving one, so an inference reading of Gaussian belief dynamics would have to come from nonstationary or nonlinear structure. The maximum caliber sketch, in which a trajectory is a sequence of exponential-family beliefs indexed by their modes, resembles a curve through a statistical manifold; that resemblance is interpretive, and because the sketch assumes independence across time it carries no transport or connection. The links to gauge structure, the Fisher metric and Hamiltonian belief dynamics are weak.

## Cross-links

Concepts: [[Bayesian mechanics]]; [[Markov blanket interpretation debate]]; [[Markov Blanket]]; [[Maximum entropy]]; [[Nonequilibrium steady state]]; [[Exponential family]]; [[Free-energy principle active inference]].

Related sources: [[aguilera-2022-particular-physics]]; [[friston-2019-particular-physics]]; [[parr-2020-markov-blankets-thermodynamics]]; [[friston-2023-fep-simpler]]; [[friston-2021-stochastic-chaos-markov]]; [[friston-2023-path-integrals-particular]]; [[heins-2022-sparse-coupling-markov]]; [[friston-2022-very-particular-comment]]; [[ramstead-2022-notation-minima-comment]]; [[heins-2022-particular-flows-attracting-sets]]; [[sakthivadivel-2026-markov-interacting-particles]]; [[sakthivadivel-2023-worked-example-classical-objects]]; [[barp-2022-geometric-methods-sampling]].

## BibTeX

```bibtex
@article{sakthivadivel2022regarding,
  author = {Sakthivadivel, Dalton A. R.},
  title = {Regarding Flows Under the Free Energy Principle: A Comment on ``{H}ow Particular is the Physics of the Free Energy Principle?'' by {A}guilera, {M}illidge, {T}schantz, and {B}uckley},
  journal = {Physics of Life Reviews},
  volume = {42},
  pages = {25--28},
  year = {2022},
  doi = {10.1016/j.plrev.2022.05.009},
  eprint = {2205.07793},
  archivePrefix = {arXiv},
  primaryClass = {cond-mat.stat-mech}
}
```
