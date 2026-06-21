# Wiki Deep Review — 2026-06-21

**Executive summary.** The vault is in good structural health. Link integrity is essentially clean: there are **0 empty files** and **0 real ghost nodes** — the prior 492-ghost-node reconciliation (commits `caaa07e` / `c4840e3`) is verified effective, and the single "broken link" the scanner reports is a cosmetic illustrative `[[wikilink]]` inside `log.md`, not a defect. The dominant finding is **source-note duplication**: the deterministic scan flags **77 duplicate-title clusters**, and the agent panel judged **all 77 to be the same underlying work** (0 genuine keep-separate), driven by two mechanical causes (papers↔refs mirrors and bibtex-key-slug re-ingests). Secondary load is **304 stub pages** awaiting elaboration or merge, and **minor index drift** (69 source papers + 6 wiki concepts not yet linked in `index.md`). Nothing here is urgent or data-losing; the work is consolidation, not repair. **No vault writes have been made — every fix below is gated on user confirmation.**

---

## 1. Link integrity & empty nodes

**This is GOOD news, and it corrects any impression that the ghost-node problem persists.**

- **Empty files: 0.** `_lint_scan.json → "empty": []`.
- **Real ghost / broken-target wikilinks: 0.** The scanner's `broken.links` list contains exactly one entry — `log.md` — and that is an **artifact**: `log.md` contains illustrative example wikilinks (e.g. the schema's sample ledger lines like `[[Natural gradient]]`, `[[Holonomy]]`) that point at slugs which are not meant to resolve. It is a documentation file, not a content node.
- The prior **492 empty/ghost nodes** fixed in `caaa07e` ("full-ingest reconciliation") and refined in `c4840e3` are **confirmed gone** — the current scan finds none. The full-ingest reconciliation did its job.

Per-page broken `[[wikilinks]]` flagged by the per-stub agents (e.g. `[[Confirmation bias]]`, `[[Unity of Consciousness]]`, `[[Free-energy principle active inference]]`) are **dangling cross-links inside otherwise-valid pages**, not empty/ghost nodes — they are catalogued in §4 and are low-severity retargeting chores.

---

## 2. Duplicate source notes (the main finding)

### Root causes

1. **`papers/` ↔ `refs/` mirrors.** The schema sanctions two note *roles* for one work — a rich `papers/` reading note and a terse `refs/` manuscript-citation note. In practice many pairs drifted into near-duplicates of the same paper. The scan's **28 case-insensitive basename collisions** (§5) are exactly these same-slug papers/refs pairs. The refs/ note often uniquely holds: the correct/complete published-venue citation (DOI, volume, pages) that the papers/ note lacks, the "why the project cites it" PIFB framing, and a distinct cross-link set.
2. **Bibtex-key-slug re-ingests from the bulk PDF ingest.** A batch ingest created second `papers/` notes under camelCase bibtex-key slugs (`Bissiri2016-generalized-bayes`, `kullback1951information`, `chung2015recurrent`, `foerster2016learning`, `Quine1951-two-dogmas`, `Lloyd2002-computational-capacity`, `gao-2017-neuroscience-dimensionality`, …) duplicating an existing clean hyphenated-slug note. Several are **3-way** clusters (one clean papers/, one camelCase papers/, one refs/).

### Tally (agent verdicts)

| Verdict | Count |
|---|---|
| Clusters where all members are the **same work** | **77 / 77** |
| Marked **keep-separate** (genuinely distinct works) | 0 |
| `merge-and-delete-redundant` (straightforward) | 57 |
| `needs-human-judgment` (citation contradiction or richer-refs/ role-reversal) | 20 |

> The "keep-separate" cases noted in prior sessions (LLaMA 1/2, Friston-2008 DEM vs *Hierarchical models in the brain*, Lahav 2022/2025) are **not** in this duplicate set — LLaMA notes are distinct files, the Friston DEM duplicate is a true papers/refs mirror of one paper, and Lahav-2025 self-identifies as a "shortened version" of the 2022 work (so it **is** a duplicate, reversing the earlier keep-separate read).

### 2a. Straightforward merges (`merge-and-delete-redundant`)

For each: keep the **Canonical**, fold the listed unique content, then delete the **Redundant**.

