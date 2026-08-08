<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 12 source-level rigor reconstruction

## Binding and disposition

This record reconstructs the load-bearing probability/operator (P),
bundle/pullback/history (G), and exact-RG/asymptotic (R) results independently
from their definitions. It then records the comparison against the repaired
source and recertifies the named counterexamples. The input revision before
the Task 12 source repair was
82648b178671b2c5759a8ece1c5cd4c796d51f0d; the immutable repaired revision
\(S\) is created only after this report, the source inventory, and the final
review are frozen.

**Claim-source-map binding:** evidence/task-12-claim-source-map.json has
raw/Git-clean SHA-256
e1ed62d3757e5d96026ab39b05838246cdb3e11d3d071d45758bf6b52c2cc25c,
size 1,982,296 bytes, LF count 35,023, CRLF count 0, lone-CR count 0, and
predicted Git-clean blob OID
f89a90396d71e3acb855bc0f61934e0a91ead86f. Its binding-set digest is
9ef4f7aa3cb2b7af235a6e8834a6209fcdffa2c7cbae3ab4a6b4205c97f2baf6,
and its two-view forward/reverse validation returned PASS.

**Independent precommit source-only adversarial approval:** the raw patch for
the 14 reviewed source and SPEC files against base
82648b178671b2c5759a8ece1c5cd4c796d51f0d has 66,130 bytes and SHA-256
8a5dfef4e304180977c7b73ed03690f34c2ffbbda87aab34db8a16265cefb85f,
with zero reported defects. The additional source-governance files
`verification/claims.json` and `verification/VERIFICATION.md` are covered by
the 16-file frozen static approval below.

**Independent frozen static approval:** the 16-file patch has 70,651 bytes and
SHA-256
08a16929ea2300ddde054be4a1acae096f103d921028e7fa8aa718532c507a0a,
the source manifest digest is
75d3a7352f95a8345bf54dae95f7ca0077986d3d34cc7834aaffb61523b5a510,
and the review reported zero defects.

**Right-inverse repair addendum:** a later source-only challenge found that
05d_relational_inference.tex incorrectly made metric difference universal for
distinct smooth right inverses. The repaired source says that distinct right
inverses can, but need not, induce different pullback metrics and gives the
exact normal-location witness reconstructed in G1 below. The repaired file has
raw SHA-256
50262022bf9096f047e8cf32fe66fa9d894a497cd8652392d16fcc09b286d8e9,
size 84,308 bytes, 1,624 LF bytes comprising 1,492 CRLF and 132 LF-only line
endings, 0 lone CR, and
predicted Git-clean blob OID c62215842168dda4749de49f04affde8d31efb2f.
The refined raw one-file repair diff against 64dd6fb4 has SHA-256
3632e4f37910983ca5640a271a89705e824c400b3b040173b1627de2e7ab90a3 and size
1,674 bytes. A follow-up independent source-only semantic audit of those exact
current bytes returned APPROVED; the original adversary approved only the
preliminary core and was not reopened for the final qualifier. This is a later
post-freeze Task 13/source-repair challenge, not a result retroactively
attributed to the original Task 12 G oracle packet. This source-only approval
does not enlarge either precommit approval or the still-required immutable
full-\(S\) review.

**Immutable full-\(S\) review:** POSTCOMMIT_EXTERNAL_REQUIRED. Neither
precommit approval is mislabeled as an immutable full-\(S\) review. That
review necessarily occurs after the containing commit exists and is external
to this self-contained report, avoiding a self-reference cycle.

Task 12 does not produce Task 13 numerical evidence, Task 14 build/render
evidence, or Task 15 terminal adjudication. In particular, this report is
source-level derivation evidence, not a substitute for the later manifest,
JUnit, bibliography, PDF, auxiliary, or immutable-tree checks.

## P reconstruction: finite measure pairs, channels, and information

### P1. Mass, composition, and the coarse action

Let \(\rho\) be a probability on a standard-Borel space \(Y\), let
\(m=e^{-H}\rho\) be a finite positive measure, and let
\(K:Y\rightsquigarrow Z\) be a normalized Markov kernel. Define
\(\rho^c=\rho K\) and \(m^c=mK\). Normalization gives
\[
 \rho^c(1)=\rho(K1)=1,\qquad
 m^c(1)=m(K1)=m(1).
\]
Thus a normalized channel preserves the evidence mass of the measure pair. If
\(K_1:Y\rightsquigarrow Z\) and \(K_2:Z\rightsquigarrow W\), Tonelli's theorem
gives
\[
 (\rho K_1)K_2=\rho(K_1K_2),\qquad
 (mK_1)K_2=m(K_1K_2).
\]
The measure-pair construction is therefore an ordered functor under kernel
composition; no density chart is needed for this statement.

Disintegrate the joint reference
\(\rho(dy)K(y,dz)=\rho^c(dz)\Pi_\rho(z,dy)\). Then
\[
 \frac{d(mK)}{d(\rho K)}(z)
 =\int_Y e^{-H(y)}\Pi_\rho(z,dy)
\]
for \(\rho^c\)-almost every \(z\), and hence
\[
 H^c(z)
 =-\log\int_Y e^{-H(y)}\Pi_\rho(z,dy)
\]
with the usual \(+\infty\) convention when the conditional integral vanishes.
Changing a density representative changes the displayed action only on a
\(\rho^c\)-null set; the finite measure pair remains primary.

For a bounded direction \(\varphi\), set
\[
 Q_z(t):=-\log\int e^{-t\varphi(y)}\Pi_\rho(z,dy).
\]
Differentiation under the bounded integral gives
\[
 Q_z'(0)=\mathbb E[\varphi(Y)\mid Z=z],\qquad
 Q_z''(0)=-\operatorname{Var}(\varphi(Y)\mid Z=z).
\]
The negative sign in the Hessian is forced by the negative conditional
log-Laplace convention. The normalized-probability chart adds the scalar
\(\log\rho(e^{-t\varphi})\); its derivatives consequently differ by the
unconditional mean and covariance terms. The two charts agree only modulo
constants.

### P2. Conditional expectation as a contraction

