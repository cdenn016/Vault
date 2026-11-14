---
type: paper
title: "A Worked Example of the Bayesian Mechanics of Classical Objects"
aliases: ["Sakthivadivel 2023 worked example classical objects"]
authors: ["Dalton A. R. Sakthivadivel"]
year: 2023
venue: "Active Inference: Third International Workshop (IWAI 2022), Communications in Computer and Information Science vol. 1721, pp. 298-318, Springer"
arxiv: "2206.12996"
doi: "10.1007/978-3-031-28719-0_21"
url: "https://arxiv.org/abs/2206.12996"
version: "arXiv:2206.12996v2 [physics.class-ph], 6 September 2022 (document dated 7th September 2022); 34 pages. This is the long preprint, not the condensed IWAI 2022 proceedings chapter (CCIS vol. 1721, pp. 298 to 318) named in the manifest."
tags: [cluster/vfe, project/multi-agent, field/physics, field/statistics]
created: 2026-11-13
updated: 2026-11-13
---

# A Worked Example of the Bayesian Mechanics of Classical Objects

> [!info] Citation
> Dalton A. R. Sakthivadivel (2023). *A Worked Example of the Bayesian Mechanics of Classical Objects*. Active Inference: Third International Workshop (IWAI 2022), Communications in Computer and Information Science vol. 1721, pp. 298-318, Springer. [arXiv:2206.12996](https://arxiv.org/abs/2206.12996) [DOI](https://doi.org/10.1007/978-3-031-28719-0_21)

[Local PDF](../pdfs/sakthivadivel-2023-worked-example-classical-objects.pdf), 34 pages; retrieved November 13, 2026. Version read: arXiv:2206.12996v2 [physics.class-ph], 6 September 2022 (document dated 7th September 2022); 34 pages. This is the long preprint, not the condensed IWAI 2022 proceedings chapter (CCIS vol. 1721, pp. 298 to 318) named in the manifest. Reading basis: The first reader worked from the extracted text and did not see the typeset pages. The note rests on the extracted text. Pages 1 to 31 were read in full (abstract, Sections I to VII, all numbered equations 1 to 20 and the footnotes); the reference list on pages 31 to 34 was skimmed. Equations (3), (5), (10), (12) to (20) were legible in the extracted text and are reported from it. The univariate Gaussian KL expression on page 11 and the matrix display of eq. (18) were partly garbled and are described in words only. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, page-005, page-006, page-008, page-009, page-010, page-011, page-012, page-015, page-016, page-017, page-018, page-019, page-020, page-021, page-022, page-023, page-024, page-025, page-026, page-027, page-028, page-029, page-030, page-031). Confirmed against those pages: (3) dX_t = f dt + sqrt(2D) dW_t; path surprisal S[gamma] = int (1/4D)<omega,omega>; (5) p(x(t)|x_0) = exp{-lambda S[gamma]}; (6), (7), (8) are free-energy functionals for states and trajectories as the note says; (10) mean constraint; -ln p(mu|eta) = (mu - sigma^{-1}(eta_b))^2 (p. 12); inverse synchrony map and double-integral map (p. 15); (12); (13); (14) (printed with |.|^2, equivalent); (15); lambda_1 proportional to D^{-1} (p. 18); Wick-rotated measure with m/2hbar (p. 19); mode-matching surprisal lambda_1(q - iint F/m)^2 (p. 21); (16); (17); (18) skew-symmetric system and d_tt q = -nu^2 q; (19) with lambda_1 = 1/2, lambda_2 = -1/nu; path-space result d_tt q - F/m = 0 (p. 28); (20). Lambda_1 statements on pp. 17, 19, 29 and the 'Newton's first law' wording on p. 22 confirmed. Title page: v2, 6 Sep 2022, dated 7th September 2022.

## TL;DR

The paper restates Bayesian mechanics as a least-surprisal principle with a synchronization map and works it out for a classical point particle, taking position as internal state, the environment as external state and the applied force as blanket state. Constrained maximum entropy and maximum caliber with a mean constraint (the Newtonian trajectory) and a vanishing-variance constraint give a Gaussian path density whose infinite-precision limit concentrates on the classical path. It ends with a sketch that links the resulting path integral to the $N = 2$ supersymmetric (BRST) formulation of classical mechanics and to chaos.

## Problem & setting

