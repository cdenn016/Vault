## Verdict

**Yes. Under the established inputs, the construction gives a well-defined, own-law parent activated from the exact conditioned retained law, with vanishing discarded information and vanishing retained-path error on the proposed growing time interval.** No additional path-space entropy hypothesis, pointwise hazard bound, or frozen-row approximation is needed.

There are two important scope qualifications:

1. The entropy estimate at later times concerns the **conditioned native law**, not automatically the independently evolving parent law.
2. Retaining evaluator samples is valid for the **joint-law physical comparison**. The specified parent dynamics is on \((S,y)\); persistent dynamics for evaluator samples has not been specified.

Below, \(\varepsilon=\varepsilon_L\) and TV means \(\sup_A|P(A)-Q(A)|\). The held-matching OU is only a comparison process: neither the native process nor the parent has its assignments externally held.

## 1. Precise conclusion

Write
\[
R_t=\mathcal L(X_t,S_t\mid E),\qquad
E=E_M(T^{1/4},1),\qquad \theta=s+1,
\]
and let
\[
r=\mathbb P(E^c)\le \rho:=3\delta+b(T,T^{1/4},1).
\]
Take sufficiently small \(T\) that \(\rho<1/2\), and set
\[
h=T^{-1/4},\qquad d=\delta+\varepsilon h<1/4,
\qquad K_T=\frac{\eta+h_b(\rho)}{1-\rho}.
\]
We also require \(\theta+h\le2s\), which follows from the stated schedules for small \(T\).

