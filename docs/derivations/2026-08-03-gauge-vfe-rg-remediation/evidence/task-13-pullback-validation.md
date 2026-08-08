# Task 13 pullback-geometry validation

## Bound source and disposition

- Source revision: `4ed9ddf6bbb0cc7870118a6aa51710e9bbc2c0ae`.
- Source tree: `07ca0745bc74d96102aa070dc1c04d67be2d19ab`.
- PB-1, PB-2, and PB-3 are reconstructed below from committed source objects.
- PB-4 remains `INCONCLUSIVE`; clean build, rendering, and visual inspection belong to Task 14.
- Each verified result is conditional on its displayed hypotheses. Application-specific existence
  claims are recorded separately as open.

## PB-1 — covariant informational pullbacks

**State:** `EVIDENCE_VERIFIED`.

Assume a finite-dimensional regular statistical model that is differentiable in quadratic mean,
has a positive-definite Fisher form, satisfies the stated third-score integrability and smoothness,
and carries a represented group action induced by a parameter-independent bimeasurable sample
re-coordinatization preserving the model. For a smooth section `s` and selected connection `omega`,

$$D^\omega s=\operatorname{ver}^{\omega}\circ Ts,$$

$$h_s^\omega(X,Y)=g^F(D^\omega sX,D^\omega sY),$$

$$c_s^\omega(X,Y,Z)=\mathcal T(D^\omega sX,D^\omega sY,D^\omega sZ).$$

The sample map sends each score to that score composed with the inverse sample map. Pushforward
integration preserves the second and third score moments, so the Fisher and Amari tensors descend
through the associated-bundle quotient. Under passive reframing,

