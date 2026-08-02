# Lens: notation / cross-reference / citation integrity

Manuscript: `manuscripts/gauge_vfe_rg/` (24 `.tex` files: `main.tex`, 20 chapter files, 3 appendices)
Bibliography: `manuscripts/references.bib` (referenced as `../references`)
Date: 2026-08-02. Interpreter: `C:/Python314/python.exe`. Engine: pdfTeX 3.141592653-2.6-1.40.27 (TeX Live 2025).

Every finding below is backed by a command that was actually run; the reported output is quoted verbatim.
Build was performed on an **isolated copy** in the scratchpad so the author's working tree was not touched.

Scripts used (all in the session scratchpad):
`xref_cite2.py`, `citediff.py`, `symbols.py`, `collide.py`, `status.py`, `status2.py`, `status3.py`, `misc.py`.

---

## Headline counts

| Check | Result |
|---|---|
| `\label{}` keys (distinct) | **952** real + 1 macro-internal `#4` = 953 scanned |
| Duplicate labels | **0** |
| `\ref`/`\eqref`/`\Cref` keys (distinct / occurrences) | **405 / 769** |
| Dangling references | **0** |
| Labels never referenced | 548 (informational, almost all `eq:`) |
| Bib entries in `references.bib` | **460** |
| Duplicate bib keys (exact) | **0** |
| Case-colliding bib keys | **0** |
| Cite keys (distinct) | **74** |
| Cited-but-missing from bib | **0** |
| Bib entries never cited | **386** |
| Build | **succeeds**, exit 0, **215 pages** |
| Undefined refs / citations / control sequences | **0 / 0 / 0** |
| Multiply-defined labels | **0** |
| Overfull / underfull boxes | **0 / 0** |
| `\status{}` registers in source | **604** |
| `\status{}` registers rendered in PDF | **604** (0 clipped, 0 missing) |
| Banned house-style words | **0** |
| UK spellings | **0** |
| `\;` / `\!` / `\,` in math | **0 / 0 / 1** (the one `\,` is legitimate) |
| Distinct font/custom math symbols in chapters | **81** |
| Distinct symbols in `appendix_notation.tex` | **17** |
| Chapter symbols absent from the notation appendix | **64** |

---

## 1. Symbol definition audit

### Method

`symbols.py` scanned the 20 chapter files, normalizing every `\mathcal{X}` / `\mathcal X`,
`\mathbb`, `\mathfrak`, `\mathsf`, `\mathscr`, `\mathbf`, `\mathrm`, `\boldsymbol`, `\mathit`
occurrence plus every custom macro declared in `main.tex:25-35`, recording file, line, and the
immediately-following sub/superscript. The same scan was run over `appendix_notation.tex`.
`collide.py` then probed each candidate collision with a meaning-specific regex.

```
### CHAPTER FILES SCANNED: 20
### DISTINCT FONT/CUSTOM SYMBOLS IN CHAPTERS: 81
### DISTINCT IN NOTATION APPENDIX: 17
=== (a) SYMBOLS USED IN CHAPTERS BUT ABSENT FROM appendix_notation.tex ===
count: 64
```

Note that the TeX level is clean: the build reports **0 "Undefined control sequence"**, so every
macro *resolves*. Everything below is a **semantic** defect — a symbol that typesets fine but whose
meaning is undeclared or double-booked.

---

### FINDING N-1 — `\mathcal L^{\rm ext}` is an undefined load-bearing symbol — **CONFIRMED**

**Claim.** The "extended ELBO" `\mathcal L^{\rm ext}` is used inside the displayed equation of a
theorem tagged `\status{ESTABLISHED}` and is defined nowhere in the manuscript.

**Location.** `06_general_coarsegraining.tex:209` and `:213` (inside `eq:cg-elbo-monotone`,
within `thm:cg-evidence-preserving-channel`).

**Severity.** high

**Evidence.**

```
$ Grep  pattern="\\rm ext|\\mathrm\{ext\}|ext\}"  glob=*.tex
06_general_coarsegraining.tex:209:\bar{\mathcal L}^{\rm ext}(\bar Q_o;o)
06_general_coarsegraining.tex:213:=\mathcal L^{\rm ext}(Q_o;o).
```

Exactly two occurrences in the whole manuscript. The word "extended" appears in the neighborhood
exactly once:

```
$ grep -rn "extended ELBO|extended evidence|extended bound|extended free" *.tex
06_general_coarsegraining.tex:207:\(Q_o\ll P_o\) implies \(\bar Q_o\ll\bar P_o\), and the extended ELBOs satisfy
```

`collide.py` confirms it is a fourth, distinct meaning of `\mathcal L`:

```
### \mathcal L
   ELBO (main.tex macro; 01,05,07_restrictions)          n= 37
   Lie derivative (05c:324,326)                          n=  2
   Laplace transform of matrix-Gamma (10:428)            n=  1
   UNDEFINED "extended ELBO" (06_gcg:209,213)            n=  2
```

**Adjudication of the carried-over candidate.** The prior session's item 1 is **correct**. There is
no definition under another glyph. The base symbol is `\Lelbo := \mathcal L` (`main.tex:35`), whose
ELBO meaning is fixed at `05_elbo.tex:123-131`; nothing in `05_elbo.tex` or `03_probability.tex`
introduces an `ext`-decorated variant, and the superscript is never explained. The displayed
equation does supply both *values*
(`\mathcal L^{\rm ext}(Q_o;o) = \log p(o) - \KL(Q_o\Vert P_o)`), so the inequality is arithmetically
self-contained; but the reader is given no way to know what "extended" contributes, nor how
`\mathcal L^{\rm ext}` relates to the `\Lelbo` of Chapter 5 — which is the same glyph `\mathcal L`.
This is an undefined symbol, not merely a missing cross-reference.

