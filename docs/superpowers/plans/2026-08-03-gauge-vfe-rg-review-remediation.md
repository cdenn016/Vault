# Gauge-VFE RG Review Remediation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the manuscript's incomplete cross-scale theory with a fully typed, gauge-covariant effective VFE/RG construction for arbitrary finite standard-Borel agent networks; prove the exact law, action, interaction, Fisher, generalized-mode, fixed-object, beta-function, and timeless-history results; repair every referee finding; and publish source, evidence, closure, and wiki revisions whose claims are independently reconstructible and mechanically bound to the exact released source.

**Architecture:** The repair separates three compatible but noninterchangeable levels. Exact Markov pushforward acts nonlinearly on normalized laws. Its local action derivative is reverse-kernel conditional expectation and contracts canonical normalized `L^p`/Fisher tangents. Exact finite-network interactions are assembled in a full power-set Hoeffding space, transported through the coarse action, extracted modulo constants, and optionally projected with an explicit residual; this extensive operator supports relevant, marginal, and irrelevant generalized modes without contradicting Fisher contraction. A source/evidence/closure/wiki (`S/E/C/W`) lifecycle binds the derivation, numerical stress tests, TeX build, independent reconstruction, and research-vault synthesis without self-reference.

**Tech Stack:** LaTeX with `pdflatex` and BibTeX, finite standard-Borel probability and Banach-space operator theory, information geometry, Gaussian/Hermite score calculus, Python 3.14 with NumPy/SciPy/mpmath/pytest, JSON Schema, PowerShell, Poppler PDF tools, the rigorous-theory-search and verification ledgers, the Research-vault linter, and Git in an isolated worktree.

**Required skills:** Use `rigorous-theory-search` for Tasks 1, 5--10, 15, and 17; `verification` for Tasks 3, 4, 13--18; `research-wiki` for Task 18; `tikz` if an existing figure must be materially redrawn in Task 12; `pdf` for Task 14; and `superpowers:verification-before-completion` for Task 19. Use `superpowers:subagent-driven-development` for execution, with a fresh implementer and an adversarial reviewer for each load-bearing task.

## Global Constraints

- Work only in `C:\tmp\Research-gauge-vfe-rg-review-remediation-20260803` on branch `codex/gauge-vfe-rg-review-remediation-20260803`; preserve every byte of the dirty live checkout at `C:\Users\chris and christine\Desktop\Research` until the final protected-WIP synchronization gate.
- Treat `docs/superpowers/specs/2026-08-03-gauge-vfe-rg-review-remediation-design.md` as the approved contract. A change to its mathematical types or release semantics requires a recorded amendment before implementation.
- The affirmative-existence instruction is a search prior labeled `SEARCH_PRIOR_AFFIRMATIVE`, never evidence. Every positive mathematical claim closes only by a derivation or proof; numerical checks corroborate finite endpoints but do not prove theorems.
- “General network” means every finite standard-Borel product network of arbitrary, unbounded finite cardinality and every admitted finite blocking channel. No fixed-size enumeration closes that quantifier. Countably infinite and thermodynamic-limit universality remain explicitly outside the proved theorem unless separate summability and convergence hypotheses are added and proved.
- Keep normalized law/action tangents distinct from extensive interaction coordinates. Do not infer the absence of relevant interaction modes from `L^p` or Fisher contraction.
- Keep exact interaction closure distinct from a retained projection. Every projected flow carries the quotient residual norm, and no projected beta function is called exact without invariant-subspace proof.
- Keep scale depth, an oriented unparameterized inference-orbit coordinate, Fisher duration, and physical time distinct. Do not introduce an external time variable.
- Preserve the bundle ontology: a principal bundle with group `G`, two associated statistical fibers for beliefs and models, section-valued agents, declared gauge transformations, and typed cross-scale maps.
- Use American English in all new prose. Define every symbol before use, punctuate display equations, and attach claim statuses at theorem/definition scope rather than stacking multiple tags in one heading.
- Cite primary literature or authoritative monographs for external mathematics. The manuscript and project wiki may document the construction but are not independent authority for it.
- Run all non-Torch Python work with `C:\Python314\python.exe`. No CUDA claim is part of this task.
- Use `apply_patch` for hand edits. Do not modify generated evidence after source revision `S`; any source, bibliography, test, verifier, or build-logic change after `S` creates a new `S` and invalidates downstream evidence.
- The release order is strict: source `S`, evidence `E`, closure `C`, wiki `W`, then an uncommitted active `.verification/ledger.json` bound to the exact published revision. Preserve the final ledger-bearing worktree through the final report.
- Commit only task-owned changes. Before each commit run `git diff --check`, inspect `git status --short`, and stage explicit paths.

---

## File and Interface Map

Primary manuscript inputs to modify:

- `manuscripts/gauge_vfe_rg/main.tex`
- `manuscripts/gauge_vfe_rg/01_introduction.tex`
- `manuscripts/gauge_vfe_rg/02_geometry.tex`
- `manuscripts/gauge_vfe_rg/03_probability.tex`
- `manuscripts/gauge_vfe_rg/04_generative.tex`
- `manuscripts/gauge_vfe_rg/05_elbo.tex`
- `manuscripts/gauge_vfe_rg/05a_expfamily.tex`
- `manuscripts/gauge_vfe_rg/05b_local_collective_elbo.tex`
- `manuscripts/gauge_vfe_rg/05c_pullback_geometry.tex`
- `manuscripts/gauge_vfe_rg/05d_relational_inference.tex`
- `manuscripts/gauge_vfe_rg/06_general_coarsegraining.tex`
- `manuscripts/gauge_vfe_rg/06_gaussian.tex`
- `manuscripts/gauge_vfe_rg/06a_generative_gaussian.tex`
- `manuscripts/gauge_vfe_rg/07_general_renormalization.tex`
- `manuscripts/gauge_vfe_rg/07_restrictions.tex`
- `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex`
- `manuscripts/gauge_vfe_rg/08_infogeometry.tex`
- `manuscripts/gauge_vfe_rg/09_coarsegraining.tex`
- `manuscripts/gauge_vfe_rg/10_renormalization.tex`
- `manuscripts/gauge_vfe_rg/11_obstructions.tex`
- `manuscripts/gauge_vfe_rg/12_philosophy.tex`
- `manuscripts/gauge_vfe_rg/appendix_notation.tex`
- `manuscripts/gauge_vfe_rg/appendix_claim_ledger.tex`
- `manuscripts/gauge_vfe_rg/appendix_numerical_provenance.tex`
- `manuscripts/gauge_vfe_rg/SPEC.md`
- `manuscripts/references.bib`

