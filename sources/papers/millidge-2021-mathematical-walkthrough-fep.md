---
type: paper
title: "A Mathematical Walkthrough and Discussion of the Free Energy Principle"
aliases: ["Millidge et al. 2021 mathematical walkthrough fep"]
authors: ["Beren Millidge", "Anil Seth", "Christopher L. Buckley"]
year: 2021
venue: "arXiv preprint (cs.AI); v1 30 Aug 2021, v2 1 Oct 2021"
arxiv: "2108.13343"
doi: "10.48550/arXiv.2108.13343"
url: "https://arxiv.org/abs/2108.13343"
version: "arXiv:2108.13343v2 [cs.AI], arXiv stamp 1 Oct 2021; title page and running header dated 5th October, 2021; 34 pages."
tags: [cluster/vfe, cluster/info-geometry, project/multi-agent, field/neuroscience, field/cs-ml, field/physics]
created: 2026-11-13
updated: 2026-11-13
---

# A Mathematical Walkthrough and Discussion of the Free Energy Principle

> [!info] Citation
> Beren Millidge, Anil Seth, Christopher L. Buckley (2021). *A Mathematical Walkthrough and Discussion of the Free Energy Principle*. arXiv preprint (cs.AI); v1 30 Aug 2021, v2 1 Oct 2021. [arXiv:2108.13343](https://arxiv.org/abs/2108.13343)

[Local PDF](../pdfs/millidge-2021-mathematical-walkthrough-fep.pdf), 34 pages; retrieved November 13, 2026. Version read: arXiv:2108.13343v2 [cs.AI], arXiv stamp 1 Oct 2021; title page and running header dated 5th October, 2021; 34 pages. Reading basis: The first reader worked from the extracted text and did not see the typeset pages. I read the text of all 34 pages in full: main text pp. 1 to 23, Appendix 10 (pp. 28 to 34) and Mathematical Appendix 11.1 (p. 34); the reference list (pp. 23 to 27) was skimmed. No equation was checked against a PDF page image and no figure was seen (Figure 1 is known only through its extracted labels and caption). Equations reported in the note are those whose extracted form is unambiguous; equations whose extraction was doubtful are listed in open_points and not reported as fact. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, 007, 008, 009, 010, 012, 013, 014, 015, 016, 017, 018, 019, 020, 021, 028, 031, 032, 034). Confirmed against those pages: 1, 3, 4, 5, 6, 12, 13, 17, 18, 19, 20 (printed as = ln p*(i,s,a), so the sign clash with Eqs. 6 and 29 is in the paper), 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33; the unnumbered Section 10.4.2 display (p. 32) is printed with (Q_bb - Gamma_bb). Title, authors (Anil K Seth), arXiv v2 stamp 1 Oct 2021, title-page and header date 5th October 2021 all match.

## TL;DR

The paper is a tutorial rederivation of the free energy principle in the form of Friston's 2019 monograph: Langevin dynamics with a nonequilibrium steady state, the Helmholtz (Ao) decomposition, the Markov blanket factorization, the marginal flow lemma, the synchronization map $\sigma$ between conditional modes, and the free energy lemma under a Laplace-encoded variational density. Its appendix lists the assumptions each step needs and marks the contested ones, and concludes that the principle is an interpretation of already given dynamics whose inference reading is exact only for conditional modes under strong restrictions on solenoidal coupling and on $\sigma$.

## Problem & setting

The authors address the lack of an explicit, accessible derivation of the central claim of the free energy principle, the free energy lemma: that the internal states of any system with a Markov blanket at nonequilibrium steady state can be read as performing variational inference about external states. They follow the order of presentation of Friston (2019), with the condensed versions in Parr, Da Costa and Friston (2020) and Da Costa et al. (2021), and place the technical objections of Biehl, Pollock and Kanai (2020) and Aguilera et al. (2021) in footnotes and in Appendix 10. The standing assumptions (Section 2 and Appendix 10.1) are that the whole system obeys an autonomous Langevin equation with additive white Gaussian noise of constant, state-independent, diagonal covariance $2\Gamma$; that it is ergodic with a unique steady-state density $p^*(x)$ covering the external states as well; and that the state splits into external $e$, internal $i$, sensory $s$ and active $a$ states obeying a blanket factorization at steady state. The main text deliberately presents the argument in its most favorable form and defers criticism to the appendix.

