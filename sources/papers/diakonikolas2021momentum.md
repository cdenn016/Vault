---
type: paper
title: "Generalized Momentum-Based Methods: A Hamiltonian Perspective"
aliases:
  - "Diakonikolas 2021"
  - "Hamiltonian momentum methods"
authors:
  - Diakonikolas, Jelena
  - Jordan, Michael I.
year: 2021
arxiv: "1906.00436"
url: https://arxiv.org/abs/1906.00436
tags:
  - cluster/info-geometry
  - project/transformer
  - field/mathematics
  - field/cs-ml
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Generalized Momentum-Based Methods: A Hamiltonian Perspective

> [!info] Citation
> Diakonikolas, J. & Jordan, M. I. (2021). "Generalized Momentum-Based Methods: A Hamiltonian Perspective." SIAM Journal on Optimization. arXiv:1906.00436.

## TL;DR
The paper derives a broad class of momentum-based optimization methods from a single time-varying Hamiltonian, recovering Nesterov's accelerated gradient descent and Polyak's heavy ball method as special cases. Convergence analysis flows directly from conserved quantities of the Hamiltonian rather than from separately constructed Lyapunov functions, unifying and extending prior results to constrained minimization in non-Euclidean normed spaces. A one-parameter family indexed by $\lambda \in [0,1]$ interpolates between the accelerated method ($\lambda=1$, rate $O(1/k^2)$) and a generalized heavy ball method ($\lambda=0$, rate $O(1/k)$).

## Problem & setting
The paper addresses the convergence theory of accelerated and momentum-based optimization methods, which are widely used in machine learning yet lack a unified nonasymptotic analysis covering both convex and nonconvex objectives, constrained domains, and non-Euclidean geometries. Prior inertial approaches using second-order ODEs encounter technical obstacles when extended to non-Euclidean or constrained settings, and their Lyapunov functions must be constructed ad hoc. The authors seek a principled derivation of the dynamics and its convergence certificates from a single mechanical object.

## Method
The central construct is the time-dependent Hamiltonian
$$H_M(x, z, \tau) = h(\tau)\, f(x/\tau) + \psi^*(z),$$
where $\tau = \alpha_t$ is a time reparametrization, $\psi^*$ is the convex conjugate of a strongly convex mirror-map $\psi$, $h(\tau) = \tau^\lambda$ for $\lambda \in [0,1]$, and $(x, z)$ are canonical position-momentum coordinates in a primal-dual pair of normed spaces. Hamilton's equations of motion yield the continuous-time dynamics (MoD):
$$\dot{x}_t = \frac{\dot{\alpha}_t(\nabla\psi^*(z_t) - x_t)}{\alpha_t}, \qquad \dot{z}_t = -\frac{h(\alpha_t)\dot{\alpha}_t}{\alpha_t}\nabla f(x_t).$$
Two conserved invariants of this Hamiltonian, $C^f_t$ and $C_t$, are exhibited and shown to encode convergence in function value (for convex $f$) and convergence in gradient norm (for potentially nonconvex $f$), respectively. The discrete-time method (GMDf) is derived by choosing the discretization so that $C^f_k \leq C^f_{k-1}$, making the conserved quantity a monotone Lyapunov function in discrete time. The use of the Bregman divergence $D_\psi$ associated with $\psi$ handles non-Euclidean geometry and eliminates the non-elastic boundary shocks that arise in the friction/inertial approach.

## Key results
For convex $f$ that is $L$-smooth and $\mu$-strongly convex, the discrete-time method (GMDf) with $H_k = A_k^\lambda$ achieves:
- $f(\hat{x}_k) - f(x^*) = O\!\left(\frac{L}{\mu k^2}\right)$ for $\lambda \in (0,1]$ (optimal rate, matching Nesterov),
- $f(\hat{x}_k) - f(x^*) = O\!\left(\frac{f(x_0)-f(x^*)+D_\psi(x^*,x_0)}{1+\sqrt{c\mu/L}\,k}\right)$ for $\lambda=0$ (heavy ball, rate $O(1/k)$).

For nonconvex $f$, the heavy-ball instantiation ($\lambda=0$) achieves the optimal rate $\min_{0\leq i\leq k}\|\nabla f(x_i)\|_*^2 = O(L(f(x_0)-f(x^*))/k)$ in general normed spaces, extending previously known Euclidean results. The analysis is unified across constrained and unconstrained settings, Euclidean and non-Euclidean norms.

## Relevance to this research
The Hamiltonian formulation of momentum-based methods is directly relevant to the VFE transformer program in two respects. First, VFE minimization is carried out iteratively as an optimization procedure; understanding the convergence properties of momentum-augmented E-step updates (if adopted) requires exactly this kind of non-Euclidean, constrained convergence theory, since the belief space is SPD/Riemannian rather than flat Euclidean. Second, the Bregman divergence $D_\psi$ plays a central structural role here, paralleling the KL divergence terms in the free energy functional; the mirror-map $\psi$ in (GMDf) corresponds formally to the convex potential that generates the information-geometric structure on the belief manifold. The conserved Hamiltonian quantities $C^f_t$ and $C_t$ are analogous to the free-energy Lyapunov structure guaranteeing VFE descent. Finally, the paper's treatment of non-Euclidean normed spaces (including $\ell_1$ and $\ell_\infty$) may inform future work on $GL(K)$-equivariant transport where the natural geometry is not the flat $\ell_2$ inner product.

## Cross-links
- Concepts: [[Bregman Divergence]], [[Information Geometry]], [[Variational Free Energy]]
- Related sources: [[wibisono-2016-variational-accelerated|wibisono2016variational]], [[su-2016-differential-equation-nesterov|su2016differential]]
- Manuscript/Project: [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{diakonikolas2021momentum,
  author  = {Diakonikolas, Jelena and Jordan, Michael I.},
  title   = {Generalized Momentum-Based Methods: {A} {H}amiltonian Perspective},
  journal = {SIAM Journal on Optimization},
  year    = {2021},
  note    = {arXiv:1906.00436},
}
```
