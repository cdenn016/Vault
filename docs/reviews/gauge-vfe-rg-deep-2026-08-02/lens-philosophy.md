# Lens: philosophy of science — claim-status discipline and framing

**Reviewer lens.** Falsifiability, scope, theory-ladenness, progressive-vs-degenerative, novel-construction-vs-rediscovery,
manuscript-as-authority circularity — applied here as **claim-status discipline**: does each `\status{}` tag match what is
delivered, do the interpretive chapters respect the fences the mathematical chapters set, and is the open-obligation ledger
complete?

**Chapters read in full:** `01_introduction.tex`, `11_obstructions.tex`, `12_philosophy.tex`, `appendix_claim_ledger.tex`,
`appendix_numerical_provenance.tex`. **Skimmed:** `main.tex`, `SPEC.md`, plus targeted greps across all 20 chapter files.

**Out of scope per `00-settled-ground.md`:** every declared-open obligation (continuum limit, physical-time identification,
physical-law identification, etc.), and every pass-1/pass-2/LG/RG/PB verified item.

**Overall adjudication.** The epistemic contract is unusually well built and mostly honored. The falsifiability posture is
exemplary and I found no manufactured empirical content (see *Falsifiability assessment*, below). The defects are of one
family: **prose-level claims about what other chapters prove, made without a theorem-level `\Cref`, one of which is now
false because its target was deleted**; plus **four unindexed open obligations**, one of them load-bearing; plus **two
philosophy citations that do not support the sentences citing them**.

Findings are ordered by severity. Thirteen findings: 2 high, 6 medium, 5 low. No critical.

---

## P-1 — Chapter 12 attributes to the geometry chapter a proof that does not exist

- **claim:** "The geometry chapter proves that curved and flat averaged connections are mathematically possible, but does
  not choose a canonical connection or construct an observable sensitive to it."
- **location:** `12_philosophy.tex:101-102`
- **severity:** high
- **status:** the sentence sits immediately after `\status{CONJECTURE}` (`12:100`) and functions as the *established
  premise* on which that conjecture rests. It should be **deleted**, or replaced by a `DEFINITION`-grade statement of what
  Chapter 2 actually declares.
- **evidence:**
  - `02_geometry.tex` contains **zero** occurrences of `averag` (whole-file grep). A manuscript-wide grep for `averag`
    returns only `05b:428`, `05d:247,253` (outside-averaged conditional VFE), `07b:494,501` (Haar/rotation average
    counterexample), `09:708,710,714,721` (Haar orbit average), `appendix_notation:112`, and `12:100` itself. **There is
    no averaged-connection construction anywhere in the manuscript.**
  - `02_geometry.tex` contains exactly **one** occurrence of `curvature`, at `02:368-370`, and it says the opposite of
    the attributed claim: *"The connections in \eqref{eq:geo-principal-connections} are chosen data; no curvature or
    transport is inferred from the agent frames."*
  - The complete numbered-result inventory of Chapter 2 (grep of `*heading` macros) is: `def:geo-context-base`,
    `def:geo-principal-systems`, `hyp:geo-smooth-tier`, `def:geo-associated-bundles`, `def:geo-cross-morphisms`,
    `prop:geo-intertwining-cross-map`, `def:geo-connections`, `def:geo-covariant-defects`, `def:geo-agent`,
    `prop:geo-moment-pushforward`, `hyp:geo-common-trivializations`, `def:geo-graph-links`,
    `prop:geo-trivializing-criterion`, `hyp:geo-graph-base-transport`, `hyp:geo-flat-links`. **No result concerns
    connection curvature.** `def:geo-connections` (`02:266-271`) *declares* `\omega_b,\omega_m` as chosen data.
  - `02:621` explicitly blocks the inference the sentence needs: the pointwise flat-link specialization does not imply
    "that the principal connection is flat or that the two channel frames coincide."
  - **Provenance of the error.** The prior verification ledger records `R17`: *"Proposition 2.31 constructs an averaged
    connection and gives a sufficient flatness condition, but does not prove nontrivial curvature or holonomy."* `R17`
    was discharged by **removing** the proposition from Chapter 2; the dependent sentence in Chapter 12 was left standing.
    It now overclaims **twice**: the proof does not exist, and even the deleted proposition did not deliver the *curved*
    half.
- **fix:** replace `12:101-102` with:
  "\Cref{def:geo-connections} declares $\omega_b$ and $\omega_m$ as chosen data and infers no curvature from the agent
  frames; nothing in this document selects a canonical connection or constructs an observable sensitive to its holonomy."
  The `CONJECTURE` at `12:100` then stands on its own, which is where a conjecture belongs.
