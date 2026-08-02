# Construction and adversarial verification: pullback geometry and timeless inference

Date: 2026-08-01
Artifact: `manuscripts/gauge_vfe_rg`
Verification target: the pullback, inference-history, and cross-scale geometry added in Chapters 5c and 5d and integrated through the general coarse-graining/RG chapters

## Binding mathematical answer

At a fixed context `c`, a statistical law is one point of the fiber `(E_x)_c`. A change from law `A` to law `B` is not one moving point without further data; it is a curve

\[
\Gamma:J\longrightarrow(E_x)_c,
\qquad \Gamma(\lambda_0)=A,
\qquad \Gamma(\lambda_1)=B.
\]

Because `varpi_x o Gamma = c`, every tangent `dot Gamma` lies in `ker T varpi_x`. The curve is therefore intrinsically vertical, independently of any connection. The parameter `lambda` is disposable bookkeeping, not primitive time. Its oriented unparameterized image represents the update history. A connection is needed only when the base projection varies and one asks which part of a total-space velocity is horizontal transport and which part is vertical statistical change.

The endpoints do not select a path, an orientation, or a duration. A realized curve has Fisher length; the Fisher--Rao distance between `A` and `B` is the infimum of such lengths and need not equal the realized length.

## The effective construction

### Covariant informational pullback

For each belief or model channel `x`, the associated statistical bundle is

\[
\varpi_x:\mathcal E_x\to\mathcal C,
\qquad
V\mathcal E_x=\ker T\varpi_x.
\]

A selected principal connection induces an Ehresmann splitting and a vertical projection `ver^{omega_x}`. For a section `s`, the connection-relative vertical first jet is

\[
D^{\omega_x}s=\operatorname{ver}^{\omega_x}\circ Ts.
\]

The descended vertical Fisher metric `g_x^F` and Amari--Chentsov tensor `T_x^A` then induce base tensors

\[
h_{s,x}^{\omega_x}(X,Y)
=g_x^F(D^{\omega_x}sX,D^{\omega_x}sY),
\]

\[
c_{s,x}^{\omega_x}(X,Y,Z)
=T_x^A(D^{\omega_x}sX,D^{\omega_x}sY,D^{\omega_x}sZ).
\]

These are globally defined and passive-gauge invariant under the stated equivariance hypotheses. They are connection-relative. If `omega' = omega + a`, the induced vertical correction `R_a` gives

