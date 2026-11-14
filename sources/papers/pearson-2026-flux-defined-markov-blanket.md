---
type: paper
title: "Does a Flux-Defined Markov Blanket Screen Self-Replicating Gray--Scott Spots? A Computational Test of a Blanket Condition from the Free Energy Principle"
aliases: ["Pearson 2026 flux defined markov blanket"]
authors: ["John E. Pearson"]
year: 2026
venue: "arXiv preprint (q-bio.NC); v1 19 Oct 2026, v2 24 Oct 2026"
arxiv: "2610.27235"
doi: "10.48550/arXiv.2610.27235"
url: "https://arxiv.org/abs/2610.27235"
version: "arXiv:2610.27235v2 [q-bio.NC], arXiv stamp 24 Oct 2026; the title page is dated October 27, 2026; 18 pages. The Electronic Supplementary Material cited throughout is not part of this PDF."
tags: [cluster/vfe, project/multi-agent, field/physics, field/statistics, field/neuroscience]
created: 2026-11-13
updated: 2026-11-13
---

# Does a Flux-Defined Markov Blanket Screen Self-Replicating Gray--Scott Spots? A Computational Test of a Blanket Condition from the Free Energy Principle

> [!info] Citation
> John E. Pearson (2026). *Does a Flux-Defined Markov Blanket Screen Self-Replicating Gray--Scott Spots? A Computational Test of a Blanket Condition from the Free Energy Principle*. arXiv preprint (q-bio.NC); v1 19 Oct 2026, v2 24 Oct 2026. [arXiv:2610.27235](https://arxiv.org/abs/2610.27235)

[Local PDF](../pdfs/pearson-2026-flux-defined-markov-blanket.pdf), 18 pages; retrieved November 13, 2026. Version read: arXiv:2610.27235v2 [q-bio.NC], arXiv stamp 24 Oct 2026; the title page is dated October 27, 2026; 18 pages. The Electronic Supplementary Material cited throughout is not part of this PDF. Reading basis: The first reader worked from the extracted text and did not see the typeset pages. I read the text of all 18 pages in full, including Tables 1 to 3 and the figure captions; the reference list (pp. 16 to 18) was skimmed. Equations 1 to 7 are simple in the extracted text and are reported from it; none was checked against a PDF page image. Table values are taken from the extracted text where the row and column assignment is clear. Figures 1 to 5 were not seen. The supplement (ESM) was not available, so every claim the paper supports by an ESM section is reported as the paper's statement only. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, 002, 003, 004, 005, 006, 007, 008, 009, 010, 011, 012, 013, 014, 015). Confirmed against those pages: 1, 2, 3, 4, 5, 6, 7; the two-sided data processing inequality (p. 5); Phi_X = -D_X integral of Laplacian X dA (p. 5). Parameters D_u, D_v, F, k and the 1024 x 1024 grid were checked. Table 1 values (marginal -0.233 to -0.244, partial -0.1815 to -0.1896, screened 37.7 to 40.2 percent), Table 2 (0.075, 0.130, 0.061; up 73, down 19 percent) and Table 3 (0.173 at w = 0, at most 0.005 from w = 24, placebo from 16 px) were checked. Also checked: rho median 0.032 over 93,684 transitions; autocorrelation lags 48, 62, 61, 58; KL remainder median 0.010; r = 0.934 over 689 divisions. Title, author, the date October 27, 2026 and the arXiv v2 stamp of 24 Oct 2026 match.

## TL;DR

A numerical test of the conditional independence condition of a Markov blanket on self-replicating spots in the chaotic regime of the Gray-Scott reaction-diffusion model. With the blanket taken to be the net diffusive flux across each spot's boundary, coarse interior and exterior states are not screened: flux removes about 38 to 40 percent of the linear shared variance and raises the nonlinear conditional mutual information, which the author attributes to flux acting as a collider. A band of surrounding field about one spot radius thick does screen, but so does the same band around placebo disks containing no spot, so the author reads this as a property of a short-range field and not as evidence of inference.

## Problem & setting

The free energy principle holds that systems coupled by short-range forces generically have a Markov blanket, $p(\mu,\eta|s,a) = p(\mu|s,a)p(\eta|s,a)$ (Eq. 1), and that given a steady-state density, a blanket and a synchronization map, internal states can be read as inferring external states (Friston 2013; Friston et al. 2023). Critics have argued that blankets can be imposed after the fact (Raja et al. 2021), that they are not generic in weakly coupled linear stochastic systems (Aguilera et al. 2022), and that statistical and dynamical blankets are conflated (Bruineberg et al. 2022). The author notes that no direct test exists in a nonlinear, spatially extended, many-body system and supplies one. The system is the Gray-Scott model with the autocatalytic step $U + 2V \to 3V$ in the spot-splitting chaotic regime of Pearson (1993), simulated deterministically on a periodic square. Spots are individuated geometrically by thresholding, watershed and merging. Samples from one long trajectory and from ensembles of perturbed realizations are treated as draws from a stationary distribution, an ergodicity assumption the author says cannot be proved.

## Method

The fields obey $\partial_t u = D_u\nabla^2 u - uv^2 + F(1-u)$ and $\partial_t v = D_v\nabla^2 v + uv^2 - (F+k)v$ (Eqs. 2 and 3), with $D_u = 2\times 10^{-5}$, $D_v = 10^{-5}$, $F = 0.018$ and $k = 0.055$, on a $1024\times 1024$ pseudo-spectral grid. For each organism-instance the interior state $I$ is the mean $v$ in a shrunken core, the exterior state $E$ is the mean $v$ in a ring 24 pixels wide just outside the boundary, and the blanket state is the pair of net diffusive fluxes $B = (\Phi_u,\Phi_v)$ with $\Phi_X = -D_X\int_\Omega\nabla^2 X dA$ (Section 3.2). Three blanket criteria are tested: timescale separation (A), a directed sensory and active asymmetry (B), and conditional independence $I \perp E \mid B$ (C), which the author treats as the decisive one. Criterion C is tested linearly through the partial correlation of the residuals of $I$ and $E$ after regression on the leading principal component of the standardized flux pair (Eq. 5), and nonlinearly through the conditional mutual information $\mathrm{MI}(X;Y|Z) = \iiint p(x,y,z)\ln[p(x,y|z)/(p(x|z)p(y|z))] dx dy dz$ (Eq. 4), estimated with the Frenzel-Pompe nearest-neighbor estimator ($k_{NN} = 5$) and compared with local-permutation nulls. The coarse-graining to $I$ and $E$ is justified by a two-sided data processing inequality, $\mathrm{MI}(X;Y|Z) \ge \mathrm{MI}(F(X);G(Y)|Z)$, so that a positive value is a lower bound for finer descriptions with fixed masks. As an exploratory control, Section 5 computes a template-deviation proxy (Eq. 6) and a linear-Gaussian variational free energy $\mathcal{F} = \mathrm{KL}(q(s)\|p(s)) - E_{q(s)}[\log p(o|s)]$ (Eq. 7) with hidden state $s := E$, observation $o := (\Phi_u,\Phi_v)$ and $q(s|I)$ a Gaussian whose mean is a regression of $E$ on $I$.

## Key results

All results are numerical and nothing is proved. Criterion A (Section 3.1, p. 5): over 93,684 transitions the median of $\rho = v_{cntr}\tau/R$ is 0.032, so a spot moves about 3 percent of its radius per relaxation time; the flux autocorrelation times (about 61 and 58 time units) exceed that of $I$ (48) and not that of $E$ (62), so the strict criterion is left unresolved. Criterion B (Section 3.2, p. 5): $\Phi_u < 0$ and $\Phi_v > 0$ in all of about 96,000 instances, which the author discounts as nearly a consequence of the segmentation. Criterion C, linear (Table 1, p. 6): the marginal correlation is $-0.233$ to $-0.244$ and the partial correlation $-0.1815$ to $-0.1896$ across three ensembles and one trajectory, so flux screens 37.7 to 40.2 percent of the shared variance. Criterion C, nonlinear (Table 2, p. 7): the marginal $\mathrm{MI}(I;E)$ is $0.075 \pm 0.002$ nats; given flux it is $0.130 \pm 0.001$ (up 73 percent, 21 to 32 null standard deviations above the null in individual subsamples); given the boundary concentration $(u_\partial,v_\partial)$ it is $0.061 \pm 0.002$ (down 19 percent). The collider structure $I \to \Phi \leftarrow E$ is argued from the dependence of diffusive flux on both sides of the boundary and supported by the opposite directions of these two conditionings (p. 7). Five alternative explanations are reported as checked and rejected (Section 3.3.3), and a threshold-based individuation reproduces the sign with a smaller linear magnitude (Section 3.3.4, pp. 8 to 9). The partial correlation is negative at every distance out to about 20 radii and concentrated within one radius (Section 3.4). Conditioning on flux plus summaries of a field band of width $w$ lowers the dependence between the interior and the shell beyond the band from 0.173 nats at $w = 0$ to at most 0.005 nats from $w = 24$ pixels, about one radius; placebo disks screen from 16 pixels (Table 3, p. 10). In Section 5 (pp. 11 to 13) the Gaussian free energy equals $-\ln p(o)$ plus a small KL remainder (median 0.010 nats) and tracks the template proxy through 689 divisions ($r = 0.934$); the author states that this is not evidence of inference.

## Limits

The author lists the limits (Sections 4, 6.2 and 6.4): $I$ and $E$ are coarse summaries, so failure for them does not exclude a screening partition of the full state; the test is at a single instant, while a blanket may concern history; the dynamics are deterministic, while Friston's construction assumes a stochastic steady-state density; the segmentation boundaries are state dependent; ergodicity is supported only informally, and ensemble realizations remain correlated in organism count at the 3000-step burn-in; the study covers one parameter regime of one model. My observations: the data processing bound protects the choice of $I$ and $E$ but, as the author says, not the choice of $B$, and flux is a derived quantity and not a state variable, so the negative result concerns one operational blanket; much of the supporting evidence sits in a supplement that this PDF does not contain; the preprint is unrefereed.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The paper bears on how a Markov blanket should be operationalized for a spatially extended agent or a collective in the gauge-theoretic multi-agent model. Two findings carry over as constraints, not as theorems. First, a boundary variable that is a joint function of both sides (here a flux; by analogy a coupling or message term computed from the states of two agents) behaves as a collider, and conditioning on it can increase the dependence between the sides; a blanket candidate built from inter-agent coupling terms would face the same test. That analogy is interpretive. Second, screening by a thick band of the ambient field is generic under short-range coupling and occurs around regions that contain no organism, so approximate conditional independence at a coarse-grained boundary does not by itself identify an agent or a meta-agent. The construction of a well-behaved linear-Gaussian free energy that follows the life cycle with no inference in the dynamics parallels baltieri-2020-predictions-eye-beholder and is a caution for Gaussian-belief descriptions. The paper has no counterpart to statistical fibers, transport or the Fisher metric; its link is to the blanket and coarse-graining objects only, and the evidence comes from one deterministic model.

## Cross-links

Concepts: [[Markov Blanket]]; [[Markov blanket interpretation debate]]; [[Bayesian mechanics]]; [[Mutual information]]; [[Data processing inequality]]; [[Coarse Graining]]; [[Nonequilibrium steady state]]; [[Variational free energy]].

Related sources: [[friston-2013-life-as-we-know-it]]; [[friston-2023-fep-simpler]]; [[aguilera-2022-particular-physics]]; [[bruineberg-2022-emperors-markov-blankets]]; [[dacosta-2021-bayesian-mechanics]]; [[palacios-2020-hierarchical-markov-blankets]]; [[friston-2021-stochastic-chaos-markov]]; [[pearl-1988-probabilistic-reasoning-intelligent]]; [[sakthivadivel-2022-weak-markov-blankets]]; [[virgo-2022-sensorimotor-history-markov-blankets]]; [[baltieri-2020-predictions-eye-beholder]]; [[sakthivadivel-2026-markov-interacting-particles]].

## BibTeX

```bibtex
@misc{pearson2026flux,
  author = {Pearson, John E.},
  title = {Does a Flux-Defined {M}arkov Blanket Screen Self-Replicating {G}ray--{S}cott Spots? {A} Computational Test of a Blanket Condition from the Free Energy Principle},
  year = {2026},
  eprint = {2610.27235},
  archivePrefix = {arXiv},
  primaryClass = {q-bio.NC},
  doi = {10.48550/arXiv.2610.27235},
  note = {arXiv preprint, version 2}
}
```
