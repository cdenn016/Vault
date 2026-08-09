<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 15 adversarial adjudication of the conditional finite gauge-VFE/RG target

## Frozen question and binding verdict

This memo tests the mathematical target frozen by
`problem-contract.json:5-32,49-57,76-87` and atomized by
`claim-ledger.json:66-70`.  The source revision named by the three reconstruction
memos is `14551bb8d463f229a3b451d7222042d134c2c52d`.  The adjudicated proposition is
the conditional implication

\[
\forall d\in\mathfrak D_{\mathrm{fin}},
\qquad \mathsf H(d)\Longrightarrow \mathsf C(d),
\tag{S15.1}
\]

where \(\mathfrak D_{\mathrm{fin}}\) permits every finite vertex cardinality but
only finite standard-Borel products, and \(\mathsf H\) includes every declared
law, channel, product-reference, bundle-map, configuration, regularity,
comparison, and history hypothesis actually consumed by the relevant
conclusion.  It is not the unconditional assertion
\(\forall d\,\mathsf C(d)\), and it is not an existence theorem for undeclared
application-specific bundle maps or configuration semiconjugacies.

**Verdict for the frozen conditional finite mathematical target:
`EVIDENCE_VERIFIED`.**  I found no admitted finite datum satisfying all frozen
hypotheses for which a target conjunct fails.  No proposed Critical or High
attack survives premise matching.  The sharpest source-level concern is that
the local marked-attention paragraph does not repeat the word “measurable”; its
literal pointwise algebra admits a nonmeasurable array.  The complete theorem,
however, assumes a supplied joint marked attention-event *law*, and the contract
requires measurable versions for every displayed conditional expectation.
That concern is therefore a source-tightening item, not a counterexample to
(S15.1).

This mathematical verdict does not overwrite the aggregate release state in
`claim-ledger.json:67-70`.  That entry also binds operational numerical,
manifest, build, PDF, rendered-status, and auxiliary-freshness obligations.
Those obligations are outside this memo's allowed surface and explain why the
broader ledger entry remains unreleased even though the conditional
mathematical implication above closes.

## Evidence method and independent comparison

I reconstructed the probability, ELBO, interaction, DQM, bundle, configuration,
and history seams from the manuscript source before reading the completed
probability/operator memo.  I then compared the calculations with the three
frozen Task 15 reconstructions:

| Reconstruction | Frozen SHA-256 | Comparison result |
|---|---|---|
| `task-15-geometry-reconstruction.md` | `eb6b3ee7697d2089d7d0aabe34be2b9cedeb3525603fb1cab8ed86abbf8f087f` | Agrees on conditional bundle/configuration closure, projectability counterexamples, anomaly signs, and the semiconjugacy factor. |
| `task-15-rg-reconstruction.md` | `d71eba8eb15760d004f4b78e6f8390da414c8cbe984adf873938f2d30c6093a1` | Agrees on scale-wise product-reference admission, full-interaction exactness, generated terms, typed beta/fixed objects, and the finite/infinite boundary. |
| `task-15-probability-operator-reconstruction.md` | `0b42ce4988d2ad086bb2284e897dae892da925d43eb98620ba7372fa73daada4` | Agrees on extended ELBO typing, the common-channel chain rule, DQM/Fisher contraction, local/global VFE, attention labels, observation randomization, and the diagonal-cloning boundary. |

Agreement is not closure evidence by itself.  The closing evidence below is the
displayed derivation, exact finite witness, or type check against the frozen
hypotheses.

## Adversarial attack register

| ID | Proposed attack | Proposed severity | Disposition |
|---|---|---:|---|
| S15-A1 | Coarse ELBO monotonicity can fail or evidence can change. | High | Not sustained: the theorem attaches one common normalized latent channel to both laws and leaves the selected observation fixed. |
| S15-A2 | Local block objectives do not determine the collective ELBO, and observation-as-interaction deletes evidence. | High | Not sustained: the local theorem compares laws with one outside marginal; randomization preserves the observation random variable and its sigma-algebra. |
| S15-A3 | A coarse law need not be equivalent to a product reference. | High | True boundary, not a defect: target-scale product equivalence is an explicit per-arrow premise. |
| S15-A4 | “Finite full interaction” falsely means a dimension-free finite-parameter ansatz. | High | Not sustained: exactness retains all \(2^{|V|}-1\) sectors; sparse/finite-parameter closure is explicitly excluded. |
| S15-A5 | The marked attention event is not measurably typed. | High candidate | Not sustained against the complete target; local wording merits tightening.  A supplied event law and measurable conditional expectations are explicit global hypotheses. |
| S15-A6 | DQM/Fisher contraction fails when the coarse mechanism depends on the parameter. | High | Correct counterexample outside scope; every admitted channel is parameter independent. |
| S15-A7 | Principal scale maps, descended sections, and configuration manifolds need not exist. | Critical if automatic existence were claimed | Not sustained: the scale morphism and regular configuration objects are declared inputs, and automatic descent is explicitly refuted in the source. |
| S15-A8 | Horizontal anomalies should add without transport, or composite zero should force factorwise zero. | High | Refuted by type and cancellation; the source uses the correct transported cocycle and does not claim factorwise necessity. |
| S15-A9 | Equality of objectives automatically semiconjugates natural-gradient flows. | Critical if claimed | Explicitly refuted by the source; the target theorem additionally assumes functional compatibility and horizontal conformality. |
| S15-A10 | Beta functions, fixed objects, universal exponents, or an infinite-volume theory follow canonically from finite blocking. | Critical if claimed | Not sustained: comparison data are hypotheses, fixedness is tier-specific, and universality/infinite-volume claims are excluded. |

