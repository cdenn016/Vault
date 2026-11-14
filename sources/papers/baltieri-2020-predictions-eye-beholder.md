---
type: paper
title: "Predictions in the eye of the beholder: an active inference account of Watt governors"
aliases: ["Baltieri et al. 2020 predictions eye beholder"]
authors: ["Manuel Baltieri", "Christopher L. Buckley", "Jelle Bruineberg"]
year: 2020
venue: "ALIFE 2020: The 2020 Conference on Artificial Life (MIT Press), pp. 121-129"
arxiv: "2006.11495"
doi: "10.1162/isal_a_00288"
url: "https://arxiv.org/abs/2006.11495"
version: "arXiv:2006.11495v2 [q-bio.NC], 26 Jun 2020; 9 pages. The ALIFE 2020 proceedings pagination and DOI are not printed on this PDF."
tags: [cluster/vfe, cluster/participatory/philosophy-of-mind, project/multi-agent, field/neuroscience, field/philosophy, field/cs-ml]
created: 2026-11-13
updated: 2026-11-13
---

# Predictions in the eye of the beholder: an active inference account of Watt governors

> [!info] Citation
> Manuel Baltieri, Christopher L. Buckley, Jelle Bruineberg (2020). *Predictions in the eye of the beholder: an active inference account of Watt governors*. ALIFE 2020: The 2020 Conference on Artificial Life (MIT Press), pp. 121-129. [arXiv:2006.11495](https://arxiv.org/abs/2006.11495) [DOI](https://doi.org/10.1162/isal_a_00288)

[Local PDF](../pdfs/baltieri-2020-predictions-eye-beholder.pdf), 9 pages; retrieved November 13, 2026. Version read: arXiv:2006.11495v2 [q-bio.NC], 26 Jun 2020; 9 pages. The ALIFE 2020 proceedings pagination and DOI are not printed on this PDF. Reading basis: The first reader worked from the extracted text and did not see the typeset pages. I read the text of all 9 pages in full, including footnotes; the reference list (pp. 7 to 9) was skimmed. Equations 6 to 16 are short and unambiguous in the extracted text and are reported from it; no equation was checked against a PDF page image. The first two lines of the linearized system (Eq. 5) are not reported because a sign could not be confirmed. Figure 1 was not seen. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, 002, 003, 004, 005, 006, 007). Confirmed against those pages: 3, 4, 5 (third line; the second line is printed with a plus sign before g sin^2(psi_0)/(l cos psi_0) Delta psi, and the note correctly does not report it), 6, 7, 8, 9, 10, 11, 12, 13, 14 (printed as pi_z = 1/I, then corrected in the text to k/I), 15, 16. Title, authors and the arXiv v2 stamp of 26 Jun 2020 match.

## TL;DR

The paper writes a linear-Gaussian active inference model whose action equation, under two assumptions (an overdamped generative model and a choice of constants), reproduces the linearized engine equation of a steam engine regulated by a Watt centrifugal governor. Because the governor is the standard example of a system without representations, the authors conclude that generative models are descriptions held by an observer and not internal representations of the system, and that admitting a description as prediction error minimization carries limited explanatory weight for cognition.

## Problem & setting

Predictive processing and active inference are often read as representationalist theories in which a system carries an internal generative model. Van Gelder (1995, 1998) used the Watt governor to argue that cognition may be better described by dynamical systems theory than by computation over representations. The authors ask whether the governor nonetheless admits an active inference description. They take the standard governor model of Pontryagin (1962), after Maxwell (1868) and Vyshnegradsky (1877), linearized near equilibrium, and reuse their earlier derivation of PID control as active inference with linear generative models (Baltieri and Buckley 2019). The free energy is the Laplace-encoded form of Friston (2008) and Buckley et al. (2017), with Gaussian fluctuations and generalized coordinates kept to first order. The stance is explicitly as-if, following McGregor (2017): the governor is treated as though it were an agent that stabilizes its observation, the flyball arm angle $\psi$, by acting on the steam valve, and the authors warn at the outset that this description should not be taken literally.

## Method

