# Adversarial adjudication of RG-F2 and RG-F3

Role: skeptic. Mandate: refute or downgrade. Default to REFUTED under uncertainty.
Target: `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex` at working-tree revision of
2026-08-02 (HEAD `11bd0e8`, file clean, `git status --porcelain` empty for that path).
Recomputation: `C:/Users/CHRISA~1/AppData/Local/Temp/claude/C--Users-chris-and-christine-Desktop-Research/21b92b09-6f32-47fa-8f90-6f5faa59e5a3/scratchpad/skeptic_f2f3.py`,
interpreter `C:/Python314/python.exe`, numpy, seed 20260802. Every residual below is machine
output from that script, run by me, not quoted from `lens-rg.md`.

---

## Verdicts

| Finding | Raised at | Verdict |
|---|---|---|
| **RG-F2** — fixed-point dichotomy; "Exhaustive" is status inflation | HIGH | **REFUTED** |
| **RG-F3** — `c_b` forced to zero; unstated cocycle | MEDIUM-HIGH | **REFUTED** (one detachable LOW notation fragment survives and belongs to RG-F7) |

Both findings are **mathematically correct and reproduce exactly**. Neither identifies a defect
in the manuscript. RG-F2's headline charge collides with a settled ledger item and misreads the
theorem title. RG-F3's headline charge is stated in the manuscript's own printed proof.

---

## Freshness gate (applies to both)

`00-settled-ground.md:3-5` permits re-raising settled material only if "the manuscript text
touching it has changed since the recorded revision, in which case say so explicitly and give
the diff." I ran the diff.

```
$ git diff -U0 a997a60 HEAD -- manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex | grep "^@@"
@@ -552 +552 @@
@@ -555,5 +555,8 @@
```

