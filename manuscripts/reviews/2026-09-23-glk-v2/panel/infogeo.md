# Information-geometry and Gaussian/SPD-geometry report: GL(K)_attention_v2 and supplement (2026-09-23)

Investigator: information-geometry lens (Claude Opus 5.5). Targets: `Research\manuscripts\GL(K)_attention_v2.tex` (Main) and `GL(K)_supplementary_v2.tex` (Supp), line numbers as in the brief. Prior review read first (`V3_Transformer\docs\reviews\2026-09-22-glk-v2\review.md`, `investigators\probability.md`, `gauge.md`, `independent-math-check.md`, `figure-data-plan.md`). Nothing outside the scratchpad `panel` directory was modified. No GPU, no Lean, no tamper tests, no forward pass of the model.

Evidence base. (1) `panel\infogeo\infogeo_checks.py` and `infogeo_checks_patch.py` (numpy 2.4, scipy 1.17, sympy 1.14 under `C:/Python314/python.exe`, seeded): every identity listed in the brief recomputed; residuals in `infogeo_checks.json` and `infogeo_checks_patch.json`. (2) `panel\infogeo\l3_extract.py` read the archived `D:\DATA_KEEP\31.04_wikitext-103_K256_4-layer_noHM\final_model.pt` once with `torch.load(weights_only=True, map_location="cpu", mmap=True)`, one thread, CUDA hidden, and saved small slices (48 unigram-sampled token rows, positional rows, the log-variance table, the 16 relational maps); `l3_static_cov.py`, `l3_consistency.py` and `l3_layer0_D.py` analyze them in numpy (outputs `l3_*.json`). The reconstruction reproduces the archived per-layer diagnostics (Finding 1(e)), so it is the diagnosed model state; it uses current `vfe3` conventions because the dirty source bytes of the run are unrecoverable. (3) Primary sources read for locators: van Erven and Harremoes 2014 (arXiv 1206.2459, text in `infogeo\vanerven_2014.txt`) and Wainwright and Jordan 2008 (`infogeo\wainwright_jordan_2008.txt`); abstracts of Du, Hu and Lee 2018, Kunin et al. 2021, Arora, Li and Lyu 2019, and Amari 2007 checked online.

## Verdict

No displayed identity in my scope is mathematically wrong. Every formula the brief lists recomputes to rounding level (Section "Verified identities"). The findings are of three kinds: exact results the paper misses that change how Sections 2.6, 3.1 and 3.3 should be organized (Findings 2, 4, 5, 8, 9); unstated redundancies that make two reported diagnostics representation-dependent (Finding 3); and one empirical fact about the reported run that changes how its Gaussian routing must be described: the stored covariance collapsed to about 1.04 I, so the covariance channel used for routing is static frame geometry (Finding 1). The sharp routing bound of lead L7 is proved (Finding 6).

## Findings (strongest first)

### 1. In the reported run the routing covariance is static frame geometry: stored Sigma_p is about 1.04 I and C_i is about 1.04 (U_i^T U_i)^{-1}
**Location:** Main 1119 (Sigma^(l+1) = Sigma^(l)), 1134 ("stored beliefs are diagonal Gaussians, but each role projection retains its full 32 x 32 reduced covariance"; "covariance and frame are held fixed through the stack"), 985, 1183 ("covariance-aware routing"); eq:projected_full_kl.
**Severity:** high
**Evidence:**
(a) Structure (independent code copy). The predictive branch returns `sigma = belief.sigma` (`vfe3\inference\e_step.py:838`); the block MLP covariance contract is `passthrough`; one realized frame context is passed to every layer (`vfe3\model\stack.py:138-148`, with `e_phi_lr = 0`); the initial covariance is `exp(sigma_log_embed[x_i])` (`vfe3\model\prior_bank.py:840, 996`); U_i = exp(X_{x_i}) exp(Y_i). Hence C_i and every V_{Q,i}^{(l,h)}, V_{K,j}^{(l,h)} are functions of (token type, position, layer, head) only, never of context.
(b) Term classification of eq:projected_full_kl (exact; two-way numerical decomposition in `infogeo_checks.json`, section I): -1/2 log det V_{Q,i} and -r/2 are row constants; 1/2 log det V_{K,j} is a source-only static bias; 1/2 b_j^T P_j b_j is source-only (contextual for l >= 1); 1/2 Tr(P_j V_{Q,i}) is a static pair term; 1/2 a_i^T P_j a_i and -a_i^T P_j b_j are contextual pair terms weighted by the static per-source metric P_j. Under a shared key covariance the trace and query-quadratic terms become exact row constants (row fraction 1.000, interaction 3.9e-16).
(c) Archived weights. All 50,257 x 256 stored log-variances: mean 0.043, s.d. 0.052, range [-0.65, 0.66], against the initialization log 15 = 2.708. The unigram-weighted trace CV is 0.048 (research.json records `sigma_trace_cv` 0.047 with `sigma_trace_cv_gate_pass: false`). So Sigma_p is about 1.04 I, and C_i matches 1.04 (U_i^T U_i)^{-1} to a median relative Frobenius gap of 7.6% (max 19%; 48 token-position pairs covering 28% of unigram mass); the anisotropy of C_i (median condition number 29.5) comes from the frames. For Sigma proportional to I, C_i depends only on the symmetric factor P_i of the polar decomposition U_i = O_i P_i; the rotational part of the frame affects only xi_i. The arithmetic of the regularizer is consistent with this: decoupled AdamW with `sigma_weight_decay` 0.04 at `m_p_sigma_lr` 0.001 under the cosine schedule multiplies a gradient-free row by exp(-0.04 x 121) = 0.008, taking 2.708 to 0.02; the observed 0.043 +/- 0.052 indicates weak gradient pressure on the table (an inference, not a measured gradient).
(d) Magnitudes in logit units (divided by tau = sqrt 32), all layers and heads: source-only log-det bias s.d. 0.09-0.25; trace term source (column) s.d. 0.03-1.05, but its pure pair (interaction) s.d. only 0.003-0.11; the per-source precision P_j differs from the across-source mean by a median 19-24% (relative Frobenius). At layer 0, where every term is static, the total static source s.d. is 0.18-1.21 and the static pair s.d. 0.12-0.44 logits; raw D_ij spans 8-115 against the 2048 cap.
(e) Fidelity of the reconstruction: minimum raw query-map singular values 6.64 / 12.32 / 12.05 / 10.44 and key-map 23.76 (layer 0) equal the archived `metrics_per_layer.csv` values to printed precision; maximum projected condition number 520 / 204 / 84 / 137 against archived 550 / 210 / 89 / 163; minimum eigenvalue 44.6 / 152 / 144 / 109 against 43.1 / 151 / 137 / 108 (a sample of 48 pairs versus one 128-token sequence).
**Fix:** After "The covariance and frame are held fixed through the stack" (1134) add: "Consequently $C_i$ and every projected covariance depend only on token type and position. In Eq.~\eqref{eq:projected_full_kl}, $\tfrac12\log\det V_{K,j}$ and $\tfrac12\operatorname{Tr}(P_jV_{Q,i})$ are context-independent learned biases, and $P_j$ is a context-independent metric that weights the contextual mean terms. In the recorded run the stored log-variances end at $0.043\pm0.052$ from an initial $\log15$, so $\Sigma_p\approx1.04I$ and $C_i\approx1.04(U_i^\top U_i)^{-1}$: the covariance used for routing is determined by the frames to within about 8\% (median relative Frobenius deviation)." Add the static-versus-contextual logit decomposition to prior placeholder F3 Panel C, and describe the planned covariance-aware versus mean-only comparison (1183) as a test of this frame-metric channel. This is a reporting correction; it does not ask for a configuration change.
**Falsifies:** A dump of `prior_bank.sigma_log_embed` from the executed run with log-variances far from 0 or strongly anisotropic within tokens, or evidence that the executed (dirty) code updates Sigma or the frames between layers.
**Status:** The manuscript statements (passthrough, fixed frames, full reduced covariance) are E/D and accurate. The phrases "full 32 x 32 reduced covariance" and "covariance-aware routing" invite reading the channel as learned uncertainty, so the prose inflates by omission.
**Novelty vs prior review:** extends C7 and R6 with new evidence (Sigma_p about I; C_i about the frame Gram inverse; covariance acting as a static source bias and per-source metric); disagrees with the low weight of C7 as far as interpretation of the experiment is concerned.