**Fix.** Either (a) add a one-line definition immediately before `eq:cg-elbo-monotone` stating what
the `ext` decoration means and how it differs from `\Lelbo`, and add a row to
`appendix_notation.tex`; or (b) if the object *is* the Chapter-5 ELBO evaluated on the
observation-conditioned pair, drop the superscript entirely and write `\Lelbo(Q_o;o)` via the macro,
matching `07_restrictions.tex:302-305` which already writes exactly that shape without any
superscript.

---

### FINDING N-2 — `R_b`/`R_m` vs `\mathcal R_b`: collision **REFUTED**; a different, real defect in its place

**Claim tested.** Does `R_b`/`R_m` (`02_geometry.tex:361-365`, "the represented coordinate changes")
collide with `\mathcal R_b` (`07b_agent_network_rg.tex`, block-`b` renormalization operator)?

**Answer: REFUTED as stated.** They are different glyphs (roman `R` vs calligraphic `\mathcal R`),
and the subscripts mean different things. `collide.py` output:

```
### \mathcal R
   block-b renormalization operator (07b)   n= 12 files=['07b_agent_network_rg']
      first: [(07b,614),(07b,619),(07b,623),(07b,628)]
```

and the `b` in `\mathcal R_b` is a **block scale factor**, not the belief channel —
`07b_agent_network_rg.tex:623` reads `$\mathcal R_{b_1b_2}=\mathcal R_{b_2}\mathcal R_{b_1}$` and
`:638` divides by `$\log b$`. So the prior session's assertion that "Chapter 7b uses the opposite
convention **for `R_b`**" was indeed a **symbol confusion**, exactly as the settled-ground note
suspected.

Roman `R_b`/`R_m` occurs at only three lines in the entire manuscript
(`02_geometry.tex:361,363,365`); the apparent 07b hits in the raw regex were substring matches
inside `\mathcal R_b`.

**However**, checking the surface claim surfaced three genuine defects, below (N-3, N-4, N-5).

---

### FINDING N-3 — `R` is quadruple-booked, and the two "represented frame change" uses feed reciprocal group elements

**Claim.** Roman `R` denotes four different objects, and the two that are both called "the
represented frame/coordinate change" transform matrices in mirrored directions because they are
applied to reciprocal group elements — a fact stated in neither displayed equation.

**Location.** `02_geometry.tex:361-365` (`eq:geo-defect-gauge-laws`);
`02_geometry.tex:661-664` (`eq:geo-represented-frame-change`);
`07b_agent_network_rg.tex:312-317` (`eq:rg-linear-cross-scale-covariance`);
`11_obstructions.tex:201-209`; `appendix_notation.tex:175-178`.

**Severity.** high (notation), **not** a mathematical error

**Evidence.** `collide.py`:

```
### R (roman, subscripted)
   R_b / R_m  (02: represented coordinate changes)   02_geometry:361,363,365
   R_{x,f} / R_{x,c}  (07b: rep. of frame rechoice)  07b:312,313,315,317
   R_i  (11: observation noise covariance)           11_obstructions (+02:662,664; 04:286)
   R  (stochastic refinement kernel)                 appendix_notation:176; 07_general_renormalization:501
```

The four meanings, with source text:

1. `appendix_notation.tex:176` — `\(Q,R\)` = "coarse map and **stochastic refinement kernel**".
   This is the only `R` the notation contract declares.
2. `02_geometry.tex:361` — "If $R_b,R_m$ denote the represented coordinate changes, their matrices obey
   $(D\Phi)'=R_m(D\Phi)R_b^{-1}$". **Channel index is a subscript. No direction stated.**
3. `02_geometry.tex:661-664` — `$R_i^b=\rho_b(g_i)$, $R_i^m=\rho_m(g_i)$`. **Same concept, same
   chapter, 300 lines later, but the channel index is now a superscript and the agent index a
   subscript.**
4. `11_obstructions.tex:201` — `$R_i\succ0$`, an observation **noise covariance**, alongside
   `$\Theta_i\in\GL^{+}(K)$`.

**On the mirrored sandwich.** Both formulas are *correct*; the mirror is an artifact of which group
element is fed to the representation, and neither displayed equation says.

- `04_generative.tex:283-287` fixes the ch.2/ch.4 convention: section rechoice
  `$u_i^{x\prime}=u_i^x\cdot(g_{a,i}^x)^{-1}$`, "the represented matrix $R_{a,i}^x$ multiplies sample
  coordinates", acting as `$k_i'=R_i^bk_i$`. So `new = R·old` with `R = \rho(g)`.
  A map `M : E_b\to E_m` then obeys `M' = R_m M R_b^{-1}` — matching `eq:geo-defect-gauge-laws`. ✓
- `07b_agent_network_rg.tex:300-317` declares `$R_x:G\to\operatorname{GL}(V_x)$` and sets
  `$R_{x,f}=\bigoplus_iR_x(a_i^x)$` where `a_i^x` is the **section-rechoice** element of
  `eq:geo-local-reframing` (`02_geometry.tex:150`, `u_i^{b\prime}=u_i^b\cdot a_i`). By
  `02_geometry.tex:157` that rechoice sends coordinates to `$\widehat\rho_b(a_i)^{-1}\beta_b$`, i.e.
  `new = R^{-1}·old`. Hence `$\mathsf C_x'=R_{x,c}^{-1}\mathsf C_xR_{x,f}$` — mirrored, and also ✓.