The coupled governor and engine reduce to three first-order equations in the arm angle $\psi$, its velocity and the flywheel speed $\omega$ (Eq. 3), with equilibrium $\cos\psi_0 = G/k$ and $n^2\omega_0^2 = g/(l\cos\psi_0)$ (Eq. 4). Linearization about equilibrium gives, for the engine, $\Delta\dot{\omega} = -(k\sin\psi_0/I)\Delta\psi$ (third line of Eq. 5). The generative model assigned to the governor is $\psi = x + z$ and $x' = -\alpha(x - \psi_0) + w$ (Eq. 6), with hidden state $x$, observation $\psi$, exogenous input $\psi_0$, convergence rate $\alpha$, and Gaussian terms $z \sim N(0,\sigma_z^2)$ and $w \sim N(0,\sigma_w^2)$. The Laplace-encoded free energy $F \approx -\ln P(\psi,x)$ evaluated at $x = \mu_x$ (Eq. 7) becomes $F \approx \frac{1}{2}[\pi_z(\psi - \mu_x)^2 + \pi_w(\mu_x' + \alpha(\mu_x - \psi_0))^2 - \ln(\pi_z\pi_w)]$ (Eq. 8), with precisions $\pi_z = 1/\sigma_z^2$ and $\pi_w = 1/\sigma_w^2$. Action is assumed to affect observations, $\psi = f(a)$ (Eq. 9). The recognition dynamics are the gradient descent $\dot{\tilde{\mu}}_x = \tilde{\mu}_x' - k_p\partial F/\partial\tilde{\mu}_x$ and $\dot{a} = -k_a\partial F/\partial a$ (Eq. 10), which at a point attractor give $\dot{\mu}_x = \mu_x' - k_p[-\pi_z(\psi - \mu_x) + \pi_w\alpha(\mu_x' + \alpha(\mu_x - \psi_0))]$ and $\dot{a} = -k_a(\partial\psi/\partial a)\pi_z(\psi - \mu_x)$ (Eq. 11). Assumption 1 takes $\alpha$ very large, so $\mu_x$ relaxes quickly to $\psi_0$ (Eq. 12) and $\dot{a} \approx -k_a(\partial\psi/\partial a)\pi_z(\psi - \psi_0)$ (Eq. 13). Assumption 2 sets $\pi_z = k/I$ (Eq. 14 and the sentence after it), $k_a = 1$ and $\partial\psi/\partial a = \sin\psi_0$ (Eq. 15), giving $\dot{a} \approx -(k\sin\psi_0/I)\Delta\psi$ (Eq. 16), which the authors identify with $\Delta\dot{\omega}$.

## Key results

The one formal result is a derivation, not a theorem: under Assumptions 1 and 2 the action update of the active inference model coincides with the linearized engine equation, Eq. 16 against the third line of Eq. 5 (pp. 4 to 5). It follows by direct calculation from the free energy of Eq. 8. No simulation is run and no numerical results are reported. In the overdamped limit the expected hidden state $\mu_x$ is eliminated, so the state-estimation half of the scheme leaves no trace in the final dynamics (p. 5). Footnote 1 (p. 3) justifies stabilizing $\psi$ instead of $\omega$ because $\psi$ is a single-valued monotonic function of $\omega$, and observes that the roles could be exchanged, with the engine treated as the agent and the governor as its environment. The remaining results are argued philosophically (Discussion and Conclusion, pp. 5 to 7). Looking for the generative model of Eq. 6 inside the governor is called a category mistake, because the uncertainties $w$ and $z$ and the choice $\alpha \gg 0$ are relative to an observer. Reading generative models as internal representations is described as an instance of Jaynes's mind projection fallacy. Virtually any system is said to admit a description as prediction error minimization, so that such a description has limited explanatory power for cognition by itself; this is argued from the governor and from the earlier PID result and is not proved. Active inference is granted instrumental value as a shared formal language linking the good regulator theorem, the internal model principle, perceptual control theory and Rosen's notion of entailment, with a further link to nonequilibrium thermodynamics. The authors also assert (p. 7) that the literature conflates realist and instrumentalist readings of Markov blankets and defer that case to later work.

## Limits

The correspondence covers only the engine equation for $\Delta\dot{\omega}$ in the linearized system; the flyball arm equations are treated as the environment and are not derived from the free energy. The match depends on identifications chosen for the purpose (measurement precision equal to $k/I$, $\partial\psi/\partial a$ equal to $\sin\psi_0$, unit learning rate), which the authors present as convenient. The generality claim rests on one example plus their earlier PID paper. My observations: the symbol $\phi$ denotes the spindle speed in Eq. 1 and the arm angular velocity in Eq. 3 and Table 1; and the identification of $\dot{a}$ with $\Delta\dot{\omega}$ equates the action variable with the engine speed deviation by stipulation, which is exactly the as-if step the paper discusses.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The paper is a caution addressed to any program that reads dynamics as inference, and it bears on how the gauge-theoretic multi-agent model should phrase claims about its agents. A linear system near a fixed point admits a Gaussian generative model, a quadratic free energy with precisions and a gradient flow, with the precisions fixed after the fact from mechanical constants ($\pi_z = k/I$). Gaussian beliefs with precision weighting and gradient descent on a free energy are therefore available as a redescription of an ordinary feedback regulator, so the presence of that structure does not by itself distinguish an inferring agent from a governor. Footnote 1, on exchanging agent and environment, parallels the internal and external symmetry noted in millidge-2021-mathematical-walkthrough-fep and bears on any assignment of which side of a boundary holds the beliefs. There is no geometry in the paper, so the link to transport, the Fisher metric, Hamiltonian belief dynamics and meta-agents is weak. Its use for the vault is as a worked reference case for the Markov blanket interpretation debate and for the difference between describing a system with a generative model and attributing one to it.

## Cross-links

Concepts: [[Markov blanket interpretation debate]]; [[Bayesian mechanics]]; [[Generative model]]; [[Variational free energy]]; [[Prediction error]]; [[Active Inference]]; [[Precision weighting]]; [[Laplace approximation]].

Related sources: [[bruineberg-2022-emperors-markov-blankets]]; [[buckley-2017-fep-mathematical-review]]; [[friston-2008-dem]]; [[friston-2010-free-energy-principle]]; [[ramstead-2019-enactive-inference]]; [[friston-2019-particular-physics]]; [[clark-2013-predictive-brains]]; [[hohwy-2013-predictive-mind]]; [[baltieri-2025-bayesian-internal-model-principle]]; [[virgo-2021-interpreting-dynamical-systems-bayesian]]; [[biehl-2023-interpreting-systems-pomdps]]; [[friston-2026-generative-modelling-nonequilibrium]]; [[pearson-2026-flux-defined-markov-blanket]].

## BibTeX

```bibtex
@inproceedings{baltieri2020predictions,
  author = {Baltieri, Manuel and Buckley, Christopher L. and Bruineberg, Jelle},
  title = {Predictions in the eye of the beholder: an active inference account of {W}att governors},
  booktitle = {ALIFE 2020: The 2020 Conference on Artificial Life},
  publisher = {MIT Press},
  pages = {121--129},
  year = {2020},
  doi = {10.1162/isal_a_00288},
  eprint = {2006.11495},
  archivePrefix = {arXiv},
  primaryClass = {q-bio.NC}
}
```
