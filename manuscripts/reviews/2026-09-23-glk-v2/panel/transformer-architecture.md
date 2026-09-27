# Transformer and attention-architecture referee report: GL(K) v2 main manuscript

Panel lens: transformer/attention architecture.
Reviewer model: Claude Opus 5.5 (investigator, not a verifier). Date 2026-09-23.
Targets: GL(K)_attention_v2.tex (1207 lines) and the supplement, read in full; line numbers refer to those bytes.
Scope: Introduction related work (57-73), Sec. 2.3 (361-402), Sec. 2.6.1 (726-792), Sec. 2.7 (796-807), Sec. 3.3-3.4 (926-959), all of Sec. 4 (962-1091), Algorithm 1 (1102-1126), and the experiment discussion (1181-1185).

**Verdict.**
Every Section 4 identity I recomputed is correct as stated (residuals at or below 7e-15), and the stated perturbation bound is valid but loose; the sharp bound is 2 tanh(eps/2).
The consequential problems are readings of the reported model that the manuscript does not state.
In the trained network the explicit attention residual is functionally inert.
The routing covariance is a static (token, position) quantity supplied almost entirely by the frames.
The frames act as token- and position-indexed multiplicative adapters around the neural components and hold 90% of the parameters.
Proposition 4.1 with its compensating prior was published for point queries by Movellan and Gabbur (2020).
None of these is a mathematical error; together they change what the paper can say its experiment and its correspondence show.

**What was executed.**
(i) numpy/scipy/sympy checks of every Section 4 identity, the bound, the variance statements, the rotary relativity identity, and the head-space redundancy (transformer_checks/sec4_checks.py, CPU).
(ii) An independent float64 CPU recomputation of the reported forward pass from the saved final weights: final_model.pt loaded with torch.load(..., weights_only=True, map_location="cpu"), one thread, via C:/anaconda/python.exe.
No vfe3 code was executed; conventions were traced from the vfe3 source.
The recomputation reproduces the run's own logged per-layer diagnostics to four digits (details under F1) and gives next-token cross-entropy 3.782 and 2.851 nats on two passages of 128 and 122 GPT-2 tokens (reported test CE 3.435), so it is a valid probe (transformer_checks/fwd_probe.py, probe2.py, probe3.py).
(iii) Primary-source checks of every citation recommended below.
No GPU work, training, Lean, or tamper checks were run, and nothing outside the panel scratch directory was modified.

## Findings

### F1. The explicit attention residual is numerically inert in the trained model
**Location:** Main 885-889 (eq:relational_predictive_residual), 926-937 (eq:relational_block_composition), 1047-1053 (eq:projected_transformer_residual and "The explicit residual is part of this architecture"), Table tab:fep_nn_correspondence row "Predictive residual" (1085), Abstract 52 ("A causal residual architecture"), 1183 ("Residual and MLP necessity").
**Severity:** high
**Evidence:**
Recomputation from the final weights with the executed conventions: U_i = exp(X_{x_i}) exp(Y_i) per 32x32 block; full-scope S_Q, S_K, T, O per layer; KL bounded to [0, 2048]; tau = sqrt(32); causal ALiBi slopes 2^{-h}; one affine LayerNorm shared across depths with eps = 1e-6; coordinate GELU MLP; covariance passthrough; linear decoder plus unigram log-prior.
Validation against the run's own records: raw minimum singular values of S_Q and S_K per layer are 6.6434/23.7553, 12.3226/31.0635, 12.0475/37.1210, 10.4429/37.5394, identical to metrics_per_layer.csv to four decimals.
The maximum singular value of O_h T_h is 26238.6, 8844.1, 5460.9, 4577.8 (logged 26238.7, 8844.1, 5460.9, 4577.9).
The Frobenius norm of the message over a 128-token sequence is 7.46e5, 7.23e5, 1.08e6, 3.73e5 (logged for a validation sequence: 7.41e5, 7.34e5, 1.09e6, 3.71e5).
On the WikiText-style passage the median per-token ratio of message norm to incoming-state norm is 2.18e4, 5.66e3, 5.41e3, 1.77e3 at layers 0-3, with minimum 789 over all tokens and layers; the second passage gives 2.05e4, 6.48e3, 5.69e3, 2.01e3.
After the shared LayerNorm, the incoming state changes the normalized output u_i by a median relative 1.4e-4, 3.3e-4, 3.6e-4, 7.0e-4 (maximum 1.4e-3).
Deleting the attention residual at all four layers changes the passage cross-entropy from 3.782183 to 3.782066 (second passage: 2.850831 to 2.850710); deleting the message instead raises it to 12.39 (12.07).
The MLP's own skip is active (median ratio of MLP output norm to its input norm 0.97-1.83), and the effective rank of the centered stream rises from about 60 at the embedding to about 85 at the output, so the network is not in the rank-collapse regime of pure attention (Dong et al. 2021).
The logged trajectory shows the regime forming early: the last-layer message norm over 128 tokens is already 1.66e4 at step 1200 (0.5% of training), and the largest singular value of O_h T_h grows from 43 at step 1200 to 4578 at the end, consistent with drift along the approximate scale symmetry that post-addition LayerNorm gives the attention branch.
Under the recorded bf16 autocast, the MLP's linear layers receive inputs rounded at unit roundoff 2^-9 (about 2e-3), which exceeds the state's median relative contribution at layers 0-2; this is an inference from autocast semantics, not a GPU execution.
The brief's L4 premise took weight_norm_mu = 3024.9 as the token-mean table norm.
That field is the quadrature sum over every optimizer group tagged with role mu (vfe3/train.py:859-875), which includes the relational maps.
The token-mean table has Frobenius norm 380.1 (row RMS 1.70; passage median state norm 2.4 at layer 0), so the layer-0 ratio is about four times larger than the brief estimated.
**Fix:** Keep the algebraic identity of Sec. 4.3, but call the correspondence structural and report the trained balance. Proposed insertion at the end of Sec. 5.2:
```latex
In the trained model the explicit attention residual is numerically inert. Over a 128-token passage the message exceeds the incoming state by median factors of $2.2\times10^{4}$, $5.7\times10^{3}$, $5.4\times10^{3}$, and $1.8\times10^{3}$ at layers 0 to 3. After the shared LayerNorm the state contributes a relative change below $1.4\times10^{-3}$, and deleting the residual at every layer changes the passage cross-entropy by $1.2\times10^{-4}$ nats. The residual fixes the form of each layer but not its trained function; token identity reaches later layers through the frames, the self-weight of routing, and the skip around the MLP.
```
Change the Table entry to "Explicit additive term; numerically inert after training in the reported run", and change "A causal residual architecture" in the abstract to "A causal architecture".
For the program, the formalism-native repair is a fusion rule whose self-weight is set by declared precisions or a KL budget rather than by unconstrained content gains (Task 4, item d).
The standard-architecture diagnosis is that post-addition normalization lets training attenuate the identity path in both passes, whereas pre-normalization keeps its gradient path an identity (Xiong et al. 2020); that is a statement about the neural baseline, not a recommendation to add components.
**Falsifies:** A declared evaluation set on which the median ratio is of order one, or on which deleting the residual changes CE by more than about 1e-2 nats; or a convention error in my recomputation, which would have to reproduce the four logged diagnostics to four digits by accident.
**Status:** D as an architectural definition (exact algebra). The abstract, Table tab:fep_nn_correspondence and Sec. 4.3 imply a functioning residual stream; the trained record contradicts that functional reading. Inflated.
**Novelty vs prior review:** new (lead L4, with a corrected premise).

