---
type: run
title: "MultiAgentELBO parent memory across locality priors (X3), September 30, 2026"
aliases: ["X3 locality parent memory September 2026", "Locality prior parent-memory study"]
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/vfe, cluster/info-geometry, project/multi-agent, field/mathematics, field/statistics, field/physics]
year: 2026
created: 2026-09-30
---

# Parent memory across locality priors (X3)

> [!info] Citation
> MultiAgentELBO project (2026). *Parent memory across locality priors: September 30, 2026*. Implementation, contract, results, and evidence in `docs/research/2026-09-30-locality-parent-memory/` (CONTRACT.md, RESULTS.md, evidence/), with code in `src/multiagent_elbo/realizations/gaussian/locality.py` and the profile `experiments/locality_parent_memory.py`.

## Setting

The study tests the locality hypothesis of [[multiagentelbo-2026-09-30-spin-foam-integration-review]] (proposal X3) after the user's locality decision. Agents sit on a declared ring with state dimension $K=2$ and independent $\mathrm{GL}^+(2,\mathbb R)$ links $\exp(0.2\,G)$. Attention is held at the source prior (the high-temperature reading): each row attending to a source is a record of precision $\kappa\pi_{ij}$ on the transported residual, so under joint descent a one-way row still moves its source. The prior families are a hard window of radius 4, exponential decay with rate 0.5, power laws with $\alpha=2$ and $\alpha=1$, complete uniform support (mean-field reference), and a one-way window. The one-way window is run under joint descent and, separately, under a declared row-only drift that is not descent of the collective free energy. The parent is the block mean over blocks of 16 agents, observed in the held Ornstein–Uhlenbeck reference at sampling interval 0.5, with horizon $H=50$ and context lengths $k=0,\dots,5$, for $N=64$ to $2{,}048$. The measured quantity is the exact omitted-history information $D_{H,k}=\sum_t I(Z_t;Z_{0:t-k-1}\mid Z_{t-k:t-1})$ of the theory's memory identity.

## Results

Local priors keep a fitted per-step decay ratio near 0.29 to 0.31, flat in $N$, with finite size-independent memory per block (about $2$ to $3\times10^{-2}$ nats for window and exponential priors). The $\alpha=2$ power law behaves like the local families. The $\alpha=1$ power law drifts toward mean-field as $N$ grows (ratio 0.175 to 0.131). Complete support has the fastest decay (ratio 0.113, flat in $N$), and its memory per block falls roughly as $N^{-1.9}$, reaching $3\times10^{-9}$ nats at $N=2{,}048$. With identity links the complete-support block-mean parent is exactly Markov, because the precision is $\alpha I+\beta\mathbf 1\mathbf 1^\top$. The declared row-only one-way drift carries about 40 times the memory of joint descent on the same support (ratio 0.65), still flat in $N$.

The review's hypothesis held for local priors and was refuted for complete support: size-uniform prediction of this parent does not require locality, and the mechanism that makes complete support benign is exchangeability. Locality is where finite residual memory sits.

Checks: seven new and seventeen existing tests passed; the identity "path KL = memory + row risk" held to $8.8\times10^{-12}$ relative on 27 instances; two independent routes for $D_{H,k}$ agree to $3.4\times10^{-12}$; $D_{H,k}$ is nonincreasing in $k$ in all 60 instances. One cross-check against the existing hidden filter at $N=64$ missed its $10^{-9}$ relative tolerance at $4.2\times10^{-9}$ ($4\times10^{-14}$ absolute) and is recorded as a miss. Sixty instances took 405 s on the Ryzen CPU in float64.

## Scope

One link draw per $N$, one parameter point, one retention map (block means, a frame-dependent choice), stationary start, attention held at the prior, and row-stochastic (mean-field-scaled) priors. Extensive coupling, finite-temperature attention, moving links, and other retention maps were not run and could change the complete-support conclusion. These are finite numerics, not theorems, and set no direction on their own.

## Relevance to this research

Updates [[Coarse Graining]] and [[Gauge-Theoretic Multi-Agent VFE Model]] on the locality decision. Contrasts with the expectation recorded in [[Spin foam coarse-graining for agent networks]] that size-uniform control needs locality: for this Gaussian parent, exchangeability suffices. Connects to [[Graphon limits of agent networks]] (the complete-support mean-field limit) and [[multiagentelbo-2026-09-30-gaussian-parent-dynamics]] (the held-OU reference it extends).
