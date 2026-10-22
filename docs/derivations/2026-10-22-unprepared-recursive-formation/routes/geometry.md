<!-- rigorous-theory-search-metadata {"schema_version":"rigorous-theory-search/v1","contract_id":"contract-sha256-b542fc3173c340f7c3430dc4795f9964d742d9047e059add3a8949d73f3bbcbe","target_digest":"b542fc3173c340f7c3430dc4795f9964d742d9047e059add3a8949d73f3bbcbe"} -->
# Dynamical compatibility of retained collective geometry

## Result and scope

An initially geometry-preserving retention need not remain so under the original full KL/Fisher field. For a fixed sample retention, the new local test is the conditionally centered derivative of the complete score force. An incoming peer derivative can generate a hidden contextual score immediately, even when the initial contextual direction is exactly retained. The first Fisher loss is quadratic in elapsed time. Under initial orbit-score sufficiency, changing the collective minimizing connection cannot remove that leading loss.

This is a scoped obstruction and a constructive compatibility criterion, not a nonexistence result for the frozen existential target. Unprepared law values alone do not rule out exact selected-jet geometry: through every strictly positive finite law there are nonconstant contextual families whose marginal retains their entire Fisher tensor. Pure local KL relaxation preserves these families without requiring equality of their conditional laws. Identity peer coupling generally does not. Neither result supplies two-stage clique formation or an autonomous compressed parent.

The two mechanisms investigated here are propagation of score sufficiency under the fine vector field, and compensation by state-selected or moving retentions. The latter requires an actual derivative and an event-time correction. It cannot be justified by the fixed-channel data-processing inequality.

## Sources and conventions

The live source is `Research/manuscripts/MAgent_Theory_2.0/` at the revision recorded in `../source-manifest.json`: Chapter 2 geometry, Chapter 3's complete KL derivative and equal-mobility Fisher field, and Chapter 12's conditional Wishart construction. The prior `2026-10-22-endogenous-recursive-geometry/routes/optimized-geometry.md` already proves the static optimized-loss identity. Its Wishart companion proves sufficiency of common-precision contextual and orbit scores; it also identifies lost shape-allocation directions. The prior analytic-behavior result concerns a fixed analytic waiting-closed response protocol. None of those statements proves persistence of a newly chosen geometry-preserving jet under arbitrary peer forces.

The following dictionary fixes the geometric objects.

| Object | Meaning and convention |
| --- | --- |
| \(\mathcal C\) | Smooth contextual base; its coordinates are not sample contents or inference time. |
| \(\mathcal N\) | Regular finite-dimensional family of normalized laws \(P_x\) on a standard Borel sample space \(\mathsf Y\), or a finite product of positive probability simplexes. |
| \(g_x\) | Fisher metric \(g_x(u,v)=\mathbb E_x[\ell_u\ell_v]\), with the same unit product normalization before and after retention. |
| \(G\), \(J_x\xi\) | A declared Lie group of sample pushforwards and its infinitesimal left action. These pushforwards preserve Fisher information. An arbitrary parameter transformation is not assumed to be such an action. |
| \(\mathcal C\times G\) | Local trivialization of the principal bundle; nontrivial overlaps require the usual transition cocycle. |
| \(p_t:\mathcal C\to\mathcal N\) | The contextual section evolved for the same inference time \(t\) at every context. |
| \(A_t\) | Fine collective minimizing connection, with \(D^{A_t}p_t=dp_t+J_{p_t}A_t\). |
| \(C:\mathsf Y\rightsquigarrow\mathsf Z\) | A fixed normalized sample channel, independent of the law, context, and inference time, unless explicitly replaced below by a moving channel. |
| \(R(x)=P_xC\) | Statistical law retention. Its output law alone is not automatically a sufficient configuration state. |
| \(P_t^C f\) | Conditional expectation \(\mathbb E_t[f(Y)\mid Z]\) under \(P_{p_t}(dy)C(y,dz)\); conditional expectations are identified with their pullbacks to the joint space when taking norms. |