| Canonical (keep) | Redundant (merge → delete) | Unique content to preserve | Note |
|---|---|---|---|
| `papers/vanrietvelde-2020-qrf-perspective-neutral.md` | `refs/vanrietvelde-2020-change-of-perspective.md` | "Why cited" QRF↔Ω_ij framing; holonomy/quotient reading; gauge cross-links; alias "Perspective-neutral framework" | **Fix author spelling Hühn → Höhn** on merge |
| `papers/friston-frith-2015-duet.md` | `papers/friston-2015-duet.md` | Generalised-gradient eq; Markov-blanket synchrony argument; FEP/Markov-blanket cross-links | **Drop the redundant's bogus aliases** (`friston-2015-active-inference-mdp/epistemic`) — they hijack a different paper |
| `papers/bissiri-2016-general-bayesian-updating.md` | `papers/Bissiri2016-generalized-bayes.md`, `refs/bissiri-holmes-walker-2016-general-bayes.md` | **arXiv 1306.6430** (missing on both papers notes); Gibbs-posterior framing; tempered-coupling PIFB context | 3-way; camelCase slug disfavored |
| `papers/brukner-2018-no-go-observer-facts.md` | `refs/brukner-2018-no-go-observer-facts.md` | **Published venue Entropy 20(5):350, DOI 10.3390/e20050350** (canonical is arXiv-only); transported-consensus framing | basename collision |
| `papers/chung-2015-vrnn.md` | `papers/chung2015recurrent.md` | ELBO detail; fixed-prior ablation; 6 extra cross-links | Redundant is the **longer** note (892w) — genuine merge |
| `papers/lahav-2022-relativistic-consciousness.md` | `papers/lahav-2025-relativistic-consciousness.md`, `refs/lahav-neemeh-2022-relativistic-consciousness.md` | refs/ manuscript-usage + Editorial caveat; **corrected year=2022** | "2025" note is a shortened reprint, not a new work |
| `papers/hewitt-2019-structural-probe.md` | `refs/hewitt-manning-2019-structural-probe.md` | PIFB "parse-completeness conjecture"; intrinsic-Σ-metric idea; 3 cross-links | basename collision |
| `papers/friston-2017-active-inference-process-theory.md` | `refs/friston-2017-active-inference-process.md` | Manuscript framing (single-agent baseline); info-geometry/Hamiltonian cross-links; Editorial scoping note | Verify canonical's `curiosity` aliases resolve |
| `papers/slonim-2000-agglomerative-ib.md` | `refs/slonim-2000-agglomerative-ib.md` | Meta-agent/RG-flow coarse-graining framing; 3 IB-family links | basename collision; reconcile 1999-vs-2000 venue |
| `papers/fiedler-1973-algebraic-connectivity.md` | `refs/fiedler-1973-algebraic-connectivity.md` | **DOI 10.21136/CMJ.1973.101168**; λ₂-as-parent-mass framing; **adopt refs/ `project/multi-agent` dual tagging** | basename collision; canonical under-tagged |
| `papers/fuchs2014-qbism-locality.md` | `refs/fuchs-2014-qbism.md` | **Add alias `fuchs-2014-qbism`** (inbound-link target across participatory cluster) or backlinks break; pagination 749–754, DOI | many notes link the refs slug |
| `papers/voita-2019-attention-heads.md` | `refs/voita-2019-multihead.md` | `project/multi-agent` tag; mechanistic-interp cross-links; positional-vs-syntactic-head PIFB reading | — |
| `papers/sengupta2017gauge.md` | `refs/sengupta-friston-2017-bayesian-gauge-theory.md` | **Load-bearing editorial provenance** (manuscript-bib reconciliation, 1705.06614 disambiguation) — must survive; PIFB cross-links | basename collision |
| `papers/VanRaamsdonk-2010-spacetime-entanglement.md` | `refs/vanraamsdonk-2010-entanglement-spacetime.md` | Participatory cross-links; essay-status editorial caveat | — |
| `papers/carlip-2014-emergent-gravity.md` | `refs/carlip-2014-challenges-emergent-gravity.md` | **Vol 46, pp 200–208, DOI 10.1016/j.shpsb.2012.11.002**; "critical counterweight" framing; methodology tags | — |
| `papers/nickerson-1998-confirmation-bias.md` | `papers/nickerson-1998-confirmation.md`, `refs/nickerson-1998-confirmation-bias.md` | **DOI 10.1037/1089-2680.2.2.175**; multi-agent tag + Active-Inference links from (2); belief-inertia/SocialPhysics lineage from refs/ | 3-way; verify wason slugs; keep refs slug (inbound target) |
| `papers/luppi-2019-consciousness-integration-diversity.md` | `refs/luppi-2019-consciousness-integration-diversity.md` | **Citation-disambiguation editorial** (Nat. Commun. 10:4616 2019, not 12:4427 2021); review/remove misleading `Luppi2021` alias | basename collision |
| `papers/deutsch-2015-constructor-information.md` | `refs/deutsch-marletto-2015-constructor-information.md` | "Contrast class" framing (most important); **fix DOI → 10.1098/rspa.2014.0540** (refs is correct) | needs DOI verification |
| `papers/zurek-2003-einselection.md` | `refs/zurek-2003-decoherence.md` | Participatory cross-links; full pagination 715–775, issue 3 | — |
| `papers/friston-2008-dem.md` | `refs/friston-2008-dem.md` | Disambiguation callout (DEM vs *Hierarchical models in the brain*); Bayesian-mechanics cross-links; `number/publisher` | basename collision |
| `papers/schwarz-1978-bic.md` | `refs/schwarz-1978-bic.md` | **DOI 10.1214/aos/1176344136**; union `project/multi-agent`; MDL/meta-agent cross-links | basename collision |
| `papers/chalmers-1995-facing-up-consciousness.md` | `refs/chalmers-1995-facing-up.md` | Issue number 2(3), publisher; "relocation not dissolution" framing; panpsychism/explanatory-gap links | — |
| `papers/wainwright-2008-graphical-models-variational.md` | `refs/wainwright-jordan-2008-graphical-models-variational-inference.md` | Gaussian mean-parameter identity; standalone-book editorial; distinct cross-links | **Both ~960–977w — careful merge**; reconcile Blei/Amari slugs |
| `papers/ramsauer2021hopfield.md` | `refs/ramsauer-2021-hopfield.md` | `project/multi-agent`; metastable-state framing; cross-links | Keep content; **consider rename to hyphenated slug** |
| `papers/chechik2005information-bottleneck-gaussian.md` | `refs/chechik-2005-gaussian-ib.md` | `cluster/spd-geometry`, `project/multi-agent`; Gaussian-belief-tuple framing; Pennec link | consider rename to cleaner slug |
| `papers/adlam-2022-cross-perspective.md` | `refs/adlam-rovelli-2022-cross-perspective.md` | **Published venue *Philosophy of Physics* (2023)**; `cluster/gauge-theory`; gauge-transport cross-links | reconcile wheeler-1989 vs 1990 slug |
| `papers/sonderby-2016-ladder-vae.md` | `refs/sonderby-2016-ladder-vae.md` | `project/multi-agent`; shadow-prior framing; cross-links | basename collision (same stem) |
| `papers/foerster-2016-dial.md` | `papers/foerster2016learning.md` | Antisymmetric-reward gradient analysis; Colour-Digit MNIST mention | keep canonical's hyphenated cross-links |
| `papers/kullback-1951-kl-divergence.md` | `papers/kullback1951information.md` | Bregman-divergence-for-exp-families point; data-processing-inequality note; γ_ij coupling | intra-papers/ dup |
| `papers/gao-2017-neural-dimensionality.md` | `papers/gao-2017-neuroscience-dimensionality.md` | Broader cortical-area list; (M,T) phase boundary; fuller h→s→p→q→o hierarchy | keep canonical's complete journal metadata |
| `papers/su2024roformer.md` | `refs/su-2021-roformer-rope.md` | "RoPE as abelian gauge frame" framing; `project/multi-agent`; cross-links | year 2024(journal)/2021(arXiv) not a contradiction |
| `papers/fuchs-2020-se3-transformer.md` | `papers/fuchs2020-se3-transformer.md` | **Fix ScanObjectNN result** (base 72.8% → +z 85.0%, redundant is correct); attentive-self-interaction layer; rep-theory cross-links | intra-papers/ collision |
| `papers/friedkin1990-social-influence-opinions.md` | `refs/friedkin-johnsen-1990.md` | Susceptibility-form update + caveat; belief-inertia cross-link web; `project/multi-agent` | optional rename to firstauthor-year slug |
| `papers/castellano-2009-statistical-physics-social-dynamics.md` | `refs/castellano-fortunato-loreto-2009-social-dynamics.md` | Belief-inertia/SocialPhysics cross-link web; "all first-order/overdamped" argument; multi-agent tags | — |
| `papers/chalmers-2016-combination-problem.md` | `refs/chalmers-2016-combination-problem.md` | PIFB panprotopsychist framing; pp.179–214 + subtitle; cross-links | basename collision; keep finer tags |
| `papers/strouse-2017-deterministic-ib.md` | `refs/strouse-2017-deterministic-ib.md` | **Venue Neural Computation 29(6):1611–1630** (canonical arXiv-only); MDL/crisp-assignment framing; cross-links | basename collision |
| `papers/caticha-2019-entropic-dynamics-qm.md` | `refs/caticha-2019-entropic-dynamics.md` | **Venue Entropy 21(10):943, DOI 10.3390/e21100943**; Hamiltonian/belief-inertia cross-links; confirm `project/transformer` | basename collision |
| `papers/friston-2023-fep-simpler.md` | `refs/friston-2023-fep-simpler.md` | **Venue Physics Reports 1024:1–29, DOI**; Markov-blanket-debate + Hamiltonian cross-links; participatory tags | basename collision; flag canonical's conflated alias block for human |
| `papers/bousso-2002-holographic.md` | `refs/bousso-2002-holographic-principle.md` | participatory-it-from-bit + holography-theme cross-links; Fisher-metric framing | keep canonical's finer tag |
| `papers/tishby-1999-information-bottleneck.md` | `refs/tishby-1999-information-bottleneck.md` | Only two aliases to fold (refs is a near-strict subset) | basename collision; **cleanest merge in batch** |
| `papers/maldacena-1999-adscft.md` | `refs/maldacena-1998-ads-cft.md` | **Record BOTH ATMP-1998 & IJTP-1999 citations**; participatory tags/cross-links; AdS/CFT aliases | reconcile AdS/CFT wikilink naming vault-wide |
| `papers/kirchhoff-2018-markov-blankets-of-life.md` | `refs/kirchhoff-2018-markov-blankets-life.md` | Issue 15(138); nested-blanket/meta-agent framing; **union all participatory sub-tags** + `cluster/multi-agent` + `project/transformer` | — |
| `papers/latane1981psychology.md` | `refs/latane-1981-social-impact.md` | belief-inertia force-law framing; SocialPhysics cross-links; **accented "Latané"** | **rename to `latane-1981-social-impact`** (better slug) |
| `papers/uhlmann-1976-transition-probability.md` | `refs/uhlmann-1976-transition-probability.md` | **DOI 10.1016/0034-4877(76)90060-4**; `project/transformer`; quantum-monotone-metric cross-links | basename collision |
| `papers/wigner-1960-unreasonable-effectiveness.md` | `refs/wigner-1960-unreasonable-effectiveness.md` | participatory/methodology tags; structural-realism cross-links | basename collision; fix "in"→"on" journal typo |
| `papers/padmanabhan-2010-thermodynamical-gravity.md` | `refs/padmanabhan-2010-thermodynamic-gravity.md` | DOI 10.1088/0034-4885/73/4/046901 + issue; thermodynamic-gravity-triad cross-links | repoint intra-triad links after delete |
| `papers/jacobson-1995-einstein-equation-of-state.md` | `refs/jacobson-1995-thermodynamics-spacetime.md` | DOI 10.1103/PhysRevLett.75.1260 + issue; aliases; triad cross-links | **repoint `padmanabhan-2010-thermodynamic-gravity` links** to surviving slug |
| `papers/sakthivadivel2022-bayesian-mechanics-geometry.md` | `refs/sakthivadivel-2022-geometry-bayesian-mechanics.md` | participatory/transformer tags; Bayesian-mechanics-hub cross-links | reconcile Friston-2019/Da-Costa-2021 dup slugs; consider rename |
| `papers/sengupta-2016-neuronal-gauge.md` | `refs/sengupta-2016-neuronal-gauge-theory.md` | participatory tags; **follow-up ref Sengupta&Friston 2017 (1705.06614)** — genuinely new; gauge cross-links | basename collision |
| `papers/press2022-alibi.md` | `refs/press-2021-alibi.md` | `project/multi-agent`; "ALiBi from entropy-regularized consensus prior" framing; cross-links | standardize year=2022; reconcile RoPE slug |
| `papers/hinton-2002-products-of-experts.md` | `refs/hinton-2002-poe.md` | Gaussian PoE precision-addition identity; meta-agent-pooling contrast; `cluster/multi-agent` | pick one bibtex key |
| `papers/katharopoulos-2020-linear-transformers.md` | `refs/katharopoulos-2020-linear-transformers.md` | (refs is a strict subset) | basename collision; remove canonical's "(refs mirror)" self-link |
| `papers/quine-1951-two-dogmas.md` | `papers/Quine1951-two-dogmas.md`, `refs/quine-1951-two-dogmas.md` | Underdetermination + Quine-1975 entry; `[[Web of Belief]]`/`[[Quine1960-word-and-object]]`; `project/multi-agent` | 3-way merge |
| `papers/beal-2003-variational-bayesian.md` | `refs/beal-2003-variational-algorithms-approximate-bayesian-inference.md` | ELBO/VBEM fixed-point eqs; Editorial Rényi/gauge caveat; ELBO/theme cross-links | both deep — genuine 2-way merge |
| `papers/blei-2017-variational-inference.md` | `refs/blei-2017-variational-inference.md` | participatory-it-from-bit additive-KL↔product-prior link; 2 cross-links | basename collision |
| `papers/clark-2019-bert-attention.md` | `papers/clark2019does-bert-look.md`, `refs/clark-2019-bert-attention.md` | refs/ parse-conjecture + `project/multi-agent`; (2) `[[GL(K) Attention Manuscript]]` + field tag | 3-way; **map `field/linguistics`→`field/cs-ml`** (not in closed vocab) + keep `field/neuroscience` |
| `papers/clark-2013-predictive-brains.md` | `papers/clark2013whatever.md`, `papers/clark-2013-whatever-next.md` | Full VFE functional + 5 PP-claims + active-inference links; Free-Energy-Principle/Bayesian-Brain/dark-room | **Fix DOI → 10.1017/S0140525X12000477** (the -whatever-next DOI is wrong); 3-way |

