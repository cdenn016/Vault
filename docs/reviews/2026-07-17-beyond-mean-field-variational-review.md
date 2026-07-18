# Variational Review: Beyond Mean Field

Scope: `PIFB2.tex:3405-3559` and the added `Yedidia2005` and `CornwallJackiwTomboulis1974` bibliography records. The nested ELBO algebra was recomputed with SymPy on a normalized finite hierarchical model; the residual of Eq. `eq:nested_state_configuration_identity` was exactly `0`. The attention-row envelope was also recomputed: substituting \(\beta_j^*\propto\pi_j e^{-E_j/\tau}\) into \(\sum_j\beta_jE_j+\tau\mathrm{KL}(\beta\|\pi)\) gives \(-\tau\log\sum_j\pi_j e^{-E_j/\tau}\) with exact residual `0`.

## Findings

### 1. The no-double-counting remark falsely separates marginal belief entropy from state-correlation entropy

**Severity:** high

**Location:** `PIFB2.tex:3493`, `PIFB2.tex:3554-3556` (`rem:beyond_mf_no_double_counting`)

**Evidence:** Line 3556 states that “Gaussian belief entropy” and “state-posterior correlation entropy” live on different sample spaces. They do not. If \(q_i\) are the marginals of the correlated state posterior \(Q_X(Y)\), both are components of the same state-level joint entropy. For a block Gaussian,
\[
H(Q_X)=\frac12\log\det(2\pi e C)
=\sum_i\frac12\log\det(2\pi e C_{ii})-\mathcal I_Q(Y_1;\ldots;Y_N),
\]
where \(\mathcal I_Q\) is total correlation. Bethe entropy implements the same bookkeeping with region counting numbers. Adding marginal Gaussian entropies and a separate “correlation entropy” as independent entropies would double count the state entropy. Wainwright and Jordan (2008), Sec. 4.1, derive Bethe entropy as a node-entropy/mutual-information decomposition, not as entropies on distinct sample spaces: [primary monograph](https://people.eecs.berkeley.edu/~jordan/sail/readings/wainwright-jordan-fnt.pdf).

**Proposed correction:** Replace the last sentence of the remark with: “Marginal belief entropies and the correlation correction are components of the single state-posterior entropy and must be combined once; attention-row entropy and configuration entropy are entropies on separate simplex and configuration spaces.”

### 2. Bethe/Kikuchi region optimization is not a generic evidence bound or a controlled monotone hierarchy

**Severity:** high

**Location:** `PIFB2.tex:3482` (`eq:beyond_mf_bethe_entropy` discussion), `PIFB2.tex:3504-3508` (`eq:beyond_mf_bare_action`)

**Evidence:** The tree statement is correct, but the loopy extension is overstated. Locally consistent Bethe beliefs can be pseudomarginals that do not correspond to any global \(Q_X\), and the Bethe/Kikuchi objective gives, in general, neither an upper nor a lower bound on the log partition function. Wainwright and Jordan (2008), Secs. 4.1 and 7, explicitly distinguish nonconvex Bethe/Kikuchi objectives from tree-reweighted convex relaxations that do provide bounds. Yedidia, Freeman, and Weiss (2005) establish stationary-point and exact acyclic-region-graph results, while describing region selection as a complexity/accuracy tradeoff rather than a guaranteed monotone hierarchy: [author PDF](https://people.csail.mit.edu/billf/publications/Constructing_Free_Energy.pdf), [DOI](https://doi.org/10.1109/TIT.2005.850085). Therefore line 3508 is correct for a genuine normalized sparse-Gaussian family, but false for a generic loopy region pseudomarginal family.

**Proposed correction:** Split the statement: retain the variational upper bound for globally normalized posterior families such as sparse Gaussians; call Bethe/Kikuchi a non-bounding region approximation unless global realizability or a bound-preserving construction such as tree reweighting is imposed, and replace “controlled hierarchy” with “family of increasingly expressive region approximations whose error need not improve monotonically.”

### 3. The declared configuration variable omits the belief coordinates required by the proposed vacuum action

**Severity:** high

**Location:** `PIFB2.tex:3414`, `PIFB2.tex:3457-3463` (`eq:beyond_mf_configuration_prior`), `PIFB2.tex:3493-3508` (`eq:beyond_mf_bare_action`), `PIFB2.tex:3556`

**Evidence:** Line 3414 defines \(X\) as priors, models, supports, and frame or edge variables, while \(Y\) carries the state latents. The five-term functional proposed as a truncation of \(\mathcal F_{\mathrm{vac}}\), however, depends explicitly on the live belief/model densities \(q_i,s_i\), attention rows \(\beta,\gamma\), and the observation likelihood (`eq:free_energy_functional_final`, lines 682-687). Line 3493 also puts the fast state \(k_i\) and slow model variable \(m_i\) inside \(Y_i\). If \(q_i,s_i\) are marginals of \(Q_X\), then \(P_0\) depends on the variational posterior and the fixed-prior chain-rule proof of `thm:nested_state_configuration_vfe` no longer applies. If they are independent coordinates of \(X\), the manuscript has duplicated state-posterior objects without specifying the relation between them. The earlier exact Gibbs lift instead explicitly takes \(X\) to be a full belief configuration (`PIFB2.tex:3620`).

**Proposed correction:** Choose one level and rename it explicitly: either enlarge \(X\) to contain distinct configuration fields \(\widehat q_i,\widehat s_i,\beta,\gamma\) and define their relation to \(Q_X\), or keep \(X\) free of posterior beliefs and remove the live \(q_i,s_i\) sectors from \(\mathcal F_{\mathrm{vac}}\); in either case list exactly which observation-free five-term sectors survive in the vacuum action.

### 4. The nested-ELBO theorem is algebraically correct but omits conditions needed for its theorem statement

**Severity:** medium

**Location:** `PIFB2.tex:3436-3454` (`thm:nested_state_configuration_vfe`, `eq:nested_state_configuration_identity`)

**Evidence:** Direct symbolic expansion of the joint KL chain rule gives residual `0`, so the temperature coefficient and signs are correct. The theorem nevertheless does not state that \(X\mapsto Q_X\) is a measurable probability kernel, that \(p_\theta(o)=\int P_0(dX)p_\theta(o\mid X)\) is positive and finite, or that the relevant KL/integral terms are finite (or are interpreted consistently as extended-real quantities without \(\infty-\infty\)). Without those hypotheses, \(R(dX)Q_X(dY)\), the integral in \(\mathcal J\), and the “if and only if” equality clause need not be well-defined. These are standard conditions for the variational identity; see Bishop (2006), Sec. 10.1, and Wainwright and Jordan (2008), Sec. 3.6.

**Proposed correction:** Add the probability-kernel measurability, positive finite evidence, absolute-continuity, and finite-term hypotheses, then define \(p_\theta(o)\) explicitly before the identity.

### 5. “Controlled reductions” overstates three unproved limiting operations

**Severity:** medium

**Location:** `PIFB2.tex:3552`, `PIFB2.tex:3559`

**Evidence:** Factorizing the state posterior is a defined restriction, but \(T_{\mathrm{cfg}}\to0\) recovers a selected deterministic saddle only under a Laplace-principle/concentration hypothesis; exchangeable empirical-measure closure needs a propagation-of-chaos or large-deviation argument; and projection of the exact RG image is controlled only after a norm and a quantitative residual bound are supplied. The manuscript itself says the RG closure is a truncation hypothesis and that its residual must be measured (line 3552), so calling all four operations “controlled reductions” is stronger than the supplied results.

**Proposed correction:** Call them “formal limits and truncations” and state the separate conditions that would promote each to a controlled approximation.

### 6. The 2PI status is correctly fenced, but the closing summary should remain conditional

**Severity:** low

**Location:** `PIFB2.tex:3548`, `PIFB2.tex:3552`, `PIFB2.tex:3559`

**Evidence:** Line 3548 correctly identifies the bilocal source, double Legendre transform, and stationarity condition, and explicitly classifies 2PI as proposed rather than derived. This matches Cornwall, Jackiw, and Tomboulis (1974): [DOI](https://doi.org/10.1103/PhysRevD.10.2428). Line 3559 then shifts to the unqualified present tense, “the 2PI action makes the two-point sector self-consistent,” although no \(\Gamma_2[\varphi,G]\), source convention, skeleton truncation, or gauge-consistent 2PI construction has been given. Line 3552 also groups a configuration-level 2PI covariance with a region-enlarged state posterior, although these are different probabilistic levels.

**Proposed correction:** Write “a future gauge-consistent 2PI construction would make the configuration two-point sector self-consistent,” and keep it separate from state-level region enlargement.

## Bibliography check

The added `Yedidia2005` record at `references.bib:4103-4112` and `CornwallJackiwTomboulis1974` record at `references.bib:4114-4122` have correct author lists, titles, venues, years, page ranges, and DOIs. No bibliography correction is required.
