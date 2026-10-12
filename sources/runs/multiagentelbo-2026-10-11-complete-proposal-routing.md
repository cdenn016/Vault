---
type: run
title: "MultiAgentELBO complete-state outward proposal routing"
aliases: ["Gaussian complete-state proposal routing"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/spd-geometry, cluster/vfe, project/multi-agent, field/mathematics, field/statistics, field/cs-ml]
created: 2026-10-11
updated: 2026-10-11
---

# MultiAgentELBO complete-state outward proposal routing

An additive CPU wrapper routes the original saved-noise Fisher proposal across all five exact-reference state families. One new analytic fixture passes once: JUnit records one test, zero failures/errors/skips and 0.127 seconds. Its first missing-module failure (.126 seconds) is preserved without replay. Full N512 field/proposal/codec/native transfer remains unrun; all four RG gates stay OPEN near subjective 65% at c_*.

## Construction and evidence

[Code PR309](https://github.com/cdenn016/MultiAgentELBO/pull/309) uses source 7b5019d958d1eed6025a58c3d8e002dc30fd4456. The [code record](https://github.com/cdenn016/MultiAgentELBO/blob/7b5019d958d1eed6025a58c3d8e002dc30fd4456/docs/research/2026-10-03-latent-link-rg-plan/R2-COMPLETE-PROPOSAL-ROUTING.md) and [validation](https://github.com/cdenn016/MultiAgentELBO/blob/7b5019d958d1eed6025a58c3d8e002dc30fd4456/docs/research/2026-10-03-latent-link-rg-plan/evidence/r2-state-proposal-validation-20261011.json) bind the final 7,870-byte wrapper, 6,435-byte fixture and first red/green receipts. Validation is 4,905 bytes / SHA256 bbda690d6993331fe2600cd7ecd000ad73521e6b5610c3b65a8535cb761dbc30.

Actual Desktop main/HEAD/origin/main and the task worktree agree at merge 63d348d0040fe3fb391c030c92c4d96bad0e0f21, with clean tracked content.

The interface fisher_state_proposal_ball(noise,state,direction,dt,temperature) consumes decoded Fraction state, supplied object-Arb direction and saved float64 noise converted to exact rational balls. Matter uses its covariance; generators invert stored precision, apply the existing lower covariance-Cholesky proposal and invert the candidate back to precision. Every generator episode is updated, including future episodes beyond the matter prefix. Source hard zeros remain exact; output row sums are enclosures containing one, with exact simplex centering left to the endpoint codec. Only known-symmetric matrices are averaged. Finite/SPD checks stop without floors, repair, precision retry, projection or new randomness.

The C1/N1/K2/T2/E1/D4/A3 fixture contains 49 coordinates and 392 noise bytes at 256-bit Arb precision. Distinct future-link means, noise and exponents, correlated covariances and lower sampling charts ground routing. Supplied analytic directions isolate it from the full field. This tiny case validates the adapter; it does not admit a native trajectory or direct large-network science.

## Remaining full-scale work

The next N512 input mapping uses the retained-reference input snapshot and original trajectory model.npz: matter_J_0, matter_H, matter_sources, matter_link_index, matter_reverse and matter_tau map to the existing consumer's J_0, H, sources, link_index, reverse and tau. Original offsets/rule and step-zero noise remain separate complete inputs. The saved binary controls are h=7378697629483821/295147905179352825856 and temperature=3602879701896397/72057594037927936, with mass 16; they differ from the exact rational formal controls and require their own transfer charge.

Prospective state, direction, noise and output each occupy 97,280 logical slots. Routing requires 5,632 Gaussian and 1,536 source proposals, plus 4,096 inversions in each direction. Parent work includes 6,144 receiver and 6,144 sender incidences, 8,192 loop-factor incidences and 6,144 history contributions. These counts are not measured memory bytes. Full caches, conversion, arithmetic radii, output and process costs remain pending; the earlier 406.916-second kernel estimate is not a full-field budget.

## Relevance to this research

This continues [[multiagentelbo-2026-10-11-process-fisher-cpu]], [[multiagentelbo-2026-10-11-outward-fisher-arithmetic]] and [[multiagentelbo-2026-10-11-recognition-code]], in the live g11 record/loop and c10 complete-carrier context. Both-channel compatibility, actual-law prediction, compact segments/exits, repeated continuation, growing limits and persistent hierarchy remain open.

The user requests a break after commit/push/merge and actual canonical fast-forward. Next resume charges complete parent work and freezes full-state arithmetic/proposal admission. No GPU/probe, Torch, model/default/config/host or theory change occurs; GPU access requires explicit authorization.

~~~bibtex
@misc{codex2026completeproposalrouting,
  author = {Codex},
  title = {Complete-State Outward Proposal Routing},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/309},
  note = {One new tiny CPU fixture; complete N512 execution and native transfer unrun}
}
~~~
