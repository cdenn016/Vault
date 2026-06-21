---
type: paper
title: "Quantum probabilities as Bayesian probabilities"
aliases:
  - "Caves 2002"
  - "QBism foundations"
  - "caves2002-quantum-bayesian"
authors:
  - Caves, Carlton M.
  - Fuchs, Christopher A.
  - Schack, Rüdiger
year: 2002
arxiv: quant-ph/0106133
url: https://doi.org/10.1103/PhysRevA.65.022305
tags:
  - cluster/participatory/quantum-foundations
  - project/multi-agent
  - field/physics
  - field/philosophy
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Quantum probabilities as Bayesian probabilities

> [!info] Citation
> Caves, C. M., Fuchs, C. A., & Schack, R. (2002). "Quantum probabilities as Bayesian probabilities." Physical Review A 65, 022305. arXiv:quant-ph/0106133.

## TL;DR
This paper argues that all quantum probabilities, even those arising from pure states, are Bayesian (subjective) degrees of belief rather than objective frequencies. Using Gleason's theorem and the Dutch-book argument, the authors show that any consistent Bayesian probability assignment over quantum questions must take the standard Born-rule form, that maximal information about a quantum system forces a unique pure-state assignment, and that quantum mechanics provides a tighter probability-frequency connection than is possible classically. The notion of an "unknown quantum state" is eliminated from tomography via the quantum de Finetti representation theorem.

## Problem & setting
The standard view holds that probabilities arising from pure quantum states are objective, prescribed by physical law, and thus incompatible with a Bayesian (subjective) interpretation. The authors challenge this: if quantum states encode knowledge rather than objective reality (motivated by Einstein's EPR argument and experimental bounds on superluminal influences), all probabilities derived from them are subjective. Prior art includes frequentist and Copenhagen interpretations of quantum probability, de Finetti's classical exchangeability theorem, and Gleason's 1957 theorem on measures over Hilbert-space subspaces.

## Method
The argument proceeds in three steps. First, Gleason's theorem: assuming (i) quantum questions correspond to complete orthonormal projector sets, (ii) Dutch-book consistency (no sure-loss betting strategy), and (iii) noncontextuality, any probability assignment must satisfy

$$p(\hat{\Pi}) = \mathrm{tr}(\hat{\rho}\,\hat{\Pi}), \quad \hat{\Pi} = |\psi\rangle\langle\psi|,$$

for some density operator $\hat{\rho}$. This is the Born rule, derived from coherence alone.

Second, the Dutch-book uniqueness argument for maximal information: if a scientist is certain that projector $\hat{\Pi} = |\psi\rangle\langle\psi|$ will yield outcome 1, consistency forces $\langle\psi|\hat{\rho}|\psi\rangle = 1$, hence $\hat{\rho} = |\psi\rangle\langle\psi|$ — a unique pure-state assignment. Maximal quantum information is not complete (unlike the classical case), so this pure state still assigns nontrivial probabilities to other measurements.

Third, the quantum de Finetti representation: for an exchangeable sequence of density operators $\hat{\rho}^{(N)}$ (symmetric and consistent under partial trace), the unique decomposition is

$$\hat{\rho}^{(N)} = \int d\rho\; p(\rho)\; \rho^{\otimes N},$$

where $p(\rho)$ is a probability measure over density operators. This eliminates "unknown quantum states" from tomography, replacing them with a Bayesian prior over density operators that is updated by data via Bayes's rule.

## Key results
1. Gleason's theorem implies that Dutch-book consistency plus the Hilbert-space structure of quantum questions fully determines the Born rule — Bayesian degrees of belief are constrained to the standard quantum probability form.
2. Maximal information about a quantum system uniquely determines a pure state via Dutch-book consistency; this uniqueness holds even though the state cannot be verified by addressing questions to the system alone.
3. Pure maximal-information states force i.i.d. product-state assignments over $N$ copies, yielding multinomial distributions that concentrate near true frequencies as $N \to \infty$ — a probability-frequency connection strictly stronger than what Bayesian reasoning can justify classically.
4. The quantum de Finetti theorem eliminates "unknown quantum states" from tomography: the experimenter's exchangeable prior over systems is decomposed into a mixture of i.i.d. pure states, with convergence to agreement between different experimenters as data accumulate.

## Relevance to this research
This paper is a foundational reference for the **participatory realism / QBism** strand of the VFE research program. Several direct connections arise. The view that quantum states are states of knowledge — Bayesian beliefs rather than objective properties — maps directly onto the VFE transformer's treatment of beliefs as Gaussian tuples $(μ, Σ, φ)$ encoding an agent's epistemic state, not objective facts about the world. The Dutch-book derivation of the Born rule from consistency of belief-updating parallels the VFE principle: beliefs evolve to minimize surprise (free energy), not because reality dictates a particular state but because coherent inference demands it. The quantum de Finetti representation (mixture over i.i.d. density operators, updated by Bayes's rule) is structurally analogous to the prior-bank / PriorBank decode in the VFE architecture, where a latent mixture prior over learned prototypes is updated by VFE minimization. The "maximal-but-incomplete information" theme — a pure state prescribes nontrivial probabilities for all other questions — resonates with the SPD belief geometry, where a Gaussian with small but nonzero covariance is maximally informed yet fundamentally uncertain. More broadly, this paper supports the participatory-realism interpretation being developed in `Manuscripts-Theory/PIFB.tex`, where agents' beliefs constitute reality rather than passively reflecting a mind-independent world.

## Cross-links
- Concepts: [[Participatory Realism]], [[Bayesian Inference]], [[Quantum Foundations]], [[de Finetti Representation]]
- Related sources: [[fuchs-2002-quantum-mechanics]], [[jaynes-2003-probability]]
- Manuscript/Project: [[PIFB]], [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{Caves2002,
  author  = {Caves, Carlton M. and Fuchs, Christopher A. and Schack, R{\"u}diger},
  title   = {Quantum probabilities as {B}ayesian probabilities},
  journal = {Physical Review A},
  volume  = {65},
  pages   = {022305},
  year    = {2002},
  doi     = {10.1103/PhysRevA.65.022305},
  eprint  = {quant-ph/0106133},
}
```
