<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e","schema_version":"rigorous-theory-search/v1","target_digest":"cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e"} -->
# Smooth loss, exact collective geometry, and a restriction on further compression

Date: October 22, 2026. Bounded constructive route. This file is the sole output owned by the geometry investigator.

## Target and scope

The frozen target asks for existence of at least four initially unpartitioned agents whose original smooth two-sector KL/Fisher flow selects two successive persistent parent levels, with genuinely lossy configuration retention, exact same-time dynamics, complete admitted response histories, and exact collective geometry. No prescribed hierarchy or erasure gate is permitted. This route does not solve endogenous selection or successive public compression.

The exact results below are (i) a smooth, non-Gaussian, genuinely lossy reduction of the original dynamics with a coupled evaluator, nonconstant inherited responses, nonzero collective connection curvature, and a positive contextual residual tensor; and (ii) an obstruction to smooth positive-dimensional compression preserving the entire residual tensor for unrestricted contextual first jets. The witness retains every child's public law and forgets its private law. Its associative join concatenates those public factors. It is a geometric completion of the existing conditional-reconstruction architecture, not a new derivation of that architecture or a construction of endogenous grouping.

The introduced hypotheses are explicit product preparations, fixed public/private represented coordinates, conditional-reconstruction channels, and context-independent private preparations. These are stronger than the frozen target. A finite-dimensional invariant family is used only to display the curved geometry; the underlying product splitting works for bounded positive general laws. No Gaussian closure is used.

## Sources and conventions

Read live sources: `chapters/02_geometry.tex` in full; `03_dynamics.tex`; the gradient and response sections of `05_inheritance.tex`; `07_smooth_closure.tex`; the supplied-tree construction and regularity limitation in `10_boundary_closure.tex`; `docs/research/2026-10-21-boundary-closure.md`; and `docs/research/2026-10-21-geometry-integration.md`. The wiki's `Agents as fibre-bundle sections.md` was consulted for source continuity. The live manuscript convention controls where older wiki formulas differ. Chapter 07 already gives the conditional-reconstruction identity and the private-spectrum evolution. The prior boundary record already gives the selective common-target channel used below.

