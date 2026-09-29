---
type: paper
title: "Bose-Einstein condensation in complex networks"
aliases:
  - "Bianconi and Barabási 2001"
  - "Bianconi and Barabasi 2001"
  - "Fitness model of growing networks"
authors:
  - Bianconi G.
  - Barabási A.-L.
year: 2001
arxiv: "cond-mat/0011224"
doi: "10.1103/PhysRevLett.86.5632"
url: "https://arxiv.org/abs/cond-mat/0011224"
tags:
  - cluster/social-physics
  - cluster/social-physics/networks-and-contagion
  - cluster/multi-agent
  - project/social-physics
  - project/multi-agent
  - field/physics
  - field/cs-ml
created: 2026-09-28
updated: 2026-09-28
---

# Bose-Einstein condensation in complex networks

> [!info] Citation
> G. Bianconi and A.-L. Barabási (2001). "Bose-Einstein condensation in complex networks." *Physical Review Letters* **86**(24), 5632–5635. doi:10.1103/PhysRevLett.86.5632. arXiv:cond-mat/0011224.

## Verification record

Metadata verified on 2026-09-28 against the arXiv abstract page (journal reference and DOI). Full text read. Gathered by Claude Opus 5.5, verified by Claude Fable 5.1 (verdict VERIFIED). The verifier noted that "founding order persists" in the first-mover phase is a gloss: older nodes have more links, but the leader's share still decays as $t^{-1/2}$. The relevance section states that decay.

## Verified content

In the fitness model of a growing network, a new node attaches to node $i$ with probability $\Pi_i=\eta_ik_i/\sum_j\eta_jk_j$ (Eq. 1), where $\eta_i$ is a fitness, and the energy $\epsilon_i=-(1/\beta)\log\eta_i$ (Eq. 2) maps the model onto a Bose gas. The chemical potential is fixed by $I(\beta,\mu)=1$ (Eq. 10). When $I(\beta,0)<1$ this equation has no solution and the fittest node captures a finite fraction of all links, $n_0/(mt)=1-I(\beta,0)$ (Eqs. 14–15), a winner-takes-all condensate. In the $t\to\infty$ limit the paper distinguishes three phases: (a) scale-free, "first-mover-wins", in which the oldest node's share $k_{\max}/(mt)$ decays as $t^{-1/2}$; (b) fit-get-rich; and (c) the Bose–Einstein condensate. Equation 18 gives a lower bound on the condensation temperature, and Figure 2 shows the chemical potential and $k_{\max}/(mt)$ as functions of $T$.

## Relevance to this research

Condensation here is a transition in who attends to whom: a finite fraction of links condenses onto one source. In the multi-agent model that corresponds to the parent's retained source assignment, not to the discarded within-pair coordinates of [[multiagentelbo-2026-09-28-early-parent]]. It is a genuine limit transition with an order parameter, the condensate fraction, and so is an example of the kind of large-network object that a formation transition in networks of hundreds of agents would need. In the first-mover phase older nodes keep more links, but the leader's share still vanishes as $t^{-1/2}$, so founding advantage there is graded rather than permanent. The limit is network growth, $t\to\infty$, not $T\to0$, and nothing here addresses discarded relative entropy. The mapping is interpretive. See [[Phase transitions in social systems]] and [[Soft formation and the activation clock]].

## Cross-links

- Concepts: [[Network structure — small-world and scale-free]], [[Phase transitions in social systems]], [[Soft formation and the activation clock]]
- Themes: [[Statistical physics of social systems and collective behavior]]
- Related sources: [[barabasi-albert-1999-scale-free]], [[albert-barabasi-2002-statistical-mechanics]], [[castellano-marsili-vespignani-2000-axelrod-transition]]

## BibTeX

```bibtex
@article{bianconi2001bose,
  author        = {Bianconi, G. and Barab{\'a}si, A.-L.},
  title         = {{Bose-Einstein} condensation in complex networks},
  journal       = {Physical Review Letters},
  volume        = {86},
  number        = {24},
  pages         = {5632--5635},
  year          = {2001},
  doi           = {10.1103/PhysRevLett.86.5632},
  eprint        = {cond-mat/0011224},
  archivePrefix = {arXiv}
}
```