So `R_{\text{ch.2}} = \rho(g)` and `R_{\text{ch.7b}} = \rho(a)` with `a = g^{-1}`. Internally
consistent; externally unverifiable by a reader, because `02_geometry.tex:361` introduces `R_b` with
no definition at all and the reconciling statement lives two chapters away.

**Fix.** (i) At `02_geometry.tex:361`, replace "the represented coordinate changes" with the explicit
definition already available at `:661` and cite `\eqref{eq:geo-represented-frame-change}`, using the
same index placement (`R_i^b`, not `R_b`). (ii) At `07b:312`, add one clause stating that `a_i^x` is
the rechoice element of `eq:geo-local-reframing`, so the inverse placement is visibly the same
convention. (iii) Add an `R` row to `appendix_notation.tex` distinguishing the refinement kernel from
the represented frame change, or rename one of them. (iv) Rename the ch.11 noise covariance
(`R_i \to \Sigma_i^{\mathrm{obs}}` or similar).

---

### FINDING N-4 — the `b` subscript is overloaded: belief channel vs. block scale factor

**Claim.** `appendix_notation.tex:5-6` states the contract "Superscripts \(b\) and \(m\) always
denote the belief and model channels", but `b` is used pervasively as a *subscript* for the belief
channel and, in Chapter 7b, as a *subscript* for the RG block scale factor.

**Location.** contract at `appendix_notation.tex:5`; belief-channel subscripts at
`02_geometry.tex:361` (`R_b`), `:684` (`P_b`), `\mathcal E_b`, `\mathcal B_b`, `\rho_b`, `\omega_b`,
`appendix_notation.tex:170` (`C_\ell^b`); block-scale subscripts at
`07b_agent_network_rg.tex:605-638` (`K_b`, `C_b`, `I_b`, `\mathcal R_b`, `\mathcal R_b^\rho`,
`\mathcal R_b^H`, `\mathfrak B_b^H`, `b_1`, `b_2`, `\log b`) and `07_restrictions.tex:27,60,69`
(`b\in\mathfrak B`, a coordinate block).

**Severity.** medium

**Evidence.** `07b_agent_network_rg.tex:605-638`:

```
kernel $K_b=C_bI_b$. ...
\mathcal R_b(\rho,m_o) =\bigl((\rho C_b)I_b,(m_oC_b)I_b\bigr) =(\rho K_b,m_oK_b).
$\mathcal R_{b_1b_2}=\mathcal R_{b_2}\mathcal R_{b_1}$
\mathfrak B_b^H[H;\rho] =\frac{\mathcal R_b^H[H;\rho]-H}{\log b}.
```

and `07_restrictions.tex:27`: `C_Q=\operatorname{blockdiag}_{b\in\mathfrak B}\left(C_b\right)`.

Three unrelated `b`-subscripted senses coexist: belief channel (Part I), coordinate block
(Ch. 7 restrictions), RG scale factor (Ch. 7b).

**Fix.** Reserve `b` for the belief channel as the contract promises. Use `s` or `\lambda` for the RG
scale factor in 7b and `\beta` or an explicit `B` for coordinate blocks, then add a
"reserved indices" paragraph to `appendix_notation.tex`.

---

### FINDING N-5 — `P_b` means both the belief principal bundle and an SPD precision matrix

**Claim.** `P_b` is declared in the notation contract as a principal bundle and is reused in
Chapter 11 for a precision matrix.

**Location.** `appendix_notation.tex:179-183`; `02_geometry.tex:684,688`;
`11_obstructions.tex:209,212,247,257,259,262,268,271,282,284,286,288,296,302,303,307`.

**Severity.** high

**Evidence.** `collide.py`:

```
### P (roman, subscripted b)
   P_b = belief principal bundle (02:684)     n= 2 files=['02_geometry']
   P_b = apex precision matrix (11)           n= 9 files=['11_obstructions']
```

Source text:

```
02_geometry.tex:684:\pi_b:P_b\to\mathcal C,
02_geometry.tex:688:Q=P_b\times_{\mathcal C}P_m,
appendix_notation.tex:179: \(P_b,P_m;\ G_b\times G_m\) & optional product-gauge extension

11_obstructions.tex:209:P_b=P_0+\sum_{i=1}^{n}\Theta_i^{\top}R_i^{-1}\Theta_i ,
11_obstructions.tex:288:\rho=\lambda_{\max}\left(P_b^{-1/2}BP_b^{-1/2}\right)<1 .
```

One is a fiber bundle over `\mathcal C`; the other is a `K\times K` SPD matrix being inverted and
square-rooted. The clash is aggravated because Chapter 11 is *about* the bundle theory's
obstructions, so both readings are live in the reader's mind, and because the same passage also
reuses `R_i` (finding N-3) and `\Theta_i` (finding N-6).

**Fix.** Rename the Chapter 11 precision to `J_b` (the manuscript already uses `J` for precisions
throughout Chapter 6 and `J_\star` two lines earlier at `11_obstructions.tex:201`), or subscript it
with the apex node label rather than `b`.

---

### FINDING N-6 — `\Theta` carries six distinct meanings

**Claim.** `\Theta` denotes six different objects across the manuscript, one of which is
appendix-declared.

**Location / Severity.** high

**Evidence.** `collide.py`:

