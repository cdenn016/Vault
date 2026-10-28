---
type: concept
title: "GL(K) gauge-equivariant attention"
aliases:
  - "glkgaugeequivariantattention"
  - "GL(K) attention"
  - "Gauge-equivariant attention"
  - "Gauge-theoretic attention"
tags:
  - cluster/gauge-theory
  - cluster/attention
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-06-21
updated: 2026-10-28
---

# GL(K) gauge-equivariant attention

## A generative reading of the MLP, October 28, 2026

[[dennis-2026-cue-result-memory]] is a working note, intended for integration into the main manuscript, that replaces the MLP the paper's non-neural section leaves uninterpreted by exact conditioning of a cue/result component bank in reference coordinates ([[Cue-result generative memory]]). The block is passively gauge covariant, its weights are expected-likelihood routing to persistent agents, and its mean response is the posterior result-cue cross-covariance times the record precision.

## Learned frames against capacity controls, October 26, 2026

In [[vfe3-2026-10-26-paper-arms]], at $K=128$ and one epoch, removing the learned per-type $GL(K)$ frames cost 0.212 nats of test cross-entropy. Frames frozen at their random initialization recovered 0.005 nats of that, and replacing the frames by a per-type additive hidden-layer table with as many parameters as the frame table recovered 0.058. The gain therefore comes from frames learned per type, acting multiplicatively, and not from random group elements or from the parameter count of the frame table. The frame gap widens through training, and part of its late train-set advantage does not transfer to validation. A per-type multiplicative map without the group structure is the control this run did not include.

## Transformer layers derived from an objective: prior art, October 6, 2026

Three NeurIPS papers derive transformer layers from an objective and are the prior art for the program's claim of a derived rather than ad hoc transformer. [[yang-2022-transformers-optimization-perspective]] builds a pairwise energy whose majorization-minimization step is softmax self-attention, proves that alternating gradient steps on the attention and feed-forward energies descend their sum outside a bounded region, and adds ReLU as a proximal step; the price is symmetric weights shared across depth, a feed-forward part that is a single symmetric linear map, and evidence that consists of energy-descent curves. [[hoover-2023-energy-transformer]] starts from an engineered energy (a log-sum-exp attention term over keys and a modern-Hopfield term over learned memories on layer-normalized tokens), so that attention, a tied-weight MLP, LayerNorm as the gradient of a Lagrangian and the residual step all follow from descent with a Lyapunov guarantee; it reports masked-image completion and graph benchmarks. [[yu-2023-white-box-transformers-sparse-rate-reduction]] (CRATE) derives attention as an approximate gradient step on a subspace coding rate and replaces the MLP by one ISTA step of nonnegative sparse coding, and reaches ImageNet-1K accuracy 1.6 points below ViT-S at about 22M parameters. All three train their parameters by backpropagation through the unrolled forward pass, and none treats tokens as distributions with propagated covariance, uses a divergence for routing, or has a frame or gauge group.

Against these, the program's distinguishing content is that its forward pass is exact inference in a stated Gaussian model rather than descent of a chosen energy: routing is the source posterior, content is transported by group-valued links, covariances propagate, and the construction is covariant under per-token $\mathrm{GL}(K)$ frames ([[dennis-2026-glk-attention-v2-rework-2026-10-05]], [[dennis-2026-minimal-agent-model]]). What the prior art has and the program lacks is a derived MLP that has been trained (CRATE's ISTA block; ET's Hopfield module, the closest analogue of the untrained [[Template routing]] block), a derivation of LayerNorm (ET, and Yang et al. in an appendix), and a descent guarantee across a whole block (Yang et al.'s AIM theorem; ET's energy). None of the three is backprop-free, so the aim of [[dennis-2026-backprop-free-vfe-language-architecture]] has no precedent among them.

> [!note] Editorial: Yang et al.'s Theorem 3.1 update weights tokens by $\beta_j\exp(y_i^\top y_j)$ with $\beta_j=e^{-\|y_j\|^2/2}$, which equals $\operatorname{softmax}_j(-\tfrac12\|y_i-y_j\|^2)$, the isotropic unit-covariance Gaussian-KL routing of this page's shared-frame limit. The two derivations (an MM step on a pairwise energy, a source posterior) therefore meet at that limit. The comparisons in this section are the vault's reading of the three papers, which do not discuss this program; the search was not exhaustive.

## Prior readings of attention as a sheaf, connection or gauge theory, October 6, 2026

A literature check on the bundle and lattice-gauge language of the October 5 rework found precedent for each ingredient. Graph attention has been extended to cellular sheaves ([[barbero-2022-sheaf-attention-networks]], abstract only), sheaf diffusion with orthogonal restriction maps is a discrete $O(d)$-bundle with a connection Laplacian ([[barbero-2022-sheaf-neural-networks-connection-laplacians]], [[bodnar-2022-neural-sheaf-diffusion]]), and [[disipio-2025-curved-spacetime-transformers]] calls the attention operator a discrete connection by analogy with general relativity, measuring the turning angle of layerwise token trajectories. [[favoni-2022-lattice-gauge-equivariant-cnns]] and [[nagai-2025-cask]] run networks on lattice gauge fields, and [[sengupta2017gauge]] is a gauge theory of variational inference whose attention is neuronal precision weighting. The synthesis is in [[Gauge equivariance and geometric deep learning]].

> [!note] Editorial: In none of these is the object a principal $\mathrm{GL}(K)$-bundle of per-token frames with Gaussian statistical fibers and links $\Theta_{ij}=U_ie^{L_{ij}}U_j^{-1}$, and none states the routed-transport factorization of multi-head attention, as far as the abstracts and the parts read show. This is not an exhaustive search and was not checked adversarially; the novelty of the combination is unverified. In [[disipio-2025-curved-spacetime-transformers]] the update $W_O\hat\alpha_{ij}W_V$ coincides with the affine-chart edge map, so the nearest published statement of the first-order chart is an analogy, not a group-theoretic result.

## Main manuscript rework: agents, comparison links and routed transport, October 5, 2026

[[dennis-2026-glk-attention-v2-rework-2026-10-05]] (drafted by Claude Opus 5.5 agents, reviewed by Claude Fable 5.1, float64 identity checks) rebuilds the main manuscript around communication among statistical agents. The base is a single context $c_*$; each token is an agent whose belief, prior and frame live in a statistical bundle associated with a principal $\mathrm{GL}(K)$-bundle, and a belief is a point of the statistical fiber $\mathbb R^K\times\mathrm{SPD}(K)$ with its [[Fisher information metric]], not a vector of the sample fiber. The four head maps get an agent reading: the sender emits a key $S_K\xi_j$ and content $T\xi_j$, the receiver forms a query $S_Q\xi_i$ that is never transmitted and writes what it receives through the receiving map $\widetilde O$, and the routing weights $\beta_{ij}$ are the decision of whom to hear, computed from the query and the key. When $S_Q$ and $S_K$ are square and invertible the routing cost is exactly $D_{\mathrm{KL}}(q_i\|(\Theta^{\mathrm{cmp}}_{ij})_*q_j)$ with the group-valued comparison link $\Theta^{\mathrm{cmp}}_{ij}=U_iS_Q^{-1}S_KU_j^{-1}$, so the divergence of a receiver's belief from a linked sender belief is the full-rank case of the projected score; through a map of rank below $K$ that divergence is infinite. The notation is now $L_{ij}$ for the Lie-algebra generator, $\Theta_{ij}=U_ie^{L_{ij}}U_j^{-1}$ for the group link and $\Omega_{ij}=U_iU_j^{-1}$ for the flat link.

