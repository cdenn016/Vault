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

The scientific scope and conventions for future edits are recorded in `AUTHORING.md`. The main text and companion now include a two-stage finite-time fusion example with an explicitly nonsmooth square-root-KL interaction, inherited lognormal laws, and exact fresh-response kernels. Formation under the original smooth KL potential, smaller autonomous parents with internally distinct parameters, and the derivation of directional transport remain open. The earlier finite-state hierarchy remains a separate example of supplied retentions.
