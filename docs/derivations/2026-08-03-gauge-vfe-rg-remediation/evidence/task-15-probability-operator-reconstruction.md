<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 15 probability/operator/ELBO reconstruction

## Frozen basis, scope, and verdict

This memo independently reconstructs the scoped probability, operator, and ELBO claims directly from the manuscript's definitions and hypotheses. No theorem conclusion is used as a premise. The reconstruction is frozen to Git revision `14551bb8d463f229a3b451d7222042d134c2c52d` and to contract `contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b`. The contract's relevant domain is a finite standard-Borel product network, a finite positive measure pair, and a normalized parameter-independent Markov kernel; see `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/problem-contract.json:5-32,49-57,66-78`.

The source snapshot is:

| Source | SHA-256 |
|---|---|
| `manuscripts/gauge_vfe_rg/SPEC.md` | `ab59a4d02e1c475b6384403013458d39f88f170d592edf802d4c772dd7320571` |
| `manuscripts/gauge_vfe_rg/03_probability.tex` | `5cf6a326900cf373f04f6d05379df20cca0edc1cdde51a0daae9e739a9813520` |
| `manuscripts/gauge_vfe_rg/05_elbo.tex` | `d6bd224135ed4cf370548729713555415b4cc0eef5f76f6c7a65853d073ff2cc` |
| `manuscripts/gauge_vfe_rg/05b_local_collective_elbo.tex` | `22d35509fa707e46de71e331df614ccf2aa48572cc456a02ee717a7a9dc39b60` |
| `manuscripts/gauge_vfe_rg/06_general_coarsegraining.tex` | `4891a8f5fa86ac0fa5266381e2c67161125645034ca40395cb2e3ed1b67dc9b2` |
| `manuscripts/gauge_vfe_rg/07_general_renormalization.tex` | `ceda98a49f4122de39d70f784288860ab727abfa217a92b1230591e6ce76bcad` |
| `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex` | `5eb159493ec727218e2eaca4cf47f3fddeb090f6e193352846ad2a43181437ca` |
| `docs/derivations/2026-08-03-gauge-vfe-rg-remediation/problem-contract.json` | `7cba2e9bbfe34028d6a994359e53c761779bd255c5405bfa3996c50ca575bc22` |

**Scoped verdict: PASS.** I found no load-bearing defect in the finite-network probability/action/ELBO chain under its stated hypotheses. Every scoped identity below is supported by a direct measure-theoretic derivation. The result has exact boundaries, however: the classical split ELBO needs absolute continuity and log-integrability; an ordinary coarse/fine VFE difference needs finite fine KL; nonlinear action derivatives live on bounded finite-action charts; the general Fisher theorem admits an `o(||h||^2)` singular component whereas the later score-coordinate definition is deliberately dominated; local conditional VFEs are coordinate potentials rather than summable agent costs; observation-as-interaction preserves the conditioning sigma-algebra; the attention row formula needs label exclusivity and full recognition factorization; and Hoeffding extraction needs product equivalence separately at every scale. Removing any one of these premises activates an explicit counterexample below.

This is a scoped evidence verdict, not a release decision for geometric, gauge, configuration, history, or spectral claims outside this memo.

## Claim record

| ID | Atomic claim | Result | Closing evidence in this memo |
|---|---|---|---|
| P15-01 | Normalized probability kernels, regular conditional versions, and the extended/classical ELBO are correctly typed. | Supported | Direct RN/KL derivation and singular/log-tail counterexamples in Section 1. |
| P15-02 | A fixed normalized Markov kernel pushes the complete measure pair exactly and induces the stated RN action. | Supported | Null-set, mass, RN, and tower proofs in Section 2. |
| P15-03 | The bounded nonlinear action map is a conditional log-Laplace map with the stated first and second Frechet derivatives. | Supported | Banach-algebra and tilted-kernel calculation in Section 3. |
| P15-04 | Reverse conditional expectation contracts `L^p`, and its `L^2` defect and equality condition are exact. | Supported | Conditional Jensen and total-variance proof in Section 4. |
| P15-05 | Parameter-independent coarse-graining preserves DQM, including admissible singular parts, and contracts Fisher information. | Supported | Joint-lift/statistic proof, sharp singular-mass witnesses, and equality boundary in Section 5. |
| P15-06 | A common latent channel gives the exact coarse VFE chain rule without changing evidence. | Supported | Relative-entropy chain rule and finite equality condition in Section 6. |
| P15-07 | Collective, block-local, and local-global ELBO statements are exact, but the local objectives do not form an additive ledger. | Supported | Conditional posterior/KL chain proofs and a two-agent overcounting witness in Section 7. |
| P15-08 | Attention as an exclusive latent label gives the stated posterior row and constant-row ELBO; correlations add conditional total correlation. | Supported | Bayes/Gibbs calculation and two finite counterexamples in Section 8. |
| P15-09 | Observation kernels admit an interaction presentation without deleting the conditioning information. | Supported | Kernel randomization, mutual-information chain rule, and a Bernoulli deletion witness in Section 9. |
| P15-10 | Full finite Hoeffding extraction is correctly typed only after scale-wise product equivalence is supplied. | Supported | Mobius inversion and diagonal-cloning counterexample in Section 10. |

No claim in this table depends on agent agreement. Its closing support is the displayed derivation or counterexample at the frozen source revision.

## 1. Probability substrate and exact ELBO domain

### 1.1 Normalized measures precede densities

The manuscript first declares normalized generative and recognition kernels and only then extracts RN densities. In particular,

\[
P_\theta(do,dy\mid X)
=p_\theta(o,y\mid X)\,\nu_D^O(do)\nu_D^Y(dy),
\qquad
p_\theta(o\mid X)=\int p_\theta(o,y\mid X)\nu_D^Y(dy).
\]

This ordering is explicit at `manuscripts/gauge_vfe_rg/03_probability.tex:123-137` (`def:prob-normalized-kernels`, `eq:prob-generative-density`, `eq:prob-evidence`). It rules out treating an arbitrary nonnegative energy factor as a probability before proving that its normalizer lies in \((0,+\infty)\).

On standard-Borel observation and latent spaces, a regular conditional posterior exists and is unique only for observation-marginal-almost every `o`. On the selected full-measure regular set,

\[
0<p_\theta(o\mid X)<\infty,
\qquad
\Pi_{\theta,X}(o,B)
=\frac{\int_Bp_\theta(o,y\mid X)\nu_D^Y(dy)}{p_\theta(o\mid X)}.
\]

The exact source is `03_probability.tex:140-180` (`eq:prob-regular-observations`, `eq:prob-rcp-density`). The source's `o=0` slice witness is decisive: two Lebesgue-density versions of the same Gaussian product law can be changed on `{0} x R` so that their ratio formulas give different posteriors at `o=0`. Hence a version-independent pointwise ELBO at every observation would be false. The actual theorem correctly asserts the result only on a selected regular version, equivalently almost surely in `o`.

### 1.2 Extended ELBO is primary

Fix a regular observation and define the finite slice measure and posterior

