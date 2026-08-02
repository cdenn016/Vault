# Adversarial re-adjudication of N-1, N-3, N-5, N-6, N-7

Target: `manuscripts/gauge_vfe_rg/`. Date: 2026-08-02.
Posture: skeptic. The mechanical grep counts in `lens-integrity.md` are accepted as given and are not
contested anywhere below. What is contested is (a) whether each count denotes a *defect*, and
(b) whether HIGH is the right register.

Every file:line below was read in full context, not grepped in isolation.

---

## 0. The governing question no finding asked: what does the notation contract actually promise?

Four of the five findings (N-3, N-5, N-6, N-7) presuppose that `appendix_notation.tex` establishes a
one-symbol-one-meaning discipline that the chapters then breach. Read the preamble:

```
appendix_notation.tex:4-8
This appendix is a type checker, not a second development of the theory.
Superscripts \(b\) and \(m\) always denote the belief and model channels.
They may have different representations, fiber dimensions, connections, and
coarse maps, but the ambient theory induces both channels from one principal
\(G\)-bundle.
```

That is the whole contract. It contains exactly one universally quantified promise — "**superscripts**
`b` and `m` always denote the belief and model channels" — and nothing about glyph uniqueness. The
table's third column is headed "Meaning and prohibited identification": the appendix's declared job
is to stop the reader from *identifying two typed objects that share a word or a glyph*, not to
guarantee that no glyph is reused.

The appendix says so four more times in its own closing paragraphs, each time about a shared *name*
rather than a shared symbol:

- `appendix_notation.tex:195-203` "Three uses of ``pullback.''  ... These are three different typed
  constructions; their shared word transfers no theorem."
- `appendix_notation.tex:224-229` "Two uses of ``coarse.'' ... no shared word changes their types or
  transfers a theorem from one to another."
- `appendix_notation.tex:187-193` "Three transports that must remain distinct."
- `appendix_notation.tex:205-212` "Four notions of order and path. ... None is identified with
  physical time."

The manuscript's declared discipline is therefore **deliberate controlled reuse with an explicit
non-identification clause**, and it applies that discipline in-line at every site the findings
flag (`06_gaussian.tex:137-140`, `11_obstructions.tex:6-16`, `07b_agent_network_rg.tex:301`). Also
relevant: `appendix_notation.tex` is `\Cref`'d from **zero** other files
(`grep -rn "app:notation-contract" *.tex` returns only its own `\label` at `:2`). It is a
back-of-book type table, not a normative front-matter contract the chapters are audited against.

Under a contract that promises nothing about glyph uniqueness, an unlisted reuse is a housekeeping
item. That alone caps N-3/N-5/N-6/N-7 well below HIGH before any per-finding evidence is examined.

---

## N-1 — `\mathcal L^{\rm ext}` is undefined

**Verdict: SURVIVES-AT-LOWER-SEVERITY (low).**

The finding's own text concedes the load-bearing point and then does not follow it:
"The displayed equation does supply both *values* ... so the inequality is arithmetically
self-contained" (`lens-integrity.md:110-111`). That is an admission that the theorem does not depend
on the symbol. Four independent lines of evidence confirm it and add that the concept is defined in
the manuscript, just not under an `ext`-decorated glyph.

**(i) The theorem's conclusion uses no property of `\mathcal L^{\rm ext}` beyond the displayed
equality.** The display is a four-term chain:

```
06_general_coarsegraining.tex:208-215
\bar{\mathcal L}^{\rm ext}(\bar Q_o;o)
=\log p(o)-\KL(Q_oK\Vert P_oK)
\geq
\log p(o)-\KL(Q_o\Vert P_o)
=\mathcal L^{\rm ext}(Q_o;o).
```

The mathematical content is the middle `\geq`, which is KL data processing. The two named symbols are
labels attached to the outer ends. The proof confirms this exactly:

```
06_general_coarsegraining.tex:218-222
Normalization of \(K\) preserves the observation marginal. Disintegration
commutes with the parameter-independent channel. Absolute continuity and
\eqref{eq:cg-elbo-monotone} follow from the preceding data-processing
theorem.
```

Delete both labels and the theorem is unchanged.

