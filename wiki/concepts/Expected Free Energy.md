---
type: concept
title: "Expected Free Energy"
aliases:
  - EFE
  - "Expected free energy"
  - "Expected free-energy functional"
  - "G(pi)"
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
  - project/transformer
status: draft
created: 2026-06-21
updated: 2026-06-21
---

# Expected Free Energy

**Expected free energy** (EFE), written $G(\pi)$, is the free-energy functional evaluated over
*future* outcomes that have not yet occurred. Whereas [[Variational free energy]] (VFE) scores how
well an agent's current beliefs explain outcomes it has *already* observed, expected free energy
scores a candidate course of action — a **policy** $\pi$ (a sequence of control states) — by the
free energy the agent *expects* to incur if it follows that policy into the future. In
[[Active inference]], action selection is cast as inference over policies: an agent prefers
policies that minimize expected free energy, and the central result is that this single quantity
decomposes into an exploratory (epistemic) term and a goal-directed (pragmatic) term, giving
active inference a built-in, principled resolution of the explore–exploit dilemma without any
hand-engineered exploration bonus or separate reward function
([[friston-2017-active-inference-process-theory]], [[friston-2016-active-inference-learning]],
[[smith-2022-active-inference-tutorial]]).

## Definition

Active inference is formulated on a generative model — typically a partially observable Markov
decision process (POMDP) — over outcomes $o$, hidden states $s$, and policies $\pi$, with a
likelihood $p(o\mid s)$, policy-conditioned transitions $p(s_\tau \mid s_{\tau-1}, \pi)$, and a
vector of **prior preferences** $p(o\mid C)$ encoding which outcomes the agent treats as
*a priori* probable, i.e. desirable ([[smith-2022-active-inference-tutorial]]). Variational free
energy for past/present outcomes is the expected log-ratio of approximate posterior to generative
model,

$$
F = \mathbb{E}_{q(s)}\!\left[\ln q(s) - \ln p(o, s)\right],
$$

an upper bound on surprisal $-\ln p(o)$ whose minimization drives $q(s)$ toward the true posterior
$p(s\mid o)$ ([[smith-2022-active-inference-tutorial]]; see [[Variational free energy]]). Because
future outcomes are not yet known, they must be treated as **random variables** distributed under
the agent's predictions $q(o_\tau \mid \pi)$. Taking the expectation of the future free energy
under those predicted outcomes yields the expected free energy of policy $\pi$ at future time
$\tau$,

$$
G(\pi) = \mathbb{E}_{q(o_\tau, s_\tau \mid \pi)}\!\left[\ln q(s_\tau \mid \pi) - \ln p(o_\tau, s_\tau \mid \pi)\right],
$$

where the posterior preferences over outcomes $p(o\mid C)$ enter in place of a generic prior — this
is the formal device by which "what the agent wants" is folded into the same inferential objective
that governs "what the agent believes" ([[friston-2017-active-inference-process-theory]]).

## The epistemic + pragmatic decomposition

The single expression for $G(\pi)$ admits two complementary, exactly-equivalent rearrangements that
are the heart of why active inference behaves intelligently.

**Epistemic + pragmatic value.** Grouping terms so that the preference distribution $p(o\mid C)$ is
isolated gives

$$
G(\pi) \;=\; \underbrace{-\,\mathbb{E}_{q(o\mid\pi)}\big[\ln p(o\mid C)\big]}_{\text{pragmatic (extrinsic) value}}
\;-\; \underbrace{\mathbb{E}_{q}\big[\,D_{\mathrm{KL}}[\,q(s\mid o,\pi)\,\|\,q(s\mid\pi)\,]\,\big]}_{\text{epistemic (intrinsic) value}}.
$$

The **pragmatic** (extrinsic, goal-directed) term rewards policies whose expected outcomes match the
agent's preferences $C$ — this is the active-inference analogue of utility or reward. The
**epistemic** (intrinsic, exploratory) term is the *expected information gain* about hidden states:
the KL divergence between the posterior over states *after* a predicted observation and the posterior
*before* it, i.e. the **Bayesian surprise** an outcome is expected to deliver. Equivalently this
epistemic term is the mutual information $I[s;o\mid\pi]$ between states and outcomes under the policy
([[friston-2016-active-inference-learning]], [[friston-2017-active-inference-process-theory]]).
Because $G$ is *minimized*, policies that maximize both the agreement with preferences and the
expected information gain are favored, so curiosity (epistemic foraging) emerges automatically from
the same objective — no separate intrinsic-reward signal is added
([[friston-2017-active-inference-process-theory]]).

