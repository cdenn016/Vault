---
type: concept
title: "Threshold models and complex contagion"
aliases:
  - "Threshold models"
  - "Complex contagion"
  - "Social contagion"
  - "Cascades and contagion"
tags:
  - cluster/social-physics
  - project/social-physics
status: stable
created: 2026-06-19
updated: 2026-07-13
---

# Threshold models and complex contagion

## Definition

**Threshold models** describe binary collective behavior — joining a riot, adopting an innovation, going on strike, registering for a service — through individual *adoption thresholds*: each person acts only once the fraction (or number) of others who have already acted exceeds their own threshold. Granovetter introduced this scheme to model collective action ([[granovetter-1978-threshold-models]]): writing $r(t)$ for the fraction who have acted by time $t$ and $F$ for the cumulative distribution of thresholds across the population, the aggregate trajectory iterates $r(t+1) = F(r(t))$ and settles at the fixed points $r^* = F(r^*)$, whose stability is governed by $F'(r^*)$. The signature, counterintuitive consequence is that two populations with almost identical *average* dispositions can produce radically different macro outcomes — total quiescence versus a full bandwagon — because the outcome depends on the entire *shape* of the threshold distribution, not its mean. A single individual whose threshold drops from four to three can be the difference between a cascade that recruits the whole crowd and one that stalls after a handful of actors, because the system sits near a tipping point where the stable equilibrium jumps discontinuously.

Placed on a network, the same rule becomes a model of cascades. In Watts's fractional-threshold formulation ([[watts-2002-global-cascades]]), each node adopts once the fraction of its *neighbors* who have adopted exceeds its individual threshold $\phi$, and the question is when a handful of seed adopters can ignite a global cascade that flips a finite fraction of the whole population. The analysis turns on *vulnerable* nodes — those that adopt if even a single neighbor does, i.e. nodes of degree $k \le \lfloor 1/\phi \rfloor$ — and a global cascade requires the subgraph of vulnerable nodes to percolate. This yields a *cascade window*: cascades occur only in an intermediate band of mean connectivity, bounded below by sparsity (the vulnerable cluster fails to span) and above by density (each node has so many neighbors that one seed cannot move its fraction past threshold), and inside the window the cascade-size distribution is bimodal — most seeds fizzle, a few go global.

The threshold rule sharpens into a qualitative distinction that Centola and Macy named ([[centola-macy-2007-complex-contagion]]). A *simple* contagion transmits through a single exposure — information, rumor, a pathogen — and behaves like an epidemic on the network. A *complex* contagion requires *reinforcement from multiple distinct sources* before an individual adopts, as costly, risky, or norm-laden behaviors do. For complex contagions the familiar "strength of weak ties" logic reverses: a long bridging tie that connects an ego to a single distant adopter delivers only one of the several independent confirmations adoption demands, so what carries a complex contagion across social distance is the *width* of a bridge — how many parallel ties span two communities — not its length. Clustering and redundancy, normally dismissed as inefficient for spreading, become the very structures that enable complex spread, while the random rewiring that accelerates simple contagion can stall complex contagion entirely. Centola's online network experiment confirmed this directly ([[centola-2010-online-experiment]]): a health behavior seeded into a clustered-lattice network spread *farther and faster* than the same behavior in a random network of identical average degree, because clustering supplies the repeated, overlapping reinforcement a complex contagion needs to push an ego across its threshold.

## Why it matters here

For the SocialPhysics program, threshold and complex-contagion models are discrete-choice benchmarks for the continuous belief dynamics in [[belief-inertia]]. Granovetter's threshold flip can motivate a comparison between social pull and explicit anchoring, but the VFE state has no binary adoption variable, hard threshold, irreversible transition, or hazard. Its current theorem establishes only fixed symmetric DeGroot under the primary unweighted Fisher flow, a standard nonuniform reversible transient under $G_\rho$ or agent-specific rates, and a restricted reversible anchored stationary equilibrium independent of the positive flow metric. It does not derive threshold cascades, persistent polarization, or distinct collective phases.

Complex contagion provides network-level comparison targets, not a tighter recovered mechanism. Row-normalized attention reallocates relative source weight and does not impose a quorum of distinct sources; a single source can dominate a row. The present theory therefore predicts neither Centola and Macy's wide-bridge condition nor Watts's cascade window. Testing those effects would require an explicit multi-source reinforcement statistic, adoption rule, and network intervention. [[Bounded confidence]] is likewise only a soft similarity analog, not a hard threshold. Clustering, cascade, and threshold models remain benchmarks against which such an extension could be evaluated.

## Details

