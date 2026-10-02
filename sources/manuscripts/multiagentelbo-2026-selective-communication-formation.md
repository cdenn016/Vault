---
type: manuscript
title: "Selective Communication and Collective Formation: MultiAgentELBO Assessment, September 20, 2026"
aliases: [Selective Communication Formation Assessment September 2026]
authors: [MultiAgentELBO research program]
year: 2026
tags: [cluster/multi-agent, cluster/gauge-theory, cluster/attention, cluster/vfe, project/multi-agent, project/transformer, field/mathematics, field/cs-ml]
created: 2026-09-20
source_status: source-based assessment and proposed extension
origin_repository: "C:/Users/chris and christine/Desktop/MultiAgentELBO"
origin_path: "docs/derivations/2026-09-11-meta-agent-formation-frontier-and-locality/links-as-communication-subspaces.md"
origin_revision: "dbbf978324fdfc38a16c859e256ecaa84b3e64db plus the working-tree source identified below"
origin_sha256: "1752e597c5813ecd69ea26118df340e3a1e7cf75d94c6c1289123338edb7e820"
---

# Selective Communication and Collective Formation: MultiAgentELBO Assessment, September 20, 2026

## Source and status

MultiAgentELBO research program, *Links as selective communication interfaces*, September 20, 2026. This immutable ingest records the [repository assessment](<C:/Users/chris and christine/Desktop/MultiAgentELBO/docs/derivations/2026-09-11-meta-agent-formation-frontier-and-locality/links-as-communication-subspaces.md>) prepared from Robert C. Dennis's proposed cognitive-subspace interpretation, the live GL(K) manuscripts and read-only implementation tracing. The working-tree source hash above identifies the actual document; the Git base alone does not identify its uncommitted content.

The note concerns the connection to collective formation. The separate [[dennis-2026-glk-matrix-links-2026-09-20]] source already records the matrix-link manuscript revision. The present source supplies an assessment and a proposed extension, with explicit algebra and counterexamples; it adds no formation theorem, empirical result, formal verification closure, or proof of population free-energy descent for the transformer predictive residual. The cognitive reading is an interpretation of represented variables, not a human-cognition experiment.

## Mechanism inherited from the manuscripts