The central result is a routed-transport theorem: with tiled heads, the shared generator $L=OT$ and routing outside the exponent, the message is $m_i=\sum_jU_if(L)\Pi(\boldsymbol\beta_{ij})U_j^{-1}\mu_j$ with oblique head projectors $\Pi_h$ and $f(L)=L$, $I+L$, $e^L$ in the affine, first-order and exponential charts. [[Multi-head attention]] is therefore a routed oblique projection followed by link transport; when all heads share one routing pattern the exponential chart gives the lattice hopping term $\sum_j\beta_{ij}\Theta_{ij}\mu_j$, and a standard transformer layer is the affine chart with residual coefficient 1. Matrix-valued and group-valued links share the endpoint law and covariance; they differ in invertibility (a groupoid rather than a monoid, hence inverse edges and [[Holonomy]]), in the reachable component $\mathrm{GL}^+(K)$ and in optimization geometry. Whether $OT\in\mathrm{GL}(K)$ in a standard transformer is the wrong question: single heads are singular, the stacked product is generically invertible but unconstrained, and the group-valued objects are $e^{OT}$ and $I+OT$. Receiver inference and latent links moved to the supplement.

The October 7 peer review and revision of the manuscript is [[dennis-2026-glk-attention-v2-review-2026-10-07]].

A tied variant with $S_K=T$ and a Bayesian receiver, in which the receiving map and the residual follow from conditioning, is a separate note, [[dennis-2026-minimal-agent-model]], and is not part of the paper.

## Edge-dependent and latent content links, October 6, 2026