### F2. Routing covariance is a static token-and-position quantity carried by the frames
**Location:** Main 67 ("retain their full reduced covariance"), 937 (covariance passthrough), 977-985, 1009, 1069, 1095, 1134, 1171.
**Severity:** high
**Evidence:**
Code path: the predictive branch returns sigma unchanged (vfe3/inference/e_step.py:834-838); the block MLP uses covariance passthrough; LayerNorm acts on the mean only; e_phi_lr = 0 keeps frames fixed; one shared frame serves both roles (vfe3/gradients/relational.py:33-34).
Hence C_i = U_i^{-1} Sigma_p(x_i) U_i^{-T}, with U_i = exp(X_{x_i}) exp(Y_i), depends only on token type and position at every depth.
In eq:projected_full_kl the covariance-only terms (1/2)[Tr(P_j V_{Q,i}) - r + log det V_{K,j} - log det V_{Q,i}] are therefore a static pair bias B(x_i, i, x_j, j), and P_j = (S_K C_j S_K^T)^{-1} is a static per-key metric; the only contextual term is the Mahalanobis form (a_i - b_j)^T P_j (a_i - b_j).
The trained variance table carries almost no information: log sigma has RMS 0.067 over all 50257 x 256 entries and 99.66% of entries satisfy abs(log sigma) < 0.2 (1st to 99th percentile -0.086 to 0.173).
So Sigma_p is close to the identity, and C_i lies within a median 9.4-10.0% relative Frobenius distance of (U_i^T U_i)^{-1} on both passages.
Within-row logit spread (standard deviation over allowed keys, averaged over rows and heads) of the static covariance terms is 0.45 at layer 0, against 0.28 for the mean term and 2.3 for ALiBi; at layers 1-3 it is 0.05-0.08 against 1.0-2.2 for the mean term.
Replacing the static pair bias by its row mean changes routing by mean total variation 0.15-0.16 at layer 0 and 0.02 at layers 1-3; replacing the per-key metrics P_j by one sequence-shared metric changes routing by 0.11-0.19.
At layer 0 every logit term is a static function of tokens and positions, as in any first attention layer; the distinction matters from layer 1 on.
The key-only terms -(1/2 tau)[log det V_{K,j} + b_j^T P_j b_j] are intrinsic key biases.
Gu et al. (ICLR 2025) report that an attention sink "acts more like key biases, storing extra attention scores", and Litman and Guo (arXiv:2601.15380) add an explicit key-only logit bias to absorb sink mass; the Gaussian router has such a bias built in.
The trained model shows no position-0 sink: mean mass on position 0 is at most 0.043 for rows 64 onward in every head and layer.
**Fix:** State in Sec. 3.3 and Sec. 5 that covariance in the evaluated model is a static function of token type and position, that its routing contribution is a static pair bias plus a per-key metric, and that the learned variances collapsed to near unity so the frames supply the covariance. Proposed sentence after line 1134:
```latex
Because covariances and frames are fixed through the stack, $C_i=U_i^{-1}\Sigma_{p}(x_i)U_i^{-\top}$ depends only on token type and position. The covariance-dependent part of $D_{ij}$ is then a static pair bias and $P_j$ a static per-key metric. The trained variance table is close to the identity ($|\log\sigma|<0.2$ for 99.7\% of entries), so $C_i$ lies within about $10\%$ of $(U_i^{\top}U_i)^{-1}$ and the covariance channel of the router is carried by the frames.
```
Redesign the mean-only control of line 1183 so it can separate uncertainty-aware routing from extra static parameters: include mean-only routing plus a learned per-key metric and a static (token, position) pair bias of matched size.
**Falsifies:** A checkpoint whose variance table is materially non-unit, or an implementation that propagates covariance across layers; either would make the covariance terms contextual.
**Status:** The manuscript correctly calls covariance a routing state rather than propagated uncertainty (D, scope-correct). The phrases "retain their full reduced covariance" and covariance-aware routing invite an uncertainty reading that the trained record does not support. Inflated in interpretation.
**Novelty vs prior review:** extends C7 with new evidence (variance collapse, static pair-bias decomposition, frame-determined covariance).

### F3. Proposition 4.1 and the compensating prior repeat Movellan and Gabbur (2020); the Introduction cites a distant precedent instead
**Location:** Main 67 (Pro-Attention sentence), 987-1020 (prop:projected_dot_product, eq:projected_key_bias_compensation), 1169; references.bib.
**Severity:** high (positioning of the central Section 4 result)
**Evidence:**
Movellan and Gabbur (arXiv:2010.15583) write Gaussian-mixture responsibilities with terms -(alpha_j/2) times the squared distance between query and key mean (their Eqs. 14-15), remove the key norm with a prior pi_ij proportional to exp(alpha times the squared key norm over 2) (Eqs. 16-17), and recover dot-product attention (Eqs. 20-21).
That is the manuscript's compensating prior eq:projected_key_bias_compensation, for point queries.
Nguyen et al. (ICML 2022, PMLR 162:16595-16621) give the same mixture reduction under equal variances and normalized keys (Sec. 2.1, Eqs. 3-4; already R7).
Gabbur, Bilkhu and Movellan (NeurIPS 2021) show that dot-product attention is a special case of MAP inference and adapt keys and values by EM.
Kim, Papamakarios and Mnih (ICML 2021, PMLR 139:5562-5571) define L2 self-attention, P_ij proportional to exp(-(squared distance between x_i^T W^Q and x_j^T W^K)/sqrt(D/H)), which is the isotropic shared-covariance case of Prop. 4.1, and prove it Lipschitz when query and key maps are tied, whereas dot-product attention is not Lipschitz on unbounded inputs.
The new content fits one line using the manuscript's own identity eq:supp_kl_decomposition: D_KL(q|p) = -E_q log p - H(q), and H(q_{Q,i}) is a row constant, so beta_ij = softmax_j(log pi_ij + E_{q_{Q,i}}[log p_{K,j}]/tau), the mean-field responsibility under an uncertain query.
Relative to a point query at a_i this adds -Tr(P_j V_{Q,i})/(2 tau), which depends on the pair when P_j varies, as it does in the trained model (F2).
Pro-Attention (Bae, Cheon and Kim 2022, IEEE Access 10:131192-131201; author list as in Crossref, matching the bib) "regard[s] each component of a token vector as a sample from the probability distribution" of that token, estimates its statistics, and scores pairs by KL at a cost independent of the feature dimension (abstract via Semantic Scholar).
These are per-token scalar statistics, not multivariate projected query and key Gaussians; I could not retrieve the full text to confirm whether a Gaussian family is assumed.
**Fix:** Replace line 67's Pro-Attention sentence by:
```latex
Pro-Attention treats the components of each token vector as samples of a token-specific distribution and scores token pairs by the KL divergence between the estimated distributions \citep{Bae2022ProAttention}. Gaussian-mixture accounts derive softmax routing as mixture responsibilities, including the key-norm term and a prior that cancels it \citep{Movellan2020ProbabilisticTransformers,Gabbur2021ProbabilisticAttention,Nguyen2022MGK}, and L2 self-attention retains the same key-norm term \citep{Kim2021Lipschitz}.
```
and add after the proof of Prop. 4.1:
```latex
\begin{remark}
Since $D_{\mathrm{KL}}(q\|p)=-\mathbb E_q\log p-H(q)$ and $H(q_{Q,i})$ is constant on row $i$,
\begin{equation}
\beta_{ij}=\softmax_j\bigl(\log\pi_{ij}+\mathbb E_{q_{Q,i}}[\log p_{K,j}]/\tau\bigr),
\end{equation}
the mean-field responsibility of a Gaussian mixture under an uncertain query. For a point query at $a_i$ it is the mixture responsibility of \citet{Movellan2020ProbabilisticTransformers} and \citet{Nguyen2022MGK}, and Eq.~\eqref{eq:projected_key_bias_compensation} is the prior with which \citet[Eqs.~16--21]{Movellan2020ProbabilisticTransformers} recover dot-product attention. The query covariance adds $-\operatorname{Tr}(P_jV_{Q,i})/(2\tau)$, which depends on the pair whenever $P_j$ varies with the source.
\end{remark}
```
**Falsifies:** A reading of Movellan and Gabbur's Eqs. 14-21 in which the prior does not cancel the key norm, or an existing passage crediting that construction.
**Status:** Prop. 4.1 is correct (P; recomputed, residual 4.4e-15). "We establish an exact reduction" is accurate as a derivation but implies novelty for the key-norm bias and its compensation, which the literature already has. Inflated as a contribution.
**Novelty vs prior review:** extends R7 (R7 cited MGK only and described the delta as stating the key-norm bias and a controlled approximation; Movellan and Gabbur already contain the bias and its compensation).