Two hunks, both in `sec:rg-path-space` (the section retitled from "Dynamic closure lives on path
space" to "Ordered-path closure and memory"). Lines 599-848 — the RG transformation, the beta
functionals, `thm:rg-fixed-point-equations`, `eq:rg-fixed-action-ray`, the linearization, and the
closure theorem — are byte-identical to the text on which RG-2 was closed, modulo a three-line
offset. **The settled-ground exception does not open.**

(Note for the record: the ledger's `artifact_revision` `git:e4377537…` is the commit
`docs: record gauge VFE live WIP reconciliation`, at which `07b_agent_network_rg.tex` was not yet
tracked — `git ls-tree -r e4377537` shows no `07b`. The file entered git at `a997a60`. The pin is
therefore a docs-commit pin over a live WIP, not a content hash of the `.tex`. This is a
provenance weakness in the ledger, not a licence to re-litigate: the two-hunk diff above pins the
content directly and shows the verified text intact.)

---

# RG-F2 — REFUTED

## 1. The collision with RG-2 is real and decisive

`00-settled-ground.md:95-96` paraphrases RG-2 as "exhaustive invariant measures". The ledger's
actual statement (`.verification/local-global-rg-ledger.json`, claim `RG-2`, state
`EVIDENCE_VERIFIED`, severity high, `open_obligations: []`, `counterevidence: []`) reads:

> "Under the displayed equivariance, integrability, positivity, lumpability-or-path-space, and
> semigroup hypotheses, the construction supplies composable gauge-covariant cross-scale
> operators, exact meta-attention, reference-dependent action and attention beta functions, and
> **exhaustive invariant measure-pair fixed-point equations**."

Evidence `RG-2-e1` is `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex:243-804` — a range that
contains `thm:rg-fixed-point-equations` (712-747), `eq:rg-fixed-action-ray` (729-731), the sector
list (779-799), and the "not a proof of approach to a nontrivial critical fixed point" disclaimer
(801-806). The adversarial candidate that lost both orderings was `RG-2-obstruction`: "The
strongest covariance, averaging, memory, moving-reference, or **fixed-point objection**."

RG-F2 is a fixed-point objection to the exhaustiveness of the measure-pair fixed-point equations,
raised against unchanged text, inside the exact evidence range of a closed high-severity ledger
item whose losing candidate was defined as that objection. **Out of bounds.**

## 2. "Exhaustive" is exhaustive over the *equations*, and the equations are exhaustive

RG-F2 charges that "Exhaustive" in the title inflates status. Read the theorem
(`07b:712-724`):

> "**A normalized fixed theory is exactly a rescaled invariant pair** `R_b(ρ_*,m_*)=(ρ_*,m_*)`
> for every declared `b`. **On the dominated normalized tier this is equivalent to the
> conjunction** `R_b^ρ ρ_* = ρ_*`, `R_b^H[H_*;ρ_*] = H_*`, almost everywhere with respect to the
> fixed reference."

"Exhaustive" modifies "fixed-point equations": the claim is that these equations capture *every*
fixed theory — a necessary-and-sufficient characterization. It is not a claim to have enumerated
the solutions, and the very next paragraph says so in as many words (`07b:779-780`):

> "The equations characterize all fixed points **without claiming that every model class admits a
> closed-form enumeration.**"

The characterization is what the proof proves, and it holds. Direct test of the biconditional on
2000 random `(K, H)` draws — the pair equation `R_b(ρ,m)=(ρ,m)` and the conjunction
`{ρK=ρ, R^H[H;ρ]=H}` are checked independently and compared for joint vanishing:

```
iff-agreement failures over 2000 random (K,H) draws : 0.0
```

Zero failures in either direction. RG-F2 does not exhibit a fixed theory outside the equations —
it cannot, because the equations are an identity — so the exhaustiveness charge has no target.

The subsidiary jab, that the proof (`07b:740-747`) is "a definitional restatement plus one
Radon-Nikodym line," describes the proof accurately and mistakes accuracy for a defect. An
equivalence theorem of this shape *is* proved by unfolding the definition of invariance and taking
one Radon-Nikodym derivative. A proof that is short and correct is not a proof that is incomplete.
The review's own scope rule (`00-settled-ground.md:131-135`) admits proofs that are "wrong,
circular, incomplete"; brevity is on none of those lists.

## 3. "No isolated, no hyperbolic fixed point" attacks vocabulary the manuscript does not use

Whole-manuscript greps over `manuscripts/gauge_vfe_rg/*.tex`:

- `hyperbolic` — **zero occurrences anywhere in the manuscript.**
- `isolated` in `07b` — exactly two occurrences, `07b:771` ("isolated eigenoperator") and
  `07b:775` ("isolated point spectrum"). Both are properties of the *spectrum* of
  `D_H R_b^H`, not of the fixed point. Neither asserts that a fixed point is isolated in the
  fixed-point set.
- `ergodic`, `irreducible`, `reducible` — **zero occurrences anywhere in the manuscript.**

The last one is the load-bearing observation. RG-F2's dichotomy is "either `K_b` is uniquely
ergodic (then `H_*` is constant) or `K_b` is reducible (then the fixed set is a simplex)." The
manuscript imposes **no ergodicity or irreducibility hypothesis on `K_b` at all**. Both horns are
therefore already inside its declared hypothesis set, and the theorem — a characterization valid
for every `K_b` — is correct on both. A dichotomy that partitions the manuscript's own hypothesis
class, with the theorem true on each part, is not a counterexample to the theorem.

Further, the manuscript's *first named example* is the maximally reducible horn (`07b:781`):

> "The identity channel fixes every law."

That is an infinite-dimensional fixed simplex with `λ = 1` of full multiplicity, named, in the
text, immediately after the theorem. RG-F2 quotes this line itself and then classifies it away as
"degenerate" — but the manuscript never claimed a nondegenerate-channel nontrivial fixed point.
It claimed the opposite (`07b:801-806`):

> "This monotone flow is information loss under resolution, **not a proof of approach to a
> nontrivial critical fixed point.** Attraction requires spectral control of
> \eqref{eq:rg-linearized-action} on the declared common space."

And `07b:792-799` adds a paragraph of qualifications whose stated purpose is "prevent an invariant
form from being mislabeled as a complete fixed theory."

## 4. Recomputation — the dichotomy reproduces, and confirms nothing is broken

Irreducible branch (`n = 6`, random Markov `K_b`):

```
dim(invariant simplex)  : 1
||rho_* K - rho_*||     : 1.11e-16
||m_*/Z - rho_*||_max   : 0.0
H_*                     : [0 0 0 0 0 0]   spread: 0.0
||R^H[H_*] - H_*||      : 0.0
```

Reducible branch (block-diagonal `K_b`, two classes of size 3, reference
`ρ_* = (½p₁, ½p₂)` held fixed, `m_*` swept):

```
dim(invariant simplex)  : 2
||rho_* K - rho_*||     : 5.55e-17
theta=0.25  H_* = [ 0.6931  0.6931  0.6931 -0.4055 -0.4055 -0.4055]  ||R^H[H_*]-H_*|| = 1.665e-16
theta=0.50  H_* = [ 0      0       0       0       0       0     ]  ||R^H[H_*]-H_*|| = 0.000e+00
theta=0.75  H_* = [-0.4055 -0.4055 -0.4055  0.6931  0.6931  0.6931]  ||R^H[H_*]-H_*|| = 1.665e-16
row sums of D_H R^H     : [1 1 1 1 1 1]
eigenvalues             : -0.0545, 0.0856+/-0.1392i, 0.2640, 1.0000, 1.0000
multiplicity of 1       : 2
```

Independently reproduced (my own block construction and seed, not the lens's). The one-parameter
family exists, the residuals are at machine epsilon, and `λ = 1` has multiplicity 2. **Every
number in RG-F2 is right.** None of them contradicts a sentence in the manuscript.

A one-parameter fixed family under a reducible kernel is the expected structure of the solution
set of a *linear* invariance equation: `{(ρ,m) : ρK=ρ, mK=m}` is a convex set, and its dimension
is the number of ergodic classes. Calling that a defect would make the Perron–Frobenius theorem a
defect. A `λ = 1` direction along the family is *marginal*, which is one of the three outcomes
`07b:772-774` explicitly provides for.

One technical correction to RG-F2's own statement (iii), which claims "every point of that simplex
is another fixed pair with finite-valued action": the **extreme** points of the simplex have
`dπ_*/dρ_* = 0` off their ergodic class, so `H_* = +∞` there and they are excluded by the
finite-valued action space at `07b:749-750`. Only the relative interior gives finite `H_*`. The
dimension conclusion survives; the quantifier as printed does not.

## 5. What is left

The dichotomy is a true proposition that the manuscript does not state. Adding it as a remark
after `thm:rg-fixed-point-equations` would be an improvement to the exposition. That is an
**enhancement, not a finding**: it does not make a proof wrong, circular, or incomplete; it does
not use an undefined symbol; it does not create an internal inconsistency; and it does not inflate
status, because the manuscript's status tag covers exactly the characterization it proves. Under
`00-settled-ground.md:131-135` an enhancement of this kind is out of scope, and under RG-2 the
underlying claim is closed.

**RG-F2: REFUTED.** Recommend it be recorded as a non-defect enhancement note, not carried at HIGH
or at any severity.

---

# RG-F3 — REFUTED

## 1. The crux: is `Z = e^{-c_b} Z` valid, or does `Z` get rescaled away?

The brief asks whether the normalizer is rescaled at each step so the constant is absorbed. It is
not. Read the definition verbatim (`07b:627-631`, `eq:rg-reference-dependent-action-map`):

```latex
\mathcal R_b^H[H;\rho]
:=-\log\frac{d\bigl((e^{-H}\rho)K_b\bigr)}
{d(\rho K_b)}.
```

There is **no renormalization of the numerator measure**. `(e^{-H}ρ)K_b` is pushed forward as an
unnormalized submeasure; only the reference in the denominator is a probability. So total mass is
tracked through the step, and the argument runs: `ρ_*K_b = ρ_*` plus
`R_b^H[H_*;ρ_*] = H_* + c_b` gives `d(m_*K_b)/dρ_* = e^{-c_b} dm_*/dρ_*`, hence
`m_*K_b = e^{-c_b}m_*`, hence `Z = e^{-c_b}Z` for Markov `K_b`, hence `c_b = 0` when `0 < Z < ∞`.
`positive finite evidence` is indeed a standing hypothesis — `07b:815`, inside
`thm:rg-complete-effective-theory`'s hypothesis list.

Reproduced:

```
mass of m_*        : 1.0
mass of m_* K_b    : 1.0
c_b =  0.0 : ||R^H[H_*] - (H_* + c_b)||_max = 1.665e-16
c_b =  0.3 : ||R^H[H_*] - (H_* + c_b)||_max = 3.000e-01
c_b = -0.3 : ||R^H[H_*] - (H_* + c_b)||_max = 3.000e-01
```

**RG-F3's mathematics is valid.** The step survives my attempt to break it. It also survives the
mass-rescaling escape: with `K_b → s K_b` (a non-Markov `I_b` scaling all mass by `s = 3.7`),
numerator and denominator scale together and the action map is unchanged, residual `1.665e-16`.
And the sub-Markov escape fails for a different reason: `K = 0.6 P` gives
`||ρ_*K - ρ_*||_max = 0.1106`, breaking the *first* component of `eq:rg-fixed-action` before
`c_b` is ever reached.

So the finding's derivation is correct. That is not the question. The question is whether the
manuscript failed to say it.

## 2. The manuscript says it — twice, including in the proof

`07b:733-734`, the sentence RG-F3 quotes as the offending text:

> "It represents the normalized pair in \eqref{eq:rg-fixed-measure-pair} only when the reference
> is also invariant **and normalization fixes `c_b = 0`**."

The verb is *fixes*: normalization **determines** `c_b = 0`. The sentence names normalization as
the mechanism that pins the constant. RG-F3 reads it as a side condition listed alongside
reference invariance and charges that it is really a consequence — but "normalization fixes
`c_b = 0`" already asserts that it is a consequence *of normalization*. That is the finding's own
thesis, printed in the text it attacks.

`07b:744-746`, the proof paragraph:

> "Quotienting by the action's additive gauge gives \eqref{eq:rg-fixed-action-ray}, but
> **restoring the tracked evidence mass removes that freedom.**"

"Restoring the tracked evidence mass removes that freedom" is the mass-conservation argument in
one clause. RG-F3's proposed replacement text reads "mass conservation forces `c_b = 0`, so the
ray equation is not weaker" — a paraphrase of the sentence already in the proof. **The charge of
status inflation fails: the prose asserts exactly what the mathematics licenses and no more.**

## 3. "Weaker is not weaker" is wrong in the sector the manuscript declares

RG-F3 concludes: "the 'weaker fixed-ray equation' is **not weaker**: it has exactly the same
solution set as `eq:rg-fixed-action` under the chapter's own standing hypotheses." Two problems.

First, logical strength is not solution-set inhabitation. `∃c : R[H] = H + c` is a weaker
predicate on `H` than `R[H] = H` whether or not the extra solutions happen to be inhabited. The
manuscript's word "weaker" describes the quantifier structure, which is correct as printed.

Second, and decisively, the manuscript states the ray equation *in a declared sector where the
mass is not tracked*, and in that sector the solution sets genuinely differ. `07b:726-728`:
"**If the evidence mass is discarded** and actions are considered only projectively, the weaker
fixed-ray equation is …". And `07b:641-643`: "**If the evidence mass is deliberately forgotten**
and finite unnormalized actions are quotiented by additive constants, the same formula is
interpreted in that quotient." With the mass discarded, `m_*` is a ray, `m_*K_b = e^{-c_b}m_*` is
a genuine eigenmeasure equation, and `c_b ≠ 0` is realizable. Explicit witness, biased walk on `Z`
with `p = 0.3`, `q = 0.7`, `m(x) = 2^x`:

```
m K = theta m,  theta = 1.550000
||mK - theta m||_rel (interior) : 0.0
c_b = -log theta = -0.4382549309
total mass Z = infinity
```

Exact eigenmeasure, exact nonzero `c_b`, `Z = ∞`. The ray equation admits solutions the normalized
equation does not, precisely when the mass is untracked — which is precisely the condition under
which the manuscript introduces it. RG-F3 computes its `c_b = 0.3` counterexample in the
**normalized** setting, the setting the manuscript already says forces `c_b = 0`, and reports the
expected `3.00e-01` residual as a discovery.

RG-F3 does concede in passing that "a nonzero `c_b` requires `Z ∈ {0, ∞}`", then treats that as an
excursion into the OPEN infinite-volume sector rather than as what it is: the demonstration that
the manuscript's "weaker" is the correct word.

## 4. The cocycle is implied, not missing

The shift-equivariance that drives it reproduces exactly:

```
R^H[H + c] = R^H[H] + c    residual : 2.220e-16   (c = 1.7)
```

so at a fixed ray with invariant reference, `eq:rg-kernel-semigroup` (`07b:607-610`,
`K_{b₁b₂} = K_{b₁}K_{b₂}`) forces `c_{b₁b₂} = c_{b₁} + c_{b₂}`, hence `c_b = γ log b` for
measurable solutions. The mathematics is right.

It is not an "unstated hypothesis." It is a *consequence* of two displayed hypotheses. A condition
entailed by the hypotheses already on the page is redundant, not missing; stating it would be an
addition, not a repair. And in the sector the chapter actually works in, `c_b ≡ 0` satisfies the
cocycle trivially, so the omission is inert. The interesting object RG-F3 names — `γ`, the
free-energy-density beta — lives in the infinite-volume sector that `appendix_claim_ledger.tex`
declares OPEN and that `00-settled-ground.md:120-129` lists as out of scope
("infinite-volume RG limit").

## 5. The one fragment that survives

The `c_b` symbol collision is real. My own grep over `manuscripts/gauge_vfe_rg/*.tex` returns
exactly two occurrences of the glyph:

- `07b_agent_network_rg.tex:730` — `\mathcal R_b^H[H_*;\rho_*]=H_*+c_b` (additive action
  normalizer).
- `10_renormalization.tex:160` — "If a typical coarse cut contains `\(c_b\asymp b^s\)` fine
  edges" (a count of fine edges).

Same glyph, same subscript, and the subscript carries the same meaning in both places — `10:144`
fixes `b` as the block size ("equal blocks of size `b`"), which is the same `b` as `07b:602`
("Let `b>1` label one blocking ratio"). This is **not** a different subscript, and the collision is
verified.

But it is a notation defect of LOW severity, it is not what RG-F3 is about, and `lens-rg.md`
already carries it as a bullet inside RG-F7 (`lens-rg.md:466-467`). Inside RG-F3 it is a
duplicate. It should be recorded once, under RG-F7.

**RG-F3: REFUTED** as a MEDIUM-HIGH finding. Both halves of its title fail — `c_b = 0` is not
unstated (`07b:733-734`, `07b:744-746`), and the cocycle is entailed rather than missing. The
detachable LOW notation fragment (`c_b` collision, `07b:730` vs `10:160`) is verified and belongs
to RG-F7.

---

## Adversarial self-tests I ran against my own refutations

- **Tried to make "Exhaustive" mean "here is the complete list of fixed measures."** If it did,
  RG-F2 would land. It does not: the ledger statement is "exhaustive invariant measure-pair
  fixed-point **equations**", the theorem body is an equivalence, and `07b:779-780` explicitly
  disclaims enumeration. Three independent readings agree.
- **Tried to find a manuscript claim of isolation, hyperbolicity, or an existing nontrivial
  critical fixed point.** Greps return zero for `hyperbolic`, zero for `ergodic`/`irreducible`/
  `reducible`, and the only two `isolated` in `07b` are spectral. `07b:801-806` denies the
  existence claim outright.
- **Tried to make the `Z = e^{-c_b}Z` step fail** so RG-F3's math would be wrong (which would have
  been a different kind of finding). It does not fail: the action map carries no renormalization
  (`07b:629-630`), uniform mass rescaling cancels (`1.665e-16`), and sub-Markov `K` breaks the
  reference-invariance component first (`0.1106`).
- **Tried to make the ray equation genuinely equivalent to the normalized equation in all
  sectors**, which would have vindicated "not weaker." It is not: the `Z = ∞` eigenmeasure witness
  gives an exact `c_b = -0.4383` solution with residual `0.0`.
- **Tried the freshness escape**, that the verified text has moved since RG-2 closed. It has not:
  two hunks, both at 552-562, none in 599-848.
- **Checked whether either finding is rescued by the OPEN-obligation carve-out.** No: neither
  finding attacks an item the appendix declares open; both attack `ESTABLISHED` text that is
  correct as printed.

## Files

- This adjudication.
- Recomputation: `C:/Users/CHRISA~1/AppData/Local/Temp/claude/C--Users-chris-and-christine-Desktop-Research/21b92b09-6f32-47fa-8f90-6f5faa59e5a3/scratchpad/skeptic_f2f3.py`
  (`C:/Python314/python.exe`, numpy, seed 20260802; checks 1-5).
