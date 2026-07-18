# VFE 4.0 Zero-Dimensional Population White Paper Revision Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite the VFE 4.0 LaTeX white paper so its exact ELBO is formulated on a correlated population fiber over the zero-dimensional reduction of the general agents-as-local-sections theory.

**Architecture:** Preserve the normalized causal generative joint and structured ELBO, but replace the causal-graph base with a general smooth noumenal base followed by the specialization \(\mathcal C=\{\ast\}\). Separate sample bundles, statistical bundles, agent marginals, the global recognition law, same-point frame comparisons, and optional graph connection data.

**Tech Stack:** LuaLaTeX, BibTeX, TikZ, `scientific_report.sty`, Git worktrees, primary-source bibliography.

## Global Constraints

The paper is a theoretical white paper, not an empirical V4 result. The categorical token likelihood remains normalized and cross-entropy remains its negative log likelihood. The exact ELBO requires one normalized generative joint and one normalized recognition law. Mean-field is an optional control, not a default assumption. Smooth-base geometry, zero-dimensional reduction, and internal graph structure remain distinct. All prose uses American English and the repository manuscript-style constraints.

### Task 1: Reframe the front matter and observation semantics

**Files:**

- Modify: `manuscripts/VFE4_gauge_causal_elbo_whitepaper.tex`
- Modify: `manuscripts/vfe4_whitepaper/01_executive_scope.tex`
- Modify: `manuscripts/vfe4_whitepaper/02_observations_related_work.tex`

- [x] Replace the title and abstract framing with the general bundle plus zero-dimensional population reduction.
- [x] State that token occurrences are observations and that the causal graph is an internal factor graph.
- [x] Add the joint-first recognition choice and the agent-marginal interpretation to the claim-status boundary.
- [x] Retain the exact target-blind prediction versus target-conditioned recognition distinction.
- [x] Compile the front matter through the full master document and repair references.

### Task 2: Replace the graph-base geometry

**Files:**

- Modify: `manuscripts/vfe4_whitepaper/03_bundle_geometry.tex`
- Modify: `manuscripts/vfe4_whitepaper/figures/vfe4_bundle_dual_coordinates.tex`
- Modify: `manuscripts/vfe4_whitepaper/figures/vfe4_graphical_abstract.png` or replace its inclusion with a revised vector schematic

- [x] Define \(\mathcal C\), \(P\), sample associated bundles, and statistical associated bundles.
- [x] Define agents as smooth local statistical sections on open domains and state their marginal-consistency obligations.
- [x] Derive the zero-dimensional population fiber and internal causal graph.
- [x] Separate smooth connection, flat same-point frame comparison, and optional discrete graph connection.
- [x] Redraw the geometry schematic so all token agents are visibly stacked over one base point.
- [x] Compile and inspect the revised geometry pages.

### Task 3: Retype the normalized joint and structured recognition law

**Files:**

- Modify: `manuscripts/vfe4_whitepaper/04_generative_model.tex`
- Modify: `manuscripts/vfe4_whitepaper/05_structured_information_form.tex`
- Modify: `manuscripts/vfe4_whitepaper/figures/vfe4_factor_graph.tex`

- [x] Replace graph-vertex fiber notation with labeled copies of the common zero-dimensional sample fibers.
- [x] Retain the normalized source priors, receiver kernels, categorical emission, and normalization proof.
- [x] Define \(Q\) as the primitive correlated population law and recover local agent beliefs by pushforward.
- [x] State the agent-first copula or compatible-conditionals alternative without using it in the exact core.
- [x] Retain sparse block precision, natural/expectation duality, and mean-field as a nested restriction.
- [x] Compile and inspect the factor and coordinate figures.

### Task 4: Reconcile the ELBO, updates, and transformer crosswalk

**Files:**

- Modify: `manuscripts/vfe4_whitepaper/06_elbo_coordinate_updates.tex`
- Modify: `manuscripts/vfe4_whitepaper/07_transformer_crosswalk.tex`

- [x] Retype the mixed reference measure and latent inventory on the population product fiber.
- [x] Preserve the evidence identity and factorwise KL decomposition.
- [x] Make coordinate-update guarantees conditional on the same complete ELBO.
- [x] Explain source routing as inference over internal causal ancestry, not transport across base points.
- [x] Preserve the V3 obstruction and state why V4 is a new normalized construction rather than a relabeling.
- [x] State the exact boundary between posterior target access and predictive target leakage.

### Task 5: Revise hypotheses, limitations, appendices, and notation

**Files:**

- Modify: `manuscripts/vfe4_whitepaper/08_hypotheses_limitations.tex`
- Modify: `manuscripts/vfe4_whitepaper/09_appendices.tex`

- [x] Add geometry-reduction and marginal-consistency verification obligations.
- [x] Remove any remaining implication that graph holonomy is base curvature.
- [x] Retype the bundle-map oracle and notation table.
- [x] Retain the normalization, Gaussian, gauge-pushforward, and information-factor proofs after notation changes.
- [x] Add a precise limit stating that the noumenal base is a modeling hypothesis not identified by language data.

### Task 6: Independent review and final verification

**Files:**

- Modify as required by confirmed review findings.
- Update: `docs/2026-07-18-edits.md`

- [x] Obtain independent differential-geometry, variational-inference, and transformer-causality reviews.
- [x] Resolve every critical or high-severity finding and record the resolution.
- [x] Run citation, duplicate-label, unresolved-reference, banned-pattern, spelling, and placeholder scans.
- [x] Run `git diff --check`.
- [x] Compile from a clean task-owned output directory with LuaLaTeX and BibTeX.
- [x] Inspect the compilation log and representative rendered pages, including every revised figure.
- [x] Commit, push, merge to `main`, safely fast-forward the live Research checkout without touching unrelated WIP, and remove the task worktree.
