<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e","schema_version":"rigorous-theory-search/v1","target_digest":"cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e"} -->
# Coupled Wishart compression under the original full Fisher field

Date: October 22, 2026. Third bounded constructive round. This file is the only output changed in this round. It extends `routes/wishart-geometry.md` by a smooth moment-dependent channel and leaves the earlier files unchanged.

## Exact result and scope

The proposed moment-dependent channel works. It creates genuine dependence of every belief law's velocity on the other belief laws and, separately, of every model law's velocity on the other model laws. The shared-precision Wishart family remains invariant under the full density Fisher field. Public matrix summation still gives an exact same-time parent Fisher flow and an associative, genuinely lossy joining operation. The collective minimizing connection, its nonzero curvature, and its rank-two contextual residual tensor are inherited for every finite time on the stated section.

This strengthens the constant-channel construction. It does not derive membership selection or create the shared-precision preparation. The constitutive channels still ignore their input sample, and the chosen local evaluator does not couple the belief and model sectors. The new interaction is through the current population moments. No claim of generic closure for arbitrary law families or arbitrary contextual shape variation is made.

The frozen target remains the existence of endogenous recursive formation without a prescribed hierarchy. The construction below supplies exact recursive inheritance with nontrivial law coupling; it leaves the endogenous selection obligation separate.

## Types, conventions, and admissible preparations

The represented state and model samples are SPD matrices \(X_i,Y_i\in\mathrm{Sym}_2^+\). The context base is an open rectangle \(\mathcal C=(a_-,a_+)\times(-\chi_0,\chi_0)\), with \(0<a_-<a_+<\infty\). Sample coordinates and context coordinates are different objects. There are \(N\ge4\) fine agents.

Write \(W_{\alpha,P}\) for the density

\[
W_{\alpha,P}(dX)=
\frac{(\det P)^\alpha}{\Gamma_2(\alpha)}
(\det X)^{\alpha-3/2}e^{-\operatorname{tr}(PX)}dX,
\quad \alpha>1/2,\ P\in\mathrm{Sym}_2^+,
\]

\[
\Gamma_2(\alpha)=\sqrt\pi\Gamma(\alpha)\Gamma(\alpha-1/2).
\tag{1}
\]

Its normalization and convolution law were derived directly in `wishart-geometry.md`, equations (1)-(2). Briefly, at \(P=I\), use \(x_{11}=t\), \(x_{12}=\sqrt t u\), \(x_{22}=v+u^2\), with Jacobian \(\sqrt t\), to separate two gamma integrals and one Gaussian scalar integral. Congruence by \(P^{-1/2}\) has Jacobian \((\det P)^{-3/2}\), giving (1). For independent matrices with common precision, the convolution integral at \(S\) and the substitution \(X=S^{1/2}US^{1/2}\) give a density proportional to \((\det S)^{\alpha+\beta-3/2}e^{-\operatorname{tr}(PS)}\); normalization then proves

\[
W_{\alpha,P}*W_{\beta,P}=W_{\alpha+\beta,P}.
\tag{2}
\]

This permits every real shape above \(1/2\); it does not assume a Gaussian sampling representation.

The admitted preparations are

\[
q_i=W_{\alpha_i,P},\qquad s_i=W_{\beta_i,Q},
\tag{3}
\]

with common \(P,Q\) across agents. Shape parameters vary independently between preparations and agents, but are constant over the context base. They lie in fixed compact intervals inside \((1/2,\infty)\). Precision eigenvalues initially lie in a fixed compact positive interval. These are introduced preparation assumptions. The fine recognition law is the product over agents and sectors, without a probability distribution over configurations.

The structure group is \(SO(2)\), acting on the left by \(X\mapsto gXg^T\) and \(Y\mapsto gYg^T\). Hence \(P\mapsto gPg^T\), \(Q\mapsto gQg^T\), and shapes are fixed. The explicit principal bundle is \(\mathcal C\times SO(2)\), with associated law fibers. The metric is the ordinary Fisher metric of the product law, with every physical child weight equal to one. The connection convention is

\[
D^{\mathcal A}p=dp+J_p\mathcal A,
\qquad
\mathcal A'=\operatorname{Ad}_g\mathcal A-(dg)g^{-1}.
\]

