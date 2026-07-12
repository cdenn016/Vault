---
type: theme
title: "Inference machinery — variational EM and filtering"
aliases:
  - "Variational EM and filtering"
  - "Inference machinery"
  - "E-step / M-step inference loop"
  - "Filtering inference"
tags:
  - cluster/vfe
  - cluster/methodology
  - project/transformer
status: stable
created: 2026-06-18
updated: 2026-07-12
---

# Inference machinery — variational EM and filtering

## The big picture

The [[VFE Transformer Program]] treats every token not as a fixed vector but as a
*belief*: a per-token diagonal Gaussian with mean `mu` and covariance `Sigma`. The
machinery that updates those beliefs, and the parameters that shape them, is the
subject of this page. It is the engine room of the architecture — the loop that, on
each forward pass, decides what the model currently believes and how confident it is,
and on each backward pass, updates parameters through a separate decode loss. The
architecture borrows the alternating skeleton of [[Variational EM]], but its target-blind
belief filter and decode cross-entropy do not optimize a single shared functional.
“Structural EM” names that organization, not a coordinate-ascent guarantee.
[[gl-k-attention-2026-07-09-review-revision]]

The unifying observation, due to [[neal-1998-variational-em]], is that the
Expectation-Maximization algorithm is not two unrelated operations but coordinate
ascent on *one* functional — the negative [[Variational free energy]], equivalently the
[[Evidence lower bound (ELBO)]]. The E-step holds parameters fixed and optimizes the
variational belief distribution `q`; the M-step holds `q` fixed and optimizes the
parameters. Neal and Hinton show this functional view licenses *incremental*
and *partial* updates: you need not run either step to convergence before switching.
That permission applies to textbook shared-functional EM. The transformer's target-blind
belief objective and decode cross-entropy are distinct, so its one-step filter is not
licensed by Neal–Hinton monotonicity. [[gl-k-attention-2026-07-09-review-revision]]

Where Neal and Hinton supply the algorithmic justification, [[friston-2010-free-energy-principle]]
supplies the semantics. Friston's free-energy principle casts perception, attention,
and learning as a single imperative: minimize variational free energy, an upper bound on
surprise (negative log model evidence). In this reading the E-step is *perception*
(inferring hidden causes of the input), the M-step is *learning* (improving the
generative model), and the precision terms that weight prediction errors are *attention*.
For the VFE transformer this is conceptual background, not a literal single-objective
description of its structural-EM schedule. [[gl-k-attention-2026-07-09-review-revision]]

For the discrete (POMDP)
incarnation of the same scheme, [[smith-2022-active-inference-tutorial]] is the standard
operational reference: it writes out the explicit variational and expected-free-energy update
equations and the worked mean-field factorization over hidden states, policies, and parameters,
giving an equation-level E-step/M-step template against which to benchmark this program's
filtering loop.

The remaining ingredient — what makes the beliefs Gaussian and the updates concrete — comes
from the predictive-coding lineage. [[rao-1999-predictive-coding]], [[bogacz-2017-free-energy-tutorial]],
and [[millidge-2020-pc-approximates-backprop]] turn the abstract free-energy functional
into explicit, local, precision-weighted [[Prediction error]] dynamics on Gaussian
variables. Exact-backprop recovery is a convergence result for the source model; it does
not certify the transformer's truncated, two-objective filtering loop. [[gl-k-attention-2026-07-09-review-revision]]

## Key threads

**EM as free-energy coordinate ascent.** The foundational thread is
[[neal-1998-variational-em]]'s reframing of EM. By exhibiting EM as ascent on the negative
free energy `F(q, theta)`, it makes the E-step an explicit optimization over the belief
`q` rather than a fixed posterior computation, which is precisely what is needed when the
exact posterior is intractable and `q` must be an approximating diagonal Gaussian. The
incremental and sparse variants Neal and Hinton justify are precedents for partial updates
on one shared functional. The transformer's `filtering` label is only an analogy: its
target-blind belief and decode objectives are distinct, so their guarantee does not
transfer. What a textbook E-step optimizes is fixed by the chosen mean-field
factorization, and [[winn-2005-variational-message-passing]] makes that structure
computational: on conjugate-exponential models, mean-field variational inference becomes local
message passing on a factor graph, pinning down which factorization underwrites a given update
and providing a comparison for local message routing. The deployed attention
uses precision-weighted pairwise belief mismatches, not observation-prediction
errors from that factor graph.