The following sections give the exact witness, source anchor, and falsification
condition for every proposed Critical or High attack.

## S15-A1 — common Markov channel and fixed evidence

Let \(Q\) and \(\Pi_o\) be fine recognition and posterior laws on \(\mathsf X\),
and let one normalized parameter-independent kernel
\(K:\mathsf X\rightsquigarrow\mathsf Z\) be attached to both.  Define

\[
\widehat Q(dx,dz)=Q(dx)K(x,dz),\qquad
\widehat\Pi_o(dx,dz)=\Pi_o(dx)K(x,dz).
\]

Since the conditional law of \(Z\) given \(X\) is the same under both joint
lifts,

\[
\operatorname{KL}(Q\Vert\Pi_o)
=\operatorname{KL}(QK\Vert\Pi_oK)
 +\int \operatorname{KL}
 \bigl(\widehat Q(dx\mid z)\Vert
       \widehat\Pi_o(dx\mid z)\bigr)\,QK(dz).
\tag{S15.2}
\]

The evidence mass is unchanged because \(K(x,\mathsf Z)=1\): if
\(m_o(\mathsf X)=z_o\), then \((m_oK)(\mathsf Z)=z_o\).  Consequently, for
\(\mathcal F_o(Q)=-\log z_o+\operatorname{KL}(Q\Vert\Pi_o)\),

\[
\mathcal F_o(Q)-\mathcal F_o^c(QK)
=\mathbb E_{QK}
 \operatorname{KL}(\widehat Q_{X\mid Z}\Vert
                    \widehat\Pi_{o,X\mid Z})\ge 0,
\tag{S15.3}
\]

and the corresponding ELBO rises only by deletion of a conditional inference
gap, not by increased evidence.  This is exactly
`07b_agent_network_rg.tex:24-73`, especially
`thm:rg-exact-coarse-vfe` at lines 34-66, and the extended-ELBO domain is set in
`05_elbo.tex` rather than inferred from separately integrable logarithms.

**Typed attack witness if the common-channel premise is removed.**  Take
\(\mathsf X=\{*\}\), \(Q=\Pi_o=\delta_*\), and common output
\(\mathsf Z=\{0,1\}\).  Push \(Q\) with \(K_Q(*,\cdot)=\delta_0\) and
\(\Pi_o\) with \(K_\Pi(*,\cdot)=\delta_1\).  Then

\[
\operatorname{KL}(Q\Vert\Pi_o)=0,
\qquad
\operatorname{KL}(QK_Q\Vert\Pi_oK_\Pi)=+\infty.
\]

This is not admitted by `problem-contract.json:12,29,50-52` or by the common
pushforward at `07b_agent_network_rg.tex:24-31`.

**Severity and disposition.**  High if the theorem compared independently
fitted channels or coarsened the selected observation; not sustained for the
frozen target.

**What would falsify this disposition.**  One normalized, parameter-independent
common \(K\) and one finite-evidence pair satisfying the frozen hypotheses for
which (S15.2) fails, or for which \((m_oK)(\mathsf Z)\ne m_o(\mathsf X)\), would
falsify it.

## S15-A2 — local/global ELBO and observation as interaction

For a block \(B\) with outside coordinate \(C=B^c\), disintegrate the posterior
as \(\Pi_o(dc,db)=\Pi_{o,C}(dc)\Pi_{o,B}(db\mid c)\).  For two joint laws
\(Q=Q_Cr_B\) and \(Q'=Q_Cr'_B\) with the same outside marginal and finite
posterior KLs, the KL chain rule gives

