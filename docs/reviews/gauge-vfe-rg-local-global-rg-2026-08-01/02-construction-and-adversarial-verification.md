# Local/global ELBO and exact agent-network RG: construction and adversarial verification

Date: 2026-08-01
Scope: `manuscripts/gauge_vfe_rg`
Primary derivations: `05b_local_collective_elbo.tex` and `07b_agent_network_rg.tex`

## Verdict

A complete effective theory has been constructed for every finite standard-Borel agent hypergraph under explicit additional hypotheses. The only inherited foundation is one principal bundle (P\to\mathcal C), its structure group (G), and two associated statistical bundles for belief and model laws. The principal bundle does not imply a generative probability law, an ELBO, attention, an observation semantics, a coarse channel, a connection, a cross-fiber map, or an RG. Each of those objects is separately declared and then used in a proved identity.

The affirmative local/global statement is an exact-potential theorem. An agent or meta-agent minimizes a conditional VFE obtained by disintegrating one fixed normalized collective joint. A unilateral conditional change has exactly the same VFE change as the collective objective after averaging over the unchanged exterior. The local objectives are not additive shares of the global objective: a shared interaction factor appears in every incident coordinate potential but once in the collective law.

The exact RG is a common Markov pushforward of normalized laws. Its closed state contains the baseline probability, evidence submeasure, recognition and posterior laws, induced hyperedges, simultaneous root-framed holonomy and boundary data, joint attention-event law, and the full path law or exact memory kernels. Pairwise, memoryless, scalar-row, or averaged-group-link descriptions are proved truncations unless their closure conditions hold.

## Logical boundary and hypotheses

| Layer | Status | Objects |
|---|---|---|
| Inherited geometry | Given | (P\to\mathcal C), (G), (\mathcal E_b=P\times_{\widehat\rho_b}\mathcal B_b), (\mathcal E_m=P\times_{\widehat\rho_m}\mathcal B_m) |
| Probabilistic model | Additional hypothesis | normalized (P_0(dy)), normalized interaction-record kernels (K_a(y_{\partial a},do_a)) |
| Variational model | Additional hypothesis | normalized recognition law (Q\), absolute continuity, finite/no-indeterminate domains |
| Gauge interaction data | Additional hypothesis | channel-specific graph/incidence links, separate represented actions, optional cross-channel morphisms |
| Attention | Additional hypothesis | fixed receiver/source priors and a normalized label likelihood; recognition never enters the generative kernel |
| Coarse description | Additional hypothesis | recognition-independent gauge-equivariant Markov channel (C), pushed references, component-root filtration |
| Renormalization | Additional hypothesis | rescaling kernel (I_b), typed kernel composition (K_b=C_bI_b), analytic domains when actions or generators are used |

This separation implements the user's clarification that the bundle geometry is solid while the preexisting ELBO/RG theory is not presumed sound.

## The effective local and collective VFE

For an arbitrary finite hypergraph, the fixed normalized joint is

\[
P_\theta(dy,do)=P_0(dy)\prod_{a\in\mathcal A}K_a(y_{\partial a},do_a).
\]

Conditional normalization of every (K_a) proves normalization even on cyclic interaction graphs. At a regular dominated record (o), let (H_o=-\sum_a\log\ell_a(o_a\mid y_{\partial a})), (Z(o)=\int e^{-H_o}dP_0), and (\Pi_o=Z(o)^{-1}e^{-H_o}P_0). Then

\[
\mathcal F_o(Q)=\mathrm{KL}(Q\Vert P_0)+\mathbb E_QH_o
=-\log Z(o)+\mathrm{KL}(Q\Vert\Pi_o).
\]

For a nonempty agent block (B), condition the baseline on (b=y_{B^c}) and include every factor incident to (B):

\[
\mathcal F_{B,o}(r_B;b)
=\mathrm{KL}(r_B\Vert P_{0,B}(\cdot\mid b))
+\mathbb E_{r_B}H_{B,o}
=-\log Z_B(b)+\mathrm{KL}(r_B\Vert\Pi_{o,B}(\cdot\mid b)).
\]

Writing (H_o=H_{B,o}+H_{\bar B,o}), the finite-domain decomposition is

\[
\mathcal F_o(Q)=\mathrm{KL}(Q_{B^c}\Vert P_{0,B^c})
+\mathbb E_{Q_{B^c}}\!left[H_{\bar B,o}
+\mathcal F_{B,o}(r_B;Y_{B^c})\right].
\]

Therefore, for (Q=Q_{B^c}r_B) and (Q'=Q_{B^c}r'_B),

