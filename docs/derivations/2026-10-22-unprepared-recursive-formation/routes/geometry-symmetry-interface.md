<!-- rigorous-theory-search-metadata {"schema_version":"rigorous-theory-search/v1","contract_id":"contract-sha256-b542fc3173c340f7c3430dc4795f9964d742d9047e059add3a8949d73f3bbcbe","target_digest":"b542fc3173c340f7c3430dc4795f9964d742d9047e059add3a8949d73f3bbcbe"} -->
# Actual Fisher geometry of the anchored physical-rotation quotient

## Result and scope

The local section-valued retention in `parent-closure.md`, equations (P11)--(P21), preserves the contextual Fisher geometry of actual normalized parent laws. Its canonicalizing physical rotations are constant across the evaluation context. This gives an equality of every collective minimizing cost, with the original product Fisher normalization. It is stronger than assigning the fine tensor to a quotient as metadata. It does not give an isometry in every state direction: the discarded constant relative orientations have positive fine Fisher norm.

The construction closes original-time evolution only with its moving-canonicalization term. The Fisher metric of the canonical product-law slice is generally different from the metric on the isometric quotient. The first metric establishes contextual geometry; the second can describe gradient descent on quotient states. They cannot be substituted for one another.

The results below are conditional on a fixed reference context, a regular local phase chart, and the independently established physical symmetry of the fine dynamics and response class. These are route-specific choices. The frozen target requires an open full law domain and a declared regular contextual family, not equality for every possible contextual jet. The local construction meets that geometric scope. It does not prove clique formation. A globally single-valued representative on one fixed sample fiber is not constructed; the global quotient has a finite stabilizer change and needs bundle charts.

The source construction read for this note is `parent-closure.md`, especially (P1)--(P15), (P18)--(P23). The live Chapter 2 geometry and Chapter 3 dynamics of `Research/manuscripts/MAgent_Theory_2.0/` fix the Fisher normalization and complete natural-gradient convention. `geometry.md` gives the separate moving-channel and variable-event-time formulas. The final section below analyzes the later bridge communicated by the parent: all-source self loops, fixed Haar angular comparison, and uniform local evaluator and reference, so that the bit couplings and angular evaluator coupling are both zero. This differs from the nonself, possibly nonzero-coupling example written in `parent-closure.md`; no theorem about that example's clique dynamics is imported.

## Typed conventions

| Object | Type, action, and convention |
| --- | --- |
| Contextual base \(\mathcal C\) | A smooth manifold, restricted below to a compact coordinate patch with fixed anchor \(c_*\). Context is distinct from inference time \(t\). |
| Sample spaces | \(K=M=\{-1,1\}\times S^1\), with \(d\nu=\frac12\sum_{z=\pm1}\delta_z\otimes d\theta/(2\pi)\). |
| Statistical fibers | Strictly positive normalized laws \(q_i(c)\), \(s_i(c)\). Their internal bit-angle dependence is unrestricted. The within-agent recognition law is \(q_i\otimes s_i\). |
| Physical action | \(A=(S^1)^N\), acting on densities from the left by \((\tau_a f)(z,\theta)=f(z,\theta-a)\). The same \(a_i\) acts on \(q_i,s_i\). It changes physical laws in a fixed sample frame. |
| Discarded group | \(H_I=\{a\in(S^1)^I:\prod_i e^{ia_i}=1\}\). Local lifted representatives satisfy \(\sum_i a_i=0\). Only rotations constant over \(\mathcal C\) are quotiented. |
| Collective gauge group | \(G=S^1\), with common angle \(\chi(c)\) acting on every primitive belief and model coordinate. The physical action commutes with this action. |
| Infinitesimal action | \(J_f\xi=-\xi\partial_\theta f\); its score is \(-\xi\partial_\theta\log f\). |
| Metric | Unit Fisher metric \(g_f(v,w)=\int (vw/f)d\nu\), summed over all belief and model factors. |
| Connection convention | \(D^A p=dp+J_p A\), with \(A'=A-d\chi\). A passive gauge change is \(p'=\tau_\chi p\). |
| Statistical section | \(p_t:c\mapsto(q_{i,t}(c),s_{i,t}(c))_{i\in I}\). Its entire retained portion is part of the parent state. |
| Parent fibers | \(K^I,M^I\) with product measures and normalized product densities \(Q_I,S_I\). The gauge rotates every primitive circle coordinate once. The aggregate angle has gauge charge \(|I|\). |

