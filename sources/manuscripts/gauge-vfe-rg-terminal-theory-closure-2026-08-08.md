---
type: manuscript
title: "Gauge-Covariant Variational Free Energy and Renormalization: 2026-08-08 Terminal Theory Closure Record"
aliases:
  - "Gauge VFE RG terminal theory closure"
  - "Finite conditional gauge VFE RG closure"
authors:
  - Robert C. Dennis
year: 2026
status: in preparation
tags:
  - cluster/vfe
  - cluster/multi-agent
  - cluster/gauge-theory
  - cluster/info-geometry
  - project/multi-agent
  - project/transformer
  - field/mathematics
  - field/statistics
  - field/cs-ml
  - field/physics
created: 2026-08-08
updated: 2026-08-08
---

# Gauge-Covariant Variational Free Energy and Renormalization: 2026-08-08 Terminal Theory Closure Record

## Scope and provenance

This immutable record banks the terminal adjudication of the manuscript *Gauge-Covariant
Variational Free Energy and Renormalization*. The released repository state is commit
`69f7b06c531cef9eafe613851eeedfdb8f83df04` with contract digest
`b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b`. That commit contains
the terminal theorem, reconstructions, adjudication, and release records. The manuscript source
used for the clean build was fixed at `28f66d63aff177d6ff9326796a485dff7afc8b8d`; its build,
PDF, pullback, and visual evidence was archived at
`14551bb8d463f229a3b451d7222042d134c2c52d`. Task 15 then adjudicated that unchanged source.

The governing records are
`docs/derivations/2026-08-03-gauge-vfe-rg-remediation/construction-or-strongest-theorem.md`,
`final-report.md`, and `release.json`. The release state is `COMPLETE_AFFIRMATIVE`: all 73
atomic claims are `EVIDENCE_VERIFIED`, with no unresolved obligation inside the frozen target.
This is authoritative for the current terminal status and the later refined formulations. It
preserves [[gauge-vfe-rg-pullback-geometry-2026-08-01]] as provenance for its own snapshot.

## Strongest verified result

For every admitted finite standard-Borel agent network and every finite composable sequence of
admitted scale arrows, the manuscript supplies a complete conditional VFE/ELBO and
gauge-covariant effective-scale theory. "Conditional" is load-bearing: the theorem assumes the
declared normalized Markov channels, reference measures, product-reference equivalences,
bundle and configuration maps, recognition lifts, smoothness and integrability conditions,
related sections, and comparison isomorphisms that type each construction.

### Measure pairs, DQM, and Fisher contraction

A normalized parameter-independent Markov channel pushes the reference and likelihood measures
together, preserves their finite evidence mass, and induces the exact coarse action by a
conditional log-Laplace transform. For a differentiable-in-quadratic-mean (DQM) model, including
the stated nondominated singular remainder, the coarse score is conditional expectation,

$$
\ell^{\mathrm c}(Z)=\mathbb E[\ell(Y)\mid Z],
$$

and the Fisher-information loss is the conditional score covariance,

$$
I-I^{\mathrm c}
=\mathbb E\!\left[\operatorname{Cov}(\ell(Y)\mid Z)\right]
\succeq0.
$$

Equality is score recoverability at that parameter, not automatic recovery of the whole
statistical experiment.

### Local agents, blocks, and collective VFE

The local VFE of one agent is the singleton case of an exact conditional block VFE, while every
nonempty block can be treated as a meta-agent coordinate. With finite posterior KL and a shared
outside marginal, the collective-VFE difference is exactly the outside expectation of the
block-VFE difference. Local objectives are therefore coordinate restrictions of one joint VFE;
they are not independently additive potentials. A displayed marginal still does not determine
its joint-law lift or Fisher metric, so an exact recognition lift remains application data.

Every normalized standard-Borel observation kernel also has an equivalent environment-node
message realization. This is an operational redescription: the realized message remains the
conditioning record, and the theorem does not confer biological agency or erase observations.

### Exact finite interaction and scale theory

At each admitted product-reference scale, the complete nonempty-subset Hoeffding interaction
family is exactly isomorphic to bounded actions modulo constants. Exact coarse graining closes in
that full finite space. A retained pairwise or sparse ansatz instead carries an explicit residual,
which vanishes exactly when its retained image is invariant. Posterior disintegrations provide
typed fine/coarse bridge kernels; aggregation and prolongation form typed sandwich operators;
and attention coarsens associatively only at the normalized measurable marked-event-law level
before row normalization.

