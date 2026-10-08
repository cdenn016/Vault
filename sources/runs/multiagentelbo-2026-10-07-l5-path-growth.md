---
type: run
title: "MultiAgentELBO L5 growing dyadic paths and retained covariance"
aliases: ["L5 growing-path covariance and determinant scaling"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/physics, field/statistics]
created: 2026-10-07
updated: 2026-10-07
---

# MultiAgentELBO L5 growing dyadic paths and retained covariance

The actual first-original-copy dyadic selector has monotone composite paths of length $r+c\le2(s-1)$, where $s=2^d$ is the block side. The unchanged nonlinear anchored prior supplies path-length-normalized logarithmic second moments, ensemble trace centering and stationary-axis singular-log rates. In the actual isotropic Gaussian GL(2) control, explicit iid-increment concentration yields an exact largest-covariance growth rate $4\gamma$ per block side, with $\gamma>0$. A separate covariant determinant statistic converges to a nonzero scalar in a growing-block/growing-parent limit. These results do not prove a full retained-state limit or a nonlinear growth rate. No simulation or GPU was used.

## Source and derivation

Codex (2026), *L5 growing dyadic paths and retained covariance*, MultiAgentELBO analytical research record, published revision `930a55701d1d123de3cc9004deb65a4624dd78e6`. The [derivation](https://github.com/cdenn016/MultiAgentELBO/blob/930a55701d1d123de3cc9004deb65a4624dd78e6/docs/research/2026-10-03-latent-link-rg-plan/L5-PATH-GROWTH.md), [independent reconstruction](https://github.com/cdenn016/MultiAgentELBO/blob/930a55701d1d123de3cc9004deb65a4624dd78e6/docs/research/2026-10-03-latent-link-rg-plan/L5-PATH-GROWTH-CHECK.md), and [source intake](https://github.com/cdenn016/MultiAgentELBO/blob/930a55701d1d123de3cc9004deb65a4624dd78e6/docs/research/2026-10-03-latent-link-rg-plan/evidence/l5-path-growth-intake-20261007.json) record the proof, source correspondence, explicit assumptions and access limitations. The independently reconstructed report has normalized UTF-8 LF SHA256 `0a953955dae5c785929d4c1574e4c159ab0e6c4a277d146186a71f15960bda5d`. This identifies the inspected text and is not a mathematical acceptance criterion. The analytical source is filed with the existing run records; no fresh sampling run is implied.

```bibtex
@misc{codex2026l5pathgrowth,
  author = {Codex},
  title = {L5 Growing Dyadic Paths and Retained Covariance},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/blob/930a55701d1d123de3cc9004deb65a4624dd78e6/docs/research/2026-10-03-latent-link-rg-plan/L5-PATH-GROWTH.md},
  note = {MultiAgentELBO analytical research record, revision 930a55701d1d123de3cc9004deb65a4624dd78e6}
}
```

The live c10 forest-tree proposition already supplies compatible transport composition. The source-derived induction checks the actual upper-left roots, three dyadic joins, original row-major copy ordering, and right multiplication. At each descending binary bit, a path takes its row chunk before its column chunk. Its top-row endpoint has the straight original horizontal product; its bottom-right endpoint has $2(s-1)$ distinct factors. Matching nonwrapping finite-torus selectors are required; both sides at least $2s$ suffice. General depth is analytical, whereas L3 executed depths one and two. The comparison preserves every original internal, boundary and parallel dressed group mark.

## Covariance and invariant diagonal

Fix an episode and $v=(A_T^{-1})_{nn}>0$, where $A_T=aI_T+mL_{\mathrm{path},T}$. For $c=0$, every primitive has independent centered Gaussian entries of variance $v$. The baseline comparison matter has covariance $I_2$. The actual rooted mean retains

$$
Z_I=s^{-2}\sum_{i\in I}T_i z_i,\qquad
V_I=s^{-4}\sum_{i\in I}T_iT_i^\top.
$$

Write $X=tI+S$, with $S$ traceless. Gaussian orthogonal projection makes $t$ and $S$ independent. Orthogonal conjugation invariance gives a direction-independent log-length increment law. Transposing the actual right product makes an exact left product whose scalar increments are iid conditional on the entire past. If $r\ge1$ is the largest singular value of $\exp S$, angular averaging gives the exact positive coefficient

$$
\gamma=\mathbb E\log\frac{r+r^{-1}}2>0.
$$

The coefficient is not numerically estimated. The centered increment moment generating function is bounded by $\exp(8v\theta^2)$. Chernoff bounds, two basis columns and a union over overlapping paths then give simultaneous bounds on every transport. The bottom-right covariance term gives the lower rate, and the sum of all $s^2$ terms gives the upper rate. On every matching diagonal with $s\to\infty$ and $\log N=o(s)$,

$$
\max_I\left|s^{-1}\log\lambda_{\max}(V_I)-4\gamma\right|
\longrightarrow0
$$

in probability. Every polynomial scalar covariance or feature normalization retains escape. Projecting the normalized conditional Gaussian onto a maximum-variance direction gives an explicit finite-size small-ball bound, valid for any conditional mean; polynomially rescaled samples escape every fixed-radius ball. This is a statement about this supplied readout and comparison law, not a general formation obstruction. Cancelling the exponential rate alone does not prove tightness or convergence of a rescaled covariance.

Use the existing baseline matter precision $M_i=\Sigma_i^{-1}$ and the carried-metric volume distortion

$$
\chi(W:j\to i)=\log|\det W|+\tfrac12\log\det M_i-\tfrac12\log\det M_j.
$$

It is pointwise invariant when the link, metric and law transform passively. Normalized transport singular values and the eigenvalues of $M_{r_I}^{1/2}V_IM_{r_I}^{1/2}$ are invariant as well. This does not assert an active symmetry of the anchored Frobenius-coordinate prior or choose a metric for the connection spectrum in Theory.

In baseline coordinates $\chi(T_i)$ is exactly the Gaussian sum of primitive traces along its path, with variance $2v(r+c)$. Let $P=N/s^2$ and define

$$
H_{N,d}=\frac1{Ns}\sum_i\chi(T_i)^2.
$$

Dependence between paths within a block is retained. Distinct blocks use disjoint primitive sets only in this Gaussian control. The exact mean and variance bound are

$$
\mathbb E H_{N,d}=2v(1-1/s),\qquad
\operatorname{Var}(H_{N,d})\le8v^2/P.
$$

Therefore $H\to2v$ in $L^2$ when both $s$ and $P$ grow. The unmultiplied statistic $H/s$ tends to zero. For the existing torus family, choose $N_j=512\cdot4^j$ and $s_j=2^{\lfloor j/2\rfloor}$; both indices grow and $\log N_j=o(s_j)$. Error bounds are summable on this explicit diagonal, yielding the same covariance rate and scalar limits almost surely under any common coupling of these finite laws. Volume-first then depth gives the same determinant-statistic limit. This is not a claim about convergence of archived samples or at maximal depth with $P=1$.

## Nonlinear scope and primary references

The unchanged nonlinear prior supplies $\mathbb E[(\lambda(T_i)/s)^2]\le4M$, where $\lambda(W)=\max(0,\log\|W\|,\log\|W^{-1}\|)$. Each orientation's spatially constant trace history cancels from every plaquette and retains its centered Gaussian factor. Translation invariance and uniform integrability consequently give ensemble-centered traces in spatial limits. This does not give independent increments or zero drift on every ergodic component.

Stationary-axis exterior products obey the subadditive theorem's hypotheses, with normalized second moments bounded. Their rates exist almost surely and in $L^1$, possibly as nonconstant invariant functions. The primary proof is J. Michael Steele, *Kingman's subadditive ergodic theorem*, Annales de l'Institut Henri Poincare, Probabilites et Statistiques 25(1), 93–98 (1989), [primary PDF](https://www.numdam.org/item/AIHPB_1989__25_1_93_0.pdf). Its extracted prose was read; displayed equations were omitted by OCR and a local download timed out. [Pitman's author-course Lecture 12, Section 12.1](https://www.stat.berkeley.edu/~pitman/s205s03/lecture12.pdf) supplied the readable matching statement. The model-specific integrability, stationarity, subadditivity, finiteness and $L^1$ upgrade are reconstructed explicitly in the linked check. No unperformed full-text or screenshot inspection is claimed.

The general random-product precedent is Harry Furstenberg, *Noncommuting random products*, Transactions of the American Mathematical Society 108(3), 377–428 (1963), [doi:10.1090/S0002-9947-1963-0163345-0](https://doi.org/10.1090/S0002-9947-1963-0163345-0). The Harvard-hosted primary PDF was downloaded and the relevant section 8.3 read from extracted text/page images. Its printed moment and group hypotheses require more than noncompact links. The exact isotropic-control proof above uses a direct argument rather than an unchecked extension of that theorem.

```bibtex
@article{steele1989kingman,
  author = {Steele, J. Michael},
  title = {Kingman's Subadditive Ergodic Theorem},
  journal = {Annales de l'Institut Henri Poincare, Probabilites et Statistiques},
  volume = {25}, number = {1}, pages = {93--98}, year = {1989},
  url = {https://www.numdam.org/item/AIHPB_1989__25_1_93_0.pdf}
}
@article{furstenberg1963products,
  author = {Furstenberg, Harry},
  title = {Noncommuting Random Products},
  journal = {Transactions of the American Mathematical Society},
  volume = {108}, number = {3}, pages = {377--428}, year = {1963},
  doi = {10.1090/S0002-9947-1963-0163345-0}
}
```

## Relevance to this research

This advances the growing-path obligation left by [[multiagentelbo-2026-10-07-l5-retained-limit]]. It provides useful arbitrary-size control for the actual tree, an explicit diagonal, and a nonzero invariant scalar limit. The scalar limit coexists with exponential covariance escape, so it cannot stand in for a complete parent-law limit. The spatial exponents are separate from b05's derivative scale cocycle and its unresolved stationary blocking family.

A compatible covariant normalization or retained channel must still control fluctuations, anisotropy, dressed marks and the full joint law. The nonlinear action needs new correlation/concentration and growth estimates; neither ensemble trace centering nor a stationary-axis theorem supplies them. Original joint descent, predictive compression accuracy, endogenous formation, O1/O3/O4/O5 and sparse-graph S1 remain open. [[multiagentelbo-2026-10-07-l5-exponential-diagnosis]] preserves both numerical failures without retry. No connection eigenvalues, new loop family, manuscript edit, runtime/configuration change or GPU allocation occurred. The broad goal remains active.

[[Gauge-Theoretic Multi-Agent VFE Model]]
[[Staged hierarchy formation and RG composability]]
[[Renormalization-group flow of beliefs]]
[[Mathematics MOC]]
[[Physics MOC]]
[[Statistics MOC]]
