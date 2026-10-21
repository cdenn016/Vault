---
type: concept
title: Lattice gauge theory
aliases:
  - Lattice gauge
  - Wilson lattice gauge theory
  - Link variable
  - Plaquette
  - Wilson loop
tags:
  - cluster/gauge-theory
  - cluster/spd-geometry
  - project/multi-agent
  - project/transformer
status: draft
created: 2026-06-18
updated: 2026-10-20
---

# Lattice gauge theory

## Learned models on lattice gauge fields, October 6, 2026

Two sources in the vault run networks on lattice gauge fields, the opposite direction from the program's use of lattice-gauge language. [[favoni-2022-lattice-gauge-equivariant-cnns]] (L-CNNs) takes $\mathrm{SU}(N_c)$ link variables $U_{x,\mu}$, which transform as $\Omega_xU_{x,\mu}\Omega_{x+\mu}^\dagger$, together with locally transforming matrix channels $W_{x,i}$. Its convolution parallel-transports $W$ from neighboring sites along coordinate axes, $W\to\sum\omega\,UWU^\dagger$, its bilinear layer multiplies locally transforming matrices so that alternating the two grows arbitrary contractible Wilson loops, and a trace layer gives gauge-invariant output; with Polyakov loops for non-contractible topology the authors argue such a network can approximate any gauge-covariant function on the lattice. [[nagai-2025-cask]] builds attention weights from Frobenius inner products of links and staples. In both, the gauge field is the input and gauge equivariance is a real constraint on every layer. In the GL(K) manuscripts the frames are learned parameters, the covariance is artificial in the sense of [[francois-2019-artificial-gauge-symmetries]], and the lattice is the communication graph above one context ([[dennis-2026-glk-attention-v2-rework-2026-10-05]]). The L-Exp layer of [[favoni-2022-lattice-gauge-equivariant-cnns]], which multiplies the exponential of a locally transforming Lie-algebra element onto a given link, is the nearest structural parallel to the exponential link $\Theta_{ij}=U_ie^{L_{ij}}U_j^{-1}$.

> [!note] Editorial: The L-Exp parallel is formal. It acts on a given compact-group gauge field, whereas the GL(K) generator is a learned map into $\mathrm{GL}^+(K)$. [[disipio-2025-curved-spacetime-transformers]] and the sheaf-network sources of [[Gauge equivariance and geometric deep learning]] are the other prior readings of attention as a connection; none states the lattice-gauge reading of a token transformer.

## The lattice above a point, October 5, 2026

[[dennis-2026-glk-attention-v2-rework-2026-10-05]] states in what sense attention carries a lattice gauge structure. The lattice is the communication graph above a single base point $c_*$, with agents as vertices and allowed source relations as edges; it discretizes no base manifold and is not the single-site reduction of large-$N$ gauge theory in the Eguchi–Kawai sense, whose links are labeled by collapsed lattice directions. Invertible links obeying the endpoint law $\Theta_{ij}\mapsto g_i\Theta_{ij}g_j^{-1}$ are lattice gauge data and, as edge variables under independent vertex groups, bifundamental fields of a quiver gauge theory; singular head maps and comparison maps are quiver-representation and cellular-sheaf data ([[hansen-2018-toward-a-spectral-theory-of-cellular-sheaves]]), of which group links are the invertible restriction. When all heads share one routing pattern, the exponential chart turns the routed message into the hopping term $\sum_j\beta_{ij}\Theta_{ij}\mu_j$. In the trained $K=128$ model the group links are numerically low rank, so inverse-edge holonomies must be computed in log space from the generator spectrum ([[vfe3-2026-10-05-k128-exponential-and-parameter-accounting]]).

## Latent link generators and the induced Wilson action, October 3, 2026

