<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 9, route D: primary-source and applicability map

## Executive disposition

This audit separates a citation's historical or model-specific support from the
proof burden of the present manuscript.

1. Jona-Lasinio's equations (2.13)--(2.14) support the **binary**, scalar,
   independent Gaussian/Hermite linearization.  The arbitrary integer-block
   theorem, its DQM realization, its exact operator spectrum, and every gauge or
   correlated extension are proofs of the present work, not imported results.
2. Jona-Lasinio's equations (5.10)--(5.11) support conditional expectation as
   the linearization for the paper's self-similar Gaussian random-field model.
   They do not establish that formula for every agent network or every
   standard-Borel channel without the manuscript's own score-pushforward proof.
3. Jona-Lasinio's equations (7.4)--(7.5) support a typed generalized-mode
   cocycle **conditional on an assumed compatible basis in every tangent
   space**.  The source does not prove that such bases exist or are complete.
4. Kemeny--Snell Theorem 6.3.2 is a finite-state theorem.  It is the exact
   finite analog of equation `eq:rg-strong-lumpability`, but it does not by
   itself source a standard-Borel theorem.  The standard-Borel extension is
   valid after adding a surjective Borel quotient hypothesis and the short
   measurability proof below.
5. The sentence following `eq:rg-strong-lumpability` presently overstates the
   contrapositive.  Failure of the row-sum condition proves failure of one
   coarse kernel common to all fine initial laws.  It does **not** imply, in
   general, that at least one individually initialized coarse process is
   non-Markov.  A four-state counterexample is given below.
6. Nakajima (1958) and Zwanzig (1960) are historically appropriate antecedents
   for projection/elimination and memory-kernel formalisms.  Neither primary
   paper proves the exact discrete recurrence
   \(\mathsf CT\mathsf Q(\mathsf QT\mathsf Q)^n\mathsf QT\mathsf P\).
   That identity must be derived in this manuscript by iterating its two block
   recurrences; the citations should be explicitly historical.

No manuscript, bibliography, control-plane JSON, build artifact, or Git state
was changed by this route.

## Bound source snapshot

The line mappings below were checked at repository commit
`3dbe4c610ccc3c0645d25d06ed8fd3074eb4ba3a`.  At the time of inspection:

| artifact | SHA-256 |
|---|---|
| `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex` | `902E6ECF583CF084ADDCCDB3E84A265CFC8EEF5D4BA3BD3749E533295E6BD95C` |
| `manuscripts/references.bib` | `EA0F0B4F2800A0E711F246689CA8D54E2F57EF445B0C34491D5A3A06687A8B41` |
| `evidence/task-9-hermite-analysis.md` | `7A94CDF1776D7D7FB88A8672BEDD042C739C66B4A5C61E8DCC98F27D1D83BEEB` |
| `problem-contract.json` | `A9E1999C85EE333F23A1AACB90A6A51B526565D1E89F958374201A55D06878DE` |

The contract digest is the digest in the metadata header.  Source records were
checked on 2026-08-04 against the publisher pages and, where available, the
primary text.  The downloaded arXiv primary PDF for Jona-Lasinio had SHA-256
`261C0F5F8E2A47E65678886F605E3680B18A29A35C255690CAED0BE17B41EC11`.

## Concrete source-to-claim table