- **falsifies:** reinstating a labeled existence result in Chapter 2 for curved and flat connections on `P` and citing it
  at `12:101` by theorem-level `\Cref` would refute this finding.

---

## P-2 — The open-obligation ledger is incomplete: the RG-monotone obligation is not indexed

- **claim (ledger charter):** "This appendix collects the manuscript's unresolved obligations in one place."
  (`appendix_claim_ledger.tex:4`)
- **location:** `appendix_claim_ledger.tex` (omission); source obligation at `08_infogeometry.tex:333-336`
- **severity:** high
- **status:** the body statement is correctly tagged `\status{OPEN}`; the **ledger** is what is defective.
- **evidence:**
  - `08_infogeometry.tex:333-336`: *"Whether a monotone functional decreases under the full declared aggregation/RG map
    is open. Closing it requires either exhibiting a Markov kernel whose pushforward realizes the map, after which the
    classical theorem applies verbatim, or exhibiting a Lyapunov functional and proving its decrease directly.
    `\status{OPEN}`"*
  - Grep of `appendix_claim_ledger.tex`: `monotone` occurs **once**, at line 82, inside *Bayesian-RG bridge*, and it is
    about comparing this flow with **BKS**, not about this flow's own monotone. `Lyapunov` occurs **once**, at line 120,
    inside *Intrinsic scale selection*, as one candidate route to a **scale selector**. Neither states the obligation.
    A monotone that runs to an endpoint would in fact *fail* to supply a nondegenerate selector, so the two obligations
    are not merely differently worded — they pull in opposite directions.
  - **Why it is load-bearing.** `prop:ig-pullback-vs-pushforward` (`08:222-234`) proves the coarse operator is a
    **pullback along an inclusion of mean submodels**, not a Markov pushforward, and that the two differ by a PSD Schur
    term with the restriction larger in Loewner order. The standard reason to believe an RG map loses information in one
    direction — data processing — is therefore **provably unavailable here and is not replaced**. The document is titled
    "…and Renormalization"; `12:233-241` proposes a cross-scale empirical test that presumes a directed flow; and the
    ledger nowhere tells a reader that the arrow itself is unestablished.
- **fix:** add to `appendix_claim_ledger.tex` §"General coarse maps and renormalization":
  "**Monotone for the declared coarse/RG map (open).** The declared aggregation operator is a pullback along an inclusion
  of mean submodels (`\Cref{prop:ig-pullback-vs-pushforward}`), not a Markov pushforward, so data processing supplies no
  monotone. Closing this requires either a Markov kernel whose pushforward realizes the map, after which the classical
  contraction theorem applies verbatim, or a Lyapunov functional with a proof of decrease. `\status{OPEN}`"
- **secondary omissions in the same ledger** (fix by adding one line each):
  1. `06_general_coarsegraining.tex:415-417` — *"KL equality does not automatically make its Bayes recovery equivariant;
     an equivariant conditional version is an additional hypothesis or theorem, especially for noncompact groups.
     `\status{OPEN}`"* The ledger's *Partition selection and experiment-level recovery* item attaches "gauge-compatible"
     to the **selector**, not to the **recovery kernel**, and says nothing about noncompact `G`.
  2. `12_philosophy.tex:137-141` — ontic structural realism, tagged `\status{OPEN}` with an explicit closure condition
     ("elimination of whatever is unidentifiable"), is absent from the ledger's §"Geometric and physical interpretation".
     The ledger's closing paragraph disclaims *ontological closure*, which is a different thesis.
  3. `10_renormalization.tex:519-521` — *"A gauge-invariant real-space block selector, zero-mode treatment, and entropy
     normalization remain open."* The selector is indexed; **zero-mode treatment and entropy normalization** are not.
- **falsifies:** a ledger entry naming the monotone obligation, or a proof/counterexample in the body, closes this.
- **note (adversarial self-check):** I checked all 40 body `\status{OPEN}`/`\status{CONJECTURE}` sites against the 21
  ledger obligations. Everything else maps cleanly: `03:305`→continuum law theory; `04:389`, `05:523`, `05a:267`,
  `05a:364`→regular frame-coordinate quotient / optimization and projection; `05c:842`, `05d:762`→fine–coarse
  semiconjugacy; `06:429`, `07gr:562`, `10:521`→partition selection; `06:658`, `07gr:498`→infinite-volume RG limit;
  `07gr:466`, `10:285`, `10:389`→two-index limits and universality; `07gr:554`→Bayesian-RG bridge;
  `07restrict:327`, `09:909`→intrinsic scale selection; `08:238`→information-geometric transfer; `09:209`→admissible cone
  classification; `09:329`, `09:499`, `11:411`, `12:219`→nonflat-link compression; `10:238`→scalarized attraction;
  `10:483`, `10:574`→stochastic inverse RG; `11:315`→update robustness; `12:96`→graph-to-base identification;
  `12:100`→operational base holonomy; `12:209`, `12:242`→physical-law identification. The ledger is 4 items short of
  complete, not structurally broken.

