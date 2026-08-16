---
type: concept
title: Assignment flow
aliases:
  - Assignment flows
  - Assignment manifold
  - Patch assignment flow
  - Patch assignment flows
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-08-12
updated: 2026-08-12
---

# Assignment flow

## Definition

An **assignment flow** is a smooth dynamical system on a product of statistical manifolds, designed
to label data observed on a graph. Each vertex $i$ of a graph carries an *assignment vector*
$W_i$ living in the relative interior $\mathcal{S}_c$ of the probability simplex over $c$ candidate
labels; the **assignment manifold** is the product $\mathcal{S}_c^n$ over all $n$ vertices, equipped
with the Fisher–Rao product metric

$$
g_w(u,v)=\sum_{\ell}\frac{u_\ell v_\ell}{w_\ell}.
$$

The flow is a coupled system of replicator equations $\dot W = R_W[F(W)]$, where $F$ is a *fitness*
or *payoff* function and $R_w(x)=w\circ x-\langle x,w\rangle w$ is the **replicator operator** — the
inverse Fisher–Rao metric tensor expressed in ambient coordinates. When $F$ is the Euclidean gradient
$\partial J$ of a smooth potential, the flow is literally the Riemannian gradient flow
$\dot W=\operatorname{grad}J(W)=R_W[\partial J(W)]$ of $J$ on the assignment manifold
([[gonzalez-alvarado-2025-patch-assignment]]).

The label is read off in the limit: under suitable conditions on the fitness function the flow
converges to vertices of the simplex, $W_i(t)\to e_{\ell(i)}$, so the smooth flow terminates in a
hard labeling ([[gonzalez-alvarado-2025-patch-assignment]]).

Assignment flows were introduced by Åström, Petra, Schmitzer and Schnörr (JMIV 2017) and are the
**discrete precursor of the [[Sigma flow|sigma flow]]**, which replaces the graph by a Riemannian
domain manifold ([[cassel-2024-sigma-flows]]).

## Why it matters here

Three features make this the most direct external analogue of the program's belief dynamics.

First, **the geometry is the algorithm.** The replicator operator is not a design flourish; it *is*
the inverse Fisher metric, so an assignment flow is a [[Natural gradient|natural-gradient]] flow on a
[[Statistical manifold|statistical manifold]] by construction. The program's Fisher–Rao
natural-gradient belief update is the same move applied to a Gaussian family instead of a simplex.

Second, **the interaction structure is learned, not hand-designed.** In the basic instance
$\dot W=R_W[\Omega W]$ the spatial interaction matrix $\Omega(t)$ comprises a non-local graph
Laplacian together with a term steering the flow toward discrete decisions, and $\Omega(t)$ is
learnable from data; geometric integration of the flow therefore generates a network, which is why
the authors describe assignment flows as **"neural ODEs on graphs"**
([[gonzalez-alvarado-2025-patch-assignment]]).

Third, **there is a variational-mechanics reading.** The solution of the flow is a critical point of
a Lagrangian action functional whose integrand pairs the Fisher–Rao kinetic term
$\lVert\dot P\rVert_g^2$ against a variance term in the fitness
([[gonzalez-alvarado-2025-patch-assignment]], following Savarino–Albers–Schnörr's geometric mechanics
of assignment flows). This is a genuinely close structural cousin of
[[Hamiltonian belief dynamics]] — a kinetic-plus-potential action on a statistical manifold — and is
worth reading before re-deriving that machinery.

What is *absent*, and marks the boundary with the program's own construction: there is no principal
bundle, no gauge group, no local frame, no connection, and no curvature. The interaction matrix
$\Omega$ couples simplices directly rather than transporting them, so nothing in the formalism
answers the program's motivating question of how to compare beliefs held in different frames.

## Details

**Patch assignment flows (P-AFs).** [[gonzalez-alvarado-2025-patch-assignment]] generalizes the
vectorized flow $\dot w = R^{\mathfrak v}_w[(\Omega\otimes I_c)w]$ to
$\dot w = R^{\mathfrak v}_w[(\Omega\otimes\Omega_c)w]$, adding an explicit **label–label** interaction
alongside the spatial one, a form general enough to cover multi-population and multi-game dynamics.
The paper's specific instance encodes *both* interactions entirely in a dictionary $\mathcal{D}$ of
labeled template patches together with a **patch dictionary graph** whose weighted adjacency
$\Omega_{\mathcal D}$ records how consistently two templates agree on the intersection of their
supports. The objective maximized is a bilinear patch-consistency energy
$J(P)=\sum_{ij\in\mathcal E}\langle P_i,\Omega_{\mathcal D}P_j\rangle$, and the resulting flow is
shown to be independent of the (arbitrary) orientation chosen for the underlying graph. Because the
dictionary graph is typically symmetric, several labelings can be locally consistent at once, and the
converged assignment vectors can be read as an **uncertainty quantification** over those
alternatives — the mean patch assignment function marks ambiguous sites rather than silently picking
one. Regularization is thus fully explicit in the dictionary, with a single user parameter $\lambda$
balancing initial data against dictionary-induced regularization.

**Where the program overlaps.** The replicator/simplex machinery here is the same object that appears
in [[Replicator dynamics]] on the evolutionary-game side of the vault; the assignment-flow literature
imports the fitness-function vocabulary from population dynamics explicitly
([[gonzalez-alvarado-2025-patch-assignment]]). Reading the two pages together makes clear that the
"consensus" and "selection" readings of the same equation are a change of interpretation, not of
mathematics.

**Forward pointer.** The concluding section of [[gonzalez-alvarado-2025-patch-assignment]] states
that discrete symmetries of the patch dictionary will next be studied from the viewpoint of *locally
equivariant networks generated by geometric flows* — i.e. via [[Bundle scale space|bundle scale
spaces]] ([[cassel-2025-bundle-scale-spaces]]). That sentence is the seam along which the Heidelberg
group's information-geometric and gauge-theoretic halves are being stitched together.

## Sources

- [[gonzalez-alvarado-2025-patch-assignment]] — assignment manifold, replicator operator, Riemannian
  gradient-flow form, patch assignment flows, the action-functional characterization, and the
  uncertainty-quantification behaviour.
- [[cassel-2024-sigma-flows]] — the continuous-domain successor; identifies assignment flows as
  products of statistical manifolds with Fisher–Rao geometry read as neural ODEs.
- [[cassel-2025-bundle-scale-spaces]] — the locally-equivariant successor programme the
  patch-assignment paper points toward.

## See also

- [[Sigma flow]]
- [[Harmonic map]]
- [[Statistical manifold]]
- [[Fisher information metric]]
- [[Natural gradient]]
- [[Replicator dynamics]]
- [[Hamiltonian belief dynamics]]
- [[Graph Laplacian]]
- [[Information geometry and natural gradient]]
