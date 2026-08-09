<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Complete finite-network gauge--VFE effective theory

## Theorem

Let \(V_\ell\) be an arbitrary finite agent set, with no uniform bound on
\(\lvert V_\ell\rvert\), and let

\[
X_\ell=\prod_{i\in V_\ell}X_{\ell,i}
\]

be a finite product of standard-Borel spaces. At every admitted scale suppose
the following data have been supplied.

1. A probability reference \(\rho_\ell\), a finite positive likelihood measure
   \(m_\ell=e^{-H_\ell}\rho_\ell\) with
   \(0<m_\ell(X_\ell)<\infty\), and the normalized evidence law
   \(\pi_\ell=m_\ell/m_\ell(X_\ell)\).
2. A normalized parameter-independent Markov channel
   \(K_\ell:X_\ell\rightsquigarrow X_{\ell+1}\), with the standard-Borel
   disintegrations and measurable versions used below.
3. When interaction coordinates are invoked, a product probability
   \(\nu_\ell=\bigotimes_i\nu_{\ell,i}\) equivalent to \(\pi_\ell\), and the
   analogous separately declared product equivalence at the target scale.
4. One principal bundle and its belief and model statistical associated
   bundles, regular DQM statistical fibers, represented gauge actions,
   selected connections and sections, and every equivariant scale morphism
   used by a conclusion.
5. When configuration histories are invoked, a regular configuration
   manifold with a strong declared Fisher metric, a \(C^2\) VFE objective,
   locally unique gradient flow, and every smooth coarse configuration map or
   exact recognition-law lift used by the statement.
6. When beta functions or ordinary fixed points are invoked, the scale ratios,
   rescaling maps, reference measures, norms, and bounded comparison
   isomorphisms needed to put consecutive objects in one comparison space.

Assume throughout the support, domination, integrability, smoothness,
family-closure, equivariance, and quotient hypotheses attached to each tier in
the bound claim ledger. Then the following construction exists and is exact.

### 1. Measure-pair renormalization and evidence

Define

\[
  \rho_{\ell+1}=\rho_\ell K_\ell,
  \qquad
  m_{\ell+1}=m_\ell K_\ell,
  \qquad
  H_{\ell+1}=-\log\frac{dm_{\ell+1}}{d\rho_{\ell+1}}.
\]

Both masses are preserved. In particular,

\[
  m_{\ell+1}(X_{\ell+1})=m_\ell(X_\ell),
\]

so the evidence is unchanged by the common channel. If
\(\Pi_{\rho,\ell}(z,dy)\) is the reverse conditional under
\(\rho_\ell(dy)K_\ell(y,dz)\), then

\[
  e^{-H_{\ell+1}(z)}
  =\int e^{-H_\ell(y)}\Pi_{\rho,\ell}(z,dy)
\]

for \(\rho_{\ell+1}\)-almost every \(z\). These finite-measure-pair maps compose
exactly under kernel composition. Stronger pointwise equalities require
coordinated Radon--Nikodym versions and are not part of the invariant claim.

For a posterior \(\Pi_o\), recognition law \(Q_o\ll\Pi_o\), and the same
channel \(C\) attached to both, relative-entropy disintegration gives

\[
\begin{aligned}
 \mathcal F_o(Q_o)
 &=\mathcal F_o^c(Q_oC)\\
 &\quad+\int
   \operatorname{KL}
   \bigl(\widehat Q_o(dy\mid z)
         \Vert
         \widehat\Pi_o(dy\mid z)\bigr)
   (Q_oC)(dz).
\end{aligned}
\]

Thus the coarse VFE is no larger. On the finite-KL branch, equality holds
precisely when the displayed conditional KL vanishes, meaning that no
posterior information remains unresolved inside a coarse fiber. Equality of
two infinite extended values carries no recovery conclusion. This is an
identity for one common structural channel and one observation event, not a
comparison of arbitrarily refitted coarse models.

### 2. Local, agent, block, and collective ELBOs