The generator is \(\Omega=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\), so \(J_P\xi=\xi[\Omega,P]\). The connections and metrics below concern statistical law families. No SPD Riemannian exponential, logarithm, or retraction is used.

## Normalized channels and their complete derivative

Fix \(\alpha_0,\beta_0>1/2\) and \(\kappa>0\). The original proper local reference remains

\[
r_i=W_{\beta_0,I},\qquad G_i(m,dk)=W_{\alpha_0,I}(dk).
\tag{4}
\]

Thus \(R_i=r_iG_i\) is normalized. Define the current population moments and precision targets by

\[
M_q=\sum_i\mathbb E_{q_i}X_i,\qquad
\Lambda_q=I+\frac\kappa N M_q,
\]

\[
M_s=\sum_i\mathbb E_{s_i}Y_i,\qquad
\Lambda_s=I+\frac\kappa N M_s.
\tag{5}
\]

For every original source edge, including self, use

\[
\mathcal K_{ij}^q[\mathbf q](x,dX)=W_{\alpha_0,\Lambda_q}(dX),
\qquad
\mathcal K_{ij}^s[\mathbf s](y,dY)=W_{\beta_0,\Lambda_s}(dY).
\tag{6}
\]

These are normalized Markov kernels for all positive laws with finite first moments. Their input sample is ignored. Their output law varies smoothly with the population moment on a regular dominated domain. The Wishart preparation is a special invariant subfamily, not a restriction needed to define the kernels.

Use all agents as sources with positive priors \(\pi_{ij}=1/N\), and the original arbitrary temperatures \(T_q,T_s>0\). These self channels are nonidentity channels. Initialize source rows at their priors, or use the exact Gibbs reduction employed in the assembled construction. All sources within a receiver row have identical costs, so the original row flow preserves those priors. The Gibbs-reduced matter field is identical. The belief part of the exact original potential is

\[
\mathcal E_q=\sum_i\left[
\mathrm{KL}(q_i\Vert W_{\alpha_0,I})
+\mathrm{KL}(q_i\Vert W_{\alpha_0,\Lambda_q})\right],
\tag{7}
\]

and the model part is its sector exchange.

The moment-dependent terms in the peer part of (7) are

\[
\operatorname{tr}(\Lambda_qM_q)-N\alpha_0\log\det\Lambda_q.
\]

Since \(d\Lambda_q=(\kappa/N)dM_q\), their differential is

\[
\operatorname{tr}(C_q dM_q),
\quad
C_q=\Lambda_q+\frac\kappa N(M_q-N\alpha_0\Lambda_q^{-1})
=I+\frac{2\kappa}N M_q-\kappa\alpha_0\Lambda_q^{-1}.
\tag{8}
\]

Every matrix here is symmetric, so this is an ordinary trace pairing on symmetric variations. The second term of (8) includes all law-dependent-channel derivatives. For an individual edge, \((dq_j)\mathcal K_{ij}=0\) at a frozen kernel because the signed source variation has zero mass, while \(q_j(d\mathcal K_{ij})=dW_{\alpha_0,\Lambda_q}\). The latter depends on variations of every law through (5). Keeping only the receiver derivative would incorrectly replace \(C_q\) by \(\Lambda_q\).

Up to an additive constant, the complete density force at \(q_i\) is

\[
h_i^q(X)=2\log q_i(X)
-2(\alpha_0-3/2)\log\det X
+\operatorname{tr}[(I+C_q)X].
\tag{9}
\]

The logarithm is relative to the declared Lebesgue measure. Every term has finite variance on the regular Wishart domain. Substituting the centered force into \(\dot q_i=-q_i(h_i^q-\mathbb E_{q_i}h_i^q)\) and differentiating (1) gives exactly

\[
\dot\alpha_i=-2(\alpha_i-\alpha_0),
\qquad
\dot P=-2P+I+C_q.
\tag{10}
\]

The model equations replace \((\alpha_i,P,\alpha_0,C_q)\) by \((\beta_i,Q,\beta_0,C_s)\). Normalization supplies the constant part of the logarithmic derivative. This verifies tangency of the full unrestricted-density Fisher field, rather than postulating a finite-family projection. In particular all children have the same precision velocity whenever their precisions agree, so the common-precision assumption is invariant.