---

## P-3 — `esfeld2008moderate` is cited in support of the position it was written to reject

- **claim:** "Ontic structural realism, in which structure is all that exists, is available but unsupported
  \citep{Ladyman2007,Ladyman2014,esfeld2008moderate}."
- **location:** `12_philosophy.tex:136-139`
- **severity:** medium
- **status:** `\status{OPEN}` on the claim is fine; the **citation** is the defect.
- **evidence (primary source):** Esfeld & Lam, *Moderate structural realism about space-time*, Synthese 160:27-46 (2008),
  abstract: *"According to moderate structural realism, objects and relations (structure) are on the same ontological
  footing, with the objects being characterized only by the relations in which they stand. This paper sets out a moderate
  version of metaphysical structural realism that stands in contrast to both the epistemic structural realism of Worrall
  and the — radical — ontic structural realism of French and Ladyman."*
  SEP, *Structural Realism* (Ladyman): Esfeld "rejects eliminativism", holding "(a) relations require relata but denies
  that (b) these relata must have intrinsic properties over and above the relations in which they stand"; moderate
  structural realism maintains "things and relations but neither is ontologically primary or secondary."
  The manuscript's sentence characterizes OSR as "structure is all that exists" — precisely the eliminative thesis Esfeld
  & Lam construct their paper to avoid. `Ladyman2007` and `Ladyman2014` do support the characterization; `esfeld2008moderate`
  contradicts it.
- **compounding point:** the manuscript's very next sentence — "The manuscript proves invariance or unidentifiability, not
  elimination of whatever is unidentifiable" — **is** the moderate position. So the one citation that fits the
  manuscript's own result is attached to the reading it disclaims, and the position it actually occupies goes uncited.
- **fix:** `\citep{Ladyman2007,Ladyman2014}` for eliminative OSR; then add: "A moderate structural realism, on which
  relata exist but are characterized only by the relations in which they stand \citep{esfeld2008moderate}, is the reading
  the invariance and unidentifiability results actually fit; this document does not argue for it either.
  `\status{DEFINITION}`"
- **falsifies:** a passage in Esfeld & Lam 2008 endorsing "structure is all that exists" would refute this.

---

## P-4 — The van Fraassen citation does not support the idle-wheel criterion

- **claim:** "This chapter adopts an explicit idle-wheel criterion: a posit with no trace in any declared observable is
  removed by parsimony. `\status{DEFINITION}` This is an interpretive standard in the spirit of empirical adequacy
  \citep{vanFraassen1980}, not a theorem."
- **location:** `12_philosophy.tex:65-68`
- **severity:** medium
- **status:** `DEFINITION` is the right tag for declaring a criterion; the **attribution** is wrong.
- **evidence (primary source):** van Fraassen, *The Scientific Image* (1980): acceptance of a theory "involves as belief
  only that it is empirically adequate" (p. 12), and theories are to be construed **literally**, since "a literal
  construal may elaborate on what that something is, but will not remove the implication of existence" (p. 11).
  Constructive empiricism prescribes **agnosticism about unobservables while retaining them in the theory**; it does not
  license removing a posit, and van Fraassen treats parsimony/simplicity as a *pragmatic*, not epistemic, virtue.
  An eliminative "no observable trace ⟹ remove" rule is a verificationist/Occamist principle, not empirical adequacy.
- **why it matters here:** the criterion is doing real work — §`sec:phil-noumenon` uses it to decide when the noumenal
  reading "earns its keep". Under the cited doctrine the noumenal posit would simply be **retained and disbelieved**, and
  the section's question would not arise in that form. The citation lends empiricist authority to a stronger move than the
  cited author makes.
- **fix:** "This is an eliminative parsimony rule adopted here by choice. It is stronger than constructive empiricism,
  which prescribes agnosticism about unobservables while retaining them in a literally construed theory
  \citep[11--12]{vanFraassen1980}. `\status{DEFINITION}`"
