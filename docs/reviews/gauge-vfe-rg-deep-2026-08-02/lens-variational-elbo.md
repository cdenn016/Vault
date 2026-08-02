# Lens review — variational inference / free energy

**Reviewer lens:** ELBO and free-energy decomposition, evidence identity, mean-field and
structured factorization, total correlation, E/M separation, exponential-family closure,
normalization and integrability side conditions, absolute continuity, recognition-law
insertion into the generative target.

**Chapters read in full:** `05_elbo.tex`, `05a_expfamily.tex`, `05b_local_collective_elbo.tex`.
Cross-read for the `\mathcal L^{\rm ext}` question: `03_probability.tex`, `04_generative.tex`,
`06_general_coarsegraining.tex`, `07b_agent_network_rg.tex`, `appendix_notation.tex`,
`appendix_claim_ledger.tex`, `main.tex`.

**Method.** Every load-bearing identity in these chapters was recomputed independently, either
symbolically (sympy) or on a concrete finite model (3 discrete agents on a hypergraph with
overlapping factor scopes; 2 receivers with 3 source labels and a 4-state latent; 1-D Gaussian
exponential family; a 4-dimensional quadratic ELBO). Scripts:
`<scratchpad>/vfe_check.py` and `<scratchpad>/additive_check.py` (run with
`C:/Python314/python.exe`). Residuals below are reproduced verbatim from those runs.

**Out of scope, honored.** LG-1, LG-2, RG-1, RG-2, R01–R21, FINAL-01–08, PB-1–4, and every
obligation the manuscript's own `appendix_claim_ledger.tex` declares OPEN or CONJECTURE. Nothing
below re-raises any of them. The two findings V1 and V2 attack *additional* claims that sit
between those verified entries and are not covered by them: V1 attacks a negative universal claim
in `sec:local-additive-accounting` (LG-1 covers the *positive* local/collective ELBO results only),
and V2 attacks the stated hypothesis of `prop:obs-attention-elbo` (LG-2 certifies the *conclusion*
under the intended factorization, not the sufficiency of the displayed hypothesis).

---

## Adjudication of carried-over candidates

### Candidate #1 — `\mathcal L^{\rm ext}` undefined → **CONFIRMED**, see finding **V3**.

Whole-tree grep confirms the glyph occurs at exactly two places, both inside
`eq:cg-elbo-monotone`:

```
06_general_coarsegraining.tex:209:  \bar{\mathcal L}^{\rm ext}(\bar Q_o;o)
06_general_coarsegraining.tex:213:  =\mathcal L^{\rm ext}(Q_o;o).
```

plus the prose "the extended ELBOs satisfy" at `06:207`. There is **no definition anywhere**:
not in `05_elbo.tex`, not in `05a_expfamily.tex`, not in `03_probability.tex`, not in
`appendix_notation.tex` (which has no `\Lelbo` / `\mathcal L` row at all), and not under another
glyph. The nearest relative is a *prose-only, unnamed, unsymbolized* object at `05_elbo.tex:458`
("its canonical relative-log extension", displayed as `\E_q[\log(p_0/q)]`). Note also that
`main.tex:35` defines `\newcommand{\Lelbo}{\mathcal L}`, so `06` is writing the ELBO glyph
longhand and bypassing the manuscript's own macro — a sign of ad hoc insertion. Details and
severity in V3.

### Candidate #2 — total-correlation / factorization at `05b:292-315` → **KILLED**. Not a finding.

The prior session's report was wrong. Recomputed on a 3-agent model
(`|Y| = 2 x 3 x 2`, product baseline `P_0 = ⊗ρ_i`, genuinely correlated `Q`):

```
F_o(Q)                        = 0.6608893601660132
TC(Q) + Σ_i KL(Q_i||ρ_i) + E_Q[Σ_a E_{a,o}] = 0.6608893601660133
residual                      = -1.11e-16
```

Moreover the identity needs **no extra hypothesis at all** beyond `Q ≪ P_0 = ⊗ρ_i`, which
`thm:obs-collective-vfe` already carries. Proof: `Q ≪ ⊗ρ_i` forces `Q_i ≪ ρ_i` and hence
`Q ≪ ⊗Q_i` (if `∏φ_i = 0` on a set, some `φ_i(y_i)=0`, and `Q(φ_i(Y_i)=0) = ∫_{φ_i=0} φ_i dρ_i = 0`).
The three integrands then satisfy `log(dQ/d⊗ρ) = log(dQ/d⊗Q_i) + Σ_i log(dQ_i/dρ_i)` pointwise
`Q`-a.s., and each term's *negative* part is integrable — for probability measures
`∫ (φ log φ)^- dν ≤ ν(X)/e = 1/e` since `x log x ≥ -1/e`. Sums of extended-real integrals with
integrable negative parts add, so the identity holds unconditionally in `[0,∞]`; no
`∞ - ∞` is reachable. The `L^1(Q)` proviso the manuscript states at `05b:309-311` is needed only
for splitting `E_Q[Σ_a E_{a,o}]` into `Σ_a E_Q E_{a,o}`, exactly as written. There is no missing
factorization hypothesis. The one residue is cosmetic (finding **V4**).