### 2. Projected Gaussian-KL routing is exactly dot-product routing in exponential-family dual coordinates; Proposition prop:projected_dot_product is its mean block
**Location:** Main 971-1009 (eq:projected_full_kl, Proposition prop:projected_dot_product), Table tab:fep_nn_correspondence row "Query/key dot product".
**Severity:** medium
**Evidence:** For Gaussian laws on R^r with sufficient statistic (y, y y^T), write the query in expectation coordinates eta_{Q,i} = (a_i, V_{Q,i} + a_i a_i^T) and the key in natural coordinates theta_{K,j} = (P_j b_j, -P_j/2), with pairing <eta, theta> = eta_1^T theta_1 + Tr(eta_2 theta_2) = a^T P b - Tr(P(V + a a^T))/2, log-partition A(theta_{K,j}) = b_j^T P_j b_j/2 + log det V_{K,j}/2 + (r/2) log 2 pi, and conjugate A*(eta_{Q,i}) = -H(q_{Q,i}). The mixed form of the KL divergence, Wainwright and Jordan 2008, Section 5.2, Eq. (5.11) (verified in the extracted text: "D(theta_1 || theta_2) = A(theta_2) + A*(mu_1) - <mu_1, theta_2>"), gives D_ij = A(theta_{K,j}) + A*(eta_{Q,i}) - <eta_{Q,i}, theta_{K,j}>. Residual against the Cholesky KL: 9.8e-15 over 200 random cases (float64 eps 2.2e-16, D of order 1-10). Therefore, with no covariance hypothesis, beta_ij = softmax_j(<eta_{Q,i}, theta_{K,j}>/tau - A(theta_{K,j})/tau + log pi_ij) exactly: a dot product in R^{r + r(r+1)/2} (560 per head at r = 32) between query expectation parameters and key natural parameters, with the key log-partition as source bias and A*(eta_{Q,i}) as row constant. When V_{K,j} = V_* the second-order key coordinate is shared, its pairing with V_{Q,i} + a_i a_i^T is a row constant, and the remaining mean block a_i^T V_*^{-1} b_j - b_j^T V_*^{-1} b_j/2 is Eq. main_dot_product_scope (residual 3.9e-16). This is the canonical-divergence structure of a dually flat family (Amari and Nagaoka 2000, Ch. 3). It also produces the classification of Finding 1(b) at once: row term A*(eta_{Q,i}), source term A(theta_{K,j}), and all pair dependence inside one bilinear pairing.
**Fix:** Insert after eq:projected_full_kl:
```latex
Write the query law in expectation coordinates and the key law in natural coordinates,
\begin{equation}
\eta_{Q,i}=\bigl(a_i,V_{Q,i}+a_ia_i^\top\bigr),\qquad
\theta_{K,j}=\bigl(P_jb_j,-\tfrac12P_j\bigr),\qquad
\langle\eta,\theta\rangle=\eta_1^\top\theta_1+\operatorname{Tr}(\eta_2\theta_2).
\end{equation}
With the Gaussian log-partition $A(\theta_{K,j})=\tfrac12b_j^\top P_jb_j+\tfrac12\log\det V_{K,j}+\tfrac r2\log2\pi$
and its conjugate $A^*(\eta_{Q,i})=-H(q_{Q,i})$, Eq.~\eqref{eq:projected_full_kl} is the mixed form of the
divergence \citep[Sec.~5.2, Eq.~(5.11)]{Wainwright2008},
\begin{equation}
D_{ij}=A(\theta_{K,j})+A^*(\eta_{Q,i})-\langle\eta_{Q,i},\theta_{K,j}\rangle .
\label{eq:dual_pairing}
\end{equation}
The categorical optimizer is therefore exactly
$\beta_{ij}=\softmax_j\bigl(\langle\eta_{Q,i},\theta_{K,j}\rangle/\tau-A(\theta_{K,j})/\tau+\log\pi_{ij}\bigr)$,
a dot product in $\mathbb R^{r+r(r+1)/2}$ between query expectation parameters and key natural parameters,
with the key log-partition as a source bias. Proposition~\ref{prop:projected_dot_product} is the case in which
the second-order key coordinate $-\tfrac12P_j$ is shared, so that only the mean block
$a_i^\top V_*^{-1}b_j$ of the pairing varies with the source.
```
In Table tab:fep_nn_correspondence replace "Exact cross term for projected full Gaussians; other covariance terms remain in general" by "Exact dot product in dual coordinates, Eq. (dual_pairing); reduces to the r-dimensional mean block under shared key covariance".
**Falsifies:** A pair of nondegenerate Gaussian laws violating Eq. (dual_pairing); none exists, since it is Eq. (5.11) of Wainwright and Jordan specialized, and none appeared in 200 trials.
**Status:** The proposition is P and correct; the paper labels the whole correspondence conditional, which deflates it: the conditional equality is the r-dimensional projection of an unconditional identity.
**Novelty vs prior review:** new.

