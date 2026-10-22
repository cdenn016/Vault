<!-- rigorous-theory-search-metadata {"schema_version":"rigorous-theory-search/v1","contract_id":"contract-sha256-b542fc3173c340f7c3430dc4795f9964d742d9047e059add3a8949d73f3bbcbe","target_digest":"b542fc3173c340f7c3430dc4795f9964d742d9047e059add3a8949d73f3bbcbe"} -->
# Unprepared formation: the common construction and its limits

There is an existential construction of two-stage native routing formation with exact physical-symmetry retention under the frozen contract. Its initial laws range over a full open neighborhood of positive densities, including independently variable bit-circle correlations. The statistical channels are selective from the outset. The result concerns endogenous selection of a compressible block; it does not claim that the flow first creates an exact equivalence between previously distinguishable states.

The routing proof is in `routes/staged-cliques.md`; the full density derivative, retention, responses, and simultaneous bridge are in `routes/parent-closure.md`; contextual geometry and its event-time qualification are in `routes/geometry-symmetry-interface.md`. The arguments below specify their common interface. No separate route alone establishes this interface.

## One fixed original architecture

Use six homogeneous agents. Both sectors have sample space \(\{-1,1\}\times S^1\), with the uniform product probability measure as dominating measure. Each \(q_i\) and \(s_i\) is an independently variable strictly positive normalized density. Take the proper uniform local reference and evaluator, \(r=G=1\), equal unit Fisher mobilities, fixed positive temperature \(T\), all-source rows including self, and fixed uniform priors \(\pi_{ij}=1/6\). The common normalized channel keeps the source bit and emits an independent uniform angle:

\[
K((z,\theta),d(z',\theta'))=\delta_z(dz')\frac{d\theta'}{2\pi}.
\]

There is no membership label in these data. The channel has no switch, threshold, or state-dependent activation. Its fixed lack of angular transmission is a material assumption. It is not the identity channel on the entire sample space.

Let \(\mu_i\) be the binary marginal density of \(q_i\). Exactly,

\[
D(q_i\Vert\mu_j\otimes\mathrm{Haar})
=D(q_i\Vert\mu_i\otimes\mathrm{Haar})+D(\mu_i\Vert\mu_j).
\]

The first term cancels from the Gibbs row but remains in the energy derivative. The complete belief force, modulo a sample-independent scalar, is

\[
h_i^q=2\log q_i-\sum_j\beta_{ij}\log\mu_j
-\sum_k\beta_{ki}\frac{\mu_k}{\mu_i},
\qquad
\dot q_i=-q_i(h_i^q-\mathbb E_{q_i}h_i^q).
\tag{S1}
\]

All sums include self. The self sender ratio is one, but the self comparison cost is the receiver's conditional angular entropy and is generally nonzero. The model equation is the same in \(s,\eta,\gamma\). Dropping this entropy or the incoming ratios changes the model.

On a positive bounded neighborhood in normalized \(C^k\) density charts, the right side is locally Lipschitz. Every operation is a logarithm on a positive range, a bounded integral, a positive marginal ratio, a product, or a finite Gibbs normalizer. This supplies local unique interior solutions and continuous dependence without a finite-dimensional closure assumption. The theorem uses a compact finite time interval; it does not assert global regularity for every positive density.

## Routing without initial equality constraints

Use the product reference trajectory

\[
q_i(z,\theta)=\mu_i(z)p_{k_i}(\theta-\chi_i),\quad
s_i(m,\varphi)=\eta_i(m)p_{l_i}(\varphi-\zeta_i),\quad
p_k(\theta)=e^{k\cos\theta}/I_0(k).
\tag{S2}
\]

Substitution into (S1), including its centering term, proves exact separation. The binary marginals follow the original binary identity-channel, all-source, \(J=0\) Fisher system, and

\[
k_i(t)=k_i(0)e^{-2t},\quad l_i(t)=l_i(0)e^{-2t},
\qquad \dot\chi_i=\dot\zeta_i=0.
\tag{S3}
\]

These identities locate a reference trajectory; they are not imposed on the admitted open class.

The routing proof chooses finite separated binary coordinates, then sufficiently small fixed \(T=h^2>0\). The rescaling \(x_i=h u_i\) changes amplitude only. Its limiting field is

\[
\dot u_i=-u_i+\sum_j(w_{ij}+w_{ji})(u_j-u_i),
\qquad
w_{ij}=\frac{e^{-(u_i-u_j)^2/2}}{\sum_k e^{-(u_i-u_k)^2/2}}.
\tag{S4}
\]

No time rescaling or slow mobility is inserted. Two nearby pairs activate internally before their centers approach. Their inherited parent rows subsequently activate mutually. A third, more distant pair provides a nonempty complement at the second event. The finite-time decoupling and crossing arguments are in `routes/staged-cliques.md`.

At every level the same fixed threshold is applied to both sectors and directions of the inherited rows