[[dennis-2026-dynamic-links]] gives the attention links a lattice-gauge dynamics by making their generators latent variables with a prior inside the variational free energy, following the Euclidean reading of the Wilson weight $e^{-S}$ as a probability measure ([[wilson-1974-confinement-quarks]]). The lattice is depth by token: an edge from $(j,\ell)$ to $(i,\ell+1)$ for each causal source, self edges time-like, and elementary loops that compare two-step routes from $(k,\ell)$ to $(i,\ell+2)$. The curvature energy on each loop is the Frobenius defect $\tfrac12\|W-I\|_F^2$ of the reference-coordinate holonomy, which is $K-\operatorname{tr}W$, Wilson's plaquette density, on $O(K)$ and remains separating on $\mathrm{GL}(K)$. The time-like loops contribute the square of a discrete electric field, so the kinetic term comes from the same action as in the Hamiltonian formulation ([[kogut-susskind-1975-hamiltonian-lattice-gauge]]); linearized, the link field equation is a screened, massive Euclidean Maxwell equation. For undirected Gaussian matter, integrating out the states induces $S_{\rm ind}=\tfrac12\log\det J(X)$, bounded below, whose hopping-parameter expansion is a sum of Wilson loops with the triangle term $\frac{\lambda_E^3}{d_id_jd_k}(K-\operatorname{tr}F)$ at leading order (ratio of exact to leading term $1.15\to1.0003$ as the matter gets heavier); in that model the non-compact generator directions acquire edge-local mass terms even on a tree. Directed (causal) matter induces nothing, so in the transformer's causal model the curvature energy is a declared prior.

## Matrix communication links, September 20, 2026

The group-valued connection formulation below is one case. General matrix links are also legitimate gauge-covariant fields; [[wetterich-2014-linear-lattice-gauge-theory]] supplies a compact-group precedent. The current manuscript construction is

$$\mathsf S_{j,h}=T_hU_j^{-1},\qquad
\mathsf R_{i,h}=U_iO_h,\qquad
L_{ij}^{(h)}=\mathsf R_{i,h}\mathsf S_{j,h},\qquad
L_{ij}^{(h)\prime}=g_iL_{ij}^{(h)}g_j^{-1}.$$

These links can be singular. At fixed routing, $\mathcal C_{ij}=U_i(\sum_h\beta_{ij}^{(h)}O_hT_h)U_j^{-1}$ is a covariant multi-head edge operator and can be full rank. Shared reference matrices constrain its edge dependence. This construction concerns full multivariate Gaussian site states; diagonal storage is an implementation approximation. [[dennis-2026-glk-matrix-links-2026-09-20]]

For one head, $L_{ij}L_{jk}-L_{ik}=U_iO(TO-I_s)TU_k^{-1}$. The condition $TO=I_s$ gives flat identifications on $U_i\operatorname{im}O$. For shared unweighted maps, an $r$-edge path is $U_{i_0}(OT)^rU_{i_r}^{-1}$, so equal-length paths with equal endpoints agree. Its failure to identify one-edge and two-edge processing alone is not arbitrary edge curvature.

Ordered loop products transform by conjugation, making their traces invariant even for singular links. Invertible connection holonomy is a more specific object. Causal attention supplies no directed cycles through distinct token positions, so additional loop edges must be declared. The underlying $\Omega_{ij}=U_iU_j^{-1}$ remains flat. An independent connection extension can instead use $F_{i,h}\Theta_{ij}$ with $F_{i,h}=U_iO_hT_hU_i^{-1}$; it is not part of the reported parameterization. [[dennis-2026-glk-matrix-links-2026-09-20]]

