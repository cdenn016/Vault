---
type: concept
title: "Exponential family"
aliases:
  - "Exponential families"
  - "Exponential Families"
tags:
  - cluster/info-geometry
  - cluster/vfe
  - project/transformer
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Exponential family

An exponential family is a parametric family of distributions whose density has the canonical form p(x|theta) = h(x) exp(<theta, T(x)> - A(theta)), with natural parameters theta, sufficient statistics T(x), and log-partition (cumulant) function A. Gradients of A give the moments (mean of T), its Hessian is the Fisher information, and the dual (mean) parameters are E[T(x)]. Exponential families are the natural setting for variational inference and information geometry: the Gaussian belief states used throughout the program are exponential-family members, conjugate updates are linear in natural parameters, and the Fisher metric / natural gradient inherit their structure from A.

## Related
[[Statistical manifold]], [[Fisher information metric]], [[Variational free energy]], [[Natural gradient]], [[Information geometry and natural gradient]]

## Sources
[[wainwright-2008-graphical-models-variational]], [[jaynes-1957-information-statistical-mechanics]], [[blei-2017-variational-inference]]