\[
B_{IJ}^q=\frac1{|I|}\sum_{i\in I}\sum_{j\in J}\beta_{ij},
\qquad
B_{IJ}^s=\frac1{|I|}\sum_{i\in I}\sum_{j\in J}\gamma_{ij}.
\tag{S5}
\]

Self masses and primitive counts remain present. These are aggregations of the original rows, not newly fitted Gibbs rows. In each sector and direction a pair qualifies when \(B_{IJ}>1/10\) and \(B_{IJ}-\sum_{K\notin\{I,J\}}B_{IK}>1/20\). A block cannot have two qualifying partners, since each would have to exceed the other by more than \(1/20\). Merge disjoint qualifying pairs at their first closed-threshold contact; the proved crossings are transverse with strict contrast and immediate strict membership. All comparisons use this same rule. The labels of the three reference pairs specify an initial neighborhood, not constitutive membership data.

Choose a compact horizon extending beyond the second join. The reference density trajectory stays positive, with nonzero angular first moments. Its strict initial and inter-event inequalities, transverse crossings, positive persistence windows, and nonzero geometric quantities survive in an open neighborhood of the full density domain. This includes arbitrary small bit-circle correlations, different conditional profiles, and independent changes of all belief and model laws. The initial laws can be chosen pairwise distinct. Their equality diagonals are invariant under the smooth permutation-equivariant field, so uniqueness prevents a first exact collision at finite regular time. Taking all label permutations makes the admitted open class permutation invariant. It is not claimed dense or universal.

## Lossy parents and original-time closure

Independently rotate each primitive agent's belief and model by the same physical angle. Equation (S1), the rows, and Fisher metric are equivariant under \((S^1)^6\). For a block \(I\), discard

\[
H_I=\{(a_i)_{i\in I}:\sum_{i\in I}a_i=0\pmod{2\pi}\}.
\tag{S6}
\]

This changes actual constituent angular laws in fixed physical coordinates. Its continuous directions differ from the one common collective rotation used for geometry. A two-child join loses one relative orientation; joining two parents loses another because \(H_I\times H_J\subsetneq H_{I\cup J}\).

The exact parent state is section valued. Fix a reference context \(c_*\), and work on a lifted-angle chart with nonzero first moments. Set

\[
\vartheta_i=\arg\mathbb E_{q_i(c_*)}e^{i\theta},\quad
\phi_I=|I|^{-1}\sum_{i\in I}\vartheta_i,\quad
\alpha_i=\phi_I-\vartheta_i.
\]

Rotate the entire child section by \(\alpha_i\), constant over evaluation context, and take products as the actual normalized parent laws \(q_I,s_I\). Marginalization recovers their factors. The parent retains all relative orientation profiles away from the anchor but cannot recover the discarded constant offsets. Its size grows with the block.

At the next join use primitive-count-weighted phase averages. Sequential and direct retention agree on the common chart. Native event times are invariant under (S6), so retaining them does not recover the lost offsets. Finite sampled histories do not deterministically identify the offsets either, since all admitted response densities are positive. Storing exact constituent laws would invalidate this loss claim and is not part of the protocol.

Let \(\omega_i\) be the instantaneous first-moment angular velocity at the anchor, computed from the retained representative, and \(\bar\omega_I\) its arithmetic mean. The exact retained factor equation is

\[
\partial_t\widetilde q_i
=V_i^q(\widetilde x)
-(\bar\omega_I-\omega_i)\partial_\theta\widetilde q_i,
\tag{S7}
\]

with the same correction for \(\widetilde s_i\). It is autonomous on the retained network of sections and uses the original time. It includes the derivative of the moving representative. In \(C^k\) charts this identity is asserted in \(C^{k-1}\); differentiability of rotations as maps \(C^k\to C^k\) is not assumed.

Equation (S7) is not generally the ordinary unit-Fisher gradient of a new single parent KL. The kinetic quotient metric and the Fisher metric of a canonical product representative can differ. The exact result is inherited dynamics with the displayed compensator, while the geometric result below uses actual product-law Fisher information.

## One recursive response protocol

Before formation, declare that a query to a current block returns its constituent bit vector and the sum modulo \(2\pi\) of independent angular samples from its constituents. The model sector has the corresponding joint response. Native source choices and transmitted bit samples are also allowed. Policies may use the recorded history and query current whole blocks, but may not split a compressed block to expose an individual absolute angle. This rule applies at every block size.

These are normalized pushforward kernels of actual product laws. Equation (S6) leaves their joint distributions invariant. The aggregate angular response is nonconstant: its first moment is \(\prod_{i\in I}\mathbb E_{q_i}e^{i\theta}\), nonzero on the regular neighborhood. Equality of the closed waiting-time flow and each next-record joint kernel proves equality of every finite adaptive joint history by chronological conditioning. Earlier records are carried forward. Queries do not reset the law state or perform an undeclared Bayesian update.