Verification/build inputs to create or modify:

- `manuscripts/gauge_vfe_rg/verification/run_checks.py`
- `manuscripts/gauge_vfe_rg/verification/claims.json`
- `manuscripts/gauge_vfe_rg/verification/requirements.txt`
- `manuscripts/gauge_vfe_rg/verification/VERIFICATION.md`
- `manuscripts/gauge_vfe_rg/verification/result.schema.json`
- `manuscripts/gauge_vfe_rg/verification/manifest-policy.json`
- `manuscripts/gauge_vfe_rg/verification/lifecycle_gate.py`
- `manuscripts/gauge_vfe_rg/verification/build_audit.py`
- `manuscripts/gauge_vfe_rg/verification/tests/test_factorization_gap.py`
- `manuscripts/gauge_vfe_rg/verification/tests/test_runner_cli.py`
- `manuscripts/gauge_vfe_rg/verification/tests/test_manifest_binding.py`
- `manuscripts/gauge_vfe_rg/verification/tests/test_lifecycle_gate.py`
- `manuscripts/gauge_vfe_rg/verification/tests/test_build_audit.py`
- `manuscripts/gauge_vfe_rg/build.ps1`

Durable proof/evidence directory:

- `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/problem-contract.json`
- `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/approach-registry.json`
- `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/claim-ledger.json`
- `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/dependency-dag.json`
- `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/counterexample-register.md`
- `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/construction-or-strongest-theorem.md`
- `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/adversarial-report.json`
- `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/release.json`
- `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/final-report.md`
- Evidence subrecords under `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/evidence/` for each proof, test, build, reconstruction, and source mapping.

Authorized wiki revision `W`:

- Create `sources/manuscripts/gauge-vfe-rg-cross-scale-operator-theory-2026-08-03.md`.
- Modify `wiki/projects/Gauge-Theoretic Multi-Agent VFE Model.md`.
- Modify `wiki/concepts/Coarse Graining.md`.
- Modify `wiki/concepts/Renormalization group flow.md`.
- Modify `wiki/concepts/Renormalization-group flow of beliefs.md`.
- Modify `index.md` and append to `log.md`.

---

### Task 1: Freeze the Proof Contract and Open a Diverse Search Portfolio

**Files:** Create the nine rigorous-theory-search artifacts and `evidence/` directory listed above.

**Interfaces:** Consumes the approved design and referee report; produces a canonical claim inventory, typed dependency DAG, approach-family registry, falsifiers, and release gates used by all later agents.

- [x] **Step 1: Create `problem-contract.json` with exact quantifiers and types.** Record arbitrary finite standard-Borel networks, measure pairs, positive Markov kernels, action quotient spaces, full interaction spaces, selected projections, gauge data, score tangents, configuration manifolds, and the `SEARCH_PRIOR_AFFIRMATIVE` label. Record countably infinite networks, thermodynamic limits, physical time, and unproved universality as exclusions.
- [x] **Step 2: Create one claim-ledger entry per theorem or correction.** Include stable IDs for measure/action map, derivative, `L^p` contraction, Fisher defect, Dobrushin criterion, essential spectrum, circle norm witness, Hoeffding inverse theorem, exact/projected interactions, score lift, Hermite spectrum, generalized modes, cocycle, beta functions, fixed objects, pullback compatibility, history semiconjugacy, extended ELBO, probability hypotheses, gauge laws, Gaussian positivity, and all referee minor repairs.
- [x] **Step 3: Encode the proof-obligation DAG.** Every conclusion must list its exact hypotheses and parent claims; no compatibility edge may be dismissed without proof.
- [x] **Step 4: Register genuinely distinct approach families.** Start at least normalized action quotients, full Hoeffding interactions, weighted action spaces, score/DQM tangents, Gaussian/Hermite spectral realization, transfer-operator/cocycle formulations, category/diagram type checking, and counterexample/falsifier search. Mark weighted-one-space unification as a competing route, not the favored answer.
- [x] **Step 5: Dispatch independent mechanism-diverse theorem agents and adversarial agents.** Require each return to contain concrete lemmas/equations or a falsifying example. Record convergence by mathematical family and redirect duplicate approaches to underexplored families.
- [x] **Step 6: Validate artifact structure and commit.** Run:

```powershell
& "C:\Python314\python.exe" -m json.tool docs\derivations\2026-08-03-gauge-vfe-rg-remediation\problem-contract.json > $null
& "C:\Python314\python.exe" -m json.tool docs\derivations\2026-08-03-gauge-vfe-rg-remediation\claim-ledger.json > $null
& "C:\Python314\python.exe" -m json.tool docs\derivations\2026-08-03-gauge-vfe-rg-remediation\dependency-dag.json > $null
rg -n "[T]ODO|[T]BD|[r]outine|[o]bvious" docs\derivations\2026-08-03-gauge-vfe-rg-remediation
```

Expected: all JSON parses; the final search returns no placeholders or unsupported proof shortcuts. Commit `docs: open gauge VFE RG proof portfolio`.

### Task 2: Add Verification Tests That Initially Fail

**Files:** Create all five `verification/tests/test_*.py` files; modify `verification/requirements.txt`.

**Interfaces:** Consumes the approved verifier contract; produces deterministic red tests for stable determinants, fail-closed CLI behavior, manifest coverage, lifecycle purity, and build auditing.

- [x] **Step 1: Pin every dependency the protocol actually uses.** Record the
  exact authenticated versions of `numpy`, `scipy`, `sympy`, `mpmath`,
  `pypdf`, and `pytest` with strict `name==version` requirements; require each
  declared distribution to be present with exact-one authenticated provenance
  and the identical metadata version in production.  Do not declare the
  absent and unused `jsonschema` package merely because the verifier consumes
  a JSON Schema document: the protocol's strict validator is self-contained.
- [x] **Step 2: Encode scalar and high-condition determinant witnesses.** Include this exact scalar oracle:

```python
@pytest.mark.parametrize("epsilon", [1e-3, 1e-6, 1e-9])
def test_scalar_gap_uses_log1p(epsilon):
    lam = np.array([[1.0, epsilon], [epsilon, 1.0]])
    got = factorization_gap(lam, [[0], [1]])
    want = -0.5 * math.log1p(-(epsilon * epsilon))
    assert got.value == pytest.approx(want, rel=5e-12, abs=0.0)
```