**(ii) `eq:cg-elbo-monotone` is never referenced outside its own chapter.** All four references are
local, and all four cite it for the data-processing content:

```
$ grep -rn "cg-elbo-monotone" *.tex
06_general_coarsegraining.tex:214  \label{...}
06_general_coarsegraining.tex:221  "...follow from the preceding data-processing theorem"
06_general_coarsegraining.tex:229  "The increase in ... reflects discarded information"
06_general_coarsegraining.tex:245  "...KL data processing, evidence preservation, and ... do not follow"
```

`thm:cg-evidence-preserving-channel` is referenced **zero** times (`grep -rn` returns only its own
`\theoremheading`). Nothing downstream inherits the symbol.

**(iii) The object is defined in Chapter 5 — under the name the finding searched for in prose but
not in math.** `05_elbo.tex:458` introduces exactly this quantity, distinguishes it from
`eq:elbo-definition`, and displays it:

```
05_elbo.tex:458-464
The separately integrated ELBO of \eqref{eq:elbo-definition} is undefined
because (H4) fails, while its canonical relative-log extension distinguishes them:
\E_q\left[\log\frac{p_0}{q}\right]=0, ...
```

and `05_elbo.tex:102` states why the extension is needed: "Relative entropy remains well defined in
\([0,\infty]\) without (H4). What fails without it is the split of the identity into two separately
finite expectations: the difference defining the ELBO can be an undefined \(\infty-\infty\)."

`\mathcal L^{\rm ext}(Q_o;o) := \log p(o)-\KL(Q_o\Vert P_o)` is precisely that: the relative-log
extension of `\Lelbo`, valued in `[-\infty,\log p(o)]`, agreeing with `\Lelbo` wherever (H4) holds
(by `eq:elbo-identity` at `05_elbo.tex:137-146`, `\log p = \Lelbo + \KL`).

**(iv) The manuscript declares a policy that makes the in-situ display the correct place for this.**

```
03_probability.tex:240
Where a later result tolerates an extended-real relative entropy, the relaxation
is stated at that point rather than absorbed into the notation here.
```

`06_general_coarsegraining.tex:207` ("the extended ELBOs satisfy") followed immediately by the
display *is* that statement at that point.

**The finding's own proposed fix (b) would introduce a defect.** It suggests dropping the superscript
and writing `\Lelbo(Q_o;o)`, "matching `07_restrictions.tex:302-305`". But `\Lelbo` is defined at
`05_elbo.tex:121-128` as `\E_{Q_X}[\log p_\theta - \log q_X]`, whose existence needs (H4)
(`\Cref{hyp:elbo-evidence-domain}`). `thm:cg-evidence-preserving-channel` assumes no (H4) for either
`Q_o` or `Q_oK`. Erasing the `ext` decoration silently imports a hypothesis the theorem does not
state. The decoration is doing real work. And `07_restrictions.tex:302-311` is the informal preview,
which itself forward-refers to Chapter 6 for the precise version — "The general hypotheses and
equality conditions are stated in \Cref{ch:coarsegraining}" (`07_restrictions.tex:310-311`). Chapter 6
adding the decoration that Chapter 7's preview omits is a coherent authorial ordering, not an
oversight.

**What genuinely survives.** The superscript is never glossed and there is no `\Cref` back to
`05_elbo.tex:458` or `03_probability.tex:240`. A reader can plausibly wonder whether
`\mathcal L^{\rm ext}` is a *different, stronger* functional than `\Lelbo`. That is a one-clause
expository gap in an unreferenced terminal result. **Low**, not high. "Undefined load-bearing symbol"
is wrong on both adjectives.

---

## N-3 — `R` is quadruple-booked; ch.2 / ch.7b feed reciprocal group elements

**Verdict: SURVIVES-AT-LOWER-SEVERITY (low).**

The finding already grants the decisive point in its own body: "Both formulas are *correct*; the
mirror is an artifact of which group element is fed to the representation" and it self-labels
"**not** a mathematical error" (`lens-integrity.md:163, 197`). So no proof step is wrong. The residual
claim is that the direction is "externally unverifiable by a reader". Three checks reduce that.

