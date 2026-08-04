# Task 9 independent adversarial verification (Opus, maximum rigor)

**FAIL**

Date: 2026-08-04. Worktree: `C:\tmp\Research-gauge-vfe-rg-review-remediation-20260803`.
Branch `codex/gauge-vfe-rg-theory-remediation-20260804`, `HEAD = 3dbe4c610ccc3c0645d25d06ed8fd3074eb4ba3a`,
working tree dirty with the Task 9 edits. Every conclusion below was recomputed
from the current bytes listed in `evidence/task-9-static-proof-control.md`. No
integration summary, no ledger disposition, and no agreement among the three
Task 9 route analyses was accepted as evidence.

The verdict is **FAIL on exactly one blocker**, recorded in Section 1. The
blocker is a LaTeX-semantics defect that makes four labels undefined and six
`\Cref` targets unresolved; two of those six references were added by Task 9.
The mathematics of Task 9 is clean: I found **no mathematical blocker**. Every
load-bearing derivation in obligations 1 through 9 was reproduced independently
and is correct as stated. Section 3 records the recomputations. Section 4
records non-blocking findings that must not be read as blockers.

---

## 1. BLOCKER

### B-1. Four `\...heading` calls receive `\label` as their second argument, so four labels are never defined and six `\Cref` targets are undefined

**Severity: blocker. Release-blocking for the manuscript build; propagated by Task 9.**

**Exact locations.**

| Malformed construct | File:line | Label that is never defined |
| --- | --- | --- |
| `\propositionheading{Bounded recentering gives analyticity at every bounded action}` | `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex:259` + `:260` | `prop:rg-action-bounded-recentering` |
| `\propositionheading{Product equivalence is an admitted, not an automatic, scale premise}` | `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex:1109` + `:1110` | `prop:rg-product-equivalence-not-preserved` |
| `\theoremheading{Hoeffding assembly is an exact finite-network action isomorphism}` | `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex:1174` + `:1175` | `thm:rg-hoeffding-action-isomorphism` |
| `\propositionheading{Radon--Nikodym covariance of the nonlinear interaction step}` | `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex:1243` + `:1244` | `prop:rg-interaction-rn-gauge-covariance` |

**The unsupported statement.**
`evidence/task-9-integrated-proof.md:631-633` asserts:

> Cross-reference resolution across the same files: 557 unique
> `\Cref`/`\cref`/`\ref`/`\eqref`/`\autoref`/`\pageref` targets, zero
> unresolved.

That statement is true only as a string match of reference keys against
`\label{...}`/`heading{...}{...}` keys in the source text. It is false as a
statement about the document LaTeX will actually produce. I reproduced the
557/0 string-level result exactly (Section 2 of the static-control report), and
it is exactly the wrong check for these four sites.

**The derivation that makes it wrong.**
`manuscripts/gauge_vfe_rg/main.tex:86-100` defines

```latex
\newcommand{\resultheading}[4]{%
  \syncstatementcounter{#2}%
  \label{#4}%
  \paragraph{#1~\csname the#2\endcsname\ (#3).}%
}
\newcommand{\propositionheading}[2]{\resultheading{Proposition}{proposition}{#1}{#2}}
\newcommand{\theoremheading}[2]{\resultheading{Theorem}{theorem}{#1}{#2}}
```

Both wrappers take **two mandatory arguments**. At `07b:259` the source is

```latex
\propositionheading{Bounded recentering gives analyticity at every bounded action}
\label{prop:rg-action-bounded-recentering}
```

TeX scans `#1` as the balanced group `{Bounded recentering ...}`. It then scans
`#2` as an *undelimited* parameter: it skips the space token produced by the end
of line 259 and takes the next token. That token is the control sequence
`\label`, not a brace group. Therefore

* `#2 = \label`,
* the body expands to `\syncstatementcounter{proposition}\label{\label}\paragraph{Proposition~\theproposition\ (Bounded recentering ...).}`,
* the group `{prop:rg-action-bounded-recentering}` that follows `\label` in the
  source remains in the input stream and is typeset as ordinary body text, and
* the key `prop:rg-action-bounded-recentering` is **never** passed to `\label`.

There is no redefinition anywhere that changes this: `grep -rn -e renewcommand
-e providecommand -e DeclareRobustCommand manuscripts/gauge_vfe_rg/*.tex`
returns only `\arraystretch`, `\chaptermark`, `\@pnumwidth`, `\@tocrmarg`, and
the ten `\the<counter>` redefinitions. There is no `.sty` in the directory that
touches the heading macros.

**Concrete consequence, with the six affected reference sites.**

| Reference site | Target | Introduced by |
| --- | --- | --- |
| `07b_agent_network_rg.tex:362` | `prop:rg-action-bounded-recentering` | `3dbe4c61` |
| `07b_agent_network_rg.tex:1307` | `prop:rg-action-bounded-recentering` | `3dbe4c61` |
| `07b_agent_network_rg.tex:1354` | `prop:rg-action-bounded-recentering` | `3dbe4c61` |
| `07b_agent_network_rg.tex:1412` | `thm:rg-hoeffding-action-isomorphism` | **Task 9 (uncommitted)** |
| `07b_agent_network_rg.tex:1462` | `prop:rg-interaction-rn-gauge-covariance` | `3dbe4c61` |
| `07b_agent_network_rg.tex:2250` | `thm:rg-hoeffding-action-isomorphism` | **Task 9 (uncommitted)** |

Every one of these will emit `LaTeX Warning: Reference '...' undefined` and
render as `??`, plus four stray label keys printed as body text, plus a
`\label{\label}` write into the `.aux` file. Plan Task 14 Step 3 requires "zero
undefined references/citations, duplicate labels, ... literal `??`", so this
condition cannot reach the build gate.

**Attribution, established mechanically, not asserted.**
`git blame` on the working tree distinguishes committed from Task 9 lines:

```
$ git blame -L 258,261 -- manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex
3dbe4c61 ... 259) \propositionheading{Bounded recentering gives analyticity at every bounded action}
3dbe4c61 ... 260) \label{prop:rg-action-bounded-recentering}
$ git blame -L 1109,1110 -L 1174,1175 -L 1243,1244 -L 1412,1412 -L 2250,2250 -- .../07b_agent_network_rg.tex
3dbe4c61          ... 1109) \propositionheading{Product equivalence is an admitted, not an automatic, scale premise}
3dbe4c61          ... 1110) \label{prop:rg-product-equivalence-not-preserved}
3dbe4c61          ... 1174) \theoremheading{Hoeffding assembly is an exact finite-network action isomorphism}
3dbe4c61          ... 1175) \label{thm:rg-hoeffding-action-isomorphism}
3dbe4c61          ... 1243) \propositionheading{Radon--Nikodym covariance of the nonlinear interaction step}
3dbe4c61          ... 1244) \label{prop:rg-interaction-rn-gauge-covariance}
00000000 (Not Committed Yet ... 1412) \Cref{thm:rg-hoeffding-action-isomorphism} becomes a hypothesis of the mode
00000000 (Not Committed Yet ... 2250) inverse identities of \Cref{thm:rg-hoeffding-action-isomorphism} together with
```