Write
\[
 U\varphi(z):=\int\varphi(y)\Pi(z,dy)
             =\mathbb E_\pi[\varphi(Y)\mid Z=z],
\]
where \(\pi=m/m(1)\), \(\pi^c=\pi K\), and \(\Pi\) is a fixed reverse
conditional law. Conditional Jensen gives, for every \(1\leq p<\infty\),
\[
 \|U\varphi\|_{L^p(\pi^c)}^p
 \leq\int U(|\varphi|^p)\,d\pi^c
 =\|\varphi\|_{L^p(\pi)}^p.
\]
The essential-supremum definition gives the \(p=\infty\) case. Also
\(\pi^c(U\varphi)=\pi(\varphi)\), so constants and means are preserved for all
\(p\). For \(p=2\), the orthogonal-projection identity is exact:
\[
 \|\varphi\|_2^2-\|U\varphi\|_2^2
 =\mathbb E_\pi\!\left[\operatorname{Var}(\varphi\mid Z)\right].
\]
Equality holds exactly when \(\varphi=U\varphi(Z)\) almost surely, equivalently
when the tested direction is measurable with respect to the retained
sigma-algebra.

For a reverse kernel \(\Pi\), its Dobrushin coefficient is
\[
 \delta(\Pi):=\sup_{z,z'}\|\Pi(z,\cdot)-\Pi(z',\cdot)\|_{\rm TV}.
\]
The oscillation seminorm obeys
\[
 \operatorname{osc}(U\varphi)
 \leq\delta(\Pi)\operatorname{osc}(\varphi).
\]
This is the operator norm on the bounded-function quotient by constants. The
zero branch must be retained: if \(\delta(\Pi)=0\), all rows agree, so
\(U\varphi\) is constant and the quotient operator is exactly zero. A
logarithm of \(\delta\) is therefore not a universally finite rate
coordinate.

### P3. DQM transfer and Fisher equality

Let a family \(P_\theta\) be differentiable in quadratic mean at
\(\theta_0\), with vector score \(s\in L^2_0(P_{\theta_0})\). For a small
increment \(h\), the square-root expansion consists of its absolutely
continuous linear part plus a singular remainder whose total mass is
\(o(\|h\|^2)\). Lift the experiment to
\[
 M_\theta(dy,dz)=P_\theta(dy)K(y,dz).
\]
Because \(K\) is parameter independent, the joint likelihood ratio and joint
score depend only on \(y\), and the same singular \(o(\|h\|^2)\) bound survives
the lift. Marginalization to \(z\) is a Markov map, hence an \(L^2\) contraction
of square roots. The output family \(P_\theta K\) is DQM with score
\[
 s^c(z)=\mathbb E_{\theta_0}[s(Y)\mid Z=z].
\]
Consequently
\[
 I^c=\mathbb E[s^c(s^c)^\mathsf T]\preceq
 I=\mathbb E[ss^\mathsf T],
\]
and for every tangent vector \(u\),
\[
 u^\mathsf T(I-I^c)u
 =\mathbb E\!\left[
   \operatorname{Var}(u^\mathsf Ts\mid Z)\right].
\]
Matrix equality holds exactly when every score component, equivalently every
tested scalar score \(u^\mathsf Ts\), is \(Z\)-measurable almost surely. This
is a local equality at the stated parameter; it does not alone prove global
sufficiency or recovery of the experiment.

### P4. The circle topology probe

On the unit circle with Haar probability \(\lambda\), let
\(D(x)=2x\bmod1\) and \(U f=f\circ D\). Haar invariance makes \(U\) an
isometry on \(L^\infty(\lambda)\), so
\[
 r_{L^\infty}(U)=1.
\]
For periodic \(C^\alpha\), \(0<\alpha\leq1\), equipped with the
sup-plus-Holder norm,
\[
 [f\circ D^n]_\alpha\leq2^{\alpha n}[f]_\alpha.
\]
The Fourier mode \(f(x)=e^{2\pi i x}\) has
\([f\circ D^n]_\alpha\) of order \(2^{\alpha n}\), so the upper bound is sharp:
\[
 r_{C^\alpha}(U)=2^\alpha.
\]
Thus relevance is a statement in a declared operator topology, not a property
of the kernel formula alone.

For the noisy operator
\[
 U_\epsilon f=(1-\epsilon)f\circ D
 +\epsilon\int f\,d\lambda,\qquad0<\epsilon<1,
\]
the associated rows have Dobrushin coefficient \(1-\epsilon\). Constants form
an eigenline with eigenvalue one, while the Haar-mean-zero invariant subspace
satisfies \(U_\epsilon=(1-\epsilon)U\). Hence
\[
 r_{C^\alpha}(U_\epsilon)
 =\max\{1,(1-\epsilon)2^\alpha\}.
\]
At \(\alpha=1,\epsilon=1/4\), the full Holder spectral radius is \(3/2\)
although the \(L^\infty/\mathbb R\mathbf1\) contraction coefficient is
\(3/4\). Dobrushin controls the oscillation quotient; it does not control the
Holder seminorm or delete the constant eigenline.

### P5. Product-reference obstruction

Let a deterministic channel clone a uniform bit:
\(x\mapsto(x,x)\). Its output law gives positive mass to both diagonal atoms
and zero mass to both off-diagonal atoms. Any product probability equivalent
to that output would have two marginals charging both bit values and would
therefore give positive mass to the off-diagonal atoms, a contradiction. The
nonatomic diagonal embedding is similarly singular with respect to every
product of its nondegenerate marginals. Exact pushforward of a law therefore
does not imply admission into a product-reference interaction chart.

## G reconstruction: bundles, pullbacks, and histories

### G1. Pullback geometry and gauge scope

Let \(\pi:E\to C\) and \(\bar\pi:\bar E\to\bar C\) be associated statistical
bundles with connections \(\omega,\bar\omega\), fiber Fisher metrics
\(g^F,\bar g^F\), and sections \(s,\bar s\). The vertical covariant derivative
is
\[
 D^\omega s=\operatorname{ver}^{\omega}\circ Ts,
\]
and the section-induced base tensor is
\[
 h_s^\omega=(D^\omega s)^*g^F.
\]
A passive gauge change simultaneously changes the local frame, the
representatives of \(s\) and \(\omega\), and the coordinate components of
\(g^F\). The geometric tensor \(h_s^\omega\) is unchanged by that coordinated
redescription. This covariance is not active-gauge invariance at fixed
connection. Replacing \(\omega\) changes the horizontal/vertical split and
generally changes \(D^\omega s\) and \(h_s^\omega\). The construction is
therefore section- and connection-relative.