- [x] **Step 3: Freeze a deterministic 3,138-draw replacement protocol.** Cover dimensions 2--16, condition numbers through `1e14`, exact block-diagonal, near-decoupled, scale, permutation, nested-refinement, and selected 100-digit mpmath controls; name it as a new protocol rather than a reproduction of a lost historical generator.
- [x] **Step 4: Encode CLI and manifest mutation tests.** Parameterize TeX, `SPEC.md`, bibliography, style, build script, claim map, runner, requirements, schema, policy, lifecycle code, build audit, and tests. Assert malformed JSON, missing/extra fields and paths, line-ending changes, semantic changes, unknown/duplicate checks, revision mismatch, NaN, and infinity all fail.
- [x] **Step 5: Prove verify-mode immutability in tests.** Hash the result before and after every passing and failing invocation; assert neither mode and both modes fail, update writes atomically, and verify writes only an explicitly separate report.
- [x] **Step 6: Encode `S/E/C/W` allowlist tests and build-log fixtures.** Cover correct diffs and injected forbidden files at every boundary.
- [x] **Step 7: Run the red suite and save JUnit.** Run:

```powershell
& "C:\Python314\python.exe" -m pytest manuscripts\gauge_vfe_rg\verification\tests --junitxml C:\tmp\gauge-vfe-rg-red.junit.xml
```

Expected: failures identify the absent interfaces, not import/syntax defects. Commit `test: specify gauge VFE RG release verification`.

### Task 3: Implement Stable Schur and Canonical-Correlation Determinant Gaps

**Files:** Modify `07_restrictions.tex`, `appendix_numerical_provenance.tex`, `verification/run_checks.py`, `verification/claims.json`, and `verification/VERIFICATION.md`; satisfy `test_factorization_gap.py`.

**Interfaces:** Produces `GapStep`, `GapResult`, `validate_partition`, `two_block_factorization_gap`, and stable multiblock `factorization_gap` diagnostics.

- [x] **Step 1: Validate SPD inputs and partitions.** Reject overlaps, omissions, empty blocks, bad indices, nonsymmetry beyond tolerance, failed Cholesky, NaN, and infinity.
- [x] **Step 2: Implement the two-block formula.** Use Cholesky factors and `scipy.linalg.solve_triangular` to compute `R=L_A^{-1} C L_D^{-T}`, its singular values `rho`, and `-0.5*sum(log1p(-rho**2))`; never subtract large log determinants or form an explicit inverse.
- [x] **Step 3: Implement multiblock telescoping.** Merge along a declared refinement order, sum two-block increments, and return singular values, minimum `1-rho**2`, residual-derived clipping decisions, Cholesky residuals, backward-error bounds, and the merge order.
- [x] **Step 4: Replace absolute thresholds in `check_cg_factor_gap`.** Derive scale-aware tolerances from accumulated backward error and make every nonfinite or excessive singular-value excursion a failed check.
- [x] **Step 5: State the stable manuscript formula.** In `07_restrictions.tex`, retain the exact determinant identity, derive `\Delta=-\frac12\sum_a\log(1-\rho_a^2)` from the Schur complement, and specify Cholesky solves with `log1p(-\rho_a^2)` as the numerical realization. Update the numerical provenance and claim map to identify the new frozen stress protocol.
- [x] **Step 6: Run the focused tests.** Expected: all determinant tests pass, including all 3,138 draws and mpmath controls:

```powershell
& "C:\Python314\python.exe" -m pytest manuscripts\gauge_vfe_rg\verification\tests\test_factorization_gap.py -q
```

- [x] **Step 7: Commit.** Commit `fix: stabilize Gaussian factorization gaps`.

### Task 4: Implement the Fail-Closed Result, Manifest, Lifecycle, and Build Interfaces

**Files:** Modify `run_checks.py`, `VERIFICATION.md`, `requirements.txt`, `build.ps1`; create both JSON files, `lifecycle_gate.py`, and `build_audit.py`; satisfy the remaining verification tests.

**Interfaces:** Implement:

```python
discover_bound_inputs(repo_root: Path) -> dict[str, Path]
build_manifest(repo_root: Path) -> dict
build_result(repo_root: Path, source_revision: str) -> dict
semantic_payload(document: dict) -> dict
canonical_json_bytes(value: object) -> bytes
validate_result_shape(document: dict) -> list[str]
verify_result(result_path: Path, repo_root: Path) -> VerificationReport
atomic_write_json(path: Path, value: object) -> None
```

- [x] **Step 1: Define an exhaustive manifest policy.** Recursively bind all manuscript TeX plus `SPEC.md`, parent bibliography/style, build script, core verifier files, schemas, lifecycle/build code, and every verification test. Reject unexpected governed extensions instead of silently excluding them.
- [x] **Step 2: Replace the CLI contract.** Implement a required mutually exclusive group:

```text
run_checks.py --update RESULT [--source-revision SHA] [--report REPORT]
run_checks.py --verify RESULT [--report REPORT]
```