| source location | source hypotheses and conclusion | exact current or repaired manuscript target | what the citation can support | what remains the manuscript's proof | falsifier |
|---|---|---|---|---|---|
| Jona-Lasinio (2001), equations (2.8)--(2.14), especially (2.13)--(2.14) | Scalar i.i.d. variables; binary normalized block sum; standard Gaussian fixed density; first-order deformation \(p_\eta=p_G(1+\eta h)\); normalization, centering, and variance constraints (2.9)--(2.11).  The linearized binary operator has Hermite eigenfunctions and \(\lambda_k=2^{1-k/2}\). | Proposed Gaussian/Hermite repair: \(X_i\stackrel{\mathrm{iid}}\sim N(0,1)\), \(Z=b^{-1/2}\sum_{i=1}^bX_i\), \(L_bh=b\,\mathbb E[h(X_1)\mid Z]\), and \(L_be_k=b^{1-k/2}e_k\).  No such theorem or Jona-Lasinio citation was yet present in `07b_agent_network_rg.tex` at the bound snapshot; the candidate appears in `construction-or-strongest-theorem.md:49--55` and is proved in `task-9-hermite-analysis.md`. | Historical and mathematical precedent for the **\(b=2\)** eigenvalue formula and Hermite modes, with the three moment constraints. | Extension to every integer \(b\ge2\); DQM realization; normalized Hermite convention; boundedness/compactness and the status of zero in the spectrum; correlated, multivariate, or gauge cases. | The source uses a nonbinary block, a correlated law, or proves the full nonlinear CLT remainder; or the repaired manuscript attributes any of those claims to equations (2.13)--(2.14). |
| Jona-Lasinio (2001), equations (5.1)--(5.11), especially (5.10)--(5.11) | A lattice self-similar random field with block map \(R_{\alpha,n}\), \(1\le\alpha<2\); a self-similar **Gaussian** fixed measure \(P_G\); a deformation \(P_G(1+h)\).  Linearization is conditional expectation given the block variables; generalized infinite-dimensional Hermites satisfy the displayed model-specific eigen-equation. | Repaired generalized-mode discussion must say that conditional expectation is a source-supported realization in this self-similar Gaussian-field model, not a universal theorem for arbitrary agent networks.  The universal score map, if claimed, must be tied to the manuscript's DQM/Markov-kernel theorem. | Conditional expectation as an RG linearization and generalized Hermite modes in the source's self-similar Gaussian random-field setting. | The general standard-Borel score pushforward, arbitrary network blocking, existence of a complete mode basis, and gauge covariance. | The repaired prose drops the Gaussian/self-similar-field hypotheses or cites (5.10)--(5.11) as a proof for every Markov kernel. |
| Jona-Lasinio (2001), equations (7.2)--(7.5) | Tower property for nested block variables; tangent spaces at \(P\) and \(R^*_{\alpha,n}P\).  The paper explicitly **assumes** a basis \(H_k^P\) in every tangent space satisfying generalized equation (7.4), and then derives \(\lambda_k(m,R^*_{\alpha,n}P)\lambda_k(n,P)=\lambda_k(mn,P)\). | Repaired generalized-mode/cocycle claim must begin: "Assume compatible mode frames satisfying the typed relation ..."  It may then cite equations (7.4)--(7.5) for the conditional-expectation precedent and cocycle. | The typed cross-law eigen-relation as a framework and the multiplicative law derived from tower composition, conditional on the assumed frames. | Existence, completeness, uniqueness, measurability, and scale-coherence of mode frames; any scalar identification of distinct tangent spaces; any ordinary spectrum without a declared reference-space identification. | Any source passage proving basis existence in the stated generality, or repaired prose presenting the basis as a consequence rather than a hypothesis. |
| Kemeny--Snell (1976), section 6.3, Definition 6.3.1 and Theorem 6.3.2, printed p. 124 | A **finite**, discrete-time Markov chain with transition matrix \(P=(p_{ij})\) and a finite partition \(\{A_1,\ldots,A_r\}\).  Lumpability means that for every starting vector the lumped process is Markov and its transition probabilities do not depend on that vector.  Necessary and sufficient: \(\sum_{s_k\in A_j}p_{\ell k}\) is constant over \(s_\ell\in A_i\), for every \(i,j\). | Current `07b_agent_network_rg.tex:1355--1366`, equation `eq:rg-strong-lumpability`.  Repaired target: explicitly declare standard-Borel fine and coarse spaces, a **surjective Borel** statistic \(c\), and say "one coarse kernel, independent of the fine initial law." | The finite row-sum criterion and its universal-initial-law meaning; historical origin of the term lumpability. | The standard-Borel extension, including measurability of the factored kernel; the path-action consequence; every claim about failure for an individual initial law. | A source theorem stated for arbitrary standard-Borel kernels, or a repaired manuscript that still infers individual non-Markovness solely from failure of the universal criterion. |
| Nakajima (1958), title, abstract, and Liouville/transport construction | Quantum steady diffusion; a stationary solution of Liouville's equation constrained to reproduce a prescribed average-density distribution; a kinetic equation with a weak-interaction limit. | Current `07b_agent_network_rg.tex:1368--1388`, equations `eq:rg-memory-operators` and `eq:rg-initial-noise-vanishing`. | Historical antecedent for projection/elimination methods in quantum transport and for what later became the Nakajima--Zwanzig lineage. | The manuscript's exact discrete-time block recurrence, its operator domains, lag indexing, and autonomous-closure iff conditions. | The 1958 primary text contains exactly the manuscript's discrete powers of \(\mathsf QT\mathsf Q\) with the same types and lag convention. |
| Zwanzig (1960), primary abstract and article record | Projection operators in the Hilbert space of Gibbsian ensemble densities split relevant and irrelevant parts; the relevant part satisfies a kinetic equation generalizing Van Hove's master equation; application to a classical weakly interacting system. | Same current lines and equation labels as the Nakajima row.  Repaired prose should call the formula a "discrete projection-elimination identity, historically analogous to the Nakajima--Zwanzig formalism." | Direct historical support for relevant/irrelevant projection and elimination into a kinetic equation. | The exact discrete recurrence and every claim on the manuscript's abstract observable space. | The 1960 paper gives the same discrete recurrence rather than its continuous-time/kinetic projection formalism. |