#### Post-freeze repair: right-inverse configuration metrics

The later source-only challenge establishes that, in general, configuration
extraction data do not determine a pullback metric without a selected lift.
Consider the normal location family
\(N((\theta,\eta),I_2)\), whose Fisher metric is
\(d\theta^2+d\eta^2\), and let \(\pi(\theta,\eta)=\theta\). For every
constant \(c\ne0\),
\[
 \iota_0(x)=(x,0),\qquad \iota_c(x)=(x,c),\qquad
 \iota_\Delta(x)=(x,x)
\]
are smooth right inverses of \(\pi\). Their derivatives are respectively
\((1,0)\), \((1,0)\), and \((1,1)\), so
\[
 \iota_0^*g^F=\iota_c^*g^F=dx^2,
 \qquad
 \iota_\Delta^*g^F=2dx^2.
\]
Thus distinct right inverses can induce the same metric, while another right
inverse of the same extraction can induce a different one. The valid boundary
is that the lift must be declared as additional metric data unless a separate
uniqueness, canonicity, or lift-independence theorem is proved, not that
distinct lifts must always give distinct metrics.

### G2. Covariant jet chain rule and anomaly

Let \(\Psi:E\to\bar E\) be a bundle morphism over \(f:C\to\bar C\), suppose
\(\Psi\circ s=\bar s\circ f\), and write \(L=T^V\Psi\). With
\(\operatorname{hor}^\omega_eX\) denoting the horizontal lift, define the
vertical horizontal anomaly by the fixed sign convention
\[
 A_\Psi(e;X)
 :=T\Psi(\operatorname{hor}^\omega_eX)
   -\operatorname{hor}^{\bar\omega}_{\Psi(e)}(TfX).
\]
Splitting \(TsX\) into horizontal and vertical parts and differentiating the
related-section square gives the exact chain rule
\[
 D^{\bar\omega}\bar s(TfX)
 =L(D^\omega s(X))+A_\Psi(s(c);X).
\]
Thus the commutative value square alone does not commute first jets. The
anomaly vanishes exactly when \(T\Psi\) maps the relevant fine horizontal
lifts to the coarse horizontal lifts; compatible connections are a
sufficient global way to impose that condition.

For composable arrows \(0\to1\to2\), the anomaly is ordered:
\[
 A_{02}(e;X)
 =T^V\Psi_{12}\!\left(A_{01}(e;X)\right)
 +A_{12}\!\left(\Psi_{01}(e);Tf_{01}X\right).
\]
The image point and pushed base vector are part of the type. Composite
vanishing requires cancellation of these two typed terms and does not force
either factor anomaly to vanish.

### G3. Fisher defects and the nonadditive base residual

Whenever the vertical fiber arrow is induced by a normalized
parameter-independent Markov channel, define
\[
 \Delta_{01}:=g_0^F-L_{01}^*g_1^F\succeq0.
\]
For composable arrows, pure algebra gives the unconditional vertical cocycle
\[
 \Delta_{02}
 =\Delta_{01}+L_{01}^*\Delta_{12}.
\]
No anomaly appears because this identity is entirely vertical.

The pullback base defects
\(\delta_{jk}:=(D^{\omega_j}s_j)^*\Delta_{jk}\) need not be additive. Put
\[
 v_X=L_{01}(D^{\omega_0}s_0X),\qquad
 A_X=A_{01}(s_0;X),\qquad
 u_X=v_X+A_X=D^{\omega_1}s_1(Tf_{01}X).
\]
Pulling back the vertical cocycle and subtracting the second-stage base defect
gives
\[
\begin{aligned}
 \delta_{02}(X,Y)-\delta_{01}(X,Y)
 -(f_{01}^*\delta_{12})(X,Y)
 &=\Delta_{12}(v_X,v_Y)-\Delta_{12}(u_X,u_Y)\\
 &=-\Delta_{12}(v_X,A_Y)
   -\Delta_{12}(A_X,v_Y)
   -\Delta_{12}(A_X,A_Y).
\end{aligned}
\]
On the diagonal this is
\[
 -2\Delta_{12}(v_X,A_X)-\Delta_{12}(A_X,A_X).
\]
Hence the sharp additive base cocycle holds exactly when the two
\(\Delta_{12}\)-quadratic forms on \(v_X\) and \(u_X\) agree for every \(X\).
Vanishing \(A_{01}\) is sufficient but not necessary.

For one arrow, inserting the jet chain rule into the two pullback metrics gives
\[
\begin{aligned}
 h_s^\omega(X,X)-f^*h_{\bar s}^{\bar\omega}(X,X)
 ={}&\Delta_\Psi(D^\omega sX,D^\omega sX)\\
 &-2\bar g^F(LD^\omega sX,A_\Psi)
 -\bar g^F(A_\Psi,A_\Psi).
\end{aligned}
\]
Thus a nonzero anomaly may preserve or reverse the base order. Fiber Fisher
contraction alone supplies no unconditional base-metric contraction.

### G4. Descent and the five curve types