```
### \Theta
   Theta_e^x = edge-copy group element (02, appendix)   n=26  02,07b,09,11,ledger,notation
   Theta_ij = represented graph link (06_gaussian:138)  n= 3  06_gaussian:138,142,181
   Theta = Gaussian natural parameter (06_gaussian:38)  n= 2  06_gaussian:38,47
   Theta_i = observation loading matrix (11)            n= 6  11:201,209,212,215
   Theta = matrix-Gamma / Laplace argument (10)         n= 2  10:425,428
   Theta = parameter set (06_gcg:55)                    n= 6  06_gcg:55,57,127,139
```

Verbatim:

- `02_geometry.tex:532` — `\Theta_e^b,\Theta_e^m\in G` (group elements; the appendix row at
  `appendix_notation.tex:131-138` governs these).
- `06_gaussian.tex:38` — "the natural parameter pair $(h,\Theta)$ with $\Theta=-\tfrac12J$" (a
  negative-definite matrix).
- `06_gaussian.tex:138` — `\Theta_{ij}:=\rho_b(\Theta_{ij}^b)\in\GL^+(K)` (a represented link).
- `06_general_coarsegraining.tex:55` — `\mathcal E=(\mathsf X,\{P_\theta\}_{\theta\in\Theta})` (a
  parameter **set**).
- `10_renormalization.tex:425` — "For \(\Theta\succeq0\), the corresponding matrix-Gamma law".
- `11_obstructions.tex:201` — `$\Theta_i\in\GL^{+}(K)$` (observation loading matrices).

The worst pair is `06_gaussian.tex:38` (`\Theta` = natural parameter, defined `-J/2`) against
`06_general_coarsegraining.tex:55` (`\Theta` = parameter index set) — adjacent chapters — and against
`06_gaussian.tex:138` (`\Theta_{ij}` = graph link) **inside the same file**.

**Fix.** Keep `\Theta_e^x`/`\Theta_{ij}^x` for graph links (appendix-declared). Rename the Gaussian
natural parameter to `\Lambda` or keep `-J/2` inline; rename the parameter set to `\mathsf T` or
`\Xi`; rename the ch.11 loading matrices to `A_i` or `H_i`; and add a `\Theta` disambiguation row to
the notation appendix.

---

### FINDING N-7 — `\mathcal R` carries six distinct meanings, none declared in the notation appendix

**Location / Severity.** high

**Evidence.** `collide.py`:

```
### \mathcal R
   root set of a DAG (04,05)                    04_generative:22 ; 05_elbo:302,348
   descent ray (05d:287)                        05d:287
   smooth coarse map Q_f -> Q_m (05d:719)       05d:719,720,724,727,728,734,735,745,746
   level-l Markov coarse map (05d:769)          05d:769,780,783
   block-b renormalization operator (07b)       07b:614,619,623,628,638,715,721,723,730,761,764,771
   hatted RG map \widehat{\mathcal R}_\ell (07) 07:46,345,347,349,354,383,386,387
```

Verbatim:

- `04_generative.tex:22` — `$\mathcal R=\{r:\operatorname{pa}(r)=\varnothing\}$` (a vertex subset).
- `05_elbo.tex:302` — "let \(\mathcal R\subseteq V\) be the root set".
- `05d_relational_inference.tex:287` — `\mathcal R^-_{\Fenergy_i}(Q)=\{-a\operatorname{grad}^F\Fenergy_i(Q):a>0\}` (a ray).
- `05d_relational_inference.tex:719` — "$\mathcal R:\mathcal Q_f\to\mathcal Q_m$ be a smooth coarse map".
- `07b_agent_network_rg.tex:614` — `\mathcal R_b(\rho,m_o)` (RG operator on a measure pair).

Note that meanings 2, 3 and 4 all live in **one file**, `05d_relational_inference.tex`, 430 lines
apart. The `symbols.py` scan confirms `\mathcal R` is among the 64 chapter symbols with **no row in
`appendix_notation.tex`**.

**Fix.** Rename the DAG root set to `\mathsf{Rt}` or `V_0`; keep `\mathcal R` for the
coarse/renormalization map family (it is the dominant use and matches `\widehat{\mathcal R}`); and
add a `\mathcal R` row to the notation appendix distinguishing the coarse map, the level-indexed map,
and the block operator.

---

### FINDING N-8 — further multi-meaning symbols: `\mathcal A`, `\mathcal E`, `\mathcal C`, `\mathfrak B`, `\mathcal L`

**Severity.** medium

**Evidence.** `collide.py`:

```
### \mathcal A
   agent object          02_geometry:378   $\mathcal A^i=(\mathcal C_i;q_i,s_i,u_i^b,u_i^m)$
   set of interaction factors  05b:18,53,78,143,145
   Markov generator adjoint    07b:651,653,654,658,660,679,680   ($\mathcal A^*$)
   aggregation map             10:33,36,53,54,57,68              ($\mathcal A_S$)

### \mathcal E
   associated law bundles (appendix-declared)   \mathcal E_b,\mathcal E_m — 11 files
   statistical experiment   06_gcg:55   $\mathcal E=(\mathsf X,\{P_\theta\})$
   quadratic energy         09:35,530   $\mathcal E(z)=\tfrac12z^\top Lz$

### \mathcal C
   agent context patch      \mathcal C_i,\mathcal C_j — 02,03,05d,06a,12 (appendix-declared)
   congruence-diagonal cone \mathcal C_H — 06_gaussian:337; 09:127,134,136,160,171; 10

### \mathfrak B
   coordinate block partition   06_gaussian:54 ; 07_restrictions:21,23,27,32,60,69,91,98,103
   discrete beta functional     07b:637        $\mathfrak B_b^H[H;\rho]$
```

