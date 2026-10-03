---
type: run
title: "MultiAgentELBO activation source cubature calibration, October 3, 2026"
aliases: ["Activation source integration accuracy"]
authors: ["MultiAgentELBO project"]
year: 2026
tags: [cluster/multi-agent, cluster/vfe, cluster/info-geometry, project/multi-agent, field/statistics, field/mathematics]
created: 2026-10-03
---

# Activation source cubature calibration

MultiAgentELBO project (2026). *Activation source-integration calibration*. Code commit [2ae407a](https://github.com/cdenn016/MultiAgentELBO/commit/2ae407a2de0e48e1f021fdffe5240a427ef79dff), [PR123](https://github.com/cdenn016/MultiAgentELBO/pull/123). Immutable [results](../archives/multiagentelbo-2026-10-03-activation-source-calibration/results.md.txt), [contract](../archives/multiagentelbo-2026-10-03-activation-source-calibration/contract.md.txt) and [summaries](../archives/multiagentelbo-2026-10-03-activation-source-calibration/summary.json) preserve committed source bytes. Per-row data and executed source snapshots remain in the linked code commit.

## Frozen design and reference

The saved study supplies sixteen activation draws for each of two frozen GL(2,R) models, at 512 and 1,024 nodes. Each receiver has cycle and stride-17 sources, temperature 0.5, and a three-node star. Initial configuration is product Gaussian and its assignment is independently drawn from the learned prior. Conditioning on sixteen-node arithmetic block means therefore gives an exact Gaussian activation fiber.

A one-dimensional characteristic-function integral evaluates the expected binary logistic probability of a quadratic Gaussian logit. The comparison preserves the production rule's six physical Gaussian coordinates, Cholesky orientation and twelve positive cubature points. Receiver zero is an actual first marginal of the implemented sequential candidate. Other unprefixed rows calibrate the integration primitive only; later joint-candidate rows depend on hypothetical prefix labels.

## Results

The one-thread CPU analysis completed 24,576 rows across 32 activations in 19.718451 seconds. At N=512 and N=1024, all-receiver mean absolute probability errors were 0.01567402 and 0.01585559, with maxima 0.12651286 and 0.17316566. Mean Bernoulli row KL values were 0.00167340 and 0.00185331 nats. Receiver-zero mean errors were 0.00301274 and 0.00196645, with mean KL 0.0000187551 and 0.0000081791 nats.

All reconstructed initial means agreed with both saved grids to within 3.34e-16. Adaptive integration estimates were below 1e-10 and the analytic tail bound was about 2.70e-17; the adaptive estimates are not rigorous enclosures. Five tiny tests passed, checking independent direct Gaussian integration, coordinate changes, dense conditioning, native logits and the existing public cubature path. All saved row arithmetic and group mean errors/KLs were independently checked.

Receivers are correlated and each size uses one frozen model realization. These are descriptive numerical errors, without nodewise standard errors, a general size trend or model-general statistical inference. No trajectories, training or GPU jobs ran; the active profile and production filter are unchanged.

## Relevance to this research

This gives a concrete accuracy defect to address in practical O1. The next bounded implementation should improve binary source probabilities and their associated tilted Gaussian moments together. Updating only probabilities would leave the filter's moments tied to the old discrete rule. The work continues [[multiagentelbo-2026-10-03-entropic-time-scale]]'s practical O1 continuation without reopening its exhausted formation loop.

The reference is for full-proposal row marginals at activation. Visible intensities require subtracting full self-assignment probability. A sum of these row KL values is not joint source KL or retained path KL. Native no-visible-change histories require survival filtering, so this activation calculation does not supply an exact later Gaussian filter. General practical O1, full O4, intrinsic partitions and hierarchical feedback remain unresolved.

The contract cites the primary characteristic-function inversion treatment and acknowledges Kassis et al. (2026), [Scientific Agent Skills](https://doi.org/10.48550/arXiv.2609.00065), for the design procedure.
