# Pass-2 graph ML, GNN, pooling, and coarsening audit

**Audit lens:** graph machine learning, message-passing GNNs, graph pooling and
coarsening, graph signal processing, gauge-equivariant graph networks,
oversmoothing, rewiring, and rigorous ML/RG relationships.

**Revision audited:** `f568b7b18973268fc1febafd3805f3cce64f933d`

**Files read:** `main.tex`, `SPEC.md`, `02_geometry.tex`,
`07_restrictions.tex`, `09_coarsegraining.tex`, `10_renormalization.tex`,
`12_philosophy.tex`, the July 29 continuation review and closure ledger, the
verified manuscript ledger, and the Research-vault pages and source notes on
graph Laplacians, spectral graph theory, Laplacian/network RG, geometric deep
learning, gauge-equivariant CNNs, and Mehta--Schwab.

**Protocol note:** the requested `P/D/S/E/C` acronym is not defined in the
review protocol, the manuscript, or the specification. Per the coordinator's
instruction, this memo does not invent an expansion. Each finding instead
records the manuscript's literal status macro, a plain-English audit
classification, and whether the prose inflates that status.

**Bottom line:** no critical or high graph-ML defect was found. The manuscript
does not claim to be a GNN, does not claim that its graph or partition is
learned, does not claim that `S^T Lambda S` preserves arbitrary graph signals
or ELBOs, and does not confuse its hard identification with exact
marginalization. The two medium findings concern the undeveloped bridge from
its exact Galerkin energy restriction to diffusion/message passing. Four
low-severity findings identify scope wording and theorem-grade additions. None
re-raises R1--R21.

## What the current construction is—and is not

| Relationship | Audit classification | Evidence |
|---|---|---|
| Interaction graph and partition | **Fixed structural data** in the present theory; learning either object is only a future estimation/selection problem | `02_geometry.tex:13`; `09_coarsegraining.tex:240-250,451-454`; `12_philosophy.tex:129-131` |
| Hard `0/1` identification followed by \(\Lambda_{\rm c}=S^\top\Lambda S\) | **Exact** quadratic-energy restriction on \(\operatorname{range}S\), under the declared Gaussian interaction-family and flatness hypotheses | `09_coarsegraining.tex:213-279` |
| Aggregation-based algebraic multigrid | **Exact structural identity**: the displayed operator is a Galerkin coarse form with a piecewise-constant prolongator | `09_coarsegraining.tex:276-277` |
| DiffPool-style graph pooling | **Algebraic resemblance only**: DiffPool learns a generally soft assignment, pools node embeddings, and coarsens an adjacency; the manuscript fixes a hard partition and precomposes an energy | Ying et al. 2018 §3.2, equations (3)--(4), versus `09_coarsegraining.tex:240-250` |
| Complete Gaussian-law flow | **Not claimed**: \(h\) aggregates but is excluded from the RG state, and a coarse reference measure and normalizer are still required | `10_renormalization.tex:75-93` |
| Spectrum preservation | **Not established by Galerkin closure**: preserving the interaction family and preserving a low-frequency subspace are different claims | `10_renormalization.tex:454-542`; Loukas 2019 |
| ELBO preservation or ELBO-based scale selection | **Correctly rejected as generic**: different latent inventories bound different evidences | `07_restrictions.tex:304-342` |
| Mehta--Schwab deep-learning/RG equivalence | **Analogy unless its RBM kernel and trace condition are supplied**; it is not the same operation as deterministic energy precomposition | Mehta and Schwab 2014 equations (18)--(22), versus `10_renormalization.tex:85-93` |
| Oversmoothing | **Analogy for the present RG flow**; it becomes an exact theorem only for a separately declared diffusion/message-passing semigroup | `09_coarsegraining.tex:443-446`; `10_renormalization.tex:627-633` |
| Graph rewiring | **Separate model/architecture intervention**, not an exact consequence of the declared blocking | `09_coarsegraining.tex:456-477,867-873` |

## Findings

### 1. The imported Laplacian-RG diffusion rule is not yet gauge-covariant

**Location:** `manuscripts/gauge_vfe_rg/10_renormalization.tex:629-633`

**Severity:** medium