### F4. In the reported model the frames are token- and position-indexed multiplicative adapters around the neural components
**Location:** Main 73 (contribution), 804-807 (prior bank), 1132-1136 (architecture and parameter count), 1169, 1183 (baselines), 1189 (Conclusion: "a lattice-gauge structure at the level of link fields").
**Severity:** high (what the only experiment can be said to show; baseline design)
**Evidence:**
Writing xi_i^(l) = U_i^{-1} mu_i^(l) (reference coordinates, i.e. unitary gauge) turns the executed model into four pieces.
Input: xi_i^(0) = exp(-Y_i) exp(-X_{x_i}) mu_p(x_i), a multiplicative token-position embedding.
Attention: xi_i^att = xi_i + sum_{j,h} beta_ij^(h) O_h T_h xi_j, frame-free given beta, where beta depends on xi and on the static C_i of F2.
Nonlinear block: xi_i^(l+1) = U_i^{-1} G^(l)(U_i xi_i^att) with G = (id + MLP) composed with LayerNorm, so the shared LayerNorm and the MLP are conjugated by a token- and position-specific invertible block matrix.
Readout: W_out mu_i^(L) = W_out U_i xi_i^(L).
Equivalently, in local coordinates each token and position receives its own invertible factor on the query, key, value and output maps: S_Q U_i^{-1}, S_K U_j^{-1}, T_h U_j^{-1}, U_i O_h.
On the recomputed model the token frames are almost entirely token specific (median relative distance of X_x from the passage mean X-bar is 0.987-0.994), moderately conditioned (block condition number median 3.1-3.2, maximum 27-39; singular values 0.24-11.4), and hold 411,705,344 of 456,654,162 parameters in a sparsely accessed table; summary.json reports 18,176,849 active parameters per token.
The positional frames are an absolute learned table clamped beyond position 127 (vfe3/model/positional_phi.py:62-76) with no relative structure: the median relative step between adjacent positions' generators is 1.12.
Known architectural relatives are input-selected transition matrices, where "every character has an associated weight matrix" (Sutskever, Martens and Hinton, ICML 2011, Eqs. 3 and 5); feature-wise conditioning (FiLM, Perez et al. 2018), of which the frames are a full-block generalization indexed by token and position; weights generated by lookup, a degenerate hypernetwork (Ha, Dai and Le 2016); and scaling of input-side lookup tables, which lowers language-model loss at fixed compute (Huang et al., ICML 2025; Yu et al., NeurIPS 2025).
Archived single-seed K = 20 runs on an older one-layer full-Gaussian route point the same way: the MLP applied in reference coordinates (canonical_frame, 132.40 test perplexity) against the frame-conjugated coordinate MLP (121.3-127.9), and an additive use of the same table (per_token_additive, 214.50) against the multiplicative frames (per_token, 132.78). These are suggestive only.
The Conclusion's lattice-gauge sentence describes frame-dressed, attention-weighted output-value products: in reference coordinates the routed link is A_ij = sum_h beta_ij^(h) O_h T_h, the sum of the head OV circuits of Elhage et al. (2021), and its gauge-invariant content, including loop traces, is that of this frame-free algebra.
**Fix:** Add after the covariance proposition, or in Sec. 5.2, a paragraph giving the places the frames enter in reference coordinates, the equivalent local-coordinate adapter reading, and the 90.16% share. Reword the Conclusion:
```latex
Sending and receiving maps factor matrix-valued links on the token graph. In reference coordinates the routed link is $\sum_h\beta_{ij}^{(h)}O_hT_h$, the attention-weighted sum of the head output--value products, and the frames dress it with the endpoint factors $U_i$ and $U_j^{-1}$; its invariant content, including loop traces, is that of this frame-free algebra.
```
Extend the planned frame comparison (1183) to separate structure from lookup capacity: an equal-size table used additively (the existing per_token_additive control); a factorized frame table phi_x = A c_x with small code dimension, in the manner of the factored transition tensor of Sutskever et al.; identity frames with an enlarged input table; and the reference-coordinate MLP (canonical_frame) to measure the capacity contributed by conjugating the MLP.
**Falsifies:** An executed demonstration that the reference-coordinate rewrite changes the logits would refute the identification (it is algebra; the coordinator's residual was 4e-15). Controlled comparisons in which capacity-matched controls without multiplicative frames match the frame model would locate the frames' role in capacity rather than structure, sharpening rather than refuting this reading.
**Status:** The passive-covariance proposition is correct (P). The contribution statement and the Conclusion describe the frames geometrically (D/S) but not their executed functional role, and "a lattice-gauge structure at the level of link fields" is inflated relative to the invariant content.
**Novelty vs prior review:** extends R1 (adds the architectural identification, token-specificity and capacity data, and the lookup-capacity control design).

### F5. The routing perturbation bound is valid but loose, and vacuous on the trained router; the sharp bound is 2 tanh(eps/2)
**Location:** Main eq:projected_bias_error and eq:projected_softmax_bound (1022-1034).
**Severity:** medium
**Evidence:**
For any source set A, the gap beta(A) - p(A) is largest when delta = eps_i on A and delta = -eps_i off A, which gives beta(A) = p(A) e^{2 eps_i} / (p(A) e^{2 eps_i} + 1 - p(A)).
sympy maximizes beta(A) - p(A) over p(A) at p(A) = 1/(e^{eps_i} + 1) with value tanh(eps_i/2).
Hence the L1 distance sum_j abs(beta_ij - p_ij) is at most 2 tanh(eps_i/2), which is at most min(eps_i, 2), with equality for two sources.
In 20,000 random rows neither bound was violated, the ratio of the L1 distance to 2 tanh(eps/2) reached 1.0000, and the stated bound exceeded the actual L1 distance by a median factor of 22.
At eps = 0.7 the two-point L1 distance is 0.67275, equal to 2 tanh(0.35), while e^{1.4} - 1 = 3.055.
The stated bound exceeds the trivial value 2 whenever eps > ln(3)/2, about 0.549.
On the trained model, with the key-norm bias isolated under a sequence-shared key metric, the median eps is 0.38-0.48, 1.05-1.50, 2.15-2.45 and 2.68-3.32 at layers 0-3; the stated bound is vacuous for 98-100% of rows at layers 1-3, the sharp bound has medians 0.38-1.86 and is never violated, and the realized L1 medians are 0.17-0.77.
The variance statements at 1034 are correct: simulated r = 32 gives chi-square variance 64.1 (2r = 64) and independent dot-product variance 32.2 (r = 32); r = 256 gives 515 and 257; after division by 2 sqrt(r) and sqrt(r) the standard deviations are 0.71 and 1.00.
**Fix:** Replace the sentence before eq:projected_softmax_bound and the display by:
```latex
Writing $\beta_{ij}=p_{ij}e^{\delta_{ij}}/\sum_k p_{ik}e^{\delta_{ik}}$ with $|\delta_{ij}|\le\varepsilon_i$, the gap $\beta_i(A)-p_i(A)$ for any source set $A$ is largest when $\delta_{ij}=\varepsilon_i$ on $A$ and $\delta_{ij}=-\varepsilon_i$ off $A$. Maximizing the resulting expression over $p_i(A)$ gives
\begin{equation}
\sum_j|\beta_{ij}-p_{ij}|\le 2\tanh(\varepsilon_i/2)\le\min(\varepsilon_i,2),
\label{eq:projected_softmax_bound}
\end{equation}
with equality for two sources and $p_i(A)=1/(1+e^{\varepsilon_i})$.
```
Keep the ratio bound between e^{-2 eps_i} and e^{2 eps_i} if a multiplicative statement is wanted, and report the measured eps distribution with the sharp bound (prior figure plan F3, panel B).
**Falsifies:** A row whose L1 distance exceeds 2 tanh(eps/2); none was found analytically, in 20,000 random rows, or in about 1,000 trained rows.
**Status:** P (the stated bound is valid); its presentation as the operative control is weakened by its looseness.
**Novelty vs prior review:** new (L7 confirmed); it also updates the prior figure plan, whose F3 panel B plots min(2, e^{2 eps} - 1).

### F6. Heads carry an unstated GL(r_h) x GL(s_h) redundancy, so the reported conditioning diagnostics depend on an arbitrary basis
**Location:** Main 366-402 (Sec. 2.3), Table tab:link_conventions, 1159 (singular values 6.64-12.32; condition numbers 88.7-550.5).
**Severity:** medium
**Evidence:**
For any A in GL(r_h), the map (S_Q, S_K) to (A S_Q, A S_K) is a common invertible pushforward of both comparison laws, so every D_ij is unchanged by eq:glk_invariance (executed residual 3.9e-14; a contragredient change alters D by 5.4e3).
For tied maps the router depends only on the kernel of S, a point of a Grassmannian.
The content pair has (T_h, O_h) to (B T_h, O_h B^{-1}), which leaves O_h T_h fixed.
Under a routing-invariant A the projected-covariance condition number moved from 7.3 to 837 and the minimum singular value of S_Q from 1.94 to 0.92, while the relative spectrum of V_{K,j}^{-1} V_{Q,i} stayed fixed (7.8e-14).
The raw singular values and projected-covariance condition numbers at 1159 are therefore coordinates on the redundancy orbit, not properties of the operator; the singular values of O_h T_h and the relative spectrum are invariant.
parameter_motion.json and the recomputation show comparison-map norms growing 39-54-fold and T, O norms 36-48-fold, consistent with drift along the exact comparison-space scale direction and the approximate content scale direction created by post-addition LayerNorm (F1).
A further consequence: because common scaling of (S_Q, S_K) leaves D invariant, routing cannot sharpen through comparison-map norm growth, unlike the dot-product logit x^T W_Q W_K^T y; sharpness is set by the Mahalanobis geometry of the states and by tau.
**Fix:** In Sec. 2.3 define the comparison and content spaces without a preferred basis and state the redundancy:
```latex
The comparison and content spaces carry no preferred basis. For $A\in\mathrm{GL}(r_h)$ the pair $(S_{Q,h},S_{K,h})\mapsto(AS_{Q,h},AS_{K,h})$ is a common invertible pushforward of both comparison laws, so every $D_{ij}^{(h)}$ is unchanged by Eq.~\eqref{eq:glk_invariance}; for $S_Q=S_K$ the score depends only on $\ker S$. Likewise $(T_h,O_h)\mapsto(BT_h,O_hB^{-1})$ with $B\in\mathrm{GL}(s_h)$ leaves $O_hT_h$ unchanged.
```
In Sec. 5 replace the raw singular values and projected-covariance condition numbers by invariant diagnostics (relative spectrum of V_{K,j}^{-1} V_{Q,i}, principal angles between the row spaces of S_Q and S_K, singular values of O_h T_h), or state that the reported numbers are basis dependent.
**Falsifies:** A term on the evaluated forward path that breaks the common left GL(r_h) action; there is none, although weight decay breaks it in the optimizer, which is why norms equilibrate rather than diverge.
**Status:** Absent from the manuscript; the diagnostics at 1159 are presented as operator properties (E, inflated in meaning).
**Novelty vs prior review:** new (L5 confirmed from the architecture side).

### F7. The rotary section omits that comparison-space rotations make the full Gaussian score exactly relative, and the reported positional mechanism is absolute
**Location:** Main 1055-1067 (Sec. 4.4, eq:projected_rope_kernel), Table tab:fep_nn_correspondence row "RoPE score" (1084), 804-807, 1132-1134.
**Severity:** medium
**Evidence:**
Applying eq:glk_invariance with A = R_j^{-1} gives KL((R_i)_* q_{Q,i} | (R_j)_* p_{K,j}) = KL((R_{i-j})_* q_{Q,i} | p_{K,j}) for arbitrary projected covariances, so the rotary Gaussian score depends on position only through i - j.
Executed on random anisotropic covariances, including invariance under a common shift of both positions, the residual is 2.8e-14.
Isotropy is needed only to reduce the score to the dot-product form, not for relative-position dependence.
The evaluated model uses no rotations (pos_rotation = "none"); its positional information is ALiBi plus learned absolute multiplicative frames exp(Y_i) (F4), which are unstructured in position and clamped past 127, so the model gives up the length-extrapolation motivation of ALiBi (Press et al. 2022).
The closest learned relative generalization is LieRE (Ostmeier et al., ICML 2025), which exponentiates dense learned skew-symmetric generators.
**Fix:** Add after eq:projected_rope_kernel:
```latex
Because the rotations act on both comparison laws, Eq.~\eqref{eq:glk_invariance} with $A=R_j^{-1}$ gives
\begin{equation}
D_{\mathrm{KL}}\bigl((R_i)_*q_{Q,i}\|(R_j)_*p_{K,j}\bigr)=D_{\mathrm{KL}}\bigl((R_{i-j})_*q_{Q,i}\|p_{K,j}\bigr)
\end{equation}
for arbitrary projected covariances, so the rotary Gaussian score depends on position only through $i-j$. Isotropy is needed only to reduce this score to the dot-product form.
```
Change the Table entry to "Relative dependence exact for arbitrary projected covariances; dot-product form requires shared isotropic covariance", and state in Sec. 5.2 that positional information enters through ALiBi and absolute learned multiplicative frames.
**Falsifies:** An anisotropic example in which the rotary score depends on i and j separately; none was found.
**Status:** The stated identity is correct (P) but understates what holds; the reported positional mechanism is never described as absolute (omission).
**Novelty vs prior review:** new.

### F8. Section 2.6.1 claims a "unified derivation" that its last paragraph withdraws, and misses the direct precedent
**Location:** Main 726-792; 65 and 720 (citations for entropy-regularized routing).
**Severity:** medium
**Evidence:**
Line 729 says the general solution "provides a unified derivation of several attention masks and positional preferences"; line 792 says the biases are "accommodated ... rather than derived from first principles".
Litman and Guo (arXiv:2601.15380, v2 of 23 August 2026) write attention as the minimizer of -<p, s> + tau KL(p|pi) with solution softmax(s/tau + log pi), treat ALiBi as a prior that "commits every head to a fixed monotone recency prior", and introduce a key-only logit bias for sinks.
Niculae and Blondel (NeurIPS 2017) give softmax(x/gamma) as the gradient of the entropy-smoothed max over the simplex and generalize the regularizer.
The content specific to Sec. 2.6.1 is narrow: the log-prior enters with unit coefficient while the energy is divided by tau, so temperature never rescales positional biases.
Line 732, "Within our generative model", conflicts with the paper's scope discipline; the only generative object here is the local source model eq:mixture_joint.
The causal prior is written pi_j with no receiver index although it depends on i.
Blank lines around the displays at 733-746 create spurious paragraph breaks, and a stray period sits on its own line after the label of eq:causal_prior.
**Fix:** Replace "provides a unified derivation of" by "gives a common parameterization of"; cite Niculae and Blondel at lines 65 and 720 and Litman and Guo at 729 and 792; change "Within our generative model" to "Within the local source model of Eq. (mixture_joint)"; write pi_ij throughout; remove the blank lines around the displays and move the period inside the cases display. The subsection is a candidate for the supplement (prior R2).
**Falsifies:** A derivation in the manuscript that selects a particular positional prior beyond the causal support from its premises; none is present.
**Status:** S presented as D at 729 (inflated), correctly deflated at 792.
**Novelty vs prior review:** new (the precedent and the internal inconsistency); overlaps R2 on placement.

### F9. Prior C2 misdescribes Press et al., but its qualification matters more than it said, because the live run has five heads
**Location:** Main 775, 1109, 1134; prior review C2.
**Severity:** medium if the forthcoming K = 160 result is reported; low otherwise
**Evidence:**
The ALiBi paper states the rule for general head counts: "for n heads, our set of slopes is the geometric sequence that starts at 2^(-8/n) and uses that same value as its ratio" (Press et al. 2022, Sec. 3), with the 8-head schedule 1/2, ..., 1/2^8.
The manuscript's sentence at 775 reports the paper faithfully, so C2's statement that the simple geometric sequence is "the original power-of-two-head rule" is inaccurate about the paper.
The reference code does use a different construction for non-powers of two, and vfe3 follows the code (vfe3/attention_prior.py:25-47).
The live V3_Transformer launcher sets embed_dim = 160 and n_heads = 5 with causal_alibi and alibi_slope = 1 (train_vfe3.py:107-108, 232-235).
For H = 5 the executed slopes are (1/4, 1/16, 1/64, 1/256, 1/2) in head order, whereas 2^{-8h/5} gives (0.330, 0.109, 0.0359, 0.0118, 0.0039).
If that run is reported, lines 775 and 1134 would misstate the executed prior; for H = 8 code and formula agree exactly.
**Fix:** At 775:
```latex
\citet{press2022train} state the geometric schedule $\lambda_h=2^{-8h/H}$; their reference implementation, which we follow, uses it when $H$ is a power of two and otherwise appends alternate slopes of the next power-of-two schedule to the nearest lower one.
```
In the methods for any H = 5 run, list the executed slopes.
**Falsifies:** A launcher or checkpoint for the reported run with a power-of-two head count.
**Status:** The manuscript's sentence is a correct citation; the risk is a future methods mismatch.
**Novelty vs prior review:** disagrees with C2 on its characterization of the paper; extends C2 with the H = 5 evidence.

### F10. Prior C3 is correct; prior C4 is right in outcome, but the constraint it softens is a necessary condition in this architecture
**Location:** Main 749-757, 792; prior review C3, C4.
**Severity:** low
**Evidence:**
C3: Longformer defines a "window size w" in which "each token attends to 1/2 w tokens on each side", and Mistral 7B attends to "positions between i - W and i" with W = 4096. The manuscript's "window of size w" with abs(i - j) at most w (2w + 1 positions) conflicts with both conventions, so C3 is correct.
C4: prefix measurability of p(x_{i+1} given x_{<=i}) requires every layer's support to lie in {0, ..., i}, because every state at every depth depends on its own token (the embedding enters at layer 0 and the frames at every layer).
The constraint pi_ik = 0 for k > i is therefore necessary here, not only sufficient. What the framework does not select is the prior within the prefix (uniform, windowed, ALiBi).
The phrase "the causal mask is the one positional prior the framework does fix" conflates the support constraint with the uniform prior eq:causal_prior.
**Fix:** For C3, use "radius w" and write the causal window as i - w <= j <= i. For C4:
```latex
The autoregressive factorization requires $\pi_{ik}=0$ for $k>i$ at every layer, because each state depends on its own token; within that support any prior, whether uniform, windowed, or ALiBi, is admissible.
```
**Falsifies:** For C4, an architecture in this family whose states at some depth do not depend on their own token, which would permit future positions without leakage.
**Status:** Wording (S).
**Novelty vs prior review:** agrees with C3; agrees with C4's outcome and corrects its rationale.

## Leads tested

**L1: CONFIRMED and sharpened (F4).**
The reference-coordinate rewrite is exact.
In the reported model the frames enter as a multiplicative token-position factorization of the input and covariance tables, and as token- and position-dependent conjugation of the shared LayerNorm, the MLP and the readout.
In local coordinates they are per-token, per-position invertible adapters on the query, key, value and output maps.
They are almost entirely token specific (relative dispersion 0.99), moderately conditioned, and 90.16% of the parameters.
The routed links are frame-dressed, attention-weighted output-value products, so the Conclusion's lattice-gauge sentence overstates their invariant content.

**L3: CONFIRMED and quantified (F2).**
Covariance is static per (token, position).
The variance table collapsed to near unity (RMS log sigma 0.067), so C_i is within about 10% of (U_i^T U_i)^{-1}.
Covariance acts as a static pair bias (large at layer 0, TV 0.15 when removed; small later, TV 0.02) and as a per-key metric (TV 0.11-0.19 against a shared metric).
Its key-only terms are intrinsic key biases, the mechanism attention sinks otherwise emulate; no sink was observed.

**L4: CONFIRMED, stronger than stated, with a corrected premise (F1).**
weight_norm_mu is a role-group aggregate, not the token table.
The actual message-to-state ratio is 2.2e4 at layer 0 and at least 790 everywhere; deleting the residual changes CE by 1.2e-4 nats.
The MLP skip is active and there is no rank collapse.
For design: post-addition LayerNorm with a dominant branch attenuates the identity path in both passes; pre-normalization would keep an identity gradient path (Xiong et al. 2020), and the formalism-native alternative is precision-weighted or budgeted fusion (Task 4, item d).

**L5: CONFIRMED (F6), within my Sec. 2.3 lens.**
Cogredient invariance holds to 3.9e-14; the conditioning diagnostics at 1159 are basis dependent; the observed norm growth is consistent with drift along these directions.

**L7: CONFIRMED (F5).**
The sharp bound is 2 tanh(eps/2), attained by two sources; the stated bound is vacuous on 98-100% of trained rows at layers 1-3.

**L8: CONFIRMED, with ranking (F3, F8, Task 4).**
Highest relevance to this manuscript: Movellan and Gabbur 2020 (identical compensation prior), Litman and Guo 2026 (KL-to-prior attention with ALiBi as a prior and key-only sink biases), Kim, Papamakarios and Mnih 2021 (L2 attention, Lipschitz with tied maps), Nguyen et al. 2022 (already R7), Niculae and Blondel 2017 (entropy-smoothed max).
For the program: Sukhbaatar et al. 2019 and Geva et al. 2021 (Task 4).
Lower: Martins and Astudillo 2016 (a sparse alternative to entropic routing, relevant only if learned hard supports are wanted); Gabbur et al. 2021 (EM adaptation of keys and values, relevant to test-time belief revision).
CRATE is already R7. The Pro-Attention description should be corrected (F3).

**L9: CONFIRMED in my sections.**
m is both the ALiBi slope (eq:alibi_prior) and the routed message m_i (465, 885).
a denotes the projected query mean (973), the head aggregate a_i^(l,h) (884), the ALiBi slope a_h (1109), the reference-basis change a (386), and a path length (568).
b denotes the projected key mean (973), the LayerNorm bias (930), the ALiBi logit bias b_ij^(h) (1109), the relative bias b_delta (783), the MLP biases, and b_out.
P_i is the mixture joint (690) and P_j the key precision (983).
V is the vocabulary size (799), the projected covariances V_{Q,i} and V_{K,j}, and a content variable V = T X_j (902).
Suggested: slope lambda_h, message m_i, head aggregate z_i^(h) (as already used at 1045), key precision Lambda_j.

**L10: MODIFIED.**
Sentences carrying a negation or scope limit are 26% of Sec. 4 (19 of 74) and 25% of the Discussion, but 14% of the Introduction; "dominated" overstates.
The problem is placement: disclaimers are interleaved inside derivations.
A theorem-first Sec. 4 would read: Proposition A (routing is the mean-field responsibility under an uncertain query; shared key covariance gives the biased dot product), Corollary (ordinary attention exactly when key norms are constant on the support, or under the compensating prior), Proposition B (the sharp perturbation bound), Proposition C (the value/output concatenation identity), Proposition D (the rotary Gaussian score is relative for arbitrary covariances), followed by one scope paragraph.

L2 and L6 are outside my lens.

## Prior review C2-C4 check

C2 mischaracterizes Press et al. but its qualification is warranted for a stronger reason (F9).
C3 is correct as stated, verified against Longformer and Mistral 7B (F10).
C4 has the right outcome with an adjusted rationale: the prefix-support constraint is necessary in this architecture, and only the prior within the prefix is left unselected (F10).

## Formalism-native replacements and minimal experiments (Task 4)

The reported model locates part of its capacity in exactly the components the program wants to remove: a coordinate MLP made token specific by frame conjugation (F4), a linear readout, and a post-addition LayerNorm that erased the attention residual (F1).
Each has a replacement built from the paper's own objects (Gaussian laws, Gibbs source selection, content maps, KL), and several can be tested with code that already exists.
One strategic consequence comes first.
If every other component becomes covariant, reference coordinates remove the frames except as a multiplicative factorization of the (token, position) input and covariance tables; they would then carry an inductive bias, not dynamics.
If the program wants frames to be part of an agent's state, they need context dynamics (frames revised by inference, e_phi_lr > 0) or connection data on a graph with cycles, which the causal graph lacks (Sec. 2.4.3, line 607).

**(a) Gibbs routing to a persistent Gaussian template bank in place of the MLP.**
Augment each row's source set with M context-independent sources: key laws N(b_m, W_m) in a head's comparison space, content vectors c_m in its content space, and prior mass omega_m folded into pi.
The layer then solves the same objective eq:relational_routing_objective over S_i together with the templates, and its only nonlinearity is the Gibbs normalization the paper already derives.
Sukhbaatar et al. (2019) concatenate persistent key and value vectors to the context under one softmax, remove the feed-forward layer, and report WikiText-103 test perplexity 20.6 at 133M parameters against 24.0 for Transformer-XL Standard at 151M (their all-attention model uses adaptive span); Geva et al. (2021) show that feed-forward layers operate as key-value memories, which is unnormalized attention over d_ff persistent keys.
Matching the 1,050,880 MLP parameters per layer with diagonal templates (32 mean, 32 variance and 32 content numbers each) gives about 1,370 templates per head.
Reading the templates as a Gaussian mixture prior on states makes the layer one coordinate-ascent step of a declared mixture model; that reading is standard variational EM but has to be written.

**(b) Reliability-weighted routing.**
The project's September 20 construction replaces beta_j proportional to pi_j exp(-delta_j/2) by beta_j proportional to pi_j exp(-w delta_j/2), with inferred reliability w = (nu + d)/(nu + delta) under a Student-t record law.
This is a nonlinear, uncertainty-dependent routing rule obtained from inference rather than from an activation. The conditional theory exists; the implementation is new, and the record law must be chosen.

**(c) Covariance propagation by moment matching.**
Replace passthrough by the routed mixture covariance of line 1069 plus the channel term of eq:main_gaussian_link_marginal, summed over heads: Sigma_i^att = Q_i + sum_j beta_ij [L_ij Sigma_j L_ij^T + (L_ij mu_j - m_i)(L_ij mu_j - m_i)^T].
The covariance terms of D then become contextual, which is the only setting in which covariance-aware routing can mean uncertainty-aware routing (F2). Combined with (a), the whole layer is a Gaussian assumed-density step.
Test: the variation, across contexts, of the covariance-only logit terms for a fixed (token, position), and CE against passthrough at matched parameters.

**(d) Residual as precision-weighted or budgeted fusion.**
Replace "add the message, then LayerNorm" either by the Gaussian fusion mu^+ = (Lambda_i + Lambda_m)^{-1}(Lambda_i mu_i + Lambda_m m_i), which treats the routed message as a noisy observation of the receiver's own state, or by the September 20 budgeted interpolation Q_t proportional to Q_*^t r^{1-t}, with t fixed by a KL budget.
In both, the self-weight is set by declared precisions or by the budget and cannot be erased by growing the content gain, which is the failure mode of F1.
The observation model for messages (what the message observes), or the reference and budget, must be specified.

**(e) Covariant normalization.**
The existing Mahalanobis norm, mu scaled by sqrt(K/(mu^T Sigma^{-1} mu)) (vfe3/geometry/norms.py), is invariant under the site action; a normalization of xi in reference coordinates is the other option. With (d), normalization may be unnecessary, since fused means are bounded by the budget.

**(f) Readout.**
The prior-bank Gibbs readout of Sec. 2.8 exists in code. The September 20 Gaussian latent-utility law is the principled alternative, at a large-vocabulary integration cost.

**(g) Frames: structure or capacity.**
Factorized frames phi_x = A c_x with small code dimension F (the analogue of the factored transition tensor of Sutskever et al. 2011) separate frame structure from table size at fixed geometry.

**Testable now with existing code:** the reference-coordinate MLP (block_mlp_mode = canonical_frame) and the gauge-gate MLP against the coordinate MLP; the Mahalanobis block norm; the prior-bank decoder; the per_token_additive frame-capacity control; identity frames; attention_residual = False (predicted small endpoint effect, F1); mean-only routing with and without a matched static pair bias (F2).
A proportionate protocol is K = 64 or 128, four layers, 30k steps, three paired seeds, the archived 128-token protocol, and per-layer message-to-state ratios logged over training.

**New code, no new theory:** (a) the template bank; (c) moment-matched covariance; (g) factorized frames.

**Needs new theory:** (b) selection of the record law and its sequence-level objective; (d) the message observation model, or the reference and budget; a derivation of depth and composition as coordinate ascent on one declared population objective with a template-bank prior; and the prefix-only sequence likelihood that the variational objective bounds (the first open obligation of the September 20 report).

## Placeholders to add or re-prioritize

The prior plan's F1-F6 and T1-T2 stand, with these changes.

F3, panel B: plot the sharp bound 2 tanh(eps/2) instead of min(2, e^{2 eps} - 1), which is vacuous for 98-100% of trained rows at layers 1-3. Panel C: the per-layer logit decomposition into static covariance terms, the Mahalanobis term and ALiBi (numbers under F2 can seed it).

New F7, high priority, Sec. 5: residual balance. Panel A: median message-to-state ratio per layer over training (metrics.csv logs only the last-layer message norm; add per-layer message and state norms). Panel B: frozen-checkpoint CE with the attention residual removed, the message removed, and the MLP skip removed, per layer, on the declared evaluation set. Permitted inference: the functional role of each skip in the trained model, not what training without it would reach.

New T3, Sec. 5 or supplement: frame structure versus lookup capacity. Rows: reported frames; identity frames; identity frames plus an equal-size additive table; factorized frames at several code sizes; reference-coordinate MLP. Columns: total parameters, active parameters per token, CE, tokens per second. Permitted inference: whether multiplicative structure or table size carries the frames' contribution.

Place F2 below F7 and T3 in priority: the passive-covariance identity is already proven, whereas F1, F2 and F4 raise the unresolved empirical questions.

## Method, evidence, and limits

Scripts are in panel/transformer_checks/.
sec4_checks.py (C:/Python314/python.exe) covers the KL expansion, Prop. 4.1, the isotropic reduction, the compensation prior, the counterexample, 20,000 bound trials with a sympy maximization, the variance statements, temperature rescaling, rotary relativity, the head redundancy, and ALiBi slopes.
fwd_probe.py, probe2.py and probe3.py (C:/anaconda/python.exe, CPU, one thread, float64) recompute the forward pass from final_model.pt loaded with weights_only=True; fwd_probe_out.json holds the main output.
Residuals: KL expansion 3.6e-15; Prop. 4.1 4.4e-15; isotropic reduction 7.1e-15; compensation prior 5.6e-16; counterexample exact (0.6224593312, 0.3775406688); temperature rescaling 4.4e-16; rotary relativity 2.8e-14; cogredient invariance 3.9e-14; relative spectrum 7.8e-14; shared-covariance Gaussian routing against the biased dot product on trained weights, at most 3.8e-16 in total variation.
Limits: the ratio and ablation numbers come from two passages (128 and 122 tokens; one written in WikiText style from memory, one generic). They agree with the run's own logged validation diagnostics but are per-passage measurements, not corpus estimates.
No GPU work, training, Lean, or tamper checks were run; no manuscript, bibliography, data, or code file was modified.
Vault ingestion candidates, not written: the inert-residual measurement, the static-covariance decomposition, and the Movellan-Gabbur and Litman-Guo precedents. The vault's recorded "dominant residual path" (80-85% prior weight) concerns the older E-step architecture, the opposite regime from the predictive-content model.

## Recommended bibliography entries (verified against primary pages this session)

```bibtex
@misc{Movellan2020ProbabilisticTransformers,
  author = {Movellan, Javier R. and Gabbur, Prasad},
  title = {Probabilistic Transformers},
  year = {2020},
  eprint = {2010.15583},
  archivePrefix = {arXiv}
}
@inproceedings{Gabbur2021ProbabilisticAttention,
  author = {Gabbur, Prasad and Bilkhu, Manjot and Movellan, Javier R.},
  title = {Probabilistic Attention for Interactive Segmentation},
  booktitle = {Advances in Neural Information Processing Systems},
  volume = {34},
  year = {2021}
}
@inproceedings{Nguyen2022MGK,
  author = {Nguyen, Tam Minh and Nguyen, Tan Minh and Le, Dung D. D. and Nguyen, Duy Khuong and Tran, Viet-Anh and Baraniuk, Richard and Ho, Nhat and Osher, Stanley},
  title = {Improving Transformers with Probabilistic Attention Keys},
  booktitle = {Proceedings of the 39th International Conference on Machine Learning},
  series = {PMLR},
  volume = {162},
  pages = {16595--16621},
  year = {2022}
}
@inproceedings{Kim2021Lipschitz,
  author = {Kim, Hyunjik and Papamakarios, George and Mnih, Andriy},
  title = {The Lipschitz Constant of Self-Attention},
  booktitle = {Proceedings of the 38th International Conference on Machine Learning},
  series = {PMLR},
  volume = {139},
  pages = {5562--5571},
  year = {2021}
}
@inproceedings{Niculae2017Regularized,
  author = {Niculae, Vlad and Blondel, Mathieu},
  title = {A Regularized Framework for Sparse and Structured Neural Attention},
  booktitle = {Advances in Neural Information Processing Systems},
  volume = {30},
  year = {2017}
}
@inproceedings{Martins2016Sparsemax,
  author = {Martins, André F. T. and Astudillo, Ramón Fernandez},
  title = {From Softmax to Sparsemax: A Sparse Model of Attention and Multi-Label Classification},
  booktitle = {Proceedings of the 33rd International Conference on Machine Learning},
  series = {PMLR},
  volume = {48},
  pages = {1614--1623},
  year = {2016}
}
@misc{Litman2026AttentionPriors,
  author = {Litman, Elon and Guo, Gabe},
  title = {You Need Better Attention Priors},
  year = {2026},
  eprint = {2601.15380},
  archivePrefix = {arXiv},
  note = {Version 2, 23 August 2026}
}
@misc{Sukhbaatar2019PersistentMemory,
  author = {Sukhbaatar, Sainbayar and Grave, Edouard and Lample, Guillaume and Jégou, Hervé and Joulin, Armand},
  title = {Augmenting Self-attention with Persistent Memory},
  year = {2019},
  eprint = {1907.01470},
  archivePrefix = {arXiv}
}
@inproceedings{Geva2021KeyValue,
  author = {Geva, Mor and Schuster, Roei and Berant, Jonathan and Levy, Omer},
  title = {Transformer Feed-Forward Layers Are Key-Value Memories},
  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},
  year = {2021}
}
@inproceedings{Gu2025AttentionSink,
  author = {Gu, Xiangming and Pang, Tianyu and Du, Chao and Liu, Qian and Zhang, Fengzhuo and Du, Cunxiao and Wang, Ye and Lin, Min},
  title = {When Attention Sink Emerges in Language Models: An Empirical View},
  booktitle = {International Conference on Learning Representations},
  year = {2025}
}
@inproceedings{Sutskever2011GeneratingText,
  author = {Sutskever, Ilya and Martens, James and Hinton, Geoffrey E.},
  title = {Generating Text with Recurrent Neural Networks},
  booktitle = {Proceedings of the 28th International Conference on Machine Learning},
  year = {2011}
}
@inproceedings{Perez2018FiLM,
  author = {Perez, Ethan and Strub, Florian and de Vries, Harm and Dumoulin, Vincent and Courville, Aaron},
  title = {{FiLM}: Visual Reasoning with a General Conditioning Layer},
  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
  year = {2018}
}
@misc{Ha2016HyperNetworks,
  author = {Ha, David and Dai, Andrew and Le, Quoc V.},
  title = {HyperNetworks},
  year = {2016},
  eprint = {1609.09106},
  archivePrefix = {arXiv}
}
@inproceedings{Huang2025OverTokenized,
  author = {Huang, Hongzhi and Zhu, Defa and Wu, Banggu and Zeng, Yutao and Wang, Ya and Min, Qiyang and Zhou, Xun},
  title = {Over-Tokenized Transformer: Vocabulary is Generally Worth Scaling},
  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},
  year = {2025}
}
@inproceedings{Yu2025ScalingEmbedding,
  author = {Yu, Da and Cohen, Edith and Ghazi, Badih and Huang, Yangsibo and Kamath, Pritish and Kumar, Ravi and Liu, Daogao and Zhang, Chiyuan},
  title = {Scaling Embedding Layers in Language Models},
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2025}
}
@inproceedings{Ostmeier2025LieRE,
  author = {Ostmeier, Sophie and Axelrod, Brian and Varma, Maya and Moseley, Michael E. and Chaudhari, Akshay and Langlotz, Curtis},
  title = {{LieRE}: Lie Rotational Positional Encodings},
  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},
  year = {2025}
}
@inproceedings{Xiong2020LayerNorm,
  author = {Xiong, Ruibin and Yang, Yunchang and He, Di and Zheng, Kai and Zheng, Shuxin and Xing, Chen and Zhang, Huishuai and Lan, Yanyan and Wang, Liwei and Liu, Tie-Yan},
  title = {On Layer Normalization in the Transformer Architecture},
  booktitle = {Proceedings of the 37th International Conference on Machine Learning},
  year = {2020}
}
```
Not re-fetched this session: Elhage et al. (2021), "A Mathematical Framework for Transformer Circuits", Transformer Circuits Thread (canon). Dong et al. (2021) is already in references.bib as dong2021attention.

Sources consulted:
[Press et al., ALiBi](https://ar5iv.labs.arxiv.org/html/2108.12409);
[Litman and Guo](https://arxiv.org/abs/2601.15380);
[Movellan and Gabbur](https://ar5iv.labs.arxiv.org/html/2010.15583);
[Gabbur et al.](https://proceedings.neurips.cc/paper/2021/hash/23937b42f9273974570fb5a56a6652ee-Abstract.html);
[Nguyen et al.](https://proceedings.mlr.press/v162/nguyen22c.html);
[Kim et al.](https://proceedings.mlr.press/v139/kim21i/kim21i.pdf);
[Niculae and Blondel](https://ar5iv.labs.arxiv.org/html/1705.07704);
[Martins and Astudillo](https://proceedings.mlr.press/v48/martins16.html);
[Sukhbaatar et al.](https://ar5iv.labs.arxiv.org/html/1907.01470);
[Geva et al.](https://arxiv.org/abs/2012.14913);
[Gu et al.](https://arxiv.org/abs/2410.10781);
[Pro-Attention abstract via Semantic Scholar](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ACCESS.2022.3229055) and [Crossref record](https://api.crossref.org/works/10.1109/ACCESS.2022.3229055);
[Sutskever et al.](http://www.cs.toronto.edu/~bonner/courses/2014s/csc321/readings/sutskever2011icml.pdf);
[FiLM](https://arxiv.org/abs/1709.07871);
[HyperNetworks](https://arxiv.org/abs/1609.09106);
[Over-Tokenized Transformer](https://arxiv.org/abs/2501.16975);
[SCONE](https://arxiv.org/abs/2502.01637);
[LieRE](https://arxiv.org/abs/2406.10322);
[Xiong et al.](https://arxiv.org/abs/2002.04745);
[Longformer](https://ar5iv.labs.arxiv.org/html/2004.05150);
[Mistral 7B](https://ar5iv.labs.arxiv.org/html/2310.06825).
