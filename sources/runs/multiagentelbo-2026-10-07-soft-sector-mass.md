---
type: run
title: "MultiAgentELBO conditional soft-sector mass and localization, October 7, 2026"
aliases: ["MultiAgentELBO O1 mass continuation October 7"]
authors: ["MultiAgentELBO project"]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/info-geometry, project/multi-agent, field/mathematics, field/statistics, field/physics, field/cs-ml]
created: 2026-10-07
---

# MultiAgentELBO conditional soft-sector mass and localization

MultiAgentELBO project (2026). *O1 substantial mass under controlled non-isometry, and arbitrary-N localized GL sections*. Published in [PR162](https://github.com/cdenn016/MultiAgentELBO/pull/162), pinned to merge [ff0fcabe1a48f16c0a9f751ab29cbe7dd8aa3791](https://github.com/cdenn016/MultiAgentELBO/commit/ff0fcabe1a48f16c0a9f751ab29cbe7dd8aa3791). Producer source is 0782265079aed12784b7cbdd5f868a8dc0be1f98; corrected saved-only checker is 8a127e3 and results commit is c2d2222ccf1556861fbf327e2d672c64b6d8126b. Primary records are the [complete derivation and results](https://github.com/cdenn016/MultiAgentELBO/blob/ff0fcabe1a48f16c0a9f751ab29cbe7dd8aa3791/docs/research/2026-10-07-soft-fixed-sectors/O1-MASS-BOUND.md), [producer record](https://github.com/cdenn016/MultiAgentELBO/blob/ff0fcabe1a48f16c0a9f751ab29cbe7dd8aa3791/docs/research/2026-10-07-soft-fixed-sectors/evidence/o1-mass-summary.json), [saved-only readback](https://github.com/cdenn016/MultiAgentELBO/blob/ff0fcabe1a48f16c0a9f751ab29cbe7dd8aa3791/docs/research/2026-10-07-soft-fixed-sectors/evidence/o1-mass-readback.json) and [original record with attributed continuation](https://github.com/cdenn016/MultiAgentELBO/blob/ff0fcabe1a48f16c0a9f751ab29cbe7dd8aa3791/docs/research/2026-10-07-soft-fixed-sectors/RECORD.md).

```bibtex
@misc{multiagentelbo2026softsectormass,
  author = {{MultiAgentELBO project}},
  title = {O1 substantial mass under controlled non-isometry, and arbitrary-N localized GL sections},
  year = {2026},
  howpublished = {MultiAgentELBO PR162, numerical source revision 0782265},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/162}
}
```

## Source continuity, assumptions and derivation

This sequential Codex continuation of Claude's October 7 soft-sector record stays at one base point, using the live theory's connection form, reversal law and covariant vertex metric. It is not independent mathematical adjudication of either record, a novelty survey or a new formation model. The prior record's mass-weighted link-repair identity already exists; O1's unresolved step was substantial graph volume. [[bandeira-2013-connection-cheeger]], Theorem 2.4 and Lemmas 3.3-3.5, were read in the primary arXiv v2 PDF. Their orthogonal norm-fluctuation argument informs the extension but their group-rounding theorem is not transplanted to noncompact GL. [[hansen-2018-toward-a-spectral-theory-of-cellular-sheaves]], section 7.2, is the broader structural motivation, not an asserted GL mass theorem.

Write the vertex metric as $M_v=m_vG_v$, with declared scalar graph masses $m_v>0$ and SPD $G_v$. This decomposition is comparison data; choosing $m_v=1$ gives ordinary vertex count. Positive scalar connecting-edge weights $w_e$ must satisfy $W_e\succeq w_eG_i$ and $\Theta_e^TW_e\Theta_e\succeq w_eG_j$. Let $\gamma>0$ be the corresponding scalar Poincare gap and $q_*=\max_v\sum_{e\ni v}w_e/m_v$. For a normalized section, define $a_v=|x_v|_{G_v}$ and $\lambda=E(x)$. Covariant whitened transport singular values determine forward/reverse non-isometry costs $\delta_e,\delta_{\bar e}$. The orientation-independent distortion budget is $D_x=\sum_e w_e\min(\delta_e^2a_j^2,\delta_{\bar e}^2a_i^2)$.

The amplitude energy obeys $Q_0(a)^{1/2}\le\sqrt\lambda+\sqrt{D_x}$. Thus with $\epsilon=(\sqrt\lambda+\sqrt{D_x})^2/\gamma<1$, its weighted variance is at most $\epsilon$. The mean-amplitude normalization and a level-set argument give, for $S=\{v:a_v\ge\kappa\bar a\}$, a graph-volume deficit at most $v_\kappa=\epsilon/[(1-\kappa)^2(1-\epsilon)]$ and outside section mass at most $[\kappa/(1-\kappa)]^2\epsilon$. If $v_\kappa<\gamma/(\gamma+2q_*)$, S contains a component larger than half the graph volume, with fraction at least $1-(1+2q_*/\gamma)v_\kappa$. The supplied record includes each proof step and the existing rank-one repair's average correction budget on that component.

These bounds require expansion to dominate non-isometry as well as energy. They do not guarantee a low boundary ratio, predictive information or metastability. Rank-one corrected maps may be singular; represented-group admission and a covariant sufficient invertibility condition are separate. Passive nonorthogonal frame changes carry metrics along and preserve the masses, distortions and bounds. Actively choosing a different metric can change the physical statement.

## Arbitrary-N construction and numerical reconstruction

On any connected maximum-degree-d graph, choose a root, $h_v=c^{-\operatorname{dist}(r,v)}$ with $c>\sqrt{d-1}$, and uniformly invertible bounded matrices $B_v$. Set $H_v=h_vB_v$, $\Theta_{i\leftarrow j}=H_iH_j^{-1}$, $M_v=I$ and $W_e=I+\Theta_e^{-T}\Theta_e^{-1}$. All per-edge singular values and edge metric bounds stay uniform in N, yet $x_v=H_vz$ is an exact section whose mass is concentrated in a bounded-radius neighborhood, with an explicit geometric tail. Along any growing bounded-degree expander family its carrier fraction tends to zero despite a positive scalar gap. This is a general construction, not a small-network inference or a measured random-graph scaling law.

Three determinant-one matrices, identity and noncommuting upper/lower shears, give a nonabelian GL+(2,R) instance even though its transport holonomy is flat. If a declared self loop with $\Theta=(1+\eta)I,W=I$ is added at every vertex, the connection form becomes $L_{\mathrm{flat}}+\eta^2I$, so the same localized sections become positive bottom modes. This extension explicitly changes the validation model and is not an edit of the original lattice/plaquette archive. A uniform pathwise amplitude-comparability condition would exclude the flat construction, whereas per-edge bounds do not supply that condition. Accumulated residuals in the general nonzero-energy pathwise regime remain open.

One six-regular graph at N512 and one at N2048 ground the construction. The once-only producer passed 42 array comparisons over 153,608 entries in 1.345917 seconds. The independently implemented saved-only arithmetic check passed 86 over 209,970 entries in 3.376862 seconds, maximum discrepancy $7.6200851185\times10^{-13}$. Its first attempt failed because a helper subtracted boolean masks; the failed log was retained and the exact-mask repair was checked before the affected readback was rerun. No producer, original observation or trajectory was regenerated. Numerical validation supports the supplied construction, not a universal proof or independent mathematical certification.

| Agents | Approximate scalar gap | Analytic conservative gap lower bound | Near-isometric connected-fraction bound | Localized mass on 37 agents |
| --- | ---: | ---: | ---: | ---: |
| 512 | 1.558361 | .000652316 | .999874 | .999561 |
| 2048 | 1.541312 | .000139577 | .997243 | .999470 |

The certificate uses the separate all-pairs path bound $2/[(N-1)\operatorname{diameter}]$, not an approximate eigenvalue treated as a rigorous gap. Near-isometric controls use shear 1e-7 and bottom eigenvalue 1e-12; their actual level sets contain every agent. Localized controls use c=8, shear .25 and bottom eigenvalue 1e-6. Their per-edge singular values range from .110348 to 9.062258 and maximum condition number is 1.283196 at both sizes. Thirty-seven agents are 7.23%/1.81% of the two graphs and hold more than 99.94% physical mass. The uniform radius-two tail bound is .000796475. Their near-isometry certificate is correctly uninformative because its hypotheses fail.

CPU NumPy/SciPy sufficed. Full arrays, source snapshots, logs and failed readback are retained at `MultiAgentELBO/artifacts/soft-fixed-sectors/o1-mass-20261007`. No full suite, GPU, original-data resampling, active-config edit or historical exact heavy node was used.

## Relevance and remaining obligations

This conditionally addresses soft-sector O1 in [[Cellular sheaves and sheaf Laplacians]], [[Graph synchronization and connection Laplacians]] and [[Meta-agents and hierarchical emergence]]. It complements [[multiagentelbo-2026-10-07-graded-retention]]: even a substantial slow carrier need not recover predictive information, while a localized mode must not be labeled a formed block merely because its eigenvalue is small.

General strongly non-isometric/pathwise criteria, theory-wide O3 metric choice and graph-family S1 remain open. The active RG program in [[Gauge-Theoretic Multi-Agent VFE Model]] and [[Staged hierarchy formation and RG composability]] returns next to the existing L5 nonlinear finite-size/tail/scaling obligation. Original coupled dynamics, continuous-target precision, independent-instance prediction and thermodynamic closure remain outstanding. Navigation: [[Mathematics MOC]], [[Statistics MOC]], [[Physics MOC]] and [[CS-ML MOC]].
