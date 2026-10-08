---
type: run
title: "MultiAgentELBO L5 minimum covariance growth and fixed-record decoder limits"
aliases: ["L5 minimum covariance and fixed-record information limit"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/physics, field/statistics]
created: 2026-10-07
updated: 2026-10-07
---

# MultiAgentELBO L5 minimum covariance growth and fixed-record decoder limits

For the actual independent Gaussian GL(2) control and supplied equal-weight dyadic tree, the minimum covariance has exponential rate $s^{-1}\log\lambda_{\min}(V_s)\to3\gamma$, complementing the established maximum rate $4\gamma$. This closes a missing premise for the existing original-record decoder. A fixed finite original patch eventually inside the origin block loses conditional information in standardized parent matter; one-depth joint KL, fixed-window total variation and fixed-observation posterior limits follow. Retained geometry and hidden-mark raw contexts remain separate. This is an analytical result for this supplied channel at arbitrary growing size, with no simulation or GPU calculation.

## Source and derivation

Codex (2026), *L5 minimum covariance growth and fixed-record decoder limits*, MultiAgentELBO analytical research record, published revision `c2dff71d1c933443f6138bde43cba21db0db2c83`. The [derivation](https://github.com/cdenn016/MultiAgentELBO/blob/c2dff71d1c933443f6138bde43cba21db0db2c83/docs/research/2026-10-03-latent-link-rg-plan/L5-COVARIANCE-DECODER-LIMIT.md), [separate bounded reconstruction](https://github.com/cdenn016/MultiAgentELBO/blob/c2dff71d1c933443f6138bde43cba21db0db2c83/docs/research/2026-10-03-latent-link-rg-plan/L5-COVARIANCE-DECODER-LIMIT-CHECK.md), and [source intake](https://github.com/cdenn016/MultiAgentELBO/blob/c2dff71d1c933443f6138bde43cba21db0db2c83/docs/research/2026-10-03-latent-link-rg-plan/evidence/l5-covariance-decoder-intake-20261007.json) preserve the actual-tree geometry, hypotheses, finite-size bounds, conditioning and convergence distinctions. Normalized UTF-8 LF report SHA256: `46cabb79e5257d472455e746ad98397fc3a324941b4aa8c83a15f0ad53e37990`. This identifies the inspected text and does not constitute mathematical acceptance by itself. The separate reconstruction uses the same inherited model, with no formal ledger closure or independent-model adjudication.

```bibtex
@misc{codex2026l5covariancedecoder,
  author = {Codex},
  title = {L5 Minimum Covariance Growth and Fixed-Record Decoder Limits},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/blob/c2dff71d1c933443f6138bde43cba21db0db2c83/docs/research/2026-10-03-latent-link-rg-plan/L5-COVARIANCE-DECODER-LIMIT.md},
  note = {MultiAgentELBO analytical record, revision c2dff71d1c933443f6138bde43cba21db0db2c83}
}
```

## Covariance geometry and quantitative control

This extends [[multiagentelbo-2026-10-07-l5-path-growth]] and [[multiagentelbo-2026-10-07-l5-normalized-marks]]. For $s=2h$, the two actual paths to $(h-1,2h-1)$ and $(2h-1,2h-1)$ have disjoint primitive sets, lengths $3h-2$ and $4h-2$, and independent uniform leading singular lines. Their rank-one covariance terms give the lower bound. Every bottom-half path shares the ordered prefix $Q_h$; testing perpendicular to its leading left singular line gives the matching upper bound without assuming residual-path independence.

For $0<u\le\gamma h/2$ and $w>0$, the stated lower/upper bounds fail with probability at most $(2s^2+4)e^{-u^2/(128vh)}+e^{-w}$. A parent union gives $(2N+4P)e^{-u^2/(128vh)}+Pe^{-w}$, $P=N/s^2$. The minimum rate is uniform in probability on matching nonwrapping diagonals with $\log N=o(s)$ and almost sure for nested dyadic origin blocks or the explicit summable diagonal. Finite unions extend it to a fixed episode horizon despite temporal link correlation.

Together with the maximum rate, $s^{-1}\log\det V_s\to7\gamma$ and $s^{-1}\log\kappa(V_s)\to\gamma$. Scalar normalization cannot keep both eigenvalues nondegenerate. The exact identity root term gives $V_s\succeq s^{-4}I$, controlling bad events and proving $\mathbb E\|V_s^{-1}\|\to0$. These rates use the existing carried baseline metric. They are spatial/covariance rates, not an O3 connection metric, O5 spectrum or RG linearization exponent.

## Existing original-record decoder and information

Fix a finite original-record patch whose receiver/candidate nodes eventually lie in the origin block. Its shared-node observation remains $O=H_\ell(X)z+\eta$ with positive noise covariance $R_0$. Fixed-node binary transports stabilize. The cross covariance $C_s=\operatorname{Cov}(O,Y_s\mid X,\ell)$ equals $s^{-2}B_\ell(X)V_s^{-1/2}$ with a fixed finite bracket. It decays at least at logarithmic rate $-3\gamma/2$. The exact decoder is $N(m_O+C_sy,V_O-C_sC_s^\top)$, whose residual is at least $R_0$.

Its conditional record information is $I_s=-\log\det(I-Q_s)/2$, $Q_s=V_O^{-1/2}C_sC_s^\top V_O^{-1/2}$, and tends to zero. The depth-independent noise envelope $I_s\le\log(\det V_O/\det R_0)/2$ is integrable for this finite Gaussian patch. Therefore expected information vanishes, and the joint law of $(X,\ell,O,Y_s)$ factorizes from a standard Gaussian in KL. Any size-dependent retained mark inherits this error bound relative to its actual marginal; convergence of that mark law is not implied.

For a fixed window $(Y_s,Y_{2s},\ldots)$, the exact cross covariance is $(s/t)^2V_t^{-1/2}V_s^{1/2}$, $t=2^ks$. Its upper logarithmic rate is $2\gamma-3\gamma2^k/2<0$. Conditional covariance tends to identity, giving joint total-variation factorization from the shared history and original records. For every fixed observation $o$, the same window factorizes in total variation from the depth-independent posterior $P(X,\ell\mid o)$. A fixed finite episode horizon follows using fresh conditional matter. The window's expected KL to a full iid product requires a further integrability estimate and is not claimed.

## Relevance and remaining obligations

The result supplies a precise information-discarding mechanism for the [[Gauge-Theoretic Multi-Agent VFE Model]] and [[Staged hierarchy formation and RG composability]] studies. It advances [[Renormalization-group flow of beliefs]] without identifying the full retained parent with its matter marginal. Original retained geometry can still predict records; a fixed hidden-mark raw context still reweights links through its mean/covariance likelihood. The result covers a fixed patch and fixed depth window, not moving boundary queries or every parent's prediction at once.

The compatible full noncentral all-copy/boundary mark and evaluator limit remains open, including signed matrix normalization, shared-axis scale memory and the behavior of inverses/decoder access. Gaussian growth estimates do not transfer to the nonlinear action. Original joint descent, autonomous predictive/flow control, endogenous formation, O1/O3/O4/O5 and sparse-graph S1 remain unfinished. Both N8192 reconstruction failures stay unresolved. No active control, source support, loop family, manuscript or historical run changed. The user requested publication and then a break; this checkpoint does not complete the overall goal.
