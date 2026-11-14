---
type: concept
title: "Maximum entropy"
aliases:
  - "MaxEnt"
  - "Maximum-entropy principle"
  - "Maximum Entropy Principle"
  - "Principle of maximum entropy"
tags:
  - cluster/info-geometry
  - cluster/participatory
  - project/multi-agent
  - project/transformer
status: draft
created: 2026-06-21
updated: 2026-11-13
---

# Maximum entropy

## Definition

The maximum-entropy (MaxEnt) principle of Jaynes selects, among the probability distributions consistent with given constraints, typically expectation values of observables, the one of maximum Shannon entropy, as the least-biased assignment ([[jaynes-1957-information-statistical-mechanics]]). For expectation constraints $\langle J_k\rangle=C_k$ the solution has [[Exponential family|exponential-family]] form,

$$p(x)\propto\exp\Big\{-\sum_k\lambda_kJ_k(x)\Big\},$$

whose natural parameters are the Lagrange multipliers. This links the principle to statistical mechanics, to Bayesian inference and to entropic-dynamics derivations in which short-step transition probabilities come from constrained entropy maximization ([[johnson-2011-entropic-dynamics-measurement]]). Maximum caliber is the same principle applied to probabilities over trajectories.

## Details

Within the free energy literature an early link is an identity. Corollary 3 of [[friston-2012-fep-biological-systems|Friston 2012]] rearranges free energy as the negative entropy of the proposal density minus the expected log joint, so that minimizing it maximizes that entropy under the constraint of explaining sensory states. [[sakthivadivel2022-bayesian-mechanics-geometry|Sakthivadivel 2022]] states as theorems that approximate Bayesian inference is equivalent to entropy maximization under a constraint and that the constraints are a gauge degree of freedom.

[[sakthivadivel-2022-entropy-maximising-parallel-transport|The parallel-transport paper of the same author]] gives that gauge reading a bundle. Differentiating $p=e^{-\lambda J}$ gives $\partial_ip=-\lambda\partial_iJp$, the equation of a covariantly constant section for the connection $dJ$ on a principal bundle over state space whose structure group is the positive reals, and a change of constraints acts as $p\mapsto e^{-\lambda J'}p$ with $\lambda J\mapsto\lambda J'+\lambda J$. The connection is exact, so the bundle is flat and every holonomy is trivial, and the construction is restricted to stationary processes with gradient drift (see [[Parallel transport]]). The vault's note on that paper records that its invariance theorem establishes only that the transformed action has the same stationarity equation, and that the statement and proof of its transport formula disagree in sign and factor. An independent precedent is [[polettini-2012-nonequilibrium-thermodynamics-gauge|Polettini 2012]], where the gauge transformation is a change of prior, $\rho_i\to e^{-\varphi_i}\rho_i$, and relative entropy is minus the change of entropy under it, $\delta S=\langle\varphi\rangle_\rho=-S(\rho'\|\rho)$.

The path-space version, a duality between maximum caliber and free energy minimization, is claimed and not yet established. [[sakthivadivel-2022-regarding-flows-fep|Sakthivadivel's reply to Aguilera et al.]] sketches a constrained caliber functional with a time-dependent mean constraint and labels its positive claims conjectures. [[sakthivadivel-2023-worked-example-classical-objects|The worked example for classical objects]] recasts free energy minimization across a synchronization map as a maximum-entropy problem on internal states, and applies maximum caliber with a mean constraint (the Newtonian trajectory) and a vanishing-variance constraint to obtain a Gaussian path density that concentrates on the classical path at infinite precision. It adopts the name G-theory for the duality, states no theorems, and concedes that the derivation assumes that classical systems follow forces, so the physical law enters through the constraint. [[sakthivadivel-2022-functorial-statistical-physics|The functorial note]], an announcement with proof sketches, presents maximum caliber as a functorial field theory composing Gibbs-type kernels under a sewing law and calls the result a partial formalization.

## In this work

> [!note] Editorial: maximum entropy in the gauge-theoretic program
> The program meets maximum entropy in its exponential-family (Gaussian) beliefs and in its entropy-regularized attention weights, whose softmax form is a constrained entropy maximization with the temperature as multiplier, as the vault's note on [[jaynes-1957-information-statistical-mechanics|Jaynes 1957]] records. The gauge reading above is abelian and flat, over the state space of one system with fiber the line of density values; the program's fibers are manifolds of Gaussian beliefs, its group is nonabelian and its transport acts between agents, so the correspondence is an analogy and not a theorem. What carries over is the trivial sector, in which reweighting a density by $e^{-\lambda J'}$ is a change of reference potential. The claim that physical law can be read off from maximum-entropy inference is supported by these sources only in the weaker form in which the law is supplied as a constraint.

## Related

[[Exponential family]], [[Fisher information metric]], [[Variational free energy]], [[Bayesian mechanics]], [[Parallel transport]], [[Gauge transformation]], [[Process-space variational inference]], [[Entropy]], [[Participatory realism (it from bit)]]

## Sources

- [[jaynes-1957-information-statistical-mechanics]] — the maximum-entropy principle as inference under incomplete information.
- [[johnson-2011-entropic-dynamics-measurement]] — entropic dynamics, with transition probabilities from constrained maximum entropy.
- [[sakthivadivel2022-bayesian-mechanics-geometry]] — approximate Bayesian inference as constrained entropy maximization; constraints as gauge freedom.
- [[sakthivadivel-2022-entropy-maximising-parallel-transport]] — the constraint as flat connection $dJ$; the maximum-entropy density as covariantly constant section.
- [[polettini-2012-nonequilibrium-thermodynamics-gauge]] — change of prior as gauge transformation; relative entropy as minus the entropy shift.
- [[friston-2012-fep-biological-systems]] — Corollary 3, the identity linking free energy minimization to Jaynes's principle.
- [[sakthivadivel-2022-regarding-flows-fep]] — conjectural maximum caliber sketch with a time-dependent mean constraint.
- [[sakthivadivel-2023-worked-example-classical-objects]] — maximum caliber worked for a classical particle; G-theory named, law assumed in the constraint.
- [[sakthivadivel-2022-functorial-statistical-physics]] — announcement: maximum caliber as composition of Gibbs-type kernels with a sewing law.
