---
type: paper
title: "Global culture: A noise-induced transition in finite systems"
aliases:
  - "Klemm, Eguíluz, Toral and San Miguel 2003"
  - "Klemm et al. 2003"
  - "Axelrod model with cultural drift"
authors:
  - Klemm K.
  - Eguíluz V.M.
  - Toral R.
  - San Miguel M.
year: 2003
arxiv: "cond-mat/0205188"
doi: "10.1103/PhysRevE.67.045101"
url: "https://arxiv.org/abs/cond-mat/0205188"
tags:
  - cluster/social-physics
  - cluster/social-physics/evolutionary-and-cultural
  - cluster/multi-agent
  - project/social-physics
  - project/multi-agent
  - field/physics
  - field/sociology
created: 2026-09-28
updated: 2026-09-28
---

# Global culture: A noise-induced transition in finite systems

> [!info] Citation
> K. Klemm, V. M. Eguíluz, R. Toral and M. San Miguel (2003). "Global culture: A noise-induced transition in finite systems." *Physical Review E* **67**, 045101(R). doi:10.1103/PhysRevE.67.045101. arXiv:cond-mat/0205188.

## Verification record

Metadata verified on 2026-09-28 against the arXiv abstract page (journal reference and DOI). Full text read. Gathered by Claude Opus 5.5, verified by Claude Fable 5.1 (verdict VERIFIED). The verifier added two precisions, recorded below: the universal scaling form uses an effective rate $f=r(1-1/q)N\ln N$, and the $r\to0$ limit does not recover the model without noise.

## Verified content

The paper adds cultural drift, random single-trait changes at rate $r$, to Axelrod's model of cultural dissemination. The abstract states that disordered multicultural states are metastable, proved in one dimension through a Lyapunov potential, $V=-\sum_{i=1}^{N-1}l(i,i+1)$ (p. 2). A mean-field first-exit recursion (Eqs. 1–2) gives the relaxation time $T=N\ln N$ (Eq. 3). Figure 4 plots the largest-domain size against $r$ for several $N$, and Figure 5 collapses the data in the scaling variable $R=rT=rN\ln N$; the stated universal form uses the effective rate $f=r(1-1/q)N\ln N$. Drift at rates small compared with $1/T$ drives a finite system to global culture, while larger rates keep it disordered. Footnote [10] says that the word "transition" is used although this is not a phase transition in the sense of equilibrium statistical mechanics, because it disappears in the thermodynamic limit. The paper also notes that the $r\to0$ limit does not recover the $r=0$ model.

## Relevance to this research

This is the closest social-model analogue of the two remedies in [[Soft formation and the activation clock]]. In a finite population, noise can erase the founding disorder if the system is given longer than $T=N\ln N$, which is the "wait out the transient" remedy. As $N\to\infty$ that time diverges, so the founding configuration stops being a transient that can be waited out, and a coarse description has to carry it, which is the memory-variable remedy. The sharpness is a finite-size competition between time scales, and the authors themselves separate it from a genuine phase transition. For the multi-agent program the lesson concerns scale: which remedy is available can depend on the number of agents, so a result obtained on a four-agent cycle does not settle the question for networks of hundreds of agents. The discarded quantities differ, trait-level heterogeneity here and within-pair disagreement coordinates in [[multiagentelbo-2026-09-28-early-parent]]. The mapping is interpretive.

## Cross-links

- Concepts: [[Axelrod model of cultural dissemination]], [[Phase transitions in social systems]], [[Soft formation and the activation clock]]
- Themes: [[Statistical physics of social systems and collective behavior]]
- Related sources: [[castellano-marsili-vespignani-2000-axelrod-transition]], [[axelrod-1997-dissemination-of-culture]], [[castellano-2009-statistical-physics-social-dynamics]], [[yang-1952-phase-transitions-condensation]]

## BibTeX

```bibtex
@article{klemm2003global,
  author        = {Klemm, K. and Egu{\'\i}luz, V. M. and Toral, R. and San Miguel, M.},
  title         = {Global culture: A noise-induced transition in finite systems},
  journal       = {Physical Review E},
  volume        = {67},
  pages         = {045101(R)},
  year          = {2003},
  doi           = {10.1103/PhysRevE.67.045101},
  eprint        = {cond-mat/0205188},
  archivePrefix = {arXiv}
}
```