Remove implicit output rewriting. Verify in memory and preserve the input bytes
on success and failure. In update mode, stage both result and report, perform
all closing checks before publishing either, atomically replace the valid result
first, and publish only a report that binds that exact result and run receipt.
A pre-commit failure must preserve existing result/report bytes; a partial
two-file publication must be mechanically unauthenticatable rather than being
misrepresented as a portable joint atomic rename.
- [x] **Step 3: Bind provenance and semantics.** Record UTC timestamp, full source Git revision, dirty state, exact dependency versions, canonical semantic-payload SHA-256, schema version, complete path set, and finite JSON numbers. Exclude only the timestamp and digest field from the semantic digest.
- [x] **Step 4: Compare bytes to source revision `S`.** In evidence mode allow `HEAD=E` while proving each bound source path equals its Git blob at `S`; reject revision, manifest, payload, check-ID, and shape drift.
- [x] **Step 5: Implement lifecycle allowlists.** Parse `git diff --name-status -z`, enforce source-to-evidence, evidence-to-closure, closure-to-wiki, and optional wiki-to-publication byte identity.
- [x] **Step 6: Implement build auditing.** Record tool versions, exact command sequence and exit codes, complete inputs/digest, PDF hash/bytes/pages/metadata, log/aux/bbl/toc hashes, duplicate labels, unresolved references/citations, rerun requests, fatal errors, overfull boxes, literal `??`, invalid statuses, stale auxiliaries, and changed-page render selection.
- [x] **Step 7: Add the non-circular release bootstrap and extend `build.ps1`.** Treat exact approved external PowerShell transport bytes as the public trust root with typed `Build`, `NumericalUpdate`, and `NumericalVerify` modes. Keep a readable ASCII bootstrap body plus a deterministic one-line ASCII `ScriptBlock.Create`/base64 transport, and mechanically require that decoding the transport reproduces the body byte-for-byte without dynamic-expression evaluation. Because the body exceeds the Windows command-line limit and multiline `-Command -` is statement-streamed, pre-hash the one-line transport externally and feed those exact raw bytes on binary standard input to fixed PowerShell `-NoProfile -NonInteractive -Command -`. Carry the twelve untrusted invocation values plus the externally computed transport digest and byte count only in a closed exact `GAUGE_VFE_BOOTSTRAP_*` environment schema; bind that independent transport identity into the checked receipt without claiming self-authentication. Lock fixed PowerShell/Git/Python as applicable, validate controlled Git metadata and full `S`, and authenticate the exact source-revision driver before launch. Build mode materializes the exact `S:build.ps1` blob through one retained `CreateNew` handle under a fixed non-reparse temporary base and verifies its Git object identity. Because that write-capable creation handle cannot be safely downgraded for a child path reopen, read the exact authenticated bytes through the still-held handle, generate a one-line ASCII `ScriptBlock.Create`/base64 child transport, and stream it in binary mode to fixed child PowerShell under an exact closed `GAUGE_VFE_BUILD_*` environment. The inner script receives explicit repository/materialized source identities and never treats its in-memory `$PSCommandPath` as provenance. Retain all handles and check M1 plus the typed report before cleanup. Numerical modes instead S-bind and lock the exact checkout `run_checks.py` path and execute that same path under fixed Python `-I -S`, preserving its repository-root semantics. Production must not resolve evidence tools through caller `PATH` or inner-driver defaults. Direct checkout-script execution is unauthenticated convenience only. The inner build driver accepts explicit output, audit, repository/source, tool, and source-revision parameters; requires a nonmutating numerical verification; and discovers external TeX/BibTeX inputs by repeating the complete disposable command sequence to a bounded monotone fixed point while retaining deny-write/delete locks. It snapshots every pdfTeX pass recorder, unions pass-one/pass-three/pass-four plus BibTeX inputs, discards discovery outputs, and runs the four evidence passes from a fresh directory with `-no-shell-escape`, rejecting any evidence input outside the prelocked external envelope. Bind the numerical report to the authenticated runner's exact canonical stdout and bind the build audit to an authenticated auditor digest marker before trusting either pathname. The numerical runner locks the policy first, transactionally retains the complete rediscovered governed set through M1, and stages result/report output until all closing checks pass. Before build launch, the outer bootstrap retains the exact fresh output-directory identity. Afterward it requires the audit's complete artifact map to equal a recursive non-reparse output inventory, retains every artifact (including `main.pdf`) against write/delete/substitution, rejects additions, and rechecks the exact set through M1. The outer bootstrap then retains and same-handle validates the typed result/report/audit relationship through its own M1 and receipt. Fail on any bootstrap, verifier, tool, source-envelope, governed-handle, output-transaction, process-channel binding, external-input, artifact-set, or audit finding. Require command-length, stdin/env transport, decoded-body equality, exact inner-payload handoff, tampered-driver, write/delete/rename, object-mismatch, PATH-spoof, reparse-temp, early-failure, path-replacement, forged valid report/audit substitution, governed A-to-B-to-A, existing-target transaction failure, output-artifact substitution/addition, external A-to-B-to-A, new evidence-input, first/final-pass-only input, and nonconvergence red witnesses.
- [x] **Step 8: Run the complete suite.** Run:

```powershell
$task4Temp = "C:\tmp\gauge-vfe-rg-task4-final-20260804"
& "C:\Python314\python.exe" -m pytest `
  -p no:cacheprovider `
  --basetemp "$task4Temp\pytest" `
  --junitxml "$task4Temp\gauge-vfe-rg-verification.junit.xml" `
  manuscripts\gauge_vfe_rg\verification\tests
```

Create the fresh external `$task4Temp` directory before the run and refuse to reuse an existing path. Expected: zero failures/errors/skips; report counts only by parsing the JUnit XML, and record the XML SHA-256 with the exact source hashes. Commit `feat: make gauge VFE RG verification fail closed`.

### Task 5: Repair Probability Semantics and the Exact Extended ELBO

**Files:** Modify `03_probability.tex`, `05_elbo.tex`, `05a_expfamily.tex`, `05b_local_collective_elbo.tex`, `06_general_coarsegraining.tex`, `appendix_notation.tex`, `appendix_claim_ledger.tex`, and the proof ledger/evidence record.

**Interfaces:** Produces one fixed family-level domination tier, typed kernels/densities, a definition of `\mathcal L^{\mathrm{ext}}`, and a proved local/collective ELBO identity in which observations are interaction records generated by other agents or environmental channels.

- [ ] **Step 1: State the fixed probability universe.** Use a fixed countable atomic mixed-coordinate support where invoked; distinguish probability kernels from sigma-finite integration kernels; require jointly measurable density versions relative to a common family-level dominating measure.
- [ ] **Step 2: Define the extended likelihood once.** Near the base ELBO definition introduce `\mathcal L^{\mathrm{ext}}` with its sample spaces, normalization, reference measures, and conditioning variables; replace the undefined later uses with cross-references.
- [ ] **Step 3: Derive local agent VFE.** For agent `i`, condition on its Markov blanket/interaction record, identify the likelihood contribution generated by agent-agent and agent-environment channels, and prove `F_i = KL(q_i || p_i(\cdot\mid o_i)) - \log p_i(o_i)` under stated absolute-continuity hypotheses.
- [ ] **Step 4: Derive the correlated multi-agent ELBO.** State the joint recognition law before any mean-field restriction, prove the exact collective identity, and show the local terms plus correlation/mutual-information correction rather than assuming an additive factorization.
- [ ] **Step 5: State the observation ontology precisely.** Prove that an observation is a realized interaction-channel output. The theory can be agent-only only after the “environment” is represented as additional channel-bearing agents or exogenous stochastic systems; deleting observations without replacing their sigma-algebra is not equivalent.
- [ ] **Step 6: Independently reconstruct all equalities.** An adversarial agent must audit normalization, Radon--Nikodym directions, conditioning sigma-algebras, and double-counting. Record the proof and falsifiers in the ledger.
- [ ] **Step 7: Run static checks and commit.** Run `rg -n "mathcal L\^\{ext\}|sigma-finite|dominat|interaction record" manuscripts/gauge_vfe_rg`; expected: definition precedes every use and all claims have exact hypotheses. Commit `docs: repair probability and extended ELBO semantics`.

