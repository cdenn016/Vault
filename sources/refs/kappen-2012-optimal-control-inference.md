---
type: reference
title: "Optimal Control as a Graphical Model Inference Problem"
aliases:
  - "Kappen, Gómez and Opper 2012"
  - "Optimal control as a graphical model inference problem"
  - "Kappen2012"
authors:
  - Hilbert J. Kappen
  - Vicenç Gómez
  - Manfred Opper
year: 2012
arxiv: "0901.0633"
doi: 10.1007/s10994-012-5278-7
url: https://arxiv.org/abs/0901.0633
tags:
  - cluster/vfe
  - project/transformer
  - field/cs-ml
  - field/mathematics
  - field/physics
created: 2026-09-23
updated: 2026-09-23
---

# Optimal Control as a Graphical Model Inference Problem

> [!info] Citation
> Hilbert J. Kappen, Vicenç Gómez, Manfred Opper (2012). "Optimal Control as a Graphical Model Inference Problem." *Machine Learning* **87**, 159–182. DOI: [10.1007/s10994-012-5278-7](https://doi.org/10.1007/s10994-012-5278-7). Preprint: [arXiv:0901.0633](https://arxiv.org/abs/0901.0633) (v3 read).

## TL;DR

For a class of stochastic control problems in which the control cost is the KL divergence of the controlled from the uncontrolled dynamics plus a state cost, the total cost is itself a KL divergence to an unnormalized target. The optimal controlled path distribution is then a Boltzmann distribution, the optimal cost is minus the log partition function, and computing the control is an inference problem open to exact or approximate graphical-model methods.

## What it establishes

Section 2 ("Control as KL minimization") takes the per-step cost to be $\log\frac{p_t(x_{t+1}\mid x_t,u_t)}{q_t(x_{t+1}\mid x_t)}+R(x_t,t)$, with $q$ the free (uncontrolled) dynamics (Eq. 2). The expected cost becomes $C(x_0,p)=\mathrm{KL}(p\Vert\psi)=\mathrm{KL}(p\Vert q)+\langle R\rangle$ with $\psi(x_{1:T}\mid x_0)=q(x_{1:T}\mid x_0)\exp(-\sum_tR(x_t,t))$ (Eqs. 3–4). Minimizing over normalized $p$ gives the Boltzmann distribution $p=\psi/Z(x_0)$ (Eq. 5) and the optimal cost $C=-\log Z(x_0)$ (Eq. 6), a closed form in the known $q$ and $R$ (derivation in Appendix A). The same section shows that path-integral control is the continuous-space, continuous-time limit with Gaussian noise. Sections 3 and 4 apply exact (junction tree) and approximate (belief propagation, cluster variation) inference to a block-stacking task and a multi-agent stag-hunt game. Section 5 compares the approach with the EM method of [[toussaint-storkey-2006-probabilistic-inference-mdp]] and states that Friston's free-energy formulation is the special case of time-independent dynamics and costs with an infinite horizon.

## Relevance to this research

The September 2026 v2 revision of the GL(K) attention manuscript cites this paper for control as KL minimization. The Boltzmann optimum with cost $-\log Z$ parallels the manuscript's result that the minimum routing free energy of a receiver is $-\tau\log Z_i$, attained by the Gibbs row. With [[levine-2018-control-as-inference]] and [[toussaint-storkey-2006-probabilistic-inference-mdp]], it supplies the control-as-inference background of the binary compatibility record that makes Gibbs routing an exact posterior. See [[GL(K) gauge-equivariant attention]], [[Softmax]], and [[Active Inference]].

## Local full text

The arXiv v3 PDF is stored at `sources/pdfs/Kappen2012.pdf` ([local PDF](../pdfs/Kappen2012.pdf)). Source: [arXiv:0901.0633](https://arxiv.org/pdf/0901.0633). SHA-256: `4c153c2bb2eb5571e6a9090c0dc7cf8c5a05006f9ee542a20715b2d2a9204ac2`.

## BibTeX

```bibtex
@article{Kappen2012,
  author = {Kappen, Hilbert J. and G{\'o}mez, Vicen{\c{c}} and Opper, Manfred},
  title = {Optimal Control as a Graphical Model Inference Problem},
  journal = {Machine Learning},
  volume = {87},
  pages = {159--182},
  year = {2012},
  doi = {10.1007/s10994-012-5278-7},
  eprint = {0901.0633},
  archivePrefix = {arXiv}
}
```
