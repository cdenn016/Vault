# Panel brief: deep peer review of PIFB2.tex (2026-09-24)

You are one expert investigator on a referee panel. Read this brief in full before starting. Your lens-specific instructions arrive in your prompt; this brief carries what every lens shares.

## Target (read-only)

- Manuscript: `C:\Users\chris and christine\Desktop\Research\manuscripts\PIFB2.tex` (Git Bash: `/c/Users/chris and christine/Desktop/Research/manuscripts/PIFB2.tex`). 3956 lines, 79,455 words, SHA-256 `f80e6dab…080ec4`. Title: "A Gauge-Theoretic Framework Toward a Participatory 'It From Bit' Program: Mathematical Foundations and Computational Implementation", R. C. Dennis. Byte-identical to `MultiAgentELBO/Theory/PIFB2.tex` and to the bytes reviewed on 2026-09-13, so every ledger entry bound to PIFB2 below still applies.
- Bibliography: `C:\Users\chris and christine\Desktop\Research\manuscripts\references.bib`. One figure: `figures/pifb2_scaling.pdf`.
- Long lines: 37 source lines exceed 2000 characters (maximum 3553). The Read tool may truncate them. If a line looks cut off, print it whole with Bash, e.g. `sed -n '1575p' "<file>" | fold -w 1500`.
- Do not modify PIFB2.tex, references.bib, any Theory file, or any wiki page. You may write only your own panel file and scripts under this review directory, and scratch files under the session scratchpad.

## Line map of PIFB2.tex

Abstract 58-72. Introduction 73-93 (ontology commitments O1-O4). Epistemic status, levels 1-3, fence register 94-127. Related work 128-135. One rung: base manifold, statistical manifolds, principal and associated bundles, agents as sections, frames, transport, connection, curvature, Regime I and II, discrete Wilson holonomy, transport hierarchy, four curvatures, working simplifications including the KL invariance theorem 136-515. Single-scale free energy, mixture-of-sources attention, attention priors, base priors, pointwise and complete functional 516-734. State-dependent precision, envelope theorem, environmental agents, explicit symmetry breaking 735-928. Timescales and adiabatic structure, natural gradient 929-1005. Zero-dimensional limit and transformer recovery, RoPE, alpha rows 1006-1303. WikiText-103 dimension sweep 1304-1324. Precision as stiffness (mass) 1325-1532. Coarse-graining I, meta-agent barycenter, licensing, threshold detector 1533-1661. Coarse-graining II, cross-scale shadows 1662-1678. Coarse-graining III, RG status 1679-1702. Coarse-graining IV, Ouroboros tower and apex 1703-1731. Prospective validation 1732-1750. Discussion 1751-1801. Conclusion to Part I 1802-1809. Part II: Level-3 preamble and postulate register 1810-1827; time as information flow and meta-agent clock 1828-1866; it from bit, pullback construction, three tiers, Gaussian example 1867-1893; Lorentzian signature problem, postulates, GL(2,C) worked example, causal route, temporal direction 1894-2014; collective geometry, consensus metric, observable sectors, observer-dependent reality, physical quantities program 2015-2069; gravity, macroscopic objects, measurement 2070-2085; consciousness 2086-2106; gauge invariance as consensus and philosophy of science 2107-2132; open problems 2133-2151; conclusion 2152-2159; methods and statements 2160-2211. Appendices: A gradients 2212-2515; B rock example 2516-2591; C mathematical details 2592-2661; D covariance dynamics 2662-2891; E quadratic forms and transported KL 2892-2955; F conditional representation theorem for forward KL 2956-3161; G augmented hierarchical model and mean-field fixed point 3162-3412; H beyond mean field, effective action 3413-3568; I RG construction and theorem-level statements 3569-3941; notation 3942-3953.

## What the author wants from this review