\[
\mathcal F_o(Q')-\mathcal F_o(Q)
=\mathbb E_{Q_{B^c}}
\left[\mathcal F_{B,o}(r'_B)-\mathcal F_{B,o}(r_B)\right].
\]

This is the local/global compatibility result. For a regular product recognition family with block-diagonal Fisher metric, positive learning rates, and a finite (C^1) VFE, the corresponding local natural-gradient blocks satisfy

\[
\frac{d}{dt}\mathcal F_o
=-\sum_i\gamma_i(\nabla_i\mathcal F_o)^\top G_i^{-1}
(\nabla_i\mathcal F_o)\le 0.
\]

For a product baseline, additive accounting is instead

\[
\mathcal F_o(Q)=\mathrm{TC}(Q)+\sum_i\mathrm{KL}(Q_i\Vert\rho_i)
+\mathbb E_Q\!\left[\sum_aE_{a,o}\right].
\]

The expectation cannot be split factorwise without factorwise integrability. This ledger counts every physical interaction record once and is distinct from the overlapping coordinate-local potentials.

## Attention and observation semantics

A fixed categorical source label (J_i\sim\pi_i) with selected-record likelihood proportional to (\exp[-D_{ij}/\tau_i]) gives

\[
\beta^P_{ij}(y)
=\frac{\pi_{ij}e^{-D_{ij}(y)/\tau_i}}
{\sum_k\pi_{ik}e^{-D_{ik}(y)/\tau_i}},
\]

and the exact mean-field recognition sector

\[
\mathcal F_i^{\mathrm{att}}(\beta_i^Q)
=\mathrm{KL}(\beta_i^Q\Vert\pi_i)
+\tau_i^{-1}\sum_j\beta_{ij}^Q\mathbb E_QD_{ij}.
\]

Thus the familiar
(\sum_j\beta_{ij}\mathbb E D_{ij}+\tau_i\mathrm{KL}(\beta_i\Vert\pi_i))
is (\tau_i\) times the standard ELBO sector, not an independently temperature-weighted part of the same standard ELBO. Its Fisher row flow is the replicator equation while the latent recognition law is held fixed; simultaneous latent evolution adds its chain-rule term.

Every normalized kernel (K(do\mid y)) between standard-Borel spaces has a randomization representation (O=F(Y,U)) with (U\sim\mathrm{Unif}[0,1]). Conversely, marginalizing an environment state/message policy gives a normalized observation kernel. Consequently the probability theory admits an operational agent/environment-node presentation, but the realized messages remain conditioning records in the ELBO. Calling every boundary node an autonomous agent requires additional criteria such as persistent state, action, a Markov blanket, or its own local VFE. The bundle geometry and ELBO do not supply that ontology.

## Exact coarse-graining and RG

For the same structural Markov channel (C:Y\rightsquigarrow Z), attach (C) to both recognition and posterior laws. The extended-real KL chain rule gives

\[
\mathcal F_P(Q)
=\mathcal F_{P^c}(QC)
+\mathbb E_{QC}\mathrm{KL}
\bigl(\widehat Q(dy\mid z)\Vert\widehat\Pi(dy\mid z)\bigr).
\]

The evidence is unchanged because (C) acts only on latent variables. The coarse ELBO rises exactly by the discarded conditional inference gap; no evidence has been manufactured.

The primary RG state is the normalized pair

\[
(\rho,m_o),\qquad m_o=e^{-H_o}\rho.
\]

Pushing both measures gives (\rho^c=\rho C), (m_o^c=m_oC), effective likelihood (L_o^c=dm_o^c/d\rho^c), and

\[
e^{-H_o^c(z)}
=\mathbb E_\rho[e^{-H_o(Y)}\mid Z=z].
\]

The tower property proves exact staged composition. Factor elimination generates arbitrary hyperedges; anchored Möbius inversion reconstructs every finite-valued effective action, while an extended-valued action can be retained as one top-order factor. The hidden-star calculation gives a nonzero cubic term for sufficiently small couplings, proving that pairwise closure is false in general.

Posterior disintegration supplies exact agent/meta association kernels. Gauge-covariant linear coarse maps are separately typed on vector feature fibers. Component-root indexing handles disconnected blocks; multiplicative weights and interroot transports are required for strict nested composition. The exact gauge state retains root features, channel-typed based holonomy maps, and every dressed boundary edge simultaneously. Separate conjugacy-class quotients lose their relative orientation, and a noncompact quotient is not presumed standard Borel.

Attention is coarse-grained through the joint marked event law

\[
\eta_{ij}=\alpha_i\beta_{ij},\qquad
\eta^c_{IJ}=\mathbb E\!\left[\sum_{i\in I,j\in J}\eta_{ij}\mid Z\right],
\qquad
\beta^c_{IJ}=\eta^c_{IJ}/\alpha_I^c.
\]

The theory pushes (\eta), not (\beta) alone. Marked parallel edges or the full marked operator-feature kernel are retained. A conditionally Bochner-integrable Hom moment is a derived observable; it is not a group element and does not retain mark-feature correlations by itself.

For dynamics, the complete path law is pushed forward. A state-level first-order kernel is exact for every initial law precisely under strong lumpability. Weakly lumpable initial laws can remain Markov even when strong lumpability fails. Otherwise the exact theory retains history or the derived memory/noise operators.

With rescaling kernel (I_b), define (K_b=C_bI_b) and require (K_{b_1b_2}=K_{b_1}K_{b_2}). Then

\[
\mathcal R_b(\rho,m_o)=(\rho K_b,m_oK_b).
\]

The discrete action and beta retain their reference argument:

\[
\mathcal R_b^H[H;\rho]
=-\log\frac{d((e^{-H}\rho)K_b)}{d(\rho K_b)},
\qquad
\mathfrak B_b^H[H;\rho]
=\frac{\mathcal R_b^H[H;\rho]-H}{\log b}.
\]

For a continuous common-reference semigroup with (p_t=r_te^{-H_t}),

\[
\dot H_t
=-\frac{\mathcal A^*(r_te^{-H_t})}{r_te^{-H_t}}
+\frac{\mathcal A^*r_t}{r_t},
\]

on the stated generator and positivity domain. Attention evolves primarily through (\eta); on positive receiver support,

\[
\dot\beta_{IJ}
=\frac{\dot\eta_{IJ}-\beta_{IJ}\dot\alpha_I}{\alpha_I}.
\]

The exhaustive fixed-point equation is the pair equation

\[
\mathcal R_b(\rho_*,m_*)=(\rho_*,m_*).
\]

On the dominated tier it is equivalent to reference invariance together with (\mathcal R_b^H[H_*;\rho_*]=H_*). A fixed action ratio without a fixed reference is not a fixed theory. Linearization is valid on the positive finite coarse-likelihood domain; infinite-dimensional scaling uses the full spectrum and spectral radius, with eigenoperators only for point spectrum. Identity and terminal fixed theories are exact. Strictly stable/Gaussian laws give fixed constant-likelihood pairs; one fixed block size also admits semistable laws. Flat holonomy and uniform or one-hot attention are only qualified invariant sectors until the remaining graph, occupancy, and rescaling data are also self-similar.

## Adversarial search and repairs

The approach registry records eight independent construction families. Three specialist routes were kept independent through the first round: conditional disintegration, Wilsonian law pushforward, and gauge path-groupoid/operator compression. A second round cross-attacked the candidate lemmas. A third round audited the integrated chapters, and a fourth frozen-source round attempted explicit counterexamples. A final delta round checked every repair.

The most important rejected claims and their replacements were:

| Rejected shortcut | Countermechanism | Surviving theorem |
|---|---|---|
| Sum local VFEs to obtain the global VFE | shared factors are counted once globally but in every incident coordinate potential | exact-potential difference identity plus a separate additive ledger |
| Use posterior-to-posterior peer KL in a fixed generative joint | the generative target would read the live recognition law | fixed normalized interaction-record and source-label joint |
| Close pairwise factors under elimination | hidden-star elimination generates a cubic interaction | full hypergraph closure |
| Average transported links back into (G) | convex averages of group representations can leave the group and lose mark-feature correlations | marked edges/kernel; Hom moment only on its integrability domain |
| Treat a fixed action ratio as a fixed RG theory | different references can share (H) and flow differently | invariant measure pair, or invariant reference plus invariant action |
| Classify a fixed-(b) sum law as strictly stable | log-periodic semistable laws are also fixed at one scale | strict stability as an all-scale example; semistable single-scale extension |
| Claim state-Markov closure after every blocking | hidden state produces memory unless lumpability holds | path-space closure and exact memory/noise operators |
| Quotient holonomy separately from root features/boundary links | relative orientation invariants are lost | simultaneous root-framed equivariant datum |

Round-four closure verdicts were PASS after repair for: local/global finite-domain composition; the strict inherited-geometry boundary; component-root covariance and nested linear composition; normalized joint-event attention; common-channel law pushforward; reference-dependent action beta; positive-likelihood linearization; weak-lumpability qualification; full-spectrum scaling; and the finite arbitrary-graph closure theorem.

## Symbolic and mechanical evidence

The following exact checks were used as sanity checks, not substitutes for the proofs:

- SymPy expansion of the hidden Ising star returned the cubic coefficient (2\operatorname{sech}^2(h)\tanh(h)J_1J_2J_3).
- Symbolic summation of the attention replicator flow returned zero, preserving each simplex row.
- A typed scalar example returned (CP=1) while (CAP=-1), confirming that message compression is not an energy-positivity theorem.
- The discrete KL example returned (\log(5/4)=0.2231435513\ldots).
- Anchored Möbius reconstruction and the categorical-attention KL expansion both had exact zero residual.

The final build and visual-verification record is appended after the last source freeze. The evidence-gated claim ledger is stored in `.verification/local-global-rg-ledger.json` and is validated before closure.

## Scope of completeness

The result is complete for arbitrary finite standard-Borel agent hypergraphs satisfying the displayed hypotheses; it is not a fixed-size computation or a special graph family. Projectively consistent countable cylinder laws supply finite-cylinder versions, but a prescribed infinite observation can still be null. DLR-state existence/uniqueness, thermodynamic free-energy-density convergence, and interchange of volume and RG limits remain explicitly separate infinite-volume obligations. Those are not used by the finite theorem.
