<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e","schema_version":"rigorous-theory-search/v1","target_digest":"cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e"} -->
# Public Wishart compression with exact dynamics and curved collective geometry

Date: October 22, 2026. Second bounded constructive round, requested by the parent investigator. This supplements `routes/geometry.md`; it does not replace the frozen target or the earlier artifact.

## Result and its limits

There is a smooth, genuinely lossy, associative public parent construction for four or more distinct children under the original two-sector unit-Fisher KL flow. Both sectors carry non-Gaussian matrix laws. The parent forgets each child's individual shape parameter and retains their sum. A fixed sample-sum channel realizes that compression. The ordinary same-time parent Fisher gradient, all declared joint sum-response histories, and the nontrivial collective connection and contextual residual tensor are inherited exactly. The connection has nonzero curvature and the residual tensor has rank two for every finite time in the explicit section below.

This is an invariant-family existence witness, not endogenous formation. Common precision matrices and context-constant shapes are preparation assumptions. Every block can be compressed from time zero; nothing here selects membership or makes a previously unavailable quotient appear later. Original communication channels are constant reference-output channels, so the model has no dynamical peer coupling. These qualifications cannot be omitted when using this result against the frozen target.

The construction uses the original potential from `03_dynamics.tex`, the full-density Fisher equation there, and the collective connection and fixed-channel score formulas from `02_geometry.tex`. The normalization, convolution, flow, and curvature calculations are supplied below, without an external theorem about Wishart laws or Gaussian sampling.

## Typed dictionary and actions