The free energy principle is often said to be as general as the principle of stationary action, yet worked applications to specific physical systems are rare, and the mechanics of the systems that carry beliefs is hard to extract from the mechanics of the beliefs. The paper asks what Bayesian mechanics says in the simplest case, classical objects with trivial (infinitely precise) beliefs. The standing assumptions are Itô diffusions with additive Gaussian white noise of constant amplitude $D$ (an ideal heat bath), a quadratic path action with the Stratonovich correction neglected, conditional independence of internal and external states given blanket states, existence of conditional expectations and of a synchronization map $\sigma$, and a Laplace (Gaussian) approximation. It builds on Friston 2019, Parr, Da Costa and Friston 2020, Da Costa et al. 2021, the path formulation of Friston et al. 2022, the author's own geometry and analysis paper, and the Ramstead et al. review, whose typology of mode-matching, mode-tracking and path-tracking it instantiates. It also draws on maximum caliber (Pressé et al. 2013) and on the earlier derivation of Newtonian dynamics from maximum caliber by González, Davis and Gutiérrez (2014).

## Method

Section II.B starts from $dX_t = f(X_t,t)dt + \sqrt{2D}dW_t$ (eq. 3), defines the fluctuation $\omega_t = v_t - f(X_t,t)$ and the path surprisal $S[\gamma] = \int_0^t \frac{1}{4D}\langle\omega_\tau,\omega_\tau\rangle d\tau$, with path density $p(x(t) \mid x_0) = \exp\{-\lambda S[\gamma]\}$ (eq. 5). Two coupled systems $\eta$ and $\mu$ with blanket $b$ have conditional means related by $\sigma(\hat\mu_{b,t}) = \hat\eta_{b,t}$, and the variational free energy of a recognition density $r(\eta \mid \mu)$ is written for states (eqs. 6 and 7) and for trajectories (eq. 8). Section II.D recasts this as a maximum-entropy problem on internal states with the mean constraint $E_{p(\mu\mid\eta)}[\mu \mid \eta] = \sigma^{-1}(\hat\eta_b) = \hat\mu_b$ (eq. 10) and a variance constraint, giving $-\ln\{p(\mu \mid \eta)\} = (\mu - \sigma^{-1}(\hat\eta_b))^2$. Section III specializes: the position $q$ is the internal state, the total force $F_t$ is the blanket (sensory) state, and the inverse synchrony map is $\sigma^{-1} : \eta_t \to F_t \to q_t$ with $F(\eta,t) \mapsto \iint F(\eta,s)/m = q_t$. The constraints are $E_{p(q)}[q] = \iint F(\eta)/m$ (eq. 12) and zero accumulated variance along a path (eq. 13). Maximum entropy then gives $$p(q) = \exp\left\{-\lambda_1\left(q - \lambda_2\iint\frac{F(\eta)}{m}\right)^2\right\}$$ (eq. 14) and, over paths, $$p(q,t) = \exp\left\{-\lambda_1(t)\int_0^t\left(q(\tau) - \lambda_2(\tau)\iint\frac{F(\eta,s)}{m}\right)^2 d\tau\right\}$$ (eq. 15), which the author calls the general equation for Bayesian classical mechanics. Sections V to VII evaluate it for a stone at rest, a falling stone, a circular orbit and general path-tracking, and Section VII.B rewrites the Dirac-concentrated path measure with ghost fields.

## Key results

All results are derivations at a physicist's level of rigor; the paper states no theorems and reports no simulations. Section III (pp. 14 to 18) argues that the path density (15) reproduces classical dynamics when $\lambda_2 = 1$ and the precision multiplier $\lambda_1$ tends to infinity, with the heuristic $\lambda_1 \propto D^{-1}$ (p. 18); the author compares this with the $\hbar \to 0$ limit of the Feynman path integral. Section IV (pp. 18 to 21) argues informally, through Ehrenfest's theorem and a Wick-rotated Wiener measure with scale $m/2\hbar$, that the modal path of a fluctuating system is the classical path, so that surprisal minimization is already present in quantum mechanics; the proof of the $\hbar \to 0$ statement is explicitly omitted (p. 20). Section V (pp. 21 to 22) gives mode-matching for a stone with $\sum F = -F_g + F_N = 0$ (eq. 16) and surprisal $\lambda_1(q - \iint F(\eta)/m)^2$. Section VI.A (pp. 22 to 24) treats free fall, $q(t) = q(0) + v(0)t - \frac{1}{2}gt^2$ (eq. 17), as mode-tracking that terminates in a fixed mode and identifies the motion with the gradient component of the Helmholtz decomposition. Section VI.B (pp. 24 to 26) treats an orbit through a skew-symmetric linear system (eq. 18), equivalent to $\partial_{tt}q = -\nu^2 q$, and identifies it with the solenoidal component, using $-\nabla\ln\{p(q,t)\} = 2\lambda_1(q(t) - \lambda_2\hat q)$ (eq. 19) with $\lambda_1 = 1/2$ and $\lambda_2 = -1/\nu$. Section VII.A (pp. 26 to 28) states that the path-space gradient of the surprisal vanishes if and only if $\partial_{tt}q(t) - F(\eta,t)/m = 0$ and says the step needs further work to be rigorous. Section VII (p. 26) adopts the name G-theory, from Ramstead et al., for the duality between maximum caliber and path-based Bayesian mechanics; Section VII.B (pp. 29 to 31) writes the classical path measure as $Z[C] = \int_\Gamma\prod_t\delta(x_t - x_{t,cl})e^{-\lambda_1(t)\int_0^t C(\tau)x(\tau)d\tau}\mathcal{D}x(t)$ (eq. 20), applies the Gozzi-Reuter-Thacker procedure, and asserts that Bayesian classical mechanics is an $N = 2$ supersymmetric theory whose ghosts correspond to Jacobi fields and whose symmetry breaking is a candidate basis for non-ergodicity. This last part is presented as a sketch.