### Task 6: Repair Gauge, Gaussian, Information-Geometric, and Philosophy Claims

**Files:** Modify `02_geometry.tex`, `04_generative.tex`, `06_gaussian.tex`, `08_infogeometry.tex`, `09_coarsegraining.tex`, `11_obstructions.tex`, `12_philosophy.tex`, appendices, and `references.bib` if authoritative keys are absent.

**Interfaces:** Produces consistent restriction/pushforward directions, valid density tiers, strict/semidefinite Gaussian results, the correct Campbell family, and narrowed source attributions.

- [ ] **Step 1: Fix cross-scale and gauge directions.** Define the direction of every restriction map `R`; make measure-level pushforward the general statement; reserve determinant density formulas for differentiable equal-dimensional tiers; rename any nonclosed “full residual group” object.
- [ ] **Step 2: Reconcile frame notation.** Distinguish `h_i` from contextual `h_i^x`, correct inverse/congruence laws, require `K(x,Y)=1` for a probability kernel, and use the closure `\overline H` where holonomy closure is required.
- [ ] **Step 3: Repair Gaussian positivity.** State `A_i\succ0` where strict positivity is needed; otherwise prove positive semidefiniteness and the exact null-space criterion.
- [ ] **Step 4: Correct Campbell's family.** Replace the one-function normalized citation claim with the nonnormalized two-function family actually supported by Campbell (1986).
- [ ] **Step 5: Repair philosophy source attributions.** Narrow Esfeld and van Fraassen statements to what their sources support; preserve the manuscript's own eliminative or structural thesis as a separately status-tagged proposal rather than an imported conclusion.
- [ ] **Step 6: Remove the stale connection claim.** Delete orphan label `02_geometry.tex` near the former averaged-connection proposition and replace `12_philosophy.tex`'s stale credit with a status-tagged statement actually proved in the manuscript.
- [ ] **Step 7: Audit and commit.** Require an adversarial geometry/info-geometry pass and a bibliography-key build check. Commit `docs: repair gauge and information geometry claims`.

### Task 7: Prove the Exact Measure-Pair and Local Action Theorems

**Files:** Modify `07_general_renormalization.tex`, `07b_agent_network_rg.tex`, `appendix_notation.tex`, `appendix_claim_ledger.tex`; update proof artifacts.

**Interfaces:** Produces exact nonlinear `Q_ell`, Fréchet derivative, Hessian, contraction, Fisher defect, Dobrushin criterion, essential-spectrum theorem, and norm-dependence witness.

- [ ] **Step 1: Define the scale-indexed measure pair.** Specify normalized `\pi_\ell`, coarse kernel/pushforward, reverse kernel, action quotient by constants, and the local analytic bounded chart `\mathcal U_{\ell,\epsilon}\subset L^\infty(\pi_\ell)`.
- [ ] **Step 2: Prove analyticity and derivatives.** Derive `D Q_\ell(0)` as reverse-kernel conditional expectation and `D^2 Q_\ell(0)` as negative conditional covariance, with all source/target spaces typed.
- [ ] **Step 3: Prove `L^p` contraction and the exact `L^2` defect.** State the equality as conditional variance/Fisher information loss and specify equality conditions.
- [ ] **Step 4: Prove Dobrushin oscillation contraction.** State the nonautonomous sufficient convergence criterion using `B_{n\leftarrow\ell}\to\infty` and the convention `\log 0=-\infty`; do not call it necessary.
- [ ] **Step 5: Prove the bounded positive-unital essential-spectrum statement.** Declare the Calkin-algebra convention and exact hypotheses.
- [ ] **Step 6: Give the circle norm witness.** Prove spectral radius `1` on `L^\infty` but `2^\alpha` on periodic `C^\alpha`, demonstrating that relevance is norm/identification dependent.
- [ ] **Step 7: Run independent reconstruction and commit.** The reconstructor receives theorem statements and definitions but not the manuscript proof. Reconcile every discrepancy before commit `docs: prove exact RG action theorems`.

### Task 8: Construct the Full Finite-Network Interaction Operator

**Files:** Modify `06_general_coarsegraining.tex`, `07_general_renormalization.tex`, `07b_agent_network_rg.tex`, notation/claim appendices; update proof artifacts.

**Interfaces:** Produces the full Boolean-lattice Hoeffding interaction space, assembly/extraction inverses on the action quotient, exact nonlinear RG, its derivative cocycle, retained projection, and explicit residual.

- [ ] **Step 1: Quantify over arbitrary finite networks.** Let `V_ell` be any finite set with standard-Borel coordinate spaces and product reference `nu_ell` equivalent to `pi_ell`; prove common null sets and preservation under admitted scale maps.
- [ ] **Step 2: Define the full power-set interaction space.** Include every nonempty subset, chosen zero-mean Hoeffding gauge, Banach norms, gauge-covariant assembly `E_ell`, and extraction `P_ell`.
- [ ] **Step 3: Prove inverse identities.** Establish `P_ell E_ell=I` and `E_ell P_ell=I` on the bounded action quotient. Prove the normalization preserves the declared gauge factor and separates the evidence-mass constant.
- [ ] **Step 4: Define exact and retained interactions.** Set the exact coarse interaction to `g_{ell+1}^{ex}=P_{ell+1}\bar U_ell E_ell g_ell`; introduce a typed bounded idempotent retained projection and the quotient residual `\bar r_{ell+1}^Q`.
- [ ] **Step 5: Define the nonlinear map and derivative cocycle.** Along an exact orbit use `M_ell(g_ell)=P_{ell+1}\bar U_ell(g_ell)E_ell`; never write an ordinary eigenvalue equation across unequal scale spaces.
- [ ] **Step 6: Prove uniformity in network size.** The proof may use finiteness of each Boolean lattice but no maximum `|V|` or exhaustive fixed-size computation.
- [ ] **Step 7: Adversarial audit and commit.** Check domination, boundedness, quotient well-definedness, gauge covariance, exact/projected wording, and residual norm. Commit `docs: construct exact finite-network interaction RG`.

### Task 9: Build the Score Lift, Hermite Spectrum, Generalized Modes, Beta Functions, and Fixed Objects