**Risk + ambiguity.** Regrouping the *same* quantity around the predicted-outcome distribution
$q(o\mid\pi)$ instead gives the form most often quoted in implementations
([[smith-2022-active-inference-tutorial]], [[friston-2017-active-inference-process-theory]]):

$$
G(\pi) \;=\; \underbrace{D_{\mathrm{KL}}\!\left[\,q(o\mid\pi)\,\big\|\,p(o\mid C)\,\right]}_{\text{risk}}
\;+\; \underbrace{\mathbb{E}_{q(s\mid\pi)}\!\left[\,H[\,p(o\mid s)\,]\,\right]}_{\text{ambiguity}}.
$$

**Risk** is the KL divergence between the outcomes a policy is *predicted* to produce and the
outcomes the agent *prefers*: it penalizes policies likely to land the agent in dispreferred
states. **Ambiguity** is the expected entropy of the likelihood $p(o\mid s)$ — the residual outcome
uncertainty that remains even when the hidden state is known — and minimizing it drives the agent
toward states where observations are maximally informative about (i.e. maximally diagnostic of) the
hidden cause. The two decompositions are algebraically equivalent: risk corresponds to the negated
pragmatic value plus a predictive-entropy term, and ambiguity is the complement that, together with
risk, reconstructs the epistemic/pragmatic split ([[smith-2022-active-inference-tutorial]]). Which
form one writes is a matter of which grouping is most convenient — risk/ambiguity is natural for
the discrete POMDP code, epistemic/pragmatic for the conceptual explore–exploit reading.

## Policy selection: $\pi = \mathrm{softmax}(-G)$

Active inference treats action as inference: the agent infers a posterior over policies whose
log-probability is *proportional to the negative expected free energy*. The prior over policies is
itself a [[Softmax]] of $-G$,

$$
p(\pi) = \sigma\!\big(-\gamma\, G(\pi)\big),
\qquad
\sigma(x)_i = \frac{e^{x_i}}{\sum_j e^{x_j}},
$$

where $\gamma$ is a **policy precision** (an inverse temperature) controlling how sharply the agent
commits to the best policy; in the neural process theory $\gamma$ is identified with phasic
dopamine and is itself updated from a Gamma hyperprior
([[friston-2017-active-inference-process-theory]]). After outcomes are observed, the full posterior
over policies additionally subtracts the *variational* free energy accrued so far, giving the
update used in the SPM/POMDP implementations
([[smith-2022-active-inference-tutorial]], [[friston-2017-active-inference-process-theory]]):

$$
\pi = \sigma\!\big(\ln \mathbf{E} - F(\pi) - \gamma\, G(\pi)\big),
$$

