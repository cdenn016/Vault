---
type: reference
title: "Statistical Physics of Spin Glasses and Information Processing: An Introduction"
aliases: ["Nishimori 2001", "Statistical Physics of Spin Glasses and Information Processing", "Nishimori line"]
authors: ["Hidetoshi Nishimori"]
year: 2001
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, project/social-physics, field/physics, field/statistics, field/cs-ml]
created: 2026-06-20
updated: 2026-06-20
---

# Statistical Physics of Spin Glasses and Information Processing: An Introduction

> [!info] Citation
> Nishimori, H. (2001). *Statistical Physics of Spin Glasses and Information Processing: An Introduction*. International Series of Monographs on Physics, Vol. 111. Oxford University Press, Oxford. ISBN 978-0-19-850940-8.

## TL;DR

The standard introduction to the **statistical mechanics of disordered systems and its identity with Bayesian inference**. Nishimori develops the replica and cavity methods for spin glasses (Sherrington–Kirkpatrick and beyond) and then shows that the *same* free-energy machinery solves canonical information-processing problems: error-correcting codes, image restoration, and associative memory ([[ramsauer2021hopfield|Hopfield]] networks) are all spin systems whose Bayes-optimal decoding is a thermal average. The book's signature contribution is the **Nishimori line** — a special locus in the temperature/disorder plane, fixed by a gauge symmetry of the disorder average, on which the system is at the Bayes-optimal "temperature equals true noise level" condition and many quantities become exactly computable.

## What it establishes

The core identity is that a Bayesian inference problem with a known noise model maps onto a disordered spin system whose Boltzmann distribution *is* the posterior. The partition function is the evidence; the free energy is (minus) the log-evidence; the Bayes-optimal estimator is a magnetization (a thermal/posterior expectation). Key constructions:

- **The Nishimori line** — using a gauge transformation on the quenched disorder, Nishimori derives exact identities (the "Nishimori conditions") that hold when the assumed prior/noise matches the true generating process. On this line the internal energy is exactly computable, replica-symmetry-breaking is suppressed in key quantities, and "Bayes-optimal" becomes a precise thermodynamic statement.
- **Replica and cavity methods** — systematic tools for computing the disorder-averaged free energy $\overline{\ln Z}$, i.e. the typical-case behavior of the inference problem.
- **Information-processing applications** — error-correcting codes (the decoding threshold as a phase transition), image restoration (MAP/MPM estimation as ground-state vs. finite-temperature averaging), and the storage capacity of associative memories, all as one statistical-mechanics framework.

## Why the project cites it

This is the program's bridge between **free energy as thermodynamics** and **free energy as inference**, made rigorous for many-body systems with disorder. The [[Multi-agent variational free energy|multi-agent VFE]] functional is exactly a free energy whose minimization performs inference, and Nishimori's book is the canonical demonstration that the disorder-averaged free energy of a coupled system *is* the right object for typical-case Bayesian behavior — the natural statistical-mechanics partner for the program's coarse-graining to [[Meta-entropy|meta-entropy]] and its [[Renormalization-group flow of beliefs|RG flow of beliefs]]. Two threads connect tightly. First, the **Nishimori line** is the disordered-system version of the program's recurring "Bayes-optimal / matched-prior" condition, and its derivation *via a gauge symmetry of the disorder average* is a striking precedent for the program's claim that the relevant structure on belief space is gauge-theoretic ([[Gauge transformation]]). Second, the spin-glass strand is where the [[Statistical physics of social systems and collective behavior]] theme flags the program's most-wanted unbuilt result — genuine frustration / metastability in coupled beliefs, which needs nontrivial [[Holonomy]] — and Nishimori is the reference for what frustrated-disorder physics (the [[mezard-parisi-virasoro-1987-spin-glass|Mézard–Parisi–Virasoro]] theory) actually delivers and at what cost.

> [!note] Editorial: Cited for the statistical-mechanics-of-inference framework and the Nishimori-line gauge identity, not for a specific computation the program reproduces. The project treats it as the rigorous many-body counterpart of its "free energy minimization = inference" stance.

```bibtex
@book{nishimori2001statistical,
  author    = {Nishimori, Hidetoshi},
  title     = {Statistical Physics of Spin Glasses and Information Processing: An Introduction},
  series    = {International Series of Monographs on Physics},
  volume    = {111},
  publisher = {Oxford University Press},
  address   = {Oxford},
  year      = {2001},
  isbn      = {978-0-19-850940-8}
}
```
