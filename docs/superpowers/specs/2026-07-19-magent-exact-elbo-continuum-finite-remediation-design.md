# MAgent Exact-ELBO Continuum--Finite Remediation Design

## Purpose

This revision repairs the peer-review findings in `manuscripts/MAgent_exact_elbo_whitepaper.tex` and its modular source without changing the paper's intended ontology. The theory remains a continuum field theory on associated statistical bundles over the contextual base manifold. The normalized finite-design ELBO is its rigorously defined lattice or discretized realization for calculation, inference, and implementation. The revision must prevent those two levels from being identified without an explicit sampling, reconstruction, or continuum-limit map.

## Continuum-primary mathematical hierarchy

An agent carries continuum distribution-valued sections $q_i,s_i,p_i,r_i$ over its support. These section fields are the primary theoretical objects. For a finite design $D=\{c_a\}_{a=1}^{M}$, evaluation gives a finite family of laws, but the recognition kernel $Q_X(dY\mid o)$ also depends on the observation and structural configuration. Its coordinate marginals will therefore be denoted $q_{i,a}^{o,X}$ and $s_{i,a}^{o,X}$. They are exact finite probabilistic objects and the variables available to an implementation.

The manuscript will introduce a typed sampling map from continuum section fields to finite families. A compatibility condition may identify $q_{i,a}^{o,X}=q_i^{o,X}(c_a)$ and $s_{i,a}^{o,X}=s_i^{o,X}(c_a)$ only after a posterior-indexed continuum section family has been supplied. The finite kernel by itself does not select a unique smooth extension away from $D$. Continuum reconstruction therefore requires a declared interpolation or extension operator and regularity assumptions. A continuum limit requires a refining sequence of designs, compatible finite laws, a topology, tightness or compactness as appropriate, and convergence of observables or functionals. No such limit will be claimed merely from the exact finite ELBO.

This is the same structural distinction that separates a continuum gauge field from link variables on a lattice. The analogy will be stated as a mathematical organizing principle, not as proof that a continuum probability measure or a renormalized continuum limit already exists. The finite ELBO remains exact on its declared finite product space. The continuum PIFB2 functional remains a field-level construction whose relation to the finite theory is a sampling or discretization crosswalk with open reconstruction and limit obligations.

## Repairs

The bundle and probability chapters will use unindexed $q_i(c),s_i(c)$ only for continuum section fields. Finite marginals of $Q_X$ will carry the indices $(i,a,o,X)$. The geometry figure will show separate continuum evaluation and finite marginalization arrows, joined only by an explicitly labeled compatibility condition. The structured-recognition and ELBO chapters will use finite marginal notation throughout.

The related-work discussion will compare the construction with structured variational inference and variational message passing, region-based free energies, federated or partitioned variational inference, and gauge-equivariant learning using primary sources. Novelty language will be narrowed to the manuscript's documented synthesis and its proved moving-peer obstruction. Historical priority beyond the completed search will not be asserted.

The PIFB2, VFE 4.0, and executable crosswalks will cite immutable repository commit-and-path locators. The response identity will state the exact equality condition. The moving-peer obstruction will be formulated with iterated pathwise derivatives on an admissible open parameter rectangle and will state positivity, nonconstancy, and no-cancellation hypotheses. The executable chapter will distinguish explicitly assigned configuration values from inherited defaults and will cite both operator construction and transport application paths. The prior Task-12 record will be labeled historical and unverified at the current source revision, while a new revision-bound verification record will contain commands, environment, artifact identities, and outcomes. Duplicate PDF destinations and missing display punctuation will be repaired.

## Research-vault writeback

The revision will append a new immutable manuscript source note that records the continuum--finite distinction, the exact source revision, the executable revision, the verification commands, and artifact hashes. Existing immutable source notes will not be edited. Relevant wiki synthesis pages will be updated only where the new distinction changes the stored account. `index.md` will list any new page, and `log.md` will receive an append-only operation entry. Vault lint must report no broken links, graph-grey nodes, empty files, case collisions, or identity collisions.

## Verification and publication

The claim ledger will bind each correctness and provenance claim to the repaired source revision and current evidence. Verification will include symbolic or analytic checks of the affected identities, citation-key and bibliography checks, static notation/reference scans, the finite-oracle test suite, direct `pdflatex` and BibTeX passes, warning review, PDF page rendering and visual inspection, artifact hashes, `git diff --check`, and an independent verifier who did not author the edits.

Work will remain isolated from the dirty live Research checkout. After all checks close, the repair branch will be committed and pushed. A clean integration worktree will merge the branch into current `origin/main` and push non-force. The live Research checkout will be fast-forwarded only when Git proves that doing so does not overwrite its unrelated tracked or untracked work.
