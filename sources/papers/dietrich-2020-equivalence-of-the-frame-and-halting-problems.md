---
type: "paper"
title: "Equivalence of the Frame and Halting problems"
aliases: ["Equivalence of the Frame and Halting problems (Fields source, 2020)"]
authors: ["Dietrich, E.", "Fields, C."]
year: 2020
doi: "10.3390/a13070175"
url: "https://chrisfieldsresearch.com/FP-HP-algorithms.pdf"
tags: ["cluster/participatory", "cluster/participatory/philosophy-of-mind", "project/multi-agent", "field/cs-ml", "field/philosophy", "field/mathematics"]
created: "2026-11-01"
updated: "2026-11-01"
---

# Equivalence of the Frame and Halting problems

> [!info] Citation
> Dietrich, E. and Fields, C. (2020) Equivalence of the Frame and Halting problems. Algorithms 13: 175 (doi:10.3390/a13070175).

[Local full text](../pdfs/dietrich-2020-equivalence-of-the-frame-and-halting-problems.pdf). [Primary source](https://chrisfieldsresearch.com/FP-HP-algorithms.pdf).

## Reading basis

Published article, July 20, 2020. Read PDF pages 1 and 3–5 (operational formulation, Theorem 1 proof, and extensions). This is a targeted ingestion reading, not a full proof audit.

## Contribution and scope

Dietrich and Fields formulate an open-domain frame problem for a finite agent that cannot observe the whole environment. They claim equivalence with the Halting Problem, and discuss related limits on identifying systems and grounding symbols. The setup usefully distinguishes the observed environment from unobserved degrees of freedom, so missing information cannot silently be treated as a known state. However, the displayed reverse implication in Theorem 1 moves from undecidability of eventual halting to inability to determine a next state. Given a specified program and complete current configuration, a single transition can be computed; eventual halting undecidability alone does not prevent that. Thus the displayed argument does not establish the advertised equivalence as written.

## Relevance to this research

The open-environment question is relevant to [[Markov Blanket]] and operationally scoped agent models, but the equivalence claim should not be used as a theorem supporting the project. Incomplete observational access, algorithmic undecidability, and computational expense are different limitations. This ingest records the specific proof limitation encountered on PDF page 4; it does not supply a replacement theorem for all formulations of the frame problem.

## BibTeX

```bibtex
@article{dietrich-2020-equivalence-of-the-frame-and-halting-problems,
  author = {Dietrich, E. and Fields, C.},
  title = {Equivalence of the Frame and Halting problems},
  year = {2020},
  journal = {Algorithms},
  doi = {10.3390/a13070175},
  url = {https://chrisfieldsresearch.com/FP-HP-algorithms.pdf},
  volume = {13},
  number = {7},
  pages = {175}
}
```
