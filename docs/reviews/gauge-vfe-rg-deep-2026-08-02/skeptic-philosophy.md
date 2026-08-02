# Adversarial skeptic pass — philosophy lens findings P-1 and P-2

Mandate: refute. Default verdict is REFUTED where evidence is ambiguous. Every claim below is
pinned to `file:line` in `manuscripts/gauge_vfe_rg/` at the working-tree revision of 2026-08-02
(files dated `Aug 1 20:12`), plus git history at `96b7b5f`.

---

## P-1 — "The geometry chapter proves that curved and flat averaged connections are mathematically possible"

### Verdict: **SURVIVES-AS-STATED** (severity **high** upheld), with one sub-claim of the finding **refuted**.

I attacked this on all four requested axes. Three failed outright; the fourth produced a
mitigation, not a refutation. I also found the finding's *provenance paragraph* to be wrong — in a
direction that makes the manuscript look better historically but changes nothing about the current
text.

### Axis 1 — is the supporting result elsewhere under different wording? **No.**

Whole-directory grep, all 24 `.tex` files, case-insensitive `averag`:

```
05b:428, 05d:247, 05d:253      outside-averaged conditional VFE
07b:10, 07b:494, 07b:501       averaged group link / Haar rotation-average counterexample
09:708, 09:710, 09:714, 09:721 Haar orbit average
appendix_notation:112          outside-averaged conditional block VFE
12_philosophy.tex:100          the sentence under attack
```

Zero hits in `02_geometry.tex`. No hit anywhere is a connection. Grep for `partition of unity`,
`subordinate`, `convex combination`, `mixture of connections`, `omega_.*avg`: **no matches
anywhere in the manuscript**. Grep for `curvature` manuscript-wide returns six sites; the only one
in Chapter 2 is `02_geometry.tex:369`:

> "The connections in \eqref{eq:geo-principal-connections} are chosen data; no curvature or
> transport is inferred from the agent frames."

Every other `curvature` hit is a disclaimer (`12:86`, `12:231`, `11:415`) or an unrelated label
(`05d:587`, `11:150`, `05_elbo:514`).

Chapter 2's complete numbered inventory (grep of `*heading{` macros, `02_geometry.tex`):
`def:geo-context-base` (16), `def:geo-principal-systems` (40), `hyp:geo-smooth-tier` (100),
`def:geo-associated-bundles` (117), `def:geo-cross-morphisms` (183),
`prop:geo-intertwining-cross-map` (219), `def:geo-connections` (266), `def:geo-covariant-defects`
(324), `def:geo-agent` (375), `prop:geo-moment-pushforward` (399),
`hyp:geo-common-trivializations` (504), `def:geo-graph-links` (527),
`prop:geo-trivializing-criterion` (559), `hyp:geo-graph-base-transport` (587),
`hyp:geo-flat-links` (608). Fifteen results, none about connection curvature. `def:geo-connections`
(`02:266-280`) *chooses* $\omega_b,\omega_m$ as data.

There is no repairable pointer. "The geometry chapter" is not a loose reference to something that
exists elsewhere; the referent does not exist in the document.

### Axis 2 — does the R17 averaged-connection construction still exist anywhere? **No — and the finding's provenance is wrong in the manuscript's favor.**

