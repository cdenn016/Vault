# Task 6 philosophy source map

## Scope and revision binding

This artifact audits the Esfeld--Lam and van Fraassen attributions changed in
`manuscripts/gauge_vfe_rg/12_philosophy.tex`, verifies the replacement for the
deleted averaged-connection credit, and records the bibliography metadata used
in `manuscripts/references.bib`. The review used the repository at Git base
`2a4f7fe` plus the Task 6 working-tree edits. It did not modify any central
proof-control JSON.

The source-facing files after the edits have these SHA-256 digests:

- `manuscripts/gauge_vfe_rg/12_philosophy.tex`:
  `5E717AD6C701CAA479A91308CF3C789FB3D9F56397C36FA88A06A399D8221F01`
- `manuscripts/references.bib`:
  `EA0F0B4F2800A0E711F246689CA8D54E2F57EF445B0C34491D5A3A06687A8B41`

All external records below were checked on 2026-08-04. The source-verifier
view tested direct support, and the skeptic view tested stronger readings,
missing scope, and possible counterevidence. Consensus between those views was
not treated as closure; each terminal state below is tied to a current primary
source or publisher record.

## Authoritative source records

### S-ESFELD-1

Michael Esfeld and Vincent Lam, “Moderate Structural Realism about Space-Time,”
*Synthese* 160, 27--46 (2008). DOI:
[10.1007/s11229-006-9076-2](https://doi.org/10.1007/s11229-006-9076-2).
The current [Springer publisher record](https://link.springer.com/article/10.1007/s11229-006-9076-2)
gives the authors, volume, pages, issue year, DOI, and abstract. The abstract
places “objects and relations (structure) ... on the same ontological footing”
and characterizes objects only through the relations in which they stand. It
explicitly contrasts this moderate view with radical ontic structural realism.

### S-VF-1

Bas C. van Fraassen, *The Scientific Image* (Oxford University Press, 1980).
Book DOI:
[10.1093/0198244274.001.0001](https://doi.org/10.1093/0198244274.001.0001);
print ISBN 9780198244271; online ISBN 9780191597473. The current
[Oxford University Press book record](https://academic.oup.com/book/7116)
states that constructive empiricism retains a literal understanding of
scientific language and that theory acceptance involves no more belief than
empirical adequacy. The publisher's
[Chapter 2 record](https://academic.oup.com/book/7116/chapter/151631337),
DOI [10.1093/0198244274.003.0002](https://doi.org/10.1093/0198244274.003.0002),
confirms that the formulation occurs in Chapter 2. The
[digitized primary-book record](https://books.google.com/books/about/The_Scientific_Image.html?id=yXbnCwAAQBAJ)
confirms the 1980 Clarendon Press edition and its pagination. In that edition,
p. 11 requires a “literal construal of the language of science,” and p. 12
states that “acceptance of a theory involves as belief only that it is
empirically adequate.” These are the two propositions cited by the revised
text; neither page states the manuscript's idle-wheel removal rule.

### S-MANUSCRIPT-1

The current manuscript is the primary source for the replacement mathematical
credit. In `05c_pullback_geometry.tex`,
`thm:pb-pullback-gauge-invariance` at lines 111--135 proves passive-frame
invariance for the covariant Fisher and Amari--Chentsov pullbacks of a fixed
connection--section pair. `prop:pb-pullback-connection-change` at lines
157--190 proves their exact connection-change formulas. Neither result
constructs an averaged connection, chooses a canonical connection, or supplies
a population observable sensitive to base holonomy.

## Claim-to-source adjudications

### T6-PHIL-01: van Fraassen scope

- **Revised claim:** Constructive empiricism combines literal theory language
  with belief on acceptance only in empirical adequacy; the manuscript's rule
  that removes an observably idle posit is a separate, stronger proposal.
- **Manuscript location:** `12_philosophy.tex:65--75`.
- **Evidence:** S-VF-1 directly supports the positive description of
  constructive empiricism. The manuscript, rather than van Fraassen, is now
  explicitly named as the author of the removal rule.
- **Source-verifier view:** The imported description is no stronger than the
  primary text. The citation points to p. 11 for literal construal and p. 12
  for acceptance as belief only in empirical adequacy.
- **Skeptic view:** The public publisher extract does not catalog every
  parsimony principle van Fraassen discusses. The revised text therefore does
  not claim that he rejects every eliminative heuristic; it makes only the
  narrower source-to-rule separation needed here.
- **Adjudication:** `EVIDENCE_VERIFIED`.
- **Falsification condition:** A passage in the cited primary work deriving a
  mandatory “no observable trace, therefore remove the posit” rule from
  constructive empiricism would refute the scope distinction. A surviving
  sentence attributing the manuscript's removal rule to van Fraassen would
  refute the remediation.

### T6-PHIL-02: Esfeld--Lam scope

- **Revised claim:** Esfeld and Lam set out moderate structural realism, with
  objects and relations on the same ontological footing and objects
  characterized relationally. The manuscript keeps eliminative OSR as a
  different, unsupported proposal and cites only Ladyman sources for it.
- **Manuscript location:** `12_philosophy.tex:157--172`.
- **Evidence:** S-ESFELD-1 directly states the moderate thesis and explicitly
  contrasts it with radical OSR. The revised radical-OSR sentence no longer
  cites `esfeld2008moderate`.
- **Source-verifier view:** The revised attribution tracks the publisher
  abstract nearly term for term without importing an eliminativist conclusion.
- **Skeptic view:** Esfeld and Lam still offer a metaphysical structural
  realism; the source does not establish that this manuscript instantiates it.
  The revised text therefore labels compatibility as an `OPEN` manuscript
  proposal and says that neither structural reading follows from the formal
  invariance results.
- **Adjudication:** `EVIDENCE_VERIFIED`.
- **Falsification condition:** A primary-source passage in the cited article
  endorsing the claim that structure alone exists and objects are eliminated
  would refute this mapping. A surviving Esfeld citation attached to the
  eliminativist sentence would refute the remediation.

### T6-PHIL-03: replacement of the averaged-connection credit

- **Revised claim:** The current manuscript proves passive-frame invariance for
  fixed connection--section pullbacks and exact formulas for their dependence
  on a changed chosen connection. It does not claim a canonical connection or
  a population observable sensitive to holonomy.
- **Manuscript location:** `12_philosophy.tex:105--125`.
- **Evidence:** S-MANUSCRIPT-1. A post-edit static scan finds no occurrence of
  `averaged connection`, `averaged connections`, or `curved and flat` in
  `12_philosophy.tex`.
- **Source-verifier view:** Both cited labels exist, and their theorem and
  proposition statements match the revised sentence.
- **Skeptic view:** Connection dependence of pullback tensors does not by
  itself establish curvature, holonomy, canonical selection, or operational
  observability. The revised text expressly marks those conclusions
  `NOT-CLAIMED`, while the proposed operational bridge remains
  `OPEN` with controlled positive and negative settlement conditions.
- **Adjudication:** `EVIDENCE_VERIFIED`.
- **Falsification condition:** A missing label, a cited result that fails to
  prove the stated invariance or change formula, or any surviving credit to an
  averaged-connection result would refute this remediation.

### T6-PHIL-04: bibliography metadata

- **Revised claim:** Both affected records carry verified identifiers.
- **Bibliography locations:** `references.bib:1913--1921` and
  `references.bib:4498--4507`.
- **Evidence:** S-VF-1 verifies the newly added van Fraassen DOI and the existing
  ISBN. S-ESFELD-1 verifies the existing Esfeld--Lam authors, title, journal,
  volume, number, pages, year, and DOI.
- **Adjudication:** `EVIDENCE_VERIFIED`.
- **Falsification condition:** A current Oxford or Springer correction showing
  a different identifier or bibliographic field would reopen the record.

## Static closure results

The following checks were executed on the edited working tree on 2026-08-04:

- The BibTeX scanner found 9 unique citation keys in `12_philosophy.tex`, 0
  missing keys, and 0 duplicate bibliography keys. `vanFraassen1980` and
  `esfeld2008moderate` each have exactly one definition.
- The reference scanner found 6 unique cross-reference targets, 0 missing
  labels, and 0 duplicate labels. Both replacement theorem-level targets have
  exactly one definition.
- Brace depth ended at 0 with minimum depth 0 in `12_philosophy.tex`,
  `references.bib`, and this evidence artifact.
- The Task 6 files contain 0 banned LaTeX spacing macros, 0 stale
  averaged-connection-credit phrases, 0 banned prose phrases from `SPEC.md`,
  and 0 British-English spelling hits from the checked list.
- The chapter diff adds 13 status tags on 13 separate lines. Manual scope
  review confirmed that each tag closes one declared, imported, conjectural,
  open, or not-claimed proposition; evidence obligations follow outside the
  tag's claim sentence.
- `git diff --check` exited 0 with no whitespace errors. Git emitted only
  line-ending conversion warnings for working-tree files.
