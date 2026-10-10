---
type: run
title: "Charged finite retained-reference transition"
aliases: ["Native retained-reference hierarchy refresh", "Owned Fisher-to-parent reference step"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# Charged finite retained-reference transition

Codex (2026). *Charged finite retained-reference transition*. MultiAgentELBO [PR263](https://github.com/cdenn016/MultiAgentELBO/pull/263), source commit 5700549b92607d7eb5664799a026bf2790ea040f and merge 890a091dcf5ed9f34c3d3ffbe6b3f74418e61e7e, adds [retained_reference_step](https://github.com/cdenn016/MultiAgentELBO/blob/890a091dcf5ed9f34c3d3ffbe6b3f74418e61e7e/src/multiagent_elbo/realizations/gaussian/latent_retained_reference.py) and the [retained transition contract](https://github.com/cdenn016/MultiAgentELBO/blob/890a091dcf5ed9f34c3d3ffbe6b3f74418e61e7e/docs/research/2026-10-03-latent-link-rg-plan/R2-RETAINED-REFERENCE-TRANSITION.md). One callable composes the existing common-old-state moment-field Fisher proposal with a new-state future-generator refresh of the supplied finite hierarchy, canonical affine copies/reversals, coisometries and factorized original-record decoder. It owns and charges the full fine recognition cache and one old-state replay snapshot. Six new tiny tests and 29 adjacent tests passed in one CPU run. Logical tensor inventories and named workspace lower bounds supply no peak-memory certificate, source compression, native posterior/population accuracy or growing operational law. All four RG gates remain open at roughly 65%; the N512/q9 production consumer is unrun in this checkpoint.

```bibtex
@misc{codex2026retainedreference,
  author = {Codex},
  title = {Charged finite retained-reference transition},
  year = {2026},
  howpublished = {MultiAgentELBO implementation checkpoint PR263},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/263}
}
```

## Existing native update and future readout

The fixed-c_* real GL+(2) lattice contract, original simultaneous product-Fisher force and opt-in thermostat remain those of the existing native and moment-trajectory paths. Every receiver and sender record contributes through one old HistoryRecognitionState: moment_history_direction computes that state's direction, and fisher_joint_proposal applies the supplied independent FisherNoise Brownian inputs. The new callable composes these operations without replacing the field, estimator, update convention or active defaults. The finite proposal remains a retraction approximating the declared continuous process, with finite-step, quadrature and population errors separate.

The current executable production profile is experiments/gaussian_moment_fisher_trajectory.py: N512, K2, three observed matter/source episodes and four generator episodes, mass 16, temperature .05, order-9 Cartesian primitive quadrature, primitive chunk 32 and four dt=1/40000 steps. Its saved result and settings are preserved. This checkpoint does not rerun that consumer, allocate the GPU or change the profile.

Future components use the updated generator episode C, where C is the observed prefix length, with the supplied standardized readout noise, joint component masses and identities. They do not use the stale pre-update slice. Forecast matter is the original fresh baseline N(a,J_0^-1), and source labels retain original pi. Observed matter means/covariances and beta are not substituted as the future sensor. Inference consumes only observed offsets; no heldout observation enters the update or refresh.

This is one fresh-baseline matter reference channel with a supplied finite component bank. It does not replace the general levelwise state in live c10, which includes both law channels and both cross morphisms. Inference time, learning episode and coarse depth remain separate indices. [[multiagentelbo-2026-10-09-hierarchy-codec]] and [[multiagentelbo-2026-10-09-joint-frame-codec]] provide the preceding canonical-frame, cost and root-relative continuity context, rather than an adoption of a packed codec in this implementation.

## Owned reference state and finite hierarchy

The returned RetainedReferenceStep owns updated full recognition parameters, one separately charged old-state replay snapshot, a frozen model, integration noise/weights, observed offsets, FisherNoise, readout noise, component masses/IDs, direction, component cache, hierarchy outputs and decoder factors. Tensor bindings are detached and cloned from caller inputs; later caller mutation does not change the retained packet. Mass/dt/temperature, layout/depth/prefix and original tau have explicit retained tensor bindings. The next call consumes its current state and model with that call's declared inputs; the object does not accumulate earlier reference objects or inference snapshots.

The refresh rebuilds the finite supplied dyadic hard hierarchy from updated future generator components. Each stage retains actual raw parent mean, covariance, precision, information vector, scalar density normalizer, transports, endpoints and all original positive copy slots, including internal loops and parallel copies. Shared primitive realizations and inverse reversals persist. Copies are neither independently redrawn nor deduplicated.

For the raw parent chart h_I(y)=m_I+F_Iy, use the ordinary symmetric positive-definite covariance frame F_I=Q_I^(1/2) and its inverse. A dressed raw copy G_e from J to I has

$$
B_e=F_I^{-1}G_eF_J,\qquad
b_e=F_I^{-1}(G_em_J-m_I),
$$

and exact affine reversal (B_e^-1,-B_e^-1 b_e). Translation belongs to the copy state even though it cancels from a centered Gaussian feature channel. The retained raw means and frame maps preserve original-unit interpretation. Covariance normalization here is distinct from the native proposal retraction and from base transport.

Fine-node coisometry blocks use F_I^-1 w_i T_i chol(Sigma_i), with original baseline fine covariance. Adjacent-stage blocks use the same actual child-root transports, compatible weights and child covariance frames. Intermediate factors cancel in ordered stage composition, so canonical channels agree with the compatible direct composite tree. Independently recursive nonsymmetric root-relative charts retain their separate orthogonal cocycle obligation. The complete primitive/recognition cache is deliberately kept so that the next native update and fresh frame refresh remain callable.

Nonfinite derived hierarchy, frame and copy outputs stop rather than returning a nonfinite tuple. The API also requires an unobserved generator episode, matching layout, normalized nonnegative component masses, distinct long component IDs and supplied nonempty readout inputs. These checks do not supply a posterior or growing-limit admission theorem.

## Factorized original-record decoder and query cost

The full all-row decoder is retained as factors: original receiver/source IDs and support, pi, signed/shared primitive maps, fresh matter baseline/covariance and independent per-receiver record-noise covariance. A requested finite joint query assembles the actual shared columns before computing record covariance and any supplied parent bridge. Shared sender covariance and primitive inverse dependence remain in that query.

RetainedReferenceStep.query(receiver_ids) snapshots only the requested incident catalog through the existing decoder. It neither enumerates every network-wide source pattern nor allocates an unconditional dense all-row covariance. For four supported choices at each of N receivers, network-wide pattern enumeration would require 4^N patterns. Factorization represents the same finite conditional law without that enumeration or an uncharged external-model lookup. The caller's later component enumeration/conditioning remains exponential in query size and incurs additional query storage and computation. The method does not make a large requested query free.

## Logical bytes and workspace lower bounds

Logical tensor groups charge old/new recognition state, frozen model, integration/Brownian/readout inputs, field direction, component cache, hierarchy/frame/copy outputs and decoder factors. Each distinct tensor object is counted once in group order; identity aliases are references. Distinct views remain distinct logical entries. Scalar controls, identifiers, graph layout and supplied hierarchy depth stay explicit.

This is a logical element inventory, not physical allocator usage. Python/container overhead and autograd/native-library workspace are excluded. Named moment signed-map, proposal covariance and parent eigenvector arrays provide workspace lower bounds only. They are not peak-process measurements or certified allocator bounds. Matrix exponentials, quadrature, products, inverses, SPD roots, requested joint-query arrays and arithmetic are separately incurred computation. Source-bit packing, useful parent compression and sufficient finite-bank integration accuracy do not follow from these charges.

The extensive cache plus one replay snapshot is a charged finite reference operation. It supplies an executable comparison seam for retained evolution, while complete native/posterior/population error, useful total cost, complete two-channel/coupling data, recursive chart control, compatible growing size/depth law and endogenous formation remain open.

## Completed mechanical validation and unrun production boundary

The six new tiny CPU tests ground update-to-refresh timing, original fresh baseline, every affine copy/reversal and raw density units, canonical staged/direct channel composition, shared-node joint covariance and hard support, owned bindings with logical byte charges, and the required unobserved generator slice. A 4x4 K2 fixture is used because two dyadic levels need sixteen children; its noncommuting links validate these finite reference formulas without setting research direction or proving large-network behavior. The initial missing-module check preceded implementation.

After the final finite-output guard and float64 density-normalizer oracle, one focused-and-adjacent pass completed 35 tests: six new and 29 adjacent, with zero failures, errors or skips. Pytest reported 1.93 seconds; JUnit reported 1.936 seconds. The receipt uses C:/anaconda/python.exe, torch 2.10.0.dev20251210+cu128 on device cpu, one torch thread and declared sequential BLAS thread settings. Its two warnings are Triton discovery of missing cuobjdump.exe and nvdisasm.exe; they are tool-discovery warnings rather than failures.

The exact source-bound [test receipt](https://github.com/cdenn016/MultiAgentELBO/blob/890a091dcf5ed9f34c3d3ffbe6b3f74418e61e7e/docs/research/2026-10-03-latent-link-rg-plan/evidence/r2-retained-reference-tests-20261009.json) binds the invocation and counts. Ignored artifacts/r2-retained-reference-tests-20261009.xml is 5,403 bytes, SHA256 bbc8ba562db4efadc0d62b9da9076e942332aaed7289678159ea96a7325d2a73, and matches in both code copies. Its machine-readable counts were read administratively during this ingest; no tests were rerun. Ordinary focused tests are not independent mathematical adjudication or a network-scale experiment.

The finite-q9 N512 native consumer and larger retained-state executions remain unrun in this checkpoint. No current launcher, default, configuration, host setting, manuscript, model or thermostat adoption changes. The GPU remains user-owned. All four RG completion gates remain open and the roughly 65% planning estimate is unchanged.

## Source bindings and relevance to this research

| Published item | Bytes | SHA256 |
|---|---:|---|
| latent_retained_reference.py | 11842 | d09c305fd0d02c2b82f1eda386d9f69872b9b7bef6f68c4a32ffb617d43f3797 |
| test_gaussian_latent_retained_reference.py | 11485 | e430faa02819d98383ed7459cdb5b73f030cff81aef2d67b5a4f3ea81f5eae7f |
| R2-RETAINED-REFERENCE-TRANSITION.md | 8822 | adfc9c1cd2bc8ade131b136a3b85fd6d66b3278f5f1846e99ea1083f72c5ab5e |
| evidence/r2-retained-reference-source-intake-20261009.json | 6499 | beb47c726ae1d152117e484b302b19894346f0d60a4e599acc0cd84cf18ea8bb |
| evidence/r2-retained-reference-tests-20261009.json | 8171 | e2bfa515756e9920800e45192433475d7294ad5d3f3672e4c06a3302156f113e |

The final intake binds twenty repository sources, including the ignored JUnit artifact, three live theory sources and one dated wiki context. Read-only live context is SPEC's scope/index conventions, c10's complete levelwise state and compatible composite-tree rules, and c12's original all-copy hierarchy. Their bytes match the source intake. The consulted theme is explicitly as of Research c65a0aab4fe6c730c92cedb868cb0d3386d7c896, 128709 bytes, SHA256 ca69dbc3fe0513f61c28300f92e5bdd4a41e79d7c08decedf1c639a36b8674a5; this ingest subsequently updates its synthesis.

Actual canonical Code main, HEAD and origin/main were confirmed at 890a091dcf5ed9f34c3d3ffbe6b3f74418e61e7e before vault mutation. Completed artifacts/r2-retained-reference-handoff-20261009.json has SHA256 36cdd58ce3cd38a26f16d02394ea6fba46805a8970e851d9692bf8e725eac0f0 in both code copies. This handoff records source/parity/preservation rather than scientific accuracy.

This develops [[Staged hierarchy formation and RG composability]], [[multiagentelbo-2026-10-09-hierarchy-codec]] and [[multiagentelbo-2026-10-08-native-flow-handoff-fisher-step]]. It makes the charged finite retained-reference refresh callable while preserving the separation between native update, supplied hierarchy, forecast law, cost and limiting closure. Only this new immutable note and the existing theme/root index/append-only log change. All 28 earlier October 9 immutable notes, ten prior postflight receipts, seven unique live source bindings and protected weekly-report WIP are preserved; this ingest runs no scientific workload or test and changes no code or manuscript.