The field has genuine interagent dependence. On (3), \(M_q=A P^{-1}\), where \(A=\sum_i\alpha_i\); changing one child's shape changes \(M_q\) and therefore the precision velocity of every child. More generally a moment variation \(H=dM_q\) changes (8) by

\[
dC_q[H]=\frac{2\kappa}N H
+\frac{\kappa^2\alpha_0}N\Lambda_q^{-1}H\Lambda_q^{-1},
\]

which is nonzero for every nonzero positive semidefinite \(H\). There is no cross-sector coupling for the product evaluator (4); both sectors have their own nontrivial population coupling.

## Global SPD well-posedness

The shape equations have explicit positive solutions

\[
A(t)=N\alpha_0+e^{-2t}(A(0)-N\alpha_0),
\qquad m(t)=A(t)/N.
\tag{11}
\]

Let \(m_-=\min(m(0),\alpha_0)>0\), \(m_+=\max(m(0),\alpha_0)\). The matrix right side of (10) is a smooth rational function of \(P\) and commutes with it. A diagonalization of the initial precision therefore gives a solution with fixed eigenvectors, and each positive eigenvalue solves

\[
\dot p=f(p,m(t))
=-2p+2+\frac{2\kappa m(t)}p
-\frac{\kappa\alpha_0 p}{p+\kappa m(t)}.
\tag{12}
\]

Choose

\[
\delta=\min\left(1,\frac{\kappa m_-}{1+\kappa\alpha_0}\right)>0,
\qquad L=2+\kappa m_+.
\]

For \(0<p\le\delta\), the first two terms of (12) have nonnegative sum, the third is at least \(2(1+\kappa\alpha_0)\), and the magnitude of the negative last term is at most \(\kappa\alpha_0\). Hence \(f(p,m)>0\). For \(p\ge L\),

\[
f(p,m)\le-2p+2+\frac{2\kappa m_+}p<-2p+4<0.
\]

Thus every eigenvalue remains in

\[
\left[\min(p(0),\delta),\max(p(0),L)\right].
\tag{13}
\]

The right side is smooth and uniformly Lipschitz on this compact positive interval. The local solution consequently extends uniquely to every finite time. The corresponding matrix solution is the unique SPD solution because the rational matrix field is locally Lipschitz on \(\mathrm{Sym}_2^+\). The same argument applies to the model sector.

All shapes remain in compact intervals above \(1/2\); all precisions remain uniformly SPD and bounded. The density formula (1), with a slightly larger compact parameter set, dominates logarithmic determinant derivatives near the boundary and polynomial moments in the tails. This justifies differentiation, finite KL, square-integrable scores, and the full Fisher equation along the entire trajectory. The construction proves global regular evolution on this admitted invariant family; it does not assert global well-posedness on an unrestricted infinite-dimensional law manifold.

Different initial shapes remain different for every finite time. Precision eigenvalue ordering is also strict at every finite time. Indeed,

\[
f_p=-2-\frac{2\kappa m}{p^2}
-\frac{\kappa^2\alpha_0m}{(p+\kappa m)^2}<-2.
\tag{14}
\]

For the scalar solution map \(\Phi_t(p_0)\), differentiation with respect to \(p_0\) gives

\[
\partial_{p_0}\Phi_t(p_0)
=\exp\left(\int_0^t f_p(\Phi_u(p_0),m(u))du\right)>0.
\tag{15}
\]

The exponent is finite on each finite interval by (13). Two unequal eigenvalues therefore do not collide in finite time. Their difference contracts at least as fast as \(e^{-2t}\). This last statement does not imply finite-time isotropy.

## Exact parent energy and recursion

For disjoint blocks \(I\), retain \(n_I=|I|\), \(A_I=\sum_{i\in I}\alpha_i\), \(B_I=\sum_{i\in I}\beta_i\), and the sum laws

\[
q_I=W_{A_I,P},\qquad s_I=W_{B_I,Q}.
\]

The normalized sample map is fixed: \((X_i,Y_i)_{i\in I}\mapsto(\sum_iX_i,\sum_iY_i)\). Formula (2) proves the retained laws. The total moment and primitive population count are exactly

\[
M_q=\sum_I\mathbb E_{q_I}X_I,\qquad N=\sum_I n_I.
\tag{16}
\]

The denominator in (5) remains this primitive \(N\), not the number of current parents. The coarse reference and target shapes must be \(n_I\alpha_0\) and \(n_I\beta_0\). Define the parent-population belief energy by