An individual constituent absolute-angle query fails descent. Its exclusion is a stated limit of the interface, not an approximation. The theorem preserves the declared recursive experiments, not every microscopic observable.

## Collective geometry through the same events

Use the common simultaneous \(S^1\) action on all belief and model angles and the original sum Fisher normalization. The constant-over-context rotations commute with this action. Their contextual derivatives are rotated original derivatives. Zero means of independent factor scores eliminate cross terms. Thus the actual parent Fisher cost equals the original cost for every \(\xi\):

\[
\bar g(dRp+\bar J\xi,dRp+\bar J\xi)
=g(dp+J\xi,dp+J\xi).
\]

The minimizing connection classes, Lie-algebra stabilizer kernels, and minimized contextual tensors agree. On the regular local chart the curvature agrees as well.

An explicit section uses contexts \((k,\chi)\), all belief factors \(p_{k e^{-2t}}(\theta-\chi)\), all model factors \(p_{l e^{-2t}}(\varphi)\), \(l>0\), and context-independent binary coordinates. Put \(a_t=A(k e^{-2t})\), \(b_t=A(l e^{-2t})\), where \(A(v)=vI_1(v)/I_0(v)\). For a block of primitive count \(n\),

\[
\mathcal A_t=-\frac{a_t}{a_t+b_t}d\chi,
\qquad
\mathcal F_t=-\frac{b_t e^{-2t}A'(k e^{-2t})}{(a_t+b_t)^2}dk\wedge d\chi,
\]

\[
h_{\chi\chi}=n\frac{a_tb_t}{a_t+b_t}>0,\qquad
h_{kk}=n e^{-4t}\operatorname{Var}_{p_{k e^{-2t}}}(\cos\theta)>0.
\tag{S8}
\]

For \(v>0\), \(A'(v)>0\) because \(I_1/I_0=\mathbb E\cos\theta>0\) and its derivative is the positive variance of \(\cos\theta\). Curvature and rank two persist at every finite time on the reference section, and by a positive compact margin on sufficiently small smooth section neighborhoods. No Gaussian closure or common covariance is used.

To obtain such a section through every arbitrary nearby initial law configuration \(x\), choose \(c_*=(k_*,0)\), let \(\vartheta_i(x)\) be its belief first-moment phase, and set

\[
q_{i,x}(k,\chi)=\tau_\chi
\left[\frac{e^{(k-k_*)\cos(\theta-\vartheta_i(x))}q_i(z,\theta)}
{\int e^{(k-k_*)\cos(\theta-\vartheta_i(x))}q_i(z,\theta)d\nu}\right],
\qquad s_{i,x}(k,\chi)=s_i.
\tag{S9}
\]

This is a smooth normalized extension through \(x\) and reproduces the displayed geometric witness at the reference configuration. It is equivariant under each simultaneous physical rotation of \(q_i,s_i\): the phase in its tilt shifts by the same angle as the density. Therefore the assigned contextual profile cannot encode the discarded orientation through a fixed external template. Evolving (S9) gives geometric persistence on a full open set of independent anchor law values, while preserving the exact positive-dimensional retention fibers. An arbitrary non-equivariant extension would not establish that last assertion.

Membership for the section-valued parent is selected at the fixed anchor. The same block is represented across the contextual patch, and geometry is compared at a common physical time. If each evaluation context instead chooses its own birth time \(\tau(c)\), its derivative gains \(Vd\tau\). That distinct comparison requires the event-pullback calculation in `routes/geometry.md` and is not asserted automatically.

## Scope

The affirmative construction is existential and finite-horizon: fixed homogeneous selective channels, fixed positive temperature, an open set of full regular laws, two finite native-routing handoffs with a genuine exterior at the second, original-time inherited dynamics, the stated joint histories, and nonzero collective geometry on the stated sections. All parameter choices are existence bounds; no numerical calibration or experimental result is claimed.

The symmetry is available before formation. Routing selects its blocks and handoff times. The result does not establish generic formation for arbitrary channels, newly created exact redundancy, unrestricted microscopic sufficiency, bounded parent dimension, an ordinary single-KL parent model, global phase-root charts, or infinite-depth recursion. Strict clique contrasts hold for the proved finite windows.

Exact projectability is the relevant closure criterion; see [Horstmeyer and Atay, Characterization of Exact Lumpability for Vector Fields on Smooth Manifolds](https://arxiv.org/abs/1607.01237). Fixed-channel Fisher sufficiency and monotonicity are treated by [Ay, Jost, Le, and Schwachhofer, Information geometry and sufficient statistics](https://arxiv.org/abs/1207.6736), with conditional-density characterizations also in [Yamaguchi and Nozawa, On statistics which are almost sufficient from the viewpoint of the Fisher metrics](https://arxiv.org/abs/2305.04199). These sources supply criteria, not this formation construction. Its derivatives and normalizations are calculated in the local proofs. No worldwide novelty claim is made.