**The free-energy principle and precision-weighted perception.**
[[friston-2010-free-energy-principle]] elevates the same functional to a theory of
neural computation, and [[rao-1999-predictive-coding]] gives its mechanistic prototype:
hierarchical predictive coding, where feedback connections carry top-down predictions and
feedforward connections carry *precision-weighted prediction errors*. The precision (inverse
variance) gates how strongly each error influences belief updates — high precision means
"trust this error, attend to it." This is the conceptual seed of the architecture's
precision-weighted attention (see the theme [[Variational free energy and predictive coding]]
and the method [[Predictive coding network]]). [[bogacz-2017-free-energy-tutorial]] makes the
mapping operational, deriving for Gaussian beliefs the explicit E-step belief-relaxation
update (gradient descent on free energy in `mu`) and the M-step precision-learning update
(updating `Sigma` and weights). The transformer's belief-side precision weighting is
analogous, but its one-step filter and separate decode objective do not reproduce both
updates. [[buckley-2017-fep-mathematical-review]] supplies the cleanest
self-contained worked derivation of the same continuous-state machinery — the Laplace-encoded
variational free energy, the gradient-descent E-step on `mu`, and the precision-weighted
prediction-error dynamics for Gaussian beliefs — serving as a derivation bridge from the
Bishop/Beal ELBO canon to the Friston-style free-energy claims that the filtering E-step mirrors.

**Predictive-coding/backpropagation equivalence is conditional.**
[[millidge-2020-pc-approximates-backprop]] proves exact-gradient recovery for the source
model under its convergence and scheduling assumptions. The transformer's finite one-$s$/one-$q$
inner schedule, separate decode objective, and no-neural-network pure path do not satisfy that
theorem by description alone. [[gl-k-attention-2026-07-09-review-revision]]

**Population representability separates filtering from smoothing.** A fixed-model mean-field ELBO
has zero mixed third variation $D^3_{q_iq_jq_j}$, whereas a nondegenerate transported consensus
term $D_{\mathrm{KL}}(q_i\Vert T_{ij}q_j)$ does not. The population consensus scalar is therefore
not generally the ELBO of one fixed joint on the original token states. A finite positive
receiver-response map still has a Brouwer equilibrium when incoming source roles are frozen, but
that filtering equilibrium is not thereby stationary for the global smoothing scalar. A separate
configuration-space Gibbs lift is exact when its partition function is finite; it changes the
latent variable from token states to whole belief configurations. These distinctions govern which
fixed-point, CAVI, and evidence-bound claims can accompany each executable update mode.
[[vfe-population-generative-status-2026-07-12]]

**Credit assignment by inference: the backprop-free track.** The 2026-07-11 plan
([[Nudged two-phase EM]], banked in [[2026-07-11-backprop-free-plan-and-pure-fep-postmortem]])
turns the structural-EM caveats above into a constructive prescription: restore the observation
term to the belief update (the [[participatory-it-from-bit|PIFB]]-canonical placement) in a pair
of symmetric target-nudged continuations of the free E-step, and estimate the through-$q^*$
credit that fixed-$q^*$ M-steps drop by the [[scellier-bengio-2017-equilibrium-propagation|equilibrium-propagation]]
contrast of analytic envelope statistics. The adjudicated post-mortem of VFE_2.0's target-blind
clean-EM attempt (~25000 PPL) is the negative result motivating this: at a target-blind fixed
point, the envelope theorem fails for the decode term by construction, and a provable temperature
degeneracy ($\partial F_{red}/\partial\tau = \mathrm{KL}(\beta\|\pi)\ge 0$) makes several
hyperparameters unlearnable by any free-energy descent. Design stage only; the EqProp theorem's
equilibrium premise does not hold under truncated settling, so gates replace guarantees.

**Amortization and iterative refinement.** VAEs and iterative-amortized methods provide
recognition-network and learned-optimizer precedents. The pure transformer contains neither:
it carries model and belief states explicitly and applies finite target-blind refinements.
Amortization is therefore a comparison, not the precise template or a demonstrated gap-closing result for
`filtering`. See [[Amortized inference]], [[Variational autoencoder (VAE)]], and
[[Iterative amortized inference]]. [[gl-k-attention-2026-07-09-review-revision]]

## How it lands in this work

In the decoded config, each token carries diagonal-Gaussian model and belief states. The inner
stage first performs one target-blind $s$ refinement toward the learned global $r$ and
gamma-weighted model consensus. It then sets $q_i^{(0)}=p_i=s_i^{(1)}$ and performs one
target-blind natural-gradient $q$ refinement on alignment/self-coupling terms. Neither is an
argmin or CAVI update. The outer stage minimizes decode cross-entropy through both unrolled
paths. See the structural-EM disclosure in [[Variational EM]]; no shared-functional monotonicity
or exact-backprop guarantee applies to this loop. [[gl-k-attention-2026-07-09-review-revision]]