**Files:** Modify `07_general_renormalization.tex`, `07b_agent_network_rg.tex`, `08_infogeometry.tex`, appendices, bibliography, and proof artifacts.

**Interfaces:** Produces an inhabited relevance spectrum and typed cross-scale dynamics rather than a merely formal eigenvalue definition.

- [ ] **Step 1: Define the DQM score lift.** Relate centered action quotients isometrically to `L^2_0` scores; state why higher Hermite scores need not generate two-sided bounded exponential-action charts.
- [ ] **Step 2: Prove the integer-block Gaussian theorem.** For `b>=2`, define `L_b=R_bE_b` on normalized Gaussian score tangents and derive probabilists' Hermite eigenvalues `b^{1-k/2}` with completeness and domains.
- [ ] **Step 3: Cite Jona-Lasinio precisely.** Attribute conditional expectation and the Gaussian/Hermite realization without using the manuscript as authority; add Kemeny--Snell and Nakajima--Zwanzig sources where the repaired text invokes their standard results.
- [ ] **Step 4: Define generalized modes.** Provide compatible families across scale spaces and a Lyapunov/Oseledets-style cocycle formulation. Forbid `M_ell v=lambda v` unless a declared identification places both sides in one space.
- [ ] **Step 5: Define discrete beta functions.** Use explicit comparison maps `J_ell` before subtraction; introduce a continuous scale connection only on a separately declared smooth scale manifold.
- [ ] **Step 6: Define fixed objects and flows.** Separate fixed laws, fixed action classes, fixed interaction coordinates, and fixed configurations; state relevant/marginal/irrelevant as a definition relative to norms and comparison maps.
- [ ] **Step 7: Cross-check with exact/projected tiers.** A projected finite matrix always reports its residual; only invariant retained spaces inherit an exact beta function.
- [ ] **Step 8: Independent reconstruction and commit.** Commit `docs: derive RG modes beta functions and fixed objects` after oracle erasure and adversarial scope review.

### Task 10: Integrate Fisher Pullbacks and Timeless Histories

**Files:** Modify `05c_pullback_geometry.tex`, `05d_relational_inference.tex`, `07_general_renormalization.tex`, `07b_agent_network_rg.tex`, `08_infogeometry.tex`, appendices, and proof artifacts.

**Interfaces:** Produces family-closed Markov Fisher contraction, contextual base pullbacks, a separate configuration Fisher metric, and a typed history semiconjugacy without imposed time.

- [ ] **Step 1: Prove score/action compatibility.** Show the centered action derivative agrees with score conditional expectation and that the scalar `L^2` defect is Fisher information loss.
- [ ] **Step 2: State the bundle-level Fisher theorem.** Require DQM fine/coarse families, finite Fisher norm, parameter-independent normalized Markov fiber morphism, family closure, smooth score pushforward, related sections, and horizontal-lift compatibility.
- [ ] **Step 3: Separate the two pullbacks.** Keep the contextual Fisher pullback tensor on the base manifold distinct from the Fisher metric on the manifold of admissible section configurations; state the latter's base measure, channel weights, gauge quotient, finiteness, and nondegeneracy hypotheses.
- [ ] **Step 4: Type vertical and horizontal histories.** A curve inside one statistical fiber is vertical; a curve over base points requires a connection/covariant derivative; the base remains static and timeless in the construction.
- [ ] **Step 5: Prove the history condition.** For independently recomputed vector fields require `T\hat R_ell\circ X_ell=a_ell(X_{ell+1}\circ\hat R_ell)` with positive `a_ell`; derive only an orientation-preserving orbit reparameterization.
- [ ] **Step 6: Enforce two-index notation.** Use `Q^{(ell)}(r)` with independent scale depth `ell` and orbit position `r`; do not identify either with Fisher duration or physical time.
- [ ] **Step 7: Audit and commit.** Commit `docs: integrate Fisher pullbacks with timeless RG histories` after a geometry and dynamical-systems adversarial pass.

### Task 11: Close Referee Minor Repairs, Notation, Status, and Citations

**Files:** Modify `main.tex`, `07_restrictions.tex`, `09_coarsegraining.tex`, `10_renormalization.tex`, `11_obstructions.tex`, the other chapters/appendices named in the review, `SPEC.md`, `references.bib`, `claims.json`, and `VERIFICATION.md`.

**Interfaces:** Produces a consistent notation/claim inventory and a manuscript with no stale references, unsupported attributions, or breakable/stacked status tags.

- [ ] **Step 1: Expand the notation appendix.** Add the law, action, interaction, score, configuration, quotient, projection, residual, comparison-map, cocycle, and beta-function tiers.
- [ ] **Step 2: Remove the nested-forest restriction from measure-pair composition.** Retain only hypotheses actually used by the composition proof.
- [ ] **Step 3: Distinguish the two constants currently both called `c_b`.** Update all definitions and references.
- [ ] **Step 4: Repair cross-references and coarse-graining notation.** Point `11_obstructions.tex` to `eq:cg-cut-excess`; define `B`, `B^\perp`, `G`, `Q`, and `\operatorname{pdet}` before their uses in `09_coarsegraining.tex`; use closed holonomy `\overline{\mathcal H}` or state the required compact-closed hypothesis; and remove every orphan/duplicate label.
- [ ] **Step 5: Repair refinement and asymptotic terminology.** In `07_restrictions.tex`, state determinant-gap monotonicity only along a declared nested refinement tree. In `10_renormalization.tex`, rename the claimed “Tauberian” direction to its correct Abelian/Karamata direction.
- [ ] **Step 6: Make statuses unbreakable and singular.** Define `\status` with `\mbox`; split doubled statuses near `01_introduction.tex` lines 102/114 and `06_general_coarsegraining.tex` near line 180 into independently scoped claims.
- [ ] **Step 7: Remove or reconcile the emergent-time keyword.** Metadata must say only what the proved timeless-history framework supports.
- [ ] **Step 8: Update the numerical claim inventory.** Ensure one semantic `NUMERICAL` occurrence per mapped claim and no unwrapped status cell.
- [ ] **Step 9: Run source scans.** Run:

```powershell
rg -n "[T]ODO|[T]BD|[r]outine|[o]bvious|emergent time|\?\?" manuscripts\gauge_vfe_rg
rg -n "\\status\{[^}]+\}.*\\status\{" manuscripts\gauge_vfe_rg\*.tex
```

Expected: no placeholders, unsupported shortcuts, unresolved markers, or doubled tags. Commit `docs: close gauge VFE RG notation and citation findings`.

