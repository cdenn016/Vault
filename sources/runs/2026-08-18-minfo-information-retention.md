---
type: run
title: "M-info: boundary mutual-information retention deflates the sup-norm capacity story (2026-08-18)"
aliases:
  - "M-info measurement"
  - "2026-08-18 information retention"
  - "MI capacity statistic"
tags:
  - cluster/multi-agent
  - cluster/gauge-theory
  - cluster/vfe
  - project/multi-agent
  - field/physics
  - field/statistics
created: 2026-08-18
updated: 2026-08-18
---

# M-info: boundary mutual-information retention deflates the sup-norm capacity story (2026-08-18)

> [!info] Provenance and evidence boundary
> Repository `MultiAgentELBO`, amendment 9 pre-registered in
> `docs/superpowers/specs/2026-08-17-rescaling-map-design.md` before running; implementation
> and results committed at `f904d5c` (same day as the audit remediation `4eed61f`,
> [[2026-08-18-rescaling-audit-capacity-reversal]]). Interpreter `C:/Python314/python.exe`,
> numpy 2.4.4, CPU, exact marginalization on both sides; the declared seed revalidated
> against the published chain (site sup 1.4321, pair sup 0.0163) before measurement. Tests pin
> the constant-sector control, the ceiling, determinism, and gauge invariance of the statistic.

## The statistic

$R_{\mathrm{MI}} = I(P_1;P_2)\,/\,I(X_{B_1};X_{B_2})$: boundary mutual information between
the first two coarse parents under the coarse law, against the same quantity between their
child blocks under the fine law, both in nats. Because the coarse law is the exact pushforward
of the fine law through the per-block Bayes kernels and each parent depends only on its own
block's children, the [[Data processing inequality]] gives $R_{\mathrm{MI}} \le 1$ as a
theorem. The statistic is a functional of the law alone — invariant under parent relabelings
and per-site state permutations — so it is alphabet-comparable and gauge-invariant by
construction, the property the sup norm had to have repaired into it (audit F8).

## Results (declared 6-cycle panel, ratio two)

| quantity | offsets $\{1\}$ ($k=1$) | offsets $\{1,2\}$ ($k=3$) |
|---|---|---|
| ceiling $I(X_{B_1};X_{B_2})$ | $4.97 \times 10^{-6}$ nats | $1.49 \times 10^{-5}$ nats |
| $R_{\mathrm{MI}}$, nine-state parents | 0.0230 | 0.0667 |
| $R_{\mathrm{MI}}$, 27-label root-framed sector parents | 0.0254 | 0.0702 |
| relative sector gain | +10.2% | +5.3% |
| constant-sector control | exact | exact |

The sector gain of amendment 8 survives in the law — direction confirmed at both boundary
multiplicities — but the magnitudes deflate: the blocking transmits only 2–7% of the boundary
information, against sup-norm retentions of 0.156–0.568, and the sector gain is +10%/+5%
rather than the sup norm's +34%/+29%. The ceiling itself is tiny because the declared seed's
pair coupling is weak (sup 0.0163); everything is seed-local by declaration.

## The one-parameter reading

> [!note] Editorial: back-of-envelope consistency check, not a derivation.
> For weak dependence $I \approx \tfrac{1}{2}\chi^2$ is quadratic in the correlation. With a
> single per-cut-edge transmission factor $t \approx 0.156$ and coherent aggregation of $k$
> cut edges into one coarse pair table, $R_{\mathrm{sup}} \approx k\,t$ and $R_{\mathrm{MI}}
> \approx k\,t^2$ reproduce all four nine-state numbers within ~10% (predicted 0.156/0.47 and
> 0.024/0.073 against measured 0.156/0.441 and 0.023/0.067). The same check exposes the
> sup-norm sector gain as mostly coordinate inflation: a genuine +34% transmission rise would
> force a +79% MI rise, and the measured rise is +10%.

## The structural moral

Regeneration restores interaction without restoring information. The fine boundary information
is gone at $\sim t^2 \approx 2\%$ per step — unrecoverable by any rule operating on the coarse
law — while the regenerated attention rebuilds coarse coupling from the two objects blocking
conserves exactly, the Wilson-line connection and the coarse beliefs. Hierarchies of this kind
maintain *structure* all the way up while microscale *information* dies within levels; the lab
now measures the two with different instruments (pair sup for structure, $R_{\mathrm{MI}}$ for
information). The empirical anchor for the same split in neuroscience is
[[zheng-meister-2025-unbearable-slowness]] ($10^9$ bits/s consumed, ~10 bits/s emitted), and
the one rigorous sense in which a macro level can nevertheless "beat" micro — interventional
effective information, not observational — is [[hoel-2013-causal-emergence]].

## Relevance to this research

Closes ROADMAP item 2 (the alphabet-comparable capacity statistic) and prices item "extended
downward kernels": a confirmed but small sector gain at a weakly correlated seed says pair
that construction with a stronger seed or a richer sector map, judged by M-info, before
investing. The Cooper-pair reading of sector-carrying parents is backed by
[[bcs-1957-theory-of-superconductivity]].