### Candidate #3 — `R_b, R_m` direction. Not my lens; not adjudicated here.

---

## Findings

### V1 — The additive-accounting no-go is false as stated; a symmetric split that both sums to the collective VFE and reproduces every unilateral derivative exists on the manuscript's own example hypergraph

**Claim attacked.** "A symmetric set of local objectives therefore cannot both add to the
collective VFE and reproduce every unilateral derivative for a genuinely interacting factor."

**Location.** `05b_local_collective_elbo.tex:313-315`, inside the `\status{ESTABLISHED}` block at
`05b:308-318`. It is the stated support for the chapter thesis at `05b:10-12` ("the local
objectives are coordinate potentials, **not summands of a canonical symmetric decomposition**").

**Severity.** high.

**Status tag / inflation.** Tagged `\status{ESTABLISHED}` at `05b:318`, asserted with no proof, and
the prose word "therefore" presents it as a consequence of the preceding double-counting sentence,
which it is not. Prose inflation is present: the preceding sentence establishes only that the
*incident-factor* rule double counts; the quoted sentence universally quantifies over all symmetric
local objectives.

**Evidence (recomputation).** Define the symmetric, order-free, allocation-forced weight rule

```
w_{i,a} = 1                                    if i ∈ ∂a
w_{i,a} = (1 - |∂a|) / (N - |∂a|)              if i ∉ ∂a
F_i     = KL(Q_i || ρ_i) + Σ_a w_{i,a} E_Q[E_{a,o}]
```

which requires only `|∂a| < N` for every factor. Then `Σ_i w_{i,a} = 1` for every `a`, so
`Σ_i F_i = F_o` exactly; and `w_{i,a} = 1` on every incident `a`, so `F_i - F_o = Σ_{a: i∉∂a}
(w_{i,a}-1) E_Q[E_{a,o}]` is *identically free of* `η_i`, hence `F_i` reproduces not only every
unilateral derivative but every finite unilateral difference of `F_o`. Numerically, on a product
recognition family with softmax coordinates:

```
TRIANGLE  N = 3  scopes = [(0,1), (1,2), (0,2)]
  sum_i F_i - F_o                       =  0.0
  max_{i,c} |d_eta F_i - d_eta F_o|     =  7.63e-11        (finite-difference truncation only)
  [incident-only rule] sum_i F_i - F_o  =  0.0300797844    (double counts, as manuscript says)
  [1/|scope| rule]     sum_i F_i - F_o  =  0.0   but max deriv mismatch = 0.2267340949

MANUSCRIPT FIGURE HYPERGRAPH  N = 5  scopes = [(0,1), (1,2,4), (2,3)]
  sum_i F_i - F_o                       =  1.67e-16
  max_{i,c} |d_eta F_i - d_eta F_o|     =  1.11e-10
  [incident-only rule] sum_i F_i - F_o  = -0.6697516366
  [1/|scope| rule]     sum_i F_i - F_o  = -5.55e-17, max deriv mismatch = 0.1237467814
```

The second run is the manuscript's own Figure at `05b:258-287` (5 agents; factors `o_a={1,2}`,
`o_b={2,3,5}`, `o_c={3,4}`). So the counterexample is not exotic: it lives on the chapter's own
illustration.

The rule is symmetric in every sense the sentence can intend: one formula for every agent,
determined solely by incidence and cardinalities, equivariant under every automorphism of the
labeled hypergraph, requiring no ordering and no free allocation parameter. Indeed the weights are
*forced*: derivative matching pins `w_{i,a} = 1` for `i ∈ ∂a`, summation pins
`Σ_{i∉∂a} w_{i,a} = 1 - |∂a|`, and symmetry among the non-incident agents pins the rest. The
manuscript's escape clause at `05b:315-317` ("the result depends on the order or allocation") is
therefore inapplicable to this witness.

**What is actually true.** The claim becomes true under an unstated **graph-locality** hypothesis:
if each `F_i` is required to be a function of `KL(Q_i||ρ_i)` and the *incident* factor expectations
`{E_Q[E_{a,o}] : a ∈ A_i}` only, then `Σ_i F_i = F_o` forces `Σ_{i∈∂a} w_{i,a} = 1` while
derivative matching forces `w_{i,a} = 1` on each `i ∈ ∂a`, so `|∂a| = 1` for every factor and no
genuine interaction remains. It is also true without locality when some factor has global scope
`|∂a| = N` (in particular for the two-agent single-factor case, where the two requirements force
`A(η_1,η_2)` to be additively separable). Both restrictions are absent from the text.

The mechanism the manuscript declares impossible is the standard *counting-number* /
inclusion–exclusion construction of region-based free energies (Yedidia–Freeman–Weiss 2005,
Sec. IV-A), where negative counting numbers are the norm and exist precisely so each factor is
charged once. Citation and verbatim excerpt below.