### 2b. `needs-human-judgment` subset (citation contradictions / role reversals)

These are still the **same work**, but a human should resolve a citation contradiction or a papers/refs role-reversal *before* merging:

- **`lloyd-2002-computational-capacity-universe.md`** (+ `Lloyd2002-computational-capacity.md`, `refs/lloyd-2002-computational-capacity.md`): three notes give **mutually inconsistent journals** (Nature 406 vs Nature 406+DOI vs **PRL 88:237901**). Reality: PRL 88, 237901 is correct — **both papers notes have the wrong Nature citation.** Keep the universe note's body, fix journal to PRL, carry the password-protected-PDF provenance warning and susskind/PIFB links, delete the two redundant.
- **`swingle-2012-entanglement-renormalization-holography.md`** ← `refs/swingle-2012-entanglement-renormalization.md`: canonical cites **Phys. Rev. B 86, 045117 (wrong)**; refs cites **Phys. Rev. D 86, 065007 (correct)**. Fix to PRD on merge; union gauge-theory vs participatory tags; reconcile RT-source slug.
- **`johnson-2011-entropic-dynamics-measurement.md`** ← `refs/johnson-caticha-2011-measurement-problem.md`: refs has the full proceedings citation **AIP Conf. Proc. 1443:104–116 (2012), DOI 10.1063/1.3703626** the canonical lacks; "collapse as consensus" framing.
- **`beltagy2020longformer.md`** ← `refs/beltagy-2020-longformer.md`: the sanctioned reading-note/citation-note split — human decides keep-both vs merge; if merge, fold `project/multi-agent` + PIFB cross-links; rename to hyphenated slug.
- **`dempster-1977-em-algorithm.md`** ← `refs/dempster-1977-em.md`: refs has unique Editorial (free-energy/ELBO reinterpretation is *later* Neal-Hinton work), denser project cross-links, fuller BibTeX; reconcile Neal-Hinton slug.
- **`jiang2023-mistral7b.md`** ← `refs/jiang-2023-mistral.md`: fold `project/multi-agent` + "architecture furniture" PIFB framing; prefer hyphenated slug.
- **`deffuant2000-bounded-confidence.md`** ← `refs/deffuant-2000-bounded-confidence.md`: **fix citation** — canonical's "(2001) ACS 03(3):11" is wrong; refs's **ACS 3(1n04):87–98 (2000)** is correct; fold cross-links + editorial.
- **`flache-2017-social-influence-models.md` (refs/)** ↔ `papers/flache2017-opinion-dynamics.md`: **role reversal** — the refs/ note is richer and better-slugged; the papers/ note uniquely holds the three influence-class update equations. Human decides which folder/type survives; the equations must be folded in.
- **`petz-1996-monotone-metrics.md`** ← `refs/petz-1996-monotone-metrics.md`: **canonical has an internal contradiction** (which operator-mean is smallest/largest); refs has the correct ordering (Bures/SLD smallest, RLD largest) — use refs to fix it. Also fold participatory/quantum-foundations framing + tags. basename collision.
- **`fuchs-2017-participatory-realism.md`** ← `refs/fuchs-2017-participatory-realism.md`: refs has the full **book-chapter citation** (Durham & Rickles eds., Springer pp.113–134) the canonical lacks; gauge cross-links; reconcile Wheeler slug. basename collision.
- **`hegselmann-2002-opinion.md`** ← `refs/hegselmann-krause-2002.md`: **critical link-routing** — 9+ wiki pages backlink the *refs* slug `[[hegselmann-krause-2002]]`; deleting it orphans them unless redirected/aliased. Richest content is the papers note.
- **`chalmers-2013-panpsychism.md`** (papers ↔ refs, **same basename**): active Obsidian ambiguity. Keep papers content, port refs PIFB-self-classification + pagination + forward links, delete refs so basename is unique.
- **`anderson1980perseverance.md`** ← `papers/anderson1980-belief-perseverance.md` (+ un-batched `refs/anderson-1980-belief-perseverance.md` — a **3rd copy**): **statistical contradictions** to verify against source (F(1,54)=7.86 reported p<.01 vs p<.05; an Exp-2 interaction F present in one note only). Keep most-backlinked note as canonical.
- **`nickel-2017-poincare-embeddings.md`** ← `refs/nickel-kiela-2017-poincare-embeddings.md`: **both slugs live** in the wiki — alias the deleted one. refs has correct NeurIPS-2017 venue (canonical is arXiv-only) + PIFB hierarchy framing.
- **`bialek2001predictability.md`** ← `refs/bialek-2001-predictability-complexity.md`: refs slug is the one wiki backlinks (alias it); fold PIFB inverse-K framing.
- **`strawson-2006-realistic-monism.md`** (papers ↔ refs, **same basename**): active ambiguity; keep papers, port anti-emergence framing + Freeman-reprint DOI + forward links, delete refs.
- **`bartlett-2007-reference-frames.md`** ← `refs/bartlett-rudolph-spekkens-2007-reference-frames.md`: 6+ pages backlink the refs slug — alias it. Fold speakable/unspeakable + φ_i-as-physical-frame framing.
- **`rovelli-1996-relational-qm.md`** (papers ↔ refs, **same basename**): active ambiguity; keep papers, port fibre-bundle/"no global section" framing, delete refs.
- **`bonnabel-2009-spd-fixed-rank.md`** ← `refs/bonnabel-sepulchre-2009-psd-fixed-rank.md`: both slugs live — alias the deleted one. refs has full pagination 31(3):1055–1070 + arXiv:0807.4462 + degenerate-regime motivation.

