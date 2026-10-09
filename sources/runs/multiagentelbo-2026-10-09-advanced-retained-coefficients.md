---
type: run
title: "Advanced retained-state coefficients and Gaussian endpoint recurrence"
aliases: ["N512 complete new R2 coefficient packet and recursive reference endpoint"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/spd-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# Advanced retained-state coefficients and Gaussian endpoint recurrence

This intake records [MultiAgentELBO PR226](https://github.com/cdenn016/MultiAgentELBO/pull/226), source commit `88401cb0f40e0c5a7a0a9ed0b1be11b36afd1709`, merge/frozen execution `1f2fee08de1191df401bcc4a677986560a065baf`, and [PR227](https://github.com/cdenn016/MultiAgentELBO/pull/227), outcome commit `04d1e938c090313e5ee7f2c35eb18059db72631a`, merge `a00d6c60489a7ce6903601f11aeffbf6ed50191a`. One new packet reconstructs complete native transition coefficients at the causally generated retained state R2. A separate Gaussian identity carries the existing reference endpoint recursively, with horizon-independent mean/covariance storage. No new proposal, nonlinear likelihood assimilation or compact native filter is executed by this batch.

```bibtex
@misc{codex2026advancedretainedcoefficients,
  author = {Codex},
  title = {Advanced retained-state coefficients and Gaussian endpoint recurrence},
  year = {2026},
  howpublished = {MultiAgentELBO research records, pull requests 226 and 227},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/227}
}
```

## Advanced-state causal coefficient packet

[The frozen contract](https://github.com/cdenn016/MultiAgentELBO/blob/a00d6c60489a7ce6903601f11aeffbf6ed50191a/docs/research/2026-10-03-latent-link-rg-plan/R3-GENERATED-RETAINED-COEFFICIENT-CONTRACT.md) consumes the completed [[multiagentelbo-2026-10-09-generated-prefix-filter]] archive for the same `depth-0-prefix-1-draw-0` case and 128 supplied parents. Retained preceding-slice means, all matter covariances/source rows and all four current generator mean/precision slices are decoded. The selected matter mean anchor is the causal prefix-two Gaussian endpoint mean. It is a measurable point for polynomial reconstruction, not a realized generated hidden mean or a conditional expected force. Generated hidden means, realized noises, future R3 coordinates and future episode records are excluded. The observed episode prefix remains 0-2; inference prefix two is a different index.

The fixed profile remains N512, K2, 1024 primitive reversal pairs, three observed matter/source slices, four generator slices, mass 16, literal order-nine nodes/weights, h=1/40000 and T=.05. One complete common-state finite-rule Fisher point field uses all four advanced generator slices, including the generator-only fourth slice and every prior, ordered-loop, kinetic, sender and receiver term. Seven explicit moment banks inside that field and one additional selected bank precede checkpoint replays. Selected K,h0 supplies the full hidden mean force Kx-h0 and its diagonal matter precision target, with incoming and outgoing records preserved.

The new selected response bank has 14 independent mean/symmetric-precision coordinates for every primitive, 14,336 coordinates in total. Complete new-R2 prediction banks export 1,536 source, 4,096 generator-mean and 10,240 generator-covariance rows, totaling 15,872. Every row retains B,b,c, supports and IDs, with no future y. The new packet reconstructs the complete original JointDirection at a supplied hidden x while preserving Fisher preconditioning and covariance-to-precision coupling. Source recovery uses supported contrasts; setting a supported reference gradient to zero changes only the irrelevant common row constant. Old-R1 banks remain the completed R1-to-R2 likelihood, and are not reused as forces at R2.

[The result](https://github.com/cdenn016/MultiAgentELBO/blob/a00d6c60489a7ce6903601f11aeffbf6ed50191a/docs/research/2026-10-03-latent-link-rg-plan/R3-GENERATED-RETAINED-COEFFICIENT-RESULTS.md) reports anchor recovery errors of 3.428701766949871e-12 in generator mean covectors, 2.465583293087548e-12 in supported source contrasts, 8.526512829121202e-14 in generator precision targets and 1.332267629550188e-15 in selected matter precision targets. These are floating discrepancies within the frozen 1e-8 field allowance, without an accuracy target or interval certificate. The unchanged guarded degree-24 response construction approximates derivatives of the literal finite rule; population integration, response approximation and computed matrix/factor/solve/contraction arithmetic remain excluded.

## Reference endpoint recurrence and its scope

[R3-GAUSSIAN-ENDPOINT-RECURRENCE.md](https://github.com/cdenn016/MultiAgentELBO/blob/a00d6c60489a7ce6903601f11aeffbf6ed50191a/docs/research/2026-10-03-latent-link-rg-plan/R3-GAUSSIAN-ENDPOINT-RECURRENCE.md), equations (1)-(3), starts from the existing Gaussian reference endpoint N(m,C), allowing singular C, and the original physical affine increment X'=FX+d+epsilon with covariance Q>0. Joint conditioning on the new full-row-rank parent constraint AX'=M gives both the smoothed old marginal and the new endpoint, including cross-covariance. Only the nonsingular observation covariance A(FCF^T+Q)A^T is solved. Regression and conditional Markov factorization show inductively that carrying the new m,C gives exactly the endpoint of joint Gaussian conditioning on every available parent constraint. No old constraint is dropped and no belief-covariance reset occurs. This equality concerns the Gaussian reference; the native nonlinear retained likelihood remains a separately controlled tilt.

[gaussian_endpoint_reference.py](https://github.com/cdenn016/MultiAgentELBO/blob/a00d6c60489a7ce6903601f11aeffbf6ed50191a/experiments/gaussian_endpoint_reference.py) implements that reference recurrence with physical covariance and Cholesky solves, retaining null directions without a floor. Three tiny fixtures independently compare complete chronological-noise QR endpoints and last-two-time joints, including smoothing, cross-covariance and zero-initial-uncertainty increments. They ground this Gaussian identity only. Persistent Gaussian state has p+p^2 float64 entries with p=NK, or 8,396,800 bytes at N512/K2, independent of inference horizon. Dense propagation, temporary two-time joints, complete retained R, model and likelihood coefficients remain charged. This is neither network-size compression nor a Chapter 11 regular finite-filter, common dominating-measure decoder or native RG closure.

## First invocation, independent readback and resources

The independent reader reconstructs all four advanced generator-slice fields, including 16,384 generator mean and 65,536 full precision-target entries, selected moments/responses, complete K,h0, every prediction bank and the anchor identities. All 2,904 comparisons over 4,820,139 entries pass, maximum absolute discrepancy 3.283484595328900e-13. Producer and reader each complete on their first scientific invocation without failure or retry. The seven distinct pre-outcome tiny cases, including the three endpoint QR cases, remain passing without a post-science rerun.

Producer time is 384.458152 seconds with cumulative peak 1,648,009,216 bytes; reader time is 131.391206 seconds with peak 153,321,472 bytes. Thirteen output NPZ archives contain 25,976,288 logical bytes and occupy 7,129,420 compressed bytes. Historical input/source snapshots occupy 242,084,079/409,870 bytes. The expanded quadrature array has about 860 million logical bytes but is a zero-additional-storage view; checkpoint/autograd work and temporaries remain covered by elapsed/peak measurements and separately reported logical costs. No new model/config, proposal, trajectory, observation, noise draw or GPU operation occurs.

All 431 producer input, 34 source and 944 reader bindings match original/snapshot lengths and hashes. The canonical replay at `MultiAgentELBO/artifacts/generated-retained-coefficients/r3-n512-generated-retained-coefficients-20261009/` contains 480 files and 252,394,861 bytes with full count/length/SHA256 copy parity. Runtime producer receipt is 742,643 bytes, SHA256 `6dd3000d00cd0f03e766b8fc7d414da3920b2def79710bae5085fa71c52d8805`; reader receipt is 2,028,849 bytes, SHA256 `b568f0402909acf03cff3954f6d9946091a0231d9966f53a7a2c812874e7053a`. The replay manifest is 238,444 bytes, SHA256 `80ef0deaba098d0bfbccdf3e3541bdefc8da4324ccfab34f217d96c1c2e500e4`. Executed snapshots preserve original bytes separately from Git newline normalization of tracked copies.

Additional canonical Desktop code bindings at merge `a00d6c60489a7ce6903601f11aeffbf6ed50191a` are: contract 12,187 bytes, SHA256 `ea8ec5931527b8e6538c58eb2b07ff0a95edf39ba345c01d716d907726688302`; result 4,977 bytes, SHA256 `03dd09a8314a2098a289c5d4ae59f0c717110a4f915451a6a7082f2378afd45a`; endpoint note 4,894 bytes, SHA256 `56faafc5d6c436579eb2f077e9b2c73c43e1b5fcfcb1a8d7ada9eab12d986ce3`; endpoint helper 2,546 bytes, SHA256 `e4769aca0b27e8572e262825b39d02c4098af228d819b61a1bfe6dcd15f52617`. These intake checkout bindings do not replace runtime source ancestry.

## Relevance to this research

This packet completes the advanced-state coefficient seam identified in [[multiagentelbo-2026-10-09-generated-prefix-filter]] and needed for the next original causal transition in [[Renormalization-group flow of beliefs]]. It preserves original geometry/source identities and the full Fisher law described by [[Staged hierarchy formation and RG composability]]. It supplies coefficients and a finite-dimensional Gaussian reference endpoint, not an assimilated nonlinear filter, conditional mean-force dynamics or integrated posterior.

The next recursive-kernel preparation is in progress: draw from the current physical endpoint fiber, apply the original new-R2 kernel and compare the same-joint downward conditional at generated R3/M3 with the recursive Gaussian reference. No new proposal from this coefficient packet has an outcome at this publication. [[Gauge-Theoretic Multi-Agent VFE Model]] retains actual-history accumulation, nonlinear posterior integration, compressed native closure, continuous/native-posterior accuracy, endogenous formation and growing size/depth as open obligations. All four RG gates remain open, the goal stays active, the GPU remains user-owned and the 144-case CUDA grid remains unrun.
