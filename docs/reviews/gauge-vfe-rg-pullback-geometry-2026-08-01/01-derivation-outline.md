# Derivation outline: covariant pullbacks and timeless inference histories

Date: 2026-08-01
Scope: mathematical construction added to `manuscripts/gauge_vfe_rg`

## 1. Typed geometric data

For either statistical channel (x\in\{b,m\}), let

\[
\varpi_x:\mathcal E_x\longrightarrow\mathcal C
\]

be an associated statistical bundle with vertical bundle
(V\mathcal E_x=\ker T\varpi_x).  A selected principal connection induces an Ehresmann splitting

\[
T\mathcal E_x=H^{\omega_x}\mathcal E_x\oplus V\mathcal E_x
\]

and vertical projection (\operatorname{ver}^{\omega_x}).  A smooth agent section
(s:\mathcal C\to\mathcal E_x) therefore has the covariant vertical first jet

\[
D^{\omega_x}s:=\operatorname{ver}^{\omega_x}\circ Ts:
T\mathcal C\longrightarrow V\mathcal E_x.
\]

This projection is load bearing.  The Fisher tensor is vertical; without a connection, (Ts(X)) has no canonical vertical component when (X\neq0).

## 2. Informational tensors perceived through a section

Suppose the statistical fiber is regular and has vertical Fisher metric (g_x^F) and Amari--Chentsov tensor (T_x^A), invariant under the represented gauge action.  Define

\[
h_{s,x}^{\omega_x}(X,Y)
=g_x^F(D^{\omega_x}sX,D^{\omega_x}sY),
\]

\[
c_{s,x}^{\omega_x}(X,Y,Z)
=T_x^A(D^{\omega_x}sX,D^{\omega_x}sY,D^{\omega_x}sZ).
\]

The represented action and transformed connection make (D^{\omega_x}s) equivariant.  Invariance of the fiber tensors then cancels the passive frame transformation in every slot.  Thus (h) and (c) are global tensors on the base, although they depend on the chosen connection.

