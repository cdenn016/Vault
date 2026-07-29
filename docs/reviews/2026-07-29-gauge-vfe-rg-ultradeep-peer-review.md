# Ultradeep Peer Review: *Gauge-Covariant Variational Free Energy*

## Review record

- Manuscript: `manuscripts/gauge_vfe_rg/main.tex` and its twelve included chapters
- Specification: `manuscripts/gauge_vfe_rg/SPEC.md`
- Source revision: `1de9c213203e46ee02d793d2c465eb046e3f73f0`
- Review date: 2026-07-29
- Review worktree: `C:\tmp\Research-gauge-vfe-rg-review-20260729`
- Review branch: `codex/gauge-vfe-rg-review-20260729`
- Decision: **major revision**
- Scope: mathematical correctness, constructional rigor, probability semantics, geometry, information geometry, coarse-graining, RG dynamics, novelty, philosophical scope, source accuracy, and PDF production

This report reviews the manuscript as a tentative mathematical research program, not as a finished empirical theory. The standard applied is the one the manuscript adopts for itself: definitions must be typed, every theorem must remain inside its hypotheses, numerical observations do not prove mathematical claims, and an interpretive declaration cannot inherit the status of the algebra that motivates it.

## Executive assessment

The project is worth continuing. It has a real organizing contribution: it tries to put gauge-covariant population models, one normalized joint, one exact ELBO, correlated Gaussian recognition, aggregation, and RG language inside one explicitly typed construction. Several parts are unusually careful and survive close review. The directed-joint normalization argument, the exact ELBO after a density version is fixed, the Gaussian information-form calculations, the global interaction-family balance condition, the block mean-field optimum, the basic aggregation identities, the scalar projective calculations, and the distinction among graph links, base connections, and pointwise comparisons are all useful.

The current manuscript is not yet mathematically secure at the point where its title makes its strongest promise. Its proposed \(A=0\) RG fixed ray is a singular Laplacian quadratic form. It is not a normalized Gaussian recognition law on the declared Lebesgue space, has no finite log normalizer or Fisher metric, and does not support the exact ELBO as currently typed. At that same ray the proposed generalized pencil is singular; after the consensus kernel is removed, the pair is \((\bar L,\bar L)\) and all generalized eigenvalues are \(1\), so the advertised low-frequency spectral label disappears. The two main “fixed-point law” invariants therefore fail together.

A second foundational issue occurs in the bundle convention. With a right principal action, the stated quotient convention and \(u_i=\sigma_0\!\cdot U_i\) make the \(j\)-to-\(i\) transition \(U_i^{-1}U_j\), not the manuscript’s \(\Omega_{ij}=U_iU_j^{-1}\). Most downstream residual formulas reveal the intended convention and can probably be preserved by changing the frame parametrization to \(u_i=\sigma_0\!\cdot U_i^{-1}\), then correcting the reference-change law. This is repairable, but it must be repaired before claims of associated-bundle covariance are treated as established.

The RG chapter is presently a strong operator-level research proposal rather than a theorem about normalized VFE laws or universality. The natural full matrix coupling cone has invariant matrix-range faces, so sum-only aggregation cannot be primitive there for \(K>1\). A finite population has an atomic spectral measure, not a density with a small-\(d\) exponent. The blocking changes dimension and becomes a dynamical system only after a hierarchical identification is supplied. Component preservation is proved, but convergence to one fixed point, uniqueness, and scheme independence are not; the manuscript nevertheless promotes those conclusions to `ESTABLISHED` in later prose and status tables.

My recommendation is not to abandon the line. It is to split the theory into two layers:

1. an algebraic/operator RG on positive-semidefinite interaction forms, where the \(A=0\) ray legitimately lives; and
2. a proper probabilistic theory, obtained either by retaining a mass/pinning sector or by rebuilding the Gaussian law, base measure, ELBO, Fisher geometry, and coarse maps on the consensus quotient.

That split turns the main defect into a productive program. It also makes clear which extensions are genuinely new: the novelty is most plausible in a gauge-typed synthesis and in the compatibility theorems among its layers, not in pinning Gaussian free fields, generalized-pencil theory, Perron–Frobenius theory, scalar Kron reduction, or Gaussian coordinate-ascent convergence separately.

## Review protocol

### Ten specialist assignments

The review used ten distinct specialist assignments in staggered waves. The platform allowed three reusable expert-agent slots in parallel, so the ten experts were assignments rather than ten simultaneously resident processes. Every assignment read the source revision directly and worked read-only.

| No. | Specialist lens | Principal question |
|---:|---|---|
| 1 | Gauge theory, principal bundles, and topology | Are the actions, quotient conventions, transition maps, holonomies, and trivialization claims mutually consistent? |
| 2 | Measure theory, probability kernels, and exact ELBOs | Are the joint, posterior, density, absolute-continuity, and evidence claims version-invariant and correctly scoped? |
| 3 | Matrix analysis and coarse-graining | Do the matrix cones, Schur complements, aggregation rules, and proposed closure results hold? |
| 4 | Information geometry and spectral theory | Are the Fisher charts and generalized spectra regular on the claimed domain and meaningful at the fixed ray? |
| 5 | Perron–Frobenius and RG dynamical systems | Is there a typed endomorphism, primitive cone map, contraction, basin, fixed ray, or universality result? |
| 6 | Gaussian graphical models and cyclic normalization | Which precision claims define proper laws, and which cyclic or factorwise conclusions are too broad? |
| 7 | Literature, novelty, and constructive extensions | Which ingredients are known, which combination may be original, and which open questions already have answers? |
| 8 | Philosophy of science and falsifiability | Which interpretations are declarations, which conclusions are testable, and where are status upgrades unsupported? |
| 9 | Cross-manuscript notation, status, sources, and production | Are symbols, hypotheses, status registers, references, and the compiled artifact internally consistent? |
| 10 | Adversarial skeptic and final adjudicator | Can each high-severity finding be rescued, refuted, narrowed, or verified from primary evidence? |

### Mechanical and source checks

- The source was reviewed in a clean worktree at the exact revision above; the live Research vault and its unrelated work in progress were not modified.
- `latexmk` encountered the installed TeX Live `tlu` “attempt to concatenate a nil value” failure. A direct `pdflatex`/BibTeX/`pdflatex` fallback produced a 185-page PDF with resolved citations and references.
- The build log reports five floats too large for a page: Chapter 7 line 338, Chapter 9 line 661, Chapter 10 line 475, Chapter 11 line 292, and Chapter 12 line 152.
- Rendered inspection confirms that several status-register tables cross the footer and are clipped. These are production defects, not merely log warnings.
- Exact symbolic checks were performed for the singular pencil, a regularized pencil, the matrix Kron counterexample, the normalizer curvature, the rank-face obstruction, and the Gaussian star iteration. Numerical agreement was used only as corroboration of derivations.
- Primary literature was checked for pinned/quotient Gaussian fields, singular pencils, Perron–Frobenius theory on positive maps, scalar and sheaf Kron reduction, integrated density of states, and Gaussian coordinate descent.
- A machine-validated evidence claim ledger accompanies this report in `.verification/ledger.json`.

## What survives the review

The following results or constructional choices survived the specialist sweeps in their stated domains:

- reverse-topological composition of normalized kernels gives one normalized directed joint;
- after a density/kernel version is fixed at the selected observation, the single-ELBO identity and KL gap are algebraically exact;
- the total-correlation proof has the correct accounting and sign, although the proposition's prose reverses which named objective is larger;
- the Gaussian log normalizer, moments, conditionals, and information-form block assembly are correct;
- Proposition 6.11’s global balance condition for membership in the interaction family is correct;
- the Gaussian block-restriction optimum, determinant gap, underdispersion result, and mean-tie Schur-complement cost are correct;
- the interaction energy identity and exact kernel criterion are correct;
- aggregation closure in the flat, fixed-\(K\) interaction family, semigroup composition, pair-merge factorization, and biadditive functional equation are correct;
- congruence preserves a regular generalized pencil, and the determinant scaling in Proposition 10.9 is correct when the pencil is regular;
- Proposition 10.11’s Sylvester classification is correct for one positive-semidefinite matrix under full congruence;
- the reciprocal-pair kernel and determinant formulas are correct;
- the Gaussian star precision-addition update is correct;
- the manuscript often does separate graph-link holonomy, pointwise comparison products, and smooth-connection holonomy explicitly; a panel suggestion that it collapsed all three was rejected after direct inspection of `02_geometry.tex:408-469`.

These strengths are substantial. The required revision is concentrated at the seams where the manuscript moves from an operator to a probability law, from finite data to a thermodynamic density, from a dimension-changing sequence to a dynamical system, and from a conditional mathematical statement to an interpretive conclusion.

## Claim-status audit

The table distinguishes the manuscript’s claim from this review’s verdict. `REFUTED` here means that the statement as written has a current counterexample or derivation against it; it does not mean that every nearby, weaker statement is false.

