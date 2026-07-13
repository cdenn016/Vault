---
type: concept
title: "Voter model"
aliases: ["Voter model", "Copy-a-neighbour dynamics", "Spatial conflict model", "Coalescing-walk duality"]
tags: [cluster/social-physics, project/social-physics]
status: draft
created: 2026-06-19
updated: 2026-07-13
---

# Voter model

## Definition

The **voter model** is the simplest interacting-particle system for binary agreement: each site of a graph holds one of two discrete states (say $\sigma_i \in \{0,1\}$, two "opinions" or two competing species), and the population evolves by the most elementary imitation rule imaginable — at random times a site copies the state of one randomly chosen neighbour. In the canonical update a site $i$ picks a uniform neighbour $j \in \partial i$ and sets $\sigma_i \to \sigma_j$. There is no confidence threshold, no preference for one state, no noise, and no inertia; the only ingredient is copy-a-neighbour imitation on a fixed interaction topology. The model was introduced by Clifford and Sudbury as a model of **spatial conflict** between two populations competing for territory ([[clifford-sudbury-1973-spatial-conflict]]), and its name and rigorous theory came shortly after from the probability literature ([[holley-liggett-1975-voter-model-ergodic]]). Because each update merely transfers an existing state, the global density of each opinion is conserved in expectation — the mean opinion is a martingale — so the long-run behaviour is driven entirely by fluctuations, not by any built-in drift. The central question is whether those fluctuations eventually drive the whole system to one opinion (**consensus**, or "fixation") or leave the two opinions mixed forever (**coexistence**).

The answer is a clean dimension-dependent dichotomy. On low-dimensional lattices ($d \le 2$) the system "clusters" and fixates at a single consensus opinion; on high-dimensional lattices ($d \ge 3$) it relaxes instead to a one-parameter family of nontrivial stationary states in which both opinions coexist, indexed by the conserved opinion density $\rho$. Holley and Liggett make this rigorous through a **duality with coalescing random walks**: tracing the genealogy of an opinion backward in time turns the forward voter dynamics into a system of random walkers that move and merge, so the probability that two sites agree equals the probability that two walks started at them eventually coalesce. Coalescence is governed by recurrence versus transience of the difference walk, which is exactly what flips at $d = 2$ — recurrent walks always meet (correlations build up, consensus), transient walks do not (incomplete coalescence, a continuum of extremal invariant measures $\nu_\rho$). On heterogeneous networks the lattice analysis breaks down: Sood and Redner show that the *plain* magnetization is no longer conserved and one must instead track a **degree-weighted** opinion density $\omega = \sum_k k\,P(k)\,n_k / \langle k\rangle$, in which variable the mean consensus time scales as $T_N \sim N\,\langle k\rangle^2/\langle k^2\rangle$, so that broad (scale-free) degree distributions with large second moment reach unanimity faster relative to their size, with high-degree hubs acting as effective opinion reservoirs ([[sood-redner-2005-voter-heterogeneous-graphs]]).

## Why it matters here

The voter model is the canonical binary-agreement baseline, but it is not a derived overdamped limit of the current gauge-VFE theory. The dated theorem-first record [[belief-inertia-2026-07-12-theorem-first-revision]] proves only a continuous Gaussian DeGroot subclass: fixed symmetric coupling under the primary unweighted product Fisher metric, or nonuniform reversible coupling under an additional $\rho$-weighted metric or equivalent agent-specific rates. Copy-a-neighbor imitation has a discrete state space, stochastic overwrite rule, martingale structure, and coalescing-walk duality absent from [[Multi-agent variational free energy]]. Concentrating attention on one source does not derive that process. The voter model is therefore a benchmark and structural analogy for consensus, coexistence, and topology-dependent timescales, not a corner already subsumed by the VFE descent.

The Clifford--Sudbury formulation and Holley--Liggett ergodic theory are foundational comparison targets. Their coalescing-walk duality is mathematical machinery for the voter process, not machinery inside the gauge-VFE functional. The Sood--Redner heterogeneous-graph result is adjacent network context: it shows how topology controls consensus time, a structural question also asked of the attention graph ([[Community detection and modularity]], [[Meta-agents and hierarchical emergence]]), but the equations differ. Coexistence, clustering, and topology dependence are analogies for [[Echo chambers and polarization]], [[Bounded confidence]], [[Renormalization-group flow of beliefs]], and [[Meta-entropy]]. Likewise, the absence of momentum in the voter model makes it a useful control for conditional kinetic claims, not proof that [[Hamiltonian belief dynamics]] fills a necessary gap.