If (\omega'=\omega+a), write (R_a(X)) for the vertical infinitesimal action contributed by the connection change.  Then

\[
D^{\omega'}sX=D^{\omega}sX+R_a(X)
\]

and

\[
h_s^{\omega'}(X,Y)=h_s^\omega(X,Y)
+g(R_aX,D^\omega sY)+g(D^\omega sX,R_aY)+g(R_aX,R_aY).
\]

Hence passive gauge invariance is not connection independence.  The principal bundle alone does not select a unique perceived base geometry.

For independent belief and model fibers, (h_{q_i,b}^{\omega_b}) and (h_{s_i,m}^{\omega_m}) are separately typed tensors.  A scalar sum requires declared positive weights or a joint metric.  The shared principal bundle does not provide cross-channel units or a bilinear cross term.

## 3. Rank and quotient audit

When (g_x^F) is positive definite,

\[
\operatorname{rad}h_s^\omega=\ker D^\omega s,
\qquad
\operatorname{rank}h_s^\omega=\operatorname{rank}D^\omega s.
\]

Thus (h_s^\omega) is Riemannian exactly where (D^\omega s) is injective.  At constant rank, the vector bundle (T\mathcal C/\ker D^\omega s) inherits a metric.  This is not automatically the tangent bundle of a quotient manifold.  Such a quotient additionally requires involutivity of the null distribution, a sufficiently regular leaf space, and basicness of the tensor.

Two exact witnesses prevent overstatement:

- Rank jump: on (\mathbb R), (s(x)=\mathcal N(x^2,1)) with the zero connection gives (h=4x^2dx^2).
- Nonintegrable constant rank: on (\mathbb R^3), the one-form (\alpha=dz-x\,dy) gives (h=\alpha^2), while (\alpha\wedge d\alpha\neq0).  Its rank is constant but its radical is a contact distribution.

## 4. Four different kinds of curves

Let (\Gamma:J\to\mathcal E_x) and (\gamma=\varpi_x\circ\Gamma).  The connection-relative decomposition is

\[
\dot\Gamma
=H^{\omega_x}_{\Gamma}(\dot\gamma)
+\operatorname{ver}^{\omega_x}(\dot\Gamma).
\]

The types are:

1. **Fixed-context fiber curve.**  If (\gamma(\lambda)=c), then (\Gamma(\lambda)\in(\mathcal E_x)_c) and (\dot\Gamma\) is canonically vertical.  No connection is needed to establish verticality.
2. **Horizontal lift.**  If (\operatorname{ver}^{\omega_x}\dot\Gamma=0), the curve is horizontal relative to (\omega_x).  It represents parallel transport, not intrinsic statistical updating.
3. **Mixed base-traversing curve.**  If both terms are nonzero, a chosen connection is required to distinguish transport from statistical change.
4. **Section history.**  A family (\lambda\mapsto s_\lambda) is a curve in a declared configuration space of sections.  Its adjoint map (\Sigma(\lambda,c)=s_\lambda(c)) satisfies (\varpi\Sigma(\lambda,c)=c), so (\partial_\lambda\Sigma(\lambda,c)) is vertical for every fixed (c).

A base curve needs no connection.  Its horizontal lift and the horizontal--vertical decomposition of a curve above it do.

For a fixed-context curve, the Fisher path length is

\[
L_F[\Gamma]=\int_J\sqrt{g^F_{\Gamma(\lambda)}(\dot\Gamma,\dot\Gamma)}\,d\lambda.
\]

Endpoints (A,B\in(\mathcal E_x)_c) do not determine an update curve or its length.  The Fisher--Rao distance is the infimum of these lengths over admissible curves; it need not equal the length of the realized update.

## 5. Parameter-free VFE histories

The fixed, timeless base (\mathcal C) is not used as an evolution parameter.  Work instead on a regular inference configuration manifold (\mathfrak M_{\mathrm{inf}}), which may be one fiber, a finite-design product of fibers, or a separately justified section manifold.  A parameterized curve (\xi:I\to\mathfrak M_{\mathrm{inf}}) represents the same oriented history after any orientation-preserving (C^1) reparameterization.

VFE decrease alone supplies neither a unique curve nor a speed.  After choosing a configuration metric (\mathfrak G), the positive ray

\[
\mathbb R_{>0}\bigl[-\operatorname{grad}_{\mathfrak G}\mathcal F\bigr]
\]

selects oriented unparameterized integral curves away from critical points.  Equivalently, any representative satisfies

\[
\xi'(\lambda)=-\upsilon(\lambda)
\operatorname{grad}_{\mathfrak G}\mathcal F(\xi(\lambda)),
\qquad \upsilon(\lambda)>0.
\]

A common positive scalar (\upsilon) changes only parameterization.  Anisotropic or independently block-scaled mobility generally changes the orbit.  For example, for (\mathcal F=(x^2+y^2)/2), rates ((1,1)) trace a ray while rates ((1,2)) trace (y=y_0(x/x_0)^2).

Calling this orbit an exact local or collective VFE history requires a separate joint-law lift.  A pair of marginal belief--model sections does not determine the dependence structure of a conditional or full recognition law.  On an admissible conditional-law manifold (\mathfrak R_B), declare an extraction map and a smooth right inverse

\[
\pi_i^{\mathrm{conf}}:\mathfrak R_B\to\mathcal Q_i,
\qquad
\iota_i:\mathcal Q_i\to\mathfrak R_B,
\qquad
\pi_i^{\mathrm{conf}}\circ\iota_i=\operatorname{id}.
\]

At fixed outside marginal (Q_{B^c}), the exact coordinate objective is the outside-averaged conditional VFE

\[
\overline{\mathcal F}_{B,o}(Q_i)
=\mathbb E_{Q_{B^c}}
\mathcal F_{B,o}(r_B^{Q_i};Y_{B^c}).
\]

Under the local--global theorem's support and finiteness hypotheses, plus the smooth domination needed to differentiate under the expectation, this differs from the restricted collective VFE only by a (Q_i)-independent term.  The exact Fisher metric is (\iota_i^*G_{\mathfrak R_B}^F), or its justified quotient.  A weighted marginal Fisher sum is exact only under separately proved block orthogonality or fixed dependence.

On a selected regular oriented orbit, Fisher arclength defines an intrinsic information coordinate

\[
\tau(p)-\tau(p_0)=\int_{[p_0,p]}ds_{\mathfrak G}.
\]

It is invariant under the disposable parameter (\lambda).  In Fisher unit-speed gauge,

\[
\frac{d\xi}{d\tau}
=-\frac{\operatorname{grad}\mathcal F}{\|\operatorname{grad}\mathcal F\|},
\qquad
\frac{d\mathcal F}{d\tau}
=-\|\operatorname{grad}\mathcal F\|.
\]

This constructs agent-relative information duration, not physical time.  It can stall on critical or null segments, depend on the realized path, and have finite total length even when an algorithmic parameter is unbounded.  A canonical orthogonal unit-speed clock on a region would require exactness of

\[
\vartheta=-\frac{d\mathcal F}{\|\operatorname{grad}\mathcal F\|},
\]

including local closedness and zero periods globally.  Those conditions are not automatic.

## 6. Operational and meta-agent geometry

For a parameter-independent normalized Markov record channel, the coarse score is the conditional expectation of the fine score.  Therefore

\[
g_{\mathrm{fine}}-\Psi^*g_{\mathrm{coarse}}
=\mathbb E\!\left[\operatorname{Cov}(\ell_{\mathrm{fine}}\mid R)\right]
\succeq0.
\]

Let (\Psi:E\to\bar E) cover (f:\mathcal C\to\bar{\mathcal C}), and suppose (\Psi\circ s=\bar s\circ f).  If (\Psi) preserves horizontal lifts, then

\[
D^{\bar\omega}\bar s\circ Tf=T^V\Psi\circ D^\omega s
\]

and hence

\[
f^*h_{\bar s}^{\bar\omega}
=(D^\omega s)^*(T^V\Psi)^*\bar g^F
\preceq h_s^\omega.
\]

Without connection compatibility, an explicit vertical mismatch term enters the first-jet chain rule.  Without descent of (\Psi\circ s) along fibers of (f), a fine section defines only a section of the pulled-back coarse bundle, not a meta-section on (\bar{\mathcal C}).

For composable Markov maps, the Fisher defects telescope:

\[
\Delta_{02}=\Delta_{01}+(T^V\Psi_{01})^*\Delta_{12}.
\]

This is the exact cross-scale information-loss cocycle.  The corresponding path-length inequality applies to the coarse image of the same fine path.  It does not compare independently recomputed meta-agent and fine-agent natural-gradient histories unless their vector fields obey an oriented semiconjugacy

\[
Tf(X_{\mathrm{fine}})=\alpha X_{\mathrm{meta}}\circ f,
\qquad \alpha>0.
\]

Finally, a beta function for perceived geometry requires the same reference-space identifications as every other RG component.  Tensors living on different bases cannot be subtracted or differentiated canonically.  After declared identifications (I_\ell), one may define (\widehat h_\ell=I_\ell^*h_\ell) and differentiate or difference (\widehat h_\ell) with respect to RG depth.  That depth is a scale coordinate, not inference duration.

## 7. Exact boundary of the affirmative construction

The construction affirmatively supplies:

- global, gauge-invariant, connection-relative Fisher and Amari pullbacks;
- the perceived semimetric and its radical/quotient conditions;
- a rigorous vertical/horizontal/mixed/section-history taxonomy;
- oriented natural-gradient histories without primitive time;
- Fisher information length along those histories;
- meta-agent first-jet naturality, Markov contraction, and an additive cross-scale defect;
- reference-typed RG flow of perceived geometry.

It does not by itself supply a canonical connection, a nondegenerate base metric, a Lorentzian spacetime, a unique path from two endpoint laws, a global synchronized clock, or semiconjugacy of independently recomputed fine and meta flows.  Each would require additional declared structure or a separate theorem.
