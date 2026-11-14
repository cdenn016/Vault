---
type: paper
title: "Interpreting Dynamical Systems as Bayesian Reasoners"
aliases: ["Virgo et al. 2021 interpreting dynamical systems bayesian"]
authors: ["Nathaniel Virgo", "Martin Biehl", "Simon McGregor"]
year: 2021
venue: "Machine Learning and Principles and Practice of Knowledge Discovery in Databases (ECML PKDD 2021 workshops, incl. 2nd International Workshop on Active Inference, IWAI 2021), Communications in Computer and Information Science, Springer, pp. 726-762"
arxiv: "2112.13523"
doi: "10.1007/978-3-030-93736-2_52"
url: "https://arxiv.org/abs/2112.13523"
version: "arXiv:2112.13523v1 [cs.AI], 27 Dec 2021 (37 pages: main text pp. 1-9, references pp. 9-11, Appendices A-D pp. 12-37). This is the preprint of the chapter in the ECML PKDD 2021 workshop proceedings (IWAI 2021), pp. 726-762; the proceedings citation is not printed on the PDF."
tags: [cluster/vfe, project/multi-agent, field/cs-ml, field/mathematics, field/statistics]
created: 2026-11-13
updated: 2026-11-13
---

# Interpreting Dynamical Systems as Bayesian Reasoners

