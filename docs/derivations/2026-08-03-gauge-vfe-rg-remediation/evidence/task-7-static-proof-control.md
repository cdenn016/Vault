# Task 7 static proof-control audit

## Scope and revision binding

This non-build audit covers the integrated Task 7 source state based on
`a2cca53bc2691bcaa5107445822a77f3b4996df9`.  It deliberately does not treat
the two scratch LaTeX syntax probes as release evidence; the clean release
build remains Task 14.

The audited source digests are:

- `07_general_renormalization.tex`: `FB24FE2864C34C61253C60E2E3258A4BFAAFAC8EF2DE08133E9968A07CCF8925`
- `07b_agent_network_rg.tex`: `18FC259CE52A834F1EA536123032AAC60D83B857551F568D028819C3E5F9FF87`
- `appendix_notation.tex`: `8EC60852F9E6B000E125C6F00E8B692B743924046D90AF2F61AE28B21E94733D`
- `appendix_claim_ledger.tex`: `567112B06528307248EAD8F1877FABE20C08EBA7746F3AC3E813AD87EBAA0F1B`

The three mathematical review artifacts have digests:

- `task-7-exact-action-proof.md`: `150C66FCC6F0C9529B9E5731D7E7EC34E6C45F66E49427991357AC8518EE83B7`
- `task-7-independent-reconstruction.md`: `62E18B74E4FC40DE0A8B7FA1E83FB55CB75A53ED01C173C2996C29415663DCE6`
- `task-7-operator-adversarial.md`: `E8FD27F90420A3697E6703088F5BFA9446669CB1C8C1E28F88D164E8D16E4B46`

## Mechanical results

A read-only UTF-8 scanner recomputed the following facts over the four changed
TeX files and the full chapter set:

- unescaped brace depth ended at zero and never became negative in every
  changed TeX file;
- begin/end environment multisets agree in every changed TeX file;
- all changed files contain zero banned `\,`, `\;`, or `\!` spacing macros,
  zero checked British-English spellings, zero mojibake markers, and zero lines
  carrying more than one status tag;
- the full manuscript has 1,086 unique explicit or heading-defined labels,
  zero duplicate definitions, and zero unresolved `ref`, `eqref`, `Cref`,
  `cref`, `autoref`, or `pageref` targets;
- the bibliography has 460 unique keys, zero duplicates, and zero missing keys
  among manuscript citations;
- the problem contract, approach registry, claim ledger, dependency DAG, and
  adversarial report all parse as JSON;
- every evidence identifier used by a claim resolves to a ledger record, every
  ledger artifact exists, and every recorded artifact digest matches current
  bytes;
- all ten Task 7 claims are present in the ledger, have admissible derivation or
  supplemental adversarial evidence, and are marked `EVIDENCE_VERIFIED`;
- the rigorous-theory-search checkpoint validator exits zero; and
- `git diff --check` exits zero.  Its only messages are Git's expected
  LF-to-CRLF working-tree conversion warnings.

The aggregate scanner verdict is `PASS`.  These checks establish syntax,
inventory, artifact binding, and checkpoint-control facts only.  The separate
derivations close the mathematical claims.

## Falsification conditions

This artifact becomes stale if any bound source or mathematical-review byte
changes.  A nonzero brace or environment imbalance, duplicate or missing
label/key, unresolved evidence identifier, artifact-digest mismatch, invalid
control JSON, nonzero checkpoint-validator result, banned language or spacing
hit, ambiguous status line, or nonzero `git diff --check` result refutes its
`PASS` verdict and requires regeneration.
