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
updated: 2026-06-19
---

# Lattice gauge theory

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

> [!note] Editorial: The identification "edge-relaxed belief transport = Wilson
> link variable, plaquette holonomy = curvature diagnostic" is the program's own
> reading; the lattice-gauge sources establish the objects (links, plaquettes,
> Wilson loops, the Hamiltonian), and the program maps its agent-network
> connection onto them.

## Sources

- [[wilson-1974-confinement-quarks]] — origin of the lattice formulation: link variables, plaquette action, Wilson loop, area-law confinement (central).
- [[kogut-susskind-1975-hamiltonian-lattice-gauge]] — the continuous-time Hamiltonian formulation (links + conjugate electric fields, Gauss law) the M-step dynamics mirror (central).
- [[creutz-1983-quarks-gluons-lattices]] — the methodology textbook: plaquette/Wilson-loop observables and Monte-Carlo sampling for measuring curvature (central).
- [[milnor-1976-left-invariant-metrics]] — $GL^+(K)$ admits no bi-invariant metric, so the electric-term inner product / link metric is a choice.
- [[arnold-1989-classical-mechanics]] — symplectic/Hamiltonian geometric-mechanics framework behind the Hamiltonian lattice formulation and belief dynamics.
- [[lee-2012-smooth-manifolds]] — smooth-manifold and fiber-bundle foundations: a lattice gauge field as a discrete principal-bundle connection.

## See also

- [[Holonomy]]
- [[Parallel transport]]
- [[Non-flat connection and the photon analogy]]
- [[Gauge transformation]]
- [[Killing form]]
- [[participatory-it-from-bit]]