\[
D^{\omega'}sX=D^\omega sX+R_a(X),
\]

so the perceived Fisher tensor acquires the two cross terms and the quadratic `g(R_aX,R_aY)` term. The bundle geometry alone therefore does not select a unique perceived base metric.

When `g_x^F` is positive definite,

\[
\operatorname{rad}h_s^\omega=\ker D^\omega s,
\qquad
\operatorname{rank}h_s^\omega=\operatorname{rank}D^\omega s.
\]

At constant rank, `T C / rad h` is a metric vector bundle. Identifying it with the tangent bundle of a quotient manifold additionally requires involutivity, a regular leaf space, and basicness of the induced tensors along the radical foliation.

### Vertical, horizontal, mixed, and section-history curves

For an arbitrary total-space curve `Gamma` with base projection `gamma`,

\[
\dot\Gamma
=H^\omega_\Gamma\dot\gamma
+\operatorname{ver}^\omega\dot\Gamma.
\]

This yields four distinct objects:

1. A constant-base curve is vertical without a connection.
2. A base curve `gamma` is a curve in the fixed manifold `C`; it needs no connection.
3. A horizontal lift of `gamma` is selected by a connection and represents comparison by parallel transport.
4. A curve with nonzero base velocity and nonzero covariant vertical velocity is mixed relative to that connection.

An agent changing its law at every context is a curve of sections, not a curve through the contextual base. If `s_r` is the history and

\[
\Sigma(r,c)=s_r(c),
\]

then `varpi Sigma(r,c)=c`; consequently `partial_r Sigma(r,c)` is vertical at every fixed `c`. The same statement holds for a coarse meta-agent section. Each history value also yields an ordered family of connection-relative perceived base semimetrics `r mapsto h_{s_r}^omega`. This is changing geometry on a fixed base, not motion of the base.

### Exact VFE orbit selection

A pair of marginal belief--model sections does not determine the dependence structure of a conditional or full recognition law. To call the configuration history an exact VFE history, the construction declares

\[
\pi_i^{\mathrm{conf}}:\mathfrak R_B\to\mathcal Q_i,
\qquad
\iota_i:\mathcal Q_i\to\mathfrak R_B,
\qquad
\pi_i^{\mathrm{conf}}\circ\iota_i=\operatorname{id}.
\]

The right-inverse condition forces the lifted conditional/full law to reproduce the displayed agent configuration; the lift carries any required correlation or copula data. At fixed outside marginal, define

\[
\overline{\mathcal F}_{B,o}(Q_i)
=\mathbb E_{Q_{B^c}}
\left[\mathcal F_{B,o}(r_B^{Q_i};Y_{B^c})\right].
\]

Under the support, positive-evidence, finiteness, and integrability hypotheses of the local--global potential theorem, plus smooth domination sufficient for differentiation under this expectation, the restricted collective VFE satisfies

\[
\mathcal F_o(Q_{B^c}r_B^{Q_i})
=C(Q_{B^c})+\overline{\mathcal F}_{B,o}(Q_i).
\]

Their differentials and natural-gradient rays agree when the same block metric is used. A single realized conditional VFE at one blanket value need not have that gradient. The exact recognition Fisher metric is the joint-law pullback

\[
\mathsf G_i^F=\iota_i^*G_{\mathfrak R_B}^F
\]

on a nondegenerate tier, or its justified quotient. A weighted sum of marginal metrics is exact only under separately established block orthogonality or fixed dependence.

VFE decrease by itself selects neither a curve nor its speed. On a regular metric inference space, the positive ray of the natural-gradient field selects an oriented unparameterized orbit:

\[
\dot Q=-v\,\operatorname{grad}^F\mathcal F_i,
\qquad v>0.
\]

Positive scalar mobility changes only parameterization. Anisotropic mobility generally changes the path. Natural-gradient integral curves are not generally geodesics.

### Emergent information duration

After the orbit has been selected, its Fisher line element defines

\[
L_F[Q]
=\int\sqrt{\mathsf G_i^F(\dot Q,\dot Q)}\,d\lambda.
\]

This is invariant under orientation-preserving reparameterization. With Fisher arclength `tau` as a representative parameter,

\[
\frac{dQ}{d\tau}
=-\frac{\operatorname{grad}^F\mathcal F_i}
{\|\operatorname{grad}^F\mathcal F_i\|_F},
\qquad
\frac{d\mathcal F_i}{d\tau}
=-\|\operatorname{grad}^F\mathcal F_i\|_F.
\]

Thus orientation comes from the VFE descent ray and duration from Fisher length. This is an emergent agent-relative information duration on the realized history. It is not identified with physical time. It can stall at critical or null segments, and a global clock on a region exists only if the normalized VFE one-form is exact, including vanishing periods.

### Meta-agent and RG geometry

If a bundle morphism `Psi:E -> Ebar` covers a base coarse map `f`, the fine and coarse sections obey `Psi o s = sbar o f`, and horizontal lifts are preserved, then

\[
D^{\bar\omega}\bar s\circ Tf
=T^V\Psi\circ D^\omega s.
\]

Without compatibility the exact first-jet formula retains a vertical mismatch term. If the fiber map is also a normalized parameter-independent Markov channel, Fisher data processing yields

\[
h_s^\omega-f^*h_{\bar s}^{\bar\omega}\succeq0.
\]

The defect is the conditional covariance of the fine score. For two composable scales it obeys the cocycle

\[
\Delta_{02}=\Delta_{01}+(T^V\Psi_{01})^*\Delta_{12}.
\]

This compares one fine history with its pushed-forward history. Independently recomputed fine and meta VFE histories agree only under an additional oriented vector-field semiconjugacy. A beta function for perceived geometry is defined only after transporting levelwise tensors to a common reference space. RG depth is a scale coordinate, not inference duration.

## Adversarial search and repairs

The following objections were required to return exact equations or counterexamples. Every surviving objection was repaired in the manuscript before closure.

| Candidate defect | Exact adversarial witness | Repair and disposition |
|---|---|---|
| Constant rank automatically gives a quotient manifold | `h=(dz-x dy)^2` has constant rank but a contact radical with `alpha wedge d alpha != 0`. | Separate the metric quotient vector bundle from a manifold quotient; require involutivity. `REPAIRED`. |
| Involutivity and a smooth leaf space suffice for tensor descent | On `R^2`, take a normal-location fiber and connection coefficient `A=e^y dx`; then `h=e^{2y}dx^2`, `rad h=span(partial_y)`, but `L_{partial_y}h != 0`. | Require horizontal/basic tensor invariance along radical leaves in addition to a regular leaf space. `REPAIRED`. |
| Perceived geometry is connection independent | A Gaussian-location section with two different connection coefficients changes `D^omega s` and hence `h`. | Give the full linear-plus-quadratic connection-change formula and label the geometry connection-relative. `REJECTED` as a general claim. |
| Any contrast function yields dualistic geometry | The contrast `(mu-nu)^4` has a degenerate second jet on the diagonal. | Require a positive-definite mixed second form; otherwise retain only possibly degenerate divergence jets. `REPAIRED`. |
| Generic contrast jets are Fisher/Amari tensors | A generic divergence has its own second and third jets. | Use `g_D` and `c_D`; identify them with Fisher/Amari only for KL or a separately proved equality case. `REPAIRED`. |
| Gauge covariance of two-point contrast comparison is automatic | Acting on only one argument changes a simultaneous-invariant contrast. | Require simultaneous represented `G` invariance and compatible parallel transport. `REPAIRED`. |
| A constant-base diagonal evaluation can be mixed | Its projected base velocity is zero, so every tangent is vertical. | Classify constant-base diagonal histories as vertical; reserve mixed for nonconstant base projection with nonzero covariant vertical part. `REPAIRED`. |
| A pair of marginal sections determines exact joint VFE | A correlated Gaussian can share both displayed marginals while changing joint Fisher and VFE data. | Require a conditional/full-law lift carrying dependence data. `REPAIRED`. |
| Any smooth map into joint laws is a lift | Map `N(mu,1)` to a joint law whose first marginal is `N(mu+1,1)`; smoothness and nondegenerate pullback do not restore the marginal. | Add `pi_conf o iota = id` and require the full law to reproduce the declared configuration. `REPAIRED`; live re-audit closed. |
| The averaged local/collective differential exists automatically | Choose `Pi_{o,B^c}=delta_0` and fixed `Q_{B^c}=delta_1`; then conditional evidence can vanish and VFE is infinite. | Import absolute-continuity, positive-evidence, finiteness, integrability, and dominated differentiation hypotheses. `REPAIRED`; live re-audit closed. |
| A realized conditional VFE has the collective coordinate gradient | Conditioning at one blanket value is not the outside expectation in the collective decomposition. | Use the outside-averaged local objective at fixed outside marginal. `REPAIRED`. |
| Natural-gradient histories are geodesics | Integral curves of `-grad F` have acceleration determined by `F`, not generally zero covariant acceleration. | Explicitly separate gradient-flow orbits from geodesics. `REJECTED` as a general claim. |
| Free/proper/isometric gauge action is enough in infinite dimensions | Orbit tangents can be nonclosed, so the quotient-speed infimum can vanish without being attained. | Restrict the standard result to finite dimensions; require a smooth principal quotient, closed split orbit tangents, and smooth orthogonal complements in section spaces. `REPAIRED`. |
| Levelwise sections alone imply coarse first-jet naturality | Without `Psi o s = sbar o f`, the two first jets are not derivatives of one commuting diagram. | Require related sections and horizontal compatibility; otherwise retain the mismatch. `REPAIRED`. |
| Every coarse map contracts Fisher geometry | Parameter-dependent fitting and deterministic Galerkin restriction do not satisfy the Markov score identity. | Restrict contraction to normalized parameter-independent Markov fiber maps. `REJECTED` as a general claim. |
| Metric contraction compares independently recomputed fine/meta flows | Two different natural-gradient vector fields need not be related by the coarse map. | State contraction only for the image of one path; require oriented semiconjugacy for separate flows. `REPAIRED`. |

## Closure verdict

The affirmative mathematical framework survives adversarial audit under its displayed hypotheses. It establishes global gauge-invariant but connection-relative informational pullbacks, the exact fixed-base vertical interpretation of law change, parameter-free oriented VFE histories, Fisher information duration, and cross-scale/meta-agent pullback geometry with explicit defect and semiconjugacy terms.

The construction deliberately does not claim that the principal bundle alone chooses a connection, that every perceived semimetric is nondegenerate, that every marginal configuration admits a smooth joint-law lift, that all section-space quotients are smooth, or that information duration is physical time. Those are named additional structures or open realization obligations, not missing steps hidden inside the proved statements.
