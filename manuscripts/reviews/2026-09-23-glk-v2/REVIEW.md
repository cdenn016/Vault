# Deep peer review: GL(K)_attention_v2 and GL(K)_supplementary_v2

**Manuscript.** R. C. Dennis, *Gauge-Covariant Gaussian Attention through Projected Matrix Links*, with its Supplementary Material. Reviewed bytes: `GL(K)_attention_v2.tex` SHA-256 `85b3918c…f3f` and `GL(K)_supplementary_v2.tex` `69607aed…e44`, the same bytes as the 2026-09-22 review in `V3_Transformer/docs/reviews/2026-09-22-glk-v2/`. The present review extends that one rather than repeating it; where the two disagree, the disagreement is stated in the section "Disagreements". Placeholders were inserted into the manuscript after the review (section "Placeholders inserted"), so the live files now hash to `34e07480…c52f` and `5f4ab7ad…0a57`.

**Method.** A coordinator (Claude Opus 5.5) read both documents, the verified-ledger record at git `HEAD` (the working-tree copy is deleted), the Research wiki, the prior review, the relevant parts of `gauge_vfe_rg`, and the preliminary data in `D:\DATA_KEEP`. Eight investigator lenses then worked in parallel, each recomputing the identities in its scope and checking primary sources: gauge theory, information geometry, variational inference, transformer architecture, empirical methods and numerics, philosophy of science and framing, editorial and citation, and code-versus-manuscript fidelity. The full lens reports, scripts, and outputs are in `panel/`. Following the 2026-09-23 agent policy, no adjudication pass was run; the findings below are investigator findings backed by executed checks and cited sources, and specific items can be sent to the `adjudicate` skill. All investigators ran on the same model as the coordinator, so no cross-model verdict is claimed.

**Scope instructions honored.** The paper is not required to be a complete VFE, FEP, or ELBO model. Missing final data are not counted as defects; placeholders were inserted instead. The author's motivation, that neural networks are one instantiation of a more general information and agent principle, is treated as the program the paper should serve.

## Recommendation and summary

**Major revision before submission.** The mathematics is sound: across eight lenses, every load-bearing identity in both documents was recomputed, and none has a sign, coefficient, normalization, or index error (residuals at machine precision; table in "Verification record"). The problems are in what the paper says its results are, in what it leaves unsaid, and in how its one experiment is described.

The headline property, gauge covariance, holds for any operator that reads the states only through the reference moments $(\xi_i,C_i)$. It holds for dot-product attention and for arbitrary nonlinear maps written that way, and it places no constraint on the learned interfaces $S_Q,S_K,T,O$. The learned frames are local dressing fields in the sense of the dressing-field method, so the covariance is of the kind Kretschmann called physically vacuous. The Conclusion's "lattice-gauge structure at the level of link fields" names no invariant content beyond the standard value/output operator, because on causal support the only closed walks are self-loops. Meanwhile the paper's informative results never reach the abstract, introduction, or conclusion. These include an exact dual-coordinate dot-product form of Gaussian-KL routing, a key-norm penalty that survives concentration and LayerNorm, the reference-coordinate normal form, and the link rank and composition algebra. The body restates six scope disclaimers two to eight times each, at 2.4 times the negation rate of comparable published papers. The central Section 4 reduction and its compensating prior are already in Movellan and Gabbur (2020) for point queries. The isotropic case is L2 self-attention (Kim, Papamakarios and Mnih 2021).

The experiment's numbers all match the archive, but the trained model does not use two mechanisms the text describes. The explicit attention residual is numerically inert: the message exceeds the state by a median factor of about $2\times10^4$ at layer 0, and deleting the residual changes cross-entropy by about $10^{-5}$ nats. An unreported weight decay drove the stored variances from 15 to about 1.04, so the routing covariance is almost entirely the static frame metric $(U_i^\top U_i)^{-1}$ of each token and position. No archived run supplies a matched comparison, and every run shares one model seed and one data-order seed.

The revision this review asks for is mostly reframing, reorganization, citation, and reporting. Four exact results that the panel derived make the paper stronger and shorter. It also asks for a small set of checkpoint-only measurements before any retraining.

## What is new here, and what is not

The author asked directly whether the KL-to-prior form of attention (Litman and Guo 2026, Proposition 3.1) is new. It is not new there, and it was not new in this manuscript either. Minimizing $-\langle p,s\rangle+\tau D_{\mathrm{KL}}(p\|\pi)$ over the simplex gives $\operatorname{softmax}(s/\tau+\log\pi)$. That is the Gibbs (Donsker–Varadhan) variational principle, Kullback's minimum-discrimination-information result, and the exponentiated-gradient step. The attention-specific readings also predate both works:
- Bianchessi et al. (arXiv:2505.22842, v1 28 May 2025) formulate positional encoding as a prior and recover NoPE and ALiBi as uniform and Laplace priors.
- Litman (arXiv:2508.08369, v1 11 August 2025) derives softmax attention as one-sided entropic optimal transport.
- Niculae and Blondel (2017) give the regularized-attention framework.
- Yang et al. (2018) add a learnable Gaussian locality bias to the logits.

The earliest dated record of the author's version on this machine is V3_Transformer commit `e4bbc58` (2026-05-29, "attention-prior registry (uniform / causal / alibi log-bias)"). Priority is therefore not available to anyone, and Section 2.6.1 should not be presented as a contribution.

What Litman and Guo do add is architectural and empirical (checked against the v2 full text). Their method, Goat, parameterizes the unnormalized log-prior as $\mathcal K_{ij}=\sum_r[\alpha_r\cos\omega_r(i-j)+\beta_r\sin\omega_r(i-j)]+u_h(j)$. The first term is a learnable, content-independent Fourier series in the offset with fixed geometric frequencies (base $10^4$). The second is a key-only term $u_h(j)=\lambda_hj+g_h(\phi_{\mathrm{abs}}(j))+b_h\mathbf 1\{j=0\}$: a learned slope, a small absolute-position MLP, and a first-token bump. They realize the prior exactly inside one unmodified SDPA or FlashAttention call by reserving $2R+2$ dimensions of each head for positional features, and the prior enters at unit temperature. They read attention sinks as the prior dominating when the content logits have a small range: their Theorem 5.1 is $\pi_{ij}e^{-\omega_i}\le p_{ij}\le\pi_{ij}e^{\omega_i}$, with $\omega_i$ the range of the content scores. They report length extrapolation at 125M parameters (C4) and 1.23B parameters (FineWeb), plus retrieval, vision, and genomics tasks.

Litman and Guo concede that the prior term "is isomorphic to an additive positional encoding". The KL-to-prior generalization therefore adds interpretation, not expressivity: any additive logit bias $b_{ij}$ equals $\log\pi_{ij}$ up to a row constant, with $\pi_{ij}=\operatorname{softmax}_jb_{ij}$. Their relative term has the same function class as the "global positional bias" of Transformer-XL (Dai et al. 2019, §3.3, term (d), $v^\top W_{k,R}R_{i-j}$ with $R$ a fixed sinusoid matrix). They cite Transformer-XL only in their introduction. Their Theorem 3 reads ALiBi as the maximum-entropy exponential prior over lags; Bianchessi et al. identified ALiBi with an exponential (Laplace) distance prior first. They cite neither Bianchessi et al., nor Niculae and Blondel, nor Movellan and Gabbur. For this manuscript, cite Litman and Guo in Section 2.6.1 as concurrent work on learned priors. Their prior is also a candidate entry for the code's prior registry. Do not cite them as the source of the identity.

