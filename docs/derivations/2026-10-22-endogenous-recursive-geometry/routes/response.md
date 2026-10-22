<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e","schema_version":"rigorous-theory-search/v1","target_digest":"cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e"} -->
# Response closure, composition, and a finite-history obstruction

The exact new results are a sharp finite-history identification theorem for reused-child responses and a conditional construction of the smallest response-and-update quotient compatible with arbitrary admitted joins. Neither result constructs endogenous recursive formation. The closure construction is a criterion with an explicit measurability obligation; its retained state is not called compressed without a noninjectivity witness. The finite-history theorem does not apply to a protocol that always draws a fresh child.

## Target and source continuity

The frozen target is existential: there must exist at least four agents, normalized constitutive data in the original smooth two-sector KL/Fisher model, and a nonempty initially unpartitioned preparation class, for which the same fine dynamics selects a persistent first organization and then a parent containing at least two first parents. Every preparation and admitted control/record history must preserve exact dynamics in original time, responses, and the specified collective geometry. Actual configuration information must be lost beyond a relabeling, while children remain distinct. No supplied hierarchy, erasure gate, extra attraction, Gaussian closure, or distribution over configurations is introduced here.

The live sources read were `03_dynamics.tex`, `05_inheritance.tex` (deterministic descent, boundary composition, causal memory, partitions), `07_smooth_closure.tex` (conditional mean force, marked spectrum, feedback), `09_public_compression.tex`, `10_boundary_closure.tex`, and `02_geometry.tex` (score projection, moving channels, retained minimizing connection), all under `manuscripts/MAgent_Theory_2.0/chapters/`. The prior records were `docs/research/2026-10-21-public-compression.md` and `2026-10-21-boundary-closure.md`.

Those sources already give the phase reduction and its ordinary-response failure, Gibbs-probe identification, reciprocal incoming-force moments, the supplied-tree response construction, and the measurable/non-DQM character of its discarded phases. The results below do not reclassify those constructions as endogenous. In particular, the associative selective-channel construction in the prior record already provides a restricted response witness; it supplies neither the required formation selector nor the general coupled-evaluator closure.

## Exact model used by this route

For a fixed fine configuration, let each agent have laws `q_i` and `s_i` on standard Borel spaces, recognition law `q_i tensor s_i`, and proper reference `R_i(dk,dm)=r_i(dm)G_i(m,dk)`. Its local term is the expectation

\[
 E_{0,i}=\int\log\frac{d(q_i\otimes s_i)}{dR_i}(k,m)q_i(dk)s_i(dm).
\]

The full potential is

\[
 E=\sum_i E_{0,i}+\sum_{ij}\beta_{ij}\int\log\frac{dq_i}{d\nu^q_{ij}}dq_i
 +T_q\sum_i\sum_j\beta_{ij}\log\frac{\beta_{ij}}{\pi^q_{ij}}
 +\text{the corresponding model-sector terms},
 \qquad \nu^q_{ij}=q_j\mathcal K^q_{ij}[\mathbf q].
\]

All displayed Radon–Nikodym derivatives require absolute continuity and finite relative entropy. For derivatives below, positive densities and bounded log densities and log-reference densities on the interval used are sufficient; channel derivatives are assumed to justify differentiation under the integrals. The original Fisher velocity is `dot q_i=-q_i(h_i-E_{q_i}h_i)` with every receiver, sender, and channel derivative included. In particular,

\[
 d\nu^q_{ij}=(dq_j)\mathcal K^q_{ij}+q_jD\mathcal K^q_{ij}(d\mathbf q),
 \qquad d\operatorname{KL}(a\Vert b)=\int\log(a/b)da-\int(a/b)db.
\]

The Gibbs-reduced alternative uses the original positive temperatures and the exact envelope derivative. Nothing in the response theorem needs a modification of this energy or flow. The response constructions below are normalized conditional experiments given a configuration, not probability distributions over configurations.

## A sharp finite-history identification theorem

Let `Y` be standard Borel. Fix `N>=1`. For arbitrary probability laws `mu_1,...,mu_N` on `Y`, choose one hidden child `J` uniformly once and draw `n` conditionally independent samples from that same child's current law. The declared joint law is

\[
 \mathbb P_x(J=j,dy_1\cdots dy_n)=\frac1N\prod_{r=1}^n\mu_j(dy_r),
 \qquad K_n(x,dy_{1:n})=\frac1N\sum_{j=1}^N\mu_j^{\otimes n}(dy_{1:n}).
\]