| ID | Manuscript claim or status | Review verdict | Severity | Minimal disposition |
|---|---|---|---|---|
| R1 | The \(A=0\) fixed ray is an effective Gaussian law/fixed point of the VFE construction | `REFUTED` as a normalized law; valid as a PSD operator ray | High | Pin, quotient, retain a mass, or relabel it |
| R2 | The associated-bundle convention yields \(\Omega_{ij}=U_iU_j^{-1}\) from \(u_i=\sigma_0U_i\) | `REFUTED` | High | Use \(u_i=\sigma_0U_i^{-1}\) and repair reference changes, or invert all downstream transports |
| R3 | Proposition 10.9 supplies \(NK\) generalized eigenvalues at the fixed ray | `REFUTED` at that ray | High | Restore regular-pencil hypotheses or define a quotient pencil |
| R4 | A low-\(d\) spectral density/exponent labels the finite fixed point | `REFUTED` at the fixed ray and ill-typed at finite \(N\) | High | Use an SPD reference form and a thermodynamic IDS |
| R5 | Sum-only aggregation may be primitive on the intended full matrix coupling cone | `REFUTED` for \(K>1\); literal existential wording is under-specified | High | Scalarize, quotient with a proved metric, or add internal mixing |
| R6 | Proper projection gains are cases of the declared invertible directed model, and Hypothesis 6.13 excludes every nonprojection gain | `REFUTED` | Medium-high | Separate relaxed factorwise, invertible factorwise, and global conditions |
| R7 | Full matrix-weighted Kron closure remains open | `REFUTED` as an open full-family question | Medium-high | Record the counterexample; study closed subfamilies |
| R8 | The selected-observation ELBO is a measure-level statement independent of density versions | `REFUTED` without an a.e. or version declaration | Medium | State it marginal-a.e. through an RCP, or make the version part of the model |
| R9 | Every cyclic closure/fold in the stated broad sense is inadmissible | `REFUTED` in that breadth; the flat unanchored reciprocal-pair result is correct | Medium | Scope the no-go to the analyzed architecture |
| R10 | Component preservation implies one reached fixed point and no observable class variation | `REFUTED` | High | Make conditional on convergence, uniqueness, and scheme independence |
| R11 | Open 2.32 is unsettled | `REFUTED` by a one-dimensional counterexample | Medium | Close negatively |
| R12 | Gaussian-star fixed-point existence and convergence are open | `REFUTED` for the displayed exact Gaussian updates | Medium | Add the direct contraction theorem |
| R13 | A proper closed subset of posterior support necessarily causes infinite reverse KL | `REFUTED` | Medium | Replace by a posterior-null support condition |
| R14 | The normalizer force pushes the scalar transport toward identity | `REFUTED`; sign is reversed for the displayed term | Medium | Correct the sign and distinguish coordinate from model changes |
| R15 | The fixed-point/physical-law interpretation currently yields a falsifiable physical theory | `INCONCLUSIVE`; the only proposed empirical residue is still open | High | Declare an empirical domain and risky cross-scale protocol |
| R16 | A pointwise graph coboundary recovers global bundle triviality | `REFUTED`; it does not supply a smooth Čech zero-cochain | Medium-high | Treat global triviality as a prior hypothesis |
| R17 | Proposition 2.31 proves that local disagreement can induce nontrivial base holonomy | `REFUTED` as an implication of that proposition | Low-medium | Give an explicit curved example or leave the possibility open |
| R18 | The manuscript satisfies its own epistemic-status and numerical-reproducibility contract | `REFUTED` | Medium-high | Repair the taxonomy, coverage, registers, seeds, and reproduction package |
| R19 | Proposition 5.2's named free-energy comparison has the displayed total-correlation sign | `REFUTED` in the statement; proof algebra is correct | Low | Distinguish substituted free energy from negative pseudo-ELBO |
| R20 | Proposition 3.9's density criterion applies directly to the subspace-supported law | `REFUTED` outside its domination hypotheses | Low-medium | Use the direct null-set argument |
| R21 | Nonconstant \(Q\mapsto P_{\theta,Q}\) forces moving evidence and the stated ELBO consequences | `REFUTED` | High | Replace with a no-distinguished-target statement or add hypotheses |

## Adversarial adjudication

The final specialist was asked to steelman every principal finding and reject findings that depended on rhetoric, an avoidable interpretation, or a stronger claim than the manuscript actually makes. The binding calibration was:

| Finding | Verdict on the review finding | Calibrated severity | Strongest rescue tested |
|---|---|---|---|
| \(A=0\) fixed ray is outside the normalized Gaussian/ELBO family | Verified | High, not critical | It is valid as a projective boundary operator, but that does not supply a normalized law, evidence, posterior, or ELBO |
| Right-principal frame/transition convention is inverted | Verified | High | \(u_i=\sigma U_i^{-1}\) repairs the intended link algebra, provided the reference-change laws change too |
| Fixed-ray generalized pencil and spectral exponent fail | Verified | High | Pinning/quotienting can regularize the pair, but at the ray the quotient spectrum is still all \(1\); a nontrivial exponent also needs a large-\(N\) measure |
| Full-matrix-cone primitivity | Verified on the natural full cone | High | A scalar/restricted cone can satisfy the literal existential conjecture, so Conjecture 10.8 itself is inconclusive until its cone is fixed |
| Projection/nonprojection claims | Verified | Medium-high | Singular factor-local gains admit proper projections; declared invertible gains do not; global assembly admits cancellation |
| Selected-\(o\) density ELBO version dependence | Verified | Medium | An almost-everywhere statement or a declared canonical version repairs the theorem |
| Cyclic no-go and normalizer force | Verified after narrowing | Medium | The flat rootless reciprocal pair fails; generic anchored globally normalized cyclic Gaussians need not |
| Unrestricted matrix-Kron closure | Verified negative | Medium-high | Commuting/simultaneously diagonalizable subfamilies remain plausible positive cases |
| Component preservation upgraded to convergence/one fixed point | Verified | High | A new contraction, uniqueness, and scheme-independence theorem would be required |
| Graph holonomy globally conflated with Čech/base topology | Broad finding rejected; local instances verified | Medium locally | Chapter 2 makes the distinctions; `02_geometry.tex:487` and Chapter 12 cross them without a bridge |
| Open 2.32 universal converse | Verified negative | Medium | No stated restriction excludes the flat averaged-connection counterexamples |
| Proposition 4.5 moving-target necessity theorem | Verified false | High | Requiring the observation marginal itself to vary repairs only one premise, not all asserted ELBO consequences |

The final ranking, after this calibration, is:

1. the right-principal frame/transition mismatch;
2. the upgrade from component preservation to convergence, one fixed point, and no class variation;
3. the singular fixed-ray pencil and invalid spectral-exponent construction;
4. Proposition 4.5's moving-target ELBO necessity theorem; and
5. the use of the \(A=0\) boundary ray as a normalized Gaussian/ELBO law.

The adjudicator also reduced several local defects: the total-correlation issue is a low-severity wording/sign attribution because the displayed proof is correct; the subspace-density application is low-to-medium because a later direct proof establishes the intended infinite-KL conclusion; and Proposition 2.31's holonomy sentence is a proof-attribution gap rather than evidence that the desired curved example is impossible.

## Major comments

### 1. The proposed fixed point is outside the manuscript’s probability space

**Locations:** `06_gaussian.tex:13-38,93-118`; `09_coarsegraining.tex:306-317`; `10_renormalization.tex:136-170,390-394`; compare `11_obstructions.tex:35-45`

**Severity:** high

Chapter 6 defines the recognition family by
\[
q(y\mid h,J)=
\exp\!\left(h^\top y-\frac12y^\top Jy-\mathsf A(h,J)\right),
\qquad J\succ0,
\]
with \(J^{-1}\) and \(\log\det J\) in the log normalizer. The proposed fixed ray in Chapter 10 sets every self term \(A_i=0\), hence \(J=\Lambda=L\). Proposition 6.5 itself gives
\[
L(\mathbf 1_N\otimes v)=0
\qquad\text{for every }v\in\mathbb R^K.
\]
Therefore \(\det L=0\). If \(h\) has a component along the nullspace, the exponent is unbounded in one direction; if it does not, the kernel is constant along that nullspace and has infinite Lebesgue integral. There is no normalized full-space Gaussian, covariance \(L^{-1}\), finite log normalizer, or Fisher metric at the ray.

This is not an edge case. It is the exact point the manuscript calls scale free and later interprets as an effective law. The manuscript applies the same argument correctly to the reciprocal fold in `11_obstructions.tex:43-45`: a singular precision does not define a normalized law. The two chapters must use one standard.

The statement in `09_coarsegraining.tex:315` that a positive-semidefinite coarse operator is a “valid Gaussian model” has the same defect. The correct implication is only that it is a valid nonnegative quadratic form. For a full-space Gaussian one needs
\[
S^\top\Lambda S\succ0
\quad\Longleftrightarrow\quad
\operatorname{range}(S)\cap\ker\Lambda=\{0\}.
\]

**Repair options**

1. **Operator-only repair.** Call \(A=0\) a boundary fixed ray of interaction quadratic forms. Do not call it a Gaussian recognition law, an ELBO state, or a point of the Fisher manifold.
2. **Pinned or massive repair.** Retain an SPD global-mode prior or pin enough coordinates to remove the complete kernel. This preserves a proper full-space or affine-subspace law but changes the exact fixed ray.
3. **Quotient repair.** Work on
   \[
   \mathbb R^{NK}/(\mathbf1_N\otimes\mathbb R^K)
   \quad\text{or a chosen orthogonal complement,}
   \]
   assume the remaining kernel is absent, and use the induced Lebesgue measure and pseudodeterminant there. Then rederive the recognition kernel, absolute-continuity hypotheses, ELBO, Fisher geometry, and coarse maps on that space. A pseudoinverse written inside the existing full-space density is not a normalization.

