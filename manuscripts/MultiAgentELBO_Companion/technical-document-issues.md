# Issues noticed in the technical documents while writing the companion

The companion's drafters (Claude Opus 5.5) reported these while reading `../MultiAgentELBO_Theory/`
in September 2026. Nothing here was changed in the theory folder. Items marked "checked" were
confirmed by the cross-model checker (Claude Fable 5.1) or against the source by the integrator; the
rest are one drafter's reading and should be confirmed before editing. None is a false theorem.

## Statement or proof text

- `rem:rg-memory-partial-refresh` (c08), proof: "Only state 2 moves under M, to 3 with probability
  1/2" is inaccurate; since a_32 = a_23 = 1/2, state 3 also moves to 2, and the proof uses "since it
  moved from 3". The displayed probabilities and the (1 − ω)/3 gap are correct.
- `rem:rg-two-agent-example` (c11) says the multipliers obey "the bound 3^2 − 1 = 8" of
  `prop:rg-interaction-native-growth-bound`; that proposition bounds by the target size, here
  |V_1| = 1, giving 3^1 − 1 = 2. The 8 is the source extraction constant.
- `prop:full-graph-downward-coupling` (c12, near line 652) writes `\mathbb P^\ell_N`; should be
  `\mathbb P^\ell_{\mathfrak N}`.
- `prop:rg-formation-endogenous-cycle` (a): the least rate × resolution² / T "is 4ε^{-4}"; strictly
  (4+T)ε^{-4} or (4+5T)ε^{-4}, so "at least" would be exact.
- `rem:gauss-membership-frame-dependence` (G) lists generalized eigenvalues of (L, Λ) among
  frame-independent membership criteria, but L exists only after an L + A split made in a chart where
  membership holds. Counterexample (N = 2, K = 1): [[2,−1],[−1,2]] with W = 1, A = (1,1) has pencil
  spectrum {0, 2/3}; its reframing by diag(1,2), [[2,−2],[−2,8]], is in the family with W = 2,
  A = (0,6) and has spectrum {0, 1}.
- `ch:gaussian-introduction` (G0) says positive additive rules are forced linear "under a
  measurability hypothesis"; `prop:grg-positive-additive-linear` has no such hypothesis (positivity
  gives monotonicity).

## Opening and summary wording stronger than the statements

- c01 opening: "forms successive meta-agents under free-energy descent with learning" implies that
  learning drives formation; the c13 scope paragraph and `rem:rg-formation-saturation` say the
  coherence conclusion holds with the record off and the parameter frozen (checked).
- c13 opening calls `conj:phil-contrast-formation` "the conjecture of the interpretation chapter"
  (stale; it is a theorem), and says "two witnesses answer yes" to a question about succession with
  own-law learning, which the four-cycle witness (one level, no learning) does not answer.
- c05 opening and physicist's summary state the exact potential game without the singleton,
  product-profile restriction of `cor:obs-potential-game` (checked; the checker judged this within
  the meaning of a potential game).
- c06: the transformer correspondence row "value and output maps, residual" is marked derived; what
  `prop:obs-selective-receiver-update` derives is a tied value map of a different model (checked).
- c06 physicist's summary: "the seed of symmetry breaking in the two-timescale and formation
  chapters" has no statement behind it (checked).
- c09 opening: "information of order N² at a tie among N agents" is proved for a fixed finite label
  set with supplied extensive log masses (checked).
- c10 physicist's summary: marginals have one parent "exactly when" their transported laws coincide in
  an invariant law; `thm:cg-holonomy-kl-marginal` needs attainment for that.
- c04 physicist's summary: "reciprocal latent conditionals define no joint" overstates
  `prop:gen-gibbs-counterexample` ("need not give a finite Z_X").
- c02 physicist's summary: "in lattice gauge theory only closed-loop products are invariant" holds
  for pure gauge theory; with matter, dressed links are invariant (Supplement B's
  `open:rg-lattice-typing` itself uses the Z_2 gauge–Higgs dressed link).