The belief machinery uses the Gaussian-family Fisher metric. At each recorded source SHA, the frame
table is routed through AdamW by the committed gate and stored configuration, although dirty provenance
prevents byte-level reconstruction. Heavy-ball is confined to the disabled custom outer frame optimizer;
BCH/retraction is confined to disabled in-E-step frame revision; and the shared pullback conditioner is
inactive because both optional routes are off. Optional frame conditioning is not a Fisher natural gradient.
[[gl-k-attention-2026-07-09-review-revision]]

Because `Sigma` is symmetric-positive-definite, the belief-covariance updates
live on the SPD manifold and use Riemannian retractions rather than naive
additive steps (the theme [[SPD-manifold geometry and Riemannian optimization]]).
The belief-side objective may use an order-[[Renyi divergence|Rényi divergence]]
with KL as the order-one limit. This pairwise discrepancy is not the variational
Rényi bound of [[li-turner-2016-renyi-vi]]. The decoder is trained by a separate
cross-entropy objective, so no single ELBO or Rényi bound is jointly ascended by
the two inner refinements and the outer update. The inference machinery is structural EM
with distinct inner and decode objectives.
[[gl-k-attention-2026-07-09-review-revision]]

> [!note] Editorial (2026-07-10): The literal `"filtering"` label denotes the target-blind
> belief-refinement component; the retained route precedes it with one model-channel refinement.
> It is analogous to the iterative refinement of
> [[marino-2018-iterative-amortized-inference]], but it is not Neal–Hinton incremental EM because
> the inner and decode updates optimize distinct objectives. Reading this finite refinement as
> a streaming online filter is this program's design choice rather than a claim made by either source.

## Open questions / gaps

Several tensions remain unresolved by the available sources. First, **how many
filtering iterations suffice.** The depth of the target-blind filter is an
empirical compute/relaxation trade-off. Marino et al. provide a learned
amortized-refinement comparison, but their amortization-gap result does not
define the stopping rule for this nonamortized update.

Second, **the structural-EM boundary.** The deployed objectives are already distinct at KL order,
so no Neal–Hinton monotone-improvement guarantee applies before considering Renyi order.
[[gl-k-attention-2026-07-09-review-revision]]

Third, **the backprop-equivalence boundary.**
[[millidge-2020-pc-approximates-backprop]] proves recovery under a converged
source-model schedule. The target-blind filter optimizes a different objective,
so there is no “recovered decode gradient” whose approximation error can be
inferred from that theorem.

Fourth, **amortization under gauge structure.** The recognition network of
[[kingma-2013-auto-encoding-variational-bayes]] assumes a fixed coordinate frame, but this program
transports beliefs across learned gauge frames; whether an amortized encoder can remain consistent
under parallel transport and holonomy (the cross-cluster theme
[[Gauge equivariance and geometric deep learning]]) is unexamined by any source in this digest.

## Sources synthesized

- [[neal-1998-variational-em]] — EM as coordinate ascent on a single free-energy/ELBO functional;
  partial-update guarantees apply only while both coordinates improve that functional.
- [[winn-2005-variational-message-passing]] — mean-field VI on conjugate-exponential models as
  local factor-graph message passing; pins down the factorization behind a given E-step.
- [[friston-2010-free-energy-principle]] — free-energy minimization as a unified account of
  perception, attention, and learning; the training-objective semantics.
- [[smith-2022-active-inference-tutorial]] — discrete (POMDP) active inference: explicit
  variational/expected-free-energy updates and the mean-field factorization as an E-step/M-step
  template.
- [[rao-1999-predictive-coding]] — hierarchical predictive coding; precision-weighted prediction
  errors as the mechanistic prototype.
- [[bogacz-2017-free-energy-tutorial]] — explicit Gaussian E-step belief-relaxation and M-step
  precision-learning updates.
- [[buckley-2017-fep-mathematical-review]] — self-contained continuous-state FEP derivation
  (Laplace VFE, gradient E-step on `mu`, precision-weighted prediction-error dynamics) bridging
  the ELBO canon to Friston-style claims.
- [[kingma-2013-auto-encoding-variational-bayes]] — the VAE: amortized Gaussian recognition and the
  reparameterization trick.
- [[marino-2018-iterative-amortized-inference]] — learned iterative optimizer
  reducing an amortization gap; comparison for repeated refinement, not a
  template that identifies the deployed filter.
- [[millidge-2020-pc-approximates-backprop]] — converged predictive-coding updates recover
  backpropagation under the source paper's schedule; this does not cover the one-step filter.
- [[vfe-population-generative-status-2026-07-12]] — state-level ELBO obstruction,
  receiver-response equilibrium, configuration-Gibbs lift, and V3 two-hop update scope.

Cross-cluster anchors drawn on above: [[amari-1998-natural-gradient]] for the
Gaussian belief metric and [[li-turner-2016-renyi-vi]] as a distinct
variational-bound comparison. Neither identifies the frame/decode M-step.
