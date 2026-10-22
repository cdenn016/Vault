<!-- rigorous-theory-search-metadata {"schema_version":"rigorous-theory-search/v1","contract_id":"contract-sha256-cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e","target_digest":"cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e"} -->
# An exact interacting two-stage formation construction

## Result and assumptions

There is an explicit non-Gaussian, four-agent realization of state-selected recursive formation within the original smooth KL/Fisher model. A relabeling-equivariant rule selects two first parents and then their union from an open class of initially singleton configurations. Every fine child remains distinct at every finite time. Each join forgets a continuous public model-law distinction, even after membership-event times are retained. Parent laws, evaluators, channels, source priors, original-time dynamics, admitted adaptive joint response histories, collective minimizing connections, and rank-two contextual tensors are inherited exactly. The connection curvature is nonzero at every finite time.

This is an existential construction in the general-law framework, conditional on its displayed statistical architecture. It uses matrix Wishart laws with common precision across agents, context-constant individual shapes, moment-dependent comparison channels, fresh extensive responses, and a fixed threshold membership criterion. The initial class is open inside this invariant family, not in all probability-law configurations. No membership tree is supplied. Every block's additive quotient is already mathematically available initially; the state rule selects when it becomes the operative parent description. The fine dynamics never fuses, resets, or erases a child law. The threshold is declared, not derived uniquely from the KL functional.

The complete proofs are [coupled flow](routes/coupled-wishart-flow.md), [coupled geometry](routes/coupled-wishart-geometry.md), [membership and actual information loss](routes/wishart-selection.md), and [joint response histories](routes/wishart-response.md). The latter two use only the shape equations and fixed addition, so their proofs transfer unchanged when the constant-channel precision equation is replaced by the coupled equation derived below.

## Original model and full derivative

On the represented-content space \(\operatorname{SPD}(2)\), use the density
\[
W(a,P)(dX)=\frac{\det(P)^a}{\sqrt{\pi}\Gamma(a)\Gamma(a-\tfrac12)}
\det(X)^{a-3/2}e^{-\operatorname{tr}(PX)}dX,\qquad
a>\tfrac12,\quad P\succ0.
\]
This is a law of matrix contents, not a Gaussian covariance closure. The real shape need not be an integer or half-integer. Normalization and convolution are proved directly by changes of variables in [wishart-geometry.md](routes/wishart-geometry.md).

Agent \(i\) has \(q_i=W(\alpha_i,P)\), \(s_i=W(\eta_i,Q)\), and product recognition. Here \(\eta_i\) denotes the model shape called \(\beta_i\) in the route files, avoiding confusion with a source-row weight. Choose proper fixed local data
\[
r_i=W(\eta_0,I),\qquad G_i(m,dX)=W(\alpha_0,I)(dX),
\qquad \alpha_0,\eta_0>\tfrac12.
\]
For \(N=4\), \(\kappa>0\), set
\[
M_q=\sum_i\mathbb E_{q_i}X,\qquad
\Lambda_q=I+\frac{\kappa}{N}M_q,\qquad
\mathcal K^q_{ij}[\mathbf q](x,dX)=W(\alpha_0,\Lambda_q)(dX).
\tag{1}
\]
Use the exchanged model-sector construction. All sources, including self, are allowed with \(\pi_{ij}=1/N\). These self channels are explicitly nonidentity channels. Every channel is normalized; it ignores its particular input sample but depends smoothly on all laws through their moments.

With arbitrary original positive temperatures, equal source costs within each receiver row give exact Gibbs rows equal to their priors. The permitted Gibbs-reduced original potential for one sector is
\[
E_q=\sum_i\left[
\operatorname{KL}(q_i\Vert W(\alpha_0,I))
+\operatorname{KL}(q_i\Vert W(\alpha_0,\Lambda_q))\right].
\tag{2}
\]
Its complete channel derivative is
\[
C_q=\Lambda_q+\frac{\kappa}{N}
(M_q-N\alpha_0\Lambda_q^{-1})
=I+\frac{2\kappa}{N}M_q-\kappa\alpha_0\Lambda_q^{-1}.
\tag{3}
\]
The resulting unrestricted-density force, up to a constant, is
\[
h_i(X)=2\log q_i(X)-2(\alpha_0-\tfrac32)\log\det X
+\operatorname{tr}[(I+C_q)X].
\]
Substituting into \(\dot q_i=-q_i(h_i-\mathbb E_{q_i}h_i)\) proves exact invariance:
\[
\dot\alpha_i=-2(\alpha_i-\alpha_0),\qquad
\dot P=-2P+I+C_q,
\tag{4}
\]
with the exchanged equation for \(\eta_i,Q\). This is full-density tangency, not a projected parameter update. Freezing \(\Lambda_q\) would omit part of (3) and compute a different vector field.