> [!info] Citation
> Nathaniel Virgo, Martin Biehl, Simon McGregor (2021). *Interpreting Dynamical Systems as Bayesian Reasoners*. Machine Learning and Principles and Practice of Knowledge Discovery in Databases (ECML PKDD 2021 workshops, incl. 2nd International Workshop on Active Inference, IWAI 2021), Communications in Computer and Information Science, Springer, pp. 726-762. [arXiv:2112.13523](https://arxiv.org/abs/2112.13523) [DOI](https://doi.org/10.1007/978-3-030-93736-2_52)

[Local PDF](../pdfs/virgo-2021-interpreting-dynamical-systems-bayesian.pdf), 37 pages; retrieved November 13, 2026. Version read: arXiv:2112.13523v1 [cs.AI], 27 Dec 2021 (37 pages: main text pp. 1-9, references pp. 9-11, Appendices A-D pp. 12-37). This is the preprint of the chapter in the ECML PKDD 2021 workshop proceedings (IWAI 2021), pp. 726-762; the proceedings citation is not printed on the PDF. Reading basis: Read in full from the extracted text: main text (pp. 1-9) and Appendices B, C and D (pp. 21-37). Appendix A (pp. 12-21), a tutorial on string diagrams and Markov categories that the authors say contains no original material, was skimmed. The first reader worked from the extracted text and did not see the typeset pages. The central definitions (eqs. 5 and 6) and Propositions 1 and 2 (eqs. 50, 55, 57, 64) are string diagrams that the extraction does not preserve; I report them through the authors' own discrete-case expansions, eqs. (44)-(46), (48) and (65)-(67), which are legible. Equations (73), (76), (78), (81), (82), (84) and (85) are also reported from the text. Equations (70), (72) and (75) are partly garbled and are not reproduced. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, page-004, page-005, page-008, page-022, page-023, page-024, page-026, page-028, page-029, page-030, page-031, page-032, page-033, page-034, page-036, page-037). Confirmed against those pages: (44) and (45) on p. 22; (48) and the triviality argument on p. 24; (50) as the equation that Proposition 1 refers to (p. 24); (55)/(57) as the subject of Proposition 2 (p. 26); (64) identified with Jacobs eq. 16 (p. 29); (66) and (67) on p. 30; (73) and (76) on p. 33, together with the 0.75/0.25 model (74); (78) on p. 34; (82) on p. 36; (84) and (85) on p. 36. Also checked: Definition 1 with gamma: Y x S -> P(Y), the subjectively-impossible-input discussion and the stochastic choice of posterior (p. 23), the dependence only on which transitions are possible (p. 23), the trivial-model remark (p. 8), Appendix B.3 on conjugate priors, the version stamp arXiv:2112.13523v1 [cs.AI] 27 Dec 2021, and the 37 pages.

## TL;DR

The paper defines, in the language of Markov categories, what it means for an input-driven stochastic machine to admit a consistent interpretation as performing Bayesian filtering or Bayesian inference: an interpretation map from machine states to beliefs over a hypothesized hidden variable, together with a model kernel, such that the machine's own update realizes Bayes' rule on those beliefs. The interpretation depends only on the machine's internal dynamics and not on the true environment, so no stationarity assumption is needed, and interpretations are in general not unique. In the deterministic inference case the definition coincides with Jacobs's string-diagram definition of a conjugate prior.

## Problem & setting

Active inference and Bayesian mechanics rest on the idea that the internal states of a physical system parametrize probability measures over external states. The paper asks when such a reading is appropriate, restricted to perception without action. It treats the matter as one of interpretation, in the spirit of Dennett's intentional stance, but ties the interpretation to the dynamics so that the existence of an interpretation of a given kind is a well-posed mathematical question. The standing setting is discrete time; a machine is a Markov kernel on a state space driven by inputs, thought of as part of a larger process (the Bayesian network of eq. 1) whose initial distribution is arbitrary. Beliefs update by exact Bayes' rule. The model belongs to the interpretation and need not match the true environment, so beliefs can be consistent and incorrect. The work builds on categorical probability (Cho and Jacobs, Fritz), on Jacobs's channel-based account of conjugate priors, on Biehl and Kanai's study of Dirichlet hyperparameter dynamics, and positions itself against the Bayesian-mechanics part of the free energy principle literature (Friston 2019, Parr et al. 2020, Da Costa et al. 2021).

## Method

Definition 1: a machine consists of measurable spaces $Y$ (states) and $S$ (inputs) and an update kernel $\gamma: Y \times S \to P(Y)$. An interpretation consists of an interpretation map $\psi_H: Y \to P(H)$, read as a function assigning to each state a belief over a hidden space $H$, together with a model; a machine with a chosen interpretation is called a reasoner. For filtering the model is a kernel $\kappa: H \to P(H \times S)$ giving the next hidden state and the emitted sensor value. Composing $\psi_H$ with $\kappa$ and marginalizing gives the reasoner's beliefs $\psi_{S,H'}$ about the next input and next hidden state (eq. 3) and $\psi_S$ about the next input (eq. 4). Definition 2 calls $(\psi_H, \kappa)$ a consistent Bayesian filtering interpretation when the string-diagram equation (5) holds, which for discrete spaces is eq. (44), $\psi_{S,H'}(h, s \mid y) \gamma(y' \mid y, s) = \psi_S(s \mid y) \gamma(y' \mid y, s) \psi_H(h \mid y')$ for all $s, h, y, y'$, equivalently eq. (45), $\gamma(y' \mid y, s) > 0 \Rightarrow \psi_{S,H'}(h, s \mid y) = \psi_S(s \mid y) \psi_H(h \mid y')$. Definition 3 is the special case of a static hidden parameter with model $\phi: H \to P(S)$ (inputs treated as independent and identically distributed); its discrete form is eq. (66), $\gamma(y' \mid s, y) > 0 \Rightarrow \psi_H(h \mid y) \phi(s \mid h) = \psi_S(s \mid y) \psi_H(h \mid y')$, to be compared term by term with $p(h) p(s \mid h) = p(s) p(h \mid s)$ (eq. 67). Appendix D proposes a dictionary with the free energy principle: internal states play the role of $Y$, sensory states the role of $S$, the model is $\phi(s \mid \eta) := p(s \mid \eta)$ from the stationary density (eq. 82), and the interpretation map is $\psi(\eta \mid \mu) := q_\mu(\eta) := \mathcal{N}(\eta; \sigma(\mu), \Sigma(\mu))$ (eq. 85) with synchronization map $\sigma(\mu) := f_E(f_M^{-1}(\mu))$ (eq. 84).

## Key results

