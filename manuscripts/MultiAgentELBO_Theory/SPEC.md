# Authoring spec: gauge-covariant VFE at one base point and its renormalization

Read this file in full before editing any file in this folder (`manuscripts/MultiAgentELBO_Theory/`
in the Research vault, formerly `Theory/` in the MultiAgentELBO repository). It fixes the
architecture, the writing and status rules, the notation, and the mechanics. The mathematical
content the documents must contain, and the typed constructions they rely on, are in this folder's
`CONTENT.md`. Earlier rules and dated consolidations are in git history (MultiAgentELBO `Theory/`
and this vault's former `manuscripts/gauge_vfe_rg/`) and in MultiAgentELBO `docs/research-log/`;
they are not authority for new text.

This spec replaced the earlier single-file spec on 2026-09-23, after the streamlining review in
MultiAgentELBO `docs/reviews/2026-09-23-theory-streamlining-review/` (`REPORT.md`, `phase2/PLAN.md`). The
author's decisions D1 to D13 recorded there govern and are built into the rules below; among them,
the thermodynamic Fisher theorems are ESTABLISHED at their stated hypotheses (D9), and prose,
duplication, and disclaimers are trimmed without cutting any result beyond the plan's cut list
(D10).

## 0. Architecture and scope

Three documents share one source directory, one preamble style, and one bibliography.

- **Main manuscript** (`main.tex`): the theory at one fixed base point `c_*`. It develops agents
  as local sections of belief and model associated bundles of one principal `G`-bundle, their
  independent dynamic interaction links, the normalized joint law and one collective evidence
  bound, attention and selective communication, fiber information geometry and inference
  histories, fast beliefs and slow models, exact coarse-graining of the pointwise agent network,
  and meta-agent formation. It must be readable on its own, contains no `\cref` into a
  supplement, and may name a supplement as a document.
- **Supplement G** (`supplement_gaussian.tex`): the multivariate-Gaussian realization. It cites
  the main manuscript and never Supplement B. Its coarse families admit newly generated
  positive-semidefinite self terms; the strict no-new-anchor pair family is a named subfamily
  (`def:cg-no-new-anchor-pair`, in the main manuscript).
- **Supplement B** (`supplement_base.tex`): base transport, infinite networks, and spatial
  realizations, deferred until the single-point theory is complete; it may cite the main
  manuscript and Supplement G. It carries connections, covers and connection descent,
  base-direction pullbacks and section-space histories, multi-point designs, the relative-frame
  apparatus, the asymptotic Wilsonian apparatus (mode exponents, tempered comparisons, interaction
  beta functions, fixed points, scale connection), and the lattice cluster, whose typing (lattice
  sites as agents at `c_*` or as base points) is `open:rg-lattice-typing`.

Supplement chapters are numbered G0, G1, ... and B0, B1, ... (chapter 0 is the introduction);
their appendices are GA, GB and BA to BD.

The main manuscript's renormalization is the exact finite-step coarse-graining channel of the
pointwise agent network: effective action, residual, finite-step multipliers, and the native
growth bound. It is called exact coarse-graining. Words such as relevant, irrelevant, fixed
point, and beta function are not used in the main manuscript except in one pointer to Supplement
B and in the related-work chapter when they describe other authors' constructions. The
interaction graph at `c_*` is the support of the source prior, a structural parameter that is
complete unless masked; attention weights are strictly positive on it, and dynamic structure is
carried by attention weights and link values. Discrete edge creation and deletion is one open
problem (`open:obs-edge-creation`), not part of the model; coarse multigraphs are induced
structure. Meta-agent membership may be random: the finite partition catalog of the normalization
models (hierarchical or global normalization), typed as the structural mark `R_\ell`, is intended
at `c_*` and enters the multiscale-VFE chapter; it creates no edge. The finite-depth formation
theorem and its proofs stay in the main manuscript, with the scope stated in the chapter.

Chapter 1 of the main manuscript may state the aim of the research program in the manuscript's
own typed vocabulary: a participatory multi-agent theory in which agents are local sections,
collectives form through their coupled inference, and parents act back on their children through
normalized laws. It must not import content, results, labels, or terminology from the author's
earlier program manuscript (PIFB2), which is not cited. Interpretation beyond what the
mathematics uses belongs in the interpretation chapter and later in a separate program paper.
The interpretation chapter distinguishes proved model comparisons from open empirical identification.
The September 26 review closes the D13' selection statement with a manuscript proof; no replacement
conjecture is required. Decision D13 was revised by the author on 2026-09-24 (D13'): the former
conjecture, formation on the four-cycle from every Gaussian initial mean with probability bounded
below uniformly in the regime parameter, is the ESTABLISHED proposition
`prop:phil-seeded-contrast-formation`, with blocks restricted to `2 <= |I| <= |V|-1`, whose
probability comes from the preparation's matching seed with source learning idle. The theorem,
under the unchanged label `conj:phil-contrast-formation`, is the adiabatic law-level selection
statement: at a fixed small temperature and learning mobility `epsilon_L -> 0`, the learned
product-row source prior selects one perfect matching from almost every Gaussian initial law, with
recognition mass off that matching tending to zero on a horizon of order
`epsilon_L^{-1} log(1/epsilon_L)`, while the frozen-prior arm's long-time pairing law is symmetric;
its proof is in `ca_selection_proofs.tex`, and its former open-problem row is removed. This does not
settle an explicit joint power-law regime, event-level formation, or parent closure. The subsequent corollary `cor:phil-joint-selection` establishes a joint limit along implicit common mobility thresholds, with a possibly temperature-dependent matching; `prop:phil-temperature-tracking` gives an explicit power condition for tracking only. The executable does
not appear: no repository paths,
code modules, configuration keys, run records, hashes, or software field names in any document.

**Single-point defaults.** In the main manuscript the design is `D={c_*}`; design and incidence
indices are dropped. Belief and model channels use one common local frame `u_i` per agent, a gauge
choice rather than a hypothesis, because no energy, kernel, or evaluator reads the relative frame.
The channels may still carry inequivalent representations, independent link families, and
declared cross maps. The relative frame `h_i` lives in Supplement B and returns to the core only
if frames become dynamical agent states.

## 1. Prose

R1. Write flowing paragraphs in American English. A paragraph develops one idea and may contain
several claims. No bullet lists in the body, no spacing macros (`\;`, `\,`, `\!`), no horizontal
rules, and none of these phrases: "key insight", "crucially", "critically", "notably",
"importantly", "it's worth noting", "fundamentally", "leverages", "underscores". Punctuate
displays as sentences. Refer to labeled objects only with `\cref` or `\Cref`; never hard-code a
chapter, section, or result number.

R2. Every definition, standing hypothesis, theorem, proposition, lemma, corollary, conjecture,
open problem, and claim-bearing remark is a numbered statement made with the heading macros
`\definitionheading`, `\hypothesisheading`, `\lemmaheading`, `\propositionheading`,
`\theoremheading`, `\corollaryheading`, `\conjectureheading`, `\openproblemheading`, and
`\remarkheading`. A former construction is a definition and a former requirement is a standing
hypothesis (the old macros are compile-only aliases). The statement runs from its heading to its
status tag; hypotheses of a result appear inside its statement; commentary after the tag makes no
new claim. The `hypothesis` heading is reserved for standing restrictions adopted for a whole
chapter or part, and it says what it excludes.

R3. Each chapter opens with the question it answers, its main result stated informally with a
`\cref`, and where that result is used, then gives its scope paragraph (R5). Each main-manuscript
chapter ends with a physicist's summary of at most one page. A running example, three agents at
`c_*` in one loop with nontrivial holonomy, is introduced in the geometry chapter and reused.

## 2. Statements and status

R4. Status is shown once per numbered statement. Definitions, standing hypotheses, conjectures,
and open problems carry their status in the heading type and need no tag. Every theorem-type
statement (lemma, proposition, theorem, corollary) and claim-bearing remark carries exactly one
tag, and a statement with several labeled conclusions carries one tag for all of them:

- `\status{ESTABLISHED}`: proved in this manuscript;
- `\status{STANDARD}`: a known result, cited to a checked primary source with a theorem or
  section locator;
- `\status{NUMERICAL}`: supported only by a named computation; computation is not proof.

The fourth tag, `\status{NOT-CLAIMED}`, appears once per scope paragraph (R5) and nowhere else. A
refutation is an ESTABLISHED negative statement, never NOT-CLAIMED. Unnumbered text that
motivates, summarizes, restates, or points makes no new claim and carries no tag; the
introduction, chapter openings, and summaries cite labels instead. If a sentence needs a status
that no numbered statement provides, number it. A captioned table summarizing numbered statements
(such as the transformer correspondence table) gives each row's standing (derived, declared,
absent) as table content, with a `\cref` to the statement behind each derived row, and carries no
tags. The status table of Chapter 1 (`tab:status-taxonomy`) lists exactly these tags and heading
types with their meanings and matches this section in substance.

R5. Scope. Chapter 1 contains one section, "Standing conventions and scope", which states once
what the whole manuscript declines to claim: physical time, spacetime, agency, ontology,
canonical selectors, graph links as base transport, and, during the single-point phase, base
maps, neighborhoods, and connection descent. Each chapter may add one scope paragraph after its
opening, listing chapter-specific declined claims (one `\status{NOT-CLAIMED}` tag for the
paragraph) and open items (each with a `\cref` to its open problem). Nothing in the standing
section is repeated in a chapter. Declining a statement is not refuting it; keep the two apart.
A declined statement and the open construction that would settle it are recorded separately: the
declined statement in the scope paragraph, the construction as an open problem with its own
ledger row.

R6. Standing conventions. The same section fixes the defaults: measurable spaces are nonempty and
standard Borel; laws and kernels are normalized and measurable; a coarse channel is a
recognition-independent Markov kernel on latent coordinates that leaves observations unchanged
and, at `c_*`, is vertical over the identity of `c_*`; an admitted observation has finite
positive evidence; structural data are parameters unless a configuration prior or a structural
channel is declared, and the declaration names its law; the interaction graph at `c_*` is the
support of the source prior (Section 0). Absolute continuity of a recognition law with respect to
the posterior is not a default: it is clause (H3) of `hyp:elbo-evidence-domain`, and its failure
is the singular branch of the extended ELBO. A statement mentions only departures from these
defaults. Do not use "declared", "normalized", "actual", "complete", "retained", "exact", or
"fixed" when the word restates a default or a symbol's definition.

R7. Notation. One glyph has one meaning in each document (section 3). A local symbol takes an
unused glyph or a decoration; never write "X here is not the Y of Chapter k", rename instead.

R8. Gaps. A hand-wave ("clearly", "one can show", "for suitable conditions", "in the
appropriate limit") is discharged by a proof, computation, exact condition, or checked primary
source, or becomes an open problem stating what holds, under which hypotheses, what is unproved,
and what would settle it; the gap keeps one sentence and a `\cref`. Never weaken a verb instead.

R9. Numerical support. A NUMERICAL statement names its check once. Seeds, controls, tolerances,
digests, software fields, run records, run commands, and script locators live in
this folder's `verification/VERIFICATION.md` or MultiAgentELBO `docs/`, not in the manuscript. Each document's
numerical index is one table: claim label, check label, what is tested, control, and seed or "no
randomness", with no repository locator. A measurement without a control is not evidence for a
structural claim; if a control was not run, the table says so.

R10. Provenance. No document contains dates other than the title-page date, revision history,
review or certification stages ("draft", "proposed", "pending adjudication", "released",
"certified"), repository paths, API or field names, hashes, or comments recording transcription.
Status is a mathematical fact at the statement. The audit trail lives in MultiAgentELBO `docs/`.

R11. Ledger. Each document ends with one open-problem table (item, `\cref` locator, settling
condition) listing only its open problems and conjectures. It restates no established result.

R12. Citations. Cite primary sources with locators (theorem, section, or equation numbers) for
every STANDARD statement and every attribution. Check that the source says what it is cited for.
Do not re-prove textbook results in full; state them as STANDARD with a citation, and keep a proof
only where the hypotheses differ from the source. A proof is replaced by a citation only after
the locator has been checked; otherwise the proof stays and the statement stays ESTABLISHED. The
manuscript never cites itself or PIFB2 as authority.

The following claim rules were adopted by the author on 2026-09-24. They govern every statement,
open problem, and conjecture about learning, recursion, episodes, and settling conditions.

R13. Learning claims (the Curie rule). Let `H` be the symmetries shared by the generative model with
its observed records, the parameterization, and the kinetics, including the kinetic metric and the
proposal mechanism; `H` may be a group of graph automorphisms or a residual gauge group. A claim
that learning creates or selects a structure that `H` does not fix names the `H`-breaking datum it
amplifies (the initial law, the initial parameter, the model, or the records) and states the
frozen-learning arm on the same data as its null. A claim that learning selects a structure that `H`
fixes names the symmetry it restores, with the frozen arm at the non-invariant initial value as its
null. A claim of selection without such a datum names the hypothesis its mechanism violates and
declares the mechanism as a model element: a rule that reads realized paths, records, or a finite
ensemble, in which case the claim concerns realized paths unless the law of the selected structure
is proved to break `H`; selection among non-unique optimizers, critical points, or branches;
boundary non-uniqueness at masked entries, which is edge creation outside Section 0; or a
nonequivariant metric, mobility, or proposal mechanism. An equivariant law-level learning rule whose
coupled law–parameter system is unique cannot be claimed to break a symmetry shared by the initial
law and the initial parameter; the four-cycle instance is part (c) of
`prop:phil-seeded-contrast-formation`.

R14. Recursive coalescence. A two-stage claim declares a handoff time, deterministic or a stopping
time; a first-stage event of the history up to the handoff, with its block partition; a second-stage
event and its block, with windows measured from the handoff; one statistic of the handoff state (the
probability of the second-stage event, the probability that it has occurred by declared times, or
the probability of a declared block); and a handoff class, fixed before the comparison, that
contains every first-stage handoff and, with probability bounded below, the handoffs of histories
without first-stage formation. The comparison is between histories of one process; processes that
differ in a supplied initial law or parameter differ by an asymmetry that R13 governs. If the
second-stage event, with its block, occurs with probability tending to one uniformly over starts in
the handoff class at the declared windows, the sequence is a supplied-scale sequence, not recursion,
whatever differences appear before those windows; this takes precedence over any margin. Otherwise
the second coalescence counts as recursive only if, after first-stage formation, the second-stage
event has probability bounded below and its block is a union of at least two first-stage blocks, and
the declared statistic is larger after first-stage formation than after a counterfactual handoff in
the class by a margin bounded below. A margin in the other direction, where first-stage formation
delays or suppresses the second coalescence, is recorded as first-stage dependence and does not
count as recursion. A second-stage proof that uses only hypotheses on the handoff state that also
hold for counterfactual handoffs in the class establishes a supplied-scale sequence.

R15. Coherence episodes. A coherence episode, as distinct from the learning episodes indexed by `n`
in `def:full-graph-episode-joint`, carries a restoring clause and a horizon clause. The restoring
clause names the interaction whose restoring rate holds the block's coherence at the declared
resolution above the thermal scale, with the restoring rate times the squared resolution, divided by
the temperature, tending to infinity; the condition is evaluated on the actual sheet law or on the
source-marginal landscape, not on a sheet held fixed by hand. The horizon clause requires either
horizons short compared with the stationary recurrence time of the event, measured by the rate of
entrance into it from a set of stationary mass bounded below and not by its stationary occupation,
or a probability or rate of the event exceeding its stationary value by a margin bounded below.
Coherence that meets the restoring clause and fails the horizon clause, as when its stationary
probability tends to one, is restored equilibrium coherence: a claim may state it, with its
restoring clause, as a property of the stationary law or of relaxation from declared starts, but not
as formation. Coherence that fails the restoring clause is coincidental and does not count as
formation.

R16. Settling conditions. Each open problem's and conjecture's settling condition is restricted to a
stated class, and both of its branches are nontrivial: neither branch is met by an existing
statement of the documents or by a trivial construction.

## 3. Notation

The main manuscript uses these symbols with these meanings only; supplements keep their own short
tables and never reuse a core glyph with a different meaning. "Replaces" names the rename to apply.

| Symbol | Meaning | Replaces |
| --- | --- | --- |
| `\mathcal C`, `c`, `c_*` | contextual base, a context, the fixed base point | `\mathcal C` as a cone (cones are `\mathcal W`); `c` as a constant (use `\mathrm c_1,\mathrm c_2`) or variance |
| `\mathscr P_G`, `G`, `\pi` | principal bundle, structure group, principal projection | `\varpi_\ell` for principal projections; `G_\ell` as graph datum (use `\mathfrak N_\ell`) |
| `\rho_b`, `\rho_m`; `\widehat\rho_x`; `\mathbb V`; `\rho^{\mathbb W}_x`, `\mathbb W_x` | representations on the belief and model sample fibers; pushforward actions on law fibers; a real vector sample fiber of a channel, with block coordinate spaces `\mathbb V_I` and fixed fiber `\mathbb V_{I,\mathrm{fix}}=\ker L_I`; representation of the linear feature tier and its feature fiber | `\rho_x`, `V_x` for the feature tier; `\mathsf F_I` for the fixed fiber |
| `\mathcal B_x`, `\mathcal E_x`, `\varpi_x` | law fiber, associated bundle, associated projection, channel `x\in\{b,m\}` | |
| `u_i`, `g_i`, `U_i`, `\varphi_i` | common local frame of agent `i`; passive re-expression (vertex gauge); frame relative to a reference point `\sigma` of the fiber, `u_i=\sigma\cdot U_i^{-1}`; local function of an automorphism | `a_i`, `b_i`, `a_i^x`, `h_i^x`, `R_i^x` as rechoices; `k_i^x` for automorphisms |
| `T_{ij}` | pointwise frame comparison | `T` as transition, tree, rescaling, or temperature |
| `\mathfrak I=(V,E,\bar{\ })`, `e`, `\bar e` | interaction multigraph at `c_*`, oriented edge copy, reversal | `\mathfrak I_D` as incidence set (Supplement B writes `I_D`) |
| `\Theta^x_e`, `\mathsf t^x_e`, `\mathring\Theta^x_e=U_i^{-1}\Theta^x_eU_j` | independent link on edge copy `e:j\to i`, with `\Theta^x_{\bar e}=(\Theta^x_e)^{-1}`; link map of the fiber; per-edge twist | `\Omega^{x,\ell}_{ij}`, `B_e`, `\tau^x_e`; `H^x_e` (horizontal lift, Supplement B only) |
| `\Theta^x_p`, `\Theta^x_{I\leftarrow i}`, `\widehat\Theta^x_e` | path product, tree transport to a block root, block-dressed edge | `\tau^x_{I\leftarrow i}`, `V^x_e` |
| `\mathrm{Hol}^x(p)`, `\mathrm{Hol}^x_I` | holonomy of a closed walk, based holonomy group of a block | `H_e`, `H_\gamma`, `H^x(\gamma)` |
| `\Phi`, `\widetilde\Phi` | cross-associated-bundle morphisms | `\Phi` as an evolution map, flow, or row free energy |
| `V`, `N`, `i,j` | agent set, number of agents (also the extensive size of a finite labeled mixture), agent indices | `V` as side information, volume, or a vector fiber (use `\mathbb V`) |
| `y`, `\mathsf Y`, `o`, `X`, `\theta` | latent sample, latent space, observation, structural data, generative parameters | `X` as a vector field or process |
| `k_i`, `m_i`; `q_i^b`, `q_i^m`; `\mathfrak q_i^b`, `\mathfrak q_i^m` | belief sample and model presentation of agent `i`; belief-law and model-law sections; law points at the law-point level | |
| `\mathsf Y^{\mathrm{law}}_i`, `\mathsf Y^{\mathrm{cfg}}`, `\operatorname{pres}`, `\kappa^{\mathrm{cfg}}` | law-point block, configuration space, presentation map, presentation kernel; every energy names its level (sample, law point, configuration) | `C` for the presentation kernel |
| `\mathbb P_{\theta,V}`, `\mathbb Q_{V,o,X}`, `\boldsymbol\Pi_{\theta,V,o,X}` | constructed joint, selected recognition coupling, posterior slice | bare `P`, `Q`, `\Pi_o` outside lemma-local use |
| `\mathcal L_V`, `\mathcal F_V=-\mathcal L_V`, `\KL` | ELBO, free energy, relative entropy (use `\Lelbo`, `\Fenergy`, `\KL`) | raw `\mathcal L`, `\mathcal F`, `\operatorname{KL}` |
| `a\in\mathfrak A`, `K_a`, `E_{a,o}` | record factor, its normalized record kernel, its negative log density | `\ell_a`, `K_f`; `a` as design index (Supplement B writes `d`) |
| `\pi_{ij}`, `\beta^{x}_{ij}`, `\alpha^x_i`, `\eta^x_{ij}`, `\mathcal N_i`, `(i,h)` | source prior; attention row of receiver `i` (role mark `P`, `\Pi`, or `Q`); receiver occupancy; event law, which carries no head index; source set (self-edge declared per model); receiving row of head `h` (multi-head label models are `open:obs-multihead-attention`) | `\gamma_{ij}` (use `\beta^m_{ij}`), `b^x_{ij}` |
| `\eta_e`, `\beta_e`, `\Theta_e`, `D_e` | edge-copy indexing at every depth; pair quantities are sums over copies | `D_{ij}` when copies differ |
| `\tau_i`, `\mathsf c_{ij}`, `\mathsf r_i`, `\Fenergy^{\mathrm{att},x}_i` | attention temperature, replicator cost, row relaxation rate, row free energy | `\tau` as clock or tree transport; `u_{ij}`; `\gamma_i` as rate; `\Phi^x_{i,\ell}` |
| `S^Q_e`, `S^K_e`, `K^v_e`; `\mu^Q_i`, `\mu^K_j`, `d^\circ_i` | query and key comparison maps, composed value kernel; projected query and key means, dot-product scale | `K_e` for comparison maps, `S_Q`, `S_K` |
| `\mathsf L^{\mathrm{enc}}_e`, `\mathsf L^{\mathrm{tr}}_e`, `\mathsf L^{\mathrm{dec}}_e`, `\mathsf L_e`, `\mathsf L^{\mathrm{val}}_e` | encoder, transmission, decoder, composite, and value linear maps of the communication layer | `A_e`, `C_e`, `D_e`, `L_e`, `L_e^{\mathrm{val}}` |
| `\Sigma^+_i`, `\Sigma^{\mathrm{pred}}_i`, `\widetilde W_i=W_i/\tau_i`; `S_j`, `\Upsilon`, `v` | receiver posterior and predictive covariances, tempered receiver weight; source sample, random side information and its values | |
| `f`, `s=(s_{\mathrm m},\theta)`; `\mathsf G_{\mathrm f}`, `\mathsf G_{\mathrm s}`, `\varepsilon`, `\mathsf G_\varepsilon=\varepsilon\mathsf G_{\mathrm f}\oplus\mathsf G_{\mathrm s}`, `F_{\mathrm{red}}`; `\lambda` | fast and slow coordinate blocks; block metrics, rate ratio, rate-separated metric, reduced functional; coordinates of a recognition family | `f`, `s` as base maps or sections (Supplement B); `\eta` as recognition coordinates |
| `g^F`, `T^F`, `\mathbf s_\theta`; `\mathfrak k_q`, `\mathfrak g_q`; `\mathfrak t` | Fisher tensor, Amari–Chentsov tensor, score; orbit Fisher form and isotropy algebra at `q`; Fisher duration (information clock) | `\ell_\theta`, `s_\theta` as score; `\tau` as clock |
| `\mathcal Q_\ell`, `\mathsf F_\ell`, `\mathscr V_\ell`, `\operatorname{Fl}^{\mathscr V_\ell}_t` | configuration manifold, coarse configuration map, vector field, its flow | `\mathsf R_\ell` as configuration map, `X_\ell`, `\Phi_t`; `\mathsf F_I` as a fixed fiber |
| `\varkappa`, `\mathfrak K`, `\mathfrak C`, `\operatorname{ret}` | parity amplitude, residual second-moment tensor, signed cross tensor, retained-law map | `\kappa`, `K`, `C`, `\rho` in these roles |
| `\ell` | RG depth only, including the level index of the formation family | `\ell` as likelihood, score, child index, or constant; `s` as formation level |
| `I`, `J`, `A` | child blocks and parent label | `A` as self term (Supplement G only), amplitude, or constant |
| `\mathfrak m_\ell`, `\mathfrak M_\ell`; `R_\ell`, `\mathsf R_\ell` | membership kernel and joint endpoint membership kernel; structural mark sampled by the structural channel (for example a random partition), and its space | `m_\ell`, `M_\ell`; `R_\ell` as a projection; `\mathsf R_\ell` as a configuration map |
| `C_A`, `C^{\mathrm{struct}}_{\ell+1\leftarrow\ell}` | parent coarse kernel, structural channel | `C` as covariance or deterministic map in the core |
| `\mathcal G_\ell` | space of Hoeffding interaction coordinates | `\mathcal G` as an acting group (use `\mathbb G`, stabilizer `\mathbb G_Q`), holonomy image group (use `\mathfrak H_r`), potential (use `\mathscr J_i`), Gaussian fiber (use `\operatorname{Gau}(\mathbb V)`, and `\mathscr C` for a law class in it), or forward map (use `\mathfrak O`) |
| `\gamma\in\mathfrak G`; `\mathsf s_\gamma`, `\mathsf v_\gamma=\nabla\mathsf s_\gamma`, `\mathcal I_\gamma`, `\bar{\mathsf p}_\gamma`, `\mathsf w` | finite mixture or geometry label; bulk log-mass density, tie slope, bulk Fisher density, limiting label law, window coordinate `\theta=\theta_0+\mathsf w/N` | `s_\gamma`, `v_\gamma`, `g_\gamma`, `\pi_\gamma`, `u`; `\gamma` as a rate |
| `\vartheta`, `\mathsf j_m`, `q^{\star,p}_\vartheta` | formation family: learned scalar, proposal marks, restricted optimizer; its other letters that collide with this table (`J_s`, `Q_s`, `A`, `T`, `R`, `f`, `\pi`, `D`, `b`, `c`, `d_i`, `u`, `v`, `x`, `X_t`, `\zeta_e`) are replaced once, in a local table at the chapter opening that the proof appendix shares | `\pi^p_\vartheta`; `s` as level index |

In Supplements G and B the following are fixed: the block reframing group `\Gamma_b=\rho_b(G)`,
equal to `\GL^+(K)` in the Gaussian specialization; operator cones `\mathcal W`; Gaussian
information parameters `(\mathsf h,\Lambda)` with moments `\mu=\Lambda^{-1}\mathsf h`,
`\Sigma=\Lambda^{-1}` and log normalizer `\mathsf A(\mathsf h,\Lambda)`, replacing `(h,J)` and the
covariance `C`; the Gaussian block rescaling `\zeta_\ell`; the horizontal lift `H^x_e`, the
relative frame `h_i`, the design index `d`, the incidence set `I_D`, the base-cocycle residual
`\mathcal R`, the scale bundle morphism `\Psi`, and the covariant defect `\mathcal D\Phi` of a
cross map (it needs a base tangent vector) belong to Supplement B; the core writes an unnormalized
potential as `\widetilde p_X` (not `\Psi_X`), and Supplement G does not use `\Psi`. The lattice
part of Supplement B keeps `b=\tanh h`, `t=\tanh j`, `J_S`, its volume, and its pressures in one
local table at its head; neither the belief channel label nor the relative frame occurs there. The
core defects are the cross-scale morphism defects of the network-state chapter and the vertical
defect cocycle of the fiber-geometry chapter, each written with the glyph of its defining display.
Metrics are sans-serif (`\mathsf G`); chapter-local symbols not listed here are chosen by the
owning chapter under R7 and declared in its opening. The encoding, transmission, and decoding
kernels of the communication layer are `\mathsf E^v_e`, `\mathsf N^v_e`, `\mathsf D^v_e`; the
Hoeffding conditional-expectation operators of the network coarse-graining chapter are written
`\E_{\ell,B}` (not `\mathsf E_{\ell,B}`), as expectations under the product reference.

Label prefixes: `eq:geo-*`, `eq:prob-*`, `eq:gen-*`, `eq:elbo-*`, `eq:exp-*`, `eq:gauss-*`,
`eq:restrict-*`, `eq:ig-*`, `eq:cg-*`, `eq:rg-*`, `eq:obs-*`, `eq:obst-*`, `eq:pb-*`, `eq:hist-*`;
`ch:*`, `sec:*`, `app:*`; `def:*`, `hyp:*`, `thm:*`, `prop:*`, `lem:*`, `cor:*`, `conj:*`,
`open:*`, `rem:*`, `claim:*`; `tab:*`, `fig:*`. A new label's prefix matches its heading type.
Every existing label is kept exactly when text moves or a statement changes type or title (so
`thm:` on a corollary, `cons:` and `req:` labels, `conj:grg-fixed-b-attraction` on a proposition,
and the `-draft` labels all stay), because cross-document references depend on them.

## 4. Mechanics

The preambles are in `main.tex`, `supplement_gaussian.tex`, and `supplement_base.tex`; chapter
files contain no preamble and no `\begin{document}`, start with `\chapter{...}` and a
`\label{ch:...}` (appendix files with their appendix heading and `\label{app:...}`), and add no
`\usepackage` lines. Cross-document references use `xr-hyper`, loaded before
`scientific_report.sty` (which loads `hyperref`), through `\externaldocument{main}` in both
supplements and `\externaldocument{supplement_gaussian}` in Supplement B; every label is unique
across the three documents. Available: `amsmath`, `mathtools`, `bm`, `mathrsfs`, `cleveref`,
`natbib`, `tikz`, `longtable`, `xr-hyper`, and `sciencetable` from `scientific_report.sty`. Shared
macros are defined identically in each preamble: `\KL`, `\E`, `\R`, `\given`, `\Tr`, `\Sym`,
`\PSD`, `\GL`, `\Lelbo`, `\Fenergy`, `\status`, and the heading macros of R2. Use them.

Proof headings have one form in all three documents. A proof opens a new paragraph with
`\noindent\emph{Proof.}`; in a proof appendix, a proof of a statement made in a chapter opens with
`\noindent\emph{Proof of \Cref{<label>}.}`, and a proof of only some conclusions of the statement
above it names them (`\noindent\emph{Proof of the early bound and the covector estimate.}`). Do not
use `\paragraph{Proof.}` or an indented `\emph{Proof.}`. A chapter whose longer proofs are deferred
says so once in its opening and points to the appendix section after each statement whose proof
moved (`The proof is in \cref{<appendix section>}.`; one pointer may serve consecutive statements).

The bibliography is this folder's `references.bib`, not the vault-wide `manuscripts/references.bib`.
Check whether a key exists before adding one, and never invent a DOI, page range, or quotation.
Build in a scratch copy of this folder's `*.tex`, `*.bib`, and `*.sty`, never inside this folder (a
stale `main.aux` there breaks BibTeX), then copy the finished `main.pdf` back, since it is the
folder's only tracked build product. Run `latexmk -pdf` on
`main.tex`, then `supplement_gaussian.tex`, then `supplement_base.tex` (each supplement reads the
`.aux` files of the documents it cites). A change is finished only when all three documents build
with no undefined references or citations and no multiply defined labels.

When several agents edit in parallel, each edits only its assigned files; `main.tex`,
`supplement_*.tex`, `SPEC.md`, `CONTENT.md`, and `references.bib` are edited by one designated
agent at a time.

**Sequential continuation, coherence and first-block scope.** The proved
prop:phil-selected-pair-persistence transfers the late selected law to actual
path persistence at Euclidean resolution T^(1/4) for duration T^(-1/4).
This is restored equilibrium coherence under R15. The separate
prop:phil-early-block-null keeps the original early contrast detector and
proves equality in the limit of conditional first-block laws for
epsilon_L=o(T^(1/4)). Neither result closes the original adaptive-family
regime epsilon_L=T^(1/8), its loop comparison, or parent activation.

**Sequential continuation, parent scope.** The propositions
prop:phil-actual-conditioned-parent and prop:phil-actual-parent-dynamics
activate the existing fixed channel after a completed late coherence prefix
on the joint schedule. They give separate vanishing averaged discarded KL
and complete retained-path TV while the parent learns from its own law.
They do not replace the actual activation distribution by an independent
Gaussian, condition on future survival, close arbitrary realized histories,
or establish a recursive next formation.