**Fix.** Replace `05b:313-315` with, e.g.: "A set of **graph-local** objectives — each a function of
its agent's own relative entropy and of the factors incident to it — therefore cannot both add to
the collective VFE and reproduce every unilateral derivative for a genuinely interacting factor;
symmetric splits that do both exist, but they charge every agent a negative share of factors it
does not touch (the counting-number construction of region-based free energies,
`\citep{Yedidia2005}`), and are therefore not local objectives in the sense of
`\Cref{thm:obs-local-multiagent-elbo}`." Then weaken `05b:10-12` correspondingly, or add "of local
objectives".

**Falsifies.** The universally quantified no-go at `05b:313-315`, and the framing sentence at
`05b:10-12`. It does **not** touch `thm:obs-local-multiagent-elbo`, `thm:obs-local-global-potential`,
`eq:obs-global-ledger`, or LG-1, all of which I re-verified exact (below).

---

### V2 — `prop:obs-attention-elbo`'s displayed hypothesis is insufficient for its displayed conclusion; the defect is exactly the total correlation the manuscript's own Prop. in Ch. 5 warns about

**Claim attacked.** "If a mean-field recognition row `β^Q_i` is independent of `y`, its exact
categorical contribution to the collective VFE is `-E_Q log c_i(o_i,Y) + F_i^att(β_i^Q)`", with
`F_i^att(β^Q_i) = KL(β^Q_i||π_i) + τ_i^{-1} Σ_j β^Q_{ij} E_Q D_{ij}`, and the softmax optimum
`β^{Q*}_{ij} ∝ π_{ij} exp(-E_Q D_{ij}/τ_i)`.

**Location.** `05b_local_collective_elbo.tex:347-375`; the offending clause is line 355;
`eq:obs-attention-full-contribution` (358), `eq:obs-attention-vfe` (363-365),
`eq:obs-attention-recognition-optimum` (370-372). Proof at `05b:377-390`.

**Severity.** high.

**Status tag / inflation.** `\status{ESTABLISHED}` at `05b:375`. The word "exact" in the statement
is the inflation: the displayed identity is exact only under a factorization that the proposition
never displays. "Mean-field" occurs exactly once in the three chapters I own (`05b:355`) and is
never defined, while `05_elbo.tex:23` explicitly declares "No factorization is imposed here" for
the recognition kernel.

**Evidence (recomputation).** With the augmented baseline `P_0^{aug}(dy,dj) = P_0^Y(dy) ∏_i π_i(dj_i)`
of `eq:obs-attention-augmented-baseline`, write `Q(dy,dj) = Q_Y(dy) Q_{J|Y}(dj|y)`. Then exactly

```
F_o(Q) = KL(Q_Y||P_0^Y)
       + E_{Q_Y}[ TC(Q_{J|Y}) ]                       <-- MISSING TERM
       + Σ_i [ KL(β_i||π_i) + τ_i^{-1} Σ_j β_{ij} E_{Q_Y} D_{ij} - E_{Q_Y} log c_i ]
```

The hypothesis "`β^Q_i` is independent of `y`" makes each *row* `y`-free and thus gives
`J_i ⊥ Y` marginally, which is enough for the energy term but **not** for the KL term: the
relative entropy to `⊗_i π_i` picks up the cross-receiver total correlation
`E_{Q_Y}[TC(Q_{J|Y})] ≥ 0`, which vanishes iff the source labels are conditionally independent
across receivers given `Y`, `Q_Y`-a.s.

Two receivers, three sources, four latent states, `τ = (0.8, 1.4)`:

```
(a) fully factorized Q = Q_Y ⊗ β_1 ⊗ β_2 :   F_o - claimed = 0.0                (exact)
(b) y-free rows, J_1,J_2 correlated       :   F_o - claimed = 0.09335399997832239
                                              E_{Q_Y}[TC(Q_{J|Y})] = 0.09335399997832222
                                              difference           = 1.67e-16
(c) y-free rows, y-DEPENDENT copula       :   F_o - claimed = 8.017971629632e-04
                                              E_{Q_Y}[TC(Q_{J|Y})] = 8.017971629629e-04
                                              difference           = 3.31e-16
```

Case (a) confirms the proposition is *true* under full mean-field, so this is a hypothesis defect,
not a computational error. Cases (b) and (c) satisfy the displayed hypothesis verbatim (every row
`β^Q_i` is a fixed vector independent of `y`) and falsify the displayed identity.

The sign matters and it is the same failure mode as `prop:elbo-total-correlation-signs`
(`05:58-65`): the claimed contribution is `F_o` **minus** a total correlation, so the ELBO it
implies is **larger** by that total correlation and can exceed the log evidence. `05:350`
explicitly forbids this substitution — "replacing it by `Σ_b E_{Q_X}[log q_b]` inflates the bound
by the total correlation" — which makes this an internal inconsistency, not merely an omission.

The consequence is not confined to the ledger: the claimed softmax coordinate optimum is not the
coordinate optimum when the labels are coupled. Minimizing the *true* `F_o` over `β_1` with the
`(J_1,J_2)` coupling held at a fixed odds-ratio kernel (IPF, positive association) gives

