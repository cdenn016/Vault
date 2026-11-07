---
type: paper
title: "Evidence and Intervention: A Coupled Active-Inference Extension of Rational Speech Act Models"
aliases: ["Gwon Murphy Chung 2026 evidence and intervention"]
authors: ["Yonghyeon Gwon", "Elliot Murphy", "Chun Kee Chung"]
year: 2026
venue: "arXiv preprint"
arxiv: "2610.04347"
doi: "10.48550/arXiv.2610.04347"
url: "https://arxiv.org/abs/2610.04347v1"
version: "arXiv v1, submitted 2026-10-03"
tags: [cluster/vfe, cluster/multi-agent, project/multi-agent, field/cs-ml, field/psychology]
created: 2026-11-07
updated: 2026-11-07
---

# Evidence and Intervention: A Coupled Active-Inference Extension of Rational Speech Act Models

> [!info] Citation
> Gwon, Y., Murphy, E., and Chung, C. K. (2026). *Evidence and Intervention: A Coupled Active-Inference Extension of Rational Speech Act Models*. [arXiv:2610.04347v1](https://arxiv.org/abs/2610.04347v1), October 3. [Primary PDF](https://arxiv.org/pdf/2610.04347v1). Preprint; no journal publication is asserted.

[Local v1 PDF](../pdfs/gwon-2026-evidence-intervention.pdf), 83 pages; retrieved November 7, 2026. Version identification follows the arXiv record.

## TL;DR

Dialogue couples action interpretation to an attributed partner policy while separating state inference, parameter learning, prospective evaluation, and habitual policy priors.

## Problem & setting

Each interlocutor models the other's pragmatic state and response. Sections 3.6–3.7 construct action likelihoods from pre-action information, preventing the observed action from generating its own likelihood.

## Method

For extended policies, likelihood sums attributed policy probabilities sharing the observed first action. Under the stated one-step, equal-evidence restriction,

$$
P_A(a\mid z)=\frac{E_{A\leftarrow B}(a\mid z)e^{-\gamma G_{A\leftarrow B}(a,z)}}{Z_{A\leftarrow B}(z)}.
$$

The listener's negative log likelihood retains $\log Z(z)$. Thus attributed speaker EFE enters listener VFE through a normalized likelihood, not as a jointly minimized sum of objectives.

## Key results

Section 3.12 recovers RSA distributions under explicit one-step restrictions. Worked examples illustrate clarification-dependent audience design, persistent misunderstanding, and closing with residual uncertainty. These are model constructions rather than empirical validation.

## Relevance to this research

This is a close comparator for receiver-aware [[Expected Free Energy]] policies. It neither supplies GL channel geometry nor proves collective boundary formation. Its explicit separation of updates complements [[friston-frith-2015-hermeneutics]] and [[frank-goodman-2012-pragmatic-reasoning]].

## Cross-links

[[Active inference communication and collective boundaries]]; [[Collective active inference]].

## BibTeX

```bibtex
@misc{gwon2026EvidenceIntervention,
  author = {Gwon, Yonghyeon and Murphy, Elliot and Chung, Chun Kee},
  title = {Evidence and Intervention: A Coupled Active-Inference Extension of Rational Speech Act Models},
  year = {2026},
  eprint = {2610.04347},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL},
  doi = {10.48550/arXiv.2610.04347},
  url = {https://arxiv.org/abs/2610.04347v1},
  note = {Version 1, submitted October 3, 2026; preprint}
}
```
