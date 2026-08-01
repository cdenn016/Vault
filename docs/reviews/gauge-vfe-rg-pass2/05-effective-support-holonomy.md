# Expert 05 — Effective-support holonomy, variable-rank fibers, and nonflat closure

## Scope and bottom line

This memo reviews the gauge/topological claims in
`02_geometry.tex`, the singular-weight and partial-coarse constructions in
`09_coarsegraining.tex`, the corresponding RG scope in `10_renormalization.tex`,
and the graph-holonomy claims in `11_obstructions.tex`. It does not repeat R1–R21
from the first ultradeep review.

The central result is positive:

> The existing fixed-\(K\), single-\(\mathrm{GL}^{+}(K)\)-link family is not
> closed when cut twists disagree, but the linear-quadratic theory already has
> an exact, gauge-covariant, variable-rank closure in the category of cellular
> sheaf Laplacians with rectangular endpoint maps. What remains open is
> compression of that richer datum to one invertible group-valued link, not the
> existence of any closed nonflat coarse category.

In physicist's language: a nonflat link need not be summarized by one new
parallel transporter. It can instead be summarized by the two linear maps that
tell each endpoint which components of its state are compared on that edge.
Those maps can be rectangular when the endpoints carry different numbers of
surviving modes. Blocking then just composes maps, so blocking twice agrees with
blocking once. This is the same elementary reason transfer matrices compose.

### Architecture tags used below

- **GENERAL** — belongs before the MV-Gaussian realization: principal bundles,
  graph-link holonomy, abstract rank-changing gauge objects, and the distinction
  between a group link and a general comparison relation.
- **MVG / LINEAR-QUADRATIC REALIZATION** — uses finite-dimensional vector
  spaces, positive-semidefinite forms, kernels, congruences, or Gaussian
  normalizability. These results should appear only after the full general
  coarse-graining/RG theory in the reordered manuscript. Some are operator
  theorems that apply beyond Gaussian probability laws, but they are not
  theorems about arbitrary belief fibers.

## Finding EH-0 — The general geometry must use independent belief and model gauge bundles

**Location.** `02_geometry.tex:56-63` declares two representations of the same
group; lines 106–113 require both channels to move under the same \(g_i\);
lines 115–140 correctly describe independent bundles but relegate them to an
extension; lines 201–203 derive both channel links from the same
\(\Omega_{ij}\). The same diagonal choice is consumed downstream, for example
at `04_generative.tex:301-313` and `432-435`.

**Severity.** High architecture. The present construction is consistent, but it
is a diagonal/shared-frame specialization rather than the requested general
theory.

**Manuscript status.** `\status{DEFINITION}` for the shared group and
`\status{ESTABLISHED}` for Proposition 2.5's intertwining criterion.

**Review status.** `\status{REFUTED}` if the shared group is presented as the
general theory; `\status{ESTABLISHED}` as a valid specialization.

**Plain-English category and inflation verdict.** Nothing is wrong with using
one frame when the model explicitly identifies the two gauge freedoms. What is
too narrow is making that identification before the general theory has been
stated.

### Product-bundle typing

Use independent principal bundles
\[
P^{b}\xrightarrow{\pi_b}\mathcal C,\qquad
P^{m}\xrightarrow{\pi_m}\mathcal C
\]
with structure groups \(G_b\) and \(G_m\). Their fiber product
\[
P^{b}\times_{\mathcal C}P^{m}
\]
is a principal \(G_b\times G_m\)-bundle. The belief/state and model law bundles
are formed separately:
\[
\mathcal E_b=P^b\times_{\rho_b}\mathcal B_b,\qquad
\mathcal E_m=P^m\times_{\rho_m}\mathcal B_m .
\]
Agent \(i\) chooses a pair of frames \((u_i^b,u_i^m)\). Its independent gauge
change is \((g_i^b,g_i^m)\).