---

## 3. Stub pages (304) — triage

The scanner flags **304 stub pages**: **196 concept stubs**, **106 source-paper stubs**, **2 template artifacts** (`templates/concept.md`, `templates/method.md` — false positives, exclude from the queue). The per-stub agent panel's tally:

| Disposition | Count |
|---|---|
| **keep-as-stub** (peripheral, adequate) | 221 |
| **elaborate** | 53 (of which **10 high-priority**) |
| **merge-into-existing** | 27 |
| **delete-artifact** (templates) | 2 |
| stubs carrying a side **issue** (broken link / bad tag / metadata) | 112 |

> Note: the source-paper stubs are immutable reference *cards* — per schema they are **not** elaboration targets (synthesis lives on the concept/method pages they feed). Essentially all 106 paper stubs are `keep-as-stub`; the elaborate/merge actions land on `wiki/concepts/` pages.

### High-priority to elaborate (10)

| Page | What it needs (one line) |
|---|---|
| `wiki/concepts/Belief coupling.md` | Gauge-transported KL coupling β_ik·KL(q_i‖Ω_ik q_k); bounded-confidence & PoE limits; consensus/meta-agent role |
| `wiki/concepts/Expected Free Energy.md` | G = epistemic (info-gain) + pragmatic (value) decomposition; risk/ambiguity form; policy = softmax(−G) (thinnest stub, 78w) |
| `wiki/concepts/Exponential family.md` | Canonical form; natural↔mean dual params; log-partition = cumulant gen; Hessian = Fisher; Gaussian beliefs; conjugacy |
| `wiki/concepts/Fibre Bundle.md` | base/fibre/structure-group; principal vs associated; connection→transport→curvature→holonomy |
| `wiki/concepts/Gaussian Beliefs.md` | (μ,Σ) as exp-family belief; nat/moment params; SPD covariance geometry; congruence gauge action; closed-form KL |
| `wiki/concepts/GL(K) gauge group.md` | GL(K) as structure group; gl(k) algebra; GL(K)/O(K)=SPD cone; congruence action; **fix mis-sourcing** |
| `wiki/concepts/GL(K) gauge-equivariant attention.md` | Central manuscript construction: per-token gauge frames; congruence-transformed QK; GL(K)-invariant scores; SPD geometry |
| `wiki/concepts/Markov Blanket.md` | Formal sensory/active/internal partition; conditional-independence def; agent-boundary + coupling role |
| `wiki/concepts/Mean-Field Approximation.md` | Factorized q(z); CAVI coordinate ascent; variance underestimation; stat-physics link to opinion dynamics |
| `wiki/concepts/Mutual information.md` | Definition/identities; chain rule; DPI; IB objective; quadratic-limit relation to Fisher metric |