Let \(\mathsf Q_C^h\) be the parent path law, initialized **exactly** at \(C_\#R_\theta\), with inherited rows \(p(\theta)\) and its own source-learning equation. Let \(\mathsf Q_E^h\) be the law of the retained native path on \([\theta,\theta+h]\), conditional on \(E\). Then
\[
\boxed{
\operatorname{TV}(\mathsf Q_C^h,\mathsf Q_E^h)
\le
2\rho+(h+3)\delta+\frac{4hd}{1-4d}.
}
\tag{1}
\]

For the outer optimizer discarded conditional KL, denoted \(\mathcal D_{\rm opt}\), and the physical discarded conditional KL **with both evaluator samples retained**, denoted \(\mathcal D_{\rm phys}\),
\[
\boxed{
\sup_{\theta\le t\le2s}\mathcal D_{\rm opt}(R_t)\le K_T,
\qquad
\sup_{\theta\le t\le2s}\mathcal D_{\rm phys}(R_t)\le K_T+T.
}
\tag{2}
\]
These are averaged conditional-KL statements, not uniform fiberwise bounds. They apply along the supplied common schedules, for the supplied almost-everywhere set of base points. No stabilization of the selected matching as \(T\to0\) is required.

## 2. The parent is well-defined, including its own-law learning

### State space, normalization and continuous dynamics

Use the finite disjoint union
\[
\mathcal Y=\bigsqcup_{S\in\{-,+\}^4}\{S\}\times W_S.
\]
The two matching strata have dimension nine; the other fourteen have dimension twelve. On each stratum put
\[
B_S=P_{W_S}A_S|_{W_S},
\qquad
L_Sf=-\langle B_Sy,\nabla f\rangle+T\Delta_{W_S}f.
\]
For matching strata, invariance of \(W_S\) makes this precisely the projected OU. Elsewhere it is the original OU. Since \(A_S\succeq TI\), also \(B_S\succeq TI\).

The displayed \(J_p\) is a measurable probability kernel: the source lift is a probability kernel, the posterior assignment weights sum to one, and the final operation is the **target** projection. In particular,
\[
S'=S\quad\Longrightarrow\quad P_{W_S}x=y.
\]
Thus self-proposals do not move the retained state. A single rate-one clock is exactly the appropriate construction.

All reference laws must be pushed forward as normalized measures. For example, with
\[
Z_S(T)=\int e^{-x^TA_Sx/(2T)}\,dx,
\qquad Z_p=\sum_S\pi_p(S)Z_S(T),
\]
we have \(\mu_p(S)=\pi_p(S)Z_S/Z_p\). On a matching stratum, integrating the hidden coordinates contributes the factor
\[
\zeta_Z(T)=\frac{(2\pi T)^{3/2}}
{(4+5T)\sqrt{8+T}}
\]
to the density on \(W_S\). **This factor cannot be dropped when comparing different-dimensional strata.** Defining the parent optimizer reference as \(C_\#\mu_p\) retains it automatically. The physical law has its own normalization and hidden integral.

### Nonexplosion and moments

For a prescribed continuous row path in the open cube, construct the process between successive rate-one Poisson times using the appropriate linear OU, and apply \(J_p\) at each proposal. There are finitely many proposals on every finite interval; every Gaussian lift is finite almost surely. Variable dimension creates no explosion.

There is also a direct moment bound. A source lift has \(x=y+z\), with \(z\perp y\), and every target projection satisfies
\[
|P_{W_{S'}}x|^2\le |y|^2+|z|^2.
\]
On matching strata,
\[
\mathbb E|z|^2
=\frac{T}{8+T}+\frac{2T}{4+5T}\le\frac{5T}{8};
\]
elsewhere it is zero. Hence the parent generator satisfies
\[
\mathcal L_p|y|^2
\le-2T|y|^2+24T+\frac{5T}{8}.
\tag{3}
\]
The inherited conditioned initial law has finite second moment: the native second moment is finite, and conditioning on a positive-probability event increases its bound by at most \(1/\mathbb P(E)\).

### Closing the deterministic own-law equation

This part does require a proof, but the given model supplies the necessary regularity.

The native rows are strictly interior at every finite time. Variation of constants gives
\[
p_i(t)\ge\tfrac12e^{-\varepsilon t},
\qquad 1-p_i(t)\ge\tfrac12e^{-\varepsilon t}.
\]
Starting from the inherited rows, any parent solution similarly obeys
\[
\min\{p_i^C(u),1-p_i^C(u)\}
\ge e^{-\varepsilon u}
\min\{p_i(\theta),1-p_i(\theta)\}>0,
\tag{4}
\]
where parent time \(u\) starts at zero.

On a compact cube \([a,1-a]^4\), posterior dependence on the rows is uniformly Lipschitz, **even uniformly in the unbounded state \(x\)**. If \(b_i(x,p_i)\) is a posterior Bernoulli probability, then
\[
\partial_{p_i}b_i
=\frac{b_i(1-b_i)}{p_i(1-p_i)},
\qquad
|\partial_{p_i}b_i|\le\frac1{4a(1-a)}.
\]
The product-posterior coupling bound and integration against the row-independent source lift therefore give
\[
\sup_{S,y}\operatorname{TV}
\bigl(J_p((S,y),\cdot),J_{\tilde p}((S,y),\cdot)\bigr)
\le L_a\|p-\tilde p\|_1,
\quad L_a=\frac1{4a(1-a)}.
\tag{5}
\]
For prescribed row paths with the same initial state law, common-clock coupling yields
\[
\operatorname{TV}(Q^p_{[0,u]},Q^{\tilde p}_{[0,u]})
\le L_a\int_0^u\|p(v)-\tilde p(v)\|_1\,dv.
\tag{6}
\]
Now apply a fixed point argument to
\[
\Phi[p]_i(u)=e^{-\varepsilon u}p_i(\theta)
+\varepsilon\int_0^u e^{-\varepsilon(u-v)}
Q_v^p(S_i=+)\,dv.
\]
On a sufficiently short interval of length \(H\), (6) gives sup-norm contraction constant at most \(2\varepsilon L_aH^2\). Formula (4) supplies a positive compact-cube margin on every prescribed finite horizon, so this construction continues over that horizon.

Consequently there is a **unique deterministic own-law row path and associated parent process law**, nonexplosive on all finite intervals. No externally specified fine-row path, uniform-in-\(T\) Lipschitz constant, or further regularity assumption is needed.

## 3. Entropy conditioning works for a past-prefix event

Let \(U_t=(X_t,S_t)\), \(B=1_E\), and \(\alpha=\mathbb P(E)=1-r\). Write \(R_t^0=\mathcal L(U_t\mid E^c)\). The exact identity is
\[
\alpha D(R_t\|\mu_{p(t)})
+(1-\alpha)D(R_t^0\|\mu_{p(t)})
=D(q_t\|\mu_{p(t)})+I(B;U_t).
\tag{7}
\]
It follows by computing the relative entropy of the joint law of \((B,U_t)\) against \(\mathcal L(B)\otimes\mu_{p(t)}\) in two orders.

**Nothing in (7) requires \(E\) to be measurable from the endpoint.** It can be any event on the underlying probability space. In particular, no path-space entropy estimate is needed here. Since \(I(B;U_t)\le h_b(r)\),
\[
D(R_t\|\mu_{p(t)})
\le\frac{\eta+h_b(r)}{1-r}
\le K_T,
\qquad \theta\le t\le2s.
\tag{8}
\]
The last replacement uses \(r\le\rho<1/2\).

Disintegrating over \(Y=C(U_t)\),
\[
D(R_t\|\mu_{p(t)})
=D(C_\#R_t\|C_\#\mu_{p(t)})
+\underbrace{\int D(R_t(dx\mid S,y)\|\kappa_S(dx\mid y))
\,C_\#R_t(dS,dy)}_{\mathcal D_{\rm opt}(R_t)}.
\tag{9}
\]
This proves the first bound in (2).

Because \(\kappa_S\) is row-independent on matching strata and is the identity conditional elsewhere, this discarded term is unchanged if the reference rows are replaced by \(p^C\). That does **not** imply
\(D(R_t\|\mu_{p^C(t)})\le K_T\): the retained marginal reference can change.

Past-prefix measurability has a different role: it ensures that after \(\theta\), the conditional native process has its original future transition mechanism, started from \(R_\theta\), rather than a future-conditioned transition mechanism.

## 4. The physical comparison really can retain both evaluator samples

Here is a direct verification that does not silently condition the hidden Gaussian incorrectly.

Fix a matching stratum and retained value \(y\). Write \(x=y+z\), using the stated orthonormal hidden coordinates \(z=(z_0,z_1,z_2)\). Put \(D=D_{\rm ev}\). The supplied normals give
\[
\|Dz\|^2=2(z_1^2+z_2^2),\qquad
\langle Dy,Dz\rangle=0.
\tag{10}
\]
Let \(g_0\) be the physical outer hidden conditional and \(g\) the optimizer hidden conditional. Their precision matrices give exactly
\[
g(dz)=\frac{e^{-\|Dz\|^2}g_0(dz)}{Z_Z},
\qquad
Z_Z=\frac{4+T}{4+5T}.
\tag{11}
\]
Thus, for any actual conditional hidden law \(R_y\),
\[
D(R_y\|g_0)+\mathbb E_{R_y}\|Dz\|^2
=D(R_y\|g)+c_T,
\quad c_T=\log\frac{4+5T}{4+T}.
\tag{12}
\]

Use evaluator coordinates
\(e=(m_{\rm ev},v_{\rm ev})\), where
\(v_{\rm ev}=k_{\rm ev}-m_{\rm ev}\); this is an invertible change of the retained samples. Let \(K\) and \(L\) be the stated recognition and physical evaluator kernels. With their specified conditional Gaussian sampling,
\[
D(K(\cdot\mid x)\|L(\cdot\mid x))=\|Dx\|^2.
\]
Form the two conditional joint laws
\[
\mathcal R_y(dz,de)=R_y(dz)K(de\mid y+z),
\qquad
\mathcal P_y(dz,de)=g_0(dz)L(de\mid y+z).
\]
The physical discarded KL at this retained \(y\), **after retaining all of \(e\)**, is
\[
\ell_{\rm phys}(y)
=D(\mathcal R_y\|\mathcal P_y)
-D(\mathcal R_y^e\|\mathcal P_y^e).
\]
Equations (10)–(12) turn this into
\[
\ell_{\rm phys}(y)
=D(R_y\|g)+c_T+\|Dy\|^2
-D(\mathcal R_y^e\|\mathcal P_y^e).
\tag{13}
\]
Project the retained increment \(v_{\rm ev}\) onto \((DZ_M)^\perp\). Under recognition its law is Gaussian with mean \(Dy\) and covariance \(I/2\) on that subspace; under the physical law it has mean zero and the same covariance. This remains true regardless of \(R_y\), because the projection removes \(Dz\). Data processing therefore gives
\[
D(\mathcal R_y^e\|\mathcal P_y^e)\ge\|Dy\|^2.
\]
Hence
\[
\ell_{\rm phys}(y)\le D(R_y\|g)+c_T.
\]
There is no discarded variable on the other fourteen strata. Averaging proves
\[
\mathcal D_{\rm phys}(R)
\le\mathcal D_{\rm opt}(R)
+c_T R(S\text{ is a matching})
\le\mathcal D_{\rm opt}(R)+T,
\tag{14}
\]
since
\[
c_T=\log\!\left(1+\frac{4T}{4+T}\right)
\le\frac{4T}{4+T}\le T.
\]

The distinction matters: \(g\) is the optimizer hidden conditional given \((S,y)\), **not generally the hidden conditional after also observing evaluator samples**. Their retention is handled by the subtracted evaluator-marginal KL in (13), not by falsely declaring those samples independent of hidden coordinates. The Gaussian sampling here must mean the stated joint/product evaluator kernel; merely specifying two Gaussian marginals without their conditional coupling would not determine this calculation.

## 5. Detailed balance supplies exactly the needed average hazard

For frozen \(p\), the fine heat-bath proposal satisfies
\[
\mu_p(dx,S)\beta_p(S'\mid x)
=\mu_p^X(dx)\beta_p(S\mid x)\beta_p(S'\mid x).
\tag{15}
\]
Because \(\kappa_S\) is the optimizer conditional on the source fiber, the joint transition measure of the parent proposal is the pushforward of (15) by
\[
(x,S,S')\longmapsto\bigl((S,P_{W_S}x),(S',P_{W_{S'}}x)\bigr).
\]
It is symmetric. Thus \(J_p\) is reversible with respect to \(C_\#\mu_p\), despite the variable-dimensional strata. The stratumwise OU parts are also reversible for the corresponding Gaussian conditionals.

Let \(\sigma_M=P_{W_M\#}\nu_T^M\), with its assignment label suppressed, and define the parent departure intensity
\[
\lambda_p(y)
=\int\kappa_M(dx\mid y)\,[1-\beta_p(M\mid x)].
\]
Disintegration gives
\[
\int\sigma_M(dy)\lambda_p(y)
=\int\nu_T^M(dx)\,[1-\beta_p(M\mid x)].
\tag{16}
\]
The right side is the equilibrium flow out of \(M\), divided by \(\mu_p(M)\). Detailed balance and total proposal rate one imply
\[
\int\sigma_M\lambda_p
\le\frac{1-\mu_p(M)}{\mu_p(M)}.
\tag{17}
\]

The parent's learning satisfies \(|(p_i^C)'|\le\varepsilon\). Its rows therefore stay within \(d\) of the selected vertex during \([0,h]\), giving
\[
\pi_{p^C_u}(M)\ge(1-d)^4\ge1-4d.
\]
The sheet-weight ordering yields
\[
\mu_{p^C_u}(M)
=\frac{\pi_{p^C_u}(M)Z_M}{\sum_S\pi_{p^C_u}(S)Z_S}
\ge\pi_{p^C_u}(M).
\]
Consequently,
\[
\int\sigma_M(dy)\lambda_{p^C_u}(y)
\le\frac{4d}{1-4d},\qquad 0\le u\le h.
\tag{18}
\]
This is an **integrated sheet-mass argument**, not a pointwise posterior bound. In particular, \(\beta_p(M\mid x)\ge\pi_p(M)\) is generally false.

Crucially, both the held-matching OU and its stationary law \(\sigma_M\) are independent of the rows. Thus (18) can be applied at every deterministic time-dependent value \(p^C_u\), using the **same** stationary comparison process. There is no need to freeze \(p^C\) or add a row-perturbation error.

## 6. The coupling does not assume stationarity conditional on survival

For any random element \(U\), including an entire future path,
\[
\mathcal L(U)=(1-r)\mathcal L(U\mid E)
+r\mathcal L(U\mid E^c).
\]
Therefore
\[
\operatorname{TV}(\mathcal L(U\mid E),\mathcal L(U))
=r\operatorname{TV}(\mathcal L(U\mid E),\mathcal L(U\mid E^c))
\le r.
\tag{19}
\]
There is no \(r/(1-r)\) loss. In particular,
\[
\operatorname{TV}(C_\#R_\theta,\sigma_M)\le\rho+\delta.
\tag{20}
\]

Let \(Y\) be the stationary held-matching retained OU. Couple its initial law maximally to the exact parent initial law. On the initial-success event \(A_0\), use common Brownian motion and rate-one proposal marks until the parent's first departure \(\tau\) from \(M\). Self-proposals leave the paths identical.

The correct compensator estimate is
\[
\begin{aligned}
\mathbb P(A_0,\tau\le h)
&=\mathbb E\int_0^h
1_{A_0}1_{\{\tau\ge u\}}
\lambda_{p^C_u}(Y_u)\,du\\
&\le\int_0^h\mathbb E\lambda_{p^C_u}(Y_u)\,du\\
&\le\frac{4hd}{1-4d}.
\end{aligned}
\tag{21}
\]
Use the predictable pre-departure indicator in the compensator; its value at a single departure time does not affect the integral.

The law of \(Y_u\) **conditioned on initial success and survival need not be stationary**. We simply discard those indicators and use the unconditional stationary marginal. This is the essential domination step.

Combining (20)–(21),
\[
\operatorname{TV}(\mathsf Q_C^h,\mathsf H_M^h)
\le\rho+\delta+\frac{4hd}{1-4d},
\tag{22}
\]
where \(\mathsf H_M^h\) is the stationary held retained path law. By (19) and the established native path estimate,
\[
\operatorname{TV}(\mathsf Q_E^h,\mathsf H_M^h)
\le\rho+(h+2)\delta.
\tag{23}
\]
Their triangle inequality is exactly (1).

**There is no \(h\rho\) term.** Initial mismatch is paid once, rather than repeatedly transporting a stationary hazard estimate to the evolving parent law. This matters because the selected scaling would not make a generic \(h\rho\) error vanish.

## 7. Scaling and the optional row comparison

Here
\[
\rho\le3T+8\sqrt{2/\pi}\,T^{1/4}+3408T^{1/2},
\]
and
\[
d\le T+T^{7/4},\qquad
h\delta\le T^{3/4},\qquad
hd\le T^{3/4}+T^{3/2}.
\]
Thus the bound in (1) is \(O(T^{1/4})\), while
\[
K_T=O\!\left(T^{1/4}\log(1/T)\right)\longrightarrow0.
\]
Also
\[
s=2\varepsilon^{-1}\log(1/\varepsilon)
\ge4T^{-2}\log(1/T),
\]
so \(1+h\le s\) eventually.

The optional row-path comparison is valid with one distinction: the original fine rows are sourced by the **unconditional** native law, not by \(R_t\). Direct comparison through the held process gives parent versus unconditional-native path TV at most
\[
B_0=\rho+(h+3)\delta+\frac{4hd}{1-4d}.
\]
Since the initial rows agree, variation of constants then gives
\[
\sup_{u\le h}\|p^C_u-p(\theta+u)\|_\infty
\le(1-e^{-\varepsilon h})B_0
\le\varepsilon hB_0.
\tag{24}
\]
Using only parent-versus-conditioned-native TV in this argument would require an additional conditioning correction.

## 8. Exact scope and remaining gaps

### What is established

* An autonomous, nonexplosive parent with deterministic **own-law** learning.
* Exact initialization from \(C_\#R_\theta\), without factorization of retained correlations or a Gaussian reset.
* Vanishing averaged information discarded from the actual conditioned native law, including the stated physical comparison with evaluator samples retained.
* Vanishing path-TV error for retained dynamics over the increasing duration \(T^{-1/4}\).

The Gaussian integration in \(J_p\) defines the parent's proposal kernel. It is not a claim that the actual fine hidden conditional equals that Gaussian, and it does not replace the inherited initial retained distribution.

### What is not established

**Exact dynamical lumpability.** The continuous matching OU projects exactly. The whole compressed fine process need not be Markov: two hidden states on the same retained fiber can give different assignment-proposal probabilities and different projected targets. The kernel \(J_p\) is the optimizer-conditional averaged kernel. The rare-departure coupling, not an exact lumpability assertion, justifies its use here.

**A later parent entropy theorem.** After activation, \(Q^C_u\) need not equal \(C_\#R_{\theta+u}\). Path TV controls bounded path observables; it does not transfer relative entropy. For example, on the same retained Gaussian space, choose \(\sigma_M(A_n)=e^{-n^2}\) and set
\[
Q_n=(1-1/n)\sigma_M+(1/n)\sigma_M(\cdot\mid A_n).
\]
Then TV is at most \(1/n\), while binary data processing shows \(D(Q_n\|\sigma_M)\to\infty\). Thus a later parent entropy or free-energy claim requires its own estimate.

**Evaluator path dynamics.** For the static physical statement, push the complete joint law, including the evaluator samples. Do not reconstruct its initial joint law by independently resampling those retained samples. If they are intended as persistent parent state coordinates, their dynamics must additionally be defined; the stated \(J_p\) specifies only \((S,y)\). Likewise, normalized pushforward references do not by themselves prove that pushforward commutes with a separately proposed optimization problem.

**First formation, recursion, or every-history activation.** None follows from the late selected-coherence inputs.

### What an extension to a specified first-prefix event would require

Keep the proposed earlier event \(F\) unchanged. For a deterministic activation time \(\vartheta\), require \(F\in\mathcal F_\vartheta\) and \(\mathbb P(F)>0\), and let
\(R_t^F=\mathcal L(X_t,S_t\mid F)\). A sufficient quantitative extension of this proof is to establish, for that very event:
\[
\begin{aligned}
e_0&=\operatorname{TV}(C_\#R_\vartheta^F,\sigma_M)\to0,\\
e_1&=\operatorname{TV}(\mathcal L(C(X,S)_{[\vartheta,\vartheta+h]}\mid F),
\mathsf H_M^h)\to0,\\
\zeta&=\mathcal D_{\rm opt}(R_\vartheta^F)\to0,
\end{aligned}
\]
together with inherited row distance \(\delta_F\) satisfying
\[
d_F=\delta_F+\varepsilon h<1/4,
\qquad hd_F\to0.
\]
Then the same proof gives path error at most
\[
e_0+e_1+\frac{4hd_F}{1-4d_F},
\]
and initial physical discarded KL at most \(\zeta+T\). A uniform later native-static claim requires the corresponding uniform conditional information estimate.

These conditional assumptions can follow from high probability of \(F\) and the same unconditional inputs, but high probability is not logically necessary: a rare event can be harmless if its conditional bias is independently controlled. A sharper identity makes the needed information control explicit. With \(U_t=(X_t,S_t)\), \(Y_t=C(U_t)\), \(B=1_F\), and \(\alpha=\mathbb P(F)\),
\[
\alpha\mathcal D_{\rm opt}(R_t^F)
+(1-\alpha)\mathcal D_{\rm opt}(R_t^{F^c})
=\mathcal D_{\rm opt}(q_t)+I(B;U_t\mid Y_t).
\tag{25}
\]
Thus
\[
\frac{\mathcal D_{\rm opt}(q_t)+I(B;U_t\mid Y_t)}{\alpha}\to0
\]
is one sufficient information condition for the unchanged event. It is not supplied for an arbitrary earlier first block.

The obstruction is real even on your existing Gaussian hidden fiber: conditioning \(g\) on a hidden event \(A\) has discarded KL \(\log(1/g(A))\), which can be arbitrarily large although its retained marginal is unchanged. Conditioning on an exact full realized past fixes the hidden endpoint and gives a point mass, singular relative to \(g\). In contrast, a positive-probability event at a fixed time cannot create singularity when the unconditional endpoint has a density; it can still create large information bias. First-entry stopping times introduce a further issue—stopped endpoint laws can concentrate on boundaries, and deterministic-time estimates cannot simply be evaluated at those stopping times.

**Bottom line:** the late, high-probability prefix construction closes the stated activation problem. The decisive mechanisms are the event-information identity, row-independent matching conditionals, and the killed stationary-reference coupling. The remaining gaps concern stronger claims—earlier first episodes, recursive formation, persistent evaluator dynamics, or later parent entropy—not the scoped activation theorem proved above.

