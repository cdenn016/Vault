---
type: manuscript
title: "The Inertia of Belief: 2026-07-13 Final Verification Addendum"
aliases:
  - "Belief-inertia final verification addendum"
  - "Final belief-inertia panel reconciliation"
authors:
  - Robert C. Dennis
year: 2026
status: in preparation
tags:
  - cluster/social-physics
  - cluster/social-physics/opinion-dynamics
  - cluster/multi-agent
  - cluster/vfe
  - cluster/gauge-theory
  - cluster/info-geometry
  - project/social-physics
  - project/multi-agent
  - field/physics
  - field/mathematics
  - field/sociology
created: 2026-07-13
updated: 2026-07-13
---

# The Inertia of Belief: 2026-07-13 Final Verification Addendum

## Scope and provenance

This immutable addendum records the final-panel correction to `manuscripts/belief_inertia.tex` on branch `codex/belief-inertia-ultradeep-review-20260712`. It supplements, and supersedes only where stated, [[belief-inertia-2026-07-12-theorem-first-revision]]. The manuscript and wiki corrections were finalized in commit `7bb02bc8ff7a43d2d4a1137e87a2178059a1e5b3` (`fix: align belief-inertia social reductions and wiki claims`). The historical source note [[belief-inertia]], the 2026-07-12 revision record, and the protected PIFB2 comparator remain unchanged.

The hashes printed in the 2026-07-12 revision record describe the pre-Task-11 source snapshot. Task 11 subsequently applied layout-only manuscript changes and a bibliography record-type correction before final verification. They were accurate for that earlier checkpoint but are not the hashes of the final reviewed files. The final post-correction hashes are recorded below.

The Sampson source-note provenance sentence belongs to the original Task 2 source-creation transaction. Task 2 created the comparator note and then clarified its journal-versus-rendered-arXiv author order before the transaction was finalized at commit `87590762f9e0b617d1f886d1f410e0ee3ebcd24c`. It was not a post-ingest mutation of a finalized immutable note, and no history was rewritten.

## Final-panel corrections

The primary mean geometry remains the unweighted product Fisher metric,

$$
G_{\mathrm{prod}}=\sigma^{-2}(I_N\otimes I_d).
$$

Under this metric, fixed symmetric influence gives the continuous-time DeGroot reduction. For a nonuniform reversible row-stochastic matrix $W$ with stationary measure $\rho$, the unweighted flow retains the factor $D_\rho$ and is proportional to $-D_\rho(I-W)\mu$. Exact cancellation to $-(I-W)\mu$ requires the additional stationary-measure-weighted metric

$$
G_\rho=\sigma^{-2}(D_\rho\otimes I_d),
$$

equivalently the mean Fisher block of the fixed-label joint family $P(i,x)=\rho_iq_i(x)$, or agent-specific rates proportional to $\rho_i^{-1}$. The restricted anchored Friedkin--Johnsen equilibrium inherits the same metric or rate qualification. General directed DeGroot and Friedkin--Johnsen dynamics are not derived.

For first-order Fisher flow, the local linearization is $\delta\dot x=-\eta G^{-1}H_F\delta x$. At fixed $G$ and learning rate $\eta$, greater positive modal stiffness speeds linear relaxation and reduces the static response to a matched force. Stiffness alone therefore does not explain slower belief revision. A slower timescale requires an independently varied mobility or learning rate, damping or kinetic metric, or an explicit slow state. This direction is distinct from the conditional second-order kinetic interpretation.

The social-science boundary is correspondingly narrow. Bounded confidence is a finite-temperature soft analog rather than an exact Hegselmann--Krause or Deffuant recovery. Voter-model copying, evolutionary-game dynamics, Social Impact Theory's number law, general conformity, and persistent polarization are benchmarks or interpretive comparators unless additional state variables or mechanisms are introduced. Canonical support for perseverance, confirmation-bias taxonomy, and Social Impact Theory is now provided by the manuscript's Anderson, Nickerson, and Latan\'e citations.

## Final source hashes

- Final `manuscripts/belief_inertia.tex` after commit `7bb02bc8ff7a43d2d4a1137e87a2178059a1e5b3`: SHA-256 `B821E0A79D377521AA012B543BAB76B0B0161AB6B8658AB93DBE049ECD4E9231`.
- Final shared `manuscripts/references.bib`: SHA-256 `01491289DB2DBB426F5EC156C9D123F568F415E04378FDB626E721F6654F3E62`.
- Final symbolic regression `docs/reviews/2026-07-12-belief-inertia-symbolic-checks.py`: SHA-256 `C4334A3679C0632C37CD6DFB5ED530D88D3C32B0383DCFE5B11CBEF75BFE71ED`.
- Protected comparator `manuscripts/PIFB2.tex`: SHA-256 `50F382C51BFAC8B8841A4FE6AFF2887CE05D3D47DD905C6D20A91A688152D81B`.
- Protected historical note `sources/manuscripts/belief-inertia.md`: SHA-256 `ADD9AA3AE8497AE9DB28FB66B07F55C56DBB80F8601726160BDBE0DC5DCB5E92`.
- Preserved 2026-07-12 revision record: SHA-256 `E1F4CDE3A71D0AA852B93AE3955C3C5650093116E8ECAC8E52C8F152C02FBF6F`.
- Ultradeep peer review: SHA-256 `2D5D5694A08DA334DF89E44C9AEC5DD1B935ED386D097FE2CF31176C81D5F1DE`.

## Verification status and residual limits

The exact symbolic regression now checks both the residual $D_\rho$ factor under the primary metric and its cancellation under $G_\rho$, as well as the first-order stiffness-versus-relaxation-time direction. The clean final-panel build produces a 39-page PDF with no forbidden LaTeX diagnostics, no unresolved citations or references, no overfull boxes, and 22 nonblocking underfull boxes. Vault lint reports zero defects in all five structural categories.

These checks establish internal mathematical, bibliographic, and documentary consistency. They do not supply empirical validation, identify the kinetic metric, derive persistent polarization under passive attractive attention, or show that a social-psychological construct is uniquely measured by a VFE parameter. No new data were created, analyzed, or claimed.

## Relevance to this research

This addendum is the authoritative final verification source for [[Belief inertia]], [[Mass as Fisher information]], [[Belief perseverance and confirmation bias]], [[Opinion dynamics]], [[Bounded confidence]], [[Echo chambers and polarization]], [[Social Impact Theory]], [[Social influence and conformity]], [[Voter model]], [[Evolutionary game theory and cooperation]], [[Sociophysics]], [[Statistical physics of social systems and collective behavior]], [[SocialPhysics]], and [[Gauge-Theoretic Multi-Agent VFE Model]]. It preserves the earlier records as immutable provenance while correcting the final metric scope, stiffness direction, social-model boundary, and snapshot hashes.
