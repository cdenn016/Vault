# Task 8 static proof-control audit

## Scope and revision binding

This non-build audit covers the integrated Task 8 source state based on
`17b59ae4bbd909f9c94e08867c9114dbcbcca3bf`.  It does not promote either a
scratch syntax probe or a prior manuscript build to current release evidence;
the clean release build remains Task 14.

The audited source digests are:

- `06_general_coarsegraining.tex`: `5E7028EBCD5B2A311F67E3AFA39AED116CE357C47284DDE4E92808B07E9E0E79`
- `07_general_renormalization.tex`: `5F0604C948220A22C3321918C0634481AD9ADB5FB4A25B1AEF78ED91A6858080`
- `07b_agent_network_rg.tex`: `902E6ECF583CF084ADDCCDB3E84A265CFC8EEF5D4BA3BD3749E533295E6BD95C`
- `appendix_notation.tex`: `0CD7926AAC4568FA771136400B04F46808E4384791C7D2A11D7151304D64884B`
- `appendix_claim_ledger.tex`: `10D5C12A97CBCDD48EBF7E46854BF56FA01D00DC5F52D091E7513AEEDB1E4FA1`

The three mathematical review artifacts have digests:

- `task-8-interaction-proof.md`: `B5F3B294AF0958E4E9CFEF02F8F1DF29471295419B0F913565DB187EB0F0C4B7`
- `task-8-independent-reconstruction.md`: `7C0AE6DE11DA4F50ABDD0CB246CC99DD08ABD13E5E6BDFEAFDCA67858EFD1429`
- `task-8-gauge-adversarial.md`: `AC0C370CDDC053FD4F39393C0A15252AA2C6E195DFE312661C468F5F79311259`

## Mechanical results

A read-only UTF-8 scanner recomputed the following facts over the four changed
TeX files and the complete chapter set:

- unescaped brace depth ended at zero and never became negative in every
  changed TeX file;
- begin/end environment stacks close in order in every changed TeX file;
- all changed files contain zero banned `\,`, `\;`, or `\!` spacing macros,
  zero checked British-English spellings, zero mojibake markers, and zero lines
  carrying more than one status tag;
- the full manuscript has 1,118 unique explicit or heading-defined labels,
  zero duplicate definitions, and 474 unique `ref`, `eqref`, `Cref`, `cref`,
  `autoref`, or `pageref` targets with none unresolved;
- the bibliography has 460 unique keys, zero duplicates, and 74 cited keys
  with none missing;
- the problem contract, approach registry, claim ledger, dependency DAG, and
  adversarial report all parse as JSON;
- every evidence identifier used by a claim resolves to a ledger record, every
  ledger artifact exists, and every recorded artifact digest matches current
  bytes;
- the `hoeffding-inverse`, `interaction-gauge-domination`,
  `exact-interaction-map`, and `projected-interaction-residual` claims are
  present, have eligible mathematical evidence, and are marked
  `EVIDENCE_VERIFIED`;
- the rigorous-theory-search checkpoint validator exits zero; and
- `git diff --check` exits zero.  Its only messages are Git's expected
  LF-to-CRLF working-tree conversion warnings.

The aggregate scanner verdict is `PASS`.  These checks establish syntax,
inventory, artifact binding, and checkpoint-control facts only.  The bound
derivations, rather than agreement among reviewers, close the mathematical
claims.

## Falsification conditions

This artifact becomes stale if any bound source or mathematical-review byte
changes.  A nonzero brace or environment imbalance, duplicate or missing
label/key, unresolved evidence identifier, artifact-digest mismatch, invalid
control JSON, nonzero checkpoint-validator result, banned language or spacing
hit, ambiguous status line, or nonzero `git diff --check` result refutes its
`PASS` verdict and requires regeneration.