- **falsifies:** a passage in *The Scientific Image* recommending removal of traceless posits would refute this.

---

## P-5 — "Supports" is an evidential verb the chapter's own standard forbids, and it consumes an obligation the ledger declares open

- **claim:** "This supports an epistemic structural-realist reading in Worrall's sense \citep{Worrall1989}."
- **location:** `12_philosophy.tex:132-133`
- **severity:** medium
- **status:** `\status{DEFINITION}` (tag placed at `12:136`, governing the paragraph). The verb "supports" asserts more
  than `DEFINITION` licenses; it should read "is compatible with / is the formal analogue of".
- **evidence:**
  - The chapter's own standard, `12:10`: *"Availability is not support, and no preference below changes a theorem proved
    in the preceding chapters."* The parallel sentence three lines later gives OSR "available but unsupported". Nothing in
    the mathematics grounds the asymmetry between the two verbs.
  - What the mathematics delivers (`eq:phil-invariants`): a list of quantities invariant under a **declared redundancy
    group of the manuscript's own formalism** — ELBO/KL values, `rank M`, `spec(L,Λ)`, passive-coordinate classes of the
    pullback tensors, conjugacy classes of graph-link holonomies.
  - Worrall 1989 argues a **diachronic** thesis: what is retained of the unobservable world **across theory change**
    (Fresnel's equations surviving into Maxwell's theory), motivated by the pessimistic meta-induction plus the
    no-miracles argument. Invariance under a gauge group internal to one fixed formalism is a different invariance and is
    not evidence for the epistemic thesis. Getting from the former to the latter requires identifying the formalism with
    a target system — which is `\ref{claim:physical-law-identification}`, declared `OPEN` by this manuscript. So the word
    "supports" quietly draws on an obligation the ledger records as unpaid. This is the one place in Chapter 12 where the
    manuscript's own framework is used as authority for an epistemic conclusion about the world.
- **fix:** "The list \eqref{eq:phil-invariants} is the formal analogue of the structural residue that epistemic structural
  realism takes to survive theory change \citep{Worrall1989}. It is an invariance inside one declared formalism, and it
  bears on the epistemic thesis only after `\ref{claim:physical-law-identification}`. The reading is available, not
  supported. `\status{DEFINITION}`"
- **falsifies:** a demonstration that the listed invariants are retained across a **change of theory**, not a change of
  frame, would earn "supports".

---

## P-6 — Chapter 12 declares three tags and uses six; its single `ESTABLISHED` has no theorem-level warrant

- **claim:** "This chapter proves no mathematical result. … A reading carries `\status{DEFINITION}`; the sole
  interpretive restriction used later, observational closure, carries `\status{HYPOTHESIS}`; and unresolved empirical or
  interpretive consequences carry `\status{OPEN}`."
- **location:** `12_philosophy.tex:4-10`; violating uses at `12:40` (`ESTABLISHED`), `12:43,51,198,205,210`
  (`NOT-CLAIMED`), `12:100` (`CONJECTURE`)
- **severity:** medium
- **status:** the chapter's declared tag inventory is incomplete, and `SPEC.md` §5c states flatly: *"**No interpretive
  claim may carry `ESTABLISHED`.**"*
- **evidence:**
  - `12:36-40`: "The informational pullbacks of \Cref{ch:pullback-geometry} can give this fixed base an agent-, section-,
    and connection-relative positive-semidefinite tensor. Passive gauge invariance of that tensor does not make it
    independent of the chosen connection, and degeneracy can leave contextual directions unmeasured.
    `\status{ESTABLISHED}`" — the content is true and is proved in Chapter `05c`, but the warrant offered is a
    **chapter-level** `\Cref`, not `thm:pb-pullback-gauge-invariance` / `thm:pb-pullback-rank-quotient`.
  - This is exactly the referencing style that let **P-1** survive: three prose chapter-descriptors appear in Chapter 12
    — "The projective-limit chapter" (`12:32`), "The geometry chapter" (`12:101`), "The obstruction chapter" (`12:186`).
    The first names **no chapter at all** (the material is `sec:cg-projective-laws` inside `ch:coarsegraining`); the
    second attributes a proof that does not exist. Prose descriptors do not break at build time; `\Cref` does.
- **fix:** (a) rewrite `12:6-9` to enumerate all six tags and to state that `ESTABLISHED` in this chapter marks **only
  verbatim restatements of results proved elsewhere, cited by theorem-level `\Cref`**; (b) change `12:36` to
  `\Cref{thm:pb-pullback-gauge-invariance,thm:pb-pullback-rank-quotient}`; (c) replace every prose chapter-descriptor in
  Chapter 12 with a `\Cref`; (d) reconcile with `SPEC.md` §5c, which currently forbids what `12:40` does.