Let \(f:C\to\bar C\) be a surjective smooth submersion and set
\(t=\Psi\circ s\). A section \(\bar s\) satisfying
\(t=\bar s\circ f\) exists exactly when \(t(c)=t(c')\) whenever
\(f(c)=f(c')\); under the submersion hypothesis this value-level condition
gives a unique smooth descent. The infinitesimal condition \(Tt(V)=0\) for
\(V\in\ker Tf\) proves constancy only on connected components of fibers, so it
does not replace the global fiber-constancy condition when fibers are
disconnected. If \(f\) is not a submersion, a continuous set-theoretic descent
need not be smooth.

Five notions must remain separate.

1. A fixed-fiber vertical curve \(\gamma(r)\subset E_c\) has
   \(\pi\gamma(r)=c\) and requires no base connection.
2. A base curve \(c(r)\subset C\) has a connection-relative horizontal lift
   after an initial total-space point is chosen.
3. A horizontal total-space curve \(e(r)\) satisfies
   \(\omega(\dot e)=0\).
4. A mixed total-space curve has both horizontal and vertical components; its
   vertical component depends on the chosen connection.
5. A curve of sections \(r\mapsto s_r\) changes an entire field over \(C\);
   it is not a curve inside one statistical fiber.

The Fisher length of a regular statistical or configuration path,
\[
 \mathcal L(\gamma)=\int
 \sqrt{g_{\gamma(r)}(\dot\gamma(r),\dot\gamma(r))}\,dr,
\]
is invariant under orientation-preserving reparameterization and therefore
defines an intrinsic path duration after the metric and path are chosen. It
does not select an origin, orientation, synchronization between agents, or a
primitive physical time. A Fisher-null segment can stall this duration, and a
connection or metric change changes the construction.

### G5. Exact history semiconjugacy

Let \(X\) and \(\bar X\) be \(C^1\) vector fields with maximal flows
\(\Phi_t\) and \(\bar\Phi_\tau\), and let \(R\) be \(C^1\). Independently
computed oriented histories agree along a fine orbit precisely when
\[
 TR\,X=a\,(\bar X\circ R)
\]
there with a continuous strictly positive factor \(a\), together with the
required existence on the corresponding maximal intervals. If the fine
maximal interval through \(Q\) is \((\alpha,\beta)\), define
\[
 \sigma_Q(t)=\int_0^t a(\Phi_sQ)\,ds.
\]
Uniqueness of the coarse ODE gives
\[
 R(\Phi_tQ)=\bar\Phi_{\sigma_Q(t)}(RQ)
\]
on the accumulated image interval
\[
 \Sigma_Q=
 \left(\lim_{t\downarrow\alpha}\sigma_Q(t),
       \lim_{t\uparrow\beta}\sigma_Q(t)\right).
\]
This interval lies inside the coarse maximal interval. Full traversal holds
if and only if its two endpoint limits equal the two endpoints of that coarse
maximal interval. When both flows are complete on \(\mathbb R\), this is
equivalent to divergence of the two improper integrals of \(a\) along the fine
orbit. A positive uniform lower bound is sufficient, not necessary.

At a coarse critical point \(\bar X(RQ)=0\), the vector equation forces
\(TRX=0\) but imposes no pointwise algebraic value on \(a(Q)\). Continuity from
nearby regular points may uniquely determine, permit many, or obstruct a
strictly positive extension. The claim that the factor is always arbitrary
at a critical point is therefore too strong.

The endpoint distinction is witnessed in both directions. For
\(X=\partial_x\), \(\bar X=\partial_y\), and \(R(x)=\arctan x\),
\(a(x)=(1+x^2)^{-1}>0\), but \(\Sigma=(-\pi/2,\pi/2)\) although both ambient
flows are complete. For \(R(x)=\operatorname{arsinh}x\),
\(a(x)=(1+x^2)^{-1/2}\) has infimum zero while
\(\sigma(t)=\operatorname{arsinh}t\) spans all of \(\mathbb R\).

Finally, equality of objective functions does not imply natural-gradient
semiconjugacy. The differential is metric independent, whereas
\(-G^{-1}dF\) depends on \(G\). With \(R=\mathrm{id}\),
\(F=(x^2+2y^2)/2\), and metrics
\(\operatorname{diag}(1,1)\) and \(\operatorname{diag}(1,\kappa)\),
colinearity on \(xy\ne0\) forces both \(a=1\) and \(\kappa=1\). A metric
compatibility or horizontal-conformality hypothesis is therefore load
bearing.

## R reconstruction: typed RG, beta functions, and asymptotics

### R1. Ordered cocycles and comparison-space beta

For typed scale maps \(R_{k\leftarrow\ell}:X_\ell\to X_k\),
\[
 R_{m\leftarrow\ell}
 =R_{m\leftarrow k}\circ R_{k\leftarrow\ell}.
\]
Differentiation at \(x\) gives the ordered derivative cocycle
\[
 D R_{m\leftarrow\ell}(x)
 =D R_{m\leftarrow k}(R_{k\leftarrow\ell}x)
  \circ D R_{k\leftarrow\ell}(x).
\]
If compatible typed modes satisfy
\[
 M_\ell v_\ell=\lambda_\ell v_{\ell+1},
\]
then the accumulated scalar multiplier is the ordered product
\(\prod_{\ell}\lambda_\ell\). This is not an ordinary eigenvalue equation
until the adjacent tangent spaces have been explicitly identified.

Let \(J_\ell:X_*\to X_\ell\) be declared isomorphisms and let
\(T_\ell:X_\ell\to X_{\ell+1}\). The reference-space step and discrete beta
are
\[
 \widehat T_\ell=J_{\ell+1}^{-1}T_\ell J_\ell,\qquad
 \beta_\ell(g)=
 \frac{\widehat T_\ell(g)-g}{\log b_\ell}.
\]
Without the \(J_\ell\), \(T_\ell g-g\) subtracts vectors in different spaces
and is ill typed. Changing \(J_\ell\) changes beta even when every native
step is the identity, so the comparison scheme is part of the result.

### R2. Reference changes and retained residuals

Suppose \(\rho'=e^{-\Delta}\rho\) is a bounded normalized reference change and
the same finite measure is represented by
\(e^{-H}\rho=e^{-H'}\rho'\). Then \(H'=H-\Delta\). If
\[
 R_K^H[H;\rho]
 =-\log\frac{d((e^{-H}\rho)K)}{d(\rho K)},
\]
the chain rule for Radon-Nikodym derivatives gives the inhomogeneous law
\[
 R_K^H[H';\rho']
 =R_K^H[H;\rho]-R_K^H[\Delta;\rho].
\]
Thus a law fixed point does not automatically define an action fixed point:
the reference cocycle contributes an affine term.

Let \(I_\ell:G_\ell^{\rm ret}\to G_\ell^{\rm full}\) be a retained
reconstruction and \(P_\ell I_\ell=I\). For an exact full interaction step
\(T_\ell\), decompose
\[
 T_\ell I_\ell g
 =I_{\ell+1}P_{\ell+1}T_\ell I_\ell g
  +\mathcal E_\ell(g),
\qquad
 \mathcal E_\ell(g)
 =(I-I_{\ell+1}P_{\ell+1})T_\ell I_\ell g.
\]
The retained beta is exact on the admitted retained image if and only if
\(\mathcal E_\ell(g)=0\) for every admitted \(g\), equivalently
\[
 T_\ell(\operatorname{im}I_\ell)
 \subseteq\operatorname{im}I_{\ell+1}.
\]
Projection idempotence alone does not imply this invariance; a zero retained
beta may coexist with a nonzero omitted exact component.

### R3. Fixed objects and monodromy

A fixed law, a fixed action relative to a reference, a fixed exact
interaction, a fixed retained interaction, an invariant bundle section, and a
fixed configuration are predicates in different categories. None transfers
to another tier without a stated commuting and sufficiently faithful bridge.
For a period-\(p\) nonautonomous scheme, the relevant endomorphism is the
ordered monodromy
\[
 \mathcal M_\ell
 =T_{\ell+p-1}\circ\cdots\circ T_\ell
\]
after the required reference-space identifications. A monodromy-fixed object
may lie on a nontrivial \(p\)-cycle and need not be fixed by any one-step map.
The same warning applies to reference-space modes: a scalar spectrum is a
property of the identified monodromy, not of an untyped cross-scale arrow.

### R4. Exact path coarse graining

For the unweighted path \(P_m\), its combinatorial Laplacian has eigenvalues
\[
 \lambda_{m,k}=2-2\cos\frac{\pi k}{m},
 \qquad k=0,\ldots,m-1.
\]
If \(b\mid m\) and \(S:\mathbb R^{m/b}\to\mathbb R^m\) is the unnormalized
block-constant prolongation, every internal fine edge has zero difference and
each interblock boundary contributes once. Hence the Galerkin identity is
\[
 S^\mathsf T L_mS=L_{m/b},\qquad S^\mathsf TS=bI.
\]
Iteration gives the same identity at every admissible depth; using an
isometric prolongation instead would introduce the corresponding mass
normalization and must not be silently mixed with this convention.

For \(0\leq\lambda<4\), set
\(\theta(\lambda)=\arccos(1-\lambda/2)\). The exact normalized counts are
\[
\begin{aligned}
 N_m(\lambda)
 &=\frac{1+\lfloor m\theta(\lambda)/\pi\rfloor}{m},\\
 U_m(\lambda)
 &=\frac{\lfloor m\theta(\lambda)/\pi\rfloor}{m},
\end{aligned}
\]
where \(U_m\) excludes the zero mode; both are clipped to their evident
endpoint values outside \([0,4]\). At every continuity point,
\[
 N_m(\lambda),U_m(\lambda)\longrightarrow
 N(\lambda)=\frac1\pi\arccos(1-\lambda/2),
\]
and \(N(\lambda)\sim\sqrt{\lambda}/\pi\) as \(\lambda\downarrow0\).

If \(m=b^L\), then at every fixed depth \(r\), the coarse size
\(b^{L-r}\to\infty\) and the thermodynamic spectral law survives. At maximal
depth \(r=L\), the graph has one vertex and spectral measure \(\delta_0\).
Taking the thermodynamic limit at fixed depth and taking maximal depth first
therefore do not commute.

### R5. Abelian heat asymptotics

Let the zero-mode-excluded lower-edge count satisfy
\[
 U(\lambda)\sim c\lambda^\alpha L(1/\lambda),
 \qquad \lambda\downarrow0,
\]
with \(\alpha>0\) and \(L\) slowly varying. Karamata's Abelian theorem for the
Laplace-Stieltjes transform gives
\[
 Z(t):=\int_{(0,\infty)}e^{-t\lambda}\,dU(\lambda)
 \sim c\Gamma(\alpha+1)t^{-\alpha}L(t).
\]
Likewise its \(k\)-th tilted moment numerator has the asymptotics obtained by
adding \(\lambda^k\). For the normalized heat-tilted law,
\[
 t\,\mathbb E_t[\lambda]\to\alpha,\qquad
 t^2\,\mathbb E_t[\lambda^2]\to\alpha(\alpha+1),
\qquad
 t^2\operatorname{Var}_t(\lambda)\to\alpha.
\]
This is the Abelian direction. No converse from heat moments to a regularly
varying counting law is asserted without separate Tauberian hypotheses.

### R6. Gaussian Hermite replication

Let \(X_1,\ldots,X_b\) be independent standard normal variables and
\(Z=b^{-1/2}\sum_iX_i\). For normalized probabilists' Hermites
\(e_k=\operatorname{He}_k/\sqrt{k!}\), joint Gaussian regression yields
\[
 \mathbb E[e_k(X_1)\mid Z]=b^{-k/2}e_k(Z).
\]
The replicated score operator
\[
 \mathcal L_bh=b\,\mathbb E[h(X_1)\mid Z]
\]
therefore satisfies
\[
 \mathcal L_be_k=b^{1-k/2}e_k.
\]
All displayed eigenvalues are nonzero and tend to zero. On the declared
centered \(L^2\) Hermite tier, finite Hermite sums lie in the range, so the
range is dense. It is not closed because the diagonal multipliers tend to
zero; equivalently, a sequence with square-summable coefficients after
multiplication need not have square-summable coefficients before division.
The kernel is trivial, while the range is dense and not all of the space.
Thus zero belongs to the continuous spectrum, not the point spectrum. The
formula uses scalar independence and the unit-variance block normalization;
correlated or multivariate extensions require separate statements.

## Counterexample recertification and named probes

The following constructions were recomputed from their definitions. They are
not accepted merely because they appeared in an earlier report.

### Weighted one-space nonlinearity witness

Let
\[
 B=c_0(5^n)
 =\left\{f:\|f\|_w:=\sup_n5^{-n}|f_n|<\infty,\
                 5^{-n}f_n\to0\right\}.
\]
Define
\[
 (Uf)_n=\frac{f_0+f_{n+1}}2,\qquad
 Q(f)_n=-\log\frac{e^{-f_0}+e^{-f_{n+1}}}{2}.
\]
The function
\(\varphi_n=\tfrac13+\tfrac23\,4^n\) belongs to \(B\) and direct substitution
gives \(U\varphi=2\varphi\). Thus the bounded linear operator has a relevant
eigenvalue on this one-space chart.

For \(a_N=5^{-N/2}\), let \(f^{(N)}\) have its only nonzero coordinate at
\(N+1\), with value \(A_N=a_N5^{N+1}\). Then
\(\|f^{(N)}\|_w=a_N\to0\), while at coordinate \(N\),
\[
 Q(f^{(N)})_N=-\log\frac{1+e^{-A_N}}2,\qquad
 (Uf^{(N)})_N=\frac{A_N}{2}.
\]
Because the first expression tends to \(\log2\),
\[
 \liminf_N
 \frac{\|Q(f^{(N)})-Uf^{(N)}\|_w}{\|f^{(N)}\|_w}
 \geq\frac52.
\]
Therefore \(U\) is not the Frechet derivative of \(Q\) at zero in this
weighted norm. This recertifies CE-WEIGHTED-FRECHET and forbids a
weighted-one-space identification of linear spectral relevance with
nonlinear action analyticity.

### Twelve probability, ELBO, and observation witnesses

| register ID | independent reconstruction | conclusion |
|---|---|---|
| CE-MOVING-ATOM | If one sigma-finite measure dominated \(\mu_\theta=\tfrac12\delta_\theta+\tfrac12N(0,1)\) for every \(\theta\in\mathbb R\), it would assign positive mass to every singleton. A sigma-finite measure has at most countably many positive-mass atoms, by a countable finite-measure cover and positive-mass thresholds. | No common sigma-finite dominator exists for the moving uncountable atomic support. |
| CE-NONMEASURABLE-VERSION | On \([0,1]^2\), choose non-Borel \(N\) and set \(p(o\mid x)=1+1_N(x)1_{\{x\}}(o)\) relative to Lebesgue measure in \(o\). Each section integrates to one and represents the uniform law, but the set \(\{(x,o):x\in N,\ o=x\}\) is not Borel; otherwise its pullback by \(x\mapsto(x,x)\) would make \(N\) Borel. | Pointwise density versions do not supply joint parameter-observation measurability. |
| CE-PARTITION-COFINALITY | Let \(C=[0,1/3]\). No finite dyadic partition refines \(\{C,C^c\}\), since that would make \(C\) a finite union of dyadic cells, whose endpoints are dyadic rationals. | One generating sequence of finite partitions is not cofinal among all finite measurable partitions. |
| CE-SIGMAFINITE-DECREASING | For counting measure on \(\mathbb N\), \(C_n=\{n,n+1,\ldots\}\downarrow\varnothing\), but every \(\nu(C_n)=\infty\). | Continuity from above needs a finite first set; sigma-finite proofs must localize to finite-measure pieces. |
| CE-TC-DIAGONAL | If \(U\) is uniform on \([0,1]\), the law of \((U,U)\) gives the diagonal mass one, while the product of its uniform marginals gives the diagonal mass zero. | The joint law is singular to the product law and its total correlation is \(+\infty\); finite entropy subtraction is unavailable. |
| CE-H4-CANCELLATION | Normalize \(q_n\propto[n(\log n)^2]^{-1}\), \(n\geq2\), and take a bounded nonconstant positive tilt \(r\), bounded away from zero, with \(E_qr=1\). Then \(E_q\log q=E_q\log(qr)=-\infty\), but the relative-log values are \(0\) and \(E_q\log r=-\mathrm{KL}(q\Vert qr)<0\). | The extended relative-measure ELBO is primary; the classical split needs the stated integrability hypothesis H4. |
| CE-INFINITE-DPI-EQUALITY | Map \(a\mapsto u\) and \(b,c\mapsto v\), with \(P=(\delta_a+\delta_b)/2\) and \(Q=(\delta_b+\delta_c)/2\). Fine and coarse KL are both \(+\infty\). Recovery would require \(L(v)=Q\) and \(L(u)=2P-Q\), but the latter has coefficient \(-1/2\) at \(c\). | Equality \(+\infty=+\infty\) in data processing has no recovery consequence. |
| CE-RCP-EXCEPTION | For independent uniform \((O,X)\), both the uniform conditional kernel and the version changed to \(\delta_0\) at \(O=0\) are regular conditional probabilities. Pushing them through any nonconstant deterministic function of \(X\) gives different pointwise values at that exceptional observation. | A fine measurable RCP version must be fixed as model data before a pointwise pushed conditional is asserted. |
| CE-BLOCK-EVIDENCE | For \(p_J(y_1,y_2)\propto e^{Jy_1y_2}\) on \(\{-1,1\}^2\), \(J\ne0\), one exact mean-field coordinate update has \(q_1(y_1)\propto e^{Jm_2y_1}\), but \(q_1q_2\) remains a product and cannot equal the correlated posterior. The update maximizes the common ELBO in that coordinate, yet leaves a positive posterior gap. | Coordinate ascent increases the shared bound; evidence ascent in an EM comparison needs the old bound to be tight, not merely one exact block update. |
| CE-ATTENTION-CORRELATION | Let two conditional labels be equal almost surely and uniform on \(\{0,1\}\). Both row marginals are uniform, but the joint has two atoms rather than four and its total correlation is \(\log2\). | Fixed or latent-independent row marginals do not imply conditional row independence or a product-row ledger. |
| CE-ATTENTION-EXTRA-RECORD | With equal label prior and equal displayed energies, add \(R\) with \(P(R=1\mid J=0)=1/4\) and \(P(R=1\mid J=1)=3/4\). At \(R=1\), the energy-only row is \((1/2,1/2)\), whereas Bayes gives \((1/4,3/4)\). | A softmax row is exact only when the complete selected-record likelihood is label exclusive up to a label-independent residual. |
| CE-OBSERVATION-DELETION | For \(Y\sim\operatorname{Bernoulli}(1/2)\) and message \(O=Y\), conditioning gives \(P(Y\mid O=o)=\delta_o\); deleting \(O\) gives the nondegenerate prior. | Recasting an observation as an environment-agent message preserves the observation sigma-algebra; it does not erase conditioning. |

### Right-inverse pullback-metric witness

The normal-location computation in G1 recertifies
CE-RIGHT-INVERSE-SAME-METRIC. The distinct right inverses \(\iota_0\) and
\(\iota_c\) have the same differential and therefore the same pullback
\(dx^2\), whereas \(\iota_\Delta\) pulls back the same ambient Fisher metric
to \(2dx^2\). This simultaneously refutes the false universal and preserves
the weaker nonuniqueness conclusion: extraction data do not in general fix a
lift or the resulting configuration Fisher metric. A separate uniqueness,
canonicity, or lift-independence theorem can remove that extra choice.

### Remaining required probes

| probe | result |
|---|---|
| Reset channel | A channel to one point has \(U\varphi=E\varphi\), hence zero on the centered quotient. This sustains the explicit \(\delta=0\) Dobrushin branch and refutes any positive lower bound on pushed Fisher score norm. |
| Deterministic channel | Conditional expectation becomes composition with the retained statistic; equality in \(L^2\)/Fisher holds exactly for retained-measurable directions, not for every direction. Diagonal cloning additionally fails product-reference admission. |
| Circle norms | The same doubling kernel has radius \(1\) on \(L^\infty\) and \(2^\alpha\) on sup-plus-Holder \(C^\alpha\); the noisy version has quotient coefficient \(1-\epsilon\) but full Holder radius \(\max\{1,(1-\epsilon)2^\alpha\}\). |
| Nonclosed projection/range | Hermite multipliers \(b^{1-k/2}\to0\) give a dense nonclosed range and continuous spectrum at zero. Finite-dimensional truncation would hide this obstruction. |
| Cross-scale subtraction | The expression \(T_\ell g-g\) is undefined for \(g\in X_\ell\) and \(T_\ell g\in X_{\ell+1}\) until comparison maps \(J_\ell\) are supplied; moving \(J_\ell\) can create a nonzero beta for identity native steps. |
| Vertical/horizontal confusion | A fixed-fiber curve requires no connection, while horizontal or mixed total-space curves over a moving base do. Pullback duration of a curve of sections is a third construction and supplies no canonical clock. |
| Independently optimized histories | Equal objectives with unequal metrics fail natural-gradient semiconjugacy. The arctan witness shows incomplete traversal despite positive factor; the arsinh witness shows full traversal despite zero factor infimum. |
| Right-inverse metric scope | Distinct smooth right inverses need not have distinct pullback metrics: the two constant normal-location lifts both give \(dx^2\), while the diagonal lift gives \(2dx^2\). Extraction data therefore do not determine the metric in general; a separate uniqueness, canonicity, or lift-independence theorem can remove the lift choice. |

The arctan and arsinh calculations recertify CE-PARTIAL-TRAVERSAL and
CE-FULL-TRAVERSAL-ZERO-INF. The noisy-circle calculation recertifies
CE-NOISY-CIRCLE. The exact normal-location calculation recertifies
CE-RIGHT-INVERSE-SAME-METRIC.

## Source comparison and repair table

The independent P/G/R reconstruction was compared against the current source
by stable file and theorem/equation locators. The following were source defects
or missing hypotheses and were repaired. Items not listed here were equivalent
presentations or stronger source statements whose hypotheses remained visible.

| seam | stable source locator | repair verified at source level |
|---|---|---|
| Belief/model bundle bridge | 02_geometry.tex, product-bundle and mapping-bundle paragraphs | Separates the two principal bundles from a declared principal comparison map and equivariant fiber map; the product bundle creates neither automatically. |
| Measure action and Jacobian | 03_probability.tex, density-version paragraph following the pushforward action | Makes the group action measure level; a density and its base-measure Jacobian transform together. |
| Passive gauge convention | 06_general_coarsegraining.tex, transported parent-law and root-frame equations | Uses one old-to-new represented map consistently for laws, channels, and holonomy conjugation. |
| Shared-link admissibility | 04_generative.tex, shared-link admissibility equation | Distinguishes the fixed-datum solution family from the setwise stabilizer group and removes the false closure implication. |
| Pullback quotient regularity | 05c_pullback_geometry.tex, pullback rank quotient theorem | Requires a smooth Hausdorff quotient, surjective-submersion quotient map, exact tangent kernel, and basic tensors; involutivity alone is not enough. |
| Local VFE differentiation | 05d_relational_inference.tex, eq:hist-chartwise-vfe-envelope | Adds joint measurability and compact-chart \(L^1\) envelopes through second order before differentiating the outside expectation. |
| Right-inverse metric scope | 05d_relational_inference.tex, joint-law versus weighted-product Fisher comparison | Replaces the false universal by the sharp statement that distinct smooth right inverses can, but need not, induce different pullback metrics; the two constant lifts and the diagonal lift supply both sides of the boundary. |
| Critical semiconjugacy factor | 05d_relational_inference.tex, factor regularity paragraph | States algebraic underdetermination at a critical point while retaining the separate continuity-extension obligation. |
| History interval endpoints | 05d_relational_inference.tex, eq:hist-semiconjugacy-endpoint-image and eq:hist-complete-semiconjugacy-integrals | Replaces lower-bound necessity by the exact endpoint/improper-integral criterion and includes arctan/arsinh witnesses. |
| Exact independent-orbit length | 05d_relational_inference.tex, independent-history witness | Replaces a decimal-only assertion by the exact integral \(\int_0^1\sqrt{1+16u^6}\,du>\sqrt2\). |
| Anomaly base point | 05c_pullback_geometry.tex, horizontal-anomaly chain rule and base-defect cocycle | Evaluates each anomaly at the image point and pushed base vector and retains the exact nonadditive residual. |
| Duration scope | 05d_relational_inference.tex, Fisher-duration and semiconjugacy discussion | Separates orbit parameter, Fisher length, metric dilation, and scale depth; no primitive clock is inferred. |
| Operator category | 07_general_renormalization.tex and SPEC.md, state-category declaration | Declares Banach spaces and bounded linear maps for the analytic operator tier rather than treating an operator as a set map. |
| Abstract versus kernel composition | 07_general_renormalization.tex, eq:rg-right-acting-kernel-composition | Separates categorical composition from right-acting kernel juxtaposition and records the reversed written order. |
| Path RG and Galerkin normalization | 07_general_renormalization.tex, prop:rg-noncommuting-limits | Adds exact contiguous-block quotients, normalized and unnormalized Galerkin factors, exact eigenvalues/counts, and the fixed-depth/maximal-depth noncommutation. |
| Coarse Borel state | 07b_agent_network_rg.tex, attention covariance paragraph | Transforms the coarse state by \(\vartheta_{\ell+1}\) and distinguishes it from the direct-sum feature operator \(R_{x,c}\). |
| \(L^\infty\) endpoint | 07b_agent_network_rg.tex, conditional-expectation contraction | Includes \(1\leq p\leq\infty\), mean preservation, and the centered quotient. |
| Reference monodromy | 07b_agent_network_rg.tex, eq:rg-reference-step and monodromy paragraph | Types the reference-space endomorphism and distinguishes a monodromy-fixed cycle from one-step fixedness. |
| Symbol collisions | appendix_notation.tex and the repaired RG interaction equations | Separates the principal bundle, interaction extraction, retained projection, configuration arrow, coarse-state action, and related reused symbols. |
| Numerical inventory documentation | verification/VERIFICATION.md, opening inventory contract | Updates the governed inventory to 13 literal numerical-status tokens and 11 substantive entries after the schedule-protocol status was added; the distinct 30-check numerical suite plus source-inventory check remains unchanged. |

No surviving comparison discrepancy was classified as an unproved routine
compatibility statement. The source-level derivations above are the current
support for the repaired history endpoint theorem; historical Task 10 records
that asserted lower-bound necessity are not evidence for that claim.

## Status-scope reconstruction

The forward inventory contains 73 unique ledger claims. Their source-support
classes at the repaired source boundary are:

| support class | count |
|---|---:|
| proof or derivation (proof) | 51 |
| definition | 1 |
| primary citation (primary_source) | 4 |
| explicit negative boundary (negative_boundary) | 2 |
| numerical protocol (numerical_protocol) | 0 |
| operational check closed at source level (operational_check) | 8 |
| unresolved downstream obligation (open_obligation) | 7 |
| **total** | **73** |

The finalized map contains 190 forward edges: 181 resolved-current edges, six
future-obligation edges, two future-revision edges, and one companion one-way
edge. All 73 claims are mapped, and the seven claims without full current
support are exactly the seven downstream `INCONCLUSIVE` claims listed below.

The reverse inventory contains 282 theorem-style headings and six formal
inline nodes, for 288 formal source nodes. It contains 289 source labels,
including one documented alias. The refrozen current status scan finds 847
status tags: 840 governed tags and seven taxonomy-table exceptions. Exact final file/line
locators and committed-blob hashes belong to the companion claim-source map,
whose finalized precommit binding is recorded at the top of this report.

The live claim ledger has 66 EVIDENCE_VERIFIED claims and seven
release-ineligible INCONCLUSIVE claims. It has no CANDIDATE or LLM_SUPPORTED
claim. The seven open claims are exactly:

1. target: Task 13 numerical/manifest/proof-bundle evidence and Task 14
   build/render/auxiliary evidence;
2. pullback-ledger-provenance: Task 13 PB1--PB4 validation at \(S\);
3. determinant-gap-stability: Task 13 JUnit and high-precision reproduction;
4. manifest-fail-closed: Task 13 authenticated update, verification, and
   mutation probes;
5. minor-emergent-time-keyword: Task 14 PDF metadata/text check;
6. minor-status-unbreakable: Task 14 rendered and extracted-text inspection;
7. minor-generated-aux: Task 14 clean build and auxiliary-file inventory.

These are terminal for the present source-level attempt and explicitly
release ineligible; none is silently treated as a queued candidate.

## Live-control repairs

1. The former task-9-primary-source-record alias is replaced by the real
   task-9-primary-source-map evidence at
   evidence/task-9-primary-source-map.md, SHA-256
   ad0e8102fbee51f0302cd0d05bcf6e019be16d39911da24a2b9d90286a6350e2.
   The obsolete claim that the primary PDF was unavailable is removed.
2. The duplicate task-10-symbolic-control evidence node and all 17 claim
   references to it are removed; byte identity with task-10-integrated-proof
   cannot create independent evidence.
3. Exactly 15 operational/source-control claims are typed
   OPERATIONAL_IDENTIFICATION; determinant-gap-stability remains a
   NUMERICAL_OBSERVATION.
4. The history-semiconjugacy claim now states the exact endpoint criterion,
   the complete-flow improper-integral specialization, the sufficiency but
   nonnecessity of a positive infimum, and the critical-point continuity
   obligation. Its old Task 10 evidence edges are removed.
5. CE-WEIGHTED-FRECHET, CE-RIGHT-INVERSE-SAME-METRIC, and all twelve rows from
   CE-MOVING-ATOM through CE-OBSERVATION-DELETION are individually recertified
   above. The register also contains the repaired arctan row and the new arsinh
   and noisy-circle rows, all with terminal evidence status.
6. The stale outside-Task-10 counterexample gap, the stale primary-PDF gap,
   the stale lower-bound necessity, and the completed probability attack are
   removed. The remaining planned adversarial work is limited to the stated
   Task 13/14 source-build gates.

After this report is byte-final, the coordinator mechanically replaces the
provisional identity in the existing task-12-source-rigor DERIVATION evidence
node with this report's SHA-256 and propagates the same identity to every
adversarial-report reference. The evidence node is already attached to all 66
EVIDENCE_VERIFIED claims; hash propagation does not alter the seven downstream
INCONCLUSIVE states.

## Static control checks

The owned-control finalization pass checks only the five Task 12 artifacts
owned by this lane. It does not run a TeX/PDF build, numerical tests, JUnit,
the Task 13 manifest probes, or any Task 14 render inspection.

| check | result |
|---|---|
| JSON parsing of claim-ledger.json, approach-registry.json, and adversarial-report.json | PASS: all three parse with ConvertFrom-Json. |
| Claim-state count and exact seven-open-set check | PASS: 73 claims = 66 EVIDENCE_VERIFIED + 7 INCONCLUSIVE; the seven IDs are exactly the downstream set listed above; 15 claims are OPERATIONAL_IDENTIFICATION and one is NUMERICAL_OBSERVATION. |
| Evidence-reference integrity and removal of the two obsolete evidence IDs | PASS: 28 evidence nodes, zero unresolved claim references, and zero nodes or references named task-9-primary-source-record or task-10-symbolic-control. |
| Counterexample-register candidate count | PASS: zero CANDIDATE rows and 70 EVIDENCE_VERIFIED rows. |
| git diff --check on the five owned artifacts | PASS: no whitespace error; the tracked-file check and the untracked-report no-index check emitted only Git's expected LF-to-CRLF warning. |

The claim-source map and the two independent precommit source approvals are
now exactly bound above. The immutable full-\(S\) review remains a necessarily
postcommit external operation. Until that review and the later-task evidence
are complete, this source-level report must not be read as a release
attestation.
