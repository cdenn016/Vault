---
type: paper
title: "Interpreting systems as solving POMDPs: a step towards a formal understanding of agency"
aliases: ["Biehl and Virgo 2023 interpreting systems pomdps"]
authors: ["Martin Biehl", "Nathaniel Virgo"]
year: 2023
venue: "Active Inference. IWAI 2022. Communications in Computer and Information Science, vol. 1721, Springer, Cham, pp. 16-31"
arxiv: "2209.01619"
doi: "10.1007/978-3-031-28719-0_2"
url: "https://arxiv.org/abs/2209.01619"
version: "arXiv:2209.01619v2 [cs.AI], stamped 11 Jul 2025 on the PDF (16 pages). This is the preprint of the IWAI 2022 proceedings chapter (Communications in Computer and Information Science 1721, pp. 16-31, Springer 2023); the proceedings citation is not printed on the PDF."
tags: [cluster/vfe, project/multi-agent, field/cs-ml, field/statistics, field/philosophy]
created: 2026-11-13
updated: 2026-11-13
---

# Interpreting systems as solving POMDPs: a step towards a formal understanding of agency

> [!info] Citation
> Martin Biehl, Nathaniel Virgo (2023). *Interpreting systems as solving POMDPs: a step towards a formal understanding of agency*. Active Inference. IWAI 2022. Communications in Computer and Information Science, vol. 1721, Springer, Cham, pp. 16-31. [arXiv:2209.01619](https://arxiv.org/abs/2209.01619) [DOI](https://doi.org/10.1007/978-3-031-28719-0_2)

[Local PDF](../pdfs/biehl-2023-interpreting-systems-pomdps.pdf), 16 pages; retrieved November 13, 2026. Version read: arXiv:2209.01619v2 [cs.AI], stamped 11 Jul 2025 on the PDF (16 pages). This is the preprint of the IWAI 2022 proceedings chapter (Communications in Computer and Information Science 1721, pp. 16-31, Springer 2023); the proceedings citation is not printed on the PDF. Reading basis: Read in full from the extracted text: main text pp. 1-9, references pp. 9-10, and Appendices A-D pp. 10-16, including the proof of Proposition 1 in Appendix B. The first reader worked from the extracted text and did not see the typeset pages. Equations (2), (3), (4), (5), (6), (7), (10), (11) and (14) are legible and unambiguous in the extracted text and are reported from it. Equation (1) is a string diagram that the extraction reduces to a list of wire labels; I did not see it and rely on the authors' statement that eq. (2) is the same condition in standard notation. Equations (22), (23) and (26) of the Sondik example are garbled in extraction and are not reproduced. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, page-004, page-005, page-006, page-007, page-008, page-009, page-010, page-011, page-012, page-013, page-014, page-015, page-016). Confirmed against those pages: (2) both sides as printed on p. 7; (3) belief update with denominator over h-bar, h-bar' on p. 7; (4) Bellman equation and (5) argmax policy on p. 8; (6) omega(m) = pi*(psi(m)) on p. 8; (7) in Proposition 1 on p. 9; (10) and (11) in Appendix A on p. 11; (14) subjective-possibility condition on p. 12. Also checked: Definitions 1-5 (pp. 6-8), the hypotheses of Proposition 1 and the p. 9 sentence on V-bar*, the Proposition 2 relabel in Appendix B (p. 11), the Appendix C threshold 0.1188 and the 'tedious to check but true' remark (pp. 13-14), Definition 7 using both kappa and beta (p. 16), footnote 3 and the conclusion on information state processes, and the version stamp arXiv:2209.01619v2 [cs.AI] 11 Jul 2025, 16 pages.

## TL;DR

The paper gives a formal definition of when a stochastic Moore machine can be consistently interpreted as solving a partially observable Markov decision process: an interpretation map must send machine states to beliefs over a hypothesized hidden state that update by exact Bayesian filtering under the machine's own kernel, and the machine's output must equal the POMDP-optimal action for the belief its state encodes. Proposition 1 shows that the encoded beliefs then obey the standard belief-state update, so the optimal value function and policy transfer to machine states. An agent is defined as a machine together with such an interpretation.

## Problem & setting

The question is under what circumstances a system can be said to have beliefs and goals, and how these relate to its physical state. The authors start from Dennett's intentional stance but replace the comparison of predictive performance across stances by a consistency check: given full knowledge of the system's dynamics, can meanings be assigned to its states so that they implement belief updating and optimal choice. Three commitments restrict the scope. The system is a stochastic Moore machine (inputs, a possibly stochastic internal state, and an output that is a deterministic function of the state). Beliefs are finitely supported probability distributions updated exactly by Bayes' rule. Goals and rationality are those of an infinite-horizon discounted POMDP. The hidden states and rewards belong to the interpretation and need no physical realization, and the interpretation depends only on the machine, not on its true environment, so an agent's beliefs can be consistent and wrong. The paper extends the consistent Bayesian filtering interpretations of Virgo, Biehl and McGregor (2021), uses standard POMDP theory (Kaelbling et al. 1998, Hauskrecht 2000, Sondik 1978), and contrasts itself with the free energy principle literature, where the model is derived from the actual external dynamics.

## Method

A machine is a triple $(M, I, \mu)$ with machine kernel $\mu: I \times M \to PM$ (Definition 1), and a stochastic Moore machine adds an output space $O$ and an expose function $\omega: M \to O$ (Definition 2). Definition 3 introduces a consistent Bayesian influenced filtering interpretation $(H, A, \psi, \alpha, \kappa)$: a hidden state space $H$, an action space $A$, an interpretation map $\psi: M \to PH$, an action function $\alpha: M \to A$, and a model kernel $\kappa: H \times A \to P(H \times I)$, subject to the consistency equation (2), required for all $m, m', h', i$: $\left(\sum_{h}\sum_{a} \kappa(h', i \mid h, a) \psi(h \mid m) \delta_{\alpha(m)}(a)\right) \mu(m' \mid i, m) = \psi(h' \mid m') \left(\sum_{h}\sum_{a}\sum_{h''} \kappa(h'', i \mid h, a) \psi(h \mid m) \delta_{\alpha(m)}(a)\right) \mu(m' \mid i, m)$. Equation (1) states the same condition as a string diagram. When $A$ has one element this reduces to the filtering interpretation of the 2021 paper. A POMDP is a tuple $(H, A, S, \kappa, r)$ (Definition 4) with belief update, eq. (3), $f(b, a, s)(h') = \sum_{h} \kappa(h', s \mid h, a) b(h) / \sum_{\bar h, \bar h'} \kappa(\bar h', s \mid \bar h, a) b(\bar h)$, an optimal value function solving the Bellman equation (4), $V^*(b) = \max_{a} \{ \sum_{h} b(h) r(h, a) + \gamma \sum_{s, h, h'} \kappa(h', s \mid h, a) b(h) V^*(f(b, a, s)) \}$, and an optimal policy $\pi^*$ given by the maximizing action (eq. 5). Definition 5 then says that a stochastic Moore machine $(M, I, O, \mu, \omega)$ has a consistent interpretation as a solution to a POMDP $(H, O, I, \kappa, r)$ with interpretation map $\psi$ when (i) $(H, O, \psi, \omega, \kappa)$ is a consistent influenced filtering interpretation of the machine part, the expose function playing the role of the action function, and (ii) $\omega(m) = \pi^*(\psi(m))$ (eq. 6). The machine never observes the rewards of the POMDP used to interpret it.

## Key results

Proposition 1 (p. 9, proof in Appendix B, pp. 11-12) is the one proved result: for a machine with a consistent interpretation as a POMDP solution, any $m, m'$ with $\mu(m' \mid i, m) > 0$, and any input $i$ that is subjectively possible in the sense of eq. (14), the encoded belief satisfies $\psi(h' \mid m') = f(\psi(m), \pi^*(\psi(m)), i)(h')$ (eq. 7). The proof divides eq. (2) by the transition probability and by the subjective probability of the input. From this the authors conclude, in one sentence without a separate proof (p. 9), that $\bar V^*(m) := V^*(\psi(m))$ is an optimal value function on machine states with optimal policy $\omega$. Appendix A (pp. 10-11) rewrites eq. (2) as $\psi(h' \mid m'(i, m)) = \psi_{H,I}(h', i \mid m) / \psi_I(i \mid m)$ (eq. 11) for subjectively possible inputs, and notes that transitions of zero probability impose no condition; Appendix B (p. 12) adds that a subjectively impossible input leaves the machine kernel unconstrained. Section 3 (p. 8) observes from the definitions that the standard belief-state solution, with state space $PH$, kernel $\delta_{f_{\pi^*}}$ and output $\pi^*$, is itself a stochastic Moore machine to which Definition 5 applies. Appendix C (pp. 13-14) gives one further example, a deterministic machine on $M = [0, 1]$ with two inputs and two outputs and an output threshold at 0.1188, built from the known solution of Sondik's two-state POMDP; its consistency is described as tedious to check but true and is asserted, not shown, and optimality of the policy is deferred to Sondik (1978). Three remarks are argued informally in the introduction (pp. 4-5): interpretations depend only on the machine and not on the environment; a machine with no outputs can carry an interpretation whose actions exist only inside the interpretation; and because $\psi$ need not be injective, an interpretation includes a coarse-graining of the internal state. The relation to the sufficient information state processes of Hauskrecht is conjectured (footnote 3 and conclusion) and left open. There are no simulations.

## Limits

The authors state that the definition covers stochastic Moore machines only, requires exact Bayesian updating (approximate inference of the free energy kind is out of scope), uses deterministic actions and a single notion of goal (discounted infinite-horizon reward), and is offered as one example of an agent definition, not a claim about living systems. Nothing is said about how many POMDP interpretations a machine admits or how to find one. My observations: the only worked example is verified by assertion; ties in the maximization of eq. (5) and degenerate rewards (for which condition (ii) is vacuous or ill-defined) are not discussed; Proposition 1 reappears in Appendix B under the label Proposition 2; and Definition 7 names the belief-MDP kernel both $\kappa$ and $\beta$.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The paper bears on the step where an agent's internal state is read as a belief. Its interpretation map $\psi: M \to PH$ is the same kind of object as a map from physical state to a point of a statistical fiber, and eq. (2) is a discrete-time, exact-Bayes condition that such a map must satisfy for the reading to be consistent. It supplies a criterion that needs no Markov blanket and no steady state, and it separates the agent's model from the true environment, which is the situation a multi-agent model with agent-specific frames presupposes. It also challenges belief dynamics that descend a variational free energy: those are approximate and fall outside the definition by the authors' own statement. The remark that non-injective interpretation maps coarse-grain the internal state points toward meta-agents but is one sentence. There is no geometry here (no Fisher metric, connection, or transport between agents) and nothing on collectives. The link is moderate for the foundations of belief ascription and absent for the gauge and information-geometric objects; the correspondence with statistical fibers is interpretive, not exact.

## Cross-links

Concepts: [[Bayesian mechanics]]; [[Markov blanket interpretation debate]]; [[Active Inference]]; [[Bayesian Inference]]; [[Free-energy principle active inference]]; [[Coarse Graining]]; [[Generative model]]; [[State space models]].

Related sources: [[virgo-2021-interpreting-dynamical-systems-bayesian]]; [[baltieri-2025-bayesian-internal-model-principle]]; [[dacosta-2021-bayesian-mechanics]]; [[friston-2019-particular-physics]]; [[friston-2013-life-as-we-know-it]]; [[friston-2023-fep-simpler]]; [[parr-2020-markov-blankets-thermodynamics]]; [[biehl-2021-technical-critique]]; [[friston-2015-active-inference-epistemic-value]].

## BibTeX

```bibtex
@inproceedings{biehl2023interpreting,
  author = {Biehl, Martin and Virgo, Nathaniel},
  title = {Interpreting Systems as Solving {POMDPs}: A Step Towards a Formal Understanding of Agency},
  booktitle = {Active Inference. IWAI 2022},
  series = {Communications in Computer and Information Science},
  volume = {1721},
  pages = {16--31},
  publisher = {Springer},
  address = {Cham},
  year = {2023},
  doi = {10.1007/978-3-031-28719-0_2},
  eprint = {2209.01619},
  archivePrefix = {arXiv},
  primaryClass = {cs.AI}
}
```