## Details

The dynamics is fully specified by the elementary update $\sigma_i \to \sigma_j$ with $j \sim \mathrm{Uniform}(\partial i)$. Three structural facts organize everything. First, **conservation**: each event moves a state without creating or destroying it, so on a regular lattice the expected opinion density is invariant and the magnetization is a martingale; the dynamics has no drift and no built-in preference, so whatever order emerges comes from fluctuations and geometry alone ([[clifford-sudbury-1973-spatial-conflict]]). Second, **duality**: the genealogical reversal of the forward process is a system of coalescing random walks, and the equal-opinion probability for sites $x,y$ equals the coalescence probability of walks started at $x$ and $y$ ([[holley-liggett-1975-voter-model-ergodic]]). Because coalescence inherits the recurrence/transience of the difference walk, the long-run behaviour splits sharply at dimension two: for $d \le 2$ the walks are recurrent, walkers always eventually meet, two-point correlations grow without bound, the system clusters, and a single opinion fixates; for $d \ge 3$ the walks are transient, coalescence is incomplete, and there is a continuum of extremal translation-invariant stationary measures $\nu_\rho$ indexed by the conserved density $\rho$, each a genuine coexistence state. Holley and Liggett prove these $\nu_\rho$ are exactly the extremal invariant measures, closing the ergodic theory.

Third, **topology dependence beyond the lattice**. Sood and Redner observe that on a graph with degree distribution $P(k)$ the naive magnetization is *not* conserved — high-degree nodes are imitated and imitate at different rates — and the correct conserved order parameter is the degree-weighted density $\omega = \sum_k k\,P(k)\,n_k / \langle k\rangle$ ([[sood-redner-2005-voter-heterogeneous-graphs]]). In this variable the mean time to consensus on $N$ nodes obeys
$$ T_N \sim N\,\frac{\langle k\rangle^2}{\langle k^2\rangle}, $$
so heterogeneity enters through the moments of the degree distribution: scale-free networks with a heavy tail (large $\langle k^2\rangle$) reach unanimity faster relative to their size than regular lattices, with hubs serving as opinion reservoirs that anchor and propagate consensus. Network structure is likewise important for attention graphs, but this is a structural analogy rather than a shared equation. The three papers provide benchmarks at the levels of model definition, rigorous dimension-dependent behavior, and network-topology timescales; [[SocialPhysics]] does not currently derive their stochastic voter dynamics.

The three sources thus benchmark model definition, rigorous stochastic behavior, and network timescales. They do not furnish an overdamped recovery result for [[SocialPhysics]].

## Sources

- [[clifford-sudbury-1973-spatial-conflict]] — the founding "spatial conflict" formulation of copy-a-neighbour imitation; conserved magnetization and the consensus-versus-coexistence question.
- [[holley-liggett-1975-voter-model-ergodic]] — rigorous ergodic theory via coalescing-random-walk duality; the dimension-dependent dichotomy and the extremal invariant measures $\nu_\rho$.
- [[sood-redner-2005-voter-heterogeneous-graphs]] — voter model on networks; degree-weighted conserved density and consensus time controlled by the moments of the degree distribution.

## See also

- [[Opinion dynamics]] — the averaging-model family of which the voter model is the discrete, zero-confidence corner.
- [[Multi-agent variational free energy]] — the continuous Gaussian functional compared with, but not reduced to, copy-a-neighbor imitation.
- [[belief-inertia-2026-07-12-theorem-first-revision]] · [[Belief inertia]] — the current restricted theorem status and conditional kinetic postulate.
- [[Sociophysics]] · [[SocialPhysics]] — the broader programme and the founding project page.
- [[Echo chambers and polarization]] · [[Bounded confidence]] — the persistent-disagreement / coexistence phenomenology.
- [[Hamiltonian belief dynamics]] · [[Mass as Fisher information]] — the underdamped regime the memoryless voter model cannot reach.
- [[Community detection and modularity]] · [[Meta-agents and hierarchical emergence]] — network structure as a control parameter for consensus.
- [[Renormalization-group flow of beliefs]] · [[Meta-entropy]] — the multi-scale, connectivity-controlled view.
