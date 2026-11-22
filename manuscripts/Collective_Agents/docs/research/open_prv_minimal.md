# Minimal provenance with identifiers (`open:prv-minimal`)

- Status: active
- Opened: 2026-11-21
- Updated: 2026-11-21
- Sessions: 1

## Target

- Locked statement: From `ext4_prv.tex` (`open:prv-minimal`, lines 113–115): "For $Q_x=0$ on a graph with cycles and an arbitrary schedule, \cref{prop:prv-clock} is exact with $n$ pairs per node. Determine the least storage of an exact protocol as a function of $n$ and of the cycle structure of $G$, and whether growth with $n$ is necessary."
- Falsifier: Any exact continuous protocol on $C_n$ (for $n \ge 10$) with $o(n)$ real numbers per node, or on $G_k$ (subdivided $K_{2,k}$ plus edge $uv$) with $o(k)$ real numbers per node, would refute the lower bounds; any counterexample schedule on a multi-block graph where the Block-Cut Channel Protocol deviates from $p(x_t \mid o_{D_v})$ would refute the upper bound.
- May assume: Live model of `ext4_prv.tex` (line 7) and `def:prv-protocol` (line 10): $Q_x = 0$, $x_{t+1} = A x_t$ with $A$ invertible (or exactness for $x_0$ for arbitrary $A$), $x_0 \sim \mathcal{N}(m_0, P_0)$ with $P_0 \succ 0$, connected graph $G = (V, E)$ on $n = |V|$ identified nodes, observations $o_{v,t} = H_v x_t + v_{v,t}$ with independent $v_{v,t} \sim \mathcal{N}(0, R_v)$, $R_v \succ 0$, and arbitrary finite schedules of observations and one-way reports $u \to v$ over links of $G$. For lower bounds, continuous (C2) or $C^1$ (C3) dependence of node states on continuous observation data for each fixed discrete schedule, and full-rank sensing $\rank H_v = d$ (generalizing directly to a shared $r$-dimensional subspace).
- Must not assume: Fixed or synchronous schedules, anonymous nodes, bounded number of observations per node, or that storage is measured without regularity (discontinuous set-theoretic bijections $\mathbb{R}^N \leftrightarrow \mathbb{R}$ trivialize real-number dimension).
- Alternative forms: Characterizing exact continuous storage up to constant factors on standard graph families ($C_n$, $K_n$, $K_{2,k}$, unicyclic graphs, cacti, bounded-block-size graphs) and establishing a sharp qualitative dichotomy for $O(1)$ vs unbounded growth with $n$ in terms of biconnected components (blocks), circumference $\operatorname{circ}(G)$, and maximum local vertex-connectivity $\theta(G)$.
- Test instance: (i) $G = C_8$ ($k = 6, m = 3, d = 1$): light-cone schedule yields an exact $3 \times 3$ grid with $4$-element active core, exact SymPy rank $4/4$, forcing $a_0 + a_7 \ge 4/3$ (and $\ge 4d/3$ in dimension $d$); (ii) cactus chain of $m$ triangles ($n = 2m + 1$): Block-Cut Channel Protocol uses at most $4$ extra pairs per node for all $n$ against $n$ pairs in `prop:prv-clock`.
- Out of scope: Process noise $Q_x \succ 0$ (`thm:prv-window`, `prop:prv-ledger`), model-aware encoders off schedule (`open:prv-aware`), hierarchies with distinct node variables (`open:prv-hierarchy`), and anonymous deterministic protocols (`thm:prv-cover`).
- Reading chosen: We measure provenance storage in continuous real numbers (and in Gaussian pairs of $d(d+3)/2$ real numbers for upper bounds, noting discrete counters separately) under `def:prv-protocol`, requiring continuity (for C2) or $C^1$ regularity (for C3) of state/message maps in the observation data for each fixed discrete schedule. Without continuity, any finite tuple of reals can be packed into one real number, which is the trivial reading we exclude (matching `rem:prv-cover-scope` and `thm:prv-window`).

## Conventions

| Key | Choice | Test value |
| --- | --- | --- |
| Gaussian pair | $(\Lambda, h)$ represents density $\propto \exp(h^\top x - \tfrac12 x^\top \Lambda x)$; size $d(d+3)/2$ reals | For $d=1$: pair $(2, 6)$ is $\mathcal{N}(3, \tfrac12)$; size is $2$ reals |
| Observation item ($Q_x=0$) | About $x_0$: $e_{v,t} = ((A^t)^\top \Lambda_v^{\mathrm o} A^t, (A^t)^\top H_v^\top R_v^{-1} o_{v,t})$ | For $d=1, A=2, H=1, R=1, t=1, o=3$: $e = (4, 6)$ |
| Information set & report | $D_v$ starts $\emptyset$; obs at $(v,t)$ adds $(v,t)$ to $D_v$; one-way report $u \to v$ sets $D_v \leftarrow D_u \cup D_v$ | After $o_{1,1}$, $1 \to 2$, $D_2 = \{(1,1)\}$, $D_1 = \{(1,1)\}$ |
| Exactness (`def:prv-protocol`) | After every event, node $v$ outputs $s_v = \pi_0 + \sum_{e \in D_v} e$ (about $x_0$, mapped by $A^t$ to $x_t$ for invertible $A$) | On $K_2$ with $\pi_0=(1,0)$, $e_1=(1,2)$, $e_2=(1,4)$: after $1\to 2$, $s_2=(3,6)$ |
| Graph invariants | $\operatorname{circ}(G)$ = length of longest simple cycle ($0$ on trees); $\theta(G) = \max_{u \ne v} \kappa_G(u, v)$; $b_{\max}(G) = \max_{B \in \mathcal{B}(G)} |V(B)|$ | On $K_{2,5}$: $\operatorname{circ}=4$, $\theta=5$, $b_{\max}=7$; on $C_6$: $\operatorname{circ}=6$, $\theta=2$, $b_{\max}=6$ |

## Claims

### C1: Block-Cut Channel Protocol (Exact Upper Bound)