**P/D/S/E/C:** unassigned because the acronym is undocumented. Literal
manuscript status: the generalized-spectrum requirement is `ESTABLISHED`, while
the empirical scale diagnostics are `OPEN`; the sentence calling
diffusion-equivalence a “principled replacement” is untagged. Audit
classification: source-backed construction gap. The phrase “principled
replacement” inflates the present result because the scalar rule has not been
lifted to the manuscript's gauge-typed block setting.

**Evidence:** the executable mathematical path says that local reframing acts
on the interaction form by congruence,
\[
L' = G^{-\top} L G^{-1},
\]
and `10_renormalization.tex:633` correctly requires a generalized spectrum of a
pair. The imported Laplacian RG instead uses the Euclidean heat kernel
\(K_\tau=\exp(-\tau L)\), normalizes it to
\(\rho_\tau=K_\tau/\operatorname{Tr}K_\tau\), and creates blocks by thresholding
its matrix entries; see [Villegas et al. 2023, equations (1) and the real-space
rule](https://www.nature.com/articles/s41567-022-01866-8). Matrix exponentials
are covariant under similarity, not congruence.

An executed two-node, \(K=2\) witness used
\[
L=\begin{pmatrix}I_2&-I_2\\-I_2&I_2\end{pmatrix},\qquad
g=\begin{pmatrix}2&1\\0&1\end{pmatrix},\qquad G=\operatorname{diag}(g,g).
\]
This common frame change remains inside the matrix-weighted interaction family.
The measured discrepancy was
\[
\left\|e^{-L'}-G e^{-L}G^{-1}\right\|_F
=0.5507282503874092.
\]
Declaring a positive reference form repairs the operator covariance. With
\(R=I_4\), \(R'=G^{-\top}RG^{-1}\), \(H=R^{-1}L\), and
\(H'=(R')^{-1}L'\), the same check returned
\[
\left\|e^{-H'}-G e^{-H}G^{-1}\right\|_F=0,
\]
because \(H'=GHG^{-1}\). Thus \(\operatorname{Tr}e^{-\tau H}\), its generalized
eigenvalues, and spectral entropy can be frame independent.

That repair still does not recover Villegas et al.'s entrywise communicability
rule. A generic \(R\succ0\) need not produce a Markov generator. For the
two-node scalar Laplacian and
\[
R=\begin{pmatrix}5&-2\\-2&1\end{pmatrix}\succ0,
\qquad
-R^{-1}L=\begin{pmatrix}1&-1\\3&-3\end{pmatrix},
\]
one off-diagonal generator entry is negative. For \(K>1\), raw heat-kernel
blocks also change by \(K'_{ij}=g_iK_{ij}g_j^{-1}\), so entry thresholds have no
frame-independent meaning. Cohen et al.'s gauge-equivariant construction
requires feature transport and an intertwining constraint rather than
coordinate-entry invariance; see [Cohen et al. 2019
§2.3--2.4](https://proceedings.mlr.press/v97/cohen19d.html).

**Falsification condition:** this finding is defeated by a declared admissible
reference class \(R\), the generator \(H=R^{-1}L\), a proof of its gauge
covariance, and a block-selection statistic invariant under
\(K_{ij}\mapsto g_iK_{ij}g_j^{-1}\), together with any positivity assumptions
needed for the word “diffusion.”

**Concrete repair:** replace “the diffusion-equivalence rule is a principled
replacement” with an `OPEN` gauge-lift statement, then define the
\(R\)-self-adjoint heat semigroup and use invariant block scores—for example,
when \(R=\operatorname{blkdiag}(R_i)\),
\(\operatorname{Tr}(R_iK_{ij}R_j^{-1}K_{ij}^{\top})\)—instead of raw entries.

**Placement after the requested reordering:** state the abstract
similarity-covariant semigroup for a pair of forms in the general RG part; put
the block-\(\GL^+(K)\) counterexample, the local \(R_i\) score, and the
matrix-weighted diffusion interpretation in the later Gaussian realization.

### 2. Galerkin energy closure does not supply coarse message passing

**Location:** `manuscripts/gauge_vfe_rg/09_coarsegraining.tex:240-250`;
`manuscripts/gauge_vfe_rg/10_renormalization.tex:75-93`

**Severity:** medium

**P/D/S/E/C:** unassigned because the acronym is undocumented. Literal
manuscript status: `DEFINITION`, with the limitation on complete Gaussian laws
stated explicitly. Audit classification: missing graph-signal/ML bridge. The
current local claims are not inflated; the gap matters when Chapter 10 invokes
Laplacian diffusion as a partition selector.

**Evidence:** \(L_{\rm c}=S^\top L S\) is a bilinear form. A propagation
operator additionally needs a reference or mass form. If fine signals use
\(\langle x,y\rangle_R=x^\top Ry\), then the induced objects are
\[
M_{\rm c}=S^\top R S,\qquad
H_{\rm c}=M_{\rm c}^{-1}S^\top L S,\qquad
C=M_{\rm c}^{-1}S^\top R.
\]
The manuscript already records \(S^\top S=\operatorname{diag}(n_I)\otimes I_K\)
at line 250, but no coarse reference-form flow, reduction \(C\), node-signal
map, or message-passing intertwining law is declared.

An executed scalar path-graph witness used clusters
\(\{1,2\}\) and \(\{3\}\):
\[
L=\begin{pmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{pmatrix},\quad
S=\begin{pmatrix}1&0\\1&0\\0&1\end{pmatrix}.
\]
It gives
\[
L_{\rm c}=\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad
M_{\rm c}=\operatorname{diag}(2,1).
\]
Treating \(L_{\rm c}\) as an ordinary Euclidean generator gives eigenvalues
\((0,2)\); the generalized pair \((L_{\rm c},M_{\rm c})\) gives
\((0,1.5)\). For \(x=(1,0,-1)\) and one Euler step with \(\alpha=0.2\),
fine-step-then-pool returned \((0.4,-0.8)\), while
pool-then-\(H_{\rm c}\) returned \((0.35,-0.7)\), error
\(0.1118033989\). Using \(L_{\rm c}\) naively returned \((0.2,-0.7)\), error
\(0.2236067977\). The mass correction fixes the typing; it does not force
commutation because \(\operatorname{range}S\) is not invariant under the fine
generator.

This distinction is established in current graph-coarsening theory.
[Loukas 2019](https://www.jmlr.org/papers/v20/18-680.html) proves restricted
spectral and cut guarantees under additional approximation conditions; the
Galerkin identity alone is not that guarantee. [Joly and Keriven 2024
§3](https://proceedings.neurips.cc/paper_files/paper/2024/hash/d041d6bb47c01a4ce327a1773703e9a0-Abstract-Conference.html)
show that even high-quality spectral coarsening need not preserve naive message
passing and introduce a generally oriented coarse propagation matrix,
\(S_{\rm c}^{\rm MP}=QSQ^+\), with a theorem bounding the lifted signal error.

The probability boundary is already correctly stated:
`10_renormalization.tex:83` excludes \(h\) from the RG state and says that this
prevents reading the flow as complete Gaussian laws; lines 85--93 require a
coarse reference measure and normalizer. Likewise,
`07_restrictions.tex:304-339` proves that ELBOs across changed latent
inventories do not furnish a generic coarse-graining cost. The missing object
is therefore a graph-signal map, not another ELBO claim.

**Falsification condition:** this finding is defeated by a declared
prolongation/reduction pair, a flowed reference form or mass matrix, a coarse
propagator, and either an exact intertwining theorem or a quantitative error
bound on a named signal subspace.

**Concrete repair:** add a proposition separating (i) exact quadratic-form
restriction, (ii) generalized spectral approximation, and (iii)
message-passing preservation, with
\[
CH-H_{\rm c}C=CH(I-SC)
\]
as the exact residual and \(\operatorname{range}S\)-invariance as the
self-adjoint exact-commutation condition.

**Placement after the requested reordering:** put the prolongation/reduction
and intertwining theorem in the pre-Gaussian general coarse-map/RG theory.
Instantiate \(M_{\rm c}=S^\top RS\), \(h_{\rm c}=S^\top h\), and the numerical
path witness only in the later multivariate-Gaussian part.

### 3. Hard closure fails for ordinary learnable soft pooling, and “not permitted” is overbroad

**Location:** `manuscripts/gauge_vfe_rg/09_coarsegraining.tex:240-279`

**Severity:** low

**P/D/S/E/C:** unassigned because the acronym is undocumented. Literal
manuscript status: hard aggregation is `DEFINITION` and its closure theorem is
`ESTABLISHED`. Audit classification: scope boundary plus a concrete negative
extension result. The theorem is correct; the words “no ... fitted coarse
coupling is ... permitted” at line 279 overstate its domain.

**Evidence:** the proof uses a hard \(0/1\) partition. DiffPool instead learns a
soft row assignment and computes both pooled embeddings
\(X_{\rm c}=S^\top Z\) and a pooled adjacency \(A_{\rm c}=S^\top A S\); see
[Ying et al. 2018 §3.2, equations
(3)--(4)](https://proceedings.neurips.cc/paper_files/paper/2018/hash/e77dbaf6759253c7c6d0efc5690369c7-Abstract.html).
Learning or softening \(S\) is not a harmless generalization of the manuscript's
interaction-family theorem.

An executed connected path on four nodes, with three soft clusters, used
\[
S=\begin{pmatrix}
.40&.40&.20\\
.10&.10&.80\\
.10&.11&.79\\
.09&.11&.80
\end{pmatrix}.
\]
Every row sums to one, \(S\) has full column rank, and the fine \(L\) is the
ordinary path Laplacian. The coarse form was
\[
S^\top LS=
\begin{pmatrix}
.0901&+.0900&-.1801\\
.0900&+.0901&-.1801\\
-.1801&-.1801&+.3602
\end{pmatrix}.
\]
It is positive semidefinite and has zero row sums, but its \((1,2)\) off-diagonal
is \(+0.09\). It therefore cannot be written in the manuscript's scalar
interaction family, whose off-diagonals must be \(-W_{IJ}\leq0\). Hard
partition closure does not extend to standard soft assignments.

Learned coarse couplings remain legitimate as different approximate
architectures. [Cai, Wang, and Wang
2021](https://openreview.net/forum?id=uxpzitPEooJ) explicitly learn coarse edge
weights to improve coarsening quality. Such a model does not inherit the exact
hard-identification semantics, sufficient-statistic map, or closure theorem.

**Falsification condition:** the negative extension is defeated by a proof that
the displayed full-rank row-stochastic witness belongs to the interaction
family; the wording issue is defeated by explicitly restricting “not
permitted” to exact hard energy precomposition within the declared family.

**Concrete repair:** change line 279 to “no separate fitted coupling is
permitted **if the target is the exact hard-identification trace in this
interaction family**,” and add the soft-assignment witness as the boundary to
learnable graph pooling.

**Placement after the requested reordering:** the abstract distinction between
fixed hard maps and data-dependent Markov/learned maps belongs in the general
coarse-map theory. The positive-off-diagonal witness is a Gaussian
matrix-weighted realization and should appear after the reordered Gaussian
part begins.

### 4. The open partition problem lacks a permutation- and gauge-equivariant ML formulation

**Location:** `manuscripts/gauge_vfe_rg/09_coarsegraining.tex:451-477`;
`manuscripts/gauge_vfe_rg/09_coarsegraining.tex:823-855`

**Severity:** low

**P/D/S/E/C:** unassigned because the acronym is undocumented. Literal
manuscript status: partition selection is `OPEN`; the coarse-frame
nonidentifiability and \(\GL^+(K)\)-valued pooling no-go are `ESTABLISHED`.
Audit classification: constructive theorem-grade extension. There is no
inflated current claim.

**Evidence:** `09_coarsegraining.tex:454` proves that admissibility filters
partitions but selects none. Lines 845--855 prove that a symmetric,
left-equivariant map
\(\GL^+(K)^n\to\GL^+(K)\) cannot choose a coarse frame. That no-go does **not**
forbid a scalar cluster-assignment matrix: its codomain and transformation law
are different.

The graph itself is also fixed at this stage. `02_geometry.tex:13` types the
interaction structure as finite combinatorial data in the structural
configuration \(X\); `12_philosophy.tex:129-131` places estimation of
\((U_i,A_i,W_{ij},L_{ij})\) in an empirical extension that has not been
supplied. A learned graph or learned partition would therefore be a new
statistical map, not an alternative reading of the current declarations.

For a fine-node permutation \(P\) and coarse-label permutation \(Q\), the
correct assignment law is
\[
S(P\!\cdot\!X)=P\,S(X)\,Q^\top.
\]
If \(\Lambda'=P\Lambda P^\top\), direct substitution gives
\[
(PSQ^\top)^\top\Lambda'(PSQ^\top)
=Q(S^\top\Lambda S)Q^\top .
\]
Likewise pooled node features transform as
\((PSQ^\top)^\top(PZ)=Q(S^\top Z)\). This is the exact algebra behind the
permutation result in [Ying et al. 2018,
Proposition 1](https://proceedings.neurips.cc/paper_files/paper/2018/hash/e77dbaf6759253c7c6d0efc5690369c7-Abstract.html).
The manuscript declares an abstract partition, so it is safe under relabeling,
but any **selector** or learned assignment must satisfy this law.

Gauge typing adds a second condition. Assignment scores must be built from
gauge-invariant scalars; otherwise a change of local frames changes which
agents are clustered. A typed message rule can be stated without choosing a
coarse frame. If node features obey \(x_i'\!=\rho(g_i)x_i\), links obey
\(L_{ij}'=g_iL_{ij}g_j^{-1}\), and \(a_{ij}\) is invariant, then
\[
m_i=\sum_j a_{ij}\rho(L_{ij})x_j
\quad\Longrightarrow\quad
m_i'=\rho(g_i)m_i .
\]
This is the discrete message-passing counterpart of the transport and
intertwining requirements in [Cohen et al. 2019
§2](https://proceedings.mlr.press/v97/cohen19d.html). It also explains the
manuscript's exact cut obstruction: lines 456--477 prove that disagreeing cut
twists cannot be compressed to one \(\GL^+(K)\) link without retaining an
excess term.

**Falsification condition:** this opportunity disappears if the manuscript
declines every learned or algorithmic partition selector. It becomes closed if
an assignment rule is given, its node-permutation and local-gauge laws are
proved, and it is shown to preserve the holonomy admissibility filter.

**Concrete repair:** add an `OPEN` problem asking for a scalar,
permutation-equivariant and gauge-invariant assignment rule whose hard output
passes the established holonomy test; state explicitly that the coarse-frame
no-go does not rule out this differently typed selector.

**Placement after the requested reordering:** state the permutation law and
typed-message naturality condition in the general graph/coarse-map part before
Gaussian models. Put the \(\GL^+(K)\) link law, holonomy filter, and
\(\Delta_{IJ}\) obstruction in the later gauge-Gaussian realization.

### 5. Oversmoothing is only an analogy here, but a holonomy-fixed diffusion theorem is available

**Location:** `manuscripts/gauge_vfe_rg/09_coarsegraining.tex:443-446`;
`manuscripts/gauge_vfe_rg/10_renormalization.tex:627-633`

**Severity:** low

**P/D/S/E/C:** unassigned because the acronym is undocumented. Literal
manuscript status: the holonomy/kernel statement is `ESTABLISHED`; no
oversmoothing claim is currently made. Audit classification: exact theorem
opportunity plus analogy fence. There is no current inflation.

**Evidence and derivation:** let \(R\succ0\), \(L\succeq0\), and
\(H=R^{-1}L\). The operator is self-adjoint and positive in the
\(R\)-inner product and is similar to
\(R^{-1/2}LR^{-1/2}\). The finite-dimensional spectral theorem therefore gives
\[
e^{-tH}\longrightarrow \Pi_{\ker L}^{(R)}
\quad(t\to\infty),
\qquad
\left\|e^{-tH}-\Pi_{\ker L}^{(R)}\right\|_R
\le e^{-t\lambda_+},
\]
where \(\lambda_+\) is the smallest positive generalized eigenvalue of
\((L,R)\). This is an exact diffusion-collapse statement.

For the manuscript's positive-definite internal edge weights,
`09_coarsegraining.tex:443-446` identifies \(\ker L\) with parallel sections
whose seed lies in the fixed subspace of the graph holonomy group. The
diffusion limit is therefore not generically “all node features become one
Euclidean constant.” It is the \(R\)-orthogonal projection onto
holonomy-fixed parallel sections. Trivial holonomy on a connected graph
recovers transported constants; nontrivial holonomy can reduce that surviving
fiber.

This supplies a rigorous connection to oversmoothing, but only for the
declared linear semigroup. [Oono and Suzuki
2020](https://arxiv.org/abs/1905.10947) prove exponential approach to a
low-information subspace for GCNs under spectral and weight conditions; it is
not an unconditional theorem for every learned GNN. Current work makes that
boundary sharper: [Zhuo et al.
2025](https://proceedings.mlr.press/v260/zhuo25a.html) construct weight choices
that avoid oversmoothing, including at infinite depth. The manuscript's
changing-dimension blocking flow is not repeated message passing and should
not be called oversmoothing without the separate \(H\)-semigroup declaration.

Rewiring belongs on the other side of the same fence. Curvature-based rewiring
can mitigate GNN over-squashing; see [Topping et al.
2022](https://arxiv.org/abs/2111.14522). Here, adding or changing an edge
changes \(L\), the Gaussian energy, and potentially the graph-link holonomy.
It is a new model/architecture operation, not a consequence of
\(S^\top\Lambda S\), and it requires a new gauge-typed link on every added
edge.

**Falsification condition:** the analogy warning is defeated only by an
explicit message-passing architecture whose layer operator is the declared
semigroup or a controlled discretization of it. The theorem is defeated by a
counterexample to the finite-dimensional spectral decomposition under
\(R\succ0\) and \(L\succeq0\).

**Concrete repair:** add the heat-limit proposition with the holonomy-fixed
kernel corollary, label the GNN interpretation `NOT-CLAIMED` outside its
linear/weight hypotheses, and classify any rewiring as a separate,
gauge-typed model-selection intervention.

**Placement after the requested reordering:** put the \(R\)-self-adjoint heat
limit in the general spectral/RG theory. State the holonomy-fixed corollary and
the graph-neural oversmoothing/rewiring comparison only in the later
matrix-weighted gauge-Gaussian realization.

### 6. The RG literature section omits the exact ML/RG precedent and its limiting hypothesis

**Location:** `manuscripts/gauge_vfe_rg/10_renormalization.tex:612-615`;
`manuscripts/gauge_vfe_rg/10_renormalization.tex:85-93`

**Severity:** low

**P/D/S/E/C:** unassigned because the acronym is undocumented. Literal
manuscript status: no current Mehta--Schwab claim exists. Audit classification:
primary-source literature omission. There is no current prose inflation, but a
future “architecture is RG” sentence would be false without the distinction
below.

**Evidence:** the chapter says that three bodies of RG literature bear on its
construction, but it omits the standard deep-learning/RG precedent.
[Mehta and Schwab 2014](https://arxiv.org/abs/1410.3831) establish a one-to-one
mapping between variational RG and RBM-based deep networks by identifying the
RG operator with an RBM joint energy. Their exact conditional reading requires
the trace condition
\[
\operatorname{Tr}_{h}\exp T(v,h)=1;
\]
their equations (18)--(22) then equate the RG Hamiltonian and RBM hidden
Hamiltonian and, in the exact case, reproduce the data distribution.

The present manuscript performs a different operation:
\(y=S\tilde y\) embeds coarse variables as configurations constant on hard
clusters and precomposes the energy. `09_coarsegraining.tex:101-122` proves
that this is not restriction of a continuous fine law to a null subspace and
requires a newly declared coarse reference measure and normalizer.
`10_renormalization.tex:83-93` further excludes \(h\) from the RG state. Thus
Mehta--Schwab is an exact precedent **inside its RBM/variational-RG
construction**, not a theorem identifying the present deterministic
aggregation with a deep network.

**Falsification condition:** the omission is defeated by a checked
Mehta--Schwab citation and a comparison that records the RBM hidden-variable
kernel, trace condition, marginalization, and the present map's different
sample-space direction.

**Concrete repair:** add a fourth, short literature subsection titled
“Variational RG and deep architectures,” classifying the relationship as a
historical exact precedent with an analogical connection to the present flow,
not as inherited exactness.

**Placement after the requested reordering:** this comparison belongs in the
general RG literature before any multivariate-Gaussian realization. A later
Gaussian note may then say that the hard linear map is one concrete
operator-flow instance, still not an RBM layer.

## Theorem-grade open directions

1. **Abstract message-passing/coarse-map intertwining.** Let \(P:V_c\to V_f\)
   be a prolongation, \(C:V_f\to V_c\) a reduction with \(CP=I\), and \(H\) a
   fine operator. Define \(H_c=CHP\). Prove exact commutation criteria for
   \(CH=H_cC\) and quantitative bounds in terms of
   \(CH(I-PC)\). This is general linear/coarse-map theory and belongs before
   the Gaussian realization. The Gaussian instance uses
   \(P=S\), \(C=(S^\top RS)^{-1}S^\top R\).

2. **Permutation- and gauge-natural learned blocking.** Construct a scalar
   assignment functor satisfying
   \(S(P\!\cdot\!X)=PS(X)Q^\top\), invariant under local frame changes, and
   constrained so its hard cells are graph-trivializing. Prove that the
   resulting coarse map is natural under node isomorphisms and residual coarse
   gauge transformations. The general naturality theorem belongs before
   Gaussian models; holonomy admissibility is the later gauge realization.

3. **Gauge-covariant heat flow and holonomy-fixed oversmoothing.** For a
   declared local reference form, prove similarity covariance of
   \(e^{-tR^{-1}L}\), define invariant block communicability, and prove
   convergence at the generalized spectral-gap rate to the
   holonomy-fixed parallel-section space. Separate Euclidean positivity,
   vector-bundle diffusion, and GNN weight assumptions.

4. **Approximate spectral and probabilistic preservation.** Combine a
   Loukas-style restricted spectral approximation with the manuscript's
   matched coarse reference measure. Under explicit
   \((1-\varepsilon)A\preceq B\preceq(1+\varepsilon)A\) hypotheses on a
   matched subspace, derive log-determinant, zero-mean Gaussian KL, and
   filtered-signal error bounds. Do not call the result ELBO preservation
   across latent inventories; Proposition 8.18 forbids that generic reading.

5. **Soft-assignment closure classification.** Characterize the
   row-stochastic matrices \(S\) for which \(S^\top LS\) is an
   \(M\)-matrix/Laplacian for every scalar or matrix-weighted Laplacian \(L\).
   The executed full-rank soft witness above proves that ordinary softmax
   assignments are not sufficient. A positive classification would identify
   which learnable pooling families can remain inside the manuscript's
   interaction cone.

## Placement map for the requested theory-first reordering

| Proposed material | General theory/RG before Gaussian | Later multivariate-Gaussian realization |
|---|---|---|
| Coarse maps and message passing | \(P,C,H,H_c\), naturality, exact residual and approximation theorem | \(S^\top RS\), \(S^\top\Lambda S\), \(S^\top h\), path witness |
| Fixed versus learnable partitions | Deterministic, Markov, and data-dependent map types; permutation law | Hard-\(0/1\) closure and soft-assignment \(M\)-matrix counterexample |
| Gauge-typed graph learning | Abstract represented features, transported messages, intertwining | \(\GL^+(K)\) links, matrix weights, holonomy, \(\Delta_{IJ}\) |
| Diffusion and spectra | Pair-of-forms heat semigroup, generalized spectrum, intertwining | Matrix-weighted connection Laplacian, local reference blocks, invariant communicability |
| Oversmoothing and rewiring | Conditional semigroup theorem; rewiring typed as a model intervention | Holonomy-fixed kernel and energy change from added gauge links |
| ML/RG history | Mehta--Schwab, DiffPool, Loukas, Joly--Keriven, with exact/structural/analogy labels | Gaussian realization only after those boundaries are fixed |

## Plain-language summary for a physicist

The graph in this manuscript is presently a fixed piece of model structure,
not a graph learned from data. Its blocking matrix identifies all variables in
one cluster and restricts the quadratic energy to that subspace. That operation
is exact and is the same Galerkin algebra used in multigrid. It is not, by
itself, a neural pooling layer: a GNN also needs a rule for pooling signals, a
propagation operator, a learnable or fixed assignment policy, and permutation
equivariance.

The closest new ML connection is diffusion. Once a positive reference form is
declared, \(R^{-1}L\) gives a coordinate-covariant heat flow, and long-time
diffusion projects onto the modes fixed by graph holonomy. That is a precise
gauge version of linear oversmoothing. It should not be identified with the
current changing-dimension RG flow or with every trained GNN. Learned soft
pooling and rewiring are valid extensions, but they change the model and do
not inherit the manuscript's exact closure theorem.

## Primary sources checked

- [Ying et al., “Hierarchical Graph Representation Learning with
  Differentiable Pooling,” NeurIPS
  2018](https://proceedings.neurips.cc/paper_files/paper/2018/hash/e77dbaf6759253c7c6d0efc5690369c7-Abstract.html)
- [Loukas, “Graph Reduction with Spectral and Cut Guarantees,” JMLR
  2019](https://www.jmlr.org/papers/v20/18-680.html)
- [Joly and Keriven, “Graph Coarsening with Message-Passing Guarantees,”
  NeurIPS
  2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/d041d6bb47c01a4ce327a1773703e9a0-Abstract-Conference.html)
- [Cai, Wang, and Wang, “Graph Coarsening with Neural Networks,” ICLR
  2021](https://openreview.net/forum?id=uxpzitPEooJ)
- [Gilmer et al., “Neural Message Passing for Quantum Chemistry,” ICML
  2017](https://proceedings.mlr.press/v70/gilmer17a.html)
- [Cohen et al., “Gauge Equivariant Convolutional Networks and the Icosahedral
  CNN,” ICML 2019](https://proceedings.mlr.press/v97/cohen19d.html)
- [Bronstein et al., “Geometric Deep Learning: Grids, Groups, Graphs,
  Geodesics, and Gauges,”
  2021](https://arxiv.org/abs/2104.13478)
- [Villegas et al., “Laplacian Renormalization Group for Heterogeneous
  Networks,” Nature Physics
  2023](https://www.nature.com/articles/s41567-022-01866-8)
- [Oono and Suzuki, “Graph Neural Networks Exponentially Lose Expressive Power
  for Node Classification,” ICLR
  2020](https://arxiv.org/abs/1905.10947)
- [Zhuo et al., “Graph Neural Networks (with Proper Weights) Can Escape
  Oversmoothing,” ACML
  2025](https://proceedings.mlr.press/v260/zhuo25a.html)
- [Topping et al., “Understanding Over-Squashing and Bottlenecks on Graphs via
  Curvature,” ICLR 2022](https://arxiv.org/abs/2111.14522)
- [Mehta and Schwab, “An Exact Mapping between the Variational Renormalization
  Group and Deep Learning,”
  2014](https://arxiv.org/abs/1410.3831)

## Verification disposition

| Claim | State | Closure evidence |
|---|---|---|
| Raw \(e^{-\tau L}\) is not covariant under the manuscript's general congruence action | `EVIDENCE_VERIFIED` | Exact transformation algebra plus current executed \(K=2\) block witness |
| \(e^{-\tau R^{-1}L}\) is similarity covariant when \(R\) transforms with \(L\) | `EVIDENCE_VERIFIED` | Exact derivation plus executed zero-residual control |
| Galerkin quadratic closure does not imply message-passing commutation | `EVIDENCE_VERIFIED` | Exact residual identity, current path witness, Loukas 2019, Joly--Keriven 2024 |
| Generic soft row assignments need not preserve the interaction-family sign structure | `EVIDENCE_VERIFIED` | Current connected-path, full-column-rank executed witness |
| A scalar permutation/gauge-natural selector is not prohibited by the \(\GL^+(K)\)-valued coarse-frame no-go | `EVIDENCE_VERIFIED` | Type comparison and exact transformation law |
| Pure \(R\)-self-adjoint diffusion converges to the holonomy-fixed kernel | `EVIDENCE_VERIFIED` | Finite-dimensional spectral derivation plus the manuscript's established kernel theorem |
| Mehta--Schwab exactness does not transfer automatically to hard energy precomposition | `EVIDENCE_VERIFIED` | Checked primary equations (18)--(22) and current manuscript map types |

**Finding count:** 0 critical, 0 high, 2 medium, 4 low.
