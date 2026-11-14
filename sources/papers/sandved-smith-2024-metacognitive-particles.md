---
type: paper
title: "Metacognitive particles, mental action and the sense of agency"
aliases: ["Sandved-Smith and Da Costa 2024 metacognitive particles"]
authors: ["Lars Sandved-Smith", "Lancelot Da Costa"]
year: 2024
venue: "arXiv preprint (q-bio.NC)"
arxiv: "2405.12941"
doi: "10.48550/arXiv.2405.12941"
url: "https://arxiv.org/abs/2405.12941"
version: "arXiv:2405.12941v2 [q-bio.NC], 14 June 2024, as stamped on page 1 of the PDF text."
tags: [cluster/vfe, cluster/participatory, cluster/participatory/consciousness, project/multi-agent, field/neuroscience, field/physics, field/philosophy]
created: 2026-11-13
updated: 2026-11-13
---

# Metacognitive particles, mental action and the sense of agency

> [!info] Citation
> Lars Sandved-Smith, Lancelot Da Costa (2024). *Metacognitive particles, mental action and the sense of agency*. arXiv preprint (q-bio.NC). [arXiv:2405.12941](https://arxiv.org/abs/2405.12941)

[Local PDF](../pdfs/sandved-smith-2024-metacognitive-particles.pdf), 13 pages; retrieved November 13, 2026. Version read: arXiv:2405.12941v2 [q-bio.NC], 14 June 2024, as stamped on page 1 of the PDF text. Reading basis: The first reader worked from the extracted text and did not see the typeset pages. I read all 13 pages of the text in full, including Appendix A and the reference list. No equation could be checked against a PDF page. The equations reported, namely (3), (7) to (16), (18), (20), (22) and the appendix systems (23) and (24), are legible and unambiguous in the extracted text, apart from the bold-face marking of most-likely paths, which the extraction flattens and which I restored from the surrounding definitions. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001 through page-013 (all 13)). Confirmed against those pages: (1), (2), (3), (5), (6), (7), (8), (9), (10), (11), (12), (13), (14), (15), (16), (17), (18), (19), (20), (21), (22), (23), (24); title-page metadata (title, two authors with equal-contribution footnote, arXiv:2405.12941v2 [q-bio.NC], 14 Jun 2024) confirmed.

## TL;DR

The paper defines a metacognitive particle, in the particular-partition language of the path-based free energy principle, as a cognitive particle in which one subset of internal paths parameterizes posterior beliefs about another subset of internal paths. It separates passive metacognition, where the higher level reads the lower level only through the particle's sensory paths, from active metacognition, where an internal Markov blanket with its own sensory and active paths lets the higher level act on the sufficient statistics of lower-level beliefs, and it proposes a joint belief over lower-level internal and active paths as a formal sense of agency. The contribution is definitional: no existence theorem, sufficient conditions or simulations are given.

## Problem & setting

The paper asks what metacognition, understood as beliefs about beliefs, looks like in the terms of statistical physics. The standing assumptions are those of the path-based free energy principle: the system obeys a Langevin equation $\dot{x} = f(x) + w$ (eq. 1), is partitioned as $x = (\eta, b, \mu)$ (eq. 2), and the boundary paths form a Markov blanket between external and internal paths, $\eta \perp \mu \mid b$ (eq. 3), with the blanket split into sensory and active paths $b = (s, a)$ and a sparse flow (eq. 6). A particle is called cognitive when a map from internal paths to beliefs exists such that the most likely internal path given blanket paths encodes the posterior over external paths (eq. 7). Remark 3.1 separates a particle, which only has a blanket over some period, from a cognitive particle, which has beliefs; earlier treatments took particles to be cognitive by definition. Strange particles are those whose active paths do not directly influence internal paths and whose blanket and internal fluctuations are negligible. The paper builds on the path-integral paper of Friston et al. (2023), Da Costa et al. (2021), Parr et al. (2020), a 2024 commentary by the same two authors, and the deep parametric active inference model of Sandved-Smith et al. (2021).