There is genuine interagent coupling:
\[
DC_q[H]=\frac{2\kappa}{N}H+
\frac{\kappa^2\alpha_0}{N}\Lambda_q^{-1}H\Lambda_q^{-1}.
\]
Its trace pairing with any nonzero symmetric \(H\) is strictly positive. Moment changes of one agent affect the other agents' forces. The two sectors have separate population coupling; the selected product evaluator does not add cross-sector coupling.

Let \(A=\sum_i\alpha_i\), \(m=A/N\). Since \(M_q=A P^{-1}\), every precision eigenvalue solves
\[
\dot p=-2p+2+\frac{2\kappa m(t)}p
-\frac{\kappa\alpha_0p}{p+\kappa m(t)},\qquad
m(t)=\alpha_0+e^{-2t}(m(0)-\alpha_0).
\tag{5}
\]
Uniform positive lower and finite upper barriers prove global SPD existence. The derivative of the right side with respect to \(p\) is
\[
-2-\frac{2\kappa m}{p^2}
-\frac{\kappa^2\alpha_0m}{(p+\kappa m)^2}<0.
\]
The scalar solution has strictly positive derivative with respect to its initial value at every finite time. Distinct eigenvalues cannot meet in finite time. Compact positive parameter neighborhoods justify all KL, logarithmic-determinant, moment, and Fisher-score calculations.

## Exact recursive inheritance

For a current block \(I\), retain \(n_I=|I|\), \(A_I=\sum_{i\in I}\alpha_i\), \(B_I=\sum_{i\in I}\eta_i\), and common \(P,Q\). Independent matrix addition gives
\[
q_I=W(A_I,P),\qquad s_I=W(B_I,Q).
\]
The parent reference, evaluator, and peer targets have shapes \(n_I\alpha_0,n_I\eta_0\), obtained by convolving the actual child outputs. Its source prior is \(\pi^c_{IJ}=n_J/N\), the sum of the original priors over the sender block.

The total moments and primitive count are retained exactly:
\[
M_q=\sum_I\mathbb E_{q_I}X_I,\qquad N=\sum_I n_I.
\]
Use these same quantities in (1), including after only one parent remains. The complete derivative of the parent original-KL energy is still (3), since \(\sum_I n_I=N\). Its ordinary unit-Fisher equations are therefore
\[
\dot A_I=-2(A_I-n_I\alpha_0),\qquad
\dot B_I=-2(B_I-n_I\eta_0),
\]
together with exactly (4). This proves the same-time vector-field square directly; it does not assert equality of fine and coarse energies.

Joining adds \((n,A,B)\) and keeps the common precisions. It is associative, and references, channels, source priors, moments, and evolution all commute with it. The final parent retains its inherited nonidentity internal-source term. Replacing that channel by identity would change the dynamics.

## State selection, persistence, and information loss

Fix \(\delta>0\). Start with four singletons and read \(b_I=A_I/n_I-\alpha_0\). Join current blocks when \(|b_I-b_J|\) first reaches \(\delta\). Simultaneous threshold edges join their connected components. Between events, \(\dot b_I=-2b_I\); at a join, \(b\) takes the primitive-count-weighted average.

Let \(a_1<a_2<a_3<a_4\) be the sorted initial belief shapes, with successive gaps \(d_1,d_2,d_3\). The nonempty open class
\[
\delta<\min(d_1,d_3),\qquad d_2>\max(d_1,d_3)
\]
gives the lower and upper pair events
\[
t_L=\tfrac12\log(d_1/\delta),\qquad
t_R=\tfrac12\log(d_3/\delta),
\]
followed by their union at
\[
t_2=\tfrac12\log\left(
\frac{d_2+(d_1+d_3)/2}{\delta}\right)>\max(t_L,t_R).
\]
The [selection proof](routes/wishart-selection.md) excludes intervening cross joins and cascades. Both first parents coexist for a nonzero interval. Joined child-block distances remain below threshold afterward, and all fine belief laws remain distinct at every finite time. The rule is invariant under relabeling and uses retained quantities at both stages.

One explicit nonempty choice is \(\alpha_0=\eta_0=\kappa=1\), \(\delta=1/10\), sorted belief shapes \((1,6/5,9/5,21/10)\), and independently varying model shapes near \((4/5,11/10,7/5,17/10)\). The gaps are \((1/5,3/5,3/10)\), so the three event times are \(\tfrac12\log2\), \(\tfrac12\log3\), and \(\tfrac12\log(17/2)\). A sufficiently small open neighborhood and all its relabelings obey the same strict inequalities. Choose the contextual chart \(a\in(1/5,2/5)\), a bounded open interval of \(\chi\), and \(b=3/10\). This supplies actual admissible constants and an open preparation class; no existence assumption is hidden in the notation.