Let \(B\subseteq V_\ell\) be nonempty and write the outside configuration as
\(b=x_{B^c}\). Fix the measurable baseline conditional
\(P_{0,B}(dx_B\mid b)\) and incident-record likelihood
\(L_{B,o}(x_B;b)\) on the posterior-full regular outside set, and define

\[
 Z_B(b)=\int L_{B,o}(x_B;b)P_{0,B}(dx_B\mid b)\in(0,\infty),
 \qquad
 \Pi_{o,B}(dx_B\mid b)
 =\frac{L_{B,o}(x_B;b)P_{0,B}(dx_B\mid b)}{Z_B(b)}.
\]

Disintegrate the selected posterior as
\(\Pi_o(dx)=\Pi_{o,B}(dx_B\mid b)\Pi_{o,B^c}(db)\). The exact local extended
VFE of a candidate block law \(r_B\) is

\[
 \mathcal F^{\mathrm{ext}}_{B,o}(r_B;b)
 =-\log Z_B(b)
  +\operatorname{KL}
    \bigl(r_B\Vert\Pi_{o,B}(\cdot\mid b)\bigr).
\]

For \(B=\{i\}\) this is the local VFE of agent \(i\); for a general block it is
the VFE of the corresponding meta-agent. If \(Q\) and \(Q'\) have finite
posterior KL, share the same outside marginal, and differ only in the
conditional block law, then

\[
 \mathcal F_o(Q')-\mathcal F_o(Q)
 =\mathbb E_{Q_{B^c}}
   \left[
    \mathcal F^{\mathrm{ext}}_{B,o}(r'_B;Y_{B^c})
    -\mathcal F^{\mathrm{ext}}_{B,o}(r_B;Y_{B^c})
   \right].
\]

Consequently an exact local conditional update is a coordinate update of the
same collective VFE. Local and global VFE are not competing objectives, and
local potentials may not be independently summed: overlapping conditionals,
correlations, and total-correlation terms belong to the one joint law. An
exact local coordinate step need not by itself increase model evidence; that
stronger statement requires a complete exact posterior phase.

The extended ELBO is

\[
 \mathcal L_o^{\mathrm{ext}}(Q)
 =\log z_o-\operatorname{KL}(Q\Vert\Pi_o),
\]

with values in the extended reals. The classical expected-log-likelihood
minus entropy split is only a corollary under its separate absolute-continuity
and log-integrability hypotheses. The extended formulation remains valid for
singular laws and prevents undefined \(\infty-\infty\) cancellations.

### 3. Observations as agent--environment interaction

Every normalized observation kernel \(O:X\rightsquigarrow\mathcal O\) between
standard-Borel spaces admits a randomization representation

\[
  o=F(x,U),\qquad U\sim\operatorname{Unif}[0,1],
\]

for a measurable \(F\). Therefore one may realize the observation as the
message emitted by an environment node whose state contains \(U\). Conversely,
marginalizing any environment-node state and normalized message kernel
produces an observation kernel. Hence an operationally agent-only
presentation is always available if environment nodes are admitted as agents.

This equivalence preserves the observation sigma-algebra. It does not delete
conditioning, turn an unobserved prior into a posterior, or prove that every
environment node is biologically or ontologically an agent. “Observation” is
the role played by an interaction message in the inference problem; the
agent/environment ontology remains a modeling interpretation.

### 4. Exact nonlinear action calculus

Let \(\Pi_\ell(z,dy)\) be a selected reverse conditional for
\(\pi_\ell(dy)K_\ell(y,dz)\). On the bounded action chart define

\[
 Q_\ell(\varphi)(z)
 =-\log\int e^{-\varphi(y)}\Pi_\ell(z,dy).
\]

At a general center \(\varphi\), introduce the tilted reverse law

\[
 \Pi_\ell^\varphi(z,dy)
 =\frac{e^{-\varphi(y)}\Pi_\ell(z,dy)}
        {\int e^{-\varphi}\,d\Pi_\ell(z)}.
\]

Then the map is locally real analytic and

\[
 DQ_\ell(\varphi)[h]
 =\mathbb E_{\Pi_\ell^\varphi}[h\mid z],
 \qquad
 D^2Q_\ell(\varphi)[h,k]
 =-\operatorname{Cov}_{\Pi_\ell^\varphi}(h,k\mid z).
\]

At the origin the derivative is ordinary conditional expectation. The
evidence-mass constant is retained in the measure-pair tier and removed only
in the explicitly projective action tier. Indeed,

\[
 Q_\ell(\varphi+c)=Q_\ell(\varphi)+c,
 \qquad
 \overline Q_\ell[\varphi]=[Q_\ell(\varphi)]
\]

defines the induced map on bounded actions modulo constants. An arbitrary
\(L^2\) score need not possess a two-sided exponential neighborhood, so the
nonlinear action chart and DQM tangent space are related but not identical.

### 5. Score pushforward and Fisher loss

If a statistical family is DQM with centered score
\(\ell_\theta\in L^2(P_\theta)\), including the allowed Le Cam singular
remainder, then a normalized parameter-independent channel produces the
coarse score

\[
 \bar\ell_\theta(Z)
 =\mathbb E[\ell_\theta(X)\mid Z].
\]

The Fisher defect is the positive-semidefinite conditional covariance

\[
 I_X-I_Z
 =\mathbb E\operatorname{Cov}(\ell_\theta(X)\mid Z)
 =\mathbb E
  [(\ell_\theta-\bar\ell_\theta(Z))
   (\ell_\theta-\bar\ell_\theta(Z))^T].
\]

Equality in a direction means that directional score is \(Z\)-measurable at
the parameter in question; it does not by itself imply global recovery or
sufficiency of the entire statistical experiment.

### 6. Full interaction coordinates and the exact effective action

Assume \(\pi_\ell\sim\nu_\ell\) for the declared product reference. For
\(A\subseteq V_\ell\), let \(C_A\) integrate the complement against the
product reference and define the Boolean projectors

\[
 P_A=\sum_{B\subseteq A}(-1)^{\lvert A\rvert-\lvert B\rvert}C_B.
\]

They satisfy

\[
 P_AP_B=\mathbf 1_{A=B}P_A,
 \qquad
 \sum_{A\subseteq V_\ell}P_A=I.
\]

Let \(\mathcal G_\ell\) be the \(\ell^1\)-sum of the nonempty hierarchical
zero-mean ranges, let \(E_\ell\) assemble the components, and let
\(\mathsf H_\ell\)
extract them. Modulo the evidence-mass constant,

\[
 \mathsf H_\ell E_\ell=I,
 \qquad
 E_\ell\mathsf H_\ell=I,
 \qquad
 \|E_\ell\|\le1,
 \qquad
 \|\mathsf H_\ell\|\le 3^{\lvert V_\ell\rvert}-1.
\]

For \(g\in\mathcal G_\ell\), choose a representative \(\varphi_g\) with
\([\varphi_g]=E_\ell g\). The exact nonlinear
full-interaction map is

\[
 \mathsf T_\ell^{\mathcal G}
 =\mathsf H_{\ell+1}\,\overline Q_\ell\,E_\ell,
\]

and its derivative at \(g\) is

\[
 D\mathsf T_\ell^{\mathcal G}(g)
 =\mathsf H_{\ell+1}\,
  \overline U_\ell^{\varphi_g}\,E_\ell,
\]

where \(\overline U_\ell^{\varphi_g}\) is tilted conditional expectation on
action classes. The untilted operator is the derivative only at \(g=0\).

For bounded idempotent retained projections \(R_\ell\), define

\[
 g_{\ell+1}^{\mathrm{ret}}
 =R_{\ell+1}\mathsf T_\ell^{\mathcal G}(g_\ell),
 \qquad
 r_{\ell+1}^{\mathcal G}
 =(I-R_{\ell+1})\mathsf T_\ell^{\mathcal G}(g_\ell).
\]

The retained theory is exact on its whole retained sector if and only if

\[
 \mathsf T_\ell^{\mathcal G}(\operatorname{Ran}R_\ell)
 \subseteq\operatorname{Ran}R_{\ell+1}.
\]

Otherwise \(r_{\ell+1}^{\mathcal G}\) is the exact truncation residual. Hidden
variables generally generate higher hyperedges, marked operator--feature
kernels, and path memory. The complete finite theory is exact because it
retains all nonempty finite subsets; it is not a theorem that pairwise,
sparse, memoryless, or finite-parameter ansatzes close.

### 7. Meta-agent bridges, interactions, and attention

For a block \(I\) and fine agent \(j\), disintegration of the posterior bridge
produces Bayes-adjoint kernels satisfying

\[
 \Pi_{o,j}(dy_j)K_{I\leftarrow j}(y_j,dz_I)
 =\Pi^c_{o,I}(dz_I)K_{j\leftarrow I}(z_I,dy_j).
\]

These are exact pair marginals. They reconstruct the full fine posterior only
under an additional conditional-independence or sufficiency condition.

For a declared root-framed feature representation with normalized block
weights \(\sum_{i\in I}w_{Ii}=1\), define aggregation and prolongation by

\[
 (C_xz)_I
 =\sum_{i\in I}w_{Ii}
   R_x(\tau_{I\leftarrow i}^{x})z_i,
 \qquad
 (P_x\bar z)_i
 =R_x(\tau_{I\leftarrow i}^{x})^{-1}\bar z_I,
\]

with \(C_xP_x=I\). If \(A_x\) is the fine interaction operator, the exact
typed cross-scale operators are

\[
 A^x_{I\leftarrow j}=(C_xA_x)_{Ij},
 \qquad
 A^x_{j\leftarrow I}=(A_xP_x)_{jI},
 \qquad
 A^x_{I\leftarrow J}=(C_xA_xP_x)_{IJ}.
\]

Attention must be coarsened as a normalized measurable joint marked event
law. If the measurable event weights are
\(\eta_{ij}=\alpha_i\beta_{ij}\), then

\[
 \eta^c_{IJ}
 =\mathbb E
  \left[\sum_{i\in I,j\in J}\eta_{ij}\,\middle|\,Z\right],
 \qquad
 \alpha_I^c=\sum_J\eta^c_{IJ},
 \qquad
 \beta^c_{IJ}=\frac{\eta^c_{IJ}}{\alpha_I^c}
\]

on occupied rows; an unoccupied row is immaterial. Pushing a row-stochastic
\(\beta\) without receiver occupancy is not associative. Meta-attention and
the meta-interaction kernel are distinct conditional terms in the block ELBO.

### 8. Gauge bundles and agent-perceived base geometry

For a statistical associated bundle \(E\to C\), selected connection \(\omega\),
section \(s\), and vertical Fisher tensor \(g^F\), define

\[
 D^\omega s=\operatorname{ver}^\omega\circ Ts,
 \qquad
 h_s^\omega=(D^\omega s)^*g^F.
\]

This is the agent-perceived informational geometry on the contextual base. It
is invariant under passive gauge re-expression when the section, connection,
and fiber tensor are transformed together. It is connection relative, is
generally a semimetric, and satisfies

\[
 \operatorname{rad}h_s^\omega=\ker D^\omega s.
\]

For a scale morphism \(\Psi:E\to\bar E\) over \(f:C\to\bar C\), define the
horizontal anomaly

\[
 A_\Psi(e;X)
 =T_e\Psi(H_e^\omega X)
  -H_{\Psi(e)}^{\bar\omega}(T_cfX).
\]

Related sections obey the exact covariant-jet chain rule

\[
 D^{\bar\omega}\bar s(TfX)
 =T^V\Psi(D^\omega sX)+A_\Psi(s;X).
\]

The vertical Fisher defect

\[
 \Delta_F^\Psi
 =g^F-(T^V\Psi)^*\bar g^F
\]

is positive semidefinite for a normalized parameter-independent Markov fiber
map. Writing \(u=D^\omega sX\), \(L=T^V\Psi\), and \(a=A_\Psi(s;X)\), the
exact base comparison is

\[
 h_s^\omega-f^*h_{\bar s}^{\bar\omega}
 =\delta_\Psi-\mathcal X_\Psi-\mathcal Q_\Psi,
\]

where

\[
 \delta_\Psi(X,Y)=\Delta_F^\Psi(u_X,u_Y),
\]

\[
 \mathcal X_\Psi(X,Y)
 =\bar g^F(Lu_X,a_Y)+\bar g^F(a_X,Lu_Y),
 \qquad
 \mathcal Q_\Psi(X,Y)=\bar g^F(a_X,a_Y).
\]

Zero anomaly is sufficient for base contraction, not necessary. The sharp
directional criterion is

\[
 2\bar g^F(Lu_X,a_X)+\|a_X\|_{\bar g^F}^2
 \le\delta_\Psi(X,X).
\]

For composable arrows,

\[
 A_{12\circ01}
 =T^V\Psi_{12}A_{01}+A_{12}\circ Tf_{01},
\]

and

\[
 \Delta_F^{12\circ01}
 =\Delta_F^{01}+(T^V\Psi_{01})^*\Delta_F^{12}.
\]

The vertical defect cocycle is unconditional algebraically. Its pullback to
the base has the exact anomaly residual recorded in the ledger; it is not an
unconditional additive cocycle.

### 9. Configuration geometry, histories, and information duration

The construction is nonempty. On a compact measured base, take a fixed-
covariance normal location fiber and weighted-\(L^2\)-independent basis fields
\(\phi_a\). Then

\[
 s_\xi(c)=\mathcal N
 \left(\sum_a\xi_a\phi_a(c),\Sigma_0\right),
 \qquad
 \mathcal Q\cong\mathbb R^N,
\]

with strong constant Gram metric

\[
 \Phi_{ab}
 =\int \phi_a(c)^T\Sigma_0^{-1}\phi_b(c)w(c)\,d\mu(c).
\]

This yields a locally unique natural-gradient flow for every \(C^2\)
objective. For a general multi-agent exact VFE history, a smooth right-inverse
lift into a joint recognition-law family and its joint Fisher pullback must be
declared or proved. Marginal sections alone do not determine correlations or a
joint Fisher metric; distinct lifts can, but need not, induce distinct metrics.

A pointwise bundle morphism induces a coarse section only when the transformed
fine section is constant on fibers of the base map and descends smoothly. A
separately declared affine averaging construction is also available under its
disintegration, convexity, integrability, and closure hypotheses. Let
\(f_\#\mu=\bar\mu\), disintegrate
\(\mu(dc)=\bar\mu(d\bar c)\kappa_{\bar c}(dc)\), let
\(L=T^V\Psi\), and let \(Z\in T_s\mathcal Q_\ell\). In the constant-metric
case its exact quadratic configuration defect is

\[
 \begin{aligned}
 \Delta_{\mathrm{avg}}(Z)
 &=\mathsf G_\ell(Z,Z)
   -\mathsf G_{\ell+1}(T\mathsf R_\ell Z,T\mathsf R_\ell Z)\\
 &=\underbrace{\int_{\mathcal C_\ell}
      w\,\Delta_F^\Psi(Z,Z)\,d\mu}_{\text{channel loss}}\\
 &\quad+\underbrace{\int_{\mathcal C_\ell}
      (w-\bar w\circ f)(L^*\bar g^F)(Z,Z)\,d\mu}_{\text{weight gap}}\\
 &\quad+\underbrace{\int_{\mathcal C_{\ell+1}}
      \bar w\,
      \operatorname{Var}_{\kappa_{\bar c}}^{\bar g^F}(LZ)\,d\bar\mu}
      _{\text{context gap}}.
 \end{aligned}
\]

This requires base-measure matching, coarse-weight domination, and joint
convexity in the declared chart. Generic chart barycenters need not be
realizable by parameter-independent Markov channels and need not contract
Fisher geometry.

The curve types are distinct. A change of law in one fixed fiber is vertical.
A total-space curve over a changing base is horizontal only relative to a
chosen connection and is otherwise mixed. A base curve has no vertical or
horizontal predicate. A curve of sections is a configuration-space curve, and
its evaluation at a fixed base point has vertical velocity.

For a selected regular configuration path \(Q(r)\), define

\[
 \nu_F(r)=\sqrt{\mathsf G^F(\dot Q,\dot Q)},
 \qquad
 \tau(r)=\int_{r_0}^{r}\nu_F(u)\,du.
\]

This Fisher duration is covariant under orientation-preserving
reparameterization, with equal accumulated length at corresponding points,
and supplies an arc-length coordinate wherever \(\nu_F>0\). Along a
natural-gradient ray,

\[
 \frac{dQ}{d\tau}
 =-\frac{\operatorname{grad}^F\mathcal F}
         {\|\operatorname{grad}^F\mathcal F\|_F},
 \qquad
 \frac{d\mathcal F}{d\tau}
 =-\|\operatorname{grad}^F\mathcal F\|_F.
\]

This is emergent information duration only in the precise sense that it is
constructed from a selected belief/model history and Fisher metric rather than
postulated as an external coordinate. It is path dependent, depends on metric,
origin, and orientation, can stall on null segments, and is not a primitive or
global physical time.

Independently optimized fine and coarse histories share an oriented orbit only
when

\[
 T\mathsf R_\ell X_\ell
 =a_\ell\,X_{\ell+1}\circ\mathsf R_\ell,
 \qquad a_\ell>0.
\]

Functional compatibility of objectives plus horizontal conformality of a
surjective submersion is a sufficient condition, with

\[
 a_\ell=\chi_\ell'\varphi_\ell^2.
\]

Neither equality of objectives nor fiber Fisher contraction alone implies
this relation. The manuscript-specific configuration maps and their
semiconjugacy remain application obligations, not consequences of the bundle
construction.

### 10. Beta functions, modes, and fixed objects

Along an exact interaction orbit, the derivatives

\[
 D_\ell=D\mathsf T_\ell^{\mathcal G}(g_\ell)
\]

form the ordered cocycle

\[
 D_{n\leftarrow\ell}=D_{n-1}\cdots D_\ell.
\]

A compatible mode is a scale-indexed line satisfying

\[
 D_\ell v_{\ell,a}=\lambda_{\ell,a}v_{\ell+1,a}.
\]

It is not an ordinary eigenvector until consecutive spaces are identified.
With scale ratios \(b_\ell>1\) and bounded isomorphisms
\(J_\ell:\mathcal G_*\to\mathcal G_\ell\), define

\[
 \widehat{\mathsf T}_\ell
 =J_{\ell+1}^{-1}\mathsf T_\ell^{\mathcal G}J_\ell,
 \qquad
 \widehat R_\ell=J_\ell^{-1}R_\ell J_\ell,
 \qquad
 \beta_\ell^{\mathrm{ex}}(g)
 =\frac{\widehat{\mathsf T}_\ell(g)-g}{\log b_\ell}.
\]

On \(\operatorname{Ran}\widehat R_\ell\), define

\[
 \beta_\ell^{\mathrm{ret}}(g)
 =\frac{J_{\ell+1}^{-1}R_{\ell+1}
        \mathsf T_\ell^{\mathcal G}(J_\ell g)-g}{\log b_\ell}.
\]

The exact-minus-retained beta defect
\(\delta\beta_\ell:=\beta_\ell^{\mathrm{ex}}-
\beta_\ell^{\mathrm{ret}}\) is the transported truncation residual

\[
 \delta\beta_\ell(g)
 =\frac{J_{\ell+1}^{-1}
          r_{\ell+1}^{\mathcal G}(J_\ell g)}{\log b_\ell}.
\]

These beta components depend on the reference measure and comparison scheme.
A continuous beta additionally requires a smooth scale bundle and a scale
connection; discrete endpoints do not determine one.

For a nonautonomous sequence, an invariant object is a section
\(y_{\ell+1}=F_\ell(y_\ell)\). After common-space identifications one may ask
for a reference object fixed by every transported step. In an autonomous
scheme this reduces to an ordinary fixed point of one repeated map. A
periodic sequence may instead be classified by monodromy fixed objects and
cycles. Fixedness at the law, action, interaction, attention, bundle, and
configuration tiers does not transfer without a declared commuting bridge.

### 11. Exact realizations and limiting boundary

For an integer \(b\ge2\), iid \(X_i\sim\mathcal N(0,1)\), and
\(Z=b^{-1/2}\sum_iX_i\), the extensive tangent operator on
\(L^2_0(\gamma)\)

\[
 \mathscr L_bh
 =\mathbb E\left[\sum_{i=1}^{b}h(X_i)\mid Z\right]
\]

has normalized Hermite eigenfunctions
\(e_k=\operatorname{He}_k/\sqrt{k!}\), \(k\ge1\), with eigenvalues

\[
 \mathscr L_be_k=b^{1-k/2}e_k.
\]

Thus degree one is relevant, degree two marginal, and higher degrees
irrelevant in this scalar iid tangent sector. Correlation, dimension,
normalization, and nonlinear iteration change the conclusion and require new
theorems.

For a Gaussian target with precision \(\Lambda\succ0\), the optimal
block-product Gaussian recognition covariance is
\(\Sigma_I=\Lambda_{II}^{-1}\), and the exact factorization gap is

\[
 \mathcal G_{\mathrm{fact}}
 =\frac12\left(
   \sum_I\log\det\Lambda_{II}-\log\det\Lambda
  \right)\ge0.
\]

It is nonincreasing under comparable block merging and vanishes exactly at
the corresponding block-diagonal boundary. The deterministic stress protocol
checks the stable implementation; the algebraic proof supplies the theorem.

The exact path-graph quotient and Abelian Karamata calculation show that
finite-stage closure does not determine a thermodynamic RG. Fixed-depth
thermodynamic and maximal-depth limits can differ. Let
\(U(\lambda)=N(\lambda)-N(0)\) be nondecreasing and right-continuous with
\(U(0+)=0\). Suppose, for \(c>0\), \(\alpha>0\), and \(L\) slowly varying at
infinity, that

\[
 U(\lambda)\sim c\lambda^\alpha L(1/\lambda)
\]

as \(\lambda\downarrow0\), and suppose the positive heat trace is finite at
some \(t_0>0\). Define

\[
 M_k(t)=\int_{(0,\infty)}\lambda^k e^{-t\lambda}\,dU(\lambda),
 \qquad
 S_+(t)=\log M_0(t)+t\frac{M_1(t)}{M_0(t)}.
\]

Then the forward Abelian implication gives

\[
 -\frac{dS_+}{d\log t}\longrightarrow\alpha.
\]

No Tauberian converse, universal exponent, or infinite-volume existence
theorem follows.

## Proof and completeness

The measure-pair and VFE identities follow from Radon--Nikodym pushforward,
normalization, and the relative-entropy chain rule. The local/global identity
is the same chain rule after posterior disintegration over a block and its
outside marginal. Standard-Borel randomization proves the observation--message
equivalence. Conditional log-Laplace differentiation proves the nonlinear
action calculus, while DQM projection and total covariance prove Fisher data
processing.

Finite-product Fubini and Boolean inversion prove the full interaction
isomorphism. Conjugation by its exact inverse yields the nonlinear interaction
map and the residual identities. Disintegration of posterior bridges and joint
marked attention events yields the agent--meta and meta--meta kernels. Bundle
quotient descent, the connection splitting, and direct expansion prove the
covariant-jet, anomaly, pullback, and cocycle formulas. The explicit normal-
location coefficient family proves nonvacuity of the configuration tier;
standard ODE theory then supplies local histories. Arc-length substitution and
vector-field intertwining prove the duration and semiconjugacy statements.
The chain rule proves the derivative cocycle and all beta residual formulas.

Every universal conjunct in the frozen finite target is therefore either an
actual construction, an exact identity under its named hypotheses, or an
exact boundary stating that an additional map or closure property must be
declared and checked. The construction is complete for each admitted finite
network and every finite composable scale sequence.

It does **not** prove automatic existence of principal scale maps, product
references after arbitrary channels, exact joint recognition lifts, generic
configuration maps, model-specific natural-gradient semiconjugacy, a
nontrivial invariant sparse interaction ansatz, canonical rescaling, a
continuous beta, Gaussian attraction, universality, or an infinite-volume or
continuum limit. Those strengthenings are outside the frozen target or remain
explicit open application obligations.