`\mathcal A^i` (agent, ch. 2) against `\mathcal A^*` (generator adjoint, ch. 7b) is the sharpest —
both are superscripted `\mathcal A`. `\mathcal C_H` is dangerous because `\mathcal C` with a subscript
is the appendix-declared context patch (`\mathcal C_i`), so `\mathcal C_H` reads as "the context patch
of agent H" rather than the matrix cone `\{HDH^\top: D\succeq0\text{ diagonal}\}` it actually denotes
(`06_gaussian.tex:337`). `\mathcal L` is covered in N-1 (4 meanings, incl. the Lie derivative
`\mathcal L_Z` at `05c_pullback_geometry.tex:324,326`).

**Fix.** Rename the ch. 9 energy to `E(z)` or `\mathsf E(z)`; rename the congruence cone to
`\mathsf{Cone}_H` or `\mathcal K_H`; rename the ch. 7b generator to `\mathsf L` or `\mathcal G`;
rename the ch. 7b beta functional to `\beta_b^H` (it is called a beta functional in prose anyway).

---

### FINDING N-9 — the notation appendix covers 17 of 81 chapter symbols; `\Lelbo` and `\Fenergy` are absent

**Claim.** `appendix_notation.tex` describes itself as "a type checker" but omits the manuscript's
central variational symbols.

**Severity.** medium

**Evidence.**

```
### DISTINCT FONT/CUSTOM SYMBOLS IN CHAPTERS: 81
### DISTINCT IN NOTATION APPENDIX: 17
=== (a) SYMBOLS USED IN CHAPTERS BUT ABSENT FROM appendix_notation.tex ===
count: 64
  \E        n=  89 chapters=12
  \GL       n=  23 chapters= 6
  \KL       n=  90 chapters=12
  \Lelbo    n=  49 chapters= 4
  \PSD      n=  15 chapters= 3
  \R        n=  87 chapters=15
  \Sym      n=  17 chapters= 5
  \Tr       n=  23 chapters= 4
  \mathcal R n= 48 chapters= 5
  \mathcal L n=  8 chapters= 5
  ... (54 more)
```

Several of these (`\R`, `\Tr`, `\E`, `\KL`, `\GL`, `\Sym`, `\PSD`) are standard and arguably need no
row. But `\Lelbo` (= `\mathcal L`, the ELBO, 49 uses) and plain `\Fenergy` are the manuscript's two
central objects, and the appendix declares only the *decorated* variant
`\(\overline{\Fenergy}_{B,o}\)` (`appendix_notation.tex:111`) — a derived quantity — without ever
declaring the base symbol. Combined with N-1 and N-8 this is why `\mathcal L` accumulated four
meanings unchecked.

**Fix.** Add rows for `\Lelbo`/`\mathcal L` and `\Fenergy`/`\mathcal F` at the head of the table, then
rows for `\mathcal R`, `\mathcal A`, `\Theta`, `R`, `P_b`, and `\mathcal C_H`.

---

### FINDING N-10 — `C_\ell^b, C_\ell^m` are declared in the appendix but never appear in that form

**Claim.** The notation contract declares a glyph the chapters do not use.

**Location.** `appendix_notation.tex:170-174` vs `07_general_renormalization.tex:219,222,273`.

**Severity.** low

**Evidence.** `misc.py`:

```
  C_ell^b     chapters=   0  appendix=1  <== IN APPENDIX ONLY (unused in chapters)
```

```
$ Grep pattern="C_\{?\\ell\}?\^|C\^\{?[bmx]\}?_\{?\\ell|c_\\ell"
appendix_notation.tex:170:\(c_\ell,C_\ell^b,C_\ell^m\) &
07_general_renormalization.tex:219:\Omega_{\ell+1,c_\ell\gamma}\circ C_{\ell,b,x}\right),\nonumber\\
07_general_renormalization.tex:222:\widetilde\Omega_{\ell+1,c_\ell\gamma}\circ C_{\ell,m,x}\right).
07_general_renormalization.tex:273:\mathscr G_{\ell+1,b,c_\ell(x)}\circ C_{\ell,b,x}\circ
```

The chapter writes `C_{\ell,b,x}` (three comma-separated subscripts, with a base point `x`); the
appendix writes `C_\ell^b`. `c_\ell` itself matches (`07:160`). This is the *only* appendix-declared
symbol absent from the chapters — the `(b) symbols defined but never used` count is otherwise
**0**.

**Fix.** Change `appendix_notation.tex:170` to `\(c_\ell,C_{\ell,b,x},C_{\ell,m,x}\)` and note that
the base point `x` is carried.

---

### FINDING N-11 — `\Lagg` is a dead macro

**Claim.** `\Lagg` is defined in the preamble and never used.

**Location.** `main.tex:33`.

**Severity.** low

**Evidence.** `misc.py`:

```
### \Lagg USAGE (defined main.tex:33) ###
  chapters: 0  all tex: 1
```

The single occurrence is the `\newcommand` itself. `main.tex:24` states "shared macros: chapters
must use these and must not redefine them", so an unused entry is contract noise.

**Fix.** Delete `\newcommand{\Lagg}{\Lambda_{\mathrm{c}}}` from `main.tex:33`.

---

### FINDING N-12 — `\mathcal L` and `\mathcal F` written raw instead of through the mandated macros

**Claim.** `main.tex:24` mandates the shared macros, but several chapters write the expansion
directly.

**Location.** `01_introduction.tex:41`; `06_general_coarsegraining.tex:209,213`;
`07_restrictions.tex:302,305`.

**Severity.** low

**Evidence.**

