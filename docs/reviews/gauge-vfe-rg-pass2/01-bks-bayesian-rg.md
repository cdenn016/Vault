# BKS Bayesian-renormalization and information-geometry review

**Review baseline:** `f568b7b18973268fc1febafd3805f3cce64f933d`
**Lens:** Berman–Klinger–Stapleton Bayesian renormalization; dynamical Bayes; Fisher stiffness/sloppiness; model-space versus sample-space flow; scale orientation; admissible bridges to the manuscript
**Verdict:** 3 medium findings; 0 high or critical findings

## Scope and status protocol

I checked the executable mathematical claims in `08_infogeometry.tex`, `09_coarsegraining.tex`, `10_renormalization.tex`, and `11_obstructions.tex` against the primary BKS and Berman–Heckman–Klinger papers. I also checked `SPEC.md`, the prior R1–R21 disposition, `manuscripts/verified-ledger.md`, the three required wiki concept pages, and `sources/papers/berman-2023-bayesian-renormalization.md`.

The requested P/D/S/E/C acronym is not defined in the manuscript package. I therefore do not guess it. Each finding reports the literal manuscript `\status{...}` macro, when one exists, plus a plain-English category and an inflation verdict.

The following repaired passages are clean and are not re-raised:

- `08_infogeometry.tex:182-207` correctly separates latent sample space, recognition-parameter space, and generative-model parameter space, and leaves the transfer of the BKS scale criterion to \(\Lambda\) `OPEN`.
- `10_renormalization.tex:621` correctly states the local Gaussian-location identity \(I_{\mu\mu}=\Lambda\) in the manuscript's moment chart. That component equality is not itself a bridge to BKS's generative-model Fisher metric.
- `10_renormalization.tex:623` correctly reports that BKS's implemented pruning rule thresholds diagonal Fisher entries \(I_{ii}\), not eigenvalues, and that the paper supplies no diagonal-to-spectral bridge.
- `11_obstructions.tex:115-122` correctly rejects the former endpoint extrapolation and correctly states that no common scale map or operator comparison has established opposite flow directions.
- No R1–R21 regression was found. The remaining issues are new inconsistencies in the later literature discussion.

## Evidence ledger

| Checked claim | Verification state | Closure evidence |
|---|---|---|
| “The Fisher information metric” is the tensor that supplies the BKS diffusion covariance | `REFUTED` | BKS Eqs. (35), (38), and (43) use \(I^{-1}\); Eq. (44) pushes the inverse Fisher tensor forward |
| BKS dynamical Bayes itself is the displayed Fokker–Planck/ERG flow | `REFUTED` as stated | BKS Eq. (33) is a centered-KL replicator equation for \(\pi_T(\theta)\); the Fokker–Planck equation appears only after a late-\(T\) Gaussian approximation, inverse-problem restriction, posterior-predictive construction, and pushforward |
| Proposition 11.3 quantitatively realizes BKS stiff/sloppy directions | `REFUTED` as a completed bridge | Proposition 11.3 contains no generative likelihood, model-parameter Fisher matrix, or Fisher eigenspaces; `08_infogeometry.tex:207` declares the bridge `OPEN` |
| The BKS and manuscript flows have been shown to run in opposite directions | `INCONCLUSIVE` | A local small-\(\tau\) covariance contrast exists, but no \(\tau\leftrightarrow\ell\) map and no common operator/state space are supplied; `11_obstructions.tex:122` says exactly this |

## Findings

### 1. The BKS summary collapses distinct flows and names the wrong diffusion tensor

**Location:** `manuscripts/gauge_vfe_rg/10_renormalization.tex:619`

**Severity:** medium

**Manuscript status and inflation:** No `\status{...}` macro is attached. The sentence is presented as a source-backed literature fact. It is inflated in two ways: a conditional, asymptotic construction is stated as an unqualified identification, and the covariant Fisher metric is named where the pushed-forward inverse Fisher cometric supplies the diffusion covariance.

**Manuscript evidence:**

> “Berman, Klinger and Stapleton identify dynamical Bayesian updating with an exact renormalization group flow, with the Fisher information metric in the role of the diffusion kernel...”

**Primary-source adjudication:**

BKS's construction has three different probability objects.