I recovered the deletion from git. Commit `96b7b5f` ("manuscript: make gauge VFE RG theory
rigorous", 2026-08-01) removed an entire section `\section{An induced connection from the frames}`
with label `sec:geo-induced-connection`, containing:

- **Definition 2.29** (frame-induced local connection, $u_i^*\omega_i=0$),
- **Proposition 2.30** ($A_i$ is flat),
- **Proposition 2.31** ($A=\sum_i(\chi_i\circ\pi)\omega_i$ over a subordinate partition of unity, plus a sufficient flatness criterion),
- **Proposition 2.32**, tagged `\status{ESTABLISHED}`: *"Local disagreement neither forces nor excludes curvature… local frame-induced connections may disagree while every partition-of-unity average is flat. Conversely, local disagreement can produce a curved average for a specified partition."* with explicit $\GL^{+}(1)$ witnesses — the flat one on $\R$ ($F=-d\chi_2\wedge dx=0$), the curved one on $\R\times(0,1)$ with $a=-y\,dx$, $F=dx\wedge dy\neq0$, and computed holonomy $\operatorname{Hol}_A(\partial R)=e^{-\ell(c-b)}\neq1$.

**This refutes the finding's sentence** "even the deleted proposition did not deliver the *curved*
half." Deleted Proposition 2.32 delivered exactly both halves, with witnesses. The Chapter 12
sentence was accurate when written; it was falsified by the deletion, not by overclaim at the time
of writing. The finding also names the wrong proposition (2.31 gave the *flatness criterion*; 2.32
gave the curved/flat dichotomy).

None of this rescues the manuscript. Grep of the current text for `GL^{+}(1)`, `dx\wedge dy`,
`flat witness`, `curved witness`, `Open 2.16`: **zero hits**. The construction is gone.

Corroborating debris: `02_geometry.tex:263-264` carries **two** `\label`s on one section —

```
\section{Chosen connections, parallel transport, and covariant defects}
\label{sec:geo-three-transports}
\label{sec:geo-induced-connection}
```

`sec:geo-induced-connection` names a section that no longer exists and is referenced by nothing
(`grep -rn "sec:geo-induced-connection" *.tex` returns only the definition line). That is a second,
independent artifact of the same deletion and confirms the provenance chain.

### Axis 3 — is the sentence load-bearing? **Partially — this is the one axis that lands, and it is a mitigation only.**

The sentence is a premise for the conjecture at `12:98-100`. The same conjecture is stated
independently in the ledger at `appendix_claim_ledger.tex:144-148` ("Operational base holonomy
(conjecture): Choose a canonical or empirically specified base connection and construct a
population observable sensitive to its holonomy, or prove that every admissible observable is
insensitive to it. Graph-link holonomy alone does not settle this question."), and that statement
carries **no** averaged-connection premise. So deleting `12:100-102` costs the manuscript nothing:
no theorem, definition, hypothesis, or downstream claim depends on it.

This is why the finding is high and not critical. It is not why it is less than high.

### Axis 4 — is "mathematically possible" so weak as to be harmless? **No.**

Two reasons the attack fails.

1. The load-bearing verb is *proves*, not *possible*. The sentence asserts that **this document**
   contains a proof. It does not. For a manuscript whose entire apparatus is claim-status
   discipline — `SPEC.md:76-77` "A claim with no status is a defect"; `SPEC.md` §2 "A reader must
   be able to tell, at every point, whether they are reading something established… Ambiguity here
   is the worst defect this document can have" — a false internal "X proves Y" is the exact defect
   the apparatus exists to prevent.
2. The predicate is not merely weak, it is **unparseable in this document**. "Averaged connections"
   has no referent anywhere in the manuscript (Axis 1). A reader cannot evaluate the sentence as
   trivially true, because the object it quantifies over is undefined. Compare `appendix_notation`,
   which indexes `averaged` only at line 112, for the outside-averaged conditional block VFE.

One more point the finding understates in the manuscript's disfavor: under `SPEC.md` §2.1 the
`\status{}` macro governs **the statement it follows**, so `\status{CONJECTURE}` at `12:100`
governs the *preceding* sentence ("A separate conjectural route is…"). The sentence at
`12:100-102` therefore carries **no tag at all**, which `SPEC.md:76` calls a defect on its own
terms. The finding's charitable framing ("sits under a CONJECTURE tag") is more generous to the
manuscript than the SPEC allows.

### Decisive evidence

| Assertion | Evidence |
|---|---|
| Chapter 2 proves nothing about averaged connections | `02_geometry.tex`, zero `averag` hits; 15-result inventory contains no curvature result |
| Chapter 2 says the opposite | `02_geometry.tex:369` |
| The construction existed and was deleted | `git show 96b7b5f -- manuscripts/gauge_vfe_rg/02_geometry.tex` — removed Defs/Props 2.29–2.32 and `\section{An induced connection from the frames}` |
| Deletion left debris | orphan `\label{sec:geo-induced-connection}` at `02_geometry.tex:264`, referenced nowhere |
| The finding's provenance sub-claim is wrong | deleted Prop 2.32 *did* deliver the curved half, with $F=dx\wedge dy\neq0$ and $\operatorname{Hol}=e^{-\ell(c-b)}\neq1$ |
| The sentence is untagged | `SPEC.md` §2.1 tag-placement convention + `SPEC.md:76` |

### Correction to the finding (adopt before publishing)

Strike "even the deleted proposition did not deliver the *curved* half" and replace with: "The
deleted **Proposition 2.32** delivered both halves with explicit $\GL^{+}(1)$ witnesses; the
sentence was true when written and was falsified by the removal at `96b7b5f`. The overclaim is
therefore single, not double." The finding's own falsifier — "reinstating a labeled existence
result in Chapter 2 … would refute this" — is now concrete: reinstate Proposition 2.32 verbatim
from `96b7b5f^`, or delete `12:100-102`. Add the orphan `\label` at `02:264` to the fix list.

---

## P-2 — "The open-obligation ledger is incomplete: the RG-monotone obligation is not indexed"

### Verdict: **SURVIVES-AT-LOWER-SEVERITY — LOW.**

The bare omission is real but partially subsumed, is not a defect under the document's own stated
ledger charter, and the argument that made it **high** is false.

### The load-bearing argument is refuted

The finding's "Why it is load-bearing" says:

> "The standard reason to believe an RG map loses information in one direction — data processing —
> is therefore **provably unavailable here and is not replaced**… the ledger nowhere tells a reader
> that the arrow itself is unestablished."

Both halves are false.

**(a) Data processing is available and is used.**
`06_general_coarsegraining.tex:197-221`, `thm:cg-evidence-preserving-channel`, `\status{ESTABLISHED}`:

```
\bar{\mathcal L}^{\rm ext}(\bar Q_o;o) = \log p(o) - KL(Q_oK || P_oK)
                                       >= \log p(o) - KL(Q_o || P_o)   (eq:cg-elbo-monotone)
```

with proof at `06:220-222`: "Absolute continuity and \eqref{eq:cg-elbo-monotone} follow from the
preceding data-processing theorem."

**(b) A monotone for the declared coarse/RG map is ESTABLISHED, not open.**
`07b_agent_network_rg.tex:34-57`, `thm:rg-exact-coarse-vfe`, `\status{ESTABLISHED}` — for the
common Markov coarse channel of `eq:rg-common-pushforward`,

```
F_P(Q_o) = F_{P^c}(Q_o^c) + ∫ KL( Q̂_o(dy|z) || Π̂_o(dy|z) ) Q_o^c(dz)     (eq:rg-vfe-chain-rule)
```

and `07b:53`: "**In particular, the fine VFE is at least the coarse VFE.**" Restated as a flow at
`07b:801-806`, `\status{ESTABLISHED}`:

> "Along every exact coarse path, \eqref{eq:rg-vfe-chain-rule} makes the recognition gap
> nonincreasing and the ELBO nondecreasing at fixed evidence. **This monotone flow is information
> loss under resolution**, not a proof of approach to a nontrivial critical fixed point."

That is an arrow, proved, in the chapter that constructs the agent-network RG. It is exactly the
"exhibiting a Markov kernel whose pushforward realizes the map" route that `08:333-334` names —
discharged for the Markov sector. Settled ground `RG-1` already verified this construction, and
`appendix_claim_ledger.tex:61-62` records it: "The normalized evidence-preserving joint-law
pushforward is now supplied by \Cref{thm:rg-exact-coarse-vfe}."

**(c) The ch-8 OPEN is narrower than the finding represents.** It sits inside
`\section{What is not claimed}` (`sec:ig-notclaimed`, `08:314`) and is scoped by the two sentences
before it: `08:324-325` "No Markov/data-processing monotonicity theorem is asserted for the
**deterministic Galerkin aggregation map**. `\status{NOT-CLAIMED}`" and `08:328-331` "The theorem
does not cover the aggregation operation of the following chapters, because by
\Cref{prop:ig-pullback-vs-pushforward} the coarse operator is a **restriction**…". The manuscript
has two coarse sectors — a Markov pushforward (arrow proved) and a mean-restriction aggregation
(arrow open) — and Chapter 8 exists precisely to keep them apart. The finding's phrase "the RG"
does not denote; it merges the two sectors that the cited proposition separates. That is the
inverse of the conflation `prop:ig-pullback-vs-pushforward` was written to block.

**(d) `12:233-241` does not presume a directed flow.** The protocol reads: "One would fit only at
fine resolution, push the result through each blocking without coarse refitting, and compare the
predicted held-out coarse statistic both with data and across admissible blockings." It requires a
well-defined evidence-preserving blocking **map** — supplied by `thm:rg-exact-coarse-vfe` — and
invokes no monotone, no contraction, and no fixed-point approach. The claim that the test "presumes
a directed flow" is unsupported by the text it cites.

### Partial subsumption under an existing entry

`Lyapunov` occurs exactly three times in the manuscript: `05d:608` (unrelated — a Lyapunov scalar
for a local objective), `08:334` (the obligation), and `appendix_claim_ledger.tex:120`. The ledger
entry reads:

> **Intrinsic scale selection (open).** Find a nondegenerate criterion internal to one fixed
> evidence problem, **or prove endpoint degeneracy for a stated class**. A successful alternative
> may be **a normalized Markov pushforward or a proved Lyapunov functional**; the determinant gap
> and quotient-volume convention do not supply one. `\status{OPEN}`
> — `appendix_claim_ledger.tex:117-121`

Both of `08:333-335`'s named closure routes appear here **verbatim and in the same order**, and
`Lyapunov` has no other plausible source in the document. The ledger author demonstrably wrote this
entry from the Chapter 8 sentence.

The finding's counter — *"A monotone that runs to an endpoint would in fact fail to supply a
nondegenerate selector, so the two obligations… pull in opposite directions"* — misreads the entry.
The entry is a **disjunction**: "Find a nondegenerate criterion … **or prove endpoint degeneracy for
a stated class**." Proving a monotone decreases to an endpoint *is* the second disjunct. The two
obligations are not opposed; they are the two branches of one ledger item. Cross-check
`07_restrictions.tex:322-325`, the body source of the entry, which states the same disjunction
("What would settle the problem positively is a functional … not monotone to an endpoint … A
negative result would have to prove endpoint degeneracy for a precisely stated class").

Subsumption is partial, not total: the ledger entry's *goal* is a scale selector, and a reader
hunting for "does the aggregation map have an arrow?" would have to infer it from the two named
routes. That residue is what keeps the finding alive at all.

### The ledger does not promise per-claim exhaustiveness

- Charter, `appendix_claim_ledger.tex:4-8`: "This appendix collects the manuscript's unresolved
  obligations in one place. It does not upgrade any of them. … **The local theorem statements and
  hypotheses remain authoritative.**" The ledger explicitly defers authority to the body.
- `SPEC.md:98-104`: "The former per-chapter registers are replaced by one compact, **nonduplicative**
  appendix of unresolved obligations. It collects conjectures and open problems **by topic** and
  says what would close each one. … **The obligation ledger is an audit index, not a second
  exposition of the theory**, and it must not duplicate every local result."

By design, 21 topic entries index ~40 body `OPEN`/`CONJECTURE` sites — the finding's own
adversarial self-check documents that many-to-one mapping. "Site X is not indexed 1:1" is therefore
not a defect under the document's own stated standard unless the *topic* is absent. The topic here
(what would supply a monotone/selector for the aggregation map) is present at `ledger:117-121`.

### The three secondary omissions, verified individually

1. **`06_general_coarsegraining.tex:415-417`** — verified present and `\status{OPEN}`: "KL equality
   does not automatically make its Bayes recovery equivariant; an equivariant conditional version
   is an additional hypothesis or theorem, especially for noncompact groups." Ledger coverage:
   *Partition selection and experiment-level recovery* (`ledger:57-64`) names "one common recovery
   kernel for an entire statistical experiment" — the same kernel, a different property. The
   finding is right that "gauge-compatible" attaches grammatically to the **selector**
   (`ledger:63-64`), and that noncompact `G` is unnamed. **Partially unindexed. Low.**
2. **`12_philosophy.tex:136-139`** — verified `\status{OPEN}` on ontic structural realism. Ledger's
   `claim:physical-law-identification` (`ledger:176-182`) disclaims "ontological closure", which is
   indeed a different thesis. But `12:8-9` declares that in this chapter `OPEN` marks "unresolved
   empirical or **interpretive** consequences" — a broader category than "obligation the manuscript
   owes". The manuscript does not owe a proof of OSR; it declines the reading. Requiring this in an
   obligation ledger would import a metaphysical non-commitment into an audit index that `SPEC.md:104`
   says must not duplicate. **Not a ledger defect.**
3. **`10_renormalization.tex:518-521`** — verified `\status{OPEN}`: "A gauge-invariant real-space
   block selector, zero-mode treatment, and entropy normalization remain open." Grep of
   `appendix_claim_ledger.tex` for `zero-mode`, `zero mode`, `entropy`: **zero hits**. The selector
   is indexed; the other two are not, under any wording. **Genuinely unindexed — the cleanest of
   the three. Low.**

### Decisive evidence

| Finding sub-claim | Verdict | Evidence |
|---|---|---|
| Body tags the obligation `OPEN` | correct | `08_infogeometry.tex:331-335` |
| No ledger entry *names* the aggregation monotone | correct | `appendix_claim_ledger.tex`, all 21 entries |
| Not subsumed by an existing entry | **refuted (partial subsumption)** | `ledger:117-121` reproduces both of `08:333-335`'s closure routes verbatim; `Lyapunov` occurs 3× manuscript-wide |
| "The two obligations pull in opposite directions" | **refuted** | `ledger:118` disjunct "or prove endpoint degeneracy for a stated class"; `07_restrictions.tex:322-325` |
| Data processing "provably unavailable … and not replaced" | **refuted** | `06:207-221` `eq:cg-elbo-monotone` ESTABLISHED, proved *from* data processing |
| "the RG [has] no established arrow" | **refuted** | `07b:34-57` `thm:rg-exact-coarse-vfe` ESTABLISHED; `07b:53` "the fine VFE is at least the coarse VFE"; `07b:801-806` "This monotone flow is information loss under resolution. `\status{ESTABLISHED}`" |
| `12:233-241` presumes a directed flow | **refuted** | protocol at `12:236-241` needs only an evidence-preserving blocking map |
| Ledger charter promises exhaustiveness | **refuted** | `ledger:7-8` defers to body; `SPEC.md:100-104` "audit index", "by topic", "nonduplicative" |
| `06:415-417` unindexed | partially correct | `ledger:57-64` covers the kernel, not its equivariance |
| `12:137-139` unindexed | correct but not a defect | `12:8-9` scope of `OPEN` in this chapter |
| `10:518-521` zero-mode/entropy unindexed | **correct** | zero hits for `zero-mode`/`entropy` in the ledger |

### What is left, at LOW

Three sub-obligations are not named in the ledger — the aggregation-map monotone (by name; its two
closure routes *are* there), equivariant Bayes recovery under noncompact `G`, and zero-mode
treatment plus entropy normalization. All three are visible as `\status{OPEN}` in the body. The
recommended repair is the finding's own: add one line each. The recommended demotion is from
**high** to **low**, and the recommended deletion is the entire "Why it is load-bearing" paragraph,
which asserts a state of affairs (`no established arrow`) that `07b:34-57` and `07b:801-806`
contradict with an `ESTABLISHED` theorem. A reviewer who wants a floor of **medium** can rest it on
the charter sentence at `ledger:4` read as an exhaustiveness promise; that reading is undercut by
`ledger:7-8` and `SPEC.md:104` and I do not endorse it.
