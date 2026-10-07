---
type: paper
title: "(De)Constructing Dimensions"
aliases:
  - Arkani-Hamed Cohen Georgi 2001
  - ACG deconstruction
  - Dimensional deconstruction
authors:
  - Arkani-Hamed, N.
  - Cohen, A. G.
  - Georgi, H.
year: 2001
arxiv: hep-th/0104005
url: https://arxiv.org/abs/hep-th/0104005
tags:
  - cluster/gauge-theory
  - cluster/multi-agent
  - project/multi-agent
  - project/transformer
  - field/physics
created: 2026-10-07
---

# (De)Constructing Dimensions

> [!info] Citation
> Arkani-Hamed, N., Cohen, A. G., and Georgi, H. (2001). *(De)Constructing Dimensions*. Phys. Rev. Lett. 86, 4757–4761. [arXiv:hep-th/0104005](https://arxiv.org/abs/hep-th/0104005) (v1, April 2, 2001). DOI [10.1103/PhysRevLett.86.4757](https://doi.org/10.1103/PhysRevLett.86.4757). [Local PDF](../pdfs/arkani-hamed-2001-deconstructing-dimensions-arxiv-hep-th-0104005.pdf) (arXiv v1, 142783 bytes, SHA-256 `7b97dd1c44fa561bbba76931a474a71d3dab8b77afc06c7dc712e6f3a65b1eb7`), downloaded October 7, 2026 and read in full.

## TL;DR

A four-dimensional gauge theory whose gauge groups and bifundamental fermions are arranged on a ring ("moose" or quiver diagram) produces, at long distances, a five-dimensional gauge theory in which only the fifth dimension is a lattice. Strong dynamics condenses the bifundamental fermion pairs into unitary link fields $U_{j,j+1}(x)$, and the kinetic term of these links is the hopping term of a lattice gauge theory along the ring. The gauge-boson mass matrix is the ring Laplacian, and its spectrum is the Kaluza–Klein tower of a gauge field on a circle.

## Problem and setting

Higher-dimensional gauge theories have dimensionful couplings and need a cutoff. The paper builds the extra dimension instead of postulating it, from a renormalizable and asymptotically free four-dimensional theory. The example (§2) has gauge group $\mathrm{SU}(m)^N\times\mathrm{SU}(n)^N$ on an $N$-sided polygon with cyclic symmetry, and Weyl fermions transforming as $(m,\bar n,1)$ and $(1,n,\bar m)$ under the three groups on each side.

## Method

When the $\mathrm{SU}(n)$ groups confine at scale $\Lambda_s\gg\Lambda$, each fermion pair attached to a strong group condenses, $\langle\chi_{i,i}\chi_{i,i+1}\rangle\sim4\pi f_s^3U_{i,i+1}$ with $U_{i,i+1}$ an $m\times m$ unitary matrix (Eq. 2.3). Below $\Lambda_s$ the theory is $N$ copies of $\mathrm{SU}(m)$ coupled to nonlinear sigma-model fields with the bifundamental law $U_{i,i+1}\mapsto g_i(x)U_{i,i+1}g_{i+1}^{\dagger}(x)$ (Eq. 2.4). The low-energy action (Eq. 2.5) is
$$S=\int d^4x\Big[-\frac{1}{2g^2}\sum_j\operatorname{tr}F_j^2+f_s^2\sum_j\operatorname{tr}\big(D_\mu U_{j,j+1}\big)^{\dagger}D^\mu U_{j,j+1}+\cdots\Big],\qquad D_\mu U_{j,j+1}=\partial_\mu U_{j,j+1}-iA_\mu^jU_{j,j+1}+iU_{j,j+1}A_\mu^{j+1}.$$
The authors read this as a five-dimensional $\mathrm{SU}(m)$ gauge theory latticized in the fifth direction only, with lattice spacing $a=1/(gf_s)$, circumference $R=Na$ and coupling $1/g_5^2=f_s/g$ (Eqs. 2.6–2.7). The condensed moose diagram "is a picture of the fifth dimension".

## Key results

The condensates break $\mathrm{SU}(m)^N$ to the diagonal subgroup. The gauge-boson mass matrix is $g^2f_s^2$ times the circulant matrix with 2 on the diagonal and $-1$ on the cyclic neighbors (Eq. 2.8), whose eigenvalues $M_k^2=4g^2f_s^2\sin^2(\pi k/N)$ (Eq. 2.9) reduce for $|k|\ll N$ to the Kaluza–Klein masses $2\pi|k|/R$ of a circle (Eq. 2.10). The unbroken diagonal coupling is $g_4^2=g^2/N$, which reproduces $1/g_4^2=R/g_5^2$ (Eq. 2.11). The static potential between charges at different sites falls as $1/(r_5^2+r^2)$ for $a\ll r\ll R$ (Eq. 3.2), while at distances short compared with $1/\Lambda$ and $1/\Lambda_s$ the theory is four-dimensional and interactions between sites $\ell,j$ arise only at $2|\ell-j|+1$ loops. The paper takes the two defining properties of an extra dimension to be coordinate labels that change as particles move and locality of interactions in those labels, and attributes locality to the nearest-neighbor structure of the moose (§3). Translation invariance and higher-dimensional Lorentz invariance are additional properties that may or may not arise; in the ring model both do, with $\mathrm{SO}(4,1)$ recovered as $a\to0$ (§4, Eq. 4.1). A linear sigma model with a quartic potential, or an $\mathcal N=1$ supersymmetric version with superpotential $W=\sum_iS_i(\det\Phi_i-\mu^2)$, gives perturbative completions (§6). The conclusions note that deconstructed dimensions need not have a manifold interpretation, citing a figure-eight moose as an example (§7).

## Relevance to this research

The action (2.5) is the form taken by independently supplied agent links when the base $\mathcal C$ has positive dimension: per-agent connections $A^{(i)}$ on $\mathcal C$ and bifundamental links $\Theta_{ij}(c)$ with kinetic term $\lVert\nabla\Theta\rVert^2$, $\nabla_a\Theta_{ij}=\partial_a\Theta_{ij}+A^{(i)}_a\Theta_{ij}-\Theta_{ij}A^{(j)}_a$. This identifies the agent graph with the latticized direction and $\mathcal C$ with the continuum directions; see [[Cellular sheaves and sheaf Laplacians]] and [[Lattice gauge theory]].

> [!note] Editorial: The mass matrix (2.8) generalizes from the ring to any agent graph. Expanding $\lVert\nabla\Theta\rVert^2$ about links of constant value, the quadratic term in the base connections is $\sum_{ij}\lVert A^{(i)}\bar\Theta_{ij}-\bar\Theta_{ij}A^{(j)}\rVert^2$, a sheaf Laplacian of the agent graph acting on the Lie-algebra-valued fields $A^{(i)}$, which is the connection Laplacian of the adjoint bundle when the links are unitary. The link kinetic term therefore penalizes disagreement between the agents' base connections after transport, with a stiffness set by the graph spectrum, and its zero modes are the collective connections that all agents share up to transport. This is a derivation for this note, not a result of the paper.

The transfer has limits. The links in the paper are unitary, the gauge groups compact, and the link values are produced by confining dynamics or a potential; the program's links lie in $\mathrm{GL}^+(K)$ and their values come from the variational free energy. The continuum fifth dimension needs locality and large $N$; a complete attention graph lacks the locality the paper takes as defining an extra dimension. Translation invariance is not required, so the paper's argument does not exclude irregular agent graphs; it simply makes no continuum claim about them.

## Cross-links

- Concepts: [[Lattice gauge theory]], [[Cellular sheaves and sheaf Laplacians]], [[Graph synchronization and connection Laplacians]], [[Holonomy]]
- Related sources: [[wilson-1974-confinement-quarks]], [[kogut-susskind-1975-hamiltonian-lattice-gauge]], [[dennis-2026-glk-attention-v2-rework-2026-10-05]]

## BibTeX

```bibtex
@article{ArkaniHamed2001Deconstructing,
  author        = {Arkani-Hamed, Nima and Cohen, Andrew G. and Georgi, Howard},
  title         = {(De)Constructing Dimensions},
  journal       = {Phys. Rev. Lett.},
  volume        = {86},
  pages         = {4757--4761},
  year          = {2001},
  doi           = {10.1103/PhysRevLett.86.4757},
  eprint        = {hep-th/0104005},
  archivePrefix = {arXiv}
}
```