The live [GL(K) main manuscript](https://github.com/cdenn016/Vault/blob/4406ebebaf4f94b26c2ad24f19ebadee15f988dd/manuscripts/GL(K)_attention.tex), Section `sec:relational_communication`, distinguishes the full local frame $U_i$, receiving/sending comparison maps $S_Q,S_K$, content extraction $T_h$ and insertion $O_h$. A head sends $T_hU_j^{-1}\mu_j$ and has unweighted communication map

$$L_{ij}^{(h)}=U_iO_hT_hU_j^{-1}.$$

The rectangular maps act on represented states. They do not project the gauge group itself to a smaller group. A head's content kernel specifies undisclosed directions and its receiving image specifies where information enters. The maps also specify gain and correspondence; an arbitrary $O_hT_h$ is not a projector. Other heads, routing observables and later dynamics can disclose directions hidden from one head. If $S_Q\ne S_K$, the comparison concerns compatible role observables rather than a common measurement of two complete laws.

The source's read-only trace of the V3_Transformer working tree at `e028f71`, including the current launcher WIP, reports 96-dimensional frames and three 32-dimensional interfaces per layer, with each head reading the full input. The $S_Q,S_K,T,O$ maps are learned and shared over tokens within each layer/head. This is a dated source-reported configuration, not a new model run or a statement that each edge learns an arbitrary independent map.

At the fixed base point $c_*$, the [live supplement](https://github.com/cdenn016/Vault/blob/c2cd46d86a5424339bf2284fd07782db6d921335/manuscripts/GL(K)_supplementary.tex), Appendix `app:matrix_links`, already supplies the relevant independent-link extension. For an invertible represented link $B_e=\rho(\Theta_e):E_j\to E_i$ and receiver processing $F_i=U_iOTU_i^{-1}$,

$$\mathcal L_e=F_iB_e,\qquad \mathcal L_e'=g_i\mathcal L_eg_j^{-1}.$$

Singular communication therefore coexists with invertible independent belief/model links and their inverse reversal. The reverse communication map is separately declared. The ambient agents remain local sections; vector coordinates are a specialization, and no base transport is introduced.

## Communicated agreement and private disagreement

For a common measurement $Y=M X$ with a completion $(Y,Z)$ and the required regular conditional laws, finite relative entropy decomposes as

$$D_{\mathrm{KL}}(q\Vert p)=D_{\mathrm{KL}}(q_Y\Vert p_Y)+\mathbb E_{q_Y}D_{\mathrm{KL}}\bigl(q(dz\mid Y)\Vert p(dz\mid Y)\bigr).$$

For $M=(1,0)$, $q=\mathcal N((0,a),I_2)$ and $p=\mathcal N((0,b),I_2)$, measured KL is zero and complete KL is $(a-b)^2/2$. Thus communicated agreement leaves arbitrary private disagreement possible. Equality of separate head marginals also need not identify their joint law: centered Gaussians with covariance off-diagonal entries $\rho$ and $-\rho$ have the same coordinate marginals and different joint laws when $0<|\rho|<1$.

A pair of $K$-dimensional linear states constrained by $r$ independent shared-coordinate equalities has $2K-r$ remaining coordinates: one common interface and two private complements. This is a linear-state dimension count, not a Gaussian-law dimension formula or a parent-dynamics theorem. A prospective collective must retain private variables, their conditional laws or memory, or control their contribution to free energy and subsequent evolution. Reduced KL cannot simply replace the complete-law KL bounds in the preceding formation construction.

A represented link descends through surjective measurements precisely when it respects their kernels:

$$M_i B_e=\bar B_eM_j\quad\Longleftrightarrow\quad B_e\ker M_j\subseteq\ker M_i.$$

A coordinate-swap link can expose a previously hidden coordinate. Likewise, for $\dot x=Ax$, autonomous $y=Mx$ requires $MA=\bar A M$. These conditions distinguish the existence of reduced observables from closure of their inherited dynamics.

## Normalized records and the blanket condition

The existing MultiAgentELBO `Theory/05b_local_collective_elbo.tex` assembles a normalized latent baseline with normalized interaction-record kernels. Making records depend on declared reduced observables preserves that assembly on a cyclic graph. Multiplying reciprocal state-conditionals is a different construction and has no automatic normalization. A generative record must depend on its declared latent arguments and parameters, not on live recognition parameters substituted without a model definition.

For private state $Z$, interface $Y$ and exterior $W$, a blanket claim requires $Z\perp W\mid Y$. The factorization

$$P(dy,dz,dw)=P(dy)R(dz\mid y)S(dw\mid y)$$

supplies this conditional independence. Interface-only crossing records and a baseline private conditional depending only on the interface provide a sufficient setting. Low rank by itself, sparse drift, hidden baseline correlations or additional hidden-dependent routing do not establish it. Even instantaneous conditional independence does not establish autonomous interface dynamics. See [[Markov blanket interpretation debate]] and [[biehl-2021-technical-critique]] for the distinction between probabilistic and dynamical claims.

## Proposed next calculation

The assessment proposes adding communicated and private coordinates to the normalized homogeneous four-cycle construction. Its objective and metric must determine which differences actually relax and which private variables, evaluator marks, source assignments and independent-link data the parent must retain. Learning a communication map would require its update to come from the declared normalized model. This is the next bounded obligation recorded by the assessment; this ingest does not report it as solved and does not claim a second endogenous collective episode.

## Relevance to this research

The connection joins [[GL(K) gauge-equivariant attention]] to the [[Gauge-Theoretic Multi-Agent VFE Model]] and [[Staged hierarchy formation and RG composability]] without requiring complete children to become identical. It locates the additional probabilistic and dynamical obligations on [[Meta-agents and hierarchical emergence]] and the [[Markov blanket interpretation debate]]. [[dennis-2026-glk-matrix-links-2026-09-20]] remains the source for the existing matrix-link manuscript construction.

## BibTeX

```bibtex
@misc{multiagentelbo2026selectivecommunication,
  author = {{MultiAgentELBO research program}},
  title = {Links as Selective Communication Interfaces},
  year = {2026},
  month = sep,
  note = {Unpublished repository assessment dated September 20, 2026; source-based synthesis and proposed formation extension}
}
```
