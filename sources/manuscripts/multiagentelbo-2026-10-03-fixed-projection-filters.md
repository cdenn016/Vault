---
type: manuscript
title: "MultiAgentELBO finite-horizon fixed-projection filters, October 3, 2026"
aliases: ["Fixed-projection filter approximation with unrestricted smooth complexity"]
authors: ["MultiAgentELBO project"]
year: 2026
tags: [cluster/multi-agent, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-03
---

# Finite-horizon fixed-projection filters

> [!info] Citation
> MultiAgentELBO project (2026). *Finite-horizon fixed-projection filters with unrestricted smooth complexity*. Code commit [266e1f7](https://github.com/cdenn016/MultiAgentELBO/commit/266e1f77968b03bdf0c4963adaa3247f351b5e7b), [PR118](https://github.com/cdenn016/MultiAgentELBO/pull/118). The immutable archive is sources/archives/multiagentelbo-2026-10-03-fixed-projection-filters/. This continues [[multiagentelbo-2026-10-03-conditional-parent-error]] and [[multiagentelbo-2026-10-03-continuous-parent-limits]].

## Statement and assumptions

The [approximation derivation](../archives/multiagentelbo-2026-10-03-fixed-projection-filters/fixed-projection-filter-approximation.md.txt) treats a fixed finite-dimensional affine switching diffusion, a finite assignment set, constant positive-definite noise covariance, positive quadratic-softmax full-mark probabilities and rate-one whole-assignment redraws. The retained projection is fixed and full-row-rank; initialization has a finite fourth moment and may be correlated or singular. For each requested finite horizon H and tolerance eta, it constructs a deterministic retained-history parent with three continuous internal coordinates and retained path relative entropy less than eta. The retained initial law is unchanged.

The clock and two scalar registers have smooth autonomous coefficients, continuous initialization on each assignment stratum and identity updates at actual assignment changes. A smooth density decoder determines both the parent drift and its source probabilities under the actual native channels. The dimension is independent of horizon and accuracy, but the coefficient functions, density dictionary, numerical precision and derivative bounds may grow without restriction. The theorem does not supply one coefficient set for all horizons.

## Construction and mathematical evidence

The native hidden law admits a predictable density at positive times under the stated nondegenerate affine model, even when activation is singular. Native fourth moments place it in L2 of the weighted density space L1((1+|z|^2)dz). Increasing finite sampled-history sigma-fields approximate that density; their finite libraries can be replaced by finite positive Gaussian mixtures. A common Gaussian component gives a library-independent quadratic bound on source negative log probabilities. Localizing retained coordinates proves expected source-cost continuity along the full approximation sequence. The ideal mixed posterior has characteristic risk bounded by delta^2 K_H + H[-log(1-delta)], which tends to zero.

The [smooth realization derivation](../archives/multiagentelbo-2026-10-03-fixed-projection-filters/smooth-finite-history-realization.md.txt) encodes initial observations on safe quantization cores, captures later prefixes in alternating scalar registers, and charges all short capture intervals and exceptional paths explicitly. Overflow cells with positive probability are included. Its decoder uses a convex finite library and never reads an overwritten register outside a charged interval. This produces the required weighted-density approximation under the native law. Finite auxiliary budget and the existing conditional-characteristic identity then identify the small risk with retained path KL.

The derivations were reconstructed at their stated assumptions. Local links, display delimiters, equation tags, spacing and whitespace checks passed. These document checks do not independently prove the mathematics. No numerical experiment, model test, GPU calculation or theorem-prover run was performed.

## Relation to existing research and limits

The live Chapter 11 definition at Research commit 60e2126 requires individual smoothness but states no uniform derivative or complexity bound. The older P09 approximate-filter lower-bound route additionally assumes uniform regularity and compactness. This construction does not contradict that conditional lower bound or exact-closure obstruction; it shows why their extra hypotheses matter when considering an infimum over increasingly complicated filters.

For a specified sequence of finite horizons, the construction can be chosen separately at each parameter value, with dimension remaining three. Contained windows inherit its total-variation bound. Assignment-dependent projections introduce continuous-coordinate jump kernels and support obligations that remain unresolved here. No uniform large-N result, useful complexity estimate, accuracy certificate for the existing Gaussian-message implementation, formation mechanism or full O1/O4 closure follows. [[Gauge-Theoretic Multi-Agent VFE Model]] and [[Staged hierarchy formation and RG composability]] retain these open obligations. Theory manuscripts and previous source notes are unchanged.

## BibTeX

    @misc{multiagentelbo2026fixedprojection,
      author = {{MultiAgentELBO project}},
      title = {Finite-Horizon Fixed-Projection Filters with Unrestricted Smooth Complexity},
      year = {2026},
      howpublished = {Research records, MultiAgentELBO commit 266e1f7},
      url = {https://github.com/cdenn016/MultiAgentELBO/commit/266e1f77968b03bdf0c4963adaa3247f351b5e7b}
    }