### Medium / low elaborate (43, grouped)

- **Info-geometry / VFE core (medium):** `Amari-Chentsov tensor`, `Bregman divergence`, `Conjugate-Exponential Family`, `Maximum entropy`, `Sufficient statistics`, `Optimal transport`, `Operator Monotone Functions`, `Entropy`, `Belief Compression`, `Recognition Density`, `Data processing inequality` (low).
- **Gauge / geometry (medium):** `Characteristic Classes`, `Diffeomorphism invariance`, `Spherical harmonics`, `Exponential map (Riemannian)`, `Wigner-D Matrices` (low), `Classifying Space` (low), `Symplectic geometry` (low), `Dirac Quantization` (low), `Decoherence-free subsystems` (low), `Grassmann Manifold` (low).
- **Attention / ML (medium):** `Associative Memory`, `Energy-Based Models`, `Multi-head attention`, `Belief Propagation`, `Gaussian Belief Propagation`, `Deep Networks` (→ note in §3 merge list).
- **Belief / social dynamics (medium):** `Bayesian Inference` (make canonical hub), `Bayesian brain hypothesis`, `Belief dynamics`, `Theory of Mind`, `Phase transitions in social systems`, `Self-organized criticality`, `Bounded Rationality` (add source).
- **Physics / participatory (low):** `Bekenstein bound`, `Born Rule`, `Bell inequalities`, `Black Hole Thermodynamics`, `CSL model`, `Canonical Correlation Analysis`, `Entanglement entropy`, `Bayesian Probability`, `Rational inattention` (fix source slug).

### Merge into existing canonical pages (27)

| Stub (merge from) | Target (canonical) |
|---|---|
| `wiki/concepts/Approximate Bayesian inference.md` | `Variational free energy` |
| `wiki/concepts/Attention as Inference.md` | `Precision weighting` |
| `wiki/concepts/Attention as Precision.md` | `Precision weighting` |
| `wiki/concepts/Bayesian Belief Updating.md` | `Bayesian Inference` |
| `wiki/concepts/Bayesian reasoning.md` | `Bayesian Inference` |
| `wiki/concepts/Belief Updating.md` | `Bayesian Belief Updating` |
| `wiki/concepts/Causal Explanation.md` | `Belief perseverance and confirmation bias` |
| `wiki/concepts/Coarse Graining.md` | `Renormalization-group flow of beliefs` |
| `wiki/concepts/Confirmation holism.md` | `Web of Belief` |
| `wiki/concepts/Consciousness and Active Inference.md` | `Mathematical consciousness science` |
| `wiki/concepts/Covariant Entropy Bound.md` | `Bekenstein bound` |
| `wiki/concepts/Critical Phenomena.md` | `Phase transitions in social systems` |
| `wiki/concepts/Decoherence.md` ⇄ `Quantum Decoherence.md` | consolidate under `Decoherence` (canonical), alias the other |
| `wiki/concepts/Deterministic Annealing.md` | `Information bottleneck` |
| `wiki/concepts/Distributional Clustering.md` | `Information bottleneck` |
| `wiki/concepts/Gauge Theory.md` | `Gauge transformation` |
| `wiki/concepts/Gauge transport.md` | `Parallel transport` |
| `wiki/concepts/Group representation theory.md` | `Irreducible representation` |
| `wiki/concepts/Hierarchical Latent Variable Models.md` | `Hierarchical generative model` |
| `wiki/concepts/Horizon Entropy.md` | `Horizon thermodynamics` |
| `wiki/concepts/Phase Transitions.md` | `Critical Phenomena` |
| `wiki/concepts/Quantum Decoherence.md` | `Decoherence` |
| `wiki/concepts/Relative Position Encoding.md` | `Relative positional encoding` |
| `wiki/concepts/Riemannian Manifold.md` | `Riemannian geometry` |
| `wiki/concepts/Tomita-Takesaki theorem.md` | `Modular automorphism group` |
| `wiki/concepts/Transport Operator.md` | `Parallel transport` |