\[
\mathcal E_q^c=\sum_I\left[
\mathrm{KL}(q_I\Vert W_{n_I\alpha_0,I})
+\mathrm{KL}(q_I\Vert W_{n_I\alpha_0,\Lambda_q})\right],
\tag{17}
\]

with the model exchange. Its moment-dependent part is still
\(\operatorname{tr}(\Lambda_qM_q)-N\alpha_0\log\det\Lambda_q\), since \(\sum_In_I=N\). Its complete derivative is therefore the same \(C_q\), and its ordinary unit-Fisher flow is

\[
\dot A_I=-2(A_I-n_I\alpha_0),\qquad
\dot B_I=-2(B_I-n_I\beta_0),
\qquad \dot P=-2P+I+C_q,\qquad\dot Q=-2Q+I+C_s.
\tag{18}
\]

Summing (10) gives exactly (18), at the original time. No fine-to-parent energy identity or inserted mobility is needed.

The parent evaluator is the normalized constant law \(G_I(m,dk)=W_{n_I\alpha_0,I}(dk)\), with proper model reference \(W_{n_I\beta_0,I}\). For independent fresh outputs across receiver children, summing the actual output laws (6) yields the normalized parent target \(W_{n_I\alpha_0,\Lambda_q}\), and analogously for the model sector. Thus the target law and its state dependence are inherited, rather than added at the parent level.

The inherited parent source prior is \(\pi^c_{IJ}=n_J/N\), obtained by summing the original source-label weights over block \(J\). It is positive and normalized at every partition. When only one final parent remains, its nonidentity self channel retains the second KL term in (17). Replacing it by an identity self-channel with zero self-cost would delete that contribution and change the flow. No new source prior or internal interaction is introduced at this handoff.

Joining adds counts and shapes and sums the two sample matrices. Associativity follows from ordinary addition and (2), and (18) commutes with this operation. At every stage the inherited coupling uses the same total moment (16). Positive-dimensional shape-allocation fibers are lost at every nontrivial join. Independent variations in model shapes with belief shapes fixed can keep every belief-shape-only event time unchanged, so recording such times does not reconstruct the discarded model allocations.

## Exact collective geometry and finite-time curvature

At fixed shape, the precision score and its Fisher metric are

\[
\ell_U(X)=\alpha\operatorname{tr}(P^{-1}U)-\operatorname{tr}(UX),
\qquad
g^F(U,V)=\alpha\operatorname{tr}(P^{-1}UP^{-1}V).
\tag{19}
\]

They follow by differentiating normalization in (1); in particular \(\mathbb EX=\alpha P^{-1}\). For common contextual precision changes, summing the fine scores gives

\[
A\operatorname{tr}(P^{-1}U)-\operatorname{tr}(US_X)
+B\operatorname{tr}(Q^{-1}V)-\operatorname{tr}(VS_Y),
\tag{20}
\]

which is exactly the score of the two retained sum laws. Conjugation-orbit scores have the same property. The retention channel is fixed and independent of context and state, so its Fisher loss is positive semidefinite. Equation (20) proves zero loss on every contextual or orbit direction used here. Hence \(\Delta(r_X,J\xi)=0\), and the residual Fisher lengths are also exactly retained. Fine and coarse infinitesimal stabilizers are both the rotations commuting with \(P,Q\); positive shape totals cannot add a null orbit direction. Thus the entire minimizing connection classes agree, not merely one arbitrarily chosen representative.

Initially choose the context section

\[
P(a,\chi)=R_\chi\operatorname{diag}(e^a,e^{-a})R_\chi^T,
\qquad Q=\operatorname{diag}(e^b,e^{-b}),\quad b>0.
\tag{21}
\]

Let \(p_+(a,t)=\Phi_t(e^a)\), \(p_-(a,t)=\Phi_t(e^{-a})\), using the belief scalar flow (12). The model precision has two unequal eigenvalues depending only on time, obtained from its corresponding scalar flow. By (15),

\[
p_+>p_->0,\quad
\partial_ap_+>0,\quad\partial_ap_-<0
\]

for every finite time. Put \(r=p_+/p_->1\). Then \(\partial_ar>0\). From (19), the belief and model locked inertias are