**(i) The direction is stated in Chapter 2, 200 lines *before* `:361`, in the section on frame
choices.**

```
02_geometry.tex:148-158
u_i^{b\prime}=u_i^b\cdot a_i, \qquad u_i^{m\prime}=u_i^m\cdot b_i, ...
They change associated coordinates by
$\beta_b'=\widehat\rho_b(a_i)^{-1}\beta_b$ and $\beta_m'=\widehat\rho_m(b_i)^{-1}\beta_m$.
```

A reader who has that has the old-to-new coordinate matrix. The finding asserts "`02_geometry.tex:361`
introduces `R_b` with no definition at all and the reconciling statement lives two chapters away"
(`lens-integrity.md:201-202`). The reconciling statement is `02_geometry.tex:157`, same chapter, and
`02_geometry.tex:661-664`, same chapter.

**(ii) The sandwich is type-forced, so the phrase "the represented coordinate changes" pins `R`
uniquely.** `D\Phi` maps belief-fiber coordinates to model-fiber coordinates. Writing `R_x` for the
matrix implementing old-to-new in channel `x`, the only type-correct form is
`(D\Phi)' = R_m(D\Phi)R_b^{-1}` — which is `02_geometry.tex:363` verbatim. There is exactly one matrix
answering to "the represented coordinate change"; the equation is self-definitional.

**(iii) Chapter 7b declares its `R` type explicitly, in situ, one line before use.**

```
07b_agent_network_rg.tex:300-301
On a separately declared linear feature fiber $V_x$, let
$R_x:G\to\operatorname{GL}(V_x)$ be a linear representation.
```

`R_x` in 7b is *the representation itself*, a map `G -> GL(V_x)`, not a matrix — a different type from
ch.2's `R_b`, declared as such. `R_{x,f}=\bigoplus_i R_x(a_i^x)` is then `\rho_x(a)`, and by
`02_geometry.tex:157` the coordinate matrix is its inverse, giving
`\mathsf C_x'=R_{x,c}^{-1}\mathsf C_x R_{x,f}` at `:315`. Consistent, and derivable from data the
reader already has. The finding's own remediation (ii) — "add one clause stating that `a_i^x` is the
rechoice element of `eq:geo-local-reframing`" — is **already in the file**, 50 lines earlier:

```
07b_agent_network_rg.tex:262-263
Under the passive section rechoices
$a_i^b=a_i$ and $a_i^m=b_i$ of \Cref{eq:geo-local-reframing}, it transforms as
```

**(iv) All three equations in the finding are dead ends.**

```
$ grep -rn "geo-defect-gauge-laws|geo-represented-frame-change|rg-linear-cross-scale-covariance" *.tex
02_geometry.tex:366                  \label{eq:geo-defect-gauge-laws}
02_geometry.tex:665                  \label{eq:geo-represented-frame-change}
07b_agent_network_rg.tex:318         \label{eq:rg-linear-cross-scale-covariance}
```

Zero references each. No proof anywhere consumes the convention.

**(v) The ch.11 "fourth meaning" is not a fourth meaning.** The finding lists `R_i` at
`11_obstructions.tex:201` as an "observation noise covariance". The chapter calls it something else:

```
11_obstructions.tex:225
exactly, for every $v\in\R^{K}$ and every choice of transports and link covariances.
```

`R_i` is the **link covariance** on edge `(b,i)`, paired with the graph link `\Theta_i` — part of the
declared graph-link data set out in the chapter's own opening (`11_obstructions.tex:6-16`), not an
unrelated Kalman-style noise matrix. And the appendix-declared refinement kernel `R` occurs at
exactly **one** site in the whole manuscript (`07_general_renormalization.tex:501-503`), nine
chapters from `02_geometry.tex:361`.

**What survives.** `02_geometry.tex:361` introduces `R_b,R_m` by prose phrase alone with no formula,
where a formula was available 200 lines later at `:661-664`, and with a subscript/superscript index
placement inconsistent with that site. That is a real inconsistency, in an equation nothing cites.
**Low.**

---

## N-5 — `P_b` means both the belief principal bundle and an SPD precision matrix

**Verdict: REFUTED.**