This is a normalized instantaneous batch response. The fine laws are not reset during the batch. The persistent hidden label creates dependence between records. No density, parameterization, exponential family, or latent configuration preparation is assumed.

**Theorem 1.** If two `N`-child configurations have the same `K_N`, their empirical measures of child laws agree:

\[
 \frac1N\sum_{j=1}^N\delta_{\mu_j}=\frac1N\sum_{j=1}^N\delta_{\mu'_j}.
\]

The horizon `N` cannot be replaced by `N-1` uniformly, even if every child law is a strictly positive Bernoulli law. For positive arbitrary child weights, and at most `N` distinct child laws in each candidate, `K_{2N-1}` determines the weighted empirical law. The horizon `2N-1` is likewise sharp in that class.

**Proof of identification for uniform weights.** Enumerate the finitely many distinct laws in the union of the two collections as `nu_1,...,nu_M`. For every unequal pair choose a measurable event on which their probabilities differ. There are finitely many such events. A linear combination `h` of their indicators can be chosen so that the numbers

\[
 a_l=\int h d\nu_l
\]

are all different: every unwanted equality excludes one proper hyperplane of coefficient vectors, and a finite union of proper hyperplanes does not cover Euclidean space. Rescale and translate `h` into `[0,1]`. Equality of `K_N` implies equality of all its lower-dimensional marginals, and therefore

\[
 p_r:=\sum_{j=1}^N\left(\int h d\mu_j\right)^r
 =\sum_{j=1}^N\left(\int h d\mu'_j\right)^r,
 \qquad r=1,\ldots,N.
\]

Let `e_k` be the elementary symmetric polynomial of degree `k` of these `N` numbers, with `e_0=1`. Differentiating the finite product `prod_j(1+a_j z)` and equating coefficients in its logarithmic derivative gives the recursion

\[
 ke_k=\sum_{r=1}^k(-1)^{r-1}e_{k-r}p_r,\qquad k=1,\ldots,N.
\]

Thus the power sums determine every coefficient of `prod_j(z-a_j)`, including multiplicities. The two multisets of `h`-expectations agree. Since `h` separates every law in the finite union, the multisets of laws agree. This proves the assertion, including repeated identical child laws.

**Sharpness for uniform weights.** Choose `N` distinct numbers `t_1,...,t_N` in `(0,1)` and put `P(z)=prod_j(z-t_j)`. For sufficiently small nonzero `delta`, `P(z)+delta` also has `N` distinct real roots `t'_j` in `(0,1)`: choose disjoint root neighborhoods with opposite endpoint signs for `P`; sufficiently small perturbations preserve those signs and give one root in each interval, accounting for all `N` roots. All coefficients except the constant coefficient agree. The displayed recursion therefore gives equal power sums through degree `N-1` and unequal degree-`N` sums. Under `mu_j=Ber(t_j)`, the probability of any ordered binary batch of length `n` with `r` successes is the uniform average of `t_j^r(1-t_j)^{n-r}`. This polynomial has degree at most `n`. Consequently all batches through length `N-1` agree, whereas the all-success event at length `N` differs. Every law is strictly positive. For `N=1`, the assertion that zero observations do not identify a law is immediate.

**Positive arbitrary weights.** Subtract the weighted empirical measures of two candidates and write the result as `sum_{l=1}^M c_l delta_{nu_l}`, with `M<=2N`. The same separating `h` gives

\[
 \sum_{l=1}^M c_l a_l^r=0,\qquad r=0,\ldots,2N-1.
\]

The equations with `r=0,...,M-1` have Vandermonde determinant `prod_{l<k}(a_k-a_l)`, which is nonzero. Hence every `c_l=0`.

For sharpness let `m=2N-1`, choose `t_j=a+jh` in `(0,1)`, `j=0,...,m`, and use weights proportional to `binom(m,j)` on the even and odd index sets separately. Each set has `N` elements, and each normalizing sum is `2^{m-1}`. The difference of their degree-`r` moments is proportional to

\[
 \sum_{j=0}^m(-1)^j\binom mj(a+jh)^r.
\]

This is zero for `r<m` and nonzero for `r=m`. To verify this, iterating the forward-difference operation lowers the degree of a polynomial by one, and its `m`th application to a monic degree-`m` polynomial is the nonzero constant `m!h^m`. The same Bernoulli batch calculation proves agreement through `2N-2` observations and disagreement at `2N-1`. All weights and all Bernoulli probabilities are positive. This completes the proof.

**Two-sector consequence.** Take `Y=K times M` and `mu_i=q_i tensor s_i`. Select one child once; each repetition draws a fresh belief/model pair independently conditional on that child. Theorem 1 identifies the unordered collection of the paired laws `(q_i,s_i)` because each product law determines both marginals. Independent hidden labels for the two sectors do not establish this paired identification.

If a retention preserves this response kernel, equality of retained states forces equality of that unordered collection. On an identical-agent Gibbs-reduced model whose remaining source rows and constitutive data are determined by the law tuple and relabel equivariantly, no additional continuous public-law information can be forgotten. With dynamic source rows, the conclusion identifies the child-law collection, not all routing coordinates. It is not a universal impossibility result for the frozen target.

If instantaneous batches are excluded but arbitrarily small positive waiting intervals and noninvasive repeated sampling are admitted, continuity of the laws under the fine flow yields `K_N` as the zero-wait limit. Equality for all positive intervals then implies its equality. A protocol with compulsory finite waiting, feedback resetting inside the batch, or freshly redrawn child labels requires a separate analysis. In particular, fresh labels give `(N^{-1}sum_i mu_i)^{tensor n}` at a fixed configuration and do not satisfy this identification theorem.

## An exact minimal response-and-update closure

Here is a conditional construction rather than a claim that storing all future behavior is a compressed parent. Let `S` be a standard Borel admitted configuration space. Include a declared protocol register when a response reuses a child or other latent variable; its preparation is part of that protocol. The original deterministic flow is still the flow of the laws themselves. Assume all admitted flow segments remain in a regular domain with unique solutions.

Represent one action by a normalized kernel

\[
 M_a:S\rightsquigarrow O_a\times S.
\]

A flow interval has a singleton outcome and `M_t(x)=delta_{(*,Phi_t x)}`. A record with normalized conditional density `k_a(x,o)` and exact state update `U_a(x,o)` has

\[
 M_a(x,do,dx')=k_a(x,o)\lambda_a(do)\delta_{U_a(x,o)}(dx').
\]

The density form is optional; the kernel formulation covers general standard Borel outcomes. It includes Bayes updates only when the specified recognition family is preserved or enlarged explicitly. In particular, a cross-sector likelihood is not silently projected back to product recognition.

For a measurable outcome event `B` define the substochastic observation operator

\[
 T_a^B f(x)=\int 1_B(o)f(x')M_a(x,do,dx').
\]

Choose countably many actions and countable event generators closed under finite intersections; additional actions can be included by a separately proved continuity extension. Choose a countable family of bounded observables `O` that the parent must retain. Start with their rational unital algebra, repeatedly adjoin `T_a^B f` for every current algebra element, and close under rational sums and products. The resulting countable algebra `A` is the smallest such invariant observable algebra. Enumerate it as `(f_n)` and define

\[
 R(x)=(f_n(x))_{n\ge1}.
\]

Introduce the following realization assumptions: `Z=R(S)` is a standard Borel measurable subspace of the countable product, and `R` has a measurable right inverse. These are not automatic for arbitrary measurable quotients. A verified finite-dimensional closed statistic, or a supplied quotient with an explicit measurable selector, would discharge them.

**Theorem 2.** Under these assumptions there are normalized kernels `M_a^c:Z -> O_a times Z` satisfying

\[
 M_a(x,B\times R^{-1}C)=M_a^c(Rx,B\times C).
\]

They preserve every finite adaptive joint record-and-retained-state history. If another measurable retention `Q` with a measurable selector preserves the same state-transition kernels and the observables `O`, then `R=r circ Q` for a measurable `r`. Thus `R` is the coarsest exact quotient in this specified strong state-update class. The procedure is idempotent on its own descended system with the same protocol and observables.

**Proof.** For every `f in A` and generating event `B`, `T_a^B f` is in `A`, so it is constant on `R` fibers. Therefore the finite measures `M_a(x,B times R^{-1}(dot))` have the same integrals against the coordinate algebra whenever `Rx=Ry`. The elementary functional monotone-class principle extends equality to every bounded function measurable for the coordinate sigma algebra: a vector space containing constants and an algebra, and closed under bounded monotone limits, contains every bounded function measurable for that algebra. Its hypotheses hold because integration against finite measures commutes with bounded monotone limits. The coordinates generate the Borel sigma algebra of `Z`. Extending over the outcome event generator gives equality of the whole pushed joint kernel. Define the coarse kernel by evaluating it at a measurable representative `iota(z)`. It is normalized, measurable, and independent of the representative.

Repeated conditioning with that joint kernel proves equality of the next joint record/state law given each retained history. Induction proves every finite adaptive history, even when the action is selected from all earlier observed records. This argument preserves dependence; it does not replace a joint response by a product of marginals. For a flow action the equality of deterministic kernels is exactly `R Phi_t=Phi_t^c R` in original time.

If `Q` has the stated properties, the observables factor through it. Factorization is preserved by algebra operations and by every `T_a^B`, using the descended joint kernel. Induction gives factorization of every `f_n`, hence of `R`, with measurability supplied by the selector. Applying the procedure again to the descended system recovers those same generated coordinates, so its fibers are singletons. This is idempotence for a fixed system and fixed protocol only. It does not prohibit another quotient when a later join changes the observable interface.

The tuple `(f_n(x))` is an exact construction of a possible sufficient state, not a demonstrated compression. Theorem 1 gives a case where it identifies the entire public child-law collection. No claim of finite dimension, a finite evaluation algorithm, or compression follows from its definition.

## Joining without supplying a tree

For each possible finite block `I`, let `S_I` denote its admitted configuration data, including the boundary information actually required by the same original fine system. Let `J_{I,J}:S_I times S_J -> S_{I union J}` be a declared measurable fine joining map for disjoint blocks. In the intended application this is a representation handoff inside the original population, not adding a new attraction or deleting an old edge.

Suppose these maps are associative on their admitted domains. Construct the smallest family of bounded observable algebras with the following properties: each contains the prescribed block responses and selection observables; each is closed under its exact admitted joint record/update operators; and whenever `f` belongs to the union algebra, the section

\[
 x_I\longmapsto f(J_{I,J}(x_I,x_J))
\]

belongs to the `I` algebra for every admitted partner state `x_J`, and likewise with the blocks exchanged. This family exists as an abstract family of function algebras by taking the intersection of all families with these properties; the family of all bounded measurable functions is one candidate when the joining maps and transitions are measurable. Each operation and each specified section survives intersection.

This construction considers all admitted joins, not a chosen tree. It may be uncountably generated. A standard Borel realization with measurable selectors remains an explicit hypothesis; countable action data alone do not establish countability after all partner sections are added.

**Theorem 3.** If these algebras have quotient realizations `R_I` with measurable selectors, then every fine join descends uniquely:

\[
 R_{I\cup J}J_{I,J}=\bar J_{I,J}(R_I,R_J).
\]

The descended joins inherit associativity and preserve the exact subsequent history laws whenever their admitted transition kernels are the same kernels used in the closure. Commutation of joining with evolution additionally assumes the corresponding fine joining square: the jointly controlled fine network update, pushed through `J`, equals the union update. For a representation handoff within one original system this is a checkable compatibility condition; evolving the two blocks independently would generally fail it. Conversely, a single union observable whose pullback distinguishes two pairs with equal retained children falsifies the existence of such a descended join.

**Proof.** Equality of `R_I` makes every section in the `I` algebra equal. Then equality of `R_J` makes the other section equal. Hence every union observable has the same value on the two joined configurations. Define `bar J` by joining measurable representatives and applying `R_{I union J}`; the previous argument establishes representative independence. Applying this identity twice and using associativity of the fine joins proves associativity after retention. Theorem 2 supplies subsequent history preservation. When the fine joining square holds, composing it with the retained update squares proves the coarse joining square by substitution. The converse is immediate by pulling the purported union observable back through the descended join.

This proves a compositional sufficient-state construction and locates its possible failure. It does not prove nontrivial fibers at either join. The smallest isolated-block response state can be too small for composition: joining can make partner-dependent functions observable that were absent from the isolated protocol. Adding all partner sections repairs exact composition but can remove all compression.

A proposed selector can be included without assuming a tree. For finitely many candidate partitions, add its finite-valued choice, or the indicator of membership in each admissible set-valued choice, to the prescribed observables. Then the selector is determined by the retained state. This is exact retention of an already specified selector, not derivation of one. A genuine formation witness must still derive that selector from current laws/interactions or accessible histories, prove its persistence, and show that adding its observables leaves nontrivial fibers through two stages. Idempotence at a fixed interface does not answer this changed-interface question.

## What fresh-child closure must add under the actual force

The first missing observable can be written explicitly. On a common reference `A`, write `q_i=f_i A`, take identity peer channels and normalized nonself rows, and put

\[
 v_i(k)=-\int\log\rho_i(k,m)s_i(dm),\qquad
 R_i(dk,dm)=\rho_i(k,m)A(dk)B(dm).
\]

For finite positive tables, or bounded positive density charts justifying the integrals, the complete belief derivative up to one additive constant is

\[
 h_i=2\log f_i+v_i-\sum_j\beta_{ij}\log f_j
       -\sum_k\beta_{ki}\frac{f_k}{f_i},
 \qquad c_i=\int f_i h_i dA.
\]

The ratio is the incoming source derivative. With the fresh mixture density `m=N^{-1}sum_i f_i`, exact summation gives

\[
 \dot m=m-\frac1N\sum_i f_i
       \left(2\log f_i+v_i-\sum_j\beta_{ij}\log f_j-c_i\right).
\]

Indeed, the incoming term sums to `N^{-1}sum_k f_k sum_i beta_{ki}=m`. It cannot be omitted before this summation: it also enters every `c_i`. The model-sector formula is exchanged. In the Gibbs-reduced case every `beta` here is its original optimized value; in the dynamic-row case their original Fisher equations must be retained. Law-dependent channels add their complete channel-variation terms and need their own closure proof.

Thus even the first response derivative requires logarithmic cross profiles, evaluator assignments, and normalization profiles. Applying exact flow/update closure determines which further functions are necessary. Merely closing a formal sequence of Lie derivatives is not substituted for exact flow closure in the smooth category: a smooth function can have every time derivative zero at one point without vanishing on an interval. A finite regular statistic satisfying `DR V=bar V circ R`, with a locally unique parent ODE, would be sufficient and would avoid that issue. No such noninjective two-stage statistic has been produced here.

For comparison, a common likelihood reset applied separately to each child gives `f_i^+=L f_i/Z_i`, where `Z_i=int L f_i dA`. The fresh mixture after that specified reset requires `sum_i f_i/Z_i`. Conditioning a hidden-child mixture instead updates the child weights and is a different operation. Any claimed feedback closure must choose and preserve the actual operation and its joint history law.

## Geometric compatibility is a separate obligation

The algebras above are measurable response constructions. They supply neither a smooth statistical bundle nor a parameter-independent sample channel. Fisher data processing cannot be applied to them without that realization. For a smooth equivariant realization `R` with fine and coarse metrics `g,g_c`, put `Delta=g-R^*g_c`. For a fine minimizing residual `r_X=d p(X)+J A^F(X)`, retention of the same minimizing connection representative requires

\[
 \Delta(r_X,J\xi)=0\quad\text{for every }X,\xi.
\]

Equality of the full affine minimizing classes additionally requires `ker J=ker J_c`. If those conditions hold, the residual-tensor defect is exactly `Delta(r_X,r_Y)`. Its vanishing is another requirement if the tensor itself must be retained without loss. These follow directly by comparing the fine and coarse normal equations as in `geo:retained-connection`. They are not consequences of response sufficiency. A law-dependent statistic needs its actual derivative, including statistic motion; a non-DQM discarded phase supplies no smooth Fisher direction.

## Status, falsifiers, and next decisive action

The mechanism fingerprint is: finite exchangeable child-history moments; separating bounded test functions; Newton/Vandermonde recovery; minimal invariant observable algebras; all-partner section closure; explicit fresh-mixture incoming-force profile. This differs from unrestricted Gibbs probing, the known binary observability determinant, the phase parent, and the supplied binary profile tree. No novelty claim relative to the mathematical literature is made.

Theorem 1 is falsified by two different weighted empirical law measures satisfying its stated sample-count and weight conditions but with identical joint batch laws. A purported example can be checked by the separating-function and polynomial argument. Theorem 2 requires a standard Borel quotient and selector; failure to provide them leaves the realization conditional. A union observable that differs for equal retained children falsifies Theorem 3's section-closure hypothesis or a proposed application. None of these theorems closes the frozen existential target negatively.

The minimal remaining constructive obligation is an explicitly normalized original KL/Fisher model and admitted fresh-response/control class whose all-partner closure has nontrivial fibers at two selected joins, together with a state/history-derived persistent membership selector and a smooth geometric realization satisfying the displayed connection conditions. The next action that would materially change the answer is to exhibit such fibers and a closed update for a concrete model, or to prove their absence for a declared candidate class. Calling the canonical quotient a parent, without those fibers, would not advance formation.

Only read-only source inspection and writing this assigned derivation ran. No numerical experiment, simulation, GPU query, Lean work, external theorem invocation, or verification panel was performed. This file is the output artifact; no manuscript was edited.
