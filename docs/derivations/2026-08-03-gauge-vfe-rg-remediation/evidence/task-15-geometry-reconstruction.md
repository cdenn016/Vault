<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->

# Task 15 independent geometry and history reconstruction

## Frozen scope and verdict

This memo is an independent reconstruction of the information-geometric,
differential-geometric, pullback, configuration, and inference-history sector of
the frozen target at Git commit
`14551bb8d463f229a3b451d7222042d134c2c52d`.  I used the frozen
`problem-contract.json` and the source definitions and hypotheses listed below.
I did **not** read `construction-or-strongest-theorem.md`, the bound claim
ledger, the dependency DAG, or any other Task 15 memo. All conclusions were
derived from the frozen definitions and source hypotheses. A wiki source note
was consulted only to locate the current
manuscript files; none of its conclusions was accepted as mathematical
evidence.

**Sector verdict: CONDITIONAL PASS.**  The exact bundle, covariant-jet,
pullback, projectability, horizontal-anomaly, Fisher-defect, cocycle,
configuration-tier, curve, duration, and conditional semiconjugacy statements
reconstruct from the stated hypotheses.  They are `EVIDENCE_VERIFIED` as
conditional mathematical claims by the derivations below.  No automatic
existence theorem follows for a principal scale morphism, an exact
recognition-law lift, a generic configuration coarse map, a related coarse
section, or an oriented semiconjugacy for the manuscript's application-specific
RG maps.  Those are declared inputs or open application obligations.  The
stronger reading that the bundle data alone automatically provide them is
`REFUTED` by explicit counterexamples.  The frozen target is not refuted by
this boundary because its geometry/history quantifiers explicitly range over
compatible scale morphisms, regular configuration manifolds, and selected
histories meeting their local assumptions.  Thus the verified result is a
conditional typed theory, not an unconditional realization theorem.

The no-physical-time boundary is exact: Fisher duration is an oriented,
metric-relative arc length on a selected regular history.  The source neither
constructs nor claims an operational physical clock, a global synchronized
clock, Lorentzian structure, or an identification of RG depth with time.

### Frozen source identities

| Source | SHA-256 |
|---|---|
| `manuscripts/gauge_vfe_rg/02_geometry.tex` | `8A39F1C6D2E0AC92ACC159C47739B13CD7D190054563BCCFE77E447EDC5D9D95` |
| `manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex` | `A035CF5F69E9179F56B2D94CB697989D15E2BB4B0B13E412BC98354342BB9196` |
| `manuscripts/gauge_vfe_rg/05d_relational_inference.tex` | `7B1D486962235465D69A105B51E6608148C4D8B4FA942ADB2D4384A0CA868715` |
| `manuscripts/gauge_vfe_rg/06_general_coarsegraining.tex` | `4891A8F5FA86AC0FA5266381E2C67161125645034CA40395CB2E3ED1B67DC9B2` |
| `manuscripts/gauge_vfe_rg/07_general_renormalization.tex` | `CEDA98A49F4122DE39D70F784288860AB727ABFA217A92B1230591E6CE76BCAD` |

## Claim-level adjudication

| ID | Atomic claim | State | Exact scope |
|---|---|---|---|
| G15-1 | The declared principal bundle and represented law fibers produce typed associated bundles; an equivariant fiber map produces a well-defined associated-bundle morphism. | `EVIDENCE_VERIFIED` | Conditional on the declared bundle, invariant fiber, and intertwining law. |
| G15-2 | An arbitrary principal scale morphism exists from the bundle data alone. | `REFUTED` | The extension-bundle isomorphism is necessary and sufficient; Hopf versus trivial bundles give a counterexample. |
| G15-3 | The covariant vertical jet pulls the fiber Fisher tensor back to a passive-gauge-invariant, connection-relative semimetric. | `EVIDENCE_VERIFIED` | Regular DQM fiber, positive Fisher form, bimeasurable parameter-independent sample action, smooth section, chosen connection. |
| G15-4 | Constant rank alone makes the semimetric a metric on a quotient manifold. | `REFUTED` | Constant rank gives a vector-bundle quotient only; a contact-distribution example defeats involutivity. |
| G15-5 | A fine section descends through a coarse base map exactly under fiber projectability, with the differential criterion when fibers are connected. | `EVIDENCE_VERIFIED` | Surjective smooth submersion; smooth bundle morphism; connected fibers for the differential converse. |
| G15-6 | A pointwise bundle morphism automatically induces a configuration-space map. | `REFUTED` | Total collapse of (S^1) with (Q(x)=\mathcal N(\sin x,1)) is nonprojectable. |
| G15-7 | Covariant first jets satisfy the chain rule with one exact horizontal anomaly, and anomalies compose in the stated ordered form. | `EVIDENCE_VERIFIED` | Smooth bundle morphisms and chosen source/target connections. |
| G15-8 | Parameter-independent Markov pushforward contracts the vertical Fisher metric; the base pullback contracts when the horizontal anomaly vanishes. | `EVIDENCE_VERIFIED` | DQM transfer, family closure, smooth induced map, normalization, and related sections. |
| G15-9 | Base contraction survives an arbitrary nonzero horizontal anomaly. | `REFUTED` | The exact signed formula has cross and quadratic anomaly terms; an identity-channel example gives a strictly negative fine-minus-coarse tensor. |
| G15-10 | Vertical Fisher defects form an unconditional pullback cocycle; base defects have the stated exact residual and sharp equality condition. | `EVIDENCE_VERIFIED` | Whenever the typed vertical defects and related sections are defined. Positivity additionally needs Markov arrows. |
| G15-11 | A nonempty regular configuration manifold with a strong Fisher metric and locally unique gradient flow is explicitly constructed. | `EVIDENCE_VERIFIED` | The finite normal-location coefficient tier with (L^2)-independent basis fields. |
| G15-12 | Marginal belief/model sections canonically determine an exact joint Fisher metric and exact VFE lift. | `REFUTED` | Distinct right inverses of the same extraction map can induce different pullback metrics; the lift remains declared data. |
| G15-13 | Vertical, horizontal, mixed, base-probe, and configuration-history curves are correctly typed; Fisher length is invariant under positive reparameterization. | `EVIDENCE_VERIFIED` | Regular curves on the declared statistical/configuration tiers. |
| G15-14 | Same-path Markov images have no greater Fisher duration, with equality exactly at score sufficiency. | `EVIDENCE_VERIFIED` | Same fine path and one normalized parameter-independent kernel; not independently recomputed flows. |
| G15-15 | Functional compatibility plus horizontal conformality implies oriented natural-gradient semiconjugacy with the stated factor. | `EVIDENCE_VERIFIED` | Strong metrics, (C^2) objectives, surjective submersion, closed horizontal splitting. |
| G15-16 | The manuscript's specific RG maps are already proved to semiconjugate their independently recomputed natural-gradient flows. | `INCONCLUSIVE` | Functional compatibility on an orbit neighborhood and horizontal conformality are explicitly still open. |
| G15-17 | Fisher duration, an orbit parameter, RG depth, and physical time are canonically identical. | `REFUTED` | They have different types and independent choices; no operational bridge is supplied. |