- Statement: Let $Q_x = 0$, let $G = (V, E)$ be a connected graph whose $n$ nodes carry identifiers, and let $A$ be invertible (or take exactness for $x_0$ for arbitrary $A$). Decompose $G$ into its biconnected components (blocks) $\mathcal{B}(G)$. There is an exact provenance protocol under arbitrary schedules of observations and one-way reports that stores $1$ Gaussian pair per bridge link, $0$ state on non-bridge links, and at each node $v$ stores $\sum_{B \ni v,\, |V(B)| \ge 3} (|V(B)| - 1)$ extra pairs and $\sum_{B \ni v,\, |V(B)| \ge 3} |V(B)|$ integer counters beyond its output pair $s_v$. In particular, on trees it reduces identically to `thm:prv-tree`(a) ($0$ extra node pairs, $1$ pair per link), on any 2-connected graph it uses $n - 1$ extra pairs per node, and on any family with bounded maximum block size $b_{\max}(G) = O(1)$ and bounded 2-connected block-degree per vertex it uses $O(1)$ pairs per node and per link independent of $n$.
- Status: proved
- Review: fresh-context
- Check: verifier (swarm #17), 2026-11-21, fresh-context reconstruction + independent 1,000-event simulation on 10-node 3-block/2-bridge graph (max error `6.22e-15`), no defect located.
- Evidence: Complete derivation in `open_prv_minimal.md` (Section "Derivations", Proof of C1) and cleaned write-up; two-channel verification in `open_prv_minimal-checks/verify_prv_minimal.py` (`open_prv_minimal-checks/verify_prv_minimal_stdout.txt`): max error vs information-form sum $\le 6.04 \times 10^{-14}$ (Channel A) and vs batch covariance-form Gaussian conditioning $\le 1.21 \times 10^{-10}$ (Channel B) across 5 multi-block graphs (`tree_8`, `unicyclic_C4_tree`, `barbell_K4`, `cactus_3tri`, `multi_block`), exact storage counts verified, plus two planted-error negative controls failing with errors $3.89 \times 10^1$ and $4.67 \times 10^1$.
- Depends on: none

### C2: Cycle Circumference Lower Bound for Continuous Protocols

- Statement: Let $Q_x = 0$ and $A$ be invertible, and let $G = (V, E)$ be a connected graph containing a simple cycle $C$ of length $\ell \ge 6$ on which every vertex $v \in V(C)$ has sensing matrix $H_v$ of rank $d$. Consider any exact provenance protocol (`def:prv-protocol`, even with a shared global clock and unbounded link storage) in which, for each fixed discrete schedule, node states lie in Euclidean spaces $\mathbb{R}^{a_v}$ (plus arbitrary discrete metadata) and depend continuously on the observation data. Set $k = \ell - 2$ and $m = \lfloor k/2 \rfloor = \lfloor (\ell - 2)/2 \rfloor \ge 2$. Then there exist adjacent vertices $u, v \in V(C)$ such that $a_v + a_u \ge d \cdot \frac{(m-1)^2}{m}$ (and $a_v + \dim_{\mathbb{R}}(m_{u\to v}) \ge d \cdot \frac{(m-1)^2}{m}$), hence $\max_{w \in V(C)} a_w \ge \frac{d}{2}\frac{(m-1)^2}{m} = \Omega(d \cdot \operatorname{circ}(G))$. In particular, on $C_n$ (and any graph with $\operatorname{circ}(G) = \Theta(n)$), $\Theta(d \cdot n)$ continuous real numbers per node are necessary.
- Status: proved
- Review: fresh-context
- Check: verifier (swarm #17), 2026-11-21, fresh-context reconstruction + independent verification on $C_6, C_8$, no defect located.
- Evidence: Complete derivation in `open_prv_minimal.md` (Proof of C2) via light-cone schedule on $C$, 4-point mixed-difference inversion on an $(m-1) \times (m-1)$ grid, and Brouwer's invariance of domain; verified in `open_prv_minimal-checks/verify_prv_minimal.py` (`open_prv_minimal-checks/verify_prv_minimal_stdout.txt`) for $C_6, C_8, C_{10}, C_{12}$ with exact zero causal leakage, exact SymPy ranks $1/1, 4/4, 9/9, 16/16$ (Channel A), numerical recovery residuals $\le 1.78 \times 10^{-15}$ for $d=3$ (Channel B), and two negative controls (2k rounds leaks `True`; flipped sign fails with error $2.78$).
- Depends on: none

### C3: Local-Connectivity / Subset-Union Lower Bound for $C^1$ Protocols

- Statement: Let $Q_x = 0$ and $A$ be invertible, and let $G = (V, E)$ contain two vertices $u, v$ connected by $k + 1 \ge 3$ internally disjoint paths $P_1, \dots, P_{k+1}$ such that each $P_s$ ($1 \le s \le k$) has an internal vertex $w_s$ with $\rank H_{w_s} = d$. Consider any exact provenance protocol (`def:prv-protocol`, asynchronous one-way reports with no global sub-event clock; or with a shared global clock if each $P_s$ has length $\ge 4$ and $uv \in E$) whose node states lie in Euclidean spaces $\mathbb{R}^{a_w}$ (plus arbitrary discrete metadata) and are $C^1$ functions of the observation data for each fixed discrete schedule. Then there is a neighbor $r$ of $v$ on $P_{k+1}$ such that $a_v + a_r \ge \lceil d \cdot k \cdot 2^{k-1}/(2^k - 1) \rceil > \frac{d \cdot k}{2}$. Consequently, every connected graph $G$ with $\theta(G) = \max_{u \ne v} \kappa_G(u, v) \ge 3$ and full-rank sensing requires $\max_{w \in V} a_w > \frac{d}{4}(\theta(G) - 1) = \Omega(d \cdot \theta(G))$ continuous real numbers per node.
- Status: proved
- Review: fresh-context
- Check: verifier (swarm #17 flagged gap C3-1; repaired via constant-rank theorem on open-dense $U$; swarm #19 rechecked), 2026-11-21, fresh-context reconstruction, no defect located.
- Evidence: Complete derivation in `open_prv_minimal.md` (Proof of C3) via constant-rank Jacobian subspaces $L_S(x^*), R_T(x^*)$, block-coordinate subspaces $U_L(S, i), U_R(T, i)$, and cross-intersecting bijection counting; verified in `open_prv_minimal-checks/verify_prv_minimal.py` (`open_prv_minimal-checks/verify_prv_minimal_stdout.txt`) for $K_{2,4}$ (64 pairs) and $K_{2,5}$ (256 pairs), matching partition upper bound $a + b \le k + 2$ for $k = 4, 5, 6$, and negative control for $k = 4, a + b = 2$ ($30 < 32$).
- Depends on: none

### C4: Biconnected-Component Dichotomy

- Statement: For every 2-connected graph $B$ on $b = |V(B)| \ge 3$ vertices with circumference $C = \operatorname{circ}(B)$, maximum degree $\Delta = \Delta(B)$, and maximum local vertex-connectivity $\theta = \theta(B)$, we have $\operatorname{diam}(B) \le \lfloor C/2 \rfloor$, $\Delta \le 1 + \theta^{\lceil C/2 \rceil - 1}$, and $b \le 1 + \Delta^{\lfloor C/2 \rfloor}$. Consequently, along any sequence of connected graphs $G_n$ with full-rank sensing and bounded 2-connected block-degree per vertex, $O(1)$ continuous provenance storage per node and per link suffices under arbitrary schedules (among exact $C^1$ protocols) if and only if the maximum block size $b_{\max}(G_n)$ is bounded; whenever $b_{\max}(G_n) \to \infty$, $\max(\operatorname{circ}(G_n), \theta(G_n)) \to \infty$ and per-node continuous storage must diverge.
- Status: proved
- Review: fresh-context
- Check: verifier (swarm #17, #19 after C3-1 repair), 2026-11-21, fresh-context reconstruction, no defect located.
- Evidence: Complete derivation in `open_prv_minimal.md` (Proof of C4) using Menger's theorem, minimal spanning subtree of $N_B(u)$ in $B - u$, and Moore-type degree-diameter induction; checked in `open_prv_minimal-checks/verify_prv_minimal.py` (`open_prv_minimal-checks/verify_prv_minimal_stdout.txt`) on 5 two-connected graphs (`C_6`, `K_5`, `K_{2,5}`, `Wheel_7`, `Prism_5`), cactus chain scaling ($n = 11, 51, 101$ with constant $4$ pairs vs $n$), and non-2-connected negative control `barbell(3,5)` ($\operatorname{diam}=8 > \lfloor 3/2 \rfloor = 1$).
- Depends on: C1, C2, C3

### C5: Naive Graph-Invariant Upper Bounds (FVS, Treewidth, Max-Degree, Circumference Alone)

- Statement: Every connected graph $G$ admits an exact $C^1$ provenance protocol for $Q_x = 0$ and arbitrary schedules whose per-node continuous storage is bounded solely by a function of (a) the feedback vertex set size $\mathrm{fvs}(G)$, (b) the treewidth $\mathrm{tw}(G)$, (c) the maximum degree $\Delta(G)$, or (d) the circumference $\operatorname{circ}(G)$ alone.
- Status: refuted
- Review: fresh-context
- Check: verifier (swarm #17, #19 after C3-1 repair), 2026-11-21, fresh-context reconstruction, no defect located.
- Evidence: Counterexample families verified in `open_prv_minimal-checks/verify_prv_minimal.py` (`open_prv_minimal-checks/verify_prv_minimal_stdout.txt`): (i) $G_k$ (edge $uv$ plus $k$ internally disjoint paths $v - a_s - m_s - b_s - u$ of length $4$, $n = 3k + 2$) has $\mathrm{fvs}(G_k) = 2$, $\mathrm{tw}(G_k) = 2$, and $\operatorname{circ}(G_k) = 8$, yet requires $> dk/2 = \Omega(d \cdot n)$ continuous storage by C3 (refuting (a), (b), (d)); (ii) $C_n$ has $\Delta(C_n) = 2$, $\mathrm{fvs}(C_n) = 1$, $\mathrm{tw}(C_n) = 2$, yet requires $\Omega(d \cdot n)$ continuous storage by C2 (refuting (a), (b), (c)).
- Depends on: C2, C3

## Derivations

### Proof of C1 (Block-Cut Channel Protocol)

Let $\mathcal{B}(G)$ be the set of blocks (maximal 2-connected subgraphs and bridges) of the connected graph $G = (V, E)$, and let $T_{\mathrm{BC}}(G)$ be its block-cut tree (bipartite graph on $V \sqcup \mathcal{B}(G)$ with an edge $(v, B)$ iff $v \in V(B)$). For each incident pair $(v, B)$ with $v \in V(B)$, deleting the edge $(v, B)$ from $T_{\mathrm{BC}}(G)$ splits $T_{\mathrm{BC}}(G)$ into two components, inducing a partition of $V$ into:
- $\mathrm{In}(v, B)$: vertices of $V \setminus \{v\}$ whose unique path to $v$ in $T_{\mathrm{BC}}(G)$ begins with $(v, B)$;
- $\mathrm{Out}(v, B) := V \setminus \mathrm{In}(v, B)$ (which contains $v$).

For any fixed block $B \in \mathcal{B}(G)$, the sets $\{\mathrm{Out}(w, B) : w \in V(B)\}$ partition $V$: every $x \in V$ has a unique nearest vertex $w \in V(B)$ in $T_{\mathrm{BC}}(G)$, and $x \in \mathrm{Out}(w, B)$. Moreover, every path in $G$ from $x \in \mathrm{Out}(w, B)$ to $y \in V(B) \setminus \{w\}$ must pass through $w$.

**Protocol specification:**
- Every node $v \in V$ maintains its output pair $s_v$, initialized to $\pi_0$.
- Every bridge $e = uv \in E$ (block of size $2$) maintains a link pair $c_e$, initialized to $\pi_0$. Non-bridge links carry no state.
- For every 2-connected block $B \in \mathcal{B}(G)$ ($|V(B)| \ge 3$) and every $v \in V(B)$, node $v$ stores:
  - for each $w \in V(B) \setminus \{v\}$, a pair $E_{B, v}(w)$ (initially $0$) and a counter $c_{B, v}(w) \in \mathbb{Z}_{\ge 0}$ (initially $0$);
  - a self-version counter $c_{B, v}(v) \in \mathbb{Z}_{\ge 0}$ (initially $0$).
  Define the shorthand $I_{v, B} := \sum_{w \in V(B) \setminus \{v\}} E_{B, v}(w)$ and $E_{B, v}(v) := s_v - \pi_0 - I_{v, B}$ (neither is stored separately).
- **Observation at $v$ with item $e$:** set $s_v \leftarrow s_v + e$, and increment $c_{B, v}(v) \leftarrow c_{B, v}(v) + 1$ for every 2-connected block $B \ni v$.
- **Report $u \to v$ over a bridge $e = uv$:** $u$ sends $s_u$; $v$ sets $s_v \leftarrow s_v + s_u - c_e$, the link sets $c_e \leftarrow s_u$, and for every 2-connected block $B \ni v$, $v$ increments $c_{B, v}(v) \leftarrow c_{B, v}(v) + 1$.
- **Report $u \to v$ over an edge $uv \in E(B)$ of a 2-connected block $B$:** $u$ sends $\{(c_{B, u}(w), E_{B, u}(w)) : w \in V(B)\}$ (using $E_{B, u}(u) = s_u - \pi_0 - I_{u, B}$). For each $w \in V(B) \setminus \{v\}$, if $c_{B, u}(w) > c_{B, v}(w)$, $v$ updates $s_v \leftarrow s_v - E_{B, v}(w) + E_{B, u}(w)$, $E_{B, v}(w) \leftarrow E_{B, u}(w)$, and $c_{B, v}(w) \leftarrow c_{B, u}(w)$. If at least one entry changed, $v$ increments $c_{B', v}(v) \leftarrow c_{B', v}(v) + 1$ for every other 2-connected block $B' \ni v$, $B' \ne B$.

**Inductive invariants:** For any $S \subseteq V$, write $\mathrm{Items}(S)$ for the set of observation items whose source lies in $S$. For each 2-connected block $B$ and $w \in V(B)$, let $D_w^{\mathrm{out}(B)} := D_w \cap \mathrm{Items}(\mathrm{Out}(w, B))$, and let $S^{(0)}_{B, w} \subseteq S^{(1)}_{B, w} \subseteq \dots \subseteq S^{(c_{B, w}(w))}_{B, w}$ record the value of $D_w^{\mathrm{out}(B)}$ immediately after each time $c_{B, w}(w)$ is incremented (starting at $S^{(0)}_{B, w} = \emptyset$). We prove by induction on the number of events that:
1. For every $v \in V$, $s_v = \pi_0 + \sum_{e \in D_v} e$.
2. For every bridge $e = uv$, $c_e = \pi_0 + \sum_{e' \in D_u \cap D_v} e'$; every item in $D_v \cap \mathrm{Items}(\mathrm{Out}(u, e))$ lies in $D_u$, and every item in $D_u \cap \mathrm{Items}(\mathrm{Out}(v, e))$ lies in $D_v$.
3. For every 2-connected block $B$ and every $v, w \in V(B)$: $c_{B, v}(w) \le c_{B, w}(w)$, $D_v \cap \mathrm{Items}(\mathrm{Out}(w, B)) = S^{(c_{B, v}(w))}_{B, w}$, and $E_{B, v}(w) = \sum_{e' \in S^{(c_{B, v}(w))}_{B, w}} e'$.

*Base case:* All $D_v = \emptyset$, all $s_v = c_e = \pi_0$, all $E_{B, v}(w) = 0$, all $c_{B, v}(w) = 0$. All three invariants hold.

*Observation at $v$:* Adds a fresh item $e$ (source $v$) to $D_v$ only. Invariant 1 holds since $s_v$ adds $e$. Invariant 2 holds as in `thm:prv-tree`(a) because $v \in \mathrm{Out}(v, e')$ for every bridge $e'$ incident to $v$, and $e$ lies in no other $D_x$. For invariant 3: for every 2-connected block $B \ni v$, $v \in \mathrm{Out}(v, B)$, so $D_v^{\mathrm{out}(B)}$ grows by $\{e\}$, $c_{B, v}(v)$ increments by $1$, $S^{(c_{B, v}(v))}_{B, v}$ records the new $D_v^{\mathrm{out}(B)}$, and $E_{B, v}(v) = s_v - \pi_0 - I_{v, B}$ increases by $e$ while $I_{v, B}$ is unchanged. For any $w \in V(B) \setminus \{v\}$, $v \notin \mathrm{Out}(w, B)$, so $D_v \cap \mathrm{Items}(\mathrm{Out}(w, B))$ is unchanged. For blocks $B \not\ni v$, $v \in \mathrm{Out}(w^*, B)$ for the unique cut-vertex $w^* \in V(B)$ separating $v$ from $B$, and no vertex of $B$ is affected by the observation at $v$.

*Report $u \to v$ over a bridge $e = uv$:* By invariant 2, $s_v + s_u - c_e = \pi_0 + \sum_{D_v \cup D_u} e'$, preserving invariant 1 at $v$, and $D_u \cap (D_u \cup D_v) = D_u$, preserving $c_e = \pi_0 + \sum_{D_u \cap D_v'} e'$. For any other bridge $e' = vw$ incident to $v$, $\mathrm{Out}(u, e) \subseteq \mathrm{Out}(v, e')$ and $\mathrm{Out}(w, e') \subseteq \mathrm{Out}(v, e)$, so the exact tree proof of `thm:prv-tree`(a) shows $D_v' \cap D_w = D_v \cap D_w$ and preserves invariant 2 on all bridges. For any 2-connected block $B \ni v$, the bridge $e$ lies outside $B$, so $\mathrm{Out}(u, e) \subseteq \mathrm{Out}(v, B)$, hence every new item in $D_u \setminus D_v$ has source in $\mathrm{Out}(v, B)$ (since items in $D_u$ with source in $\mathrm{Out}(v, e) \supseteq \mathrm{In}(v, B)$ already lie in $D_v$ by invariant 2!). Thus $D_v \cap \mathrm{Items}(\mathrm{Out}(w, B))$ is unchanged for all $w \in V(B) \setminus \{v\}$, while $D_v^{\mathrm{out}(B)}$ grows to $D_v^{\mathrm{out}(B)} \cup (D_u \setminus D_v)$, $c_{B, v}(v)$ increments, and $E_{B, v}(v) = s_v - \pi_0 - I_{v, B}$ increases by $\sum_{D_u \setminus D_v} e'$, preserving invariant 3.

*Report $u \to v$ over an edge $uv \in E(B)$ of a 2-connected block $B$:* Since $\{\mathrm{Out}(w, B) : w \in V(B)\}$ partitions $V$, $D_v' = D_v \cup D_u$ decomposes as the disjoint union over $w \in V(B)$ of $(D_v \cap \mathrm{Items}(\mathrm{Out}(w, B))) \cup (D_u \cap \mathrm{Items}(\mathrm{Out}(w, B))) = S^{(c_{B, v}(w))}_{B, w} \cup S^{(c_{B, u}(w))}_{B, w} = S^{(\max(c_{B, v}(w), c_{B, u}(w)))}_{B, w}$. For $w = v$, invariant 3 gives $c_{B, u}(v) \le c_{B, v}(v)$, so the $w = v$ component is unchanged. For each $w \in V(B) \setminus \{v\}$, replacing $(c_{B, v}(w), E_{B, v}(w))$ whenever $c_{B, u}(w) > c_{B, v}(w)$ updates $E_{B, v}(w)$ to the sum over $S^{(\max(c_{B, v}(w), c_{B, u}(w)))}_{B, w}$ and updates $s_v$ by the exact difference, preserving invariants 1 and 3 on $B$. For any other 2-connected block $B' \ni v$ ($B' \ne B$), $\mathrm{In}(v, B) \subseteq \mathrm{Out}(v, B')$, so every new item added to $D_v$ has source in $\mathrm{Out}(v, B')$, leaving $I_{v, B'}$ unchanged and updating $D_v^{\mathrm{out}(B')}$ with $c_{B', v}(v)$ incremented. For any bridge $e' = vw$ incident to $v$, $\mathrm{In}(v, B) \subseteq \mathrm{Out}(v, e')$, so every new item in $D_u \setminus D_v$ has source in $\mathrm{Out}(v, e')$ and cannot lie in $D_w \setminus D_v$ (by invariant 2 on $e'$, any item of $\mathrm{Out}(v, e')$ in $D_w$ is already in $D_v$); hence $D_v' \cap D_w = D_v \cap D_w$, preserving invariant 2.

Exactness for $x_0$ follows from invariant 1, and for $x_t = A^t x_0$ when $A$ is invertible. Storage counts follow directly from the state specification. $\square$

### Proof of C2 (Cycle Circumference Lower Bound)

Let $C$ be a simple cycle of length $\ell \ge 6$ in $G$, with vertices labeled $0, 1, \dots, k, k+1$ in cyclic order ($k = \ell - 2 \ge 4$) and edges $(s, s+1)$ for $0 \le s \le k$ plus $e^* = (k+1, 0)$. Set $m = \lfloor k/2 \rfloor \ge 2$. All edges of $G$ outside $E(C)$ never fire during the schedule, so no information crosses chords or external paths; the edge $e^*$ fires only at the final step.

**Light-cone schedule:** Fix two integers $T_0, T_1 \in \{k, k+1, \dots, 2k-1\}$. Execute $2k - 1$ rounds $t = 1, 2, \dots, 2k-1$, each consisting of:
1. *Observations:* Each internal vertex $s \in \{1, \dots, k\}$ makes its $t$-th observation $o_{s, t}$, with $x_{s, t} := (A^t)^\top H_s^\top R_s^{-1} o_{s, t} \in \mathbb{R}^d$. Since $A$ is invertible and $\rank H_s = d$, the linear map $o_{s, t} \mapsto x_{s, t}$ is surjective onto $\mathbb{R}^d$.
2. *Endpoint deliveries:* If $t \le T_0$, fire $1 \to 0$; if $t \le T_1$, fire $k \to k+1$.
3. *Anti-cascading internal sweeps:* Fire $(k-1 \to k), (k-2 \to k-1), \dots, (1 \to 2)$ in descending order, then fire $(2 \to 1), (3 \to 2), \dots, (k \to k-1)$ in ascending order.

Finally, fire the single report $(k+1) \to 0$.

**Information sets and causal independence:** By induction on $t \in \{1, \dots, 2k-1\}$, at the start of phase 2 of round $t$, vertex $s \in \{1, \dots, k\}$ holds $\{(s', r) : 1 \le s' \le k,\; 1 \le r \le t - |s - s'|\}$ because each anti-cascading sweep advances information by at most $1$ hop per round in each direction. Hence after round $2k - 1$:
$$D_0(T_0) = \{(s, r) : 1 \le s \le k,\; 1 \le r \le T_0 - s + 1\}, \qquad D_{k+1}(T_1) = \{(s, r) : 1 \le s \le k,\; 1 \le r \le T_1 - k + s\}.$$
For causal independence: the schedules for all $T_0, T_1 \in \{k, \dots, 2k-1\}$ are identical through round $k$. The first event that depends on $T_0$ occurs at phase 2 of round $k+1$ (whether $1 \to 0$ fires). Moving right at most $1$ hop per round in phase 3, any causal effect of $T_0$ reaches vertex $s \in \{2, \dots, k\}$ only at the end of round $k + s - 1$, so it reaches vertex $k$ at the end of round $2k - 1$, *after* phase 2 ($k \to k+1$) of round $2k - 1$ has already completed. Thus the state $\sigma_{k+1}(T_1; x) \in \mathbb{R}^{a_{k+1}}$ (and hence the message $m_{(k+1)\to 0}(T_1; x)$ over the untouched link $e^*$) depends only on $T_1$ and $x_{D_{k+1}(T_1)}$, and is independent of $T_0$. Symmetrically, the state $\sigma_0(T_0; x) \in \mathbb{R}^{a_0}$ depends only on $T_0$ and $x_{D_0(T_0)}$, and is independent of $T_1$.

**2D-grid embedding and topological dimension bound:** Restrict $T_0$ to the $m$ values $T_0^{(i)} := 2(m + i) - 1$ ($i = 1, \dots, m$) and $T_1$ to the $m$ values $T_1^{(j)} := k + 2(j - 1)$ ($j = 1, \dots, m$); both sets lie in $\{k, \dots, 2k-1\}$ because $2m \le k$. For each $(a, b) \in \{1, \dots, m\}^2$, define the observation key $(s(a, b), r(a, b)) := (m + a - b + 1,\; m + a + b - 1)$. Since $2 \le s(a, b) \le 2m \le k$ and $m + 1 \le r(a, b) \le 3m - 1 \le 2k - 1$, these $m^2$ keys are distinct valid observations in the schedule, and satisfy:
$$r(a, b) + s(a, b) = 2(m + a) \le T_0^{(i)} + 1 \iff a \le i, \qquad r(a, b) - s(a, b) = 2(b - 1) \le T_1^{(j)} - k \iff b \le j.$$
Set $x_{s, r} = 0$ for every $(s, r)$ outside the active $(m-1) \times (m-1)$ subgrid $\mathcal{G}^* := \{(s(a, b), r(a, b)) : 2 \le a \le m,\; 2 \le b \le m\}$, and let $x = (x_{a, b})_{2 \le a, b \le m} \in (\mathbb{R}^d)^{(m-1)^2}$ vary freely. For each $(i, j) \in \{1, \dots, m\}^2$, after $(k+1) \to 0$ fires, node $0$ must output the exact information vector:
$$S(i, j; x) := h_0 + \sum_{\substack{2 \le a, b \le m \\ a \le i \text{ or } b \le j}} x_{a, b} = h_0 + \sum_{a=2}^m \sum_{b=2}^m x_{a, b} - \sum_{a=i+1}^m \sum_{b=j+1}^m x_{a, b},$$
which is a function of $(\sigma_0(T_0^{(i)}; x),\; \sigma_{k+1}(T_1^{(j)}; x))$ (and of $(\sigma_0(T_0^{(i)}; x),\; m_{(k+1)\to 0}(T_1^{(j)}; x))$). For every $(i, j) \in \{2, \dots, m\}^2$, the 4-point mixed difference satisfies:
$$S(i, j; x) - S(i, j-1; x) - S(i-1, j; x) + S(i-1, j-1; x) = -x_{i, j}.$$
Therefore, the continuous map $\Gamma : \mathbb{R}^{d(m-1)^2} \to \mathbb{R}^{m(a_0 + a_{k+1})}$ defined by $\Gamma(x) := \bigl((\sigma_0(T_0^{(i)}; x))_{i=1}^m,\; (\sigma_{k+1}(T_1^{(j)}; x))_{j=1}^m\bigr)$ is injective (as $x$ is uniquely recovered from $\Gamma(x)$ via the outputs $S(i, j; x)$ and the 4-point difference). By Brouwer's invariance of domain, a continuous injection $\mathbb{R}^N \hookrightarrow \mathbb{R}^M$ requires $M \ge N$, so $m(a_0 + a_{k+1}) \ge d(m-1)^2$, i.e., $a_0 + a_{k+1} \ge d \cdot \frac{(m-1)^2}{m}$. Replacing $\sigma_{k+1}$ by $m_{(k+1)\to 0}$ yields the identical bound $a_0 + \dim_{\mathbb{R}}(m_{(k+1)\to 0}) \ge d \cdot \frac{(m-1)^2}{m}$. $\square$

### Proof of C3 (Local-Connectivity / Subset-Union Lower Bound)

Let $P_1, \dots, P_{k+1}$ be $k + 1$ internally disjoint $u$-$v$ paths in $G$, with internal vertices $w_s \in V(P_s) \setminus \{u, v\}$ having $\rank H_{w_s} = d$ for $s = 1, \dots, k$, and let $r$ be the neighbor of $v$ on $P_{k+1}$ (with $r = u$ if $P_{k+1}$ is the single edge $uv$). All edges outside $\bigcup_{s=1}^{k+1} E(P_s)$ never fire.

**Schedule:** Each $w_s$ ($1 \le s \le k$) makes one observation $o_s$ with $x_s := (A^1)^\top H_{w_s}^\top R_{w_s}^{-1} o_s \in \mathbb{R}^d$ (surjective onto $\mathbb{R}^d$). Fix any $S, T \subseteq [k] := \{1, \dots, k\}$.
- *Asynchronous case (no global sub-event clock):* (1) For each $s \in T$, propagate $w_s$'s item along $P_s$ from $w_s$ to $u$; then propagate $u$'s state along $P_{k+1}$ from $u$ to $r$. (2) For each $s \in [k] \setminus T$, propagate $w_s$'s item along $P_s$ from $w_s$ to $u$. (3) For each $s \in S$, propagate $w_s$'s item along $P_s$ from $w_s$ to $v$. (4) Fire $r \to v$. Because every report is one-way and $u$ never sends back into $P_s$, each $w_s$ experiences the identical local event sequence independent of $T$, so $v$'s state $\Phi_S(x) \in \mathbb{R}^{a_v}$ before $r \to v$ depends only on $(S, x_S)$; likewise $r$'s state $\Psi_T(x) \in \mathbb{R}^{a_r}$ was frozen at step 1 and depends only on $(T, x_T)$.
- *Global-clock case (each $P_s$ has length $\ge 4$ with neighbors $a_s$ of $v$, $b_s$ of $u$, and $uv \in E$):* At $t=1$, all $w_s$ observe $x_s$ and propagate to $a_s$ and $b_s$; at $t=2$, fire $a_s \to v$ for $s \in S$ and $b_s \to u$ for $s \in T$; at $t=3$, fire $u \to v$. Again $\Phi_S(x)$ depends only on $(S, x_S)$ and $\Psi_T(x)$ depends only on $(T, x_T)$, even with global timestamps.

**Constant-rank Jacobian subspaces and cross-intersecting counting:** Let $G_{S, T}(x) := (\Phi_S(x), \Psi_T(x)) \in \mathbb{R}^{a_v + a_r}$. For any $C^1$ map $F : \mathbb{R}^{dk} \to \mathbb{R}^m$, the set $U_F$ of points where $\rank DF(\cdot)$ is locally constant is open and dense in $\mathbb{R}^{dk}$ (on any nonempty open ball $B$, the maximum rank $r_{\max}$ is attained at some $x_0 \in B$, and a nonvanishing $r_{\max} \times r_{\max}$ minor stays nonzero on a neighborhood $W \subseteq B$ of $x_0$). Thus the finite intersection $U := \bigcap_S U_{\Phi_S} \cap \bigcap_T U_{\Psi_T} \cap \bigcap_{S, T} U_{G_{S, T}}$ is open and dense in $\mathbb{R}^{dk}$; fix $x^* \in U$, and set $L_S := \operatorname{rowspace}(D_x \Phi_S(x^*)) \subseteq (\mathbb{R}^d)^S$ ($\dim L_S \le a_v$) and $R_T := \operatorname{rowspace}(D_x \Psi_T(x^*)) \subseteq (\mathbb{R}^d)^T$ ($\dim R_T \le a_r$). For $\alpha \in [d]$ and $A \subseteq [k]$, let $\mathbf{1}_A^{(\alpha)} \in (\mathbb{R}^d)^k$ place $e_\alpha \in \mathbb{R}^d$ in slots $s \in A$ and $0$ elsewhere.

By the constant-rank theorem applied to $G_{S, T}$ at $x^*$, for every $v \in \ker DG_{S, T}(x^*) = \ker D\Phi_S(x^*) \cap \ker D\Psi_T(x^*)$ there is a $C^1$ curve $\gamma : (-\epsilon, \epsilon) \to \mathbb{R}^{dk}$ with $\gamma(0) = x^*$, $\gamma'(0) = v$, and $G_{S, T}(\gamma(t)) = G_{S, T}(x^*)$. By exactness after $r \to v$, $h_0 + \sum_{s \in S \cup T} x_s$ is a function of $G_{S, T}(x)$ (without assuming differentiability of the readout/fusion map), so $t \mapsto \langle \mathbf{1}_{S \cup T}^{(\alpha)}, \gamma(t) \rangle$ is constant near $0$; differentiating at $t = 0$ gives $\mathbf{1}_{S \cup T}^{(\alpha)} \in (\ker D\Phi_S(x^*) \cap \ker D\Psi_T(x^*))^\perp = L_S + R_T$ for all $S, T \subseteq [k]$ and $\alpha \in [d]$. Applying the same constant-rank argument to $\Phi_S$ and $\Psi_T$ individually (using exactness of $v$'s and $r$'s outputs before $r \to v$) gives $\mathbf{1}_S^{(\alpha)} \in L_S$ and $\mathbf{1}_T^{(\alpha)} \in R_T$.

For each $S \subseteq [k]$ and $i \in S$, define $U_L(S, i) := \{y \in \mathbb{R}^d : y \otimes e_i \in L_S\} \subseteq \mathbb{R}^d$; similarly $U_R(T, i) := \{y \in \mathbb{R}^d : y \otimes e_i \in R_T\}$. For any fixed $S$, the subspaces $\{U_L(S, i) \otimes e_i : i \in S\}$ lie in disjoint coordinate blocks of $(\mathbb{R}^d)^S$, so $\sum_{i \in S} \dim U_L(S, i) \le \dim L_S \le a_v$, and likewise $\sum_{i \in T} \dim U_R(T, i) \le a_r$.

Now fix any $S \subseteq [k]$, any $i \in S$, and set $T := ([k] \setminus S) \cup \{i\}$, so $S \cap T = \{i\}$ and $S \cup T = [k]$. For each $\alpha \in [d]$, write $\mathbf{1}_{[k]}^{(\alpha)} = u + w$ with $u \in L_S$ and $w \in R_T$. Since $w_s = 0$ on $S \setminus \{i\}$ and $u_s = 0$ on $T \setminus \{i\}$, we have $u_s = e_\alpha$ on $S \setminus \{i\}$, $w_s = e_\alpha$ on $T \setminus \{i\}$, and $u_i + w_i = e_\alpha$. Hence $\mathbf{1}_S^{(\alpha)} - u = (e_\alpha - u_i) \otimes e_i \in L_S$ and $\mathbf{1}_T^{(\alpha)} - w = u_i \otimes e_i \in R_T$, so $e_\alpha = (e_\alpha - u_i) + u_i \in U_L(S, i) + U_R(T, i)$. Since this holds for all $\alpha \in [d]$, $U_L(S, i) + U_R(T, i) = \mathbb{R}^d$, giving $\dim U_L(S, i) + \dim U_R(T, i) \ge d$.

The map $(S, i) \mapsto (([k]\setminus S) \cup \{i\}, i)$ is a bijection on the $k \cdot 2^{k-1}$ pairs $\{(S, i) : i \in S \subseteq [k]\}$. Summing $\dim U_L(S, i) + \dim U_R(T, i) \ge d$ over all such pairs yields:
$$d \cdot k \cdot 2^{k-1} \le \sum_{\emptyset \ne S \subseteq [k]} \sum_{i \in S} \dim U_L(S, i) + \sum_{\emptyset \ne T \subseteq [k]} \sum_{i \in T} \dim U_R(T, i) \le (2^k - 1)(a_v + a_r).$$
Hence $a_v + a_r \ge \lceil d \cdot k \cdot 2^{k-1}/(2^k - 1) \rceil > \frac{d \cdot k}{2}$. For $\theta(G) = \max_{u \ne v} \kappa_G(u, v) \ge 3$, Menger's theorem provides $\theta(G)$ internally disjoint $u$-$v$ paths (at most one of which is the direct edge $uv$, leaving at least $k = \theta(G) - 1$ paths with internal vertices, and at least one remaining path $P_{k+1}$), giving $\max_{w \in V} a_w > \frac{d}{4}(\theta(G) - 1)$. $\square$

### Proof of C4 (Biconnected-Component Dichotomy)

Let $B$ be a 2-connected graph on $b = |V(B)| \ge 3$ vertices with $C = \operatorname{circ}(B) \ge 3$, $\Delta = \Delta(B) \ge 2$, and $\theta = \theta(B) \ge 2$.
1. *Diameter bound:* For any distinct $x, y \in V(B)$, Menger's theorem yields two internally disjoint $x$-$y$ paths in $B$, each of length at least $\operatorname{dist}_B(x, y)$. Their union is a simple cycle of length at least $2 \operatorname{dist}_B(x, y)$, so $2 \operatorname{dist}_B(x, y) \le C$, hence $\operatorname{diam}(B) \le \lfloor C/2 \rfloor$.
2. *Degree bound:* Let $u \in V(B)$ have degree $\Delta$. Since $B$ is 2-connected, $B - u$ is connected; let $T'$ be a minimal subtree of a spanning tree of $B - u$ spanning $N_B(u)$, so every leaf of $T'$ lies in $N_B(u)$. Any path of length $L$ in $T'$ between two leaves forms with $u$ a simple cycle of length $L + 2 \le C$, so $\operatorname{diam}(T') \le C - 2$ and the radius of $T'$ is at most $r_T := \lceil (C - 2)/2 \rceil = \lceil C/2 \rceil - 1$. For any $v \in V(T')$ of degree $d_v$ in $T'$, each of the $d_v$ components of $T' - v$ contains a leaf in $N_B(u)$, yielding $d_v$ internally disjoint $v$-$u$ paths in $B$, so $d_v \le \kappa_B(u, v) \le \theta$, i.e., $\Delta(T') \le \theta$. By standard Moore counting from a center vertex of $T'$, $\Delta = |N_B(u)| \le |V(T')| \le 1 + \theta \sum_{j=0}^{r_T - 1} (\theta - 1)^j \le 1 + \theta^{r_T}$ (using the elementary induction $\theta \sum_{j=0}^{r-1} (\theta - 1)^j \le \theta^r$ for all $\theta \ge 2, r \ge 1$: base $r=1$ is $\theta = \theta$; step is $\theta + (\theta - 1)\theta^r \le \theta^r + (\theta - 1)\theta^r = \theta^{r+1}$).
3. *Vertex bound:* Fixing any root $v_0 \in V(B)$, every vertex is at distance at most $r_B := \lfloor C/2 \rfloor \ge 1$ from $v_0$, so by the same induction $b \le 1 + \Delta \sum_{j=0}^{r_B - 1} (\Delta - 1)^j \le 1 + \Delta^{r_B}$.

Consequently, if $\max(\operatorname{circ}(G_n), \theta(G_n)) \le M_0$ is bounded, then every 2-connected block $B$ has bounded size $b \le 1 + (1 + M_0^{\lceil M_0/2 \rceil - 1})^{\lfloor M_0/2 \rfloor}$. Contrapositively, $b_{\max}(G_n) \to \infty$ forces $\max(\operatorname{circ}(G_n), \theta(G_n)) \to \infty$, so C2 and C3 force per-node continuous storage to diverge. Conversely, if $b_{\max}(G_n)$ and the 2-connected block-degree per vertex are bounded, C1 achieves $O(1)$ pairs per node and per link. $\square$

## Failed routes

### R1: Bounding minimal storage by FVS, treewidth, or maximum degree

- Tried: Conjecturing that minimal provenance storage is bounded by $O(\mathrm{fvs}(G))$, $O(\mathrm{tw}(G))$, or $O(\Delta(G))$.
- Failed because: $C_n$ has $\mathrm{fvs} = 1, \mathrm{tw} = 2, \Delta = 2$ yet requires $\Omega(d \cdot n)$ storage (C2); $G_k$ has $\mathrm{fvs} = 2, \mathrm{tw} = 2, \operatorname{circ} = 8$ yet requires $\Omega(d \cdot n)$ storage (C3).
- Reopen if: The schedule is restricted (e.g., synchronous flooding or bounded-gap schedules) rather than arbitrary.

### R2: Attempting an $O(\log n)$ dyadic protocol on $C_n$

- Tried: Exploiting the single-crossing cut-index property on $C_n$ (which gives an $O(\log n)$-dimensional solution for the one-observation-per-node prefix/suffix subproblem $\mathbf{1}_{[1,k]} \in L_i + R_j$).
- Failed because: Under arbitrary schedules with repeated observations, the light-cone schedule on $C_n$ embeds an independent $(m-1) \times (m-1)$ 2D grid of observations $(s, r)$ in $(r+s, r-s)$ coordinates, destroying the 1D dyadic structure and forcing $\Omega(d \cdot n)$ continuous storage (C2).
- Reopen if: Each node is restricted to at most one observation (where the prefix/suffix problem has $O(\log n)$ dyadic upper bound).

## Open obligations

- [ ] O1 (sessions: 1): Determine whether the quantitative lower bound $\Omega(d \cdot \max(\operatorname{circ}(G), \theta(G)))$ can be tightened to $\Omega(d \cdot b_{\max}(G))$ on every 2-connected graph $B$, or whether there exist 2-connected graphs with $\max(\operatorname{circ}(B), \theta(B)) = o(|V(B)|)$ that admit exact $o(d \cdot |V(B)|)$ storage.
- [x] O2 (sessions: 1): Obtain fresh-context verification from `@verifier` on Claims C1–C5 and update Review / Check fields accordingly. (Completed 2026-11-21: swarm #17 and #19, all claims C1–C5 at `no defect located`.)

## Review Log

- 2026-11-21 (`@verifier`, swarm #17): Fresh-context reconstruction of `cleaned_writeup_prv_minimal.md`. Verdicts: C1 `no defect located` (independent 1,000-event check, max error `6.22e-15`); C2 `no defect located` (independent check on $C_6, C_8$); C3 `defect located` — C3-1 (gap: applying chain rule at $x=0$ assumed differentiability of readout/fusion map, witness $\Phi_S(x)=(x_s^3)$); C4 `no defect located` (inheriting C3-1); C5 `no defect located` (inheriting C3-1).
- 2026-11-21 (disposition of C3-1): Accepted; repaired C3 by evaluating Jacobians at $x^* \in U = \bigcap_S U_{\Phi_S} \cap \bigcap_T U_{\Psi_T} \cap \bigcap_{S,T} U_{(\Phi_S,\Psi_T)}$ (open dense locally-constant-rank set) and applying the constant-rank theorem on $C^1$ level curves without assuming differentiability of readout/fusion maps.
- 2026-11-21 (`@verifier`, swarm #19): Recheck of repaired C3 (and C4/C5 inheritance): `no defect located` across all claims C1–C5.

## Literature

| Claim | Source | Locator | Read depth | Date read | Verdict |
| --- | --- | --- | --- | --- | --- |
| Live problem & baseline schemes | `sections/ext4_prv.tex`, `sections/appext4_prv.tex` | `def:prv-protocol`, `thm:prv-tree`, `prop:prv-clock`, `open:prv-minimal` | full | 2026-11-21 | matches |

## Searches

| Query | Tool | Date | Not searched |
| --- | --- | --- | --- |
| none (no novelty claim made; all proofs are self-contained) | n/a | 2026-11-21 | external literature on distributed provenance lower bounds |

## Log

- 2026-11-21: opened and completed Session 1 derivations (C1–C5) and two-channel verification script `open_prv_minimal-checks/verify_prv_minimal.py` (all checks and planted-error negative controls passed). Reporting gate: (1) Literally asked for least storage of an exact protocol for $Q_x=0$ on graphs with cycles under arbitrary schedules as a function of $n$ and cycle structure, and whether growth with $n$ is necessary; answered by Block-Cut Channel Protocol upper bound (C1), $\Omega(d \cdot \operatorname{circ}(G))$ and $\Omega(d \cdot \theta(G))$ lower bounds (C2, C3), biconnected-component dichotomy (C4), and refutation of FVS/tw/$\Delta$/circ-alone bounds (C5). (2) Two ways to miss the point: proving only a one-observation-per-node bound (which misses the $\Omega(n)$ cycle lower bound) or forgetting continuity/regularity (trivializing real-number dimension); both avoided. (3) Strongest referee objection: quantitative gap between $\Omega(d \cdot \max(\operatorname{circ}(G), \theta(G)))$ and $O(b_{\max}(G))$ on 2-connected graphs with small $\operatorname{circ}$ and $\theta$, plus global-clock caveat on unsubdivided $K_{2,k+1}$; both explicitly disclosed (O1 and statement of C3). (4) No speculative claims or unverified citations; three ways the result could still be wrong (causal leak in C2 schedule, missing cut-vertex invariant in C1, or $d \ge 2$ block-independence bug in C3) are each directly checked by both proof and executed script. (5) O1 remains as a quantitative refinement; O2 is the pending `@verifier` check. Next action: lint record, write cleaned write-up, and hand off to `@verifier`.