| Object | Definition |
|---|---|
| Context | \(\mathcal C=(a_-,a_+)\times(-\chi_0,\chi_0)\), with \(0<a_-<a_+\). Context coordinates are \((a,\chi)\). |
| Represented samples | \(X_i,Y_i\in\mathrm{Sym}_2^+\), independent between agents and sectors under the declared product law. These matrices are not context coordinates. |
| Fine law configuration | \(q_i=W_{\alpha_i,P}\), \(s_i=W_{\beta_i,Q}\), with \(\alpha_i,\beta_i>1/2\), \(P,Q\in\mathrm{Sym}_2^+\), common \(P,Q\) across children. |
| Structure group | \(G=SO(2)\), with a left action on matrices \(X\mapsto gXg^T\), and the corresponding pushforward on laws. |
| Parameter action | \(\alpha\mapsto\alpha\), \(P\mapsto gPg^T\). |
| Principal bundle | The explicit construction uses \(\mathcal C\times SO(2)\), with ordinary right principal action and the associated left sample representation. |
| Lie algebra | \(\xi\Omega\), \(\Omega=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\). Thus \(J_P\xi=\xi[\Omega,P]\). |
| Statistical metric | Fisher metric of the product of the declared fine laws; coarse metric is the ordinary Fisher metric of the retained sum laws, with no extra reweighting. |
| Retention | \(C_I((X_i,Y_i)_{i\in I})=(\sum_iX_i,\sum_iY_i)\), a fixed deterministic normalized Markov kernel. |
| Configuration map | \(R_I((\alpha_i,\beta_i)_{i\in I},P,Q)=(A_I=\sum_i\alpha_i,B_I=\sum_i\beta_i,P,Q,n_I=|I|)\). |
| Connection convention | \(D^Ap=dp+J_pA\), \(A'=\operatorname{Ad}_gA-(dg)g^{-1}\). |
| Transport | Horizontal transport along a path rotates samples by the solution of \(\dot g g^{-1}=-A(\dot c)\); in this abelian case the angle is \(-\int A\). |

A general invertible congruence \(X\mapsto gXg^T\) sends \(P\) to \(g^{-T}Pg^{-1}\) and preserves Fisher information and KL only when the law and reference are carried together. The fixed identity-precision references below have orthogonal symmetry. Their fixed-model symmetry is not all of \(GL(2)\). The symmetry used for the collective connection is the common \(SO(2)\) action above.

The matrices \(P,Q\) are distribution parameters. No affine-invariant SPD metric, SPD exponential map, or Euclidean surrogate for such an operation is invoked. Every metric below is derived from the sample-law Fisher score.

## Normalization and public convolution

For \(\alpha>1/2\), define a probability density relative to Lebesgue measure \(dX=dx_{11}dx_{12}dx_{22}\) on \(\mathrm{Sym}_2^+\) by

\[
W_{\alpha,P}(dX)
=\frac{(\det P)^\alpha}{\Gamma_2(\alpha)}
(\det X)^{\alpha-3/2}e^{-\operatorname{tr}(PX)}dX,
\qquad
\Gamma_2(\alpha)=\sqrt\pi\Gamma(\alpha)\Gamma(\alpha-1/2).
\tag{1}
\]

To verify the normalizer at \(P=I\), parameterize

\[
x_{11}=t>0,\qquad x_{12}=\sqrt t u,
\qquad x_{22}=v+u^2,\quad v>0,\ u\in\mathbb R.
\]

Then \(\det X=tv\), \(\operatorname{tr}X=t+v+u^2\), and the Jacobian is \(\sqrt t\). The integral factors as
\(\Gamma(\alpha)\Gamma(\alpha-1/2)\sqrt\pi\), finite precisely for the stated range. For general \(P\), substitute \(X=P^{-1/2}ZP^{-1/2}\). Congruence by a matrix \(B\) has absolute Jacobian \(|\det B|^3\) on symmetric two-by-two matrices: for diagonal \(B\), the three coordinate factors are \(b_1^2,b_1b_2,b_2^2\); orthogonal diagonalization supplies the general positive case. Combining this Jacobian with the determinant power gives the multiplier \((\det P)^{-\alpha}\), proving (1).

For independent \(X\sim W_{\alpha,P}\) and \(Y\sim W_{\beta,P}\), their sum density at \(S>0\) is proportional to

\[
e^{-\operatorname{tr}(PS)}
\int_{0<X<S}(\det X)^{\alpha-3/2}
(\det(S-X))^{\beta-3/2}dX.
\]

Substitute \(X=S^{1/2}US^{1/2}\). The integral becomes a constant independent of \(S\), times \((\det S)^{\alpha+\beta-3/2}\). The constant is positive. Tonelli's theorem and normalization of the input convolution show it is finite; normalization of (1) then determines the output constant. Therefore

\[
X+Y\sim W_{\alpha+\beta,P}.
\tag{2}
\]

Induction proves the arbitrary finite-block formula. This argument does not require integer or half-integer shape, a Gaussian representation, or a Laplace-transform uniqueness theorem.

The shape-sum map has positive-dimensional fibers. For example, \((\alpha_1,\alpha_2)=(1,3)\) and \((3/2,5/2)\) have the same retained shape four, but their child laws differ and are not related by a child permutation. The model-sector shapes can be varied independently in the same way. Thus the configuration loss is genuine and smooth.

## Original potential and exact same-time flow

Fix \(\alpha_0,\beta_0>1/2\). For every child choose the proper reference

\[
r_i=W_{\beta_0,I},\qquad
G_i(m,dk)=W_{\alpha_0,I}(dk).
\]

The evaluator is normalized and independent of the model sample. Thus \(R_i=r_iG_i\) is the product of these two proper references. For every allowed directed distinct-agent edge choose

\[
\mathcal K_{ij}^q(x,dk)=W_{\alpha_0,I}(dk),
\qquad
\mathcal K_{ij}^s(y,dm)=W_{\beta_0,I}(dm).
\tag{3}
\]

These are fixed normalized kernels, with no state-dependent gate. They do not carry source information. Use all other agents as sources, positive uniform priors, and arbitrary original \(T_q,T_s>0\). Rows start at their priors. Every source in a given row has the same cost, so rows remain at their priors. The Gibbs-reduced system has the same matter equation. The exact original energy is

\[
\mathcal E=2\sum_i\left[
\mathrm{KL}(q_i\Vert W_{\alpha_0,I})
+\mathrm{KL}(s_i\Vert W_{\beta_0,I})\right].
\tag{4}
\]

There are no hidden incoming derivatives: when varying a sender law, \((dq_j)\mathcal K_{ij}=0\) because the kernel is constant and \(dq_j\) has total mass zero. Channel derivatives vanish identically. Receiver derivatives give the second copy of each local KL in (4).

For any positive normalized density \(q\) relative to its fixed reference \(q_*\), the full unit-Fisher equation generated by \(2\mathrm{KL}(q\Vert q_*)\) is

\[
\partial_t\log(q/q_*)=-2\left[\log(q/q_*)-\mathbb E_q\log(q/q_*)\right].
\]

Its exact solution is \(q_t\propto q_0^{s}q_*^{1-s}\), with \(s=e^{-2t}\). Substitution of (1) therefore proves full-density invariance, with

\[
\alpha_i(t)=\alpha_0+s(\alpha_i(0)-\alpha_0),
\quad P(t)=I+s(P(0)-I),
\]

\[
\beta_i(t)=\beta_0+s(\beta_i(0)-\beta_0),
\quad Q(t)=I+s(Q(0)-I).
\tag{5}
\]

This is the actual unrestricted-density Fisher field on the family; no projected finite-dimensional flow is substituted. The coefficient two comes from (4), so the original time is preserved.

All shapes remain above \(1/2\), and both precision matrices remain SPD for every finite time and converge to \(I\). On compact initial parameter sets inside this domain, shapes and precision eigenvalues stay in a common regular compact domain. Differentiation under integrals is justified by slightly enlarging the compact parameter domain: logarithmic determinant powers at the boundary remain integrable, and the strictly positive lower precision bound controls all polynomial tails. The explicit normalizer proves finite KL, square-integrable scores, and smooth parameter derivatives. Thus the paths are regular and global. The shapes and precisions in (5) have unique solutions. Distinct initial shapes remain distinct at every finite time, since their differences multiply by \(s>0\).

For a block \(I\), (2) gives parent laws

\[
q_I=W_{A_I,P},\qquad s_I=W_{B_I,Q},
\quad A_I=\sum_{i\in I}\alpha_i,
\quad B_I=\sum_{i\in I}\beta_i.
\]

Their equations are exactly

\[
\dot A_I=-2(A_I-n_I\alpha_0),\quad
\dot B_I=-2(B_I-n_I\beta_0),\quad
\dot P=-2(P-I),\quad\dot Q=-2(Q-I).
\tag{6}
\]

These are also the unrestricted Fisher equations of

\[
\mathcal E_I^c=2\left[
\mathrm{KL}(q_I\Vert W_{n_I\alpha_0,I})
+\mathrm{KL}(s_I\Vert W_{n_I\beta_0,I})\right],
\tag{7}
\]

by the same normalized-power calculation. The coarse reference laws are themselves exactly the sums of the fine reference samples. Explicit normalized parent data are \(r_I=W_{n_I\beta_0,I}\), \(G_I(m,dk)=W_{n_I\alpha_0,I}(dk)\), and constant parent peer channels returning the corresponding receiver reference. With independent fresh draws across receiver children, summing the original outputs in (3) gives exactly these parent outputs by (2). Thus the evaluator and communication maps, as well as the law and equation, are supplied. Equality of fine and coarse scalar energies is neither true nor needed: (5)-(7) prove the original-time vector-field square directly. The conditional information discarded by summation has its own energy, but it does not enter the retained velocity on this admitted class.

## Fisher geometry retained by the fixed sum channel

For a precision variation \(U\in\mathrm{Sym}_2\), differentiating the log density gives

\[
\ell_U(X)=\alpha\operatorname{tr}(P^{-1}U)-\operatorname{tr}(UX).
\tag{8}
\]

Differentiating normalization first gives \(\mathbb EX=\alpha P^{-1}\). Differentiating twice, or differentiating that first identity in a second precision direction, gives

\[
g^F_{\alpha,P}(U,V)
=\alpha\operatorname{tr}(P^{-1}UP^{-1}V).
\tag{9}
\]

The full family also has shape scores; (9) is the precision block used by this contextual section, not an assertion that precision and shape scores are always orthogonal.

Assume each \(\alpha_i,\beta_i\) is constant over the context base, while \(P(c),Q(c)\) may vary. Then the fine collective public score for \((U,V)\) is

\[
A_I\operatorname{tr}(P^{-1}U)-\operatorname{tr}(US_X)
+B_I\operatorname{tr}(Q^{-1}V)-\operatorname{tr}(VS_Y),
\tag{10}
\]

where \(S_X=\sum_iX_i\), \(S_Y=\sum_iY_i\). This is precisely the parent score. Both contextual and common conjugation-orbit scores are measurable from the fixed retained sums. Consequently their Fisher loss is zero, including every mixed contextual-orbit pairing. Equivalently, summing (9) gives exactly the parent precision metric with coefficients \(A_I,B_I\).

The fine infinitesimal stabilizer consists of the rotations commuting with both \(P,Q\). Because every shape is strictly positive, the same condition gives the parent infinitesimal stabilizer. Hence \(\ker J=\ker\bar J\). The exact mixed-loss condition \(\Delta(r_X,J\xi)=0\) and the stabilizer criterion are both satisfied. The complete minimizing connection classes agree, and their residual tensors agree. A claim of mere Fisher contraction would have been weaker; equations (8)-(10) establish score equality in every direction used here.

The family of all child shape allocations is not discarded without Fisher loss. The loss is confined away from the declared contextual and orbit directions. This is exactly the restriction identified by the obstruction in `geometry.md`.

## Explicit nonzero curvature for every finite time

At initial time set

\[
P(a,\chi)=R_\chi\begin{pmatrix}e^a&0\\0&e^{-a}\end{pmatrix}R_\chi^T,
\qquad
Q=\begin{pmatrix}e^b&0\\0&e^{-b}\end{pmatrix},
\quad b>0.
\tag{11}
\]

Let \(A=\sum_i\alpha_i\), \(B=\sum_i\beta_i\), both positive constants on the context. At a diagonal precision with eigenvalues \(p_1,p_2\), the orbit tangent is

\[
[\Omega,P]=\begin{pmatrix}0&p_1-p_2\\p_1-p_2&0\end{pmatrix},
\]

and (9) gives locked inertia \(2A(p_1-p_2)^2/(p_1p_2)\). Radial and orbit directions are orthogonal since their matrices are diagonal and off-diagonal respectively. Thus

\[
k_1(a)=8A\sinh^2a,\qquad k_2=8B\sinh^2b>0.
\]

The collective normal equation gives

\[
\mathcal A^F=-\frac{k_1}{k_1+k_2}d\chi,
\qquad
h^{\min}=2A da^2+\frac{k_1k_2}{k_1+k_2}d\chi^2,
\tag{12}
\]

and

\[
\mathcal F=d\mathcal A^F
=-\frac{k_1'(a)k_2}{(k_1+k_2)^2}da\wedge d\chi\ne0.
\tag{13}
\]

These are the fine and parent values simultaneously.

The statement persists for every finite time, not just at the initial jet. Put \(s=e^{-2t}>0\) and

\[
u=1+s(e^a-1),\qquad v=1+s(e^{-a}-1),
\]

with the analogous fixed-context eigenvalues for \(Q(t)\). Replace \(A,B\) by their positive totals from (6). Then

\[
k_1(a,t)=\frac{2A(t)(u-v)^2}{uv}
=\frac{8A(t)s^2\sinh^2a}{1+2s(1-s)(\cosh a-1)},
\tag{14}
\]

and \(k_2(t)>0\) is independent of context. The radial coefficient becomes

\[
A(t)s^2\left[\frac{e^{2a}}{u^2}+\frac{e^{-2a}}{v^2}\right]>0.
\]

The forms (12)-(13) hold with those replacements. To verify \(\partial_ak_1>0\), write \(D=1+2s(1-s)(\cosh a-1)\), \(c=s(1-s)\). Up to positive factors its derivative has numerator

\[
2\cosh a D-2c\sinh^2a
=2(1-2c)\cosh a+2c(\cosh^2a+1)>0,
\]

since \(0\le c\le1/4\). Thus curvature is nonzero and the contextual tensor has rank two at every finite time. At \(t\to\infty\), both precisions approach identity, orbit rank drops, and the residual tensor tends to zero. No smooth unique minimizing connection at that limiting isotropic stratum is inferred from the finite-time formulas.

Under a passive frame rotation by \(\vartheta(c)\), both public precision angles gain \(\vartheta\). Their total momentum one-form gains \((k_1+k_2)d\vartheta\). Therefore \(\mathcal A'=\mathcal A-d\vartheta\), exactly the required affine law. The covariant score transforms by pushforward, and the Fisher metric is invariant. A nonzero (13) gives path-dependent rotation holonomy on the otherwise trivial bundle. No identification of this transport with endpoint frame ratios is made. On multiple patches, the same formulas glue when the prescribed transition functions satisfy their cocycle; the witness supplies no nontrivial topology or emergent transition data.

## Normalized response histories and associative joining

Declare the response/control class as follows. At each record time, choose a block \(I\) and any normalized kernel \(L_a(do\mid S_X,S_Y)\). Draw fresh independent samples from the fine product recognition laws, sum them, and apply that kernel. Controls select record times, blocks, and readout kernels from previous records; they do not reset fine laws or alter the reference potential. The identity sum readout is included and is nonconstant in \(A_I,B_I,P,Q\). Its law is precisely \(q_I\otimes s_I\).

The parent law therefore gives every joint one-step record kernel, not merely separate marginal outputs. Equations (5)-(6) give equality of subsequent states at the original times. Induction gives equality of every finite joint admitted history under adaptive readout selection. A repeated hidden fine sample, arbitrary child identity readout, Bayesian fine-state resetting, or a reference-changing control is a different protocol and is not covered. This response class is fixed here before preservation is asserted; no failed protocol is removed later.

For disjoint blocks with common precisions, joining is

\[
(n_I,A_I,B_I,P,Q)\star(n_J,A_J,B_J,P,Q)
=(n_I+n_J,A_I+A_J,B_I+B_J,P,Q).
\tag{15}
\]

At sample level it sums the two retained matrices in each sector; at law level it convolves. Equation (2) proves this operation, and associativity of addition proves exact associativity. Equation (6) commutes with (15). The parent references also join because shapes \(n_I\alpha_0,n_J\alpha_0\) add to \((n_I+n_J)\alpha_0\). Fisher score equality applies again to the common precision directions at every joining stage. Each stage may discard actual public shape-allocation information, including information retained by its two children. Thus this construction improves on the first route's public-tuple concatenation.

For example four distinct shape pairs may be joined into two parents and then their parent. Both joins are lossy over the admitted preparation class. However the pairs in that sentence are an illustrative choice of regrouping, not a selected hierarchy. The same algebra permits every disjoint regrouping from the start.

## Minimal failure and the unresolved formation mechanism

Permit a context direction with \(d\beta_1=1\), \(d\beta_2=-1\), all belief shapes and both precisions fixed. The retained model-shape sum has zero derivative. The fine score is the centered difference \(\log\det Y_1-\log\det Y_2\), with strictly positive variance. It is orthogonal to common rotation scores, because determinant is invariant under conjugation: differentiation of its expectation along the orbit is zero. Hence this direction has positive fine minimized residual length and zero parent length. Exact geometric inheritance fails as soon as discarded shape allocations vary contextually. This is an explicit failure test, not a hypothetical concern.

The same model-shape variation between preparations, held constant over the context, certifies real loss even if membership events and their times are retained. Suppose a separate event selector reads only the belief shapes \(\alpha_i\). Prepare \((\beta_1,\beta_2)\) and \((\beta_1+\delta,\beta_2-\delta)\), with \(\delta\ne0\) small enough to keep both above \(1/2\), all belief data fixed. The event history and the parent model shape are identical, while the fine model laws differ. At every later finite time the shape difference is \(e^{-2t}(\delta,-\delta)\), still nonzero, and the retained model total remains equal. Thus a birth time that might reveal a belief-shape gap cannot recover this independent model allocation. At a second join, the analogous perturbation transfers model total between the two first parents while keeping the final total fixed. This conclusion is conditional on the selector not consulting those model allocations or adding records that identify them.

Common precision is also load-bearing. If children have different \(P_i\), their sum density generally need not have form (1), and contextual precision scores need not be measurable from the total matrix. Neither closure nor geometry is claimed in that case. The original independent relaxation does not make unequal precision parameters become exactly equal at a finite time, since their differences are multiplied by \(e^{-2t}\).

The strongest result is an exact smooth public compression with associative repeated loss, original two-sector dynamics, full declared response histories, and curved retained geometry for every finite time on an explicit invariant preparation class. Endogenous selection remains open: the system is reducible under every grouping already at time zero, the channels in (3) have no peer dependence, and the flow creates no choice of persistent membership. A selector based on shape thresholds could assign time-dependent labels, but additional reasoning would be needed to show why that convention constitutes formation rather than a chosen description. This artifact supplies the geometric and dynamical witness needed to test such a separate mechanism; it does not supply that mechanism.

No computation, experiment, GPU operation, external literature query, or formal proof assistant was used. Only analytical derivations and source reads were performed.
