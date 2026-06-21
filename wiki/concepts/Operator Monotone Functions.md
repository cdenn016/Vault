---
type: concept
title: "Operator Monotone Functions"
aliases:
  - "Operator monotone function"
tags:
  - cluster/info-geometry
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Operator Monotone Functions

A function f on the positive reals is operator monotone if A <= B (in the Loewner order) implies f(A) <= f(B) for all SPD/Hermitian matrices. By Loewner's theorem these are exactly the functions with a Pick/Nevanlinna integral representation. Operator monotone functions parameterize the Kubo-Ando theory of operator means and, via Petz's theorem, classify all monotone (contractive) Riemannian metrics on the space of density matrices: each symmetric operator monotone function f with f(t)=t f(1/t) yields one monotone metric (Bures, BKM, RLD as special cases). They are central to the information geometry of SPD belief states and the divergence/retraction registries in the VFE codebase.

## Related
[[Fisher Information Metric]], [[SPD-manifold geometry and Riemannian optimization|SPD Geometry]], [[Information Geometry]]

## Sources
[[petz-1996-monotone-metrics]]