### Delete (fuzzy-match artifacts)

These were **swept into the stub batch by mistake** and must be removed from the review queue — but the **files themselves are kept** (they are tooling):

- `templates/concept.md` — page template (`{{Concept}}` placeholder, `tags:[cluster/]`).
- `templates/method.md` — page template (`{{Method / Model}}` placeholder).

No actual content pages are recommended for deletion (all 304 are either real stubs to keep/elaborate/merge, or these two templates to exclude).

---

## 4. Correctness & frontmatter issues

### A. Slug / year / metadata inconsistencies on source-paper stubs

- `anderson-morley-1971-laplacian-eigenvalues.md` — filename/title say **1971**, frontmatter/BibTeX say **1985** (actual pub year). Reconcile.
- `barlow-1990-unsupervised-learning.md` — filename 1990 vs frontmatter **1989**; aliases mix both.
- `burda-2015-iwae.md` — filename 2015 vs frontmatter/BibTeX **2016** (ICLR); arXiv 2015.
- `carhart-harris-2018-entropic-brain-revisited.md` — `-revisited` in filename but alias/key omit it; `[[carhart-harris-2018-entropic-brain]]` resolves only via alias.
- `chiribella-2016-quantum-from-principles.md` — filename/alias 2016 vs frontmatter/BibTeX **2017**; BibTeX author order differs from title.
- `freidel-geiller-2021-edge-modes.md` — title/alias 2021 vs year/venue/BibTeX **2020** (JHEP 2020(11):026).
- `globerson-2004-sufficient-dimensionality-reduction.md` — filename/alias 2004 vs year/venue/BibTeX **2003** (JMLR vol 3).
- `luppi-2021-synergistic-core.md` — slug/alias 2021 vs frontmatter/venue/BibTeX **2022** (Nat Neurosci 25:771–782).
- `penrose-2000-mathematical-physics.md` — slug says "mathematical-physics" but actual chapter title is "Wavefunction Collapse as a Real Gravitational Effect" (frontmatter title is correct).
- `fuchs-2002-quantum-mechanics.md` — mixes 2002 preprint vs 2003 published year without note (both technically correct).
- `von-neumann-1932-mathematical-foundations.md` — citation callout "(1932)" vs 1955 translation emphasis (1932 frontmatter year is correct).
- `woodford-2001-imperfect-information.md` — filename `-2001-` vs frontmatter year **2003** (body explains 2001 WP vs 2003 pub; acceptable).
- `wilson2010-bayesian-online-hazard.md` — alias list has self-referential junk alias `"wilson2010-bayesian-online-hazard (target)"` — drop it (ghost-ingest artifact).
- `lahav-2018-microscopic-sync.md` — **unverified bibliography** ("venue: unverified", title embeds "(Lahav et al. 2018)", BibTeX note "Citation details unverified"). Likely a ghost-node from a citation in `lahav-2022`; verify or remove.

### B. Invalid / non-schema tags

- **`cluster/cs-ml`** (cs-ml is a *field* facet, not a cluster) appears on source stubs `boyda-2021-su-n-flows.md`, `kanwar-2020-equivariant-flow.md`, `radford-2018-gpt1.md`, `vilnis-2015-gaussian-embeddings.md`, and on wiki stubs `Activation Functions` (questionable), `Contrastive learning`, `Language Modeling`, `Recurrent networks`, `Softmax`, `Syntactic structure in neural networks`, `Transformer Architecture`. Drop the cluster tag (field/cs-ml already present where applicable).
- **`cluster/statistics`** (not in closed vocab) on `wiki/concepts/Missing information principle.md` and `wiki/concepts/de Finetti representation theorem.md`. Replace with `cluster/methodology` or drop.
- `gubser-1998-gauge-gravity.md` — tagged `cluster/participatory/quantum-foundations`; `cluster/gauge-theory` would fit better/alongside (soft flag).
- `wiki/concepts/Vanishing gradient.md` — lists "exploding gradient problem" as an *alias*; they are dual phenomena → make it a related concept, not an alias.
- `wiki/concepts/Relational Quantum Mechanics.md` — empty `aliases:` key (omit or give a value).

### C. Broken / dangling wikilinks inside otherwise-valid stubs

(retargeting chores; **not** ghost nodes)

