---
type: manuscript
title: "Group-Valued Links and Inference in Gauge-Covariant Gaussian Attention"
aliases: ["Unified Attention Companion", "Attention unification October 2026"]
authors: ["Robert C. Dennis"]
year: 2026
url: "manuscripts/Attention/attention_unified.tex"
tags: [cluster/attention, cluster/gauge-theory, cluster/info-geometry, cluster/vfe, project/transformer, project/multi-agent, field/mathematics, field/cs-ml, field/statistics]
created: 2026-10-03
---

# Group-Valued Links and Inference in Gauge-Covariant Gaussian Attention

## Citation and scope

Robert C. Dennis (2026). *Group-Valued Links and Inference in Gauge-Covariant Gaussian Attention*. Standalone working companion, October 3, 2026, [LaTeX source](../../manuscripts/Attention/attention_unified.tex). This consolidates the six notes on frame natural gradients, link origin, link curvature, projected-gradient receivers, projected prediction, and template routing. The originals and the four existing GL(K) manuscripts remain unchanged. The source-coverage and implementation record is [the consolidation record](../../docs/attention-unification-2026-10-03.md).

The author selected **Option A, exponential group-valued links**, as the primary direction for later integration into the GL(K) attention manuscript. This is an authorial research choice, not a result inferred from small-network checks. Compression (Option B) and the implemented head sum (Option C) are supporting comparisons and implementation bridges.

## Construction

The primary object is $\Theta_{ij}=U_i\exp(X_{ij})U_j^{-1}$. It is invertible and transforms by the endpoint law. For a low-rank generator $X=OT$, the exact identity $e^{OT}=I+O\varphi_1(TO)T$ relates the group link to the current selective channel. The affine and logarithmic descriptions overlap on stated real-logarithm domains; they are not globally equivalent parametrizations of all invertible matrices. An unsent complement persists locally only after complement preservation is declared. A full additive residual does not follow from that complement construction when the channels tile the fiber.

The inverse-edge triangle $F_{ijk}=\Theta_{ik}^{-1}\Theta_{ij}\Theta_{jk}$ coexists with the absence of directed causal cycles. Flatness on the complete ordered support is the composition cocycle, equivalent to recurrence, and invertible flat fields are pure gauge. A constant exponential edge has the same conjugacy class of holonomy on every triangle; it is nonflat unless that exponential is identity. There is no defined extremal ordering that makes it "maximally curved." Regression links derive from joint cross-covariances and may be singular. For a jointly Gaussian ordered sequence, the all-strict-triples regression cocycle is equivalent to the first-order Markov property. A regression map is not automatically an exponential group link.

The predictive, receiver, and template constructions retain separate probability models. The predictive covariance is the moment calculation of a declared product-source, independently routed kernel. The receiver's frozen expected-log-likelihood energy produces a normalized generalized posterior or a variational coordinate update; averaging separately normalized label-conditioned posteriors generally gives a different mixture. The template mean-field KL responsibilities differ from the structured posterior obtained by treating the incoming Gaussian as evidence. Untied values are a declared readout, not a natural-gradient mean update without additional assumptions.

The frame section keeps the Frobenius-pullback and belief-family Fisher distinct. The latter has stabilizer null directions; its positive completion is an additional geometry. Its batch implementation uses input-occurrence counts normalized by the scored-token count. The stored-frame optimizer is not the output Fisher of the language model and does not imply Fisher optimization of content maps. The infinite-distance singular-boundary result concerns a noiseless Gaussian pushforward; a positive output noise floor changes that statistical model.

## Current implementation and evidence

Implementation descriptions were traced against the VFE_3.0 working tree at base commit `f35c573ab81a7a7273d5561e2f6f0168a3fa95ff`, including existing uncommitted changes. The provenance record includes hashes of the relevant files; the Git SHA alone is not a reconstruction of that working tree. No VFE source/configuration edit is part of this consolidation.

The inspected launcher selects projected predictive attention, moment-matched covariance, diagonal Gaussian storage, a linear decoder, and AdamW frame updates. The channel-likelihood receiver and closed-form receiver updates, Gaussian-template block, completed frame-Fisher policy, and group-log retraction are reachable alternatives. Template routing still uses local coordinates and covariance passthrough; its structured posterior and reference-coordinate version are theoretical constructions. Existing routing-holonomy diagnostics were present as uncommitted work; they do not implement a learned independent exponential edge generator.

The manuscript supplies derivations and reports focused existing one-thread CPU checks separately from historical numerical measurements. Tiny checks ground formulas and code paths only. No GPU workload, training comparison, or large-population experiment was run for this consolidation. No superiority of an optimizer or attention route, and no common population ELBO for the whole composed stack, is established.

## Relation to the larger theory

The current GL(K) attention manuscript already contains the reference-coordinate construction and predictive moment theorem. The gradient companion supplies derivative support. The supplement gives the normalized-joint/evidence identity and population covariance scope. The nonlinear extension constructs a separate correlated population model with source and reliability inference and information control. Its expected record costs generally differ from marginal Gaussian KL routing. The unified companion maps these relationships and the passages that would need later revision; it does not yet integrate into those manuscripts.

## Relevance to this research

This is the integration reference for [[GL(K) gauge-equivariant attention]], [[Projected predictive attention]], [[Projected gradient attention]], [[Template routing]], [[Holonomy]], and [[Natural gradient]]. It preserves the author's chosen group-valued direction while distinguishing mathematical identities, model choices, current implementations, and empirical questions. It also supplies a bridge to correlated agent theory without claiming that current per-token Gaussian tensors carry cross-agent covariance.

## Prior source notes

[[dennis-2026-phi-natgrad]], [[dennis-2026-link-origin]], [[dennis-2026-link-curvature]], [[dennis-2026-projected-gradient]], [[dennis-2026-projected-predictive]], [[dennis-2026-template-routing]], [[dennis-2026-glk-projected-matrix-links-v2]], and [[dennis-2026-neuron-free-agent-theory]].

## BibTeX

```bibtex
@unpublished{dennis2026attentionunified,
  author = {Robert C. Dennis},
  title = {Group-Valued Links and Inference in Gauge-Covariant Gaussian Attention},
  year = {2026},
  note = {Standalone theoretical and implementation companion, October 3, 2026}
}
```
