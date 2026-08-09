<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 15 adversarial defense of the conditional finite gauge--VFE/RG target

## Frozen target and independent steelman

The proposition defended here is the mathematical implication bound by
`problem-contract.json` and atomized in `claim-ledger.json`:

\[
 \forall d\in\mathfrak D_{\mathrm{fin}},
 \qquad
 \mathsf H(d)\Longrightarrow \mathsf C(d).
 \tag{D15.1}
\]

Here \(\mathfrak D_{\mathrm{fin}}\) contains finite standard-Borel agent
networks of every finite cardinality and finite interaction hypergraphs.
There is no uniform cardinality ceiling.  The premise \(\mathsf H(d)\) is not
shorthand for finiteness alone.  It includes the normalized
parameter-independent Markov channel, measurable reverse-kernel versions,
finite positive measure pair, target product-reference equivalence whenever
Hoeffding coordinates are invoked, DQM regularity whenever scores are invoked,
declared equivariant principal and associated-bundle arrows whenever geometry
is invoked, projectability whenever a section is descended, regular strong
configuration geometry whenever a history is invoked, and reference-space
identifications whenever beta functions, ordinary modes, or fixed objects are
compared.

The conclusion \(\mathsf C(d)\) is the typed finite construction: exact
measure-pair and law pushforwards; the bounded nonlinear action and its
derivatives; full finite-subset interaction coordinates and exact residuals;
score projection and Fisher loss; bundle, configuration, and history formulas;
and typed scale composition, cocycles, beta data, and fixed objects.  It also
includes exact statements of where a projected or application-specific tier
requires an additional hypothesis.  Equation (D15.1) does **not** assert that
an arbitrary pair of bundles admits a scale morphism, that every fine section
descends, that every channel preserves a product-equivalent target law, or that
the manuscript's application-specific natural-gradient flows are already
semiconjugate.

The implication is nonvacuous.  Finite product probability models with the
identity channel supply its probability and interaction tiers, and the
fixed-covariance normal-location coefficient construction in
`05d_relational_inference.tex:235-324` supplies a finite-dimensional strong
configuration manifold and locally unique natural-gradient histories.  The
iid normal blocking model in `07b_agent_network_rg.tex:780-1056` supplies the
explicit score/mode realization.  These examples establish satisfiability of
the hypothesis package; they are not substituted for the universal proof.

The frozen evidence used here is:

| Artifact | SHA-256 | Bytes |
|---|---:|---:|
| `problem-contract.json` | `7cba2e9bbfe34028d6a994359e53c761779bd255c5405bfa3996c50ca575bc22` | 11,510 |
| `claim-ledger.json` | `e4aad3402e069f71e0fd63f71d6ef78b9a48fba621e9a54a188dd2d554fed2be` | 119,251 |
| manuscript `SPEC.md` | `ab59a4d02e1c475b6384403013458d39f88f170d592edf802d4c772dd7320571` | 54,048 |
| `construction-or-strongest-theorem.md` | `d340dad09cd24fe912dd2f0d3ffda8f33ef98d62bc2dad1f05c4cf03c08999a2` | 24,133 |
| probability/operator reconstruction | `0b42ce4988d2ad086bb2284e897dae892da925d43eb98620ba7372fa73daada4` | 50,325 |
| geometry reconstruction | `eb6b3ee7697d2089d7d0aabe34be2b9cedeb3525603fb1cab8ed86abbf8f087f` | 40,797 |
| RG reconstruction | `d71eba8eb15760d004f4b78e6f8390da414c8cbe984adf873938f2d30c6093a1` | 46,979 |
| skeptic | `77d02e1b143cda0675b045cd77193d5d3369936361f0e8eda68994486dc02e21` | 35,361 |
| corrected oracle reconstruction | `445a6b27481945bae309982c47751552bee0bb5bb55cfe3dd34d24e26ab0302a` | 55,444 |

Each disposition below is derived from the cited source equations and exact
premise matching.

## Constructive spine of the finite theorem