## Limits

The author concedes that the derivation of the Euler-Lagrange equation starts from the assumption that classical systems follow forces (p. 29 and footnote 25), that the noise is Gaussian with constant variance (footnote 5), that the Stratonovich term is dropped (footnote 6), and that the Helmholtz and path-gradient arguments await formalization. Footnote 10 grants that for non-agential objects the inferential reading is as-if. Observations of this reader: the role of $\lambda_1$ is stated inconsistently, with the classical limit given as $\lambda_1 \to \infty$ on p. 17, as $\lambda_1$ set to $\hbar$ and sent to zero on p. 19, and as a multiplier tending to zero on p. 29; p. 22 attributes the equal-and-opposite-force statement to Newton's first law; the identification of an applied force with a blanket state is defended verbally (p. 15) and no conditional-independence statement is derived for it; and mass enters only through the mean constraint, so Newton's law is encoded in the constraint.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The paper bears on Hamiltonian belief dynamics and belief inertia by contrast more than by support. It places classical mechanics at the infinite-precision corner of Bayesian mechanics: the precision multiplier $\lambda_1 \propto D^{-1}$ controls fluctuations about a modal path, while the mass $m$ sits inside the mean constraint as a given parameter. A program that reads inertial mass as Fisher information or precision of belief makes a different identification, in which precision itself is the inertia. Nothing here derives second-order dynamics from the geometry of beliefs, and the author says the derivation assumes the classical law. What the paper would supply is the explicit duality between constrained maximum caliber on internal trajectories and free energy minimization across a synchronization map for Gaussian beliefs, including the mean and variance matching conditions (eqs. 9 to 11), which is the single-agent Gaussian case that any fiber of Gaussian beliefs would have to reproduce. Its reading of the gradient and solenoidal parts as free fall and orbital motion is illustrative. The force-as-blanket construction uses the blanket concept loosely and should be cited with that caveat. There is no connection, transport or multi-agent content. The link is moderate for the maximum-caliber duality, weak elsewhere, and interpretive throughout.

## Cross-links

Concepts: [[Bayesian mechanics]]; [[Maximum entropy]]; [[Hamiltonian belief dynamics]]; [[Belief inertia]]; [[Mass as Fisher information]]; [[Markov Blanket]]; [[Laplace approximation]]; [[Process-space variational inference]].

Related sources: [[sakthivadivel2022-bayesian-mechanics-geometry]]; [[ramstead-2023-bayesian-mechanics]]; [[friston-2019-particular-physics]]; [[friston-2023-fep-simpler]]; [[parr-2020-markov-blankets-thermodynamics]]; [[dacosta-2021-bayesian-mechanics]]; [[friston-2023-path-integrals-particular]]; [[friston-2021-stochastic-chaos-markov]]; [[sakthivadivel-2022-entropy-maximising-parallel-transport]]; [[sakthivadivel-2022-regarding-flows-fep]]; [[sakthivadivel-2022-weak-markov-blankets]].

## BibTeX

```bibtex
@inproceedings{sakthivadivel2023worked,
  author = {Sakthivadivel, Dalton A. R.},
  title = {A Worked Example of the {B}ayesian Mechanics of Classical Objects},
  booktitle = {Active Inference: Third International Workshop, IWAI 2022},
  series = {Communications in Computer and Information Science},
  volume = {1721},
  pages = {298--318},
  publisher = {Springer},
  year = {2023},
  doi = {10.1007/978-3-031-28719-0_21},
  eprint = {2206.12996},
  archivePrefix = {arXiv},
  primaryClass = {physics.class-ph},
  note = {The proceedings chapter is a condensed version of the 34-page arXiv preprint (v2, 6 September 2022), which is the version read}
}
```