## Jona-Lasinio: equation-by-equation applicability

### Equations (2.13)--(2.14)

The source first fixes the binary recursion
\[
 \zeta_{n+1}=2^{-1/2}(\zeta_{n1}+\zeta_{n2})
\]
and its convolution RG.  It then fixes the unit-variance Gaussian and uses a
linear density deformation satisfying three orthogonality constraints.  Within
that setting, equation (2.13) is the linearized operator and equation (2.14)
gives
\[
 \lambda_k=2^{1-k/2}
\]
with Hermite eigenfunctions.  Immediately afterward, the paper says that the
nonlinear terms needed to complete the CLT argument are not pursued.

Consequently, a precise repaired citation is of the form:

> For the binary Gaussian density linearization and its Hermite eigenvalues,
> see Jona-Lasinio, equations (2.13)--(2.14).  The arbitrary-\(b\) DQM theorem
> below is proved here.

The citation must not be attached to a sentence claiming nonlinear global
attraction, arbitrary block size, the exact compact spectrum, correlated
inputs, or gauge covariance.

### Equations (5.10)--(5.11)

Equation (5.10) identifies the derivative of the random-field RG at its
self-similar Gaussian fixed measure with conditional expectation given block
variables.  Equation (5.11) reports Sinai's generalized Hermite modes and
model-specific powers of the block parameter.  The operative hypotheses are
not decorative: the lattice block map, self-similarity, Gaussianity, and the
field's normalization exponent determine the formula.

The safe manuscript use is an example or precedent.  A general score identity
for a parameter-independent Markov kernel instead follows from the
manuscript's own DQM calculation:
\[
 s_{\mathrm{coarse}}(z)=\mathbb E[s_{\mathrm{fine}}(Y)\mid Z=z].
\]
Jona-Lasinio is not a replacement for proving the regularity, domination, and
version hypotheses of that statement.

### Equations (7.4)--(7.5)

The exact logical order in the source is decisive.  It interprets conditional
expectation as a map between the tangent spaces at two different probability
laws and then says that it **assumes** bases in those spaces connected by
equation (7.4).  Only under this assumption does the tower property yield the
cocycle (7.5).

Thus a repaired theorem may state
\[
 D K_n(P)H_k^P
 =\lambda_k(n,P)H_k^{K_nP},
 \qquad
 \lambda_k(m,K_nP)\lambda_k(n,P)=\lambda_k(mn,P),
\]
provided the first relation and compatible mode frames are explicit
hypotheses.  The source does not permit replacing this typed family by one
untyped eigenvector equation on a single Hilbert space unless the manuscript
also supplies the required identifications.