A birth time can reveal a two-child belief-shape gap, so that gap is not used as the loss witness. Instead vary two model shapes by \((\eta_i,\eta_j)\mapsto(\eta_i+\epsilon,\eta_j-\epsilon)\), with all belief shapes fixed. The parent model law, total moments, coupled future precision evolution, and every membership event and time remain unchanged, while fine laws vary continuously. Distinct fixed belief labels rule out a mere permutation. At the second join, transfer model shape between the two first-parent sums while preserving their final sum; this discards a further continuous distinction.

Past sample records are carried by the controller. They are not erased or claimed to have identical distributions across different initial preparations. The loss concerns the present parent state and its future admitted interface.

## Joint response histories

The predeclared interface draws fresh independent fine samples at each query and reports the two sums for each current block. Any normalized readout kernel on the whole vector of current-block sums is allowed, including overlapping unions of whole current blocks using shared same-batch samples. Its conditional law is
\[
K_\Pi=\bigotimes_{I\in\Pi}
[W(A_I,P)\otimes W(B_I,Q)].
\]
Closed waiting-time evolution and addition joins preserve this entire kernel. Induction conditional on the retained state and carried record history proves equality of every finite adaptive joint history of actions, times, records, and retained states, for each preparation. The coupled extension changes only the closed waiting-time equation; the [history proof](routes/wishart-response.md) otherwise applies verbatim.

Queries cutting through a retained block require additional intersection-shape data. Repeated hidden-child sampling and child-specific Bayesian resets are different interfaces. No belief reset is silently performed when a response is recorded.

## Curved geometry retained at every stage

Let shapes be constant over the contextual chart \((a,\chi)\), with \(a>0\), and initialize
\[
P(0;a,\chi)=R_\chi\operatorname{diag}(e^a,e^{-a})R_\chi^T,\qquad
Q(0)=\operatorname{diag}(e^b,e^{-b}),\quad b>0.
\]
Use common \(SO(2)\) conjugation and the manuscript convention \(D^Ap=dp+J_pA\). The represented matrices are distinct from contextual coordinates.

The precision score and Fisher metric are
\[
\ell_U(X)=\alpha\operatorname{tr}(P^{-1}U)-\operatorname{tr}(UX),
\qquad
g(U,V)=\alpha\operatorname{tr}(P^{-1}UP^{-1}V).
\]
Every common-precision contextual and orbit score is measurable from the retained sums, and the infinitesimal stabilizers agree. Thus the full minimizing connection classes and contextual tensors agree exactly, despite loss of shape-allocation information.

Let \(p_+(t,a)>p_-(t,a)\) be the belief eigenvalues. From (5), \(p_+\) increases and \(p_-\) decreases with \(a\) at every finite time. For a block define
\[
k_1=2A_I(t)\frac{(p_+-p_-)^2}{p_+p_-},\qquad
k_2=2B_I(t)\frac{(q_+-q_-)^2}{q_+q_-}>0.
\]
Then \(\partial_a k_1>0\), while \(k_2\) is independent of \(a\). Fine and parent geometry have
\[
\mathcal A^F=-\frac{k_1}{k_1+k_2}d\chi,\qquad
h^{\min}=g_{aa}da^2+\frac{k_1k_2}{k_1+k_2}d\chi^2,
\]
where \(g_{aa}=A_I[(\partial_a p_+/p_+)^2+
(\partial_a p_-/p_-)^2]>0\). Hence
\[
\mathcal F=-\frac{(\partial_a k_1)k_2}{(k_1+k_2)^2}
da\wedge d\chi\ne0.
\]
The geometry has rank two and nonzero curvature for every finite time, including both joins and afterward. It transforms under the required affine gauge law. The fixed sum retention has no moving-channel correction.

If discarded shape allocations vary over context, their positive fine Fisher lengths are lost and exact contextual geometry fails. Thus context-constant allocation is substantive. The [optimized-geometry identity](routes/optimized-geometry.md) separately proves the exact loss criterion.

## Boundaries of the result

The theorem supplies a conditional existence witness, with actual interagent coupling, no supplied tree, no erasure gate, distinct children, two selected stages, and exact inheritance. It does not prove common precision emerges from unrestricted laws: in this model \(P_i-P_j=e^{-2t}(P_i(0)-P_j(0))\), so unequal precisions never become exactly equal at finite time.

It does not prove a unique membership criterion, spontaneous creation of new operational redundancy, closure of identity-channel dynamics, unrestricted child responses, arbitrary contextual shape variation, a thermodynamic/RG limit, or emergent spacetime. The moment channels are global constitutive data, not a sparse local communication architecture. Within these limits, all components of the displayed finite construction are analytic derivations rather than numerical observations.

For the continuous-shape convention, see Letac and Massam's [central Wishart discussion](https://arxiv.org/html/1108.2849). Normalization, convolution, force, selection, response, and curvature arguments are supplied in the linked local proofs. No simulation, GPU computation, or formal proof assistant was used.
