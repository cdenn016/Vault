---
type: run
title: "MultiAgentELBO native discarded-energy control and two-step CPU admission"
aliases: ["Native discarded-energy control and two-step CPU admission"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/info-geometry, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-08
updated: 2026-10-08
---

# MultiAgentELBO native discarded-energy control and two-step CPU admission

[Code PR190](https://github.com/cdenn016/MultiAgentELBO/pull/190), merged at `d6620b5504999b29d6cbaf500d3d06b480e27651`, continues [[multiagentelbo-2026-10-08-moving-parents-bond-factor]]. It supplies an actual-flow residual estimate for the centered recognition decoder, analyzes a conditional bridge-activation mechanism, and executes the bounded CPU device reference. Mathematical claims here report the source derivations and their assumptions; this ingestion is not an independent adjudication.

```bibtex
@misc{codex2026discardedenergydeviceadmission,
  author = {Codex},
  title = {Native Discarded-Energy Control and Two-Step CPU Admission},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/190},
  note = {Finite-instance analytical estimates and a retained-input CPU admission}
}
```

## Native centered residual

The [R3 derivation](https://github.com/cdenn016/MultiAgentELBO/blob/d6620b5504999b29d6cbaf500d3d06b480e27651/docs/research/2026-10-03-latent-link-rg-plan/R3-DISCARDED-ENERGY-CONTROL.md) uses the actual conditional quadratic mean optimum $u(G)=K(G)^{-1}h(G)$ as the reference of the weighted lift. It changes the decoder rather than the native scientific model or mobility. The discarded energy $R_*$ is twice the exact product-recognition reconstruction KL. The mean block of collective Fisher dissipation bounds $R_*$ from below through the smallest eigenvalue of $C^{1/2}KC^{1/2}$.

Positive Gaussian anchors and bounded initial free energy confine all deterministic Gaussian coordinates. Bounded expected record costs also bound supported source log odds, giving a compact interior deterministic orbit. If $B$ is the initial free energy above its fixed nonnegative-term baseline, the source obtains $\int_s^t R_* dt\leq e^{4B+2}[F(x_s)-F(x_t)]$. This supplies a vanishing late-activation energy tail for each fixed finite instance, without a stationary-point convergence assumption. The constant can grow prohibitively with network size and supplies no uniform activation rate.

For the declared Fisher thermostat, stopped energy dissipation plus small-noise coupling yields residual and exit control after the common clock $s(T)=\sqrt{\log(1/T)}$, on fixed windows measured from activation. Conditional retained-path mean-square bounds give convergence in probability; the latter extends to fixed interior initial distributions and independent Gaussian probes by bounded convergence. Expected bounds over unbounded initial states or probes still need moment domination. This is not path total variation, exact latent-posterior recovery, a regular compressed filter, a growing-size/depth theorem or a result with structural jumps and learned generative parameters. Nine small-coordinate SymPy identities ground coefficients separately from the general derivation.

## Conditional bridge mechanism

The [R4 analysis](https://github.com/cdenn016/MultiAgentELBO/blob/d6620b5504999b29d6cbaf500d3d06b480e27651/docs/research/2026-10-03-latent-link-rg-plan/R4-SECOND-STAGE-MECHANISM.md) keeps the same normalized bond candidate. Natural reward learning has the exact mean-coordinate law $\dot m=\epsilon(s-m)$, including the normalizer. A closed realized bond is not automatically reinforced, and bounded unregularized reward equilibria cannot approach a hard selected pattern. Those statements do not exclude transient episodes, mixed patterns or diverging learned rewards.

An internal bond does supply a strictly positive covariance contribution to a neighboring bridge's activation-gap derivative on arbitrary finite graphs: shrinking recognition width lowers expected transported mismatch. Mean, baseline, geometry and learning terms can oppose it. With actual trajectory containment and gap conditions, one-versus-two whole-catalog redraw bounds give a counterfactual margin $e^{-H}(1+H-e^{t_c})$, positive for $t_c<\log(1+H)$. The source does not establish those gap conditions, a nontrivial persistent partition, the required initial-law probability or recurrence bounds. No structural model was adopted or simulated.

## CPU execution and relevance

The [frozen admission and results](https://github.com/cdenn016/MultiAgentELBO/blob/d6620b5504999b29d6cbaf500d3d06b480e27651/docs/research/2026-10-03-latent-link-rg-plan/R1-DEVICE-ADMISSION-RESULTS.md) use preparation zero at N512 and N1024, all three controls, sixteen training draws and 256 future-score draws. At producer revision `28da450a9150e7b1d13ff6970bc394aa195ce150`, all six arms reach actual time .1 in two .05 steps without backtracking. Elapsed time is 143.288434 seconds; cumulative process peak is 1,437,818,880 bytes and retained NPZ volume is 111,753,453 bytes. Five tiny tests pass. NumPy-only reconstruction confirms saved values, with score error at most 1.78e-15 and recovered-noise error at most 1.34e-15.

Future simultaneous/alternating generator means differ by at most 1.02712e-4 and 1.45121e-4 at the two sizes, while future precisions remain equal. Their mean marginal log-score differences are -1.77450e-6 and +5.05205e-7; these selected preparations establish neither an arm advantage nor native accuracy. CUDA remains unrun because another Python GPU workload is active, and the full independent grid remains disabled. The results advance [[Renormalization-group flow of beliefs]] and [[Staged hierarchy formation and RG composability]] within [[Gauge-Theoretic Multi-Agent VFE Model]], while all four full RG gates remain open. No manuscript edit or historical retry accompanied the batch.