where $\mathbf{E}$ is a fixed prior over policies (the agent's "habit"). The softmax-over-negative-
EFE rule is exactly the Boltzmann/Gibbs form: low-$G$ policies dominate, and $\gamma$ tunes the
exploration temperature. This is the discrete-state ancestor of the temperature-scaled attention
weights elsewhere in this program (see *Relevance* below).

## Key results

- **Explore–exploit is solved by construction.** Minimizing one functional, $G$, simultaneously
  maximizes goal-attainment (pragmatic value / negative risk) and information gain (epistemic value
  / negative ambiguity), so exploratory behavior is not bolted on but falls out of Bayes-optimal
  policy inference ([[friston-2016-active-inference-learning]],
  [[friston-2017-active-inference-process-theory]]).
- **Epistemic foraging emerges with no curiosity reward.** Simulated agents seek out
  information-rich observations purely because doing so lowers expected free energy; in the
  two-armed-bandit-with-hint task of [[smith-2022-active-inference-tutorial]], varying preference
  precision and policy precision $\gamma$ smoothly trades the agent between information-seeking and
  reward-seeking ([[smith-2022-active-inference-tutorial]]).
- **A process theory, not just a normative ideal.** Reading the gradient descent on $F$ and the
  softmax on $-G$ as neuronal dynamics reproduces a broad catalogue of empirical phenomena
  (repetition suppression, mismatch negativity, place-cell activity, dopaminergic transfer), with
  variational free energy serving as a Lyapunov function for the dynamics
  ([[friston-2017-active-inference-process-theory]]).
- **Same objective, three timescales.** Perception (state inference), action (policy selection via
  $G$), and learning (Dirichlet parameter updates) are all gradient flows on free energy, differing
  only in *what* is optimized and on *what* timescale — the fast E-step / slow M-step separation
  ([[friston-2016-active-inference-learning]], [[smith-2022-active-inference-tutorial]]).

## Relevance to this research

Expected free energy is the action-selection layer that the present program reuses and generalizes.

The softmax-over-negative-EFE policy rule $\pi = \sigma(-\gamma G)$ is the structural ancestor of
the temperature-scaled attention weights that fall out of the multi-agent free-energy functional in
[[GL(K) gauge-equivariant attention]]: there, an information-geometric divergence between
gauge-transported beliefs plays the role of the per-policy score $G$, and the inverse-temperature
$\beta$ plays the role of the policy precision $\gamma$. The epistemic/pragmatic (equivalently
risk/ambiguity) split is the reference decomposition against which the program's attention-entropy
and meta-entropy couplings should be read — the ambiguity term (expected likelihood entropy) is the
discrete cousin of the entropy regularizer on the attention distribution.

Because policy precision $\gamma$ here is exactly an inverse temperature on a free-energy score, EFE
also connects to the program's information-geometric machinery: the curvature of these free-energy
landscapes is governed by the [[Fisher information metric]], gradient flows on them are
[[Natural gradient]] flows, and the precision/temperature parameters are the action-side analogue of
the [[Precision weighting]] that the transformer applies on the perception side. The single-agent
EFE of [[friston-2017-active-inference-process-theory]] supplies the **baseline that the multi-agent
generalization must reduce to**: coupling many such agents yields
[[Multi-agent variational free energy]] and the group-level objective of
[[Collective active inference]], where each agent's expected free energy is augmented by terms
coupling its predicted outcomes to its neighbors' beliefs. See
[[Variational free energy and predictive coding]] and
[[Inference machinery — variational EM and filtering]] for where this template plugs into the
[[VFE Transformer Program]] and the [[Gauge-Theoretic Multi-Agent VFE Model]].

As of 2026-06-28 the EFE functional is operationalized for the *transformer* as well, not only the multi-agent
setting: [[2026-06-28-active-inference-efe-policy-scorer-spec]] pre-registers a default-off, no-grad EFE policy
scorer that reranks candidate token continuations by $G(\pi)=\mathrm{KL}[q(o\mid\pi)\|p(o\mid C)]+\mathbb{E}_{q(s\mid\pi)}H[p(o\mid s)]$
with $Q(\pi)=\mathrm{softmax}(\log E-\gamma G)$, using an explicit *peaked task preference* for $p(o\mid C)$ so the
risk term is a genuine goal rather than negative log-likelihood. The design records a sharp caveat that the
canon makes inevitable: at a one-step, sigma-free point belief the epistemic term $\mathcal{I}(o;s\mid\pi)$ is
identically zero, so the first version is a pragmatic preference-matching reranker and the epistemic/ambiguity
machinery stays inert until belief-uncertainty enters the rollout (or the $\sigma$ signal passes a pre-registered
validation gate). Nothing is implemented and no efficacy is claimed.

As of 2026-06-29 that pre-registered $\sigma$-validation gate has been measured, and it FAILed
([[2026-06-29-sigma-gate-fail-and-collapse]]). On the prior-bank decode checkpoint the belief-covariance trace is
*anti-correlated* with realized cross-entropy ($\rho=-0.137$) and near-constant (cv $0.0445$), so $\sigma$ is not a
usable epistemic signal — the information-gain / ambiguity arm stays inert *empirically*, not only by the $H{=}1$
scope argument. The cause is structural: the vfe3 belief E-step carries no observation/data-precision term (a
[[Variational EM|target-blind E-step]]; the canonical $-\mathbb{E}_q[\log p(o\mid x)]$ term is a gated stub with no
live caller), so the covariance is a near-static learned prior the [[Precision weighting|precision]] machinery never
contracts toward data. Making the EFE epistemic term live would require wiring an observation-precision term into
the E-step covariance gradient — the canonical-vs-reduced choice the manuscripts lay out.

> [!note] Editorial: The risk/ambiguity and epistemic/pragmatic decompositions, the
> softmax-over-$-G$ policy rule, and the explore–exploit and epistemic-foraging results are
> established by the cited sources. The mappings to GL(K) attention weights, meta-entropy, the
> Fisher/natural-gradient reading, and the multi-agent generalization are *this program's* synthesis,
> not claims of the cited papers.

## Related

[[Variational free energy]] · [[Active inference]] · [[Free-energy principle active inference]] ·
[[Precision weighting]] · [[Softmax]] · [[Fisher information metric]] · [[Natural gradient]] ·
[[Belief Propagation]] · [[Multi-agent variational free energy]] · [[Collective active inference]] ·
[[GL(K) gauge-equivariant attention]] · [[Bayesian mechanics]]

## Sources

[[friston-2017-active-inference-process-theory]] ·
[[friston-2016-active-inference-learning]] ·
[[smith-2022-active-inference-tutorial]]
