# Task 6 static source audit

## Scope and revision binding

This non-build audit covers the integrated Task 6 source state based on
`2a4f7fea2da25afef2867f15632b8f96e2780f73`.  It deliberately does not run
LaTeX; the clean four-pass build remains a later source-frozen task.

The audited source digests are:

- `02_geometry.tex`: `728AEE6C8F2FC3A3EA9B934F44EDB25C94CDEF5F4E34726665D696B0EF968A3F`
- `04_generative.tex`: `FBD5181B70729B17BA5420714E97EE84763835C2470029CC02F38B4DFFD0A18B`
- `06_gaussian.tex`: `1FD385BF899B4A719FAA212580EA6E2CD0B90EE7ED19A72EE6D184DCBFABC916`
- `06_general_coarsegraining.tex`: `5E7028EBCD5B2A311F67E3AFA39AED116CE357C47284DDE4E92808B07E9E0E79`
- `08_infogeometry.tex`: `0B91582CAE8E540C96E89CCD4AFAF591A3882998F26D7C493F62280688CA3BDC`
- `09_coarsegraining.tex`: `6D6A3BA9FCD2FCC001B97AC6DDF225CE4B23401A92312A25810816F196328911`
- `11_obstructions.tex`: `0895618EC0D2232015FF9ED3223AEE9C4B26DD342F8CAB1275E13DD27DB714CA`
- `12_philosophy.tex`: `5E717AD6C701CAA479A91308CF3C789FB3D9F56397C36FA88A06A399D8221F01`
- `appendix_notation.tex`: `DCE27D4833FF7F84944EFDB1EDABBB541B07F06DCA6327470B91362439DB9DB9`
- `appendix_claim_ledger.tex`: `92E4ED2910C31F2DB2E635A8430B7B2D1ADD4D5D1B89A3FA05DD50B5D34655AA`
- `references.bib`: `EA0F0B4F2800A0E711F246689CA8D54E2F57EF445B0C34491D5A3A06687A8B41`

## Mechanical results

A read-only UTF-8 scanner recomputed the following facts over the ten changed
TeX files and the full chapter set:

- unescaped brace depth ended at zero and never became negative in every
  changed TeX file;
- begin/end environment multisets agree in every changed TeX file;
- all changed files contain zero banned `\,`, `\;`, or `\!` spacing macros,
  zero checked British-English spellings, and zero mojibake markers;
- the full manuscript has 1,033 unique explicit or heading-defined labels,
  zero duplicate definitions, and zero unresolved `ref`, `eqref`, `Cref`,
  `cref`, `autoref`, or `pageref` targets;
- the bibliography has 460 unique keys, zero duplicates, and zero missing keys
  among manuscript citations;
- the Task 6 philosophy diff adds 13 tags on 13 separate lines: three
  `DEFINITION`, two mathematical `ESTABLISHED`, five `NOT-CLAIMED`, and three
  `OPEN`, with no doubled added-line tag;
- `K(x,\mathsf Y)=1`, Campbell's issue number and DOI, and the compact-closure
  notation are present; the removed `sec:geo-induced-connection` label and the
  stale averaged-connection phrases are absent; and
- `git diff --check` exits zero.  Its only messages are Git's expected
  LF-to-CRLF working-tree conversion warnings.

The aggregate scanner verdict is `PASS`.  These checks establish syntax,
inventory, and source-scope facts only; the mathematical claims are closed by
the separate derivation and primary-source artifacts.

## Falsification conditions

This artifact is stale if any bound source byte changes.  A nonzero brace or
environment imbalance, duplicate or missing label/key, missing explicit kernel
normalization, stale connection credit, newly added doubled status, banned
spacing/language hit, or nonzero `git diff --check` result refutes its `PASS`
verdict and requires regeneration.