[[dennis-2026-edge-latent-links]] (working note, drafted by Claude Opus 5.5, describing code merged in VFE_3.0 PR #50) replaces the shared link $e^{L}$ by $G_{ij}=g_ie^{L}E_{ij}$ with a rank-$r$ edge factor read from normalized states. The curved mode $E_{ij}=\exp(A_iB_j^\top)$ gives triangle holonomies that vary between triangles; the pure-gauge control $G_{ij}=g_ie^{L}g_j^{-1}$ keeps every holonomy in the class of $e^{L}$. Both start exactly at the exponential chart. A latent extension infers the receiver factor per context (the only factor that can be inferred causally) by damped natural-gradient steps on the floor-free predictive-covariance trace plus an anchored prior and an optional depth-loop prior in which the shared generators cancel. No training result is reported for these arms.

## Lie-algebra links in the main manuscript, October 4, 2026

[[dennis-2026-glk-lie-algebra-links-v2]] (revision drafted by Claude Opus 5.5, float64 identity checks, no cross-model review) carries Option A into the main GL(K) manuscript. The link $\Theta_{ij}=U_i\exp(X_{ij})U_j^{-1}$ is the primary communication object; the frames dress the generator, so $X_{ij}$ is reference data that changes only by the adjoint action under a common reference change. For the stored value and output maps, $\exp(OT)=I+O\varphi_1(TO)T$ splits the link into the flat identification and a channel term whose first-order part is the projected matrix link, and on the principal-logarithm domain the linear and exponential links are an exact change of coordinates rather than a truncation. With routing outside the exponent and tiled heads, the message resums into the receiving map $\widetilde O=e^{OT}T^{-1}=T^{-1}+O\varphi_1(TO)$: order zero is a head-routed flat transport, order one the standard value path, order two cross-head mixing. The implemented `content_link_chart` options are $\widetilde O=O$ (affine), $T^{-1}+O$ (first order) and $e^{OT}T^{-1}$ (exponential), which represent the same tiled mean maps up to the real-logarithm domain. Read as evidence, the same channels give the closed-form channel-likelihood receiver of [[Projected gradient attention]], a Gaussian power posterior.

## Latent link generators, October 3, 2026

[[dennis-2026-dynamic-links]] (agent-drafted derivation note, float64 checks at $K\le4$, nothing trained) promotes the exponential link generators $X_{ij}$ to latent variables, inferred per context together with the token states and routing labels, with a normalized prior made of an anchor $\|X-\bar X\|^2/2\sigma^2$ and a Frobenius-defect curvature energy on the loops of a depth-by-token lattice. The transport term of its free energy is exactly $\mathrm{KL}(q(\zeta')\|\mathcal N(\bar m,\bar Q))+\tfrac12\operatorname{tr}(\bar Q^{-1}V)$, with $V$ the moment-matched predictive covariance already implemented. The link field equation is driven by a delta-rule current, a precision-weighted prediction error times the source state. Without the anchor the per-context optimum is a rank-one transport outside the exponential chart, so the anchor is necessary. Stationary generators can still exist at critical points of the exponential map, and the chart infimum is approached at the rank-one transport only when $\xi_j^\top C_j^{-1}\xi'\ge0$; otherwise it lies strictly above it (corrected October 4, [[multiagentelbo-2026-10-04-lie-algebra-links]]). The implemented `content_link_chart="exponential"` is the zero-temperature limit with $\bar X=OT$, so dynamic links are fluctuations around the current model; they are not implemented.

[[multiagentelbo-2026-10-04-lie-algebra-links]] carries the same exponential chart into the multi-agent theory. Each edge there has a latent generator $\mathring\omega_e$ with link $U_i\exp(\mathring\omega_e)U_j^{-1}$, a Gaussian base prior with an anchor, and a loop-defect curvature action. The transformer's static chart is the zero-width limit of that model. The theory proves the per-context results in general form: a delta-rule current in the link field equation, a degenerate link problem without the prior, first-order natural-gradient inference whose Euler step is the Bayesian learning rule, and an induced Wilson-type action only for jointly normalized undirected matter. None of it is implemented in `vfe3`.

## Unified companion and primary group-valued direction, October 3, 2026

[[dennis-2026-attention-unified]] consolidates the six Attention notes into one standalone manuscript. The author selected Option A, $\Theta_{ij}=U_i e^{X_{ij}}U_j^{-1}$, as the primary construction for later integration; compression and the current head sum remain supporting bridges. The existing GL(K) manuscripts are unchanged. The companion relates the predictive moment theorem, the receiver energies, template inference, and frame optimization to the main paper and its gradient, supplementary, and nonlinear extensions.

> [!warning] Scope corrections to the October 2 summaries
> The unified derivations qualify [[dennis-2026-link-origin]] and [[dennis-2026-link-curvature]]: a constant nonidentity exponential link is nonflat, without a defined claim of maximal curvature; affine/exponential equivalence requires a real-logarithm domain; complement persistence is an additional assumption; and the Gaussian orbit Fisher has stabilizer null directions. Inverse-edge triangle holonomy is possible on causal support even though forward causal walks have no nontrivial cycles. A frozen expected-log-likelihood receiver update is distinct from a mixture of separately normalized label-conditioned posteriors.

The October 3 launcher selects moment-matched covariance, diagonal storage, and AdamW frames. Statements below about an evaluated passthrough/full-covariance route retain their historical scope. Current template routing remains a local-coordinate mean readout; no whole-stack GL(K) covariance or common population-ELBO descent follows from component identities.

The program studies Gaussian routing and predictive communication between locally framed agents. The current manuscript is *Gauge-Covariant Gaussian Attention and Predictive Communication*; the immutable [[gl-k-attention]] note records an earlier version. [[dennis-2026-glk-matrix-links-2026-09-20]] records the September matrix-link revision.

## Retained routes and the gradient receiver, October 2, 2026

The VFE_3.0 implementation now executes only the two projected routes, [[Projected predictive attention]] and [[Projected gradient attention]]; transported attention through the flat identification $\Omega_{ij}=U_iU_j^{-1}$, which the historical sections below describe, is retired, and the structure groups are `block_glk` and `so_n` (`VFE_3.0/docs/2026-10-02.md`). [[dennis-2026-projected-gradient]] supplies the gradient route's receiver: under cut routing (source labels inferred from the comparison record only), a channel likelihood that compares the receiver's measurement $O_h^\top x$ with the sender's message $T_h\bar\xi_j$ in the value space counts the receiver entropy once and has the tempered Gaussian posterior as its exact minimizer. The gauge-equivariance report figure now tests the projected score, routing, readout and receiver under a random passive frame action, with float64 residuals about $10^{-13}$. A design record behind [[dennis-2026-phi-natgrad]] shows that the complete gauge-invariant content of the link field is the simultaneous similarity class of the content maps $M_h=O_hT_h$ (given self-links), so the frames carry no invariant information of their own.

## Group-valued origin of the matrix links, October 2, 2026

[[dennis-2026-link-origin]] asks where the singular links $L_{ij}^{(h)}=U_iO_hT_hU_j^{-1}$ come from. As exponential link $U_i\exp(O_hT_h)U_j^{-1}=\Omega_{ij}+U_iO_h\varphi(T_hO_h)T_hU_j^{-1}$, $L$ is the first-order term and the non-communicating part is the identity on $\ker T_h$. As compression of a primitive link, it is the communicating block of a Levi (parabolic) factorization with a hidden Schur complement. As head sum, $\sum_h\beta^{(h)}_{ij}L^{(h)}_{ij}=U_iOB_{ij}TU_j^{-1}$ is generically a $\mathrm{GL}(K)$ element and with trivial frames is exactly the standard multi-head value path $\sum_jW_OB_{ij}W_Vx_j$. The note ranks the constructions A (exponential) > B (compression) > C (head sum) by principledness and C > A > B by closeness to standard attention. For the attention residual, the exponential construction with the receiver carrying the unsent complement gives a residual only on directions that no head writes, and none when the heads tile the fiber ($K=Hd$, as the code requires); the code's additive $r=1$ residual matches neither this nor the Gaussian-fusion residual $\alpha/(\alpha+\lambda)$ of the gradient receiver, and is the ResNet optimization device. In the tiled case the exponential construction adds no expressive power over the head sum with receiving maps $OE_{:,h}$. Identities were checked numerically at small dimension; nothing was trained. See [[Lattice gauge theory]] and [[Holonomy]].

## Edge-dependent links and curvature, October 2, 2026

[[dennis-2026-link-curvature]] asks what an edge-dependent generator can add to the exponential link of [[dennis-2026-link-origin]]. The answer it gives is curvature: the triangle holonomy $F_{ijk}=U_k(G_{ik}^{-1}G_{ij}G_{jk})U_k^{-1}$ is the frame-independent content of the link field, a constant generator is maximally curved, positional links are flat, and the head-sum link has the multiplicative routing defect $\beta_{ij}\beta_{jk}/\beta_{ik}$ (flat only for $\beta_{ij}=c_i/c_j$). A principled non-positional edge-dependent link is the regression link of a joint Gaussian, whose curvature is the partial cross-covariance and whose rank-$d$ optimum is reduced-rank regression, a second-order-statistics reading of the low-rank channel $OT$ (identification of the learned $(O,T)$ with it is a hypothesis, not a result; see [[Canonical Correlation Analysis]]). The regression link needs cross-covariances that vanish in the mean-field family. The same note gives the Fisher metric of a link acting on a Gaussian belief, shows that the singular boundary of $\mathrm{GL}(K)$ is at infinite Fisher distance, and contrasts additive affine updates (which can cross $\det=0$ in one step) with multiplicative group updates (which cannot); see [[Natural gradient]]. Agent-drafted, float64 checks at $K=4$, nothing trained, no claim about perplexity ([[Holonomy]], [[Lattice gauge theory]]).

## Moment-matched predictive covariance, September 27, 2026

On the [[Projected predictive attention|projected predictive route]] the evaluated model passes the covariance through, so $\Sigma$ stays the encoded token-type lookup at every depth. The v2 exact-status theorem already gives the moment-matched covariance of the predictive kernel; it is now implemented as the opt-in `predictive_covariance="moment_matched"`, with cross-head terms, between-source spread, residual persistence and self-edge terms, and a covariant reference floor $\epsilon(\mathrm{Tr}\,C_i/K)I$ ([[dennis-2026-projected-predictive]]). It is positive definite, obeys the passive law $\Sigma_i^+\mapsto g_i\Sigma_i^+g_i^\top$, and depends on context through the spread of the attended sources. Tests match a brute-force enumeration of the kernel; no training run uses it yet.

## Positioning in the v2 revision, September 23, 2026

The v2 revision, *Gauge-Covariant Gaussian Attention through Projected Matrix Links* (`manuscripts/Attention/GL(K)_attention_v2.tex`), adds citations that fix what the construction does and does not claim. The learned frames $U_i$ are a local dressing field in the sense of [[fournel-2014-gauge-invariant-composite-fields]], and the reference moments $(\xi_i,C_i)$ are the dressed variables. By criterion (C1) of [[francois-2019-artificial-gauge-symmetries]] the passive $\mathrm{GL}(K)$ covariance is therefore artificial, the kind of covariance Kretschmann objected to ([[norton-1993-general-covariance]]). The frames fix an $\{e\}$-structure ([[weiler-2021-coordinate-independent-cnns]]), and the covariance constrains none of $S_Q$, $S_K$, $T$, $O$. See [[Dressing field method]].

The Section 4 shared-covariance reduction and its compensating prior have a point-query precedent in [[movellan-2020-probabilistic-transformers]]: the independent content law (Eq. 7), the mixture-mean readout (Eq. 14), and the key-norm-linked prior (Eq. 16 with Eqs. 20–21). The same reading appears in [[gabbur-2021-probabilistic-attention]] and, as mixture responsibilities, in [[nguyen-2022-probabilistic-attention-keys]]. The isotropic case of the reduction is L2 self-attention ([[kim-2021-lipschitz-self-attention]]), so L2 attention rather than dot-product attention is the natural transformer limit of Gaussian-KL routing. The Gaussian token prior bank has its precedent in the KL-scored Gaussian word embeddings of [[vilnis-2015-gaussian-embeddings]].

Entropy-regularized Gibbs routing has attention-specific precedents in [[niculae-2017-regularized-attention]] and [[litman-2025-entropic-optimal-transport-attention]]. The Section 2.6 row objective with a KL divergence to a prior is Proposition 3.1 of the concurrent [[litman-2026-attention-priors]], whose learned prior has the function class of term (d) of [[dai2019transformerxl]]. The Section 2.6.1 positional priors follow [[bianchessi-2026-bayesian-attention-mechanism]], where NoPE and ALiBi are uniform and Laplace priors.

A binary compatibility record with $P(o=1\mid J=j)=\exp(-D_{ij}/\tau)$ is a valid probability because $D_{ij}\ge0$. Conditioning on $o=1$ makes Gibbs routing the exact source-label posterior at every temperature. This is the optimality-variable device of [[levine-2018-control-as-inference]] (Section 2.2, Eq. 3) and [[toussaint-storkey-2006-probabilistic-inference-mdp]]. In [[kappen-2012-optimal-control-inference]] the Boltzmann optimum has cost $-\log Z$, which parallels the minimum routing free energy $-\tau\log Z_i$.

A remark in Section 5.2 of the revision contrasts this with noisy-query routing. There the projected query mean is treated as a noisy measurement, with noise covariance $V_{Q,i}$, of a draw from the key law. The exact source posterior is then $\beta_{ij}\propto\pi_{ij}\mathcal N(a_i;b_j,V_{Q,i}+V_{K,j})$, the expected likelihood kernel of [[jebara-2004-probability-product-kernels]]. Gibbs routing does not flatten when the query is uncertain, but this rule does: with shared key covariance it is whitened L2 routing with $V_*$ replaced by $V_{Q,i}+V_*$. It has the same frame covariance and comparison-map redundancy as Gibbs routing. The evaluated model does not implement it.

The comparison cospan $E_i\to H^{\mathrm{cmp}}\leftarrow E_j$ is a pair of restriction maps into an edge stalk, so cellular sheaves ([[hansen-2018-toward-a-spectral-theory-of-cellular-sheaves]], [[bodnar-2022-neural-sheaf-diffusion]]) are a closer counterpart than [[Lattice gauge theory]]. The comparison maps carry a cogredient $\mathrm{GL}(r_h)$ redundancy, under which gradient flow conserves $S_QS_Q^\top+S_KS_K^\top$ ([[kunin-2021-neural-mechanics]]); the content maps have the balance invariant $T_hT_h^\top-O_h^\top O_h$ ([[du-2018-balanced-layers]]). The revision reports that AdamW without weight decay drifted along this orbit in the reported run, so raw conditioning diagnostics depend on the basis, and that AdamW's decoupled weight decay ([[loshchilov-hutter-2019-adamw]]) on the stored log-variances drove the variances from 15 to about 1.045. [[das-2019-tarmac]] is cited as the precedent for reading tokens as communicating agents. The experiment's components are cited to [[merity2017-pointer-sentinel]] (WikiText-103), [[hendrycks2016gaussian]] (GELU), [[ba-2016-layer-normalization]] (LayerNorm), and AdamW, and the locator for the Rényi-divergence invariance is [[vanerven-2014-renyi-kl]] (Theorem 9, data processing for every order; Theorem 28, additivity).

## Selective interfaces and collective formation, September 20, 2026

[[multiagentelbo-2026-selective-communication-formation]] applies the existing communication construction to the multi-agent formation question. Comparison maps $S_Q,S_K$ determine routing observables, while $T$ and $O$ select transmitted content and receiving directions. A small comparison KL permits private disagreement; distinct role maps do not even compare a common measurement. Independent invertible interaction links remain separate from local processing through $\mathcal L_e=F_i\rho(\Theta_e)$.

The proposed collective coordinates comprise a shared interface together with the private states or conditional laws required by the parent. Complete-law formation bounds, a Markov blanket and autonomous reduced dynamics do not follow from low-rank communication alone. This is a source-based connection and a proposed extension, with no new formation theorem or population-VFE descent claim for the predictive residual. See [[Meta-agents and hierarchical emergence]] and [[Markov blanket interpretation debate]].

## Predictive communication and matrix links, September 20, 2026

[[dennis-2026-glk-matrix-links-2026-09-20]] records the current full-Gaussian construction. At fixed layer, independent comparison maps act on $\xi_i=U_i^{-1}\mu_i$ and $C_i=U_i^{-1}\Sigma_iU_i^{-\top}$. Their projected Gaussian KL determines routing; separate content maps give

$$L_{ij}^{(h)}=U_iO_hT_hU_j^{-1},\qquad
\mathcal C_{ij}=\sum_h\beta_{ij}^{(h)}L_{ij}^{(h)},\qquad
m_i=\sum_j\mathcal C_{ij}\mu_j.$$

Under independent passive site changes, with all moments and frames transformed consistently, $L_{ij}'=g_iL_{ij}g_j^{-1}$ and $m_i'=g_im_i$. This concerns unrestricted full Gaussian covariances. The diagonal implementation and fixed-coordinate normalization, MLP, and decoder do not establish whole-stack GL(K) equivariance.

A head may be rank deficient while the routed sum is full rank. Attention heads describe communication channels and need not coincide with frame blocks. Sending and receiving subspaces may overlap; the maps also specify gains and correspondence. The frame transport $\Omega_{ij}=U_iU_j^{-1}$ remains flat, while the communication links need not obey its composition law. See [[Lattice gauge theory]] and [[Holonomy]] for the precise loop and path scope.

The matrix-link algebra is established by the displayed factorization. It does not select an invariant action, a normalized population model, or an MLP theory. The user has left the MLP interpretation open. Earlier sections below describe historical constructions and their dated evidence; they are not a specification of the September predictive-content architecture. In particular, the older identification of heads with gauge blocks should not be carried over to this full-width, independently parameterized layer construction. [[dennis-2026-glk-matrix-links-2026-09-20]]

## Setup: tokens as Gaussian agents on a bundle

Fix a feature dimension $K$. Each token $i$ carries a belief $q_i=\mathcal N(\mu_i,\Sigma_i)$
with mean $\mu_i\in\mathbb R^K$ and covariance $\Sigma_i$ a **symmetric positive-definite (SPD)**
matrix. The covariance is the *belief geometry*: an agent that is confident along some directions
and uncertain along others is a non-isotropic $\Sigma_i$. These covariances live on the SPD cone
$\mathrm{SPD}(K)$, which is the symmetric space $\mathrm{GL}(K)/O(K)$
([[Symmetric spaces and the SPD cone]]); the affine-invariant Riemannian structure of that cone is
the geometry the program uses to move, average, and compare beliefs
([[SPD-manifold geometry and Riemannian optimization]]).

Over the token base sits a principal $G$-bundle whose fibers are statistical manifolds; the agents
are sections of it ([[Agents as fibre-bundle sections]]). Each token additionally carries a **gauge
frame** $U_i\in\mathrm{GL}(K)$ — a local, invertible change of basis for the $K$-dimensional
feature space. In the manuscript's real exponential chart the frames are generated from
$\phi_i\in\mathfrak{gl}(K)$ as $U_i=\exp(\phi_i)$. This chart reaches only
$\operatorname{image}(\exp)$, a proper subset of $\mathrm{GL}^+(K)$, even though the ambient
divergence theorem below applies to every invertible frame. The transport that carries token $j$'s
frame into token $i$'s frame is the composition

$$\Omega_{ij} \;=\; \exp(\phi_i)\,\exp(-\phi_j)\;=\;U_i U_j^{-1}\in\mathrm{GL}(K).$$

This $\Omega_{ij}$ is the bundle's discrete analogue of [[Parallel transport]]: it is the object
applied to a neighbor's belief before that belief is compared to one's own. The full-Gaussian
pushforward is exact under common $\mathrm{GL}(K)$ changes of frame. The live diagonal covariance
family is closed exactly only under monomial transports; a general congruence leaves that family and
therefore requires projection or approximation.

## Definition: the congruence-transformed, GL(K)-invariant score

In ordinary dot-product attention the score is the inner product $Q_iK_j^\top$ of a query and a
key ([[vaswani-2017-attention]], [[Attention mechanisms — theory and positional structure]]).
Gauge-equivariant attention replaces this inner product with an **information divergence between
transported beliefs**. The generalized attention weight is

$$\beta_{ij} \;=\; \operatorname{softmax}_j\!\Big(-\,\tfrac1\tau\,
D_{\mathrm{KL}}\!\big[\,q_i \,\big\|\, \Omega_{ij}\,q_j\,\big]\Big),$$

where $\Omega_{ij}q_j$ denotes the pushforward of the neighbor's Gaussian under the transport map,
$\tau$ is a temperature, and the softmax normalizes over candidate sources $j$. This rule is not
posited — it is **derived** from the variational free energy of a mixture-of-sources generative
model in which agent $i$ infers which neighbor generated its state; the KL term arises exactly and
the softmax is the closed-form (KKT) solution of the constrained optimization over the categorical
source-selection posterior ([[gl-k-attention]]).

Two geometric facts make this well posed and frame-independent.

**Congruence on covariances.** A frame change $G\in\mathrm{GL}(K)$ acts on a covariance not by
similarity but by the **congruence (sandwich) action** $\Sigma\mapsto G\,\Sigma\,G^\top$. This is
the action under which the SPD cone is the orbit of the identity and $O(K)$ the stabilizer, i.e.
the very action that realizes $\mathrm{SPD}(K)=\mathrm{GL}(K)/O(K)$
([[Symmetric spaces and the SPD cone]], [[pennec-2006-affine-invariant-tensor]],
[[bhatia-2007-positive-definite-matrices]]). Transporting a neighbor's belief therefore sends
$\mu_j\mapsto\Omega_{ij}\mu_j$ and $\Sigma_j\mapsto\Omega_{ij}\Sigma_j\Omega_{ij}^\top$ — the
congruence keeps a covariance a covariance (Sylvester's law of inertia) and scales its determinant
by $(\det\Omega_{ij})^2$.

**Frame invariance of the score.** The query/key inner product, read through this geometry, becomes
the congruence-transformed quadratic form of the KL between two Gaussians. The key theorem of the
manuscript is that this score is invariant under a *common* gauge change:

> [!important] Theorem (GL(K) gauge invariance)
> For Gaussians $P,Q$ on $\mathbb R^K$ and any $\Omega\in\mathrm{GL}(K)$,
> $$D_{\mathrm{KL}}(\Omega_*P\,\|\,\Omega_*Q)=D_{\mathrm{KL}}(P\,\|\,Q),$$
> because the $(\det\Omega)^2$ Jacobian factors from the two Gaussian normalizations cancel
> identically. The result extends to **all $f$-divergences**, so the transport need only satisfy
> $\det\Omega_{ij}\neq0$ — the full $\mathrm{GL}(K)$ acts as a gauge symmetry of the attention
> scores ([[gl-k-attention]]).

This is the precise sense in which the attention is "gauge-equivariant": the per-token frames
$U_i\in\mathrm{GL}(K)$ are gauge degrees of freedom, and the scores — hence the attention pattern —
are unchanged when every frame is left-multiplied by a common $\mathrm{GL}(K)$ element. The
information-divergence form is what buys this invariance; a raw Euclidean dot product would not be
congruence-invariant. The invariance is the discrete-geometry counterpart of the classical
statement that divergences are coordinate-free on a [[Statistical manifold]]
([[cencov-1982-statistical-decision-rules]], [[amari-2016-information-geometry-applications]]),
specialized here to the linear-frame ($\mathrm{GL}(K)$) reparameterizations the bundle allows.

## Key results

- **Attention is derived, not assumed.** The full KL-plus-softmax rule above follows from a
  multi-agent VFE on a principal bundle with statistical-manifold fibers; the softmax is the KKT
  solution for the source-selection posterior and the KL is exact ([[gl-k-attention]]
  [[Variational free energy]]). What that derivation costs, stated exactly, is settled in
  the MAgent exact-ELBO attention-row derivation (2026-07-27) and summarized in the next section.

- **The shared-frame Regime-I reduction is narrower than standard attention.** The vertex cocycle
  makes loop transport flat but does not force pairwise identity. If one transport is constant on
  every attended edge including a self edge, or on all three edges of a transitive triple, then
  $\Omega_{ij}=I$. With isotropic covariance, the Gaussian KL then gives an identity-bilinear score
  plus a key-norm bias. An arbitrary learned $M=W_QW_K^\top$ is an additional structural map, not a
  transport factor recovered from this limit.

- **Architectural choices can be compared with the geometry.** Approximately constant key norms can
  cancel the key-norm bias in the strict identity-transport reduction, but this is not a derivation of
  LayerNorm or of a general QK metric
  [[Multi-head attention]] is a block-diagonal restriction of the gauge algebra
  $\bigoplus_a\mathfrak{gl}(d_{\mathrm{head}})$; RoPE positional encoding is reinterpreted as
  position-dependent gauge frames; and ALiBi/T5/causal biases are non-uniform attention priors
  $\pi_j$ entering the logits additively as $+\log\pi_j$ ([[gl-k-attention]]
  [[Attention mechanisms — theory and positional structure]]).

- **Covariance fixed point and SPD dynamics.** Minimizing the free energy in $\Sigma_i$ yields the
  matrix precision fixed point
  $\Sigma_i^{-1}=\tfrac12\big[\Sigma_{p,i}^{-1}+\sum_j\beta_{ij}(\Omega_{ij}\Sigma_j\Omega_{ij}^\top)^{-1}\big]$:
  each agent's precision is a $\beta$-weighted blend of its prior precision and its neighbors'
  *transported* precisions — manifest [[Precision weighting]]. Updates to $\Sigma$ are taken as
  natural-gradient steps with an SPD-manifold retraction ([[SPD-manifold geometry and Riemannian optimization]]
  [[Natural gradient]], [[Fisher information metric]]).

- **Flat-bundle (vanishing holonomy) regime.** The gauge transformer's vertex-frame transport
  satisfies the cocycle identity $\Omega_{ij}\Omega_{jk}\Omega_{ki}=I$ as an *algebraic*
  identity, so its Regime-I [[Holonomy]] vanishes. A standard transformer has no transport
  variable or intrinsic holonomy; only the imposed identity-transport comparison point is flat.
  An edge-relaxed extension
  $\Omega_{ij}=\exp(\phi_i)\exp(\delta_{ij}G)\exp(-\phi_j)$ promotes the bundle to non-trivial
  holonomy (Regime II), reserved for the companion participatory program ([[participatory-it-from-bit]]).
  No nonzero Regime-I holonomy exponent exists.

- **Forward-KL uniqueness is conditional.** For a fixed admissible witness, the density-ratio range
  must contain a nonempty open essential interval, or overlapping configurations must identify their
  integration constants. Under that richness condition, closure selects the positive ray
  $f_c(t)=c(t\log t-t+1)$ up to divergence-null affine terms. The convention $f''(1)=1$, or fixed
  exponents and coefficients, sets $c=1$. A diagonal family under general transport does not
  automatically supply the required witness.

- **The nested attention envelope uses optimized costs, not a differentiated product.** For
  $F_i(\beta_i)=\min_{q_i}\{D_{\mathrm{KL}}(q_i\|p_i)+\sum_j\beta_{ij}C_{ij}(q_i)\}$
  the envelope identity is $\partial F_i/\partial\beta_{ij}=C_{ij}(q_i^*(\beta_i))$.
  At fixed $q_i$, the attention-coordinate objective is linear in $\beta_i$ plus its entropy
  regularizer and gives the Gibbs row. After eliminating $q_i$, this becomes an implicit Gibbs
  fixed point. One must not differentiate $\sum_j\beta_{ij}C_{ij}(q_i^*(\beta_i))$ as though it
  were $F_i$.

- **The retained sweep is two-channel and same-scale.** Every archived configuration activates
  `prior_source=model_channel` and `s_e_step=true`. One target-blind $s$ refinement toward a
  learned global, token-uniform $r$ and gamma-weighted model consensus supplies
  $q_i^{(0)}=p_i=s_i^{(1)}$, followed by one target-blind $q$ refinement. Outer cross-entropy
  differentiates through both paths; the inner hyper-prior and gamma terms are not scored again.
  The learned route includes the model tables, $r$, token and learned positional frames, output
  projection and bias, and the active mixer. This does not establish a slower model timescale or
  the full multiscale PIFB hierarchy.

- **Coarse-grained mean dispersion is covariance broadening, not necessarily anisotropy.** The
  law-of-total-covariance contribution $\operatorname{Var}_A(\mu)$ is positive semidefinite and may
  be proportional to the identity. The historical sum of its norm and the block-averaged input
  deviation is only a triangle-inequality upper-bound proxy for the actual block deviation.

- **The isotropic geometric bias measures scale and shape distortion.** The bias vanishes exactly
  for orthogonal transport, but $\Omega=cR$ with $R\in\mathrm{O}(K)$ preserves isotropic shape
  while changing covariance scale and gives nonzero bias unless $c=1$. A nonzero bias therefore
  does not by itself diagnose directional anisotropy.

- **The vacuum/training language is interpretive and stabilizer-dependent.** An observation-free
  divergence sector may have gauge redundancy when its priors are transport-compatible. A fixed
  non-invariant likelihood generally reduces that redundancy to its stabilizer; it does not by
  itself force specialization, unequal Euclidean norms, or a phase transition. Those dynamical
  claims require a declared order parameter and evidence not supplied by the retained sweep.

### Derived from the exact ELBO: what it costs (2026-07-27)

The MAgent exact-ELBO white paper (2026-07-19 continuum-finite remediation record) originally graded the entropy-regularized attention row an *engineered scalar*, because its own
exact row model needs frozen normalized templates and unit temperature, and because a row-local
construction does not define a normalized population joint on shared state variables. Chapter 9 named
a way out — a fixed normalized model carrying a **declared source label** can have an exact ELBO once
compatibility and global normalization are proved — without carrying it out.
The MAgent exact-ELBO attention-row derivation (2026-07-27) carries it out, and the result is that
the rule is derivable **under four stated hypotheses**, three of which the theory does not itself
select.

**The temperature is not free.** A nonunit $\tau$ needs a separately normalized tempered model, whose
normalizer contributes a per-source log-determinant logit:
$$\beta_{ij}^{\star(\tau)}\propto\pi_{ij}\exp\left[-\tfrac1\tau D_{\mathrm{KL}}-\tfrac12\left(1-\tfrac1\tau\right)\left(\log\det\Sigma_j+2\log\lvert\det\Omega_{ij}\rvert\right)\right].$$
For $\tau>1$ this discounts sources whose transported belief occupies more volume, beyond what the KL
says. At the executable's $\tau=\kappa\sqrt K=\sqrt7$ the exact and posited rows differ by **0.069** in
total variation, and by exactly $0$ at $\tau=1$. Because the transport enters only through
$\lvert\det\Omega_{ij}\rvert$, which the $f$-divergence invariance theorem above cancels *inside* the
divergence, this logit is a property of the tempering and not a breach of that invariance.

**The live-peer problem narrows to the covariance channel.** With the label as a genuine latent, the
exact CAVI coordinate for the source posterior reproduces the KL-softmax row **exactly** when the link
noise is tied as $R_{ij}=\Omega_{ij}\Sigma_j\Omega_{ij}^\top$. The sender *mean* is free throughout and
is never replaced by a template — strictly weaker than the frozen-template exception, which freezes
both moments. The sender *covariance* is not, because the tie constrains a generative parameter to
track $\Sigma_j$. Untying it moves the row by up to 0.99992, so the tie is substantive; untied, the
edge energy is a Mahalanobis term in the model's own link metric plus dispersion penalties on both
endpoints.

### The tie is a postulate, and it is the temperature (2026-07-27)

The MAgent exact-ELBO link-covariance-tie record (2026-07-27) grades the tie and merges two
hypotheses that were being tracked separately. The first result supersedes the earlier reading that the
KL form is simply "the specialization" of the untied family.

**The tie and the unit temperature are one hypothesis.** Demand that the offset be source-free *as an
identity in the sender mean*, which is unconstrained and sweeps $\mathbb R^d$ since $\Omega_{ij}$ is
invertible. The coefficient of the quadratic form in $\Delta_{ij}$ is
$\tfrac12(R_{ij}^{-1}-\tau^{-1}S_{ij}^{-1})$, so source-freeness forces $R_{ij}=\tau S_{ij}$; the
surviving term then varies with $\log\det S_{ij}$ at rate $(\tau-1)/(2\tau)$, vanishing only at
$\tau=1$. So $R_{ij}=cS_{ij}$ reproduces the tempered row above *exactly* at $\tau=c$ — the generative
link-covariance scale and the recognition softmax temperature are **the same parameter**, and the two
findings above are one rather than two. A divergence-scored row at nonunit temperature is the exact
coordinate of no model in the family, so the lift does not reach the deployed $\tau=\sqrt7$.

**The tie is not an M-step fixed point.** The unique stationary point in the link covariance is
$R^\star_{ij}=\Sigma_i+S_{ij}+\Delta_{ij}\Delta_{ij}^\top$, so $R^\star-S_{ij}\succ0$ always and the
evidence lower bound forgone per edge is exactly the Stein loss between them. The row prices sources as
though the receiver were already certain and already in agreement.

**A correlated recognition family buys stationarity or the row, never both.** With a jointly Gaussian
pair factor the tie becomes attainable, requiring
$C\Omega^\top+\Omega C^\top=\Sigma_i+\Delta\Delta^\top$ — but that condition fixes the symmetric
combination uniquely and thereby makes the row offset source-dependent. Mean field is the unique member
yielding the row, and the member where the tie is not stationary. This closes the escape route rather
than opening one, and it tells the correlated-VFE track to proceed on its own merits.

> [!important] The tie is a declared postulate, not a derived identity.
> It is a constrained-covariance modeling choice of the Celeux–Govaert kind. The uniqueness result that
> does hold — that $R_{ij}=S_{ij}$ is the only link covariance producing the row — is a statement about
> the target rule, since the model was selected by requiring it.

Two corollaries worth keeping. Tying does **not** make the link reproduce the transported sender: the
predictive covariance is $2S_{ij}$, and the choice reproducing it is $R_{ij}=0$, outside the SPD cone.
And profiling $R$ out instead gives an exact, gauge-invariant, genuinely stationary rule
$\beta_{ij}\propto\pi_{ij}\det(\Sigma_i+S_{ij}+\Delta\Delta^\top)^{-1/2}$ that should still be rejected:
its logit grows like $\log(1+m^2)$ against $m^2/2$, so it cannot select on means, and at $\Delta=0$ it
is Loewner-monotone in $S_{ij}$, ranking sender confidence rather than agreement.

### The Gaussian assumption sits on the link, not the beliefs

The governing statement is that **the M-step reads the recognition family only through the link's
expected sufficient statistic**. A Gaussian link makes $-\log\mathcal N(y_i;\Omega_{ij}y_j,R)$ affine in
$zz^\top$, so that statistic is the residual second moment and nothing above second order can enter.
The M-step gap and its Stein-loss deficit therefore survive for any *product* recognition family with a
mean and a finite nonsingular residual second moment, Gaussian or not — the sharp control being that a
Gaussian with matched first two moments gives the same energy to Monte Carlo noise. The right weakening
of the product hypothesis is $\operatorname{sym}(C\Omega_{ij}^\top)=0$, not independence, which for
$d\geq2$ is strictly weaker than $C=0$.

Non-Gaussian beliefs **cost** the divergence-scored row rather than rescuing the tie. Under the tie the
offset is $H(q_i)+d/2+D_{ij}$, with $D_{ij}$ the m-projection defect of the transported sender against
its own Gaussian moment match, so the row survives exactly when the receiver cannot separate each
source from that match. And among elliptical families closed under linear pushforward, a source-free
gauge-covariant link-covariance rule exists **iff the family is Gaussian**, in which case it is uniquely
the tie. Gaussianity here is forced, not assumed for convenience.

What does carry weight is Gaussianity of the *link*. For an elliptical link the stationarity condition
becomes Maronna's weighted fixed point $R^\star=\mathbb E[w(Q)zz^\top]$, and the tie's necessary scalar
condition is $\mathbb E[\psi(Q_S)]=d$ with $\psi(u)=uw(u)$ — the Gaussian obstruction being exactly
$\psi=\mathrm{id}$. A heavy-tailed generator has $\psi$ bounded and admits a unique $\kappa^\star>1$, so
the tie becomes attainable, though never as an identity, and there the row is a robust score rather
than a Gaussian divergence.

**Normalization forces an ordered mask, and the cocycle is why.** Every one-parent-per-agent assignment
has a cycle, so the augmented product is never a directed factorization unrestricted. Worse, under the
program's own cocycle transport $\Omega_{ij}=U_iU_j^{-1}$ a *reciprocal* pair has a **singular**
assembled precision for every SPD link covariance, with kernel vector $(v,\Omega_{ij}^{-1}v)$: both
link factors express the same agreement relation, so the joint is flat along the gauge-consistent ray
and has infinite mass. A topologically ordered source mask — a causal mask being the canonical case —
restores $Z=1$ identically. Excluding only the self edge does not, since two-cycles survive.

> [!important] The mask is a normalization requirement, not an architectural convenience.
> This is comfortable for the causal language model and uncomfortable for the multi-agent setting,
> where the source relation is bidirectional by design. The bidirectional route is available — adding
> the self-prior anchor (PIFB2's $T_1$) restores positive definiteness — but yields a
> [[Lattice gauge theory|Markov random field]] whose partition function depends on the label
> configuration, so $-\log Z(J)$ enters the label objective and does not separate across receivers
> (measured spread 1.76 nats at $N=3$). There the softmax row is exact only under a further declared
> approximation.

A fourth consequence ties the self term to the row: a distinguished label slot with
$p(y_i\mid j_i=\varnothing)=p_i(y_i)$ contributes $D_{\mathrm{KL}}(q_i\Vert p_i)+H(q_i)$, so the
self-coupling and the peer couplings are competing slots of **one** simplex and folding the self term
inside costs exactly one belief entropy. See [[Multi-agent variational free energy]].

## KL vs Bures: which distortion measures belief distance?

The manuscript's load-bearing distortion is the **KL divergence** between transported Gaussians,
which is asymmetric and is the information-geometric ($\alpha$-connection) object whose invariance
under $\mathrm{GL}(K)$ is proved above. A natural sibling is the **Bures / Bures–Wasserstein
distance** on covariances — the classical shadow of the quantum Bures metric, which is the *smallest*
monotone (quantum-Fisher) metric and is generated by Uhlmann fidelity
([[Quantum information geometry]]). The two are not interchangeable: KL is the relative-entropy
distortion that yields the closed-form Gibbs/softmax update and the $f$-divergence invariance
theorem, whereas the Bures geometry is the transport-optimal (Wasserstein) one. The
affine-invariant SPD metric the program actually uses for $\Sigma$-updates,
$\langle A,B\rangle_\Sigma=\operatorname{tr}(\Sigma^{-1}A\Sigma^{-1}B)$, is a *third* choice,
congruence-invariant by construction ([[Symmetric spaces and the SPD cone]],
[[pennec-2006-affine-invariant-tensor]]).

> [!note] Editorial: The manuscript's invariance results are stated and proved for KL and the full
> $f$-divergence class; it does not derive the attention rule from a Bures distortion. Reading the
> belief geometry "via KL/Bures distortion" should therefore be understood as: KL supplies the
> derived attention scores and their $\mathrm{GL}(K)$ invariance, while Bures and the affine-invariant
> metric are the neighboring SPD geometries that make the covariance side of the construction
> well-posed. A Bures-distortion variant of the score is a plausible but currently *unproven*
> alternative, and the quantum-metric non-uniqueness ([[petz-1996-monotone-metrics]],
> [[Quantum information geometry]]) is exactly why one cannot assume KL and Bures coincide off the
> commuting case.

## Relation to prior gauge / equivariant / SPD-attention work

The construction sits downstream of the geometric-deep-learning program, which organizes neural
architectures by the symmetry groups they respect ([[bronstein-2021-geometric-deep-learning]],
[[Gauge equivariance and geometric deep learning]], [[Group equivariance]]). Gauge-equivariant CNNs
make convolutions covariant under local frame changes on a manifold ([[cohen-2019-gauge-cnn]],
[[Gauge equivariant CNN]]); GL(K) attention is the attention-mechanism analogue, with the divergence
replacing the steerable kernel. The closest attention-specific prior art is Riemannian self-attention
on the SPD manifold ([[wang-2023-riemannian-self-attention-spd]]), which the manuscript review flags
as the nearest neighbor. The "attention is variational inference" reading also connects to the
kernel/linear-attention lineage ([[tsai-2019-kernel-attention]]) and to the free-energy-principle
literature it operationalizes ([[Free-energy principle active inference]], [[parr-2022-active-inference]],
[[Variational free energy and predictive coding]]). The most direct conceptual precursor — that
approximate Bayesian inference *is itself* a gauge theory — is
[[sengupta2017gauge|sengupta-friston-2017-bayesian-gauge-theory]] (with [[sengupta-2016-neuronal-gauge|sengupta-2016-neuronal-gauge-theory]]);
the manuscript's bibliographic review identified these as the prior art it must position against.

## Relevance to this research

This is the attention-mechanism cornerstone of the gauge-theoretic VFE program. It is the page that
ties together the program's three pillars: the **gauge** scaffold (frames $U_i\in\mathrm{GL}(K)$,
transport $\Omega_{ij}$, [[Holonomy]], [[Gauge transformation]]); the **information geometry**
(KL distortion, [[Fisher information metric]], [[Natural gradient]],
[[Information geometry and natural gradient]]); and the **belief geometry** (SPD covariances on
$\mathrm{GL}(K)/O(K)$, [[Symmetric spaces and the SPD cone]]). It anchors the
[[VFE Transformer Program]] and feeds the [[Gauge-Theoretic Multi-Agent VFE Model]], where the same
transported-belief machinery drives meta-agent coarse-graining and the
[[Renormalization group flow]] / [[Meta-agents and hierarchical emergence]] thread.
The construction derives its own KL-softmax attention rule rather than positing it. Its strict
shared-frame, isotropic limit yields an identity-bilinear score plus a key-norm bias; a general
transformer compatibility $W_QW_K^\top$ and value map remain structural additions. It is therefore
the formal pivot for a scoped comparison with transformer attention, not a theorem that arbitrary
transformer attention is an exact special case.

## Related

[[GL(K) gauge group]] · [[Symmetric spaces and the SPD cone]] ·
[[SPD-manifold geometry and Riemannian optimization]] ·
[[Attention mechanisms — theory and positional structure]] · [[Multi-head attention]] ·
[[Variational free energy]] · [[Free-energy principle active inference]] · [[Precision weighting]] ·
[[Fisher information metric]] · [[Natural gradient]] · [[Holonomy]] · [[Parallel transport]] ·
[[Gauge transformation]] · [[Agents as fibre-bundle sections]] · [[Group equivariance]] ·
[[Gauge equivariant CNN]] · [[Gauge equivariance and geometric deep learning]] ·
[[Quantum information geometry]] · [[Statistical manifold]] · [[Dressing field method]]

## Sources

October 6, 2026 objective-derived transformers: [[yang-2022-transformers-optimization-perspective]] · [[hoover-2023-energy-transformer]] · [[yu-2023-white-box-transformers-sparse-rate-reduction]] · [[ramsauer2021hopfield]]

October 6, 2026 prior readings: [[barbero-2022-sheaf-attention-networks]] · [[barbero-2022-sheaf-neural-networks-connection-laplacians]] · [[disipio-2025-curved-spacetime-transformers]] · [[favoni-2022-lattice-gauge-equivariant-cnns]]

October 6, 2026 edge and latent links: [[dennis-2026-edge-latent-links]]

October 5, 2026 rework: [[dennis-2026-glk-attention-v2-rework-2026-10-05]] · [[dennis-2026-minimal-agent-model]]

[[dennis-2026-dynamic-links]] · [[dennis-2026-link-curvature]] · [[dennis-2026-link-origin]] · [[gl-k-attention]] · [[vaswani-2017-attention]] · [[bronstein-2021-geometric-deep-learning]] ·
[[cohen-2019-gauge-cnn]] · [[wang-2023-riemannian-self-attention-spd]] ·
[[tsai-2019-kernel-attention]] · [[pennec-2006-affine-invariant-tensor]] ·
[[bhatia-2007-positive-definite-matrices]] · [[amari-2016-information-geometry-applications]] ·
[[cencov-1982-statistical-decision-rules]] · [[petz-1996-monotone-metrics]] ·
[[parr-2022-active-inference]] · [[sengupta2017gauge|sengupta-friston-2017-bayesian-gauge-theory]] ·
[[sengupta-2016-neuronal-gauge|sengupta-2016-neuronal-gauge-theory]] · [[participatory-it-from-bit]]

v2 revision positioning (2026-09-23): [[francois-2019-artificial-gauge-symmetries]] · [[fournel-2014-gauge-invariant-composite-fields]] · [[norton-1993-general-covariance]] · [[weiler-2021-coordinate-independent-cnns]] · [[movellan-2020-probabilistic-transformers]] · [[gabbur-2021-probabilistic-attention]] · [[nguyen-2022-probabilistic-attention-keys]] · [[kim-2021-lipschitz-self-attention]] · [[niculae-2017-regularized-attention]] · [[litman-2025-entropic-optimal-transport-attention]] · [[litman-2026-attention-priors]] · [[bianchessi-2026-bayesian-attention-mechanism]] · [[vilnis-2015-gaussian-embeddings]] · [[levine-2018-control-as-inference]] · [[toussaint-storkey-2006-probabilistic-inference-mdp]] · [[kappen-2012-optimal-control-inference]] · [[hansen-2018-toward-a-spectral-theory-of-cellular-sheaves]] · [[bodnar-2022-neural-sheaf-diffusion]] · [[kunin-2021-neural-mechanics]] · [[du-2018-balanced-layers]] · [[loshchilov-hutter-2019-adamw]] · [[das-2019-tarmac]] · [[dai2019transformerxl]] · [[vanerven-2014-renyi-kl]] · [[merity2017-pointer-sentinel]] · [[hendrycks2016gaussian]] · [[ba-2016-layer-normalization]] · [[jebara-2004-probability-product-kernels]]