## Kemeny--Snell and the standard-Borel boundary

### What Theorem 6.3.2 actually proves

For finite states, write
\[
 p_{\ell A_j}:=\sum_{s_k\in A_j}p_{\ell k}.
\]
Kemeny--Snell's condition is that \(p_{\ell A_j}\) have the same value for
every fine state \(s_\ell\in A_i\), for every ordered pair of blocks.  Those
common values form the lumped transition matrix.  Their definition includes
both quantifiers: every starting vector, and transition probabilities
independent of the starting vector.

This directly matches the finite specialization of
`eq:rg-strong-lumpability`.  It does not directly cover uncountable spaces,
measurable kernels, or measurability of a quotient factor.

### Short standard-Borel extension that the manuscript may prove

Let \(E,F\) be standard-Borel spaces, let \(c:E\to F\) be a surjective Borel
map, and let \(T:E\rightsquigarrow E\) be a Markov kernel.  The following are
equivalent.

1. There is a Markov kernel \(\bar T:F\rightsquigarrow F\), independent of the
   fine initial law, such that every projected chain \(c(X_n)\) has transition
   kernel \(\bar T\).
2. For all \(x,x'\in E\) with \(c(x)=c(x')\),
   \[
   T(x,c^{-1}B)=T(x',c^{-1}B)
   \quad\text{for every }B\in\mathcal B(F).
   \]

**Proof.**  Necessity follows by initializing at \(\delta_x\) and
\(\delta_{x'}\).  Under condition 2 define
\[
 \bar T(c(x),B):=T(x,c^{-1}B).
\]
It is well-defined and is a probability measure in \(B\).  For fixed \(B\),
the function \(g_B(x)=T(x,c^{-1}B)\) is Borel and constant on the fibers of
\(c\).  If \(A=g_B^{-1}((q,\infty))\), then \(A\) and \(E\setminus A\) are
Borel saturated sets.  Their images under \(c\) are complementary analytic
sets in the standard-Borel space \(F\), hence Borel by the analytic/coanalytic
theorem.  Therefore the factor \(z\mapsto\bar T(z,B)\) is Borel (rational
thresholds suffice), so \(\bar T\) is a Markov kernel.  The tower property now
gives
\[
 \Pr(c(X_{n+1})\in B\mid c(X_0),\ldots,c(X_n))
 =\bar T(c(X_n),B)
\]
for every fine initial law.  \(\square\)

The explicit standard-Borel and surjective-Borel hypotheses are sufficient for
this proof and close its quotient-measurability step.  Merely saying
"deterministic partition" does not record that obligation.  Because the theorem
quantifies
over **every** fine initial law, including point masses, the equality must also
hold pointwise for a fixed kernel version; an almost-everywhere equality under
one selected reference law proves only a law-relative statement.

### Refutation of the current contrapositive

The current sentence at `07b_agent_network_rg.tex:1363--1364` says that if
strong lumpability fails, the exact effective action is not first-order Markov
for at least one initial law.  This does not follow from Kemeny--Snell and is
false without an additional condition.

Take fine states \(E=\{a,b,u,v\}\), coarse states \(F=\{0,1,2\}\), and
\[
 c(a)=c(b)=0,\qquad c(u)=1,\qquad c(v)=2.
\]
Let the deterministic transition be
\[
 a\mapsto u,\qquad b\mapsto v,\qquad u\mapsto u,\qquad v\mapsto v.
\]
The row-sum condition fails in the fiber \(c^{-1}(0)\), since the one-step
probability of coarse state 1 is one from \(a\) and zero from \(b\).  Yet for
every individual initial law \(\mu\), the projected process is a homogeneous
first-order Markov chain: coarse states 1 and 2 are absorbing, and the only
used transition from coarse state 0 has probabilities
\[
 K_\mu(0,1)=\frac{\mu(a)}{\mu(a)+\mu(b)},\qquad
 K_\mu(0,2)=\frac{\mu(b)}{\mu(a)+\mu(b)}
\]
when the denominator is nonzero.  Coarse state 0 is never revisited.  What
fails is that \(K_\mu\) depends on \(\mu\); there is no single kernel valid for
all fine initial laws.

The exact safe replacement is:

> A single coarse first-order kernel, independent of the fine initial law,
> exists exactly under strong lumpability.  If the condition fails, no such
> universal kernel exists.  Particular initial laws may nevertheless yield
> first-order coarse dynamics; these are weak-lumpability or
> initial-law-specific cases.

## Nakajima--Zwanzig: historical attribution versus discrete proof

### Primary-source scope

Nakajima's publisher record describes a quantum steady-diffusion problem:
find a steady solution of Liouville's equation that reproduces a prescribed
average-density profile, leading to a kinetic equation and a weak-interaction
limit.  It is not a theorem about a discrete Markov operator on the
manuscript's observable tier.

Zwanzig's primary abstract is more explicit about the projection architecture:
projection operators on the Hilbert space of Gibbsian ensemble densities split
the density into relevant and irrelevant parts, and elimination yields a
kinetic equation for the relevant part.  It likewise does not state the
manuscript's discrete recurrence.

Citing both papers is historically accurate for the name and lineage
"Nakajima--Zwanzig projection formalism."  It is not accurate to say that
either paper proves `eq:rg-memory-operators` as written.

### Exact discrete identity that must be proved here

Assume \(\mathsf C\mathsf P=I\), so
\(\Pi=\mathsf P\mathsf C\) is a projection and
\(\mathsf Q=I-\Pi\).  For a composable linear evolution
\(x_{t+1}=\mathsf T x_t\), put
\(r_t=\mathsf Cx_t\) and \(q_t=\mathsf Qx_t\).  Then
\[
 r_{t+1}=\mathsf CT\mathsf P r_t+\mathsf CT\mathsf Q q_t,
 \qquad
 q_{t+1}=\mathsf QT\mathsf P r_t+\mathsf QT\mathsf Q q_t.
\]
Iteration of the second equation gives
\[
 q_t=(\mathsf QT\mathsf Q)^tq_0
 +\sum_{s=0}^{t-1}(\mathsf QT\mathsf Q)^{t-1-s}
   \mathsf QT\mathsf P r_s.
\]
Substitution gives the exact resolved recurrence
\[
\begin{split}
 r_{t+1}={}&\mathsf CT\mathsf P r_t
 +\mathsf CT\mathsf Q(\mathsf QT\mathsf Q)^t\mathsf Qx_0\\
 &+\sum_{s=0}^{t-1}
 \mathsf CT\mathsf Q(\mathsf QT\mathsf Q)^{t-1-s}
 \mathsf QT\mathsf P r_s.
\end{split}
\]
Thus the lag-\(n\) memory operator is exactly the operator in
`eq:rg-memory-operators`, and the initial-noise term is the operator in
`eq:rg-initial-noise-vanishing`.  This two-line iteration, together with the
typing/domain hypotheses, is the closure evidence.  Nakajima and Zwanzig may
be cited in the preceding or following historical sentence, not as a substitute
for it.

For bounded operators on the declared Banach or Hilbert tiers, the displayed
products are defined.  For unbounded \(\mathsf T\), the manuscript must add a
common invariant domain and justify every iterate.  If
\(\mathsf C\mathsf P=I\) holds only almost everywhere in an \(L^p\) class, the
recurrence must likewise be stated on that quotient/equivalence class rather
than pointwise.

## Full publisher metadata and recommended bibliography records

### Verified records

| key | complete checked metadata | primary or publisher record |
|---|---|---|
| `JonaLasinio2001` | Giovanni Jona-Lasinio, "Renormalization Group and Probability Theory," *Physics Reports* **352**, issues 4--6 (October 2001), 439--458. DOI `10.1016/S0370-1573(01)00042-4`. arXiv `cond-mat/0009219` (submitted 14 September 2000). | [ScienceDirect publisher record](https://www.sciencedirect.com/science/article/pii/S0370157301000424); [arXiv record](https://arxiv.org/abs/cond-mat/0009219); [primary PDF](https://arxiv.org/pdf/cond-mat/0009219). |
| `KemenySnell1976` | John G. Kemeny and J. Laurie Snell, *Finite Markov Chains: With a New Appendix "Generalization of a Fundamental Matrix"*, Undergraduate Texts in Mathematics, Springer-Verlag New York, 1976, first Springer edition, xii + 226 pages. Hardcover ISBN `978-0-387-90192-3`; published 1 July 1976; originally published by Van Nostrand in 1960. Theorem 6.3.2 is on printed p. 124.  The publisher record exposes no DOI for this edition. | [Springer publisher record](https://link.springer.com/book/9780387901923); [section 6.3--6.4 scan indexed by the search record](https://math.pku.edu.cn/teachers/yaoy/Fall2011/Kemeny-Snell_Chapter6.3-4.pdf). |
| `Nakajima1958` | Sadao Nakajima, "On Quantum Theory of Transport Phenomena: Steady Diffusion," *Progress of Theoretical Physics* **20**(6) (December 1958), 948--959; published 1 December 1958, received 17 August 1958. DOI `10.1143/PTP.20.948`. | [Oxford Academic publisher record](https://academic.oup.com/ptp/article/20/6/948/1930693). |
| `Zwanzig1960` | Robert Zwanzig, "Ensemble Method in the Theory of Irreversibility," *The Journal of Chemical Physics* **33**(5) (1 November 1960), 1338--1341; received 16 May 1960. DOI `10.1063/1.1731409`. | [AIP publisher record](https://pubs.aip.org/aip/jcp/article/33/5/1338/206419/Ensemble-Method-in-the-Theory-of-Irreversibility); [DOI record](https://doi.org/10.1063/1.1731409). |

The present `JonaLasinio2001` BibTeX entry at
`manuscripts/references.bib:1103--1110` omits the issue range, month, DOI, and
arXiv identifier.  No Kemeny--Snell, Nakajima, or Zwanzig entry was found at
the bound snapshot.

### Recommended BibTeX payload (not applied by this route)

```bibtex
@article{JonaLasinio2001,
  author        = {Jona-Lasinio, Giovanni},
  title         = {Renormalization Group and Probability Theory},
  journal       = {Physics Reports},
  year          = {2001},
  month         = oct,
  volume        = {352},
  number        = {4--6},
  pages         = {439--458},
  doi           = {10.1016/S0370-1573(01)00042-4},
  eprint        = {cond-mat/0009219},
  archiveprefix = {arXiv}
}

@book{KemenySnell1976,
  author    = {Kemeny, John G. and Snell, J. Laurie},
  title     = {Finite Markov Chains: With a New Appendix
               {``Generalization of a Fundamental Matrix''}},
  series    = {Undergraduate Texts in Mathematics},
  publisher = {Springer-Verlag},
  address   = {New York},
  year      = {1976},
  isbn      = {978-0-387-90192-3},
  pagetotal = {226},
  note      = {xii + 226 pages; originally published by Van Nostrand, 1960}
}

@article{Nakajima1958,
  author  = {Nakajima, Sadao},
  title   = {On Quantum Theory of Transport Phenomena: Steady Diffusion},
  journal = {Progress of Theoretical Physics},
  year    = {1958},
  month   = dec,
  volume  = {20},
  number  = {6},
  pages   = {948--959},
  doi     = {10.1143/PTP.20.948}
}

@article{Zwanzig1960,
  author  = {Zwanzig, Robert},
  title   = {Ensemble Method in the Theory of Irreversibility},
  journal = {The Journal of Chemical Physics},
  year    = {1960},
  month   = nov,
  volume  = {33},
  number  = {5},
  pages   = {1338--1341},
  doi     = {10.1063/1.1731409}
}
```

`pagetotal` is useful in BibLaTeX but may be ignored by classic BibTeX; the
theorem citation should independently specify section 6.3, Theorem 6.3.2,
printed p. 124.

## Exact repair map by current label

| manuscript anchor | required repair | citation placement |
|---|---|---|
| `eq:rg-strong-lumpability`, current lines 1355--1366 | Add standard-Borel \(E,F\), a surjective Borel \(c:E\to F\), and "one kernel independent of the fine initial law."  Replace the false "at least one initial law is non-Markov" sentence by failure of universal closure; retain initial-law-specific/weak cases.  Include the factor-measurability proof above or cite a general measurable-state theorem in addition to Kemeny--Snell. | Cite Kemeny--Snell explicitly as the finite-state theorem: `\cite[Sec.~6.3, Thm.~6.3.2, p.~124]{KemenySnell1976}`. |
| `eq:rg-memory-operators` and `eq:rg-initial-noise-vanishing`, current lines 1368--1388 | Insert the two coupled block recurrences and their iteration; state \(\mathsf C\mathsf P=I\), operator types/domains, and the initial class. | After the own proof, say that it is the discrete projection-elimination analog of the Nakajima--Zwanzig formalism and cite `\cite{Nakajima1958,Zwanzig1960}`. |
| Proposed Gaussian/Hermite theorem (not yet in `07b` at the snapshot) | State scalar iid Gaussian inputs, integer \(b\ge2\), sum normalization, normalized probabilists' Hermites, centered DQM space, and distinguish the constant mode.  Prove arbitrary \(b\), DQM realization, and spectrum locally. | Cite Jona-Lasinio equations (2.13)--(2.14) only for the binary precedent. |
| Proposed generalized conditional-expectation modes | Restrict the source attribution to self-similar Gaussian random fields, or separately prove the general DQM/Markov-channel result. | Cite equations (5.10)--(5.11) with the model scope in the same sentence. |
| Proposed generalized mode cocycle | Make compatible mode frames an explicit hypothesis; keep the tangent source and target typed; form an ordinary spectrum only after a declared identification. | Cite equations (7.4)--(7.5), noting that (7.4)'s bases are assumed in the source. |

## Recommended central-ledger dispositions

This route did not edit the root-owned claim ledger.  The evidence supports the
following updates by the root verifier:

| ledger claim | recommended state | reason |
|---|---|---|
| `jona-lasinio-mapping` | `EVIDENCE_VERIFIED` after the manuscript uses the bounded mappings above | The primary PDF and publisher metadata were checked equation by equation; every non-source extension is explicitly assigned to the manuscript's proof. |
| `minor-lumpability-memory-sources`, source-metadata/historical component | `EVIDENCE_VERIFIED` | Publisher records, theorem location, and historical scopes are checked. |
| `minor-lumpability-memory-sources`, current broad lumpability prose | `REFUTED` until repaired | The sentence inferring an individually non-Markov law is falsified by the four-state chain above. |
| `minor-lumpability-memory-sources`, standard-Borel biconditional | `EVIDENCE_VERIFIED` only after own proof and hypotheses are inserted | Kemeny--Snell alone is finite; the displayed standard-Borel factor proof closes the extension when its hypotheses are adopted. |
| `minor-lumpability-memory-sources`, discrete recurrence | `EVIDENCE_VERIFIED` only from the manuscript's own block-iteration proof | Nakajima and Zwanzig are historical evidence, not direct proof of the discrete identity. |

## Falsification checklist

The source map fails and must be reopened if any of the following occurs:

1. the repaired Jona-Lasinio citation is attached to arbitrary \(b\), correlated
   inputs, nonlinear attraction, DQM realizability, exact spectral closure, or
   gauge covariance without an adjacent own proof;
2. generalized mode bases are asserted to exist merely because source equation
   (7.4) writes them down;
3. Kemeny--Snell is described as a standard-Borel theorem rather than a
   finite-state theorem;
4. the standard-Borel repair omits surjectivity/quotient measurability or does
   not prove that \(\bar T(\cdot,B)\) is measurable;
5. failure of strong lumpability is again identified with individual
   non-Markovness rather than failure of a universal initial-law-independent
   kernel;
6. Nakajima or Zwanzig is cited as the proof of the exact discrete powers and
   lag indices;
7. the discrete recurrence is used with \(\mathsf C\mathsf P\ne I\), incompatible
   operator domains, or an unreported unresolved initial-state term; or
8. bibliography metadata differs from the publisher records above without a
   documented edition or record change.