### 3. Unstated cogredient GL(r_h) and GL(s_h) redundancies make the reported conditioning diagnostics representation-dependent (lead L5)
**Location:** Main 367-402 (comparison and content spaces declared as R^{r_h}, R^{s_h}), 386 (only the reference-basis change is stated), 681 (dilation versus sharpness), 1009 (whitened maps), 1159 (raw singular values 6.64-12.32, condition numbers 88.7-550.5); prior placeholder F5.
**Severity:** medium
**Evidence:**
(a) Eq. glk_invariance applied inside the comparison space gives D_ij(A S_Q, A S_K) = D_ij(S_Q, S_K) for every A in GL(r_h): residual 1.7e-15. The contragredient map (A S_Q, A^{-T} S_K) changes D by a factor 41 in relative terms but leaves the dot product invariant (2.3e-16); the cogredient map changes the dot product by a factor 9. The two redundancies share only O(r_h), which is exactly the residual freedom of the whitening in Proposition prop:projected_dot_product (orthogonal re-whitening residual 3.9e-16). For tied maps the costs depend on S only through its row space, a point of the Grassmannian Gr(r_h, K). On the content side m_i depends on (T_h, O_h) only through O_h T_h, so (T_h, O_h) -> (B T_h, O_h B^{-1}), B in GL(s_h), is exact. Per head this is 2 x 32^2 = 2048 redundant directions, 65,536 of the 1,048,576 relational parameters (6.25%). The Gaussian comparison space needs no inner product; its metric is supplied by the key precision, whereas a dot product needs a fixed pairing.
(b) The case A = cI gives D invariant under (a, b, V_Q, V_K) -> (ca, cb, c^2 V_Q, c^2 V_K); under a shared key covariance the routing depends on (V_*, tau) only through tau V_* (residual 6.1e-16). This is the exact content of the sentence at 681 ("gauge covariance does not identify them"), which should say it.
(c) Representation dependence: with every D_ij fixed to 5e-15, a common A moved the minimum singular values of S by factors 40 and 1/40 and cond(V_K) from 18 to 8,942, while the spectrum of V_K^{-1} V_Q, the only covariance data entering the trace and log-determinant terms, was unchanged to 1.4e-16 (`infogeo_checks_patch.json`). In the trained model the archived maxima 88.7-550.5 are all attained by query covariances; reconstructed key-covariance condition numbers are at most 18 (`l3_consistency.json`).
(d) Noether-type conservation. Because the training loss depends on (S_Q, S_K) of a head only through its D_ij, its gradient satisfies grad_{S_Q} L S_Q^T + grad_{S_K} L S_K^T = 0 (finite-difference check 1.6e-8 relative, the finite-difference floor), so gradient flow conserves Q_h = S_Q S_Q^T + S_K S_K^T; likewise it conserves T_h T_h^T - O_h^T O_h (Du, Hu and Lee 2018, NeurIPS; Kunin et al. 2021, ICLR). Toy check: plain gradient descent moves Q by 3.1e-5 and 1.5e-5 at steps 2e-3 and 1e-3 over the same flow time (drift proportional to the step), while a sign (Adam-like) update moves it 58%. In the archived run tr Q_h / tr Q_h(init) = 1,936-2,877 (norm growth 44-54, matching `parameter_motion.json` rel 39-54), and the content imbalance, zero at initialization, ends at 12-49% relative (`l3_static_cov.json`). This motion leaves every routing weight unchanged; it is optimizer-driven drift along symmetry directions. For a scale-invariant parameter it also lowers the effective angular step roughly as 1/||S|| (Arora, Li and Lyu 2019, ICLR), an implicit schedule on the routing maps (an inference; testable by gauge fixing). Heuristically, an unconfined Adam walk under the recorded schedule predicts ||Delta S|| = (sum_t eta_t^2 x 65,536)^{1/2}, about 770, against the observed 625-864 per layer.
**Fix:** After line 402 add:
```latex
The routing costs do not depend on a basis of the comparison space: Eq.~\eqref{eq:glk_invariance}
applied in $H_h^{\mathrm{cmp}}$ shows that $(S_{Q,h},S_{K,h})\mapsto(AS_{Q,h},AS_{K,h})$,
$A\in\mathrm{GL}(r_h)$, leaves every $D_{ij}^{(h)}$ unchanged. This cogredient redundancy differs from
the contragredient redundancy $(W_Q,W_K)\mapsto(W_QA,W_KA^{-\top})$ of dot-product scores; the two share
only $A\in\mathrm O(r_h)$, the residual freedom of whitening in Proposition~\ref{prop:projected_dot_product}.
For tied maps the costs depend on $S_h$ only through its row space. The content maps carry the analogous
redundancy $(T_h,O_h)\mapsto(BT_h,O_hB^{-1})$, $B\in\mathrm{GL}(s_h)$. The case $A=cI$ shows that
$D_{ij}$ is unchanged by $(a_i,b_j,V_{Q,i},V_{K,j})\mapsto(ca_i,cb_j,c^2V_{Q,i},c^2V_{K,j})$; under a
shared key covariance the routing depends on $V_*$ and $\tau$ only through $\tau V_*$.
```
Replace the first sentence at 1159 by: "Saved per-layer probes report the smallest raw query-map singular values (6.64 to 12.32) and the largest projected-covariance condition numbers (88.7 to 550.5, all attained by query covariances). Both describe the numerical representative reached by the optimizer rather than the learned routing, since the redundancy $(S_Q,S_K)\mapsto(AS_Q,AS_K)$ changes them while leaving every cost unchanged, and the raw maps grew 39- to 54-fold in norm during training. The representation-independent quantities are the spectra of $V_{K,j}^{-1/2}V_{Q,i}V_{K,j}^{-1/2}$." Prior placeholder F5 should record these relative spectra and whitened-map singular values, plus tr Q_h and the content balance per layer as optimizer-drift diagnostics. Gauge fixing (for example normalizing the mean key covariance to I at each step) is an optional implementation choice, not a requirement.
**Falsifies:** A term of the executed loss that depends on S_Q or S_K other than through D_ij (weight decay, jitter, a norm penalty) would break exact invariance and the conservation law. The inspected code gives the relational groups `weight_decay` 0.0 (`vfe3\train.py:281`) and uses zero jitter (`vfe3\relational_scoring.py:5`); the dirty run bytes could differ.
**Status:** The redundancy is not stated (omission). The diagnostics at 1159 are E, but they are presented as properties of the learned operator, which inflates their meaning.
**Novelty vs prior review:** new (confirms and extends lead L5); disagrees with prior figure plan F5, which asks for raw map singular values and single-matrix condition numbers.

