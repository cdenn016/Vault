---
type: paper
title: "Weak Markov Blankets in High-Dimensional, Sparsely-Coupled Random Dynamical Systems"
aliases: ["Sakthivadivel 2022 weak markov blankets"]
authors: ["Dalton A. R. Sakthivadivel"]
year: 2022
venue: "arXiv preprint (math-ph; cross-listed cond-mat.stat-mech, math.DS, math.PR)"
arxiv: "2207.07620"
doi: "10.48550/arXiv.2207.07620"
url: "https://arxiv.org/abs/2207.07620"
version: "arXiv:2207.07620v2 [math-ph], stamped 14 Aug 2022, with the title-page date printed as 16th August 2022; 17 pages; no journal reference."
tags: [cluster/vfe, cluster/multi-agent, project/multi-agent, field/physics, field/mathematics]
created: 2026-11-13
updated: 2026-11-13
---

# Weak Markov Blankets in High-Dimensional, Sparsely-Coupled Random Dynamical Systems

> [!info] Citation
> Dalton A. R. Sakthivadivel (2022). *Weak Markov Blankets in High-Dimensional, Sparsely-Coupled Random Dynamical Systems*. arXiv preprint (math-ph; cross-listed cond-mat.stat-mech, math.DS, math.PR). [arXiv:2207.07620](https://arxiv.org/abs/2207.07620)

[Local PDF](../pdfs/sakthivadivel-2022-weak-markov-blankets.pdf), 17 pages; retrieved November 13, 2026. Version read: arXiv:2207.07620v2 [math-ph], stamped 14 Aug 2022, with the title-page date printed as 16th August 2022; 17 pages; no journal reference. Reading basis: The first reader worked from the extracted text and did not see the typeset pages. The note rests on the extracted text alone. I read text pages 1 to 17 in full, proofs included. No equation was checked against a rendered page. The block-matrix displays (4) and the display after it are scrambled in extraction and are described in words only; the remaining equations are reported where the extracted form is unambiguous. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001 through page-016). Confirmed against those pages: (2), (3), Conjecture 1 and Conjecture 2 conditions, Theorem 1 with (5) and the expansion J = T_{eta eta} H + sum_{t in eta_C} Q H, Definition 2 blanket index, Lemma 3 Ind_max = kmh(n-1) and (7), (8), (9), the union bound 2km e^{-(1/2)(n-1) eps^2} on page 13, (10), and the Proposition 2 nonlinear index. Page locators for Theorem 1 (p5), Lemma 1 (p8), Proposition 1 (p9), Lemma 2 and Theorem 2 (p10), Lemma 3 (p11), Theorem 3 (p12) and Proposition 2 (p14) are correct. Remark 2 hypotheses, the 'ansatz' wording on page 12, the 'sketch' wording in Section 3, the 'relative blankted-ness' remark in Section 7 and the HKD+22 spin-glass citation on page 7 are confirmed. Title page: arXiv:2207.07620v2 [math-ph] 14 Aug 2022, date 16th August 2022, 17 pages.

## TL;DR

The paper defines a blanket index built from the Heins and Da Costa identity relating zeros of the Jacobian, the solenoidal matrix and the Hessian of surprisal, and calls a system weakly blanketed when this index is small. Treating the products $Q_{\eta_i t} H_{t \mu_j}$ as independent, bounded, mean-zero random variables, it applies a Chernoff (Hoeffding) bound to show that the normalized index concentrates at zero exponentially fast in the dimension $n$. It presents this as a proof of a weakened sparse coupling conjecture and of the original conjecture asymptotically.

## Problem & setting