## 1. Principal and associated bundle morphisms

The primitive geometric inputs are a finite-dimensional smooth contextual base
\(\mathcal C\), one principal right \(G\)-bundle
\(\pi:P\to\mathcal C\), invariant statistical fibers \(\mathcal B_b\) and
\(\mathcal B_m\), and represented left actions \(\widehat\rho_b\) and
\(\widehat\rho_m\).  They are declarations, not derived objects
(`02_geometry.tex:16`, `def:geo-context-base`; `02_geometry.tex:40`,
`def:geo-principal-systems`; `02_geometry.tex:103`, `hyp:geo-smooth-tier`).
The associated bundles are then actual quotient constructions

\[
 \mathcal E_x=P\times_{\widehat\rho_x}\mathcal B_x,
 \qquad (p g,\beta)\sim(p,\widehat\rho_x(g)\beta),
 \qquad x\in\{b,m\},
\]

at `02_geometry.tex:120-137` (`def:geo-associated-bundles`,
`eq:geo-associated-bundles`, `eq:geo-quotient-convention`).

For a candidate fiber map \(\phi:\mathcal B_b\to\mathcal B_m\), define
\(\Phi[p,\beta]=[p,\phi(\beta)]\).  Replacing \((p,\beta)\) by the equivalent
representative \((p g,\widehat\rho_b(g)^{-1}\beta)\) changes the proposed image
to

\[
 [p g,\phi(\widehat\rho_b(g)^{-1}\beta)]
 =[p,\widehat\rho_m(g)\phi(\widehat\rho_b(g)^{-1}\beta)].
\]

This equals \([p,\phi(\beta)]\) for all representatives exactly when
\(\phi\widehat\rho_b(g)=\widehat\rho_m(g)\phi\).  Thus the source's
intertwining construction is both typed and representative independent
(`02_geometry.tex:222-243`, `prop:geo-intertwining-cross-map`).  What is not
constructed is the intertwiner \(\phi\) itself; a common principal bundle and
relative frame cannot map inequivalent law fibers
(`02_geometry.tex:139-146`, `02_geometry.tex:245-276`).

Across scales, a \(\kappa:G_0\to G_1\)-equivariant principal map
\(\mathcal P:P_0\to P_1\) over \(f:C_0\to C_1\) exists exactly when the
extension of structure group \(P_0\times_\kappa G_1\) is isomorphic to
\(f^*P_1\).  Given \(\mathcal P\) and an intertwining fiber map \(q\),

\[
 C[p,z]=[\mathcal P(p),q(z)]
\]

is an actual associated-bundle construction
(`07_general_renormalization.tex:248-303`,
`eq:rg-principal-scale-map`, `eq:rg-scale-intertwiner`,
`eq:rg-associated-scale-map`).  The topological criterion is load bearing.  A
Hopf \(U(1)\)-bundle over \(S^2\) cannot map equivariantly over the identity to
the trivial \(U(1)\)-bundle with \(\kappa=\mathrm{id}\), because the required
principal bundles are not isomorphic (`07_general_renormalization.tex:257-266`).
This is a minimal counterexample to automatic scale-morphism existence.

## 2. Fisher pullbacks and connection-relative covariant jets

The statistical hypotheses are finite-dimensional smooth DQM families,
positive-definite Fisher forms, the required score integrability and
domination, and represented actions induced by parameter-independent
bimeasurable sample-coordinate changes
(`05c_pullback_geometry.tex:30-42`, `hyp:pb-regular-models`).  For such an
action, the score transforms by composition with the inverse sample map.  The
pushforward integration formula therefore gives