Let \(K:X\rightsquigarrow Z\) be an admitted channel and let
\(m=e^{-H}\rho\) with \(0<m(X)<\infty\).  Define

\[
 \rho'=\rho K,\qquad m'=mK,\qquad \pi'=\pi K,
 \qquad \pi=\frac{m}{m(X)}.
 \tag{D15.2}
\]

Normalization gives \(m'(Z)=m(X)\), and \(m\ll\rho\) gives
\(mK\ll\rho K\).  If \(\Pi_\rho(z,dy)\) is the reverse conditional of
\(\rho(dy)K(y,dz)\), then testing against bounded measurable functions gives

\[
 \frac{dm'}{d\rho'}(z)
 =\int e^{-H(y)}\Pi_\rho(z,dy)
 \quad \rho'\text{-a.e.}
 \tag{D15.3}
\]

and hence the effective action is the conditional log-Laplace transform.  On
the bounded action chart,

\[
 Q(\varphi)(z)=-\log\int e^{-\varphi(y)}\Pi_\rho(z,dy),
 \quad
 DQ(\varphi)h=\mathbb E_{\Pi_\rho^\varphi}[h\mid z],
 \quad
 D^2Q(\varphi)(h,k)=-\operatorname{Cov}_{\Pi_\rho^\varphi}(h,k\mid z).
 \tag{D15.4}
\]

Kernel associativity proves finite-scale composition.  Constants remain in
the measure-pair tier and are removed only after passing to the explicitly
projective action tier.

For a posterior \(\Pi_o\), recognition law \(Q_o\), and the same structural
channel \(C\) applied to both, standard-Borel disintegration gives

\[
 \operatorname{KL}(Q_o\Vert\Pi_o)
 =\operatorname{KL}(Q_oC\Vert\Pi_oC)
 +\int \operatorname{KL}
   \bigl(Q_o(dy\mid z)\Vert\Pi_o(dy\mid z)\bigr)(Q_oC)(dz).
 \tag{D15.5}
\]

The common channel preserves the observation marginal and its selected
evidence representative, so (D15.5) is exactly the fixed-evidence VFE
comparison.  This is the measure-theoretic core of the law, ELBO, and action
tiers.

On the separately admitted product-reference tier, finite-product conditional
expectations give Boolean Hoeffding projectors

\[
 P_A=\sum_{B\subseteq A}(-1)^{|A|-|B|}C_B,
 \qquad
 P_AP_B=\mathbf 1_{A=B}P_A,
 \qquad
 \sum_{A\subseteq V}P_A=I.
 \tag{D15.6}
\]

After carrying the constant separately, assembly \(E\) and extraction
\(\mathsf H\) are inverse on the full interaction space.  Conjugating the
exact action map yields

\[
 \mathsf T^{\mathcal G}=\mathsf H'\,\overline Q\,E,
 \qquad
 D\mathsf T^{\mathcal G}(g)
 =\mathsf H'\,\overline U^{\varphi_g}E.
 \tag{D15.7}
\]

Thus all generated finite hyperedges remain in the exact state.  A declared
retained projection \(R'\) instead gives the exact split
\(R'\mathsf T^{\mathcal G}g+(I-R')\mathsf T^{\mathcal G}g\); no unreported
closure is inferred.

For a DQM family, the lifted joint experiment has score \(\ell(X)\); applying
the statistic \((X,Z)\mapsto Z\) gives

\[
 \bar\ell(Z)=\mathbb E[\ell(X)\mid Z],
 \qquad
 I_X-I_Z
 =\mathbb E\operatorname{Cov}(\ell(X)\mid Z)\succeq0.
 \tag{D15.8}
\]

The allowed Le Cam singular remainder retains mass \(o(\|h\|^2)\) under a
normalized fixed channel, so it does not invalidate the DQM transfer.  At a
chosen parameter, equality in direction \(v\) means only that
\(v^T\ell(X)\) is \(Z\)-measurable.  It does not establish a reverse kernel for
the entire statistical experiment.

The geometric tier is parallel rather than silently inferred from the
probability tier.  Given the declared smooth equivariant maps, connections,
and related sections, direct vertical/horizontal splitting proves the
covariant-jet, Fisher-defect, anomaly, and cocycle identities.  Given a
separately declared regular configuration manifold and strong metric, standard
ODE theory supplies local histories.  Cross-scale history equivalence then
requires vector-field semiconjugacy, not merely equality of objective values.
Finally, beta differences and fixed-object equations are formed only after
putting consecutive objects in a declared common comparison space.  These
typed restrictions are part of the construction, not omissions from it.

## Response to S15-A1 -- common Markov channel and fixed evidence

**Strongest attack.**  A VFE comparison could be false if the coarse model is
refitted independently, if its evidence changes, if posterior and recognition
laws use different channels, or if equality of two infinite KL values is read
as recoverability.

**Response.**  None of those cases satisfies the attacked premise.  In
`06_general_coarsegraining.tex:258-308`, one normalized recognition-independent
channel is attached to the fixed joint law and to the recognition law.  Its
normalization preserves the observation marginal, so the same finite
\(\log p(o)\) appears on both sides.  Subtracting the two extended VFE
definitions and using (D15.5) gives

\[
 \mathcal F_o(Q_o)-\mathcal F_o^c(Q_oC)
 =\int \operatorname{KL}
   \bigl(Q_o(dy\mid z)\Vert\Pi_o(dy\mid z)\bigr)(Q_oC)(dz)\ge0.
 \tag{D15.9}
\]

On the finite-KL branch, equality holds exactly when the conditional gap is
zero almost surely.  `06_general_coarsegraining.tex:142-165` separately proves
why equality \(+\infty=+\infty\) carries no recovery conclusion, and why
pairwise recovery is weaker than experiment-wide sufficiency.  An example
using different channels or a parameter-dependent channel changes the
mathematical object and is outside H-MARKOV.

**Disposition:** S15-A1 does not refute (D15.1).  It correctly identifies the
common-channel and finite-KL guards, both of which are explicit in the source
and in the frozen construction.

## Response to S15-A2 -- local/global ELBO and observation as interaction

**Strongest attack.**  A local conditional functional need not equal an
additive piece of a collective VFE; subtracting extended infinities is invalid;
and calling observation an interaction could erase the conditioning
sigma-algebra.

**Response.**  The source makes no additive-potential claim.  Let
\(Q=Q_{B^c}r_B\) and \(Q'=Q_{B^c}r'_B\) share the same outside marginal and
have finite posterior KL.  The posterior chain rule in
`05b_local_collective_elbo.tex:325-369` gives

\[
 \operatorname{KL}(Q\Vert\Pi_o)
 =\operatorname{KL}(Q_{B^c}\Vert\Pi_{o,B^c})
 +\mathbb E_{Q_{B^c}}
   \operatorname{KL}\bigl(r_B(\cdot\mid Y_{B^c})
                      \Vert\Pi_{o,B}(\cdot\mid Y_{B^c})\bigr).
 \tag{D15.10}
\]

Applying (D15.10) to both laws cancels the common outside term and yields the
displayed local/global potential difference with the random outside state
\(Y_{B^c}\).  The finite-KL assumptions make both conditional fields
integrable before subtraction.  Overlapping local conditionals and total
correlation stay in the one joint law; independently summing local potentials
is expressly disallowed.

For the observation claim, standard-Borel kernel randomization realizes
\(o=F(x,U)\) with \(U\sim\mathrm{Unif}[0,1]\) as an environment-node message.
Marginalizing the node recovers the original observation kernel.  This
preserves the observation law and \(\sigma(O)\); it neither removes
conditioning nor converts an unobserved prior into a posterior.

**Disposition:** S15-A2 does not refute (D15.1).  The repaired construction's
outside argument is correctly bound as \(Y_{B^c}\), and its observation claim
is operational, not ontological.

## Response to S15-A3 -- target product-reference equivalence

**Strongest attack.**  A normalized channel can destroy equivalence to every
target product reference.  For example, clone a nondegenerate Bernoulli
variable into \((X,X)\).  The pushed law lives on the diagonal, whereas any
product law supporting both diagonal atoms also assigns positive mass off the
diagonal.

**Response.**  The witness is correct and sharp, but it attacks an omitted
hypothesis rather than the conditional interaction theorem.  Law pushforward
and the measure-pair construction require only the normalized channel.  The
Hoeffding tier is invoked separately under H-INTERACTION, which requires a
declared target product probability \(\nu_{\ell+1}\) with
\(\pi_\ell K_\ell\sim\nu_{\ell+1}\).  The cloned Bernoulli arrow therefore
remains admitted at the law tier and is not admitted at the target Hoeffding
tier.  The source states this distinction in
`07b_agent_network_rg.tex:1125-1188` and the frozen theorem repeats it before
(D15.6).

This boundary is substantive: the theorem does not prove that arbitrary
coarse channels preserve product-factor equivalence.  But (D15.1) quantifies
over the interaction conclusions only when that declared equivalence holds.

**Disposition:** S15-A3 establishes an explicit scope boundary, not a
counterexample to an admitted target conjunct.

## Response to S15-A4 -- full hyperedge closure versus finite-parameter closure

**Strongest attack.**  A finite vertex set does not make an interaction sector
finite dimensional, and the extraction norm
\(3^{|V|}-1\) is not uniform in network size.  Thus "finite" could conceal a
finite-parameter or dimension-free closure claim.

**Response.**  The exact theorem makes neither strengthening.  Finiteness of
\(V\) makes the index lattice \(2^V\) finite; each nonempty sector can still be
an infinite-dimensional function space.  Finite-product Fubini and Boolean
inversion prove the inverse identities in (D15.6), while
`07b_agent_network_rg.tex:1189-1251` derives

\[
 \|E\|\le1,
 \qquad
 \|\mathsf H\|\le\sum_{\varnothing\ne A\subseteq V}2^{|A|}
 =3^{|V|}-1.
 \tag{D15.11}
\]

The constant depends explicitly on \(|V|\).  Since every generated nonempty
subset sector is retained, the full finite theory closes exactly, even when
hidden variables create higher hyperedges.  A sparse, pairwise, memoryless, or
finite-parameter retained theory is exact only if its invariant-image
criterion is proved; otherwise the source carries the quotient residual.

**Disposition:** S15-A4 does not refute (D15.1).  It rules out claims the
frozen target already excludes.

## Response to S15-A5 -- marked attention-event law and latent labels

**Strongest attack.**  Pointwise normalized nonnegative weights need not be
measurable.  On a standard-Borel state space, choose a nonmeasurable set
\(A\) and set two event weights to \(\mathbf 1_A\) and
\(1-\mathbf 1_A\).  They sum to one pointwise but do not define a probability
kernel, so the conditional expectation in the local meta-attention display is
undefined.

**Concession.**  This exposes a real local shorthand defect in
`07b_agent_network_rg.tex:1748-1776`: that paragraph calls \(\eta\) a joint
marked event law but does not repeat the word "measurable" when introducing
\(\alpha\) and \(\beta\).  Read in isolation as assumptions on arbitrary
pointwise arrays, its displayed conditions are insufficient.  The line should
say that \(\eta_{ij}=\alpha_i\beta_{ij}\) is a jointly measurable normalized
marked-event kernel (or impose measurability on the factors).

The defect does not reach the frozen conditional target.  The complete theorem
at `07b_agent_network_rg.tex:2735-2756` assumes supplied "joint marked
attention-event laws" and globally jointly measurable disintegrations.  The
contract independently requires a measurable version for every conditional
expectation.  Consequently the nonmeasurable array is not an admitted
\(d\in\mathfrak D_{\mathrm{fin}}\).  On admitted data, define the joint event
law \(\eta_{ij}=\alpha_i\beta_{ij}\), push it by conditional expectation,
and only then disintegrate:

\[
 \eta^c_{IJ}(z)
 =\mathbb E\!\left[\sum_{i\in I,j\in J}\eta_{ij}(Y)\mid Z=z\right],
 \quad
 \alpha_I^c=\sum_J\eta^c_{IJ},
 \quad
 \beta^c_{IJ}=\eta^c_{IJ}/\alpha_I^c
 \tag{D15.12}
\]

on occupied rows.  Conditional expectation preserves total mass, and the
tower property proves nested associativity.  Coarsening \(\beta\) alone would
discard receiver occupancy and is not claimed.

The latent-label ELBO is also separately typed.  Under finite categorical
labels, positive priors, finite measurable energies, label exclusivity, and
the declared factorization, the categorical KL and conditional-kernel KL are
the two terms of one conditional chain rule
(`07b_agent_network_rg.tex:1885-1907`).  Any total-correlation correction is
retained when a factorized recognition family is imposed.

**Disposition:** S15-A5 is **partially sustained as a minor source-level
measurable-array shorthand defect** and is conceded.  It does not falsify
(D15.1), because measurability and an actual joint event law are explicit
premises of the complete target.  The frozen construction at lines 334-350 now
states the measurable-law requirement directly.

## Response to S15-A6 -- DQM and Fisher contraction

**Strongest attack.**  DQM need not use one fixed dominating measure; a
singular remainder may appear; and a parameter-dependent channel can create
information.  A density-chart proof could therefore miss admitted paths.

**Response.**  The proof in `06_general_coarsegraining.tex:170-224` uses the
Le Cam decomposition

\[
 P_{\theta_0+h}=p_hP_{\theta_0}+P_h^\perp,
 \quad P_h^\perp\perp P_{\theta_0},
 \quad P_h^\perp(X)=o(\|h\|^2),
 \tag{D15.13}
\]

not a globally dominated density chart.  Lifting through a normalized fixed
\(K\) preserves the singular mass exactly, and the lifted family remains DQM.
Projection to \(Z\) gives (D15.8); total covariance gives its
positive-semidefinite defect.  A family \(K_\theta\) falls outside the fixed
experiment channel premise.  A witness with singular mass only
\(O(\|h\|^2)\), rather than \(o(\|h\|^2)\), falls outside DQM.

The equality statement must remain local.  At one parameter,
\(I_X(v,v)=I_Z(v,v)\) if and only if the directional score
\(v^T\ell_{\theta_0}(X)\) is \(Z\)-measurable.  For a section-generated tangent,
the same criterion applies to that section-generated score.  It does **not**
mean that the full experiment is globally sufficient or recoverable.  The
Bernoulli witness in `06_general_coarsegraining.tex:243-253` has equal Fisher
information at \(\theta=0\) after discarding \(B\), yet no one
parameter-independent reverse kernel recovers the experiment away from that
point.  This is the necessary narrowing of the corresponding oracle G3
phrase, and the current construction states it correctly at lines 220-222.

**Disposition:** S15-A6 does not refute (D15.1).  The theorem covers general
Le Cam DQM under the fixed-channel premise and makes only local score-
measurability equality claims.

## Response to S15-A7 -- bundle maps, sections, and configuration existence

**Strongest attack.**  A probability channel does not automatically produce a
principal-bundle scale map, a bundle morphism need not send every fine section
to a coarse section, and marginal sections do not determine a joint
recognition law or a configuration-space Fisher metric.

**Response.**  All three statements are true and are built into the premise
typing.  `07_general_renormalization.tex:248-302` proves that an equivariant
principal map over \(c_\ell\) exists exactly when the extended fine bundle is
isomorphic to \(c_\ell^*P_{\ell+1}\).  The Hopf-versus-trivial example shows
that this condition can fail.  The theorem therefore consumes a declared
compatible principal scale map; it does not manufacture one.

Likewise, for a surjective submersion \(f\), section descent requires
\(\Psi\circ Q\) to be constant on fibers.  The differential condition is

\[
 T^V\Psi(D^\omega Q(X))+A_\Psi(Q;X)=0
 \quad\text{for every }X\in\ker Tf,
 \tag{D15.14}
\]

with connected fibers for the converse.  The collapse
\(S^1\to\{*\}\), \(Q(x)=\mathcal N(\sin x,1)\), violates (D15.14), so no
coarse section exists (`05c_pullback_geometry.tex:715-790`).  This witness
refutes automatic descent and confirms why H-CONFIG is conditional.

Finally, the source states that a general joint history needs a declared or
proved recognition-law lift and joint Fisher pullback.  It separately exhibits
a nonempty finite normal-location coefficient tier with a strong constant Gram
metric.  Thus the theorem constructs an explicit satisfiable configuration
tier while leaving the manuscript-specific map and joint lift as application
obligations.

**Disposition:** S15-A7 does not refute (D15.1).  It verifies that the
geometric and configuration declarations are load-bearing; no automatic
existence claim survives in the frozen theorem.

## Response to S15-A8 -- anomaly and cocycle algebra

**Strongest attack.**  Horizontal defects at consecutive arrows inhabit
different vertical bundles, so an untransported sum is ill typed.  Even after
transport, nonzero stage defects can cancel.  Pulling the vertical Fisher
defect cocycle to the base also creates an anomaly residual, whose quadratic
sign is easy to reverse.

**Response.**  With the stated convention, direct splitting of a composite
arrow gives

\[
 A_{12\circ01}
 =T^V\Psi_{12}\,A_{01}+A_{12}\circ Tf_{01}.
 \tag{D15.15}
\]

The transport in the first term is essential.  Equation (D15.15) permits
cancellation and nowhere infers that vanishing composite anomaly forces both
stage anomalies to vanish.

The unconditional vertical Fisher-defect identity is contravariant:

\[
 \Delta_F^{12\circ01}
 =\Delta_F^{01}+(T^V\Psi_{01})^*\Delta_F^{12}.
 \tag{D15.16}
\]

For related sections, write \(v=T^V\Psi_{01}D^{\omega_0}s_0\) and
\(\bar u=v+A\).  The exact base residual in
`05c_pullback_geometry.tex:1267-1314` is

\[
 \mathcal N(X,Y)
 =\Delta_{12}(v_X,v_Y)-\Delta_{12}(\bar u_X,\bar u_Y)
 =-\Delta_{12}(v_X,A_Y)-\Delta_{12}(A_X,v_Y)
  -\Delta_{12}(A_X,A_Y).
 \tag{D15.17}
\]

On the diagonal this is
\(-2\Delta_{12}(v,A)-\Delta_{12}(A,A)\).  Hence the sharp additive base
cocycle holds exactly when
\(\Delta_{12}(v,v)=\Delta_{12}(v+A,v+A)\), equivalently
\(\Delta_{12}(A,2v+A)=0\).  Zero first-stage anomaly is sufficient but not
necessary; the source supplies a finite cancellation witness.

**Disposition:** S15-A8 does not refute (D15.1).  The source uses transported
typed composition, retains cancellation, and prints the correct convention-
dependent quadratic sign.

## Response to S15-A9 -- natural-gradient semiconjugacy

**Strongest attack.**  Equality or pullback compatibility of objectives is
metric free, whereas a natural gradient depends on the metric.  Therefore
objective equality alone cannot make independently optimized fine and coarse
flows trace the same oriented orbit.

**Response.**  The theorem explicitly agrees.  Let

\[
 \mathcal F_\ell
 =\chi_\ell\circ\mathcal F_{\ell+1}\circ\mathsf R_\ell,
 \qquad \chi_\ell'>0,
 \tag{D15.18}
\]

on an open set containing the orbit.  If \(\mathsf R_\ell\) is a surjective
submersion with the declared closed horizontal splitting and is horizontally
conformal with dilation \(\varphi_\ell>0\), the gradient calculation in
`05d_relational_inference.tex:1454-1494` yields

\[
 T\mathsf R_\ell X_\ell
 =a_\ell X_{\ell+1}\circ\mathsf R_\ell,
 \qquad
 a_\ell=\chi_\ell'\varphi_\ell^2>0.
 \tag{D15.19}
\]

This is sufficient for oriented semiconjugacy.  The source does not call it
necessary or automatic.  At the manuscript's own configuration tier, the
required integrated conformality identity, interior attainment, and
functional compatibility remain OPEN application checks
(`05d_relational_inference.tex:1514-1553`).  The unequal-metric identity-map
witness therefore attacks objective equality alone, which the theorem already
rejects.

**Disposition:** S15-A9 does not refute (D15.1).  It reinforces the metric and
functional hypotheses and leaves the application-specific semiconjugacy open.

## Response to S15-A10 -- beta data, fixed objects, and finite scope

**Strongest attack.**  A beta difference across changing spaces is ill typed;
a projected fixed point need not be an exact fixed point; fixedness in one tier
need not transfer to another; and a construction valid for every finite
cardinality does not establish an infinite-volume RG or universality class.

**Response.**  The exact interaction beta is formed only after bounded
isomorphisms \(J_\ell:\mathcal G_*\to\mathcal G_\ell\):

\[
 \widehat T_\ell^{\mathcal G}
 =J_{\ell+1}^{-1}T_\ell^{\mathcal G}J_\ell,
 \qquad
 \beta_\ell^{\mathrm{ex}}(g)
 =\frac{\widehat T_\ell^{\mathcal G}(g)-g}{\log b_\ell}.
 \tag{D15.20}
\]

For a retained projection, the exact omitted beta is

\[
 \delta\beta_\ell(g)
 =\frac{J_{\ell+1}^{-1}
   (I-R_{\ell+1})T_\ell^{\mathcal G}(J_\ell g)}{\log b_\ell}.
 \tag{D15.21}
\]

It vanishes on the retained sector exactly when that sector is invariant under
the exact image (`07b_agent_network_rg.tex:2236-2316`).  The action beta also
depends on its reference-measure trajectory; no reference-free subtraction is
claimed.

For nonautonomous maps \(F_\ell:Y_\ell\to Y_{\ell+1}\), the primitive invariant
object is a section \(y_{\ell+1}=F_\ell(y_\ell)\).  After identifications
\(J_\ell:Y_*\to Y_\ell\), a reference fixed object satisfies every transported
one-step equation.  Autonomy reduces this to one repeated map; a periodic
sequence can instead use its monodromy and cycles
(`07b_agent_network_rg.tex:2582-2630`).  Law, action, interaction, attention,
bundle, and configuration fixedness remain separate unless a commuting bridge
is supplied.

Finally, \(\forall n<\infty\) is not an assertion at \(n=\infty\).  The source
explicitly excludes countably infinite networks, thermodynamic or
infinite-volume existence, quasilocality, blocking-independent universality,
and universal exponents.  Its finite-depth Abelian example is accompanied by
the warning that fixed-depth and maximal-depth limits can differ.

**Disposition:** S15-A10 does not refute (D15.1).  Every subtraction and fixed
equation is typed, projected residuals are retained, and no infinite-volume or
universality conclusion is drawn.

## Re-audit of the frozen construction

I re-read the current `construction-or-strongest-theorem.md` at SHA-256
`d340dad09cd24fe912dd2f0d3ffda8f33ef98d62bc2dad1f05c4cf03c08999a2`.
The previously exposed defects are repaired in these bytes:

1. Lines 89-94 restrict the KL equality characterization to the finite-KL
   branch and deny a recovery inference from two infinite extended values.
2. Lines 99-132 supply the measurable local baseline, incident likelihood,
   positive conditional normalizer, posterior conditional, and the random
   outside state \(Y_{B^c}\) used in the local/global identity.
3. Lines 208-215 type the quotient action map, while lines 261-294 use
   \(\mathsf H_\ell\) for Hoeffding extraction, select an action representative
   for each interaction coordinate, and distinguish tilted from untilted
   derivatives.
4. Lines 355-371 require a normalized measurable joint marked-event law before
   conditional expectation.
5. Lines 239-241 restrict Fisher equality to local directional-score
   measurability and expressly deny global experiment sufficiency.
6. Lines 332-344 state the block-weight normalization required for
   \(C_xP_x=I\), and lines 490-518 type every measure, weight, tangent, and
   variance term in the quadratic configuration defect.
7. Lines 631-637 correctly type a general nonautonomous invariant section,
   common-space reference fixed objects, the autonomous reduction, and periodic
   monodromy cycles.
8. Lines 641-704 bind the Hermite result to integer \(b\ge2\) and
   \(L^2_0(\gamma)\), and state the regular-variation and heat-trace hypotheses
   consumed by the forward Abelian implication.

I found no remaining load-bearing overstatement in the frozen construction.
The phrase "complete" at lines 706-739 is explicitly limited to admitted
finite networks and finite composable scale sequences, followed immediately by
the list of automatic-existence, sparse-closure, semiconjugacy, continuous-
beta, universality, and infinite-limit nonclaims.  It therefore cannot be read
as a theorem of universality or infinite volume.

The one surviving exact defect is the conceded measurable-array shorthand in
the local source paragraph `07b_agent_network_rg.tex:1748-1776`; the complete
source theorem, frozen contract, and construction all contain the stronger
measurable-law premise needed for the target implication.

## Falsification conditions

The defended state would be falsified by any one of the following, provided
the witness satisfies every premise consumed by the attacked conclusion:

1. A finite admitted measure pair and normalized common channel for which
   (D15.2), evidence preservation, or finite kernel composition fails.
2. A finite-KL posterior/recognition pair under one common channel for which
   (D15.5) or its zero-conditional-gap equality condition fails.
3. Two finite-KL joint recognition laws with the same outside marginal for
   which (D15.10) does not yield the stated local/global VFE difference.
4. An admitted product-equivalent finite scale for which the Boolean
   interaction projectors fail to invert assembly, or an exact generated
   finite-subset interaction that is discarded without a recorded residual.
5. A normalized **measurable** marked-event law and admissible nested blocking
   for which (D15.12) loses normalization or violates the tower identity.
6. A DQM path and normalized parameter-independent channel for which the
   coarse score is not conditional expectation or the Fisher defect is not
   positive semidefinite.
7. Declared compatible bundle/configuration data satisfying equivariance,
   projectability, smoothness, and the stated closure hypotheses for which the
   associated map, descended section, or displayed defect formula fails.
8. A typed composable pair for which (D15.15), (D15.16), or the exact residual
   (D15.17) fails.
9. Data satisfying (D15.18), horizontal conformality, and the submersion
   hypotheses for which (D15.19) fails.
10. Declared reference identifications and retained projections for which
    (D15.20), (D15.21), or the invariant-image criterion fails.

A nonmeasurable array, a parameter-dependent or mismatched channel, a target
law lacking the required product-reference equivalence, a nonexistent
principal map, a nonprojectable section, objective equality without metric
compatibility, an untransported cocycle sum, or an infinite-volume demand does
not satisfy the relevant premise and therefore cannot falsify (D15.1).  Such
examples remain useful boundary witnesses and must not be promoted into
admitted counterexamples.

## Final state

**Frozen conditional finite mathematical target: `EVIDENCE_VERIFIED`.**

The construction is exact for every admitted finite network and every finite
composable scale sequence under the conjunct-specific hypotheses recorded in
the contract and ledger.  S15-A1 through S15-A4 and S15-A6 through S15-A10 do
not supply an admitted counterexample.  S15-A5 identifies one real minor
source-level measurable-array shorthand defect, which is conceded but does not
reach the complete theorem because the target premise requires a measurable
joint event law.

This state is deliberately limited to the mathematical implication (D15.1).
It assigns no state to universality, infinite volume, automatic
application-specific maps, or the package's separate operational release
obligations.  The byte digest of this memo is recorded externally after the
final write so that the file is not asked to contain its own hash.