| Object | Type and convention |
|---|---|
| Context base | A smooth manifold \(\mathcal C\), later an open rectangle in \(\mathbb R^2\). It is not a represented sample space. |
| Public samples | \(z,w\in\mathbb S^1\), with normalized Haar probability \(H\). |
| Private samples | Standard Borel spaces \(V_i,U_i\), with fixed probabilities \(A_i,B_i\). Two-point spaces suffice for the witness. |
| Fine laws | \(q_i(dz,dv)=p_i(dz)\kappa_i(dv)\), \(s_i(dw,du)=t_i(dw)\lambda_i(du)\). |
| Structure group | \(G=SO(2)\cong\mathbb S^1\), acting on the left by simultaneous public sample rotations; private samples are fixed. |
| Representation | On \(T(z)=(\cos z,\sin z)^T\in\mathbb R^2\), the standard left rotation. On laws, sample pushforward. |
| Bundle | The explicit witness uses \(P=\mathcal C\times G\); law fibers are associated through the pushforward action. |
| Metric | The ordinary Fisher metric of the product of all declared \(q_i,s_i\), with unit weights. Rows are fixed at their positive priors in the witness. |
| Orbit map | \(J\xi=(J_{q_i}\xi,J_{s_i}\xi)_i\). |
| Covariant derivative | \(D^A p=dp+J_pA\). |
| Passive frame change | \(p'=g_\#p\), \(A'=\operatorname{Ad}_g A-(dg)g^{-1}\); for this abelian group, \(A'=A-d\alpha\). |
| Retention | \(R((q_i,s_i)_i)=((p_i,t_i)_i)\), a fixed marginal channel at sample level and a smooth submersion on the product family. |
| Transport | The connection gives rotation by \(-\int_\gamma A\) along a path, in the horizontal-lift convention \((X,-JA(X))\). Nonzero curvature makes transport path dependent. |

The group is a sample symmetry for Haar references and the coupled evaluator below when external vector controls are rotated with the frame. This is separate from an arbitrary invertible change of coordinates: such a change is a passive re-expression only when the references, kernels, and all controls are carried with it. No unrestricted GL symmetry of the fixed circular model is asserted.

## Exact original dynamics on the product preparation

For the general product-splitting statement, let the public state and model spaces be arbitrary standard Borel spaces. Use the Chapter-07 reference

\[
R_i=R_i^c\otimes A_i\otimes B_i,
\qquad R_i^c=r_i^cG_i^c,
\]

with the factors reordered into state/model coordinates. Define each original belief channel by

\[
\mathcal K_{ij}^q((z,v),d(z',v'))
=B_{ij}^q(z,dz')\kappa_{i,z'}(dv'),
\]

where \(\kappa_{i,z'}\) is the actual receiver conditional, including away from the product preparation. Define the model channel similarly. These are normalized for every admitted law, with no time switch or gate. Then, on the full conditional-law domain,

\[
q_j\mathcal K_{ij}^q=(p_jB_{ij}^q)\kappa_i,
\qquad
\mathrm{KL}(q_i\Vert q_j\mathcal K_{ij}^q)
=\mathrm{KL}(p_i\Vert p_jB_{ij}^q).
\]

This is a functional identity before differentiation. Thus its derivative includes every sender, receiver, and receiver-conditional channel derivative. On the product submanifold the original potential becomes

\[
\mathcal E=\mathcal E_c((p_i,t_i),\beta,\gamma)
+\sum_i\mathrm{KL}(\kappa_i\Vert A_i)
+\sum_i\mathrm{KL}(\lambda_i\Vert B_i).
\tag{1}
\]

The full density derivative at \(q_i=p_i\kappa_i\), up to an irrelevant global constant, is

\[
h_i(z,v)=h_i^c(z)+\log(d\kappa_i/dA_i)(v).
\]

The centered unit-Fisher equation therefore factors exactly:

\[
\dot p_i=-p_i(h_i^c-\mathbb E_{p_i}h_i^c),
\qquad
\dot\kappa_i=-\kappa_i(\ell_i-\mathbb E_{\kappa_i}\ell_i),
\quad \ell_i=\log(d\kappa_i/dA_i).
\tag{2}
\]

The model equation is the sector exchange. This proves full-flow tangency to the product submanifold, not merely the form of a projected gradient. The private solution is

\[
\frac{d\kappa_i(t)}{dA_i}
=\frac{\exp(e^{-t}\ell_i(0))}{\int\exp(e^{-t}\ell_i(0))dA_i}.
\tag{3}
\]

Bounded initial log densities stay bounded; their finite-time map is injective. Distinct private preparations remain distinct at every finite time. All private laws may be varied smoothly without changing the retained flow. Hence this is actual smooth configuration loss, rather than relabeling or storage of the complete fine tuple. The local product references and reconstruction channels are the reason it works; replacing them by arbitrary identity channels does not preserve (1).

## An interacting non-Gaussian witness with global regular evolution

Put \(T(z)=(\cos z,\sin z)^T\) and define the circular exponential family

\[
p_\eta(dz)=\exp(\eta\cdot T(z)-\psi(\eta))H(dz),
\qquad
\psi(\eta)=\log\int e^{\eta\cdot T(z)}H(dz).
\]

These are von Mises laws, not Gaussian laws. Set \(p_i=p_{\eta_i}\), \(t_i=p_{\theta_i}\), \(m_i=\nabla\psi(\eta_i)\), \(n_i=\nabla\psi(\theta_i)\), and \(m=N^{-1}\sum_i m_i\), \(n=N^{-1}\sum_i n_i\). Use the proper coupled public joint reference

\[
R_i^c(dz,dw)=\frac{e^{J\cos(z-w)}}{Z_J}H(dz)H(dw),
\qquad Z_J=\int e^{J\cos z}H(dz),
\tag{4}
\]

for any fixed \(J\ne0\). Its model marginal is Haar and its conditional state evaluator is normalized since the integral over \(z\) is independent of \(w\).

Admit bounded piecewise-continuous controls \(e_q,e_s\), declared in advance, and set \(a_q(m,e_q)=\kappa m+e_q\), \(a_s(n,e_s)=\kappa n+e_s\), with \(\kappa\ne0\). For every allowed distinct-agent source use the selective public channel

\[
B_{ij}^q(z,dz')=\epsilon\delta_z(dz')
+p_{a_q}(dz')-\epsilon p_j(dz').
\tag{5}
\]

The model version replaces the sector. The residual measure is positive for sufficiently small fixed \(\epsilon>0\) on the global bounded domain proved below. Thus (5) is a normalized channel with nonconstant source-sample dependence. Direct integration gives \(p_jB_{ij}^q=p_{a_q}\). Its complete derivative is

\[
(dp_j)B_{ij}^q=\epsilon dp_j,
\qquad p_j(dB_{ij}^q)=dp_{a_q}-\epsilon dp_j,
\]

so the terms sum to \(dp_{a_q}\). Freezing the channel would lose this cancellation.

Choose all other agents as allowed sources, uniform strictly positive priors, arbitrary original \(T_q,T_s>0\), and rows initially at their priors. Every cost in a given row agrees. The rows consequently stay at their priors, and the Gibbs-reduced system gives the same matter dynamics. Define

\[
W_q(m,e)=\psi(a_q)-a_q\cdot m,
\qquad c_q=\nabla_mW_q
=\kappa(\nabla\psi(a_q)-m)-a_q,
\]

and similarly \(W_s,c_s\). Substitution into the original potential gives, up to the displayed private KL terms,

\[
\mathcal E_c
=2\sum_i[\mathrm{KL}(p_i\Vert H)+\mathrm{KL}(t_i\Vert H)]
-J\sum_i m_i\cdot n_i+N\log Z_J
+NW_q(m,e_q)+NW_s(n,e_s).
\tag{6}
\]

Every factor follows from the original local KL and the row-weighted peer KLs. In particular the coefficient two is not an inserted mobility. The full unrestricted-density Fisher derivatives are linear combinations of \(\log p_i\) and the two components of \(T\). They give

\[
\dot\eta_i=-2\eta_i+Jn_i-c_q,
\qquad
\dot\theta_i=-2\theta_i+Jm_i-c_s.
\tag{7}
\]

To check full-flow invariance, the logarithmic derivative of \(p_{\eta_i}\) is
\((T-m_i)\cdot\dot\eta_i\). Substituting (7) gives exactly the centered negative of the density force from (6). Therefore no restricted-family projection has been substituted for the original density dynamics.

Here \(\|\nabla\psi\|\le1\). For controls bounded by \(E\), \(\|c_q\|,\|c_s\|\le3|\kappa|+E\). Hence every natural parameter stays within

\[
\|\eta_i(t)\|,\|\theta_i(t)\|
\le M:=\max_i(\|\eta_i(0)\|,\|\theta_i(0)\|)
+\frac{|J|+3|\kappa|+E}{2}.
\]

Smoothness and bounded derivatives on this compact parameter domain give unique global solutions on each control interval, joined continuously at control switches. A density with natural parameter norm at most \(M\) lies between \(e^{-2M}\) and \(e^{2M}\) relative to Haar. Target parameters have norm at most \(|\kappa|+E\). Choosing

\[
0<\epsilon<\tfrac12\exp[-2(M+|\kappa|+E)]
\]

therefore makes the residual in (5) uniformly positive for all admitted times and controls. Initial private log densities bounded by a fixed constant have the same global regularity by (3). This defines a nonempty preparation class using uniform bounds before the dynamics is run.

## Exact collective connection and tensor

For any regular finite-dimensional family of the product laws, the score splits into a centered public score and a centered private score. The mixed expectation is zero, hence

\[
g_{\rm fine}=g_{\rm public}+g_{\rm private},
\qquad
g_{\rm private}=\sum_i(g^F_{\kappa_i}+g^F_{\lambda_i}).
\tag{8}
\]

The group acts trivially on the private factors. Therefore \(J=(J_{\rm public},0)\), and the fine and retained orbit kernels agree exactly. The Fisher loss is
\(\Delta=g_{\rm private}\), so

\[
\Delta(v,J\xi)=0
\quad\hbox{for every tangent }v\hbox{ and every }\xi.
\tag{9}
\]

The exact mixed-loss criterion from Chapter 02 is thus verified, not inferred from contraction. The entire fine and retained affine minimizing connection classes agree for every contextual section. For their residual tensors one gets the sharper identity

\[
h^{\min}_{\rm fine}-h^{\min}_{\rm public}
=\sum_i\left[(d\kappa_i)^*g^F_{\kappa_i}
+(d\lambda_i)^*g^F_{\lambda_i}\right].
\tag{10}
\]

Consequently exact tensor inheritance holds precisely when all private contextual derivatives vanish, after removing any redundant null parameter directions. Declare the initial private laws constant over \(\mathcal C\), while allowing them to vary between preparations and agents. Equation (3) preserves this contextual constancy for every admitted public control history. Both the minimizing connection and residual tensor then descend exactly for all times on the regular geometric stratum. At a rank change the smooth-connection statement must be rechecked; the dynamic reduction continues to hold.

Here is an explicit curved stratum. Write \(\psi_0(r)=\log\int e^{r\cos z}H(dz)\). For \(\eta=r(\cos\phi,\sin\phi)\), differentiation of normalization and rotational symmetry gives

\[
g^F_{p_\eta}=\psi_0''(r)dr^2+k(r)d\phi^2,
\qquad k(r)=r\psi_0'(r).
\tag{11}
\]

The radial coefficient is the strictly positive variance of \(\cos z\). The angular coefficient also equals \(r^2\mathbb E_{p_{(r,0)}}\sin^2z\); integration of \(\partial_z(\sin z e^{r\cos z})\) verifies equality to \(r\psi_0'(r)\). For \(r>0\), \(\psi_0'(r)>0\) by pairing \(z\) with \(z+\pi\), so \(k'(r)=\psi_0'(r)+r\psi_0''(r)>0\).

Take \(N=4\). On the context rectangle \((a,\chi)\in(a_-,a_+)\times(-\chi_0,\chi_0)\), set initially

\[
\eta_1=a(\cos\chi,\sin\chi),
\quad \eta_i=(b_i,0)\ (i=2,3,4),
\quad \theta_i=0,
\]

where the distinct positive \(b_i\) lie outside \([a_-,a_+]\). All four public laws are distinct. Choose four arbitrary context-constant private preparations, also distinct if desired. Let \(K_0=\sum_{i=2}^4k(b_i)>0\). The common rotation generator is angular differentiation. Its locked inertia and momentum pairing are \(k(a)+K_0\) and \(k(a)d\chi\). Solving the normal equation gives

\[
A^F=-\frac{k(a)}{k(a)+K_0}d\chi,
\qquad
h^{\min}=\psi_0''(a)da^2
+\frac{k(a)K_0}{k(a)+K_0}d\chi^2.
\tag{12}
\]

The curvature is

\[
F=dA^F=-\frac{k'(a)K_0}{(k(a)+K_0)^2}da\wedge d\chi\ne0.
\tag{13}
\]

Thus the inherited geometry is neither a zero tensor nor merely a removable exact connection on this patch. The residual tensor is positive definite on this two-dimensional context. With controls smooth in context, smooth dependence of (7) on initial data preserves nonzero curvature, positive residual rank, and distinctness on a common nonzero time interval after restricting to a compact subrectangle. Equations (8)-(10) continue to prove equality beyond that interval wherever the regular collective stratum persists. No claim of permanent nonzero geometric rank is made.

For a passive rotation \(\alpha(c)\), every public angular coordinate gains \(\alpha\), so its momentum pairing gains the locked inertia times \(d\alpha\). The formula for the minimizer therefore gives \(A'=A-d\alpha\). Substitution into \(dp+JA\) cancels the added angular derivative. Fisher isometry then proves invariance of (12). These are actual transformation-law checks. On multiple patches the same calculation gives compatible local connection forms whenever the prescribed transition rotations obey their cocycle identities. The explicit witness has a global trivialization, so it establishes no nontrivial bundle topology. Equation (13) still creates path-dependent connection transport on that trivial bundle.

## Responses, joins, and their precise limit

Declare the response class before testing it: at each record time a policy may choose a block, sector, and any fixed normalized public kernel \(L_a(z,do)\). A fresh child label is sampled uniformly in that block and a fresh public sample is drawn. The response is

\[
K_a^I(do)=\frac1{|I|}\sum_{i\in I}\int L_a(z,do)p_i(dz),
\tag{14}
\]

with the model exchange. The identity public readout is already nonconstant. The genuine transmitted output \(p_{a_q}\) from (5), and the normalized evaluator (4), are also determined by the retained data. Policies may choose the next bounded control from the preceding records. Records do not Bayesian-reset the fine laws in this declared protocol; such resetting would require an additional invariant-family and control analysis.

The retained configuration fixes (7) and every conditional next-record kernel. Induction over record times therefore proves equality of full joint admitted record histories, including history-dependent controls. This is stronger than equality of isolated marginals. For the public samples, reusing a fixed child label can also be represented if that label and its posterior distribution are retained; that extension is not needed for (14). Private-sensitive readouts are outside the declared protocol and fail in general.

For an arbitrary block \(I\), use parent law \(P_I=\bigotimes_{i\in I}p_i\), model law \(S_I=\bigotimes_{i\in I}t_i\), count \(|I|\), and the inherited vector field indexed by its retained public factors. Its evaluator is the product of (4), hence normalized. Joining disjoint blocks is product of laws and addition of counts. This is associative, and the global means needed in (7) combine by count-weighted sums. The same fine controls and equations operate under every regrouping; no tree is supplied or needed for this algebra.

This join performs no additional public configuration compression. It retains the entire public tuple, although all fine private laws are forgotten. It cannot be reported as a second parent formation event or as a solution of the frozen existential target. The exact loss occurs in (8)-(10), and its scope is explicit.

## A sharp local obstruction to unrestricted geometric compression

**Proposition.** Let \(R:(\mathcal N,g)\to(\bar{\mathcal N},\bar g)\) be a smooth equivariant map of positive Fisher-metric statistical families. At a point \(p\), suppose \(\ker J_p=\ker\bar J_{R(p)}\). If the fine and coarse minimized residual tensors agree for every fine contextual first jet at \(p\), then \(\ker dR_p=0\).

**Proof.** Choose any \(v\in\ker dR_p\) and realize it as the derivative of a one-dimensional local contextual section. Its coarse derivative is zero, so the coarse minimized residual squared norm is zero. Equality of tensors makes the fine minimum zero. Positive definiteness implies \(P_Hv=0\), hence \(v=J_p\xi\) for some \(\xi\). Equivariance gives \(0=dR_pv=\bar J\xi\). Equality of the infinitesimal stabilizers implies \(J_p\xi=0\), hence \(v=0\). This proves the claim.

If \(R\) is also a submersion, the proposition rules out positive-dimensional local fibers. It does not exclude a discrete global quotient, nor does it exclude loss confined to directions absent from the admitted contextual jets. It requires no Markov contraction assumption. It is a necessary restriction on simultaneous exact tensor and connection-class inheritance, not a nonexistence theorem for the frozen formation target.

The minimal failure test for the constructive witness is to let one discarded Bernoulli private factor have context-varying logit \(\tau(c)\). Its additional fine residual tensor is

\[
\sigma(\tau)(1-\sigma(\tau))d\tau\otimes d\tau,
\]

while its coarse contribution is zero. The collective connection still agrees because the gauge acts trivially there. Thus any nonzero \(d\tau\) falsifies exact residual-tensor inheritance. This checks that the context restriction is load-bearing rather than cosmetic.

## Strongest supported result and next obligation

The smooth reconstruction architecture admits an explicit four-agent, coupled-evaluator, non-Gaussian reduction with genuine smooth loss, exact original dynamics and declared joint responses, and a nonzero-curvature collective connection with a positive residual tensor on a nonzero regular interval. The loss is in context-constant private factors. Arbitrary regrouping is associative but adds no public compression. This result does not select memberships, create a second lossy parent level, or establish indefinitely persistent geometric rank.

The obstruction shows why the next step cannot simply demand exact geometry for every public contextual jet while discarding smooth public state directions. A candidate endogenous selector must supply a dynamically invariant distribution of admitted contextual jets on which the discarded directions have zero residual Fisher length, or it must retain the resulting tensor defect. To change the answer, construct a state- or accessible-history-selected block retention with a nontrivial public fiber and prove that restricted-jet property is generated and preserved by the same original flow, without prescribing the block tree.

Only source reads and analytical derivations were performed. No numerical experiment, symbolic script, GPU operation, external literature query, or formal proof assistant was used. The exact formulas in this file are the checkable artifact; no executed numerical output exists.