Pinned and zero-average Laplacian Gaussians are standard; a useful primary model is Cipriani and van Ginkel’s zero-average discrete Gaussian free field, which inverts the Laplacian on the orthogonal complement of constants ([arXiv:1809.03382](https://arxiv.org/abs/1809.03382)). The possible contribution here is a gauge-compatible quotient construction that remains coherent under blocking.

**Falsification condition:** exhibit either a finite Lebesgue log normalizer for \(J=L\) on \(\mathbb R^{NK}\), or an already declared quotient/pinning construction used consistently in Chapters 5, 6, 8, 9, and 10. Neither is present at the reviewed revision.

### 2. The principal/associated-bundle conventions are inverse to the transport formulas

**Locations:** `02_geometry.tex:21-40,79-102,184-214`; downstream examples include `06_gaussian.tex:141-149`

**Severity:** high

The manuscript declares:

- a right principal action \(u\mapsto u\cdot g\);
- \(u_i=\sigma_0\cdot U_i\);
- the associated-bundle relation \((u\cdot g,b)\sim(u,g\cdot b)\); and
- \(\Omega_{ij}=U_iU_j^{-1}\) as the transport from agent \(j\) to agent \(i\).

On an overlap, the transition \(t_{ij}\) defined by \(u_j=u_i\cdot t_{ij}\) is instead
\[
t_{ij}=U_i^{-1}U_j.
\]
With the stated quotient, equality
\[
[u_j,b_j]=[u_i,b_i]
\]
therefore gives \(b_i=t_{ij}\cdot b_j=(U_i^{-1}U_j)\cdot b_j\). The transition induced by the associated bundle is not the manuscript’s \(\Omega_{ij}\).

The downstream formulas show which convention was intended. In particular, the reference coordinate \(z_i=U_i^{-1}\mu_i\) and the residual identity
\[
\mu_i-\Omega_{ij}\mu_j=U_i(z_i-z_j)
\]
are consistent if the frame parametrization is
\[
u_i=\sigma_0\cdot U_i^{-1}.
\]
Under that parametrization, a per-agent reframing \(U_i\mapsto g_iU_i\) corresponds to \(u_i\mapsto u_i\cdot g_i^{-1}\), the transition becomes \(t_{ij}=U_iU_j^{-1}=\Omega_{ij}\), and the manuscript’s vertex law
\[
\Omega_{ij}\mapsto g_i\Omega_{ij}g_j^{-1}
\]
is recovered.

This minimal repair changes the reference-trivialization law. If \(\sigma_0\mapsto\sigma_0\cdot h\) while \(u_i\) is fixed, then \(U_i\mapsto U_i h\), and \(\Omega_{ij}\) is invariant, not globally conjugated. That behavior is also geometrically natural: a transition between two fixed sections does not depend on which third reference section was used to coordinatize them.

**Required action:** choose one convention and propagate it mechanically through Chapter 2 and the gauge-covariance sections. The smallest source change appears to be the inverse in `02_geometry.tex:30` plus the reference-change statements at lines 38 and 209. A broader inversion of every downstream \(\Omega\) is possible but more disruptive.

**Falsification condition:** derive \(U_iU_j^{-1}\) as the \(j\)-to-\(i\) associated-fiber transition from all four declarations above without changing one of them.

### 3. The fixed-point pencil is singular, and the proposed spectral label collapses

**Locations:** `08_infogeometry.tex:218-240`; `10_renormalization.tex:329-348,411-417,460-462`

**Severity:** high

Proposition 8.5 correctly works with a symmetric-definite pencil and assumes \(\Lambda\succ0\). Proposition 10.9 removes that hypothesis and defines \(d_1,\ldots,d_{NK}\) as roots of
\[
\det(L-d\Lambda)=0.
\]
At the proposed fixed ray \(\Lambda=L\),
\[
L-d\Lambda=(1-d)L,
\qquad
\det((1-d)L)\equiv0.
\]
The determinant is the zero polynomial, so there is no finite \(NK\)-element generalized spectrum in the asserted sense. Congruence still preserves the Kronecker structure of the singular pencil, but multiplying an identically zero determinant by \(\det(G)^2\) does not create roots. Singular-pencil algorithms first isolate a regular part; see Hochstenbach, Mehl, and Plestenjak ([arXiv:2208.01359](https://arxiv.org/abs/2208.01359)).

Quotienting the common kernel repairs regularity but not the proposed label. On a quotient where \(\bar L\succ0\), the fixed-point pair is
\[
(\bar L,\bar L),
\]
so every generalized eigenvalue is exactly \(1\). It has no low-\(d\) connectivity density.

The same collapse appears from an SPD regularization. Let \(\Lambda=L+\varepsilon R\) with \(R\succ0\), and let \(Lv=\lambda Rv\). Then
\[
Lv=d(L+\varepsilon R)v
\quad\Longrightarrow\quad
d=\frac{\lambda}{\lambda+\varepsilon}.
\]
Every positive mode moves to \(d=1\) as \(\varepsilon\downarrow0\); the common nullspace is indeterminate at the endpoint. If a limiting Laplacian density satisfies \(\rho(\lambda)\sim C\lambda^\gamma\), the transformed density for fixed \(\varepsilon>0\) is
\[
\omega_\varepsilon(d)=
\rho\!\left(\frac{\varepsilon d}{1-d}\right)
\frac{\varepsilon}{(1-d)^2}.
\]
The low-\(d\) window loses all mass when the self-mass is removed. The \(N\to\infty\), \(d\downarrow0\), and \(\varepsilon\downarrow0\) limits do not commute.

There is a separate finite-size defect. At finite \(N,K\), the spectral measure is
\[
\nu_N=\frac1{NK}\sum_{j=1}^{NK}\delta_{d_j},
\]
which is atomic and has no Lebesgue density \(\omega(d)\). A power-law exponent needs a declared graph/population sequence, normalized counting measures, convergence to an integrated density of states, treatment of exact zero atoms, and an order of limits. Even a limiting IDS need not have a density. Lenz and Veselić give a representative rigorous framework ([arXiv:0709.2836](https://arxiv.org/abs/0709.2836)).

**Recommended replacement**

- Introduce a separate SPD, gauge-covariant reference or mass form \(R\) and study the regular pair \((L,R)\).
- Remove or pin consensus modes consistently with the probability construction.
- Define a thermodynamic family \((V_n,L_n,R_n)\), normalized cumulative counting functions, and a convergence mode.
- Define the exponent cumulatively,
  \[
  N(t)-N(0)\sim Ct^\alpha,
  \]
  and use \(\gamma=\alpha-1\) only after absolute continuity near zero is proved.
- State the order of the \(n\to\infty\), mass-to-zero, and spectral limits.

**Falsification condition:** produce a regular pencil with a nontrivial low-\(d\) spectrum at the exact \(A=0\) ray, or identify a declared thermodynamic limit and density already in the manuscript.

### 4. The Perron–Frobenius program cannot work on the natural full matrix cone without internal mixing

**Locations:** `10_renormalization.tex:179-286`

**Severity:** high

On the coupling sector, the declared aggregation map only sums edge matrices. After any fixed relabeling it has the form
\[
T=B\otimes I_{\operatorname{Sym}^K},
\]
where \(B\ge0\) acts on spatial/edge coordinates and the matrix direction is untouched.

For \(K>1\), choose a nonzero \(u\) and set
\[
W_e=a_euu^\top,\qquad a_e>0.
\]
Every iterate remains of the form
\[
(T^qW)_f=
\left(\sum_e(B^q)_{fe}a_e\right)uu^\top.
\]
No power enters the positive-definite interior. Completeness of the quotient graph does not remove this invariant matrix-range face.

There is also no unique raw Hilbert ray. If \(c>0\) is a Perron vector of \(B\), then \(c\otimes M\) is an eigenray for every \(M\succ0\). For
\[
M_t=\operatorname{diag}(t,1,\ldots,1),
\]
the Hilbert distance between \(c\otimes I\) and \(c\otimes M_t\) grows like \(\log t\), so the image diameter is unbounded. Congruence may later identify positive-definite \(M\) matrices as physically equivalent, but Birkhoff’s theorem acts on the raw ordered cone; no ordered cone or Hilbert metric has been constructed on the congruence quotient.

The manuscript’s literal Conjecture 10.8 is existential and can evade formal contradiction by selecting \(K=1\) or the scalarized cone
\[
\mathcal K^W_{M_0}
=\{(w_eM_0)_e:w_e\ge0\}
\]
for one fixed \(M_0\succ0\). That is a viable theorem, but it is a scalar spatial Perron–Frobenius result with a frozen internal matrix, not attraction on the full declared matrix family. If full matrix directions are meant to mix, the map needs an internal positive operation, for example a genuinely primitive positive or completely positive matrix map. Primitive positive-map results formalize exactly the missing full-rank condition; see Sanz et al. ([arXiv:0909.5347](https://arxiv.org/abs/0909.5347)) and Rahaman ([arXiv:1807.06872](https://arxiv.org/abs/1807.06872)).

**Required action:** state the cone \(\mathcal K^W\) explicitly. Prove the fixed-\(M_0\) theorem if that is the intended scope, or add and justify a fiber-mixing mechanism. Do not list sparsity as the only remaining obstruction.

**Falsification condition:** apply a power of the present sum-only map to an input whose every edge matrix has range \(\operatorname{span}(u)\), and obtain a positive-definite matrix in every output coordinate.

### 5. The measure-theoretic ELBO needs an observation-version repair

**Locations:** `03_probability.tex:95-112,165-180`; `04_generative.tex:81-105,373-390`; `05_elbo.tex:75-177,249-279`

**Severity:** medium

Definition 3.6 correctly says Radon–Nikodym densities are determined only up to a reference-measure null set. Theorem 5.6 then fixes an arbitrary selected observation \(o\) and uses point values
\[
p_\theta(o,y\mid X),\qquad
p_\theta(o\mid X),\qquad
P_\theta(dY\mid o,X).
\]
Those objects are not determined at every individual \(o\) by the joint measure.

A direct counterexample is enough. Let a joint density be \(p(o,y)=\phi(o)\phi(y)\) on \(\mathbb R^2\). Changing only the slice \(o=0\) to
\[
\tilde p(0,y)=\phi(0)\psi(y)
\]
for an arbitrary probability density \(\psi\) changes the density only on a two-dimensional Lebesgue-null set, so it represents the same joint probability measure. At the selected point \(o=0\), however, it changes the displayed posterior from \(\phi\) to \(\psi\), and therefore changes the KL gap and the pointwise ELBO. A different null-slice modification can change the evidence-density value as well. Corollary 4.11 itself states evidence invariance only for \(\nu_D^O\)-almost every \(o\), which exposes the mismatch with the later all-selected-\(o\) grammar.

There are two clean repairs:

1. state the posterior and ELBO identity for observation-marginal-almost-every \(o\), using a regular conditional probability; or
2. declare a particular jointly measurable density/conditional version as part of the model data, with continuity or another selection condition if point evaluation is intended.

The finite spaces used are standard Borel, so regular conditional distributions exist, but they are still unique only almost surely. A general source on existence assumptions is Faden ([DOI: 10.1214/aop/1176993081](https://doi.org/10.1214/aop/1176993081)).

Two neighboring claims also need correction:

- Proposition 5.11’s exact block E-coordinate proves preservation of absolute continuity, but it does not prove Hypothesis H4’s log-integrability. A heavy-tailed complement marginal can make the claimed ELBO expectations undefined. Add H4 for the new law or state the result first as a KL-chain-rule minimization in extended values.
- `07_restrictions.tex:39-40` says support on any proper closed subset of posterior support forces infinite KL. This is false. If \(P\) is uniform on \([0,1]\) and \(Q\) uniform on \([0,\tfrac12]\), the support is a proper closed subset while \(Q\ll P\) and \(\mathrm{KL}(Q\Vert P)=\log2\). The correct condition is support on a posterior-null set, such as a lower-dimensional affine subspace under a nondegenerate Lebesgue posterior.

**Falsification condition:** show that every Radon–Nikodym version of the same joint gives the same displayed posterior and ELBO at every selected observation, rather than only almost everywhere.

### 6. The Gaussian interaction restriction confuses local, global, and invertible cases

**Locations:** `04_generative.tex:191-220`; `06_gaussian.tex:120-162,214-247`

**Severity:** medium-high

Proposition 6.12 is a correct algebraic characterization of when one isolated receiving factor belongs to the two-node interaction family:
\[
T_i^2=T_i,\qquad
\Lambda_iT_i\succeq0\ \text{and symmetric}.
\]
The problem is its use.

First, the directed model declared immediately before it has
\[
T_i=G_i\Omega_{ij}\in\mathrm{GL}(K).
\]
An invertible idempotent is the identity. Therefore the proper projection cases of ranks \(0,\ldots,K-1\), including the numerical controls at `06_gaussian.tex:244`, lie outside that stated model. Within the invertible model, isolated factorwise membership reduces to \(T_i=I\).

Second, Hypothesis 6.13 says the later interaction family excludes every coupling whose trivialized gain is not a projection, citing Propositions 6.10 and 6.12. This contradicts Proposition 6.11, which correctly permits cancellations among a root prior, a parent deficit, and child surpluses in the assembled precision.

The scalar witness is:
\[
\Lambda_i=1,\qquad T_i=\tfrac12,\qquad \Lambda_{\rm root}=1.
\]
The joint precision is
\[
J=
\begin{pmatrix}
1&-\tfrac12\\[2pt]
-\tfrac12&\tfrac54
\end{pmatrix},
\]
which belongs to the interaction family with
\[
W=\tfrac12,\qquad A_i=\tfrac12,\qquad A_{\rm root}=\tfrac34,
\]
although \(T_i^2\ne T_i\). Thus global interaction-family membership does not require every factor to belong locally.

There is also a cross-chapter type drift: Chapter 4 explicitly permits a rank-deficient conditional mean map, while Chapter 6 replaces it by \(G_i\in\mathrm{GL}(K)\) without explaining that narrower model. Either scope can be used, but the theorem and controls must use the same one.

**Required replacement**

- A relaxed factor theorem: with singular gains permitted, isolated membership is equivalent to the projection condition.
- An invertible factor corollary: in the Chapter 6 \(\mathrm{GL}(K)\) model, isolated membership is equivalent to \(T_i=I\).
- A global theorem: assembled membership is exactly Proposition 6.11’s balance condition.
- A separate factorwise-agreement hypothesis if the author wants every local kernel to have the agreement form. That is stronger than membership of the assembled recognition precision.

**Falsification condition:** show that the displayed scalar joint fails one of Definition 6.4’s sign or row-sum requirements.

### 7. The cyclic obstruction is correct for the flat unanchored pair, not for all cyclic normalized models

**Locations:** `04_generative.tex:107-171`; `11_obstructions.tex:4-100,145-171,173-245`

**Severity:** medium after narrowing

Proposition 11.1 and Corollary 11.2 are correct:
\[
\ker J=
\{(\Omega_{uv}v,v):v\in\ker(H-I)\},
\]
and under the flat cocycle \(H=I\), the unanchored reciprocal pair is singular. The manuscript then uses this result to support “cyclic closure is inadmissible,” “every version of this fold fails,” and a broad claim that the cyclic escape is unavailable.

That generalization is too strong. Adding SPD anchors produces
\[
J_{\rm proper}
=J+\operatorname{diag}(P_u,P_v)\succ0,
\]
which defines a normalized cyclic undirected Gaussian if the global partition function is retained. Nontrivial holonomy can also make the unanchored pair definite, as the manuscript later proves. What fails is the more specific architecture: a flat, rootless reciprocal agreement fold treated through local kernels or an objective that omits the global normalizer, while also demanding the flat aggregation family.

The parameter-dependent normalizer is a cost, not a nonexistence theorem. A globally normalized Markov random field is a legitimate joint. It no longer has the directed-local-normalization convenience of Chapter 4, and it may not be closed under the chosen aggregation, but those are narrower conclusions.

The claimed direction of the scalar normalizer force is also reversed. With \(h=0\),
\[
D(a)=p_0^2+p_0(a+a^{-1})^2,\qquad
\mathsf A(a)=-\frac12\log D(a)+\text{const},
\]
and on \(\mathrm{GL}^+(1)\), \(a>0\),
\[
\mathsf A'(1)=0,\qquad
\mathsf A''(1)=-\frac4{p_0+4}<0.
\]
The identity is a strict maximum of this log-normalizer contribution. Minimizing the negative log density or negative ELBO pushes away from \(a=1\) when this term is isolated, not toward it. The complete force can also include the quadratic/data term, so no universal direction follows from the determinant witness alone. The manuscript’s second minimizer \(a=-1\) lies outside \(\mathrm{GL}^+(1)\).

Finally, varying \(a\) while holding a coordinate-isotropic self prior fixed is not a pure gauge orbit. Under a genuine reframing, the prior precision and base-measure coordinates transform as well. Nonconstancy under a change of model transport can be established; a “force on gauge freedom” requires a gauge-invariant parameter variation and is not established by this witness.

The discussion of Bayesian renormalization at `11_obstructions.tex:85-93` should also be resourced more narrowly. Berman, Klinger, and Stapleton declare a prior and likelihood and study posterior/model-space flows; their construction is not, merely because a posterior flows, a generative kernel that reads its own posterior. Different scale values do correspond to different effective descriptions, but the paper’s \(T=0\) Bayesian endpoint is not automatically the extrapolated improper Gaussian claimed here. See the primary paper ([arXiv:2305.10491](https://arxiv.org/abs/2305.10491)).

**Required action:** retitle the no-go around the analyzed flat reciprocal Gaussian fold; distinguish directed cyclic conditionals, globally normalized undirected factors, auxiliary-latent DAGs, and inference fixed-point cycles; retain the exact kernel theorem; correct the normalizer sign and source reading.

**Falsification condition:** prove a no-go over a declared class that includes SPD-anchored globally normalized cyclic Gaussian models.

### 8. The full matrix-weighted Kron question is already closed negatively

**Locations:** `06_gaussian.tex:272-278`; `09_coarsegraining.tex:604-610,657`; `10_renormalization.tex:423-425,470`

**Severity:** medium-high as an incorrect `OPEN` status; constructive as an extension

Take three agents with \(K=2\),
\[
A_1=A_2=A_3=I_2,\qquad W_{12}=0,
\]
\[
W_{13}=
\begin{pmatrix}1&0\\0&2\end{pmatrix},
\qquad
W_{23}=
\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\]
The fine precision is SPD because every node has the anchor \(I_2\). The block eliminated at node \(3\) is
\[
D=I_2+W_{13}+W_{23}
=\begin{pmatrix}4&1\\1&5\end{pmatrix}.
\]
Elimination manufactures the \(1,2\) weight
\[
W_{13}D^{-1}W_{23}
=\frac1{19}
\begin{pmatrix}9&3\\4&14\end{pmatrix},
\]
which is nonsymmetric. Hence the Schur complement leaves the interaction family. Exact symbolic arithmetic gives determinant \(233\) for the full fine precision, so no singularity is hiding in the witness.

Chapter 6 already contains the general commutation/symmetry obstruction; Chapters 9 and 10 nevertheless keep the explicit \(K=2\), three-agent counterexample as open. The surrounding literature also records general sheaf/matrix-weighted nonclosure, while retaining one-dimensional stalk closure; see Hansen and Ghrist ([arXiv:1808.01513](https://arxiv.org/abs/1808.01513)). Scalar loopy-Laplacian Kron closure is standard; see Dörfler and Bullo ([arXiv:1102.2950](https://arxiv.org/abs/1102.2950)).

A useful positive theorem remains:

> If all \(A_i\) and \(W_{ij}\) are simultaneously diagonalized by one orthogonal matrix, the precision decomposes into \(K\) scalar loopy Laplacians; arbitrary vertex elimination is Kron-closed channel by channel.

Sharing an eigenbasis only among edge weights is not enough if the anchors fail to share it.

**Required action:** close the unrestricted question negatively, add the exact witness, and replace the open item by classification of maximal Kron-closed subfamilies.

**Falsification condition:** show that one displayed matrix is not SPD/PSD as stated, that the fine precision is not SPD, or that the manufactured off-diagonal block is symmetric.

### 9. The manuscript upgrades decomposition and declarations into convergence, universality, and ontology

**Locations:** `01_introduction.tex:19-83`; `10_renormalization.tex:129-175,259-264,354-394,429-472`; `12_philosophy.tex:103-123`

**Severity:** high for the convergence upgrade and empirical/ontological scope

Proposition 10.12 proves block decomposition across connected components and preservation of that decomposition under non-straddling aggregation. It does not prove that an orbit converges, that a component has one fixed ray, that the ray is independent of initialization or blocking, or that a spectral exponent is the only continuous label.

The manuscript nevertheless says at `10_renormalization.tex:381` that coupled agents “hence reach one fixed point,” marks “no observable variation in the effective law” `ESTABLISHED` at line 467, and repeats the conclusion in Chapter 12. This directly conflicts with `10_renormalization.tex:259-264`, which says failure of contraction can leave several fixed rays within one connected population, and with Open Problem 10.5/Conjecture 10.8.

The correction is simple:

- component preservation implies one dynamically independent subsystem, not one reached limit;
- all fixed-point, shared-class, and class-inaccessibility conclusions must be conditional on a convergence theorem, uniqueness within the relevant basin, and blocking-scheme independence;
- equality of one exponent would not by itself identify a universality class, because limiting measures, amplitudes, correction exponents, mass profiles, and invariant faces can still differ.

The interpretive chapter adds a second unsupported step. “Agents directly observe other agents” is an observational-closure hypothesis. It does not entail the ontological claim at `12_philosophy.tex:110` that “there is nothing behind the appearances.” An unobserved environment can affect all agents even if every direct observation is another agent. The manuscript should separate:

1. observational closure;
2. the declaration that an RG fixed point is a physical law; and
3. ontological closure or absence of external causes.

Only the first enters the graph argument. The other two are independent hypotheses.

The manuscript is therefore a coherent formal research program, but not yet a falsifiable physical theory. Its only named empirical residue is cross-scale running, and the text correctly marks it open. There is no target empirical system, estimator for \(A_i,W_{ij},U_i\), noise model, rule matching one system across resolutions, preregistered blocking/rescaling protocol, baseline, or risky numerical prediction.

**Required action:** call the present object a rescaled blocking sequence or operator RG program until a fixed theory space and semigroup action are declared. Add a domain-of-application section before making physical-law claims. A serious empirical test should compare preregistered admissible blockings and require a held-out cross-scale statistic that an ordinary Gaussian graphical model or spectral baseline does not predict.

**Falsification condition:** a typed endomorphic flow with a proved basin, unique scheme-robust limit, and an operational cross-scale prediction would defeat the mathematical and empirical parts of this finding.

### 10. A moving model target does not force moving evidence or an improving ELBO

**Locations:** `04_generative.tex:81-105`

**Severity:** high

Proposition 4.5 infers from nonconstant dependence \(Q\mapsto P_{\theta,Q}\) that no single evidence value exists and that the associated ELBO comparison necessarily moves. That implication is false. Let \(R\) be a fixed observation law and define
\[
P_Q(do,dy)=R(do)\,Q(dy).
\]
The joint varies nontrivially with \(Q\), while every member has the same observation marginal \(R\). A Bernoulli specialization can keep the selected evidence fixed at \(1/2\) while the reverse KL changes and the ELBO improves, so even the proposition's asserted downstream alignment is not forced.

The defensible conclusion is narrower: a \(Q\)-indexed target family does not itself provide a distinguished fixed target or a fixed comparison certificate. That is a modeling-architecture objection, not a theorem that the observation evidence must change.

**Required action:** replace Proposition 4.5 with the narrower no-distinguished-target statement, or add hypotheses that force injective variation of the observation marginal and prove each desired consequence separately.

**Falsification condition:** derive the claimed evidence variation from the proposition's stated premise alone; the displayed factorized family prevents such a derivation.

## Secondary and local comments

### Open 2.32 has a one-dimensional counterexample

**Location:** `02_geometry.tex:430-467`

Let \(\mathcal C_0=\mathbb R\), \(G=\mathrm{GL}^+(1)\), \(u_1=\sigma\), and \(u_2=\sigma e^x\) on overlapping patches. The local connections for which the two sections are parallel differ: in the \(\sigma\) gauge their potentials may be written \(A_1=0\) and \(A_2=-dx\). Every convex partition-of-unity combination is a one-form on a one-dimensional base. Its curvature two-form is identically zero, even though the local connections disagree. Thus disagreement does not force nonzero curvature for every partition, and Open 2.32 should be closed negatively.

The word “canonically” at `02_geometry.tex:430` should also be removed: the global connection depends on the chosen partition of unity. Its existence is canonical only in the weak sense that some partition exists, not that the resulting connection is unique.

### The rescaling exponent is topology/blocking dependent

**Location:** `10_renormalization.tex:108-127,448`

The \(\zeta=b^2\) argument is exact for the dense homogeneous complete-graph reference family, where each coarse block pair receives \(b^2\) cut edges. It is not the unique nondegenerate scaling for sparse geometries. Consecutive blocks of a nearest-neighbor chain have one cut edge between adjacent coarse blocks, so \(W_{IJ}=W\) before rescaling and nondegeneracy requires \(\zeta=1\). Introduce a cut-growth exponent \(s\), with \(\#E(I,J)\asymp b^s\), and scope \(\zeta=b^s\) to a declared graph/blocking class.

Similarly, a fixed finite population permits only finitely many nontrivial merges. If \(N=b^m\), there are at most \(m\) equal-block steps before one node remains. The statement that eigenvalues or self terms “diverge without bound” requires a hierarchical/thermodynamic family; at fixed \(N\), the correct statement is a finite-step bound.

### Two information-geometric endpoint/type errors

**Locations:** `08_infogeometry.tex:20-30,233-240`

- If \(\eta_2=-J/2\) and \(J\succ0\), then the natural \(\eta_2\)-domain is \(\operatorname{Sym}_{--}\), not \(\operatorname{Sym}_{++}\). The \((h,J)\) chart has an SPD second component; the genuine natural coordinate has a negative-definite one.
- The proposition proves \(d=0\iff x\in\ker L\) and \(d=1\iff x\in\ker A\), but the next sentence says a direction constrained by no edge sits at \(d=1\). “No edge constrains it” means \(Lx=0\), hence \(d=0\). Replace “edge” by “self term.”

### Non-invariance does not mean no coordinate change can create family membership

**Locations:** `06_gaussian.tex:120-149`

The claim that no block-diagonal coordinate change can create the interaction family is false. Start with
\[
\Lambda_z=
\begin{pmatrix}
2I&-I\\
-I&2I
\end{pmatrix}\in\mathcal I
\]
and shear only the second block. The transformed off-diagonal block is nonsymmetric and leaves \(\mathcal I\); applying the inverse change creates membership again. The correct statement, which line 149 later gives, is that membership is not invariant under independent block-coordinate changes.

### Coarse diagonal blocks are not self terms

**Locations:** `09_coarsegraining.tex:136-147,488`

The coarse self term is \(A_I=\sum_{i\in I}A_i\). Cut weights appear in the full coarse diagonal block,
\[
(\Lambda_c)_{II}=A_I+\sum_{J\ne I}W_{IJ}.
\]
Replace statements that the self term includes cut weights by statements about the diagonal block.

### Graph-link structure is not yet bundle topology

**Locations:** `02_geometry.tex:408-425`; `12_philosophy.tex:37-54`

Chapter 2 explicitly separates pointwise comparison products, graph-link holonomy, and smooth-connection holonomy. Chapter 12 nevertheless says the noumenal reading becomes substantive “exactly when the bundle is non-trivial,” while the quantity it exhibits is the holonomy of independently declared graph links. The text later concedes that no graph embedding or path-transport equality exists. The conclusion should therefore say “when the declared graph-link structure is nontrivial.” Any inference to base-bundle topology remains under Open 2.16.

The pointwise implication at `02_geometry.tex:487` should also be removed. A graph coboundary at one common context does not supply the smooth Čech zero-cochain on every overlap required by Proposition 2.19. In the present setup, Hypothesis 2.14 already presupposes the globally trivializing coordinates \(U_i\) introduced by Hypothesis 2.10; it does not recover global bundle triviality from the pointwise graph product.

### Proposition 2.31 does not prove nontrivial induced base holonomy

**Locations:** `02_geometry.tex:430-469`; `12_philosophy.tex:50-54`

Proposition 2.31 constructs a global connection by averaging local connection forms and gives a sufficient condition for that averaged connection to be flat. The failure of a sufficient flatness condition does not prove nonzero curvature or holonomy. Yet the closing prose and Chapter 12 say the proposition shows that local disagreement can induce nontrivial base holonomy. Supply one explicit curved example, or change that statement to an open possibility. This correction is independent of the negative answer to Open 2.32: disagreement neither forces curvature nor rules it out.

### Frame symbols change mathematical type across chapters

**Locations:** `02_geometry.tex:21-38`; `04_generative.tex:260-269`

Chapter 2 defines \(u_i\) as a section into the principal bundle and \(U_i\in G\) as its group-valued coordinate. Chapter 4 instead declares \(u_i\in G\), sets \(U_i=\rho_k(u_i)\), and then reuses \(U_i\) in the link formula. Preserve the types by retaining \(u_i\) for the section and \(U_i\in G\) for its coordinate, with distinct represented matrices such as \(U_i^k=\rho_k(U_i)\) and \(U_i^m=\rho_m(U_i)\).

### Two density/ELBO statements need local correction

**Locations:** `03_probability.tex:143-166`; `05_elbo.tex:54-72,248-260`

Proposition 3.9 assumes that both measures are dominated by a declared reference measure, but its subspace-supported application uses a law that is not Lebesgue-dominated. Density values on a Lebesgue-null subspace are also version-dependent. Use the direct set argument \(Q(S)=1\), \(P(S)=0\), as Proposition 5.5 already does.

Proposition 5.2 also reverses the sign in its prose: replacing \(\log q\) with the sum of marginal log densities makes the substituted **free energy** smaller by total correlation, while its negative pseudo-ELBO is larger. The proof has the correct algebra; the proposition should name which of these two quantities it compares. The later exact E-coordinate additionally needs finite complement KL/Hypothesis 5.4, not merely complement absolute continuity.

### The status taxonomy and status registers need one mechanical source of truth

**Locations:** `SPEC.md:41-63,87`; `01_introduction.tex:19-97`; `06_gaussian.tex:268`; `09_coarsegraining.tex:1-620`; `11_obstructions.tex:143`; `12_philosophy.tex:1-6,116-121`

The specification permits six status values, while the Introduction adds `NOT-CLAIMED` as a seventh. The Introduction promises a tag on every nontrivial claim but leaves its substantive summary untagged and has no register, contrary to the requirement that every chapter end in one. Chapter 9 contains numerous seed-bearing body measurements but only one `NUMERICAL` tag; `06_gaussian.tex:268` is another untagged numerical assertion. The 300-draw statement at `11_obstructions.tex:143` supplies no seed. Chapter 12 says it contains exactly one `HYPOTHESIS` but uses the tag again at line 119, and it sometimes tags earlier mathematical consequences as `DEFINITION`.

Amend the specification to the intended taxonomy, add Chapter 1's register, tag every numerical and nontrivial assertion where made, and generate registers from a machine-readable claim ledger. Distinguish `DECLARATION` and `CONDITIONAL` if those are intended logical roles; do not make prose discipline carry dependency tracking.

### The displayed Gaussian star is not an open convergence problem

**Locations:** `07_restrictions.tex:118-124`; `11_obstructions.tex:102-128,160-164`

Let
\[
B=\sum_i\Omega_i^\top R_i^{-1}\Omega_i,\qquad
P_b=P_0+B.
\]
After exact constituent updates, the apex-mean error obeys
\[
e_b^{(t+1)}=(P_0+B)^{-1}B\,e_b^{(t)}.
\]
This map is similar to the symmetric matrix
\[
P_b^{-1/2}BP_b^{-1/2}
=I-P_b^{-1/2}P_0P_b^{-1/2},
\]
whose eigenvalues lie in \([0,1)\) because \(P_0\succ0\). The apex error therefore converges geometrically to a unique fixed mean, and factor covariances are fixed after one exact update. Replace the Gaussian open item with this theorem; reserve an open problem for delayed, noisy, asynchronous, or inexact schedules.

### Production defects affect the evidence/status apparatus

The compiled PDF is 185 pages and has no unresolved citations or cross-references after the direct build. Five status-register floats exceed page height, by approximately \(106\), \(500\), \(836\), \(368\), and \(68\) points. Rendered inspection shows content running below the footer, including the Chapter 10 register; the Chapter 9 table also forces an almost blank preceding page. Equation 2.24 exceeds the text width by about \(90.5\) points. Replace oversized floats with `longtable` or split registers by topic, and split the long equivalence into aligned lines.

The numerical results cannot be reproduced from this manuscript revision alone. Seed searches resolve to prose, but the manuscript subtree contains no scripts, data, dependency lock, or rerun command record. Add a versioned verification directory that records every numerical claim, seed, code revision, environment, command, and machine-readable result.

Three bibliography records also need production edits: an internal editorial note in `references.bib:1845` prints into the PDF; the Cohen et al. entry at line 3836 omits PMLR volume 97 and pages 1321--1330; and the Turner--Sahani entry at line 4259 omits pages 104--124 and its DOI. The Lee matrix-weighted-graph entry at lines 4156--4164 should be checked against the publisher record: DOI `10.1002/nla.2539` is listed there under Barry Lee alone, volume 31, issue 2, article e2539.

## Theory extensions worth pursuing

The following extensions are ranked by how directly they repair the theory and how much exact mathematics they can yield.

### 1. A gauge-compatible quotient Gaussian fixed point

For the biadditive ray \(W_{ij}=x_ix_jM\), let \(s=\sum_i x_i\). Then
\[
L=
\bigl(s\,\operatorname{diag}x-xx^\top\bigr)\otimes M.
\]
For \(x_i>0\) and \(M\succ0\),
\[
\ker L=\operatorname{span}\{\mathbf1\}\otimes\mathbb R^K.
\]
The first theorem should prove that \(L\) defines a proper Gaussian on the quotient by this kernel, with covariance \(L^+\) in a chosen complement, and that aggregation \(x_I=\sum_{i\in I}x_i\) preserves the quotient family. The second theorem should prove compatibility of quotient bases, measures, pseudodeterminants, and ELBOs across blocking.

This is the most direct route to making the proposed fixed point probabilistic. It must be done as a change of sample space, not by silently substituting a pseudoinverse.

### 2. A regular gauge-covariant mass-pencil universality theory

Declare an SPD form \(R\) that transforms by the same congruence as \(L\), and use the regular pencil \((L,R)\). For a thermodynamic family, define normalized cumulative spectral measures after consensus-mode removal. In the tractable family \(\Lambda=L+aR\),
\[
d=\frac{\lambda}{\lambda+a},
\qquad
N_d(t)=N_L\!\left(\frac{at}{1-t}\right).
\]
This gives an exact theorem transferring a cumulative Laplacian exponent to the generalized IDS for \(a>0\), while also proving the collapse at \(a=0\). It supplies the correct setting for spectral dimension, gaps, heat traces, and scheme-comparison tests.

### 3. A no-go theorem and a viable Perron–Frobenius theorem

Prove:

1. no map \(B\otimes I_{\operatorname{Sym}^K}\) is primitive on the full product PSD cone for \(K>1\); and
2. on \(W_e=w_eM_0\) with fixed \(M_0\succ0\), primitivity, Hilbert contraction, and the Perron ray are exactly those of the scalar spatial map \(B\).

If the author wants internal matrix mixing, introduce a positive map
\[
W_e\longmapsto\sum_r K_{er}W_rK_{er}^\top
\]
and state irreducibility/primitivity in the language of invariant faces. That would produce a genuinely matrix-valued RG rather than a spatial scalar RG carrying an inert fiber.

### 4. A matrix-Kron classification theorem

Record unrestricted nonclosure using the exact three-node witness. Then prove the positive theorem for a common orthogonal eigenbasis of all anchors and edge weights. The next research question is the maximal closed algebra: simultaneous diagonalizability, a commutative matrix \(*\)-algebra, or another condition stable under inversion and Schur complement.

This extension connects cleanly to scalar Kron reduction and cellular-sheaf Laplacians without claiming that the general block family is closed.

### 5. An enlarged non-flat pair-factor family

Replace the single invertible-link factor by a general PSD pair block
\[
Q_{IJ}=
\begin{pmatrix}
C&-B\\
-B^\top&A
\end{pmatrix}\succeq0.
\]
When \(C\succ0\), it has the exact oriented decomposition
\[
(z_I-C^{-1}Bz_J)^\top C(z_I-C^{-1}Bz_J)
+z_J^\top(A-B^\top C^{-1}B)z_J.
\]
Arbitrary PSD unary and pair blocks are closed under aggregation: internal pair factors become unary factors and cut pair factors add. This solves a closure problem by enlarging the category, at the cost of abandoning a necessarily invertible coarse group link. Cellular sheaves provide a natural language for variable stalk dimensions and restriction maps.

### 6. A three-level holonomy bridge theorem

Keep separate:

1. the Čech class of the principal bundle;
2. the representation variety of graph-link assignments modulo vertex gauge; and
3. the holonomy of a smooth base connection.

Then declare an embedding of the graph into the base and define edge links as actual parallel transports. Prove equality of loop products with path-ordered exponentials, followed by a refinement or approximation theorem. This would turn the current philosophical “signature of the base” into a mathematical statement and provide a controlled place for nontrivial topology.

### 7. Exact Gaussian-star coordinate-ascent rates

Promote the direct contraction above to a theorem for arbitrary information vector \(h\). Give parallel and sequential rates, convergence in mean and KL, and the effect of schedule choices. This closes a current open item with little additional machinery and provides a rigorous example of a participatory inference loop that actually converges.

### 8. A version-invariant kernel ELBO

State the exact identity in measure form through a regular conditional probability, for observation-marginal-almost-every \(o\). If an everywhere-defined pointwise functional is wanted, define an integrated or neighborhood-conditioned ELBO, or declare a continuous density version as model data. This extension would make the manuscript’s measure-first philosophy fully consistent with its inference theorem.

### 9. A continuum/projective-limit theory

Build a directed system of finite designs and Gaussian laws with compatible marginals. Establish tightness or an extension theorem on a declared section/distribution space, including the gauge action and reference measure. A gauge-covariant Gaussian random field on an associated vector bundle would be the natural continuum endpoint. This is a large program and should follow, not precede, the finite quotient repair.

### 10. A scheme-universality and falsifiability program

Declare a family of admissible blocking schemes and prove, or test with preregistered tolerances, which fixed-ray and spectral quantities are scheme independent. Pair this with one empirical domain, an estimation map from observations to \(A,W,U\), held-out cross-scale predictions, and ordinary Gaussian/spectral baselines. Universality should be rejected if the proposed invariant varies materially across admissible blockings.

## Recommended revision sequence

### Phase 0: correct the status surface

This phase does not require new theory.

- Correct the bundle inverse/reference convention.
- Relabel the \(A=0\) object as a PSD operator ray pending a probability repair.
- Restore \(\Lambda\succ0\) or regular-pencil hypotheses wherever generalized eigenvalues are listed.
- Close Open 2.32 and the unrestricted matrix-Kron question negatively.
- Correct the projection scope, normalizer sign, spectral endpoints, natural-coordinate domain, closed-support claim, and coarse self-term language.
- Remove convergence and uniqueness from Proposition 10.12’s consequences.
- Reconcile the status vocabulary and split oversized status tables.

### Phase 1: choose the probabilistic fixed-point architecture

Choose one of:

- a massive/pinned family that stays SPD at every scale; or
- an intrinsic/quotient Gaussian family with a newly declared sample space and base measure.

Do not mix the two. Reprove the exact ELBO, Fisher geometry, absolute continuity, and aggregation on the selected family. State clearly whether the consensus coordinate is removed, pinned, or assigned a proper prior.

### Phase 2: type the RG

Declare:

- a fixed hierarchical theory space or a category in which the dimension-changing maps compose;
- the allowed blocking schemes and rescalings;
- the exact coupling cone;
- whether internal matrix directions are frozen, quotiented, or actively mixed; and
- which object is meant by “fixed point”: an operator ray, a probability law, or a compatible family over scales.

At this phase the manuscript can prove an honest scalar/fixed-\(M_0\) Perron theorem and the matrix-cone no-go result even if general attraction remains open.

### Phase 3: rebuild universality

Use a regular mass/reference pencil and a thermodynamic IDS. Prove or explicitly leave open:

- existence of the limiting measure;
- low-energy asymptotics;
- attraction and basin;
- independence from allowed blocking choices; and
- the relation between an exponent and the full universality class.

### Phase 4: restore the interpretive claims

Only after Phases 1–3 should the manuscript ask whether the limit is a physical law. Separate observational closure from ontological closure, and attach the physical reading to a declared empirical domain and falsification protocol.

## Recommendation to the author

This is a promising research monograph in need of structural revision, not a failed idea. The foundational goal—one exact probability model with gauge-covariant comparison and controlled coarse descriptions—is strong enough to justify the work. The manuscript’s best path is to narrow its current theorem claims while expanding the exact mathematics around the boundary:

- treat \(A=0\) honestly as an intrinsic Gaussian/operator boundary;
- replace the singular self-referential pencil by a regular geometric one;
- prove the cone no-go before seeking a contraction;
- turn the matrix Kron counterexample and the Gaussian-star contraction into finished theorems; and
- reserve “universality” and “physical law” for the point at which a typed thermodynamic flow and empirical protocol exist.

After those changes, the project could make a distinctive contribution as a compatibility theory: which combinations of gauge covariance, exact ELBO semantics, Gaussian graphical structure, topology, and coarse-graining can coexist, and which cannot.

## Reproducible verification appendix

### Exact algebraic witnesses

The following checks were executed symbolically over exact rational arithmetic; none is a floating-point inference.

| Check | Exact result | Consequence |
|---|---|---|
| Fixed-ray pencil \(\det(L-dL)\) for a two-node scalar Laplacian | \(0\) identically | The determinant equation does not define a degree-\(NK\) generalized spectrum |
| Regularized pencil \(\det(L-d(L+\varepsilon I))\) | \(d\varepsilon(d\varepsilon+2d-2)\) | The non-consensus root is \(2/(2+\varepsilon)\), while the consensus root is \(0\) |
| Three-node, \(K=2\), matrix-Kron witness | full precision determinant \(233>0\); all leading principal minors \(2,6,18,48,102,233>0\) | The full anchored precision is SPD |
| Manufactured coarse transport in that witness | \(\frac1{19}\begin{psmallmatrix}9&3\\4&14\end{psmallmatrix}\) | The candidate is nonsymmetric, so it cannot satisfy the required congruence form |
| Scalar cyclic normalizer with \(D(a)=p_0^2+p_0(a+a^{-1})^2\) and \(\mathsf A(a)=-\frac12\log D(a)+\mathrm{const}\) | \(\mathsf A''(1)=-4/(p_0+4)<0\) | The identity is a local maximum of the log normalizer, reversing the stated isolated force direction |
| Common-range face under sum-only aggregation | determinant \(0\), rank \(1\) preserved | The full PSD product cone has a proper invariant face for \(K>1\) |
| Exact Gaussian-star apex update | \(e_b^{t+1}=(P_0+B)^{-1}Be_b^t\) | Similarity to \(P_b^{-1/2}BP_b^{-1/2}\) places every eigenvalue in \([0,1)\) |

For the Kron witness, the matrices were
\[
A_1=A_2=A_3=I_2,\qquad
W_{13}=\begin{pmatrix}1&0\\0&2\end{pmatrix},\qquad
W_{23}=\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad
W_{12}=0.
\]
Schur elimination of node \(3\) gives an off-diagonal block that cannot be written as \(-\Omega^\top R^{-1}\) with the matching diagonal contribution \(R^{-1}\) under the unrestricted interaction-family rules. This closes the unrestricted full-family question negatively, while leaving commuting and simultaneously diagonalizable subfamilies open for positive classification.

### Counterexamples checked by direct derivation

1. **Density version at a selected observation.** Two versions of the same joint density may differ on an observation-marginal-null slice. The pointwise posterior and pointwise ELBO at that selected observation can therefore change although the underlying measure does not. The invariant theorem is an observation-marginal-almost-everywhere statement through a regular conditional probability.
2. **Proper closed support.** Let \(P\) be uniform on \([0,1]\) and \(Q\) uniform on \([0,\tfrac12]\). Then \(\operatorname{supp}Q\) is a proper closed subset of \(\operatorname{supp}P\), \(Q\ll P\), and \(D_{\mathrm{KL}}(Q\Vert P)=\log2<\infty\).
3. **Open 2.32.** On a one-dimensional base with \(G=\mathrm{GL}^+(1)\), take frames \(u_1=\sigma\) and \(u_2=\sigma e^x\). Their induced local potentials differ by \(-dx\), but every partition-weighted connection has identically zero curvature because every base two-form vanishes.
4. **Moving target versus moving evidence.** The family \(P_Q(do,dy)=R(do)Q(dy)\) varies with \(Q\) while its observation marginal, and hence its evidence, remains \(R\).
5. **Global interaction-family membership without local projection.** With scalar \(W=\tfrac12\), the SPD precision having diagonals \(A=1\) and \(C=\tfrac54\) admits a global interaction-family factorization with gain \(T=\tfrac34\), even though \(T\) is not a projection. This refutes the converse claimed for the unrestricted global family.

### Build and artifact checks

- Clean source revision: `1de9c213203e46ee02d793d2c465eb046e3f73f0`.
- Direct build: `pdflatex`, BibTeX, then two further `pdflatex` passes in `C:\tmp\gauge-vfe-rg-build-20260729`.
- Result: 185 pages, 1,210,291 bytes, with no unresolved citations or cross-references.
- `latexmk` itself failed before compilation because the installed TeX Live helper raised `attempt to concatenate a nil value`; the direct toolchain supplied the independent fallback.
- Five overheight status floats were confirmed both in the log and by rendering the affected PDF pages.
- Static cross-reference sweep: 376 labels, 932 references, no duplicate labels, no undefined references, and all 72 cited entries resolved.
- The source revision contains no numerical reproduction package, so the manuscript's numerical observations remain `INCONCLUSIVE` as reproduced experiments even when the prose reports a seed.

### Primary-source boundary checks

The review used the following external sources to determine what is established background and what remains a plausible contribution of this manuscript:

- Cipriani and van Ginkel, [the zero-average discrete Gaussian free field](https://arxiv.org/abs/1809.03382), for quotient/mean-zero handling of Laplacian Gaussian fields.
- Dopico et al., [singular matrix pencils](https://arxiv.org/abs/2208.01359), for why a determinant polynomial that vanishes identically is not a regular generalized-eigenvalue problem.
- Lenz, Müller, and Veselić, [integrated density of states](https://arxiv.org/abs/0709.2836), for the thermodynamic limiting object required beyond a finite atomic spectrum.
- Lemmens and Nussbaum, [Birkhoff's version of Hilbert's metric](https://arxiv.org/abs/0909.5347), and Gaubert and Qu, [contraction in Hilbert's projective metric](https://arxiv.org/abs/1807.06872), for cone-interior and finite-diameter requirements.
- Dörfler and Bullo, [scalar Kron reduction](https://arxiv.org/abs/1102.2950), and Hansen and Ghrist, [Kron reduction of sheaf Laplacians](https://arxiv.org/abs/1808.01513), for known closure settings and broader restriction-map formalisms.
- Berman, Klinger, and Stapleton, [Bayesian renormalization](https://arxiv.org/abs/2305.10491), for the scope of posterior/model-space RG flows and their endpoint claims.
- Faden, [the existence of regular conditional probabilities](https://doi.org/10.1214/aop/1176993081), for the measure-theoretic scope of selected-observation conditioning.
- Blei, Kucukelbir, and McAuliffe, [variational inference](https://www.cs.columbia.edu/~blei/papers/BleiKucukelbirMcAuliffe2017.pdf), Beal's [variational algorithms thesis](https://cse.buffalo.edu/faculty/mbeal/thesis/), and Dempster, Laird, and Rubin's [EM paper](https://rss.onlinelibrary.wiley.com/doi/10.1111/j.2517-6161.1977.tb01600.x), for the fixed-joint/fixed-evidence structure behind the standard ELBO and EM comparisons.

These sources do not duplicate the manuscript's proposed synthesis. They do constrain novelty claims: the contribution should be framed as a typed compatibility/no-go theory joining these structures, plus new theorems for the specific gauge-covariant coarse category, rather than as the invention of its individual ingredients.

## Remediation continuation — 2026-07-29

This addendum records the continuation after the first referee report. It preserves the original
findings as the historical review record and separately states what the revised manuscript now
does. The working provenance is:

- branch: `codex/gauge-vfe-rg-remediation-20260729`;
- isolated worktree: `C:\tmp\Research-gauge-vfe-rg-remediation-20260729`;
- reviewed base: `593dc9902e84cfece9187e7e0a143c30f8b44a65`;
- source freeze: after the final independent variational/measure-theory rescan; and
- publication target: the Research vault only after mechanical verification and the authorized
  Git lifecycle complete.

### Continuation protocol and expert lanes

The remediation retained ten distinct expert lenses. Their purpose was not a vote: each lane was
required to produce a derivation, counterexample, source boundary, or explicit open obligation.
Independent verifier rebounds were applied after the first integration pass, and source was not
frozen until the last scope defect was repaired.

| Lane | Remediation responsibility |
|---|---|
| Measure theory and probability | RCP versions, absolute continuity, support claims, finite-design versus continuum typing |
| Variational inference | Fixed-joint ELBO semantics, E/M-coordinate finiteness, acceptance and monotonicity |
| Exponential families | Natural-domain boundaries, minimality, Bregman identities, operator versus probability layers |
| Information geometry | Natural/expectation/moment charts, DQM/Fisher scope, generalized spectra |
| Differential geometry and topology | Principal/associated-bundle conventions, Čech data, base connections and holonomy |
| Gauge theory | Edgewise stabilizers, graph-link covariance, effective-support holonomy |
| Gaussian matrix analysis | Projection regimes, Loewner comparisons, singular pencils, exact counterexamples |
| Coarse-graining and RG | Closure, rescaling, theory-space typing, fixed rays, scheme and convergence obligations |
| Numerical reproducibility | Claim inventory, stable check IDs, exact versus floating evidence, deterministic replacements |
| Adversarial integration | Cross-chapter numbering, status registers, cross-references, overclaim and seam scan |

### Central scope correction: Gaussian laws are a realization, not the theory

The author's diagnosis was substantially right: the original draft repeatedly let the
multivariate-Gaussian realization stand in for the ambient theory because it is computationally
easy. The revision now enforces a hierarchy.

1. A **state-recognition belief fiber** is a declared collection of normalized probability laws on
   a measurable state space.
2. A **model-belief fiber** is a separate collection of normalized laws on a model-parameter or
   latent-model space.
3. A **generative-kernel fiber** is a third type: a collection of Markov kernels with declared
   source and target spaces. A model-belief law is not a generative kernel.
4. A finite-dimensional **DQM/Fisher tier** is selected only after a parameter manifold,
   differentiability in quadratic mean, square-integrable scores, and nondegeneracy of the Fisher
   form have been proved or assumed.
5. A regular minimal **exponential-family tier** adds a common dominating measure, an open natural
   domain, minimal sufficient statistics, and finite log partition.
6. The **nondegenerate Gaussian tier** is a tractable realization inside that exponential-family
   tier. The Laplacian-plus-self-term interaction family is narrower again.

Thus the fibers may indeed be general spaces of beliefs and models, but they are not automatically
manifolds. Manifold, Fisher, covariance, natural-coordinate, and boundary language belongs only to
a selected regular tier. This correction is implemented in `SPEC.md`, the foundations, the new
exponential-family chapter, and every later scope statement.

### R1–R21 disposition ledger

`Addressed` below means that the false or overbroad manuscript statement was corrected, scoped, or
replaced. It does not turn an explicitly retained open problem into a theorem.

| ID | Disposition in the revised manuscript | Evidence in the revision | Remaining obligation |
|---|---|---|---|
| R1 | **Addressed; negative conclusion retained.** The \(A=0\) ray is a PSD operator ray, not a normalized Gaussian law. | Chapter 6 separates operator and probability layers; Proposition 11.16 proves singularity, nonnormalizability, absence of Fisher geometry, and absence of an ELBO instance. | A quotient, pin, or retained-mass repair must be constructed across scales before it can be called a law. |
| R2 | **Addressed.** The right-principal/left-associated convention is made consistent. | Geometry now uses \(u_i=\sigma_0\!\cdot U_i^{-1}\), derives \(\Omega_{ij}=U_iU_j^{-1}\), and separately derives agent-frame and reference-frame changes. | None for the stated convention. |
| R3 | **Addressed; negative conclusion retained.** | The pencil is called regular only after its common kernel is removed; Proposition 11.19 proves that the fixed-ray determinant is identically zero. | A quotient or reference/mass pencil is needed for a nontrivial spectral object. |
| R4 | **Addressed as an open program.** A finite spectrum is not a density or exponent. | The RG chapter requires a declared hierarchical/thermodynamic family and limiting counting function; the singular endogenous pencil is rejected. | Existence, low-spectrum asymptotics, flow covariance, and scheme robustness of an IDS remain open. |
| R5 | **Addressed.** Sum-only aggregation is not primitive on the full \(K>1\) matrix cone. | Invariant common-range faces and infinite projective diameter are proved; the viable Perron/Birkhoff statement is scoped to a scalarized cone with a primitive spatial map. | Attraction on a nontrivial matrix cone requires internal mixing or a proved quotient metric. |
| R6 | **Addressed.** Relaxed factorwise, invertible factorwise, and global membership are separated. | The Gaussian chapter proves the orthogonal-projection criterion with singular gains, identity-only behavior for invertible idempotents, and an explicit globally admissible nonprojection witness. | The random sweep remains corroboration, not proof of generic measure zero. |
| R7 | **Addressed; full-family question closed negatively.** | An exact rational \(N=3,K=2\) SPD witness produces a nonsymmetric manufactured coupling; a common-orthogonal-eigenbasis subfamily is proved closed. | Classify maximal iteratively Kron-closed subfamilies. |
| R8 | **Addressed.** | Probability and ELBO chapters use a standard-Borel RCP, a marginal-full regular-observation set, and declared pointwise versions only when supplied as model data. | Every new parameterized comparison must still provide a common regular set or declared pointwise versions. |
| R9 | **Addressed by scoping.** | The obstruction chapter rejects only the flat unanchored reciprocal Gaussian pair; anchored and globally normalized cyclic models are explicitly valid. | Closure of an enlarged nonflat pair-factor family remains open. |
| R10 | **Addressed by withdrawal.** Component preservation no longer implies convergence, uniqueness, or scheme independence. | Proposition 11.12 proves only component preservation; later conclusions list convergence, basin uniqueness, and scheme robustness as antecedents. | All three dynamical obligations remain open. |
| R11 | **Addressed and closed.** | Proposition 2.32 gives both a one-dimensional flat-disagreement counterexample and a two-dimensional curved partition-dependent example. | No remaining obligation for the former open claim. |
| R12 | **Addressed and closed for the displayed exact schedule.** | Theorem 12.8 gives the exact fixed point and a geometric contraction rate for the anchored Gaussian star. | Delayed, noisy, asynchronous, and inexact schedules remain open. |
| R13 | **Addressed.** | The restriction chapter uses the posterior-null-set criterion and includes the uniform \([0,\tfrac12]\) versus \([0,1]\) finite-KL counterexample. | None for the corrected claim. |
| R14 | **Addressed.** | The scalar normalizer derivative is recomputed with the correct sign and kept distinct from a coordinate or model update. | No dynamical interpretation follows without a declared update rule. |
| R15 | **Still `OPEN/INCONCLUSIVE`, deliberately.** | Introduction, RG, and philosophy chapters separate observational closure, arrival at a repaired fixed object, physical-law identification, and ontological closure. | Name a target system, estimator, noise model, baseline, tolerance, and risky cross-scale validation protocol. |
| R16 | **Addressed.** | Pointwise graph zero-cochains, smooth Čech zero-cochains, graph-link holonomy, and principal-connection holonomy are separately typed. | A graph-to-base transport bridge remains open. |
| R17 | **Addressed.** | Proposition 2.31 is only a sufficient flatness result; Proposition 2.32 supplies the separate explicit curved witness. | An operational population observable of base holonomy remains conjectural. |
| R18 | **Addressed; mechanically closed for the numerical/status contract.** | Status registers were synchronized, historical unreconstructable magnitudes were removed or marked inconclusive, and stable `CHK-*` replacements were introduced. The adversarial verifier then caught a stale bare Chapter 12 star/fold row: it was replaced by `CHK-OBS-STAR-FOLD-NEW-PROTOCOL`, all six bare status cells were macro-wrapped, and the recursively bound source-frozen package passes with zero manifest mismatches as recorded below. | No numerical-package repair remains. `NUM-RG-PHYSICAL-LAW` remains deliberately `INCONCLUSIVE` because a scientific validation protocol, not another numerical check, is owed. |
| R19 | **Addressed.** | The ELBO chapter distinguishes substituted free energy from the negative pseudo-ELBO and proves both total-correlation signs. | None. |
| R20 | **Addressed.** | The subspace-supported conclusion is proved directly from a posterior-null set, without applying the dominated-density proposition outside its hypotheses. | None. |
| R21 | **Addressed.** | Proposition 4.5 now proves only the no-distinguished-target result; Proposition 4.14 supplies a normalized binary family in which the three stronger readings fail. | Comparisons across moving models require a separately declared model-selection target. |

### Corrections found by the continuation verifiers

The post-integration verifier pass found several defects not isolated as separate R-items in the
first report. They were repaired before the source freeze:

- The general hierarchy now distinguishes state-belief laws, model-belief laws, and generative
  kernels. Arbitrary law fibers are not called manifolds.
- Proposition 3.12 now requires at least two nondegenerate real coordinates; singleton fibers are
  the exact counterexample. Proposition 3.13 inherits that richness condition, and its section
  nonuniqueness additionally requires an off-design point and a locally deformable selected fiber.
- The exact M-coordinate requires (H1)–(H4) for every compared parameter. A countable heavy-tail
  witness shows why two complete-log-likelihood values of \(-\infty\) cannot be compared by
  canceling an infinite entropy. The generalized acceptance and evidence-monotonicity statements
  require finite ELBOs at both endpoints.
- The finite-step quadratic counterexample for an optimizer proposal is restricted to steps whose
  start and endpoint both lie in the declared quadratic region.
- The exponential-family operator/probability intersection records the empty-set exception to its
  relative-closedness statement, and finite-step Gaussian interiority is no longer misread as a
  classification of boundary mechanisms. An anisotropic \(2\times2\) node-matrix sequence supplies
  the counterexample.
- The diagonal-affinity/annihilation equivalence is stated only in effective minimal coordinates;
  a nonminimal statistic gives an explicit nonzero-\(\Upsilon\) witness.
- Bregman projection attainment no longer rests on the false claim that intersection with an open
  mean domain destroys relative closedness. The actual obligations are nonemptiness, coercivity,
  compactness, and escape to infinity or the natural-domain boundary.
- The Gaussian block projection is described as changing the candidate \(Q\), setting its
  cross-covariances to zero and its diagonal blocks to \(J_{bb}^{-1}\preceq(J^{-1})_{bb}\); it does
  not alter any block of the fixed target \(P\).
- Cross-model ELBO noncomparability now has finite normalized binary witnesses. A deterministic
  unused coordinate makes the two latent inventories literally different without changing
  evidence, KL, or ELBO.
- Full fixed-\(K\) annihilation is equivalent to trivial graph holonomy only for positive-definite
  internal weights. For PSD weights the exact criterion is
  \(W_{ij}^{1/2}(I-\Theta_{ij})=0\), leaving an effective-support/quotient problem open.
- The analyzed scale costs now have their correct endpoint behavior: the Gaussian mean-tie cost
  favors the finest partition, while the factorization gap favors the coarsest. Mixtures require an
  external coefficient; a general intrinsic selector remains open.

### Extensions to the general theory

#### 1. Formulate coarse-graining as a Markov morphism of statistical experiments

This is the strongest route beyond Gaussians. Let an object be a statistical experiment
\(\mathcal E=(\mathsf Y,\mathscr Y,\{P_\theta\}_{\theta\in\Theta})\), and let a coarse map be a
Markov kernel \(K:\mathsf Y\rightsquigarrow\bar{\mathsf Y}\). The coarse experiment is
\(K_\#\mathcal E=\{P_\theta K\}\). Composition of kernels gives a genuinely typed semigroup or
category, so repeated coarse-graining no longer relies on identifying Euclidean parameter spaces
by hand.

A rigorous program should prove, in this order:

1. **Functoriality:** gauge pushforwards and Markov coarse maps commute, or their failure is encoded
   by an explicit natural transformation.
2. **Information monotonicity:** KL and appropriate \(f\)-divergences contract under \(K\).
3. **Sufficiency/equality:** characterize when a recovery kernel \(R\) satisfies
   \(P_\theta K R=P_\theta\) for all \(\theta\), equivalently when coarse-graining loses no
   information for the declared experiment.
4. **Stable submodels:** classify exponential and Gaussian submodels invariant under \(K\), rather
   than assuming closure from a matrix formula.
5. **Differential consequence:** on a DQM stratum, identify the coarse score as a conditional
   expectation and prove Fisher contraction; equality should correspond to local sufficiency under
   stated regularity.
6. **RG typing:** only after an identification of experiment families across scale should a fixed
   object, attraction, or universality class be defined.

This reframes the current theory as a special quadratic representation of a more general
information-losing morphism theory. It also cleanly separates exact marginalization, sufficient
statistics, model replacement, and recognition-family restriction.

#### 2. Use stratified and nonparametric belief fibers, not one universal manifold

The maximal ambient object should remain a measurable family of probability laws. Smooth geometry
can then be added stratum by stratum:

- finite-dimensional DQM strata for ordinary Fisher/Riemannian calculations;
- regular exponential-family strata for dual affine geometry and exact Bregman identities;
- Gaussian/SPD strata for closed matrix formulas;
- singular boundary strata for degenerate laws, quotient measures, changing support, and rank
  changes; and
- optional infinite-dimensional exponential manifolds, such as a Pistone–Sempi/Orlicz model, only
  inside a fixed mutual-absolute-continuity class with its integrability hypotheses declared.

The last option is not a manifold of all probability laws. Different measure classes and
support-changing limits require separate components or a stratified completion. Gauge actions
should be defined by pushforward on measures, with isotropy and orbit-type strata retained rather
than erased by a dimension count. Generative Markov kernels should remain a separate fibred
category over these belief-law fibers.

The principal theorem to seek is a **stratified coarse-map theorem**: conditions under which a
gauge-covariant Markov morphism maps one regular stratum smoothly into another, the induced tangent
map is conditional expectation on scores, Fisher information is monotone, and equality is
equivalent to a declared recovery/sufficiency condition. Boundary crossings should be reported as
stratum changes, not as points of the same Fisher manifold.

#### 3. Effective-support holonomy and variable-rank coarse fibers

The PSD-weight correction exposes a new problem not visible in the positive-definite theory.
Classify graph-link data modulo directions invisible to every internal weight, define the
effective holonomy on the resulting quotient or support bundle, and determine whether partial
coarse fibers of dimension
\(\dim\operatorname{Fix}(\operatorname{Hol}_I)\) compose under further merging. A successful theory
would replace the current fixed-\(K\) family by a variable-rank category whose links are rectangular
intertwiners and whose closure is proved rather than presumed.

#### 4. Projective-limit probability before continuum RG

For continuum belief sections, first construct a refining family of finite designs and a compatible
projective system of normalized laws. Then prove tightness on a declared section-space topology,
gauge compatibility, and convergence of the ELBO and coarse observables. An energy density written
formally on a continuum section space is not enough: the reference measure and normalizer must
exist before information geometry or RG language applies.

### Verification after the source freeze

The source-frozen numerical suite reports overall `PASS`. It inventories 39 literal
`\status{NUMERICAL}` macros: 30 substantive claims, one taxonomy entry, and eight duplicate or
current-summary status-register rows. There are zero bare `& NUMERICAL &` cells. The adversarial
verifier found that the former Chapter 12 star/fold register row still named a historical protocol;
the row now names `CHK-OBS-STAR-FOLD-NEW-PROTOCOL`, and all six bare status cells were macro-wrapped
so the inventory is complete.

The runner recursively binds all 14 TeX inputs together with `claims.json`, `run_checks.py`,
`requirements.txt`, and `VERIFICATION.md` through a repository-relative SHA-256 manifest. An independent
recheck found zero manifest mismatches. All 29 deterministic checks pass, with zero failures and
zero inconclusive check executions; source-to-check mapping validation passes, and all six required
supplemental checks are known and passing. The substantive dispositions are 29 `keep_exact` and one
`retain_as_inconclusive`. The retained item is `NUM-RG-PHYSICAL-LAW`, intentionally
`INCONCLUSIVE` because the manuscript still supplies no scientific protocol capable of validating
a physical law. Two same-environment runs produced byte-identical `current-results.json` outputs.
Its SHA-256 is
`FCAF6443EC885336A421EF898C297713755EC807A5B5FD5852964F6A3CDEE638`.

A final direct build on the same frozen source ran `pdflatex`, BibTeX, and two further `pdflatex`
passes. It produced a 255-page, 1,581,568-byte PDF with SHA-256
`DF66962CC6214089190C3643E3702DA62ADBC7CF1E59DE47954A9C284DB09E6B`. The final log contains no
undefined citations, undefined references, compilation error, fatal error, oversized float, or
overfull vertical box. The material 21-point and 24-point horizontal overflows found on the first
integration build were repaired; the maximum remaining horizontal warning is 4.7456 points and was
visually contained.

The separate `.verification/ledger.json` is the 21-claim closure ledger, and its
`artifact_revision` binds the evidence to the exact worktree snapshot. Ledger validation passes
with 20 claims `EVIDENCE_VERIFIED` and one deliberate `INCONCLUSIVE` claim, R15, whose open
obligation is the missing empirical protocol required to identify a repaired fixed object with a
physical law.
