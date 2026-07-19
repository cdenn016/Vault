# MAgent Exact-ELBO Continuum--Finite Remediation Implementation Plan

> **Execution note:** Follow the approved design in `docs/superpowers/specs/2026-07-19-magent-exact-elbo-continuum-finite-remediation-design.md`. Keep the dirty live Research checkout untouched until the final WIP-safe fast-forward.

**Goal:** Repair every confirmed peer-review finding while retaining continuum distribution-valued sections as the primary theory and making the finite normalized ELBO the exact lattice or discretized realization used for calculation and implementation.

**Architecture:** The manuscript will have three typed levels. Continuum agent sections are primitive field-theory objects. A finite design samples those fields but does not determine a unique reconstruction. The recognition kernel on the finite product space has explicitly observation- and configuration-indexed coordinate marginals. Compatibility, reconstruction, and continuum-limit claims are stated separately, with their own hypotheses.

**Success criteria:** The manuscript contains no unindexed identification between a generally `(o,X)`-dependent finite marginal and one fixed continuum section; all finite derivations remain exact; the continuum ontology remains primary; novelty and internal-source provenance are calibrated; every confirmed low finding is repaired; the current oracle suite, citation audit, TeX/BibTeX build, PDF inspection, vault lint, claim-ledger validation, and independent verification close on the repaired revision; and the requested non-force Git lifecycle completes without changing unrelated live WIP.

## Task 1: Repair the continuum--finite type hierarchy

**Files:**

- Modify `manuscripts/magent_elbo_whitepaper/01_executive_scope.tex`.
- Modify `manuscripts/magent_elbo_whitepaper/02_bundle_geometry.tex`.
- Modify `manuscripts/magent_elbo_whitepaper/03_probability_semantics.tex`.
- Modify `manuscripts/magent_elbo_whitepaper/05_structured_recognition_elbo.tex`.
- Modify any affected notation in `06_mean_field_theory.tex`, `07_configuration_elbo.tex`, `08_information_geometry_gauge.tex`, `09_pifb2_crosswalk.tex`, `11_vfe4_comparison.tex`, `12_verification_limitations.tex`, and `13_appendices.tex`.
- Modify `manuscripts/magent_elbo_whitepaper/figures/magent_geometry_type_stack.tex`.

**Steps:**

1. State that continuum distribution-valued sections remain the theory-level agent fields. When their dependence on observation and structure matters, write the posterior-indexed sections as `q_i^{o,X}` and `s_i^{o,X}` rather than treating one unindexed section as all posterior states.
2. Define a finite sampling operator from a section to its values on `D`. Define the exact finite coordinate marginals of `Q_X(dY_D|o)` as `q_{i,a}^{o,X}` and `s_{i,a}^{o,X}`.
3. State the compatibility condition between a supplied continuum posterior section and finite marginals. State directly that the finite kernel supplies neither a unique off-design extension nor a continuum probability measure.
4. Explain the lattice-gauge analogy with `WilsonConfinement1974`, `KogutSusskind1975`, and `Creutz1983`: finite variables can regularize or discretize continuum fields, but an arbitrary finite design is not automatically a cell complex, link-field theory, or proved continuum limit.
5. State the missing continuum-limit obligations: a refining design sequence, compatible finite-dimensional laws, a declared reconstruction or projective system, topology, tightness or compactness where required, convergence of the functionals or observables, and control of gauge/reference-measure effects.
6. Replace every finite marginal occurrence with the indexed notation. Preserve unindexed `q_i(c),s_i(c)` only where a continuum field is actually meant. Rename mean-field factors when needed so they cannot be confused with continuum section fields.
7. Redraw the type-stack figure so continuum evaluation and finite marginalization are different arrows joined only by a compatibility hypothesis.
8. Run a static notation scan proving that no old `q_i(c_a)` or `s_i(c_a)` marginal identification remains.

## Task 2: Repair novelty positioning and immutable provenance

**Files:**

- Modify `manuscripts/magent_elbo_whitepaper/01_executive_scope.tex`.
- Modify `manuscripts/magent_elbo_whitepaper/09_pifb2_crosswalk.tex`.
- Modify `manuscripts/magent_elbo_whitepaper/10_executable_crosswalk.tex`.
- Modify `manuscripts/magent_elbo_whitepaper/11_vfe4_comparison.tex`.
- Modify `manuscripts/references.bib`.

**Steps:**

1. Add a compact related-work section comparing the paper with variational message passing, structured stochastic variational inference, Bethe/region free-energy methods, federated belief sharing, and gauge-equivariant neural architectures. Use primary-source metadata and explain the mathematical difference rather than listing papers.
2. Add `WinnBishop2005` and `HoffmanBlei2015` bibliography entries if they are absent. Reuse the existing `Yedidia2005`, `friston2024federated`, `cohen2019gauge`, and `He2021GaugeEquivariantTransformer` entries after checking their metadata.
3. Narrow novelty language to the typed synthesis of continuum bundle fields, an exact finite correlated-state ELBO, a separate configuration tier, and the scoped moving-peer obstruction proved in the paper. State that the search does not establish historical priority for every component.
4. Add immutable `@misc` source records for `PIFB2.tex` and `VFE4_gauge_causal_elbo_whitepaper.tex` at Research commit `b93d01f57dc0a55a11bf26ec13562f7019a5c84b`, and for the MAgent implementation at commit `3f5f094ab66c4f209fc3eb3c5b35f6f38dc13df0`.
5. Cite those records in the PIFB2, executable, and VFE 4.0 chapters. Keep the exact file paths and commit hashes visible in prose or bibliography notes.
6. Verify all citation keys, URLs, and commit paths mechanically.