1. Their Eq. (33) evolves the posterior density \(\pi_T(\theta)\) on **model-parameter space**:
   \[
   \partial_T\pi_T(\theta)
   =-\left(D_{\rm KL}(\theta_\ast\Vert\theta)
   -\mathbb E_{\pi_T}D_{\rm KL}(\theta_\ast\Vert\Theta)\right)\pi_T(\theta).
   \]
   This is a centered-fitness/replicator equation, not a Fokker–Planck equation.
2. Only “at sufficiently late \(T\)” do BKS write the Gaussian approximation
   \[
   \pi_T\simeq\mathcal N\!\left(\mu_T,T^{-1}I(\mu_T)^{-1}\right)
   \]
   in Eq. (35). Their footnote 10 says explicitly that Eq. (38) represents the Bayesian posterior only for sufficiently small \(\tau=1/T\); continuation to all \(\tau\) is an interpretive extension.
3. After additionally restricting to a Bayesian inverse problem \(Y=G(\Theta)+N\), forming the posterior predictive, and pushing forward through \(G\), BKS obtain the sample-space Gaussian in Eq. (43), with covariance
   \[
   \tau (K_\tau^{-1})^{ab},\qquad
   (K_\tau^{-1})^{ab}
   =\frac{\partial G^a}{\partial\theta^i}
    \frac{\partial G^b}{\partial\theta^j}I_\tau^{ij}.
   \]
   Eqs. (45)–(46) then give the Fokker–Planck/SDE form. The diffusion covariance is therefore the **pushforward of the inverse Fisher cometric** \(I^{ij}\), not the Fisher metric \(I_{ij}\) itself. This covariance is coordinate-correct: under \(\theta'=A\theta\),
   \[
   I'^{-1}=AI^{-1}A^\top,\qquad J_G'=J_GA^{-1},
   \]
   so \(J_G'I'^{-1}J_G'^\top=J_GI^{-1}J_G^\top\). The exact SymPy residual of this identity in a generic \(2\times2\) chart was the zero matrix.

The same distinction is standard information geometry: the Fisher information is a covariant metric, while its inverse is the contravariant tensor used to turn covectors into diffusion/natural-gradient directions (Amari & Nagaoka 2000, §2.2; Nielsen 2020, §2).

The exact change of variables also rules out identifying raw dynamical Bayes with the Fokker–Planck equation. From \(T=1/\tau\),
\[
\frac{dT}{d\tau}=-\tau^{-2},\qquad
\partial_\tau\pi_\tau
=\tau^{-2}\left(D-\mathbb E_{\pi_\tau}D\right)\pi_\tau,
\]
which remains a replicator equation. The executed SymPy check returned
`dT/dtau = -1/tau**2` and
`dpi/dtau = Delta*pi(1/tau)/tau**2`.

Primary sources: Berman, Klinger & Stapleton 2023, §§3.2–3.4, Eqs. (33), (35), (38)–(46), footnote 10 ([primary PDF](https://arxiv.org/pdf/2305.10491)); Berman, Heckman & Klinger 2022, §§2.2–2.6, especially Eqs. (2.27)–(2.40) ([primary PDF](https://arxiv.org/pdf/2204.12939)).

**Exact repair:**

Replace the first clause of line 619 with:

> Berman, Klinger and Stapleton begin with a centered-KL posterior flow on model-parameter space. In the regular late-data regime they approximate that posterior by a Gaussian with covariance \(T^{-1}I^{-1}\); after setting \(\tau=1/T\), restricting to an inverse problem with forward map \(G\), and pushing the posterior predictive into sample space, the pushed-forward inverse Fisher cometric \(G_\ast I^{-1}\) supplies the diffusion covariance of an ERG-form Fokker–Planck equation. The continuation beyond the small-\(\tau\) posterior regime is part of their renormalization construction, not a Bayesian limit theorem.

Under the requested new manuscript architecture, this typed and conditional statement belongs in the **general theory/RG literature**. The Gaussian identity \(I_{\mu\mu}=\Lambda\), currently at line 621, belongs later in the **multivariate-Gaussian realization**.

**Falsification condition:** Derive Eqs. (45)–(46) directly from Eq. (33), without the late-\(T\) Gaussian approximation, inverse-problem map \(G\), posterior-predictive pushforward, or inverse Fisher tensor; or show that BKS Eq. (44) contains \(I_{ij}\) rather than \(I^{ij}\).

### 2. Stiff/sloppy language is transferred across the bridge that Chapter 9 leaves open

**Location:** `manuscripts/gauge_vfe_rg/10_renormalization.tex:619-623`; conflicting boundary at `manuscripts/gauge_vfe_rg/08_infogeometry.tex:182-207`; claimed target at `manuscripts/gauge_vfe_rg/10_renormalization.tex:158-177`

**Severity:** medium

**Manuscript status and inflation:** The literature paragraph has no status macro and presents the transfer as source-backed interpretation. Proposition 11.3 is `ESTABLISHED`, but `08_infogeometry.tex:207` marks the model-Fisher-to-\(\Lambda\) transfer `OPEN`. The inflation is treating an established but different norm-scaling theorem as a quantitative realization of an open Fisher-eigenspace bridge.

**Manuscript evidence:**

> “The second is the stiff/sloppy language itself, which names the distinction Proposition 11.3 and Section [the gate] make quantitative in this setting.”

Proposition 11.3 proves that, under the declared dense normalization \(\zeta=b^2\), the self-sector norm is bounded by \(b^{-1}\) per step while the coupling-sector norm is bounded. Its objects are the matrix sectors \(A_i\) and \(W_{ij}\). It does not define a generative likelihood \(p_\theta\), a model parameter \(\theta\), its Fisher matrix \(F_{\theta}\), or stiff/sloppy Fisher eigendirections.

By contrast, BKS define stiff/sloppy directions from large/small eigenvalues of the **generative-model parameter Fisher matrix** (§3.1), while their operational pruning experiment switches to diagonal entries \(I_{ii}\) in Eq. (55). The manuscript correctly records that spectral/diagonal gap at line 623. An exact rotation witness shows why the diagonal rule cannot carry an intrinsic or gauge-covariant label:
\[
I=\begin{pmatrix}1&0\\0&4\end{pmatrix}
\quad\longmapsto\quad
R^\top IR=
\begin{pmatrix}5/2&3/2\\3/2&5/2\end{pmatrix},
\qquad
R=\frac1{\sqrt2}\begin{pmatrix}1&-1\\1&1\end{pmatrix}.
\]
The eigenvalues remain \(\{1,4\}\), but the diagonals change from \((1,4)\) to \((5/2,5/2)\). At cutoff \(2\), the parameterwise classification changes under a mere orthogonal reparameterization. This was checked exactly in SymPy.

The manuscript's own `08_infogeometry.tex:207` gives the correct boundary: importing BKS requires declaring the coarse recognition mean as a fitted generative parameter and then proving that the resulting model-parameter Fisher metric is nondegenerate. The current text does neither. The component identity \(I_{\mu\mu}=\Lambda\) for a Gaussian recognition location family is correct but does not identify that recognition Fisher metric with BKS's generative-model Fisher metric.

BKS primary source: §§3.1 and 4.2, Eqs. (29)–(31) and (55) ([primary PDF](https://arxiv.org/pdf/2305.10491)). Canonical geometric basis: Amari & Nagaoka 2000, §2.2.

**Exact repair:**

Replace the last sentence of line 619 with:

> The second is a vocabulary-level analogy: BKS call large- and small-model-Fisher directions stiff and sloppy. Proposition 11.3 independently classifies self and coupling sectors by their powers under the declared block normalization; it does not identify those sectors with Fisher eigenspaces. Such an identification remains open until a generative parameterization and its nondegenerate Fisher metric are supplied.

Under the requested architecture, generic BKS stiffness/sloppiness may remain in **general theory**. The attempted identification with \(\Lambda\), \(A_i\), \(W_{ij}\), and Proposition 11.3 belongs in the later **Gaussian realization**, where it must remain `OPEN` unless the bridge theorem below is proved.

**Falsification condition:** Exhibit a declared generative family \(p_\theta(o)\) with \(\theta\) containing the manuscript's coarse parameters, compute its nondegenerate Fisher matrix, and prove that the self/coupling decomposition is invariant under that Fisher endomorphism and that Proposition 11.3's decaying/retained sectors coincide with its small/large Fisher spectral subspaces along the flow.

### 3. The asserted opposite flow direction contradicts the manuscript's own correct `NOT-CLAIMED` boundary

**Location:** `manuscripts/gauge_vfe_rg/10_renormalization.tex:625`; contradiction at `manuscripts/gauge_vfe_rg/11_obstructions.tex:119-122`

**Severity:** medium

**Manuscript status and inflation:** Line 625 has no status macro and states a factual comparison (“genuinely differ,” “runs the other way”). `11_obstructions.tex:120` marks the endpoint extrapolation `NOT-CLAIMED`, and line 122 marks the opposite-direction comparison `NOT-CLAIMED`. The inflation is direct: a comparison explicitly declined later is asserted earlier as established.

**Manuscript evidence:**

> “The direction of flow is where the two constructions genuinely differ... Aggregation here runs the other way...”

versus:

> “Nor does a verbal contrast between ‘posterior widening’ and ‘precision addition’ establish that the two scale directions are opposites... Relating them would require an explicit map between their scale parameters and an operator comparison in a common theory space; none is supplied here.”

The later statement is correct. BKS's \(T^{-1}I^{-1}\) covariance is a late-\(T\) result. Berman–Heckman–Klinger derive the \(1/T\) covariance under a local quadratic KL expansion, an approximately Gaussian posterior, proximity to the true parameter, and Cramér–Rao saturation; they explicitly organize corrections as a small-\(1/T\) expansion. BKS footnote 10 likewise limits the posterior reading of Eq. (38) to small \(\tau\). No theorem there controls the \(\tau\to\infty\) endpoint or proves global Loewner monotonicity when \(I(\mu_\tau)\) moves.

Even locally, the two operations are differently typed. BKS's backward flow diffuses a posterior predictive after a model-to-sample pushforward. Proposition 11.1 adds Gaussian precisions under a restriction/sufficient-statistic construction. Without a declared map \(\tau=\tau(\ell)\), a common statistical family, and one monotone or operator order transported between them, “opposite” has no mathematical referent.

**Exact repair:**

Delete the factual-opposition paragraph at line 625 from the general RG chapter. In the later Gaussian realization, replace it with:

> In the regular small-\(\tau\) regime, the BKS Gaussian approximation broadens like \(\tau I^{-1}\) when its Fisher tensor is held fixed, whereas the present sufficient Gaussian pooling rule adds precision. This is a typed local contrast, not yet a theorem that the two scale flows are opposites: no map between \(\tau\) and the aggregation level and no operator comparison on a common theory space has been supplied.

**Falsification condition:** Supply a common state/theory space, an explicit scale map \(\tau(\ell)\), and a transported operator or monotone \(M\) for which \(dM/d\tau\) and \(dM/d\ell\) have rigorously opposite signs over the claimed domain, including the moving-Fisher term and the error of the late-data approximation.

## Constructive open directions

### A. A typed Bayesian-to-ERG bridge theorem

**Hypotheses:** A regular identifiable model manifold \(\mathcal M\); a unique data-generating parameter; a uniform Bernstein–von Mises/Laplace expansion on \(0<\tau\leq\tau_0\); an SPD model Fisher metric \(I\); a smooth constant-rank forward map \(G:\mathcal M\to\mathcal S\); a declared noise law; and a smooth MAP drift potential.

**Target conclusion:** The posterior predictive has a controlled approximation whose generator is a sample-space Fokker–Planck operator with diffusion tensor
\[
D_\tau=J_G I(\mu_\tau)^{-1}J_G^\top,
\]
and \(D_\tau\) is invariant under model reparameterization and covariant under declared sample-frame changes.

**Proof obligations:** State the norm and order of the approximation error; derive the variable-coefficient generator rather than reading it off from a Gaussian kernel; prove normalization and the appropriate two-parameter evolution/semigroup property; treat rank-deficient \(G\); and separate the small-\(\tau\) Bayesian theorem from any globally declared \(\tau\)-continuation.

### B. A gauge-covariant stiffness/sloppiness gate

**Hypotheses:** Work on the identifiable quotient of the generative parameter manifold. Supply the model Fisher form \(F\) and a second positive reference form \(R\), both transforming by the same congruence under allowed frames. Assume a spectral gap around the chosen threshold.

**Target conclusion:** The generalized spectrum of
\[
Fv=\lambda Rv
\]
and its spectral projectors define frame-independent stiff/sloppy subbundles. A cutoff on those projectors, rather than on \(F_{ii}\) or the ordinary eigenvalues of one component matrix, is gauge-covariant.

**Proof obligations:** Prove quotient regularity, common-congruence invariance, smoothness of the projectors across scale, and stability under perturbations. Compare the result with BKS's diagonal pruning empirically only after the theorem fixes the intrinsic target.

### C. The missing model-Fisher/\(\Lambda\) bridge

**Hypotheses:** Declare a generative likelihood whose fitted parameter is the coarse Gaussian mean or whose parameter vector contains \((A_i,W_{ij})\). Give the map from those parameters to the recognition precision \(\Lambda\), and impose identifiability.

**Target conclusion:** Either derive the generative Fisher as an explicit pullback
\[
F_\theta=J_\theta^\top\,G_{\rm law}\,J_\theta
\]
and prove a relation to \(\Lambda\), or prove a no-bridge theorem showing that no chart-independent identification exists for the declared family.

**Proof obligations:** Keep sample, recognition, and generative parameter spaces typed; compute all Fisher blocks, including nuisance/cross blocks; quotient singular frame directions; and test whether the self/coupling decomposition is invariant under the resulting Fisher endomorphism. A component coincidence \(I_{\mu\mu}=\Lambda\) is insufficient.

### D. An orientation theorem instead of a verbal UV/IR comparison

**Hypotheses:** Embed the BKS posterior-predictive family and the manuscript's Gaussian restriction/pooling family in one declared statistical manifold; specify \(\tau(\ell)\); choose a common scalar monotone or tensor order; and restrict to a domain where the late-data approximation has a proved error bound.

**Target conclusion:** Establish opposition, agreement, or incomparability of the flows by the sign of the same transported quantity. Any of the three outcomes would close the present ambiguity.

**Proof obligations:** Include the derivative of the moving Fisher tensor,
\[
\frac{d}{d\tau}\bigl[\tau I(\mu_\tau)^{-1}\bigr]
=I^{-1}-\tau I^{-1}\frac{dI}{d\tau}I^{-1},
\]
distinguish restriction from Markov pushforward, and prove the claimed sign rather than infer it from the explicit factor \(\tau\).

## Placement under the requested manuscript architecture

The new order should split the present BKS discussion rather than move it as one block.

- **General theory and RG, before the Gaussian realization:** the typed posterior flow on model space; the inverse scale \(\tau=1/T\); the conditional late-data/inverse-problem route to a sample-space diffusion; the inverse-Fisher-cometric tensor; generic model-Fisher stiffness/sloppiness; and the statement that a global continuation is declared rather than a posterior limit theorem.
- **Multivariate-Gaussian realization, after general Renormalization:** \(I_{\mu\mu}=\Lambda\) in the moment chart; the expectation-chart caveat; restriction versus marginalization; precision pooling; the attempted identification of \(A/W\) sectors with stiff/sloppy directions; and any local comparison of posterior broadening with precision addition.

This division preserves the abstract BKS construction in the general spine while preventing Gaussian component coincidences from being used before their realization or from silently closing the model-Fisher bridge.

## Plain-language summary for a physicist

BKS starts with a probability cloud over **models**. Ordinary Bayesian learning makes that cloud concentrate, and its exact evolution is a selection-like equation weighted by KL divergence. Only after assuming lots of data, replacing the cloud by a Gaussian, and mapping model parameters through a forward model into **data space** does BKS obtain a heat equation. The covariance of that heat kernel is controlled by inverse Fisher information: high Fisher stiffness means small diffusion, and low Fisher stiffness means broad diffusion.

The manuscript compresses that chain into “the Fisher metric is the diffusion kernel.” That loses the inverse, the pushforward, the change of space, and the late-data hypothesis. It then uses “stiff/sloppy” for its self and coupling matrices even though it has not defined a generative likelihood whose Fisher eigendirections are those sectors. Finally, it says its aggregation flow is opposite to BKS, while a later chapter correctly says that no common scale or operator comparison has been supplied.

These are repairable literature/bridge errors, not failures of the manuscript's proved Gaussian or RG algebra. The clean version is: BKS supplies a conditional information-geometric template; the present Gaussian realization has a suggestive component identity; the theorem connecting them is still open.