1. PIFB2 must stand on its own as a realization of John Archibald Wheeler's participatory "it from bit" view of the universe. Judge every section by whether it serves that thesis, and whether a reader who never sees any other document can follow it.
2. PIFB2 is intended for a physics journal and a physics audience. Review as a referee at a physics venue would (foundations of physics, mathematical physics, statistical physics, or quantum foundations). Flag machine-learning or neuroscience jargon a physicist would not know, physics conventions that are violated or unusual (units and dimensions, index placement, metric signature, connection and curvature conventions, what "renormalization group", "gauge theory", "mass", "Lorentzian" mean to a physicist), and material that belongs in a different venue.
3. The Theory manuscript (`C:\Users\chris and christine\Desktop\MultiAgentELBO\Theory\`, main manuscript `main.tex` inputting `c01_program_scope.tex` to `c15_related_work.tex` and `ca_*.tex`; Supplement G `supplement_gaussian.tex` with `g00`-`g10`, `ga`, `gb`; Supplement B `supplement_base.tex` with `b00`-`b09`, `ba`-`bd`; git HEAD `5f643dc`, Theory tree clean) takes PIFB2's ideas much further mathematically. The two documents should supplement and reinforce each other. `Theory/SPEC.md` section 0 is an author rule that the Theory does not cite or import PIFB2; PIFB2 may cite the Theory. Recommendations about the pairing should therefore be PIFB2-side unless a Theory change is unavoidable, in which case label it an author decision.

## Settled record: do not re-raise (from `MultiAgentELBO/docs/reviews/verified-ledger.md`)

These bind to the exact PIFB2 bytes above. Do not re-derive or re-flag them. If your lens touches one, cite it as "registered (ledger)" in one line and move on.

- Registered open defects, adjudicated 2026-08-13 and 2026-09-13, not yet repaired: (a) the observation-term typing in `eq:pointwise_free_energy` (line 669) and `eq:free_energy_functional_final` (line 689), with m_i unbound and the two displays disagreeing; the ELBO-forced joint typing and the joint-minus-predictive Jensen gap were verified. (b) The sentence at 3633-3639 claiming a proper reference can have a non-sigma-finite pushforward; a proper reference always has a sigma-finite pushforward with density E_nu[g | R=y]. (c) The square-root conversion at 1861 in `prop:meta_clock_slowdown`: the ratio of expected KL increments gives an RMS arc-length ratio, not an expected arc-length ratio (fair-sign witness: expected ratio 1/2, RMS ratio 1/sqrt 2).
- Verified identities: the reduced attention Hessian `eq:rg_reduced_hessian` (line 3678), D^2 A = mean(D^2 E) - tau^{-1} Cov_b(dE, dE), is a Schur complement and correct. The belief-configuration Gibbs lift (`thm:belief_configuration_gibbs_lift`, 3578) builds a law over configurations and does not turn the live-peer consensus functional into the original-state ELBO excluded by `thm:state_level_elbo_nogo` (3282). Same-time PIFB2 coupling is not the dt -> 0 limit of the lagged ELBO-exact scheme (directed three-cycle counterexample; under edge symmetry they may agree up to halved coupling). On gl(K,R) the Ad-invariant symmetric bilinear forms are span{tr(XY), tr X tr Y}; no positive-definite invariant form exists; the correct no-go is positive-definiteness, not indefiniteness of every element. A Fisher-dressed curvature form of type |F phi|^2 is matter-coupled and does not contradict the pure-gauge no-go (not a defect). Transported-law coherence holds exactly when network holonomy lies in the stabilizer of the root law, not only at identity holonomy (triangle witness with Omega_12 = -I). KL expansion coefficients along a section: (1/2) g^F h^2 + (1/3) T_skew h^3 and the symmetric-stencil cancellation. The label-marginalization residual identities and the attention admission and logit-perturbation bounds of 2026-09-13.
- Framing decisions: the Theory supersedes PIFB2's single-point constructions (five-term functional becomes a normalized interaction-record joint with source-label attention; barycenter and detector become normalized marked parents; same-time shadows are forbidden by the Theory's typing prohibition; the Ouroboros self-closing apex is replaced by a declared root; Regime I becomes a specialization of independent links). Which framing the pair adopts (standalone plus external crosswalk, a bounded program-context section, or a rigorous core plus a separate program paper) is an open author decision; this review should inform it, not presume it.

## Prior reviews to consult before writing (avoid duplication)

- `MultiAgentELBO/docs/reviews/2026-09-23-theory-streamlining-review/findings/C1-pifb2-program-alignment.md`, sections (a) and (b): a node-by-node table N0-N22 of PIFB2's program with tags and the Theory's treatment (Theory file names there are the pre-2026-09-24 names; re-map by `\label` to the current `c*`, `g*`, `b*` files with grep).
- `MultiAgentELBO/docs/reviews/2026-09-13-program-review-next-phase/pifb-geometry-review.md`.
- Research wiki pages (read-only context): `Research/wiki/concepts/Participatory realism (it from bit).md`, `Participatory realism and quantum foundations.md`, `Ouroboros multi-scale dynamics.md`, `Meta-agents and hierarchical emergence.md`, `Holonomy.md`; source notes under `Research/sources/papers/` (for example `wheeler-1990-it-from-bit.md`, `fuchs-2017-participatory-realism.md`). The wiki's manuscript note describes an older version of this paper; trust PIFB2.tex over it.

A finding that repeats one of these should cite it and add only what is new.

## Standing rules for every lens

- Recompute, do not trust. Re-derive load-bearing identities with SymPy or float64 NumPy (use bare `python`; SymPy 1.14, NumPy, SciPy are installed; no torch or GPU is needed). Keep scripts tiny and fast (seconds, small dimensions); many agents share one CPU. Save every script you rely on as `C:\Users\chris and christine\Desktop\Research\manuscripts\reviews\2026-09-24-pifb2\scripts\<LENSID>_<name>.py` and report its output and residuals.
- Verify every citation you rely on against the primary source (web access is available), not against the manuscript's paraphrase.
- Classify each load-bearing claim you touch: P proven (here or by a cited result that entails it), D derived here under stated assumptions, S suggested or structural analogy, E empirical, C conjectured or open. Flag status inflation (proves, establishes, reveals, demonstrates, shows, realizes, resolves, explains attached to S or D content).
- Scope gate (repository rule): review PIFB2's existing base-manifold content (connections, pullback metrics, signature) for correctness and status as written, but do not develop new base-transport theory. If a fix would require new base-transport constructions, say so and name it as deferred work (Theory Supplement B), rather than constructing it.
- No Lean. No adjudication or verifier panel; you are an investigator. Report what you actually executed; "not checked" is a valid outcome.
- House style for your report: American spelling; no horizontal rules; do not use the words "key insight", "crucially", "critically", "notably", "importantly", "it's worth noting", "fundamentally", "leverages", "underscores"; no LaTeX spacing macros in any suggested manuscript text.

## Output contract

Write your full report to `C:\Users\chris and christine\Desktop\Research\manuscripts\reviews\2026-09-24-pifb2\panel\<LENSID>-<name>.md` (use the Write tool if you have it; otherwise Bash with a quoted heredoc: `cat > "/c/Users/chris and christine/Desktop/Research/manuscripts/reviews/2026-09-24-pifb2/panel/<file>.md" <<'EOF_REPORT'` ... `EOF_REPORT`). Keep it under about 6,000 words; rank by impact. Structure:

1. Header: lens, your model, exact line ranges you actually read, what you executed.
2. Findings, one block each, ranked most severe first:
   ### <LENSID>-<n>: <Title>
   **Location:** PIFB2.tex:<line> and equation or theorem label
   **Severity:** critical | high | medium | low (critical = a central claim is false or unsupported in a way that breaks the paper's thesis)
   **Evidence:** recomputation output, primary-source quotation (under 15 words) with page, or exact source text; not "the text says so"
   **Fix:** the specific correction, with replacement wording where useful
   **Falsifies:** what would show this finding is wrong
   **Status:** the claim's status (P/D/S/E/C) and whether the prose inflates it
3. Verified, no defect: identities or claims you recomputed and found correct, each with method, residual, and script name (these become ledger candidates).
4. Physics-audience and standalone notes for your scope (what a physics referee will stumble on; what should be condensed, moved, or replaced by a citation).
5. Complementarity notes: where your scope should cite a Theory result, or conflicts with one (give the Theory file and `\label`).
6. Not covered: parts of your scope you did not reach.

Then return the structured summary requested by your prompt.