The finding's severity argument rests on one sentence: "The clash is aggravated because Chapter 11 is
*about* the bundle theory's obstructions, so both readings are live in the reader's mind"
(`lens-integrity.md:279-281`). That sentence is false against the file.

```
$ grep -c 'principal' 11_obstructions.tex
0
$ grep -c 'bundle' 11_obstructions.tex
2
```

The word **principal appears zero times in Chapter 11.** Both occurrences of "bundle" are
disclaimers: `11_obstructions.tex:14` distinguishes graph links from "the cross-bundle morphisms
`\Phi,\widetilde\Phi`", and `11_obstructions.tex:415` states "No conclusion about bundle topology or
base curvature follows from the reciprocal-pair calculation." The principal-bundle reading of `P_b`
is not merely dormant in Chapter 11 — the chapter explicitly evacuates it.

**The Chapter 11 subscript is not the belief channel.** It is the *name of the apex latent variable*,
declared four lines before first use:

```
11_obstructions.tex:190-196
b\sim\mathcal N(0,P_0^{-1}), \qquad y_i\given b\sim\mathcal N(\Theta_i b, R_i), \qquad i=1,\dots,n .
```

`P_b` is the precision of `b`. The chapter uses the same subscript for `m_b` (mean of `b`), `q_b`
(factor of `b`), `r_b` (information vector of `b`), and `P_0` (prior precision of `b`) — a single
coherent variable-naming scheme (`11_obstructions.tex:209-313`). The finding's own remediation —
"subscript it with the apex node label rather than `b`" (`lens-integrity.md:284-285`) — asks for
what the text already does; the apex node label *is* `b`.

**The Chapter 2 use is confined to an explicitly optional 25-line section.** `P_b` occurs at
`02_geometry.tex:684, 688, 693` and nowhere else in the manuscript's geometry, all inside
`\section{Optional product-gauge extension}` (`:678`), opening "If the application genuinely requires
independently nonisomorphic principal bundles" (`:681`). The appendix row agrees: "Used only when
independent principal topology or independent physical gauge symmetries are intended. **It is not
required** for separate frames, representations, or connections in the ambient theory"
(`appendix_notation.tex:179-183`). The ambient theory's principal bundle is undecorated `P`
(`appendix_notation.tex:22-25`).

So the collision is between a `K x K` SPD matrix and a construct that the manuscript declares
optional, uses three times, and never invokes again. Nine chapters of separation, opposite types,
and a chapter that scrubs the bundle reading before the matrix appears. Note also that undecorated
`P` carries *more* simultaneous meanings than `P_b` — principal bundle
(`appendix_notation.tex:22`), joint law `P(do,dx)` (`06_general_coarsegraining.tex:198`), posterior
`P_o`, parameterized family `P_\theta` — and the finding does not flag it, because context
disambiguates. The same reasoning applies to `P_b` with more margin, not less.

HIGH is unjustified and no residual defect is identified. Adding an appendix row would be tidy;
nothing is wrong without it.

---

## N-6 — `\Theta` carries six distinct meanings

**Verdict: REFUTED.**

The count is inflated and the flagged intra-chapter collision fails the test the review set for it.

**The intra-file test, run rather than assumed.** In `06_gaussian.tex` there are 23 `\Theta`
occurrences. Bare, undecorated `\Theta` occurs at exactly **two** of them:

```
$ grep -n '\\Theta\([^_^]\|$\)' 06_gaussian.tex
38:  ... the natural parameter pair $(h,\Theta)$ with $\Theta=-\tfrac12J$ ... on the open convex
      domain $\R^{n}\times\{\Theta\prec0\}$.
47:  ... Since $J\mapsto-\tfrac12J$ is affine, convexity in $(h,\Theta)$ transfers ...
```

`:38` is the proposition statement, `:47` is its proof, nine lines apart. The natural-parameter
meaning is confined to one paragraph at the top of the chapter and never used again. The other 21
occurrences are all `\Theta_{ij}` or `\Theta_{i\operatorname{pa}(i)}` — always double-subscripted,
always in `\GL^+(K)`, first at `:138` in a *different section* (`sec:gauss-hypothesis`, `:132`), 90
lines and a section break later. The task's own safety criterion ("completely safe if one is always
subscripted `_{ij}` and the other never is") is met exactly.

