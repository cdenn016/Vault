# Adversarial skeptic — variational/ELBO lens findings V1 and V2

**Target:** `manuscripts/gauge_vfe_rg/05b_local_collective_elbo.tex`
**Findings adjudicated:** V1 (`05b:313-315`), V2 (`prop:obs-attention-elbo`, `05b:355`)
**Recomputation:** `C:/Python314/python.exe` (numpy 2.4.4), scripts
`<scratchpad>/v1_attack.py`, `<scratchpad>/v2_attack.py`. All residuals below are verbatim
run output.
**Primary canon retrieved and read:** Yedidia–Freeman–Weiss, MERL TR2004-040 (= IEEE Trans.
Inform. Theory 51(7):2282–2312), Sec. IV-A, pp. 6–7 of the TR, text extracted locally with
`pypdf`; Blei–Kucukelbir–McAuliffe (2017) §2.3 via ar5iv.

---

## VERDICT V1 — **REFUTED**

The arithmetic in V1 is correct and I reproduced it. The finding still fails, because its
witness is not a member of the class the sentence quantifies over, and no member of that class
can ever be a witness.

### 1. The manuscript fixes the class one sentence earlier, and restates it three more times

`05b:311-313`, immediately before the attacked sentence:

> By contrast, a coordinate-local objective contains every incident factor, so summing it over
> agents counts factor $a$ exactly $|\partial a|$ times.

The clause "counts factor $a$ **exactly** $|\partial a|$ times" is not decoration: it is only
true if a coordinate-local objective contains its incident factors **and no others**. So the
sentence preceding the target defines the class extensionally — own relative entropy plus the
incident factor energies, each once. The anaphoric "local objectives" at `05b:313` is
co-referential with "a coordinate-local objective" at `05b:311`; reading it as a wider class is
what manufactures the non-sequitur V1 charges.

Three independent restatements confirm the co-reference:

- `05b:282-285` (figure caption): "A block-local VFE contains every factor **incident** to the
  block. The factor $o_b$ crosses the boundary and therefore enters the block conditional;
  $o_a$ is **outside and cancels**."
- `appendix_notation.tex:153-156`, the registered meaning of $E_{a,o}$: "One actual record is
  one global factor. It may occur in several **incident** coordinate-local VFEs without being
  duplicated in the joint."
- `01_introduction.tex:83-84`, the chapter's own summary of this result: "The local objectives
  do not sum symmetrically because shared factors occur in every **incident coordinate
  objective**."

And the construction itself: `eq:obs-block-incident-energy` (`05b:142-148`) builds
$H_{B,o}$ from $\mathcal A_B=\{a:\partial a\cap B\ne\varnothing\}$ only, and the proof at
`05b:192` states "Factors disjoint from $B$ are constant as functions of $y_B$ and cancel from
the posterior conditional."

V1's witness charges agent 0 a weight $-1$ on factor $b=\{1,2,4\}$ and $-1/3$ on factor
$c=\{2,3\}$ — a factor two hops away whose scope agent 0 never meets. Measured:

```
=== C. the witness is NOT local: agent 0 reads factor c = {2,3}, two hops away ===
  d F_0^count / d eta_3 = [ 0.10774484 -0.10774484]   (agent 0 shares NO factor with agent 3)
  d F_0^count / d eta_2 = [-0.00822169  0.07471829 -0.0664966 ]
  w_counting(0, c={2,3}) = -0.333333, w_counting(0, b={1,2,4}) = -1.000000
```

Under the manuscript's construction agent 0's objective is exactly independent of $\eta_2,\eta_3$.
The witness is not a local objective by the chapter's own operative meaning of the word.

### 2. Structure theorem: **every** witness contains the entire collective VFE

This removes the argument from any particular weight rule. Let $\{F_i\}$ be real functionals on
a connected open recognition-parameter domain with (i) $\sum_i F_i=\Fenergy_o$ and
(ii) $\partial_{\eta_i}F_i=\partial_{\eta_i}\Fenergy_o$ for every $i$. Put
$h_i:=F_i-\Fenergy_o$. Then (ii) gives $\partial_{\eta_i}h_i\equiv0$, so $h_i$ is free of
$\eta_i$, and (i) gives $\sum_i h_i=-(N-1)\Fenergy_o$. Hence

$$F_i=\Fenergy_o+h_i(\eta_{-i}).$$

