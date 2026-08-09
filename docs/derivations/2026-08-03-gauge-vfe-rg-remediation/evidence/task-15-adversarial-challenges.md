<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 15 adversarial challenge record

## Frozen target

The challenged result is the conditional finite-network theorem in
`construction-or-strongest-theorem.md`, SHA-256
`d340dad09cd24fe912dd2f0d3ffda8f33ef98d62bc2dad1f05c4cf03c08999a2`.
It quantifies over arbitrary finite standard-Borel networks and finite
composable scale sequences satisfying the hypotheses declared at the tier
where each conclusion is used. It does not claim automatic scale maps,
automatic target product equivalence, sparse closure, physical time,
universality, or an infinite-volume limit.

The independent skeptic artifact is SHA-256
`77d02e1b143cda0675b045cd77193d5d3369936361f0e8eda68994486dc02e21`.
The defender re-read the final theorem and froze at SHA-256
`0bde9710dd213430b7c0b6562a5059571873386a68cf82649f74c15524977a55`.
Dispositions below are based on the displayed derivations and stated
hypotheses, not on agreement between agents.

## Mathematical challenges

| ID | Challenge | Final disposition |
|---|---|---|
| S15-A1 | Coarse ELBO monotonicity or fixed evidence can fail if different or nonnormalized channels are used. | `REJECTED`: the theorem uses one common normalized parameter-independent channel and carries the finite-KL equality guard. |
| S15-A2 | Local block objectives need not determine the collective ELBO, and observation internalization could erase conditioning. | `REJECTED`: the local identity compares finite-KL laws with one outside marginal, and randomization preserves the observation random variable and sigma-algebra. |
| S15-A3 | A channel need not preserve equivalence to a product reference. | `REJECTED` as a target counterexample: target-scale product equivalence is a separately declared premise. The challenge remains a valid boundary against automatic preservation. |
| S15-A4 | Full finite interactions might be mistaken for a dimension-free finite-parameter or sparse ansatz. | `REJECTED`: exactness retains all nonempty finite subsets and explicitly excludes automatic sparse or finite-parameter closure. |
| S15-A5 | A marked attention array can be nonmeasurable. | `REJECTED` against the final theorem, which requires a normalized measurable joint marked event law. A minor shorthand omission in one source paragraph is recorded but does not reach the complete theorem. |
| S15-A6 | A parameter-dependent channel can create Fisher information and invalidate score contraction. | `REJECTED`: parameter independence is an explicit hypothesis and the Le Cam singular remainder is carried through the channel. |
| S15-A7 | Principal scale maps, descended sections, or configuration manifolds need not exist. | `REJECTED`: these objects are supplied hypotheses where used; the theorem makes no automatic-existence claim. |
| S15-A8 | Horizontal anomalies might compose without transport, or composite zero might force factorwise zero. | `REJECTED`: the ordered transported anomaly and Fisher-defect cocycles are typed explicitly, and factorwise necessity is not claimed. |
| S15-A9 | Equal objectives might fail to semiconjugate natural-gradient histories. | `REJECTED`: the theorem requires the exact positive-ray vector-field relation or stronger sufficient metric hypotheses; objective equality alone is explicitly insufficient. |
| S15-A10 | Finite blocking might not determine canonical beta functions, fixed objects, universality, or an infinite-volume theory. | `REJECTED` as a target counterexample: comparison data are declared, fixedness is tier specific, and all universal or limiting strengthenings are excluded. |

No Critical or High mathematical counterexample survives the admitted
hypotheses. The challenges do establish sharp boundaries: weakening the
common-channel, product-reference, measurability, parameter-independence,
existence, metric-compatibility, or comparison-space premises can falsify the
corresponding conclusion.

## Operational challenges

The six document and numerical claims use ordinary private-research
reproducibility evidence. An independent read-only replay of those artifacts
is recorded in `evidence/task-15-operational-evidence.md`, SHA-256
`e3257f9ee70779f85dfe333326f5a47605a37b3502f70c5bbc7bbb0bd5c3d7a2`.

| Claim | Current evidence | Final disposition |
|---|---|---|
| `pullback-ledger-provenance` | Task 13 pullback validation `32eff6669c5223cfea72089c0f143fe4aaa506b249ce0abf5f4114bc83c65c58`; Task 14 pullback ledger `54d58f9c61b0b2bbe5d4d7a9d641062a35a8832ce95cb46b3f24faa091697b18`. | `REJECTED`: PB-1 through PB-4 are current and verified. |
| `determinant-gap-stability` | Task 13 manifest/numerical record `0ea14d2e872c22459c83f496146b9a79f4cb372c72e5a748ec351230fd36dbe4`. | `REJECTED`: all 3,138 scheduled cases passed with zero failures. |
| `manifest-fail-closed` | The same Task 13 record binds the current source inventory and all thirty numerical checks. | `REJECTED`: ordinary update/verify checks detect changed governed inputs and accept the current bound result. |
| `minor-emergent-time-keyword` | Task 14 visual audit `75ce1c4d66575e7d923c22c4052692bd961cd14b79cd174d0edcd75a4822adb8`. | `REJECTED`: rendered metadata and physical-time disclaimers are reconciled. |
| `minor-status-unbreakable` | The same Task 14 visual audit inspected the rendered status layout. | `REJECTED`: no status token is broken across lines. |
| `minor-generated-aux` | Task 14 build audit `e7376eba240444a35b33e6182373cd5d7de8bf637bea039f505d7d76f0ed1e4d`. | `REJECTED`: the four-pass build used fresh generated auxiliaries and reports no stale tracked auxiliary influence. |

## Binding verdict and falsification conditions

The conditional finite mathematical target and its six downstream operational
ancestors are `EVIDENCE_VERIFIED`. This record would be falsified by an
admitted finite typed counterexample; a failed displayed equality under its
stated hypotheses; a mismatch in a cited current artifact; a determinant-gap
case outside its stated tolerance; a broken rendered status; an unreconciled
physical-time keyword; or evidence that a stale auxiliary affected the bound
PDF. None is present in the current artifacts.
