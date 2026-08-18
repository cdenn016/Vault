---
type: run
title: "The rescaling-lab audit and the capacity reversal: a gauge-dependent sector charge retired, root-framed retention rises (2026-08-18)"
aliases:
  - "2026-08-18 capacity reversal"
  - "M-capacity re-measurement"
  - "root-framed sector charge"
  - "rescaling-lab audit 2026-08-18"
tags:
  - cluster/multi-agent
  - cluster/gauge-theory
  - cluster/vfe
  - project/multi-agent
  - field/physics
  - field/cs-ml
created: 2026-08-18
updated: 2026-08-18
---

# The rescaling-lab audit and the capacity reversal: a gauge-dependent sector charge retired, root-framed retention rises (2026-08-18)

> [!warning] Tentative — not independently verified
> A single-implementation finding: reproduced and cross-checked only inside the MultiAgentELBO
> codebase. No independent implementation, external replication, cross-model verification, or
> verification-ledger closure exists; treat every number and verdict as tentative. This
> applies to the entire 2026-08-17/18 rescaling-laboratory chain.

> [!info] Provenance and evidence boundary
> Repository `MultiAgentELBO`, audit frozen at `9743962`, remediation and re-measurement
> committed at `4eed61f` (report: `docs/audits/2026-08-18-rescaling-lab-audit.md`; declaration:
> amendment 8 of `docs/superpowers/specs/2026-08-17-rescaling-map-design.md`). Interpreter
> `C:/Python314/python.exe`, numpy 2.4.4, all CPU. The seed reconstruction was validated
> against the published chain before any new number was recorded: seed site sup $1.4321$ and
> pair sup $0.0163$ reproduced exactly from the C(3,3) working-case step; nine-state retention
> $0.156$/$0.441$ reproduced; the retired charge reproduced the published $0.144$/$0.406$, so
> the only changed ingredient is the charge. Focused tests 136 pass; the full suite passes
> except 18 pre-existing environment failures in `test_remediation_evidence.py`, out of scope.

## The finding (audit F8)

Amendment 6's sector charge $s(x_B) = \sum_{a \in B} k_a \bmod 3$ referenced each member's
belief-orbit coordinate $k_a$ to the *first family member*. Under the sample-shift gauge
$h_a$ the coordinate moves ($k_a \to k_a - h_a$) while the readout does not, so the published
M-capacity depended on the frame the instance happened to be declared in. The repaired charge
is **root-framed**: each coordinate is carried into the block root frame by the spanning-tree
transport before summing, $s(x_B) = \sum_{a \in B} (k_a + t_a) \bmod 3$, matching the frame
convention the downward kernels already use. Measured on the declared 4-cycle probe with
root-fixed shifts: the root-framed coarse pair sup is invariant to $1.9 \times 10^{-16}$; the
family-referenced charge deviates by $4.3 \times 10^{-2}$. Under a root shift the sector label
permutes with the parent label, which is the covariance a charge is entitled to.

## What the numbers become

Homogeneous 6-cycle at ratio two, declared seed, 27 parent labels (presentation times
belief-channel $Z_3$ charge):

| quantity | published 2026-08-17 (family-referenced charge, retired) | re-measured 2026-08-18 (root-framed charge) | nine-state baseline |
|---|---|---|---|
| $R_{\mathrm{cap}}$, offsets $\{1\}$ ($k=1$) | 0.144 | **0.209** | 0.156 |
| $R_{\mathrm{cap}}$, offsets $\{1,2\}$ ($k=3$) | 0.406 | **0.568** | 0.441 |
| constant-sector control | exact | exact | — |

The published null ("sector-carrying parents do not raise retention; capacity along this
sector map was not binding") **reverses**: with the gauge-covariant charge, sector-carrying
parents raise one-step pair retention at both boundary multiplicities, while retention stays
below one. The amendment-6 reading rule still governs: this licenses only that capacity was
binding at this seed under this sector map, and the sup statistic dilutes across alphabets,
so the cross-alphabet capacity question stays open pending a mutual-information statistic.

## The rest of the audit (F1–F9, all remediated at `4eed61f`)

Five parallel domain investigators, 50+ live probes; every published number of amendments 3–7
reproduced (M-bundle $0.156/0.441/0.564$; regen fixed point $0.579$ at $\tau = 1$;
sustained-over-injected $1.246$ with the seed-step denominator confirmed consistent; RC6
$0.165$–$0.265$; C1 exhaustively clean over $3^6$ gauge shifts and 144 random towers; C2
clean; C3 deviation $0.2035$ with lossless intermediate). Mechanical defects, all fixed:
controller missing the worker's 52-letter subscript-pool check; inner-2 towers constructible
but unusable; unreachable sectors floored into garbage (retention 2179 at `sector_count` 6);
zero marginals raising bare `OverflowError`; reverse-pair Moebius dedup doubling a table;
`coarse_connection` accepting disconnected blocks; a 12-letter in-process subscript ceiling;
and the Anaconda worker's numpy 2.0.0 within-session nondeterminism ($10^{-8}$ scale on the
8-cycle reduced step), now documented as the worker route's reproducibility boundary.

## Relevance to this research

This is the program's second reversal in two days on the same machinery, and structurally the
sharper one: the first (regeneration restoring interaction) showed the *passive* triviality
was a frozen-attention artifact; this one shows a published *null* was a gauge artifact — the
measurement itself failed the covariance discipline the theory imposes everywhere else. The
corrected result changes the capacity picture: parent-alphabet enlargement by the conserved
$Z_3$ charge (the singlet/triplet reading of marks) does buy retention, so capacity *was*
binding at the declared seed, strengthening the case for the mutual-information capacity
statistic and for extended downward kernels on enlarged alphabets (ROADMAP items 2–3). Method
moral for the wiki: any charge, order parameter, or diagnostic defined on gauge-variant
coordinates must be transported to a declared frame before it is measured — family-referenced
quantities are not observables in this theory.