Every admissible "local objective" is the **collective** VFE plus a correction free of the
agent's own coordinates. It therefore reads every agent's recognition state in the network.
There is no local witness, for any weight rule, on any hypergraph. Existence of the family at
all is equivalent to the vanishing of the $N$-fold mixed derivative
$\partial_{\eta_1}\cdots\partial_{\eta_N}\Fenergy_o$ (necessity is immediate since each $h_i$
omits one coordinate; sufficiency is the ANOVA decomposition on a product domain) — which is
why V1 itself must concede the claim is true when some factor has global scope $|\partial a|=N$.

Verified numerically — $F_i-\Fenergy_o$ is constant along $\eta_i$ to machine epsilon for all
five agents:

```
=== D. structure theorem: any valid witness equals F_o + h_i(eta_{-i}) ===
  agent 0: F_i - F_o over 6 random eta_0 : spread =  8.882e-16
  agent 1: spread =  4.441e-16    agent 2: spread =  1.110e-15
  agent 3: spread =  4.441e-16    agent 4: spread =  3.331e-16
```

### 3. The witness "adds to the collective VFE" only on the mean-field slice

`thm:obs-collective-vfe` (`05b:104-117`) defines $\Fenergy_o$ for **every** $Q\ll P_0$, and
`eq:obs-global-ledger` (`05b:299-305`) carries the live $\operatorname{TC}(Q)$ term precisely
because $Q$ need not be a product. V1 evaluates its witness "on a product recognition family with
softmax coordinates", where $\operatorname{TC}\equiv0$. Off that slice both required properties
fail:

```
=== E. 'adds to the collective VFE' fails off the product family ===
  correlated Q:  TC(Q) = 0.504756489291
  sum_i F_i - F_o = -5.047564892910e-01   vs  -TC(Q) = -5.047564892910e-01
  residual of (sum_i F_i - F_o) + TC(Q) =  2.220e-16
```

`thm:obs-local-global-potential` (`05b:206-234`) states its unilateral property for an arbitrary
replacement of the recognition **conditional** $r_B(\cdot\given b)$ at fixed outside marginal —
not for moves confined to a product family. On exactly such a move the witness fails derivative
matching while the manuscript's own outside-averaged local VFE reproduces it:

```
=== F. unilateral move of agent 0's conditional r_0(.|y_-0) at fixed outside marginal ===
  outside marginal unchanged along the path: max drift = 1.39e-17
  d/dt F_o = -0.018291672   d/dt F_0^count =  0.002165335   MISMATCH =  0.020457
  d/dt of the MANUSCRIPT's outside-averaged local VFE = -0.018291672  (matches to 5.55e-12)
```

So the witness reproduces "every unilateral derivative" only in a strictly smaller move space
than the one `thm:obs-local-global-potential` quantifies over.

### 4. The allocation is not forced — the escape clause at `05b:315-318` applies verbatim

V1 asserts the weights are "forced" and therefore that the manuscript's own escape clause
("the result depends on the order or allocation") is inapplicable. That is false. Summation
pins only $\sum_{i\notin\partial a}w_{i,a}=1-|\partial a|$, leaving an affine family of
dimension $N-|\partial a|-1$ per factor. Uniformity among non-incident agents is a declared
allocation, not a consequence: the automorphism group of the manuscript's own hypergraph
(edges $\{1,2\},\{2,3,5\},\{3,4\}$) is generated by $(1\,4)(2\,3)$ and has trivial stabilizer of
$\{1,2\}$, so equivariance relates weights across factors and forces nothing within a factor.
A second, visibly different valid rule passes both tests:

```
=== B. the allocation is NOT forced: a second, different valid rule ===
  counting-number (skewed)  sum_i F_i - F_o = 4.44e-16   max|d_eta F_i - d_eta F_o| = 6.66e-11
  uniform-share weights w[i][a]:      skewed weights w[i][a]:
   [[ 1.  -1.  -0.3333]                [[ 1. -2. -1.]
    [ 1.   1.  -0.3333]                 [ 1.  1.  0.]
    [-0.3333  1.   1.  ]                [-1.  1.  1.]
    [-0.3333 -1.   1.  ]                [ 0.  0.  1.]
    [-0.3333  1.  -0.3333]]             [ 0.  1.  0.]]
  max |wA - wB| = 1.0000  (two distinct witnesses, both valid)
```