```
true coordinate minimizer β_1 = [0.212508472126, 0.454836756703, 0.332654771172]
softmax formula        β_1*   = [0.210278819805, 0.454900304113, 0.334820876081]
max |difference|              = 2.2297e-03
F_o(true) = 2.123728364886512   <   F_o(softmax) = 2.123745049668524
```

A further symptom: `05b:399` writes "Holding the latent recognition law `Q_Y`, and hence every
`E_Q D_{ij}`, fixed", which silently presupposes `J ⊥ Y` — under a general `Q` the symbol
`E_Q D_{ij}` is ambiguous between `E_{Q_Y}[D_{ij}(Y)]` and `E_Q[D_{ij}(Y) | J_i = j]`, and only the
factorization collapses them.

**Adversarial self-test.** The charitable reading is that "mean-field" already means full
factorization, making the extra clause "is independent of `y`" redundant. Three things defeat that
reading. (i) The clause attaches to "a mean-field recognition **row** `β^Q_i`", i.e. it is a
property predicated of one row, and the following clause restates precisely the row-level
condition. (ii) The chapter never defines "mean-field", and `05:23` and `05:31` spend a page
insisting that the population recognition law is *not* recoverable from its marginals. (iii) A
`y`-free row family is already a restricted recognition family, and within that restriction
correlated labels remain fully admissible — so the excluded case is not vacuous. The correlated
case is also not off-support: the *exact* posterior does factorize the labels given `(Y,O)`, but
the recognition family here is constrained to `y`-free rows, so the recognition optimum within that
constrained family need not, as the numeric above shows.

**Fix.** One clause. Replace `05b:355` with: "If the recognition law factorizes as
`Q(dy,dj) = Q_Y(dy) ⊗_i β^Q_i(dj_i)` with each row `β^Q_i` independent of `y`, its exact
categorical contribution ... is". Optionally add the general statement as a remark: under
`y`-free rows alone the exact contribution is `E_{Q_Y}[TC(Q_{J|Y})] + Σ_i(...)`, and the softmax
formula is the coordinate optimum only when that defect is zero. Chapter 7b already does the exact
thing correctly at `07b:504-524`, where the joint event law `η` is disintegrated with a genuine
conditional KL chain rule rather than a product hypothesis — worth a cross-reference.

**Falsifies.** The "exact" in `05b:355-360` and, consequently, the unqualified reading of
`eq:obs-attention-recognition-optimum`. It does **not** falsify LG-2, whose conclusion holds under
the intended factorization, and it does not touch the recognition-blindness result (the generative
`D_{ij}` really does not read a live recognition law — that part is clean, see V-clean below).

---

### V3 — `\mathcal L^{\rm ext}` is an undefined load-bearing symbol, and the theorem's hypotheses are insufficient under one of the two available readings

**Claim attacked.** `thm:cg-evidence-preserving-channel`, whose *only* displayed conclusion is
`eq:cg-elbo-monotone`, stated entirely in an undefined symbol.

**Location.** `06_general_coarsegraining.tex:207` (prose), `:209` and `:213` (the symbol),
`eq:cg-elbo-monotone` at `:208-215`, `\status{ESTABLISHED}` at `:216`.

**Severity.** medium.

**Status tag / inflation.** `\status{ESTABLISHED}`. A theorem whose conclusion is written in an
undefined symbol cannot be established as stated; the ESTABLISHED tag over-reports.

**Evidence (search, exhaustive).** Grep over every `.tex` in the manuscript directory for
`\rm ext`, `\mathrm{ext}`, `\text{ext}`, `^{ext}`, "extended ELBO", "extension", `\Lelbo^`:
the glyph appears at exactly `06:209` and `06:213`, and the phrase "extended ELBO" at exactly
`06:207`. `appendix_notation.tex` contains no `\Lelbo` / `\mathcal L` row of any kind.
`main.tex:35` defines `\newcommand{\Lelbo}{\mathcal L}`; chapter 6 writes `\mathcal L` longhand,
bypassing the macro. `05_elbo.tex` defines only `\Lelbo(Q_X;X)` at `eq:elbo-definition` (`05:122-128`).

**Why this is more than notation.** The two available readings are not equivalent and the theorem
does not say which is meant.

*Reading A:* `L^ext(Q;o) := log p(o) - KL(Q||P_o)`, valued in `[-∞, log p(o)]`, well defined
whenever `0 < p(o) < ∞` regardless of integrability. Then the first and last equalities of
`eq:cg-elbo-monotone` are definitional, the inequality is the data-processing inequality already
proved just above, and the theorem carries no content beyond it — which changes what the reader
should take from it.

