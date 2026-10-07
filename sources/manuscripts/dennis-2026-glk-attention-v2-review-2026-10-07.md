---
type: manuscript
title: "Gauge-Covariant Gaussian Attention through Lie-Algebra Links (peer review and revision of October 7, 2026)"
aliases: ["Dennis GLK attention v2 review October 7 2026"]
authors: ["Robert C. Dennis"]
year: 2026
url: "manuscripts/Attention/GL(K)_attention_v2.tex"
tags: [cluster/attention, cluster/gauge-theory, cluster/vfe, project/transformer, project/multi-agent, field/mathematics, field/cs-ml, field/statistics, field/physics]
created: 2026-10-07
---

# Gauge-Covariant Gaussian Attention through Lie-Algebra Links (peer review and revision of October 7, 2026)

## Source and scope

The live sources are [GL(K) attention v2](../../manuscripts/Attention/GL(K)_attention_v2.tex) and [GL(K) supplementary v2](../../manuscripts/Attention/GL(K)_supplementary_v2.tex), revised on October 7, 2026 from the version recorded in [[dennis-2026-glk-attention-v2-rework-2026-10-05]]. The day's work, at the author's request, had four parts: a pointer to the tied key-and-content model of [[dennis-2026-minimal-agent-model]] (main `sec:nonneural` and Supplement Remark `rem:tied_record` with its own proof, without citing the note); a peer review by eight Claude Opus 5.5 investigator lenses (report, lens reports and scripts in `VFE_3.0/docs/manuscript-review-2026-10-07/`); application of every review finding except two declined with reasons; and, after the author's clarification, removal of an earlier baseline study. The settled record is `manuscripts/verified-ledger.md`. Publication: cdenn016/Vault PRs #113, #114 and #115 and the follow-up recorded in `log.md`. No human review has taken place, and the local source may change after this dated record.

## Review findings

The review recommended major revision and found no algebraic error in about two hundred recomputed identities; every reported empirical number reproduced from its run record. The problems were in what the text claimed. `cor:normal_form` was false for the evaluated predictor, whose diagonal covariance storage makes the next layer's reference covariance depend on the frames; with LayerNorm, the MLP and the decoder this means the evaluated predictor is not gauge covariant, although the attention operator is. "Exact source posterior at every temperature" held by construction for any nonnegative cost. The trained $K=128$ links run in single precision, where the trace and leftmost eigenvalues of the stored generators are not identifiable and two of four applied products have negative determinant. The "standard transformer layer is the affine chart" statement needed its hypotheses (post-normalization, no biases, fixed routing). Several published results were uncredited (Elhage et al. 2021 for the head decomposition; Banerjee et al. 2005 and Rubacher 2026 for the dual-coordinate form; Racioppo 2025, Shaj et al. 2026 and Long et al. 2026 for precision-weighted and Kalman receivers; Henry et al. 2020 for QK-normalization; Higham 2008 for the low-rank exponential).

## What the revision states

The title is kept. The abstract and introduction scope covariance to the attention operator and name five channels that break it in the evaluated model; invertibility and inverse edges are stated for exact arithmetic; the implemented holonomy is cyclic for a shared generator; routing weights are the exact posterior of a declared compatibility record and, under a Gaussian comparison record with the key tied to the content, the first mean-field label update. The program thesis is kept as motivation with one falsifiable prediction. The empirical comparison is now the October 6 per-type read-table transformer ([[vfe3-2026-10-06-block-read-baseline]]): 55.10 against 34.48 for the realization at $K=128$, one seed, with its confounds stated, and `sec:needed_experiments` fixes in advance that the frame claim is retracted if the realization does not beat that control by more than the larger of two paired standard errors and 0.03 nats at $K=128$, or if freezing the frames costs less than that margin. The earlier pairs (39.77 against 90.15, 52.91 against 117.63) were removed at the author's direction as an earlier study. The check scripts now print pass tallies (58 of 58 and 71 of 71) and library versions, and the $K=20$ link factors ship as an `.npz`.

## Relevance to this research

This revision is the current state of the main GL(K) attention manuscript of the [[VFE Transformer Program]] and replaces the comparison claims of [[dennis-2026-glk-attention-v2-rework-2026-10-05]]; see [[GL(K) gauge-equivariant attention]].