\[
M_o(B)=\int_Bp_\theta(o,y\mid X)\nu_D^Y(dy),
\qquad z=M_o(\mathsf Y_D)\in(0,\infty),
\qquad \Pi_o=M_o/z.
\]

For every probability law `Q`, including singular laws, define

\[
\mathcal L_o^{\rm ext}(Q)=\log z-\mathrm{KL}(Q\Vert\Pi_o),
\qquad
\mathcal F_o^{\rm ext}(Q)=-\log z+\mathrm{KL}(Q\Vert\Pi_o).
\]

These are well-defined because a finite real number is combined with a member of \([0,+\infty]\); no \(\infty-\infty\) subtraction occurs. The exact gap is

\[
\log z-\mathcal L_o^{\rm ext}(Q)
=\mathcal F_o^{\rm ext}(Q)+\log z
=\mathrm{KL}(Q\Vert\Pi_o).
\]

Thus `L_ext <= log z`, and equality holds exactly when `Q=Pi_o` as measures. This is `manuscripts/gauge_vfe_rg/05_elbo.tex:154-210` (`def:elbo-extended`, `thm:elbo-extended-gap`, `prop:elbo-relative-log-representation`). The source correctly avoids the superficially familiar but undefined expression \(\log z=(-\infty)+(+\infty)\) on the singular branch.

The same extended functional also has a genuine relative-log representation. If `Q << M_o` and `r=dQ/dM_o`, then

\[
\mathcal L_o^{\rm ext}(Q)=-\int\log r\,dQ,
\qquad
\int_{\{r<1\}}-\log r\,dQ
=\int_{\{r<1\}}-r\log r\,dM_o\leq z/e.
\]

The bound `-u log u <= 1/e` makes the favorable part integrable, so the integral is a legitimate extended integral rather than an infinity cancellation. If `Q` is not absolutely continuous with respect to `M_o`, the extended ELBO is `-infinity` by definition.

The classical split

\[
\mathcal L_o(Q)
=\mathbb E_Q[\log p_\theta(o,Y\mid X)-\log q(Y\mid o)]
\]

requires all four hypotheses at `05_elbo.tex:118-135` (`hyp:elbo-evidence-domain`): normalized measurable kernels and a selected conditional version, positive finite evidence, `Q << Pi_o` with a recognition density, and absolute integrability of the two log terms. Under those hypotheses the RN chain rule gives

\[
\frac{dQ}{d\Pi_o}(y)
=\frac{q(y\mid o)z}{p_\theta(o,y\mid X)},
\]

and termwise integration yields

\[
\log p_\theta(o\mid X)
=\mathcal L_o(Q)+\mathrm{KL}(Q\Vert\Pi_o).
\]

The derivation and equality condition are at `05_elbo.tex:227-289` (`thm:elbo-exact-identity`, `cor:elbo-bound-tightness`).

Two boundary witnesses are exact. First, if a Lebesgue-dominated posterior on `R^d` is compared with a `Q` supported on a proper affine subspace `S`, then `Pi_o(S)=0` and `Q(S)=1`; hence `Q` is not absolutely continuous and its KL is \(+\infty\). This is a set argument, not a density argument, and matches `03_probability.tex:329-351` (`prop:prob-density-absolute-continuity`, `eq:prob-direct-null-set`) and `05_elbo.tex:139-149` (`prop:elbo-subspace-support-singular`). Second, a standard Cauchy `Q` and standard Gaussian `Pi_o` have positive densities, so absolute continuity holds, but \(\mathbb E_Q|\log p|=\infty\) because the Cauchy law lacks a second moment. The extended ELBO still exists; only the split representation fails (`05_elbo.tex:127-135`).

**Falsification condition P15-01.** An admitted regular observation and probability `Q` for which the RN calculation above fails, or for which a zero KL does not imply equality of measures, would refute the claim. The slice-version and Cauchy witnesses instead show that the manuscript placed the hypotheses exactly where needed.

## 2. Measure-pair pushforward and RN action

Let `(X,F)` be standard Borel, let `rho` be a probability measure, and let `m << rho` be finite and positive with

\[
m(dx)=e^{-H(x)}\rho(dx),
\qquad 0<M=m(\mathsf X)<\infty,
\qquad \pi=m/M.
\]

Let `K:X -> Z` be a normalized, parameter-independent Markov kernel and define

\[
\rho'=\rho K,
\qquad m'=mK,
\qquad \pi'=\pi K.
\]

These are the objects declared at `manuscripts/gauge_vfe_rg/07_general_renormalization.tex:76-109` (`def:rg-measure-pair`, `eq:rg-measure-pair-normalization`, `eq:rg-measure-pair-arrow`, `eq:rg-measure-pair-action`). Their exactness follows from three elementary facts.

First, if `rho'(A)=0`, then

\[
0=\int K(x,A)\rho(dx)
\]

and nonnegativity implies `K(x,A)=0` for `rho`-almost every `x`. Since `m << rho`, the same holds `m`-almost everywhere, so `m'(A)=0`. Hence `m' << rho'` and the RN derivative `L'=dm'/d rho'` exists. The downstream action is the equivalence class

\[
H'=-\log L'\quad \rho'\text{-almost everywhere},
\]

with \(-\log 0=+\infty\). Second, kernel normalization preserves mass:

\[
m'(\mathsf Z)=\int K(x,\mathsf Z)m(dx)=M.
\]

Therefore `m'/M=(m/M)K=pi K`, proving the normalized-law formula. Third, Tonelli and associativity of kernel composition give

\[
(\rho,m)(K_1K_2)=((\rho K_1)K_2,(mK_1)K_2).
\]

This is the full proof of `07_general_renormalization.tex:111-137` (`prop:rg-measure-pair-composition`, `eq:rg-normalized-law-pushforward`). It also shows why the evidence mass and normalized law are different components: normalizing `m` discards `M`, while the pair retains it.

If `L=dm/d rho=e^{-H}` and `R_rho(z,dx)` is a reverse conditional under the joint `rho(dx)K(x,dz)`, then for every bounded measurable `f`,

\[
\begin{aligned}
\int f(z)m'(dz)
&=\iint f(z)L(x)K(x,dz)\rho(dx)\\
&=\int f(z)\left[\int L(x)R_\rho(z,dx)\right]\rho'(dz).
\end{aligned}
\]

RN uniqueness therefore gives