The type separation is also stated at the boundary: `\Theta\prec0` (negative definite) versus
`\Theta_{ij}\in\GL^+(K)`. No equation puts both in play. There is no derivation in which a reader
could misparse one for the other.

**The second-meaning introduction carries its own non-identification clause**, which is the
manuscript's declared discipline:

```
06_gaussian.tex:137-140
In this Gaussian belief-channel subsection, write
\(\Theta_{ij}:=\rho_b(\Theta_{ij}^b)\in\GL^+(K)\) for the represented
graph link.  This abbreviation does not identify it with a base-manifold
parallel transport.
```

**The count of six is wrong.** Two of the six collapse:

1. The `11_obstructions.tex:201` "observation loading matrices" are not a distinct meaning. The
   chapter head declares them: "Every discrete map in this chapter is a graph-link datum. We write
   \(\Theta^b_e\) and \(\Theta^m_e\) ...; **the Gaussian examples suppress the sector superscript**"
   (`11_obstructions.tex:6-9`). `\Theta_i \in \GL^+(K)` at `:201` is the same appendix-declared
   graph link (`appendix_notation.tex:131-138`) with the superscript suppressed exactly as announced,
   and the text calls its configurations "transport-consistent" (`:220`) and "a transported pooling"
   (`:247`). Same object as `06_gaussian.tex:138`, not a sixth.
2. `06_general_coarsegraining.tex:55` is not a competing use of the glyph. Every one of its six
   occurrences is the index set in `\{P_\theta\}_{\theta\in\Theta}` (`:55, :57, :127, :139, :562,
   :566`), always with the paired lowercase `\theta` in the same token. This is the single most
   entrenched convention in parametric statistics; it disambiguates itself.

That leaves the graph link (appendix-declared), a Gaussian natural parameter used twice in one
paragraph, a matrix-Gamma argument slot `\Theta\succeq0` at `10_renormalization.tex:425-432`, and a
parameter set spelled `\theta\in\Theta`. HIGH is unsupportable. A `\Theta` row in the appendix is
optional housekeeping.

---

## N-7 — `\mathcal R` carries six distinct meanings, three inside `05d_relational_inference.tex`

**Verdict: REFUTED.**

The finding refutes its own count in its own remediation: "keep `\mathcal R` for the
coarse/renormalization map family (**it is the dominant use** and matches `\widehat{\mathcal R}`)"
(`lens-integrity.md:359-361`). Four of the six listed items are that one family —
`05d:719` (smooth coarse map), `05d:769` (`\mathcal R_\ell`, level-indexed coarse map),
`07b:614` (`\mathcal R_b`, block RG operator), `07:46` (`\widehat{\mathcal R}_\ell`). Counting a map
and its indexed members as separate meanings inflates six to what is really three.

**The intra-file test in 05d, run on the passages.** The three flagged uses are:

