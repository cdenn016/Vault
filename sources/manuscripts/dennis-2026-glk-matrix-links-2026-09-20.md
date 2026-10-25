---
type: manuscript
title: "Gauge-Covariant Gaussian Attention: Matrix-Link Revision, September 20, 2026"
aliases: [GLK Matrix-Link Revision September 2026]
authors: [Robert C. Dennis]
year: 2026
tags: [cluster/gauge-theory, cluster/attention, cluster/info-geometry, project/transformer, project/multi-agent, field/cs-ml, field/mathematics]
created: 2026-09-20
---

# Gauge-Covariant Gaussian Attention: Matrix-Link Revision, September 20, 2026

## Source and revision

Robert C. Dennis, *Gauge-Covariant Gaussian Attention and Predictive Communication*, working manuscript pair revised September 20, 2026. The files were the main manuscript `GL(K)_attention.tex` and its supplement `GL(K)_supplementary.tex`. Main Section 4.4 (`sec:matrix_link_fields`) and Supplementary Appendix K (`app:matrix_links`) contain this construction. This immutable note records the revision; it does not replace the older [[gl-k-attention]] source.

The bounded manuscript-edit checks built both PDFs successfully (31 and 55 pages), resolved references and citations, and checked selected rendered pages. These are document checks, not a new empirical experiment or formal verification-ledger closure. The revision artifacts, originals, diffs, and `validation.json` are under `C:/Users/chris and christine/Desktop/V3_Transformer/docs/manuscripts/2026-09-20-glk-lattice-links/`.

## Full Gaussian site states and factorized links

The theoretical site state is $q_i=\mathcal N(\mu_i,\Sigma_i)$ with $\Sigma_i\succ0$. A local passive frame change sends $(\mu_i,\Sigma_i,U_i)$ to $(g_i\mu_i,g_i\Sigma_i g_i^\top,g_iU_i)$. The reference moments $\xi_i=U_i^{-1}\mu_i$ and $C_i=U_i^{-1}\Sigma_iU_i^{-\top}$ are unchanged. Full Gaussian projected comparisons therefore yield invariant scalar routing weights when their reference maps and prior are fixed. Diagonal storage is an implementation restriction, not the primary theoretical state space.

At a fixed layer, $T_h:\mathbb R^K\to\mathbb R^{s_h}$ sends content and $O_h:\mathbb R^{s_h}\to\mathbb R^K$ receives it. They define

$$
\mathsf S_{j,h}=T_hU_j^{-1},\qquad
\mathsf R_{i,h}=U_iO_h,\qquad
L_{ij}^{(h)}=\mathsf R_{i,h}\mathsf S_{j,h}=U_iO_hT_hU_j^{-1}.
$$

The endpoint law follows by substitution:

$$L_{ij}^{(h)\prime}=g_iL_{ij}^{(h)}g_j^{-1}.$$

This identity admits singular links. The routed sum is $\mathcal C_{ij}=\sum_h\beta_{ij}^{(h)}L_{ij}^{(h)}=U_iA_{ij}U_j^{-1}$ with $A_{ij}=\sum_h\beta_{ij}^{(h)}O_hT_h$ and message $m_i=\sum_j\mathcal C_{ij}\mu_j$. Its rank is at most $\min(K,\sum_hs_h)$ and can reach $K$ even with low-rank heads. At fixed layer its reference matrices remain in the shared span of $O_hT_h$. Sending and receiving directions may overlap; gains and their correspondence are also part of the maps.

## Composition and loop scope

For one unweighted head, suppress $h$ and put $M=OT$. Then

$$L_{ij}L_{jk}-L_{ik}=U_iO(TO-I_s)TU_k^{-1}.$$

If $TO=I_s$, the maps give flat identifications on receiving subspaces $U_i\operatorname{im}O$. Conversely, a zero defect forces $TO=I_s$ when $O$ has full column rank and $T$ full row rank. Along $r$ edges, the shared-head product is $U_{i_0}M^rU_{i_r}^{-1}$: paths with the same endpoints and length agree. The composition defect alone therefore does not establish arbitrary edge-specific curvature.

For any declared matrix-link family with the endpoint law, a closed product transforms by conjugation at its base site and its trace is invariant. Link inverses are unnecessary for this identity. A nonidentity product may express gain, contraction, or rank loss; it is not evidence that $\Omega_{ij}=U_iU_j^{-1}$ has nontrivial holonomy. That frame-derived connection remains flat. Causal attention has no directed cycles through distinct token positions, so such loop observables require a declared graph extension and additional links.

## Declared extensions and unresolved obligations

The identity $L_{ij}^{(h)}=F_{i,h}\Omega_{ij}$, with $F_{i,h}=U_iO_hT_hU_i^{-1}$, separates local processing from transport. Replacing $\Omega$ by independently supplied invertible connection links $\Theta_{ij}$ gives a possible extension $\mathcal L_{ij}^{(h)}=F_{i,h}\Theta_{ij}$. It is not a claim that the reported model learned independent connections.

For any rank of $\mathcal L_{ij}$ and $Q_i\succ0$, the channel $k_i\mid k_j\sim\mathcal N(\mathcal L_{ij}k_j,Q_i)$ is normalized. A Gaussian source induces covariance $Q_i+\mathcal L_{ij}\Sigma_j\mathcal L_{ij}^\top\succ0$. This is a declared probabilistic construction; the reported predictive mean readout does not implement that covariance propagation. A population law still needs a normalized assembly.

[[wetterich-2014-linear-lattice-gauge-theory]] supplies a precedent for general matrix links under compact site groups. Its action and continuum conclusions are not imported into GL(K). An invariant action, graph/loop structure, normalization, and dynamics remain additional choices. The MLP subsection was retained unchanged: no gauge-VFE MLP interpretation was selected, and no common-free-energy descent claim for the complete stack was added.

## Relevance to this research

This extends the vocabulary of [[GL(K) gauge-equivariant attention]] and [[Lattice gauge theory]] without conflating communication maps with invertible parallel transport. It connects the [[VFE Transformer Program]] to the general interaction language of the [[Gauge-Theoretic Multi-Agent VFE Model]], while preserving implementation and theory boundaries. [[Holonomy]] and [[Gauge equivariance and geometric deep learning]] provide the corresponding synthesis pages.

## Revision hashes

- `GL(K)_attention.tex`: `971795de93b5a13d49312f471037fd8df047425cc0af66cf455d0c0bc195084f`
- `GL(K)_supplementary.tex`: `b224236aa9bef205521266df7d2750f4aef6e04d2b24569524f649be5aabcfb6`
- `references.bib`: `6bc4404983fcd546888934f1a256f6ded9f03551b85a2e0174474903c85a97d9`
