# Verification record: sanitized rigorous-theory-search ingest

Date: 2026-08-03
Scope: Research-vault ingest of the five authored documents in the archived
`rigorous-theory-authored-docs-20260802.zip` bundle.

## Decision

The archive was ingested as one immutable `type: run` source note and one `type: method` synthesis
page. The five documents were not copied into the vault verbatim. Existing pullback, ELBO, and RG
theory pages were not rewritten because their current program-specific source records are stronger
and more directly bound than this historical methodology audit.

The ingest preserves the discovery/certification split, frozen problem contracts,
mechanism-diverse proof portfolios, acyclic claim dependencies, adversarial reconstruction,
oracle erasure, conditional Fisher/ELBO/RG derivations, and the explicitly provisional status of
the baseline grading. It does not claim that the historical implementation, benchmark, source-hash
approval, current runtime, or any future mathematical output is verified by this archive.

## Input identity

Bundle SHA-256: `DE59FA073A5B2278974D55A1EC3AA4B8FC8F742286130A8F36EB8B5931065DB7`
Bundle bytes: 35,529
Expected authored entries: 5
Observed authored entries: 5

| Relative document | SHA-256 |
|---|---|
| `docs/2026-08-02-edits.md` | `6C9653FCF0BE45B37C8239E3BFDA76A1D3DA6737BD8C52AE9029BAD5B9537BBF` |
| `docs/evals/2026-08-02-rigorous-theory-search-baseline.md` | `412092A908FB72F59D3EBD3C9A5617B2CC1988AA46080D46141F111081AD6FE7` |
| `docs/superpowers/plans/2026-08-02-rigorous-theory-search.md` | `70B9159EF251D2FAABD45E9E914997CA842C0CE51A8FDBC5D3D90B917FA02CE6` |
| `docs/superpowers/specs/2026-08-02-rigorous-theory-search-design.md` | `1129FAA8DABA57E8C2D0B996654625DD4996635575A7C9091E127FED8735D1D3` |
| `docs/verification/2026-08-02-rigorous-theory-search/independent-mathematical-reconstruction.md` | `A1E4466722D4FB72C4DC790B67CE10E73B8998F475C3E68DADCE321F517C745F` |

These hashes identify the reviewed archive only. They are not current-code or current-theory
certificates.

## Sanitization boundary

The retained source note contains relative artifact labels, mathematical equations, source-byte
hashes, status boundaries, and research relevance. It omits:

- absolute local paths and interpreter locations;
- branch, worktree, merge, push, and live-WIP operating instructions;
- protected-WIP filenames;
- runtime and model identifiers;
- process, session, host, or account metadata;
- raw event streams, stderr, private scratch, and unsafe runner metadata;
- installer internals, historical test totals, coverage figures, and complexity figures;
- stale language presenting historical source-hash approval as current certification.

A scan of the two new vault notes found no actual Windows or Unix home path, account name, host,
credential, API key, process/session identifier, or private-key marker. One generic drive-path
regular expression matched the mathematical text `$\iota:\mathcal T...$`; inspection confirmed it
was a LaTeX map declaration, not a filesystem path.

## Status audit

The five archived documents have distinct evidentiary roles:

- the edit log is a historical engineering record;
- the baseline is final-answer-only and leaves its reported 240 assertion grades provisional;
- the plan is normative rather than execution evidence;
- the design is a research-method specification;
- the independent reconstruction contains conditional mathematics but binds its historical
  approval to source files not included in this five-document archive.

Accordingly, the new source and method pages describe the archived reconstruction as conditional
mathematics. They do not claim a complete agent-network effective VFE, agent-only ontology, current
beta function, current fixed-point classification, or behavioral deployment success.

## Vault changes

Created:

- `sources/runs/2026-08-02-rigorous-theory-search-skill.md`
- `wiki/methods/Rigorous theory search.md`

Updated:

- `index.md` and `log.md`;
- the VFE Transformer and multi-agent project hubs;
- the Gauge VFE ELBO curriculum;
- four field MOCs whose displayed counts were stale relative to their live Bases tags.

No manuscript or existing theory concept page was modified.

## Mechanical checks

- Vault lint after all task files: **1,019 files**.
- Broken wikilinks: **0**.
- Graph gray nodes: **0**.
- Empty files: **0**.
- Case-insensitive basename collisions: **0**.
- Cross-file identity collisions: **0**.
- `git diff --check`: **PASS**; only platform line-ending notices were emitted.
- Frontmatter field census: **259** CS-ML, **231** Mathematics, **258** Physics, and **155**
  Statistics sources, matching the four touched MOC summaries.

New-note identities before commit:

- source note SHA-256: `834C17D74D226393387BB10342762E88278C63013FAC068C3CCBD6DA883C0DDE`;
- method page SHA-256: `4E645A8AC9F0909299DC063CAE3AAF81ED55C24DEC8164B81E1E036227858EEB`.

## Closure boundary

This verification closes the archive identity, sanitization scope, wiki propagation, and structural
integrity of the ingest. It does not re-run the archived implementation tests or paired behavioral
evaluation, independently re-prove every mathematical statement in the reconstruction, or promote
the historical audit to current program theory.
