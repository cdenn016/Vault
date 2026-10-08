---
type: run
title: "MultiAgentELBO nonlinear-prior original-record decoder bound"
aliases: ["Nonlinear prior averaged decoder bound"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/info-geometry, cluster/vfe, project/multi-agent, field/statistics, field/mathematics]
created: 2026-10-08
updated: 2026-10-08
---

# MultiAgentELBO nonlinear-prior original-record decoder bound

[Code PR195](https://github.com/cdenn016/MultiAgentELBO/pull/195), revision `c1469acf761ff5ad5e11aefb23542f275f08b3af`, contains the [bounded derivation](https://github.com/cdenn016/MultiAgentELBO/blob/c1469acf761ff5ad5e11aefb23542f275f08b3af/docs/research/2026-10-03-latent-link-rg-plan/R2-NONLINEAR-DECODER-BOUND.md). It continues [[multiagentelbo-2026-10-08-n2048-cpu-capacity]] without another simulation, reusing the anchored nonlinear prior's uniform primitive second moment.

```bibtex
@misc{codex2026nonlineardecoder,
  author = {Codex},
  title = {A Nonlinear-Prior Bound for Uniformly Queried Original Records},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/195},
  note = {Revision c1469acf761ff5ad5e11aefb23542f275f08b3af; analytical research record}
}
```

## Conditional estimate and scope

Fix fresh independent Gaussian matter, independent record noise, a supplied hard partition with average block volume $v=N/B$, fixed geometry-independent source priors and source-support fan-in cap $d_*$. Let $S$ contain $r$ uniformly sampled distinct original receivers. Conditional on complete geometry $G$, standardized parent matter $Y$ is a rank-$KB$ Gaussian projection. The good/bad link split and uniform generator second moment $M$ give the actual difference-record bound, for $g>1$,

$$
\frac{I(O_S;Y\mid G,S)}r
\le \frac K v(1+d_*g^2)
+\frac{KM}{2}\left[\frac{\log3}{(\log g)^2}+\frac2{\log g}\right].
$$

Choosing $g=v^{a/2}$ with $0<a<1$ makes the bound vanish. This information is the joint KL penalty for dropping parent matter context while retaining the exact geometry and original-record marginal. Shared sender matter, correlated nonlinear links and reverse copies remain in one joint law. The receiver term and $\log3$ distinguish the native difference record from a separate single-source channel.

Complete primitive geometry is additional $O(N)$ source memory on the lattice. The bound does not construct a compressed complete RG state. It averages original queries; fixed patches and adaptive queries need separate estimates. Growing whole-vector KL needs $r\varepsilon(v,g)\to0$. The uniform prior moment has not been transferred to the native all-prefix posterior, recognition dynamics or formation-conditioned law, and the finite constant is not evaluated as a usable tolerance.

The argument was reconstructed directly; document links, display delimiters and whitespace were checked. No new symbolic execution, test suite, experiment, GPU allocation, active-config change, historical retry or manuscript edit occurred. No formal verification-ledger closure is claimed. All four full RG gates and the global reward-law choice remain open. The user requested a break at this checkpoint; publication precedes pausing the unfinished goal.

## Relevance to this research

[[Gauge-Theoretic Multi-Agent VFE Model]] gains a nonlinear-prior decoder estimate with explicit memory and query restrictions. [[Renormalization-group flow of beliefs]] still requires controlled geometry compression, compatible joint copy/product/cancellation operations and native posterior or dynamical hypotheses. Another marginal statistic alone does not close these gaps.