```
01_introduction.tex:41:=\mathcal L(Q_X;X)
06_general_coarsegraining.tex:209:\bar{\mathcal L}^{\rm ext}(\bar Q_o;o)
06_general_coarsegraining.tex:213:=\mathcal L^{\rm ext}(Q_o;o).
07_restrictions.tex:302:\bar{\mathcal L}(\bar Q;o)
07_restrictions.tex:305:=\mathcal L(Q;o).
```

against `main.tex:35` `\newcommand{\Lelbo}{\mathcal L}` and 49 correct `\Lelbo` uses elsewhere.
This is how the `\mathcal L^{\rm ext}` of N-1 escaped notice: it does not appear in a `\Lelbo` grep.

**Fix.** Replace with `\Lelbo` (and `\bar{\Lelbo}`) at all five sites.

---

## 2. Cross-reference integrity — **CLEAN**

**Method.** `xref_cite2.py` collected `\label{}` plus every macro-generated label (the
`\definitionheading`/`\lemmaheading`/… family defined at `main.tex:86-100` emits `\label{#4}` from
its second argument — a naive `\label` grep misses 203 of them and produces 104 false "dangling"
hits). Results were then cross-checked against the 952 `\newlabel` entries in the freshly compiled
`main.aux`.

```
FILES scanned: 24
REF macros: {'Cref': 276, 'ref': 44, 'eqref': 426}
CITE macros: {'citep': 79, 'citet': 12}

LABELS distinct (source scan): 953 | total occurrences: 953
  of which macro-generated (*heading): 203
LABELS in main.aux (\newlabel, non-@cref): 952
DUPLICATE LABELS (source): 0
DUPLICATE LABELS (aux \newlabel emitted twice): 0

REF keys distinct: 405 | total occurrences: 769
DANGLING REFS (source scan): 0
DANGLING REFS (vs main.aux): 0

LABELS in aux but not found by source scan: 0 []
LABELS in source but not in aux: 1 ['#4']
```

- **Dangling references: 0.** Every one of the 405 referenced keys resolves, confirmed twice
  (source scan and compiled `.aux`).
- **Duplicate labels: 0.** No key is defined twice, and no `\newlabel` is emitted twice.
- The single source-only "label" `#4` is the macro parameter inside the `\resultheading` definition
  at `main.tex:88`, not a real label. Real label count is **952**, matching `main.aux` exactly.
- **548 labels are never referenced.** These are overwhelmingly `eq:` labels attached to displayed
  equations (e.g. `eq:cg-aggregation-matrix`, `eq:cg-coarse-blocks`). This is normal practice for a
  reference monograph and is reported as informational only, not a defect.

---

## 3. Citation integrity — **CLEAN**

**Method.** `xref_cite2.py` + `citediff.py`, cross-checked against BibTeX's own accounting in
`main.blg`.

```
BIB distinct keys: 460 | total @entries: 460
EXACT DUPLICATE BIB KEYS: 0
CASE-COLLIDING BIB KEYS: 0

CITE keys distinct: 74 | total occurrences: 121
CITED BUT MISSING FROM BIB: 0
BIB ENTRIES NEVER CITED: 386
```

Ground truth from BibTeX (`main.blg`):

```
The top-level auxiliary file: main.aux
The style file: plainnat.bst
Database file #1: ../references.bib
You've used 74 entries,
...
warning$ -- 0
```

`warning$ -- 0` is decisive: BibTeX issued **zero** warnings, so there is no missing entry, no empty
required field it chose to complain about, and no repeated entry.

**A scanner caveat worth recording.** A single-line `\citep{}` regex finds only 71 distinct keys;
`citediff.py` located the gap:

```
aux distinct: 74
src distinct: 71
IN AUX NOT IN SRC SCAN: ['Ladyman2007', 'Ladyman2014', 'esfeld2008moderate']
IN SRC SCAN NOT IN AUX: []
--- locating Ladyman2007
     12_philosophy.tex 138 exists, is available but unsupported \citep{Ladyman2007,Ladyman2014,
--- locating esfeld2008moderate
     12_philosophy.tex 139 esfeld2008moderate}. \status{OPEN}
```

These three are one `\citep{...}` wrapped across `12_philosophy.tex:138-139`. Not a defect — a
line-wrapped citation is valid LaTeX — but any future automated citation check must be multi-line
aware or it will report three phantom problems.

**On the 386 uncited entries.** `references.bib` is the *shared* bibliography of the whole research
program (it contains the transformer, social-physics, participatory-realism, and consciousness
literatures — `Vaswani2017`, `Tononi2004`, `deffuant2000`, `Chalmers1995`, …). Carrying entries this
manuscript does not cite is expected and harmless: `plainnat` emits only the 74 cited entries into
`main.bbl`. Reported for completeness, **not** as a defect.

---

## 4. Build — **SUCCEEDS, 215 pages, fully clean**

**Method.** The manuscript tree was copied to the scratchpad together with `../references.bib` so the
author's working tree was untouched, then built with `build.ps1`'s exact command sequence
(`pdflatex` → `bibtex` → `pdflatex` → `pdflatex`, `TEXINPUTS=".;..;"`).

```
$ pdflatex -interaction=nonstopmode -file-line-error main.tex ; bibtex main ; pdflatex x2
pass1 exit=0
bibtex exit=0
pass2 exit=0
pass3 exit=0
-rw-r--r-- 1 ... 1365110 Aug  2 13:01 main.pdf
```

Log analysis:

```
=== PAGES / OUTPUT ===
Output written on main.pdf (215 pages, 1365110 bytes).
=== LaTeX Warning: Reference / Citation undefined === 0
=== Undefined control sequence === 0
=== Multiply defined === 0
=== Overfull hbox === 0
=== Overfull vbox === 0
=== Underfull hbox === 0
=== Underfull vbox === 0
=== '! ' errors === 0
=== ALL LaTeX Warnings (unique text) ===   (none)
```