### 4. Gibbs routing is the geometric (exclusive) pooling of pointwise source posteriors; query covariance never tempers it
**Location:** Main 686-721 (eq:mixture_softmax_general), 985, 997 ("The query covariances may differ across receivers"); contrast with the readout discussion at 843-855.
**Severity:** medium
**Evidence:** Let p_i(j | y) be proportional to pi_ij p_{K,j}(y). Then beta*_i, proportional to pi_ij exp(E_q log p_{K,j}(y) / tau), is the minimizer of E_{y ~ q_{Q,i}} KL(beta || p_i^(tau)(. | y)) with p_i^(tau)(j | y) proportional to pi_ij p_{K,j}(y)^{1/tau}: the normalized geometric mean of the pointwise posteriors under the query law. The posterior-predictive source probability E_q p_i(j | y) minimizes the reverse expected divergence E_q KL(p_i(. | y) || beta) and is the arithmetic mean. Arithmetic and geometric means both appear in the alpha-integration family of Amari 2007 (Neural Computation 19:2780-2796), the geometric one here after normalization; the two KL characterizations above were checked directly. The paper proves this dichotomy for the vocabulary readout; in its own example the two minimizers recompute to 0.1192029 = 1/(1 + e^2) and 0.3238278 = pbar by quadrature (`infogeo_checks.json`, section P). The same dichotomy governs routing and is not stated. Consequence, exact from eq:projected_full_kl: query covariance enters D_ij only through Tr(P_j V_{Q,i})/2, a penalty on sources whose key laws are precise along the uncertain directions of the query, and it drops out entirely under a shared key covariance. Example (r = 1, keys at 0 and 2 with unit variance, query mean 0.5): the Gibbs weights stay (0.7311, 0.2689) for query variance 0.01, 1, 10 and 100, while posterior-predictive weights flatten 0.729, 0.648, 0.560, 0.520.
**Fix:** Add after eq:mixture_softmax:
```latex
For fixed $q_{Q,i}$ the optimizer \eqref{eq:mixture_softmax_general} minimizes
$\mathbb E_{y\sim q_{Q,i}}D_{\mathrm{KL}}\bigl(\beta_i\|p_i^{(\tau)}(\cdot\mid y)\bigr)$ with
$p_i^{(\tau)}(j\mid y)\propto\pi_{ij}p_{K,j}(y)^{1/\tau}$: it is the normalized geometric mean of the
pointwise source posteriors under the query law. The posterior-predictive source probability
$\mathbb E_{y\sim q_{Q,i}}p_i^{(1)}(j\mid y)$ minimizes the reverse expected divergence and differs in
general, as for the readout of Section~\ref{sec:supp_decode_derivation}. Query covariance enters $D_{ij}$
only through $\tfrac12\operatorname{Tr}(P_jV_{Q,i})$, which penalizes sources whose key laws are precise
along the uncertain directions of the query, and it drops out when key covariances are shared. A broad
query law therefore does not flatten Gibbs routing.
```
**Falsifies:** A configuration with shared key covariance in which changing V_{Q,i} changes beta_i. None exists, because V_{Q,i} then enters only the row constant c_i.
**Status:** The optimizer is P; the uncertainty semantics are unstated, and the full-Gaussian framing invites reading routing as uncertainty-weighted averaging.
**Novelty vs prior review:** new.

### 5. The KL direction is derived from the declared joint and the exclusive divergence; the alternatives change which covariance must be shared
**Location:** Main 688-701 (eq:mixture_joint, eq:mixture_posterior, eq:mixture_free_energy), 971-1009; prior review Section 6 lists "comparison KL direction" among primitives to declare.
**Severity:** medium
**Evidence:** (a) With P_i(y, j) = pi_ij p_{K,j}(y) and Q(y, j) = beta_j q_{Q,i}(y), the exclusive divergence KL(Q || P) yields sum_j beta_j KL(q_{Q,i} || p_{K,j}) + KL(beta || pi_i): the direction is forced by placing the query law in the recognition factor and the key laws as generative mixture components. (b) The inclusive divergence KL(P || Q) = KL(pi_i || beta) + sum_j pi_ij KL(p_{K,j} || q_{Q,i}) is minimized at beta = pi_i for all costs (numerical argmin minus pi: 5e-9, against Gibbs minus pi: 0.45), so the inclusive direction cannot produce content-dependent routing with this factorization. (c) The reverse per-source cost comes from a different joint, pi_ij q_{Q,i}(y) with recognition beta_j p_{K,j}(y). Its reduction to a dot product needs a shared query covariance V_# and keeps the source bias [b_j^T V_#^{-1} b_j + Tr(V_#^{-1} V_{K,j}) - log det V_{K,j}]/2 (additive remainder, interaction 3.9e-16); with only the key covariance shared, a pair-dependent remainder b_j^T V_{Q,i}^{-1} b_j survives (interaction fraction 0.080). Symmetric divergences need both covariances shared: residual interaction 0.052 for Jeffreys and 0.101 for Bhattacharyya (Renyi order 1/2) under shared key covariance (`infogeo_checks.json` section M, patch file). In the dual coordinates of Finding 2 the forward cost pairs query expectation with key natural parameters and the reverse cost pairs query natural with key expectation parameters (reverse identity residual 6.2e-15), which is why the covariance that must be shared switches sides.
**Fix:** Add to Section 2.6 after eq:mixture_energy_entropy:
```latex
The direction of $D_{ij}$ is fixed by the declared joint and the exclusive divergence: the key laws are the
generative mixture components and the query law is the recognition factor. The inclusive divergence gives
$D_{\mathrm{KL}}(P_i\|Q_{i,\beta})=D_{\mathrm{KL}}(\pi_i\|\beta_i)+\sum_j\pi_{ij}D_{\mathrm{KL}}(p_{K,j}\|q_{Q,i})$,
whose minimizer is $\beta_i=\pi_i$ for all costs. The reverse cost $D_{\mathrm{KL}}(p_{K,j}\|q_{Q,i})$ follows
from the joint $\pi_{ij}q_{Q,i}(y)$ with recognition $\beta_{ij}p_{K,j}(y)$; its reduction to a dot product
requires a shared query covariance $V_\#$ and retains the source bias
$\tfrac12[b_j^\top V_\#^{-1}b_j+\operatorname{Tr}(V_\#^{-1}V_{K,j})-\log\det V_{K,j}]$. Symmetric divergences
require both projected covariances to be shared.
```
**Falsifies:** A factorization with the query law in the recognition factor for which the inclusive divergence gives cost-dependent beta; impossible, since its beta-dependence is KL(pi_i || beta) alone.
**Status:** D given the declared joint; the modeling choice behind the direction is undisclosed, which deflates what the derivation actually establishes.
**Novelty vs prior review:** extends the prior Section 6 question with the derivation and its consequences.

