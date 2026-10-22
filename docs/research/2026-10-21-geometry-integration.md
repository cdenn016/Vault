# Pullback geometry and inheritance integration

Date: October 21, 2026.

The accepted recommendations in [the theory recovery report](<C:/Users/chris and christine/Desktop/MultiAgentELBO/docs/reviews/2026-10-21-theory-recovery/REPORT.md>) have been integrated into the live `manuscripts/MAgent_Theory_2.0/` package and its physicist's companion. This is manuscript implementation following that review. No new investigator panel, adversarial adjudication, numerical experiment, GPU operation, or Lean work was performed.

## Geometric construction

The new `chapters/02_geometry.tex` follows the interactions chapter and precedes the dynamics. Its regular tier uses general probability laws in admitted finite-dimensional statistical families with quadratic-mean differentiability and a positive Fisher metric. It does not impose Gaussian closure. The full joint-law Fisher metric is distinguished from marginal and product metrics, with a binary correlation example showing the information omitted by fixed marginals.

The chapter defines the covariant vertical first jet, proves passive gauge covariance and the dependence on the chosen connection, and states the stronger regularity needed for the transported relative-entropy expansion. It separates the radical quotient of tangent spaces from descent to a quotient manifold. A rank-one contact-form example shows why constant rank alone does not give an integrable kernel.

Collective Fisher least squares determines a minimizing connection class modulo infinitesimal isotropy. The normal equation, residual metric, change-of-connection cost, and aggregate-jet construction are proved with the stated smoothness, rank, equivariance, and quotient qualifications. Existence of an admissible full-rank jet is kept separate from full rank of the actual section and its persistence under dynamics.

The fixed-channel theorem proves the score projection and exact conditional-covariance Fisher loss under quadratic-mean differentiability. Local score recoverability is distinguished from recovery of the full statistical experiment. A varying channel has an additional score contribution. The fine/coarse base comparison retains its signed horizontal-defect terms; zero defect is a sufficient condition for contraction, not a necessary one. The collective-connection retention proposition gives the exact mixed-loss criterion and the additional isotropy condition for equality of minimizing classes. A fixed equivariant Gaussian-noise example demonstrates that Fisher contraction alone does not preserve the selected connection.

The new `appendices/determinant_example.tex` keeps the determinant-induced Lorentzian metric and circle construction as optional specializations. They require additional representation, rank, scale, and bundle data. The positive Fisher metric does not generate Lorentzian signature, and this appendix does not establish physical spacetime or a dynamical selection mechanism.

## Prediction, inheritance, and formation

`chapters/04_prediction.tex` adds common-family recovery and its exterior-independence consequence with a proof. `chapters/05_inheritance.tex` adds a metric sufficient condition for gradient inheritance, with the conformal time factor explicit; conditional separator gluing; and an exact causal history relative-entropy decomposition, allowing infinite values without subtracting infinities. The existing finite-filter derivation remains in the supplement.

The inheritance chapter also proves the finest independent and conditionally independent partition statements within their declared setting. An arbitrarily weak Ising interaction illustrates discontinuity of exact independence-based selection, and the symmetry statement identifies the obstruction to choosing a single hard partition equivariantly. These results constrain selectors; they do not derive persistent organization from the original smooth KL dynamics.

The existing boundary construction is explicitly distinguished from a smooth dimension reduction of the context base. The remaining research tasks are to construct a smooth recursive parent family satisfying dynamical, response, and geometric inheritance together, and to determine whether the original dynamics selects and maintains its memberships, comparison data, and actual geometric rank.

## Companion and package changes

The companion geometry chapter now precedes its dynamics chapter. It explains joint Fisher information, contextual pullback, collective connection selection, and information loss under compression. Worked examples include Bernoulli pullback geometry, two normal locations with a common translation, and a channel that changes the minimizing connection. The prediction and inheritance chapters explain the corresponding recovery, gradient, memory, and selector results.

The package entry points, abstract, foundations, dynamics cross-reference, outlook, base-connection appendix, notation tables, README, and authoring contract were updated to reflect this structure. Seven external bibliography entries were added: Ay, Jost, Le, and Schwachhofer (2018); Pollard (2013); Guichardet (1984); Lewis, Nigam, and Olver (2003); Gray (1990, first-edition electronic version); Ryabko (2017); and Chan et al. (2016). The supplement source and PDF were unchanged.

## Document validation

TeX Live 2025 `latexmk` completed successfully for the main manuscript and companion. Their final PDFs contain 83 and 36 pages, respectively. Both final logs contain no warnings, unresolved references or citations, duplicate-label warnings, missing-character warnings, or overfull/underfull boxes. The final source check covered 39 TeX files, 410 labels, and 24 distinct cited keys; it found no missing inputs, unresolved source references, duplicate labels, missing bibliography keys, prohibited spacing macros, or trailing whitespace.

All 119 final pages were rendered with Poppler and inspected in contact sheets. Selected mathematical pages and the companion contents were also inspected at readable resolution. Layout edits removed new short overflow pages while preserving theorem statements and proofs. The existing short endpoint page in the companion's earlier fusion chapter was left unchanged. These checks establish successful compilation and the inspected layout; they are not an independent mathematical verification.

The build evidence is local under `manuscripts/MAgent_Theory_2.0/build/`: `geometry-source-checks.json`, `geometry-final-validation.json`, the two `*-geometry-build.txt` logs, and `geometry-final-preview/`. The compiled PDFs were copied to the package's adjacent canonical PDF paths. The existing daily edit log was appended, and every previously existing byte of its entry prefix was preserved. The other 75 pre-existing changed files were preserved byte for byte. No commit, push, or merge was part of this integration request.