- **215 pages** — matches the count recorded in settled-ground item **PB-4**.
- **Zero** undefined references, undefined citations, undefined control sequences, multiply-defined
  labels, overfull/underfull boxes, and errors. The log contains exactly one line matching
  "warning", and it is a package banner (`infwarerr ... Providing info/warning/error messages`), not
  a warning.

**Zero overfull boxes was verified, not assumed.** The repo's committed `main.log` is stale (dated
29 JUL, `Output written on main.pdf (249 pages, ...)`, 126 overfull boxes) and describes a different
document state, so the contrast demanded a check that overfull reporting is still functioning. A
sanity document using the same `scientific_report.sty` was compiled with deliberate overflow:

```
sanity Overfull count: 2
Overfull \hbox (788.7843pt too wide) detected at line 5
Overfull \hbox (198.43027pt too wide) in paragraph at lines 6--7
```

Detection works; the manuscript's 0 is real. Neither `main.tex` nor `scientific_report.sty` sets
`\hfuzz`, `\vfuzz`, `\hbadness`, `\tolerance`, `\emergencystretch`, or `\sloppy` (grep returned
nothing), so nothing is suppressing the check.

**Incidental positive.** The fresh build produced `main.pdf` at **1365110 bytes**, byte-identical in
size to the committed `manuscripts/gauge_vfe_rg/main.pdf` (1365110 bytes, dated Aug 1 20:12). The
committed PDF is therefore current with the committed sources. Only `main.log`, `main.aux`,
`main.toc`, `main.out`, `main.lot`, and `main.synctex.gz` are stale (29 JUL); consider refreshing or
gitignoring them so the 249-page log does not mislead a future reviewer.

---

## 5. Status-register rendering (ledger item R18) — **RESOLVED; 0 clipped, 0 missing**

**Claim.** R18 recorded five `\status{...}` registers clipped in the compiled PDF. In the current
build, **all 604 status registers render**; none is clipped or missing.

**Severity.** none (R18 obligation discharged for this revision)

**Method.** `status.py` counted `\status{...}` in source by tag; `pdftotext -layout` extracted the
freshly built PDF; `status2.py`/`status3.py` reconciled, accounting for hyphenation across line
breaks.

Source (`status.py`):

```
SOURCE \status tag totals:
  ESTABLISHED      345
  DEFINITION        97
  OPEN              57
  HYPOTHESIS        49
  NOT-CLAIMED       40
  NUMERICAL         11
  CONJECTURE         5
  TOTAL 604
```

Naive PDF extraction appears to be 10 short:

```
PDF rendered [TAG] totals:
  ESTABLISHED 340 | DEFINITION 95 | OPEN 57 | HYPOTHESIS 49
  NOT-CLAIMED 37  | NUMERICAL  11 | CONJECTURE 5
  TOTAL 594
DELTA: DEFINITION +2, ESTABLISHED +5, NOT-CLAIMED +3
```

All 10 are hyphenated across a line break — a text-extraction artifact, not clipping. `status3.py`
locates every one:

```
=== all line-final hyphenated fragments beginning with '[' ===
  line  470: tail='...declared rather than derived. [DEFINI-'  next='TION] Bi-additive Gaussian...'
  line 1374: tail='...Leibler [40] and Csiszar [20]. [DEFINI-'  next='TION]'
  line 2699: tail='...instance of the exact ELBO at . [ESTAB-'  next='LISHED] This does not rule...'
  line 3135: tail='...block of the collective VFE flow. [ESTAB-' next=''
  line 3506: tail='...Proposition 8.10, then hs,D = hs. [ESTAB-' next='LISHED]'
  line 5257: tail='...runs in the opposite direction. [NOT-'    next='CLAIMED] In the small-...'
  line 6820: tail='...recognition covariance is restricted. [ES-' next='TABLISHED]'
  line 7747: tail='...with this structural criterion. [NOT-'    next='CLAIMED]'
  line 9275: tail='...initial collection of means. [ESTAB-'     next='LISHED]'
  line 9611: tail='...supplies no unique such criterion. [NOT-' next='CLAIMED] Identifying...'

=== search for split variants of ESTABLISHED ===
  \[ES-: 1
  \[ESTAB-: 4
  bare '[ESTABLISHED]' : 340
```

Reconciliation, exact:

| tag | whole | hyphen-split | total | source |
|---|---|---|---|---|
| ESTABLISHED | 340 | 4 (`[ESTAB-`) + 1 (`[ES-`) | **345** | 345 |
| DEFINITION | 95 | 2 (`[DEFINI-`) | **97** | 97 |
| NOT-CLAIMED | 37 | 3 (`[NOT-`) | **40** | 40 |
| HYPOTHESIS | 49 | 0 | **49** | 49 |
| OPEN | 57 | 0 | **57** | 57 |
| NUMERICAL | 11 | 0 | **11** | 11 |
| CONJECTURE | 5 | 0 | **5** | 5 |
| **TOTAL** | 594 | 10 | **604** | **604** |

Exact agreement. Corroborated independently by the **0 overfull hboxes** in §4 (verified-working
detection): nothing in the document extends past the text block, so nothing can be clipped at the
right margin.

Per-file source distribution is recorded for reference; note `07b_agent_network_rg.tex` carries 36
registers all tagged `ESTABLISHED`, and `appendix_claim_ledger.tex` carries 22 (20 `OPEN`,
2 `CONJECTURE`), all of which render.

