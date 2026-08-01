# Holonomy, transported belief KL, and meta-agent coarse-graining

Date: 2026-08-01
Scope: theorem-level investigation only; no manuscript source has been changed in this pass.

## Verdict in plain language

The anticipated mechanism is substantially correct, but it contains two logically different
conditions.

1. **Holonomy controls what can agree.** It fixes the dimension and type of the parallel, or
   frustration-free, subspace available to a cluster.
2. **Transported belief KL controls whether the present beliefs do agree.** It measures how far the
   actual state is from one common transported belief law.

Trivial represented holonomy therefore removes a geometric obstruction to a full-dimensional
meta-agent. It does not make the agents' beliefs equal. Conversely, nontrivial holonomy need not
forbid zero-loss marginal pooling for a particular state: a belief law can be invariant under a
nonidentity holonomy. Losslessness of the full joint population experiment is a further
recovery/sufficiency question.

The clean theory is consequently a conjunction:

> geometric admissibility (holonomy) + statistical coherence (transported KL) + model-selection
> license (free energy or description length) + closure of the cut data.

## 1. Typed setup

Let \(I\) be a finite connected interaction subgraph. For channel \(x\in\{b,m\}\), let
\(\mathscr B_i^x\) be the statistical-law fiber at node \(i\), and let

\[
\Omega^x_\gamma:\mathscr B_i^x\longrightarrow\mathscr B_j^x
\]

be the bimeasurable, invertible transport assigned to a declared path \(\gamma:i\to j\). This can
be either a graph-link transport, where the edge label is part of the interaction data, or
associated-bundle parallel transport induced by the chosen connection along a declared base curve.
These are not interchangeable without the curve-assignment hypothesis already stated in
02_geometry.tex.

Choose a root \(r\in I\). The channel-\(x\) holonomy group is

\[
\operatorname{Hol}_I^x(r)
:=\{\Omega^x_\ell:\ell\text{ is an internal loop based at }r\}.
\]

Only the **represented** holonomy matters to a channel. A nonidentity principal holonomy can act
trivially in a nonfaithful belief representation and nontrivially in the model representation.
If the two channels use different connections, even their underlying principal holonomies can
differ.

Strict vertex-coboundary links \(U_iU_j^{-1}\) have trivial graph holonomy on every loop. In that
regime holonomy cannot select clusters; a nontrivial discriminator requires edge-relaxed links or
parallel transport along declared base curves.

## 2. Linear holonomy theorem: the dimension of the consensus manifold

Let \(V_x\simeq\mathbb R^{K_x}\) be a linear represented fiber. For an internal oriented edge
\(e:j\to i\), let \(\Theta_e^x:V_x\to V_x\) be invertible and \(W_e^x\succ0\). Define

\[
\mathcal E_I^x(z)
=\frac12\sum_{e:j\to i}
(z_i-\Theta_e^xz_j)^\top W_e^x(z_i-\Theta_e^xz_j)
=\frac12 z^\top L_I^xz.
\]

### Theorem 1 (holonomy-fixed consensus space)

For connected \(I\),

\[
\ker L_I^x\cong
\operatorname{Fix}(\operatorname{Hol}_I^x(r)),
\qquad
f_I^x:=\dim\ker L_I^x
=\dim\operatorname{Fix}(\operatorname{Hol}_I^x(r)).
\]

Hence:

- \(f_I^x=K_x\) exactly when every represented internal holonomy acts as the identity;
- \(0<f_I^x<K_x\) gives an exact reduced-dimensional meta-variable;
- \(f_I^x=0\) leaves no nonzero parallel linear mode and must not be called a meta-agent; it is a
  zero-dimensional pinning or rejection case.

#### Proof

Positive-definite edge weights imply \(z\in\ker L_I^x\) exactly when
\(z_i=\Theta_e^xz_j\) on every internal edge. Fix a spanning tree. A root value \(v=z_r\)
determines every other vertex value uniquely by tree transport. Each non-tree edge closes a
fundamental cycle and imposes \(H_\ell^xv=v\). Fundamental-cycle holonomies generate the graph
holonomy group, so allowed root values are exactly its common fixed subspace. Conversely, any
fixed root value extends by tree transport to a zero-energy parallel section. This is a linear
isomorphism and proves the dimension statement.

The same proof with positive-semidefinite weights requires the effective-support or sheaf
qualification already derived in 09_coarsegraining.tex; edge-local null directions can hide
nonidentity transport and need not define one common quotient.

