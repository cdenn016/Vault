---
type: concept
title: "Mutual information"
aliases:
  - "I(X;Y)"
  - Mutual information
tags:
  - cluster/info-geometry
  - cluster/attention
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-06-21
updated: 2026-07-10
---

# Mutual information

## Definition

The **mutual information** between two random variables $X$ and $Y$ is the relative entropy (Kullback-Leibler divergence) between their joint distribution and the product of their marginals:

$$
I(X;Y) = D_{\mathrm{KL}}\big(p(x,y)\big\|p(x)p(y)\big)
= \sum_{x,y} p(x,y)\log\frac{p(x,y)}{p(x)p(y)}.
$$

It measures how far $X$ and $Y$ are from being independent — equivalently, how many bits (or nats) observing one variable reveals about the other. Because it is a KL divergence it inherits the master inequality $D_{\mathrm{KL}}(p\|q)\ge 0$ (Gibbs' inequality), so $I(X;Y)\ge 0$, with equality **iff** $p(x,y)=p(x)p(y)$, i.e. iff $X\perp Y$. These properties, and the development that follows, are the standard textbook account of [[cover-thomas-2006-elements-information-theory]].

Writing $H(X)=-\sum_x p(x)\log p(x)$ for the **entropy** (see [[Maximum entropy]]) and $H(X\mid Y)$ for the conditional entropy, mutual information admits the entropy decompositions

$$
I(X;Y) = H(X) - H(X\mid Y) = H(Y) - H(Y\mid X) = H(X)+H(Y)-H(X,Y).
$$

The first form reads it as the **reduction in uncertainty** about $X$ from observing $Y$. The symmetry $I(X;Y)=I(Y;X)$ is manifest in the joint-vs-product definition. For a fixed channel and input distribution it is the achieved information rate; channel capacity is the supremum of this mutual information over admissible input distributions. The quantity dates to [[shannon-1948-mathematical-theory-communication]].

## Key identities

Three structural facts make mutual information the workhorse of representation learning and of this program.

**Chain rule.** Mutual information factors over a sequence exactly as entropy does:

$$
I(X_1,\dots,X_n;Y) = \sum_{i=1}^{n} I(X_i;Y \mid X_1,\dots,X_{i-1}),
$$

with conditional mutual information $I(X;Y\mid Z)=\mathbb{E}_{Z}\big[D_{\mathrm{KL}}(p(x,y\mid z)\|p(x\mid z)p(y\mid z))\big]$. The chain rule is what lets one bound the information a whole representation carries by accumulating the marginal contributions of its parts ([[cover-thomas-2006-elements-information-theory]]).

**Data-processing inequality (DPI).** If $X\to Y\to Z$ is a Markov chain — $Z$ depends on $X$ only through $Y$ — then

$$
I(X;Y) \ge I(X;Z).
$$

No deterministic or stochastic post-processing of $Y$ can increase its information about $X$: information can only be destroyed downstream, never created ([[cover-thomas-2006-elements-information-theory]]). The DPI is the hard constraint that makes the [[Information bottleneck]] trade-off well-posed — it is *why* a compressed code $T$ of $X$ cannot retain more relevance $I(T;Y)$ than $X$ itself supplied.

**Invariance under reparameterization.** Mutual information is invariant under any invertible (one-to-one) transformation applied separately to $X$ or to $Y$; it depends on the joint distribution, not on the coordinates in which the variables are expressed. This coordinate-freeness is the discrete-information shadow of the reparameterization invariance of the [[Fisher information metric]].

## The information-bottleneck objective

The [[Information bottleneck]] (IB) of [[tishby-1999-information-bottleneck]] is built entirely from mutual information. Given a source $X$ and a *relevance variable* $Y$, one seeks a compressed representation $T$ (a stochastic encoder $p(t\mid x)$, with $T$ a function of $X$ alone so that $Y\to X\to T$ is Markov) that minimizes the information kept about $X$ while maximizing the information kept about $Y$:

$$
\mathcal{L}_{\mathrm{IB}} = I(X;T) - \beta I(T;Y),
$$

where $I(X;T)$ is the **complexity** (code rate) and $I(T;Y)$ the **accuracy** (relevance retained), traded off by a Lagrange multiplier $\beta>0$. The DPI guarantees $I(T;Y)\le I(X;Y)$, so the objective is genuinely a compression-under-a-ceiling problem. Stationarity gives a self-consistent fixed point in which the optimal assignment is a **softmax over a KL distortion**,

$$
p(t\mid x)\propto p(t)\exp\big(-\beta D_{\mathrm{KL}}(p(y\mid x)\|p(y\mid t))\big),
$$

solved by Blahut-Arimoto-style alternating projection; sweeping $\beta$ traces the **information plane** $\big(I(X;T),I(T;Y)\big)$, whose boundary generalizes the rate-distortion curve ([[tishby-1999-information-bottleneck]]). The Gaussian case has a closed-form spectral optimum ([[chechik2005information-bottleneck-gaussian|chechik-2005-gaussian-ib]]), and a layerwise "fitting-then-compression" reading of deep networks lives in the information plane ([[shwartz-ziv-2017-opening-black-box]]). See [[Information bottleneck]] for the full treatment and its mapping onto the program's variational free energy.

## Quadratic regime and the Fisher metric

Mutual information is a KL divergence, and every KL divergence reduces *locally* to the [[Fisher information metric]]. Consider a parametric family $p(x\mid\theta)$ and an infinitesimal displacement; the second-order Taylor expansion of the relative entropy is

$$
D_{\mathrm{KL}}\big(p_\theta \| p_{\theta+d\theta}\big)
= \tfrac12 d\theta^{\top} F(\theta) d\theta + o(\|d\theta\|^2),
$$

where $F(\theta)$ is the Fisher information matrix. Read in this light, mutual information is the **global** object whose **local** quadratic form is the Fisher metric ([[cover-thomas-2006-elements-information-theory]], [[Fisher information metric]]).

Two specializations make the "quadratic regime" of mutual information concrete:

- **Weak dependence.** When $X$ and $Y$ are *nearly* independent, parameterize the joint as a small perturbation of the product, $p(x,y)=p(x)p(y)\big(1+\epsilon\delta(x,y)\big)$ with $\mathbb{E}[\delta]=0$. Then $I(X;Y)=\tfrac12\epsilon^2\mathbb{E}_{p(x)p(y)}[\delta^2]+o(\epsilon^2)$ — mutual information vanishes quadratically in the coupling strength, with the leading coefficient a $\chi^2$-type Fisher quantity. Independence is therefore a *flat minimum* of $I$, and the curvature there is Fisher information.

- **Estimation / channel limit.** For a "weak channel" $Y=\theta + \text{noise}$ in which $Y$ carries a small amount of information about a parameter $\theta\sim p(\theta)$, the mutual information $I(\theta;Y)$ is governed at leading order by the Fisher information the channel supplies about $\theta$, tying $I$ to estimability through the local quadratic form ([[cover-thomas-2006-elements-information-theory]]).

> [!note] Editorial: The two displayed quadratic specializations above are the standard small-coupling and weak-channel expansions of $I$; the wiki states the leading $\tfrac12$-curvature coefficient explicitly, whereas [[cover-thomas-2006-elements-information-theory]] develops the $D_{\mathrm{KL}}$-to-Fisher local relation and the $I$-as-capacity link but does not headline these particular expansions. The identification of that curvature with the Fisher metric is standard information geometry — see [[Fisher information metric]] and [[Statistical manifold]].

This local KL expansion produces Fisher geometry. Smooth order-[[Renyi divergence]]
members also produce a Fisher quadratic form, but with an order-dependent
positive scale, while Amari [[Alpha-divergence]]s carry their own dualistic
structure. A nonlinear monotone relation between divergence values does not
transfer gradients, Hessians, affine connections, or global geometry. See
[[Information geometry and natural gradient]].

## Relevance to this research

Mutual information is the bridge between the Shannon-information vocabulary in which the gauge-theoretic VFE objective is *written* and the information geometry on which it *moves*.

**Free-energy couplings and relative entropy.** At KL order, the canonical
belief and model discrepancy terms are relative entropies, and the
attention-distribution regularizer is a KL to its attention prior. Mutual
information is the different KL between a joint law and the product of its
marginals; it does not automatically equal or aggregate a sum of pairwise
belief discrepancies. A configured order-Rényi term must be analyzed as that
distinct divergence.

**Attention and the information bottleneck.** The IB fixed point and
entropy-regularized belief coupling both contain a softmax over a KL-like
distortion, but their variables and objectives differ. The program's
self-coupling coefficient $\alpha$ is not Tishby's relevance multiplier
$\beta$, and the pairwise attention rule is not thereby an IB optimum. The
connection is a formal comparison, not an equality of functionals.

**Meta-agent coarse-graining.** Grouping units by the similarity of their predictive distributions $p(y\mid x)$ — distributional clustering that preserves mutual information with the relevance variable while compressing the input — is the information-theoretic route by which [[Meta-agents and hierarchical emergence|meta-agents]] form, and the DPI bounds how much relevant information any coarse-graining can retain (see [[Renormalization-group flow of beliefs]] and [[Multi-agent variational free energy]]).

**From information to geometry.** The KL expansion supports the
[[Fisher information metric]] used for Gaussian belief updates. It does not
turn the separate plain-AdamW frame M-step or decode optimizer into a natural
gradient, and it does not identify every pairwise information cost with one
joint statistical manifold. [[gl-k-attention-2026-07-09-review-revision]]

## Sources

- [[cover-thomas-2006-elements-information-theory]] — defines entropy, relative entropy, and mutual information; the chain rules, the data-processing inequality, and the relative-entropy-to-Fisher local relation.
- [[shannon-1948-mathematical-theory-communication]] — founding definitions of entropy and mutual information; channel capacity as the maximum of $I(X;Y)$ over input laws.
- [[tishby-1999-information-bottleneck]] — the information-bottleneck objective $I(X;T)-\beta I(T;Y)$; KL-distortion softmax assignment; the information plane.
- [[chechik2005information-bottleneck-gaussian|chechik-2005-gaussian-ib]] — closed-form Gaussian information bottleneck; spectral, phase-transition optimum.
- [[shwartz-ziv-2017-opening-black-box]] — information-plane (fitting-then-compression) dynamics of deep networks.
- [[slonim-2000-agglomerative-ib]] — agglomerative IB; relevance-preserving coarse-graining, cousin of meta-agent formation.

## See also

- [[Information bottleneck]]
- [[Fisher information metric]]
- [[Statistical manifold]]
- [[Variational free energy]]
- [[Renyi divergence]]
- [[Alpha-divergence]]
- [[Maximum entropy]]
- [[Information geometry and natural gradient]]
- [[GL(K) gauge-equivariant attention]]
- [[Meta-agents and hierarchical emergence]]
- [[Physics from Fisher information]]