Use the author's fixed notation at the bundle level:
\[
\Phi:\mathcal E_b\longrightarrow\mathcal E_m,\qquad
\widetilde\Phi:\mathcal E_m\longrightarrow\mathcal E_b,
\]
both covering \(\operatorname{id}_{\mathcal C}\). These are cross-associated-
bundle morphisms, not principal-bundle morphisms and not same-channel
transports. Separate principal connections induce the belief and model
parallel transports
\[
\Omega_\gamma:\mathcal E_{b,x}\longrightarrow\mathcal E_{b,y},\qquad
\widetilde\Omega_\gamma:\mathcal E_{m,x}\longrightarrow\mathcal E_{m,y}
\]
along a base curve \(\gamma:x\to y\). In local coordinates they obey
\[
\Omega_\gamma\mapsto
g_y^b\Omega_\gamma(g_x^b)^{-1},\qquad
\widetilde\Omega_\gamma\mapsto
g_y^m\widetilde\Omega_\gamma(g_x^m)^{-1}.
\]
The cross morphisms transform by
\[
\Phi_x\mapsto g_x^m\Phi_x(g_x^b)^{-1},\qquad
\widetilde\Phi_x\mapsto g_x^b\widetilde\Phi_x(g_x^m)^{-1}.
\]
The corresponding loop holonomies are independently conjugated. No equality,
inverse relation, parallelness, or common group element is implied.

### Cross-fiber bridge and its exact law

A cross morphism is not a fixed matrix between unrelated coordinate spaces.
It is a section of an associated Hom bundle. Parallelness is an additional
condition, not part of its existence. For \(\gamma:x\to y\), the two possible
parallelness squares are
\[
\boxed{\;
\widetilde\Omega_\gamma\Phi_x
=\Phi_y\Omega_\gamma
\;}
\qquad\text{and}\qquad
\boxed{\;
\Omega_\gamma\widetilde\Phi_x
=\widetilde\Phi_y\widetilde\Omega_\gamma .
\;}
\]
Without those hypotheses, the failures
\[
\mathcal A^\Phi_\gamma
=\widetilde\Omega_\gamma\Phi_x-\Phi_y\Omega_\gamma,\qquad
\mathcal A^{\widetilde\Phi}_\gamma
=\Omega_\gamma\widetilde\Phi_x-\widetilde\Phi_y\widetilde\Omega_\gamma
\]
are covariant Hom-bundle defects. Smoothly they are
\(D\Phi=\nabla^m\circ\Phi-\Phi\circ\nabla^b\) and
\(D\widetilde\Phi=\nabla^b\circ\widetilde\Phi-
\widetilde\Phi\circ\nabla^m\). If \(\Phi\) is an invertible parallel
morphism, the two holonomies are conjugate. If it is rectangular, singular,
nonparallel, or only partially defined, one channel may retain holonomy
invisible to the other.

For nonlinear maps of laws or Markov kernels, the same statement is expressed
by pushforward equivariance rather than matrix multiplication. Proposition 2.5
already gives one special construction: a cross-channel principal map
\(B:P_m\to P_b\), a homomorphism \(\psi:G_m\to G_b\), and a
\(\psi\)-equivariant fiber map. (The current source calls this map \(\Phi\);
rename it \(B\) or another bridge symbol so that \(\Phi\) and
\(\widetilde\Phi\) remain reserved for the two channel-bundle morphisms.) That
construction reduces the product gauge to the graph of \(\psi\). The fully
independent alternative is to keep \(\Phi\), \(\widetilde\Phi\), or a
kernel-valued bridge as transforming model data in the appropriate Hom or
kernel bundle.

### Separate admissibility and coarse compatibility

A cluster is belief-coarsenable when the belief-link assignment satisfies its
own trivial-holonomy or typed effective-support criterion. It is
model-coarsenable when the model-link assignment satisfies the corresponding,
independent criterion. Neither follows from the other unless an invertible
bridge intertwines them.

If the cross-fiber coupling is to survive a joint coarse step, the bridge must
map model parallel sections into belief parallel sections. The edgewise square
above is the sufficient local condition. The induced coarse morphism is then
the restriction of \(\Phi\) or \(\widetilde\Phi\) to those section spaces.
This is the rank-changing version
of Proposition 2.5 and is compatible with the rectangular sheaf category in
EH-2.

### Exact repair and specialization

Make the product-bundle/product-gauge construction the **GENERAL** theory.
Then state the current manuscript's choice as the diagonal specialization
\[
P^b=P^m=P,\qquad
G_b=G_m=G,\qquad
(g^b,g^m)=(g,g),
\]
with \(\rho_b\) and \(\rho_m\) two representations of that diagonal group. In
the MV-Gaussian realization, shared frames and same-channel transports may
remain when explicitly assumed. If the two Gaussian fibers have the same
dimension and a declared parallel isomorphism identifies them, this reduces
further to the familiar single-frame formula. Independently declared graph
links remain separate data, preferably denoted
\(\Theta^b_{ij},\Theta^m_{ij}\); they equal
\(\Omega_{\gamma_{ij}},\widetilde\Omega_{\gamma_{ij}}\) only after a base-curve
assignment and an equality hypothesis.