The exact nonlinear derivatives form an ordered nonautonomous cocycle. Generalized modes are
scale-indexed lines rather than eigenvectors of an unspecified common operator. Beta data and
reference fixed objects become meaningful only after declared comparison isomorphisms; retained
beta differs from exact beta by the transported residual. Periodic schemes may instead carry
monodromy fixed objects and cycles.

### Pullback geometry, anomalies, and information duration

A section and selected connection pull the fiber Fisher tensor back to a passive-gauge-invariant,
connection-relative base semimetric. A scale morphism obeys the exact covariant-jet chain rule

$$
D^{\bar\omega}\bar s\circ Tf
=T^V\Psi\circ D^\omega s+A_{\Psi,s}.
$$

The vertical Fisher defects form an unconditional cocycle. A clean positive base pullback follows
only when the horizontal anomaly vanishes; otherwise the exact base comparison contains the
corresponding cross and quadratic anomaly terms. Fixed-fiber, total-space, base, section, and
configuration histories remain distinct.

After a regular VFE history and metric have been selected, Fisher arc length supplies an
agent-relative information duration. It is path- and metric-dependent, can fail as a coordinate
where speed vanishes, and is not primitive physical time or a global synchronized clock.

## Evidence and document state

The ordinary private-research closure records:

- 73 of 73 ledger claims `EVIDENCE_VERIFIED`;
- 420 tests with zero failures, errors, or skips in the machine-readable JUnit record;
- 30 numerical checks plus the source-inventory check, all passing;
- all 3,138 scheduled factorization-gap stress cases passing with zero failures;
- PB-1 through PB-4 `EVIDENCE_VERIFIED`;
- a fresh four-pass TeX/BibTeX build producing a 300-page PDF with resolved references and
  citations; and
- visual inspection of every changed page and mapped neighbor, with an additional pass over the
  high-risk subset and no observed rendering defect.

The built artifact is
`docs/derivations/2026-08-03-gauge-vfe-rg-remediation/evidence/task-14-main.pdf`
(1,847,095 bytes; SHA-256
`fc4f111131ef39bf18762784f1ce80336304415db0adddc6b41744e3544ffd3d`). The tests and
numerical protocols support implementation and document integrity; the mathematical claims close
through the written derivations and stated falsification boundaries, not by numerical agreement.

## Exact boundary

The result does **not** establish automatic pairwise or sparse closure, automatic existence of
principal scale maps or configuration maps, a canonical coarse configuration dynamics, automatic
semiconjugacy of independently optimized flows, a scheme-independent finite beta component,
physical time, a global clock, nonlinear Gaussian attraction, a thermodynamic or infinite-volume
limit, critical universality, or universal exponents. It also does not certify that the legacy
MAgent barycenter, KL-proximity blocking, fitted eight-coupling pipeline, or VFE Transformer runtime
satisfies the theorem's application hypotheses.

Application to a concrete model must still supply or verify its principal scale maps, target
product references, exact recognition lifts, configuration manifolds and coarse maps, related
sections, objective and metric compatibility, comparison scheme, and any claimed natural-gradient
semiconjugacy.

## Relevance to this research

This closure supplies the finite mathematical backbone shared by the
[[Gauge-Theoretic Multi-Agent VFE Model]] and the [[VFE Transformer Program]]. It separates exact
effective theory from retained truncations, makes Fisher loss and cross-scale geometric anomalies
explicit, and identifies the data required to turn the abstract construction into a concrete
meta-agent or transformer coarse-graining. The next scientific step is therefore a small explicit
finite instantiation, not another general proof audit.

## Related

[[Renormalization-group flow of beliefs]] · [[Meta-agents and hierarchical emergence]] ·
[[Multi-agent variational free energy]] · [[Fisher information metric]] ·
[[Information geometry and natural gradient]] ·
[[Agents as fibre-bundle sections|Agents as fiber-bundle sections]] ·
[[Coarse Graining]] · [[Natural gradient]]

## Repository records

- `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/final-report.md`
- `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/release.json`
- `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/construction-or-strongest-theorem.md`
- `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/evidence/task-13-manifest-verification.json`
- `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/evidence/task-14-build-audit.json`
- `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/evidence/task-14-visual-audit.json`