## Method

The construction is a sequence of sparsity patterns on the flow of a Langevin system together with belief assignments. A cognitive particle carries the map $\mu \mapsto Q_{\mu}(\eta)$ with $Q_{\boldsymbol{\mu}}(\eta) \triangleq P(\eta \mid s, a)$ at the most likely internal path $\boldsymbol{\mu} = \arg\max_{\mu} P(\mu \mid s, a)$ (eq. 7). The passive example (Sect. 4, eq. 8) is a strange particle with $\mu = (\mu^{(1)}, \mu^{(2)})$ and flows $f_{\mu^{(1)}}(s, \mu)$ and $f_{\mu^{(2)}}(s, \mu^{(2)})$, with noise on external states only. The authors cite eq. 29 of the path-integral paper for the consequence that sensory paths form a blanket around the higher level, $(\mu^{(2)} \perp \eta, a, \mu^{(1)}) \mid s$ (eq. 9), which licenses the metacognitive belief $Q^{(2)}_{\boldsymbol{\mu}^{(2)}}(\eta, a, \mu^{(1)}) \triangleq P(\eta, a, \mu^{(1)} \mid s)$ (eq. 10) and its marginal over $\mu^{(1)}$ (eq. 12). Under the mean-field factorization $Q_{\mu}(\eta) = Q_{\mu^{(2)}}(\eta) Q_{\mu^{(1)}}(\eta)$ (eq. 11) this marginal is a belief about the parameters of a belief. The active case (Sect. 5, Appendix A eq. 23) nests a second particle with blanket $b^{(2)} = (s^{(2)}, a^{(2)})$ inside the first: the flow $f_{s^{(2)}}(\mu^{(1)}, b^{(2)})$ senses the lower level and $f_{\mu^{(1)}}(b^{(1)}, \mu^{(1)}, b^{(2)})$ receives the higher-level action. The lower level holds $Q_{\boldsymbol{\mu}^{(1)}}(\eta) \triangleq P(\eta \mid s^{(1)}, a^{(1)})$ (eq. 13) and the inner particle holds $Q_{\boldsymbol{\mu}^{(2)}}(\mu^{(1)}) \triangleq P(\mu^{(1)} \mid s^{(2)}, a^{(2)})$ (eq. 14). With a Gaussian lower belief $Q_{\mu^{(1)}}(\eta) = \mathcal{N}(\eta; m, \Pi)$ (eq. 15), the inner particle holds beliefs about the mean and precision, and its active paths can modulate them, which the authors read as mental action and as a proxy for attention.

## Key results

Nothing in the paper is stated as a theorem or proposition; the results are definitions with supporting argument. The typology (Sects. 3.2, 5 and 7, pp. 4 to 9) distinguishes cognitive from metacognitive particles, passive from active metacognition, and comprehensive from partial metacognition, where comprehensive means that the higher level holds beliefs about all sufficient statistics of the lower-level belief. The conditional independence in eq. 9 (p. 5) is taken from the path-integral paper and not re-derived. For strange nested particles (Appendix eq. 24, which removes the dependence of $f_{\mu^{(1)}}$ on $a^{(1)}$ and all noise on particular paths) the lower level infers its own action, $Q_{\boldsymbol{\mu}^{(1)}}(\eta, a^{(1)}) \triangleq P(\eta, a^{(1)} \mid s^{(1)})$ (eq. 16), and the sense of agency is defined as $Q_{\mu^{(2)}}(\mu^{(1)}, a^{(1)}) \triangleq Q_{\mu^{(2)}}(\mu^{(1)}) Q_{\mu^{(1)}}(a^{(1)})$, which at the most likely paths is approximately $P(a^{(1)}, \mu^{(1)} \mid s^{(2)}, a^{(2)})$ (eq. 18, p. 8), with its strength measured by the mutual information $D_{KL}[Q_{\mu^{(2)}}(\mu^{(1)}, a^{(1)}) \mid Q_{\mu^{(2)}}(\mu^{(1)}) Q_{\mu^{(2)}}(a^{(1)})]$ (eq. 20). The claim that a strange particle without metacognition cannot hold such a belief is argued from the absence of any belief over $\mu^{(1)}$. Section 7 extends the nesting to $N$ levels. Section 8.1 (pp. 9 to 10) argues informally that the number of levels stays finite through the complexity cost of free energy minimization, conjectures an innermost cognitive core whose internal paths are never the target of further beliefs, and writes the belief of that core as $Q_{\mu^{(N)}}(\eta, \mu^{(1)}, \ldots, \mu^{(N-1)}) \triangleq Q_{\mu^{(1)}}(\eta) \prod_{n=2}^{N} Q_{\mu^{(n)}}(\mu^{(n-1)})$ (eq. 22). Section 8.4 states an untested empirical prediction that eq. 20 correlates with behavior in a control-detection task. There are no simulations.

