---
type: concept
title: "Missing information principle"
tags:
  - cluster/vfe
  - cluster/info-geometry
  - cluster/methodology
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Missing information principle

The principle, central to the EM algorithm of Dempster, Laird and Rubin (1977), that the observed-data score equals the expected complete-data score given the observations, so the gap between complete-data and observed-data information is exactly the 'missing information' due to the latent variables. Formally the observed information equals the complete information minus the missing information (Orchard-Woodbury / Louis identity), which governs EM's convergence rate: the more missing information, the slower EM converges.

## Related
[[Variational EM]], [[Variational free energy]], [[Fisher information]]

## Sources
[[dempster-1977-em-algorithm]]
