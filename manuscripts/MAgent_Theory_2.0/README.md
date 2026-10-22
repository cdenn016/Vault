# MAgent Theory 2.0

The main entry point is `MAgent_Theory_2.0.tex`. Its chapters and appendices contain the core constructions and proofs. `MAgent_Theory_2.0_supplement.tex` builds the separate supporting document. `MAgent_Theory_2.0_companion.tex` builds the self-contained physicist's companion; its explanatory chapters and editable TikZ figures are under `companion/`. All use the local style, preamble, and bibliography, with no external manuscript inputs.

From this directory, compile sequentially with TeX Live:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build MAgent_Theory_2.0.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build MAgent_Theory_2.0_supplement.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build MAgent_Theory_2.0_companion.tex
Copy-Item -LiteralPath build/MAgent_Theory_2.0.pdf -Destination MAgent_Theory_2.0.pdf
Copy-Item -LiteralPath build/MAgent_Theory_2.0_supplement.pdf -Destination MAgent_Theory_2.0_supplement.pdf
Copy-Item -LiteralPath build/MAgent_Theory_2.0_companion.pdf -Destination MAgent_Theory_2.0_companion.pdf
```

The scientific scope and conventions for future edits are recorded in `AUTHORING.md`. The main text and companion include the nonsmooth square-root-KL fusion example and two constructions within the original smooth potential. Conditional log-density spectra give an exact general-law state completion under specified reconstruction channels, including marked feedback. A smooth state-controlled erasure example gives changing source preferences, persistent heterogeneous pairs, and exact inherited public dynamics on a finite product family. That example discards private and gate laws while retaining all public child states. It supplies its erasing architecture and does not establish further public aggregation or recursive smooth formation. The earlier finite-state hierarchy remains a separate example of supplied retentions. The current research record is `../../docs/research/2026-10-21-smooth-kl-formation.md`.