- **falsifies:** if `SPEC.md` §5c is amended to permit imported `ESTABLISHED` restatements with theorem-level citation,
  only (b) and (c) remain.

---

## P-7 — Misdirected cross-reference inside an `ESTABLISHED` paragraph (Chapter 11)

- **claim:** "At a level with at most two clusters, the pairwise cut-closure condition of
  \Cref{ch:gaussian-renormalization} requires their union, the whole population, to be trivializing."
- **location:** `11_obstructions.tex:401`, paragraph tagged `\status{ESTABLISHED}`
- **severity:** medium
- **status:** `ESTABLISHED` is defensible for the argument; the **reference target is wrong**.
- **evidence:** `ch:gaussian-renormalization` = `10_renormalization.tex`. That file has **zero** occurrences of
  `trivializ`, and its five occurrences of `cut` (lines 67, 159, 200, 468, 578) are none of them a closure condition.
  The condition lives in `ch:gaussian-coarsegraining`, `sec:cg-sheaf-closure`, `09_coarsegraining.tex:268-282`:
  "One group-valued coarse pair reproduces the cut exactly if and only if all cut twists coincide", with
  `Δ = A − BᵀC⁻¹B = Σ_e(Θ_e−Θ̄)ᵀW_e(Θ_e−Θ̄) ⪰ 0` at `eq:cg-cut-excess`. (The substance of `11:388` and `11:401` is
  correct: for two already-trivialized clusters, common cut twists and trivializing union coincide.)
- **fix:** `\Cref{ch:gaussian-renormalization}` → `\eqref{eq:cg-cut-excess}`.
- **falsifies:** a labeled pairwise cut-closure condition in Chapter 10 would refute this.

---

## P-8 — Untagged, unlocatable cross-chapter identification (Chapter 11)

- **claim:** "It is also the sufficiency statement of Chapter~\ref{ch:coarsegraining} read in the recognition direction:
  the statistic that the constituents supply to the apex is $\sum_i\Theta_i^{\top}R_i^{-1}y_i$, and
  \eqref{eq:obs-precision-addition} is the precision that statistic carries."
- **location:** `11_obstructions.tex:217`
- **severity:** medium
- **status:** **no tag at all**. `SPEC.md` §2.1: "A claim with no status is a defect." Should be `ESTABLISHED` with a
  one-line proof, or deleted.
- **evidence:** `ch:coarsegraining` = `06_general_coarsegraining.tex`. Its only two "sufficiency" statements are
  **negative**: `06:130` — "Without those simultaneous hypotheses, experiment-level sufficiency means directly that one
  parameter-independent `R` satisfies `P_θKR=P_θ` for all `θ`. Pairwise equality does not prove that stronger statement."
  — and `06:182` — "Fisher equality at one parameter is local score sufficiency, not global recovery", followed by a
  Bernoulli counterexample. Neither, "read in the recognition direction", yields the pooled statistic. The asserted
  Gaussian fact is true but elementary (it is the likelihood factorization of `eq:obs-star`); it is **not** an instance of
  the general theorem, and identifying the two lends a general-theory warrant to a quadratic-realization fact —
  precisely what `SPEC.md` §5d.5 forbids ("never use Gaussian notation as if it proved a theorem about all belief or
  model fibers").
- **fix:** replace with "Sufficiency of $\sum_i\Theta_i^\top R_i^{-1}y_i$ for $b$ is immediate from the factorization of
  \eqref{eq:obs-star}, in which the constituents enter the $b$-conditional only through that statistic.
  `\status{ESTABLISHED}`" — and drop the cross-chapter identification.
- **falsifies:** a labeled sufficiency theorem in `ch:coarsegraining` whose recognition-direction reading gives the pooled
  statistic would refute this.

---

## P-9 — `eq:obs-tension` states the coarsening condition at group level, where the criterion is at represented level

- **claim:** "$\text{standard coarsening needs}\quad \operatorname{Hol}(\gamma)=e_G \quad\text{on the cycles in its
  declared domain}$"