The passive gauge convention is \(p'=g_\#p\), \(A'=\operatorname{Ad}_g A-(dg)g^{-1}\). Thus \(D^{A'}p'=T(g_\#)D^Ap\). For equivariant retention, \(R(g\cdot x)=g\cdot R(x)\), differentiation gives \(dR J=\bar J\). Every equality below is local on a regular constant-rank orbit stratum. Equality of full minimizing classes additionally requires \(\ker J=\ker\bar J\). When the infinitesimal stabilizer is zero, equal minimizing forms have equal curvature \(F=dA+\tfrac12[A\wedge A]\); no preferred curvature representative is asserted when stabilizer-valued connection components remain undetermined.

## A quadratic test for dynamically generated Fisher loss

First use a deterministic fixed statistic \(C:Y\mapsto Z\). Let \(p_t(c;y)>0\) be a family of densities, with marginal \(\mu_t(c;z)\) and regular conditional density \(\kappa_t(c;y\mid z)\). On finite alphabets all formulas below hold on any compact interior time-context neighborhood under a smooth vector field. On general spaces assume a common dominating disintegration, fixed support, differentiability in time and context, and domination strong enough to justify the displayed derivatives in \(L^2\). These additional hypotheses are route-specific; mere formal differentiation of a conditional density is insufficient.

For a contextual vector \(X\), write

\[
S_X= X\log p_t,
\qquad a_X=(I-P_t^C)S_X=X\log\kappa_t.
\tag{G3}
\]

The exact Fisher loss in this direction is

\[
g_t(dp_tX,dp_tX)-\bar g_t(dRp_tX,dRp_tX)
=\mathbb E_t[a_X^2].
\tag{G4}
\]

Suppose the fine density has its original centered force equation

\[
\partial_t\log p_t=-(h_t-\mathbb E_t h_t).
\tag{G5}
\]

Here \(h_t\) is the complete variational force, including sender roles and all channel derivatives. Differentiation of the conditional normalization gives

\[
\partial_t\log\kappa_t=-h_t+P_t^Ch_t.
\tag{G6}
\]

Consequently

\[
\partial_t a_X
=-(I-P_t^C)Xh_t+\operatorname{Cov}_{\kappa_t}(h_t,a_X).
\tag{G7}
\]

The covariance is a function of the retained coordinate. To verify (G7), differentiate (G6) in \(X\), and use

\[
X(P_t^Ch_t)=P_t^C(Xh_t)+P_t^C(h_t a_X).
\]

The conditional score \(a_X\) is centered, so the last term is the stated covariance. In particular, at a time when \(a_X=0\),

\[
\left.\partial_t a_X\right|_{t=0}
=-(I-P_0^C)Xh_0.
\tag{G8}
\]

If this derivative exists in \(L^2\) and the measures vary regularly, Taylor expansion of (G4) gives

\[
g_t(dp_tX,dp_tX)-\bar g_t(dRp_tX,dRp_tX)
=t^2\mathbb E_0\left[((I-P_0^C)Xh_0)^2\right]+o(t^2).
\tag{G9}
\]

For a finite positive model this needs no interchange theorem beyond finite differentiation. Equation (G9) establishes a definite loss whenever the coefficient is nonzero. It does not assert loss when that coefficient vanishes; higher derivatives may then decide the issue. Invariance of a family of sufficient contextual directions requires the right side of (G8) to vanish on the entire proposed invariant family, followed by the corresponding uniqueness or invariance argument. Checking the equality at one point is not sufficient.

### What optimizing the connection can change

Let \(r_X(t)=dp_t(X)+J_{p_t}A_t(X)\) be the actual fine minimizing residual. Put \(\sigma_t=\ell_{r_X(t)}\), \(\alpha_t=(I-P_t^C)\sigma_t\), and assume \(\alpha_0=0\). Fix a smooth Lie-algebra complement to the common infinitesimal stabilizer. Let \(o_a(t)=\ell_{J\xi_a}\) be orbit scores for a basis of that complement, and assume the coarse locked-inertia matrix

\[
\bar K_{ab}(0)=\mathbb E_0[(P_0^Co_a)(P_0^Co_b)]
\]

is positive definite there. All fields are assumed sufficiently differentiable for the expansions below. Write

\[
b_X=\left.\frac{d\alpha_t}{dt}\right|_0,
\qquad
m_a=\mathbb E_0[b_X(I-P_0^C)o_a(0)].
\]

The optimized-loss identity and the two normal equations imply

\[
h_t^{\min}(X,X)-\bar h_t^{\min}(X,X)
=t^2\left[\|b_X\|_{L^2(P_0)}^2
+m^T\bar K(0)^{-1}m\right]+o(t^2).
\tag{G10}
\]

Here norms and expectations may equivalently be taken in the joint input-output experiment. To prove it, put \(a_t=\bar A_t(X)-A_t(X)\). The normal equations give

\[
\bar K(t)a_t=\Delta_t(r_X(t),J\cdot),
\qquad
\Delta_t(u,v)=\mathbb E_t[(I-P_t^C)\ell_u (I-P_t^C)\ell_v].
\tag{G11}
\]

The right side is \(t m+o(t)\). Therefore \(a_t=t\bar K(0)^{-1}m+o(t)\). Substitution into the prior identity

\[
h_t^{\min}-\bar h_t^{\min}
=\Delta_t(r_X,r_X)+\|\bar J a_t\|_{\bar g_t}^2
\]

proves (G10). This derivation uses the full output derivative and the same metric normalization at both levels.

If every initial orbit score is retained, \((I-P_0^C)o_a(0)=0\), then \(m=0\). In fact (G11) has a right side of order \(t^2\), so \(a_t=O(t^2)\) and its squared contribution is \(O(t^4)\). The leading loss is exactly \(t^2\|b_X\|^2\). An adjustment of the minimizing connection cannot cancel it. In this case

\[
b_X=(I-P_0^C)\left[\dot S_X(0)+\sum_a A_0^a(X)\dot o_a(0)\right],
\tag{G12}
\]

because the term \(\sum_a\dot A_0^a(X)o_a(0)\) is retained. The derivative of conditional expectation contributes zero at \(\alpha_0=0\): its weight-derivative term is the conditional covariance of a retained function with a centered conditional temporal score.

Without initial orbit-score sufficiency, the term involving \(\dot A_0\) need not vanish in the hidden conditional component. The raw contextual score can partly or entirely be projected into orbit directions. Therefore a calculation using \(Xh\) alone does not prove loss of optimized geometry in that case; one must compute the actual residual derivative \(b_X\). Equation (G10) states the valid criterion. Once this actual \(b_X\) is nonzero, the coarse connection correction adds a nonnegative contribution and cannot cancel it.

## Exact incoming-force example on an open set of law values

This example uses only strictly positive finite laws and belongs to the original KL family. It is not a clique-formation construction. Let two belief laws on a finite product alphabet be

\[
q_i(z,y)=\mu_i(z)\kappa_i(y\mid z),\qquad i=1,2,
\]

with all entries positive. Fix any proper positive references \(r_i\), and use one identity peer channel to the other agent in each source row. The source weights are then one, their row KL terms vanish, and the positive temperature is immaterial. The belief potential is

\[
E=\operatorname{KL}(q_1\Vert r_1)+\operatorname{KL}(q_2\Vert r_2)
+\operatorname{KL}(q_1\Vert q_2)+\operatorname{KL}(q_2\Vert q_1).
\tag{G13}
\]

It embeds in the original two-sector model by taking constant normalized evaluators for these belief references and independent positive model laws. It is not necessary to suppress the model sector dynamically; its contribution is independent of the contextual direction used here.

Retain the pair of \(Z\)-marginals. At initial time let context vary \(\mu_2\) only:

\[
X\mu_1=0,\qquad X\mu_2=v,\qquad \sum_zv_z=0,
\qquad X\kappa_1=X\kappa_2=0.
\tag{G14}
\]

These are assumptions about the chosen contextual jet, not equality constraints on initial law values. Every positive pair \((q_1,q_2)\) admits such a local section; the conditional values may differ arbitrarily. The fine joint experiment is the declared product \(q_1\otimes q_2\). Its contextual score at zero is \(v(Z_2)/\mu_2(Z_2)\), so marginal retention initially loses no Fisher information.

The complete forces, modulo sample-independent scalars, are

\[
h_1=2\log q_1-\log r_1-\log q_2-q_2/q_1,
\qquad
h_2=2\log q_2-\log r_2-\log q_1-q_1/q_2.
\tag{G15}
\]

The ratios are incoming derivatives. They cannot be dropped when studying the original potential. Conditional centering of their contextual derivatives gives

\[
(I-P_1^C)Xh_1
=-\frac{v_z}{\mu_1(z)}
\left(\frac{\kappa_2(y\mid z)}{\kappa_1(y\mid z)}-1\right),
\]

\[
(I-P_2^C)Xh_2
=\frac{\mu_1(z)v_z}{\mu_2(z)^2}
\left(\frac{\kappa_1(y\mid z)}{\kappa_2(y\mid z)}-1\right).
\tag{G16}
\]

For instance \(Xh_1=-v_z/\mu_2(z)-(v_z/\mu_1(z))\kappa_2/\kappa_1\), whose first term is retained and whose second has conditional mean \(-v_z/\mu_1(z)\). The other formula follows by differentiating the reciprocal ratio in \(h_2\).

Define the Pearson divergence \(\chi^2(a\Vert b)=\sum_y(a_y-b_y)^2/b_y\), which is finite and nonnegative for these positive tables. Independence of the two conditional sample coordinates and (G9) give the exact leading tensor loss

\[
g_t(dp_tX,dp_tX)-\bar g_t(dRp_tX,dRp_tX)
=t^2 L(v)+o(t^2),
\]

\[
L(v)=\sum_zv_z^2\left[
\frac{\chi^2(\kappa_2(\cdot\mid z)\Vert\kappa_1(\cdot\mid z))}{\mu_1(z)}
+\frac{\mu_1(z)^2}{\mu_2(z)^3}
\chi^2(\kappa_1(\cdot\mid z)\Vert\kappa_2(\cdot\mid z))
\right].
\tag{G17}
\]

Thus \(L(v)>0\) exactly when some \(z\) with \(v_z\ne0\) has unequal conditional laws. This is an open condition on the positive law values. For any fixed nonzero \(v\), equality of all conditionals on its support is a lower-dimensional constraint; its complement is open and dense in the interior finite-table domain. Density here concerns this example and this fixed retention, not the space of all possible parent constructions.

An exact numerical value requires no experiment. Take two values of \(z\),

\[
\mu_1=\mu_2=(1/2,1/2),\quad v=(1,-1),\quad
\kappa_1(1\mid z)=1/4,\quad\kappa_2(1\mid z)=3/4.
\]

Both conditional Pearson divergences are \(4/3\), so (G17) gives \(L(v)=32/3\). Initial fine and retained Fisher lengths are both \(4\); their difference at small positive time is \((32/3)t^2+o(t^2)\). All reference contributions vanish from this coefficient because the references are held fixed.

The example takes the common Lie group to be trivial, so the tensor is already the optimized tensor. A nontrivial common group may alter the residual as described after (G12); no claim that it cannot do so is made without that calculation. If a proposed extension has retained initial orbit scores and the same nonzero hidden residual generator in a direction orthogonal to its orbit, (G10)-(G12) prove that its collective optimization cannot remove this leading loss.

## A positive control: arbitrary conditional values can retain selected geometry

For comparison remove the peer terms from (G13), leaving a local KL flow on a finite alphabet. Write a fixed positive reference as \(r(z,y)=r_Z(z)\rho(y\mid z)\). Through any positive initial law choose a contextual family

\[
q_0(c;z,y)=\mu_0(c;z)\kappa_0(y\mid z),
\tag{G18}
\]

where \(\kappa_0\) is fixed over context but arbitrary in value. With \(a=e^{-t}\), direct substitution in the original unit-Fisher equation gives

\[
q_t=\frac{q_0^a r^{1-a}}{\sum_{z,y}q_0^a r^{1-a}},
\qquad
\kappa_t(y\mid z)
=\frac{\kappa_0(y\mid z)^a\rho(y\mid z)^{1-a}}{Z_z(t)},
\]

\[
Z_z(t)=\sum_y\kappa_0(y\mid z)^a\rho(y\mid z)^{1-a}.
\tag{G19}
\]

The conditional law remains independent of context. Every contextual score remains a function of \(Z\), so (G4) is zero for all finite times. The marginal is

\[
\mu_t(c;z)
=\frac{\mu_0(c;z)^a r_Z(z)^{1-a}Z_z(t)}{
\sum_w\mu_0(c;w)^a r_Z(w)^{1-a}Z_w(t)}.
\tag{G20}
\]

As \(\kappa_0\) ranges over all strictly positive conditional tables, the initial values in (G18) cover the full interior law domain. The contextual jets in (G18) are nevertheless selected: arbitrary perturbations that also vary the conditional over context need not preserve geometry. This distinction is required by the frozen contract.

Equation (G20) also exhibits the remaining dynamical datum. The marginal alone generally does not determine the conditional normalizer profile \(Z_z(t)\). The earlier manuscript's conditional-spectrum completion is one exact way to retain this profile. This positive control is therefore not a new autonomous parent theorem, and it gives no preferential-attention clique. Its role is to prevent promoting the incoming-force obstruction into a statement that arbitrary initial law values are themselves incompatible with selected-jet geometry.

## State-selected and moving retention

### Hard selection is locally a fixed channel

Suppose a selector chooses among finitely many fixed channels \(C_m\), for example the sum maps for finitely many membership partitions. On any open chamber where the selector is constant, the channel is fixed and (G3)-(G17) apply. Strict clique inequalities define such chambers wherever their selected partition is locally unique. Choosing a partition from the state does not by itself supply a channel-derivative term inside that chamber.

A stronger elementary statement holds for a deterministic map between finite alphabets: if every matrix entry of \(C_x\) is continuous in \(x\) and takes values in \(\{0,1\}\), then every entry is locally constant, and the map is constant on each connected domain. It cannot smoothly compensate the loss by continuously changing a deterministic grouping. A switching boundary needs a separate handoff; neither a derivative across a discontinuity nor a common law-space dimension is automatic.

### A moving channel must retain its own derivative data

For a positive differentiable normalized channel density \(k_x(z\mid y)\), put \(b_u=D_u\log k_x\) and use the joint law \(P_x(dy)k_x(z\mid y)dz\). Its output score is

\[
\bar\ell_u=P_x^C(\ell_u+b_u).
\tag{G21}
\]

This is the existing manuscript's moving-channel identity. An equivalent diagonal comparison exposes the compensating term:

\[
g_x(u,u)-\bar g_{R(x)}(DR_xu,DR_xu)
=\|(I-P_x^C)\ell_u\|^2
-2\langle P_x^C\ell_u,P_x^Cb_u\rangle
-\|P_x^Cb_u\|^2.
\tag{G22}
\]

There is no fixed sign. For a minimal state-dependent example take \(P_\theta=\operatorname{Ber}(\theta)\), \(\theta\in(2/5,3/5)\), and let the channel ignore its input sample and emit \(\operatorname{Ber}(2\theta-1/2)\). At \(\theta=1/2\), the input Fisher information is \(4\) and the output information is \(16\). The channel reads the law parameter; this is not a contradiction of data processing by a fixed kernel.

Along the actual fine vector field \(V\), its output evolution is

\[
\partial_t\log(P_xC_x)
=-P_x^Ch_x+\mathbb E_xh_x+P_x^Cb_V.
\tag{G23}
\]

An autonomous parent must determine the entire centered right side, including \(P_x^Cb_V\), from its retained configuration. Geometry requires the corresponding contextual term in (G21). Writing down a channel that cancels a Fisher loss is insufficient unless both terms and their joint future response kernels descend through the same genuinely lossy retained state. If channel parameters or memory are added, their own statistical geometry must be specified; one cannot assign them zero metric simply because they are called metadata.

Equations (G21)-(G23) concern smooth positive channel densities. A singular moving deterministic statistic requires its actual weak derivative instead, as in the live manuscript. The static optimized-loss algebra remains true for a smooth equivariant statistical map when its full derivative is used, but its nonnegative-loss conclusions require a separate proof that \(\Delta\succeq0\).

## Event times are part of the geometric handoff

Let \(V\) be a smooth vector field with local flow \(\Phi_t\). An event is the first transversal crossing of a smooth function \(f=0\) on a branch where the crossing time \(\tau(x)\) is differentiable. Thus \(df(V)\ne0\) at \(x_*=\Phi_{\tau(x)}x\). Differentiating \(f(\Phi_{\tau(x)}x)=0\) gives

\[
d\tau_x(v)=-\frac{df_{x_*}(D\Phi_{\tau(x)}v)}{df_{x_*}(V(x_*))}.
\tag{G24}
\]

For a handoff \(H(x)=R(\Phi_{\tau(x)}x)\),

\[
DH_x(v)=DR_{x_*}\left[D\Phi_{\tau(x)}v+V(x_*)d\tau_x(v)\right].
\tag{G25}
\]

This compares contextual states at their different birth times. It is not the same derivative as retention at one common inference time. The extra term can remove a flow direction: before applying \(R\), the derivative is the transversal projection

\[
\left(I-\frac{V\otimes df}{df(V)}\right)D\Phi_{\tau(x)}.
\]

Such a reduction must not be reported as fixed-time geometric inheritance. Moreover the map \(x\mapsto(\tau(x),\Phi_{\tau(x)}x)\) is locally injective on the common flow domain, with inverse \((t,z)\mapsto\Phi_{-t}z\). Recording the event time restores the allegedly lost flow coordinate before any genuinely lossy \(R\) is applied. For the actual parent \((\tau,H)\), information loss must be checked after intersecting retention fibers with the level sets of \(\tau\). This proves no general impossibility: other directions may still be lost. Multiple joins add the corresponding timing data and require the same check at each stage.

If the event criterion and retention are gauge invariant/equivariant, \(\tau(gx)=\tau(x)\) and (G24)-(G25) transform covariantly. This establishes no new transition atlas or global bundle topology. A global construction still needs coherent charts, constant orbit rank where used, and compatible parent maps on overlaps.

## Failure tests and next obligation

For the force test, suppressing the incoming ratios in (G15) makes (G16) falsely vanish. Any proposed identity-peer parent with only retained marginal geometry must confront the nonzero coefficient (G17). For the optimization test, raw loss in a contextual coordinate is insufficient when it can lie in a discarded gauge orbit; use the actual minimizing residual and check stabilizers. For a selector, verify its local chamber and event-time derivative instead of treating membership as a smooth variable. For a moving stochastic channel, check both (G21) and (G23); their correction terms are different projections of the same actual channel derivative.

The minimal constructive interface is now explicit. A clique-selected retention must provide a nontrivial family of actual contextual residuals whose conditional scores stay measurable under the full fine vector field, while its joint response and force data close on a state that still loses continuous nongauge public information. Initial score sufficiency or small intra-clique KL does not establish this invariant property. At the second join the same property must hold for the inherited force and sample experiment. For two fixed equivariant Markov retentions in the same normalization, the nonnegative optimized losses add, so a later join cannot restore a contextual tensor lost at the first.

The full target remains open in this geometry route. The results above neither require all contextual jets to be preserved nor prove that every possible moving or restricted-interface retention fails. All displayed evidence is analytical. No numerical script, experiment, GPU operation, Lean work, or Research-vault edit was performed.