The integral in the metric row can equivalently be written \(g_f(v,w)=\mathbb E_f[(v/f)(w/f)]\). Only ordinary sample rotations have been used. General invertible frame changes need not preserve the chosen evaluator or channels and are not additional physical symmetries of this construction.

## The local realization theorem

Fix a finite nonempty block \(I\) of size \(n\). Assume its densities are positive, have the derivatives used below, and have finite Fisher scores. Suppose

\[
u_i(c_*)=\int e^{i\theta}q_i(c_*;z,\theta)d\nu\ne0.
\tag{S1}
\]

Choose compatible local lifts \(\vartheta_i=\arg u_i(c_*)\) and put

\[
\phi_I=\frac1n\sum_{i\in I}\vartheta_i,
\qquad \alpha_i=\phi_I-\vartheta_i,
\qquad
\widetilde q_i(c)=\tau_{\alpha_i}q_i(c),
\quad \widetilde s_i(c)=\tau_{\alpha_i}s_i(c).
\tag{S2}
\]

Define actual parent laws by

\[
Q_I(c)=\bigotimes_{i\in I}\widetilde q_i(c),
\qquad S_I(c)=\bigotimes_{i\in I}\widetilde s_i(c).
\tag{S3}
\]

Every density in (S3) integrates to one. Since the same rotation acts on both sectors of a constituent, its physical relative belief-model orientation is retained. If the local evaluator depends on \(\theta-\varphi\), rotating only one of the sectors would change it; independent sector canonicalization would require a stronger symmetry assumption.

For every contextual pair \(X,Y\in T_c\mathcal C\) and every collective Lie algebra element \(\xi\in\mathbb R\), (S3) satisfies

\[
\begin{aligned}
&g_{Q_I}\bigl(dQ_I X+J_{Q_I}\xi,dQ_I X+J_{Q_I}\xi\bigr)
+g_{S_I}\bigl(dS_I X+J_{S_I}\xi,dS_I X+J_{S_I}\xi\bigr)\\
&=
\sum_{i\in I}\left[
g_{q_i}(dq_i X+J_{q_i}\xi,dq_i X+J_{q_i}\xi)
+g_{s_i}(ds_i X+J_{s_i}\xi,ds_i X+J_{s_i}\xi)
\right].
\end{aligned}
\tag{S4}
\]

The mixed bilinear identities follow by polarization. There is no factor of \(n^{-1}\), and the parent gauge generator is not divided by \(n\).

To prove (S4), hold the section and time fixed while differentiating its evaluation variable. The anchor is a fixed point, so \(X\alpha_i=0\), even if \(c=c_*\). Consequently

\[
X\log\widetilde q_i=\tau_{\alpha_i}(X\log q_i),
\qquad
-\partial_\theta\log\widetilde q_i
=\tau_{\alpha_i}(-\partial_\theta\log q_i).
\tag{S5}
\]

Rotation preserves the measure and thus both score inner products. The product score is the sum of factor scores. Each summand has expectation zero, because its factor is normalized and a rotation preserves normalization. Independence under the declared product laws makes every cross term between different factors zero. The same calculation applies to the model factors. This proves (S4) directly from the densities.

For a scalar gauge generator, write the fine cost as

\[
Q(X,\xi)=B(X,X)+2j(X)\xi+K\xi^2,
\tag{S6}
\]

where \(B\) is the unoptimized product Fisher tensor, \(j(X)=g(dpX,J1)\), and \(K=g(J1,J1)\). Equation (S4) proves equality of \(B,j,K\) before and after retention. On \(K>0\), the unique minimizing form and the contextual tensor are

\[
A(X)=-\frac{j(X)}{K},
\qquad
h(X,Y)=B(X,Y)-\frac{j(X)j(Y)}K.
\tag{S7}
\]

