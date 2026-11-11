---
type: concept
title: "Effective rank along relays"
aliases:
  - "Scale up, rank down conjecture"
  - "Rank of relayed content"
tags:
  - cluster/multi-agent
  - cluster/vfe
  - project/multi-agent
status: draft
created: 2026-11-11
updated: 2026-11-11
---

# Effective rank along relays

## Definition

A relay passes content through a sequence of receivers. Each receiver reads a code and moves its mean by a linear hop map, and the content that crosses $n$ hops is carried by the path product $A_n\cdots A_1$ of these maps. The effective rank of that content at a relative threshold $\mathsf f_{\mathrm{th}}\in(0,1)$ is the number of singular values of the path product that exceed $\mathsf f_{\mathrm{th}}$ times the largest one. When all receivers share a prior metric, a noiseless hop is the orthogonal projection $P_{V_j}$ onto the subspace $V_j$ of directions that the code transmits, and the common ground of a set of codes is $V_\cap=\bigcap_jV_j$, the directions that every code transmits.

The conjecture "Scale up, rank down" of the collective-agents manuscript, as recorded in [[dennis-2026-collective-agents-renormalization-results]], has two clauses. In relay networks with diversity of codes or frames the effective rank is nonincreasing in the hop distance when the codes share a direction, and it tends to the multiplicity of the top Lyapunov exponent of the path product when the singular values that belong to that exponent remain comparable, which generically gives rank one.

## Why it matters here

A collective that spans many hops can hold in common only what survives the path products across it, and two meta-agents that talk through their members exchange only what survives the hops between them. The rank of the surviving content is therefore a measure of abstraction: how much of a belief can be shared at a given scale (see [[Meta-agents and hierarchical emergence]]). The question for the program is which part of the statement that shared rank falls with scale is proved. In the cases treated so far the limit is proved, monotonicity is proved under a restriction, and monotonicity without the restriction is false.

## Details

### Fixed codes in a common metric

For fixed codes in a common metric, cyclic relays and relays in which every code recurs within a bounded number of hops converge geometrically to the projection $P_\cap$ onto the common ground. This is the theory of alternating projections ([[halperin-1962-product-projection-operators]], [[kayalar-1988-error-bounds-method]], [[badea-2012-rate-convergence-method]]). When $V_\cap\ne\{0\}$ every path product fixes $V_\cap$, so its largest singular value is one, and a projection cannot raise any singular value, $\sigma_k(P_VA)\le\sigma_k(A)$. The effective rank at a relative threshold is then nonincreasing in the hop distance, and its limit is $\dim V_\cap$ ([[dennis-2026-collective-agents-renormalization-results]]).

### Averaged meta-level hops

A hop between meta-agents can average several members' projections, $\bar P=\sum_j\mathsf w_jP_{V_j}$ with positive weights that sum to one. The map $\bar P$ is symmetric with $0\preceq\bar P\preceq I$, it fixes exactly $V_\cap$, and its rank is $\dim\sum_jV_j$, which is at least the largest rank of a member's code. Along a stationary relay of such hops the ratios of singular values are $(\lambda_k(\bar P)/\lambda_1(\bar P))^n$, so the effective rank at any relative threshold is nonincreasing, and $\Vert\bar P^n-P_\cap\Vert=\lambda_\ast^n$ with $\lambda_\ast<1$ the largest eigenvalue of $\bar P$ on the orthogonal complement of $V_\cap$. The conjecture therefore holds for stationary averaged relays in a common metric, with limiting rank $\dim V_\cap$ when the common ground is nonzero. The reading that meta-agents communicate at lower rank than their members fails at one hop: averaging parallel paths raises the rank before relay depth lowers it.

### Without a common direction