- `[[Confirmation bias]]` → retarget to `[[Belief perseverance and confirmation bias]]`: on `wason-1960-rule-discovery.md`, `wiki/concepts/Motivated reasoning.md` (and the `taber-2006` note relies on the alias).
- `[[Unity of Consciousness]]` (no target/alias): `hurley-1998-consciousness-in-action.md`, `cleeremans-2003-unity-consciousness.md`.
- `[[Consciousness and the hard problem]]` (no page): `wiki/concepts/Consciousness.md`, `Default Mode Network.md`, `Dynamic functional connectivity.md`, `Entropy and consciousness.md`.
- `[[Free-energy principle active inference]]` (no page): `wiki/concepts/Consciousness and Active Inference.md`, `Ego dissolution.md`.
- `[[Generalized Bayes]]` (no page): `knoblauch-2022-generalized-variational-inference.md`.
- `[[Agglomerative information bottleneck]]` (no page): `pereira-1993-distributional-clustering.md`.
- `[[Attention Mechanism]]` (ambiguous, no single page): `krotov-2016-dense-associative-memory.md`.
- `[[Precision-weighted attention]]` (no page; canonical is `Attention as Precision`): `sims-2003-rational-inattention.md`, `seth-2013-interoception.md` (resolves via aliases there).
- `[[Participatory Realism]]` → `[[Participatory realism (it from bit)]]`: `No-Signalling Principle.md`, `Quantum State Reduction.md`.
- Source-slug mismatches: `[[he2016resnet]]`→`he-2016-resnet` (`Deep Networks.md`); `[[sims2003-rational-inattention]]`→`sims-2003-…` (`Rational inattention.md`); `[[do carmo (1992)…]]`→`docarmo-1992-…` (`Exponential map (Riemannian).md`); `[[radford-2019-gpt2]]`→`radford2019-gpt2` (`Zero-Shot Learning.md`); `[[sakthivadivel-2022…]]` companion-paper dup slugs (Friston-2019/Da-Costa-2021).
- `[[Self-attention]]` (no page): `wiki/concepts/Sparse Attention.md`.
- `[[Thermal time hypothesis]]` (no page): `wiki/concepts/Tomita-Takesaki theorem.md`.
- `[[Hamiltonian formulation of belief dynamics]]` → `[[Hamiltonian belief dynamics]]`: `wiki/concepts/Symplectic geometry.md`.
- `[[Active Inference]]` / `[[Free Energy Principle]]` (no exact pages): `wiki/concepts/Niche Construction.md`.
- Casing-only links to verify: `[[Integrated information theory]]`, `[[Fibre Bundle]]`/`[[Classifying Space]]` from `Characteristic Classes`, several `[[Speed-Accuracy Tradeoff]]`/`[[Reaction Time Distributions]]` casing variants.

### D. Mis-sourced / under-sourced wiki stubs (claims not supported by cited source)

- `wiki/concepts/GL(K) gauge group.md` — sole source is an NLP probing paper that does **not** support the GL(K)/symmetric-space claims; needs proper gauge-theory + manuscript sourcing.
- `wiki/concepts/Gaussian Beliefs.md` — VAE/IB/matrix-cookbook sources don't ground the congruence-transport/KL-consensus claims (load-bearing concept).
- `wiki/concepts/Quantum Measurement.md` — measurement-problem/QBism claims cited only to optomechanics papers; should cite `brukner-2016-quantum-measurement-problem`.
- `wiki/concepts/Bounded Rationality.md` — Simon/KL-cost claims effectively unsourced (only `pilgrim-2023`).
- `wiki/concepts/Stochastic Thermodynamics.md` — Jarzynski/Crooks/TUR claims sourced only to an optomechanics review.
- `wiki/concepts/Consciousness and Active Inference.md` / `Generative model.md` — single tangential source for foundational claims.

### E. Duplicate-source citations *inside* wiki pages (self-resolving once §2 merges land)

- `[[friston-2015-duet]]` + `[[friston-frith-2015-duet]]` both cited on `Generalised synchrony.md` and `Sensory attenuation.md`.
- `[[lloyd-2002-computational-capacity-universe]]` + `[[Lloyd2002-computational-capacity]]` both on `Information is Physical.md`.
- `gao-2017-neural-dimensionality` + `gao-2017-neuroscience-dimensionality` both on `Dimensionality reduction.md`.

### F. Citation contradictions between duplicate notes (must be resolved on merge — see §2b)

Lloyd-2002 journal (PRL vs Nature); Swingle-2012 (PRD vs PRB); Deutsch-2015 DOI; Maldacena (ATMP-1998 vs IJTP-1999); Clark-2013 DOI; Deffuant-2000 vol/pages; Petz-1996 internal smallest/largest-metric contradiction; Anderson-1980 p-value (p<.01 vs p<.05 on F(1,54)=7.86); SE(3)-Transformer ScanObjectNN result (72.8% vs 85.0%).

---

## 5. Case-insensitive basename collisions (28)

All 28 are `papers/<slug>.md` ↔ `refs/<slug>.md` pairs with identical basenames — i.e. the same work under the same slug in two folders, producing **ambiguous `[[wikilink]]` resolution in Obsidian**. **Every one is resolved by the corresponding §2 merge** (keep the papers/ reading note, fold the refs/ unique content, delete the refs/ copy → basename becomes unique). The 28:

`blei-2017-variational-inference`, `brukner-2018-no-go-observer-facts`, `carhart-harris-2014-entropic-brain`, `chalmers-2013-panpsychism`, `chalmers-2016-combination-problem`, `clark-2019-bert-attention`, `connes-rovelli-1994-thermal-time`, `fiedler-1973-algebraic-connectivity`, `friston-2008-dem`, `friston-2023-fep-simpler`, `fuchs-2017-participatory-realism`, `hoffmann-2022-chinchilla`, `katharopoulos-2020-linear-transformers`, `luppi-2019-consciousness-integration-diversity`, `nickerson-1998-confirmation-bias`, `petz-1996-monotone-metrics`, `quine-1951-two-dogmas`, `rovelli-1996-relational-qm`, `schwarz-1978-bic`, `slonim-2000-agglomerative-ib`, `sonderby-2016-ladder-vae`, `strawson-2006-realistic-monism`, `strouse-2017-deterministic-ib`, `tishby-1999-information-bottleneck`, `uhlmann-1976-transition-probability`, `verlinde-2011-entropic-gravity`, `wheeler-1990-it-from-bit`, `wigner-1960-unreasonable-effectiveness`.