- **location:** `11_obstructions.tex:389-399`, `eq:obs-tension`, paragraph tagged `\status{ESTABLISHED}`
- **severity:** low
- **status:** `ESTABLISHED` claims more than the referenced criterion delivers.
- **evidence:** the criterion actually proved is on **represented** holonomy — `09_coarsegraining.tex:411-414`: "For a
  connected cluster, $f_I=K$ exactly when every represented holonomy … A nonfaithful representation can make represented
  holonomy [trivial while principal holonomy is not]"; and `SPEC.md` §5b: "Principal holonomy may nevertheless be
  nontrivial when the selected representation is not faithful." `Hol(γ)=e_G` is strictly stronger, and it contradicts
  Chapter 11's own channel-typing preamble (`11:6-16`).
- **fix:** `\operatorname{Hol}(\gamma)=e_G` → `\widehat\rho_b(\operatorname{Hol}(\gamma))=I`.
- **falsifies:** a proof that full-rank coarsening requires trivial *principal* holonomy would refute this.
- **hand-off:** the algebra belongs to the gauge-theorist lens; I flag only the tag/scope mismatch.

---

## P-10 — PDF metadata advertises "emergent time", which Chapter 12 explicitly disclaims

- **claim:** `pdfkeywords={… pullback geometry, emergent time, Markov kernel, renormalization group …}`
- **location:** `main.tex:21`
- **severity:** low
- **status:** untagged metadata contradicting a `\status{NOT-CLAIMED}` in the body.
- **evidence:** `12_philosophy.tex:45-51`: "The word ``timeless'' has an equally narrow meaning … It **does not assert
  that physical time is unreal or emergent**, nor identify Fisher duration with relativistic proper time, thermal time, or
  a quantum clock. `\status{DEFINITION}` `\status{NOT-CLAIMED}`" And the ledger's *Physical-time identification (open)*:
  "It is a statistical length, not a physical clock." The metadata is the manuscript's advertised framing, is what search
  indexes ingest, and is the single place where the fence is absent.
- **fix:** `emergent time` → `Fisher duration` (or `reparameterization-invariant inference duration`).
- **falsifies:** nothing; this is a one-word inconsistency between metadata and text.

---

## P-11 — Double status tags on multi-claim summary paragraphs defeat the tagging mechanism

- **claim:** e.g. `01:92-102`, a five-sentence paragraph asserting the vertical first jet, the gauge-invariant
  connection-relative pullbacks, possible Fisher degeneracy, the reparameterization quotient, Fisher-length measurement,
  and "not a physical clock" — closed by "`\status{ESTABLISHED}` `\status{NOT-CLAIMED}`".
- **location:** `01_introduction.tex:102`, `01_introduction.tex:114`, `06_general_coarsegraining.tex:180`
- **severity:** low
- **status:** both tags are individually right for *some* sentence; the reader cannot recover which.
- **evidence:** `SPEC.md` §2.1: "Use the `\status{...}` macro **immediately after the statement it governs**, and also
  name the status in the prose." §2 opens: "A reader must be able to tell, **at every point**, whether they are reading
  something established, something conjectured, something gestured at, or something still owed. Ambiguity here is the
  worst defect this document can have." A terminal pair of tags on a six-claim paragraph is that ambiguity.
- **fix:** attach each tag inline to the sentence it governs — e.g. "…the Fisher tensor may be degenerate.
  `\status{ESTABLISHED}` … not a physical clock. `\status{NOT-CLAIMED}`".
- **falsifies:** nothing; mechanical.

---

## P-12 — Roadmap sentence drops the schedule hypothesis of the contraction theorem

- **claim:** "Sections~\ref{sec:obs-survives} and~\ref{sec:obs-participatory} **prove** that an anchored Gaussian star
  supplies a unique, geometrically attracting coordinate-ascent fixed point."
- **location:** `11_obstructions.tex:18` (untagged roadmap)
- **severity:** low
- **status:** the verb "prove" is correct for uniqueness, over-scoped for attraction.
- **evidence:** `thm:obs-star-fixed-point-contraction` proves geometric contraction only for "the exact block schedule
  that updates every constituent factor from the current apex factor, in parallel or in any order, and then updates the
  apex factor" (`11:262`), with rate `ρ = λ_max(P_b^{-1/2}BP_b^{-1/2}) < 1`. `11:315` then fences: "Delayed, noisy,
  asynchronous, or inexact updates are not covered … and remain a separate convergence problem. `\status{OPEN}`", and the
  ledger indexes this as *Update robustness (open)*. Uniqueness of the fixed point is schedule-free; the geometric rate
  is not. (I verified the theorem's algebra: `I−M = P_b^{-1}P_0`, `S = I − P_b^{-1/2}P_0P_b^{-1/2}` has spectrum in
  `[0,1)`, `KL(q_b^{(t)}‖q_b^*) = ½‖e_t‖²_{P_b}`, and `Σ_i KL = ½e_tᵀBe_t`. All correct.)