Both agree exactly. Where \(K=0\), both costs have the same null generator and the same entire minimizing affine class, provided the minimum is defined. On a regular patch the connection forms agree as functions of \(c\); their abelian curvatures \(dA\) agree as well. Nonzero first moment at the anchor implies positive rotation inertia there: a zero rotation score would make the density constant in angle and its first moment zero. Positive inertia throughout the chosen contextual patch is imposed or follows by shrinking that patch.

This theorem holds separately at every regular time, even though \(\alpha_i\) varies in time. It concerns derivatives along the contextual base at that time. A state variation that changes the anchor also differentiates \(\alpha_i\); (S5) is then not the relevant formula. This is why the theorem is compatible with genuine loss of positive-Fisher-norm physical state directions.

## Gauge covariance, gluing, and recursive joins

On compatible lifted charts, a passive common gauge transformation satisfies

\[
\vartheta_i'=\vartheta_i+\chi(c_*),
\quad \phi_I'=\phi_I+\chi(c_*),
\quad \alpha_i'=\alpha_i,
\quad (Q_I',S_I')=(\tau_{\chi(c)}Q_I,\tau_{\chi(c)}S_I).
\tag{S8}
\]

The action on the product laws is understood componentwise. Differentiating gives
\(d p'=\tau_\chi(dp+J_p d\chi)\). Together with \(A'=A-d\chi\), this yields \(D^{A'}p'=\tau_\chi D^A p\), as required. The physical canonicalization is therefore compatible with the passive connection transformation on these charts.

There is a global distinction. The total anchor phase is

\[
U_I=\prod_{i\in I}\frac{u_i(c_*)}{|u_i(c_*)|}\in S^1,
\qquad e^{in\phi_I}=U_I.
\tag{S9}
\]

A globally continuous choice of \(e^{i\phi_I}\) as a function of \(U_I\) does not exist for \(n>1\). Indeed, lifting a hypothetical root around one circuit of \(U_I\) changes its angle by \(2\pi/n\), so its start and end disagree. On connected overlaps, two local choices differ by \(2\pi k/n\). Their parent laws differ by the corresponding constant common rotation. These transition rotations obey the cocycle identity because they are differences of local root choices. They give compatible local statistical laws with exactly the same Fisher geometry, rather than one chosen global density on a fixed sample fiber.

The quotient also has a finite isotropy change: the common rotation \(2\pi/n\) is an element of \(H_I\). For fine laws with nonzero first moments it is not a fine-state stabilizer when \(n>1\), but it acts trivially on the global \(H_I\) orbit. The infinitesimal stabilizer is unchanged, which is the part used in (S6)--(S7). Thus the local equality of minimizing connection classes is valid; equality of full global stabilizer groups is false. A global construction must state whether its parent is this bundle of local representatives, an orbifold quotient, or a law with an additional specified lift. Averaging unlabeled root branches is a different statistical experiment and generally loses Fisher information.

Local recursion is exact. If disjoint blocks \(I,J\) were separately canonicalized, rotate all factors of each block by

\[
\delta_I=\phi_{I\cup J}-\phi_I,
\quad \delta_J=\phi_{I\cup J}-\phi_J,
\quad
\phi_{I\cup J}=
\frac{|I|\phi_I+|J|\phi_J}{|I|+|J|}.
\tag{S10}
\]

The total rotation of primitive factor \(i\) becomes \(\phi_{I\cup J}-\vartheta_i\). Thus sequential and direct canonicalization give the same product laws on compatible lifted charts. The count weights are necessary; replacing them by an unweighted average for unequal block sizes would change the retained total phase. The parent common gauge action always rotates every primitive coordinate with unit charge. Treating the retained aggregate angle, which has charge \(|I|\), as a new unit-charge primitive would change \(J\), \(K\), and the minimizing connection.

## Moving representatives and the two metrics

Let \(V\) be the complete fine vector field, and assume its equivariance under physical rotations constant across context. The fixed Haar comparison channels and joint belief-model rotation-invariant evaluator in `parent-closure.md` satisfy this condition. Define \(\omega_i=d\vartheta_i/dt\) at the fixed anchor. Differentiating \(\widetilde q_i=\tau_{\alpha_i}q_i\) yields

\[
\partial_t\widetilde q_i
=V_i^q(\widetilde p)
-(\overline\omega_I-\omega_i)\partial_\theta\widetilde q_i,
\qquad \overline\omega_I=\frac1n\sum_i\omega_i,
\tag{S11}
\]

with the same coefficient for \(\widetilde s_i\). The sign follows from \(\partial_a\tau_a f=-\partial_\theta\tau_a f\). The angular velocities are computable from the retained factors using

\[
\omega_i=\operatorname{Im}\frac{\int e^{i\theta}V_i^q(c_*)d\nu}{u_i(c_*)}.
\tag{S12}
\]

The ratio is invariant under joint rotation. Equivariance and uniqueness of the fine flow therefore define an autonomous original-time quotient flow, and (S11) is its representative equation. It has no missing external orientation variable. For finite \(C^k\) regularity, (S11) is a classical derivative into \(C^{k-1}\); one should not infer a locally Lipschitz \(C^k\) vector field merely from this formula containing \(\partial_\theta\). The fine Banach-space ODE and the induced quotient flow establish existence and uniqueness, without that extra assertion.

The distinction between metrics can be seen on two strictly positive circle location families with fixed Fisher inertias \(I_1,I_2>0\). Their metric is

\[
ds^2=I_1d\vartheta_1^2+I_2d\vartheta_2^2.
\tag{S13}
\]

Quotient by the physical direction \((a,-a)\) and retain \(F=\vartheta_1+\vartheta_2\). Minimizing the squared lift norm under \(v_1+v_2=dF\) gives

\[
v_i=\frac{I_i^{-1}}{I_1^{-1}+I_2^{-1}}dF,
\qquad
ds_{\rm quotient}^2=\frac{dF^2}{I_1^{-1}+I_2^{-1}}.
\tag{S14}
\]

The equal-phase canonical product slice has \(\vartheta_1=\vartheta_2=F/2\), hence

\[
ds_{\rm canonical}^2=\frac{I_1+I_2}{4}dF^2.
\tag{S15}
\]

Their difference is \((I_1-I_2)^2/[4(I_1+I_2)]\) times \(dF^2\). For an invariant potential \(W(F)\), the actual quotient speed is \(-[I_1^{-1}+I_2^{-1}]W'(F)\), whereas the canonical slice's Fisher gradient gives \(-4W'(F)/(I_1+I_2)\). This example proves the metric inequivalence. It is not an assertion that the particular uniform-angle bridge has a nonzero \(W'(F)\). In that bridge all phases are stationary on the product witness. General perturbed profiles still require (S11).

There is no conflict with (S4). Equations (S13)--(S15) compare variations of the retained state and its anchor. Equation (S4) compares evaluation-context derivatives of one retained section whose anchor canonicalization is held fixed.

## Minimal failure of pointwise canonicalization

Let two fixed positive location profiles have phases \(\vartheta_1(c)=c\), \(\vartheta_2(c)=-c\), with positive inertias \(I_1,I_2\). The fine collective cost is

\[
I_1(1+\xi)^2+I_2(-1+\xi)^2,
\qquad h_{cc}=\frac{4I_1I_2}{I_1+I_2}>0.
\tag{S16}
\]

A pointwise quotient retaining only the centered profiles and total phase sees a constant law, so its contextual tensor is zero. The anchored retention (S2) retains the relative phase profiles \(c,-c\) and has exactly (S16). This is a counterexample to omitting those profiles, not to the section-valued construction. The same example can be made in the two-sector setting by rotating each constituent's belief and model together and taking \(I_i\) to be their summed inertia.

## A persistent nonflat contextual family for the finite-time bridge

Now specialize to the later bridge: fixed comparison maps retain the bit and replace the angle by Haar measure, both local references and evaluators are uniform, Gibbs source priors include self loops and are fixed, and all Fisher mobilities are one. In a product density

\[
q_i(z,\theta)=\mu_i(z)f_i(\theta),
\qquad s_i(m,\varphi)=\eta_i(m)g_i(\varphi),
\tag{S17}
\]

the receiver's conditional angular entropy is common to every logit in a row and cancels in that row. The complete angular force has coefficient two: one local entropy and one normalized receiver row. Sender derivatives depend only on the bit marginal. These statements remain true for the self term; the additional marginal derivative contributes no angular variation. Thus the complete centered angular equations are exactly

\[
\partial_t\log f_i=-2\left(\log f_i-\mathbb E_{f_i}\log f_i\right),
\qquad
\partial_t\log g_i=-2\left(\log g_i-\mathbb E_{g_i}\log g_i\right).
\tag{S18}
\]

The bit equations are the independently studied self-loop binary equations. There is no approximation in this product embedding.

Let \(p_k(\theta)=e^{k\cos\theta}/I_0(k)\), where \(I_0(k)=\int e^{k\cos\theta}d\theta/(2\pi)\). Equation (S18) is solved by

\[
f_{i,t}(\theta)=p_{a_tk_i}(\theta-\chi_i),
\qquad g_{i,t}(\varphi)=p_{a_tl_i}(\varphi-\psi_i),
\qquad a_t=e^{-2t}.
\tag{S19}
\]

The phases are fixed; the concentrations remain strictly positive for every finite time if initially positive. Choose the contextual pair \((k,\chi)\) for which each displayed belief factor is \(p_{a_tk}(\theta-\chi)\) and each model factor is \(p_{a_tl}(\varphi)\), with fixed \(l>0\). The bit trajectories are context-independent on this witness. Define the circle rotation inertia

\[
I(k)=\mathbb E_{p_k}[k^2\sin^2\theta]
=k\mathbb E_{p_k}\cos\theta.
\tag{S20}
\]

Integrating the derivative of \(\sin\theta p_k(\theta)\) around the circle proves the equality. For \(k>0\), \(\mathbb E_{p_k}\cos\theta>0\): pair opposite angles to express its numerator as an integral of \(\cos\theta\sinh(k\cos\theta)\), which is positive except on a null set. Differentiating this mean in \(k\) gives \(\operatorname{Var}_{p_k}(\cos\theta)>0\). Hence \(I(k)>0\) and \(I'(k)>0\).

Put \(A_t=I(a_tk)\), \(B_t=I(a_tl)\). Oddness of the rotation score and evenness of the concentration score make them orthogonal. For one primitive pair the common-gauge minimizer and curvature are therefore

\[
\mathcal A_t=-\frac{A_t}{A_t+B_t}d\chi,
\qquad
\mathcal F_t=-\frac{B_t a_t I'(a_tk)}{(A_t+B_t)^2}dk\wedge d\chi,
\tag{S21}
\]

and

\[
h_{\chi\chi,t}=\frac{A_tB_t}{A_t+B_t}>0,
\qquad
h_{kk,t}=a_t^2\operatorname{Var}_{p_{a_tk}}(\cos\theta)>0,
\qquad h_{k\chi,t}=0.
\tag{S22}
\]

The curvature in (S21) is nonzero for every finite \(t\). For \(n\) repeated contextual patterns, both inertias and the tensor multiply by \(n\), while the connection and curvature stay as written. Repetition describes a convenient witness section; it is not imposed on the independently perturbed initial laws. Every nonempty block and its union consequently have nonzero curvature and positive contextual rank on this witness, and the anchored quotient preserves them exactly at each stage.

These are finite-time statements. As \(t\to\infty\), the circle laws approach Haar and their rotation inertia vanishes. No uniform positive geometry bound on an infinite time interval is claimed.

## Full open neighborhoods and event anchoring

Fix a finite horizon \(T\), a compact contextual rectangle \(k\in[k_-,k_+]\) with \(k_->0\), and a compact phase chart. Along the displayed witness all densities have a positive lower bound, all anchor first moments have a positive lower bound, and the two eigenvalues in (S22) and the absolute curvature coefficient in (S21) have positive lower bounds on \([0,T]\). This follows from continuity and compactness and the strict formulas above.

Take a normalized \(C^k\) chart of all primitive densities on the compact product of contextual patch and sample space, with enough mixed derivatives for the scores and curvature, for example \(k\ge3\). On a neighborhood bounded away from zero, the complete fine field uses smooth logarithms, marginals, positive ratios, and finite Gibbs normalizations. It is locally Lipschitz in this chart. A finite cover of the compact witness trajectory gives a common neighborhood of initial sections whose solutions exist on \([0,T]\) and stay close in this norm. Equivalently, on a common bounded neighborhood a Lipschitz constant \(L\) gives a difference bound \(e^{LT}\) times the initial difference.

Moment phases on the chosen chart, Fisher costs, (S7), and their contextual derivatives are continuous under these bounds. A sufficiently small open neighborhood therefore preserves nonzero moments, the local phase chart, positive contextual rank, and nonzero curvature throughout the finite interval. The neighborhood admits independent variations of all belief/model densities and arbitrary sufficiently small bit-angle correlations. It is not restricted to the product witness, equal shapes, or equal scores. If the separate clique result supplies strict finite-time routing margins and regular event windows for this same architecture, the same finite-horizon continuity argument preserves those margins after taking the intersection of the open neighborhoods.

One can also state this openness directly in the independent law values at the anchor, without treating an entire contextual section as the initial variable. Let \(x=(q_i,s_i)_i\) range over a full open neighborhood of the product witness at \(c_*=(k_*,0)\), and let \(\vartheta_i(x)=\arg\mathbb E_{q_i}e^{i\theta}\). Assign the following regular contextual family through every such \(x\):

\[
q_{i,x}(k,\chi)
=\tau_\chi\left[
\frac{e^{(k-k_*)\cos(\theta-\vartheta_i(x))}q_i(z,\theta)}
{\int e^{(k-k_*)\cos(\theta-\vartheta_i(x))}q_i(z,\theta)d\nu}
\right],
\qquad s_{i,x}(k,\chi)=s_i.
\tag{S23}
\]

At the anchor this equals \(x\), and at the product witness it is the family used in (S19)--(S22). It is smooth in all independent law coordinates on the nonzero-moment chart. It is also physically equivariant: replacing \((q_i,s_i)\) by \((\tau_{a_i}q_i,\tau_{a_i}s_i)\) changes \(\vartheta_i(x)\) by \(a_i\), so the whole section (S23) is rotated by that same constant \(a_i\). Thus this choice of contextual family does not encode the discarded orientation in a fixed external template. Evolve these sections by the original fine field. Their continuous dependence gives the asserted geometry on a full open set of anchor law values, while exact equivariance preserves the continuous \(H_I\) fibers of the retained section. Equation (S23) chooses the contextual jets on which geometry is asserted; it imposes no factorization or common-parameter restriction on the law values themselves.

Use one state-selected partition for the whole contextual patch, selected by native rows at the fixed anchor \(c_*\). Its event time \(\tau\) is a function of that anchored trajectory, and each section is handed off on the common absolute-time slice \(t=\tau\). Thus the derivative with respect to evaluation context is \(d_c p_\tau\), and (S4) applies. Varying the initial section can vary \(\tau\), but that is a variation of state, not the contextual derivative used in the theorem.

If a different protocol instead selects a separate event time \(\tau(c)\) at each evaluation context, the relevant derivative is

\[
d_c[p_{\tau(c)}(c)]X
=(d_cp_tX)_{t=\tau(c)}+V(p_{\tau(c)}(c))X\tau.
\tag{S24}
\]

Neither the vanishing of the extra score nor invariance of the resulting tensor follows from (S4). Such a protocol requires the event-pullback calculation in `geometry.md`. It is not the anchored protocol used here.

## Supported conclusion and remaining obligation

The actual product-law realization, its gauge transformation, its recursive composition, its moving representative equation, and its equality of contextual minimizing Fisher costs are established on regular lifted charts. The uniform-angle finite-time bridge has an explicit two-dimensional contextual family with positive tensor and nonzero curvature throughout every finite observation interval, and these properties persist on full open neighborhoods of smooth initial sections.

The remaining joint obligation is to combine this neighborhood with the same architecture's independently proved strict two-stage native-routing event construction, using the fixed-anchor selector and inherited primitive interaction sums. One must also keep the predeclared response protocol and event memory invariant under the discarded physical rotations, as analyzed in `parent-closure.md`. A claim of one global representative law, a canonical-slice Fisher-gradient parent update, pointwise phase centering, or independently timed contextual events would require additional work and is not supplied by this result.

No numerical experiment, symbolic script, GPU computation, or Lean work was run. The evidence is the explicit calculations above. Research-vault files were consulted without edits.