### 6. Sharp routing perturbation bound: 2 tanh(eps_i/2) replaces e^{2 eps_i} - 1 (lead L7)
**Location:** Main 1022-1034, eq:projected_bias_error and eq:projected_softmax_bound.
**Severity:** low
**Evidence:** Proof. For A a subset of S_i, the derivative of beta(A) in delta_k is beta_k(1 - beta(A)) > 0 for k in A and -beta_k beta(A) < 0 for k outside A, so the maximum of beta(A) - p(A) over |delta| <= eps is attained at delta = eps on A and -eps off A, where it equals f(x) = x(1-x)(t-1)/(1 + x(t-1)) with x = p(A), t = e^{2 eps}. SymPy: the admissible stationary point is x* = (sqrt t - 1)/(t - 1) = 1/(1 + e^{eps}), the second derivative there is negative, and f(x*) - tanh(eps/2) simplifies to 0. Since sum_j |beta_j - p_j| = 2 max_A (beta(A) - p(A)), the sharp bound is 2 tanh(eps/2), itself at most min(eps, 2). Random search (20,000 trials, 2-19 sources, eps in (0.01, 3), half with two-valued delta): largest ratio to 2 tanh(eps/2) is 0.99999991; largest ratio to the printed bound is 0.49, so the printed bound is at least twice too large in every trial. At eps = 0.7 the two-point configuration attains 0.67275 = 2 tanh(0.35) exactly, against the printed 3.0552. The free row constant c_i is best set at the midrange of the squared key norms.
**Fix:** Replace the sentence "Writing ... hence" and the display by:
```latex
Writing $\beta_{ij}=p_{ij}e^{\delta_{ij}}/\sum_kp_{ik}e^{\delta_{ik}}$ with $|\delta_{ij}|\le\varepsilon_i$, the
quantity $\beta_i(A)-p_i(A)$ for $A\subseteq S_i$ is largest at $\delta_{ij}=\varepsilon_i$ on $A$ and
$\delta_{ij}=-\varepsilon_i$ off $A$, where it equals $x(1-x)(e^{2\varepsilon_i}-1)/[1+x(e^{2\varepsilon_i}-1)]$
with $x=p_i(A)$. Maximizing over $x$ gives
\begin{equation}
\sum_j|\beta_{ij}-p_{ij}|\le2\tanh(\varepsilon_i/2)\le\min(\varepsilon_i,2),
\label{eq:projected_softmax_bound}
\end{equation}
with equality for two sources with $p_{i1}=1/(1+e^{\varepsilon_i})$ and $\delta_{i1}=-\delta_{i2}=\varepsilon_i$.
The best row constant is the midrange, giving
$\varepsilon_i=(\max_j\|\mathsf k_j\|^2-\min_j\|\mathsf k_j\|^2)/(4\tau)$.
```
The following sentences (uniform control, o(sqrt r) dispersion at tau = sqrt r) remain valid unchanged.
**Falsifies:** Any configuration with sum_j |beta_j - p_j| > 2 tanh(eps/2); excluded by the proof above.
**Status:** P; the printed bound is valid but loose, and its exponential growth overstates sensitivity at large eps.
**Novelty vs prior review:** new; the prior probability investigator called the bound "loose when large, but correct" without the sharp constant.

### 7. The metric at lines 426 and 457: prior C1 is correct but incomplete; the construction already carries a covariant statistical metric, and adjacent subsections use different metrics
**Location:** Main 426 (G_i = U_i^{-T} U_i^{-1}, "induced by the Euclidean reference metric"), 457 (orthogonal complement U_j im T_h^T), 543 (two index-raising options), 545-559 (Gaussian lift).
**Severity:** low
**Evidence:** C1 recomputed and confirmed: the G-orthogonal complement of ker(T U_j^{-1}) for G = U^{-T} H U^{-1} is U H^{-1} im T^T (principal angle 9.8e-12), invariant under U -> U a with H -> a^T H a (3.9e-12); resetting H = I after a non-orthogonal rebasing moves it by 0.995 rad. What C1 leaves out: (i) the Fisher information metric of the Gaussian location family at the state, G_i^F = Sigma_i^{-1} = U_i^{-T} C_i^{-1} U_i^{-1} (Skovgaard 1984, Scand. J. Statist. 11:211-223), transforms correctly under both the passive action and rebasing without any extra datum (angles 5.3e-12 and 2.1e-11); (ii) with it, (G_i^F)^{-1} B_ij = Sigma_i B_ij, so the two options at 543 are one option; (iii) the complement becomes U_j C_j im T_h^T = Sigma_j U_j^{-T} im T_h^T (6.0e-12), which in the test lies 1.43 rad from the Euclidean-reference complement, so the statement at 457 depends on this unexplained choice; (iv) the Gaussian lift at 552 minimizes the Fisher norm delta^T C_i^{-1} delta, so lines 457 and 552 use different metrics without comment; Sigma_i B_ij and the lift differ only in the middle precision (key versus query), relative difference 5.6 in a generic case and zero when V_{Q,i} = V_{K,j}; (v) in the trained run Sigma_p is about 1.04 I (Finding 1), so the Fisher metric is approximately the Euclidean metric of local coordinates, the opposite convention to Table 426.
**Fix:** Declare the metric. If the Euclidean reference inner product is intended, carry it as data H with H -> a^T H a (prior C1). Otherwise use the Fisher metric: "With the Fisher metric of the location family, $G_i=\Sigma_i^{-1}=U_i^{-\top}C_i^{-1}U_i^{-1}$, which transforms as $G_i'=g_i^{-\top}G_ig_i^{-1}$ and needs no reference inner product, $G_i^{-1}B_{ij}=\Sigma_iB_{ij}$ and the complement of the invisible sending directions is $U_jC_j\operatorname{im}T_h^\top$. The Gaussian lift of Eq.~\eqref{eq:comparison_gaussian_lift} is the minimal-norm right inverse in this metric."
**Falsifies:** A role for the Euclidean reference inner product elsewhere in the paper (statistical or covariance-theoretic) that the Fisher metric cannot play.
**Status:** D and correct as a specialization; the prose presents a non-statistical metric without motivation in a paper whose states are Gaussian laws.
**Novelty vs prior review:** extends C1 (confirms it, adds the statistical alternative and the internal inconsistency with the lift).

