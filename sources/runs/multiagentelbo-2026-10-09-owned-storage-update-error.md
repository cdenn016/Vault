---
type: run
title: "Owned quadrature storage and conditional recognition-update error"
aliases: ["Exact retained input backing and coded evolution", "Finite full-recognition update allowance"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# Owned quadrature storage and conditional recognition-update error

Codex (2026). *Owned quadrature storage and conditional recognition-update error*. MultiAgentELBO [PR265](https://github.com/cdenn016/MultiAgentELBO/pull/265), source commit bc0466ce5ff687976d4ec635e9d592800aa642c3 and merge f7dd9f512feb214cac9ca6ec9a9e01f7903a7f8f, implements [exact owned broadcast inputs](https://github.com/cdenn016/MultiAgentELBO/blob/f7dd9f512feb214cac9ca6ec9a9e01f7903a7f8f/docs/research/2026-10-03-latent-link-rg-plan/R2-OWNED-INPUT-STORAGE.md) and records a [conditional finite-horizon encoded update construction](https://github.com/cdenn016/MultiAgentELBO/blob/f7dd9f512feb214cac9ca6ec9a9e01f7903a7f8f/docs/research/2026-10-03-latent-link-rg-plan/R2-RETAINED-UPDATE-ERROR.md). The storage implementation preserves supplied values and ownership while separating full logical tensor charges from unique backing bytes. The mathematical construction propagates full-recognition coding and arithmetic error through the original finite field/Fisher proposal, then refreshes the same supplied one-channel hierarchy and endpoint decoder. Actual-law exit/amplification, useful precision and total cost, native accuracy, growing laws and formation remain open; all four RG gates stay open at roughly 65%.

```bibtex
@misc{codex2026ownedstorageupdateerror,
  author = {Codex},
  title = {Owned quadrature storage and conditional recognition-update error},
  year = {2026},
  howpublished = {MultiAgentELBO storage and research checkpoint PR265},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/265}
}
```

## Exact owned input representation

[[multiagentelbo-2026-10-09-retained-admission]] identified repeated quadrature input as a separate storage seam after recording the complete extensive N512 reference. This checkpoint implements ownership of one representative along every stride-zero input dimension, followed by expansion to the original public tensor shape. Arbitrary nonbroadcast inputs retain detached-clone behavior. Caller mutation cannot change the owned representative. No fine recognition parameter, primitive/copy, frame, Brownian input, model or query component is removed, and no supplied noise value, field, Fisher proposal or decoder law changes.

The existing logical_bytes inventory still charges full element counts for each distinct tensor object, with identity aliases counted once. New owned_storage_bytes instead charges each unique device/backing-storage-pointer pair once in the same group order, using actual backing size. Multiple shared views therefore share one storage charge even when they remain separate logical entries. Neither inventory includes allocator reserve, Python/container overhead or autograd/native-library workspace. These are separate retained inventories, rather than measured process peaks or parent-compression results.

The source-bound input-only N512 check loaded the original archived rule and called only the ownership helper. Its float64 CPU view has shape (6561,4,1024,4), strides (4,0,0,1), exact representative values and caller-independent backing. Logical charge remains 859,963,392 bytes, while input backing is 209,952 bytes, reducing that input's backing by 859,753,440 bytes. This check ran no q9 field, proposal, hierarchy, prediction or GPU workload. New full-process runtime and peak memory after the change remain unmeasured. The NPZ writer still exports logical arrays; compact factor-plus-shape serialization remains unimplemented.

## Workspace correction and current mechanical validation

The former moment_signed_map_array formula aggregated every quadrature node, episode and primitive. The actual field builds signed maps within checkpointed edge chunks, so that aggregate was not a physical workspace lower bound. The corrected moment_signed_map_chunk charge is

$$
2Q\min(E,32)K^2\operatorname{itemsize},
$$

or 13,436,928 bytes for the unchanged N512 profile. Other named entries remain separate array charges, and their sum does not certify process peak. The first admission's measured 2,979,176,448-byte cumulative peak remains a measurement of that earlier implementation; correcting workspace metadata does not revise its observed outcome.

Four new storage tests cover broadcast ownership/caller independence, noncontiguous nonbroadcast fallback, unique shared-backing inventory across groups and a joined transition against dense input. The last compares every returned tensor exactly, unchanged logical charges, reduced input backing and the 4,096-byte signed-map chunk in the tiny two-level fixture. Its 4 by 4 lattice exists because sixteen children are needed to ground two dyadic stages; it supplies no large-network direction or accuracy theorem.

One final CPU invocation of the four new and six affected tests completed ten cases, with zero failures, errors or skips and JUnit time .961 seconds. It used C:/anaconda/python.exe, float64, CPU and one thread. Two Triton discovery warnings concern missing cuobjdump.exe and nvdisasm.exe. The four initial missing-helper/materialization failures and subsequent single chunk-assertion failure remain preserved in separate XML receipts. All three XML files match in both code copies; their counts were read administratively during this ingest, without running tests.

The historical 35-test result and N512 producer/reader evidence remain bound to their original core. The archived retained_reference source is 11,842 bytes with SHA256 d09c305fd0d02c2b82f1eda386d9f69872b9b7bef6f68c4a32ffb617d43f3797; current source is 13,275 bytes with SHA256 f74a8cdade2486c9bfcc88799b1089b5fb5cc20497d05ddf29aa8f3a1aeb5748. The old 45-file packet remains byte-identical in both code copies. Its successful outcome and earlier test pass are historical evidence, not validation of this changed runtime. Current source validation is scoped to the ten cases above.

## Coupled finite full-recognition evolution

The proof compares x=(mu,Sigma,beta,omega_mu,Lambda), including all observed matter/source blocks and all generator episodes, in the full Euclidean/Frobenius product norm. Both sides use the same frozen generative model and exactly retained finite-binary quadrature nodes/weights, Brownian tuples and future readout inputs. Original hard source zeros remain fixed. Fitted beta never substitutes for original future prior pi. No source learning, scientific-control change or autonomous parent update is introduced.

The declared domain is a finite convex compact interior: bounded means, positive lower/upper spectral bounds for Sigma and Lambda, and exactly normalized supported beta rows with a positive floor. The original moment implementation's distinct primitive reversal-pair IDs within each ordered loop and temperature range 0<=theta<1/4 remain hypotheses. Supplied inputs have finite realized ceilings over the chosen finite horizon. Mathematical field/proposal arithmetic is exact; any implementation arithmetic defect is charged separately. Binary row-sum or symmetry discrepancies at initialization belong in the reference transformation, initial error or arithmetic allowance. A floating allclose acceptance does not establish those exact hypotheses. The retained finite rule's mass error remains explicit rather than silently renormalizing its binary weights.

The construction supplies explicit first/second derivative bounds for the implemented inverse-transpose Cholesky reparameterization and noncommuting matrix exponential, then actual record, loop, prior and history-coupling field constants. All receiver and sender contributions stay in the same objective. Their volume, loop and input-radius dependence is explicit and conservative. The synchronous Fisher proposal coefficient K_n preserves the identity contribution once and tends to one as the step tends to zero at fixed driver ceilings; positive-temperature excess can be of order sqrt(h). This is no uniform diffusion-limit or long-horizon strong-error theorem.

For an encoded full state evolved with that same field/proposal and driver, let e_n be coupled parameter error, q_n the quantizer defect and a_n additional arithmetic defect. The source's equations (18)-(19) give

$$
e_{n+1}\le K_ne_n+q_{n+1}+a_{n+1},
$$

$$
e_n\le e_0\prod_{l=0}^{n-1}K_l+
\sum_{j=1}^n(q_j+a_j)\prod_{l=j}^{n-1}K_l.
$$

The original and coded paths use the same actual finite-quadrature field. Population/quadrature discrepancy is therefore a separate target charge. A mirrored dyadic matrix/coordinate grid with exact supported-row normalization preserves symmetry, positivity and original support under the explicit grid restrictions. It gives q<=c_enc gamma. If the original exact-real path has a positive interior clearance and K_n<=K_* over M steps, suitably small initial error and per-step defects imply that coded endpoints and pre-encoding proposals remain inside the domain. Original-path containment is an assumption; coded containment is the conclusion. The partial encoder records a distinct failure outcome if admissibility fails, rather than adding a floor, projection, support repair or different field.

The represented product recognition laws also satisfy the source's directed bound

$$
D(\mathbb Q_x\Vert\mathbb Q_{\widehat x})\le C_{rec}e^2,
$$

with C_rec=max{1/(2a_m),1/(4a_m^2),b_g/2,1/(4a_g^2),1/(2eta)} under the declared matter-covariance, generator-precision and supported-row bounds. This compares two product recognition laws. It neither compares a discrete parameter code with a continuous parameter distribution nor identifies either recognition law with the native correlated posterior.

## Refreshed original-record endpoint and charged precision

Refresh uses the same updated episode-C component identities, normalized masses and standardized readout vectors. Coupled generator error gives both-orientation primitive-map allowance delta_n=exp(X_r)u_r e_n+sigma_n, where sigma_n is an optional additional shared primitive-matrix code error. Inverse reversal uses the same primitive on each side; no independently redrawn copy is introduced.

The endpoint theorem specializes to the inherited fresh baseline a=(.7,-.4), identity matter and independent record-noise covariance, original four-slot pi=1/4, and equal compatible weights in the original hard dyadic hierarchy. With the declared root-path/word caps and smallness conditions delta_n<=1/(2J), A_h delta_n<=1, source equation (23) gives simultaneous physical-tuple/raw-score error at most A_h delta_n and

$$
D(P^{s,Y,O_{all}}\Vert\widehat P^{s,Y,O_{all}})
\le 52553N^7L_r^2\delta_n^2e^{4X_r}R_r^6.
$$

The component identity s and abstract standardized endpoint Y are shared. All original record rows retain their shared fine columns, source labels and fresh baseline. Canonical frames and affine means/offsets remain in the refreshed tuple, with compatible direct/staged cancellation on each side. This is a bound at each separately identified endpoint of the same finite supplied component bank. It is not a continuous-bank approximation theorem, KL of a singular deterministic multidepth window, arbitrary unbounded-context log-score control, or complete two-channel coupling. Independently recursive nonsymmetric charts retain their separate root-relative cocycle obligation.

The sufficient finite-bit construction encodes the complete recognition snapshot. For N512/C3/T4/A4 it counts 97,280 full scalar entries; generator parameters alone have 160N entries. With gamma=2^-p, one snapshot has upper charge P_rec[1+ceil(log2(B/gamma+2))]+2floor(log2(p+1))+1 bits. A sufficient conservative uniform choice includes p>=ceil(log2(2M c_enc K_*^M/epsilon)), together with the grid restrictions and its own initial allowance. This is an upper construction, not a necessity/lower-bound or useful storage estimate.

Frozen model, source/graph/loop IDs, normalization data, observed offsets, controls/caps, exact binary input factors/shape and shared component identities remain additional charged data. A replay archive retains its full Brownian/readout stream. Old replay/new state, direction, hierarchy/copy/frame outputs and decoder arrays stay charged when materialized. Matrix exponentials, contractions, Cholesky/inverse/SPD roots and requested decoding incur workspace and time. Optional primitive group-code bits add their source charge. The derivation supplies no packing or certified arithmetic implementation, and the old group codec alone cannot run recognition inference because it lacks the complete state and a canonical generator logarithm.

## Actual-law admission remains open

The next quantitative obligation is a useful coupled amplification-and-exit budget under the actual intended evolving law. Source equation (26) charges the compact/input/smallness event's complement with its full probability and integrates the conditional endpoint-TV bound on the event:

$$
\Pr(\mathcal G^c)+\mathbb E\left[\mathbf1_{\mathcal G}
\min\left(1,\sqrt{\tfrac12 52553N^7L_r^2e^{4X_r}R_r^6}\delta_n\right)\right].
$$

This budget is unevaluated and not proved useful. Gaussian drivers supply no deterministic input cap uniform in volume/horizon, and the explicit conservative constants do not admit native compact survival. Failure mass stays charged on a common record-plus-failure outcome space. Small exit probability alone also cannot control accumulated unbounded record log loss. A T=0 population energy theorem does not give positive-temperature finite-q containment.

Useful full precision/storage, computed arithmetic, continuous population/quadrature transfer, native correlated-posterior accuracy, complete second-channel and cross-morphism coupling, recursive-chart error, compatible growing identified laws and persistent endogenous formation remain open. Another supplied-hierarchy-only precision refinement does not settle the actual-law admission. All four gates remain open and the roughly 65% planning estimate is unchanged. No scientific control, model, active configuration, runtime default, host setting, base transport or manuscript changed.

## Published bindings and research continuity

| Published item | Bytes | SHA256 |
|---|---:|---|
| latent_retained_reference.py | 13275 | f74a8cdade2486c9bfcc88799b1089b5fb5cc20497d05ddf29aa8f3a1aeb5748 |
| test_gaussian_latent_retained_storage.py | 4526 | 0254e3cf24cf1c0489a25bb1b249bea6fc7ab02eb98df8c9f0d701a379d3dedc |
| R2-OWNED-INPUT-STORAGE.md | 4727 | 18e546ee1897faeb0428f1e359163c95a2bba03f95faad879c2087dd329d560d |
| R2-RETAINED-UPDATE-ERROR.md | 33985 | 4cf7dc6c05dfd119fc88ebb8984d99a9ec14dd3d736d834992c1a2f12e565acc |
| r2-owned-storage-tests-20261009.json | 4862 | 9551b987b9c5b424512fcf3c33a3ad70a792b64161a7b20c164da736e80616db |
| r2-owned-storage-input-20261009.json | 1079 | f3493fbfff1ea18206f4e6fc2f49fac9afa3c474f1123ce47cde8321c325e02a |
| r2-retained-storage-red-20261009.xml | 4647 | 27041360bbb8e0c04ebbacb6159d78ee38534a146705cde5e007920d4fe787b3 |
| r2-retained-storage-chunk-red-20261009.xml | 1662 | 80ca006e9b8f4242754b638d54aec5281f70bc12332d22c6164569612156fb77 |
| r2-retained-storage-tests-20261009.xml | 1748 | e04805a543ddfa64f312b38a75f0616c5195f06d813ae9c085121d66f29cc2b6 |
| evidence/r2-owned-storage-source-intake-20261009.json | 9444 | ed3019b498966bc8a4c4d2467e7707d922e6d7d53aa1969ad74c36d265b88fee |

The exact source intake binds 37 repository paths, three live theory sources and one dated theme context. Live SPEC learning/scope conventions, c10's complete levelwise state and cross-morphism defects, and c12's common structural channel remain prior context rather than certification of the new construction. Their bytes match the intake and remain unchanged. The consulted theme is as of Research b9d3cfe306cffbbe04fd05bece4a835c9f8c1f27, 130827 bytes, SHA256 2c3c1954f65d118b37333f55b9ec0cc9cbd7968b9580f2a963f8edd7b34e5f88; this later ingest updates its synthesis.

Before vault mutation, actual canonical Code main, HEAD and origin/main agreed at f7dd9f512feb214cac9ca6ec9a9e01f7903a7f8f. Completed artifacts/r2-owned-storage-handoff-20261009.json has SHA256 2dd80af830ebd7801e87d407a9901cf422bd5f06ec6515b9852ce67feab7cd79 in both code copies. All three current XML receipts and the historical complete packet retain exact canonical parity. Administrative preservation evidence remains separate from test coverage and mathematical assumptions.

This develops [[Staged hierarchy formation and RG composability]], [[multiagentelbo-2026-10-09-retained-admission]], [[multiagentelbo-2026-10-09-retained-reference]] and [[multiagentelbo-2026-10-09-hierarchy-codec]]. Only this new immutable source and the existing theme/root index/append-only log change. All 30 prior October 9 immutable notes, twelve prior postflight receipts, seven unique live source bindings and weekly-report WIP are preserved. This ingest replays no field or test and performs no new scientific investigation. Concurrent uncommitted Code research is outside this published checkpoint.