### Corollary 1 (alignment dynamics)

For a constant covariant mass form \(M_I^x=(M_I^x)^\top\succ0\), consider

\[
M_I^x\dot z=-L_I^xz,
\qquad M_I^x\succ0,
\]

The solution converges to the \(M_I^x\)-orthogonal projection onto \(\ker L_I^x\):
\[
P_{\ker L}^{M}
=S_I(S_I^\top M_I^xS_I)^{-1}S_I^\top M_I^x.
\]
On its orthogonal complement the convergence rate is controlled by the smallest positive
eigenvalue of
\((M_I^x)^{-1/2}L_I^x(M_I^x)^{-1/2}\), and
\[
\frac{d}{dt}\left(\frac12z^\top L_I^xz\right)
=-\lVert\dot z\rVert_{M_I^x}^2.
\]
Thus holonomy fixes the dimension of the attractor; the alignment energy supplies the force toward
it. Under a general \(GL\) gauge change, the mass form must co-transform by congruence. The special
choice \(M=I\) is invariant only under the corresponding orthogonal subgroup.

This is the rigorous version of "trivial holonomy permits agents to coalesce." It becomes an actual
coalescence statement only after dynamics or a state condition places the beliefs on that
manifold.

### When the alignment energy is belief KL

For Gaussian beliefs, suppose edge transport \(e:j\to i\) sends
\((\mu_j,\Sigma_j)\) to
\((\Theta_e\mu_j,\Theta_e\Sigma_j\Theta_e^\top)\), and suppose the covariances
are already parallel:
\[
\Sigma_i=\Theta_e\Sigma_j\Theta_e^\top.
\]
Then
\[
D_{\mathrm{KL}}\!\left(
\mathcal N(\mu_i,\Sigma_i)
\middle\Vert
\Theta_{e\#}\mathcal N(\mu_j,\Sigma_j)
\right)
=\frac12(\mu_i-\Theta_e\mu_j)^\top
\Sigma_i^{-1}(\mu_i-\Theta_e\mu_j).
\]
The pairwise belief-KL energy is therefore exactly a connection-Laplacian
quadratic form in the mean sector. More generally, on a regular statistical
manifold near one parallel law, transported KL has the Fisher expansion
\[
D_{\mathrm{KL}}(q_{\theta+\delta_i}\Vert
\Omega_{e\#}q_{\theta+\delta_j})
=\frac12\lVert\delta_i-T_e\delta_j\rVert_F^2
+O(\lVert\delta\rVert^3).
\]
Thus Theorem 1 is exact in this Gaussian sector and is the local
information-geometric linearization in the general case. Global convergence
for arbitrary law families still needs convexity, support, and completeness
hypotheses. In particular, a sample-space interaction Laplacian is not automatically a recognition
Fisher tensor or a natural-gradient operator; the identification requires the displayed Gaussian
or frozen-local-Fisher hypotheses.

## 3. General statistical theorem: holonomy-conditioned KL distortion

Let \(q_i^x\in\mathscr B_i^x\) be the current law at node \(i\), choose positive weights
\(w_i\) summing to one, and choose paths \(\gamma_i:i\to r\). Write

\[
\bar q_i^x=(\Omega^x_{\gamma_i})_\#q_i^x.
\]

Let \(\mathcal Q_r^x\) be the declared parent-law family at the root, stable under the represented
action, and define its holonomy-fixed part by

\[
\mathcal Q_{I,\mathrm{fix}}^x
:=\left\{Q\in\mathcal Q_r^x:
(H^x)_\#Q=Q\ \text{for every }H^x\in\operatorname{Hol}_I^x(r)\right\}.
\]

With the convention that an infimum over the empty set is \(+\infty\), define

\[
\boxed{
\mathcal K_I^x
:=\inf_{Q\in\mathcal Q_{I,\mathrm{fix}}^x}
\sum_{i\in I}w_i\,
D_{\mathrm{KL}}(\bar q_i^x\Vert Q).}
\]

### Theorem 2 (gauge- and path-independent marginal coalescence distortion)

Assume the transports are bimeasurable bijections and the parent family is action-stable.

1. \(\mathcal K_I^x\) is independent of root, chosen paths, and local gauge trivializations.
2. If the infimum is attained and all \(w_i>0\), then \(\mathcal K_I^x=0\) exactly when the
   constituent laws form one parallel section of the law bundle over \(I\).
3. If represented holonomy is trivial, the fixed-law constraint disappears and
   \(\mathcal K_I^x\) is the ordinary transported forward-KL barycenter distortion.

#### Proof

Changing the path from \(i\) to \(r\) composes \(\bar q_i^x\) with some root holonomy \(H_i^x\).
For every admissible \(Q\), holonomy invariance and KL invariance under a common bimeasurable
pushforward give

\[
D_{\mathrm{KL}}((H_i^x)_\#\bar q_i^x\Vert Q)
=D_{\mathrm{KL}}((H_i^x)_\#\bar q_i^x\Vert(H_i^x)_\#Q)
=D_{\mathrm{KL}}(\bar q_i^x\Vert Q).
\]

A root change conjugates the holonomy group and pushes every candidate law and transported
constituent through the same bijection; the same identity applies. A gauge change does the same in
local coordinates. This proves item 1.

Every KL term is nonnegative and is zero exactly when its two laws agree. With positive weights,
an attained total of zero is therefore equivalent to
\(\bar q_i^x=Q_*\) for every \(i\), where \(Q_*\) is holonomy invariant. This equality is exactly a
path-independent parallel law section. The converse is immediate. Item 3 follows because the
fixed-law set is then the whole parent family.

This theorem concerns the collection of **one-agent marginal belief laws**. It does not by itself
prove that the joint population law can be replaced losslessly by one parent latent. For example,
\(n\) independent identical laws \(Q^{\otimes n}\) have zero pairwise and barycenter distortion,
but hard tying replaces them by a diagonal law and destroys their independent fluctuations.
Equivalently, an independent pair of fair Bernoulli variables and a perfectly correlated fair
Bernoulli pair have the same one-agent marginals but different joint laws, so no recovery kernel
fed only that shared marginal can reconstruct both experiments.
Exact joint coarse-graining additionally requires a declared Markov coarse channel with a common
recovery kernel (or an equivalent sufficient-statistic theorem), together with closure of the
generative and cut data. This is the equality/recovery obligation already developed in
06_general_coarsegraining.tex.

### Two decisive counterexamples

1. **Trivial holonomy is not sufficient for belief agreement.** Take two nodes with identity
   transport and \(q_1=\mathcal N(-a,I)\), \(q_2=\mathcal N(a,I)\), \(a\ne0\). Holonomy is trivial,
   while \(D_{\mathrm{KL}}(q_1\Vert q_2)=2\lVert a\rVert^2>0\).
2. **Nontrivial holonomy does not always forbid state-specific marginal matching.** Let loop holonomy be a
   nonidentity rotation \(R\in SO(2)\) and take every transported belief to be
   \(Q_*=\mathcal N(0,\sigma^2I)\). Then \(R_\#Q_*=Q_*\), every transported KL is zero, and the laws
   coalesce exactly even though \(R\ne I\). The same rotation has no nonzero fixed mean for a generic
   angle, so this state-specific marginal result does not restore a full two-dimensional structural coarse
   fiber.

For a noncompact expanding holonomy, the fixed nondegenerate Gaussian family can be empty. For
example, \(H=2I\) cannot satisfy \(H\Sigma H^\top=\Sigma\) for any \(\Sigma\succ0\). This is why the
fixed-law set, not merely a formal group average, belongs in the general definition.

## 4. What pairwise belief KL can and cannot do

For a declared edge or path, the undirected gauge-invariant discrepancy is

\[
J_{ij}^b
=\frac12\left[
D_{\mathrm{KL}}(q_i\Vert(\Omega^b_{i\leftarrow j})_\#q_j)
+D_{\mathrm{KL}}(q_j\Vert(\Omega^b_{j\leftarrow i})_\#q_i)
\right].
\]

On a connected cluster, \(J_{ij}^b=0\) on **every actual internal edge**, including the
cycle-closing edges, is equivalent to exact parallel belief agreement and automatically makes the
realized law invariant under every loop. Thus edgewise zero KL is an exact marginal-state test.
Checking only a spanning tree or one arbitrarily selected path per pair can miss the holonomy
constraint.

A positive threshold is not an exact cluster criterion. On a path with identity transport and
\(q_i=\mathcal N(i\delta,1)\), every adjacent KL is \(\delta^2/2\), but the endpoint KL is
\((n-1)^2\delta^2/2\). A connected-component rule can therefore merge a cluster of arbitrarily
large diameter while every accepted edge is locally close.

If the parent variance is held at one, the full-cluster barycenter distortion is

\[
\mathcal K_I=\frac{\delta^2(n^2-1)}{24}.
\]

If the parent ranges instead over all nondegenerate Gaussians, it can absorb the between-agent
spread into its variance and the exact value becomes

\[
\mathcal K_I
=\frac12\log\left(1+\frac{\delta^2(n^2-1)}{12}\right).
\]

Both diverge with cluster length. The parent family must therefore be part of the coalescence
definition.

There is one useful exact flat-holonomy special case. For transported Gaussians with a common covariance
\(\Sigma\), when the parent covariance is constrained to the same value, the forward-KL parent has
mean \(\bar\mu=\sum_iw_i\mu_i\), and

\[
\mathcal K_I
=\frac12\sum_iw_i\lVert\mu_i-\bar\mu\rVert_{\Sigma^{-1}}^2
=\sum_{i<j}w_iw_jJ_{ij}.
\]

For unequal covariances and trivial represented holonomy, the unrestricted Gaussian forward-KL
barycenter is the moment-matching Gaussian

\[
\mu_*=\sum_iw_i\mu_i,
\qquad
\Sigma_*=\sum_iw_i\left[
\Sigma_i+(\mu_i-\mu_*)(\mu_i-\mu_*)^\top
\right],
\]

and its distortion is

\[
\mathcal K_I
=\frac12\left[
\log\det\Sigma_*-\sum_iw_i\log\det\Sigma_i
\right].
\]

The between-mean covariance term is mandatory. Dropping it is an approximation, not the exact
forward-KL barycenter. Outside controlled regular patches, neither KL nor its symmetrization obeys
a triangle inequality, so no global equivalence between local pair thresholds and cluster
distortion should be claimed.

For compact nontrivial linear holonomy, the constrained full-Gaussian solution can still be written
exactly. Let \(dh\) be normalized Haar measure, \(a=\sum_iw_i\mu_i\), and
\(M=\sum_iw_i(\Sigma_i+\mu_i\mu_i^\top)\). Then
\[
a_H=\int h\,a\,dh,\qquad
M_H=\int hMh^\top dh,\qquad
\Sigma_H=M_H-a_Ha_H^\top,
\]
and, when \(\Sigma_H\succ0\),
\[
Q_*=\mathcal N(a_H,\Sigma_H),\qquad
\mathcal K_I=\frac12\left[
\log\det\Sigma_H-\sum_iw_i\log\det\Sigma_i
\right].
\]
This is moment matching after holonomy symmetrization. The flat formula is the special case
\(\operatorname{Hol}=\{I\}\). Noncompact holonomy has no normalized Haar average and can leave the
fixed Gaussian family empty.

Ordinary pairwise KL among one set of root-transported representatives is not a nonflat substitute.
For \(\operatorname{Hol}=\{I,-I\}\subset GL^+(2)\) and representatives all equal to
\(\mathcal N(a,I)\), their ordinary pairwise Jeffreys divergences vanish, but the invariant parent
has mean zero and covariance \(I+aa^\top\), giving
\[
\mathcal K_I=\frac12\log(1+\lVert a\rVert^2)>0.
\]
An orbit-averaged or explicitly holonomy-conditioned statistic is required.

With trivial represented holonomy, if the parent family contains all probability laws, its
forward-KL barycenter is the mixture \(P_*=\sum_iw_iP_i\). In that case

\[
\sum_{i,j}w_iw_jD_{\mathrm{KL}}(P_i\Vert P_j)
=\mathcal K_I+\sum_jw_jD_{\mathrm{KL}}(P_*\Vert P_j)
=\sum_{i<j}w_iw_jJ^{\mathrm{Jeffreys}}_{ij}.
\]

Thus average pairwise Jeffreys divergence contains the barycenter loss plus an additional reverse
term; it is not generally the barycenter loss itself.

Support asymmetry is another obstruction to using symmetric pairwise KL as a necessary condition.
For \(P=\delta_0\) and
\(Q_\epsilon=(1-\epsilon)\delta_0+\epsilon\delta_1\),
\[
D_{\mathrm{KL}}(P\Vert Q_\epsilon)<\infty,\qquad
D_{\mathrm{KL}}(Q_\epsilon\Vert P)=+\infty,
\]
while the forward mixture-barycenter distortion tends to zero with \(\epsilon\). The KL direction
must therefore be part of the definition.

## 5. Belief and model channels must remain separate

Compute independently

\[
(f_I^b,\mathcal K_I^b),
\qquad
(f_I^m,\mathcal K_I^m).
\]

A full same-type joint meta-agent requires, at minimum, \(f_I^b=K_b\), \(f_I^m=K_m\), and zero (or declared
small) distortion in both channels. It is possible for belief holonomy to be invisible while model
holonomy is visible, or vice versa, because the representations and connections can differ.

The cross morphisms add a further closure condition. If \(\Phi:\mathcal E_b\to\mathcal E_m\) is
parallel, then for every loop

\[
H_\ell^m\circ\Phi_r=\Phi_r\circ H_\ell^b.
\]

Consequently \(\Phi_r\) maps belief holonomy-fixed modes into model holonomy-fixed modes; the same
holds in the opposite direction for \(\widetilde\Phi\). If the covariant defects
\(\mathcal D\Phi\) or \(\mathcal D\widetilde\Phi\) do not vanish on the retained modes, a joint
coarse theory must retain those defects as running data or accept a quantified closure error.

## 6. Exact, approximate, and selected meta-agents

| Case | Geometry | Belief state | Result |
|---|---|---|---|
| Full structural and marginal match | \(f_I^x=K_x\) in each required channel | \(\mathcal K_I^x=0\) | Same-type full-dimensional candidate; joint recovery remains separate |
| Partial structural and marginal match | \(0<f_I^x<K_x\) | zero distortion on retained fixed laws/modes | Reduced-rank or sheaf candidate |
| State-specific marginal match | nonidentity holonomy stabilizes \(Q_*\) | \(\mathcal K_I^x=0\) | Zero marginal pooling loss for this state, not a state-uniform or joint theorem |
| Approximate | declared retained space | \(0<\mathcal K_I^x\le\varepsilon_x\) | Lossy parent with explicit information budget |
| Forbidden in chosen family | no retained mode or no fixed parent law | finite condition unavailable | Enlarge the coarse category or reject block |

Even an admissible block need not be selected. A complete formation rule should be staged:

1. **Structural admissibility:** retained holonomy-fixed degrees and cut-link/sheaf closure.
2. **State coherence:** \(\mathcal K_I^b\) and, when a single model law is required,
   \(\mathcal K_I^m\).
3. **Joint-law validity:** a coarse Markov channel and recovery/sufficiency condition when the
   result is claimed to preserve the population experiment rather than only its marginal summary.
4. **License:** a fixed-evidence information-loss budget, free-energy improvement, or explicit
   MDL/Bayesian complexity tradeoff.
5. **Iteration:** prove that the retained channel, connection, cut data, and cross-morphism defects
   remain typed after another blocking step.

Holonomy is therefore an admissibility variable, KL is a state distortion, and free energy/MDL is
a selection rule. Combining them into one weighted scalar before these roles are separated hides
units and inserts arbitrary coefficients.

## 7. Relation to BKS and network/Laplacian RG

- **Bayesian renormalization (Berman-Klinger-Stapleton)** orders model-parameter directions by
  Fisher distinguishability. It can price which statistical directions are sloppy enough to lose,
  but it neither supplies a node partition nor tests bundle holonomy. Its posterior/model-space
  Fisher should not be identified automatically with a recognition Fisher tensor or a graph
  connection Laplacian.
- **Laplacian RG (Villegas et al.)** supplies an intrinsic diffusion scale through
  \(\rho_\tau=e^{-\tau L}/\operatorname{tr}(e^{-\tau L})\) and entropic susceptibility. In this
  theory the natural lift is a connection or sheaf Laplacian. Its exact zero modes already encode
  the holonomy-fixed space, while near-zero modes quantify approximate parallel coherence. A
  gauge-invariant real-space selector still has to be specified.
- **Network RG** emphasizes that one must transform topology, dynamics, and couplings together.
  The rectangular endpoint-map/sheaf closure in 09_coarsegraining.tex is therefore the correct
  target category when one group-valued cut link is not closed.

A practical but still hypothesis-dependent selector can use Laplacian-RG diffusion cells as
candidate blocks, score them with \(\mathcal K_I^b,\mathcal K_I^m\), reject blocks lacking the
required holonomy-fixed dimensions, and finally apply the declared free-energy/MDL license. This
keeps the literature's three roles typed rather than claiming that one paper supplies all three.

## 8. Manuscript diagnosis and lean revision design

What is already present:

- 09_coarsegraining.tex:319-345 states the fixed-section kernel formula but does not attach its
  spanning-tree proof; 09_coarsegraining.tex:347-376 separately proves exact nested composition.
- SPEC.md:365-390 correctly separates full-dimensional holonomy admissibility from belief
  consensus.
- 06_general_coarsegraining.tex:406-416 correctly leaves a gauge- and permutation-natural
  partition selector open.
- 10_renormalization.tex:503-516 correctly treats Laplacian-RG scale diagnosis separately from a
  gauge-invariant blocker.

What is missing:

1. the short proof of the kernel-holonomy formula already marked established;
2. a general marginal-law theorem connecting holonomy to transported KL, with an explicit warning
   that joint recovery remains separate;
3. the exact distinction among structural, state-specific, and dynamical coalescence;
4. the two-channel and parallel-cross-morphism compatibility corollary;
5. the common-covariance Gaussian identity connecting cluster distortion to pairwise
   \(\mathrm{KL}_{ij}\);
6. a statement that strict Regime-I coboundary links make holonomy nondiscriminating.

The chapter introduction at 09_coarsegraining.tex:6 currently says a cluster can be coarsened
"exactly when its internal holonomy is trivial." That is correct only for full fixed-dimensional,
state-independent coarsening with nondegenerate represented weights. It should be narrowed rather
than repeated elsewhere.

There is one scope decision. SPEC.md:17-21 currently excludes the earlier program's meta-agent
barycenter and executable detector. The theorem above is a new derivation and does not rely on
either artifact, but adding it still expands the manuscript from structural coarse-graining to a
state-dependent meta-agent criterion. The source should not be edited until that scope expansion
is accepted explicitly.

Two lean revision options follow.

**Conservative option (preserve current scope):**

1. Turn the bare kernel assertion in 09_coarsegraining.tex into a named proposition with the
   spanning-tree proof.
2. Add only the two counterexamples showing that structural holonomy and transported marginal KL
   imply neither one another.
3. Keep the normalized law lift, marginal barycenter criterion, and partition selection open.

**Expanded option (recommended for the user's stated meta-agent direction):**

1. Put Theorem 2 and the two-channel corollary in **General Coarse-Graining**, immediately after
   gauge/permutation equivariance and before projective systems.
2. In the Gaussian/linear realization, turn Theorem 1 into the missing proved proposition, then add
   the short gradient-flow corollary and common-covariance KL identity immediately after partial
   fixed-section aggregation.
3. Replace, rather than append to, the broad sentence in the Gaussian chapter introduction and
   revise its physicist summary to state "holonomy sets the available consensus modes; KL measures
   occupancy of them."
4. In General Renormalization, add only a short forward reference explaining that BKS prices
   statistical directions and Laplacian RG proposes scales; neither replaces the coalescence
   theorem.

In either option, SPEC.md:392-397 should be narrowed. Exact rectangular/sheaf closure and exact
nested fixed-section composition are now proved; what remains open is canonical compression back
to one invertible group link, normalized probability-law closure, and iteration of the associated
selection rule.

The wiki also needs a later, separately approved reconciliation pass. Holonomy.md and Parallel
transport.md currently move too quickly from flatness to global path independence; zero curvature
gives trivial holonomy on contractible loops, while global path independence additionally needs
trivial monodromy or a suitable simply connected domain. Non-flat connection and the photon
analogy incorrectly suggests that a flat connection forces consensus; it only permits a common
parallel chart. Coarse Graining.md presents an intrinsic scale selector more strongly than the
manuscript, which still treats the gauge-invariant blocker as open.

This arrangement keeps pure theory before the multivariate-Gaussian realization and avoids adding
another parallel discussion of the same criterion.

## Primary sources checked

- D. S. Berman, M. S. Klinger, and A. G. Stapleton, "Bayesian Renormalization,"
  https://arxiv.org/abs/2305.10491.
- P. Villegas, T. Gili, G. Caldarelli, and A. Gabrielli, "Laplacian renormalization group for
  heterogeneous networks," https://doi.org/10.1038/s41567-022-01866-8.
- E. Garuccio, M. Lalli, and D. Garlaschelli, "Multiscale network renormalization:
  Scale-invariance without geometry," https://doi.org/10.1103/PhysRevResearch.5.043101.
- A. Gabrielli, D. Garlaschelli, S. P. Patil, and M. A. Serrano, "Network Renormalization,"
  https://arxiv.org/abs/2412.12988.
