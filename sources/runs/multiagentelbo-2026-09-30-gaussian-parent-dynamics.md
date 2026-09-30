---
type: run
title: "MultiAgentELBO observed-link Gaussian parent dynamics, September 30, 2026"
aliases: ["Observed-link Gaussian inherited parent reference September 2026"]
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/vfe, cluster/info-geometry, project/multi-agent, field/mathematics, field/statistics, field/cs-ml, field/physics]
year: 2026
created: 2026-09-30
---

# Observed-link Gaussian parent dynamics

> [!info] Citation
> MultiAgentELBO project (2026). *Gaussian inherited-parent dynamics: September 30, 2026*. Implementation and retained CPU evidence, published in [PR #101](https://github.com/cdenn016/MultiAgentELBO/pull/101), merge revision 7e2214b63563c14e5d7e96c06adf6f1775306ff5. [Published result record](https://github.com/cdenn016/MultiAgentELBO/blob/7e2214b63563c14e5d7e96c06adf6f1775306ff5/docs/research/2026-09-30-gaussian-parent-dynamics/RESULTS.md).

## Summary and setting

The continuation of [[multiagentelbo-2026-09-30-pointwise-gaussian-network]] implements actual-law initialization, exact correlated-noise hidden filtering, general-SPD-mobility held-OU transitions, and the optimal time-dependent one-step Markov parent for a supplied observed schedule at $c_*$. Seven tiny CPU tests passed, then one five-case 512-agent study passed all 95 comparisons. Measured study duration was 45.35418870000285 seconds including artifact saving and excluding interpreter/import startup; the largest absolute comparison error was $6.821210263296962\times10^{-13}$ at absolute and relative tolerances $10^{-8}$. GPU execution was unnecessary and was not run.

Graph, source assignments, prior parameters, receiver comparison maps, record precisions, and observed records are held. Source comparison maps move under externally supplied deterministic flows. Each interval uses the assembled action frozen at its start, with identity mobility in the benchmark. This is exact for the declared piecewise-held dynamics, not for a continuously changing action. Seed 20260930, motion strength 0.1, three intervals of length 0.2, and the retained every-fourth-node rule are supplied controls. The initial mean is the initial-action equilibrium mean plus 0.03 cos(arange(d)); covariance is 1.2 times its equilibrium covariance. Actual inherited correlations are preserved rather than replaced by an equilibrium conditional.

## Parent and information contract

For a deterministic affine Gaussian schedule $X_{n+1}=F_nX_n+u_n+\eta_n$, independent SPD Gaussian noises and a proper Gaussian activation law, the hidden conditional given the entire retained history remains Gaussian. Its prediction includes the retained/hidden process-noise cross covariance. General SPD mobility is carried explicitly by the held-OU kernel and transforms with passive noncompact frame changes. Holding identity mobility after a nonorthogonal passive change would select different kinetics.

The comparator uses the actual propagated conditional $P(R_{n+1}\mid R_n)$ and the same initial retained law. These rows reproduce one-time and consecutive-pair marginals while minimizing forward path KL among Markov products. Gaussian conditional entropies give the finite sampled-path identity
$$
D_{\mathrm{path}}=\frac12\sum_n\left[\log\det V_{\mathrm{one-step},n}-\log\det V_{\mathrm{history},n}\right].
$$
The first term is zero analytically. Computed values are retained without clamping; the rectangular case's first value was $-8.527\times10^{-14}$. This is an expected information loss, not a pathwise log-density ratio or a score for arbitrary equilibrium rows. The existing Chapter 11 history and finite-memory constructions supply the context; no new general filtering theorem is claimed.

The predictor retains full hidden means and covariances: 768 hidden real coordinates in real cases and 1536 in realified complex cases. Its exactness does not establish a network-size-independent parent or a learned grouping.

## Executed evidence

| Observed scheduled maps | Fine real dimension | Retained coordinates | Total path KL to optimal one-step parent, nats |
| --- | ---: | ---: | ---: |
| Flat GL+(2,R) | 1024 | 256 | 0.0143704096042 |
| Independent GL+(2,R) | 1024 | 256 | 0.0117117582856 |
| Rank-one rectangular matrix | 1024 | 256 | 0.00124487796290 |
| GL(2,C), realified | 2048 | 512 | 0.00124468332069 |
| SU(2), realified | 2048 | 512 | 0.00101649257340 |

The seven-test JUnit records zero failures, errors, or skips. Tiny independent calculations check the general-mobility transition against a SciPy block exponential, actual initial conditionals, correlated-noise forecasts and densities against full-path Gaussian conditioning, actual-pair projection, path KL against direct Gaussian KL, retain-all/autonomous limits, and passive GL covariance with carried mobility. The packet took 1.77 seconds including pytest overhead. The 95 study comparisons check full retained-path KL against innovation information and compare one-time/pair moments and full-history forecast means, covariances, and densities.

These are one-seed finite instances over sampled horizon 0.6. No matched frozen arm, statistical variability, peak-memory measurement, long-horizon estimate, or causal effect of moving links was established. Positive later path loss in these instances is not a universal lower bound.

The first GREEN attempt aborted inside the independent SciPy oracle before the new OU code executed. Its evidence is preserved. A minimal SciPy-only probe passed; the mixed torch/SciPy probe reported duplicate OpenMP initialization, OMP Error #15. Process-local sequential MKL made the identical mixed probe pass with the same matrix-exponential trace, then supported the passing focused packet and study. The new launcher selects this setting before native imports. This tested runtime boundary does not explain unrelated historical Phase 13 crashes.

## Relevance to this research

[[Gaussian State Space Model]] and [[Coarse Graining]] now have a large-network conditional reference distinguishing static marginalization, one-step prediction, and full inherited history. [[Staged hierarchy formation and RG composability]] can reuse that reference without treating correct marginal laws as temporal closure. The actual-law preparation is relevant to [[Soft formation and the activation clock]], but the supplied retention and preparation are not a formation law.

Coupled belief/model/source/link learning, compressed finite-memory predictors with explicit error budgets, autonomous inherited parents, soft or recursive formation, and thermodynamic limits remain open. Endogenous observed structural histories can add likelihood information and need not preserve this Gaussian conditioning contract. The canonical Chapter 11 switching-diffusion obligation is not closed by externally prescribed control. Base transport remains outside the phase.

## Archive and execution provenance

The immutable compact archive is sources/archives/multiagentelbo-2026-09-30-gaussian-parent-dynamics/. It contains the published RESULTS.txt and CONTRACT.txt, command/runtime and study JSON, JUnit, implementation/profile/test snapshots, and historical RED/abort/probe logs. Full compact arrays remain in the originating repository at artifacts/pointwise-gaussian-network-dynamics/20260930T175442164906Z/; NPZ arrays were not copied.

Execution used C:/anaconda/python.exe, CPython 3.12.7, torch 2.10.0.dev20251210+cu128, CPU float64 and one thread, with MKL_THREADING_LAYER=SEQUENTIAL. CUDA was visible but unused. The execution receipt binds new working files on base 73d004df079e1f6d414622d1f8da15c476245a1f; publication later included only terminal-whitespace cleanup with unchanged parsed Python statements. The merged snapshot is distinct from that prepublication execution. No unchanged science, full suite, heavy replay, or Lean was rerun for publication.