### 8. Rotary scores: rotating both Gaussian laws is exactly relative for any covariance; the dot-product form needs only plane-wise isotropic key covariance
**Location:** Main 1058-1065 (eq:projected_rope_kernel and the following sentence "Under shared isotropic comparison covariance ...").
**Severity:** low
**Evidence:** Eq. glk_invariance with the common orthogonal map R_i^T gives KL((R_i)_* q_{Q,i} || (R_j)_* p_{K,j}) = KL(q_{Q,i} || (R_{j-i})_* p_{K,j}): residual 1.6e-14 under a common shift of 17 positions with anisotropic V_Q, V_K (condition 50, r = 6, three frequencies). Rotating means only, as in "a_i -> R_i a_i, b_j -> R_j b_j", breaks the relative property for the same covariances (change 1.0). The dot-product reduction requires only that the shared key covariance satisfy R_delta V_* R_delta^T = V_* for every delta; with distinct rotation frequencies this is V_* = direct sum of lambda_k I_2 over the rotation planes (residual 4.4e-16), strictly weaker than "shared isotropic comparison covariance"; the query covariance is unrestricted because it enters a row constant.
**Fix:** Replace the sentence at 1065 by:
```latex
Rotating both projected laws gives, by Eq.~\eqref{eq:glk_invariance},
$D_{\mathrm{KL}}\bigl((R_i)_*q_{Q,i}\|(R_j)_*p_{K,j}\bigr)=D_{\mathrm{KL}}\bigl(q_{Q,i}\|(R_{j-i})_*p_{K,j}\bigr)$,
a relative-position score for arbitrary projected covariances. The dot-product form with an unchanged
key-norm bias requires only that the shared key covariance commute with every $R_\delta$; with distinct
rotation frequencies this means $V_*=\bigoplus_k\lambda_kI_2$ over the rotation planes. Query covariance is
unrestricted.
```
**Falsifies:** Repeated RoPE frequencies enlarge the commutant; the plane-wise statement is for distinct frequencies, as in standard RoPE.
**Status:** D; the prose deflates the generality of the rotary statement.
**Novelty vs prior review:** new (the prior gauge report found no defect in this passage and did not note the stronger statement).

### 9. Scope and locator of eq:glk_invariance, and the data-processing inequality the paper omits
**Location:** Main 349-355, 402, 662-669 (eq:irrep_block_kl_additivity), 723-725.
**Severity:** low
**Evidence:** The identity holds: relative residual 2.8e-14 at cond(A) = 10 and 4.7e-10 at cond(A) = 1000, tracking cond(A)^2 x eps; also for squared Hellinger (2.2e-10) and Renyi order 0.3 (2.3e-10), so "The same argument applies to f-divergences" is right and extends to every Renyi order. The citation Amari2016 carries no locator. van Erven and Harremoes 2014 (bib key vanErvenHarremoes2014), Theorem 9 (data-processing inequality for every order in [0, infinity], sub-sigma-algebras), applied to A and to A^{-1}, gives the equality; its Theorem 28 (additivity over product measures) is eq:irrep_block_kl_additivity at order one (residual 8.9e-16; counterexample value 0.22314355 = -log(1 - 0.36)/2 confirmed). The same Theorem 9 gives a positive result the paper omits: for tied maps S_Q = S_K = S, D_ij <= KL(q_i || (Omega_ij)_* q_j) (500 trials; largest D_proj - D_full = -0.154), so shared comparison is a coarse-graining of complete-state alignment (the case at 723-725). For S_Q != S_K no such bound exists: identical states give D_ij = 0.607 while the full-state divergence is 0. D_ij is a divergence between role-observable laws, not between agent states.
**Fix:** Cite \citep[Thm.~9]{vanErvenHarremoes2014} (applied to $A$ and $A^{-1}$) at 355 and note that the identity holds for every Renyi order; cite Thm.~28 of the same paper for Eq.~\eqref{eq:irrep_block_kl_additivity}; add after 725: "For tied maps, $D_{ij}\le D_{\mathrm{KL}}(q_i\|(\Omega_{ij})_*q_j)$ by the data-processing inequality, so a shared comparison coarse-grains complete-state alignment; for $S_Q\ne S_K$ no such bound holds, and identical states can have $D_{ij}>0$."
**Falsifies:** Not applicable to the identity; the added inequality would be refuted by a tied-map pair with D_proj > D_full (none in 500 trials; it is a theorem).
**Status:** D and correct; missing locator; omits a positive result.
**Novelty vs prior review:** new.