*Reading B:* `L^ext = \Lelbo` of `eq:elbo-definition`, i.e. `E_Q[log p(o,Y) - log q(Y)]`. Then the
first and last equalities require the chapter-5 hypothesis (H4) (`eq:elbo-log-integrability`) at
both the fine and coarse levels, and `thm:cg-evidence-preserving-channel` states **no**
integrability hypothesis whatsoever (`06:198-200` lists only: normalized joint, regular `o`,
posterior, recognition law, normalized `Q_o`-blind channel). Under reading B the stated hypotheses
do not support the stated conclusion, and the manuscript's own witness supplies the failure: take
`Q_o = P_o` with `P_o(\{n\}) = c/(n(\log n)^2)` on `\{2,3,\dots\}` (`05:414-425`). Then
`KL(Q_o||P_o) = 0`, so reading A gives `L^ext = log p(o)`, while reading B is the undefined
`-∞ - (-∞)` because `Σ_n P_o(n)|\log P_o(n)| = ∞`.

Numerically the inequality itself is fine (`nx=6, ny=3`, random row-stochastic `K`):
`KL(Q||P) = 0.1996686145798062`, `KL(QK||PK) = 0.0018381405155496414`, monotone: True.

**Fix.** Add one line to `05_elbo.tex`, immediately after `eq:elbo-free-energy` (`05:130-133`),
promoting the prose at `05:458` to a definition:

```latex
When (H4) fails, the separately integrated bound is undefined; its canonical relative-log
extension \(\Lelbo^{\rm ext}(Q;o):=\log p_\theta(o\given X)-\KL(Q\Vert P^\star)\in[-\infty,\log
p_\theta(o\given X)]\) is defined whenever (H1)--(H3) hold, and coincides with
\eqref{eq:elbo-definition} under (H4).  \status{DEFINITION}
```

Then have `06:209,213` use `\Lelbo^{\rm ext}` (the macro) and cite that definition, and add a row to
`appendix_notation.tex`. This also makes the extended-real convention at `05b:106`,
`05b:167-169`, and `07b:509` uniform.

**Falsifies.** The self-containment of `thm:cg-evidence-preserving-channel` as stated. It does not
falsify the underlying data-processing inequality, which is correct.

---

### V4 — `Q_i` in `eq:obs-total-correlation` is never declared to be the marginal of `Q`, and the identity is false for any other choice

**Location.** `05b_local_collective_elbo.tex:292-296` (`eq:obs-total-correlation`) and `:299-305`
(`eq:obs-global-ledger`). Contrast `05_elbo.tex:34` and `eq:elbo-total-correlation`, which *do*
declare "block marginal densities `q_b`".

**Severity.** low.

**Status.** `\status{ESTABLISHED}` at `05b:306`. No inflation; the identity is true, only the
symbol is undeclared.

**Evidence.** Same 3-agent run as candidate #2. With `Q_i` = marginals of `Q`, residual
`-1.11e-16`. Substituting three independently drawn probability vectors of the same shapes in
place of the marginals moves the residual to `-0.6946949551581781`, i.e. the identity is specific to
the marginals and to nothing else.

**Fix.** In `05b:292`, write "define the total correlation of the marginals `Q_i` of `Q`" or add
`Q_i := Q\circ\pi_i^{-1}`.

**Falsifies.** Nothing. Reader hygiene.

---

### V5 — "an agent following its exact local VFE follows a block of the collective VFE flow" is not what the preceding sentence proves; it requires the *outside-averaged* local VFE

**Location.** `05b_local_collective_elbo.tex:442-443`.

**Severity.** low.

**Status.** `\status{ESTABLISHED}` at `05b:443`. Prose inflation relative to the correct statement
at `05b:428-429`, which does say "outside-averaged", and to `appendix_notation.tex:111-115`, which
registers `\overline{\Fenergy}_{B,o}` precisely as "outside-averaged conditional block VFE at fixed
`Q_{B^c}`".

**Evidence.** `eq:obs-local-global-decomposition` gives `∇_{η_i} F_o = ∇_{η_i} E_{Q_{-i}}[
F_{i,o}(r_i; Y_{-i})]`, not `∇_{η_i} F_{i,o}(r_i; b)` at any single realized blanket value `b`.
Since `H_{B,o}(y_B;b)` genuinely depends on `b`, the two gradients differ pointwise; only the
`Q_{B^c}`-average is a block gradient of the collective objective. In a multi-agent reading this is
a substantive modeling distinction (does an agent see the realized neighbor state or the
recognition-averaged one?), not a typographic one.

**Fix.** "Thus an agent following its **outside-averaged** exact local VFE follows a block of the
collective VFE flow."

**Falsifies.** Nothing proved; only the summary sentence.

---

### V6 — "There is one bound in this document, it bounds one number" is contradicted by two further bounds on two other numbers

**Location.** `05_elbo.tex:4`. Contradicted by `05b:187-189` ("Consequently `-F_{B,o}` is a local
multi-agent ELBO on the conditional log evidence `log Z_B(b)`", with `05b:200-201` conceding
"`Z_B(b)` is conditional evidence, not the collective evidence `Z(o)`") and by
`06:207-215` (`\mathcal L^{\rm ext}` and `\bar{\mathcal L}^{\rm ext}`). The two generative
constructions are also distinct objects: `04_generative.tex` builds a directed per-design-point
DAG law, `05b:51-56` builds a factor-hypergraph law with its own baseline `P_0` and evidence `Z(o)`.