1. `05d_relational_inference.tex:287` — `\mathcal R^-_{\Fenergy_i}(Q)=\{-a\operatorname{grad}^F
   \Fenergy_i(Q):a>0\}`. Carries **both** a superscript `-` and a subscript `\Fenergy_i`. It is
   defined at the display where it first appears ("At a noncritical configuration $Q$, define the
   positive descent ray", `:285`) and occurs **exactly once in the manuscript**
   (`grep -n '\\mathcal R' 05d_relational_inference.tex` returns `:287` and nothing else with that
   decoration).
2. `05d:719` — bare `\mathcal R`, defined in situ: "Let $\mathcal R:\mathcal Q_f\to\mathcal Q_m$ be a
   smooth coarse map."
3. `05d:769` — `\mathcal R_\ell`, the level-`\ell` member of the same family:
   `Q^{(\ell+1)}=\mathcal R_\ell(Q^{(\ell)})`.

Items 2 and 3 are one concept. Item 1 shares no decoration with them and occurs once. No equation in
`05d` puts two meanings in play; `:287` and `:719` are 432 lines apart with a chapter-internal
section boundary and orthogonal decoration.

**The root set is unmistakable in every occurrence.** `\mathcal R` as a vertex subset appears in
`04_generative.tex:22` (`$\mathcal R=\{r:\operatorname{pa}(r)=\varnothing\}$`) and in `05_elbo.tex`
only inside set-membership expressions: `r\in\mathcal R` (`:309, :314`), `i\in V\setminus\mathcal R`
(`:318, :323`), `|\mathcal R|` (`:348`), plus the in-situ declaration at `:302` ("let
\(\mathcal R\subseteq V\) be the root set"). It is never applied to an argument; the coarse map is
never used in a membership relation. Type-disjoint use.

HIGH is unsupportable. A `\mathcal R` appendix row is optional housekeeping; renaming the root set
would be gratuitous churn across two chapters.

---

## Verdict table

| # | Claim as raised | Verdict | Governing evidence |
|---|---|---|---|
| N-1 | `\mathcal L^{\rm ext}` undefined, load-bearing, HIGH | **SURVIVES-AT-LOWER-SEVERITY (low)** | Value given in situ twice; concept named and displayed at `05_elbo.tex:458`; policy declared at `03_probability.tex:240`; proof uses no property of it (`06_gcg:218-222`); theorem referenced 0 times |
| N-3 | `R` quadruple-booked, direction never stated, HIGH | **SURVIVES-AT-LOWER-SEVERITY (low)** | Self-labeled "not a mathematical error"; direction at `02_geometry.tex:157`; `R_x` typed at `07b:301`; `a_i^x` tied to `eq:geo-local-reframing` at `07b:262`; all three equations referenced 0 times; ch.11 `R_i` is the declared link covariance (`11:225`) |
| N-5 | `P_b` = principal bundle and SPD precision, HIGH | **REFUTED** | `grep -c 'principal' 11_obstructions.tex` = **0**; `b` is the apex latent name (`11:191`); ch.2 use confined to `\section{Optional product-gauge extension}` (`02:678-693`), declared "not required" (`appendix_notation.tex:182`) |
| N-6 | `\Theta` six meanings, two in `06_gaussian.tex`, HIGH | **REFUTED** | Bare `\Theta` = 2 of 23 occurrences, both within 9 lines, `\prec0` vs `\GL^+(K)`, 90 lines and a section break from `\Theta_{ij}`; scoped declaration with non-identification clause at `06_gaussian:137-140`; ch.11 `\Theta_i` is the declared graph link (`11:6-9`); `06_gcg` `\Theta` is `\theta\in\Theta` |
| N-7 | `\mathcal R` six meanings, three in `05d`, HIGH | **REFUTED** | Finding's own fix concedes 4 of 6 are one family; `\mathcal R^-_{\Fenergy_i}` occurs once with unique decoration and is defined at its display (`05d:285-289`); root set only ever in membership expressions |

---

## Ranking: which single item deserves the author's attention

**N-1.** It is the only one of the five that sits inside the displayed equation of a
`\status{ESTABLISHED}` theorem, it is the only one where a reader can form a *wrong belief* rather
than merely a momentary parse ambiguity (that `\mathcal L^{\rm ext}` is a different and stronger
bound than `\Lelbo`), and the repair has genuine mathematical content: the `ext` decoration marks the
(H4)-free relative-log extension of `05_elbo.tex:458`, and saying so names a hypothesis the theorem
deliberately avoids. One sentence before `eq:cg-elbo-monotone` plus a `\Cref` to `05_elbo.tex:458`
and `03_probability.tex:240` closes it.

Do **not** apply the finding's fix option (b). Replacing `\mathcal L^{\rm ext}` with `\Lelbo` would
silently import `\Cref{hyp:elbo-evidence-domain}`(H4), which
`thm:cg-evidence-preserving-channel` does not assume. That would convert an expository gap into a
mathematical one.

N-3 is second, and only for the one-line repair at `02_geometry.tex:361` (write the formula from
`:661-664` instead of the prose phrase, and match its index placement). N-5, N-6, and N-7 warrant at
most four rows added to `appendix_notation.tex` at the author's convenience. None of them justifies a
rename, and the renames proposed in N-6 and N-7 would touch `06_gaussian.tex`, `11_obstructions.tex`,
`04_generative.tex`, and `05_elbo.tex` to fix collisions the text already fences in situ.