- **fix:** "…supplies a unique fixed point that the exact synchronous schedule reaches geometrically."
- **falsifies:** an asynchronous/inexact convergence theorem would make the roadmap sentence accurate as written.

---

## P-13 — "Constituted" at a fixed point whose closed form is a declared-parameter functional

- **claim:** "At a variational fixed point of \eqref{eq:obs-star} … Each agent's effective coordinate input is therefore
  **constituted** by the apex update, and the apex input is **constituted** by the agents' updates."
- **location:** `11_obstructions.tex:247`, paragraph tagged `\status{ESTABLISHED}`
- **severity:** low
- **status:** `ESTABLISHED` is right for the update formulas; the word "constituted" is a metaphysical dependence
  predicate the algebra does not deliver, and it is the load-bearing word for Chapter 12's participatory section.
- **evidence:** the manuscript's own `eq:obs-star-fixed-point` gives
  `m_b^⋆ = P_0^{-1}(r_b + Σ_i Θ_iᵀ r_i)` — a closed-form function of the **declared** prior precision and information
  vectors alone, referring to no agent's belief. The pooling identity and the closed form are the same point, so the
  mutual dependence is a property of the **iteration** and of a fixed-point **identity**, not a constitution relation and
  not a derivation of the apex prior — which is exactly what `prop:obs-declared-root-unavoidable` says cannot happen.
  `11:249` gets this right ("a bidirectional dependence of exact mean-field coordinates **during inference**"), so the
  two sentences disagree with each other. Chapter 12 then leans on this paragraph (`12:186-193`), though it fences the
  Wheeler comparison correctly.
- **fix:** append to `11:247`: "By \eqref{eq:obs-star-fixed-point} the apex mean at the fixed point is an explicit
  function of the declared prior precision and information vectors alone, so the bidirectional dependence is a property of
  the iteration and of the fixed-point identity, not a derivation of the apex prior."
- **falsifies:** a fixed point not expressible in closed form from declared parameters would refute this.

---

## Falsifiability assessment (no finding — recorded as adjudication)

The manuscript's falsifiability posture is **honest and, for a document of this kind, exemplary**. I looked hard for
manufactured empirical content and did not find it.

- The framework as it stands makes **no discriminating empirical prediction**, and the manuscript says so in the plainest
  available terms: `12:244-248` — "No such target, estimator, tolerance, baseline margin, attraction theorem, or
  scheme-robust invariant has been supplied. The present empirical status is therefore inconclusive." The introduction
  says the same at `01:137-140`, and `claim:physical-law-identification` records it as the terminal obligation.
- The only test the current mathematics permits is declared to be **internal**: `12:225-231` — "This checks declared model
  data. It is not empirical detection of principal-bundle topology or base curvature. `\status{DEFINITION}`" That is the
  correct classification, not a hedge.
- `12:233-241` sets out a genuinely falsifiable cross-scale protocol (preregistered target, two admissible partitions,
  fit at fine resolution only, push through blocking without coarse refitting, held-out coarse statistic, declared
  tolerance, Gaussian-graphical and spectral baselines) and then states the Lakatosian scope correctly: "Failure would
  falsify **that added cross-scale hypothesis, not the finite-dimensional theorems**." This is right — the theorems are
  mathematics and are not empirically refutable — and it is the honest way to locate the programme's empirical content in
  the protective belt rather than pretending the hard core is at risk.
- **Programme classification:** the document is presently a *mathematical* research programme with **zero** empirical
  content, and it says so. It is neither progressive nor degenerative in Lakatos's empirical sense, because no novel fact
  has been predicted and no anomaly has been rescued. The one thing that would make it degenerative — absorbing failures
  by adding epicycles while keeping the empirical claim — is structurally prevented by the ledger, provided the ledger
  stays complete. That is why **P-2** matters more than its subject matter suggests: the ledger is the programme's
  anti-degeneration device, and an unindexed obligation is a hole in it.