## Limits

The authors state (Sect. 8.2, p. 10) that the exact conditions on the dynamics under which these beliefs exist are not determined here and are left to future work, as are numerical simulations; existence is asserted for a wide class of particles by reference to earlier papers. The finiteness of nesting is an informal complexity argument and the cognitive core is labeled a conjecture. My observations: the approximate equality in eq. 18 is not derived, and the product on its left is a joint only because the second factor is indexed by $\mu^{(1)}$; Sect. 3.2 says passive higher-level paths influence the lower level only through shared blanket paths, whereas eq. 8 and the text of Sect. 4 let $\mu^{(2)}$ enter $f_{\mu^{(1)}}$ directly; the blanket condition is imposed on whole paths, so nothing is claimed about same-time conditional independence.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The paper informs the hierarchical side of the gauge-theoretic multi-agent model. It is a worked statement of what it means for one blanketed subsystem to hold beliefs about the sufficient statistics of another subsystem's Gaussian belief (eq. 15), with the higher level acting on the lower level's precision. That is the same formal relation a meta-agent would bear to its constituents if its belief were placed over their fiber coordinates $(\mu, \Sigma)$, and the product form of eq. 22 is the factorized belief of the innermost level of such a stack. The correspondence is interpretive. Here the nesting runs inward, a particle inside a particle within one organism, whereas a meta-agent is obtained by coarse-graining many peers; the paper has no transport between levels beyond a sensory map, no connection, no metric and no dynamics for the beliefs. What it would supply is vocabulary and a set of sparsity patterns (eqs. 8, 23 and 24) for an internal blanket. What it would challenge is any assumption that a level can represent itself completely, since the innermost level is argued to be opaque to further belief. The link to Markov blankets of collectives is moderate, and the link to gauge transport, the Fisher metric and Hamiltonian dynamics is absent.

## Cross-links

Concepts: [[Bayesian mechanics]]; [[Markov Blanket]]; [[Metacognition]]; [[Hierarchical generative model]]; [[Meta-agents and hierarchical emergence]]; [[Precision weighting]]; [[Self-Consciousness]].

Related sources: [[friston-2023-path-integrals-particular]]; [[friston-2023-fep-simpler]]; [[dacosta-2021-bayesian-mechanics]]; [[parr-2020-markov-blankets-thermodynamics]]; [[friston-2019-particular-physics]]; [[palacios-2020-hierarchical-markov-blankets]]; [[fields-2024-principled-limitations-on-self-representation-for-generic-physical-systems]]; [[sengupta-2016-neuronal-gauge]]; [[friston-2020-sentience-markovian-monism]].

## BibTeX

```bibtex
@misc{sandvedsmith2024metacognitive,
  title = {Metacognitive particles, mental action and the sense of agency},
  author = {Sandved-Smith, Lars and Da Costa, Lancelot},
  year = {2024},
  eprint = {2405.12941},
  archivePrefix = {arXiv},
  primaryClass = {q-bio.NC},
  doi = {10.48550/arXiv.2405.12941},
  note = {arXiv v2, 14 June 2024}
}
```