### 10. The optional Gaussian-bank readout gives the class templates no frame convention
**Location:** Main 812-857 ("pi_v a normalized class template on the same latent space").
**Severity:** low
**Evidence:** q_i is a section value in G(E_i); a fixed template has to be placed in each fiber by some frame. Comparing q_i with template coordinates held fixed while q_i transforms by g_i is not passive-covariant; comparing reference laws, KL((U_i^{-1})_* q_i || pi~_v), is covariant by eq:glk_invariance. The implementation copy contains both conventions: under `encode_mode = per_token` the decode compares local-coordinate numbers directly and rejects a frame (`vfe3\model\prior_bank.py:1282-1289`), while `canonical_content_projected` pulls the query back through U_i^{-1} (`prior_bank.py:1290-1331`). The readout identities (0.11920 and 0.32383, recomputed) and the geometric-versus-arithmetic characterization of Finding 4 are unaffected.
**Fix:** Add at 812: "Templates are declared in reference coordinates and compared with $\widetilde q_i=(U_i^{-1})_*q_i$, so that $\rho_i$ is invariant under the passive action; comparing local coordinates directly defines a different, non-covariant readout."
**Falsifies:** A statement elsewhere in the main text that fixes the frame of the templates.
**Status:** D (identities correct); typing under-specified in a paper whose central claim is covariance.
**Novelty vs prior review:** new.

## Leads tested

**L3 (static covariance, pair biases): MODIFIED.** Static per (token, position, layer, head): CONFIRMED from code (Finding 1(a)) and stated in the paper itself (1119, 1134). "Pair biases": REFUTED as the dominant effect. The static pair (interaction) part of the covariance terms is 0.003-0.11 logits; the covariance terms act mainly as a static source bias (log-det s.d. 0.09-0.25, trace-column s.d. 0.03-1.05 logits) and a per-source Mahalanobis metric P_j (median 19-24% spread). Stronger than the lead: the stored covariance itself collapsed to about 1.04 I, so C_i is about 1.04 (U_i^T U_i)^{-1} (median gap 7.6%); `sigma_trace_cv` 0.047 is reproduced (unigram-weighted 0.048), but trace uniformity understates the point, which is per-coordinate isotropy.

**L5 (comparison/content redundancy): CONFIRMED and extended** (Finding 3): cogredient invariance 1.7e-15; contragredient intersection O(r_h); tied maps depend on a Grassmannian point; content GL(s_h); moment-map identity at the finite-difference floor; conserved quantities under gradient flow, violated in the run by tr Q growth of 1,936-2,877 and content imbalance 12-49%; the reported raw singular values and condition numbers are representation-dependent while the relative spectra are invariant (1.4e-16).

**L7 (sharp bound 2 tanh(eps/2)): CONFIRMED with proof** (Finding 6): SymPy maximization, 20,000-trial search (maximum ratio 0.99999991), exact attainment 0.67275 at eps = 0.7.

**L1 (partially in lens), part (b): CONFIRMED and sharpened.** The routing covariance is a static function of token type and position and, in the trained run, approximately the inverse frame Gram matrix; only the symmetric polar factor of U_i reaches C_i. Parts (a), (c), (d) and the loop-trace statement are outside this lens.

**L6 (temperature inside a normalized joint), checked from the divergence side: CONFIRMED.** Because D_ij >= 0, and the capped cost lies in [0, 2048], exp(-D_ij/tau) is a valid Bernoulli probability for every tau > 0, and conditioning on a positive record gives beta* exactly. The record is a declared likelihood of the law parameters, not of Gaussian data; it explains tau but does not derive the KL cost.

**L9 (notation), symbols in this lens: CONFIRMED.** P_i (mixture joint, 690), P_j (key precision, 982), P_{K,j} (the same precision under a second name, 537), P and Q (measures, 351), P_0 (centering projector, Supp 117); a_i (projected query mean, 973), a_i^{(l,h)} (head aggregate, 884), a (basis change, 386), a_h (ALiBi slope, Algorithm 1); R_{Q,i} (lift), R_i (RoPE), R (noise covariance, 902), R_i (receiving covariance, Supp 101).

L2, L4, L8, L10: outside this lens.

## Task 3: is KL(q_{Q,i} || p_{K,j}) derived or chosen?

Derived, conditional on two declared choices: the mixture joint with key laws as generative components and the query law as recognition factor, and the exclusive divergence KL(Q || P). Given those, no freedom remains (Finding 5(a)). The inclusive divergence with the same factorization gives beta = pi for all costs, so it is not an alternative for routing (Finding 5(b)). The reverse cost follows from a different joint (receiver law generative, sender laws as recognition candidates). Effect on the dot-product reduction: the forward cost needs a shared key covariance, and then the query covariance disappears; the reverse cost needs a shared query covariance and keeps a key-covariance source bias; Jeffreys and Bhattacharyya need both shared (Finding 5(c)). The dual-coordinate identity of Finding 2 explains the switch. The paper should state the direction as a consequence of the declared joint in Section 2.6 (proposed LaTeX in Finding 5), because the correspondence hypothesis of Proposition prop:projected_dot_product depends on it.

## Task 4: conflations of ambient and projected laws, or of stored and reference covariance

No displayed formula conflates the ambient K-dimensional law with its r-dimensional projection: every divergence is stated for reduced laws with full reduced covariance (400, 977-983), and the implementation computes exactly those (`vfe3\relational_scoring.py:43-113, 217-319`: V = L Sigma L^T with L = S U^{-1}, full reduced covariance from the diagonal state, zero jitter). The stored diagonal and the full C_i are also kept apart in the text (1095, 1134). Three smaller items remain. First, the cost bound [0, 8K] = [0, 2048] is scaled by the ambient K while each divergence lives in r_h = 32 dimensions; the bound is inactive (reconstructed layer-0 D_ij in [8, 115]; archived capped fraction 0), so this is a statement-of-scale issue, and "bounded to [0, 2048]" would avoid suggesting a K-dependence. The capped fraction, unlike the repair count of prior R4, is measured (`score >= kl_max`, `vfe3\model\model.py:1838`), over the full 8 x 128 x 128 grid of one 128-token validation sequence per layer, masked pairs included; the text should give that denominator. Second, the substantive stored-versus-reference issue is empirical and is Finding 1: the stored diagonal is about 1.04 I, so the full C_i is essentially frame geometry. Third, Supp eq:supp_expected_loglik carries K log(2 pi) for the ambient readout; after projection (857) the constant becomes r log(2 pi), which cancels in the softmax.

A sharpening of Supp B.2 (verified, no finding block): for eps > 0 the LayerNorm output lies in the bounded set {1^T y = 0, ||y||^2 < K} (largest ||y||^2 = 7.9998 < 8 in 20,000 samples at K = 8), and for eps = 0 on the sphere ||y||^2 = K. The pushforward is therefore not even a degenerate Gaussian, whose support would be a whole affine subspace. The sentence "Neither construction is a nondegenerate full Gaussian pushforward" can say this.

