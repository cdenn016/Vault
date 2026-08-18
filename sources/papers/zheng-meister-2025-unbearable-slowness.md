---
type: paper
title: "The unbearable slowness of being: Why do we live at 10 bits/s?"
aliases:
  - "Zheng and Meister 2025"
  - "10 bits per second"
  - "unbearable slowness of being"
authors:
  - Zheng, Jieyu
  - Meister, Markus
year: 2025
arxiv: 2408.10234
url: https://www.cell.com/neuron/fulltext/S0896-6273(24)00808-0
tags:
  - cluster/multi-agent
  - cluster/participatory/consciousness
  - project/multi-agent
  - field/neuroscience
  - field/statistics
created: 2026-08-18
---

# The unbearable slowness of being: Why do we live at 10 bits/s?

> [!info] Citation
> Jieyu Zheng and Markus Meister (2025). "The unbearable slowness of being: Why do we live at 10 bits/s?" *Neuron* 113(2), published online 2024-12-17. arXiv: [2408.10234](https://arxiv.org/abs/2408.10234).

## TL;DR

Human sensory systems acquire on the order of $10^9$ bits/s, yet measured behavioral
information throughput — across speech, typing, gaming, memory sports — sits near 10 bits/s, an
eight-order-of-magnitude compression. The authors argue the brain operates in two regimes: an
"outer" brain handling fast high-dimensional sensorimotor signals and an "inner" brain
processing the few bits per second that steer behavior, and they pose the unexplained
neuroscience question of why so much neural hardware serves so narrow a conscious channel.

## Key results

The 10 bits/s figure is an empirical convergence across many paradigms, not a theoretical
bound: world-record speedcubing, blindfolded memory feats, professional gaming, and language
production all land within a factor of a few of it. The sensory periphery, by contrast, is
measured in gigabits per second, so essentially all acquired information is discarded en route
to behavior. The paper frames the discrepancy as a serious open problem (serial central
processing, evolutionary path dependence) rather than resolving it.

## Relevance to this research

This is the empirical anchor for the throughput-versus-emission distinction in hierarchical
information systems: a higher level's *output* rate can be minuscule while its state update
*consumes* enormous bandwidth from below — the brain is a massive information compressor whose
inner level still requires the full $10^9$ bits/s feed to select its 10 bits well. In the
gauge-theoretic laboratory the same split is measured exactly: boundary mutual-information
retention through one blocking step is 2–7% (bounded by one via the
[[Data processing inequality]]), while regenerated attention rebuilds coarse coupling from
coarse state — levels consume much and emit little, and what they emit is generated, not
relayed. See [[Meta-agents and hierarchical emergence]] and
[[2026-08-18-minfo-information-retention]].

## Cross-links

- Concepts: [[Data processing inequality]], [[Mutual information]], [[Meta-agents and hierarchical emergence]]
- Related sources: [[2026-08-18-minfo-information-retention]], [[hoel-2013-causal-emergence]]

## BibTeX

```bibtex
@article{ZhengMeister2025,
  author  = {Zheng, Jieyu and Meister, Markus},
  title   = {The unbearable slowness of being: Why do we live at 10 bits/s?},
  journal = {Neuron},
  volume  = {113},
  number  = {2},
  year    = {2025},
  note    = {Published online 2024-12-17},
  eprint  = {2408.10234},
  archivePrefix = {arXiv}
}
```
