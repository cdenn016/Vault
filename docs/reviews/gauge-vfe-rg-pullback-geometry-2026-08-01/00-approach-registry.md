# Approach registry: pullback geometry and timeless inference

Date: 2026-08-01
Artifact: `manuscripts/gauge_vfe_rg`
Status vocabulary: `SURVIVES`, `REPAIRED`, `REJECTED`, `OPEN`

This registry records genuinely different construction families considered during the investigation.  It is organized by mathematical mechanism rather than by investigator.  A family survives only when it supplies typed maps and explicit equations; aesthetic similarity or agreement among reviewers is not evidence.

| Family | Core mechanism | Load-bearing question | Current disposition |
|---|---|---|---|
| Associated-bundle vertical geometry | Use the connection-induced projection `ver^omega` to turn the first jet of a section into a vertical tangent vector, then contract with fiberwise Fisher and Amari tensors. | Can a fiber tensor act on the derivative of a section without identifying different fibers? | `SURVIVES`: the covariant vertical first jet provides the missing typing. |
| Ordinary pullback through a local representative | Differentiate a coordinate representative of the section and pull back the coordinate Fisher matrix directly. | Is the result independent of a position-dependent gauge change? | `REJECTED`: a nonconstant passive gauge transformation creates an inhomogeneous derivative term. |
| Connection-independent perceived geometry | Seek a tensor on the base determined only by the principal bundle, statistical fibers, and section. | Do two choices of connection produce the same tensor? | `REJECTED`: the exact connection-change formula has linear and quadratic correction terms; a Gaussian-location example separates the results. |
| Rank/quotient reduction | Treat the radical of the induced Fisher semimetric as unperceived base directions and pass to a quotient. | Does constant rank alone produce a quotient manifold? | `REPAIRED`: it produces a quotient vector bundle; a quotient manifold additionally needs involutivity, a sufficiently regular leaf space, and basicness. |
| Divergence-jet construction | Recover Fisher, dual connections, and the Amari tensor from second and third jets of a divergence after parallel transport. | Can informational tensors be defined by local comparison without confusing points in different fibers? | `SURVIVES` under smoothness and transport hypotheses. |
| Oriented-orbit inference | Quotient regular natural-gradient curves by orientation-preserving reparameterizations. | Can VFE define change without a primitive time coordinate? | `SURVIVES` once a metric or mobility selects the vector-field ray; VFE decrease alone does not select an orbit. |
| Fisher arclength clock | Integrate the configuration Fisher line element along an already selected oriented orbit. | Is the resulting duration invariant under the disposable curve parameter? | `SURVIVES` on regular non-null segments; it is an agent-relative information length, not a derivation of physical time. |
| VFE value as a clock | Use strict monotonicity of free energy itself to order a history. | Is `-F` a global clock? | `REPAIRED`: it is a local relational clock only on strict-descent segments and fails at critical points, plateaus, and nonmonotone updates. |
| Global orthogonal synchronization | Integrate the normalized one-form `-dF/||grad F||` on configuration space. | Does a single unit-speed clock exist across all histories? | `OPEN` in general: local closedness and global vanishing periods are additional integrability conditions. |
| Markov operational geometry | Push a parameter-independent observation/record channel forward and identify the coarse score with a conditional expectation. | Does interaction-accessible information contract? | `SURVIVES`: the loss is the expected conditional score covariance and is positive semidefinite. |
| Deterministic coarse restriction as information loss | Apply the Markov contraction theorem to a Galerkin restriction or fitted parameter-dependent map. | Are all coarse maps Fisher contractions? | `REJECTED`: the theorem is specific to normalized parameter-independent statistical channels. |
| Cross-scale first-jet naturality | Relate fine and meta sections through a bundle morphism and compare their covariant vertical first jets. | When does a meta-agent inherit the fine perceived geometry? | `SURVIVES` with section descent and connection compatibility; otherwise an explicit vertical mismatch term remains. |
| Independent fine/meta flows | Compare the lengths of separately recomputed natural-gradient trajectories after coarse-graining. | Does metric contraction alone imply trajectory contraction? | `REJECTED`: contraction concerns the image of the same path; independently generated flows require oriented semiconjugacy. |
| RG of perceived geometry | Transport levelwise tensors to a declared reference space before differencing or differentiating them. | Can tensors on different bases be subtracted canonically? | `SURVIVES` only with the reference identifications already required by the general RG theory; RG depth is scale, not inference duration. |

## Portfolio control

The connection/vertical-jet route, the parameter-free orbit route, and the operational Markov route were kept independent through their initial derivations.  Cross-pollination occurred only after each route exposed its own obstruction: connection dependence, mobility dependence, and channel dependence respectively.  The quotient/foliation and global-clock families remained adversarial rather than being absorbed into the main construction.  Their counterexamples now delimit the exact theorem statements.

## Closure target

The construction is complete only when the manuscript contains: (1) the global covariant pullback tensors and their connection-change law; (2) the vertical/horizontal/mixed/section-history taxonomy; (3) a parameter-free VFE orbit and Fisher-length construction; (4) meta-agent first-jet naturality and Markov information defects; (5) explicit rank, foliation, mobility, synchronization, and semiconjugacy boundaries; and (6) a clean manuscript build plus an evidence-gated mathematical ledger.