- **Circularity check:** I found exactly one instance of the manuscript's own framework being used as authority for an
  epistemic conclusion — **P-5** ("supports an epistemic structural-realist reading"), which needs the
  formalism-to-world bridge that `claim:physical-law-identification` declares unpaid. Everywhere else the interpretive
  chapters cite mathematical chapters for mathematical content, which is not circularity. **P-1** is a different failure
  (a false claim about the manuscript's own contents), not circularity.
- **Novel-construction vs. rediscovery:** in scope for this lens I found no novelty overclaim. The document cites rather
  than claims aggregation-AMG (`SPEC` §7), matrix-weighted consensus, Sylvester's law, Birkhoff contraction,
  cellular-sheaf Laplacians (`HansenGhrist2019` at `09:322`), the randomization lemma (`Kallenberg2021` at `05b:483`),
  and path sampling (`GelmanMeng1998` at `11:322`). `FINAL-04` already verified the reference discipline.

## Attributions checked against primary sources

| Attribution | Location | Verdict |
|---|---|---|
| Kretschmann / Norton on general covariance | — | **absent from the current text.** Whole-manuscript grep for `kretschmann`, `norton`, `general covariance`, `machian`, `Rovelli`, `Page-Wootters`, `Jaynes`, `it from bit` returns **zero** hits. The misattribution recorded by the prior pass was excised, not reworded. Nothing to report. |
| Worrall 1989, epistemic structural realism | `12:133` | Correct source for ESR; the **inferential use** is over-strong — see **P-5**. |
| Ladyman & Ross 2007; Ladyman 2014 (SEP) | `12:138` | Support "structure is all that exists". Correct. |
| Esfeld & Lam 2008 | `12:138` | **Contradicts** the sentence citing it — see **P-3**. |
| van Fraassen 1980, empirical adequacy | `12:68` | **Does not support** the eliminative criterion — see **P-4**. |
| Kant 1781, base as a form ordering appearances | `12:55-56` | Fair use of the Transcendental Aesthetic; the citation is attached to the *scaffolding* reading only, and the noumenal reading (`12:56-57`) is offered without claiming Kant's endorsement. No finding. |
| Wheeler 1990, participatory proposal | `12:190-192` | Correct source ("it from bit", observer-participancy, Zurek volume). The manuscript fences it exactly right: "resembles … but is **neither derived from nor evidence for it**. `\status{DEFINITION}`". No finding. Bib page range 3–28 matches the standard citation. |
| Hoffman 2015 / Hoffman 2019, interface theory | `12:109-111` | Accurate. ITP's Perceptual Agent Theory formalizes the perceptual map as a **Markov kernel** between measurable spaces, which subsumes "an arbitrary measurable relation between representation and world". No finding. |
| Gelman & Meng 1998, path sampling | `11:317-322` | The displayed identity `log p(o) = ∫₀¹ E_{p_β}[log p(o|Y)]dβ` is the standard thermodynamic-integration identity; correctly labeled "an identity rather than a bound", and correctly not identified with the §`sec:obs-tau` construction. No finding. |
| Berman–Klinger–Stapleton 2023, Bayesian renormalization | `11:159-161`, `11:172-180` | `FINAL-03` already verified. Chapter 11 correctly limits BKS to its regular asymptotic setting, declines the opposite-flow claim (`\status{NOT-CLAIMED}` ×2), and does not attribute a spectral cutoff. No finding. |

## Verification of Chapter 11's mathematics touched by status claims

Checked while auditing tags; all correct, none is a finding:
`det(J+p₀I) = p₀² + p₀(a+a⁻¹)²` (trace/determinant expansion, `det J = 0`);
`A''(1) = −4/(p₀+4) < 0` (with `f(a)=(a+1/a)²`, `f''(1)=8`, `D(1)=p₀(p₀+4)`) — the sign correction demanded by the prior
pass's `R14` is now right, and the text says explicitly that this is a **maximum**;
`det J = (det(I−H))²/(det R_e det R_f)` (Schur complement of the stacked residual map);
`ker J = {(Θ_e v, v) : v ∈ ker(H−I)}`;
`m_b^⋆ = P_0^{-1}(r_b + Σ Θ_iᵀr_i)` and `ρ = λ_max(P_b^{-1/2}BP_b^{-1/2}) < 1`.

## Confidence

**HIGH** on P-1, P-2, P-3, P-4, P-7, P-10 (each rests on a mechanical grep of the current text or a verified primary
source). **MEDIUM** on P-5, P-6, P-8 (interpretive judgments about verb strength and tag scope, though each cites the
manuscript's or `SPEC.md`'s own stated standard). **MEDIUM** on P-9, P-11, P-12, P-13 (real but minor; each has a
one-sentence fix). What would shift me: on P-1, a reinstated labeled result in Chapter 2; on P-2, a ledger entry naming
the monotone obligation; on P-5, evidence that the listed invariants survive a change of *theory* rather than of frame.
