---
type: paper
title: "Thermalisation for small random perturbations of dynamical systems"
aliases:
  - "Barrera and Jara 2020"
  - "Small-noise cutoff thermalisation"
authors:
  - Barrera G.
  - Jara M.
year: 2020
arxiv: "1510.09207"
doi: "10.1214/19-AAP1526"
url: "https://arxiv.org/abs/1510.09207"
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/mathematics
created: 2026-09-28
updated: 2026-09-28
---

# Thermalisation for small random perturbations of dynamical systems

> [!info] Citation
> G. Barrera and M. Jara (2020). "Thermalisation for small random perturbations of dynamical systems." *The Annals of Applied Probability* **30**(3), 1164–1208. doi:10.1214/19-AAP1526. arXiv:1510.09207 (v5, 5 Sep 2020).

## Verification record

Checked on 2026-09-28 in two separate literature lenses (cutoff and transitions). Each check read the arXiv abstract page, the Crossref record, and the full text of arXiv v5. Gathered by Claude Opus 5.5, verified by Claude Fable 5.1, verdict VERIFIED in both. The transitions-lens verifier judged the gatherer's label "exact" for the model mapping to be overstated; the relevance section below follows that correction. The cutoff-lens verifier corrected two points of wording, both adopted here: Theorem 2.2 holds for each fixed $c$, not uniformly in $c$, and the constants $\lambda,l,\tau$ are those that Lemma 2.1 attaches to the initial point, not the coercivity constant of (H).

## Verified content

The paper studies $dx=-F(x)\,dt+\sqrt{\epsilon}\,dB$ (eq. 2.4) with a hyperbolic attractor at the origin, under a strong coercivity condition (H), $\langle x,DF(y)x\rangle\ge\lambda|x|^2$, and a growth condition (G), $|F(x)|\le c_0e^{c_1|x|^2}$. For an initial point $x_0\neq0$, Lemma 2.1 reads off the deterministic trajectory $\varphi(t,x_0)$ the constants $\lambda$, $l$, $\tau$, $\theta_k$, $v_k$: the Jordan data of $DF(0)$ that govern the slowest-decaying component present in $x_0$. The cutoff time (eq. 2.7) is

$$t_{\mathrm{mix}}=\frac{1}{2\lambda}\ln\frac1\epsilon+\frac{l-1}{\lambda}\ln\ln\frac1\epsilon+\tau,$$

and the window (eq. 2.6) is $w=1/\lambda+o(1)$. Theorem 2.2 states that for each fixed $c\in\mathbb R$ the total-variation distance to the invariant law at $t_{\mathrm{mix}}+cw$ is asymptotic to $D(t)$, the total-variation distance between a standard Gaussian and a copy shifted by $(e^{\lambda(t-\tau)}(t-\tau)^{l-1})^{-1}\epsilon^{-1/2}\Sigma^{-1/2}\sum_ke^{i\theta_k(t-\tau)}v_k$ (eq. 2.8), where $\Sigma$ solves the Lyapunov equation $DF(0)X+XDF(0)^\top=I$ (eq. 2.9). Remark 2.4 gives the explicit error-function form of the profile. Corollary 2.9 characterizes when a limiting profile exists, and Corollary 2.10 gives profile cutoff when every eigenvalue of $DF(0)$ is real. Section 2.3 notes, citing [[freidlin-2012-random-perturbations-dynamical-systems]], that other attractors are not accessible until times of order $e^{c/\epsilon}$. Linear drift is covered because $\varphi(t)=e^{-At}x_0$ makes eq. 2.8 exact; eq. 3.5 is the linearized fluctuation process used inside the proof, not a separate theorem.

## Relevance to this research

Three differences bound the match. The theorem concerns the total-variation distance of the full, unconditioned law from a deterministic start, under global conditions (H) and (G) that have not been established for the four-cycle. The model's quantity is the discarded conditional relative entropy of a law conditioned on a seed event and held. The threshold locations agree because, for Gaussians with a common covariance, both distances are monotone in the Mahalanobis length of the mean shift, and that is an elementary linear computation which the theorem does not supply. The $O(1)$ profile inside the window does not transfer. See [[Meta-agents and hierarchical emergence]].

## Cross-links

- Concepts: [[Meta-agents and hierarchical emergence]], [[Geometric singular perturbation theory]]
- Themes: [[Meta-agents and hierarchical emergence]]
- Related sources: [[barrera-2016-abrupt-convergence-small-perturbations]], [[boursier-2023-universal-cutoff-dyson-ornstein-uhlenbeck]], [[diaconis-1996-cutoff-phenomenon-markov-chains]], [[freidlin-2012-random-perturbations-dynamical-systems]], [[levin-undated-markov-chains-and-mixing-times-retrieved-author-text]]

## BibTeX

```bibtex
@article{barrera2020thermalisation,
  author        = {Barrera, G. and Jara, M.},
  title         = {Thermalisation for small random perturbations of dynamical systems},
  journal       = {The Annals of Applied Probability},
  volume        = {30},
  number        = {3},
  pages         = {1164--1208},
  year          = {2020},
  doi           = {10.1214/19-AAP1526},
  eprint        = {1510.09207},
  archivePrefix = {arXiv}
}
```
