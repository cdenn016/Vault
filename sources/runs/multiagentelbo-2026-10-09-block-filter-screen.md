---
type: run
title: "Paired N512 block-Gaussian filter projection and sparse update screen"
aliases: ["N512 saved-endpoint parent-block Gaussian screen"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/spd-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# Paired N512 block-Gaussian filter projection and sparse update screen

This intake records [MultiAgentELBO PR234](https://github.com/cdenn016/MultiAgentELBO/pull/234), frozen source merge `97e2de200737bcfd285e58d731ada0981cdf1498`, and [PR235](https://github.com/cdenn016/MultiAgentELBO/pull/235), result commit `7b6140a57354a4beaaff839c9a1893d00d4d23a9` and merge `055cf23644ebd83f40d34595b427db328d68db8c`. Five supplied Gaussian endpoints are projected, and four sparse updates of one compressed old endpoint are checked at paired archived observations. Both scientific consumers complete on their first invocation. The Gaussian component is smaller and its observed projection losses are small; a projected evolving-history error allowance remains unevaluated.

```bibtex
@misc{codex2026blockfilterscreen,
  author = {Codex},
  title = {Paired N512 block-Gaussian filter projection and sparse update screen},
  year = {2026},
  howpublished = {MultiAgentELBO research records, pull requests 234 and 235},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/235}
}
```

## Declared approximation and scope

[R3-BLOCK-GAUSSIAN-FILTER.md](https://github.com/cdenn016/MultiAgentELBO/blob/055cf23644ebd83f40d34595b427db328d68db8c/docs/research/2026-10-03-latent-link-rg-plan/R3-BLOCK-GAUSSIAN-FILTER.md), equations (1)-(8), continues the existing root/free coordinates and Gaussian endpoint of [[multiagentelbo-2026-10-09-recursive-parent-kernel]]. It uses the supplied first forest: N512/K2, 128 parents with four agents per parent, 256 root coordinates and 768 free coordinates. Original source support, 1024 shared primitive reversal pairs, complete retained geometry and mean-and-precision probe remain. The fixed numerical profile is q9, mass 16, h=1/40000, T=.05, observed matter/source slice 2 and all four generator slices at c_*.

For the original constraint Ax=M, write x=r_A+H_A u with AH_A=0 and identity free rows. The full physical Gaussian has positive definite free covariance Cff. Its projection preserves its free mean and every complete six-coordinate parent block, replacing Cff by D=blockdiag(Cff_II). Root reconstruction retains the actual archived transport matrices. The common fiber map is a bijection, so the forward projection KL is

$$
K_{proj}=D(q\Vert\overline q)
=\frac12\left(\sum_I\log\det C_{ff,II}-\log\det C_{ff}\right).
$$

The trace term cancels because each diagonal block of D^(-1)Cff is the identity. Complete within-parent root/free and cross-child marginals remain; individual-child independent marginals would be a different approximation. Passive agent frame changes within the declared parent groups preserve this projection, as proved in the code note. Neither deleting between-parent correlations nor finite coordinates alone establish a native common-measure regular decoder.

Starting from the projected old Gaussian, the unchanged selected-mean affine step has physical prediction P=F H_old D H_old^T F^T+Q, with the original strictly positive Q. After the new observation, the helper solves the complete sparse V=A_new P A_new^T and streams each exact free conditional diagonal block P_II-U_I V^(-1)U_I^T, U=P A_new^T. Projection occurs after this global conditional solve. The free conditional log determinant follows from logdet P+2log|det A_new,r|-logdet V. No independent per-parent V solve, covariance floor, clipping, jitter or mean-force replacement occurs. Between-parent coupling and LU fill remain global.

[The frozen screen contract](https://github.com/cdenn016/MultiAgentELBO/blob/055cf23644ebd83f40d34595b427db328d68db8c/docs/research/2026-10-03-latent-link-rg-plan/R3-BLOCK-FILTER-SCREEN-CONTRACT.md) fixes one old H2/q2 and the four already generated A3/M3 pairs from the full-Gaussian-reference study. The endpoint is the last block of each saved two-time Gaussian, not the old marginal smoothed by the new observation. All four online arms start from the same one projected old state. No hidden fine realization, future chart y, original noise or success event is used. Packing archived transports at weight .25 generates no readout or field. These paired functional comparisons are neither independent networks nor an evolving projected-hybrid trajectory, and they provide no statistical estimate or reference-history expectation.

## First computational outcome

[R3-BLOCK-FILTER-SCREEN-RESULTS.md](https://github.com/cdenn016/MultiAgentELBO/blob/055cf23644ebd83f40d34595b427db328d68db8c/docs/research/2026-10-03-latent-link-rg-plan/R3-BLOCK-FILTER-SCREEN-RESULTS.md) reports the independent reader's computational Gaussian values below, in nats. Its full-reference-to-online KL includes the changed old prior and resulting mean as well as correlation projection; it is distinct from either projection KL.

| Saved case | Full endpoint projection KL | Online conditional projection KL | Full reference to online block KL |
| --- | ---: | ---: | ---: |
| Old q2 | 3.5303041540458145e-8 | n/a | n/a |
| Draw 0 | 1.4121727908884414e-7 | 6.276918641546147e-8 | 1.4121729396120454e-7 |
| Draw 1 | 1.412150402203824e-7 | 6.276769072009672e-8 | 1.4121505965198417e-7 |
| Draw 2 | 1.41216963055332e-7 | 6.276897684782838e-8 | 1.4121698281546117e-7 |
| Draw 3 | 1.4121585713398536e-7 | 6.27682380821492e-8 | 1.4121587484589393e-7 |

The old projection Pinsker ceiling is .00013285902592684125; the four endpoint ceilings are about .00026572. Complete same-parent mean/covariance discrepancies are at most 1.0547118733938987e-15/1.6940658945086007e-20. These are finite saved-Gaussian comparisons, with no scientific pass threshold or posterior-accuracy interpretation. The producer's sparse Schur/determinant calculations and reader's independent original-noise complete QR, thin free-factor QR and whitened eigenvalue/log1p KL pass 8,255 comparisons over 3,477,645 entries. Maximum discrepancy is 2.9284890750571894e-12 under frozen mean/covariance/logdet-KL allowances 1e-10/1e-12/1e-9. No interval arithmetic certificate follows from floating agreement.

The Gaussian free means and covariance blocks use 43,008 bytes, compared with 8,396,800 bytes for the full physical mean/covariance. The roughly 195-fold difference concerns only those Gaussian arrays. Original IDs, root reconstruction, current R, source/model, geometry, rule, probe, decoder and likelihood ancestry remain additional costs. Each online P has 55,296 stored entries/667,652 bytes and V has 6,656/80,900 bytes. Their LU factors occupy 3,194,968/340,648 bytes respectively; permutations, other sparse matrices and streamed dense solves are charged separately. These measurements establish no uniform sparse-fill, linear-work, size/depth or total-codec bound.

Producer time is 11.694633900071494 seconds, peak 147,816,448 bytes; reader time is 6.211610900005326 seconds, peak 293,064,704 bytes. Dense oracle allocations remain included. Fourteen new archives contain 761,413 logical bytes/498,215 compressed bytes. The 15 direct input and 18 source snapshots occupy 185,371,569/143,001 bytes. Root matches 2,016 reader bindings and copies/rechecks all 49 replay files/192,085,372 bytes with exact canonical parity. The unchanged linked prior package retains all 1,011 files/779,502,238 bytes and its original state/model/history costs without another copy. The complete current replay is `MultiAgentELBO/artifacts/gaussian-block-filter-screen/r3-n512-block-filter-screen-20261009/`.

Seven pre-outcome tiny fixtures pass, with zero failures/errors/skips: producer two/.316 seconds, block helper three/.410 and independent reader two/.366. The producer's original missing-module and syntax collection failures and reader's initial missing-module collection result remain in two preserved receipt files. There is no scientific failure, retry, producer rerun or passing-fixture rerun. This intake executes no tests or science.

Runtime producer receipt is 42,796 bytes/SHA256 `fe5ec4cfbe8dfc8b3af494b704e8c7527f38f0bf2a494867066296ea251c1238`; runtime independent receipt is 6,029,791/`cf5f9d11fa00a9a8da514f4e98339d381d00dd45eba278077d0ca050f3439bd5`. The canonical package manifest is 11,025/`ada622005546457a2755c8f1b8fe1e447988d04b1151b41126a2c1e8ba5b1ffc`. Canonical Desktop code bindings at result merge `055cf23644ebd83f40d34595b427db328d68db8c` are: block-filter proof 16,055/`0b63cdde7da34cff279cbd84aeb8ded07746b736858d1423284d6266ef2e2b3d`; contract 12,833/`f3b6b50c0e49666292eb0eb073fbdad76adf670a1772af51a547eff7aa314452`; results 4,426/`a2e9fd970155eeeb366ad7ef568602160c5e50ae6815290ee3116cf84bb71bf5`. Runtime source snapshots retain executing bytes separately from Git-normalized checkout bytes; the original producer source snapshot is 19,210/`a65eab71fe44808455e1700bffe002918ebe76d434627de497be21553171d6e3`.

## Relevance to this research

This continues [[Renormalization-group flow of beliefs]] and [[Staged hierarchy formation and RG composability]] toward a declared projected Gaussian predictor whose correlation loss is charged. It changes the reference's hidden covariance approximation, preserving the original fine kernel and within-parent marginals. The proof's new accumulated allowance is the projected-hybrid expectation of capped original-kernel chart costs plus next conditional projection costs. The whole local sum may be capped only after its separate averaged contributions; a pointwise inner cap is not justified. At held-fixed H2, inherited actual-to-q2 startup error and initial q2 projection error are both charged. Known initialization is a different start, with an exact first parent-block projection.

That useful history expectation remains unevaluated. The four matched observations were not generated under an evolving projected hybrid and cannot replace that expectation or establish Monte Carlo accuracy. The existing fixed-H2 actual-law bound in [[multiagentelbo-2026-10-09-fixed-prefix-native-error]] and unrestricted raw entropy/stopped-budget limits in [[multiagentelbo-2026-10-09-compact-raw-history]] retain their distinct scopes. No nonlinear actual-filter assimilation, actual p3 identification, native episode or continuous Fisher equivalence, common-measure Chapter 11 regular closure, growing size/depth, endogenous formation or RG completion is proved. [[Gauge-Theoretic Multi-Agent VFE Model]] keeps all four RG gates open and the full goal active; the GPU remains user-owned and the 144-case CUDA grid remains unrun.