## Method

Starting from $\dot{x} = f(x) + \omega$ (Eq. 1) with steady state $p^*$, the flow is written in Helmholtz form $f(x) = (\Gamma - Q)\nabla_x \ln p^*(x)$ (Eq. 3), where $\Gamma$ is the dissipative part and $Q = -Q^T$ the solenoidal part, both taken constant; Appendix 11.1 (Eq. 33) checks that this form is stationary under the Fokker-Planck equation. The blanket condition is $p^*(e,i,b) = p^*(e|b)p^*(i|b)p^*(b)$ with $b = (s,a)$ (Eq. 4). The marginal flow lemma, cited from Friston (2019) without proof, expresses the averaged flow of a subset of states as a Helmholtz flow on its marginal density plus solenoidal coupling terms; for autonomous states $\alpha = (a,i)$ it gives $f_\alpha(x) = (\Gamma_{\alpha\alpha} - Q_{\alpha\alpha})\nabla_\alpha \ln p^*(i,s,a)$ (Eq. 5). The surprisal of particular states decomposes as $-\ln p^*(i,s,a) = E_{p^*(e|i,s,a)}[-\ln p^*(i,s,a|e)] + D_{KL}[p^*(e|i,s,a)\|p(e)]$ (Eq. 6), read as inaccuracy plus complexity. Conditional modes $\mathbf{e}(b) = \arg\max_e p(e|b)$ and $\mathbf{i}(b) = \arg\max_i p(i|b)$ (Eq. 12) are linked by a map $\mathbf{e}(b) = \sigma(\mathbf{i}(b))$ (Eq. 13), so internal modes parametrize a density $q(e;\sigma(\mathbf{i}(b)))$ over external states. Section 5 attaches two Fisher metrics to internal states, an intrinsic one on densities over internal states (Eq. 17) and an extrinsic one on the parametrized densities over external states (Eq. 18), each defined as the second derivative of a KL divergence. Section 6 defines a particular free energy by stipulating $q(e|i,s,a) = p^*(e|i,s,a)$, so that the bound term vanishes and the autonomous flow reads $\dot{\alpha} = (\Gamma - Q)\nabla_\alpha F_{particular}(s,\alpha)$ (Eqs. 19 to 21). The chain rule applied to $\sigma$ (Eqs. 22 to 25), with a Laplace-encoded Gaussian $q$ (Eq. 26), gives the mode dynamics $\dot{\mathbf{i}} = (\Gamma_\sigma - Q_\sigma)\nabla_{\mathbf{i}} F$ (Eq. 27), where $\Gamma_\sigma - Q_\sigma$ is $\Gamma_e - Q_e$ multiplied on both sides by the inverse Jacobian of $\sigma$ (no transpose appears in the printed Eq. 25). Section 7 defines the expected free energy as ambiguity plus risk with the steady-state density as generative model (Eq. 31).

## Key results

No result is stated in a theorem environment; the paper reproduces arguments of Friston (2019) and refers to them by name as lemmas. First (Section 6, Eqs. 19 to 21, pp. 14 to 15): with the variational density set equal to the true conditional $p^*(e|i,s,a)$, the autonomous flow is a Helmholtz flow on the particular free energy; the authors themselves call this something of a mathematical trick, and for a general $q$ the relation is only approximate (unnumbered display, p. 15), an approximation they attribute to the external modeler and not to the system. Second (Eqs. 22 to 27, pp. 16 to 17): for conditional modes, given an invertible differentiable $\sigma$ and a Laplace-encoded Gaussian, the internal mode follows $\dot{\mathbf{i}} = (\Gamma_\sigma - Q_\sigma)\nabla_{\mathbf{i}}F$, presented as an exact correspondence with variational inference that holds for modes only; this is derived by chain rule, with the final identification of the gradient argued in two lines. Third (Section 7, Eqs. 28 to 32, pp. 18 to 19): active states descend only the inaccuracy term (Eq. 30), and the expected free energy $G$ upper-bounds the expected predictive surprisal with equality at steady state, from non-negativity of a KL divergence; the further claim that $G$ is a Lyapunov function of self-organizing dynamics is asserted, not derived. Fourth (Section 8, pp. 20 to 22): the principle is argued to be an interpretation that cannot be falsified, closer to one direction of Noether's theorem than to the principle of least action, with applicability as the real test; four core conditions are listed on p. 21. Fifth (Appendix 10, pp. 28 to 34): an itemized audit of assumptions. Appendix 10.3.1 separates functional from statistical connectivity. Appendix 10.3.2 argues that Eq. 27 as written needs solenoidal coupling that is block-diagonal across the partition, stronger than the blanket condition and than the constraints of Friston, Da Costa and Parr (2020), and that relaxing it adds terms orthogonal to the free energy gradient. Appendix 10.4.2 shows that computing $\dot{\mathbf{e}}(b)$ through the blanket flow yields a gradient on blanket states, different from the dynamics Eq. 25 assumes. Appendix 10.4.3 gives the average-flow reading and its costs; Appendix 10.4.4 proposes replacing the argmax by a KL-optimal statistic $\xi(b)$.

