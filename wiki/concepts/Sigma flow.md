---
type: concept
title: Sigma flow
aliases:
  - Sigma flows
  - Sigma flow model
  - Sigma-alpha flow
tags:
  - cluster/info-geometry
  - cluster/gauge-theory
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-08-12
updated: 2026-08-12
---

# Sigma flow

## Definition

The **sigma flow** is the Riemannian gradient flow of a generalized harmonic energy for maps
$f:(M,h)\to(N,g)$ in which the target manifold $(N,g)$ is the *relative interior of the probability
simplex equipped with the Fisher–Rao metric*. Its stationary points are therefore
[[Harmonic map|harmonic maps]] from a closed Riemannian domain manifold into a
[[Statistical manifold|statistical manifold]], and the flow itself is a nonlinear geometric PDE
([[cassel-2024-sigma-flows]]). The name is borrowed from the physics of sigma models, which are
likewise field theories of maps into a curved target.

The construction fuses two lineages. From the Laplace–Beltrami framework for low-level vision it
takes the harmonic-map formalism and the idea of a data-induced domain metric; from
[[Assignment flow|assignment flows]] it takes the simplex-with-Fisher–Rao state space and the habit
of reading the resulting dynamical system as a neural ODE. The sigma flow is, in effect, the
**continuous-domain** version of the assignment flow, with the graph replaced by a manifold and the
non-local graph interaction replaced by a Laplace–Beltrami operator ([[cassel-2024-sigma-flows]]).

## Why it matters here

This is the closest published relative of the program's information-geometric field theory, and it
sharpens by contrast what the program's own construction actually adds. The sigma flow is a genuine
field of probability distributions over a base manifold, evolving by a geometric PDE, with
Fisher–Rao geometry in the fiber — the same silhouette as
[[Agents as fibre-bundle sections|agents as sections of associated bundles with statistical-manifold fibers]].

But the silhouette is where the agreement stops. The sigma flow has **no principal bundle, no gauge
group, no connection, and no curvature term**: the "fiber" is one fixed copy of the simplex, the map
$f$ is a plain map rather than a section of an associated bundle, and there is no local frame
freedom to be transported. Its objective is a harmonic (plus entropic) energy, not a
[[Variational free energy|variational free energy]] — there is no likelihood term, no
complexity/accuracy decomposition, and no population of agents. What it *does* have that the
program does not is a single learnable object of unusual elegance, discussed next.

> [!note] Editorial: The reading "sigma flow = the program's statistical-manifold fiber without the
> gauge half; [[Bundle scale space]] and [[cassel-2025-yang-mills-data]] = the gauge half without the
> statistical fiber" is the vault's own synthesis across the three Heidelberg papers. None of them
> claims to supply both halves, and none of them mentions variational free energy.

## Details

**The distinctive ingredient: a state-dependent, learnable domain metric.** In the classical
harmonic-map setting both metrics are given. The sigma flow instead makes the Riemannian metric $h$
of the *domain* manifold depend on the evolving state, and realizes that dependence through a mapping
with a compact, **time-variant parametrization that can be learned from data**
([[cassel-2024-sigma-flows]]). This is what converts a PDE model into a machine-learning model: the
learned object is the geometry of the domain, not a stack of weight matrices. Geometric integration
of the resulting flow yields a network — a neural ODE whose layers are time steps of a geometric
PDE, exactly the design principle also used by assignment flows.

**Standing assumptions and what is *not* proved.** The domain $(M,h)$ is taken to be a compact,
oriented, connected Riemannian manifold without boundary — for images, the torus $\mathbb{T}^2$ with
doubly periodic boundary conditions and a data-induced metric — and the maps are smooth. Compactness
is doing real work: it licenses the standard spectral theory of the Laplace–Beltrami operator, which
is the basis for the paper's Lyapunov functional ([[cassel-2024-sigma-flows]]).

> [!warning] No existence or global-convergence theorem
> [[cassel-2024-sigma-flows]] states plainly (§1.3) that its setting **violates** the basic
> assumptions of the harmonic-map literature it surveys: the target is *open*, has *positive
> sectional curvature*, and carries a *non-metric affine connection*. Existence and global
> convergence of the gradient flow are therefore **left to future work**; the paper proves a
> Lyapunov decrease and otherwise confines itself to geometric structure. Any argument that borrows
> the sigma-flow template inherits this gap and must not cite it as a well-posedness result.

**Entropic variant and labeling.** A plain harmonic energy does not by itself drive the state to a
decision. Adding an entropic potential yields an *entropic harmonic energy* whose flow converges to
the boundary of the simplex, turning the sigma flow into a proper labeling method; a
$\sigma$-$\alpha$ variant and explicit expressions in the two affine (exponential and mixture)
coordinate systems of information geometry are also given ([[cassel-2024-sigma-flows]]). The
entropic term plays the role that [[Deterministic Annealing|annealing]]-style rounding plays
elsewhere: it is what makes a smooth flow terminate in a discrete answer.

**Relation to transformers.** [[cassel-2024-sigma-flows]] devotes a section to structural
similarities between networks generated by geometric integration of sigma flows and transformer
architectures, and offers this in both directions — as an explanation of transformer-like structure
and as an invitation to use geometric design principles for structured prediction elsewhere. See
[[Attention mechanisms — theory and positional structure]].

## Sources

- [[cassel-2024-sigma-flows]] — the sigma flow model: definition, harmonic-map formulation,
  state-dependent learnable domain metric, Lyapunov functional, entropic variant, and the explicit
  statement that existence and global convergence remain open.
- [[gonzalez-alvarado-2025-patch-assignment]] — the discrete assignment-flow side of the same
  program, from which the simplex/Fisher–Rao state space and the neural-ODE reading are inherited.

## See also

- [[Harmonic map]]
- [[Assignment flow]]
- [[Bundle scale space]]
- [[Statistical manifold]]
- [[Fisher information metric]]
- [[Information geometry and natural gradient]]
- [[Gauge equivariance and geometric deep learning]]
- [[Agents as fibre-bundle sections]]