**Falsification condition.** The need for the product theory would disappear
if independent changes \((g_i^b,g_i^m)\) could act on fixed cross-associated-
bundle morphisms without their two-sided transformation and still leave the
coupling covariant. The displayed law shows that they cannot.

**Physicist summary.** Belief coordinates and model coordinates are two gauge
choices, like spin and flavor bases. The fields \(\Phi\) and
\(\widetilde\Phi\) couple them and transform on both sides. Setting both gauges
equal is allowed, but it is a gauge-locking specialization, not the starting
point.

**Architecture placement.** **GENERAL.** Put the product bundle, independent
holonomies, and bridge law before any Gaussian material. Put the diagonal
shared-frame case in the later MV-Gaussian realization.

**Notation collision to remove.** The RG aggregation map
\(\Phi_S\) at `10_renormalization.tex:275-350` (and its later occurrences)
must be renamed, for example to \(\mathcal R_S\). It is a parameter
coarse-graining map, not either channel-bundle morphism. The generic iteration
symbol \(\Phi\) in `05a_expfamily.tex:174-186` should likewise be changed if
the reservation is manuscript-wide.

## Finding EH-1 — Edgewise invisible twists do not define one “represented support” around a loop

**Location.** `09_coarsegraining.tex:340-356`, especially the transition from
the exact edgewise criterion at lines 340–345 to “effective-support cases” at
line 356; `10_renormalization.tex:24-45`, especially “the represented support”
at line 42.

**Severity.** Medium-high. The active flat/trivializing flow is unaffected, but
the claimed boundary of the nonflat extension is not yet typed.

**Manuscript status.** The edgewise equation is carried as
`\status{ESTABLISHED}`; the global support wording is included under
`\status{ESTABLISHED}` at `10_renormalization.tex:42`.

**Review status.** `\status{REFUTED}` for the existence of a canonical single
support under the current hypotheses. `\status{ESTABLISHED}` for the edgewise
criterion only.

**Plain-English category and inflation verdict.** The local algebra is correct.
The phrase “the represented support” inflates a family of edge-local quotients
into one common quotient on which loop holonomy could be multiplied. Different
edges can see different directions, so that common space need not exist.

### Exact derivation

For one edge let \(N_e=\ker W_e\), and let
\(q_e:\mathbb R^K\to\mathbb R^K/N_e\) be the quotient map. Then
\[
W_e^{1/2}(I-\Theta_e)=0
\quad\Longleftrightarrow\quad
(I-\Theta_e)\mathbb R^K\subseteq N_e
\quad\Longleftrightarrow\quad
q_e\Theta_e=q_e .
\]
Thus the edgewise statement has a precise quotient interpretation. It also
implies \(\Theta_eN_e\subseteq N_e\), hence the induced map on that one quotient
exists and is the identity.

The problem is composition across different edges. Take a triangle with
\(K=2\), oriented \(1\to2\to3\to1\), and
\[
\begin{array}{c|c|c}
e & W_e & \Theta_e\\ \hline
12 & \operatorname{diag}(1,0) & \operatorname{diag}(1,2)\\
23 & \operatorname{diag}(0,1) & \operatorname{diag}(2,1)\\
31 & I_2 & I_2 .
\end{array}
\]
For a constant identified configuration \(z_1=z_2=z_3=v\),
\[
W_{12}^{1/2}(I-\Theta_{12})v=0,\qquad
W_{23}^{1/2}(I-\Theta_{23})v=0,\qquad
W_{31}^{1/2}(I-\Theta_{31})v=0
\]
for every \(v\in\mathbb R^2\). Every internal edge is therefore annihilated by
full \(K=2\) aggregation. Yet the loop product is
\[
H=\Theta_{12}\Theta_{23}\Theta_{31}=2I_2,
\]
which fixes no nonzero vector. The edge quotients are respectively
\[
\mathbb R^2/\operatorname{span}(e_2),\qquad
\mathbb R^2/\operatorname{span}(e_1),\qquad
\mathbb R^2,
\]
so they cannot be composed into a loop endomorphism without additional
identifications. There is no shared kernel on which all three weights descend
to positive-definite forms.

This example also sharpens the prose at `09_coarsegraining.tex:345-356`.
Holonomy need not survive in one globally invisible direction. Each mismatch
can be invisible to its own edge while the loop product acts nontrivially on
every direction.