### Task 12: Perform a Source-Level Rigor Sweep and Create Revision `S`

**Files:** All source, bibliography, verifier, test, build, protocol, and proof-contract files; no generated results/PDF/closure/wiki files.

**Interfaces:** Produces the immutable source revision `S` from which all evidence is generated.

- [ ] **Step 1: Run a claim-to-source inventory.** Every theorem status and ledger claim must map to an exact label/file and a proof, definition, external citation, or explicitly numerical check.
- [ ] **Step 2: Run a type sweep.** Check every map's domain/codomain, every quotient representative, every base point, every gauge action, and every scale index.
- [ ] **Step 3: Run an oracle-erased reconstruction.** Give an independent agent definitions, theorem statements, and source citations but not the proofs; require reconstruction of all load-bearing derivations and exact discrepancy resolution.
- [ ] **Step 4: Run adversarial counterexample probes.** Include reset channels, deterministic channels, circle maps under two norms, nonclosed projections, non-equivalent references, scale-space subtraction without comparison, vertical/horizontal curve confusion, and independently optimized histories without semiconjugacy.
- [ ] **Step 5: Validate files.** Run JSON parsing, `git diff --check`, verification tests, bibliography-key scan, and the source manifest dry run. Every ledger claim must be `EVIDENCE_VERIFIED`, `REFUTED` only for an explicit negative claim, or `INCONCLUSIVE` with no release eligibility.
- [ ] **Step 6: Commit revision `S`.** Commit `docs: complete gauge VFE RG theorem remediation`; record the full `S` hash in the derivation checkpoint but do not alter source after subsequent evidence begins.

### Task 13: Generate Numerical and Manifest Evidence Bound to `S`

**Files:** Generate `verification/current-results.json`, JUnit XML under the derivation evidence directory, PB-1--PB-4 rerun evidence, and machine reports; do not modify source/test logic.

**Interfaces:** Produces deterministic evidence that names and byte-binds `S` while running from the evidence worktree.

- [ ] **Step 1: Run the full tests against `S`.** Save JUnit under `docs/derivations/.../evidence/`; parse counts from XML, not terminal output.
- [ ] **Step 2: Generate the result through the authenticated bootstrap.**
  Obtain the independently approved raw-ASCII bootstrap literal, verify its
  out-of-band SHA-256 and byte count, start fixed PowerShell with argv exactly
  `-NoProfile -NonInteractive -Command -` and the closed exact bootstrap
  environment in `NumericalUpdate` mode, and feed the approved bytes directly
  to binary standard input.  Require zero child status, a matching typed
  result/report transaction, M1 closure, and an independently validated
  bootstrap receipt.  Direct checkout execution of `run_checks.py` is a
  convenience diagnostic only and cannot generate production evidence.
- [ ] **Step 3: Verify without mutation through the authenticated bootstrap.**
  Hash `current-results.json`, repeat the same external procedure in
  `NumericalVerify` mode with a fresh report and receipt, hash the result again,
  and require byte identity plus exact report/result/receipt digest binding.
- [ ] **Step 4: Rerun PB-1 through PB-4.** Bind only files present at `S`; retain historical ledgers in Git history and create a new current evidence record rather than relabeling old evidence.
- [ ] **Step 5: Record environment and stress diagnostics.** Include Python/dependency versions, seed schedule, 3,138-draw protocol, high-precision controls, and all failure thresholds.

### Task 14: Build and Visually Audit the Manuscript Bound to `S`

**Files:** Generate `main.pdf`, build-audit JSON, logs/hashes, and visual-audit record under the evidence directory; do not modify source.

**Interfaces:** Produces a fresh four-pass PDF and machine/visual proof of document integrity.

- [ ] **Step 1: Create a fresh detached build worktree at `S` and empty output directory.** Record `pdflatex`, BibTeX, `pdfinfo`, and `pdftoppm` versions.
- [ ] **Step 2: Run the four-pass build through the authenticated bootstrap.**
  Use the externally approved one-line bootstrap transport in `Build` mode;
  require its exact source-revision inner-payload handoff, fixed tool identities,
  external-input fixed-point discovery, fresh evidence-pass directory, per-pass
  recorder union, all four zero exit codes, no stale auxiliaries, M1 closure,
  typed audit/report binding, and independently validated receipt.  Direct
  checkout execution of `build.ps1` is a convenience diagnostic only.
- [ ] **Step 3: Run the build audit.** Require zero undefined references/citations, duplicate labels, fatal controls/errors, emergency stops, rerun requests, literal `??`, invalid/doubled statuses, and new overfull boxes; record PDF SHA-256, bytes, page count, title, subject, and auxiliary hashes.
- [ ] **Step 4: Render changed pages and neighbors at 160 dpi.** If exact page mapping is uncertain, render all pages with `pdftoppm`. Inspect clipping, overlap, equation/table overflow, status wrapping, TikZ readability, headings, footers, and page transitions.
- [ ] **Step 5: Record zero-defect visual evidence.** Any layout correction changes source and therefore requires returning to Task 12 for a new `S` and rerunning all evidence.

### Task 15: Complete Independent Mathematical and Source Adjudication

**Files:** Complete evidence subrecords, `construction-or-strongest-theorem.md`, `counterexample-register.md`, and `adversarial-report.json`; no source changes.

**Interfaces:** Produces an independent proof reconstruction, source-to-claim map, adversarial verdicts, falsification conditions, and a release-eligible rigorous-theory-search record.

- [ ] **Step 1: Run at least three incompatible reconstruction lenses.** Use probability/operator theory, information/differential geometry, and statistical-physics/RG. Preserve their independent memos before cross-pollination.
- [ ] **Step 2: Challenge every critical/high claim.** Pair a skeptic and defender; require exact source locations, reachability/hypotheses, severity, and what would falsify the claim.
- [ ] **Step 3: Resolve disagreements by evidence.** Agent agreement is not closure. Recompute mathematics or consult primary sources; unresolved obligations are `INCONCLUSIVE` and block release.
- [ ] **Step 4: Run oracle erasure.** Remove answer-bearing proof text and confirm a fresh agent can reconstruct each theorem from definitions/hypotheses.
- [ ] **Step 5: Finalize the construction record.** State exact theorems, proofs, scope, counterexamples to overclaims, and the open infinite-volume boundary. No “best effort” or vague missing lemma language is permitted in a release-eligible record.

### Task 16: Commit Evidence Revision `E` and Prove `S..E` Purity