The question is what keeps two coupled random dynamical systems $\eta$ and $\mu$ statistically distinguishable, and how common the required structure is. A Markov blanket is defined (Definition 1) as a coupling state $b$ given which the statistics of $\eta$ and $\mu$ are independent. The sparse coupling conjecture, attributed to Friston and coauthors (the stochastic chaos paper of 2021), holds that sufficiently high-dimensional nonlinear systems with a stationary solution have blankets, while Aguilera et al. (2022) found blankets hard to obtain in linear models. The setting is a stationary diffusion $d\eta_t = -(\Gamma - Q) \nabla U(\eta, b, \mu) dt + \sqrt{2D} dW_t$ (2) with $Q$ skew-symmetric, $\Gamma$ positive definite and $U$ the surprisal, taken quadratic so that the Hessian $H$ is constant and the steady state Gaussian; the operator $T = \Gamma - Q$ is taken constant, or linear in states, so that $J = TH$. The work builds on Friston (2019), on the comment of Heins and Da Costa (2022) and on the author's earlier preprint on the geometry of Bayesian mechanics.

## Method

Writing the Jacobian as $J_{ij} = \sum_t T_{it} \partial_{tj} U + \sum_t \partial_j T_{it} \partial_t U + \partial_{jt} T_{it}$ (3), the paper states Conjecture 1 (sparse coupling): a flow decoupled in at least one direction, $J_{\eta_i \mu_j} J_{\mu_j \eta_i} = 0$, comes with $H_{\eta_i \mu_j} = 0$ for all pairs. Theorem 1, credited to Heins and Da Costa, says that if $J_{\eta_i \mu_j} = 0$ then $H_{\eta_i \mu_j} = 0$ if and only if $\sum_{t \in \eta_i^C} Q_{\eta_i t} H_{t \mu_j} = 0$ (5), from the expansion $J_{\eta_i \mu_j} = T_{\eta_i \eta_i} H_{\eta_i \mu_j} + \sum_{t \in \eta_i^C} Q_{\eta_i t} H_{t \mu_j}$, where $\eta_i^C$ is the set of all coordinates other than $\eta_i$. Definition 2 names the left side of (5) the blanket index of that entry and sums over $i$ and $j$ to obtain $\mathrm{Ind}(J)$; a Markov blanket exists if and only if the index vanishes, and a weak Markov blanket exists only if it is small. Conjecture 2 (non-strict sparse coupling) asks that $H_{\eta_i \mu_j} = 0$ for most pairs at some timescale. Section 3 argues from the adiabatic theorem, explicitly as a sketch, that separation of timescales leaves many zero entries in $Q$. Section 4 argues that Hessian zeros suffice to detect blankets for polynomial surprisal (Lemma 1, Proposition 1, Lemma 2, Theorem 2). Section 5 bounds each term by $h$, sets $\mathrm{Ind}_{\max}(J) = k m h (n-1)$ for $k$ external and $m$ internal components (Lemma 3), and studies the normalized variable $X = \frac{1}{h(n-1)} \sum_{t \in \eta_i^C} Q_{\eta_i t} H_{t \mu_j}$ (8) under the assumptions collected in Remark 2. Section 6 extends the index to state-dependent $T$ (Proposition 2).

## Key results

Theorem 1 (page 5) is proved by a one-line rearrangement. Lemma 1 (page 8) asserts that a zero mixed second derivative of the surprisal in $(\eta_i, \mu_j)$ is equivalent to a Markov blanket. Proposition 1 (page 9) extends this to surprisal of polynomial degree $\nu$ under the explicit hypothesis that pairwise conditional independence implies joint conditional independence; Lemma 2 (page 10), called the tower contraction lemma, and Theorem 2 conclude that $\nu - 1$ vanishing Hessian entries give a blanket for a $\nu$-tensor. Lemma 3 (page 11) states that $|\mathrm{Ind}(J)/\mathrm{Ind}_{\max}(J)| \ll 1$ for almost all $J$ implies Conjecture 2. Theorem 3 (page 12) is the main result: under Remark 2 (a multiscale adiabatic system, $E[Q_{\eta_i t} H_{t \mu_j}] = E[Q_{\eta_i t}] E[H_{t \mu_j}]$ taken to be zero, terms independent across $t$ and bounded by $h$), the additive Chernoff bound gives $P(|X| > \varepsilon) < 2 e^{-\frac{1}{2}(n-1)\varepsilon^2}$ (9), and a union bound over the $km$ pairs gives $2km e^{-\frac{1}{2}(n-1)\varepsilon^2}$ (page 13). The paper concludes that the sparse coupling conjecture holds in the limit $n \to \infty$ and the non-strict version elsewhere. Corollary 1 relaxes independence with Janson's bound for partly dependent sums, dividing the exponent by the number $\chi$ of independent sets needed to cover the index set (10). Proposition 2 (page 14) gives the nonlinear index $\sum_t Q_{it}(x) H_{tj} - \sum_t \partial_j T_{it}(x) \partial_t U(x) + \sum_t \partial_{jt} T_{it}(x)$, and Theorem 4 claims that the concentration result carries over under a two-sided bound on the extra terms. The concentration inequalities are proved given their hypotheses; the hypotheses of Remark 2 and the adiabatic sparsity of Section 3 are argued informally; nothing is simulated.