Appendix B.1 (pp. 21-24) derives three consequences in the discrete case by direct argument. First, a subjectively impossible input ($\psi_S(s \mid y) = 0$) leaves the posterior unconstrained, and may even be followed by a stochastic choice of posterior. Second, whether an interpretation is consistent depends only on which transitions have nonzero probability, not on their values. Third, if $\gamma(y' \mid y, s) > 0$ for all $y, y', s$, then eq. (48) forces $\psi_H(h \mid y')$ to be independent of $y'$, so the machine admits only trivial interpretation maps; a nontrivial interpretation requires some transitions to be impossible. The authors say they expect analogous statements beyond the discrete case, without proof. Proposition 1 (p. 24) shows that for a deterministic machine Definition 2 is equivalent to a marginalized equation (50), and Proposition 2 (p. 26) shows that the iterated machine $\gamma^n$ followed by $\psi_H$ is a conditional of the reasoner's joint belief over $n$ inputs and the final hidden state (eqs. 55 and 57); both are proved by string-diagram reasoning valid in the general measure-theoretic setting, and the extension to stochastic machines is stated as an expectation. Appendix B.3 (pp. 28-30) shows that for deterministic machines the inference consistency condition, eq. (64), is exactly the definition of conjugate prior in Jacobs (eq. 16 there), so every conjugate pair with its hyperparameter update is a machine with a consistent inference interpretation. Appendix C (pp. 31-33) gives three examples: a three-state nondeterministic machine, a counting machine on $\mathbb{N}_+ \times \mathbb{N}_+$ interpreted with a Beta family, and a machine on $\mathbb{Z}$ tracking the difference of counts ($f_1(k, s) = k + s$, eq. 73) interpreted as choosing between two coin biases; eq. (76) shows that the map $g(i, j) = \delta_{i-j}$ intertwines the two dynamics, so the second interpretation pulls back to the first machine. That every machine has an interpretation with respect to a trivial model is asserted (p. 8). Appendix D (pp. 33-37) is explicitly informal: the authors call it preliminary observations, say of its comments on the machine kernel (p. 35) that none should be considered proven, and say that they do not know whether the free energy principle's kernel obeys any consistency equation.

## Limits

The authors restrict to discrete time, exact Bayesian updating and perception without action; approximate inference, smoothing and continuous time are left to future work. Interpretations are not unique and cannot be told apart from internal dynamics alone. The comparison with the free energy principle assumes the older structure in which external states act on internal states only through sensory states (eq. 78), which Da Costa et al. no longer assume, and the authors flag this. My observations: the triviality result implies that any discrete machine with full-support transition noise has no nontrivial exact interpretation, which bears on noisy models of the free energy principle type, but the paper states it for the discrete case only and does not draw that consequence; Proposition 2 covers deterministic machines only.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The paper addresses the identification on which the vault's model rests: an agent's state as a parametrized belief, a point in a statistical fiber. The interpretation map $\psi_H: Y \to P(H)$ is a map from state space into a space of probability measures, comparable to the synchronization-map construction and to a section of a statistical bundle. The comparison is interpretive: the paper has no manifold, metric or connection. What it would supply is a precise consistency requirement (exact Bayes under the system's own dynamics) that needs no steady state, and the observation that interpretations are non-unique and not fixed by the dynamics. That non-uniqueness is a freedom of description; reading it as a gauge-like freedom is my gloss, and the paper gives it no group structure. The pullback of an interpretation along a map of machines (eq. 76) is a small precedent for transferring beliefs under coarse-graining to meta-agents. The triviality result is a challenge: belief dynamics with everywhere-positive noise can count as Bayesian reasoning only in an approximate sense that the paper leaves undefined. The link is moderate for foundations and weak for transport, Fisher geometry and Hamiltonian dynamics.

## Cross-links

Concepts: [[Bayesian mechanics]]; [[Markov blanket interpretation debate]]; [[Bayesian Inference]]; [[Conjugate-Exponential Family]]; [[State space models]]; [[Recognition Density]]; [[Agents as fibre-bundle sections]]; [[Coarse Graining]].

Related sources: [[biehl-2023-interpreting-systems-pomdps]]; [[baltieri-2025-bayesian-internal-model-principle]]; [[smithe-2023-compositional-bayesian-brain]]; [[friston-2021-interesting-observations-fep]]; [[dacosta-2021-bayesian-mechanics]]; [[friston-2019-particular-physics]]; [[parr-2020-markov-blankets-thermodynamics]]; [[biehl-2021-technical-critique]]; [[aguilera-2022-particular-physics]]; [[rosas-2020-causal-blankets-algorithmic]]; [[fritz-2019-a-synthetic-approach-to-markov-kernels-conditional-independence-and-th]]; [[cho-2017-disintegration-and-bayesian-inversion-via-string-diagrams]].

## BibTeX

```bibtex
@inproceedings{virgo2021interpreting,
  author = {Virgo, Nathaniel and Biehl, Martin and McGregor, Simon},
  title = {Interpreting Dynamical Systems as {Bayesian} Reasoners},
  booktitle = {Machine Learning and Principles and Practice of Knowledge Discovery in Databases. ECML PKDD 2021 International Workshops},
  series = {Communications in Computer and Information Science},
  volume = {1524},
  pages = {726--762},
  publisher = {Springer},
  address = {Cham},
  year = {2021},
  doi = {10.1007/978-3-030-93736-2_52},
  eprint = {2112.13523},
  archivePrefix = {arXiv},
  primaryClass = {cs.AI}
}
```