\[
k_1(a,t)=2A(t)\frac{(p_+-p_-)^2}{p_+p_-}
=2A(t)(r+r^{-1}-2),
\]

\[
k_2(t)=2B(t)\frac{(q_+-q_-)^2}{q_+q_-}>0.
\tag{22}
\]

Since \(A(t)>0\),
\(\partial_ak_1=2A(t)(1-r^{-2})\partial_ar>0\).
Radial and rotational tangent matrices are Fisher orthogonal. The radial coefficient is

\[
g_{aa}(a,t)=A(t)\left[
\left(\frac{\partial_ap_+}{p_+}\right)^2
+\left(\frac{\partial_ap_-}{p_-}\right)^2\right]>0.
\tag{23}
\]

Solving the common-rotation normal equation therefore gives, both before and after retention,

\[
\mathcal A^F=-\frac{k_1}{k_1+k_2}d\chi,
\qquad
h^{\min}=g_{aa}da^2+\frac{k_1k_2}{k_1+k_2}d\chi^2,
\]

\[
\mathcal F=d\mathcal A^F
=-\frac{(\partial_ak_1)k_2}{(k_1+k_2)^2}da\wedge d\chi\ne0.
\tag{24}
\]

This proves nonzero connection curvature and positive rank-two contextual geometry at every finite time. Neither exact equality of eigenvalues nor a zero contextual derivative is reached in finite time. Infinite-time isotropization is a different stratum and is not assigned a unique minimizing connection here.

A passive frame rotation adds its angle to both precision angles, so the momentum form gains \((k_1+k_2)d\vartheta\) and \(\mathcal A'=\mathcal A-d\vartheta\). The corresponding change in \(dp\) cancels in \(D^{\mathcal A}p\). The channels are covariant because \(M\mapsto gMg^T\) implies \(\Lambda\mapsto g\Lambda g^T\), and the identity reference is rotation invariant. The explicit bundle is trivial but the nonzero curvature makes transport path dependent. On an overlap, local forms glue under the stated affine law when transition rotations satisfy their cocycle. Neither nontrivial topology nor a state-generated comparison atlas is constructed.

## Responses, failure test, and remaining obligation

Admit arbitrary fixed normalized readout kernels of the pair of sum samples, with fresh independent draws at each record time. An adaptive policy may select readout kernels and record times from previous records. The identity sum readout is nonconstant and is included. The retained law gives the exact joint next-record kernel, while (18) gives the exact next retained state. Induction proves equality of every finite joint admitted response history. State resets, repeated use of an unretained fine sample, arbitrary identity-resolved probes, or reference-changing interventions are not part of this declared protocol. They would require separate closure conditions.

For the geometric failure test, vary \(\beta_1\) and \(\beta_2\) in opposite contextual directions while keeping their sum, all belief data, and the precisions fixed. The parent derivative is zero, but the fine score is the centered difference \(\log\det Y_1-\log\det Y_2\), with positive variance. This direction is orthogonal to conjugation orbits because determinant is invariant. The fine residual tensor is positive in that direction and the parent tensor is zero. Thus context-constant shape allocation remains a necessary preparation restriction for exact tensor inheritance; coupling (5) does not remove it.

There is also an exact finite-time limitation of this route. Allow unequal fine precisions \(P_i\) while keeping Wishart laws. Equation (9) still gives \(\dot P_i=-2P_i+I+C_q(M_q)\) with the same forcing for every child. Therefore

\[
P_i(t)-P_j(t)=e^{-2t}(P_i(0)-P_j(0)).
\]

The corresponding statement holds in the model sector. Thus the new moment coupling does not make previously unequal precisions first become exactly equal at a finite time. The shared-precision class used for exact convolution remains an invariant preparation assumption.

The exact inherited construction includes nontrivial interagent dependence, global regular dynamics, repeated public configuration loss, nonconstant joint sum responses, and nonzero retained curvature for every finite time. It permits every grouping from the initial time. This geometry route alone does not select one. The assembled construction uses the state/history rule proved in `wishart-selection.md`, with the interpretation delimited in `formation-scope.md`; its shape equations and loss witnesses are unchanged by the coupling. The model does not establish that common precision or its admissible contextual jets arise from unrestricted preparations.

No numerical experiment, symbolic script, GPU operation, external literature query, or formal proof assistant was used. The evidence is the analytical calculation above and the cited live-source conventions.