## Task 3: Repair the remaining mathematical and presentation findings

**Files:**

- Modify `manuscripts/MAgent_exact_elbo_whitepaper.tex`.
- Modify `manuscripts/magent_elbo_whitepaper/02_bundle_geometry.tex`.
- Modify `manuscripts/magent_elbo_whitepaper/06_mean_field_theory.tex`.
- Modify `manuscripts/magent_elbo_whitepaper/09_pifb2_crosswalk.tex`.
- Modify `manuscripts/magent_elbo_whitepaper/10_executable_crosswalk.tex`.
- Modify `manuscripts/magent_elbo_whitepaper/13_appendices.tex`.

**Steps:**

1. Qualify the entropy-suppressed response identity: `S_i` and the reduced row potential differ by the categorical KL response term and coincide when that term vanishes, including equal active energies under the declared prior.
2. Replace the unrestricted third Fréchet derivative notation in the moving-peer theorem with the iterated pathwise derivative actually proved. Declare one admissible open parameter rectangle and carry positive coupling, nonconstant aggregate, differentiability/dominance, and no-cancellation hypotheses into the theorem statement.
3. Prevent the duplicate `page.1` destination by disabling PDF page anchors only for the unnumbered title/front page and re-enabling them before numbered front matter.
4. Add standard punctuation to the seven displays identified by the audit.
5. Correct the active-configuration provenance: distinguish values assigned literally in `CONFIG` from omitted values inherited through dataclass defaults, and explain the `kl_regulariser_eps=None` runtime materialization.
6. Add the active belief/model operator-construction anchors in `full_vfe.py`, preserve the transport-application anchor in `lie_groups.py`, and describe the gauge-fixed model-alignment short circuit.
7. Relabel the historical Task-12 96-page statement as an unverified project record for an earlier artifact. Point to the new revision-bound verification record rather than transferring the old result to the repaired source.
8. Run `git diff --check` and targeted lexical scans for banned manuscript phrases, British spellings in touched prose, forbidden LaTeX spacing macros, and unpunctuated edited displays.

## Task 4: Build a revision-bound evidence package and Research-vault record

**Files:**

- Create or update only one `docs/2026-07-19-edits.md`.
- Create `sources/manuscripts/magent-exact-elbo-whitepaper-2026-07-19-continuum-finite-remediation.md` after the manuscript content commit exists.
- Modify `wiki/projects/Gauge-Theoretic Multi-Agent VFE Model.md`.
- Modify `index.md`.
- Append to `log.md`.
- Create or update `.verification/ledger.json` if the verification skill's local contract selects that path.

**Steps:**

1. Commit the repaired manuscript, figures, bibliography, and plan-independent checks as a content revision before creating the immutable source note.
2. Build and test that exact content revision. Record the commit, commands, tool versions, source hashes, JUnit identity, PDF/log identities, page count, warnings, citation closure, and visual-inspection result in `docs/2026-07-19-edits.md` and the new immutable source note.
3. Update the MAgent project page with the continuum-field versus finite-lattice hierarchy and link the new source note. Update the index manuscript count and entry, then append parseable `INGEST` and `LINT` lines to `log.md`.
4. Run `python docs/_lint.py` and require zero broken links, graph-grey nodes, empty files, case-insensitive basename collisions, and cross-file identity collisions.

## Task 5: Verify, review, publish, merge, and fast-forward

**Commands and evidence:**

1. Run the exact finite oracle tests with machine-readable output: `python -m pytest manuscripts\magent_elbo_whitepaper\verification\test_elbo_oracles.py -q --junitxml=C:\tmp\magent-exact-elbo-remediation-20260719.xml`.
2. Run any new symbolic or static consistency checks required by the notation repair.
3. Build from `manuscripts` into a fresh `C:\tmp\magent-exact-elbo-remediation-build-20260719` directory using direct `pdflatex`, BibTeX, and sufficient final `pdflatex` passes. Treat undefined references, undefined citations, duplicate destinations, LaTeX errors, BibTeX errors, and overfull boxes as blockers.
4. Use `pdfinfo`, render representative and changed pages, and inspect the title/front matter, the type-stack figure, related work, the moving-peer theorem, crosswalk tables, bibliography, and appendices.
5. Validate the claim ledger. Dispatch an independent verifier with the complete diff, manuscript, build log, JUnit XML, source record, and plan. Resolve every critical or important review finding and re-run affected checks.
6. Commit the verification/wiki package. Push `codex/magent-exact-elbo-remediation-20260719` with tracking.
7. Fetch again. Merge the feature branch into current `origin/main` from a clean integration worktree, resolving only additive vault conflicts and preserving both histories. Re-run the required merged-tree checks, push `main` non-force, and verify the remote SHA.
8. Preflight the dirty live Research checkout. Fast-forward it to `origin/main` only if Git can do so without overwriting its tracked or untracked work. If Git identifies an overlap, leave the live WIP untouched and report the exact blocking paths rather than stashing, reverting, or forcing.
