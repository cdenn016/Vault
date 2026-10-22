# MAgent Theory 2.0

The main entry point is `MAgent_Theory_2.0.tex`. Its chapters and appendices contain the core constructions and proofs. `MAgent_Theory_2.0_supplement.tex` builds the separate supporting document. `MAgent_Theory_2.0_companion.tex` builds the self-contained physicist's companion; its explanatory chapters and editable TikZ figures are under `companion/`. All use the local style, preamble, and bibliography, with no external manuscript inputs. Scientific scope and editing conventions are in `AUTHORING.md`.

From this directory, compile sequentially with TeX Live:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build MAgent_Theory_2.0.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build MAgent_Theory_2.0_supplement.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build MAgent_Theory_2.0_companion.tex
Copy-Item -LiteralPath build/MAgent_Theory_2.0.pdf -Destination MAgent_Theory_2.0.pdf
Copy-Item -LiteralPath build/MAgent_Theory_2.0_supplement.pdf -Destination MAgent_Theory_2.0_supplement.pdf
Copy-Item -LiteralPath build/MAgent_Theory_2.0_companion.pdf -Destination MAgent_Theory_2.0_companion.pdf
```

## Current state (2026-10-22)

The collective/local-parent main and companion chapters add the transmitted-angle model, genuinely collective physical rotation loss, exact local two-jet evolution with finite reference-state memory, actual normalized-law Fisher-cost inheritance, and a conditional finite preparation-and-history realization. The unrestricted local-parent question remains INCONCLUSIVE. The smooth finite-order and regular finite global-encoding obstructions have explicit scopes and do not prove general impossibility. Raw histories remain complete and unbounded; interaction-created invisibility, second-stage recursion and future_TODO extensions remain deferred.

The added per-agent chapter and companion derive the correct own-block and null fields, prove persistent interaction-dependent grouping with conflicting records, and give a conditional physical phase parent preserving port dynamics, admitted finite adaptive histories, persistent likelihoods, and actual nonflat collective geometry on a finite window. The phase-insensitive interface is predeclared; no new second compressive handoff is proved. Persistent grouping is restricted to the fixed initial record episode, and geometric equality is restricted to context-constant erased phases. These are conditional one-stage inheritance results, not a completed recursive formation.

A deep review on 2026-10-22 found no false main result but several structural problems, and the remediation applied the author's two decisions.

Agents hold beliefs and generative models. Chapter 1 defines the generative model of an agent (a reference over presentations, an evaluator as prior over contents, and a record likelihood), its variational free energy, and a shared generative model up to frame (a species). Chapter 3 keeps three objectives apart: a global free energy over all agents, whose local free energies give coordinate descent of one functional; per-agent free energies, in which each agent's own model and its peers' communicated laws are competing mixture sources; and the reciprocal law potential, whose flow also moves sources toward receivers. A proposition shows that the reciprocal potential is not the free energy of any fixed normalized model whose recognition laws are the agent laws. Relating the three objectives is an open problem, and both free-energy pictures are to be studied.

Chapter 5 states a formation standard with six clauses: admitted open class, state-determined selection, inheritance, compression, interaction necessity against a null flow with peer costs removed, and a second stage that depends on the first. A construction meeting selection and inheritance but failing compression or interaction necessity is a two-stage selection with exact inheritance. Measured against it, the Wishart construction (chapter 11) has a coupling-independent membership schedule, the six-agent open-law construction (chapter 12) does not establish interaction necessity in its proof regime, and the nonsmooth fusion construction (chapter 6) meets interaction necessity. A construction satisfying every clause is open. All constructions in chapters 6 to 12 concern the reciprocal potential.

Review and remediation records: `C:\Users\chris and christine\Desktop\VFE_4.0\docs\reviews\2026-10-22-magent-theory-2.0-review\` (`REPORT.md`, `lenses/`, `remediation/`). Earlier derivation and integration records are under `../../docs/derivations/` and `../../docs/research/`.