\[
e^{-H'(z)}=L'(z)
=\mathbb E_\rho[L(X)\mid Z=z]
=\int e^{-H(x)}R_\rho(z,dx)
\quad \rho'\text{-almost everywhere}.
\]

Setting `f=1` recovers `M`; applying the tower property to two kernels proves direct/staged agreement. This reconstructs `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex:78-139` (`eq:rg-success-submeasure` through `thm:rg-effective-action`).

**Equality and boundary.** Composition is equality of measure pairs, not equality of pointwise density versions. Actions are only RN equivalence classes. A literal finite action is not needed, and no \(+\infty-(+\infty)\) is formed. If `K` is not normalized, mass preservation fails. If `m` is not absolutely continuous with respect to `rho`, the asserted action is not defined relative to that reference. If one pushes `m` but not its reference, the RN type changes and the displayed conditional-partition formula is not licensed. These are direct falsification conditions for P15-02.

## 3. Nonlinear conditional log-Laplace action

Base the local action calculation at the normalized pair `pi=m/M`, `pi^c=pi C`, and choose a reverse kernel `Pi(z,dy)` satisfying

\[
\pi(dy)C(y,dz)=\pi^c(dz)\Pi(z,dy).
\]

For a bounded action increment `phi`, perturb the unnormalized measure by `m^phi=e^{-phi}m`. RN division by `mC` gives

\[
\boxed{
Q(\varphi)(z)
=-\log\frac{d((e^{-\varphi}m)C)}{d(mC)}(z)
=-\log\int e^{-\varphi(y)}\Pi(z,dy).}
\]

This is `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex:149-188` (`eq:rg-normalized-reverse-kernel`, `eq:rg-local-action-map`). It is defined on all of \(L^\infty(\pi)\) because

\[
e^{-\|\varphi\|_\infty}
\leq \int e^{-\varphi}d\Pi_z
\leq e^{\|\varphi\|_\infty},
\qquad
|Q(\varphi)(z)|\leq\|\varphi\|_\infty.
\]

Write \(Uh(z)=\int h\,d\Pi_z\). On the origin-centered ball \(\|\varphi\|_\infty<\epsilon<\log 2\),

\[
\|U(e^{-\varphi})-1\|_\infty
\leq e^\epsilon-1<1.
\]

The exponential series in \(L^\infty(\pi)\) and the logarithm series in \(L^\infty(\pi^c)\) therefore converge in their Banach algebras. Differentiating \(Q(\varphi)=-\log U(e^{-\varphi})\) gives the normalized tilted kernel

\[
\Pi^\varphi(z,dy)
=\frac{e^{-\varphi(y)}\Pi(z,dy)}{\int e^{-\varphi(u)}\Pi(z,du)}
\]

and the exact Frechet derivatives

\[
DQ(\varphi)[h](z)=\int h\,d\Pi_z^\varphi,
\qquad
D^2Q(\varphi)[h,k](z)
=-\operatorname{Cov}_{\Pi_z^\varphi}(h,k).
\]

At zero these reduce to `DQ(0)=U` and `D^2Q(0)[h,k]=-Cov_{Pi_z}(h,k)`. The covariance is bounded in \(L^\infty(\pi^c)\), so these are typed Frechet derivatives, not merely pointwise formal derivatives. This reconstructs `07b_agent_network_rg.tex:190-257` (`thm:rg-bounded-action-calculus`, `eq:rg-action-first-frechet-general`, `eq:rg-action-second-frechet-general`). Replacing `U` by

\[
U^\varphi h=\frac{U(e^{-\varphi}h)}{U(e^{-\varphi})}
\]

repeats the same argument around every bounded center, as stated at `07b_agent_network_rg.tex:259-300` (`prop:rg-action-bounded-recentering`). The `epsilon<log 2` radius is a convenient sufficient radius for one log series, not a singular boundary of `Q` on bounded actions.

The second variation has the sharp equality condition

\[
D^2Q(\varphi)[h,h]=0\quad \pi^c\text{-almost everywhere}
\]

if and only if `h` is constant on `Pi_z^phi`-almost every conditional fiber, equivalently there is measurable `g(z)` with `h(y)=g(z)` under the tilted joint. Strict bounded positivity makes that joint equivalent to the untilted joint, so the null-set statement is stable under bounded recentering.

The map is additively homogeneous and nonexpansive:

\[
Q(\varphi+c)=Q(\varphi)+c,
\qquad
\|Q(\varphi)-Q(\psi)\|_\infty
\leq\|\varphi-\psi\|_\infty.
\]

Indeed, `phi <= psi+delta` implies `Q(phi)<=Q(psi)+delta`, and the reverse inequality follows after swapping them. The exact equality condition for this global supremum bound is

\[
\operatorname*{ess\,sup}_{z}
\left|\log\mathbb E_{\Pi_z^\psi}
[e^{-(\varphi-\psi)}]\right|
=\|\varphi-\psi\|_\infty;
\]

conditional-fiber measurability of `phi-psi` is a clean sufficient case, and deterministic invertible channels realize equality for every increment. The source only claims the inequality, not a stronger universal strictness result (`07b_agent_network_rg.tex:302-317`, `eq:rg-nonlinear-action-sup-contraction`).

Constants must remain when evidence mass is retained. Only after deliberately forgetting mass may one pass to \(L^\infty/\mathbb R1\); the normalized probability perturbation differs from the unnormalized action by `log pi(e^{-phi})`, and its score is `-h+pi(h)` (`07b_agent_network_rg.tex:319-356`). At an extended-valued or unbounded boundary, the RN measure-pair action remains meaningful when dominated, but this bounded Frechet calculus and a literal action beta difference do not (`07b_agent_network_rg.tex:358-365`). A concrete separating direction is `He_3(x)=x^3-3x` under a standard Gaussian: it is in `L^2_0`, but \(\int e^{-t\mathrm{He}_3(x)}\gamma(dx)=\infty\) for every nonzero `t`, because one cubic tail has positive leading exponent on either sign of `t` (`07b_agent_network_rg.tex:821-852`).

**Falsification condition P15-03.** A bounded `phi` for which the conditional exponential moment vanishes or diverges, or a bounded direction for which differentiation gives a term other than the tilted mean/covariance, would refute the claim. The uniform bounds above exclude both possibilities. An unbounded `L^2` direction is not an admitted counterexample because it lies outside the nonlinear chart.

## 4. `L^p` contraction and the exact `L^2` defect

For the same reverse conditional operator,

\[
(U\varphi)(z)=\mathbb E[\varphi(Y)\mid Z=z],
\]

conditional Jensen gives, for \(1\leq p<\infty\),

\[
|U\varphi|^p\leq U|\varphi|^p,
\qquad
\|U\varphi\|_{L^p(\pi^c)}^p
\leq\|\varphi\|_{L^p(\pi)}^p.
\]

For \(p=\infty\), \(|U\varphi|\leq U|\varphi|\leq\|\varphi\|_\infty\). Disintegration also gives mean preservation. Thus `U:L^p(pi)->L^p(pi^c)` is a contraction and maps centered tangents to centered tangents. At `p=2`, total conditional variance gives the exact Pythagorean identity

\[
\boxed{
\|\varphi\|_{L^2(\pi)}^2
-\|U\varphi\|_{L^2(\pi^c)}^2
=\int\operatorname{Var}_{\Pi(z,\cdot)}(\varphi)\pi^c(dz)\geq0.}
\]

The defect vanishes if and only if the conditional variance is zero `pi^c`-almost everywhere, equivalently

\[
\varphi(y)=g(z)
\quad\text{for }\pi(dy)C(y,dz)\text{-almost every }(y,z)
\]

for some measurable `g`. For a deterministic block map `z=c(y)`, this is exactly \(\varphi=g\circ c\) almost everywhere. This is the complete proof and equality condition of `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex:370-414` (`thm:rg-action-lp-contraction`, `eq:rg-action-l2-conditional-defect`). The theorem does not claim one common equality characterization for all `p`: strict convexity gives conditional constancy for \(1<p<\infty\), the `p=1` condition permits conditionally common signs, and the \(p=\infty\) norm can be saturated without fiberwise constancy.

**Falsification condition P15-04.** A normalized fixed channel and `phi in L^p(pi)` with a larger output norm would refute contraction. At `p=2`, a zero defect with a nonmeasurable residual `phi-Uphi` of positive squared norm would refute the equality claim. Both are excluded by Jensen and the orthogonal-projection identity. Replicating one input law into an independent `b`-sample is not such a counterexample: the score replication map goes from one tangent space to a different product tangent space and has norm `sqrt(b)`; it is not a Markov pushforward from the original experiment (`07b_agent_network_rg.tex:601-650,854-869`).

## 5. DQM, singular parts, and Fisher contraction

### 5.1 The general Le Cam tier

The general theorem uses DQM at `theta_0` in its non-dominated form. For `h -> 0`, write the Lebesgue decomposition

\[
P_{\theta_0+h}=p_hP_0+P_h^\perp,
\qquad P_h^\perp\perp P_0,
\]

and require

\[
P_h^\perp(\mathsf X)=o(\|h\|^2),
\qquad
\int\left(\sqrt{p_h}-1-\frac12h^T\ell_0\right)^2dP_0
=o(\|h\|^2),
\]

with `ell_0 in L^2_0(P_0;R^d)`. This is the definition used in the proof at `manuscripts/gauge_vfe_rg/06_general_coarsegraining.tex:170-224` (`thm:cg-fisher-contraction`, especially lines 193-220). It matches Definition 4 in David Pollard's primary paper, [*A note on insufficiency and the preservation of Fisher information*](https://arxiv.org/pdf/1107.3797), pp. 4-5; Pollard's Theorem 7 gives preservation under a statistic and the conditional score.

Let `K` be normalized and parameter independent. Lift the experiment to

\[
J_{\theta}(dx,dy)=P_\theta(dx)K(x,dy).
\]

If `A_h` supports `P_h^perp` and is `P_0`-null, then `A_h x Y` is `J_0`-null and

\[
J_{\theta_0+h}=p_h(x)J_0+P_h^\perp K,
\qquad
(P_h^\perp K)(\mathsf X\times\mathsf Y)
=P_h^\perp(\mathsf X)=o(\|h\|^2).
\]

The square-root remainder of the absolutely continuous part has the same `L^2` norm after the lift because `int K(x,dy)=1`. Hence the joint experiment is DQM with score `ell_0(X)`. Apply the deterministic statistic `(X,Y)->Y`. The coarse law `P_theta K` is DQM with score

\[
\bar\ell_0(Y)=\mathbb E_{J_0}[\ell_0(X)\mid Y].
\]

The projected singular measure need not remain singular, but its total mass retains the required `o(||h||^2)` order; Pollard's statistic theorem accounts for any part that becomes absolutely continuous. This point is load-bearing and is correctly stated at `06_general_coarsegraining.tex:208-220`.

The Fisher matrices obey

\[
\boxed{
I_X-I_Y
=\mathbb E\!\left[\operatorname{Cov}(\ell_0(X)\mid Y)\right]
=\mathbb E[(\ell_0-\bar\ell_0)(\ell_0-\bar\ell_0)^T]
\succeq0.}
\]

Matrix equality holds if and only if `ell_0(X)=bar ell_0(Y)` almost surely. In a single direction `v`, equality holds exactly when `v^T ell_0(X)` is `Y`-measurable. This is local score sufficiency, not recovery of the entire experiment. The manuscript's finite witness is

\[
P_\theta(A=1)=\tfrac12+\tfrac\theta4,
\qquad
P_\theta(B=1)=\tfrac12+\tfrac{\theta^2}{4},
\]

with independent `A,B` and a channel retaining only `A`. At `theta=0`, the `B` score is zero, so Fisher equality holds, yet the conditional law of `B` changes with `theta`; no parameter-independent reverse kernel recovers the family (`06_general_coarsegraining.tex:243-253`). Pollard's paper likewise emphasizes that Fisher preservation does not imply global sufficiency.

### 5.2 The singular-mass threshold is sharp

Let `R` be a probability law singular to `P_0`. For sufficiently small \(|t|\), the two-sided path

\[
P_t=(1-t^4)P_0+t^4R
\]

is DQM with score zero: its singular mass is `t^4=o(t^2)` and

\[
\sqrt{1-t^4}-1=O(t^4)=o(|t|).
\]

Thus nonzero singular components are genuinely admitted by the general theorem. For the same sufficiently small \(|t|\), in contrast,

\[
\widetilde P_t=(1-t^2)P_0+t^2R
\]

has the same zero first-order square-root derivative in the dominated part, but its singular mass satisfies `t^2/t^2=1`, not `o(1)`, so it is not DQM in the stated Le Cam sense. This exact pair shows that changing `o(t^2)` to `O(t^2)` would invalidate the theorem's DQM premise.

### 5.3 The later score chart is the dominated subcase

The one-parameter definition at `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex:528-557` (`def:rg-dqm-score`, `eq:rg-dqm-definition`) assumes `mu_t << mu`; it is therefore the special case with zero singular part, not a conflicting redefinition of the general theorem. It proves centering rather than silently assuming it.

Conversely, every `h in L^2_0(mu)` has the two-sided dominated realization

\[
p_t=\frac{(1+th/2)^2}{1+t^2\|h\|_2^2/4},
\qquad \mu_t=p_t\mu.
\]

Normalization is immediate from `mu(h)=0`. Although `sqrt(p_t)` contains an absolute value, the sign-flip set lies in `{|h|>2/|t|}` and

\[
\frac1{t^2}\int
\bigl(|1+th/2|-(1+th/2)\bigr)^2d\mu
\leq\int h^2\mathbf1_{\{|h|>2/|t|\}}d\mu\longrightarrow0.
\]

The denominator contributes only `O(t^2)`. This proves two-sided DQM with score `h` and requires no exponential moments (`07b_agent_network_rg.tex:559-599`, `lem:rg-dqm-realization`). It also explains why the `L^2` Fisher completion is larger than the bounded nonlinear action chart.

For `b` independent copies the score is the sum

\[
(\mathscr I_bh)(x_1,\ldots,x_b)=\sum_{i=1}^bh(x_i),
\qquad
\|\mathscr I_bh\|_2^2=b\|h\|_2^2.
\]

After an actual fixed block channel `C_b`, the pushed score and exact budget are

\[
\mathscr L_bh
=\mathbb E\left[\sum_{i=1}^bh(X_i)\mid Z\right],
\]

\[
b\|h\|_2^2-\|\mathscr L_bh\|_2^2
=\mathbb E\operatorname{Var}\left(\sum_{i=1}^bh(X_i)\mid Z\right)\geq0,
\]

with equality exactly when the replicated score is a measurable function of `Z`. These statements and the bounded-to-general approximation proof are at `07b_agent_network_rg.tex:601-749` (`prop:rg-score-block-lift`, `thm:rg-score-pushforward-defect`).

**Falsification condition P15-05.** Parameter independence is indispensable. Let the fine law be constant on a one-point space, so its Fisher information is zero, but let `K_theta` output `Bernoulli(1/2+theta/4)`. At zero the output score is `+1/2` or `-1/2` and its Fisher information is `1/4`; contraction fails. This does not touch the theorem because the channel reads the parameter. An admitted fixed normalized channel producing such a gain, or an admitted singular component of order not `o(||h||^2)`, would refute the claim.

## 6. Common-channel coarse VFE

Let `P(do,dy)` be normalized on standard-Borel spaces, fix a regular `o`, let `Pi_o(dy)` be its posterior, and take `Q_o << Pi_o`. A normalized channel `C:Y->Z` must be the same for the generative posterior and recognition law, must not read `Q_o`, and must not alter the observation coordinate. Define

\[
P^c(do,dz)=\int C(y,dz)P(do,dy),
\quad \Pi_o^c=\Pi_oC,
\quad Q_o^c=Q_oC,
\]

and the bridge laws

\[
\widehat Q_o(dy,dz)=Q_o(dy)C(y,dz),
\qquad
\widehat\Pi_o(dy,dz)=\Pi_o(dy)C(y,dz).
\]

Because both bridge laws attach the same conditional kernel, their RN ratio is `dQ_o/dPi_o(y)` and

\[
\mathrm{KL}(Q_o\Vert\Pi_o)
=\mathrm{KL}(\widehat Q_o\Vert\widehat\Pi_o).
\]

Disintegrating both bridge laws over `z` gives the extended relative-entropy chain rule

\[
\mathrm{KL}(Q_o\Vert\Pi_o)
=\mathrm{KL}(Q_o^c\Vert\Pi_o^c)
+\int\mathrm{KL}\!\left(
\widehat Q_o(dy\mid z)\Vert
\widehat\Pi_o(dy\mid z)
\right)Q_o^c(dz).
\]

Since `C(y,Z)=1` and leaves `o` untouched, the observation evidence is identical at both scales. Substitution into `F=-log z+KL` yields

\[
\boxed{
\mathcal F_P(Q_o)
=\mathcal F_{P^c}(Q_o^c)
+\int\mathrm{KL}\!\left(
\widehat Q_o(dy\mid z)\Vert
\widehat\Pi_o(dy\mid z)
\right)Q_o^c(dz).}
\]

This reconstructs `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex:16-66` (`thm:rg-exact-coarse-vfe`, `eq:rg-vfe-chain-rule`). The coarse ELBO is higher only because a conditional inference gap was discarded; evidence did not improve.

If the fine KL is finite, all terms are finite and the ordinary real difference is the conditional KL. In that finite regime, fine and coarse VFEs are equal if and only if

\[
\widehat Q_o(dy\mid z)=\widehat\Pi_o(dy\mid z)
\quad Q_o^c\text{-almost everywhere}.
\]

Equivalently, `dQ_o/dPi_o(Y)` has a `Z`-measurable version under the bridge. Without finite fine KL, the extended equality \(+\infty=+\infty\) is not a tightness criterion and ordinary subtraction is not defined.

**Falsification condition P15-06.** Using two different channels destroys the identity. On `{0,1}`, take `Q=Pi` uniform, push `Q` through the identity but `Pi` through a constant-zero channel. Fine KL is zero while the mismatched coarse KL is infinite. Altering the observation can likewise change evidence. These cases are explicitly excluded at `07b_agent_network_rg.tex:68-73`; an example satisfying the common fixed latent-channel and unchanged-observation premises but violating the displayed chain rule would refute the theorem.

## 7. Collective and block-local ELBOs

### 7.1 The normalized finite interaction model

For a finite agent set `V`, a finite factor set `A`, a normalized baseline kernel `P_0(dy|X)`, and normalized record kernels

\[
K_a(X,y_{\partial a},do_a)
=\ell_a(o_a\mid X,y_{\partial a})\nu_a(do_a),
\]

the joint law is

\[
P_\theta(dy,do\mid X)
=P_0(dy\mid X)\prod_{a\in\mathcal A}K_a(X,y_{\partial a},do_a).
\]

Integrating the conditionally independent child records removes one normalized kernel at a time and leaves `P_0`; overlap or cycles among factor scopes do not affect normalization. The required common dominators, finite jointly measurable density versions, and prohibition on kernels reading a recognition law or posterior are stated at `manuscripts/gauge_vfe_rg/05b_local_collective_elbo.tex:18-61` (`hyp:local-interaction-kernels`); normalization is proved at lines 75-95 (`prop:obs-interaction-normalization`).

At a fixed regular record,

\[
L_o(y)=\prod_a\ell_a(o_a\mid y_{\partial a}),
\qquad H_o(y)=-\log L_o(y)=\sum_aE_{a,o}(y_{\partial a}),
\]

where `E_{a,o}=-log ell_a` and zero likelihood gives \(+\infty\). With

\[
0<Z(o)=\int L_o\,dP_0<\infty,
\qquad \Pi_o=Z(o)^{-1}L_oP_0,
\]

the one collective extended VFE is

\[
\mathcal F_o^{\rm ext}(Q)
=-\log Z(o)+\mathrm{KL}(Q\Vert\Pi_o),
\]

for every probability `Q`, with equality in the ELBO exactly at `Q=Pi_o`. This is `05b_local_collective_elbo.tex:106-181` (`eq:obs-complete-record-likelihood`, `thm:obs-collective-vfe`). The energy form `KL(Q||P_0)+E_Q H_o` is only a derived representation when it contains no indeterminate difference.

### 7.2 Exact block conditional

For nonempty `B subset V`, write `b=y_{B^c}` and split the selected likelihood into factors incident to `B` and factors missing `B`:

\[
g_{B,o}(y_B;b)=\prod_{a:\partial a\cap B\ne\varnothing}
\ell_a(o_a\mid y_{\partial a}),
\]

\[
L_{\bar B,o}(b)=\prod_{a:\partial a\cap B=\varnothing}
\ell_a(o_a\mid b_{\partial a}),
\qquad L_o(y_B,b)=g_{B,o}(y_B;b)L_{\bar B,o}(b).
\]

Fix a regular conditional `P_{0,B}(dy_B|b)` and define

\[
Z_B(b)=\int g_{B,o}(y_B;b)P_{0,B}(dy_B\mid b),
\]

while defining the full outside likelihood directly as

\[
w_B(b)=\int L_o(y_B,b)P_{0,B}(dy_B\mid b).
\]

The direct definition avoids writing \(0\cdot\infty\). Tonelli gives

\[
Z(o)=\int w_B(b)P_{0,B^c}(db),
\qquad
\Pi_{o,B^c}(db)=Z(o)^{-1}w_B(b)P_{0,B^c}(db).
\]

On the set where \(0<w_B,L_{\bar B,o},Z_B<\infty\) and \(w_B=L_{\bar B,o}Z_B\), which is `Pi_{o,B^c}`-full, the conditional posterior is

\[
\Pi_{o,B}(dy_B\mid b)
=Z_B(b)^{-1}g_{B,o}(y_B;b)P_{0,B}(dy_B\mid b).
\]

All pointwise statements are relative to the declared conditional version; outside-null points are not invariants of the joint law. These claims and the full-measure proof are at `05b_local_collective_elbo.tex:192-292` (`eq:obs-block-incident-likelihood` through `eq:obs-posterior-block-disintegration`).

For every conditional probability `r_B(.|b)`, the local functional is exactly

\[
\boxed{
\mathcal F_{B,o}^{\rm ext}(r_B;b)
=-\log Z_B(b)
+\mathrm{KL}(r_B(\cdot\mid b)\Vert\Pi_{o,B}(\cdot\mid b)).}
\]

It is minimized exactly at the conditional posterior. Now let `Q=Q_{B^c}r_B` and `Q'=Q_{B^c}r'_B` share their outside marginal, assume `Q_{B^c} << Pi_{o,B^c}`, and assume both posterior KLs are finite. The KL chain rule gives

\[
\mathrm{KL}(Q\Vert\Pi_o)
=\mathrm{KL}(Q_{B^c}\Vert\Pi_{o,B^c})
+\mathbb E_{Q_{B^c}}
\mathrm{KL}(r_B\Vert\Pi_{o,B}).
\]

Subtracting the two finite identities cancels the outside KL and `-log Z(o)`. Inside the conditional difference, `-log Z_B(b)` also cancels, yielding

\[
\boxed{
\mathcal F_o^{\rm ext}(Q')-\mathcal F_o^{\rm ext}(Q)
=\mathbb E_{Q_{B^c}}
[\mathcal F_{B,o}^{\rm ext}(r'_B;Y_{B^c})
-\mathcal F_{B,o}^{\rm ext}(r_B;Y_{B^c})].}
\]

This is `05b_local_collective_elbo.tex:294-369` (`thm:obs-local-multiagent-elbo`, `thm:obs-local-global-potential`). If `r'_B=Pi_{o,B}` almost surely, the global change is

\[
-\mathbb E_{Q_{B^c}}\mathrm{KL}(r_B\Vert\Pi_{o,B})\leq0,
\]

with equality exactly when the old conditional was already posterior-almost surely. The same identity does not license independently replacing all correlated conditionals in parallel, because the replacements need not be compatible with one joint law.

### 7.3 Why local conditional VFEs are not additive agent costs

When `P_0=prod_i rho_i`, the correct global ledger is

\[
\mathcal F_o(Q)
=\operatorname{TC}(Q)
+\sum_i\mathrm{KL}(Q_i\Vert\rho_i)
+\mathbb E_Q\sum_aE_{a,o},
\]

under the stated finite energy representation. Each factor occurs once and correlations contribute `TC(Q)=KL(Q||prod_i Q_i)`. In contrast, singleton conditional energies obey

\[
\sum_iH_{\{i\},o}(y_i;y_{-i})
=\sum_a|\partial a|E_{a,o}(y_{\partial a}).
\]

Thus summing the local conditionals overcounts every shared factor. A normalized two-agent witness makes this literal: take one binary record factor with scope `{1,2}` and `K(1|y)=e^{-1}`, `K(0|y)=1-e^{-1}`. At record `1`, the global energy is `1`, while each singleton incident energy is `1`, so their sum is `2`. No limiting or integrability issue is involved. The exact ledger and count are at `05b_local_collective_elbo.tex:423-485` (`eq:obs-global-ledger`, `eq:obs-singleton-incident-counting`).

**Falsification condition P15-07.** A finite normalized factor model whose local-global difference identity fails for two finite-KL laws sharing the same outside marginal would refute the coordinate-potential theorem. Conversely, any claim that the specific singleton conditional VFEs sum to the collective objective is already refuted by the binary two-agent witness. Additive counting-number schemes are possible but are different constructions.

## 8. Attention-label ELBO

For each receiver `i`, augment the baseline by an independent finite source label `J_i` with strictly positive prior `pi_ij`. At the complete selected record require the label-exclusive likelihood

\[
L_o^{\rm aug}(y,j)
=L_o^Y(y)\prod_i\left[
c_i(o_i,y)\exp[-D_{ij_i}(y)/\tau_i]
\right],
\qquad \tau_i>0,
\]

where no other factor reads `J_i`, every `D_ij` is finite and measurable, and the full observation kernel is normalized as model data. These hypotheses are at `manuscripts/gauge_vfe_rg/05b_local_collective_elbo.tex:487-531` (`eq:obs-attention-augmented-baseline` through `eq:obs-attention-augmented-likelihood`). Bayes' formula cancels all terms independent of `j_i` and gives the conditional posterior row

\[
\boxed{
\beta^P_{ij}(y)
=\frac{\pi_{ij}e^{-D_{ij}(y)/\tau_i}}
{\sum_k\pi_{ik}e^{-D_{ik}(y)/\tau_i}}.}
\]

Now impose the additional recognition restriction

\[
Q(dy,dj)=Q_Y(dy)\prod_i\beta_i^Q(dj_i),
\]

so rows are mutually independent and constant in `y`, and assume the displayed energy/log terms are integrable (`05b_local_collective_elbo.tex:533-545`). The exact row contribution to the collective VFE is

\[
-\mathbb E_{Q_Y}\log c_i(o_i,Y)
+\mathcal F_i^{\rm att}(\beta_i^Q),
\]

where the first term is independent of the recognition row and

\[
\boxed{
\mathcal F_i^{\rm att}(\beta_i^Q)
=\mathrm{KL}(\beta_i^Q\Vert\pi_i)
+\frac1{\tau_i}\sum_j\beta_{ij}^Q\mathbb E_{Q_Y}D_{ij}.}
\]

Strict convexity of categorical KL on a positive-prior simplex, or direct Lagrange multiplication, gives the unique interior minimizer

\[
\boxed{
\beta_{ij}^{Q\star}
=\frac{\pi_{ij}\exp[-\mathbb E_{Q_Y}D_{ij}/\tau_i]}
{\sum_k\pi_{ik}\exp[-\mathbb E_{Q_Y}D_{ik}/\tau_i]}.}
\]

This reconstructs `05b_local_collective_elbo.tex:547-600` (`prop:obs-attention-elbo`, `eq:obs-attention-posterior`, `eq:obs-attention-vfe`, `eq:obs-attention-recognition-optimum`). The posterior row and constant recognition optimum solve different problems. A finite witness is `pi=(1/2,1/2)`, `tau=1`, `D_2=0`, and `D_1=0` or `2` with equal `Q_Y` probability. Then

\[
\mathbb E\beta^P_1(Y)
=\tfrac12\left(\tfrac12+\frac1{1+e^2}\right)
\approx0.30960,
\qquad
\beta^{Q\star}_1=\frac1{1+e}\approx0.26894.
\]

Thus softmax of an expectation is not expectation of the pointwise softmax. If all differences `D_ij(Y)-D_ik(Y)` are almost surely constant, the pointwise row itself is constant and the two formulas coincide; this is a sufficient equality condition, not a claim that accidental equality cannot otherwise occur (`05b_local_collective_elbo.tex:602-608`).

For a general conditional label law `Q_{J|Y}`, the exact label ledger contains

\[
\mathbb E_{Q_Y}\operatorname{TC}(Q_{J\mid Y})
+\sum_i\mathbb E_{Q_Y}\left[
\mathrm{KL}(Q_{J_i\mid Y}\Vert\pi_i)
+\tau_i^{-1}\mathbb E_{Q_{J_i\mid Y}}D_{iJ_i}(Y)
\right]
\]

in addition to the `-E log c_i` terms. The chain rule

\[
\mathrm{KL}(Q_{J\mid Y}\Vert\textstyle\prod_i\pi_i)
=\operatorname{TC}(Q_{J\mid Y})
+\sum_i\mathrm{KL}(Q_{J_i\mid Y}\Vert\pi_i)
\]

proves it. For a sharp finite counterexample, take two fair label rows with zero energies and let `J_1=J_2` almost surely, independently of `Y`. Both row marginals equal their uniform priors, so both row KLs vanish, but the conditional total correlation is `log 2`. A naive sum of row objectives misses this positive term. This is the boundary stated at `05b_local_collective_elbo.tex:610-639` (`eq:obs-attention-correlated-ledger`).

Multiplying the row functional by `tau_i` preserves its minimizer but does not create an independently temperature-weighted sector of the same standard global ELBO unless the entire objective is rescaled or a different generalized objective is declared (`05b_local_collective_elbo.tex:641-646`).

**Falsification condition P15-08.** Add a second binary record that reads `J_i`, with selected-success probabilities `1/4` and `3/4` for two labels, while taking equal label priors and zero `D` energies. Its normalized kernel makes the exact posterior row `(1/4,3/4)`, whereas the displayed exclusive-label softmax would be uniform. Permit a correlated recognition label law; the `log 2` witness shows the row sum is incomplete. Both cases violate explicit premises. An admitted exclusive, fully factorized finite model whose Bayes or Gibbs calculation differs from the boxed formulas would refute the claim.

## 9. Observation as interaction: exact equivalence and exact non-equivalence

For a normalized kernel `K(do|y)` with standard-Borel target, the kernel randomization theorem supplies a measurable `F` and an independent `U~Uniform[0,1]` such that

\[
O=F(Y,U),
\qquad
\Pr(F(y,U)\in A)=K(A\mid y)
\]

for every `y`. Conversely, an environment state with normalized law `rho(du)` and message policy `M(y,u,A)` induces

\[
K(A\mid y)=\int M(y,u,A)\rho(du),
\]

which is measurable, countably additive, and normalized. This directly reconstructs `manuscripts/gauge_vfe_rg/05b_local_collective_elbo.tex:716-739` (`def:obs-operational-environment-node`, `thm:obs-agent-interaction-equivalence`, `eq:obs-randomization`). The cited monograph is Olav Kallenberg's [*Foundations of Modern Probability*, third edition](https://link.springer.com/book/10.1007/978-3-030-61871-1); the publisher identifies the relevant chapter as ["Kernels, Disintegration, and Invariance"](https://link.springer.com/chapter/10.1007/978-3-030-61871-1_4). The manuscript's standard-Borel target is within the randomization theorem's domain.

This representation preserves the random variable `O` and hence preserves the conditioning sigma-algebra `sigma(O)`. It is not an equivalence between conditioning on `O` and deleting `O`. In particular,

\[
I(Y;O)=\int\mathrm{KL}(P(dY\mid o)\Vert P^Y)P^O(do).
\]

If only a statistic `S=T(O)` is retained, the deterministic chain rule gives

\[
I(Y;O)=I(Y;S)+I(Y;O\mid S).
\]

The statistic preserves the posterior information exactly when `I(Y;O|S)=0`, equivalently `Y` and `O` are conditionally independent given `S` up to the usual almost-sure versions. Deletion makes `S` constant, so it is lossless exactly when `I(Y;O)=0`. For `Y~Bernoulli(1/2)` and `O=Y`, conditioning gives `P(Y|O=o)=delta_o` and `I(Y;O)=log 2`, whereas deletion returns the nondegenerate prior. This is the exact boundary at `05b_local_collective_elbo.tex:741-769` (`eq:obs-conditioning-information`, `eq:obs-conditioning-statistic-chain`).

The theorem also does not promote a random seed or boundary node to biological or autonomous agency; persistent state, action, a Markov blanket, or a local VFE would be additional hypotheses (`05b_local_collective_elbo.tex:771-783`).

**Falsification condition P15-09.** A normalized kernel on the admitted standard-Borel target with no measurable uniform randomization would refute the operational representation. A claimed deletion equivalence is already refuted by `O=Y`. The manuscript claims the first and explicitly rejects the second.

## 10. Hoeffding extraction: probability typing only

At scale `ell`, let `V_ell` be finite, let

\[
\mathsf X_\ell=\prod_{i\in V_\ell}\mathsf X_{\ell i},
\qquad
\nu_\ell=\bigotimes_{i\in V_\ell}\nu_{\ell i},
\qquad
\pi_\ell\sim\nu_\ell,
\]

where each `nu_{ell i}` is a probability law and `~` is mutual absolute continuity. Mutual absolute continuity, not bounded density ratios, makes \(L^\infty(\pi_\ell)\) and \(L^\infty(\nu_\ell)\) the same equivalence classes with the same essential-supremum norm. Product structure of `nu_ell` then makes coordinate integration representative independent. These are exactly the premises at `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex:1130-1152` (`eq:rg-interaction-product-reference`).

If `V_ell` is empty, the product is a one-point probability space, the action quotient and interaction space are both zero, and assembly/extraction are the unique zero maps. Thus the construction covers every finite cardinality, including zero, without a hidden lower bound.

For `A subseteq V_ell`, define the product-complement expectation `C_A` and Mobius projector

\[
C_Af(x_A)=\int f(x_A,y_{A^c})\nu_{A^c}(dy_{A^c}),
\qquad
P_A=\sum_{B\subseteq A}(-1)^{|A|-|B|}C_B.
\]

The product expectations commute and satisfy \(C_AC_B=C_{A\cap B}\). Finite Boolean-lattice inversion therefore gives

\[
P_AP_B=\mathbf1_{A=B}P_A,
\qquad
\sum_{A\subseteq V_\ell}P_A=I.
\]

With all nonempty subsets retained, define

\[
\mathcal G_\ell=\bigoplus_{\varnothing\ne A\subseteq V_\ell}^{\ell^1}
P_A L^\infty(\nu_\ell),
\quad
E_\ell g=\left[\sum_{A\ne\varnothing}g_A\right],
\quad
\mathsf H_\ell[f]=(P_Af)_{A\ne\varnothing}.
\]

Then

\[
\mathsf H_\ell E_\ell=I,
\qquad E_\ell\mathsf H_\ell=I
\quad\text{on }L^\infty(\nu_\ell)/\mathbb R1,
\]

and the finite bounds are `||E_ell||<=1` and `||H_ell||<=3^{|V_ell|}-1`. This is direct Mobius inversion, not a probabilistic independence claim about `pi_ell`; see `07b_agent_network_rg.tex:1182-1255` (`eq:rg-coordinate-expectation`, `eq:rg-hoeffding-mobius-projectors`, `thm:rg-hoeffding-action-isomorphism`).

The target premise

\[
\pi_{\ell+1}=\pi_\ell K_\ell\sim\nu_{\ell+1}
\]

must be supplied separately. It does not follow from product equivalence at the source. The exact counterexample is the diagonal-cloning channel from a fair bit to two bits, `x -> (x,x)`. Its output is supported on `{(0,0),(1,1)}`. Any product law charging both diagonal atoms must charge both values in both marginals, and hence must also charge the off-diagonal atoms. Therefore no product probability is equivalent to the output. The target Hoeffding chart is unavailable even though the law-level pushforward remains perfectly valid (`07b_agent_network_rg.tex:1160-1180`, `prop:rg-product-equivalence-not-preserved`).

Only when product equivalence holds at both scales is the exact finite-network interaction coordinate map typed as

\[
T_\ell^{\mathcal G}
=\mathsf H_{\ell+1}\,\overline Q_\ell\,E_\ell.
\]

It includes every nonempty hyperedge, retains the evidence mass separately, and does not assert closure of a pairwise or other sparse truncation. Its derivative at `g` uses the tilted operator `U_ell^{phi_g}`, not the untilted `U_ell` except at `g=0` (`07b_agent_network_rg.tex:1364-1413`, `eq:rg-exact-nonlinear-interaction-map`, `eq:rg-nonlinear-interaction-derivative`).

**Falsification condition P15-10.** An admitted product reference and bounded action for which finite Mobius inversion fails would refute the extraction theorem. The diagonal channel instead falsifies only the unstated idea that an arbitrary coarse image automatically admits a target product-equivalent reference. Thus the probability typing is exact and the scale-to-scale existence boundary is real.

## 11. Equality conditions collected

| Claim | Exact equality or tightness condition | Qualification |
|---|---|---|
| Extended or classical ELBO bound | `Q=Pi_o` as probability measures. | Regular positive-finite evidence; the classical formula also needs absolute continuity and log-integrability. |
| Coarse versus fine VFE | Fine and coarse bridge reverse conditionals agree `Q^c`-almost surely; equivalently the pair likelihood ratio is `Z`-measurable. | Stated as an ordinary equality condition only when the fine KL is finite. |
| Local block ELBO | `r_B(.|b)=Pi_{o,B}(.|b)`. | On the posterior-full block-regular set and relative to the declared conditional version. |
| Exact posterior block update | The collective VFE change is zero iff the old conditional is already the posterior `Q_{B^c}`-almost surely. | Same outside marginal and finite global posterior KLs. |
| Nonlinear action Hessian in direction `h` | `h` is conditionally constant on almost every tilted reverse fiber. | Bounded action chart. |
| `L^2` and Fisher contraction | Fine score/direction is a measurable function of the retained variable. | Fixed normalized parameter-independent channel; pointwise-in-parameter only. |
| Attention constant-row optimum | Unique Gibbs row based on expected energies. | Positive prior, finite expected energies, full constant-row factorization. Equality with the average posterior row is guaranteed when all energy differences are almost surely constant. |
| Observation statistic | `I(Y;O|S)=0`. | Standard-Borel regular conditional setting; deletion is the special case of constant `S`. |
| Hoeffding reconstruction | Assembly and extraction are exact inverses modulo constants. | Finite product probability reference equivalent to the normalized law, with every nonempty subset included. |

## 12. Boundary and counterexample register

| Removed or changed premise | Exact witness | What fails |
|---|---|---|
| Pointwise posterior asserted at every observation without declared versions | Change a joint density on the null slice `{0} x R`. | Posterior and ELBO values at that exceptional observation are not measure-determined. |
| `Q << Pi_o` removed | Subspace-supported `Q` versus a Lebesgue-dominated posterior. | KL is \(+\infty\); the finite classical split is unavailable. |
| Log-integrability removed | Cauchy recognition law versus Gaussian posterior. | Separate expected log terms diverge although the extended ELBO exists. |
| Reference not pushed with evidence measure | Compare `mK` to an unrelated reference. | The declared RN action and conditional-partition formula have the wrong type. |
| Bounded action chart enlarged to all `L^2` scores | Gaussian `He_3`. | The exponential normalizer diverges for every nonzero two-sided parameter. |
| Parameter-independent channel replaced by `K_theta` | Constant fine experiment; output `Bernoulli(1/2+theta/4)`. | Coarse Fisher `1/4` exceeds fine Fisher `0`. |
| DQM singular mass relaxed from `o(t^2)` to `O(t^2)` | \((1-t^2)P_0+t^2R^\perp\). | The Le Cam DQM singular condition fails. |
| Common coarse channel removed | Fine `Q=Pi` but identity versus constant coarse channels. | Fine KL is zero while mismatched coarse KL is infinite. |
| Same outside marginal removed from local comparison | Change `Q_{B^c}` as well as the block conditional. | The outside KL no longer cancels; local change is not the whole global change. |
| Local conditional VFEs summed as agent costs | One two-agent factor with selected success energy `1`. | The factor is counted twice rather than once. |
| Label exclusivity removed | Add a `J_i`-dependent factor `r_{ij}(y)`. | The posterior row contains the missing factor and is not the displayed softmax. |
| Recognition label factorization removed | Two perfectly correlated fair rows with zero energies. | A missing conditional-total-correlation term equals `log 2`. |
| Observation presentation confused with deletion | Fair bit `Y` and deterministic record `O=Y`. | Deletion loses `log 2` of mutual information and changes the posterior. |
| Product equivalence assumed to propagate automatically | Diagonal cloning `x -> (x,x)`. | No product probability is equivalent to the coarse law, so target Hoeffding coordinates are untyped. |

Every witness is finite or one-dimensional and attacks a specific missing premise; none requires a limiting network, a numerical approximation, or an appeal to physical interpretation.

## 13. Final adjudication

The finite probability layer closes as a coherent hierarchy:

\[
\text{normalized kernels}
\longrightarrow
\text{regular conditional laws and extended ELBO}
\longrightarrow
\text{measure-pair pushforward and RN action}
\longrightarrow
\text{bounded conditional log-Laplace calculus}
\longrightarrow
\text{conditional-expectation/DQM/Fisher contraction}.
\]

The collective and block ELBOs are instances of the same extended KL gap; the common-channel coarse VFE is its relative-entropy chain rule; attention is a finite latent-label specialization; and observation-as-interaction is a kernel realization that retains the conditioning record. Hoeffding coordinates are an exact finite product-reference chart layered on top of the law-level theory, not a property automatically preserved by every channel.

Accordingly, the scoped Task 15 result is **PASS: no load-bearing probability/operator/ELBO defect found at the frozen revision**. The exact boundary is not optional prose: each item in Section 12 has a counterexample. Any downstream theorem that omits those premises, treats local potentials as an additive ledger, deletes the observation sigma-algebra, turns a parameter-dependent procedure into a Markov contraction, or assumes product equivalence after arbitrary blocking would exceed what this reconstruction proves.