\[
\begin{aligned}
\operatorname{KL}(Q\Vert\Pi_o)
 &=\operatorname{KL}(Q_C\Vert\Pi_{o,C})
   +\mathbb E_{Q_C}\operatorname{KL}
     (r_B\Vert\Pi_{o,B}),\\
\operatorname{KL}(Q'\Vert\Pi_o)
 &=\operatorname{KL}(Q_C\Vert\Pi_{o,C})
   +\mathbb E_{Q_C}\operatorname{KL}
     (r'_B\Vert\Pi_{o,B}).
\end{aligned}
\]

Thus

\[
\mathcal F_o(Q')-\mathcal F_o(Q)
=\mathbb E_{Q_C}
 \left[\mathcal F_{B,o}^{\mathrm{ext}}(r'_B;C)
      -\mathcal F_{B,o}^{\mathrm{ext}}(r_B;C)\right].
\tag{S15.4}
\]

The outside term and the fixed evidence cancel.  The identity does not state
that singleton conditional objectives add to the global objective or that a
coordinate update raises evidence.  Source anchors are
`05b_local_collective_elbo.tex:294-369` and, for the nonadditive collective
ledger, `05b_local_collective_elbo.tex:423-485`.

**Typed attack witness if the common outside marginal is removed.**  Let the
posterior on two bits factor as
\(\Pi_o=\operatorname{Bernoulli}(1/4)_C\otimes
\operatorname{Bernoulli}(1/2)_B\).  Let \(Q\) have \(C=0\) almost surely and
\(Q'\) have \(C=1\) almost surely, with the same posterior block conditional in
both.  The local difference is zero, while

\[
\mathcal F_o(Q')-\mathcal F_o(Q)
=-\log(1/4)+\log(3/4)=\log 3.
\]

This violates the same-outside hypothesis, not (S15.4).

For observation-as-interaction, a normalized kernel \(K(do\mid y)\) on a
standard-Borel target admits a measurable randomization

\[
O=F(Y,U),\qquad U\sim\operatorname{Uniform}[0,1],\qquad
\Pr(F(y,U)\in A)=K(A\mid y).
\tag{S15.5}
\]

Equation (S15.5) preserves \(O\) and \(\sigma(O)\); it does not delete the
observation.  If \(Y\sim\operatorname{Bernoulli}(1/2)\) and \(O=Y\), then
\(I(Y;O)=\log 2\), whereas deleting \(O\) returns the prior.  The manuscript
states exactly this boundary at `05b_local_collective_elbo.tex:716-783`.

**Severity and disposition.**  High if (S15.4) were claimed across different
outside marginals, or if interaction randomization were identified with
deletion; neither claim is in the target.

**What would falsify this disposition.**  An admitted same-outside finite-KL
pair violating (S15.4), or a normalized standard-Borel observation kernel with
no measurable uniform randomization, would falsify it.

## S15-A3 — target product-reference equivalence

The law-level scale map requires no product structure:

\[
(\rho_\ell,m_\ell)\longmapsto
(\rho_\ell K_\ell,m_\ell K_\ell).
\tag{S15.6}
\]

The full-interaction chart is a separate tier.  At each admitted interaction
scale it requires a product probability
\(\nu_\ell=\bigotimes_{i\in V_\ell}\nu_{\ell i}\) with
\(\pi_\ell\sim\nu_\ell\).  This condition must be re-established at the target
scale.  It is explicit in `problem-contract.json:14-15,30,53-54`,
`claim-ledger.json:11,81-84`, and
`07b_agent_network_rg.tex:1130-1180`.

**Typed diagonal-cloning witness.**  Let \(X\sim\operatorname{Bernoulli}(1/2)\)
and let \(K\) be the deterministic map \(x\mapsto(x,x)\).  The coarse law is

\[
\pi^c(00)=\pi^c(11)=\tfrac12,
\qquad \pi^c(01)=\pi^c(10)=0.
\]

If a product law \(\nu_1\otimes\nu_2\) were equivalent to \(\pi^c\), positive
mass at both \(00\) and \(11\) would force both marginals to charge both
symbols.  It would then assign positive mass to \(01\) and \(10\), contradicting
equivalence.  Therefore the coarse law exists by (S15.6), but its target
Hoeffding chart is not admitted.

**Severity and disposition.**  High against automatic propagation of product
equivalence; not a defect because target-scale equivalence is a declared
premise.  The source itself gives this witness at
`07b_agent_network_rg.tex:1160-1180`.

**What would falsify this disposition.**  Either an admitted arrow whose target
does satisfy the declared product equivalence but for which the Hoeffding chart
is still untyped, or a target theorem invocation that omits the separate
target-scale premise, would reopen the attack.

## S15-A4 — exact all-hyperedge closure versus finite-parameter closure

For finite \(V\), define complement averaging and Möbius components by

\[
C_Af(x_A)=\int f(x_A,y_{A^c})\,\nu_{A^c}(dy_{A^c}),
\qquad
P_A=\sum_{B\subseteq A}(-1)^{|A|-|B|}C_B.
\tag{S15.7}
\]

The commuting identities \(C_AC_B=C_{A\cap B}\) give

\[
P_AP_B=\mathbf 1_{A=B}P_A,
\qquad
\sum_{A\subseteq V}P_A=I.
\tag{S15.8}
\]

With all nonempty subsets retained,

\[
\mathcal G_V=
\bigoplus_{\varnothing\ne A\subseteq V}^{\ell^1}P_A L^\infty(\nu),
\qquad
E(g)=\left[\sum_{A\ne\varnothing}g_A\right],
\qquad
\mathsf H[f]=(P_Af)_{A\ne\varnothing},
\]

and \(E\mathsf H=I\) modulo constants while \(\mathsf HE=I\).  The finite-size
bounds are

\[
\|E\|\le 1,
\qquad
\|\mathsf H\|\le 3^{|V|}-1.
\tag{S15.9}
\]

These are the exact results at `07b_agent_network_rg.tex:1182-1255`.  Exact
coarse closure then uses

\[
T_\ell^{\mathcal G}
=\mathsf H_{\ell+1}\,\overline{\mathcal Q}_\ell\,E_\ell,
\tag{S15.10}
\]

with generated higher-body components retained; see
`07b_agent_network_rg.tex:1364-1413`.

Finite \(|V|\) means finitely many subset sectors, not finite-dimensional
parameterization.  If one coordinate space is \([0,1]\) with Lebesgue
reference, the centered singleton sector

\[
L_0^\infty([0,1])
=\left\{f\in L^\infty:\int_0^1f(x)\,dx=0\right\}
\]

is already infinite dimensional.  Moreover, the bound (S15.9) is not uniform
in \(|V|\).  Thus neither a finite-parameter ansatz nor an infinite-volume
operator follows from the finite theorem.

**Severity and disposition.**  High if “finite theory” meant a dimension-free
finite coupling vector; not sustained.  `problem-contract.json:39,53-54,87`
requires all generated interactions and excludes automatic sparse or finite
retained closure.

**What would falsify this disposition.**  A bounded action on an admitted
finite product for which (S15.8) fails, a generated component omitted from
(S15.10) while exactness is claimed, or an assertion in the frozen target that
\(\mathcal G_V\) is finite dimensional would falsify it.

## S15-A5 — marked attention-event law and latent-label attention

Two attention constructions must not be conflated.

### Event-law coarse-graining

For receiver occupancy \(\alpha_i(y)\) and conditional source row
\(\beta_{ij}(y)\), the exact object is the joint marked event law

\[
\eta_{ij}(y)=\alpha_i(y)\beta_{ij}(y),
\qquad \sum_{i,j}\eta_{ij}(y)=1.
\tag{S15.11}
\]

Given the posterior bridge and a node partition, exact coarse attention is

\[
\eta^c_{IJ}(z)
=\mathbb E\left[
  \sum_{i\in I}\sum_{j\in J}\eta_{ij}(Y)\,middle|,Z=z\right],
\quad
\alpha_I^c=\sum_J\eta^c_{IJ},
\quad
\beta^c_{IJ}=\frac{\eta^c_{IJ}}{\alpha_I^c}
\quad\text{on }\{\alpha_I^c>0\}.
\tag{S15.12}
\]

Pushing \(\eta\), not \(\beta\) alone, preserves normalization and composes by
the tower property.  The source is `07b_agent_network_rg.tex:1745-1776`.

**Literal shorthand attack.**  Lines 1748-1756 say “row-stochastic” and
“normalized” but do not repeat “measurable.”  Let
\(Y=[0,1]\) with Lebesgue law, let \(A\subset[0,1]\) be non-Lebesgue-measurable,
take one occupied receiver \(\alpha_0=1\), and set

\[
\beta_{00}(y)=\mathbf 1_A(y),
\qquad
\beta_{01}(y)=1-\mathbf 1_A(y).
\tag{S15.13}
\]

Every row is pointwise stochastic and (S15.11) is pointwise normalized, but
\(\eta\) is not a Markov law and the conditional expectation in (S15.12) is
undefined.  This defeats the local paragraph if read as a self-contained list
of hypotheses.

It does not defeat the complete target.  The closure theorem explicitly
requires “joint marked attention-event laws” at
`07b_agent_network_rg.tex:2735-2756`, especially line 2749, and
`problem-contract.json:32` requires support and measurable-version hypotheses
for every displayed conditional expectation.  In standard probability usage,
a conditional law is a measurable kernel.  The array (S15.13) therefore fails
the target's input type.

### Latent-label ELBO

The separate variational label theorem assumes finite positive priors,
label-exclusive selected-record likelihood, finite measurable energies, full
record normalization, and—only for the constant-row optimum—the recognition
factorization.  Bayes' rule gives

\[
\beta^P_{ij}(y)
=\frac{\pi_{ij}e^{-D_{ij}(y)/\tau_i}}
       {\sum_k\pi_{ik}e^{-D_{ik}(y)/\tau_i}},
\tag{S15.14}
\]

whereas minimizing the constant-row recognition functional gives

\[
\beta^{Q\star}_{ij}
=\frac{\pi_{ij}\exp[-\mathbb E_QD_{ij}/\tau_i]}
       {\sum_k\pi_{ik}\exp[-\mathbb E_QD_{ik}/\tau_i]}.
\tag{S15.15}
\]

For a correlated conditional label law the exact ledger adds

\[
\mathbb E_{Q_Y}\operatorname{TC}(Q_{J\mid Y})
=\mathbb E_{Q_Y}
\operatorname{KL}\left(Q_{J\mid Y}\middle\Vert
\prod_iQ_{J_i\mid Y}\right)\ge0.
\tag{S15.16}
\]

These results and their distinct hypotheses occur at
`05b_local_collective_elbo.tex:487-646`.  Adding another selected-record factor
\(r_{ij}(y)\) that reads \(J_i\) changes (S15.14) by that factor, but violates
label exclusivity.  Taking two fair rows with \(J_1=J_2\) gives zero marginal
row KL and \(\operatorname{TC}=\log2\), refuting only a product-row ledger that
omits (S15.16).

**Severity and disposition.**  The nonmeasurable-array concern is a High
candidate against the isolated shorthand, downgraded to a non-load-bearing
source-tightening item after theorem-level premise matching.  The label attacks
are High only after removing explicit hypotheses.

**What would falsify this disposition.**  A measurable supplied event law for
which (S15.12) fails to normalize or compose, or a fully normalized,
label-exclusive finite model satisfying the complete recognition hypotheses
but violating (S15.14)-(S15.16), would falsify it.  Conversely, removing
“joint marked attention-event laws” from the closure theorem without inserting
explicit measurability at lines 1748-1756 would sustain the typing attack.

## S15-A6 — DQM and Fisher contraction

Let \(P_{\theta_0+h}\) be DQM at \(\theta_0\) with score
\(\ell\in L_0^2(P_{\theta_0};\mathbb R^d)\).  In the non-dominated form,

\[
P_{\theta_0+h}=p_hP_{\theta_0}+P_h^\perp,
\qquad
P_h^\perp(\mathsf X)=o(\|h\|^2),
\]

\[
\int\left(
\sqrt{p_h}-1-\tfrac12h^\top\ell
\right)^2dP_{\theta_0}=o(\|h\|^2).
\tag{S15.17}
\]

For one normalized parameter-independent \(K\), the joint lift
\(J_\theta(dx,dy)=P_\theta(dx)K(x,dy)\) has the same square-root remainder and
singular mass.  Projection to \(Y\) gives the coarse score

\[
\bar\ell(Y)=\mathbb E[\ell(X)\mid Y],
\tag{S15.18}
\]

so total covariance gives

\[
I_X-I_Y
=\mathbb E\operatorname{Cov}(\ell(X)\mid Y)\succeq0,
\tag{S15.19}
\]

with equality in direction \(v\) exactly when
\(v^\top\ell(X)\) is \(Y\)-measurable.  This is reconstructed at
`06_general_coarsegraining.tex:170-224`.

**Typed parameter-dependent-channel witness.**  Let the fine space be one
point, so \(P_\theta\) is constant and \(I_X=0\).  Let
\(K_\theta\) output
\(Y\sim\operatorname{Bernoulli}(1/2+\theta/4)\).  At \(\theta=0\), the output
score is \(+1/2\) at \(Y=1\) and \(-1/2\) at \(Y=0\), hence

\[
I_Y=\tfrac12(1/2)^2+\tfrac12(-1/2)^2=\tfrac14>I_X.
\]

This violates parameter independence and is not admitted by
`problem-contract.json:6,9,12,29,51`.

**Typed singular-mass witness.**  If
\(P_t=(1-t^2)P_0+t^2R_\perp\) with \(R_\perp\perp P_0\), then the singular mass
is exactly \(t^2\), not \(o(t^2)\), so the path is not DQM in (S15.17).
Replacing \(t^2\) by \(t^4\) restores the singular-mass order and a zero score.
Thus the general theorem does not silently admit an \(O(t^2)\) singular
remainder.

**Severity and disposition.**  High if \(K\) were parameter dependent or if
the singular remainder were weakened; not sustained under the frozen DQM and
fixed-channel premises.

**What would falsify this disposition.**  A DQM family and a fixed normalized
parameter-independent \(K\) satisfying (S15.17) for which the coarse score is
not (S15.18), or for which (S15.19) is negative in some direction, would
falsify it.

## S15-A7 — bundle maps, sections, and configuration existence

An equivariant principal scale map is extra data.  If
\(c:\mathcal C\to\bar{\mathcal C}\),
\(\kappa:G\to\bar G\), and
\(\mathcal P:P\to\bar P\) are declared, then

\[
\mathcal P(pg)=\mathcal P(p)\kappa(g).
\tag{S15.20}
\]

Such a map exists exactly when
\(P\times_\kappa\bar G\cong c^*\bar P\) as principal \(\bar G\)-bundles.
For the Hopf \(U(1)\)-bundle over \(S^2\) and the trivial \(U(1)\)-bundle over
the same base with \(c=\operatorname{id}\) and
\(\kappa=\operatorname{id}\), an equivariant map would be a bundle
isomorphism, contradicting their different first Chern classes.  The source
states this nonexistence boundary at
`07_general_renormalization.tex:248-275`.

Even after a bundle morphism \(\Psi:E\to\bar E\) is supplied, a section \(Q\)
descends through a surjective submersion \(f\) only when \(\Psi\circ Q\) is
constant on each fiber of \(f\).  On the total collapse
\(f:S^1\to\{*\}\), with unit-variance normal-location fibers, identity fiber
map, and

\[
Q(x)=\mathcal N(\sin x,1),
\tag{S15.21}
\]

no coarse section exists.  This is the explicit witness at
`05c_pullback_geometry.tex:753-790`.

The configuration arrow is therefore separately declared as a smooth map

\[
\mathsf R_\ell:\mathcal Q_\ell\to\mathcal Q_{\ell+1},
\tag{S15.22}
\]

not inferred from a sample kernel or pointwise bundle morphism; see
`05d_relational_inference.tex:962-990`.  The frozen target quantifies over a
declared compatible scale morphism and a regular configuration manifold
(`problem-contract.json:9,16-18,26,55,60`), while `claim-ledger.json:18`
explicitly says the data-only label creates no automatic existence result.

**Severity and disposition.**  Critical against an unconditional construction
from arbitrary principal bundles or a claim that every pointwise bundle map
acts on sections.  Not sustained because those conclusions are neither target
premises nor theorem conclusions.

**What would falsify this disposition.**  An admitted principal scale map and
intertwining fiber map that fail to descend to the associated bundle, an
admitted projectable section whose smooth descent fails under the stated
surjective-submersion hypotheses, or a declared finite configuration tier with
the required positive Gram data that is nevertheless empty or singular would
falsify it.

## S15-A8 — anomaly and cocycle algebra

For composable bundle morphisms
\(E_0\xrightarrow{\Psi_{01}}E_1\xrightarrow{\Psi_{12}}E_2\), the horizontal
defect is vertical and composes as

\[
A_{02}(e;X)
=T^V\Psi_{12}\big|_{\Psi_{01}(e)}A_{01}(e;X)
 +A_{12}\bigl(\Psi_{01}(e);T f_{01}X\bigr).
\tag{S15.23}
\]

The untransported expression \(A_{01}+A_{12}\) is ill typed because its
summands lie in different vertical tangent spaces.  Composite vanishing is
exactly

\[
T^V\Psi_{12}A_{01}=-A_{12},
\tag{S15.24}
\]

not factorwise vanishing.  On one-dimensional vertical spaces, take
\(T^V\Psi_{12}=1\), \(A_{01}=a\), and \(A_{12}=-a\) with \(a\ne0\): both
stage defects are nonzero but the composite defect vanishes.  The manuscript's
geometric instance and proof are at
`05c_pullback_geometry.tex:979-1032`.

For the base Fisher-defect cocycle, if \(v\) is the pushed fine jet,
\(\bar u=v+A\), and \(\Delta_{12}\) is the second-stage vertical Fisher defect,
the residual is

\[
\delta_{02}-\delta_{01}-f_{01}^*\delta_{12}
=\Delta_{12}(v,v)-\Delta_{12}(\bar u,\bar u)
=-2\Delta_{12}(v,A)-\Delta_{12}(A,A).
\tag{S15.25}
\]

Therefore the sharp base cocycle holds exactly when
\(\Delta_{12}(v,v)=\Delta_{12}(v+A,v+A)\); no unjustified factorwise
condition is inserted.

**Severity and disposition.**  High against untransported addition, the wrong
sign in (S15.25), or factorwise necessity.  The frozen formulas have the correct
types and signs, so the attack is not sustained.

**What would falsify this disposition.**  One admitted composable pair
violating (S15.23), or one admitted triple for which direct expansion of the
three base defects disagrees with (S15.25), would falsify it.

## S15-A9 — natural-gradient semiconjugacy

Objective compatibility alone is metric free and cannot intertwine natural
gradients.  For \(R=\operatorname{id}_{\mathbb R^2}\), objective

\[
F(x,y)=\tfrac12(x^2+2y^2),
\]

and metrics \(G=\operatorname{diag}(1,1)\) and
\(\bar G=\operatorname{diag}(1,\kappa)\) with \(\kappa\ne1\), the two gradients
are

\[
\operatorname{grad}^{G}F=(x,2y),
\qquad
\operatorname{grad}^{\bar G}F=(x,2y/\kappa).
\]

On \(xy\ne0\), no positive scalar \(a\) makes the first vector equal to
\(a\) times the second.  This exact counterexample is stated at
`05d_relational_inference.tex:1440-1452`.

The positive theorem instead assumes

\[
F_\ell=\chi_\ell\circ F_{\ell+1}\circ\mathsf R_\ell,
\qquad \chi_\ell'>0,
\tag{S15.26}
\]

and that \(\mathsf R_\ell\) is a surjective submersion with closed horizontal
splitting and horizontal conformality

\[
G_{\ell+1}(T\mathsf R_\ell Z,T\mathsf R_\ell W)
=\varphi_\ell^2G_\ell(Z,W)
\quad (Z,W\in\mathcal H).
\tag{S15.27}
\]

For \(u=\operatorname{grad}^{G_\ell}F_\ell\), (S15.26) makes \(u\) horizontal.
For every horizontal \(Z\),

\[
\begin{aligned}
G_{\ell+1}(T\mathsf R_\ell u,T\mathsf R_\ell Z)
&=\varphi_\ell^2G_\ell(u,Z)\\
&=\varphi_\ell^2\chi_\ell'
  G_{\ell+1}(\operatorname{grad}F_{\ell+1},T\mathsf R_\ell Z).
\end{aligned}
\]

Surjectivity of \(T\mathsf R_\ell|_{\mathcal H}\) and nondegeneracy imply

\[
T\mathsf R_\ell\operatorname{grad}F_\ell
=\chi_\ell'\varphi_\ell^2
 \operatorname{grad}F_{\ell+1}\circ\mathsf R_\ell.
\tag{S15.28}
\]

Thus the oriented factor is
\(a_\ell=\chi_\ell'\varphi_\ell^2>0\), exactly as proved at
`05d_relational_inference.tex:1454-1494`.  Lines 1514-1553 explicitly leave
verification of (S15.26)-(S15.27) for the manuscript's application-specific
maps open.  The frozen target quantifies only over configurations and histories
meeting their local assumptions.

**Severity and disposition.**  Critical against automatic semiconjugacy from
objective equality or Markov contraction alone.  The source itself refutes that
strengthening and proves only the conditional statement, so the attack is not
sustained.

**What would falsify this disposition.**  A pair of strong metrics and
\(C^2\) objectives satisfying every hypothesis in (S15.26)-(S15.27), with the
declared submersion and splitting, for which (S15.28) fails would falsify it.

## S15-A10 — beta, fixed objects, and finite versus universal claims

A discrete interaction beta can be subtracted only after bounded
isomorphisms \(J_\ell:\mathcal G_*\to\mathcal G_\ell\) identify one reference
space:

\[
\widehat T_\ell
=J_{\ell+1}^{-1}T_\ell^{\mathcal G}J_\ell,
\qquad
\beta_\ell^{\mathrm{ex}}(g)
=\frac{\widehat T_\ell(g)-g}{\Delta s_\ell}.
\tag{S15.29}
\]

Without \(J_\ell\), even the example
\(T:\mathbb R\to\mathbb R^2\), \(T(g)=(g,0)\), makes \(T(g)-g\) ill typed.
For a retained projection \(R_{\ell+1}\), the omitted part is the explicitly
transported residual; the retained beta is exact on the retained sector if and
only if the exact image is invariant.  For action beta, changing
\(\rho'=e^{-\Delta}\rho\) and \(H'=H-\Delta\) gives the inhomogeneous law

\[
\mathfrak B_b^H[H';\rho']
=\mathfrak B_b^H[H;\rho]-\mathfrak B_b^H[\Delta;\rho],
\tag{S15.30}
\]

not a reference-free vector.  These qualifications are at
`07b_agent_network_rg.tex:2121-2230` and
`claim-ledger.json:89-90`.

Likewise, the general nonautonomous invariant is a section

\[
y_{\ell+1}=F_\ell^{(\tau)}(y_\ell).
\tag{S15.31}
\]

Only after reference identifications is a fixed-object equation typed:

\[
\widehat F_\ell^{(\tau)}(y_*)
=J_{\ell+1}^{-1}F_\ell^{(\tau)}J_\ell(y_*)=y_*.
\tag{S15.32}
\]

Fixedness does not transfer between tiers.  A fixed conditional attention row
\(\beta\) with alternating receiver occupancy \(\alpha_\ell\) has alternating
event law \(\eta_\ell=\alpha_\ell\beta\).  A retained fixed point can have a
nonzero exact residual.  A period-two monodromy can fix every point even when
neither one-step map has a fixed point.  The finite witnesses are at
`07b_agent_network_rg.tex:2582-2687`.

Finally, “every finite \(|V|\) with no ceiling” does not quantify over a
countable network and supplies no uniform bound as \(|V|\to\infty\).  The
finite interaction norm bound grows as \(3^{|V|}-1\), and conditioning on an
infinite record, DLR existence/uniqueness, free-energy-density convergence, and
interchange of volume and RG limits remain separate.  The source draws this
line at `07b_agent_network_rg.tex:2813-2828`, while
`problem-contract.json:79-87` excludes countably infinite networks,
thermodynamic limits, universality, automatic spectral decompositions, and
automatic sparse closure.

**Severity and disposition.**  Critical against a canonical reference-free
beta, cross-tier fixedness, blocking-scheme-independent universality, or an
infinite-volume theorem.  None belongs to the frozen conditional finite target.

**What would falsify this disposition.**  A cross-space subtraction in the
frozen theorem without declared identifications, a retained fixed point labeled
exact despite a nonzero residual, a fixedness implication across tiers without
an injective commuting bridge, or a finite admitted instance violating one of
the conditional beta/fixed equations would falsify it.  Evidence about an
infinite-volume or universal strengthening would address a different target.

## Compound reachability check

The compound theorem is reachable because its compositions occur only after
the domain/codomain seams are made explicit:

\[
(\rho_\ell,m_\ell)
\xrightarrow{K_\ell}
(\rho_{\ell+1},m_{\ell+1})
\xrightarrow[\pi_{\ell+1}\sim\nu_{\ell+1}]{\mathsf H_{\ell+1}}
g_{\ell+1}
\xrightarrow[J_{\ell+1}]{\text{declared comparison}}
g_*.
\tag{S15.33}
\]

The law arrow in (S15.33) exists for every admitted normalized kernel.  The
interaction arrow is entered only under target product equivalence.  The last
arrow is entered only when beta, a reference fixed object, or an ordinary
spectrum is requested.  Bundle, configuration, and history arrows run in
parallel typed categories and are never identified with these three arrows by
notation.  The complete finite law-level theorem collects exactly the supplied
objects at `07b_agent_network_rg.tex:2735-2772`; its analytic extension lists
the extra beta/comparison hypotheses at lines 2774-2803.

The probability memo closes the measure/ELBO/DQM side; the geometry memo closes
the conditional bundle/configuration/history identities and separately lists
application-specific existence obligations; the RG memo closes the finite
law/full-interaction and conditional comparison tiers while rejecting their
infinite or universal extensions.  Direct substitution of their equations
leaves no domain mismatch in (S15.33).

## Final adjudication

No Critical or High defect remains in the frozen conditional finite target.
Every sharp negative witness has one of four exact dispositions:

1. it violates an explicit premise, as for mismatched channels,
   parameter-dependent coarse mechanisms, or nonmeasurable attention arrays;
2. it blocks entry into a conditional tier, as for diagonal cloning and product
   Hoeffding coordinates;
3. it refutes an automatic-existence claim the source itself rejects, as for
   Hopf-bundle scale maps, section descent, or manuscript-specific natural
   gradient semiconjugacy; or
4. it addresses an excluded strengthening, as for finite-parameter closure,
   universal exponents, physical time, or infinite-volume RG.

Accordingly, the one requested adjudication is:

\[
\boxed{\text{frozen conditional finite mathematical target}
       \;=\;\texttt{EVIDENCE\_VERIFIED}.}
\]

The verdict would become `REFUTED` upon one admitted finite counterexample to a
universal conjunct.  It would become `INCONCLUSIVE` if a load-bearing premise,
type, or derivation used above ceased to be frozen or inspectable.  Neither
condition occurs in the inspected snapshot.

## Raw artifact audit

All hashes below are raw-file SHA-256 digests; byte counts are filesystem byte
lengths.  `finalNL=true` means the raw file ends in LF.  The adjudication memo is
excluded from its own embedded digest to avoid a self-referential hash; its raw
digest is to be recorded by the caller after finalization.

| Artifact | SHA-256 | Bytes | EOL |
|---|---|---:|---|
| `problem-contract.json` | `7cba2e9bbfe34028d6a994359e53c761779bd255c5405bfa3996c50ca575bc22` | 11,510 | CRLF; finalNL=true |
| `claim-ledger.json` | `e4aad3402e069f71e0fd63f71d6ef78b9a48fba621e9a54a188dd2d554fed2be` | 119,251 | CRLF; finalNL=true |
| `task-15-geometry-reconstruction.md` | `eb6b3ee7697d2089d7d0aabe34be2b9cedeb3525603fb1cab8ed86abbf8f087f` | 40,797 | LF; finalNL=true |
| `task-15-rg-reconstruction.md` | `d71eba8eb15760d004f4b78e6f8390da414c8cbe984adf873938f2d30c6093a1` | 46,979 | LF; finalNL=true |
| `task-15-probability-operator-reconstruction.md` | `0b42ce4988d2ad086bb2284e897dae892da925d43eb98620ba7372fa73daada4` | 50,325 | LF; finalNL=true |
| `SPEC.md` | `ab59a4d02e1c475b6384403013458d39f88f170d592edf802d4c772dd7320571` | 54,048 | CRLF; finalNL=true |
| `03_probability.tex` | `5cf6a326900cf373f04f6d05379df20cca0edc1cdde51a0daae9e739a9813520` | 41,941 | CRLF; finalNL=true |
| `05_elbo.tex` | `d6bd224135ed4cf370548729713555415b4cc0eef5f76f6c7a65853d073ff2cc` | 49,605 | CRLF; finalNL=true |
| `05b_local_collective_elbo.tex` | `22d35509fa707e46de71e331df614ccf2aa48572cc456a02ee717a7a9dc39b60` | 35,090 | CRLF; finalNL=true |
| `05c_pullback_geometry.tex` | `a035cf5f69e9179f56b2d94cb697989d15e2bb4b0b13e412bc98354342bb9196` | 67,859 | CRLF; finalNL=true |
| `05d_relational_inference.tex` | `7b1d486962235465d69a105b51e6608148c4d8b4fa942adb2d4384a0ca868715` | 84,440 | CRLF; finalNL=true |
| `06_general_coarsegraining.tex` | `4891a8f5fa86ac0fa5266381e2c67161125645034ca40395cb2e3ed1b67dc9b2` | 33,532 | CRLF; finalNL=true |
| `07_general_renormalization.tex` | `ceda98a49f4122de39d70f784288860ab727abfa217a92b1230591e6ce76bcad` | 53,716 | CRLF; finalNL=true |
| `07b_agent_network_rg.tex` | `5eb159493ec727218e2eaca4cf47f3fddeb090f6e193352846ad2a43181437ca` | 136,451 | CRLF; finalNL=true |

`git diff --check`: **PASS (exit 0; no whitespace-error record)**.  Git emitted
one line-ending advisory for the separately owned
`construction-or-strongest-theorem.md`: its LF working-copy content would be
converted to CRLF if Git later touched it.  This memo did not modify that file.
