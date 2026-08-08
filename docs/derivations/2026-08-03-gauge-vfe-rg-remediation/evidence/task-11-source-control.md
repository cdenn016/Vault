# Task 11 source-control and adversarial closure

## Scope

This record closes only the source-level notation, status, cross-reference,
terminology, and citation obligations assigned to Task 11. It does not claim a
TeX/PDF build, regenerated numerical evidence, manifest closure, or terminal
release. The verification ledger for the revision containing this record binds
the complete source tree; the claim ledger separately binds this artifact by
its committed Git-blob SHA-256.

## Closed source claims

The following six atomic claims are closed by direct source inspection and the
mechanical inventories below.

1. `minor-ch9-symbols`: Chapter 9 defines (B), (B_\perp), (G), (Q),
   and `\operatorname{pdet}` before use and distinguishes (Q) from the
   recognition-law notation.
2. `minor-rg-notation`: the notation appendix types the measure-pair, action,
   interaction, score, configuration, quotient, comparison, cocycle, beta, and
   block-scaling tiers, including domain/codomain and scale indices.
3. `minor-additive-constants`: the fixed-action-ray shift is
   (c_{\mathrm{ray}}(b)), while the cut-edge count is
   (n_{\mathrm{cut}}(b)); no live manuscript source uses the former shared
   glyph (c_b).
4. `minor-abelian-label`: the counting-to-heat implication is explicitly the
   Abelian/Karamata direction, with the zero mode removed and no Tauberian
   converse claimed without additional hypotheses.
5. `minor-ch11-crossref`: Chapter 11 points the cut-closure condition to
   `eq:cg-cut-excess`, and the global label/reference inventory resolves it.
6. `minor-status-scope`: each prose claim has one visibly governed status; the
   status taxonomy is the sole explicit table exception, the RG relevance
   trichotomy is a definition, and the operational-trace route remains open
   with stated settlement conditions.

## Adversarial probes and repairs

- The phrase "connection-compatible bundle morphism" was treated as undefined
  until the Chapter 6 bridge explicitly required both
  `eq:pb-isotropy-criterion` and `eq:pb-coarse-related-sections`.
- A complete-graph counterexample with a (b)-vertex block facing a
  (b^2)-vertex complement gives (n_{\mathrm{cut}}(b)=b^3), so the statement
  (s=2) was restricted to cuts between two (\Theta(b))-sized blocks.
- Nonnested partitions reverse the determinant-gap ordering under different
  covariance pairings. The source therefore asserts monotonicity only for
  comparable refinements and calls the coarsest endpoint a generally
  nonunique minimizer, not a selector.
- The source-level Fisher theorem was attacked through the full Le Cam DQM
  singular decomposition. Lifting (P_h^\perp) through an everywhere
  normalized parameter-independent kernel preserves its
  (o(\lVert h\rVert^2)) mass and singular support, while the absolutely
  continuous square-root remainder is unchanged by the joint lift. Pollard's
  measurable-statistic preservation theorem then yields the conditional score
  and the exact Fisher conditional-variance defect.
- Working-tree byte hashes were rejected as platform-dependent provenance.
  The Task 10 table now binds 11 committed Git blobs, and independent
  recomputation passes all 11 forward bindings, the source-map binding, and
  all six reverse proof bindings.

## Mechanical inventories

- 24 TeX source files scanned.
- 1,275 unique labels; 1,217 references; zero duplicate labels and zero
  undefined references.
- 132 citation uses against 466 unique bibliography keys; zero missing or
  duplicate keys.
- 825 status tokens; zero invalid statuses, zero multi-status prose
  paragraphs, and zero substantive prose after a terminal status. The 38
  residual lexical tails are structural commands only (`\medskip`, `\label`,
  or `\end{description}`).
- 12 literal `NUMERICAL` tokens and 12 semantic entries in
  `verification/claims.json`; every file, occurrence, and line binding is
  exact.
- JSON parsing, placeholder/shortcut scans, American-English scans, and
  `git diff --check` pass.
- The committed-blob provenance checker reports 21 passed checks and zero
  failures: 11 forward rows, one source-map ledger binding, two reverse proof
  bindings in the claim ledger, and four reverse proof bindings in the
  adversarial report, plus their structural count checks.

## Deliberately unclosed boundaries

Seven ledger claims remain `CANDIDATE` after this source pass: the compound
target; PB-1--PB-4/current-ledger provenance; numerical determinant-gap stress;
manifest fail-closed behavior; rendered-PDF keyword metadata; rendered
unbreakable status tokens; and generated auxiliary-file freshness. They belong
to Tasks 13--19 or require the Task 14 build and are not promoted by source
inspection alone. `release.json` therefore remains nonterminal.