The second limb of the clause — "and is **not** the symmetric local VFE of
`thm:obs-local-multiagent-elbo`" — holds unconditionally for both witnesses. The framing
sentence at `05b:10-12` says "not summands of a **canonical** symmetric decomposition"; a
continuum of valid allocations is exactly non-canonicity.

### 5. The cited canon classifies V1's witness as non-local, and does not supply an exact split

I retrieved YFW and read Sec. IV-A rather than relying on the excerpt in the lens file. Three
mismatches, all verbatim from the primary source:

- **Regions must contain the factors they count.** "We define a region $R$ of a factor graph to
  be a set $V_R$ of variable nodes and a set $A_R$ of factor nodes, such that if a factor node
  $a$ belongs to $A_R$, all the variable nodes neighboring $a$ are in $V_R$." The validity
  condition (29) is $\sum_R c_R I_{A_R}(a)=\sum_R c_R I_{V_R}(i)=1$, a sum over regions
  **containing** $a$. In V1's witness, agent $i$ carries factor $a$ with $w_{i,a}\ne0$ while
  $i\notin\partial a$; as a YFW region, agent $i$'s region must then contain $\partial a$ for
  every weighted factor, which on the manuscript's hypergraph is all of $V$. Each "local
  objective" is the full-graph region. The canon the finding invokes places its witness outside
  the local class. YFW's negative counting numbers attach to **overlap** regions — subsets of
  the large regions, containing the shared nodes — never to a region excluding them.
- **One counting-number set, not two.** V1 weights the energies by $w_{i,a}$ and the relative
  entropies by $\delta_{ik}$. YFW: "we could generalize these approximations by allowing for
  different counting numbers for the average energy and entropy ... In this paper, we will
  always assume just one set of counting numbers." The two-set variant is fractional BP /
  convexified Bethe, not the construction cited.
- **Region-based free energies are approximations.** YFW Prop. 1 gives exactness of the average
  energy only; "the region-based entropy ... will typically only be an approximation even if the
  beliefs $b_R(x_R)$ are exactly equal to the true marginal probabilities." The canon supplies
  no exact additive split of a variational free energy. V1 obtains exactness solely by working
  where the joint entropy equals the sum of marginal entropies — the product family of §3.

YFW also state, of valid region/counting-number choices, "There are in fact an infinite number
of ways to do that" — canonical support for `05b:315-318`, against V1.

Incidental reliability note: the lens file states `Yedidia2005` is "Not currently in
`references.bib`". It is, at `manuscripts/references.bib:4130`, and `gauge_vfe_rg/main.tex:156`
loads that file.

### 6. The witness is not a free energy, so it is not the chapter's kind of object

`thm:obs-local-multiagent-elbo` (`05b:187-189`) makes the chapter's local objects ELBOs:
"$-\Fenergy_{B,o}$ is a local multi-agent ELBO on the conditional log evidence $\log Z_B(b)$."
LG-1 in `00-settled-ground.md` records this as settled: "every agent or block has an exact
conditional ELBO whose unilateral differences equal the collective VFE differences." The witness
is not an ELBO on anything the chapter defines:

```
=== G. -F_i is not an ELBO on anything the chapter defines ===
  inf over product family of F_0^count  ~ -3.658609325
  -log Z(o) = min_Q F_o(Q)               = -0.887111934
  => -F_0^count exceeds log Z(o) by      =  2.771497391 > 0
```

### What I grant

The arithmetic replicates on the manuscript's own figure hypergraph:

```
=== A. manuscript figure hypergraph, scopes [(0,1),(1,2,4),(2,3)], dims [3,2,3,2,3] ===
  counting-number   sum_i F_i - F_o =  2.22e-16   max|d_eta F_i - d_eta F_o| = 2.78e-11
  incident-only     sum_i F_i - F_o =  6.12e-01   max|d_eta F_i - d_eta F_o| = 2.78e-11
  1/|scope|         sum_i F_i - F_o =  2.22e-16   max|d_eta F_i - d_eta F_o| = 1.81e-01
```

So on a product recognition family with no globally scoped factor there exist non-local
functionals that sum to $\Fenergy_o$ and match own-coordinate derivatives. Nothing in
`05b:308-318` denies that; `05b:315-318` names the mechanism and says why it is not the object
under discussion.

