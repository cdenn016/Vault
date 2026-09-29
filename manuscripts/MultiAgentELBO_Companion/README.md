# A physicist's companion to the MultiAgentELBO theory

This folder holds a pedagogical companion to the three technical documents in
`../MultiAgentELBO_Theory/`: the main manuscript (`main.tex`, cited here as MT),
Supplement G (`supplement_gaussian.tex`), and Supplement B (`supplement_base.tex`).
The technical documents are the authority. The companion explains them to a trained
physicist and states plainly, for every main result, what kind of knowledge it is and
whether the theory delivers what it says. It proves nothing. It is not governed by the
theory folder's `SPEC.md`, which applies only to the technical documents, and it never
feeds content back into them.

Read this file in full before writing or revising any companion chapter.

## 1. Purpose and reader

The reader is a trained physicist (field theory, statistical mechanics, lattice gauge
theory, information theory at the level of Cover and Thomas) who is the author of the
program's intuitions but finds the technical documents hard to read: dense notation,
long chains of conditionals, bookkeeping hypotheses mixed with substantive ones,
nonstandard vocabulary, and abstraction that hides what a formula does. The companion
answers four questions for each technical chapter.

1. What question does the chapter answer, and what is the physical or inferential
   picture behind the answer?
2. What do the main objects and formulas mean, term by term, in the reader's own
   language, including their limiting cases?
3. What kind of knowledge is each main result: solid at the generality the theory uses,
   true only on a toy instance, true only under a substantive assumption, supported only
   by computation, open, or vague?
4. Does the chapter (and the theory as a whole) actually do what its own words say it
   does? "Works" here means exactly this: whether the mathematics delivers the claim,
   not whether anything is computable today.

## 2. Rules for companion text

**Never re-prove.** When the technical document proves a statement, the companion
states it in plain words and cites it: "the bound is invariant under passive frame
changes (\MT{cor:elbo-independent-frame-invariance})". Do not reproduce proofs, proof
sketches longer than two sentences, or chains of lemmas. A one- or two-sentence
intuition for why a proved result is true is encouraged when it helps, and is labeled
as intuition ("the reason, informally, is ..."). Never present intuition as proof.

**Never change the strength of a result.** State each result with the scope and
hypotheses it actually has in the technical document, no stronger and no weaker. If a
theorem holds for compact `G` only, say so; if a result is proved on the four-cycle
only, say so; if an ESTABLISHED statement is a refutation, it is a solid negative
result, not an open question. Before writing a status or verdict, read the statement
itself (heading to status tag) and, when the scope is unclear, its proof. The chapter
openings, scope paragraphs, and physicist's summaries of the technical documents are
useful but are not a substitute for the statements.

**Cite with the macros.** Every reference into the technical documents uses
`\MT{label}` (main manuscript; prints "MT Theorem 5.3"), `\mtc{label}` (lowercase type
mid-sentence), `\MTeq{label}` for equations (prints "MT (5.3)"), and `\SG{...}`,
`\sgc{...}`, `\SGeq{...}`, `\SB{...}`, `\sbc{...}`, `\SBeq{...}` for the supplements
(their numbers already carry G or B). Each macro accepts a comma-separated label list,
but prefer one label per macro. Use only labels that exist: check with
`grep -n 'label{<label>}' ../MultiAgentELBO_Theory/*.tex` or in the heading macros
(`\theoremheading{Title}{label}` and similar). A wrong label is a build error. Never
hard-code a technical-document number. Companion displays are unnumbered (`\[ \]`,
`equation*`, `align*`); the companion has no numbered statements of its own.

**Classify every main result with one badge.**

| Badge | Macro | Meaning |
| --- | --- | --- |
| SOLID | `\SOLID` | Proved in the technical documents (ESTABLISHED) or a checked textbook result (STANDARD), at the generality the theory relies on. Established negative results (refutations, no-go statements) are SOLID. Say "standard in substance" when the mathematics is textbook and the novelty is the typing. |
| TOY | `\TOY` | Proved, but only on a named small or special instance: the four-cycle, a pair, three binary agents, a scalar or abelian case, a specific constant schedule. Its mechanism is not established beyond that instance. |
| COND | `\COND` | Proved under a hypothesis that is substantive (it could fail in the cases the program cares about) and is not shown to hold there. Name the hypothesis. Technical hygiene (standard Borel spaces, measurability, integrability that holds in every model the program uses) does not make a result COND. |
| NUM | `\NUM` | Supported only by a named computation. |
| OPEN | `\OPEN` | An open problem or conjecture. |
| VAGUE | `\VAGUE` | An interpretation, reading, or programmatic statement without a precise mathematical statement behind it, or a construction whose meaning is not pinned down. |
| CHOICE | `\CHOICE` | A definition or standing hypothesis that is a substantive modeling commitment (where physics enters), as opposed to notation. Use it for the definitions a reader must accept to accept the theory. |