> Two collisions — `carhart-harris-2014-entropic-brain`, `connes-rovelli-1994-thermal-time`, `hoffmann-2022-chinchilla`, `wheeler-1990-it-from-bit` — appear in the basename list but **were not in the 77 duplicate-title clusters** (their titles differ enough between folders, or the panel didn't reach them). They are still same-work papers/refs mirrors and should be merged on the same principle; flag for the human to confirm alongside the §2 batch.

---

## 6. Index drift

`index.md` is missing **69 source-paper entries** and **6 wiki-concept entries** (from `_dup_scan.json → missing_index` / `wiki_missing`). These need adding to `index.md` so the catalog is complete.

### 6 wiki concepts not in index.md (list by name)

1. `Belief perseverance and confirmation bias`
2. `Bounded confidence`
3. `Echo chambers and polarization`
4. `Opinion dynamics`
5. `Reaction time distributions`
6. `Sociophysics`

(All six are **social-physics / belief-dynamics** pages — the index's social-physics section is the part most behind.)

### 69 source papers not in index.md (summary)

The 69 fall into three buckets:

- **(a) Duplicate-cluster members that should never be separately indexed** — the camelCase/refs copies slated for deletion in §2 (e.g. `Bissiri2016-generalized-bayes`, `Lloyd2002-computational-capacity`, `Quine1951-two-dogmas`, `kullback1951information`, `clark2013whatever`, `clark2019does-bert-look`, `nickerson-1998-confirmation`, `anderson1980-belief-perseverance`, `flache2017-opinion-dynamics`, `friston-2015-duet`). **Do the §2 merges first**, then index only the surviving canonical.
- **(b) Surviving canonical notes from §2 that simply were never indexed** — e.g. `adlam-2022-cross-perspective`, `bartlett-2007-reference-frames`, `beal-2003-variational-bayesian`, `bialek2001predictability`, `bissiri-2016-general-bayesian-updating`, `bonnabel-2009-spd-fixed-rank`, `bousso-2002-holographic`, `carlip-2014-emergent-gravity`, `castellano-2009-…`, `caticha-2019-entropic-dynamics-qm`, `chechik2005…`, `clark-2013-predictive-brains`, `deffuant2000-bounded-confidence`, `dempster-1977-em-algorithm`, `deutsch-2015-constructor-information`, `foerster-2016-dial`, `friedkin1990-…`, `friston-2017-active-inference-process-theory`, `fuchs-2020-se3-transformer`, `fuchs2014-qbism-locality`, `gao-2017-neural-dimensionality`, `hegselmann-2002-opinion`, `hewitt-2019-structural-probe`, `hinton-2002-products-of-experts`, `jacobson-1995-einstein-equation-of-state`, `jiang2023-mistral7b`, `johnson-2011-…`, `kirchhoff-2018-markov-blankets-of-life`, `lahav-2022-relativistic-consciousness`, `latane1981psychology`, `lloyd-2002-computational-capacity-universe`, `maldacena-1999-adscft`, `nickel-2017-poincare-embeddings`, `padmanabhan-2010-thermodynamical-gravity`, `press2022-alibi`, `ramsauer2021hopfield`, `sakthivadivel2022-…`, `sengupta-2016-neuronal-gauge`, `sengupta2017gauge`, `su2024roformer`, `swingle-2012-…`, `VanRaamsdonk-2010-…`, `vanrietvelde-2020-qrf-perspective-neutral`, `voita-2019-attention-heads`, `wainwright-2008-graphical-models-variational`, `zurek-2003-einselection`.
- **(c) Genuinely new, non-duplicate notes never indexed** — `dehaene-2011-global-neuronal-workspace`, `donnelly-freidel-2016-local-subsystems`, `dosovitskiy-2020-vit`, `garciaperez-2018-multiscale`, `hameroff-1996-orch-or`, `maldacena-2013-er-epr`, `radford2019-gpt2`, `raffel2020exploring`, `ramstead-2019-enactive-inference`, `ramstead2020variational`. These should be added to the appropriate index sections regardless of the dedup work.

---

## 7. Recommended fix plan

**Do nothing yet.** Every step below is a **vault WRITE** and requires explicit user confirmation before execution. Execute in this order so later steps see a clean state.

**(a) Merge duplicates per §2 (largest, highest-value).**
   - First the 57 `merge-and-delete-redundant` clusters (§2a) — fold unique content into the canonical, delete the redundant note(s). This also auto-resolves all 28 basename collisions (§5).
   - Then the 20 `needs-human-judgment` clusters (§2b) — for each, surface the specific citation contradiction / role-reversal / link-routing issue and let the user adjudicate before writing. Preserve inbound-link slugs as aliases where the *refs* slug is the live backlink target (Hegselmann-Krause, Bartlett-Rudolph-Spekkens, Bialek, Nickel-Kiela, Bonnabel-Sepulchre, Fuchs-2014).
   - Apply the per-cluster citation fixes (Lloyd→PRL, Swingle→PRD, Deutsch DOI, Clark-2013 DOI, Deffuant vol/pages, Petz internal ordering, SE(3) result, Anderson-1980 p-value-vs-source).
   - *This is the single most important recommendation: consolidating the 77 same-work clusters removes the dominant defect class and the basename ambiguity in one pass.*

**(b) Resolve stubs per §3 (after dedup, since some merges feed targets).**
   - Exclude the 2 template artifacts from the queue (keep files).
   - Execute the 27 `merge-into-existing` redirects (fold + alias).
   - Elaborate the 10 high-priority concept pages; schedule the 43 medium/low as ongoing.
   - Fix the §4 frontmatter/tag/link issues (invalid `cluster/cs-ml` & `cluster/statistics` tags, year/slug mismatches, dangling-wikilink retargets, mis-sourced claims).

**(c) Reconcile `index.md` (§6).**
   - Add the 6 missing concepts and the bucket-(b)/(c) surviving canonical papers; **do not** index the bucket-(a) notes that step (a) deletes.

**(d) Backtick the cosmetic `[[links]]` in `log.md` (§1).**
   - Convert the illustrative example wikilinks in `log.md` to inline code (`` `[[Natural gradient]]` ``) so the scanner stops reporting `log.md` as a broken link. Lowest priority, purely cosmetic.

Each of (a)–(d) is independent and confirmation-gated; (a) should precede (b)/(c) because deletions change the target and index sets.
