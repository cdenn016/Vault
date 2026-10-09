---
type: run
title: "Native recognition spatial snapshots and exact source quadratic moments"
aliases: ["Recognition snapshot Gibbs limits and source correction"]
authors: ["Codex"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/gauge-theory, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-08
updated: 2026-10-08
---

# Native recognition spatial snapshots and exact source quadratic moments

This record continues [[multiagentelbo-2026-10-08-saved-forecast-local-exit]] and [[multiagentelbo-2026-10-08-product-moment-fisher]]. [Code PR203](https://github.com/cdenn016/MultiAgentELBO/pull/203) publishes two bounded analytical results at commit `137a4a7cd1c3572ce1db3cf7abd4b8d984c2782b`, merged as `e1fce8d39283cbe95ad313570355a2937e2c7d76`. Root reconstructed both proofs and source/receipt hash bindings. The intake retains the live manuscript's product recognition Fisher flow and original record/ordered-loop moments in `c08b_lie_links.tex` and `g11_latent_links.tex`. The scope paragraphs of `b05_infinite_networks.tex`, `b06_wilsonian_limits.tex` and `open:rg-two-index-limits` keep spatial laws, dynamics and asymptotic RG distinct. No formal adjudication state is assigned.

```bibtex
@misc{codex2026recognitionspatialsource,
  author = {Codex},
  title = {Native Recognition Spatial Snapshots and Exact Source Quadratic Moments},
  year = {2026},
  url = {https://github.com/cdenn016/MultiAgentELBO/pull/203},
  note = {Result revision 137a4a7c; conditional rooted Gibbs existence and an exact source-component correction moment}
}
```

## Spatial law of the unchanged recognition snapshot

The [spatial snapshot derivation](https://github.com/cdenn016/MultiAgentELBO/blob/137a4a7cd1c3572ce1db3cf7abd4b8d984c2782b/docs/research/2026-10-03-latent-link-rg-plan/R5-NATIVE-RECOGNITION-SPATIAL-LIMIT.md) concerns the finite native recognition Gibbs law proportional to $e^{-F_{0,N}/T}dm_{*,N}$ at one base point $c_*$. It retains full Gaussian means/covariances, supported categorical rows and the existing nonlinear expected original-record, ordered-loop and temporal actions. Gaussian Fisher volume is used for Gaussian recognition coordinates and ordinary supported-simplex Lebesgue measure for source rows. This is a configuration-time snapshot, distinct from a latent-history law or infinite inference trajectory.

For a Gaussian factor with anchor $a$, precision $J$ and dimension $d$, the exact uncoupled recognition reference has independent $m\sim N_d(a,TJ^{-1})$ and $C\sim\mathrm{Wishart}_d(1/T-1,TJ^{-1})$. The reference source density is proportional to $e^{-D(\beta\Vert\pi)/T}$ on the supported simplex. Normalization requires $0<T<1/d_{\max}$. The reference-mixture generator has a finite exponential radius, even though its covariance is exactly $J^{-1}$; finite covariance alone does not imply every exponential moment. The main existence proof avoids an unrestricted exponential-moment assumption.

The introduced increasing tori have both side lengths tending to infinity, fixed fiber dimension and history/prefix lengths, and fixed finite-range source/loop templates with bounded local counts. Core model marks must lie in a compact admissible carrier: anchor means bounded, Gaussian and original noise precisions uniformly SPD, supported prior probabilities bounded away from zero, and action coefficients bounded. Actual heterogeneous core marks and original observations remain in the finite energy. Strict positivity separately at each size is insufficient to give a uniform source interior bound.

A compact restriction of the uncoupled reference is used only as a trial measure for the partition estimate. It supplies an entropy/action bound proportional to volume without changing the native law. Rooted entropy controls mean/covariance tails, singular covariance and source faces through explicit Gaussian, Wishart and simplex integrals. Tightness and the local conditional-density passage then give subsequential limits of the jointly uniformly rooted mark/state fields. These joint limits are shift invariant; their full covariance and source coordinates remain interior. Conditional on the entire limiting mark field and exterior recognition states, they satisfy the same local recognition Gibbs specification. The mark marginal is the actual uniform-root empirical limit, without Gibbs reweighting.

The observation extension replaces a uniform offset supremum with the deterministic empirical bound $\sup_n N_n^{-1}\sum_{y,t<C}\|o_{t,y}\|^2\leq M_o<\infty$. A compact-trial record bound is quadratic in each original observation and uses source-row normalization, so the entropy/action estimate depends on $M_o$ rather than the largest offset. No independence between observations, cells or marks is assumed. The limit retains $E\|o_0\|^2\leq M_o$ and finite expected nonnegative local actions. This is tightness and lower-semicontinuous moment control; it does not establish uniform integrability or convergence of second-moment expectations.

## Explicit periodic finite-prefix reference and remaining spatial scope

Periodically copying only the admissible N512 R0 core and original observed prefix from its 16 by 32 torus into tori of size $16k$ by $32k$ gives an explicit mathematical reference family. Each new cell still owns separate recognition variables; recognition states, latent realizations and record noise are not periodically identified or newly sampled. The empirical observation second moment equals its finite-prefix value at every volume, discharging that family's moment hypothesis exactly. No scalar value of that moment was evaluated and no data/network run was needed. Its uniformly rooted mark law is the finite mixture of periodic phases.

This conditional construction does not adopt or validate the registered independently generated R0 volume family. That family still needs a declared increasing-volume core/data admission with uniform admissibility and empirical second-moment control in its intended deterministic or probabilistic mode. The theorem asserts subsequential snapshot existence, rather than uniqueness, a full-volume or designated unrooted-site limit, mixing or convergence of archived states to equilibrium. A fixed finite continuous local readout has a weak pushforward limit along the same subsequence, with stabilized structural indices. Growing-depth products, reverse conditional kernels, unbounded decoder expectations, an infinite recognition process, native-posterior accuracy and RG/formation closure remain separate obligations.

## Exact centered source quadratic-correction moment

The [source correction derivation](https://github.com/cdenn016/MultiAgentELBO/blob/137a4a7cd1c3572ce1db3cf7abd4b8d984c2782b/docs/research/2026-10-03-latent-link-rg-plan/R3-SOURCE-QUADRATIC-MOMENT.md) retains the existing supported softmax proposal, conditioned on the old state and retained inputs with fresh independent standard Gaussian Brownian inputs. For four positive source probabilities summing to one, temperature $T=1/20$ and any positive step $h$, its centered quadratic correction satisfies

$$
E[\|Q_\beta\|^2\mid\beta]/h^2=12T^2\sum_j\beta_j^2.
$$

This is the ordinary supported Euclidean norm, preserved by an orthonormal tangent chart; it is not the Fisher norm. Writing the correction as centered symmetric Gaussian quadratic forms yields its complete covariance and exact Gaussian fourth-moment averaging. The covariance annihilates the all-ones vector, so the correction remains tangent. A compact simplex maximization, rather than sampling source rows, gives the sharp outer-floor value $111/10000=0.0111$ at permutations of $(11/20,3/20,3/20,3/20)$. The inner floor $9/50$ gives $579/62500=0.009264$; the uniform-row value is $3/400$.

This replaces only the previous loose source coefficient $32/3$, improving it by the factor $320000/333$. The unchanged sufficient Gaussian covariance-correction bounds remain $57/100$ for matter and $313/7200$ for generators, so the direct global quadratic coefficient after this source-only improvement is at most $57/100$. Those Gaussian values are sufficient bounds, rather than exact variances. The result does not evaluate covariance correction moments, cubic/higher remainders, numerical exits or function/input arithmetic and does not establish that the complete four-step forecast/common-exit target passes.

The [scalar receipt](https://github.com/cdenn016/MultiAgentELBO/blob/137a4a7cd1c3572ce1db3cf7abd4b8d984c2782b/docs/research/2026-10-03-latent-link-rg-plan/evidence/source-quadratic-moment.json) records 37 zero exact polynomial remainders: four means, sixteen covariance identities, sixteen tangent identities and the summed second moment. These checks support the algebra; the Gaussian averaging and compact maximization are supplied by the proof. The CPU calculation uses Python 3.14.4 and SymPy 1.14.0 without Torch. Its first invocation fails because an integer Groebner domain rejects the rational temperature coefficient. Selecting the rational domain `QQ` repairs that implementation issue without changing formulas or boxes; the next invocation completes in approximately 0.60 seconds, retaining both source hashes and exit codes. No network, trajectory or GPU runs.

The receipt's three bound-source hashes match published Git blobs at `95aeba5aa9ea0e1542ca46fbed3795731692f133`. A subsequent TeX correction changes a literal tab plus `frac12` into `\frac12`, preserving the Gaussian Fisher coefficient, mathematical assumptions and original receipt bytes. Root checks the earlier bindings without rerunning the symbolic calculation. The exact source-component identity is separate from numerical floating arithmetic and a complete path-error certificate.

## Relevance to this research

[[Renormalization-group flow of beliefs]] gains conditional native recognition snapshot limits with all nonlinear local terms and interior coordinates retained. [[Natural gradient]] gains a sharp source component for the existing proposal, while [[Staged hierarchy formation and RG composability]] still requires admitted independently generated volume inputs, dynamical/size-depth consistency, quantitative numerical error and native-posterior/parent/formation closure. All four full RG gates remain open, the reward choice is unadopted and the 144-case GPU calibration remains unrun. No manuscript, scientific model, source update or GPU allocation is changed by this batch.