## Limits

The author states that Remark 2 describes a particular class of complex systems and not generic physical systems, that Section 3 is a sketch, and in Section 7 that what is proved is relative blanketedness. My observations: the probability in Theorem 3 is taken over an assumed random ensemble of $(Q, H)$ entries with mean zero, introduced on page 12 as an ansatz, so the theorem does not concern any given dynamical system. A small normalized index still allows $|\sum_t Q_{\eta_i t} H_{t \mu_j}|$ of order $\varepsilon h (n-1)$, so by Theorem 1 the Hessian entry, which is the conditional dependence itself, is not shown to be small in absolute terms. The expansion in Theorem 1 writes the off-diagonal entries of $T = \Gamma - Q$ as entries of $Q$, which presumes a diagonal $\Gamma$. Lemma 1's proof inserts the conditioning variable by hand. The event in inequality (12) of Theorem 4 is empty as printed, and the proof of Theorem 3 cites a Proposition 3 that does not exist.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The paper bears on Markov blankets of individuals and collectives and on coarse-graining to meta-agents; it contains no connection, transport or bundle structure. It would supply a scalar diagnostic, the blanket index, which for a Gaussian steady state contracts solenoidal couplings against entries of the precision matrix, and a heuristic that approximate blankets become typical in high dimension. For a program that wants blankets around collectives, the useful content is the framing of a blanket as scale-dependent: page 7 describes strongly mixing subsystems with very weak blankets that form a cohesive whole at a larger scale, citing the spin glass active inference paper. The link is moderate in scope and its support is weak: the concentration theorem treats couplings as independent zero-mean random variables, so it does not show that any specified system of coupled agents has even a weak blanket, and it bounds a normalized index and not the conditional dependence. Reading the Hessian of surprisal here as a Fisher metric on a belief fiber would be interpretive; in the paper it is the Hessian of the steady-state surprisal over physical states.

## Cross-links

Concepts: [[Markov Blanket]]; [[Markov blanket interpretation debate]]; [[Bayesian mechanics]]; [[Nonequilibrium steady state]]; [[Coarse Graining]]; [[Meta-agents and hierarchical emergence]].

Related sources: [[heins-2022-sparse-coupling-markov]]; [[aguilera-2022-particular-physics]]; [[aguilera-2023-knitting-markov-blanket]]; [[friston-2021-stochastic-chaos-markov]]; [[friston-2022-very-particular-comment]]; [[friston-2019-particular-physics]]; [[sakthivadivel2022-bayesian-mechanics-geometry]]; [[heins-2023-spin-glass-active-inference]]; [[sakthivadivel-2026-markov-interacting-particles]]; [[sakthivadivel-2023-worked-example-classical-objects]]; [[friston-2012-fep-biological-systems]]; [[barp-2021-measure-preserving-diffusions]].

## BibTeX

```bibtex
@misc{sakthivadivel2022weak,
  author = {Sakthivadivel, Dalton A. R.},
  title = {Weak {M}arkov Blankets in High-Dimensional, Sparsely-Coupled Random Dynamical Systems},
  year = {2022},
  eprint = {2207.07620},
  archivePrefix = {arXiv},
  primaryClass = {math-ph},
  doi = {10.48550/arXiv.2207.07620},
  note = {arXiv v2, 14 August 2022}
}
```