\[
 \mathbb E_{g_\#p}
 [ (\ell_u\circ r_g^{-1})(\ell_v\circ r_g^{-1})]
 =\mathbb E_p[\ell_u\ell_v],
\]

and similarly for the third score moment.  This directly proves descent of the
Fisher and Amari tensors to vertical tensors on \(\mathcal E_x\)
(`05c_pullback_geometry.tex:59-87`,
`prop:pb-statistical-tensor-descent`).

A chosen connection supplies the vertical projection and the covariant first
jet

\[
 D^\omega s=\operatorname{ver}^\omega\circ Ts,
 \qquad
 h_s^\omega(X,Y)=g^F(D^\omega sX,D^\omega sY).
\]

These are definitions at `05c_pullback_geometry.tex:89-122`
(`eq:pb-covariant-first-jet`, `def:pb-informational-pullbacks`).  Under a
passive frame change \(g(c)\), both the connection coordinates and section
coordinates change, and

\[
 D^{\omega'}s'X=T\widehat\rho(g^{-1})D^\omega sX.
\]

Fisher invariance then cancels the tangent representation in both arguments,
so the base tensor is passive-gauge invariant
(`05c_pullback_geometry.tex:124-154`,
`thm:pb-pullback-gauge-invariance`).  This is covariance of one geometric pair
\((\omega,s)\), not independence of the connection and not invariance under an
active transformation with the connection held fixed.

If \(\omega'=\omega+a\), with fundamental vertical correction
\(R_a^s(X)=\vartheta_{s(c)}(a(X))\), direct subtraction of the two horizontal
lifts gives

\[
 D^{\omega'}s=D^\omega s+R_a^s,
\]

and bilinearity gives the exact connection-change identity

\[
 h_s^{\omega'}(X,Y)=h_s^\omega(X,Y)
 +g^F(R_aX,D^\omega sY)+g^F(D^\omega sX,R_aY)+g^F(R_aX,R_aY).
\]

This reconstructs `05c_pullback_geometry.tex:156-218`
(`prop:pb-pullback-connection-change`).  A minimal falsifier for
connection independence is the constant section of the unit-variance normal
location family over \(\mathbb R\): the zero connection gives \(h=0\), while
\(A'=a_0,dx\) gives \(h=a_0^2dx^2\)
(`05c_pullback_geometry.tex:220-230`,
`eq:pb-connection-dependence-example`).

Positive definiteness of the fiber Fisher metric gives the exact equality
conditions

\[
 \operatorname{rad}h_s^\omega=\ker D^\omega s,
 \qquad
 \operatorname{rank}h_s^\omega=\operatorname{rank}D^\omega s.
\]

Constant rank constructs a smooth vector-bundle quotient with a positive
metric, but not a quotient manifold
(`05c_pullback_geometry.tex:321-370`,
`thm:pb-pullback-rank-quotient`).  A quotient manifold additionally requires
an involutive radical, a regular Hausdorff leaf space with a surjective
submersion quotient, and basicness of the tensor
(`05c_pullback_geometry.tex:372-427`).  The constant-section normal family on
\(\mathbb R^3\) with connection form
\(\alpha=dz-x,dy\) has \(h=\alpha^2\), constant rank one, but
\(\alpha\wedge d\alpha\ne0\); its radical is a contact distribution
(`05c_pullback_geometry.tex:429-454`,
`prop:pb-contact-null-counterexample`).  Thus the quotient-manifold
strengthening is refuted, not merely unsupported.

## 3. Projectability, coarse sections, and the horizontal anomaly

Let \(f:C\to\bar C\) be a surjective smooth submersion and
\(\Psi:E\to\bar E\) a smooth bundle morphism over \(f\).  A coarse section is
not produced merely by writing \(\Psi\circ s\): that composite is initially a
section along \(f\).  Existence of \(\bar s\) requires

\[
 \Psi\circ s=\bar s\circ f.
\]

The horizontal anomaly is the vertical vector

\[
 A_\Psi(e;X)=T_e\Psi(H_e^\omega X)
 -H_{\Psi(e)}^{\bar\omega}(T_cfX).
\]

Both definitions and types are at `05c_pullback_geometry.tex:670-713`
(`eq:pb-coarse-related-sections`, `eq:pb-coarse-horizontal-defect`).

For a section \(Q\), differentiate \(\Psi Q\) along
\(X\in\ker T_cf\).  Splitting \(TQX=H^\omega X+D^\omega QX\) gives

\[
 T(\Psi Q)X
 =T^V\Psi(D^\omega QX)+A_\Psi(Q;X).
\]

Therefore fiber constancy implies the vanishing of this expression.  If the
fibers of \(f\) are connected, vanishing makes \(\Psi Q\) constant on each
fiber, and the quotient property of a surjective submersion constructs a
unique smooth \(\bar Q\).  This proves the sharp descent theorem
(`05c_pullback_geometry.tex:715-751`, `thm:pb-section-descent`,
`eq:pb-projectability-criterion`).  The hypotheses are sharp enough to expose
two failures:

1. If \(f(x)=x^3\), the unique factor of \(Q(x)=\mathcal N(x,1)\) is
   \(\bar Q(y)=\mathcal N(y^{1/3},1)\), which is not smooth at zero; the
   submersion hypothesis cannot be dropped.
2. For total collapse \(S^1\to\{*\}\), identity fiber map, and
   \(Q(x)=\mathcal N(\sin x,1)\), the derivative
   \(\cos x\,\partial_\mu\) does not vanish identically, so no coarse section
   exists (`05c_pullback_geometry.tex:779-790`,
   `prop:pb-nonfunctorial-descent`).

Differentiating the related-section equation without setting the anomaly to
zero gives the exact covariant chain rule

\[
 D^{\bar\omega}\bar s(TfX)
 =T^V\Psi(D^\omega sX)+A_\Psi(s;X).
\]

This is `05c_pullback_geometry.tex:792-819`
(`thm:pb-covariant-jet-naturality`).  For a morphism induced by a principal
scale map \(\mathcal P\), the anomaly is the fundamental field of

\[
 \mathfrak A_{\mathcal P}=\mathcal P^*\bar\omega-d\kappa\circ\omega.
\]

It vanishes along the section exactly when
\(\mathfrak A_{\mathcal P}(X)\) lies in the isotropy algebra of the coarse
section value.  Principal connection preservation
\(\mathfrak A_{\mathcal P}=0\) is sufficient but is necessary only for an
infinitesimally effective action
(`05c_pullback_geometry.tex:909-977`, `thm:pb-isotropy-criterion`).

For composable arrows, expanding the first horizontal lift and then the second
gives

\[
 A_{12\circ01}(e;X)
 =T^V\Psi_{12}\,A_{01}(e;X)
 +A_{12}(\Psi_{01}e;Tf_{01}X).
\]

The earlier vertical defect must be pushed by the later vertical differential,
and the later defect must be evaluated on the pushed base tangent.  This proves
the ordered composition law at `05c_pullback_geometry.tex:979-1032`
(`thm:pb-anomaly-composition`).  Composite vanishing is exactly cancellation
of these two typed terms; factorwise vanishing is sufficient but not necessary.

## 4. Fisher contraction, signed base comparison, and cocycles

For a normalized parameter-independent Markov kernel \(K\), attach it to a DQM
fine experiment and form the joint law
\(J_\theta(dx,dy)=P_\theta(dx)K(x,dy)\).  The joint directional score remains
the fine score \(\ell_u(X)\).  Projection to \(Y\) gives the coarse score

\[
 \bar\ell_u(Y)=\mathbb E[\ell_u(X)\mid Y].
\]

The Pythagorean identity for conditional expectation, equivalently total
variance, gives

\[
 \Delta_F^\Psi(u,u)
 =\|\ell_u\|_2^2-\|\mathbb E(\ell_u\mid Y)\|_2^2
 =\mathbb E\operatorname{Var}(\ell_u\mid Y)\ge0.
\]

Equality holds exactly when \(\ell_u\) is \(Y\)-measurable.  The DQM transfer
and equality condition are established directly at
`06_general_coarsegraining.tex:170-224`
(`thm:cg-fisher-contraction`) and instantiated for bundle vertical tangents at
`05c_pullback_geometry.tex:1078-1160`
(`thm:pb-pullback-fisher-defect`).  Required side conditions include family
closure, smoothness of the induced statistical map, appropriate measurable
versions, and regularity at both scales; affinity of the map on measures does
not supply these conditions.

Write \(u_X=D^\omega sX\), \(L=T^V\Psi\), and
\(a_X=A_\Psi(s;X)\).  The chain rule gives the coarse jet \(Lu_X+a_X\).
Expanding its Fisher square and using
\(g^F(u_X,u_Y)-\bar g^F(Lu_X,Lu_Y)=\Delta_F^\Psi(u_X,u_Y)\)
gives the exact signed base identity

\[
 h_s^\omega-f^*\bar h_{\bar s}^{\bar\omega}
 =\delta_\Psi-\mathcal X_\Psi-\mathcal Q_\Psi,
\]

where

\[
 \delta_\Psi(X,Y)=\Delta_F^\Psi(u_X,u_Y),\quad
 \mathcal X_\Psi(X,Y)=\bar g^F(Lu_X,a_Y)+\bar g^F(a_X,Lu_Y),\quad
 \mathcal Q_\Psi(X,Y)=\bar g^F(a_X,a_Y).
\]

This reconstructs `05c_pullback_geometry.tex:821-856`
(`thm:pb-signed-base-comparison`).  Under the Markov hypotheses, base
positivity holds on exactly those directions satisfying

\[
 2\bar g^F(Lu_X,a_X)+\|a_X\|_{\bar g^F}^2
 \le \delta_\Psi(X,X),
\]

the sharp condition at `05c_pullback_geometry.tex:858-887`
(`thm:pb-signed-positivity-criterion`).  In particular \(a=0\) is sufficient,
not necessary.  It cannot be omitted: with an identity information channel,
a constant related section, and source and target horizontal lifts differing by
\(a\partial_\mu\), the vertical information defect is zero but

\[
 h_s^\omega-f^*\bar h_{\bar s}^{\bar\omega}=-a^2dx^2<0
\]

for \(a\ne0\) (`05c_pullback_geometry.tex:889-907`).

The vertical Fisher defect has the unconditional algebraic cocycle

\[
 \Delta_F^{12\circ01}
 =\Delta_F^{01}+(T^V\Psi_{01})^*\Delta_F^{12}.
\]

This is obtained simply by adding and subtracting
\((T^V\Psi_{01})^*g_1^F\), so it needs no section and no connection
(`05c_pullback_geometry.tex:1230-1257`,
`thm:pb-fisher-defect-cocycle`).  Markov hypotheses make both summands
positive; they are not needed for the identity itself.

For related sections at three levels, let
\(v_X=T^V\Psi_{01}D^{\omega_0}s_0X\),
\(A_X=A_{01}(s_0;X)\), and
\(\bar u_X=v_X+A_X=D^{\omega_1}s_1(Tf_{01}X)\).  Pulling the vertical cocycle
back through the fine jet gives the residual

\[
 \begin{aligned}
 \mathcal N(X,Y)
 &:=[\delta_{02}-\delta_{01}-f_{01}^*\delta_{12}](X,Y)\\
 &=\Delta_F^{12}(v_X,v_Y)-\Delta_F^{12}(\bar u_X,\bar u_Y)\\
 &=-\Delta_F^{12}(v_X,A_Y)-\Delta_F^{12}(A_X,v_Y)
   -\Delta_F^{12}(A_X,A_Y).
 \end{aligned}
\]

Hence the base cocycle is exact if and only if

\[
 \Delta_F^{12}(v_X,v_X)
 =\Delta_F^{12}(v_X+A_X,v_X+A_X)
 \quad\text{for every }X,
\]

equivalently \(\Delta_F^{12}(A_X,2v_X+A_X)=0\).  This reconstructs all signs
and the sharp equality condition in
`05c_pullback_geometry.tex:1267-1335`
(`thm:pb-base-defect-cocycle`).  The sufficient conditions
\(A_{01}=0\), \(\Delta_F^{12}=0\), or
\(A_{01}\subseteq\operatorname{rad}\Delta_F^{12}\) are not necessary because
the quadratic terms can cancel.

## 5. Configuration Fisher metrics and selected lifts

The manuscript does construct one nonempty regular configuration tier.  It
chooses a compact measured base, a trivial translation bundle, the fixed-
covariance normal location family, positive bounded weight \(w\), and smooth
basis fields \(\phi_a\) independent in
\(L^2(w\mu;\Sigma_0^{-1})\).  With

\[
 s_\xi(c)=\mathcal N\!\left(\sum_a\xi_a\phi_a(c),\Sigma_0\right),
\]

the parameterization is injective and defines \(\mathcal Q\cong\mathbb R^N\).
The integrated marginal Fisher form is the constant Gram matrix

\[
 \Phi_{ab}=\int \phi_a(c)^T\Sigma_0^{-1}\phi_b(c)w(c),d\mu(c).
\]

Independence makes \(\Phi\) positive definite.  Thus every \(C^2\) objective
has a locally Lipschitz natural-gradient field
\(-\Phi^{-1}\nabla\mathcal F\) and locally unique integral curves
(`05d_relational_inference.tex:235-318`,
`def:hist-finite-configuration-tier`,
`thm:hist-finite-tier-regularity`).  This is a genuine construction, not an
existence assertion.  It is explicitly a weighted product of marginal Fisher
metrics, not automatically the Fisher pullback of a joint recognition law.

The rank condition is sharp.  On an \(M\)-atom design, the Gram rank is at most
\(MK\); a nominal coefficient family with \(N>MK\) cannot satisfy the required
independence.  On \(\mathbb R^2\), the semimetric \(dx^2\) makes the gradient
equation unsolvable for \(\mathcal F=y\) and nonunique for \(\mathcal F=x\)
(`05d_relational_inference.tex:320-353`,
`05d_relational_inference.tex:560-571`,
`prop:hist-semidefinite-gradient-obstruction`).

An exact multi-agent VFE history requires additional probability-level data:
a manifold \(\mathfrak R_B\) of conditional recognition laws, an extraction
map \(\pi_i^{\mathrm{conf}}\), and a selected smooth right inverse

\[
 \iota_i:\mathcal Q_i\to\mathfrak R_B,
 \qquad
 \pi_i^{\mathrm{conf}}\circ\iota_i=\operatorname{id}.
\]

If the configuration metric is called exact joint Fisher, it must satisfy
\(\mathsf G_i^F=\iota_i^*G_{\mathfrak R_B}^F\), with the support, finiteness,
and differentiation envelopes stated at
`05d_relational_inference.tex:372-448`
(`hyp:hist-exact-vfe-lift`, `eq:hist-exact-fisher-lift`).  These are declared
inputs for a general application.  They are nonvacuous: on a one-point base,
take \(\mathcal Q=\{\mathcal N(\xi,1):\xi\in\mathbb R\}\),
\(\mathfrak R_B=\mathcal Q\), and
\(\pi^{\mathrm{conf}}=\iota=\operatorname{id}\).  With fixed model
\(P_0=\mathcal N(0,1)\), the exact VFE
\(\mathrm{KL}(\mathcal N(\xi,1)\Vert P_0)=\xi^2/2\) is smooth and finite, and
the pullback Fisher metric is \(d\xi^2\).  This witness shows consistency, not
automatic existence for an arbitrary pair of marginal sections.

The need for a selected lift is unavoidable.  For extraction
\(\pi(\theta,\eta)=\theta\) from the Euclidean Fisher plane,
\(\iota_0(x)=(x,0)\) and \(\iota_c(x)=(x,c)\) induce \(dx^2\), while
\(\iota_\Delta(x)=(x,x)\) induces \(2dx^2\).  The displayed configuration does
not determine the joint Fisher pullback
(`05d_relational_inference.tex:475-483`).  Likewise, the exact identity

\[
 \|L\|^2-(\|L_b\|^2+\|L_m\|^2)
 =\|L-L_b-L_m\|^2-2\langle L_b,L_m\rangle
\]

shows that the joint Fisher metric and the sum of marginal metrics have no
general Loewner order.  Equality is exactly the balance of the two terms;
family-level independence with additive marginal scores is a clean sufficient
condition (`05d_relational_inference.tex:450-484`,
`eq:hist-joint-versus-product`).

## 6. Meta-agent coarse-section compatibility

There are three distinct cases.

1. **Sharp descent construction.**  If \(f\) is a surjective submersion and
   \(\Psi s\) is constant on each fiber, the descent theorem constructs a
   unique smooth \(\bar s\).  With connected fibers, the differential
   projectability equation is equivalent.
2. **Affine averaging construction.**  Given a disintegration
   \(\kappa_{\bar c}\), an affine fiber map, a convex coarse fiber, and
   Bochner integrability, one can define
   \[
   (\mathsf R_\ell s)(\bar c)
   =\int_{f^{-1}(\bar c)}\Psi(s(c))\,\kappa_{\bar c}(dc).
   \]
   This is an actual measurable/affine construction
   (`05d_relational_inference.tex:995-1016`,
   `eq:hist-averaging-coarse-map`).  Smooth closure in a configuration
   manifold is additional.  On the exhibited finite tier it is discharged by
   requiring each averaged basis field to lie in the coarse span; then
   \(\mathsf R_\ell(\xi)=E\xi\) is smooth and gauge-equivariant, and metric
   compatibility is exactly
   \(E^T\bar\Phi E\preceq\Phi\)
   (`05d_relational_inference.tex:1097-1149`,
   `prop:hist-coarse-map-smoothness`).
3. **Generic configuration arrow.**  A smooth
   \(\mathsf R_\ell:\mathcal Q_\ell\to\mathcal Q_{\ell+1}\) is separately
   declared.  The source explicitly does not construct it from an arbitrary
   pointwise bundle morphism, nor prove that the projectable set is a smooth
   submanifold (`05d_relational_inference.tex:962-993`,
   `eq:hist-configuration-coarse-map`).

For affine averaging, Fisher contraction is not automatic.  Joint convexity of
\((\bar\beta,v)\mapsto\bar g^F_{\bar\beta}(v,v)\), a weight inequality, and a
fiber contraction imply a nonnegative configuration defect.  With constant
coarse Fisher form the exact decomposition is

\[
 \Delta_{\mathrm{avg}}
 =\underbrace{\int w\Delta_F^\Psi}_{\text{channel loss}}
 +\underbrace{\int(w-\bar w\circ f)L^*\bar g^F}_{\text{weight gap}}
 +\underbrace{\int\bar w\operatorname{Var}_{\kappa}^{\bar g^F}(LZ)}
 _{\text{context gap}}.
\]

Each term is nonnegative, so equality holds exactly when all three vanish
almost everywhere.  This is
`05d_relational_inference.tex:1018-1075`
(`thm:hist-averaging-defect`).  Joint convexity is essential: averaging the
covariance coordinates \((\Sigma_1,\Sigma_2)=(1,\delta)\) of centered normal
laws with tangent \((1,0)\) gives fine metric \(1/4\) and coarse metric
\(1/[2(1+\delta)^2]\), which is larger for
\(0<\delta<\sqrt2-1\)
(`05d_relational_inference.tex:1077-1095`).

Once a related coarse section and zero horizontal anomaly have actually been
supplied, its perceived geometry is

\[
 \bar h_{\bar s}^{\bar\omega}
 =(D^{\bar\omega}\bar s)^*\bar g^F,
 \qquad
 f^*\bar h_{\bar s}^{\bar\omega}
 =(D^\omega s)^*(T^V\Psi)^*\bar g^F.
\]

For a Markov fiber map, fine minus coarse is the positive pullback of
\(\Delta_F^\Psi\) (`05c_pullback_geometry.tex:1172-1199`,
`cor:pb-meta-perceived-geometry`).  Thus “the meta-agent inherits the fine
geometry” is valid only in this precise conditional sense; a meta-agent law,
section, connection, and compatible morphism are not manufactured by the
principal bundle (`07_general_renormalization.tex:209-221`).

## 7. Curve taxonomy and information duration

For a total-space curve \(\Gamma\), the unique connection splitting is

\[
 \dot\Gamma=H^\omega_\Gamma\dot\gamma
 +\operatorname{ver}^\omega\dot\Gamma,
 \qquad \gamma=\varpi\Gamma.
\]

At each point: stationary means both terms vanish; vertical means
\(\dot\gamma=0\) with nonzero total velocity; horizontal means nonzero base
velocity and zero vertical component; mixed means both base and vertical
components are nonzero.  Only verticality is connection independent
(`05d_relational_inference.tex:42-104`, `def:hist-curve-types`,
`prop:hist-horizontal-connection-dependence`).  A base curve has no
vertical/horizontal predicate.  A curve \(Q(\lambda)\) in a section space is
not a curve in the associated bundle, but evaluation at fixed \(c\) is
intrinsically vertical because

\[
 T\varpi\,\partial_\lambda Q(\lambda)(c)=0.
\]

This is `05d_relational_inference.tex:109-137`
(`hyp:hist-regular-section-space`,
`eq:hist-pointwise-history-verticality`).  For diagonal evaluation
\(\Gamma(\lambda)=Q(\lambda)(\gamma(\lambda))\), the vertical velocity is the
sum of pointwise history change and contextual section response,

\[
 v^\omega(\Gamma)
 =\partial_\lambda\widehat\Sigma(\lambda,\gamma(\lambda))
 +D^\omega Q(\lambda)\dot\gamma(\lambda),
\]

so cancellation can even make a moving diagonal curve horizontal
(`05d_relational_inference.tex:183-206`,
`eq:hist-diagonal-evaluation-velocity`).

On a selected regular configuration curve, Fisher speed, length, and duration
are

\[
 \nu_F=\sqrt{\mathsf G^F(\dot Q,\dot Q)},\qquad
 L_F=\int\nu_F,d\lambda,\qquad
 \tau(\lambda)=\int_{\lambda_0}^{\lambda}\nu_F(u),du.
\]

Under an orientation-preserving reparameterization
\(\widetilde Q=Q\circ\phi\),
\(\widetilde\nu_F=(\nu_F\circ\phi)\phi'\), so substitution proves length and
clock covariance.  If \(\nu_F>0\), \(\tau\) is a regular arc-length coordinate.
For natural-gradient descent
\(\dot Q=-a\operatorname{grad}^F\mathcal F\), \(a>0\), division by speed gives

\[
 \frac{dQ}{d\tau}
 =-\frac{\operatorname{grad}^F\mathcal F}
 {\|\operatorname{grad}^F\mathcal F\|_F},
 \qquad
 \frac{d\mathcal F}{d\tau}
 =-\|\operatorname{grad}^F\mathcal F\|_F.
\]

This reconstructs `05d_relational_inference.tex:576-641`
(`def:hist-fisher-clock`, `thm:hist-fisher-clock-invariance`).  Positive speed
is stronger than strict monotonicity: an isolated zero can preserve monotonicity
while destroying regular invertibility, as \(h=4x^2dx^2\) and
\(\tau(r)=r^2\) show (`05d_relational_inference.tex:1586-1607`).  A zero-speed
interval stalls the clock.  Endpoints determine only the lower bound
\(d_F(A,B)\le L_F(Q)\), not the realized path or duration
(`05d_relational_inference.tex:643-672`).

For a same-path Markov image \(P^Y_\lambda=P^X_\lambda K\), conditional score
projection gives

\[
 (\nu_F^X)^2-(\nu_F^Y)^2
 =\mathbb E\operatorname{Var}(\ell_\lambda^X\mid Y)\ge0,
\]

so every common subarc has no greater record/meta-agent duration.  Equality is
exactly score measurability almost everywhere along the path
(`05d_relational_inference.tex:847-896`,
`thm:hist-record-clock-contraction`).  This does not compare independently
optimized paths.  Parameter-dependent channels add
\(\partial_\lambda\log k_\lambda(Y\mid X)\) to the projected score and can
increase information (`05d_relational_inference.tex:898-916`).

## 8. Natural-gradient semiconjugacy

For independently recomputed fine and coarse vector fields, the required
relation is not Fisher contraction but oriented vector-field semiconjugacy:

\[
 T_Q\mathsf R_\ell X_\ell(Q)
 =a_\ell(Q)X_{\ell+1}(\mathsf R_\ell Q),
 \qquad a_\ell(Q)>0.
\]

This is the definition at `05d_relational_inference.tex:1160-1170`
(`def:hist-oriented-semiconjugacy`).  Off the coarse critical set the factor is
unique and obtained by pairing with the coarse vector field.  Integrating
\(a_\ell\) along a fine orbit gives
\(\sigma_Q(t)=\int_0^t a_\ell(\Phi_sQ),ds\), and ODE uniqueness yields

\[
 \mathsf R_\ell(\Phi_tQ)
 =\bar\Phi_{\sigma_Q(t)}(\mathsf R_\ell Q)
\]

on the maximal interval traversed by the reparameterization
(`05d_relational_inference.tex:1172-1278`,
`thm:hist-oriented-semiconjugacy`).  Positivity alone does not ensure full
coarse-orbit traversal: \(\mathsf R(x)=\arctan x\) maps a complete translation
orbit only to \((-\pi/2,\pi/2)\).  Nor does semiconjugacy prevent collapse:
constant \(\mathsf R\) and zero coarse field satisfy the equation while all
coarse lengths vanish (`05d_relational_inference.tex:1280-1293`,
`prop:hist-noncollapse`).

For natural gradients, assume

\[
 \mathcal F_\ell
 =\chi_\ell\circ\mathcal F_{\ell+1}\circ\mathsf R_\ell,
 \qquad \chi_\ell'>0,
\]

and let \(\mathsf R_\ell\) be a surjective horizontally conformal submersion,
so for horizontal vectors
\(G_{\ell+1}(TRZ,TRW)=\varphi_\ell^2G_\ell(Z,W)\).  The fine gradient is
horizontal because its differential annihilates \(\ker TR\).  For every
horizontal \(Z\),

\[
 \begin{aligned}
 G_{\ell+1}(TR\operatorname{grad}F_\ell,TRZ)
 &=\varphi_\ell^2G_\ell(\operatorname{grad}F_\ell,Z)\\
 &=\varphi_\ell^2\chi_\ell'
   G_{\ell+1}(\operatorname{grad}F_{\ell+1},TRZ).
 \end{aligned}
\]

Surjectivity of \(TR\) on the horizontal space and nondegeneracy therefore give

\[
 TR X_\ell
 =\chi_\ell'\varphi_\ell^2 X_{\ell+1},
\]

which is the claimed positive semiconjugacy factor
(`05d_relational_inference.tex:1454-1494`,
`hyp:hist-functional-compatibility`,
`prop:hist-natural-gradient-sufficiency`).  Equality of objectives alone is
insufficient: on \(\mathbb R^2\), the same objective with metrics
\(\operatorname{diag}(1,1)\) and \(\operatorname{diag}(1,\kappa)\),
\(\kappa\ne1\), gives noncollinear gradients on the dense set \(xy\ne0\)
(`05d_relational_inference.tex:1445-1452`).

The source supplies a nonempty conformal example but explicitly leaves the
manuscript's own RG histories open: one must still prove functional
compatibility on an open orbit neighborhood and horizontal conformality of the
declared \(\mathsf R_\ell\)
(`05d_relational_inference.tex:1496-1553`).  Consequently the conditional
semiconjugacy theorem is verified, while application-specific existence remains
`INCONCLUSIVE`.

Once semiconjugacy holds, the parameter-rate factor cancels under the change of
variables \(u=\sigma_Q(r)\); the coarse duration is the intrinsic length of the
image orbit.  Equality, constant rescaling, or contraction of fine and coarse
durations is determined exactly by

\[
 \|T\mathsf R_\ell X_\ell\|_{G_{\ell+1}}
 \mathrel{=,\;\kappa,\;\le}
 \|X_\ell\|_{G_\ell}
\]

along the orbit (`05d_relational_inference.tex:1295-1357`,
`thm:hist-duration-relation`, `thm:hist-duration-criterion`).  This metric
condition is separate from semiconjugacy.

## 9. Fisher duration and the no-physical-time boundary

On a noncritical configuration region define

\[
 U_F=-\frac{\operatorname{grad}^F\mathcal F}{N},
 \qquad
 \alpha_F=U_F^\flat=-\frac{d\mathcal F}{N},
 \qquad
 N=\|\operatorname{grad}^F\mathcal F\|_F.
\]

A regional unit clock \(T\) exists exactly when \(\alpha_F=dT\), equivalently
when \(d\alpha_F=0\) and all periods vanish.  Direct differentiation gives

\[
 d\alpha_F=N^{-2}dN\wedge d\mathcal F.
\]

Thus even local clock potentials are obstructed whenever gradient norm varies
along a regular level set.  For \(\mathcal F(x,y)=xy\) on the first quadrant,

\[
 d\alpha_F
 =\frac{x^2-y^2}{(x^2+y^2)^{3/2}},dx\wedge dy,
\]

which is nonzero on generic neighborhoods, although each individual regular
orbit still has its arc-length coordinate
(`05d_relational_inference.tex:771-842`,
`thm:hist-global-clock-exactness`, `eq:hist-nonexact-clock-example`).

The type separation is final and explicit:

\[
 \ell\;\text{(discrete RG depth)},\qquad
 r\;\text{(chosen orbit parameter)},\qquad
 \tau^{(\ell)}\;\text{(metric arc length from an origin)}.
\]

They are not interchangeable.  A physical clock would additionally require an
operational bridge, orientation and synchronization conventions, and treatment
of critical/null segments and global periods.  None is supplied or claimed
(`05d_relational_inference.tex:1555-1624`,
`prop:hist-coordinate-independence`).  The correct verdict is therefore not
that physical time has been constructed, but that the theory rigorously avoids
making that identification.

## 10. Actual constructions versus declared inputs

| Object or existence statement | Classification | Reason |
|---|---|---|
| Associated bundles \(P\times_G\mathcal B_x\) | **Actual construction** | Quotient of declared principal bundle and invariant represented fiber. |
| Relative principal frame field between two local sections of one \(P\) | **Actual construction** | Unique by the torsor property. |
| Cross-associated morphism | **Conditional construction** | Constructed from a supplied equivariant fiber map; the fiber map is not automatic. |
| Principal scale morphism | **Declared input with exact existence criterion** | Exists iff the extension bundle matches the pullback bundle; topological failure is possible. |
| Associated scale morphism | **Conditional construction** | Constructed from a principal scale morphism and an intertwining, family-closing smooth fiber map. |
| Connections \(\omega_x\), sections \(s_x\), base/channel weights | **Declared inputs** | No canonical choice follows from the bundle. |
| Covariant jets, Fisher/Amari pullbacks, anomaly, vertical/base defects | **Actual constructions** | Explicit typed formulas once the preceding inputs exist. |
| Coarse section by sharp descent | **Conditional construction** | Unique and smooth once projectability through a surjective submersion holds. |
| Coarse section by affine averaging | **Conditional construction** | Requires disintegration, affine/convex fiber structure, integrability, and closure in the selected coarse tier. |
| Generic configuration coarse map \(\mathsf R_\ell\) | **Declared input** | Pointwise bundle maps do not define it on all sections. |
| Finite normal-location configuration tier and Gram Fisher metric | **Actual construction** | Explicit nonempty \(\mathbb R^N\) model with positive-definite metric. |
| Exact multi-agent recognition lift and exact joint Fisher metric | **Declared input** | Requires a selected right inverse and joint/correlation data; marginals do not determine it. |
| Natural-gradient orbit on the exhibited tier | **Actual local construction** | Standard local ODE existence for the constructed strong metric and a supplied \(C^2\) objective. |
| Exact VFE identification of that orbit | **Conditional construction** | Requires the exact recognition lift, support/finiteness, and domination hypotheses. |
| Fisher duration on a selected regular orbit | **Actual construction** | Arc-length integral after metric, path, orientation, and origin are supplied. |
| Regional/global scalar information clock | **Conditional construction** | Requires exact normalized VFE one-form and zero periods. |
| Natural-gradient semiconjugacy for arbitrary RG maps | **Open/declared compatibility** | Conditional theorem is proved; the manuscript-specific functional and conformal hypotheses are not. |
| Physical time or synchronized operational clock | **Outside target / not constructed** | Explicitly excluded and no bridge is supplied. |

## 11. Falsification conditions and surviving obligations

The conditional-pass verdict would be falsified by any of the following
scope-matched evidence:

1. an admitted bimeasurable parameter-independent sample action for which the
   transformed DQM score does not preserve the second moment;
2. an admitted surjective submersion with connected fibers satisfying the
   differential projectability equation but for which no smooth descended
   section exists;
3. an admitted pair of composable bundle morphisms violating either the
   ordered anomaly chain rule or the algebraic pullback cocycle;
4. an admitted normalized parameter-independent Markov kernel for which the
   output score is not conditional expectation of the fine score, or for which
   total variance gives a negative Fisher defect;
5. an exhibited finite-tier basis that is independent in the declared weighted
   \(L^2\) space but has a singular Gram matrix;
6. a surjective horizontally conformal submersion and functionally compatible
   objectives satisfying all stated strong-metric hypotheses but whose natural
   gradients fail the semiconjugacy equation;
7. a source-level operational bridge identifying \(\tau\) with physical clock
   readings under specified synchronization and causal assumptions.  No such
   bridge occurs in the frozen sources.

The surviving application obligations are narrower than the verified
mathematics:

- exhibit the actual principal scale maps and check their bundle-topology
  criterion;
- exhibit a smooth exact recognition-law lift and prove the joint Fisher
  pullback identity for each claimed exact VFE history;
- prove smooth projectability or the affine-averaging hypotheses for each
  claimed meta-agent configuration map;
- prove the isotropy/zero-horizontal-anomaly condition wherever base Fisher
  contraction is claimed;
- prove functional compatibility on an open orbit neighborhood and horizontal
  conformality for the manuscript's own independently recomputed RG flows;
- keep any physical-time interpretation outside theorem status until an
  operational bridge is separately supplied and tested.

## Oracle erasure

Re-deriving from the frozen definitions and source hypotheses reproduces the
derivations above. Every positive
conclusion follows from an explicit quotient construction,
tensor pullback, differential identity, conditional-expectation identity,
Gram-matrix argument, ODE calculation, or exactness criterion.  Every automatic
existence strengthening is either classified as a declared input/open
obligation or defeated by a typed counterexample.  The sector verdict therefore
survives oracle erasure.