### Residue

One optional word: `05b:313` could read "A symmetric set of **coordinate-local** objectives",
reusing the adjective already present at `05b:311`, for a reader who lifts the sentence out of
its paragraph. That is an editorial tightening of a true sentence, not the filed finding
("false as stated", "status inflation", high). The proposed rewrite in the lens file would be a
downgrade: it replaces a claim about the chapter's own objects with a hedged paragraph about
region-based approximations that the chapter does not use.

---

## VERDICT V2 — **REFUTED**

The algebra in V2 is correct and I reproduced it independently. The finding fails on its own
stated falsification condition: "mean-field" carries factorization, in this manuscript and in
the canon it cites.

### 1. The manuscript uses "mean-field" to mean a factorizing recognition family

`11_obstructions.tex:206-207`, the only other occurrence in the manuscript:

> **The exact mean-field coordinate is precision addition.** Under a mean-field recognition
> family **factorizing over $b$ and the constituents**, the optimal factor for $b$ at fixed
> remaining factors is Gaussian with precision ...

The participial phrase is appositive, not contrastive. The manuscript never applies "mean-field"
to a correlated family. That is the definition V2 says it searched for and did not find; V2's own
falsification condition ("V2 is wrong if 'mean-field' is defined anywhere in the manuscript to
mean full factorization") is met.

### 2. The same chapter declares the family the attention rows live in

`05b:423-425`:

> Let a regular **product** recognition family on an open parameter domain have coordinates
> $\eta=(\eta_i)_i$ and **block-diagonal** Fisher metric $G(\eta)=\bigoplus_iG_i(\eta_i)$,
> **including categorical blocks when present**.

The categorical blocks are the attention rows. `05b:445-449` then says explicitly that dropping
this is a different object: "Block orthogonality is load bearing. With a nondiagonal Fisher
metric, the global natural gradient mixes agents and independent local inversions are a different
dynamics." The chapter is not silent about correlated recognition; it excludes it by declaration.
`05b:399-401` deriving the row replicator as *the Fisher natural gradient on the open simplex*
presupposes the row is its own metric block, i.e. a factor.

### 3. `05:23` supports the reading rather than defeating it

V2 cites `05_elbo.tex:23` ("No factorization is imposed here") as evidence against. The full
sentence: "No factorization is imposed here; **the restrictions that impose one are the subject
of `\Cref{ch:restrictions}`, and they are restrictions on this object rather than replacements
for it.**" The architecture is: the population recognition kernel is unrestricted by default, and
individual results **declare** a restriction. `07_restrictions.tex:21-31` is that declared
block-factorized family. `prop:obs-attention-elbo` declares one, in the standard word for it.

### 4. The conclusion is not well-posed without factorization

The proposition asserts a per-row object: "its exact categorical **contribution** to the
collective VFE is ...". A decomposition of $\Fenergy_o$ into per-row contributions exists only
when the rows factorize. V2's own residual $\E_{Q_Y}[\operatorname{TC}(Q_{J\given Y})]$ belongs to
no row — so under correlated labels there is no "categorical contribution of row $i$" for the
proposition to be right or wrong about. Related: $\beta^Q_i$ is called a recognition **row**,
parallel to the genuine generative conditional row $\beta^P_{ij}(y)$ of
`eq:obs-attention-posterior`. Under correlated labels the recognition conditional row is
$Q(J_i\given y,J_{-i})$, which is not V2's fixed vector; V2's object is a marginal, not a row.

### 5. No internal inconsistency with `prop:elbo-total-correlation-signs`

`05:350` forbids **substituting** $\sum_b\E_{Q_X}[\log q_b]$ for the joint recognition
log-density of a correlated law. Under mean-field there is no substitution: $q=\prod_bq_b$
identically and $\operatorname{TC}=0$, so `eq:elbo-total-correlation-signs` gives
$\widetilde{\Fenergy}=\Fenergy$. The residual V2 exhibits **is** the Ch. 5 object, and its
appearance off the declared family is what `prop:elbo-total-correlation-signs` (`05:33-72`)
predicts. `05b:355` writing "mean-field" is the manuscript applying its own Ch. 5 warning, not
contradicting it. My run confirms the residual is that object, and that in the $y$-free-row case
it coincides with the plain block total correlation of `eq:elbo-total-correlation`:

```
=== (a) FULL MEAN-FIELD  Q = Q_Y (x) beta_1 (x) beta_2  [the proposition's family] ===
  F_o - claimed          = -1.110e-16          E_QY[TC(Q_J|Y)] =  1.308e-16
=== (b) y-free rows, J_1 and J_2 CORRELATED  (NOT mean-field) ===
  F_o - claimed          = 0.183158510880731984
  E_QY[TC(Q_J|Y)]        = 0.183158510880731595      difference = 3.886e-16
=== (c) y-free rows, y-DEPENDENT copula (NOT mean-field) ===
  F_o - claimed          = 0.088267670368580464
  E_QY[TC(Q_J|Y)]        = 0.088267670368580020      difference = 4.441e-16
=== residual IS prop:elbo-total-correlation-signs applied to the J blocks (case b) ===
  TC(Q; Y,J1,J2) = 0.183158510881   E_QY[TC(Q_J|Y)] = 0.183158510881
=== softmax optimum under the stated hypothesis ===
  mean-field numeric minimizer         = [0.26920426 0.17339935 0.55739639]
  eq:obs-attention-recognition-optimum = [0.26920426 0.17339935 0.55739639]
  max|difference| = 8.291e-12   -> softmax formula EXACT under the hypothesis
```

Case (a) and the softmax check confirm `eq:obs-attention-full-contribution` and
`eq:obs-attention-recognition-optimum` are exact under the proposition's hypothesis. Cases (b)
and (c) confirm V2's algebra and are off-hypothesis.

### 6. The canon fixes the term of art

Blei, Kucukelbir, McAuliffe (2017), §2.3, verbatim: "In this review we focus on the *mean-field
variational family*, where the latent variables are **mutually independent** and each governed by
a distinct factor in the variational density", $q(\mathbf z)=\prod_{j=1}^m q_j(z_j)$. `Blei2017`
and `Bishop2006` are both already in `manuscripts/references.bib` (lines 1144, 1153). A standard
term of art used in its standard sense is not an undisplayed hypothesis.

### 7. The claimed contrast with `07b:504-524` does not hold

`07b:503-525` disintegrates one index $I$ at a fixed outside context $z_{-I}$ and splits
$\KL(Q(J,Z_I\given z_{-I})\Vert P(\cdot))$ into a row KL plus a $\beta$-weighted continuation KL.
That is a label-versus-continuation chain rule for a single receiver; it performs no cross-receiver
decomposition and therefore is not "the same thing done without a product hypothesis". A
cross-reference would be a convenience, not a correction.

### What I grant

V2's decomposition is right, its numbers replicate to $4\times10^{-16}$ on my own data, and the
word "mean-field" appears once in `05b` with its factorization content supplied by a later
chapter (`11:207`), a later section of the same chapter (`05b:423-425`), and the standard
literature. A reader who takes "mean-field" as decorative reaches V2's conclusion. Displaying
$Q(dy,dj)=Q_Y(dy)\bigotimes_i\beta^Q_i(dj_i)$ at `05b:355` and citing `Bishop2006,Blei2017` costs
one clause and is worth doing — that is the "missing cross-reference" downgrade V2's own
falsification condition specifies, at **editorial/low** severity. It is not the filed finding
(hypothesis insufficient, "exact" inflated, `ESTABLISHED` over-reported, internal inconsistency,
high), and none of those survive.

---

## Summary

| Finding | Filed | Verdict | Surviving residue |
|---|---|---|---|
| V1 `05b:313-315` | high — no-go false as stated, status inflation | **REFUTED** | optional word "coordinate-local" at `05b:313`; editorial |
| V2 `05b:355` | high — hypothesis insufficient, internal inconsistency | **REFUTED** | optional one-clause display of the factorization + `\citep{Bishop2006,Blei2017}`; editorial/low |

Both findings' computations are correct; both witnesses violate a hypothesis the manuscript
states. V1's witness is excluded by the definition of "local objective" given at `05b:311-313`
and restated at `05b:282-285`, `appendix_notation.tex:153-156`, and `01_introduction.tex:83-84`,
and by the structure theorem in §V1.2 no local witness can exist. V2's witness is excluded by
"mean-field", which this manuscript (`11:207`, `05b:423-425`) and the cited canon (Blei 2017 §2.3)
use to mean factorization.