**One cosmetic residue.** Ten registers break across lines mid-word (`[ESTAB-` / `LISHED]`). They are
present and legible, but a bracketed status tag split across a line break reads poorly. Optional fix:
wrap the tag body in `\mbox{}` inside the `\status` definition at `main.tex:104`:
`\newcommand{\status}[1]{{\small\textsc{\textcolor{statusfg}{\mbox{[#1]}}}}}`. Verify afterwards that
this does not introduce overfull boxes.

---

## 6. House style — **CLEAN**

### Banned patterns: 0 occurrences

```
$ for w in "key insight" "crucially" "critically" "notably" "importantly" \
           "it's worth noting" "it is worth noting" "fundamentally" \
           "leverages" "leverage" "underscores" "underscore"; do
      grep -oin "$w" *.tex | wc -l ; done
--- 'key insight' : 0
--- 'crucially' : 0
--- 'critically' : 0
--- 'notably' : 0
--- 'importantly' : 0
--- "it's worth noting" : 0
--- 'it is worth noting' : 0
--- 'fundamentally' : 0
--- 'leverages' : 0
--- 'leverage' : 0
--- 'underscores' : 0
--- 'underscore' : 0
```

(Case-insensitive, so `Notably`/`Crucially` sentence-initial forms are covered.)

### Horizontal rules: 0 prose rules

```
$ grep -n '\\hrule|\\rule\{|\\hrulefill|^---|\\midrule|\\toprule|\\bottomrule|\\hline' *.tex
01_introduction.tex:152:\toprule
01_introduction.tex:154:\midrule
appendix_notation.tex:15:\toprule
appendix_notation.tex:17:\midrule
appendix_numerical_provenance.tex:8:\toprule
```

Every hit is a `booktabs` table rule inside a `tabular`/`longtable`. **Zero** `\hrule`,
`\hrulefill`, `\rule{`, or markdown `---` separators in prose.

### British/UK spellings: 0

```
$ grep -Ein "behaviour|colour|normalis|optimis|factoris|centre|modelling|fibre|analyse|
             organis|recognis|characteris|generalis|specialis|parameteris|discretis|
             linearis|summaris|utilis|labelled|modelled|travell|neighbour" *.tex
02_geometry.tex:501:different induced characteristic data.
(count:) 1
```

The single hit is `characteris` matching **"characteristic"** — correct American English, a false
positive of the probe. Actual UK spellings: **0**. (The probe was deliberately broadened well beyond
the requested list — `analyse`, `organis`, `generalis`, `labelled`, `neighbour`, etc. — and still
found nothing.)

### Spacing macros in math: effectively 0

```
### SPACING MACROS ###
  \;       total=    0
  \,       total=    1   top: [('05b_local_collective_elbo.tex', 1)]
  \!       total=    0
  \quad    total=   65
  \qquad   total=  284
  \:       total=    0
```

`\;` and `\!` do not occur at all. The single `\,` is:

```
05b_local_collective_elbo.tex:152:=\sum_{a:\,\partial a\cap B=\varnothing}
```

a thin space after the colon in a summation-index set-builder — standard, legitimate typesetting, not
prose-adjacent manual kerning. The 65 `\quad` / 284 `\qquad` are inter-equation separators in
`\begin{equation}` bodies (e.g. `02_geometry.tex:363-365`), which is the correct use.

**No house-style defects found.**

---

## Summary of findings

| # | Finding | Severity |
|---|---|---|
| N-1 | `\mathcal L^{\rm ext}` undefined (`06_general_coarsegraining.tex:209,213`) — **carried-over candidate CONFIRMED** | high |
| N-2 | `R_b` vs `\mathcal R_b` collision — **carried-over candidate REFUTED** (distinct glyphs; `b` = block scale in 7b) | — |
| N-3 | `R` quadruple-booked; ch.2 / ch.7b "represented frame change" feed reciprocal group elements, direction never stated | high |
| N-4 | `b` subscript overloaded: belief channel / coordinate block / RG scale factor | medium |
| N-5 | `P_b` = belief principal bundle (ch.2, appendix-declared) **and** SPD precision matrix (ch.11) | high |
| N-6 | `\Theta` carries six meanings, incl. two inside `06_gaussian.tex` | high |
| N-7 | `\mathcal R` carries six meanings, three of them inside `05d_relational_inference.tex`; no appendix row | high |
| N-8 | `\mathcal A` (4), `\mathcal E` (3), `\mathcal C_H` vs `\mathcal C_i`, `\mathfrak B` (2), `\mathcal L` (4) | medium |
| N-9 | Notation appendix covers 17 of 81 chapter symbols; `\Lelbo`/`\Fenergy` base symbols absent | medium |
| N-10 | `C_\ell^b,C_\ell^m` declared in appendix, written `C_{\ell,b,x}` in ch.7 | low |
| N-11 | `\Lagg` defined at `main.tex:33`, never used | low |
| N-12 | `\mathcal L` written raw at 5 sites instead of the mandated `\Lelbo` macro | low |

Cross-references, citations, the build, the status registers, and house style are **all clean**.
The entire defect surface of this lens is **symbol semantics**: 64 of 81 chapter symbols have no row
in the typed notation contract, and the six worst-overloaded glyphs (`R`, `P_b`, `\Theta`,
`\mathcal R`, `\mathcal A`, `\mathcal L`) carry 4-6 meanings each. Given that
`appendix_notation.tex:4` declares itself "a type checker, not a second development of the theory",
extending it to the symbols in N-3 through N-9 is the single highest-value repair.