**Files:** Generated results/PDF, proof/evidence records, PB rerun, JUnit, build/visual/adversarial records only.

**Interfaces:** Produces clean commit `E` whose only delta from `S` is evidence.

- [ ] **Step 1: Run the lifecycle gate.** `source-to-evidence` must prove every source/test/build path at `E` is byte-identical to `S` and every changed path is on the evidence allowlist.
- [ ] **Step 2: Inspect the exact diff.** `git diff --name-status S..HEAD` must contain no TeX, bibliography, schema, test, verifier, build logic, or wiki file except generated `current-results.json` and the tracked PDF explicitly classified as evidence.
- [ ] **Step 3: Commit.** Commit `evidence: bind gauge VFE RG remediation to source`; record full `E`.
- [ ] **Step 4: Re-run nonmutating checks on clean `E`.** Verify the result file, lifecycle gate, PDF/build hashes, and all proof-record hashes.

### Task 17: Create Closure Revision `C`

**Files:** Finalize `release.json`, `final-report.md`, durable closure attestation under `docs/reviews/`, and verification-skill export; no source/evidence/wiki changes.

**Interfaces:** Produces a durable clean-`E` adjudication with every release claim closed by eligible evidence.

- [ ] **Step 1: Populate the final claim inventory.** Include all Section 7.3 design claims, PB-1--PB-4, theorem-source bindings, numerical stability, manifest immutability, build/visual integrity, and S/E purity.
- [ ] **Step 2: Validate the rigorous release record.** All dependencies must be closed, all evidence paths/hash bindings must exist, and affirmative-prior wording must remain non-evidentiary.
- [ ] **Step 3: Run `evidence-to-closure`.** Require `E..C` to contain closure records only and preserve all `S/E` bytes.
- [ ] **Step 4: Commit.** Commit `docs: attest gauge VFE RG remediation closure`; record full `C`.

### Task 18: Ingest the Authorized Wiki Record and Create Revision `W`

**Files:** Exactly the seven authorized wiki records listed in the file map.

**Interfaces:** Produces a new immutable source note recording `S/E/C`, four updated synthesis pages, updated index count/listing, and append-only log entries.

- [ ] **Step 1: Create the immutable source note.** Title it `Gauge-Covariant Variational Free Energy and Renormalization: 2026-08-03 Cross-Scale Operator Theory Record`; include required frontmatter, exact `S/E/C`, artifact hashes, theorem contract, established results, retained hypotheses, open infinite-volume boundary, `Relevance to this research`, `Related`, and `Sources`.
- [ ] **Step 2: Update the four synthesis pages.** Distinguish exact law/action channel, normalized `L^p` contraction, extensive `M_ell=P_{ell+1}U_ell E_ell`, exact finite closure, projected residual, scale depth versus Fisher duration, and finite versus infinite-volume scope. Do not edit the immutable 2026-08-01 pullback note.
- [ ] **Step 3: Update index and log.** Change manuscript count 14 to 15, place the new note first under in-preparation manuscripts, append one `INGEST` and one final `LINT` line.
- [ ] **Step 4: Lint twice.** Run `C:\Python314\python.exe docs\_lint.py` before and after the log entry. Require zero broken links, gray nodes, empty files, case collisions, and identity collisions.
- [ ] **Step 5: Run `closure-to-wiki`.** Require `C..W` to contain exactly the seven approved wiki paths and preserve all prior bytes.
- [ ] **Step 6: Commit.** Commit `docs: ingest gauge VFE RG cross-scale theory`; record full `W`.

### Task 19: Rebind the Active Ledger, Publish, and Safely Synchronize

**Files:** Modify but do not commit `.verification/ledger.json`; no other post-`W` artifact changes unless a separately validated publication commit `F` is required.

**Interfaces:** Produces a validated active ledger at the exact published revision, remote `main` at `W` or byte-identical `F`, and a live checkout advanced only if protected WIP can be preserved exactly.

- [ ] **Step 1: Create the active ledger against clean `W`.** Reproduce or hash-check `S/E/C`, validate the wiki-only diff, include the complete claim inventory, and run the deterministic verification validator. Leave the ledger modified and uncommitted.
- [ ] **Step 2: Fetch and inspect remote truth.** Run `git fetch origin`, `git log --oneline -5 origin/main`, and `git rev-list --left-right --count HEAD...origin/main`.
- [ ] **Step 3: Push the feature branch.** Verify its remote tip exactly.
- [ ] **Step 4: Publish `main` from a clean integration worktree.** Fast-forward only if remote ancestry permits. If remote work creates `F!=W`, prove all task-owned and manifest-bound paths byte-identical to `W`, rebuild the complete active ledger against `F`, and validate before publishing.
- [ ] **Step 5: Verify remote reachability.** Require `git ls-remote origin refs/heads/main` to equal `W` or `F` and every committed artifact to be reachable from that tip.
- [ ] **Step 6: Audit the live WIP before synchronization.** Enumerate and hash every dirty/untracked live path, identify incoming overlaps—especially `manuscripts/gauge_vfe_rg/verification/current-results.json`—and rehearse the exact update with a WIP overlay in a disposable worktree.
- [ ] **Step 7: Advance the live checkout only if every WIP byte survives.** Never stash, reset, discard, overwrite, or silently replace protected files. If exact preservation cannot be proved, leave the live checkout unadvanced and report the single concrete overlap instead of damaging WIP.
- [ ] **Step 8: Perform final verification-before-completion.** Recheck branch/remote parity, worktree identities, S/E/C/W or S/E/C/W/F lifecycle gates, source/evidence hashes, PDF metadata, JUnit counts, wiki lint, and active ledger validation.
- [ ] **Step 9: Remove only task-owned disposable worktrees after preservation is proven.** Keep the ledger-bearing worktree if removal would lose the required active ledger.

---

## Plan Self-Review Gate

- [ ] Every approved-design section 3--10 maps to at least one task and test.
- [ ] Every referee major and minor finding maps to an exact file and task.
- [ ] Every new map/operator has a declared domain, codomain, base point, norm, and exact/projected status.
- [ ] Every mathematical claim has a proof obligation; every computational claim has a mechanical test; every source claim has a primary citation.
- [ ] The plan contains no unfinished marker, placeholder, vague test instruction, or unsupported proof shortcut.
- [ ] `S/E/C/W` mutation classes are disjoint and lifecycle-tested.
- [ ] The final active ledger binds the exact published revision and survives the final response.
