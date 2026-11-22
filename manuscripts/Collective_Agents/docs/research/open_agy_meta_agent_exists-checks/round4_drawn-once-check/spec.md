# Fixed-attention audience patterns: specification (for a blind recomputation)

No result is given here. Compute every quantity in the list at the end by a route of your own choosing.

## Model (time-invariant framework of `def:fw-system`)

- World: one scalar AR(1) component, $\eta_{t+1}=F\eta_t+w_t$, $w_t\sim\mathcal N(0,Q)$, stationary. $F=0.9$, $Q=0.05$.
- Agents: a source $S$ (index 0) and four members $1,2,3,4$ (the audience $A$).
- Every agent filters $x_t=(\eta_t,\eta_{t-1})$ with an exact Kalman filter at its steady state. Computation noise $q_cI_2$, $q_c=10^{-4}$, is added to the predicted means and included in the prior covariance $P^-$.
- Sensors: $S$ has an own sensor with noise variance $R_S=0.01$; each member has an own sensor with noise variance $R=1$. Own sensors are read every round.
- Broadcasts: every agent writes its raw reading $u_a(t)=s_a(t)$ every round.
- Channels: a message arrives as $y_{ij}(t+1)=u_j(t)+\nu_{ij}$ with $\nu_{ij}\sim\mathcal N(0,R_c)$, $R_c=0.002$, independent across receivers, senders and rounds. Latency is exactly one round, so the message read in round $t+1$ informs $\eta_t$, the second component of $x_{t+1}$, with noise variance $R_j+R_c$, and the receiver's filter uses that exact variance.
- Attention is FIXED: $S$ reads nothing; member $i$ reads, in every round, a fixed set $J_i$ of other agents.
- Contrast coordinates: prior errors $e_a(t)=m^-_{a,0}(t)-\eta_t$ for every agent including $S$.

## Conventions

- World-conditional law (`Collective_Agents/sections/04_collectives.tex`, lines 130-141): condition on the world path and on sender-side broadcast noise (none here). An agent's own sensing noise is a private input and is not conditioned on, even when the agent broadcasts its reading. Receiver-specific channel noise is private.
- Diffusive precision, contrast, collective: `04_collectives.tex`, lines 143-221. A region is any set of at least two of the five agents.
- Substitute selector (used when contrast is undefined): "the largest ratio of mean within-block to mean between-block world-conditional mutual information over balanced bipartitions". For five agents a balanced bipartition splits them into blocks of sizes 2 and 3; pairwise world-conditional mutual information of two scalar Gaussian errors with correlation $\rho$ is $-\tfrac12\ln(1-\rho^2)$.
- Test values: compound-symmetric block $\Sigma=\alpha I_n+\beta\mathbf 1\mathbf 1^\top$ with no cut has contrast $r=1+n\beta/\alpha$ ($\alpha=1$, $\beta=0.5$, $n=4$: $r=3$).

## Pattern families

- Family 1: each member reads exactly one other agent (one of the four others), all $4^4=256$ combinations.
- Family 2: each member reads exactly two other agents (a pair among the four others), all $6^4=1296$ combinations.

## Quantities

For each family:
1. For the pattern in which every member reads only $S$ (family 1) and for any one pattern in which every member reads $S$ and one fixed co-member (family 2): the world-conditional covariance entries ($\Var e_S$, $\Cov(e_S,e_i)$, $\Var e_i$, $\Cov(e_i,e_j)$ where defined), diffusivity, and $r(A)$.
2. The number of patterns whose world-conditional precision is diffusive.
3. Over the diffusive patterns: the largest regional contrast of each pattern; list the five largest values with their patterns; the number of patterns whose largest regional contrast is at least 5.3724.
4. For level $r_0=4.5$ (family 1) and $r_0=4.45$ (family 2): the number of diffusive patterns whose set of regions with contrast at least $r_0$ is exactly $\{A\}$.
5. The substitute selector for every pattern: its value for the patterns of item 1, its minimum, median and maximum over the family, the number of infinite values, and the number of patterns whose value is at least that of the all-source pattern of family 1 (family 1) or at least 1.5 (family 2).

Include one negative control (for example $R_c\times100$ on the all-source pattern) and one validation of your contrast code on the test value above.