- c14 opening says it "proves a proposition and a theorem"; it also states `cor:phil-joint-selection`,
  and eight further propositions of the line are in the appendices. Its summary of
  `prop:phil-selected-pair-persistence` omits the mobility cap ε_L ≤ T².
- `sec:intro-reading-map` and `sec:intro-conventions` (c01) name the three coarse operations "Markov
  channels, energy restriction, and parameter aggregation"; `sec:cg-three-operations` treats
  pushforward, precomposition, and Galerkin restriction (checked).
- `sec:rg-hypergraph-closure` (c11) is titled "Exact closure generically requires hyperedges";
  genericity is shown only within the star family of `prop:rg-hyperedge-generation` (d).
- Text after `hyp:pb-markov-morphism` (c07): "no such form across precisions" is broader than
  `prop:ig-galerkin-pushforward` (v), which fails only when range(ΛS) varies.
- `open:rg-lattice-typing` (B7) and its row in `tab:base-open` cite "the countable-index projective
  and DLR hypotheses of ch:agent-network-rg"; main chapter 11 contains neither. Part B-II's title
  mentions infinite networks, but no infinite agent network is constructed there.

## Scope gaps worth a decision

- c02 declines normalizability of loop-penalty link laws for noncompact G but records no open
  problem, although GL(K) is the program's target.
- `open:rg-formation-general` is posed only outside the gated family, and `prop:rg-gated-depth-one`
  is stationary only, so a transient second coalescence inside the gated family is neither excluded
  nor posed.
- Supplement G never treats complex Gaussians, Hermitian precisions, or GL(K,C) frame groups.
- MT `open:cg-natural-selector` says the Gaussian recognition costs select trivial endpoints or need
  an external coefficient; the combined cost D_tie + D_fact of `cor:restrict-combined-costs-add`
  (unit coefficients, terms moving in opposite directions under merging) is never examined as a
  selector.
- `hyp:gauss-global-interaction` requires membership in the link-trivializing chart, strictly stronger
  than law-level membership; G0's "requires A_i + O_i ⪰ 0" is chart-relative.

## Notation and labels (SPEC R7)

- Glyph collisions: Δ (discarded information in `eq:rg-vfe-chain-rule`, cut excess in
  `eq:cg-cut-excess`); W (label weights in c09, edge forms in c10); `\operatorname{par}` (parity in
  c07, parent map in c08); `\mathsf a` (rate factor and proposal weights); M (Kron pivot G7,
  biadditive factor G9, star iteration G10); the regime parameter as ε, ξ = T^{1/8}, and T^{1/8} in
  the four-cycle continuation.
- `open:cg-cut-compression` is an ESTABLISHED no-go carrying an `open:` label, and several scope
  paragraphs cite it in the open-items position.
- `def:rg-regular-finite-filter` uses ε before the open problem that introduces it.
- c07 `sec:hist-canonical-dependence-selection`: the reference-relative replacement is a
  claim-bearing sentence with no numbered statement (R4).
- `prop:geo-active-image-point` reads "one copy A ≅ G of the passive vertex group"; intended "one
  copy of G inside" it.
- Build artifact: in `main.aux` every heading-macro label's nameref title is the previous
  statement's title (`\resultheading` places `\label` before `\paragraph`). Numbers and cleveref
  types are correct; only `\nameref` would print wrong titles.

## CONTENT.md drift

CONTENT.md no longer matches the .tex in several places: the three agreements called "pairwise
independent" (contradicts `prop:geo-three-agreements` (ii)); a "differential identity" for the
local–global potential (the theorem is a finite-difference identity); a Dobrushin bound and
autonomous endomorphisms placed in c09 (the bound is in c11); an I-projection result in c07 that the
chapter does not contain; the memory duration called a STANDARD citation (it is ESTABLISHED with a
proof); chapter 14's "one theorem-type statement"; chapter 15 covering matrix-weighted consensus and
gauge fixing (it does not); G4's "volume term" (none in G4); a λ-family and an Amit-locator condition
in G that the .tex lacks; and "rank is an established discrete label" in Supplement B (no such
statement). The numerical index of Supplement B notes that the implementation behind its three
NUMERICAL remarks is retired and the values were not recomputed.
