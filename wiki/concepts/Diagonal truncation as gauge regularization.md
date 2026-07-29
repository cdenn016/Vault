---
type: concept
title: "Diagonal truncation as gauge regularization"
aliases:
  - "covariance truncation as regularizer"
  - "diagonal projection of the congruence"
  - "truncated congruence energy"
tags:
  - cluster/spd-geometry
  - cluster/gauge-theory
  - cluster/info-geometry
  - project/transformer
status: draft
created: 2026-07-25
updated: 2026-07-25
---

# Diagonal truncation as gauge regularization

## Definition

When a variational model carries **diagonal** Gaussian beliefs in a fixed ambient basis but
transports them by a **general** $\mathrm{GL}(K)$ congruence, the transported covariance
$\Omega\,\mathrm{diag}(s)\,\Omega^\top$ leaves the diagonal family and must be projected back. The
usual projection keeps only the diagonal,

$$
\big[\mathrm{diag}(\Omega\,\mathrm{diag}(s)\,\Omega^\top)\big]_k=\sum_l\Omega_{kl}^2\,s_l ,
$$

and is naturally read as an approximation error to be removed once an exact route is available.
**Diagonal truncation as gauge regularization** is the observation that under a *non-compact*
structure group the truncation is load-bearing in the opposite direction: it is what keeps the
coupling energy bounded, and removing it makes the model untrainable. The truncated expression is a
sum of squares, so it is always inflated and never near-singular, whereas the exact congruence is
near-singular along the contracted directions of an ill-conditioned $\Omega$. A Kullback–Leibler
divergence taken against a near-singular covariance grows like $\mathrm{cond}(\Omega)^2$ through its
trace term, so the exact energy inherits a heavy tail keyed to frame conditioning that the truncated
energy does not have.

## Why it matters

The tension is structural rather than numerical, and it is a cost of choosing a non-compact gauge
group. $\mathrm{GL}(K)$ frames are free to become arbitrarily ill-conditioned; there is no compact
stabilizer bounding $\mathrm{cond}(\Omega)$ from above, and nothing in a divergence-based objective
penalizes conditioning directly. Something in the pipeline must therefore bound the energy, and in
this program the diagonal projection is the implicit answer.

The regime where the exact form is well behaved is precisely the regime where it is unnecessary. If
$\Omega$ is near-orthogonal then $\mathrm{cond}(\Omega)\approx1$, the exact energy is tame, and the
truncation error it removes is negligible, so the two paths coincide and there is nothing to win. If
$\Omega$ is ill-conditioned the exact energy explodes. Exactness and a usable non-compact gauge are
in direct opposition, and there is no operating point at which the exact form is both necessary and
affordable.

The failure is also self-reinforcing rather than merely large, because it couples to
[[Divergence clamp saturation]]. Once the exact energy exceeds the safety-net ceiling the clamp
emits a constant whose derivative is zero, and the pair mask zeroes the derivative of the saturated
pair. That removes the one term whose gradient would push the frames back toward well-conditioned
values, so saturation begets more saturation. This is a sharper pathology than the original
saturation case, where a saturated regularizer simply went inert: here the saturated term is the one
maintaining the conditioning that keeps it below the ceiling.

## The alternatives, and why the obvious one fails

Three designs could bound the energy without truncation. A **compact or tied gauge** (orthogonal
frames, or generators restricted to a compact subgroup) makes $\mathrm{cond}(\Omega)=1$ by
construction and removes the problem entirely, at the cost of the non-compact expressiveness the
program set out to use. An **explicit conditioning penalty** on the frames — a Frobenius norm bound
on $\phi$, which is what the M-step projection already supplies — attacks the tail directly and is
the practical route already in use. A **covariance family closed under congruence** removes the
projection by construction.

The third is the interesting failure. Declaring the covariance diagonal in the agent's *own* fiber
frame, $\Sigma_i=U_i\,\mathrm{diag}(\sigma_i)\,U_i^\top$, does give a family closed under
$\mathrm{GL}(K)$. But under a flat Regime-I cocycle $\Omega_{ij}=U_iU_j^{-1}$ the sender frame then
cancels from the congruence and the receiver frame from the location, so the pair energy depends
only on the body-frame coordinates $a=U^{-1}\mu$ and the gauge leaves the belief coupling entirely.
The frame table receives no gradient at all. Closure is bought by making the gauge inert, which is
an ablation rather than a fix.

> [!note] Editorial: this page generalizes a measured result in one codebase into a design
> principle. The measurements are in [[2026-07-25-exact-congruence-truncation-tension]]; the claim
> that the same tension holds for any non-compact structure group with a congruence-transported
> divergence is an argument from the $\mathrm{cond}(\Omega)^2$ scaling of the Gaussian KL trace
> term, not a theorem with an independent published source.

## Measured instance

In the [[VFE Transformer Program]] at $K=20$ with an untied `block_glk` gauge, on a trained state
with vertex condition number median 11.6 and maximum 108.9, the exact congruence energy exceeds the
truncated one by a factor of 7.2 at the median, 66.9 at p90, 426 at p99, and 4604 at the maximum,
with a maximum of 10,912 nats against a clamp of 160. The observed maximum tracks
$\mathrm{cond}_{\max}^2=11{,}858$ to within 10%, which is the direct evidence for the scaling
argument. The exact arm's clamp-saturation fraction runs from 0.06 to 0.979 over 7,900 steps and the
run never recovers, while the truncated baseline holds saturation at exactly 0.0000 for 15,000 steps
and reaches validation perplexity 139.3. The exact implementation is pinned to $3\times10^{-13}$
against a dense reference, so this is a statement about the objective rather than about a bug.

## In this work

The projection lives in `transport_covariance` and is the default path for the
`gaussian_diagonal` family. Two opt-in families exist as measurement instruments and are both
default OFF: `gaussian_diagonal_exact` computes the untruncated coupling energy by pulling the query
back through $\Omega^{-1}$ rather than pushing the key forward, and `gaussian_frame_diagonal`
declares the covariance diagonal in the fiber frame. The first quantifies how much divergence mass
the truncated attention score discards; the second quantifies what the gauge channel is worth by
disconnecting it. The full-SPD family `gaussian_full` avoids the question entirely by carrying the
whole covariance, at cubic cost.

## Sources

- [[2026-07-25-exact-congruence-truncation-tension]] — the measurements and both family
  implementations
- [[2026-06-21-k160-hyperprior-saturation]] — the original clamp-saturation instance
- [[gl-k-attention]] — the congruence action and the $\mathrm{GL}(K)$ invariance theorem the exact
  identity relies on
- [[pennec-2006-affine-invariant-tensor]] · [[bhatia-2007-positive-definite-matrices]] — the
  congruence action on the SPD cone

## See also

[[Divergence clamp saturation]] · [[GL(K) gauge group]] · [[GL(K) gauge-equivariant attention]] ·
[[Symmetric spaces and the SPD cone]] · [[SPD-manifold geometry and Riemannian optimization]] ·
[[Parallel transport]] · [[Renyi divergence]] · [[VFE Transformer Program]]