Granovetter's equilibrium analysis is the cleanest statement of why aggregate behavior decouples from average disposition. The map $r(t+1) = F(r(t))$ has stable fixed points wherever $F$ crosses the diagonal from above ($F'(r^*) < 1$); shifting one person's threshold reshapes $F$ near the diagonal and can annihilate the intermediate unstable fixed point that was holding back a cascade, so the only surviving stable equilibrium leaps from a small participating fraction to near-unanimity. The mean of the threshold distribution can be held fixed across this transition — what changes is the density of $F$ in the neighborhood of the tipping point, which is why two crowds with the same "average radicalism" can diverge into quiescence and riot ([[granovetter-1978-threshold-models]]).

Watts lifts this to a random network and replaces global fractions with neighborhood fractions, which makes percolation of the vulnerable subgraph the controlling event ([[watts-2002-global-cascades]]). The cascade condition derives from a generating-function argument: a single seed ignites a system-spanning cascade only when the vulnerable cluster it touches percolates, and the boundary of that regime is set by a second-moment condition on the degree distribution weighted by the per-degree vulnerability $\rho_k$ (schematically $\sum_k k(k-1)\,P(k)\,\rho_k = \langle k \rangle$ at the upper edge of the window). Below the window the network is too sparse for the vulnerable cluster to span; above it each node is too well connected for one adopting neighbor to clear the fractional threshold, so individual influence is diluted away. Inside the window the same seed sometimes does nothing and sometimes flips a finite fraction of the whole — the bimodal cascade-size signature — which is the network-level expression of Granovetter's discontinuous jump.

Centola and Macy's contribution is to show that *what kind of contagion* you have determines *which topology* spreads it ([[centola-macy-2007-complex-contagion]]). With a threshold rule requiring $T \ge 2$ adopting neighbors, a single long-range shortcut — the very edge that accelerates a simple contagion or shrinks path length in a small-world graph — provides only one of the $T$ required signals and therefore cannot by itself seed a complex contagion in a new region. Propagation across clusters instead requires a *wide bridge*: several edges connecting the same pair of neighborhoods, so a foothold in the new region receives reinforcement from multiple sides at once. The redundancy and clustering that random rewiring destroys are exactly what complex contagion needs, which inverts the standard small-world prescription. Centola's randomized online experiment then isolates topology as the causal variable by holding the same individuals and the same average degree fixed and varying only the wiring ([[centola-2010-online-experiment]]): in the clustered condition an undecided ego receives adoption signals from multiple neighbors who *share* neighbors, so reinforcement accumulates and crosses the threshold; in the random condition the same number of signals arrive from socially distant, non-overlapping sources and rarely concentrate on any one ego. The measured adoption probability rose with the number of adopting neighbors — the empirical fingerprint of a threshold/complex-contagion rule rather than the per-contact independence of an epidemic — making this the cleanest demonstration that the topology favoring complex contagion is the opposite of the one favoring simple contagion. Read together, these four results trace a single arc: thresholds make collective outcomes discontinuous in the disposition distribution (Granovetter), networks turn that discontinuity into a connectivity-bounded cascade window (Watts), reinforcement requirements invert the role of network topology (Centola and Macy), and a controlled experiment confirms the inversion in real behavior (Centola). That arc is a core chapter of the [[Statistical physics of social systems and collective behavior]] theme this project builds on, and it furnishes the recovery targets against which the gauge-coupled VFE model's topology effects can be checked.

## Sources

- [[granovetter-1978-threshold-models]] — threshold models of collective action; the equilibrium $r^*=F(r^*)$ and why macro outcomes are not averages of individual dispositions.
- [[watts-2002-global-cascades]] — fractional-threshold cascades on random networks; vulnerable-node percolation and the cascade window in mean connectivity.
- [[centola-macy-2007-complex-contagion]] — simple versus complex contagion; the weakness of long ties and the wide-bridge requirement for reinforced spread.
- [[centola-2010-online-experiment]] — randomized network experiment showing a complex contagion spreads farther in clustered than in random networks of equal degree.

## See also

- [[Opinion dynamics]] — the continuous-belief models the threshold picture mirrors as a discrete-choice cousin.
- [[Echo chambers and polarization]] — clustering as both echo-chamber former and complex-contagion enabler.
- [[Bounded confidence]] — soft, graded selectivity contrasted with hard thresholds.
- [[Sociophysics]] · [[SocialPhysics]] — the broader program and founding project page.
- [[belief-inertia]] — supplies a restricted symmetric/reversible averaging correspondence; threshold and cascade models remain benchmarks.
- [[Multi-agent variational free energy]] — the functional whose coupling term supplies the reinforcement structure of complex contagion.
- [[Community detection and modularity]] · [[Meta-agents and hierarchical emergence]] — the clustered substructure that concentrates reinforcement.