**Give a delivery verdict.** Each companion chapter ends with a `verdictbox` whose
argument is one of `\DELIVERED`, `\NARROWER` (delivered, but in a narrower setting than
the headline wording suggests), `\PARTIAL` (part proved, part open), or `\NOTDELIVERED`
(the claim is posed but not proved). The box quotes or paraphrases what the technical
chapter says it does (its opening paragraph and the introduction's reading map), says
what the proved statements actually give, and names the gap. Be direct in both
directions: say when a chapter does exactly what it says, and say when its wording
promises more than its theorems. When a result is correct but standard (a known
identity in new notation), say so; that is information, not criticism.

**Translate into physics, and grade the translation.** Use `analogy` boxes
(`\begin{analogy}{exact}` or `{loose}` or `{structural}`) to name the physics
counterpart of a construction: Gibbs variational principle, Kadanoff blocking,
integrating out, Wilson loops, pure gauge, adiabatic elimination, Ornstein-Uhlenbeck
relaxation, spontaneous symmetry breaking, and so on. State whether the correspondence
is exact (a theorem identifies them), structural (same form, different content), or
loose (suggestive only). Never let an analogy carry a claim the technical documents do
not make.

**Explain formulas term by term.** Reproduce a key display (using the shared macros
`\KL`, `\E`, `\Lelbo`, `\Fenergy`, `\GL`, `\PSD`, `\Tr`, and the notation of the
technical documents), then say what each term is, why it has that form, what it
reduces to in familiar limits (one agent, Gaussian laws, abelian or trivial links, zero
temperature, flat links, a tree graph), and which sign or scale matters. Prefer a
concrete example (a pair, the running three-agent loop, a Gaussian) to abstraction.

**Separate conditions that matter from hygiene.** Use one `hygiene` box per chapter
(or per major result) to sort the hypotheses: which could fail in the models the
program cares about (for example, absolute continuity of the recognition law,
compactness of the structure group, a supplied hierarchy of interaction strengths,
instantaneous refresh), and which are measure-theoretic or regularity hygiene that a
physicist can take for granted on a first reading.

**Decode the house style.** The technical documents follow a strict authoring spec
(`../MultiAgentELBO_Theory/SPEC.md`): status tags on every statement, one
"NOT-CLAIMED" scope paragraph per chapter, rules R13 to R16 on what may be called
learning-driven selection, recursion, a coherence episode, or a settling condition,
and a ban on Wilsonian vocabulary in the main manuscript. Explain these where they
shape a chapter, and say whether a given qualifier is substantive or bookkeeping.

**Toy results are grounding, not direction.** Small networks (pairs, three-agent
loops, the four-cycle, three binary agents) exist in the theory to ground and validate
constructions. A small-network obstruction is not a general blocker, a small-network
positive result is not a general theorem, and no mechanism (phase transitions,
condensation, symmetry breaking, recursive formation) is ruled in or out by them. When
presenting a TOY result, separate its mechanism-level content, which may survive at
large N but is conjectural until proved there, from its small-N specifics (constants,
spectral gaps, seeded probability floors). The program's target is networks of 512 or
more agents with structure groups such as GL(K,R), GL(K,C), and SU(N); say when a
result's hypotheses (compactness, finite alphabets, scalar fibers) exclude that target.

**Scope gate.** The theory currently works at one base point `c_*`; base-manifold
transport is deferred to Supplement B. Graph links are independent variables on the
edges of the agent network (lattice gauge theory over a zero-dimensional base), not
base transport. Do not propose research, base-transport constructions, or new results.
The companion describes; it does not extend.

## 3. Chapter template

Each companion chapter mirrors one technical chapter and has these sections, in
prose paragraphs with tables where tables help (no bullet lists in running text):

1. `\section{The question and the answer}`: the chapter's question and main result in
   plain language, with its place in the theory's chain.
2. `\section{The picture}`: the intuition, with `analogy` boxes.
3. `\section{Objects and notation}`: a `decoder` table for the chapter's objects,
   symbols, and jargon (term, plain meaning, physics analogue or "none"), followed by
   any notation traps (a glyph that means something else in physics, a word used in a
   nonstandard sense).
4. `\section{The formulas, explained}`: the key displays with term-by-term explanation
   and limiting cases, citing the statements that prove them.
5. `\section{What is proved, and how solid it is}`: a `scorecard` table of the
   chapter's main results (typically 6 to 15 rows, not every lemma) with one badge
   each, followed by the `hygiene` box.
6. `\section{Toy versus general}` when the chapter has TOY content; otherwise fold a
   sentence into section 5.
7. `\section{Open ends}`: the chapter's open problems and conjectures in plain terms:
   what is unknown, and what would settle it.
8. The `verdictbox`.

Target length: four to ten typeset pages per technical chapter, more for formation.
A reader should be able to read the companion chapter first and then find the
technical chapter's main results without getting lost.

## 4. Style

American English. Academic prose in flowing paragraphs; tables for scorecards,
decoders, and comparisons. No bullet lists in running text. No horizontal rules, no
LaTeX spacing macros (`\;`, `\,`, `\!`), and none of these words or phrases: "key
insight", "crucially", "critically", "notably", "importantly", "it's worth noting",
"fundamentally", "leverages", "underscores". No praise of the theory and no
salesmanship; no hedged agreement when a verdict is negative. Punctuate displays as
sentences. Refer to companion chapters and sections with `\cref` to companion labels
(prefix `comp:`), never to hard-coded numbers. External literature is cited with
`\citet`/`\citep` using keys that already exist in `../MultiAgentELBO_Theory/references.bib`;
never add or invent a key. No repository paths, dates, run records, or software names
in the typeset text.

## 5. Files and build

`companion.tex` holds the preamble, the macros, and the chapter order. Front matter:
`f00_reading_guide.tex`, `f01_at_a_glance.tex`. Main manuscript, mirroring its chapter
numbers 1 to 15: `m01_program.tex`, `m02_04_foundations.tex`, `m05_06_elbo_attention.tex`,
`m07_08_geometry_timescales.tex`, `m09_10_channels_network_state.tex`,
`m11_12_coarsegraining_multiscale.tex`, `m13_formation.tex`,
`m14_15_interpretation_related.tex`. Supplements: `s_g1_gaussian_foundations.tex`,
`s_g2_gaussian_coarse.tex`, `s_b_base.tex`. Back matter: `z01_glossary.tex`,
`z02_open_ends.tex`. Chapter files contain no preamble and add no packages.
`technical-document-issues.md` lists errors, overstatements, and drift the drafters noticed in the
technical documents; it is a note for the theory's maintainer and is not typeset.

Build with `.\build.ps1` (PowerShell). It copies the technical sources to a scratch
directory, builds `main.tex` and both supplements there, builds the companion against
their `.aux` files, and copies `companion.pdf` back; `-SkipTheory` reuses the last
technical build. Nothing is built inside this folder or the theory folder. The build
fails, listing the labels, when a cited technical label no longer exists: that is how
the companion detects drift after the technical documents change. `companion.pdf` is
the only tracked build product; its links open the technical PDFs in
`../MultiAgentELBO_Theory/` at the cited statement.

## 6. Verification record (first edition, September 2026)

All chapters were drafted by Claude Opus 5.5. Claude Fable 5.1 checked, against the technical
statements, `f00_reading_guide.tex`, `m01_program.tex`, `m05_06_elbo_attention.tex`,
`m09_10_channels_network_state.tex`, `s_b_base.tex`, and `z02_open_ends.tex`; its findings (3 major,
about 30 minor) were applied, and none changed a verdict. At the author's request the remaining
checks were skipped to save cost: `m02_04_foundations.tex`, `m07_08_geometry_timescales.tex`,
`m11_12_coarsegraining_multiscale.tex`, `m13_formation.tex`, `m14_15_interpretation_related.tex`,
`s_g1_gaussian_foundations.tex`, `s_g2_gaussian_coarse.tex`, `f01_at_a_glance.tex`, and
`z01_glossary.tex` have no second-model check. Their drafters verified labels and recomputed
numerical witnesses, and the claim in `m13_formation.tex` that attention and learning play no role in
the coherence conclusion of the formation theorem was checked against `rem:rg-formation-saturation`.
The at-a-glance chapter states this for the reader.

## 7. Maintenance

When a technical chapter changes, rebuild, fix any undefined label, and revise the
matching companion chapter's scorecard, verdict, and explanations against the new
statements. A status or verdict that changes is a substantive edit: check it against
the statement, not against this companion's earlier wording. Verification of companion
chapters (fidelity of every status and verdict to the technical statements) is done by
a model different from the one that wrote the chapter, and the record names both.
