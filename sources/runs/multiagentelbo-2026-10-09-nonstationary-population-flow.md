---
type: run
title: "Nonstationary startup admission and population Fisher paths"
aliases: ["N512k2 nonstationary population path limit", "Unconditional fitted startup and native population flow"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-09
updated: 2026-10-09
---

# Nonstationary startup admission and population Fisher paths

Codex (2026). *Nonstationary startup admission and population Fisher paths*. MultiAgentELBO [PR258](https://github.com/cdenn016/MultiAgentELBO/pull/258), source commit 787c1bbb82c6afd752f0bec0268ab04e0a03bfe0 and merge 10316c71e78e736f50435b02870dd4ed1569d54b, publishes three complete records. The original T=0, unit-mobility population Fisher descent from its prescribed baseline has subsequential continuous infinite-network path laws under the declared ideal preparation family. The fitted finite-budget startup separately has unconditional rooted outcome admission, retaining global route and failure states, while its first-step success probability vanishes asymptotically. These results keep native population dynamics separate from the finite-pool/fixed-q9 executable. Infinite-volume uniqueness, useful numerical transfer, growing-depth operational closure and endogenous formation remain open. All four RG completion gates remain open; the roughly 65% planning estimate is unchanged.

```bibtex
@misc{codex2026nonstationarypopulation,
  author = {Codex},
  title = {Nonstationary startup admission and population Fisher paths},
  year = {2026},
  howpublished = {MultiAgentELBO mathematical checkpoint PR258},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/258}
}
```

## Declared family and different initial laws

The family is the ideal-random agent torus V_k=(Z/(16k)Z) times (Z/(32k)Z), N_k=512k^2, at fixed c_*. It retains real GL+(2) matrix links, right/down primitives with shared reversals, four nearest-neighbor source slots, ordered plaquettes, four generator episodes and three observed matter/source episodes. Mass is 16, loop coefficient 1/4, generator anchor precision (100/9)I4, matter prior N((.7,-.4),I2), record precision I2, tau=1 and source prior pi=(1/4,...,1/4). The agent graph does not introduce base-manifold transport.

The existing finite-preparation law supplies 321 Gaussian whole-history candidates per primitive, fixed finite MH uniform inputs, original baseline matter/record noise and source labels. Each selected truth is one of its candidates, with potentially global dependence; selected truths or observations are not replaced by independent rows. Ideal increasing inputs are distinct from the stored finite seeded N512/N1024/N2048 designs. Original joint marks are frozen throughout inference.

The native population start is prescribed directly: matter at its prior mean/covariance, beta=pi, zero generator means and generator covariance .09I4. It is neither the fitted state nor the correlated latent-history prior marginal. Population T=0 means zero recognition thermostat, while original record noise remains tau=1. Unit mobilities, full matter/generator covariances and all incoming sender terms are retained. Finite training/evaluation pools may be carried as diagnostic marks but do not enter this population field.

## Unconditional fitted-startup admission

The [warm-start record](https://github.com/cdenn016/MultiAgentELBO/blob/10316c71e78e736f50435b02870dd4ed1569d54b/docs/research/2026-10-03-latent-link-rg-plan/R5-NONSTATIONARY-WARM-START-ADMISSION.md) instead treats the actual simultaneous expected_hessian startup with sixteen fixed common training draws, nominal .05 steps, target inference time .1, at most 512 accepted steps and seventeen common backtracking candidates per call. Exact-real execution either accepts an SPD descending state or retains the previous accepted state on failure. Its accepted-state sequence is padded by freezing the terminal outcome, without deleting failed volumes.

Its finite-pool objective is a fixed constant plus Gaussian prior KL, categorical KL and nonnegative original record/loop/kinetic costs. The admitted preparation/training Gaussian envelopes give a uniform expected baseline objective per agent M0. Accepted descent and uniform independent rooting bound each rooted owned Gaussian KL, across all padded steps, by this same budget. Gaussian KL sublevels control means, covariance and inverse covariance inside compact interiors.

Categorical KL alone does not control a source probability approaching zero. The original mirror update has beta'_a=beta_a^(1-h) pi_a^h exp(-h c_a/tau)/Z with c_a>=0 and Z<=1. Local record costs across the finite padded path are uniformly tight by the joint Gaussian/data/training compacts, without assuming independence from fitted states. On a cost bound M the original update gives beta_a>=pi_a exp(-.1 M/tau). This supplies rooted uniform interior tightness, not a deterministic fitted floor or inverse-probability moment.

Retaining the whole bounded global route/status/inference-time mark G jointly with original marks and all padded states gives weak spatial subsequences of the unconditional outcome family. The result is annealed over ideal inputs and a single uniform root. It preserves dependence of the selected global step sizes on the entire field; it does not identify a local infinite-volume backtracking selector. Extensive objectives are retained as densities when needed; measured machine timing/memory are outside this mathematical admission.

## Finite-budget startup-success boundary

The [boundary record](https://github.com/cdenn016/MultiAgentELBO/blob/10316c71e78e736f50435b02870dd4ed1569d54b/docs/research/2026-10-03-latent-link-rg-plan/R5-STARTUP-SUCCESS-BOUNDARY.md) concerns this simultaneous arm and ideal increasing family. Its first search tries h_b=(1/20)2^(-b), b=0,...,16. A radius-two event bounds every possible finite-MH truth candidate and each original training matrix, while placing negative original observation noise along the baseline mean. A central matrix direction I2/sqrt2 reconstructs the full record covariance trace and both ordered incident-loop Hessians on the noncommutative domain. The resulting precision direction is negative even at h_min=1/1310720, so all seventeen candidates fail at that patch.

Disjoint underlying input patches pack at least ceil(N_k/41) centers. Their independence belongs to the original Gaussian inputs, not selected truth indices or observations. The constructed fixed probability p>0 gives

$$
\Pr\{\mathrm{first\ startup\ step\ accepted\ at\ }k\}
\leq(1-p)^{\lceil512k^2/41\rceil},
\qquad
\Pr\{\mathrm{complete\ startup\ success}\}\longrightarrow0.
$$

The probability p=qG^5136 qepsilon^256 qz^13 qeta^2 is deliberately unevaluated. Distant noise balls with L=200000000 supply an existence witness, without a useful finite N512 prediction. This is an original large-family algorithm boundary, not a scalar-network obstruction to continuous native dynamics or formation. One previously executed standard-library rational/patch bookkeeping calculation is recorded with its stdout; it is not rerun during intake and is not a scientific trajectory.

Success probabilities are summable along 512k^2, so almost surely sufficiently large volumes fail at their first step under any countable coupling with the specified within-volume laws. The failure-inclusive state/time/status equals the baseline/zero-time/first-step-failure reference except on the first-step-success event. Original marks remain unchanged. This gives the same subsequential joint limits for that accounting outcome, without a unique full-volume mark limit.

A nonvanishing-success hypothesis would transfer unconditional tightness to success conditioning, but it is refuted for this ideal family. Direct successful-conditioned interior tightness is still unproved; vanishing success probability alone does not prove its failure. The actual q9 caller launches only after successful startup. Its failed branch retains the failure endpoint and an absent-path cemetery value. In the ideal limit it is an all-startup-failure cemetery branch, not a successful q9 trajectory.

A separately declared mathematical continuation can start the unchanged exact-real h=1/40000, T=.05 finite-q9 raw map at every admitted endpoint, including failures. Its countable recursion is unique given the joint initial law and original driving array, and local continuous maps give fixed-step finite-prefix weak pushforward limits. That extension changes the failed-start input convention and is not the original failed pipeline behavior. It establishes neither continuous population equivalence nor floating guard-conditioned accuracy.

## Positive original population Fisher path theorem

The [population-flow record](https://github.com/cdenn016/MultiAgentELBO/blob/10316c71e78e736f50435b02870dd4ed1569d54b/docs/research/2026-10-03-latent-link-rg-plan/R5-NONSTATIONARY-POPULATION-FLOW.md) returns directly to the prescribed baseline and exact population energy. Removing only state-independent normalization constants gives E_k>=0 as Gaussian/categorical prior KL plus original nonnegative expected record, ordered-plaquette and kinetic terms. Finite preparation bounds for original observations and exact baseline Gaussian integrals give

$$
\sup_k\frac{\mathbb E E_k(X^0)}{N_k}\leq M_{\mathrm{pop}}<\infty.
$$

The displayed source constant uses B_p=4 exp(.09p^2), the admitted observation second-moment bound, and the original baseline kinetic cost 864/25 per agent. No finite-pool approximation or stationary-prior exponential moment is inserted.

Differentiation under Gaussian integrals on compact interiors gives a C1 coordinate-local collective field with finite incident radius at most two. The original product Fisher equations, in covariance coordinates, are

$$
\dot m_b=-C_b\partial_{m_b}E_k,
\qquad
\dot C_b=-2C_b(\partial_{C_b}E_k)C_b,
\qquad
\dot\beta_a=-\beta_a(v_a-\sum_c\beta_c v_c),
\qquad
v_a=\log(\beta_a/\pi_a)+c_a/\tau.
$$

Finite-dimensional local existence/uniqueness extends globally at each finite volume. The energy identity dE_k/dt=-sum_u a_u confines every Gaussian factor to its prior-KL compact. Original population record costs are bounded there independently of beta, and the exact source ODE gives beta_a(t)>=pi_a exp[-M_k(1-exp(-t))/tau]. Thus a finite-time interior escape is excluded. No Hessian PSD assumption is needed.

Uniform rooting of the energy identity supplies E integral_0^H a_(U_k+u)(t)dt<=Mpop at each fixed cell and finite H. Gaussian covariance and inverse-covariance paths are controlled by ell=sqrt(2 H A_b): exp(-ell)C_b(0)<=C_b(t)<=exp(ell)C_b(0). Mean, covariance, precision and source paths have common one-half-Hölder moduli on bounded action events. Original finite-patch observations are tight; original population costs on those Gaussian/data compacts give the separate source floor. These estimates exhibit interior path compacts uniformly in volume for each finite patch and inference interval.

Finite rational-time coordinate extraction, countable consistency and the exhibited path compacts yield one subsequence over all integer time horizons. Its normalized joint law Q retains the original frozen mark marginal and continuous interior paths in the countable local path topology. Bounded continuous integral-residual tests pass the unchanged local equations to the limit:

$$
X_u(t)=X_u^0+\int_0^t b_u(W,X(s))\,ds
\quad\text{for every cell and all }t\geq0,\quad Q\text{-almost surely}.
$$

The limiting paths are coordinatewise C1 and spatially shift invariant after uniform rooting. Disintegration gives a solution law for almost every limiting mark field. It need not be a point mass. Finite-volume uniqueness does not prove infinite-volume uniqueness, a Markov realization, a deterministic conditional semiflow or convergence of the whole volume sequence.

The inherited nonnegative action allowance is

$$
\mathbb E_Q\int_0^H a_0(t)\,dt\leq M_{\mathrm{pop}}
\quad(H<\infty),
\qquad
\mathbb E_Q\int_0^\infty a_0(t)\,dt\leq M_{\mathrm{pop}}.
$$

Finite total squared local speed gives neither finite total Fisher length nor state convergence, an all-time compact, stationarity or intrinsic formation. The infinite extensive objective is not evaluated; the preserved object is the coordinate-local population field.

Durrett, [*Probability: Theory and Examples*, fifth edition](https://math.duke.edu/~rtd/PTE/PTE5_011119.pdf), Theorems 3.10.3 and 3.2.10 and Appendix A.3 Theorem A.3.1 supply finite-dimensional weak compactness, continuous mapping and countable extension. The source record separately reconstructs native action/containment and the passage to continuous-path topology. A finite-dimensional compactness theorem alone is not asserted as a path-space theorem.

## Provenance and remaining obligations

The [source intake](https://github.com/cdenn016/MultiAgentELBO/blob/10316c71e78e736f50435b02870dd4ed1569d54b/docs/research/2026-10-03-latent-link-rg-plan/evidence/r5-nonstationary-source-intake-20261009.json) binds 26 repository sources, two live manuscript sources and the historical Vault179 theme context. Live c08b recognition flow and g11 expected records/ordered defects preserve the population coordinates and shared-copy formulas. The root researcher reconstructed the complete energy, Hessian, source, compactness and path arguments. This publication claims no formal verification-ledger closure.

Actual canonical Code main, HEAD and origin/main agree at 10316c71e78e736f50435b02870dd4ed1569d54b. Published checkpoint/source bindings match the implementation copy, while unrelated canonical WIP is preserved separately. The completed administrative handoff receipt SHA256 is fb8413190a872840d64c16156e66792d892c298c0047f2a6a0f9e3c6db30fd53. It records published non-WIP parity and preservation; it supplies no additional mathematical claim.

| Published record | SHA256 |
| --- | --- |
| Unconditional warm-start admission | da77ee9f379d045813a90a19be6b43a4e6dc8fade4231deef0965dc2ff04ef83 |
| Finite-budget startup-success boundary | a793b5f013da010ee1225dd5eb27498a8d9aed501c4a222a35abe44704163772 |
| Original nonstationary population flow | 0e8a1843b83f5dd73485d296ef5d61163df7fb4eede0b69eb961bc8a29245637 |
| Source intake | 937ef1d3ddba68043611dce38ad245cd866a58311947d3f886dae0675e723dba |

A fixed finite-depth all-copy readout has a continuous path pushforward only on compatible volumes with its tree/block origin phase retained jointly. This supplies no growing-depth control, reverse conditional-kernel convergence, compression accuracy or autonomous parent dynamics. A canonical infinite deterministic population law still needs uniqueness or a selected realization; quantitative transfer to admitted scientific approximations is separate. The new positive theorem does not identify the finite-pool/fixed-q9/T=.05 law, h-to-zero discretization, a normalized infinite observation posterior or a latent-episode kernel.

The actual-history Gamma2/a2/b2 information obligations in [[multiagentelbo-2026-10-09-second-information]] remain unresolved. [[Staged hierarchy formation and RG composability]] records this nonstationary positive size-limit result and the scoped startup boundary alongside [[multiagentelbo-2026-10-09-actual-information]] and earlier immutable intakes. [[Renormalization-group flow of beliefs]] keeps native population path existence separate from operational retained closure and formation. All four completion gates remain open. No scientific execution, tests, GPU use, model/configuration, host setting or manuscript edit occurred during these constructions or intake; the sole source-record bookkeeping execution remains separately scoped.