## Limits

The authors state that the assumptions are unlikely to hold for the biological systems of interest: ergodicity fails for path-dependent systems, the steady state must include the environment, the noise is white, additive and diagonal, and differentiability of $\sigma$ is doubtful because argmax maps are generally nondifferentiable (Appendices 10.1 to 10.4.5). They concede on p. 21 that the precise list of required assumptions is not entirely clear, and propose reading the principle as locally valid. My observations: the marginal flow lemma is quoted and not derived; the step from the Laplace density of Eq. 26 to $\partial F/\partial\mathbf{i} = \partial\ln p(\mathbf{i},b)/\partial\mathbf{i}$ is asserted; and as printed the sign conventions do not agree across equations (Eq. 20 gives $F_{particular} = \ln p^*(i,s,a)$ while Eqs. 6 and 29 use $-\ln p^*$; Appendix 10.4.2 writes $Q_{bb} - \Gamma_{bb}$ against $\Gamma - Q$ elsewhere). The page images (pp. 15 and 32) confirm both as printed.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> This is the most direct assumption ledger for the single-particle derivation that the vault's Bayesian mechanics page summarizes. For the gauge-theoretic multi-agent model it identifies what a Bayesian-mechanical reading would have to supply per agent: a joint steady state that includes the environment, a blanket factorization, block-diagonal solenoidal coupling for the exact lemma, and a smooth invertible synchronization map. The intrinsic and extrinsic Fisher geometries of Section 5 match the picture of an agent's internal state as a point on a statistical fiber of Gaussian beliefs, with the Laplace step supplying the Gaussian family; that correspondence is interpretive, since the paper treats one particle with no connection and no transport between agents. Appendix 10.3.2 treats relaxed solenoidal coupling as flow orthogonal to the free energy gradient that changes the path and rate of convergence while leaving the minimum in place; this bears on any identification of Hamiltonian belief dynamics or belief inertia with the solenoidal sector, because it is a statement about stationary flows and contains no mass or second-order term. Footnote 4, on the symmetry between internal and external states, is the nearest thing to a two-agent statement. The link to coarse-graining and meta-agents is weak.

## Cross-links

Concepts: [[Bayesian mechanics]]; [[Markov Blanket]]; [[Markov blanket interpretation debate]]; [[Nonequilibrium steady state]]; [[Variational free energy]]; [[Laplace approximation]]; [[Fisher information metric]]; [[Expected Free Energy]].

Related sources: [[friston-2019-particular-physics]]; [[dacosta-2021-bayesian-mechanics]]; [[parr-2020-markov-blankets-thermodynamics]]; [[aguilera-2022-particular-physics]]; [[biehl-2021-technical-critique]]; [[friston-2013-life-as-we-know-it]]; [[buckley-2017-fep-mathematical-review]]; [[friston-2021-interesting-observations-fep]]; [[friston-2012-free-energy-value-attractors]]; [[friston-2020-sentience-markovian-monism]]; [[ramstead-2022-notation-minima-comment]]; [[heins-2022-particular-flows-attracting-sets]].

## BibTeX

```bibtex
@misc{millidge2021walkthrough,
  author = {Millidge, Beren and Seth, Anil K. and Buckley, Christopher L.},
  title = {A Mathematical Walkthrough and Discussion of the Free Energy Principle},
  year = {2021},
  eprint = {2108.13343},
  archivePrefix = {arXiv},
  primaryClass = {cs.AI},
  doi = {10.48550/arXiv.2108.13343},
  note = {arXiv preprint, version 2}
}
```