$$D^{\omega'}s'=T\widehat\rho(g^{-1})D^\omega s,$$

and invariance of the descended fiber tensors cancels this representation in every argument.
This proves passive gauge invariance, not active invariance at a fixed connection.

For `omega' = omega + a`, with `R_a^s(X)=vartheta_{s(c)}(a_c(X))`, the exact laws are

$$D^{\omega'}s=D^\omega s+R_a^s,$$

$$h_s^{\omega'}(X,Y)=h_s^\omega(X,Y)+g^F(R_aX,D^\omega sY)
+g^F(D^\omega sX,R_aY)+g^F(R_aX,R_aY),$$

with the analogous eight-term polarized cubic identity. The normal-location witness gives `h=0`
for the zero connection and `h=a_0^2 dx^2` for `A'=a_0 dx`, so the pullback is connection-relative.

Positive definiteness gives

$$\operatorname{rad}h_s^\omega=\ker D^\omega s,
\qquad \operatorname{rank}h_s^\omega=\operatorname{rank}D^\omega s.$$

At constant rank, `TC/ker D^omega s` is a metric vector bundle isometric to
`im D^omega s`. A quotient-manifold tangent bundle additionally requires an involutive radical,
a regular Hausdorff leaf space, a surjective-submersion quotient, and tensor basicness.

Falsifiers of stronger claims are explicit: `alpha=dz-x dy` gives a constant-rank contact radical,
while `s(x)=N(x^2,1)` gives `h=4x^2 dx^2` with a rank jump. Neither violates PB-1; they prove that
constant rank, integrability, and quotient regularity cannot be conflated.

Source anchors:

- `manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex:30-87` — regularity and tensor descent.
- `manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex:92-154` — first jet and passive covariance.
- `manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex:159-231` — connection change and witness.
- `manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex:321-401` — radical, rank, and quotient guards.
- `manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex:429-465` — contact and rank-jump witnesses.

## PB-2 — fixed-base histories, VFE orbit, and Fisher duration

**State:** `EVIDENCE_VERIFIED`.

For a law history in the fiber over `c`,

$$\varpi\circ\Gamma=c\quad\Longrightarrow\quad T\varpi(\dot\Gamma)=0.$$

For a curve of sections `Sigma(lambda,c)=Q(lambda)(c)`,

$$\varpi\circ\Sigma(\lambda,c)=c
\quad\Longrightarrow\quad \partial_\lambda\Sigma(\lambda,c)\in V\mathcal E.$$

The zero velocity is stationary under the chapter's exclusive curve-type terminology; every
nonzero such evaluation velocity is vertical. With a moving base probe `gamma`,

$$v_\omega(\Gamma)=\partial_\lambda\Sigma(\lambda,\gamma(\lambda))
+D^\omega Q(\lambda)\dot\gamma.$$

The first term is history change at fixed context. The second is the vertical response of one
instantaneous section to the probe. Their sum determines whether the total-space curve is mixed or
horizontal relative to the selected connection.

An exact VFE history requires a smooth extraction map and selected right inverse,

$$\pi_i^{\rm conf}\circ\iota_i=\operatorname{id}_{\mathcal Q_i},
\qquad \mathsf G_i^F=\iota_i^*G_{\mathfrak R_B}^F,$$

or a justified metric quotient. With a fixed outside marginal, the support, finite-KL, energy
integrability, `C^2` lift, and chartwise dominated-differentiation hypotheses give

$$\mathcal F_o(Q_{B^c}\iota_i(Q_i'))-\mathcal F_o(Q_{B^c}\iota_i(Q_i))
=\overline{\mathcal F}_{B,o}(Q_i')-\overline{\mathcal F}_{B,o}(Q_i).$$

Thus the outside-averaged local VFE and restricted collective VFE have the same differential and,
with the same metric, the same natural-gradient ray. One realized blanket value need not have this
gradient, and moving the outside marginal changes the objective.

The repaired right-inverse statement is exact. For Fisher metric `d theta^2+d eta^2` and
`pi(theta,eta)=theta`, the distinct smooth lifts

$$\iota_0(x)=(x,0),\quad \iota_c(x)=(x,c),\quad \iota_\Delta(x)=(x,x)$$

satisfy

$$\iota_0^*g=\iota_c^*g=dx^2,
\qquad \iota_\Delta^*g=2dx^2.$$

Distinct right inverses can, but need not, induce different metrics. Extraction data therefore do
not determine the configuration metric without a selected lift or a separate canonicity theorem.
A marginal-product metric is likewise not automatically joint Fisher because

$$\|L\|^2-(\|L_b\|^2+\|L_m\|^2)
=\|L-L_b-L_m\|^2-2\langle L_b,L_m\rangle,$$

whose sign is not fixed.

On the declared regular strong metric tier,

$$\dot Q=-a\,\operatorname{grad}^F\mathcal F,\qquad a>0,$$

selects an oriented unparameterized orbit. Positive scalar mobility changes only parameterization;
anisotropic mobility can change the path. A semidefinite tensor can yield no gradient or many.

Fisher speed and duration are

$$\nu_F=\sqrt{\mathsf G^F(\dot Q,\dot Q)},
\qquad \tau(\lambda)=\int_{\lambda_0}^{\lambda}\nu_F(u)\,du.$$

Under an orientation-preserving reparameterization,
`tilde nu_F=(nu_F composed with phi) phi'`, so length and cumulative duration are invariant. On a
noncritical VFE orbit,

$$\frac{dQ}{d\tau}=-\frac{\operatorname{grad}^F\mathcal F}
{\|\operatorname{grad}^F\mathcal F\|_F},
\qquad \frac{d\mathcal F}{d\tau}=-\|\operatorname{grad}^F\mathcal F\|_F.$$

Critical or Fisher-null segments stall the clock. Endpoints determine Fisher distance, not the
realized update path or duration.

A regional orthogonal clock requires exactness of

$$\alpha_F=-\frac{d\mathcal F}{\|\operatorname{grad}^F\mathcal F\|_F},
\qquad d\alpha_F=N^{-2}dN\wedge d\mathcal F.$$

Closedness and zero periods are necessary and sufficient. For `F(x,y)=xy`, `d alpha_F` is generically
nonzero, so orbitwise duration need not assemble into a global clock.

Independent fine and coarse natural-gradient flows require oriented semiconjugacy,

$$T\mathsf R_\ell X_\ell=a_\ell X_{\ell+1}\circ\mathsf R_\ell,
\qquad a_\ell>0.$$

Functional compatibility alone is insufficient. A sufficient route is a surjective horizontally
conformal submersion of dilation `varphi_l` and
`F_l=chi_l composed with F_{l+1} composed with R_l`, with `chi_l'>0`; then
`a_l=chi_l' varphi_l^2`. Noncollapse and maximal-interval traversal are separate guards. The
abstract theorem is proved; semiconjugacy of the declared RG maps is open.

Source anchors:

- `manuscripts/gauge_vfe_rg/05d_relational_inference.tex:42-217` — curve and section histories.
- `manuscripts/gauge_vfe_rg/05d_relational_inference.tex:372-492` — exact lift and metric boundary.
- `manuscripts/gauge_vfe_rg/05b_local_collective_elbo.tex:294-369` — local/global identity.
- `manuscripts/gauge_vfe_rg/05d_relational_inference.tex:494-672` — orbit and duration.
- `manuscripts/gauge_vfe_rg/05d_relational_inference.tex:774-842` — exact clock criterion.
- `manuscripts/gauge_vfe_rg/05d_relational_inference.tex:1154-1553` — semiconjugacy guards.

## PB-3 — cross-scale first jets and Fisher data processing

**State:** `EVIDENCE_VERIFIED`.

Let `Psi:E -> Ebar` cover `f:C -> Cbar` and assume related sections
`Psi composed with s = sbar composed with f`. Define

$$A_\Psi(e;X)=T_e\Psi(H_e^\omega X)
-H_{\Psi(e)}^{\bar\omega}(T_cfX).$$

Differentiating the related-section identity gives the exact chain rule

$$D^{\bar\omega}\bar s(TfX)
=T^V\Psi(D^\omega sX)+A_\Psi(s(c);X).$$

Exact first-jet naturality holds when `A_Psi=0`. For an induced principal scale map this is equivalent
to the scale-connection defect taking values in the isotropy subalgebra of the coarse section value.
Vanishing of the principal defect is sufficient, but not necessary unless the action is
infinitesimally effective. Section descent is separately required: before `Psi composed with s` is
constant on fibers of a surjective submersion `f`, it defines only a pullback-bundle section.

For a strongly normalized, parameter-independent, equivariant Markov kernel, also require fine and
coarse regularity, family closure, smoothness of the induced law map and vertical differential,
common domination for the DQM transfer, and measurable parameter-smooth conditional-score versions.
Then

$$\Delta_F^\Psi=g^F-(T^V\Psi)^*\bar g^F,$$

and the pushed score is `E[ell_u(X) | Y]`. Total variance gives

$$\Delta_F^\Psi(u,u)=\mathbb E\operatorname{Var}(\ell_u\mid Y)\geq0,$$

with equality exactly when the fine score is measurable with respect to the coarse output. If
`A_Psi=0`, its base pullback is

$$h_s^\omega-f^*\bar h_{\bar s}^{\bar\omega}
=(D^\omega s)^*\Delta_F^\Psi\succeq0.$$

This is a contravariant comparison on the fine tangent space, not a canonical metric pushforward.

Without horizontal compatibility, vertical data processing survives but base contraction need not:

$$h_s^\omega-f^*\bar h_{\bar s}^{\bar\omega}
=\delta_\Psi-\mathcal X_\Psi-\mathcal Q_\Psi,$$

where `delta_Psi(X,Y)=Delta_F^Psi(u_X,u_Y)`,
`X_Psi(X,Y)=gbar(Lu_X,a_Y)+gbar(a_X,Lu_Y)`, and
`Q_Psi(X,Y)=gbar(a_X,a_Y)>=0`. The cross term is sign indefinite and both anomaly terms are
subtracted. The source gives a negative base difference at `b=1/2`; even zero vertical information
loss can coexist with the strictly negative base defect `-a^2 dx^2`.

A restriction, energy precomposition, Galerkin map, fitted approximation, parameter-dependent
kernel, or generative/recognition mismatch is outside the Markov theorem.

Source anchors:

- `manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex:673-790` — descent and nonfunctoriality.
- `manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex:792-907` — chain rule and anomaly boundary.
- `manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex:921-975` — isotropy criterion.
- `manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex:1078-1169` — Markov hypotheses and defect proof.
- `manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex:1172-1206` — meta-agent geometry and exclusions.

## PB-4 and explicit nonclaims

**PB-4 state:** `INCONCLUSIVE` pending Task 14 build and rendering evidence.

- No canonical connection or automatically nondegenerate perceived base metric is established.
- Existence and coarse preservation of an application-specific joint-law right inverse remain open.
- Fisher duration is not physical time, RG depth, a base coordinate, or a synchronized clock.
- A shared clock requires exactness, zero periods, and treatment of critical and null strata.
- Same-path Markov contraction does not compare independently recomputed fine/coarse histories.
- Semiconjugacy of the manuscript's declared RG maps remains open.
- No build, page-count, citation, reference, auxiliary-freshness, or visual claim is made here.