| Component | Canonical counterpart (verified) | Status in this paper |
|---|---|---|
| Gibbs routing as entropy- or KL-regularized argmax; log-prior additive | Donsker–Varadhan; Kullback; Niculae & Blondel 2017; Movellan & Gabbur 2020 (mixture posterior); Litman 2025; Litman & Guo 2026 | rediscovery; cite, do not claim |
| Positional biases as log-priors (causal, window, ALiBi, T5) | Bianchessi et al. 2025 (BAM); Yang et al. 2018; Litman & Guo 2026 (learned Fourier prior, the function class of Transformer-XL's term (d)) | rediscovery; one paragraph with citations |
| Gaussian-KL scoring of token Gaussians | Vilnis & McCallum 2015 (Gaussian embeddings, KL energy); Pro-Attention 2022 (univariate per-token statistics); Transformer-MGK 2022 | precedented in kind |
| Shared-covariance reduction to biased dot product; compensating prior | Movellan & Gabbur 2020, Eqs. 14–21 (point queries); Kim et al. 2021 (L2 attention, isotropic case) | derivation correct; positioning missing |
| Gauge-equivariant attention | Cohen 2019; He 2021 (cited); CASK 2025; L-CNN 2022 | the covariance here is the dressing kind, not the constraint kind |
| General matrix links through an edge space | cellular sheaves (Hansen & Ghrist 2019), Neural Sheaf Diffusion (Bodnar et al. 2022), Sheaf Attention Networks (Barbero et al. 2022); Wetterich 2014 (cited) | sheaves are the closer counterpart; the treatise already says so (09_coarsegraining.tex:2340) |
| Attention as agent communication | TarMAC (Das et al. 2019); CommNet | uncited |
| Per-token frame tables holding 90% of parameters | sparse per-token capacity: Lample et al. 2019; Huang et al. 2025 | untested against capacity-matched controls |

**What is the author's own**, stated narrowly:
- the full-reduced-covariance projected Gaussian-KL router with distinct comparison maps;
- its exact decomposition, which in the dual coordinates of the Gaussian family is a dot product in $\mathbb R^{r+r(r+1)/2}$ with a log-partition source bias (information-geometry lens, Finding 2);
- the uncertain-query term $-\operatorname{Tr}(P_jV_{Q,i})/(2\tau)$ that point-query mixture treatments lack;
- the demonstration that neither high-dimensional concentration nor LayerNorm removes the key-norm penalty at $\tau=\sqrt r$;
- the link rank and composition algebra, including the defect $U_iO_h(T_hO_h-I)T_hU_k^{-1}$;
- the derivation of the KL-to-prior objective as the categorical part of the KL of a declared mixture joint, rather than as a posited regularizer;
- the reference-coordinate normal form of the whole realization;
- the realization itself, as a feasibility record.

## Claim-status table (condensed)

Status codes: P proven, D derived here, S suggested or structural, E empirical, Def true by construction. The full 40-row table is in `panel/philosophy.md`.

| Claim (location) | Status | Prose | Comment |
|---|---|---|---|
| Title: "Gauge-Covariant" (38); abstract "local endpoint covariance law" (50) | P, automatic | inflates | M1 |
| Gibbs row is the unique minimizer (686–721, 865–879) | P, classical | accurate; restated four times | M5, M9 |
| Row is a mixture-joint KL only at $\tau=1$ (65, 721, 900, 1189) | D | deflates: exact posterior at every $\tau$ is available | M6 |
| Shared key covariance gives biased dot product (Prop. 3) | P | accurate but unpositioned; the L2 limit is unstated | M5 |
| Content links "reproduce value and output aggregation exactly" (52) | Def | inflates: $T_h,O_h$ are $W_V,W_O$ by definition | M9 |
| Loop traces and "lattice-gauge structure at the level of link fields" (50, 71, 1189) | S | inflates ("identifies") | M4 |
| Heads versus irreducible frame blocks (650–683) | P | accurate | minor |
| "Unified derivation" of positional priors (729) | S | inflates; withdrawn at 792 | M5 |
| Test perplexity 31.04 (52, 1148) | E | accurate as a record; no severity for any Gaussian or gauge claim | M8 |
| "The explicit residual is part of this architecture" (1053, 1132) | Def | the trained model does not use it | M8 |
| Stored covariance retained for routing (1134, 1171) | Def | true, but the stored variances collapsed to about 1 | M8 |

## Mathematical errors and misstatements found

No displayed identity is wrong. The following statements are incorrect or inaccurate as written.
1. The loop-product definition at 594 reuses $B_{ij}$, which at 537–543 was defined as the comparison tensor $E_j\to E_i^*$. Products of those are not type-correct. Use the generic link $L_{ij}$ (editorial E4).
2. The RoPE intertwining condition $S_QU_i^{-1}=R_iS_Q$ at 1067 over-constrains the ordered frame $U_i=e^{X_{x_i}}e^{Y_i}$. The needed condition is $S_Qe^{-Y_i}=R_iS_Q$; the printed one forces every token factor to act trivially on the comparison row space (violation 0.855 in a constructed example; gauge F8).
3. Line 857 calls the Gaussian-bank readout "a separate probabilistic construction" from the linear decoder. In fact, the linear decoder is exactly the unit-temperature Gibbs readout of the shared-covariance templates $\mathcal N(\Sigma_*w_v,\Sigma_*)$ for any $\Sigma_*\succ0$, with $\log\omega_v=b_v+\kappa_{\mathrm{uni}}\log p_{\mathrm{uni}}(v)+\tfrac12w_v^\top\Sigma_*w_v$. The belief covariance cancels, which is why the decoder reads only $\mu^{(L)}$ (variational F5; SymPy exact).
4. Supplement 76 calls the Section 2.6 mixture "a more specific local identity" of the fixed-joint construction. It is a different joint that shares only the unit-temperature row objective (variational F2).
5. Line 939 says the nonlinear maps "require a separate equivariance construction." Two such constructions are elementary and already implemented: the frame-conjugated block `canonical_frame` and the invariant-gate block `gauge_gate` (gauge F5, philosophy F2).
6. Line 729 claims a "unified derivation" of positional priors that line 792 withdraws.
7. Several Section 5 descriptions misstate what the executed model does; they are collected under M8. Examples: the operative "additive attention residual"; conditioning diagnostics presented as operator properties; "16 validation sequences" for 608 consecutive targets; `gradient_mode` and `include_attention_entropy` presented as live settings.
8. Minor pointer and pinpoint errors are listed in the minor comments: 879 points to 4.1 instead of 4.2; 660 places the passive action in 2.4 instead of 2.2; the Fuchs et al. pinpoint should be Sec. 3.2, not 2.3.

## Major comments

### M1. Gauge covariance is a dressing covariance and constrains no learned map (essential)

The covariance proof (922) uses only $\xi_i'=\xi_i$ and $C_i'=C_i$. Executed checks show the same covariance, to about $10^{-15}$, for Gaussian-KL routing, for plain dot-product routing on dressed means, and for an arbitrary nonlinear map $U_iF(U_i^{-1}\mu_i)$. They also show it for unconstrained random $S_Q,S_K,T,O$ (philosophy F1, gauge F1). The frames transform as $U_i\to g_iU_i$ and form the invariant composites $\xi_i=U_i^{-1}\mu_i$. That makes them local dressing fields (Fournel, François, Lazzarini, Masson 2014, *Int. J. Geom. Methods Mod. Phys.* 11:1450016; review by Attard et al. 2018). François (2019, *Phil. Sci.* 86:472, §2.2, criterion C1) classifies the resulting symmetry as artificial. Kretschmann's objection (Norton 1993, §5.1) applies directly, and the program's own PIFB2.tex (2113–2116) already contains a "Kretschmann bound" remark that this paper does not apply.

The contrast with the precedents the paper cites is exact. In Cohen et al. (2019, §2.4, Eq. 5) and the Gauge Equivariant Transformer (He et al. 2021, §§4.3–4.4), frames are geometric data defined only up to the structure group, so shared maps must be intertwiners. For $G=\prod_b\mathrm{GL}(d_b)$ that requirement confines each $O_hT_h$ to $\bigoplus_b\mathbb RI_{d_b}$ by Schur's lemma. Every content link would then collapse to $\sum_bc_b\Omega_{ij}^{(b)}$, and routing to blockwise frame-only divergences (commutant dimensions computed, gauge F1). The rank loss, block mixing, and composition defect that Sections 2.3–2.4 study exist only because the frames are learned dressing. In ML terms, the learned frames fix an $\{e\}$-structure (Weiler et al. 2021, §2.1.1).

The model's genuine redundancies are different and unnamed:
- a global block re-basing $(U,S,T,O)\to(Ua,Sa,Ta,a^{-1}O)$, exact for the whole reported stack ($8.9\times10^{-15}$);
- a per-head cogredient comparison redundancy $(S_Q,S_K)\to(AS_Q,AS_K)$, $A\in\mathrm{GL}(r_h)$, under which the Gaussian KL is invariant. Dot-product scores have the contragredient $(W_QA,W_KA^{-\top})$ instead; the two share only $\mathrm O(r_h)$;
- a content redundancy $(T_h,O_h)\to(BT_h,O_hB^{-1})$.

**Fix.** Either retitle, for example "Gaussian-KL Attention on Framed States: Exact Routing Reductions and Matrix-Valued Content Links", or keep the title and state in the abstract what the covariance is: a consistency property that any operator built from reference moments shares, and one that places no constraint on the learned maps. Add the dressing-field paragraph drafted in `panel/gauge.md` (F1 Fix) after the covariance proposition, with François 2019, Kretschmann/Norton, Cohen 2019, He 2021, and Weiler 2021 (the last three are already in the bibliography). Delete "gauge-theoretic" at 757, 775, and 799, where the semantics come from the categorical source model. Name the three redundancies after line 386; drop-in text is in `panel/infogeo.md` F3 and `panel/gauge.md` F4.

### M2. The bundle typing declares a gauge freedom the model does not have (essential for coherence)

The main text makes the agent's section $\sigma_i$ the reference chart ($U_i(v)=[\sigma_i,v]$) and never declares the "local coordinates" on which the passive action acts. A rechoice $\sigma_i\to\sigma_ik_i$ of a single token's section changes routing by up to 0.965, or logits by 7.63 in a separate check. So the bundle's own gauge freedom is not a symmetry, and line 340 has to describe the proved action as acting "instead" of the right action. The treatise types it differently: $u_i=\sigma_0\cdot U_i^{-1}$, one reference section $\sigma_0$ plus the agent's local frame. In that typing the right action on the agent's section is exactly the paper's passive action (checked to $9\times10^{-14}$). The frame comparison $\Omega_{ij}$ is then the same-point change of coordinates that 02_geometry calls connection-free (gauge F3).

Separately, the pullback along the constant map $\iota$ makes the contextual bundle inert. Any bundle over a finite set is trivial, the token gauge group is $G^N$, and no connection, curvature, or topology of $\mathcal P$ enters any token formula (gauge F7). Figure 1 depicts sections over overlapping neighborhoods that have no referent in the language model; its caption concedes this.

**Fix.** Adopt the treatise typing in 298–347 (drop-in LaTeX in `panel/gauge.md` F3). Rename "gauge action" to "passive site action." State what the constant pullback implies, and what would make the base load-bearing: tokens anchored at distinct contexts, with links realized by transport along base curves (treatise `hyp:geo-graph-base-transport`). The panel divided on the smooth-bundle material. The philosophy lens would move it and Figure 1 to an appendix because no result uses it; the gauge lens would keep it with the corrected typing. The coordinator's recommendation is to keep one typed paragraph for $E_i$ and $U_i$ in the main text, and move the smooth construction and Figure 1 to an appendix unless a stated result uses them.

### M3. What the frames do in the reported model (essential)

In reference coordinates the reported model is exact in the following form (residuals $3.6\times10^{-15}$ in toy replays; confirmed against the saved diagnostics of the 31.04 run to six digits at layer 0):

$$\xi_i^{(0)}=U_i^{-1}\mu_{p,x_i},\qquad C_i=U_i^{-1}\Sigma_{p,x_i}U_i^{-\top},\qquad \xi_i^{(\ell+1)}=U_i^{-1}\Phi^{(\ell)}\bigl(U_i\xi_i^{\mathrm{att},(\ell)}\bigr),\qquad z_i=W_{\mathrm{out}}U_i\xi_i^{(L)}+b,$$

with $\Phi^{(\ell)}=(\mathrm{id}+\mathrm{MLP}^{(\ell)})\circ\operatorname{LN}$, and with the attention step itself frame-free given $\beta$. The frames therefore act through four channels:
1. a multiplicative token-and-position embedding;
2. a routing covariance that is static per token type and position, because covariance passes through unchanged and frames are fixed through the stack;
3. a token- and position-specific conjugation of the shared LayerNorm and MLP;
4. a token- and position-specific decoder.

Channels 3 and 4 exist only because the coordinate block and decoder break the covariance. The run's own metadata records the block as `coordinate_nonintertwiner`. The frames are almost entirely token specific (relative dispersion 0.99) and hold 411.7M of 456.7M parameters. In architectural terms they are per-token multiplicative adapters: relatives of multiplicative RNNs (Sutskever, Martens, Hinton 2011), FiLM, lookup-generated weights, and large input tables (Huang et al. 2025). The positional frames are an absolute learned table, clamped past position 127. The 31.04 perplexity therefore has no severity against the alternative "frames supply 412M parameters of token-conditioned neural capacity" (philosophy F2, transformer F4). If the whole stack is made covariant (dressed block and a decoder on $\xi$), the frames reduce exactly to a parameterization of $\xi^{(0)}$ and $C$ (gauge F5).

**Fix.** State the normal form as a named result immediately after the covariance proposition, and say which class of block was run. The placeholder schematic `fig:placeholder_reference_gauge` is inserted for this. Replace the sentence at 939 with a description of the two implemented covariant blocks. In the experiments, test structure against capacity (M8 and the placeholders).

### M4. "Lattice-gauge structure at the level of link fields" has no invariant content here (essential)

The routed link is $\mathcal C_{ij}=U_iA_{ij}U_j^{-1}$ with the frame-free $A_{ij}=\sum_h\beta_{ij}^{(h)}O_hT_h$, the attention-weighted sum of head output–value products. That is a pure-gauge dressing of the transformer's OV operator. Every loop trace is a polynomial in the routing weights, with loop-independent coefficients $\operatorname{Tr}(O_{h_1}T_{h_1}\cdots O_{h_r}T_{h_r})$ ($6.7\times10^{-15}$; exact in SymPy). On causal support every closed walk is constant: exhaustive enumeration finds only self-loops. So the only loop observables are self-loop traces equal to those of the standard multi-head operator ($8.9\times10^{-16}$).

Wetterich (2014) separates independent link variables with an action (his §II) from composite link variables built from site fields (his §I). The attention links are the second kind. All three defining features of lattice gauge theory are absent: independent link variables, an action, and Wilson loops with content. The trained links also sit far from the flat-composition specialization ($\|T_hO_h-I\|_F/\sqrt{32}=314$–$1{,}551$). Loop observables would therefore reflect gain, not anything resembling holonomy (empirical E9).

**Fix.** Replace the final sentences of the Conclusion, line 71, and line 335 with the texts in `panel/gauge.md` F2. Demote the flat-identification Lemma to a remark: it is a telescoping identity. Position the matrix links against cellular sheaves. The comparison cospan $E_i\to H^{\mathrm{cmp}}\leftarrow E_j$ is literally a pair of restriction maps into an edge stalk, and the treatise already classifies the program's general links as a cellular-sheaf category. If a lattice claim is wanted, make it falsifiable. Train independent invertible edge variables $\Theta_{ij}$, measure triangle holonomy using $\Theta^{-1}$ on reversed edges (defined even on a DAG), and show that forcing $\Theta$ to pure gauge degrades held-out loss. Note that the non-flat transport path (`regime_ii_covariant`) was removed from vfe3 on 2026-09-20 (commit `4cf3780`, #286), and the wiki page "Non-flat connection and the photon analogy" still describes it as wired.

### M5. Positioning and precedent (essential)

Add the precedents in "What is new here, and what is not." Four matter most.
1. Movellan and Gabbur (2020, arXiv:2010.15583) already contain the independent content law (their Eq. 7), the mixture-mean readout (Eqs. 14, 20), the key-norm term, and the prior that cancels it (Eqs. 16–21). The last of these is the paper's Eq. `projected_key_bias_compensation`, for point queries. Also cite Gabbur, Bilkhu and Movellan (NeurIPS 2021).
2. Kim, Papamakarios and Mnih (2021) define L2 self-attention. It is the isotropic case of Proposition 3, and in whitened coordinates the shared-covariance case is L2 attention too. The natural transformer limit of Gaussian-KL routing is therefore L2 attention. Dot-product attention follows only with constant or compensated key norms, which the paper itself shows are not supplied by concentration or LayerNorm (1034). This is one of the paper's better results and belongs in the abstract.
3. Niculae and Blondel (2017) at lines 65 and 720, and Bianchessi et al. (2025), Litman (2025), and Litman and Guo (2026) at 729 and 792.
4. Vilnis and McCallum (2015) at 804, where the prior bank is called "the generalization of the embedding matrix."

The Pro-Attention sentence at 67 is accurate in its distinction, since Pro-Attention uses univariate per-token statistics. Its description "Gaussian query/key statistics" should say so. The drop-in replacement is in `panel/transformer-architecture.md` F3. Section 2.6.1 should shrink to one paragraph stating the identity as known. Its only specific content is that the log-prior enters with unit coefficient while the energy is divided by $\tau$, so temperature never rescales positional biases.

### M6. Exact results the paper can state, which strengthen it and remove hedges (strongly recommended)

Each item below was derived and checked by the panel. Together they replace a dozen disclaimers with statements.

1. **Gibbs routing is an exact label posterior at every temperature.** Attach to each receiver and head a binary compatibility record with $P(o=1\mid z,J=j)=\exp(-D_{ij}(z)/\tau)$. This is a valid probability because $D\ge0$, including the capped cost $[0,8K]$ actually used. The joint is then normalized for every $\tau>0$ and every source graph, including cyclic ones, and $\beta_{ij}$ is the exact conditional posterior of the source label at the given states. Under $Q_Z\prod\beta$ it is the exact mean-field coordinate optimum, and $\mathcal A_i=\tau\mathcal F_i^{\mathrm{att}}$ with $\min\mathcal A_i=-\tau\log P(o_i=1)$. This is the optimality-variable device of control as inference (Levine 2018, Eq. 3; Kappen, Gómez, Opper 2012; Toussaint and Storkey 2006). The treatise already uses it (07j:245–267, 328–335). It discharges Supplement 68 ("an additional hypothesis") and the six unit-temperature hedges. Main 721 and 900 remain literally true, and Supplement 74's sector-scaling caveat stands (variational F1; SymPy exact; normalization residual $\le2.1\times10^{-14}$). The philosophy lens adds the necessary qualifier: exactness of this kind is available for any nonnegative cost, so it shows that Gibbs routing is consistent with exact inference, not that attention must be inference. Say that once.
2. **The attention update is an exact predictive mean.** Content aggregation, the unit residual, and the head sum are together the predictive mean of the normalized kernel $k_i'\mid k,J\sim\mathcal N(k_i+\sum_hL^{(h)}_{iJ^{(h)}}k_{J^{(h)}},Q_i)$ with independent per-head labels. Its moment-matched covariance gives a principled, context-dependent replacement for covariance passthrough. The display is in `panel/variational.md` F3 (SymPy exact; enumeration $1.8\times10^{-15}$; passive law $1.1\times10^{-14}$). The derivation leaves open $T,O,Q$, the unit coefficient, head additivity, LayerNorm and the MLP, the point collapse between layers, and the relation of cross-entropy training to this model's evidence.
3. **Gaussian-KL routing is exactly a dot product in dual coordinates.** With the query in expectation coordinates $\eta_{Q,i}=(a_i,V_{Q,i}+a_ia_i^\top)$ and the key in natural coordinates $\theta_{K,j}=(P_jb_j,-\tfrac12P_j)$, $D_{ij}=A(\theta_{K,j})+A^*(\eta_{Q,i})-\langle\eta_{Q,i},\theta_{K,j}\rangle$ (Wainwright and Jordan 2008, §5.2, Eq. 5.11; residual $9.8\times10^{-15}$). Routing is therefore exactly $\operatorname{softmax}_j(\langle\eta_{Q,i},\theta_{K,j}\rangle/\tau-A(\theta_{K,j})/\tau+\log\pi_{ij})$, with no covariance hypothesis. Proposition 3 is its mean block under shared key covariance. This turns a "conditional correspondence" into an unconditional identity and generalizes to any exponential-family agent. It matters for the program.
4. **Query uncertainty does not temper Gibbs routing.** The Gibbs row is the normalized geometric mean of the pointwise source posteriors under the query law. Query covariance enters $D_{ij}$ only through $\tfrac12\operatorname{Tr}(P_jV_{Q,i})$, and drops out entirely under shared key covariance. Example: Gibbs weights stay 0.731 as query variance goes from 0.01 to 100, while the posterior-predictive (Jeffrey) weights flatten to 0.520 (information-geometry F4; variational F2). The motivating sentence at line 59 invites the opposite reading.
   - If uncertain queries should route more diffusely, the coordinator's suggestion is to model the query mean as a noisy measurement. That gives the closed-form exact posterior $\beta_{ij}\propto\pi_{ij}\mathcal N(a_i;b_j,V_{Q,i}+V_{K,j})$, the expected-likelihood (probability-product) kernel. It flattens with query variance (0.729, 0.623, 0.523, 0.503 in the same example; closed form Monte Carlo-checked). It is covariant and cogredient-invariant in the same way.
   - This alternative has not been panel-reviewed; it is offered as an option.
5. **The KL direction is derived, not chosen.** Placing the query law in the recognition factor and the key laws as mixture components forces $D_{\mathrm{KL}}(q_Q\|p_K)$. The inclusive divergence gives $\beta=\pi$ for all costs. The reverse cost needs a shared query covariance, and symmetric divergences need both covariances shared (information-geometry F5). One paragraph in 2.6 settles a question every referee will ask.
6. **Smaller exact statements.**
   - Rotary Gaussian scores are exactly relative for arbitrary projected covariances when the rotations act on both laws (residual $2.8\times10^{-14}$); isotropy is needed only for the dot-product form (transformer F7, information-geometry F8).
   - For tied maps the data-processing inequality gives $D_{ij}\le D_{\mathrm{KL}}(q_i\|(\Omega_{ij})_*q_j)$. No such bound holds for $S_Q\ne S_K$, since identical states can give $D=0.61$ (information-geometry F9).
   - In the shared isotropic case $\sigma_h^2$ and $\tau_h$ enter only through their product, so line 681 should say they are not separately identifiable (gauge F9).
   - The shared-latent model at 902–908 reproduces the same routing at $R=0$ and yields the parameter-free content rule $T(\xi_j+R_{K,j}(a_i-b_j))$, the key-side analogue of the comparison lift (variational F7).
   - The sharp routing perturbation bound is $\sum_j|\beta_{ij}-p_{ij}|\le2\tanh(\varepsilon_i/2)\le\min(\varepsilon_i,2)$, attained by two sources (SymPy proof). The printed $e^{2\varepsilon_i}-1$ exceeds the trivial bound 2 for $\varepsilon_i>0.549$ and is vacuous on 98–100% of trained rows at layers 1–3.

### M7. Internal consistency between Section 2.6, the supplement, and the treatise (essential, low effort)

Two gaps need text.

The Section 2.6 mixture builds a generative factor from the sender state, which the text calls a belief (298, 307). Supplement 59 forbids generative factors from reading a recognition law. The construction is consistent only if the Gaussian states are fixed values, meaning data computed from the prefix before routing. A point mass on a continuous latent would give infinite free energy. Under that reading the receiver enters only as a clamped recognition marginal. The unrestricted optimum with that marginal is then the Jeffrey update rather than the Gibbs row (total variation 0.065 in a random case). State the reading in one sentence, and change Supplement 76's "more specific local identity" to "a different local joint with the same unit-temperature row objective" (variational F2).

Supplement Appendix A compresses the treatise's latent-label proposition (05b:529–720) and drops five of its hypotheses:
- the product label prior (prior R5);
- label exclusivity: one extra observed label-reading factor moves a row from 0.711 to 0.908;
- integrability of $\log c_i$;
- the per-head index;
- record normalization.

It also collides on symbols with the main text and the treatise: $z$ is the latent configuration in the supplement but the content variable in Main 3.1, and $y$ is the comparison variable in Main but the latent in 05b. One displayed joint with Bernoulli records repairs all five (`panel/variational.md` F6). Retitle the appendix "Relation to a normalized latent-source model," cite Blei et al. for the identity, and delete "The broader construction provides a consistent setting for the missing identification" (Supplement 78) unless a specific theorem is stated and proved there. An unpublished treatise cannot be the warrant for a result in this paper (philosophy F9, extending prior R8).

### M8. The reported experiment does not exercise what the text describes (essential; mostly reporting)

Every number in Section 5 matches the archived records (full table in `panel/empirical.md` §1). The implementation lens also showed that an independent float64 implementation written only from the manuscript formulas reproduces the executed forward pass to $1.2\times10^{-6}$ relative. Algorithm 1 is therefore an exact description of the computation. The problems are in what the trained model does with it.

1. **The attention residual is numerically inert at the final weights.** Per-token $\|m_i\|/\|\mu_i\|$ has median $2.1\times10^4$, $5.9\times10^3$, $5.3\times10^3$, and $1.8\times10^3$ at layers 0–3 (minimum 693 over 3,072 tokens). The residual changes the LayerNorm output by at most $1.8\times10^{-3}$ relative. Setting $\mu^{\mathrm{att}}=m$ at every layer changes cross-entropy by $-8.7\times10^{-6}$ nats on average over 24 windows (extremes $\pm3\times10^{-4}$).
   - Cause: the relational maps train with weight decay 0 and content learning rate 0.01, LayerNorm is scale-invariant, and $\sigma_{\max}(O_hT_h)$ grew from 1 to $4.6\times10^3$–$2.6\times10^4$.
   - Consequence: the evaluated network is a post-normalization stack without an attention skip. The receiving token's identity reaches the next layer only through its frame and the self-weight $\beta_{ii}\approx0.09$–$0.13$.
   - The effect is run-specific: about 600 at layer 0 in the 30.14 run (content learning rate 0.0025), and 100 falling to 2–7 in the word-level 48.42 run. Short runs keep an active residual.
   - Sources: implementation F1, empirical E1, transformer F1; the archived `estep_character.json` records 22,316 at layer 0 directly.
2. **The stored covariance collapsed, so routing covariance is frame metric.** `sigma_init=15` is a variance, and the log-variance table carries an unreported decoupled weight decay of 0.04. The code's own comment calls this "an unintended lognormal prior fighting the configured sigma_init."
   - The final variances are $1.045\pm0.054$, and at least 98% of the anisotropy of $C_i$ is frame-induced.
   - Removing all covariance from routing ($C_i\to I$) costs $+0.325$ nats on 8 windows. Resetting only the stored variances costs $+0.024\pm0.024$.
   - The decay also acted as a hidden temperature: a common rescaling of all covariances changes only the Mahalanobis term, by $1/c$, so the drift sharpened that term about 14-fold during training.
   - The run's own covariance-diversity gate failed (coefficient of variation of $\operatorname{tr}\Sigma$ 0.047 against its 0.10 threshold; Spearman correlation with per-token cross-entropy 0.145) and is not reported.
   - The covariance terms act mainly as static per-source key biases (0.09–1.05 logit standard deviation) and a per-source metric that varies about 20%. The genuinely pair-dependent static term is small (0.003–0.11 logits).
   - Sources: empirical E2, implementation F2, information-geometry F1.
3. **The conditioning diagnostics at 1159 describe coordinates, not the operator.** Under the cogredient redundancy the raw singular values and condition numbers change while every cost stays fixed; one example moved a condition number from 18 to 8,942. Gradient flow would conserve $S_QS_Q^\top+S_KS_K^\top$ and $T_hT_h^\top-O_h^\top O_h$ (Du, Hu and Lee 2018; Kunin et al. 2021). AdamW without weight decay grew the first trace about 2,285-fold, which is drift along a flat direction. The invariant quantities are the generalized spectra of $(V_{Q,i},V_{K,j})$ and the relative gains, which span 0.11–5.35 (empirical E3, information-geometry F3, gauge F4). This revises the prior figure plan's F5.
4. **Coverage and protocol statements are overstated in places.**
   - The "16 validation sequences" probe is the first validation batch: 608 consecutive targets, with intact cross-entropy 3.043 against 3.4015 for the full validation set, and no interval.
   - The capped-score checks and the per-layer ranges each come from one 128-token window, and the capped fraction's denominator includes masked future pairs.
   - The largest raw causal cost observed is about 312, against the 2048 bound.
   - Training made 4.21 passes over 116.84M unique tokens, which the text does not report. Validation cross-entropy bottoms at step 216k and rises 0.0135 nats; the best checkpoint was never evaluated on test.
   - The quoted training perplexity 20.67 is one minibatch on a different context protocol; the windowed mean is 24.5.
   - The evaluated conditionals use 128-token windows at stride 32, not the full prefix of Eq. `next_token_factorization_v2`. The product is still a normalized sequence law, and the text should say which law (variational F9).
   - Sources: empirical E4–E5, implementation F4.
5. **Capacity and calibration are missing.**
   - 98.6% of parameters are per-type tables. The context-processing parameters number 5,252,608, the convention of Kaplan et al. 2020, Fig. 6. Active parameters per token are 18.18M, dominated by the decoder rows.
   - Normalized to word level in the Megatron-LM convention, and assuming both token streams encode the same text, 31.04 corresponds to about 50.6 (54.4 without end-of-line tokens). That is in the range of 2016–2017 LSTM and GCNN results, not transformer results. The abstract names neither the dataset nor the tokenizer.
   - Sources: empirical E6–E7.
6. **No archived run supplies a matched comparison.** All 13 same-generation runs use model seed 6 and data-order seed 3. The nearest candidate (30.14) differs in nine settings. In an older pair, evaluation stride alone moved cross-entropy by 0.042 nats, more than that generation's MLP ablation (empirical E8).
7. **Code and reproducibility.**
   - The mean-only and dot-product control that Section 6.4 proposes was removed from the code (V3 commit `3ab5543`, #288).
   - Both current loaders reject the archived configuration (17 unknown fields).
   - The code forces $H=B$ and $r_h=s_h=d_b$, and computes $\tau=\kappa\sqrt{d_b}$, so $\tau=\sqrt{r_h}$ holds only by construction.
   - `gradient_mode=filtering` and `include_attention_entropy=True` are route-admission constants that the predictive path never reads.
   - bf16 covers only the MLP matrix products.
   - $\kappa_{\mathrm{uni}}=1$ is fixed and $p_{\mathrm{uni}}$ is the add-one-smoothed training unigram. With $b_{\mathrm{out}}$ learned freely and undecayed, the unigram term only offsets its initialization.
   - For the live $H=5$ run, the executed ALiBi slopes are $(1/4,1/16,1/64,1/256,1/2)$, not $2^{-8h/5}$. If that run is reported, lines 775 and 1134 would misstate the prior (transformer F9).
   - The code link is invisible in print and unversioned (editorial E19).
   - Sources: implementation F3, F5–F8.

**Fix.** Report the residual ratio, the covariance collapse, and the invariant diagnostics as measured facts. They replace several disclaimers with numbers. Point the code-availability statement to a tagged release that contains the evaluated route and the proposed controls. Run the checkpoint-only measurements first; see "Data to gather".

### M9. Organization, length, and hedging (essential)

The operator is never stated in one place. Section 2 spans pages 3–17 and holds 52 of 70 display environments. The Gibbs derivation appears four times, and the complete source-selection objective arrives on pages 13–14. The explicit full KL formula first appears on page 20. None of the three formal environments is a central result. Section 2.6.1 is legacy text from PIFB2.tex:596, with its own notation ($\pi_j$ without receiver index, slope $m$ versus $a_h$ in Algorithm 1), a stray period in Eq. `causal_prior`, blank-line paragraph breaks, and first-person generative language.

The main text carries a core negation in 22.2% of prose sentences (114 of 514). The median across six published attention and equivariance papers is 9.3%, and their maximum is 15.5%. Six disclaimers recur two to eight times each, while the front matter announces results without stating them.

The correspondence table mixes three kinds of rows: derived conditional equalities, identities by construction ($W_V=T_h$, $W_O=O_h$), and non-correspondences. Split it into those three groups.

**Fix.** Give the paper a theorem-first spine. Both the philosophy and transformer lenses proposed one; the coordinator's merged version is:
- (T1) the reference-moment normal form, with covariance, the global and head redundancies, and the self-loop-only loop invariants as corollaries;
- (T2) Gaussian-KL routing in dual coordinates, with the shared-covariance reduction to whitened L2 attention, the compensating prior, the sharp bound, and the concentration counterexample;
- (T3) the probabilistic status of routing and content: exact label posterior at every temperature, and the predictive-mean kernel with its moment-matched covariance;
- (P4) link rank and composition.

State the operator once, early, next to Figure 2. Write one Scope paragraph (drop-in in `panel/philosophy.md`, "Rewrites") and delete the repeats. Move the positive results into the abstract and conclusion (rewrites R-a through R-e in the same file). Merge the supplement into the main PDF as JMLR appendices; JMLR counts appendices toward length, and the merge also removes the `xr` dependency. Move the smooth-bundle construction, Figure 1, the optional prior-bank decoder, the representation-block detail, and 2.6.1 to appendices. arXiv rejects parentheses in file names, so rename the files before submission.

## Minor comments

**Notation** (the full symbol table and the renaming scheme R1–R24 are in `panel/editorial.md`). The required renamings are:
- R1: the head aggregate $a_i^{(\ell,h)}\to z_i^{(\ell,h)}$, which frees $a_i$ for the projected query.
- R2: one symbol for the ALiBi slope, $\alpha_h$, replacing both $m$ and $a_h$.
- R3: $b_{ij}^{(h)}\to\log\pi^{(h)}_{ij}$ in Algorithm 1.
- R5: the mixture joints $P_i,Q_{i,\beta}$ and $p_i(j,y,z)$ become $\mathbb P_i,\mathbb Q_{i,\beta}$, freeing Table 1's $p_i$ and the precision $P_j$.
- R6–R7: the prior-bank templates $\pi_v\to p_v$ and the readout $\rho_i\to\hat p_i$; Section 2.8 currently inverts the roles of $\pi$ and $\omega$.
- R8: the loop-product $B_{ij}\to L_{ij}$.
- R9: $\mathcal C_{ij}\to\mathcal M_{ij}$, since $\mathcal C$ is also the contextual base.
- R10: $\pi_j\to\pi_{ij}$ in 2.6.1.
- R11: $a_i,b_j$ are used at 681, about 290 lines before their definition.

Also: $V$ has five meanings; $R$ has five; $c$ has six; the noise covariances $Q_i,R,R_i$ collide with RoPE $R_i$; the generators $X_{x_i},Y_i$ versus $\phi_c$ differ for the same objects; $\Omega_{ij}$ has five names. Do not name a reference metric $H$ (the head count).

**Internal pointers and labels** (editorial E6, E11–E15):
- 879 points to 4.1 (should be 4.2); 660 places the passive action in 2.4 (it is 2.2); 535 and 891 cite "Eq. (18)" for Eqs. 16–17; the roadmap says "Section 5.2" because Section 5 has no label.
- Figure 2 is cited only from Figure 1's caption; Tables 2 and 3 and Lemma 1 are never cited.
- Proposition 2 has no label and is called a "theorem" three times.
- Six objects carry two labels, and twelve labels have legacy names (`sec:free_energy_section`, `tab:fep_nn_correspondence`, `sec:supp_decode_derivation`, …).
- Undefined terms: VFE, ELBO, MLP, GELU, RoPE, HeadMixer, E-step, "cognitive gauge frame," and Figure 1's $\mathcal G_K$.
- Heading case is mixed (9 Title Case, 18 sentence case), and Eq. 5 lacks its period.

**Citations and bibliography** (editorial E8, E16, E17; information-geometry F9; gauge F10):
- Fuchs et al.: invariant attention and equivariant values are in Sec. 3.2 (Eqs. 10–11), not 2.3.
- Bahuleyan et al. is variational attention, not latent alignment.
- T5 uses logarithmically bucketed offsets, not one bias per offset.
- Wetterich's gauge group is compact; line 71 should name $\mathrm{GL}(K)$ as the covariance group here.
- Give a locator for Eq. `glk_invariance`: van Erven and Harremoës 2014, Thm. 9, which covers every Rényi order; Thm. 28 gives block additivity.
- Add chapter locators for Nakahara and Frankel, and the Nakahara edition.
- Cite WikiText-103 (Merity et al. 2017), GELU, LayerNorm, and AdamW for the experiment's components.
- Sengupta and Friston 2017 prints no arXiv ID (plainnat drops `eprint`); "Mistral 7b" loses its capital; ALiBi is filed as `@article`; Blei et al. lacks its issue.
- The bibliography key `he2025cask` is CASK by Nagai, Ohno and Tomiya, not He.

**Mathematical precision.**
- Supplement B.2: for $\epsilon>0$ the LayerNorm output is bounded ($\|y\|^2<K$), so its law is not even a degenerate Gaussian (information-geometry).
- The metric at 457 is Euclidean, while the lift at 552 uses the Fisher metric $C_i^{-1}$; the two orthogonal complements differ by 1.43 rad in an example. Prior C1 is correct but incomplete: the Fisher metric is already covariant and makes the two index-raising options at 543 coincide (information-geometry F7).
- Diagonal storage is a partial gauge fixing within each frame block; the real restriction is the absence of cross-block reference covariance. This relocates prior R6 (gauge F6).
- "Window of size $w$" with $|i-j|\le w$ is a radius, and the causal window is $i-w\le j\le i$ (prior C3, confirmed).
- The causal support constraint is necessary in this architecture, because every state depends on its own token; only the prior within the prefix is unselected. Prior C4 has the right outcome and the wrong reason (transformer F10).
- The cost bound $[0,8K]$ scales with ambient $K$ while each divergence is 32-dimensional. The bound is inactive, and it should be stated per head.
- The optional Gaussian-bank readout does not say in which frame the templates live (information-geometry F10).

**Layout and template** (editorial E18–E21):
- `subcaption` is loaded but unused and triggers the caption-package warning; `\graphicspath` is dead (no `\includegraphics`, and two of its five directories do not exist).
- Better pagination needs the M9 reorganization, not float options (tested).
- JMLR items: the keywords environment, `\acks`, Code Availability as a section, the supplement running head, and empty PDF metadata.

## Questions for the author

1. Is the primary claim a formalism for communication between framed Gaussian states, a new attention mechanism, or a step in deriving neural computation from agent principles? The present evidence supports the first. The second needs matched comparisons, and the third needs a derived processing rule.
2. Are the frames meant to be geometric data or learned parameters? If learned, what should gauge covariance constrain or predict? If geometric, the shared maps must become intertwiners, and M1 shows what that collapses to.
3. Should query uncertainty make routing more diffuse? If so, the KL/Gibbs row is the wrong cost (M6.4).
4. Is the residual meant to be an operative skip? If so, the design must prevent gain growth: pre-normalization, weight decay on $T$ and $O$, or precision-weighted fusion (next section).
5. Is the stored covariance meant to be learned per token? If so, remove the log-variance decay or decay toward the initialization, and report a covariance-live arm.
6. Which run will be the headline? If it is the $H=5$ run, the ALiBi statement must change (M8.7).
7. Which venue? JMLR counts appendices toward length and has no hard limit at 35 pages; TMLR has a different template and anonymity policy.

## The paper within the "no neural architectures" program

**What this paper advances.** It gives a typed comparison/content decomposition for uncertain framed states, with an exact account of what Gaussian comparison adds over L2 and dot-product comparison. It also gives an explicit ledger of what the variational objective selects (routing) and what it does not (content maps, residual, normalization, MLP, decoder). That ledger is a map of the derivation targets the program still owes. With M6 adopted, routing has an exact probabilistic status at every temperature, the content-plus-residual update is an exact predictive mean, and the decoder is a Gibbs readout. That leaves exactly two prescribed neural components, LayerNorm and the MLP.

**What undercuts the program.** The headline property is automatic (M1). The learned frames do their work inside the imported neural block and decoder, and they hold 90% of the parameters (M3). The covariance is static and nearly uniform, so an agent's uncertainty never responds to communication (M8.2). The explicit residual, one of the components the program can now derive (M6.2), is switched off by the trained model (M8.1). The prior review's motivation paragraph credited the paper with building communication "independently of a neuron-level description." Every attention operator already has that property, so it should not be the program claim (philosophy F5).

**Formalism-native replacements for the remaining neural components** (transformer lens Task 4, variational F3, coordinator):
- **(a) Replace the MLP by Gibbs routing to a learned per-layer bank of Gaussian templates.** These are persistent latent sources, "communication with latent agents." Routing to them is again an exact label posterior (M6.1), and their contribution is again a predictive mean (M6.2).
  - With shared template covariance the layer is a normalized Gaussian radial-basis network. Normalized Gaussian units are universal approximators on compacta (Benaïm 1994, *Neural Computation* 6:319–333), so there is no expressivity cost in principle.
  - Empirically, Sukhbaatar et al. (2019) removed the feed-forward layer with persistent memory vectors in attention. They report WikiText-103 perplexity 20.6 at 133M parameters, against 24.0 for Transformer-XL Standard at 151M.
  - Geva et al. (2021) show that feed-forward layers act as key-value memories.
  - Matching the MLP's 1,050,880 parameters per layer with diagonal templates gives about 1,370 templates per head.
  - This is the most direct test of the program's thesis available with the paper's own objects.
- **(b) Reliability-weighted (Student-t) routing** from the September 20 construction: a nonlinear, uncertainty-dependent routing rule obtained from inference.
- **(c) Moment-matched covariance propagation** (M6.2), which makes covariance contextual. That is the only setting in which covariance-aware routing can mean uncertainty-aware routing.
- **(d) Precision-weighted or budgeted fusion in place of "add then LayerNorm."** The self-weight is then fixed by declared precisions or a budget and cannot be erased by gain growth, which fixes M8.1 by construction.
- **(e) Covariant normalization.** The Mahalanobis norm already exists in the code.
- **(f) The prior-bank readout,** or the linear decoder read as a Gibbs readout (M6).
- **(g) Factorized frames** $\phi_x=Ac_x$, to separate frame structure from table size.

Items (a), (c), and (g) need new code but no new theory. Items (b) and (d) need an observation model or a budget. A derivation of depth as coordinate ascent on one population objective with a template-bank prior remains open.

**Strategic consequence for the frames.** If every other component becomes covariant, the frames reduce exactly to a parameterization of the input moments and the static covariance (gauge F5). For the gauge structure to carry content in the program, one of three things is needed:
- independent invertible edge variables $\Theta_{ij}$ with an action or regularizer (whose triangle holonomy is measurable on a DAG through inverse edges);
- frames revised by inference within a sequence;
- tokens anchored at distinct base contexts, with transport along base curves.

The first of these existed as `regime_ii_covariant` and was removed on 2026-09-20. The reported flat model sits at the trivial-holonomy point of the treatise's renormalization group ($H_I=e$).

**Predictions with pre-declared failure conditions** (philosophy lens, adapted):
- P1: reduction fidelity on the checkpoint. Rows with nearly shared key covariance satisfy the $2\tanh(\varepsilon/2)$ bound.
- P2: gauge structure versus symmetry breaking. Compare the coordinate, `canonical_frame`, and `gauge_gate` blocks at matched tokens with a pre-declared margin.
- P3: frames versus capacity. Compare learned frames with identity frames plus a capacity-matched per-token table.
- P4: covariance-aware routing. Compare Gaussian-KL, L2, and dot-product routing, plus a dot-product arm with a learned per-source key metric.
- P5: the program test. Replace the MLP by template routing or an inference-derived update at matched compute.

**Series organization** (philosophy lens):
- This paper: one thesis, stated in the M9 spine.
- The extension paper (`GL(K)_extension.tex`): present it as the program paper, "agent networks without prescribed neuron layers," with P5 as its empirical claim. Remove "Gauge-Covariant Gaussian Attention" from its subtitle, since its covariance is obtained the same way (its own line 341).
- The gradients companion: fold it into the extension's appendix or a technical report. The v2 predictor does not use it.
- The treatise: cite it with a stable identifier, but never as the warrant for a result in the papers.

## Relation to gauge_vfe_rg

The two are consistent where they overlap. Supplement A's row objective and temperature caveat match 05b:529–720, apart from the omissions in M7. The binary compatibility record of M6.1 is already in 07j. The treatise's typing of the agent frame (02_geometry, $u_i=\sigma_0U_i^{-1}$) is the one that makes this paper's passive action coincide with the bundle right action (M2). The treatise's cellular-sheaf classification of general links (09_coarsegraining.tex:2340) is the right home for the matrix links (M4).

The attention paper should import these results by statement and proof, or by external citation, not by reference to an unpublished treatise. The flat vertex-frame model has trivial holonomy, so nothing in this paper feeds the renormalization program except as a baseline. That is worth one sentence, not a section.

## Placeholders inserted into the manuscript

All blocks are tagged `PLACEHOLDER` (grep for it). Two macros, `\placeholderbox` and `\datapending`, are added to each preamble. No author text was removed. Both documents compile cleanly: main 34 pages and supplement 7 pages, with no errors, undefined references, or overfull boxes, built from byte-identical copies. The pre-insertion originals are preserved byte-for-byte in `V3_Transformer/docs/reviews/2026-09-22-glk-v2/source/`. The insertion script is `apply_placeholders.py` in this folder.

| Label | Location | What to gather | Existing data |
|---|---|---|---|
| abstract `\datapending` | after the 31.04 sentence | dataset, tokenizer, context; final result with matched baseline and seeds | none |
| `fig:placeholder_reference_gauge` | after the covariance proposition (§3.2) | schematic to draw (M3); no data | none needed |
| two rows in `tab:relational_run` | §5.2 | test cross-entropy at the best-validation checkpoint (step 216,000); a training-split sample on the evaluation protocol | `best_model.pt` exists; not yet evaluated |
| `tab:placeholder_interventions` | after the probe paragraph (§5.2) | frozen interventions on the full validation split with bootstrap intervals: residual, stored and routing covariance, token and positional frames, the four frame roles | panel replays on 8–24 windows indicate magnitudes (residual about $10^{-5}$, $C\to I$ +0.325, $\Sigma\to I$ +0.024 nats); do not enter them as results |
| `fig:placeholder_routing_decomposition` | after the per-layer probe paragraph | logit decomposition; $\varepsilon_i$ and routing distance with the sharp bound; key-covariance dispersion and its frame share | weight-only parts in `panel/emp/ckpt_analysis.json`; token-level parts need one evaluation pass |
| `tab:placeholder_main_results` | end of §5 | retraining arms, conventional baselines, word-level rows (P2–P5, D6–D9 below) | none qualify (single seed; older generations) |
| `fig:placeholder_learning_curves` | end of §5 | per-seed validation curves against tokens and against GPU-hours; on-protocol generalization gap | 31.04 `metrics.csv` has one seed |
| conclusion `\datapending` | after the empirical paragraph | final matched comparison | none |
| Supp. `tab:placeholder_methods_contract` | new Appendix C | resolved configuration, including every per-table decay and the log-variance decay | 31.04 `config.json` and `summary.json` supply most fields |
| Supp. `tab:placeholder_resources` | Appendix C | storage by role, context-processing parameters, active parameters, memory, throughput | 31.04: 17.3 h, about 8.0k tokens/s, 25.5 GB peak |
| Supp. `tab:placeholder_per_seed` | Appendix C | per-seed rows with model and data-order seeds | none |
| Supp. `tab:placeholder_calibration` | Appendix C | word-normalized perplexity after a tokenizer and text audit; published reference points labeled as different protocols | test NLL 963,726 nats gives about 50.6, pending the audit |
| Supp. `fig:placeholder_numerics` | Appendix C | $\|m\|/\|\mu\|$ per layer over training; invariant spectra and orbit drift; stored log-variance over training; event counts with denominators | partial in `metrics.csv`; per-layer ratios need logging |
| Supp. `fig:placeholder_head_blocks` | Appendix C | head-by-block access matrix; entropy and self-weights | panel A computable from `final_model.pt` weights alone |
| Supp. `fig:placeholder_scaling` | Appendix C | controlled width and depth sweep | existing series are confounded |

## Data to gather, in priority order

Checkpoint-only items come first. They are cheap and several of them replace disclaimers with numbers.
- D1: the frozen-intervention table on the full validation split, including per-token $\|m\|/\|\mu\|$ and $\beta_{ii}$.
- D2: test at the best checkpoint, and an on-protocol training sample.
- D3: re-evaluate the 30.14 checkpoint at context 128 and stride 32 (its positional table covers positions 0–127).
- D4: word-normalized perplexity after a tokenizer and text audit.
- D5: invariant diagnostics and the routing decomposition.
- P1: the reduction-fidelity check.

Retraining at a proportionate scale comes next ($K=64$ or 128, four layers, 30k steps, the archived protocol, at least three replicates that vary both the model seed and the data-order seed):
- D6: frames {learned, identity} × stored covariance {decayed, live}. In the decayed-covariance, identity-frame cell the router is the biased dot product to within ±5%, so that cell is the in-codebase transformer baseline.
- D7: the `per_token_additive` capacity control.
- D8: a GPT-style baseline matched on the 5.25M context-processing parameters.
- D9: attention residual off and MLP off. The prediction from M8.1 is that turning the residual off leaves converged loss nearly unchanged.
- P2: the `coordinate`, `canonical_frame`, and `gauge_gate` blocks.
- P5: MLP replaced by template routing.
- D10: content learning rate, weight decay on $T$ and $O$, or gauge-fixing arms.

For future runs, log per-table norms (not role aggregates), the invariant parts of $(S_Q,S_K)$, $\sigma_{\max}(O_hT_h)$, per-layer $\|m\|/\|\mu\|$, and log-variance statistics at every evaluation, and keep intermediate checkpoints; the archived run kept only step 240,000.

Two code prerequisites apply. Restore or tag the mean-only and dot-product route removed in #288 before running P4. Make the configuration loader accept archived schema-25 files, or ship a tagged loader.

## Verification record

Recomputed by the panel (CPU, float64 unless stated; SymPy where marked). Every identity in the manuscript that was checked holds.

| Identity or statement | Location | Result |
|---|---|---|
| Projected Gaussian KL expansion | eq. `projected_full_kl` | $4.8\times10^{-15}$ |
| Shared-covariance biased dot product; isotropic squared distance | Prop. 3 | $4.4\times10^{-15}$; $7.1\times10^{-15}$ |
| Compensating prior; counterexample | 1013–1020 | $5.6\times10^{-16}$; exact $(0.6224593312, 0.3775406688)$ |
| Minimum-norm lift, conditional mean, $B_{ij}$ transformation law | 537–559 | $\le10^{-14}$ |
| Composition defect, path products, converse under rank conditions | 564–572 | exact (SymPy) |
| Loop traces invariant; routed traces frame-free | 594–606 | $3.2\times10^{-13}$; $6.7\times10^{-15}$ |
| Irreducibility and inequivalence of product blocks; off-block complement | 643–679 | commutants computed; exact |
| Block KL additivity and counterexample | 662–669 | $8.9\times10^{-16}$ |
| Mixture free energy; Gibbs completion and value | 688–721 | $4.4\times10^{-16}$; SymPy exact |
| Normalized content-law cancellation; shared-latent correction | 891–908 | $1.1\times10^{-16}$; $1.3\times10^{-15}$ |
| Passive covariance of the attention operator | Prop. 2 | $\le2.6\times10^{-12}$ for transformation condition numbers up to 74 |
| Decode example | 850–853 | 0.1192029220 and 0.3238277811 reproduced |
| Supplement ELBO identity; population residual identities | Supp. A, B.1 | $4.4\times10^{-16}$; $3.6\times10^{-15}$ |
| Parameter decomposition of 456,654,162 | 1136 | exact, including the dead `decode_log_scale` |
| Every Section 5 number | 1093–1161 | all match the archive |

New results established by the panel, proposed for the verified ledger:
- the dual-coordinate identity ($9.8\times10^{-15}$);
- the sharp bound $2\tanh(\varepsilon/2)$ (SymPy proof, attained);
- the binary-record exact posterior at every $\tau$ (SymPy exact; $\le2.1\times10^{-14}$);
- the predictive-mean kernel and its moment-matched covariance (SymPy exact; $1.8\times10^{-15}$);
- the linear decoder as a Gibbs readout (SymPy exact; $3.4\times10^{-15}$);
- the cogredient, content, and global-rebasing redundancies ($\le8.9\times10^{-15}$) and the gradient-flow conservation laws ($3.2\times10^{-15}$, $4.5\times10^{-17}$);
- rotary relativity for arbitrary covariance ($2.8\times10^{-14}$);
- the reference-coordinate normal form ($3.6\times10^{-15}$);
- causal closed walks are self-loops (exhaustive enumeration);
- the noisy-query routing posterior (Monte Carlo; coordinator, not panel-reviewed).

## Disagreements

Among the panel lenses:
- **Pro-Attention.** The philosophy lens judged line 67's distinction accurate; the transformer lens judged the description misleading. Resolution: the distinction is accurate, and the phrase "Gaussian query/key statistics" should say "univariate per-token statistics."
- **The principal right action.** The philosophy lens found that it is not a symmetry (logits change 7.63); the gauge lens found that, in the treatise typing, it coincides with the passive action. Both are correct in their typing. The fix is to adopt the treatise typing (M2).
- **Lead L3, "pair biases".** The information-geometry lens found the covariance terms act mostly as static per-source biases plus a per-source metric, with a small pair term. The transformer lens reported a total variation of 0.15 when the static terms are removed at layer 0. These measure different things and are compatible.
- **Lead L4.** Its premise was wrong (`weight_norm_mu` aggregates every "mu"-role optimizer group, 92.6% of it relational maps), but the conclusion is stronger than the lead stated.

With the 2026-09-22 review:
- R1: right in direction, but its proposed headline, "a typed, frame-covariant organization," keeps an automatic property as the contribution.
- R2: the reordering is agreed. Preserving the smooth-bundle foundation in the main text is contested (M2).
- R5: correct and low severity; the exclusivity omission matters more (M7).
- R6: correct mathematics, but it locates the restriction in the wrong place (minor comments).
- R7: extended by Movellan–Gabbur, Kim et al., and Niculae–Blondel.
- R8: insufficient; citing the treatise adds no warrant (M7).
- C1: correct but incomplete (minor comments).
- C2: misdescribes Press et al., whose paper states the rule for general head counts. Line 775 quotes it correctly, and the real issue is the executed $H=5$ slopes (M8.7).
- C3: correct.
- C4: right outcome, wrong reason.
- F5 of the figure plan: replace the raw diagnostics with invariant ones (M8.3).
- The prior review's §1 motivation paragraph should be revised (philosophy F5).

## Provenance, limits, and files

The coordinator and all eight investigators were Claude Opus 5.5. No adjudication or cross-model verification was run, per the 2026-09-23 agent policy. The claims rest on executed checks and primary sources, and the natural candidates for the `adjudicate` skill are M1, M4, and M8.1–M8.2.

Checkpoints were loaded only with `weights_only=True` on CPU. Forward replays covered 2–24 windows of 128 tokens, not the full corpus. The historical dirty source bytes of the run are unrecoverable, but current source reproduces its saved layer-0 diagnostics to six digits. No GPU workload, training, Lean work, or tamper test was run.

A concurrent cleanup edit to `VFE_3.0` at 09:46 today made the predictive route raise `ValueError`, because `projected_moments` rejected a stacked 4-D map. Every replay in this review predates that edit. When this report was finalized, the shape check in the working tree accepted role-stacked maps (`vfe3/relational_scoring.py:55`), so that error no longer occurs there. The route was not re-run for this review, and this review did not modify that code.

The wiki, the verified ledger, and the git state of the vault were not modified. Proposed wiki updates and ledger entries are listed above for the author's decision.

Files in this folder:
- `REVIEW.md`: this report.
- `apply_placeholders.py`: the insertion script.
- `panel/BRIEF.md`: the panel brief.
- `panel/{gauge, infogeo, variational, transformer-architecture, empirical, philosophy, editorial, implementation}.md`: the eight lens reports, with drop-in LaTeX for most fixes.
- `panel/*/`: scripts and outputs. The scripts reference the original scratchpad paths, and primary-source PDFs and text extracts were not copied.
