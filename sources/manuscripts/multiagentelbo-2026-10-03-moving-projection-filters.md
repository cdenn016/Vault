---
type: manuscript
title: "MultiAgentELBO filters with changing projection ranks, October 3, 2026"
aliases: ["Moving-projection filter approximation and marked path-TV bound"]
authors: ["MultiAgentELBO project"]
year: 2026
tags: [cluster/multi-agent, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-03
---

# Filters with changing projection ranks

> [!info] Citation
> MultiAgentELBO project (2026). *Smooth parent approximation with changing projection ranks*. Code commit [ee0acdd](https://github.com/cdenn016/MultiAgentELBO/commit/ee0acddddf29f1f38db4bb85831dbd2da2532764), [PR119](https://github.com/cdenn016/MultiAgentELBO/pull/119). The immutable archive is sources/archives/multiagentelbo-2026-10-03-moving-projection-filters/. This extends [[multiagentelbo-2026-10-03-fixed-projection-filters]] and retains the characteristic-error distinction in [[multiagentelbo-2026-10-03-conditional-parent-error]].

## Result and model

The [combined derivation](../archives/multiagentelbo-2026-10-03-moving-projection-filters/moving-projection-filter-approximation.md.txt) treats a finite-dimensional affine switching diffusion with constant positive-definite covariance, positive quadratic-softmax full-mark probabilities, rate-one whole-assignment redraws and frozen coefficients at c_*. The retained state is the assignment together with an assignment-dependent linear projection of the fine state. Retained ranks can range from zero to the full dimension. For every supplied initial probability law, finite requested horizon and positive tolerance, a parent exists with the actual retained initialization and full retained-path total variation below that tolerance.

The parent has a deterministic smooth filter consisting of a clock and two scalar registers. Its decoder determines both drift and the complete jump kernel. Filter dimension is independent of horizon and accuracy; coefficient functions, density-library size, derivative bounds and required numerical precision may grow without restriction. This result does not establish one coefficient set for all horizons or a useful implementation.

## Supported jumps and predictable densities

The [kernel derivation](../archives/multiagentelbo-2026-10-03-moving-projection-filters/moving-projection-kernel.md.txt) writes X=B_j r+Z_j z on the current assignment stratum. The event to k has the pushforward law of b_k(X)nu_j(dz) under r'=P_k X. Its exact support is P_k B_j r+image(P_k Z_j), which can be a lower-dimensional affine set or one point. An SVD gives its coarea normalization. The exact hidden posterior at the jump has dimension d-rank([P_j;P_k]); it can be singular even though the configuration noise is nondegenerate.

A zero-drift uniform-assignment reference is equivalent to the full native law on each finite horizon. Every positive holding age supplies independent residual Gaussian noise in the current hidden coordinates. The native predictable hidden density is therefore strictly positive almost everywhere on path times time, although the exact posterior at the jump itself can remain singular. A disjoint union of hidden strata, with a point mass in dimension zero, supplies one common sigma-finite measure. Exact jump-time posterior decoding is not claimed by the approximate regular decoder.

## Continuous-path error and both horizon regimes

The [marked path-TV derivation](../archives/multiagentelbo-2026-10-03-moving-projection-filters/marked-path-tv-bound.md.txt) compares two laws with the same retained initial law and stratum covariance. With A the native expected between-jump drift energy, V the integrated full variation of the supported jump kernels, and e the expected Hellinger characteristic cost, it proves e<=A/8+V/2 and TV<=min(1,2sqrt(e)+16e). The proof stops the candidate/native likelihood at its first exit from [1/4,4], includes unbounded jump overshoot, controls the changed-law exit probability and pastes the unique candidate continuation. It assumes no global likelihood equivalence or hidden-density relative entropy.

The combined proof approximates a tuple of predictable hidden densities in weighted L2, using fixed Gaussian references for inactive strata. Smooth finite-history capture remains valid because the fine path is continuous on each short gate without an assignment change; the probability of any change during the gates is at most their total length. Kernel variation contracts under the common supported jump channel. For arbitrary initial laws, truncation is used only as a proof intermediate: fine-law and parent-initialization comparisons each cost at most the initial tail probability, and the delivered parent starts from the actual retained law.

For any prescribed finite horizon family H_epsilon with expected visible-change count M_epsilon(H_epsilon) tending to infinity, rate at most one gives H_epsilon-s_epsilon >= M_epsilon(H_epsilon)-1, where s_epsilon is the switching time defined by expected count one. Hence every fixed-length window placed up to s_epsilon is eventually contained in that history horizon. Restriction of the same activated path contracts TV. The horizon-dependent parent family therefore covers both O1 error regimes simultaneously at this unrestricted-complexity existence scope.

## Evidence, limits and research relevance

The load-bearing support, coarea, density, stopped-likelihood, capture and activation arguments were reconstructed. Document checks covered links, delimiters, equation tags, spacing and whitespace; they are not substitutes for the written mathematics. No numerical experiment, model test or GPU calculation ran. The two-coordinate support example is an analytical rank check, not evidence for a large-network mechanism. A targeted primary-source lookup checked the diffusion Hellinger comparison in Genon-Catalot, Laredo and Nussbaum (2002), Lemma 3; the marked comparison here is derived directly.

[[Gauge-Theoretic Multi-Agent VFE Model]] and [[Staged hierarchy formation and RG composability]] now have a moving-projection existence construction for each prescribed horizon family. Effective complexity, accuracy of the implemented Gaussian-message parent, a single design for every horizon, thermodynamic control of the parent coefficients and learned structural feedback remain unproved. O4 formation is unaffected. Theory manuscripts, previous source notes, active configurations and historical scientific evidence are unchanged.

## BibTeX

    @misc{multiagentelbo2026movingprojection,
      author = {{MultiAgentELBO project}},
      title = {Smooth Parent Approximation with Changing Projection Ranks},
      year = {2026},
      howpublished = {Research records, MultiAgentELBO commit ee0acdd},
      url = {https://github.com/cdenn016/MultiAgentELBO/commit/ee0acddddf29f1f38db4bb85831dbd2da2532764}
    }