### Exact repair

Replace the singular “represented support” with one of the following two typed
statements.

1. **Common-quotient theorem.** A fixed quotient
   \(V/N\) supports every link and makes every edge weight positive definite if
   and only if
   \[
   \ker W_e=N,\qquad \Theta_eN=N
   \quad\text{for every edge }e .
   \]
   On that quotient the usual group-valued holonomy is defined. Under weighted
   invisibility, every induced edge link is the identity.
2. **General singular case.** If the kernels differ, do not define “effective
   holonomy.” Use edge-local observation maps, equivalently the cellular-sheaf
   formulation in EH-2.

**Falsification condition.** This finding would be false if the current
manuscript hypotheses canonically produced one quotient on which all three
weights in the triangle became positive definite and on which the three
induced links composed. They do not.

**Physicist summary.** Each detector can be blind to a different polarization.
The fact that every detector misses its local mismatch does not create one
common unobservable polarization for the whole loop.

**Architecture placement.** **MVG / LINEAR-QUADRATIC REALIZATION.** Keep the
abstract warning “edge-local observability need not globalize” in the general
theory, but put kernels, quotient forms, and the triangle calculation in the
post-RG MV-Gaussian realization.

## Finding EH-2 — A closed rectangular-link category exists; only compression to one invertible link is open

**Location.** `09_coarsegraining.tex:512-569` and `867-871`;
`10_renormalization.tex:34-45` and `639-643`;
`11_obstructions.tex:335-336`.

**Severity.** High as an open-direction correction. It turns an overbroad
existence question into an exact theorem and isolates the genuinely open
uniqueness/compression problem.

**Manuscript status.** `\status{OPEN}` for whether “the variable-dimension
family admits any coarse link rule at all.”

**Review status.** `\status{ESTABLISHED}` for existence in the cellular-sheaf
quadratic category; `\status{OPEN}` only for compression to the original
single-\(\mathrm{GL}^{+}(K)\)-link family or for a uniqueness theorem.

**Plain-English category and inflation verdict.** The current OPEN statement is
too broad. A closed nonflat category is immediate once “link” is allowed to mean
a pair of rectangular endpoint maps into an edge comparison space. The
manuscript is correct that the narrower invertible-link family is not closed.

### Exact construction and proof

For each fine edge \(e=(i,j)\), choose a minimal factor
\[
W_e=C_e^{\mathsf T}C_e,\qquad
C_e:\mathbb R^K\longrightarrow E_e,\qquad
\dim E_e=\operatorname{rank}W_e .
\]
Then the fine pair energy is
\[
(z_i-\Theta_ez_j)^{\mathsf T}W_e(z_i-\Theta_ez_j)
=\left\|R_{i,e}z_i-R_{j,e}z_j\right\|_{E_e}^{2},
\]
with
\[
R_{i,e}=C_e,\qquad R_{j,e}=C_e\Theta_e .
\]
This is exactly a degree-zero cellular-sheaf Laplacian term: vertex stalks carry
the endpoint variables, the edge stalk \(E_e\) carries the compared quantity,
and the two restriction maps carry both endpoint variables into that common
edge space.

Now let partial aggregation assign \(z_i=S_{iI}w_I\) for \(i\in I\). A cut
edge \(e=(i,j)\) with \(i\in I\), \(j\in J\) becomes
\[
\left\|
\underbrace{R_{i,e}S_{iI}}_{R^{\mathrm c}_{I,e}}w_I
-
\underbrace{R_{j,e}S_{jJ}}_{R^{\mathrm c}_{J,e}}w_J
\right\|_{E_e}^{2}.
\]
Therefore the exact coarse link data are the rectangular maps
\[
R^{\mathrm c}_{I,e}=C_eS_{iI}:V_I\to E_e,\qquad
R^{\mathrm c}_{J,e}=C_e\Theta_eS_{jJ}:V_J\to E_e .
\]
Their cross block is
\[
-(R^{\mathrm c}_{I,e})^{\mathsf T}R^{\mathrm c}_{J,e}
=-S_{iI}^{\mathsf T}W_e\Theta_eS_{jJ},
\]
which is exactly the contribution in
`09_coarsegraining.tex:512-519`. The diagonal blocks agree for the same
reason.

Several fine cut edges between \(I\) and \(J\) may either be retained as a
multiedge or compressed losslessly into one edge stalk
\[
E_{IJ}=\bigoplus_{e\in\operatorname{cut}(I,J)}E_e
\]
by vertically stacking the endpoint maps. This direct-sum compression
reproduces the complete cut energy exactly.