All four malformed constructs come from commit `3dbe4c61`
(`docs: construct exact finite-network interaction RG`, Task 8). Every one of
Task 9's own twenty-nine new `\...heading` calls is well formed with both
arguments on one line; I checked each. Task 9 therefore did not create the
defect, but it did add two new dependents on `thm:rg-hoeffding-action-isomorphism`
(`cor:rg-interaction-tempered` and the proof of `prop:rg-retained-beta-residual`)
and it re-ran and re-published a mechanical check
(`task-9-integrated-proof.md:631-633`) that reports the file as clean. Under the
stated obligation ("duplicate LaTeX labels and missing reference targets across
`manuscripts/gauge_vfe_rg/*.tex`") the check does not close, so the verdict is FAIL.

**Minimal repair.** Move each label onto the heading line as the second
argument. Four one-line edits, no prose change:

```latex
% 07b:259-260  ->  one line
\propositionheading{Bounded recentering gives analyticity at every bounded action}{prop:rg-action-bounded-recentering}
% 07b:1109-1110 -> one line
\propositionheading{Product equivalence is an admitted, not an automatic, scale premise}{prop:rg-product-equivalence-not-preserved}
% 07b:1174-1175 -> one line
\theoremheading{Hoeffding assembly is an exact finite-network action isomorphism}{thm:rg-hoeffding-action-isomorphism}
% 07b:1243-1244 -> one line
\propositionheading{Radon--Nikodym covariance of the nonlinear interaction step}{prop:rg-interaction-rn-gauge-covariance}
```

(Equivalently, keep two physical lines by terminating line 259 with `%` so the
following brace group is grabbed as `#2`.) Because these are source edits, they
create a new source revision under the plan's Global Constraints and any
downstream evidence must be regenerated. The mechanical check in
`task-9-integrated-proof.md:631-633` must additionally be replaced by, or
supplemented with, a check that a heading macro's second argument is a brace
group; the string-level label/reference match cannot detect this class.

**Falsification condition for B-1.** B-1 is refuted if a `pdflatex` run over
`manuscripts/gauge_vfe_rg/main.tex` at the current bytes defines
`prop:rg-action-bounded-recentering`, `prop:rg-product-equivalence-not-preserved`,
`thm:rg-hoeffding-action-isomorphism`, and `prop:rg-interaction-rn-gauge-covariance`
and resolves all six references above. I was instructed not to run a TeX build,
so B-1 rests on the macro arity in `main.tex:86-100` and standard TeX
undelimited-argument scanning, both of which are quoted above in full.

---

## 2. Disposition of each stated obligation

| # | Obligation | Disposition |
| --- | --- | --- |
| 1 | Normalized two-sided DQM path, absolute value, `o(t)` remainder, normalization, score `h` | **CLOSED** by recomputation (3.1) |
| 2 | Product/iid lift, exact `sqrt(b)`, channel score, contraction, Fisher defect, bounded-action quotient isometry and completion, domains and null spaces | **CLOSED** by recomputation (3.2) |
| 3 | Gaussian block operator on Hermite modes, `b^(1-k/2)`, exact spectrum, `0` continuous and not an eigenvalue, relevance classes, correlated/multivariate/gauge boundaries | **CLOSED** by recomputation (3.3) |
| 4 | Typed derivative cocycle, `J_l` conjugation, product law, mode-line compatibility, finite-time and limsup exponents, bilateral tempered invariance, superexponential counterexample | **CLOSED** by recomputation (3.4) |
| 5 | Exact/retained/residual beta, types and domains, smooth-scale Banach-bundle connection, separation from physical/emergent time and contextual gauge connection | **CLOSED** by recomputation (3.5) |
| 6 | Exact/retained/projected fixed objects, invariant mode lines, residual closure, tier compatibility, no conflation of projected stationarity with exact fixedness | **CLOSED** by recomputation (3.6) |
| 7 | Corrected strong lumpability and contrapositive; must not force an individual coarse process to be non-Markov; finite `a,b,u,v` test | **CLOSED** by recomputation (3.7) |
| 8 | Source scope for Jona-Lasinio, Kemeny-Snell, Nakajima/Zwanzig; bibliographic keys, metadata, duplicates | **CLOSED**, with non-blocking findings N-3 and N-4 (3.8) |
| 9 | Status discipline; no numerical/heuristic evidence as proof; no Task 10 claim closed; no hidden finite-graph-only claim | **CLOSED** (3.9) |
| S | Static control (JSON, digests, labels, references, bibliography, `git diff --check`, encoding, placeholders, spelling, protected files, scope) | **NOT CLOSED**: "missing reference targets" fails, see B-1. All other static items pass; see `task-9-static-proof-control.md` |

---

## 3. Independent recomputations

Every identity below was rederived from the manuscript's own hypotheses without
using the integrated proof, the three route analyses, or the ledger.

### 3.1 The normalized two-sided DQM path (`lem:rg-dqm-realization`, `07b:560-600`)

Let `h in L2_0(mu)`, `a = ||h||_2^2/4`, `s_t = 1 + t h/2`, `N_t = 1 + a t^2`,
`p_t = s_t^2/N_t`.

*Normalization.* `int (1 + th/2)^2 dmu = 1 + t mu(h) + (t^2/4) mu(h^2) = 1 + a t^2 = N_t`
because `mu(h) = 0`. Hence `p_t >= 0` and `int p_t dmu = 1` for **every real `t`**,
so the path is genuinely two-sided and no small-`t` restriction is hidden.

*The absolute value.* `sqrt(p_t) = |s_t|/sqrt(N_t)`, not `s_t/sqrt(N_t)`. The
manuscript's split
`sqrt(p_t) - s_t = (|s_t| - s_t)/sqrt(N_t) + s_t (N_t^{-1/2} - 1)`
is an identity. On `{s_t < 0}` we have `t h/2 < -1`, hence `|h| > 2/|t|` and
`|s_t| = |t h/2| - 1 <= |t h|/2`, so `|s_t| - s_t = 2|s_t| <= |t h|` there and
vanishes elsewhere. Since `N_t >= 1`,

```
t^{-2} || (|s_t| - s_t)/sqrt(N_t) ||_2^2  <=  int h^2 1_{|h| > 2/|t|} dmu  ->  0
```

by dominated convergence (`h^2` is integrable). So that term is `o(|t|)` in `L2`.
This is exactly the step a wrong proof drops, and it is present and correct.

*The remainder.* `||s_t||_2 = sqrt(N_t)` exactly, so the second term has norm
`|1 - sqrt(N_t)| = a t^2/2 + O(t^4) = O(t^2) = o(|t|)`. Adding gives
`|| sqrt(p_t) - 1 - (t/2) h ||_2 = o(|t|)` from both sides. **Correct.**

*Forced centering (`07b:551-558`).* `(sqrt(p_t) - 1)^2 = p_t - 2 sqrt(p_t) + 1`
integrates to `-2 int (sqrt(p_t) - 1) dmu`, giving the exact identity
`int(sqrt(p_t) - 1) dmu = -(1/2) int (sqrt(p_t) - 1)^2 dmu`. The left side is
`(t/2) mu(h) + o(|t|)` (Cauchy-Schwarz on a probability space converts the `L2`
remainder into an `L1` remainder); the right side is `-(t^2/8)||h||_2^2 + o(t^2)`.
Hence `mu(h) = 0`. **Correct**, and it is a derivation, not an assumption.

### 3.2 Lift, channel, defect, isometry (`07b:602-820`)

*Product lift.* With `r_t = 1 + (t/2)h + t eps_t`, `||eps_t||_2 -> 0`, and
`u_i = (t/2)h(x_i) + t eps_t(x_i)`, the finite expansion
`prod(1+u_i) = 1 + sum u_i + sum_{|S|>=2} prod_{i in S} u_i` is exact, and
independence makes `|| prod_{i in S} u_i ||_{L2(mu^b)} = prod_{i in S} ||u_i||_{L2(mu)} = O(|t|^{|S|})`.
The linear remainder is bounded by `b|t| ||eps_t||_2` by the triangle inequality
(`eps_t` need not be centered, and the proof correctly does not assume it is).
So the score is `I_b h = sum_i h(x_i)`. **Correct.**

*Exact norm.* `E(I_b h)^2 = sum_i E h(X_i)^2 + sum_{i != j} E h(X_i) E h(X_j) = b ||h||_2^2`,
the cross terms vanishing by centering. Hence `||I_b|| = sqrt(b)` **exactly**,
`I_b` is injective, and `b^{-1/2} I_b` is an isometry onto its range.
`b >= 1` is admissible (`b = 1` gives the identity). **Correct.**

*Channel score.* For bounded `h`, `p_t = 1 + t h + O(t^2)` uniformly, the product
density is `1 + t I_b h + O(t^2)` uniformly, conditional expectation preserves a
uniform `O(t^2)`, and `sqrt(1+w) = 1 + w/2 + O(w^2)` uniformly on `|w| <= 1/2`.
For general `h` the argument routes through data processing for squared
Hellinger distance (`f(u) = (sqrt(u)-1)^2` convex). I reconstructed the three-term
estimate the manuscript compresses:

```
||A_t - 1 - (t/2) L_b h||  <=  ||A_t - B_t|| + ||B_t - 1 - (t/2) L_b h_n|| + (|t|/2)||L_b(h - h_n)||
```

with `A_t`, `B_t` the pushed amplitudes for `h` and for the canonical bounded
path of `h_n`. Dividing by `|t|` and taking `limsup` gives
`(sqrt(b)/2)||h - h_n|| + 0 + (sqrt(b)/2)||h - h_n|| = sqrt(b)||h - h_n||`,
which is `eq:rg-pushed-score-approximation` and is independent of `n`.
Bounded centered functions are dense in `L2_0`, so the limit is zero.
**Correct**, and the statement covers an arbitrary DQM path, not only the
canonical one.

*Fisher defect.* Total conditional variance applied to `I_b h` gives
`b||h||^2 = ||L_b h||^2 + E Var(I_b h | Z)`, so the defect is exactly the
conditional variance integral, nonnegative, vanishing iff `I_b h` is a.s.
`sigma(Z)`-measurable. **Correct.** Consistency check I ran against 3.3:
at `h = e_1`, `I_b e_1 = sum X_i = sqrt(b) Z` is `Z`-measurable, so the defect
must be zero; and `b - ||L_b e_1||^2 = b - (sqrt b)^2 = 0`. Consistent.

*Null spaces and domains.* `ker I_b = {0}`. `ker L_b` can be everything (a
block-collapsing channel), so no lower bound on `||L_b||` is available; the
manuscript records this at `07b:752-754`. `ker S_pi = {0}` on the quotient,
since `S_pi[phi] = 0` iff `phi` is a.e. constant iff `[phi] = 0`.

*Bounded-action isometry.* `S_pi[phi] = -phi + pi(phi)` is the score of
`hat pi^{t phi}` (uniform Taylor expansion of `e^{-t phi}` and of its
normalizer, both legitimate for `phi in L^inf`); it depends only on `[phi]`;
`||[phi]||_F = inf_c ||phi - c||_2 = ||phi - pi(phi)||_2` since the `L2`
projection onto constants is the mean; hence `S_pi` is an isometry. Its range is
exactly `{psi in L^inf : pi(psi) = 0}` (take `phi = -psi`), which is dense in
`L2_0(pi)` and proper whenever `L2_0(pi)` contains an unbounded element, e.g.
`pi = N(0,1)`, `h(x) = x`. So the Fisher completion is canonically `L2_0(pi)`.
**Correct.**

*Norm ordering.* `eq:rg-action-oscillation-norm` (`07b:417-425`) defines
`||[phi]||_osc = inf_c ||phi - c||_inf = (1/2)(esssup - essinf)`. On a
probability space `||.||_2 <= ||.||_inf`, so
`||[phi]||_F = inf_c ||phi - c||_2 <= inf_c ||phi - c||_inf = ||[phi]||_osc`.
**Correct** (and sharper than the `<= 2||[phi]||` chain in the route-A memo).

*Centering square.* `S_{pi^c}(Ubar[phi]) = -U phi + pi^c(U phi)` and
`U S_pi[phi] = -U phi + pi(phi)` agree because `U1 = 1` and `U` preserves the
mean (`int U phi dpi^c = int phi dpi`, from the disintegration). **Correct.**
Replicated action: `S_{mu^b}[Phi_phi] = -sum phi(x_i) + b mu(phi) = I_b S_mu[phi]`.
**Correct.**

*Domain separation.* `07b:813-820` and `08:406-411` state that a spectral
statement on `L2_0` is not a statement about the nonlinear bounded action chart
and conversely. This is the correct fence and it is stated in both places.

### 3.3 Gaussian block spectrum (`thm:rg-gaussian-hermite-spectrum`, `07b:822-970`)

`(X_i, Z)` with `Z = b^{-1/2} sum X_j` is jointly centered Gaussian with unit
variances and `Cov(X_i, Z) = b^{-1/2}`, so `X_i | Z = z ~ N(z/sqrt b, 1 - 1/b)`.
Then

```
E[e^{tX_i - t^2/2} | Z=z] = exp(tz/sqrt b + (t^2/2)(1 - 1/b) - t^2/2) = exp(sz - s^2/2),  s = t/sqrt b.
```

I verified the exponent algebra term by term. Coefficient comparison against
`exp(sz - s^2/2) = sum_k He_k(z) s^k/k!` gives
`E[He_k(X_i) | Z] = b^{-k/2} He_k(Z)`, and summing the `b` coordinates gives
`L_b e_k = b * b^{-k/2} e_k = b^{1-k/2} e_k` for `k >= 1`. Uniform in `b`; no
induction from `b = 2`. **Correct.**

*Spectrum.* `sum_{k>=1} (b^{1-k/2})^2 = sum_{k>=1} b^{2-k} = b^2/(b-1) < inf`
(at `b = 2`: `2 + 1 + 1/2 + ... = 4`). So `L_b` is Hilbert-Schmidt, hence compact;
diagonal with real positive eigenvalues in a complete orthonormal system, hence
self-adjoint and positive; `||L_b|| = sup_k b^{1-k/2} = sqrt b` = spectral radius;
`sigma(L_b) = closure{b^{1-k/2}} = {b^{1-k/2} : k >= 1} u {0}`; eigenvalues
pairwise distinct hence simple. **Correct.**

*Status of `0`.* All eigenvalues are strictly positive, so `ker L_b = {0}` and `0`
is not an eigenvalue. The range contains every `e_k` (`e_k = L_b(b^{k/2-1} e_k)`)
hence is dense. It is proper: `y = sum_k b^{1-k/2} e_k` is in `L2_0(gamma)`
(coefficients square summable, sum `b^2/(b-1)`), while a preimage would need all
Hermite coefficients equal to `1`, which is not square summable. Injective with
dense nonclosed range puts `0` in the **continuous** spectrum. **Correct.**

*Endomorphism condition.* The theorem is explicit at `07b:830-835` that it is the
unit-variance normalization, not a general theorem, that makes source and target
the same space. **Correct and load-bearing.**

*Relevance (`def:rg-hermite-relevance`, `07b:899-910`).* `y_k = log_b b^{1-k/2} = 1 - k/2`,
so `k=1` relevant (`1/2`), `k=2` marginal, `k>=3` irrelevant, and the constant
mode is absent from the centered tangent (it would have eigenvalue `b` on full
`L2(gamma)`, which I verified: `I_b 1 = b`, `E[b|Z] = b`). Consistency with
`def:rg-mode-exponents`: for a stationary `lambda = b^{1-k/2}` and `b_k = b`,
`log|lambda_{n<-l}|/s_{n<-l} = (n-l)(1-k/2) log b / ((n-l) log b) = 1 - k/2`.
**Consistent.** The relevance statement is tagged `DEFINITION`, not a theorem,
and `07b:912-922` correctly localizes the source of `>1` growth in the extensive
factor `||I_b|| = sqrt b` with the norm held fixed across scales.

*Boundaries (`prop:rg-hermite-scope`, `07b:924-970`).*
Correlated: `Var(sum X_i) = b[1 + (b-1)rho]` requires `rho > -1/(b-1)`;
`Corr(X_i, Z) = alpha = sqrt([1+(b-1)rho]/b)`; `E[He_k(X_i)|Z] = alpha^k He_k(Z)`;
summing gives `b alpha^k = b^{1-k/2}[1+(b-1)rho]^{k/2}`, which differs from
`b^{1-k/2}` for every `rho != 0` and every `k >= 1`. **Correct.**
Multivariate: tensor Hermites factor, eigenvalue depends only on `|alpha|`,
multiplicity of degree `k` is `C(d+k-1, k)`; eigenvalues strictly decreasing in
`k` so degrees do not collide. **Correct.**
Gauge: `O(d)` preserves `N(0,I_d)` and commutes with the componentwise
normalized sum, hence preserves each degree space (the manuscript claims
preservation, **not** irreducibility, which would be false); a general `GL(d)`
map sends `N(0,I_d)` to `N(0,QQ^T)`, a different reference law. **Correct.**
Replication: `I_b h` is one restricted direction of `L2_0(gamma^{ob})`, silent
about interaction scores. **Correct.**
Nonlinear attraction is fenced `OPEN` at `07b:972-975` and in
`appendix_claim_ledger.tex:110-114`.

*Exponential-action domain (`prop:ig-hermite-exponential-domain`, `08:364-396`).*
I recomputed all four cases. `N_1(t) = e^{t^2/2}` finite for all `t`.
`N_2(t) = e^t int e^{-t x^2} dgamma`; the Gaussian integral converges iff
`t + 1/2 > 0` with value `(1+2t)^{-1/2}`, so `N_2(t) = e^t (1+2t)^{-1/2}` on
`t > -1/2`. **Correct including the closed form.** For `k >= 3` the exponent
`-t He_k(x) - x^2/2` has leading term `-t x^k` with `k > 2`; odd `k` diverges on
exactly one tail for each `t != 0`; even `k >= 4` diverges on both tails for
`t < 0` and converges for `t > 0`, with `N_k(0) = 1`, so finite exactly on
`t >= 0`. **Correct**, and the conclusion "no two-sided exponential action
neighborhood for `k >= 3`" follows in both parities.

### 3.4 Cocycle, modes, exponents, tempering (`07:471-738`, `07b:1366-1417`)

*Composition (`prop:rg-cocycle-composition`).* Induction with the Frechet chain
rule at `Phi_{n+1<-l} = T_n o Phi_{n<-l}`, using `Phi_{n<-l}(x_l) = x_n`, gives
`D Phi_{n+1<-l}(x_l) = M_n M_{n<-l}`. Order fixed with the rightmost factor
first. **Correct.** Noncommutativity witness `BA != AB` for the two unipotent
matrices: `BA = [[1,1],[1,2]]`, `AB = [[2,1],[1,1]]`. **Verified by hand.**

*Mode lines (`def:rg-mode-line`, `prop:rg-mode-product`).* `M_l v_{l,a} = lambda_{l,a} v_{l+1,a}`
is well typed; the induction `M_{n+1<-l} v = lambda_{n<-l} M_n v_n = lambda_{n<-l} lambda_n v_{n+1}`
gives the ordered product with empty product one and annihilation from a zero
factor. **Correct.** The ill-typing witness (`X_0 = R`, `X_1 = R^2`, `M_0 x = (x,0)`)
is valid.

*Exponents.* `chi_{n<-l}(v_{l,a}) = y_{n<-l,a} + [log||v_{n,a}||_n - log||v_{l,a}||_l]/s_{n<-l}`
follows by taking norms in the product law. Scalar regauging:
`M_l (c_l v_l) = c_l lambda_l v_{l+1} = lambda_l (c_l/c_{l+1}) (c_{l+1} v_{l+1})`,
so `lambda'_l = lambda_l c_l/c_{l+1}` and the product telescopes to
`lambda_{n<-l} c_l/c_n`. **Correct.**

*Tempered comparison (`thm:rg-tempered-comparison`).* From
`||x_n||_n/||J_n|| <= ||J_n^{-1} x_n||_* <= ||J_n^{-1}|| ||x_n||_n`
(the left half is `||x_n||_n = ||J_n (J_n^{-1} x_n)||_n <= ||J_n|| ||J_n^{-1} x_n||_*`),
the log numerators differ by at most
`max(log||J_n||, log||J_n^{-1}||) <= log^+||J_n|| + log^+||J_n^{-1}||`,
and the fixed initial scale contributes a constant. Dividing by
`s_{n<-l} -> inf` and applying `eq:rg-tempered-trivialization` makes the
difference vanish, so the upper and lower asymptotic rates agree. **Correct**,
and the hypothesis is correctly **bilateral**.

*Superexponential falsifier (`prop:rg-superexponential-distortion`).*
`J_k u = e^{k^2} u`, `M_k = I`, `b_k = e`. Then
`hat M_k = J_{k+1}^{-1} J_k = e^{k^2 - (k+1)^2} = e^{-2k-1}` and
`hat M_{n<-0} = e^{-sum_{k=0}^{n-1}(2k+1)} = e^{-n^2}` (the sum is exactly `n^2`),
while `s_{n<-0} = n`. The apparent rate is `-n -> -inf`, the native rate is `0`,
and `log||J_n||/s_{n<-0} = n^2/n = n` fails tempering. **Verified by hand;
the counterexample is correct and it does establish that tempering the scalar
mode normalization alone is insufficient.**

*Interaction tier (`cor:rg-interaction-tempered`).* Under the displayed growth
hypothesis `log^+||J_n|| + log^+||J_n^{-1}|| <= c(1 + |V_n|)`, tempering holds
whenever `|V_n|/s_{n<-l} -> 0`, in particular for nonincreasing vertex counts
with `b_k >= b > 1` (then `|V_n| <= |V_l|` and `s_{n<-l} >= (n-l) log b -> inf`).
**Correct.** See N-2 for the one soft sentence inside this corollary.

*Oseledets.* `07:728-738` defines the rates and **declines** the splitting,
listing the four missing hypotheses and citing `Arnold1998`, status `NOT-CLAIMED`.
**Correct discipline.**

### 3.5 Beta functions (`07b:2090-2426`)

*Change of reference (`prop:rg-action-beta-reference-change`).* With
`rho' = e^{-Delta} rho`, `rho(e^{-Delta}) = 1`, `Delta` bounded, `rho'` is a
probability measure equivalent to `rho` and `e^{-H'} rho' = e^{-H} rho = m`.
The Radon-Nikodym chain rule gives
`d(mK_b)/d(rho' K_b) = [d(mK_b)/d(rho K_b)] [d(rho' K_b)/d(rho K_b)]^{-1}`,
and `-log` of the second bracket is precisely `R_b^H[Delta; rho]` by the
definition `eq:rg-reference-dependent-action-map` applied to the pair
`(rho, e^{-Delta} rho)`. Hence
`R_b^H[H'; rho'] = R_b^H[H; rho] - R_b^H[Delta; rho]`, and dividing
`(... - H')/log b = (... - H + Delta)/log b` gives
`B[H'; rho'] = B[H; rho] - B[Delta; rho]`. The added term vanishes iff
`R_b^H[Delta; rho] = Delta`. **Correct**, and the boundedness of `Delta` is what
keeps the correcting factor strictly positive and finite, which the proof states.

*Typed discrete beta (`def:rg-interaction-beta`).* `hat T_l = J_{l+1}^{-1} T_l J_l : G_* -> G_*`
and `beta^ex(g) = (hat T_l(g) - g)/Delta s_l` with both numerator terms in `G_*`.
The cross-space subtraction `T_l(g) - g` is explicitly never formed, and `J_l`
is declared as `I_l^{-1}`, consistent with `eq:rg-reference-cocycle` in `07:45-50`.
The manifold caveat is stated. **Correct typing.**

*Retained/residual (`prop:rg-retained-beta-residual`).* Subtracting the two
definitions cancels `g` and leaves `(I - hat R_{l+1}) hat T_l(g)/Delta s_l`;
substituting `hat R = J^{-1} R J` and `hat T = J^{-1} T J` gives
`J_{l+1}^{-1} (I - R_{l+1}) T_l(J_l g)/Delta s_l = J_{l+1}^{-1} r_{l+1}(J_l g)/Delta s_l`.
Applying `E_{l+1}` and `P_{l+1}` with `P E = I` gives the quotient partner and
`P_{l+1} delta bar beta^Q = r/Delta s`. The biconditional uses injectivity of
`J_{l+1}^{-1}`, positivity of `Delta s_l`, idempotence of `R_{l+1}`
(`(I-R)x = 0` iff `x = Rx` iff `x in Ran R`), and `J_l(Ran hat R_l) = Ran R_l`.
**Correct.** The `R(x,y) = (x,0)`, `T(x,y) = (x,x)` witness gives
`beta^ret = (0,0)` and `beta^ex = (0,x)` on retained inputs; `R` is bounded and
idempotent, and `T(Ran R) not subset Ran R`. **Verified.** Bounded idempotence
is therefore not closure, and the manuscript says exactly that.

*Scheme dependence.* `J' = J S` gives `hat T' = S_{l+1}^{-1} hat T S_l`;
with `T = id`, `b = e`, `J_l u = a_l u`, `beta_l(g) = (a_l/a_{l+1} - 1) g`.
**Verified.**

*Continuous tier (`def:rg-scale-connection`).* I rederived the frame law from
`tilde g' = S_s tilde g`: matching `S_s(partial_s tilde g + A_s tilde g)` against
`partial_s tilde g' + A'_s tilde g'` forces
`A'_s = S_s A_s S_s^{-1} - (partial_s S_s) S_s^{-1}`. **Correct.** The witness
`S_s = e^{s^2}` gives `A'_s = -2s` and covariant derivative
`2s e^{s^2} - 2s e^{s^2} = 0` while the raw derivative is nonzero. **Correct.**
Underdetermination: `V^(eps)(s,t) = f(s)/f(t)` with `f(s) = exp(eps sin 2pi s)`
satisfies the two-parameter law and identity, equals `1` at all integer pairs,
and has generator `2 pi eps cos(2 pi t)` at `s = t`. **Verified.**

*Separation from time and from the contextual connection.* `07b:2314-2321` states
the scale connection has base `S` and compares coupling fibers across
resolutions, while `omega_b, omega_m` have base `C_l` at one resolution; and it
is separated from the inference-orbit parameter and from Fisher duration.
`appendix_notation.tex:285-288` records `s_{n<-l}` as "a scale index, not a
duration", and `:317-322` repeats the three-way separation. `07:41-43` states the
scale diagram introduces no time variable. **The separation is complete and no
external time variable is introduced.**

### 3.6 Fixed objects (`07b:2431-2622`)

The tier split (`def:rg-typed-fixed-objects`) distinguishes invariant sections
`y_{l+1} = F_l(y_l)` (needing no identification), reference fixed objects
`J_{l+1}^{-1} F_l J_l(y_*) = y_*`, and monodromy objects for `p`-periodic
identified sequences. `F_l(y) = y` is declared ill typed without a common object.
I checked all six non-implication witnesses in
`prop:rg-fixed-object-nonimplication`:

1. `mu = (1/2,1/2)`, `rho_0 = (1/4,3/4)`, `rho_1 = (3/4,1/4)`: `dmu/drho_0 = (2, 2/3)`,
   `dmu/drho_1 = (2/3, 2)`, distinct, so `H_0 != H_1`. **Verified.**
2. `H` and `H + c` are the same additive class while
   `(e^{-(H+c)} rho)(Y) = e^{-c} m(Y)`. **Verified**, and this is exactly why
   `eq:rg-fixed-action-ray` is strictly weaker than `eq:rg-fixed-measure-pair`
   until mass preservation forces `c_b = 0`.
3. `R, T` witness: retained beta zero, exact residual `(0,x)`. **Verified** (3.5).
4. `S^1` with antipodal step and constant extraction: the antipodal map on the
   circle has no fixed point while the extracted law is constant. **Verified.**
5. `eta_l = alpha_l beta` alternates when `alpha_l` alternates with `beta` fixed.
   **Verified**, and it matches the disintegration clause of
   `thm:rg-fixed-point-equations`.
6. `F_0(x) = x+1`, `F_1(x) = x-1`: `F_1 o F_0 = id` fixes every point while
   neither one-step map has a fixed point; the invariant object is the 2-cycle.
   **Verified.**

*No conflation.* `prop:rg-retained-beta-residual` states a retained beta is
called exact only after `eq:rg-beta-exactness-criterion` is proved, and
`07b:2260-2265` explicitly names the projected line of "fixed points" as an
artifact. `appendix_claim_ledger.tex:134-139` records that no nontrivial
invariant retained subspace is known and that "every reported projected flow
carries its residual". **Projected stationarity is nowhere identified with exact
fixedness.**

### 3.7 Lumpability (`thm:rg-strong-lumpability`, `07b:1890-1967`)

*Necessity.* `mu = delta_y` in `c_#(mu T) = (c_# mu) T^c` gives
`T(y, c^{-1}B) = T^c(c(y), B)` for every `y, B`, whose right side depends on `y`
only through `c(y)`; surjectivity of `c` makes `T^c` unique. **Correct.**

*Sufficiency.* Given the fiberwise condition and a Borel right inverse
`varsigma`, `T^c(z,B) = T(varsigma(z), c^{-1}B)` is countably additive in `B`
(`c^{-1}` preserves disjoint countable unions), has mass one (`c^{-1}Z = Y`),
and is Borel in `z` (composition of Borel `varsigma` with the measurable
`y -> T(y, c^{-1}B)`). Since `c(varsigma(c(y))) = c(y)`, the hypothesis gives
`T^c(c(y),B) = T(y, c^{-1}B)`, and integrating against `mu` yields the pushforward
identity. **Correct.** The two automatic selection cases (countable coarse space;
product projection with nonempty discarded factor) are correct, and the
measurable-selection obligation is declared when neither applies.

*The contrapositive, which is the audited risk.* `07b:1953-1963` says only:
strong lumpability is exactly the every-initial-law condition, **it is not
necessary for a single initial law**, and weak lumpability at a selected initial
law is strictly weaker and is the only statement available when the criterion
fails. I searched the whole chapter set
(`grep -rn -i 'lumpab|non-Markov|first-order Markov|not Markov' manuscripts/gauge_vfe_rg/*.tex`)
and there is **no** surviving sentence claiming that failure forces some
individual coarse process to be non-Markov. The only adjacent statement,
`07b:1888`, is the weak and correct "It need not be first-order Markov."

*The manuscript's own witness.* `Y = {1,2,3}`, `c(1) = c(2) = a`, `c(3) = beta`,
`1 -> 3` surely, `2 -> {1,2}` uniform, `3 -> {1,3}` uniform. Then
`T(1,{1,2}) = 0 != 1 = T(2,{1,2})`, so the criterion fails; started at
`delta_3` the chain never leaves `{1,3}`, where `c` is injective, so the coarse
process is the relabeled fine chain, Markov with `a -> beta` surely and
`beta -> {a, beta}` uniform. **Verified.**

*The `a,b,u,v` test required by the charter.* `E = {a,b,u,v}`, `F = {0,1,2}`,
`c(a) = c(b) = 0`, `c(u) = 1`, `c(v) = 2`, deterministic `a -> u`, `b -> v`,
`u -> u`, `v -> v`. The fiber condition fails at `c^{-1}(0)` since the one-step
probability of coarse state `1` is `1` from `a` and `0` from `b`. Yet for every
initial law `mu` the coarse process is a homogeneous Markov chain: coarse `1` and
`2` are absorbing, coarse `0` is never revisited, and its only used row is
`K_mu(0,1) = mu(a)/(mu(a)+mu(b))`, `K_mu(0,2) = mu(b)/(mu(a)+mu(b))`. What fails
is that `K_mu` depends on `mu`. **The manuscript's statement survives this test:
it rules out a single initial-law-independent coarse kernel and claims nothing
more.**

*Memory recurrence (`thm:rg-projection-memory`).* With `CP = I`, `Pi = PC`
idempotent, `Q = I - Pi`, `x_n = P w_n + Q x_n`, the coupled system is
`w_{n+1} = CTP w_n + CTQ (Q x_n)` and `Q x_{n+1} = QTQ (Q x_n) + QTP w_n`.
I verified the induction for `eq:rg-unresolved-solution` at `n = 0` and at the
step (`QTQ` applied to case `n` plus `QTP w_n` reproduces case `n+1`, the new
`k = n` term being `(QTQ)^0 QTP w_n`), and substitution gives
`eq:rg-memory-recurrence` term by term. **Correct, exact, no closure assumed.**
The autonomy witness (`C(x,y) = x`, `P(w) = (w,0)`, `T(x,y) = (x,x)`) gives
`Q(x,y) = (0,y)`, `CTQ = 0` so all memory kernels vanish, `QTP w = (0,w) != 0`,
and `w_{n+1} = w_n` on the resolved class. **Verified**: `QTP = 0` is sufficient,
not necessary.

### 3.8 Source scope and bibliography

All five citation sites, found by
`grep -rn 'JonaLasinio2001|KemenySnell1976|Nakajima1958|Zwanzig1960|Arnold1998' manuscripts/gauge_vfe_rg/*.tex`:

* `07b:976` and `07b:982-997`: Jona-Lasinio is cited for the binary
  normalized-sum Gaussian/Hermite linearization (Section 2), the
  conditional-expectation identification at a self-similar Gaussian fixed point
  (Section 5), the two-tangent-space eigenvalue equation and its multiplicative
  composition law (Section 7), and the author's own statement that the nonlinear
  terms are not pursued. The "Source scope" paragraph then explicitly
  **non-attributes** the arbitrary-integer statement, the quadratic-mean
  realization, the extensive Fisher budget, the exact spectrum including the
  status of `0`, the correlated boundary, and the typed cocycle. This is exactly
  the narrowed scope the primary-source audit demands, and it does not exceed
  what a linearized-RG/Hermite/cocycle source can support. **Closed.**
* `07b:1965`: `\citet[Ch.~6]{KemenySnell1976}`, described as the classical
  **finite-state** criterion, with the standard-Borel biconditional proved in the
  manuscript. **Closed.** (Coarser than the audited `Sec. 6.3, Thm. 6.3.2, p. 124`
  anchor, which is the conservative direction.)
* `07b:2058`: Nakajima and Zwanzig cited as the historical continuous-time
  projection-operator antecedent, explicitly "not as proofs of
  `eq:rg-memory-recurrence`". **Closed.**
* `07:735`: `Arnold1998` cited once inside the `NOT-CLAIMED` paragraph that
  declines an Oseledets splitting. **Closed.**

No manuscript proof step depends on any of the five sources. Bibliography
mechanics: 464 entries, **0** duplicate keys exact, **0** case-insensitive; 79
unique cited keys, **0** undefined. Metadata for the five entries is internally
consistent with the audited publisher records. Two title fields are abbreviated
relative to the audited records; see N-3.

### 3.9 Status discipline

* `\status{NUMERICAL}` occurs three times across the Task 9 file set, all in
  `08_infogeometry.tex` at lines 195, 334, 488, all pre-existing (`git blame`
  predates the Task 9 working-tree edits), and each is explicitly self-limiting:
  "The computation is reproducible corroboration, not a proof."; "Computation is
  not proof and the proof is above."; "It establishes numerical usability only
  for that protocol; congruence invariance is proved above." **No numerical or
  heuristic evidence is presented as proof.**
* No Task 10 claim is closed. `claim-ledger.json` keeps `score-action-compatibility`,
  `bundle-fisher-defect`, `bundle-morphism-descent`, `bundle-scale-cocycle`,
  `horizontal-defect-anomaly`, `pullback-compatibility`, `configuration-fisher-metric`,
  `configuration-map`, `configuration-projectability`, `history-semiconjugacy`,
  `history-noncollapse`, and `history-duration-relation` at `CANDIDATE`, and
  `appendix_claim_ledger.tex:147-154` keeps fine-coarse history semiconjugacy
  `OPEN`. `adversarial-report.json.oracle_erasure.result = "NOT_RUN"` with
  `"No terminal release is attempted at this checkpoint"`. **Correct.**
* No hidden finite-graph-only claim. The Gaussian Hermite theorem is explicitly a
  scalar independent realization, fenced by `prop:rg-hermite-scope` and by the
  `OPEN` ledger entry "Extensive relevance beyond the scalar Gaussian
  realization". The cocycle, beta, fixed-object, lumpability, and memory results
  are stated for arbitrary Banach/standard-Borel data with no cardinality bound.
  The one finite-size quantity that appears, `||P_l|| <= 3^{|V_l|} - 1`, is used
  as a **hypothesis generator** in `cor:rg-interaction-tempered` and is honestly
  flagged at `07b:1411-1417` as a mechanism by which a fast-growing network can
  break tempering. **No fixed-size enumeration stands in for the quantifier.**

---

## 4. Non-blocking findings

These are recorded for completeness. None of them is a blocker and none should
be escalated into one.

**N-1 (minor, wording).** `07b:2610-2615` and `prop:rg-mode-tempered-normalization`
(`07:651-652`) say the scalar exponent "is unchanged **exactly when**
`|log|c_{n,a}||/s_{n<-l} -> 0`". Read as "the finite-time exponent family is
asymptotically unchanged", the biconditional holds. Read as "the asymptotic
limsup is unchanged", the necessity direction fails for a particular mode: take
`lambda_k = 1` and `c_n` with `log|c_n|/s_n` alternating between `0` and `-1`;
the limsup is `0` before and after. The load-bearing statement,
`thm:rg-tempered-comparison`, is correctly phrased as sufficient, so nothing
downstream depends on the stronger reading. Suggested wording: "the finite-time
scalar exponents differ by an amount tending to zero exactly when ...".

**N-2 (minor, incomplete justification inside a hypothesis-gated corollary).**
`cor:rg-interaction-tempered` (`07b:1392-1396`) asserts that the growth bound
"holds for every trivialization assembled from the maps of
`eq:rg-hoeffding-inverse-and-bounds` together with a bounded gauge realization,
because `||E_l|| <= 1` and `||P_l|| <= 3^{|V_l|} - 1`". The stated reason
bounds `||J_n||` but not `||J_n^{-1}||`, and it does not exhibit an `n`-uniform
constant for the gauge factor. For the natural assembly
`J_n = P_n o (gauge) o E_*` the claim does hold, with
`log^+||J_n|| <= |V_n| log 3 + O(1)` and `log^+||J_n^{-1}|| = O(1)` (the inverse
routes through the fixed reference network `V_*`), so `c` exists. The corollary's
conclusion is gated on the displayed hypothesis and is unaffected, but the
intermediate sentence currently asserts more than its stated reason delivers.

**N-3 (minor, bibliography metadata).** `manuscripts/references.bib:1129` gives
`Nakajima1958` the title "On Quantum Theory of Transport Phenomena", dropping
the subtitle "Steady Diffusion" that
`evidence/task-9-primary-source-map.md:300` records from the publisher page.
`references.bib:1119` gives `KemenySnell1976` the short title "Finite Markov
Chains" rather than the full 1976 Springer title recorded at
`task-9-primary-source-map.md:299`. Neither abbreviation changes the resolvable
identity of the work (both carry DOI/ISBN-grade fields), and neither affects any
attributed claim.

**N-4 (minor, provenance binding).**
`evidence/task-9-primary-source-map.md` exists on disk as an untracked Task 9
artifact (SHA-256 `ad0e8102fbee51f0302cd0d05bcf6e019be16d39911da24a2b9d90286a6350e2`)
but is **not** bound by any digest in `claim-ledger.json`, in
`adversarial-report.json`, or in `evidence/task-9-integrated-proof.md`. It is also
the only Task 9 artifact that records direct access to the primary PDF
(`task-9-primary-source-map.md:55` reports a downloaded arXiv PDF digest) and
that asserts equation-level anchors, whereas the bound record
(`task-9-integrated-proof.md:544-549`) states that the primary PDF text could not
be opened in the integration environment and therefore coarsens the citation to
section granularity. The two are reconcilable as different passes in different
environments, and the manuscript takes the conservative route, so no attributed
claim is overstated. The residual issue is bookkeeping: an unbound artifact in
the evidence directory asserts a stronger anchoring than the bound record, and
the run package's own discipline is recomputation of every evidence artifact
digest. Either bind it (with its scope explicitly marked as not asserted in the
manuscript) or move it out of `evidence/`.

**N-5 (minor, an inaccurate sentence in a Task 9 mechanical-control claim).**
`evidence/task-9-integrated-proof.md:642-645` states that the three remaining
multi-`\status` lines are ones "where each tag scopes a distinct sentence-level
claim". That is accurate for `08_infogeometry.tex:503` and `:529` but not for
`:543`, which is the last line of the file and reads exactly
`\status{ESTABLISHED} \status{NOT-CLAIMED}`, two adjacent tags with no
intervening text. All three lines are pre-existing (`git blame`: `a2cca53b`,
`96b7b5f6`, `0af1cbd3`); the count "none introduced by this pass" is correct;
only the characterization of the third is wrong. The repair itself remains Task 11
scope per the plan.

**N-6 (informational, not a defect).** The Task 3 verification-skill control
plane is drifted, as `task-9-integrated-proof.md:653-693` reports. I confirmed
independently that the three `.verification/*.json` files remain **untracked and
unmodified** by this pass and by Task 9 (`git status --short` shows them as `??`,
and their digests are recorded in the static-control report). Task 9 correctly
did not silence the alarm. That obligation belongs to the verification skill, not
to Task 9, and it is not counted against this verdict.

---

## 5. What would change this verdict

FAIL becomes PASS when, and only when:

1. B-1 is repaired at all four sites in `07b_agent_network_rg.tex`, and
2. a check that detects the class (heading second argument must be a brace group,
   or an actual `pdflatex` pass with zero undefined references, zero literal `??`,
   and zero duplicate labels) is run and recorded over the repaired bytes, and
3. the source digests in `evidence/task-9-integrated-proof.md` Section 3 and the
   evidence digests in `claim-ledger.json` are recomputed against the new bytes,
   since a source edit invalidates the current bindings.

No mathematical repair is required. I attempted to break every Task 9 theorem
along the lines listed in the charter and in the counterexample register, and
each attack was defeated by the manuscript's own hypotheses. The specific attacks
I ran and failed to land are: confining the DQM tangent to bounded scores;
dropping the sign-change tail in `sqrt(p_t)`; replacing the replication sum by a
mean; identifying the bounded action quotient with `L2_0`; reading Fisher
equality as sufficiency; claiming `0` is an eigenvalue of `L_b`; asserting simple
eigenvalues in dimension `d > 1`; keeping the uncorrelated normalization under
correlation; writing `M_l v = lambda v`; reversing the ordered product;
tempering only the scalar mode normalization; calling a retained fixed line
exact; reporting a beta without its comparison scheme; inferring a continuous
beta from discrete endpoints; transferring fixedness across tiers; calling a
monodromy point one-step fixed; and inferring individual non-Markovness from
failure of strong lumpability.
