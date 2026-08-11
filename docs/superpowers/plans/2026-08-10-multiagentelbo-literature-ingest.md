# MultiAgentELBO Literature Ingest Plan

> Execution note: the 2026-08-10 literature-gap review is the approved design. Work occurs only in the isolated Research-vault worktree on `codex/multiagentelbo-literature-ingest-20260810`; the dirty live vault remains untouched.

**Goal:** Bank every missing or undercovered work named concretely in the review, propagate its consequences into the wiki, and leave a lint-clean, source-verified vault branch.

**Architecture:** New external works become immutable `sources/papers/` notes. Canonical concept pages synthesize clusters instead of duplicating paper summaries. Existing correction targets receive attributed, scope-limited amendments. Shared navigation and project surfaces are integrated only after the independent subject lanes finish.

**Verification:** Use publisher, proceedings, DOI, or arXiv primary records for bibliographic and substantive claims. Run `C:\Python314\python.exe docs\_lint.py --root .`, `git diff --check`, exact manifest/file checks, and an evidence-gated claim ledger bound to the final worktree revision.

## Global constraints

- Preserve source immutability: append new source files only; never edit existing source prose.
- Use canonical ASCII `firstauthor-YYYY-keyword` filenames and canonical-filename wikilinks.
- Give every new source all applicable `cluster/*`, `project/*`, and field-of-origin-first `field/*` tags.
- Add no active-inference or decentralized-protocol behavior to the MultiAgentELBO codebase; this is a vault-only ingest.
- Preserve the review's mathematical boundaries: approximate pseudomarginals are not exact global `Q`; compact connection-Laplacian theorems do not automatically cover noncompact `GL^+(2)`; citations do not close continuum, quotient, recovery, DLR, or Oseledets obligations.
- Keep official bibliographic titles exact. Write all explanatory prose in American English.
- Do not re-ingest the four present controls: Hoffman--Blei structured SVI, Hansen--Ghrist spectral sheaves, Yedidia--Freeman--Weiss generalized BP, or Winn--Bishop VMP.

## Task 1: Variational, active-inference, and singular-learning lane

Create or promote source notes for Ay et al. (2025), Matthews et al. (2016), Senoz et al. (2021), Millidge et al. (2021), Watanabe--Amari (2002), Hasenclever et al. (2017), Wilkinson--Sarkka--Solin (2023), Bagaev--de Vries (2023), Ruiz-Serra et al. (2025), Fukuoka et al. (2026), Heskes (2006), and Tran et al. on copula variational Bayes. Create `Process-space variational inference` and `Singular statistical models`; revise `Expected Free Energy` and `Collective active inference`. Link but do not duplicate existing VI/BP concepts.

## Task 2: Gauge, information-geometry, recovery, and RG lane

Create or promote source notes for Blackwell (1953), Ahn--Chertkov--Shin (2017), Gao--Brodzki--Mukherjee, Singer--Wu (2012), Bandeira--Singer--Spielman (2013), Geiger et al. (2013), Geiger--Temmel on information-preserving Markov aggregation, Lukashchuk et al. (2025), Williamson--Cranko (2024), Ahn et al. (2018), Gerdes et al. on lattice-gauge trivializing flows, Lovasz--Szegedy graph limits, Blumenthal's Banach-space multiplicative ergodic theorem, and Froyland--Lloyd--Quas' semi-invertible Oseledets theorem. Create `Statistical experiment comparison and deficiency`, `Graph synchronization and connection Laplacians`, and `Quotient Bayesian learning`.

## Task 3: Decentralized inference, social learning, and population-limit lane

Create source notes for Campbell--How (2014), Battistelli--Chisci (2014), Bandyopadhyay--Chung (2018), Julier--Uhlmann (1997), Malioutov--Johnson--Willsky (2006), Bayraktar--Chakraborty--Wu (2023), Sznitman (1991), Duchi et al. (2014), Lalitha--Javidi--Sarwate (2018), Jadbabaie et al. (2012), Aumann (1976), Rosas et al. (2019), Williams--Beer on PID, the review's named recent PID-inconsistency source if a primary record can be identified unambiguously, and Caines--Huang on graphon mean-field games. Create `Decentralized Bayesian inference`, `Communication-constrained inference`, `Conservative information fusion`, `Graphon limits of agent networks`, `Propagation of chaos`, `Non-Bayesian social learning`, `Common knowledge and Bayesian agreement`, `O-information`, and `Partial information decomposition`. Revise `Gaussian Belief Propagation`, `Probabilistic opinion pooling`, and `Mean-field games and continuum limits`.

## Task 4: Cross-lane integration

Create an immutable provenance note for the MultiAgentELBO literature-gap review. Update the inference, information-geometry, gauge, VFE, and social-physics themes; update `Gauge-Theoretic Multi-Agent VFE Model`; add every new source and wiki page to `index.md`; append one batch `INGEST` record and the final `LINT` record to `log.md`. Record exact-source leads that remain bibliographically ambiguous as open reading leads, not invented source notes.

## Task 5: Verification and closeout

Check the source manifest, required frontmatter/sections, canonical link targets, source-to-concept backlinks, and correction caveats. Run full vault lint and diff checks. Use independent source and structure reviewers, adjudicate their findings, and validate the final claim ledger. Do not commit, push, merge, or alter the live vault unless separately authorized.