Monotonicity at a relative threshold fails when the codes share no direction. The manuscript gives three planes in $\mathbb R^3$, depending on a parameter $\mathsf o\in(0,1)$ and with no common direction, for which the path products after one, two and three hops have the nonzero singular values $(1,1)$, $(1,\mathsf o)$ and $(\mathsf o,\mathsf o)$. At every relative threshold in $(\mathsf o,1)$ the effective rank is $2$, then $1$, then $2$. A hop can shrink the largest singular value by more than the second, and the relative count then rises. In the cyclic continuation of this relay both nonzero singular values decay at the same exponential rate, $\frac23\ln\mathsf o$ per hop, while their ratio tends to zero like the inverse square of the number of cycles, so the effective rank is one from some hop on. That limit equals neither $\dim V_\cap$, which is zero, nor the multiplicity of the top Lyapunov exponent, which is two: the product over one cycle acts on the last plane as a Jordan block with a double eigenvalue. This is why the limit clause of the conjecture carries the condition that the singular values belonging to the top exponent remain comparable.

Two monotone statements survive without a common direction, for noiseless hops in a common metric. The singular values themselves do not increase along the relay, so the number of them above a fixed fraction of the largest singular value of the first hop, an absolute threshold, is nonincreasing. And the effective rank at a relative threshold is nonincreasing along stationary averaged relays, as above.

### Random hop maps

For independent, identically distributed hop maps with $\mathbb E\ln^+\Vert A_m\Vert<\infty$ the Lyapunov exponents $\Gamma_1\ge\Gamma_2\ge\cdots$ of the path product exist ([[furstenberg-1960-products-random-matrices]], [[oseledets-1968-multiplicative-ergodic-theorem]]), and the top exponent is simple for invertible maps whose generated semigroup is strongly irreducible and contracting ([[guivarc-h-1985-frontiere-furstenberg-proprietes]], [[gol-dsheid-1989-lyapunov-indices-product]]). The ratio of the second to the first singular value then decays like $e^{-n(\Gamma_1-\Gamma_2)}$, the content that survives many hops is one-dimensional, and $1/(\Gamma_1-\Gamma_2)$ is an abstraction length in hops. The manuscript cites these theorems at the level of their records and restatements, and the source notes in the vault have the same basis.

## What is not established

The limit clause of the conjecture is open for networks with many paths, where path products add and ranks can rise, for correlated or learned codes, for heterogeneous priors, where the contraction itself can fail, and for non-invertible pure relays that do not reduce to invertible factors of the code rank, such as relays whose code ranks differ along the path. No proof says how typical the failure of monotonicity is among relays without a common direction. All statements on this page concern linear maps and Gaussian beliefs.

## In this work

The results belong to the multi-agent line of the program ([[Gauge-Theoretic Multi-Agent VFE Model]]) and to the linear-Gaussian model of communicating agents of the collective-agents manuscript. They are not statements about the gauge-theoretic free-energy functional or its implementation. The related statement for codes aggregated across levels, that aggregate rank falls only along directions on which members' frames disagree and only under aggregation in public coordinates, is in the same manuscript section and is not recorded in the vault.

> [!note] Editorial: Rank and bit budgets
> The effective rank of a path product counts directions and is not a communication rate. The distinction drawn on [[Communication-constrained inference]] between the rank of an expression map and a bit budget applies here unchanged. This remark is the wiki's and is not made in the source.

## Sources

- [[dennis-2026-collective-agents-renormalization-results]]
- [[halperin-1962-product-projection-operators]]
- [[kayalar-1988-error-bounds-method]]
- [[badea-2012-rate-convergence-method]]
- [[furstenberg-1960-products-random-matrices]]
- [[oseledets-1968-multiplicative-ergodic-theorem]]
- [[guivarc-h-1985-frontiere-furstenberg-proprietes]]
- [[gol-dsheid-1989-lyapunov-indices-product]]

## See also

- [[Meta-agents and hierarchical emergence]]
- [[Approximate meta-agent theorem]]
- [[Communication-constrained inference]]
- [[Coarse Graining]]
- [[Renormalization group flow]]
- [[Collective agents literature map]]