**Severity.** low.

**Status.** Untagged framing prose in a chapter preamble.

**Fix.** "There is one bound *per fixed normalized joint and one selected conditioning*; every
further bound in this document is an instance of the same identity applied to a declared joint,
and the chapter records which number each bounds."

**Falsifies.** Nothing mathematical.

---

### V7 — "the pointwise finite factor sum" over-claims; `Σ_a E_{a,o}` is pointwise well-defined but need not be finite

**Location.** `05b_local_collective_elbo.tex:308-309`.

**Severity.** low.

**Evidence.** `E_{a,o} = -\log ℓ_a(o_a|y_{∂a}) ∈ (-∞, +∞]`, and `+∞` is explicitly permitted by the
same chapter at `05b:82-86` ("A binary success record with `K_a(1|y)=exp[-E_a(y)]` is a valid
special case only when `E_a ∈ [0,+∞]`"). The sum is therefore well defined in `(-∞,+∞]` — which is
all the ledger needs, since the remaining terms are nonnegative — but it is not "pointwise finite".

**Fix.** "each interaction appears once inside the pointwise well-defined `(-∞,+∞]`-valued factor
sum".

---

## Recomputed and found exact — no finding

Every item below was independently recomputed; residuals are machine epsilon. These are recorded so
the coordinator can see what the two findings do *not* touch.

| Object | Location | Residual |
|---|---|---|
| `eq:elbo-total-correlation-signs`, `F̃ = F - TC`, `L̃ = L + TC` | `05:58-65` | `0.0` |
| Gaussian TC formula `½(Σ_b log det C_bb - log det C)` | `eq:elbo-total-correlation-gaussian` | `-8.88e-16` |
| `eq:elbo-identity` (evidence identity) | `05:137-146` | exact by construction; sign and orientation correct |
| `cor:elbo-bound-tightness`, equality iff `Q = P^*` as measures | `05:188-197` | correct |
| `prop:restrict-principle`, `eq:restrict-sup-identity`, `eq:restrict-loss` | `05:213-236` | correct; under (H1)–(H4), `KL = log p(o) - L` is finite, so no `∞-∞` in `eq:restrict-loss` |
| `eq:elbo-kl-chain-rule` (block KL chain rule) | `05:392-404` | `-1.67e-16` |
| E-coordinate optimum `KL(Q^new‖P) = KL(R‖P_-)` | `eq:elbo-e-coordinate` | `0.0` |
| Cauchy/Gaussian witness `KL = +∞`; `c/(n log²n)` witness `KL = 0`, (H4) fails | `05:413-426` | both verified analytically; `Σ (c/2)/(n log n)` diverges |
| M-coordinate witness `r_n = 1+εh_n`, `Σq_nr_n = 1`, `r>0`, `E_q[log r] = -KL(q‖p_1) < 0` | `05:446-466` | all four conditions verified |
| `prop:elbo-evidence-monotonicity` chain | `05:480-491` | correct; correctly requires the **full** exact E-step (not a block one) for the evidence chain, per Dempster–Laird–Rubin |
| `eq:elbo-step-size-failure`, `½ d_max c²[1-(1-α d_max)²]` | `05:502-509` | `≤ 6.22e-15` over `α d_max ∈ {0.5,1,2,2.5,3}`; sign flips exactly at `α d_max = 2` |
| `prop:elbo-factorwise-decomposition`, `3MN` factor count, `eq:elbo-audit` | `05:306-348` | `0.0` on an `M=1, N=2` two-channel chain; count `3MN` correct |
| `eq:exp-kl-bregman`, `KL(Q_ϑ‖Q_θ) = D_A(θ,ϑ)` | `05a:311-317` | sympy: `simplify(KL - D_A) = 0` for the 1-D Gaussian `T=(z,-z²/2)` |
| `eq:exp-kl-dual-bregman`, `= D_{A*}(τ_ϑ,τ_θ)` | `05a:319-322` | `5.55e-17` |
| `eq:exp-projection-kkt`, `∇A*(τ̂) - θ + Bᵀλ = 0` | `05a:352-356` | correct: `∇_τ D_{A*}(τ,τ_θ) = ∇A*(τ) - θ` |
| `prop:exp-domain-boundary-no-law` (line-segment principle, `g'` unbounded, `∫g'' = ∞`) | `05a:185-214` | correct; the terse "convexity puts every `θ_τ, τ<1` in `N`" is Rockafellar's line-segment principle, valid since `θ_0 ∈ int N` and `θ* ∈ cl N` |
| `prop:exp-fixed-point-no-law` scale witness, `A(θ) = -½log θ + ½log 2π`, `N=(0,∞)` | `05a:223-243` | correct |
| `thm:obs-collective-vfe`, `F_o = -log Z + KL(Q‖Π_o)`, incl. the `Q ⋠ Π_o` branch | `05b:104-130` | correct; `Q ≪ P_0` + `Π_o(A)=0` ⟹ `H_o = +∞` `Q`-a.s. on `A` |
| `thm:obs-local-multiagent-elbo`; `Π_{o,B}` is the true full conditional of `Π_o` | `05b:164-198` | verified: `Π_o(·|y_{B^c}=b) ∝ e^{-H_{B,o}(y_B;b)} P_{0,B}(dy_B|b)` |
| `eq:obs-local-global-decomposition` | `05b:212-222` | `≤1.67e-16` for `B={2,3}`, `{1}`, `{3}` on a correlated baseline |
| `eq:obs-local-global-potential` (exact-potential identity) | `05b:224-232` | `0.0`, `2.78e-17`, `-7.63e-17` for the same three blocks |
| `eq:obs-global-ledger` | `05b:299-305` | `-1.11e-16`; unconditional in `[0,∞]` (see candidate #2) |
| `eq:obs-attention-posterior` (Bayes row) | `05b:349-353` | correct, incl. conditioning on the full record vector |
| `eq:obs-attention-full-contribution` **under full mean-field** | `05b:357-360` | `0.0` — see V2 for the hypothesis defect |
| `eq:obs-attention-recognition-optimum` (Gibbs/softmax) | `05b:369-373` | correct under full mean-field; equals `argmin_β E_{Q_Y}[KL(β‖β^P(Y))]` |
| `eq:obs-attention-replicator` = Fisher natural gradient on the open simplex | `05b:402-410` | `‖-γ(diag β - ββᵀ)∇F - β̇‖_∞ = 1.67e-16`; `Σ β̇ = 5.27e-16` |
| `eq:obs-attention-dissipation`, `dF/dt = -γ Var_β(c)` | `05b:412-416` | `1.78e-15` |
| `eq:obs-global-dissipation`, block natural-gradient descent | `05b:435-441` | correct for a product family (whose Fisher metric is automatically block diagonal) |
| Data processing / `eq:cg-elbo-monotone` inequality | `06:208-215` | `KL(QK‖PK) = 0.00184 ≤ KL(Q‖P) = 0.19967` — see V3 for the symbol |
| **E/M blindness** (Dempster–Laird–Rubin separation) | `04:120-124`, `05:430-444`, `05b:31-35`, `05b:340-342` | Clean. `eq:elbo-m-coordinate` maximizes the standard `Q`-function `E_{Q_X}[log p_ϑ(o,Y|X)]` at fixed `Q_X`; `req:gen-typing-prohibition` forbids any generative factor from reading `Q_X`; `05b:340-342` explicitly keeps the attention energy `D_{ij}` free of a live recognition law. No recognition law is inserted into the generative target anywhere in these three chapters. |
| **Posterior consistency** | `05:188-197`, `05:428` | Clean and correctly limited: the exact full E-step recovers `P_θ(·|o,X)` with zero gap; the manuscript explicitly refuses to transfer this to a product family ("A product-family coordinate is a different object entirely"). |

---

## Newly-discovered canon (for `01b_extended_evidence.md`)

1. **Yedidia, Freeman, Weiss (2005), "Constructing Free-Energy Approximations and Generalized
   Belief Propagation Algorithms", IEEE Trans. Inform. Theory 51(7):2282–2312, Sec. IV-A** —
   https://web.cs.ucla.edu/~yzsun/classes/2014Spring_CS7280/Papers/Probabilistic_Models/Constructing%20Free%20Energy%20Approximations%20and%20Generalized%20Belief%20Propagation%20Algorithms.pdf
   Verbatim: *"if some of the large regions overlap, then we will have erred by counting the free
   energy contributed by some nodes two or more times, so we then need to subtract out the free
   energies of these overlap regions in such a way that each factor and variable node is counted
   exactly once."* And: *"We say that a set of regions and counting numbers give a valid
   region-based approximation when, for every factor node a and every variable node i in the factor
   graph [(29)] ... These conditions ensure that every factor and variable node will be counted
   exactly one time in the approximation to the free energy. If a given factor or variable node is
   added into the free energy in two different regions, then there must be another region where it
   is subtracted back out."*
   This is the canonical settlement of exactly the question `sec:local-additive-accounting` asks,
   and it is the source of the counterexample in V1: valid counting numbers with
   `Σ_{R∋a} c_R = 1` exist generically and are routinely negative. **Directly load-bearing for V1.**
   Not currently in `references.bib`.

2. **Friston (2010), "The free-energy principle: a unified brain theory?", Nature Rev. Neuroscience
   11:127–138** — already in `references.bib` as `Friston2010`, but **uncited in Chapters 5, 5a,
   5b**. Verbatim: *"The third formulation expresses free energy as complexity minus accuracy,
   using terms from the model comparison literature. Complexity is the difference between the
   recognition density and the prior density on causes; it is also known as Bayesian surprise ...
   Accuracy is simply the surprise about sensations that are expected under the recognition
   density."*
   `eq:obs-collective-vfe` — `F_o(Q) = KL(Q‖P_0) + E_Q H_o` — **is** this decomposition
   (complexity `KL(Q‖P_0)`, negative accuracy `E_Q H_o`) with a factor-graph likelihood. The
   manuscript should either name and cite it or state why it declines the names. This is blue-team
   support: the collective VFE is in canonical FEP form, not an idiosyncratic functional.

3. **Watanabe (1960), "Information theoretical analysis of multivariate correlation", IBM J. Res.
   Dev. 4(1):66–82** — the origin of *total correlation*, the object used at
   `eq:elbo-total-correlation` and `eq:obs-total-correlation` and cited to nobody (only
   `Kullback1951, Csiszar1967` for the nonnegativity). Also **Studený & Vejnarová (1998), "The
   multiinformation function as a tool for measuring stochastic dependence"**, in Jordan (ed.),
   *Learning in Graphical Models*, MIT Press, for the chain-rule and conditional-independence
   characterization the manuscript uses implicitly. Neither is in `references.bib`.

4. **Monderer & Shapley (1996), "Potential Games", Games and Economic Behavior 14:124–143** — the
   exact-potential-game definition `u_i(a_i,a_{-i}) - u_i(a_i',a_{-i}) = φ(a_i,a_{-i}) -
   φ(a_i',a_{-i})` is literally `eq:obs-local-global-potential` with `φ = F_o`. Their result that
   an exact potential is unique up to an additive constant is the right frame for the
   `sec:local-additive-accounting` discussion and would sharpen it. Not in `references.bib`.

5. **Beal (2003), *Variational Algorithms for Approximate Bayesian Inference*, PhD thesis, Gatsby
   Unit, Ch. 2** — the canonical variational-EM statement: `L(q,θ) = log p(y|θ) - KL(q‖p(x|y,θ))`,
   with the VBEM separation of the E-step (optimize `q` at fixed `θ`) from the M-step (optimize `θ`
   at fixed `q`). Chapters 5's `prop:elbo-exact-e-coordinate` / `prop:elbo-exact-m-coordinate` are
   the measure-theoretically careful version of Beal Ch. 2, and Beal is the natural reference for
   the *block/partial* E-step that `open:elbo-alternating-convergence` leaves open. Not in
   `references.bib`.

6. **Bishop (2006), *PRML*, Ch. 10** (in `references.bib` as `Bishop2006`, uncited in these
   chapters) and **Blei, Kucukelbir, McAuliffe (2017), JASA 112(518):859–877** (in
   `references.bib` as `Blei2017`, uncited in these chapters) — the standard references for the
   mean-field ELBO and the coordinate-ascent updates that `05b:355` and `05b:423` invoke by name
   without citation. Citing them at `05b:355` would also force the factorization hypothesis of V2
   to be displayed.

7. **Heskes (2006), "Convexity arguments for efficient minimization of the Bethe and Kikuchi free
   energies", JAIR 26:153–190** — supplies the conditions under which a counting-number free energy
   is convex, which is the natural follow-up obligation once V1's fix admits negatively weighted
   symmetric splits.

---

## Falsification conditions for this review

- **V1 is wrong** if "symmetric" in `05b:313` is somewhere given a technical definition that
  excludes negative weights on non-incident agents, or if the manuscript elsewhere restricts local
  objectives to graph-local functionals. I searched Chapters 5, 5a, 5b, the notation appendix and
  the claim ledger and found no such definition or restriction; if one exists in a chapter I did
  not read in full, V1 downgrades to "the restriction is stated in the wrong chapter".
- **V2 is wrong** if "mean-field" is defined anywhere in the manuscript to mean full factorization
  of the recognition law over `(Y, J_1, …, J_N)`. It occurs exactly once in my three chapters
  (`05b:355`) and is never defined there; a definition elsewhere downgrades V2 to a missing
  cross-reference. V2 is also wrong if `E_{Q_Y}[TC(Q_{J|Y})]` can be shown to vanish for every
  admissible `Q` in the declared recognition family — but the family is only restricted to `y`-free
  rows, which does not constrain the copula, as case (b) shows.
- **V3 is wrong** if `\mathcal L^{\rm ext}` is defined in a file I did not grep. I grepped every
  `.tex` in `manuscripts/gauge_vfe_rg/`; if the definition lives in an included file outside that
  directory, V3 collapses to a missing cross-reference.
- All "recomputed and found exact" entries are falsified by any concrete model on which the
  residual exceeds `1e-12`. My models were deliberately small, discrete, non-degenerate, and
  correlated; a continuous or heavy-tailed instance could expose an integrability issue that a
  finite model cannot.

## Confidence

**HIGH** for V1 and V2 (both carry explicit numeric counterexamples that satisfy the displayed
hypotheses and violate the displayed conclusions), **HIGH** for V3 as a search result and MEDIUM on
its severity (the intended definition is recoverable), **HIGH** for the kill of candidate #2.
What would shift me on V1: a technical definition of "symmetric" or an explicit locality
restriction elsewhere in the manuscript. What would shift me on V2: a definition of "mean-field"
in the manuscript's own terms.