Group-valued origin of the matrix links (October 2, 2026). A singular link cannot be a factor of a group element, so the relation between $L_{ij}$ and a $\mathrm{GL}(K)$ link $\Theta_{ij}\mapsto g_i\Theta_{ij}g_j^{-1}$ must be additive or infinitesimal. [[dennis-2026-link-origin]] gives three exact constructions. In the exponential picture $\Theta_{ij}=U_i\exp(X_{ij})U_j^{-1}$ with the lemma $\exp(PQ)=I+P\varphi(QP)Q$, $\varphi(z)=(e^z-1)/z$, so for $X=O_hT_h$ one has $\Theta=\Omega_{ij}+U_iO_h\varphi(T_hO_h)T_hU_j^{-1}$: the non-communicating part is the identity on $\ker T_h$ and the matrix link is the first-order term, which places the earlier transported message (zeroth order) and the projected message (first order) in one link. In the compression picture a primitive link is cut by covariant projectors and factored as unipotent, block-diagonal, unipotent factors, with the middle factor in the Levi factor $\mathrm{GL}(d)\times\mathrm{GL}(K-d)$ of the parabolic stabilizing $\operatorname{im}O_h$ and a hidden Schur complement $S=D-CA^{-1}B$; choosing the subspace at every site is a reduction of structure group to the parabolic, and the resemblance to Higgs symmetry breaking is formal only. In the head-sum picture the operator $U_iOB_{ij}TU_j^{-1}$ applied by the code is generically in $\mathrm{GL}(K)$ and equals the standard multi-head value path when frames are trivial; its triangle loop is a ratio of routing weights, with log-holonomy $-(D_{ij}+D_{jk}-D_{ik})/\kappa+\log(\pi_{ij}\pi_{jk}/\pi_{ik})-\log Z_j$, which has no definite sign because the KL has no triangle inequality ([[Holonomy]]). Invertible links are also what give the field loop observables with reversed edges on causal support. Status: agent-drafted, identities checked in float64 at $K=6$ or $7$, no training, nothing proved beyond the note's short proofs. Whether the exponential link is the right gauge field remains a choice; the routing-independent generator is edge independent, so in the tiled case it adds loop observables and interpretation but no expressive power. The matrix link is also not a truncation of the group link: for a channel of this form, flat transport plus a linear channel term $I+O'T$ is exactly an exponential link $\exp(OT)$ whenever $I+TO'$ has a principal logarithm ($O=O'\varphi(\log(I+TO'))^{-1}$), because both are charts, affine and logarithmic, of the same embedded $\mathrm{GL}(d)$ acting on $\operatorname{im}O$ and fixing $\ker T$. "First order" then compares the two coordinates near the identity. In the tiled case the operator the projected predictive route applies is itself the group element, and the identity initialization is the origin $X=0$ of the logarithmic chart. The charts differ at the singular boundary $\det=0$, in components, in optimization geometry (the code's M-step acts in the affine chart), and at order one for finite generators; on one trained run (K=64, 2 heads) the bare message operator sits at that boundary from early in training, with stable rank 11 to 17 of 64 at the end and an unstable sign of the determinant, while the flat-plus-channel link $I+M$ keeps every eigenvalue in the right half plane at all twelve snapshots, so the exponential chart exists for the link the model applies; this is one seed and one scale ([[dennis-2026-link-origin]], [[wetterich-2014-linear-lattice-gauge-theory|Wetterich 2014]] for links that are unrestricted matrices).

An endpoint law alone is not a complete lattice gauge theory. A GL(K)-invariant action, normalized measure or dynamics, and graph structure remain to be supplied. Euclidean link norms are not generally invariant under GL(K). Neither the MLP interpretation nor a continuum limit follows from this construction.

The v2 revision (September 23, 2026) names a closer counterpart. The comparison cospan $E_i\to H^{\mathrm{cmp}}\leftarrow E_j$ is a pair of restriction maps into an edge stalk, which is the structure of a cellular sheaf rather than of a group-valued link field ([[hansen-2018-toward-a-spectral-theory-of-cellular-sheaves]], [[bodnar-2022-neural-sheaf-diffusion]]). Sheaf restriction maps need not be invertible, and sheaves with orthogonal restriction maps are discrete $O(d)$ bundles with the connection Laplacian ([[Graph synchronization and connection Laplacians]]).

## Definition

**Lattice gauge theory** is the discretization of a gauge field theory onto a
spacetime (or space) lattice, introduced by [[wilson-1974-confinement-quarks]] to
make gauge theory *non-perturbatively* well defined. The continuum connection
$A_\mu(x)$ is replaced by **link variables**: to each oriented edge from site $x$
to its neighbor in direction $\mu$ one assigns a group element
$$
U_{x,\mu}=\exp\!\big(i\,a\,g\,A_\mu(x)\big)\in G,
$$
where $a$ is the lattice spacing and $G$ the structure group. A link variable is
exactly the **discrete parallel-transport operator** along that edge: the
parallel transport along any path is the *ordered product* of the link variables
crossed, and gauge transformations act site-wise,
$U_{x,\mu}\mapsto g_x\,U_{x,\mu}\,g_{x+\hat\mu}^{-1}$, so gauge invariance is
**exact** on the lattice (no gauge fixing needed). The smallest closed loop is a
**plaquette** — the product of the four link variables around an elementary
square,
$$
U_{\mathrm{plaq}}=U_{x,\mu}\,U_{x+\hat\mu,\nu}\,U_{x+\hat\nu,\mu}^{-1}\,U_{x,\nu}^{-1},
$$
whose deviation from the identity measures the **lattice curvature** (the
discrete field strength). Wilson's action sums a curvature term over all
plaquettes,
$$
S=\beta\sum_{\mathrm{plaq}}\Big(1-\tfrac1N\,\mathrm{Re}\,\operatorname{tr}\,U_{\mathrm{plaq}}\Big),
$$
and the **Wilson loop** $\langle W(C)\rangle=\langle\operatorname{tr}\prod_{\ell\in C}U_\ell\rangle$
is the canonical gauge-invariant observable. In the strong-coupling limit the
Wilson loop obeys an **area law** $\langle W(C)\rangle\sim e^{-\sigma A(C)}$,
whose string tension $\sigma$ encodes a linearly rising (confining) potential —
Wilson's non-perturbative demonstration of quark confinement.

[[kogut-susskind-1975-hamiltonian-lattice-gauge]] recast this Euclidean
formulation as a **Hamiltonian** with continuous time and a spatial lattice: the
dynamical variables are the spatial links $U_{x,\mu}$ and their conjugate
electric-field operators $E$, evolving under
$$
H=\tfrac{g^2}{2}\sum E^2-\tfrac{1}{g^2}\sum_{\mathrm{plaq}}\big(\operatorname{tr}U_{\mathrm{plaq}}+\text{h.c.}\big),
$$
subject to a Gauss-law constraint that enforces gauge invariance on physical
states. The electric term is the kinetic energy; the magnetic (plaquette) term is
the curvature energy. [[creutz-1983-quarks-gluons-lattices]] turned all of this
into a computational discipline — the first textbook on lattice gauge theory —
laying out strong-coupling expansions, the continuum limit (tuning the bare
coupling), and Monte-Carlo (heat-bath / Metropolis) sampling of link
configurations, with the plaquette and Wilson loop as the practical diagnostics
of curvature and confinement.

## Why it matters

Lattice gauge theory supplies three things this program needs. It gives a
**concrete, finite carrier of a connection** — the link variable — that is a
genuine group element implementing parallel transport on a graph, with gauge
invariance exact and no continuum limit required to be well defined
([[wilson-1974-confinement-quarks]]). It gives a **dynamical (time-stepped)**
formulation in which the connection is evolved by an equation of motion rather
than only sampled from a static action ([[kogut-susskind-1975-hamiltonian-lattice-gauge]]).
And it gives **gauge-invariant observables** — the plaquette holonomy and the
Wilson loop — that quantify curvature and detect when a connection is genuinely
non-flat ([[creutz-1983-quarks-gluons-lattices]]). Together these make "a gauge
field on a network of nodes and edges" a fully operational object.

## Relation to this research

The participatory / multi-agent program ([[participatory-it-from-bit]]) promotes
the *flat* belief transport $\Omega_{ij}=\exp(\phi_i)\exp(-\phi_j)$ to a genuinely
**non-flat connection** in "Regime II," where edge twists relax and transport
around a loop no longer returns to the identity. The object carrying that
holonomy is precisely Wilson's lattice link variable: the program's
edge-relaxed transport is a link variable $U_{x,\mu}\in GL^+(K)$ living on the
edges of the agent network, and the plaquette holonomy is the lattice curvature
signaling a [[Non-flat connection and the photon analogy|non-flat connection]].
[[wilson-1974-confinement-quarks]] is therefore the origin reference for the
gauge object the model's M-step connection update evolves, while
[[kogut-susskind-1975-hamiltonian-lattice-gauge]] is the template for *how* it is
evolved — a continuous-time Hamiltonian on link group elements rather than a
static sampler, mirroring the model's bounded gauge-invariant lattice action and
its time-stepping of twists. [[creutz-1983-quarks-gluons-lattices]] supplies the
measurement side: the plaquette / Wilson-loop construction is the natural
gauge-invariant probe for emergent curvature in the agent network, the discrete
counterpart of [[Holonomy]] and [[Parallel transport]] on the wiki.

Three threads connect this lattice picture to the rest of the program's geometry.
The link group is $GL^+(K)$, which is **noncompact and non-abelian**, so by
[[milnor-1976-left-invariant-metrics]] it carries no bi-invariant metric — the
same structural fact that makes the choice of metric on the frame fiber a genuine
modeling decision (`omega_metric`) and that bounds the error of the BCH frame
barycenter; the Hamiltonian's "electric energy" $\propto E^2$ implicitly selects
an inner product on the algebra, which is exactly such a left-invariant-metric
choice. The Hamiltonian formulation itself sits inside the geometric-mechanics
framework of [[arnold-1989-classical-mechanics]]: Hamilton's equations as a flow
on a symplectic manifold, with Noether's symmetry–conservation correspondence as
the classical analog of the Gauss-law gauge constraint, and motion on a Lie group
as geodesic flow of an invariant metric (the Euler–Arnold picture) — the same
lens the program uses for momentum-augmented [[Hamiltonian belief dynamics]].
Finally, the whole construction lives on the smooth-manifold and fiber-bundle
scaffolding of [[lee-2012-smooth-manifolds]]: a lattice gauge field is a discrete
connection on a principal bundle over the graph, with link variables as the
discretized transport and plaquettes as the discretized curvature 2-form.

Modern machine-learning work on the lattice supplies the bridge from these
classical objects to the program's neural architecture. [[nagai-2025-cask]]
builds a **gauge-covariant Transformer** (CASK) whose attention weights are
Frobenius inner products of smeared link variables and Wilson-loop staples — the
lattice-QCD analog of the program's [[GL(K) gauge-equivariant attention]], where a
parallel-transport inner product forms the attention coefficient $\beta_{ij}$ and
an exponential-map update transports the value. [[kanwar-2020-equivariant-flow]]
and [[boyda-2021-su-n-flows]] construct **gauge-equivariant normalizing flows** on
link variables — first $U(1)$, then non-abelian $SU(N)$ — that sample the
gauge-invariant lattice measure exactly; they are direct evidence that learnable
maps over $G$-valued links can respect local gauge symmetry by construction, the
same demand the model places on its $GL^+(K)$ frame transport.

> [!note] Editorial: The identification "edge-relaxed belief transport = Wilson
> link variable, plaquette holonomy = curvature diagnostic" is the program's own
> reading; the lattice-gauge sources establish the objects (links, plaquettes,
> Wilson loops, the Hamiltonian), and the program maps its agent-network
> connection onto them.

## Curvature of causal link fields, October 2, 2026

[[dennis-2026-link-curvature]] (agent-drafted companion to [[dennis-2026-link-origin]]; float64 checks at $K=4$, nothing trained) measures the content of a causal link field by the triangle holonomy $F_{ijk}=\Theta_{ik}^{-1}\Theta_{ij}\Theta_{jk}=U_k\,G_{ik}^{-1}G_{ij}G_{jk}\,U_k^{-1}$, whose conjugacy class is gauge invariant and independent of the frames, so curvature is a property of the reference-coordinate field $G$. A field of arbitrary matrices is flat exactly when it is recurrent (each link is the ordered product of the adjacent links), and for invertible links flat is exactly pure gauge, $\Theta_{ij}=g_ig_j^{-1}$; the singular shared projector is flat and not pure gauge. Positional and rotary links are therefore flat, while the constant exponential link is maximally curved ($F=U_ke^{X}U_k^{-1}$). Holonomies of the candidate edge-dependent generators: a routed exponent $X_{ij}=OB_{ij}T$ has the additive defect $B_{ij}+B_{jk}-B_{ik}$ of the routing weights in the exponent; the head sum has their multiplicative defect $B_{ij}B_{jk}/B_{ik}$ (the KL triangle defect of the earlier note); normalized head-sum routing is flat on strict triangles only for $\beta_{ij}=c_i/c_j$, a thin subset that uniform causal attention violates. The first-order part of the exponential-link holonomy is the discrete exterior derivative of the generator cochain, with commutator corrections at second order ([[Baker-Campbell-Hausdorff formula]]). The note notes that linear state-space recurrences have flat transition products ([[State space models]]), a structural observation only.

For an inference-derived edge-dependent link, the regression link $W_{ab}=\Sigma_{ab}\Sigma_{bb}^{-1}$ of a joint Gaussian has curvature equal to the partial cross-covariance $\Sigma_{ik|j}$ and is flat exactly when $\xi_i\perp\xi_k\mid\xi_j$ (an AR(1) chain gives $W_{ij}=A^{\,i-j}$; the converse for the full Markov property is not claimed). Its rank-$d$ truncation is reduced-rank regression, and the correlated variational family needed to supply cross-covariances is absent in the mean-field family. None of this is tested in training.

> [!note] Editorial: Flatness equals recurrence and invertible flatness equals pure gauge are short exact propositions. Whether the trained routing is nearer the flat pattern than uniform attention is unmeasured, and the loop observables remain conventions on causal support, as above.

## Sources

- [[favoni-2022-lattice-gauge-equivariant-cnns]] — lattice gauge equivariant CNNs: gauge-covariant convolution and bilinear layers on $\mathrm{SU}(N_c)$ links that generate Wilson loops.
- [[dennis-2026-glk-attention-v2-rework-2026-10-05]] — the lattice as the communication graph above one context; invertible links as lattice-gauge and quiver data, singular head maps as sheaf data; routed hopping term.
- [[dennis-2026-link-origin]] — group-valued origin of the singular matrix links (exponential link, parabolic compression with Schur complement, head-sum link); agent-drafted, small-dimension numerical checks only.
- [[dennis-2026-link-curvature]] — triangle holonomy of causal link fields; flat = recurrent, invertible flat = pure gauge; holonomy table of candidate generators; regression links; agent-drafted, float64 checks at K=4.
- [[wilson-1974-confinement-quarks]] — origin of the lattice formulation: link variables, plaquette action, Wilson loop, area-law confinement (central).
- [[kogut-susskind-1975-hamiltonian-lattice-gauge]] — the continuous-time Hamiltonian formulation (links + conjugate electric fields, Gauss law) the M-step dynamics mirror (central).
- [[creutz-1983-quarks-gluons-lattices]] — the methodology textbook: plaquette/Wilson-loop observables and Monte-Carlo sampling for measuring curvature (central).
- [[milnor-1976-left-invariant-metrics]] — $GL^+(K)$ admits no bi-invariant metric, so the electric-term inner product / link metric is a choice.
- [[arnold-1989-classical-mechanics]] — symplectic/Hamiltonian geometric-mechanics framework behind the Hamiltonian lattice formulation and belief dynamics.
- [[lee-2012-smooth-manifolds]] — smooth-manifold and fiber-bundle foundations: a lattice gauge field as a discrete principal-bundle connection.
- [[dennis-2026-dynamic-links]] — latent link generators on a depth-by-token lattice, Frobenius-defect curvature prior with Wilson limit on $O(K)$, kinetic term from time-like loops, induced action and hopping expansion of undirected Gaussian matter.

## See also

- [[Holonomy]]
- [[arkani-hamed-2001-deconstructing-dimensions]] — four-dimensional quiver gauge theory whose bifundamental condensates are lattice links of a deconstructed fifth dimension; template for links $\Theta_{ij}(c)$ varying over a base with kinetic term $\lVert\nabla\Theta\rVert^2$.
- [[Cellular sheaves and sheaf Laplacians]] — sheaf coboundary as lattice covariant difference; flatness as $\delta^2=0$; Hodge decomposition of link fluctuations about a flat background.
- [[Parallel transport]]
- [[Non-flat connection and the photon analogy]]
- [[Gauge transformation]]
- [[Killing form]]
- [[participatory-it-from-bit]]
- [[GL(K) gauge-equivariant attention]] — the program's neural instantiation of gauge-invariant link inner products
- [[nagai-2025-cask]] — gauge-covariant Transformer (CASK) on lattice links
- [[kanwar-2020-equivariant-flow]] · [[boyda-2021-su-n-flows]] — gauge-equivariant flows on $U(1)$ / $SU(N)$ links