## Verified identities (residuals; float64 eps = 2.2e-16)

| Item (Main/Supp line) | Check | Result |
|---|---|---|
| eq:glk_invariance (349-355), KL | 200 random GL(4) pushforwards | rel. 2.8e-14 at cond(A)=10; 4.7e-10 at cond(A)=1e3 (tracks cond^2 eps) |
| same, f-divergence and Renyi | squared Hellinger; Renyi order 0.3 | 2.2e-10; 2.3e-10 (same random A as the first-run KL check, whose KL residual was 3.9e-10) |
| projected PD (400) | 200 random full-row-rank S | min eigenvalue 0.45 > 0 |
| C1 complement (457) | U H^{-1} im T^T; rebasing with a^T H a | angles 9.8e-12; 3.9e-12; reset H=I moves 0.995 rad |
| B_ij law (537-543) | passive action | 1.0e-14 relative |
| lift R_{Q,i} (547-559) | S R = I; cross-covariance; minimality cross term | 2.4e-16; 2.4e-16; 2.7e-15 |
| block additivity (662-669) | block-diagonal pair; counterexample c = 0.6 | 8.9e-16; 0.22314355 = -log(0.64)/2 |
| dilation (681) | passive (c mu, c^2 Sigma, c U) | 9.9e-16 relative; isotropic form 5.6e-17 |
| eq:projected_full_kl (979-983) | 300 cases vs Cholesky KL; SymPy expansion | 4.8e-15 relative; exactly 0 |
| Proposition (989-1006) | routing vs whitened formula; O(r) re-whitening | 3.9e-16; 3.9e-16 |
| key-bias counterexample (1020) | dot-product vs Gaussian weights | (0.5, 0.5) vs (0.62246, 0.37754) = (1, e^{-1/2})/(1+e^{-1/2}) |
| eq:projected_softmax_bound (1031) | valid; sharp constant | max ratio to printed bound 0.49; to 2 tanh(eps/2) 0.99999991 |
| RoPE (1058-1065) | full pushforward relative; plane-wise commutant | 1.6e-14; 4.4e-16 |
| mixture covariance (1069) | law of total covariance | 8.9e-16 |
| readout (809-857) | Gibbs 1/(1+e^2); predictive average | 0.119202922022; 0.323827781149 |
| Supp B.1 (89-110) | V_ij; expected cost; scalar 2(1-c) | 3.6e-15; 0.0; exact |
| Supp B.2 (117-129) | K=2 atoms; zero-sum; norm bound | {(1,-1), (-1,1)}; 3.1e-15; 7.9998 < 8 |
| dual pairing (Finding 2) | forward and reverse mixed forms | 9.8e-15; 6.2e-15 |
| inclusive joint (Finding 5) | argmin of KL(P || Q) over beta | equals pi to 5e-9 |

## Placeholders (additions to the prior figure-data plan)

Refine prior F3 Panel C into a per-layer table of within-row logit standard deviations, split into (i) static source bias (1/2 log det V_{K,j} plus the trace column effect), (ii) static pair trace interaction, and (iii) contextual mean terms weighted by P_j, with the layer-0 values of Finding 1(d) as a check. Add a small panel with the stored log-variance distribution (initial log 15 against final) and the C_i versus (U_i^T U_i)^{-1} gap, so readers see what the covariance channel is. Revise prior F5 to report representation-independent quantities (spectra of V_{K,j}^{-1/2} V_{Q,i} V_{K,j}^{-1/2}, whitened-map singular values) and, as optimizer diagnostics, tr Q_h and the content balance per layer; keep raw singular values only as numerical-health data labeled as such.

## Program-level observations (the author aim of a theory without prescribed neural architectures)

First, the dual-coordinate identity of Finding 2 holds for every regular exponential family (Wainwright and Jordan 2008, Eq. (5.11) is stated in that generality). For agents whose beliefs lie in any such family, exclusive-KL Gibbs routing is dot-product attention between receiver expectation parameters and sender natural parameters, with the sender log-partition as a bias. That derives the query-key bilinear form from a property of the belief family rather than from a wiring choice, and it extends beyond Gaussians (categorical, Poisson, von Mises-Fisher agents). It is a theorem-level statement the program can own.

Second, the comparison channel is basis-free: the costs are invariant under GL(r_h) on the comparison space, which therefore needs no inner product; the metric that pairs query and key is the Fisher information of the key law. A dot product needs a fixed pairing. The paper can state this intrinsic property instead of declaring the comparison space as R^{r_h} with an implicit basis.

Third, content can be derived from the same Gaussian model instead of chosen. The paper's own shared-latent conditioning law (eq:relational_shared_latent_correction), read with T = I, S_Q in place of S_K, observation noise R = V_{K,j} and observed value y = b_j, gives the receiver update xi_i + C_i S_Q^T (V_{Q,i} + V_{K,j})^{-1} (b_j - a_i), whose noiseless limit is the Gaussian lift of eq:comparison_gaussian_lift. Routing-weighted, this defines a content link fixed by the comparison geometry and removes (T_h, O_h) as free choices. This is a proposal, not a result of the paper, and it was not tested here.

Fourth, geometric versus arithmetic pooling (Finding 4) is an explicit design axis for how uncertainty should act, which standard attention hides; the program can select it on declared grounds. Fifth, the recorded run currently contains no learned uncertainty (Finding 1), so it cannot yet show what Gaussian agents add beyond a frame-induced metric.

## Files

Scripts and outputs (all under `C:\Users\CHRISA~1\AppData\Local\Temp\claude\C--Users-chris-and-christine-Desktop-VFE-3-0\e395f369-c986-4475-a188-57f61cc66b14\scratchpad\panel\infogeo\`): `infogeo_checks.py` with `infogeo_checks.json` and `infogeo_checks.log`; `infogeo_checks_patch.py` with `infogeo_checks_patch.json`; `l3_extract.py` (torch, CPU, mmap, read-only; its intermediate `l3_slices.npz` was deleted after use and is regenerated by rerunning it); `l3_static_cov.py` with `l3_static_cov.json`; `l3_consistency.py` with `l3_consistency.json`; `l3_layer0_D.py` with `l3_layer0_D.json`; primary-source text extracts `vanerven_2014.txt` and `wainwright_jordan_2008.txt`.
