---
type: run
title: "Conditional support-local Fisher amplification"
aliases: ["Local factor-incidence update bound", "Max-block retained recognition recurrence"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# Conditional support-local Fisher amplification

Codex (2026). *Conditional support-local Fisher amplification*. MultiAgentELBO [PR266](https://github.com/cdenn016/MultiAgentELBO/pull/266), source commit f666ffb57ab8a40e7cef0b1affe68f649d7c028e and merge 973aca6e9bb2f8182e89e7a51be6d258efe6925b, records [R2-LOCAL-UPDATE-AMPLIFICATION](https://github.com/cdenn016/MultiAgentELBO/blob/973aca6e9bb2f8182e89e7a51be6d258efe6925b/docs/research/2026-10-03-latent-link-rg-plan/R2-LOCAL-UPDATE-AMPLIFICATION.md). An explicit sparse local-factor Hessian comparison gives a same-driver finite-q Fisher update bound in the maximum complete-block norm. Its local coefficient is independent of N only under uniform local state, data, rule, driver and weighted-loop-incidence caps. Every receiver and sender force, native covariance/precision block, active source row and generator-history slice remains present. The coefficient and actual-law cap/exit allowance are unevaluated; full-law, storage and growing hierarchy-output costs remain charged. All four RG gates remain open at roughly 65%.

```bibtex
@misc{codex2026localupdateamplification,
  author = {Codex},
  title = {Conditional support-local Fisher amplification},
  year = {2026},
  howpublished = {MultiAgentELBO analytical checkpoint PR266},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/266}
}
```

## Original finite update and conditional local caps

[[multiagentelbo-2026-10-09-owned-storage-update-error]] supplied the full-recognition encoded recurrence with conservative volume-dependent field/proposal coefficients. This continuation replaces those coefficients through the literal local factors of the same finite-q objective. It preserves the real GL+(2) fixed-c_* lattice, K2/D4, four generator slices, three observed matter/source slices, original support and reversal-paired primitive catalog. Frozen model, prior pi, baseline, observations, history mass, loop weights, finite primitive rule and realized Brownian tuple are identical in both arms. Exact owned-broadcast storage remains separate from the mathematical field.

The five typed recognition blocks are matter mean U, matter covariance S, supported source row B, generator mean W and generator precision L. Vector blocks use Euclidean norm and symmetric matrices use Frobenius norm. The state discrepancy is the maximum over complete block discrepancies, rather than a per-agent average. Caps refer to the original fixed chart; there is no gauge-independent bound under arbitrary noncompact re-expression. Hard-zero source coordinates remain absent and zero, while supported differences have row sum zero. Symmetry and exact supported normalization are mathematical hypotheses, with initial representation and arithmetic discrepancies separately charged.

N-independence requires uniform positive spectral and source floors, bounded local means and model/data marks, positive source-prior floor, finite rule radii/mass errors, realized driver ceilings and weighted loop-incidence sums. Temperature is 0<=theta<1/4. A finite realized cap at one N does not establish such caps over an increasing-volume family. Unbounded random records and Gaussian drivers do not acquire deterministic uniform bounds merely because a finite saved realization has finite values. The finite positive quadrature weights retain their actual mass and nonunit correction; no silent normalization or population replacement occurs. Increasing q requires its own cap and population-quadrature control.

## Sparse derivative comparison with every sender retained

The scalar finite-rule objective splits exactly into matter and generator KL terms, each supported categorical row, each weighted original record, each ordered weighted loop, adjacent-episode generator mean pairs and same-block kinetic variance terms. One record depends on at most seven typed blocks: receiver U/S, sender U/S, the original primitive W/L and receiver B. A loop of length q depends on its 2q generator W/L blocks. Distinct reversal-pair IDs within an ordered loop are the original runtime hypothesis; different loops may share primitives.

For each factor, projecting its explicit local Hessian onto block b and block c bounds that block derivative and gives zero when either block is absent. Summing these actual incidences yields a nonnegative matrix M_bc with

$$
\|D_cg_b(x)\|\le M_{bc},
$$

$$
\|g_b(x)-g_b(\widehat x)\|\le\sum_cM_{bc}\|x_c-\widehat x_c\|.
$$

The proof integrates on the declared convex interior. It includes the inverse-Cholesky/exponential derivatives, sender mean and covariance terms, nonunit rule correction, KL/categorical diagonals, generator priors, all weighted loops and adjacent history terms. The source gradient's omitted common +1 changes neither its derivative nor the supported softmax. This sparse factorization changes neither estimator nor simultaneous native dynamics.

The record-count cap n_m counts receiving choices and every incoming sender occurrence; n_e counts records using a primitive. Loop caps are per-primitive weighted sums of first-derivative bounds and 2q times second-derivative bounds. Graph degree or loop length alone does not bound arbitrarily many weighted loop copies. In the original elementary-plaquette lattice, n_m<=8, n_e<=2, at most two length-four plaquettes touch a primitive and at most two adjacent history slices touch a generator block. Seven input blocks per record and 2q per loop give explicit derivative row sums. Four generator slices do not multiply a block's spatial row sum: a typed block belongs to one slice. No N, total record count, total generator-block count or total loop count appears in these local coefficients when the listed caps are uniform.

## Native Fisher correction and finite dependency cone

The same old-state targets remain H_m=S^-1+2 partial_S F_q and H_g=L-L(partial_L F_q+(partial_L F_q)^T)L, with the original matrix order. The proposal uses lower Cholesky covariance factors, covariance exponentials, native stored generator precision and supported softmax. Common covariance Brownian noise cancels from the perturbation of the exponent. Bounding update corrections around the old identity contribution yields the explicit coefficient

$$
K_\infty=1+\max(c_U,c_S,c_W,c_L,c_B),
$$

$$
\|\Phi_h(x;\zeta)-\Phi_h(\widehat x;\zeta)\|_{\infty,\mathrm{block}}
\le K_\infty\|x-\widehat x\|_{\infty,\mathrm{block}}.
$$

The source supplies every c in equations (9)-(15). The identity contribution is counted once; the source row remains exactly supported and normalized. Under fixed listed caps K_infinity has no N-dependence and tends to one as h tends to zero. Its positive-temperature pathwise excess is generally of order sqrt(h), so products over a growing step count need separate useful control. No numerical value, uniform diffusion-limit or long-time strong-error claim is supplied.

The exact raw output of a block depends only on blocks sharing its original factors, Gaussian mean/covariance partner and relevant temporal neighbors, together with fixed local data/rule and its own driver. The native lattice has spatial radius at most two cells and temporal radius one slice per step. A backward cone for a finite raw-block query over M steps has spatial radius at most 2M and temporal radius at most M within the four slices, with the source's conservative incidence-count bound. Remote initial differences outside that cone cannot affect this exact finite-step raw-state query. The cone can grow rapidly in M and gives no uniform long-horizon saving.

Locality here concerns the exact-real raw proposal. Native global finite/SPD/support stopping checks and the archived fitted preparation's shared step selection retain separate outcome laws. A remote numerical failure or global fitted step choice can change the runtime outcome. The cone result does not remove their failure/preparation charges or identify fitted initialization with deterministic baseline or zero-temperature population construction.

## Local coding recurrence and output event

Blockwise dyadic coding rounds means and mirrored symmetric entries, then normalizes each rounded active source row by its exact sum, retaining hard zeros. The source gives explicit positive-definiteness/support restrictions and a maximum block coding allowance c_Q gamma independent of how many blocks exist. Invalid inputs retain a distinct failure atom without clipping, floors or a changed field. An interior margin and actual path-survival event remain necessary.

For the same field/model/driver sequence, source equation (18) gives

$$
e_{n+1,b}\le K_n\max_{c\in D(b)}e_{n,c}+c_Q\gamma_{n+1}+a_{n+1,b},
$$

$$
E_n\le E_0\prod_{l=0}^{n-1}K_l+
\sum_{j=1}^n(c_Q\gamma_j+a_j)\prod_{l=j}^{n-1}K_l,
$$

where E_n=max_b e_n,b and a_n is the maximum additional complete-step arithmetic defect. The query-specific bound restricts caps, drivers and errors to its precise backward block-time cone. Coding/packing, field arithmetic and an arithmetic certificate are not implemented by writing these allowances. Population discrepancy cancels in the same finite-rule comparison but remains charged for a population target.

For an output kernel with conditional TV defect psi(E_M) on its actual valid cone/cap/exit event G, the common coupling gives

$$
\operatorname{TV}(\text{exact output law},\text{coded output law})
\le\Pr(G^c)+\mathbb E[\mathbf1_G\min(1,\psi(E_M))].
$$

Original-path interior clearance can imply coded containment if it exceeds the deterministic error bound; neither the local coefficient nor a saved finite enclosure supplies the native probability of G. A global all-row event unions cones across N and can add volume dependence. Independence is not assumed. The displayed output-kernel comparison does not compare a continuous parameter-state law with its discrete code in TV, which can be singular. Unbounded original-record log loss additionally needs off-event integrability. Useful actual-law cap/exit and repeated amplification allowances remain unproved and unevaluated.

## Extensive laws, storage and hierarchy output remain charged

The product-recognition KL bound still sums the number of matter/source and generator factor blocks. In the source's equation (20), maximum local error E gives E^2 times CN[1/(2a_m)+1/(4a_m^2)+1/(2eta)]+T E_prim[b_g/2+1/(4a_g^2)]. The categorical coefficient follows from its entropy Bregman remainder on the exactly normalized supported segment. A volume-independent local state error therefore does not make unnormalized full product-law divergence volume-independent. Neither recognition law is identified with the native correlated posterior.

Complete recognition coding/storage remains extensive along with frozen model, quadrature factor, Brownian stream, old replay, hierarchy/frame/copy outputs and readout. The earlier exact input-backing improvement discards no fine state or scientific force. This theorem gives no autonomous compressed parent update, packed codec, free arithmetic or parent-compression result.

For the unchanged finite hierarchy decoder, local evolved state error supplies a per-primitive allowance through exp(X_r)u_r E_M plus any separately charged group-code defect. Existing canonical-frame/copy/word factors remain unchanged: A_h=24000 J N^4 U_r^8 R_r^4 and endpoint KL coefficient 52553 N^7 L_r^2 exp(4X_r)R_r^6 retain their growth. Their inherited baseline a=(.7,-.4), identity fine/noise covariance, original four .25 prior slots and equal compatible hard dyadic weights remain hypotheses. Arbitrary baselines, native posteriors, growing root paths, depth or chart condition are not admitted by those numbers. There is no new growing hierarchy-output theorem or complete identified-law limit.

The strongest recorded advance is the explicit sparse derivative comparison and same-driver finite-horizon max-block recurrence, conditional on uniform local caps. The next unresolved obligation is a useful actual-law allowance for those local caps/exits and repeated amplification, combined with already charged growing output and storage factors. A future coefficient evaluation is a separate checkpoint; the unpublished scalar saved-input contract and its work are excluded here. Native posterior/population accuracy, full second-channel/cross-morphism coupling, recursive-chart control, growing laws and persistent endogenous formation remain open. All four gates remain open and roughly 65% is unchanged. This source-only checkpoint runs no scientific field, proposal, test, GPU workload or formal proof system and changes no model, configuration, default, host setting, base transport or manuscript.

## Source bindings and canonical publication

| Published item | Bytes | SHA256 |
|---|---:|---|
| R2-LOCAL-UPDATE-AMPLIFICATION.md | 29276 | 33d1c059bbd59acaff873b072c981efae8711aa891b126fd2416f27e5f1be9fb |
| R2-RETAINED-UPDATE-ERROR.md | 33985 | 4cf7dc6c05dfd119fc88ebb8984d99a9ec14dd3d736d834992c1a2f12e565acc |
| latent_exponential_moments.py | 10592 | 5d1e068ccb6439ad72fea7c67aa252f6f939e0a1fd8f79674acacabd9e41a2ab |
| latent_fisher_proposal.py | 6360 | 87a3a89dbd690a55382ba483be80e4e8d3622f05b02d19f76f36c05e12a4a0ac |
| R5-RAW-FIELD-LOCALITY-TRACE.md | 7798 | afb98fd62eb7cbecd35c13b3504d07eb30b6806afa93558537988c110597c5e1 |
| R3-NUMERICAL-EXIT-BUDGET.md | 17950 | 92ec342f721c5d87ab192832326d6877e26ff0739b3ec40c6ed0266c5d580d9d |
| evidence/r2-local-amplification-source-intake-20261009.json | 10862 | fb94f2783b99d24ea9d8ff1569923ab1ae8035ff6d6e3e5ef8416041e0a946eb |

The source intake binds 42 repository paths, five live sources and one dated theme context. SPEC, c10 and c12 preserve learning/scope, complete levelwise/cross-morphism state and common structural-channel context; c08b_lie_links and g11_latent_links add dynamic-link and latent-history context. These sources remain read-only and are not proof by manuscript authority. The consulted theme at Research cc7659186c0bd2bf52b2e33c701c0d772386bfff is 132002 bytes, SHA256 af65f0cd2b369660d268867528a419114ecdad400189cf03ba7e2a0724656b6b. This later ingest updates its synthesis.

Before vault mutation, actual canonical Code main, HEAD and origin/main agreed at 973aca6e9bb2f8182e89e7a51be6d258efe6925b. Completed artifacts/r2-local-amplification-handoff-20261009.json has SHA256 7c643efb0cd01b39a9457bafc60d2adc20b9ebc743be1506052e08e6faf0a19c in both code copies. That administrative handoff establishes publication/parity/preservation, separately from the conditional mathematical argument.

This develops [[Staged hierarchy formation and RG composability]], [[multiagentelbo-2026-10-09-owned-storage-update-error]], [[multiagentelbo-2026-10-09-retained-admission]] and [[multiagentelbo-2026-10-09-second-information]]. Only the new immutable source, existing theme, root index and append-only log change. All 31 prior October 9 notes, thirteen prior postflight receipts, seven earlier live source files plus the five current bindings (nine unique files), and weekly-report WIP are preserved. This ingest performs only source inspection, hashing, vault lint and authorized publication, with no science/test replay or new research mechanism.