If a second blocking uses maps \(T_{IA}:V_A\to V_I\), the twice-coarsened
restriction is
\[
(R_{i,e}S_{iI})T_{IA}=R_{i,e}(S_{iI}T_{IA}).
\]
Associativity of composition therefore proves closure under repeated
aggregation. No inverse, determinant, equal stalk dimension, or common frame is
needed.

### Gauge covariance

Under a coarse basis change \(g_I\in\mathrm{GL}(V_I)\),
\[
R^{\mathrm c}_{I,e}\longmapsto R^{\mathrm c}_{I,e}g_I^{-1}.
\]
The quadratic energy is unchanged after the matching coordinate change.
Changing an orthonormal edge basis multiplies both endpoint restrictions on the
left by the same orthogonal map. More generally, an arbitrary edge-basis change
is allowed if the edge inner product transforms with it. This is a
gauge-covariant groupoid of vertex and edge spaces, including unequal ranks.

### What the primary literature supplies, and what it does not

Hansen and Ghrist, *Toward a Spectral Theory of Cellular Sheaves*
([arXiv:1808.01513](https://arxiv.org/abs/1808.01513),
§2.2, Definitions 2.4 and 2.6; §3.2; §4.2), supply the exact ambient category:

- a vector space at every cell and linear restriction maps from vertex stalks
  to edge stalks (§2.2, Definition 2.4);
- variable stalk dimensions and non-full-rank restriction maps;
- the degree-zero Laplacian with diagonal blocks
  \(\sum R_{v,e}^{*}R_{v,e}\) and off-diagonal blocks
  \(-R_{u,e}^{*}R_{v,e}\) (§3.2);
- the distinction between a general cellular sheaf and a discrete vector bundle,
  the latter requiring invertible restrictions (§3.5);
- a proof that general **Kron/Schur-complement reduction** is not closed in the
  sheaf category, with one-dimensional vertex stalks as a positive special case
  (§4.2, Theorem 4.3).

The source does not state the manuscript-specific partial-aggregation theorem
above; that closure is the displayed direct calculation. It also does not
supply an RG rescaling, a probability normalizer, or a unique compression to
one group element.

This result does **not** reopen prior finding R7. Hansen–Ghrist's Kron no-go and
the manuscript's matrix-Kron counterexample concern exact marginalization by a
Schur complement. EH-2 concerns identification/pullback
\(S^{\mathsf T}\Lambda S\), a different operation.

### Exact repair

Replace “whether the variable-dimension family admits any coarse link rule at
all” with:

> Rectangular endpoint restrictions give an exact, gauge-covariant,
> aggregation-closed sheaf-Laplacian family. It is strictly larger than the
> fixed-\(K\) group-link family. Open questions are (i) whether this datum has a
> canonical minimal compression, (ii) when it compresses to one invertible
> transport and one positive-definite weight, and (iii) which rescaling and
> reference measures turn the operator semigroup into an RG flow of normalized
> laws.

**Falsification condition.** Produce one cut edge and nested blocking maps for
which endpoint-map precomposition fails to reproduce
\(S^{\mathsf T}\Lambda S\), or for which
\((RS)T\neq R(ST)\). The displayed identities rule this out.

**Physicist summary.** A coarse bond need not be one transporter. It can be a
small “measurement port” at each endpoint. Blocking wires the old ports into the
new variables. Wiring is associative, so the enlarged theory closes exactly.

**Architecture placement.** **MVG / LINEAR-QUADRATIC REALIZATION.** In the
general pre-Gaussian RG part, state only that the output category must be closed
under composition and may have rank-changing morphisms. After the general RG
theory, introduce the cellular-sheaf theorem as the concrete nonflat
linear-quadratic/MV-Gaussian realization.

## Finding EH-3 — Fixed-subspace partial fibers compose exactly under nested blocking

**Location.** `09_coarsegraining.tex:480-530`, `566-569`, and `870-871`;
`10_renormalization.tex:34-45`.

**Severity.** Medium-high. This is a missing derivation that closes the
vertex-fiber half of the “further merge” obligation.

**Manuscript status.** The one-step kernel result is
`\status{ESTABLISHED}`; compatibility under a further merge is left
`\status{OPEN}`.

**Review status.** `\status{ESTABLISHED}` for nested composition of the
interaction kernels. The probability-law and rescaling questions remain open.

**Plain-English category and inflation verdict.** The manuscript correctly
proves the one-step statement but leaves too much of the iterative statement
open. The surviving zero-mode space at the next level is exactly the zero-mode
space obtained by blocking the first-level zero modes.

### Proof

Let a coarse cluster \(A\) be a union of first-level clusters \(I\), and let
\(L_A\succeq0\) be the sum of all fine interaction-edge forms internal to
\(A\). Let
\[
S_A=\operatorname{blkdiag}_{I\subset A}S_I,
\qquad
\operatorname{range}S_I=\ker L_I .
\]
Every \(x\in\ker L_A\) has zero energy on every positive-semidefinite summand,
including every edge internal to each \(I\). Hence
\[
\ker L_A\subseteq\operatorname{range}S_A .
\]
Write \(x=S_Ay\). Since \(S_A\) has full column rank,
\[
y\in\ker(S_A^{\mathsf T}L_AS_A)
\quad\Longleftrightarrow\quad
0=y^{\mathsf T}S_A^{\mathsf T}L_AS_Ay
=x^{\mathsf T}L_Ax
\quad\Longleftrightarrow\quad
x\in\ker L_A .
\]
Therefore
\[
\boxed{\;
\ker L_A
=S_A\ker(S_A^{\mathsf T}L_AS_A)
\;}
\]
and a second partial aggregation map \(T_A\) lifts to the fine space as
\(S_AT_A\). This is exact functoriality of the fixed-section spaces under nested
partitions.

The proof consumes only finite-dimensional positive-semidefinite interaction
forms and full-column-rank injections. It does not consume Gaussian
normalization. It also does not include self terms \(A_i\), because the fixed
spaces are defined by the interaction operator; properness of the full coarse
Gaussian still requires `09_coarsegraining.tex:521-528`.

### Exact repair

Add this proposition immediately after the one-step partial-kernel proposition.
Then narrow the later open item to link-data compression, normalization,
rescaling, and asymptotic identification.

**Falsification condition.** A counterexample would require a zero mode of a
sum of positive-semidefinite edge energies with nonzero energy in one internal
positive-semidefinite summand, which is impossible.

**Physicist summary.** A mode with zero total spring energy must stretch no
spring inside any sub-block. So every large-block zero mode is already built
from the smaller-block zero modes, and the two-stage construction loses
nothing.

**Architecture placement.** **MVG / LINEAR-QUADRATIC REALIZATION.** Present
after the general RG semigroup, beside the sheaf closure theorem.

## Finding EH-4 — Rank-changing coarse gauges form a groupoid, not one \(\mathrm{GL}^{+}\) bundle

**Location.** `02_geometry.tex:38` and `75-85`;
`09_coarsegraining.tex:492-502`, `566-569`, and `870-871`.

**Severity.** Medium. This is a typing obligation, not a failure of the
one-step matrix calculation.

**Manuscript status.** The basis-independence statement is
`\status{DEFINITION}` and the variable-rank target is `\status{OPEN}`.

**Review status.** `\status{ESTABLISHED}` that the residual structure group
cannot canonically remain \(\mathrm{GL}^{+}(f_I)\) under the allowed ambient
\(\mathrm{GL}^{+}(K)\) gauges.

**Plain-English category and inflation verdict.** The manuscript correctly says
the category changes, but it has not yet named the new gauge object. Unequal
dimensions require a groupoid of vector spaces and isomorphisms; rectangular
edge maps are morphisms between different objects.

### Orientation counterexample

Let
\[
H=\operatorname{diag}(1,2)\in\mathrm{GL}^{+}(2),
\qquad
\operatorname{Fix}(H)=\operatorname{span}(e_1).
\]
The allowed ambient gauge \(g=-I_2\) also lies in
\(\mathrm{GL}^{+}(2)\), commutes with \(H\), and acts on the fixed line as
multiplication by \(-1\). Thus an orientation-preserving ambient gauge can
reverse the orientation of the surviving one-dimensional fiber. There is no
canonical reduction to
\(\mathrm{GL}^{+}(1)=\mathbb R_{>0}\). The residual group must contain all of
\(\mathrm{GL}(1)=\mathbb R^\times\), or an orientation of each fixed space must
be declared as extra data.

In general the coarse objects are finite-dimensional vector spaces \(V_I\) of
possibly different dimensions, with automorphism groups
\(\mathrm{GL}(V_I)\). The complete structure is a groupoid. A chosen basis
identifies one object with \(\mathbb R^{f_I}\), but that identification is gauge,
not physics.

### Exact repair

Define the coarse gauge category as:

- objects: finite-dimensional real vertex spaces \(V_I\) and Hilbert edge
  spaces \(E_e\);
- vertex automorphisms: \(\mathrm{GL}(V_I)\);
- edge automorphisms: isometries, or general \(\mathrm{GL}(E_e)\) accompanied
  by metric congruence;
- links: rectangular endpoint restrictions \(V_I\to E_e\).

If oriented coarse fibers are desired, declare orientations and restrict the
ambient gauge group to transformations preserving every induced orientation.
No canonical such restriction follows from the present data.

**Falsification condition.** A canonical \(\mathrm{GL}^{+}(f_I)\) reduction
would have to assign the same orientation to the fixed line before and after
the allowed gauge \(g=-I_2\). It cannot.

**Physicist summary.** An orientation-preserving rotation of the full state
space can flip a surviving one-dimensional mode. The sign of that mode is a
coordinate choice, so the coarse gauge group must allow the flip.

**Architecture placement.** **GENERAL.** State the rank-changing groupoid in
the general geometry/RG architecture. Realize it by fixed subspaces and
rectangular matrices only in the moved MV-Gaussian part.

## Finding EH-5 — Variable fixed spaces are stratified; constant rank is required for an ordinary bundle

**Location.** `02_geometry.tex:75-85`;
`09_coarsegraining.tex:483-502` and `566-569`;
`10_renormalization.tex:34-45`.

**Severity.** Medium as a hidden regularity condition for any continuous or
smooth extension across model/scale parameters.

**Manuscript status.** `02_geometry.tex:85` correctly warns that stratified
fibers require a declared category, but the partial-coarse and RG passages do
not discharge that obligation.

**Review status.** `\status{ESTABLISHED}` as a rank-jump obstruction;
`\status{OPEN}` for a chosen stratified RG construction.

**Plain-English category and inflation verdict.** There is no error at one
fixed finite population. The missing condition appears only when the partial
fibers are promoted to a family over continuously varying links or scale.

### Counterexample

Consider
\[
H(t)=\operatorname{diag}(1,e^t)\in\mathrm{GL}^{+}(2).
\]
Then
\[
\dim\operatorname{Fix}H(t)=
\begin{cases}
2,&t=0,\\
1,&t\neq0.
\end{cases}
\]
The fixed spaces therefore do not form an ordinary vector bundle over any
neighborhood of \(t=0\): vector-bundle rank is locally constant. This is the
standard zero-mode jump at a symmetry-enhanced point.

### Exact repair

State a constant-rank hypothesis whenever smooth bundle language is used.
Without it, stratify the parameter space by fixed-space dimension and treat
rank-changing RG steps as morphisms between strata. Do not define a smooth
connection or parallel transport across a rank jump without additional data.

**Falsification condition.** The finding would fail if an ordinary vector
bundle could have rank two at one point and rank one at every neighboring
point. It cannot by local triviality.

**Physicist summary.** The number of zero modes jumps at a special coupling.
That is a phase-boundary or symmetry-stratum phenomenon, not a smooth bundle of
states.

**Architecture placement.** **GENERAL** as a categorical warning;
**MVG / LINEAR-QUADRATIC REALIZATION** for the explicit kernel-rank
stratification.

## Finding EH-6 — The holonomy determinant theorem has a correct formula and an inflated title

**Location.** `11_obstructions.tex:291-300`.

**Severity.** Low, but worth fixing in a concision pass.

**Manuscript status.** `\status{ESTABLISHED}`.

**Review status.** `\status{ESTABLISHED}` for the formula;
`\status{REFUTED}` for the literal title “the assembled determinant is a
function of the holonomy alone.”

**Plain-English category and inflation verdict.** The proof is correct. The
determinant also depends on the two link covariances:
\[
\det J=
\frac{\det(I-H)^2}{\det R_{uv}\det R_{vu}}.
\]
Only the **transport dependence** factors through holonomy.

**Exact repair.** Rename Proposition 12.10 to:

> The transport dependence of the assembled determinant factors through the
> loop holonomy.

No proof change is needed.

**Falsification condition.** Holding \(H\) fixed while changing
\(\det R_{uv}\) changes \(\det J\), directly falsifying the literal title.

**Physicist summary.** The flux controls the transporter-dependent factor, but
the noise scales still set the overall determinant.

**Architecture placement.** **MVG-SPECIFIC.** Keep with the reciprocal
Gaussian example after the general RG theory.

## What is already sound

- The principal-bundle action is required to be free and transitive only where
  a principal action must be (`02_geometry.tex:21-36`, `331-368`). No improper
  freeness assumption is imposed on the associated law fiber itself.
- The manuscript carefully distinguishes smooth base-connection holonomy,
  pointwise comparison products, and independently declared graph-link
  holonomy (`02_geometry.tex:464-477`; `11_obstructions.tex:340`). The proposed
  cellular sheaf lives on the **population graph** and must not be conflated
  with the sheaf of smooth \(G\)-valued functions on the contextual base.
- The one-step partial-kernel identity and the properness criterion
  \(\operatorname{range}(S)\cap\ker\Lambda=\{0\}\) are correct under their stated
  positive-definite internal-weight and full-column-rank hypotheses
  (`09_coarsegraining.tex:492-530`).
- Corollary 12.9 and the determinant calculation in Proposition 12.10 correctly
  characterize the reciprocal two-cycle. The issue in EH-6 is only the title.

## Concision and flow: exact cuts

The same coarse-link open problem is restated at length in
`09_coarsegraining.tex:566-569`, `867-871`,
`10_renormalization.tex:34-45`, `639-643`, and
`11_obstructions.tex:335-336`. After adding EH-2 and EH-3:

1. Keep the theorem and proof once, in the post-RG MV-Gaussian/sheaf
   realization.
2. Keep one two-sentence open-problem statement there for minimal compression,
   normalized-law compatibility, and rescaling.
3. Replace the other four restatements with one-line cross-references.

This removes several pages of repeated qualifications while making the actual
result stronger.

## Exact theorem directions

### Safe to prove now

1. **Common effective-support quotient theorem.**
   Prove the edge identity
   \(W^{1/2}(I-\Theta)=0\iff q\Theta=q\), and characterize a fixed quotient
   carrying all positive-definite induced weights by the common-kernel and
   kernel-invariance conditions in EH-1.
2. **Nested fixed-section theorem.**
   Prove
   \(\ker L_A=S_A\ker(S_A^{\mathsf T}L_AS_A)\) for nested partitions of a
   positive-semidefinite interaction operator, as in EH-3.
3. **Rectangular sheaf-link closure theorem.**
   Factor each pair form through an edge Hilbert space, prove exact closure by
   precomposition, prove direct-sum compression of parallel cut edges, and
   prove associativity under repeated blocking, as in EH-2.
4. **Rank-changing gauge groupoid proposition.**
   First prove the independent product-gauge construction and the bridge law
   \(K_i\widetilde\Omega_{ij}^{m}=\Omega_{ij}^{b}K_j\). Then prove basis
   covariance with vertex groups \(\mathrm{GL}(V_I)\), exhibit the orientation
   counterexample, and state the constant-rank criterion for an ordinary vector
   bundle.

### Genuinely open after those theorems

5. **Minimal group-link compression and probabilistic RG.**
   Characterize when a stacked rectangular sheaf edge is equivalent to one
   positive-definite weight and one invertible \(\mathrm{GL}^{+}\) transport;
   determine whether a canonical minimal compression exists; then supply
   reference measures, normalizers, rescaling, and cross-level identifications
   needed for an RG flow of normalized laws. Hansen–Ghrist's general sheaf Kron
   no-go shows that exact marginalization cannot be assumed closed, and nothing
   in the present algebra supplies uniqueness or probability-level
   compatibility.

## Final physicist summary

There are four layers, and separating them cleans up the whole nonflat story.

1. The belief and model channels have **independent gauge bundles**. A
   cross-channel coupling is a transforming bridge, not an implicit
   identification of frames.
2. A **group connection** uses invertible maps between equal-dimensional
   fibers, so holonomy is an ordered product.
3. Singular weights can make observability **edge dependent**. Then there may
   be no common support on which that product is defined.
4. The correct general linear object is a **sheaf Laplacian**: each edge says
   which linear combinations of the two endpoint states must agree. Endpoint
   dimensions may differ, and the maps may be rectangular.

Layer 3 is already closed under the manuscript's aggregation because blocking
only composes linear maps. The hard open problem is no longer “does any nonflat
coarse theory exist?” It is “when can this richer, exact coarse datum be
compressed back into the much smaller language of one invertible transporter,
and when does the resulting operator define a compatible normalized
probability law across scales?”
