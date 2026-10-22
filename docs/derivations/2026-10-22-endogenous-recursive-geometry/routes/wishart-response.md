<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e","schema_version":"rigorous-theory-search/v1","target_digest":"cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e"} -->
# Exact extensive-response histories for the Wishart construction

Fresh extensive responses have an exact normalized parent law and preserve every finite adaptive joint history through arbitrary admitted coarsenings. They do not require the individual shape parameters. The result below uses the parent's proposed special family and assumes that its membership rule descends through the stated retained state. It proves the response and update part of that construction, not its endogenous selection or geometric part.

## Family, reference, and original evolution

Let `S_2^{++}` be the cone of real symmetric positive-definite two-by-two matrices, with Lebesgue measure `dX=dx_11 dx_12 dx_22`. Use the convention

\[
 W_2(a,P)(dX)=\frac{\det(P)^a}{\Gamma_2(a)}\det(X)^{a-3/2}e^{-\operatorname{tr}(PX)}dX,
 \qquad \Gamma_2(a)=\sqrt\pi\Gamma(a)\Gamma(a-1/2),
 \quad a>1/2,\quad P\in S_2^{++}.
\]

Primitive agent `i` has the two genuinely varying laws

\[
 q_i=W_2(\alpha_i,P_1),\qquad s_i=W_2(\beta_i,P_2),\qquad
 \zeta_i=q_i\otimes s_i,
\]

with common precisions `P_1,P_2` and individual shapes `alpha_i,beta_i>1/2`. The shapes may vary across children. In the geometric application they are constant as functions of the context coordinate; that is distinct from their evolution in inference time. The two sectors are product-recognized and have separate fresh represented-content draws.

Take fixed reference laws `A_0=W_2(alpha_0,I)` and `B_0=W_2(beta_0,I)`, with `alpha_0,beta_0>1/2`. The normalized evaluator is `G(m,dX)=A_0(dX)` and model reference is `B_0`. Thus `R=A_0 tensor B_0`. Every original comparison channel into the belief sector is the constant normalized channel `K^q_{ij}(x,dX)=A_0(dX)`; use `B_0` in the model sector. This is a restrictive constitutive choice, with no state-dependent gate or change at a join. It gives no transmission of the sender's sample. Its appropriateness for the frozen formation target is a separate construction question.

For normalized source rows, the exact original energy is

\[
 E=2\sum_i\left[\int\log\frac{dq_i}{dA_0}dq_i+
                         \int\log\frac{ds_i}{dB_0}ds_i\right]
 +T_q\sum_i\operatorname{KL}(\beta_i^{\rm row}\Vert\pi_i^q)
 +T_s\sum_i\operatorname{KL}(\gamma_i^{\rm row}\Vert\pi_i^s).
\]

The notation `beta_i^{row}` separates source rows from the model Wishart shapes `beta_i`. Source costs do not depend on the source label. Source rows therefore optimize to their original priors in the Gibbs-reduced version. If dynamic rows are included, their original row relaxation remains a separate retained block and does not affect these matter equations. This response derivation uses the exact Gibbs-reduced version, which has no omitted source-state data. The original temperatures stay positive.

All Wishart laws above have positive densities on the same support. The necessary expectations of `tr(X)` and `abs(log det X)` are finite when `a>1/2`; this follows from the gamma integrals below, also with a small positive or negative perturbation of the shape and a small perturbation of the precision. The same exponential-moment bounds give finite second moments of these scores, so the Fisher metric is defined. Hence the displayed KL terms and their first variations along compact parameter neighborhoods are finite. The full density Fisher flow, not merely a projected parameter-family flow, obeys

\[
 \partial_t\log\frac{dq_i}{dA_0}
 =-2\left(\log\frac{dq_i}{dA_0}
       -\mathbb E_{q_i}\log\frac{dq_i}{dA_0}\right).
\]

For `a(t)=exp(-2t)`, its exact solution is proportional to `(dq_i(0)/dA_0)^{a(t)} A_0`. Comparing the coefficients of `log det X` and `X` proves

\[
 \alpha_i(t)=\alpha_0+a(t)(\alpha_i(0)-\alpha_0),\qquad
 P_1(t)=I+a(t)(P_1(0)-I),
\]

with the exchanged equation for `beta_i,P_2`. These convex combinations remain strictly in the admitted shape and precision domains for all finite nonnegative times. The formulas give global existence; direct substitution proves invariance under the original full density flow. Any positive dominated solution with the stated differentiability satisfies the same log-ratio equation, whose integrating factor determines its log density up to the scalar fixed by normalization. This proves uniqueness in that regular solution class, not only uniqueness of a parameter-projected ODE. No inserted mobility is used. Distinct shape vectors remain distinct at every finite time because their differences are multiplied by `exp(-2t)`.

## Normalization and addition, with a checkable derivation

At `P=I`, write

\[
 X=\begin{pmatrix}u^2&uv\\uv&v^2+w^2\end{pmatrix},
 \qquad u,w>0,\quad v\in\mathbb R.
\]

Then `det X=u^2 w^2`, `tr X=u^2+v^2+w^2`, and the coordinate Jacobian is `4u^2 w`. The unnormalized density integral is therefore

\[
 4\left(\int_0^\infty u^{2a-1}e^{-u^2}du\right)
  \left(\int_{\mathbb R}e^{-v^2}dv\right)
  \left(\int_0^\infty w^{2a-2}e^{-w^2}dw\right)
 =\sqrt\pi\Gamma(a)\Gamma(a-1/2).
\]

For general precision, substitute `X=P^{-1/2}ZP^{-1/2}`. On the three-dimensional vector space of symmetric matrices, congruence by `L` has absolute Jacobian `abs(det L)^3`: this is immediate for diagonal `L` from the three coordinate factors and extends by orthogonal diagonalization for the positive `L` used here. The integral is thus multiplied by `det(P)^{-a}`. This proves normalization directly and the Laplace formula

\[
 \mathbb E_{W_2(a,P)}e^{-\operatorname{tr}(TX)}
 =\left(\frac{\det P}{\det(P+T)}\right)^a,
 \qquad P+T\succ0.
\]

For independent `X_i~W_2(alpha_i,P)`, multiplication of these transforms gives the transform of `W_2(sum_i alpha_i,P)`. We use the following transform-uniqueness fact: probability measures on a finite-dimensional real vector space whose moment-generating functions are finite on a neighborhood of zero and agree on that neighborhood are equal. The hypothesis holds here because `P+T` stays positive for all sufficiently small symmetric `T`; independence gives the same neighborhood for the sum. Therefore

\[
 \sum_{i\in I}X_i\sim W_2(A_I,P),\qquad A_I=\sum_{i\in I}\alpha_i.
\]

The primary-source convention check is Letac and Massam, *The Laplace transform (det s)^(-p) exp tr(s^(-1)w) and the existence of non-central Wishart distributions*, [arXiv:1108.2849](https://arxiv.org/pdf/1108.2849), equations (1)–(3) and the central density discussion on pages 1–2. Its central transform agrees after setting `w=0`, `p=a`, and `2 Sigma=P^{-1}`. The normalization and sum calculation above are supplied explicitly rather than transferred from an incompatible degrees-of-freedom convention.

## Parent laws, updates, and actual information loss

For a current block `I`, retain

\[
 r_I=(n_I,A_I,B_I,P_1,P_2),\qquad
 n_I=|I|,\quad A_I=\sum_{i\in I}\alpha_i,\quad B_I=\sum_{i\in I}\beta_i.
\]

The common precisions can be stored once for the network. The parent joint sample law is

\[
 Q_I^c=W_2(A_I,P_1)\otimes W_2(B_I,P_2).
\]

The normalized evaluator can be taken as the constant kernel `G_I^c(M,dS)=W_2(n_I alpha_0,I)(dS)`, with model reference `W_2(n_I beta_0,I)`. This is the convolution of the primitive references. The exact retained dynamics is

\[
 \dot A_I=-2(A_I-n_I\alpha_0),\quad
 \dot B_I=-2(B_I-n_I\beta_0),\quad
 \dot P_1=-2(P_1-I),\quad\dot P_2=-2(P_2-I).
\]

It is also the full Fisher flow of twice the KL from this parent product law to the stated product reference, restricted to its invariant Wishart family. This follows by the same log-density calculation. It does not require the fine energy to equal a function of the retained state, and does not assert a general Fisher isometry in the shape directions.

For disjoint blocks, the joining operation adds counts and shapes and keeps the common precisions:

\[
 (n_I,A_I,B_I)\star(n_J,A_J,B_J)
 =(n_I+n_J,A_I+A_J,B_I+B_J).
\]

It is associative and commutes with the displayed original-time evolution by direct addition of the right sides. The sample joining map `(S_I,T_I,S_J,T_J)->(S_I+S_J,T_I+T_J)` is fixed and normalized as a deterministic Markov kernel. Independence and Wishart addition prove that it yields `Q_{I union J}^c` exactly.

There is continuous information loss on every block with at least two children. For example, replace `beta_1,beta_2` by `beta_1+epsilon,beta_2-epsilon` with sufficiently small nonzero `epsilon`; shapes remain above `1/2`, `B_I` is unchanged, and the individual model laws change continuously. Generic choices are not a permutation. This loss is unaffected by an alpha-only selection criterion. Two successive joins have independent shape-splitting fibers whenever the relevant child-parent model-shape sums are allowed to vary while their union sum remains fixed. If selection times or other retained data impose additional shape constraints, those must be included; no claim is made that they preserve every such fiber automatically.

## Predeclared response protocol and joint history theorem

The base protocol is noninvasive. Its actions choose waiting times, current-block joins allowed by the given membership rule, and normalized readout kernels. They never reset the fine belief or model laws. Observed samples become controller records; they are not silently converted into Bayes updates of `q_i` or `s_i`.

At any query time, let `Pi={I_1,...,I_m}` be the current disjoint partition. Declare the batch sample law

\[
 \bigotimes_{i=1}^N\bigl[q_i(dX_i)s_i(dY_i)\bigr].
\]

All primitive samples are fresh, independent across primitives and sectors conditional on the current deterministic configuration, and independent of previous query randomness. Return the vector

\[
 Z_\Pi=\bigl((S_I,T_I)\bigr)_{I\in\Pi},\qquad
 S_I=\sum_{i\in I}X_i,\quad T_I=\sum_{i\in I}Y_i.
\]

The exact normalized conditional law is

\[
 K_\Pi(r,dz)=\bigotimes_{I\in\Pi}
       \left[W_2(A_I,P_1)(dS_I)W_2(B_I,P_2)(dT_I)\right].
\]

Any chosen normalized Markov readout `H_e: (S_2^{++} times S_2^{++})^m -> O_e` is also admitted, with response kernel `K_Pi H_e`. It can depend measurably on the observed history through `e`. This includes querying only some current blocks, applying arbitrary fixed tests to their matrices, and reporting overlapping unions of whole current blocks by adding their same-batch aggregate matrices. It never exposes a constituent matrix inside a retained block. The protocol is specified as this class before comparing fine and parent responses.

**Exact history theorem.** Fix any admitted initial fine configuration. Suppose every membership handoff used by a policy is determined by the retained network state and already observed controller history, and uses the addition join above. Allow any finite sequence of measurable adaptive waiting times, permitted joins, and readouts from this predeclared class, with finite query times. The fine process and retained process induce exactly the same joint law of all records, chosen actions, query times, and retained network states. The result also holds with external policy randomization independent of the fresh samples.

**Proof.** At time zero initialize each retained block by the stated sums. The deterministic fine flow gives exactly the retained ODE for all future waiting durations. Suppose the histories and retained state agree in law through step `k`. Condition on the common current history and state, including the external policy randomization when used. The policy chooses the same next waiting duration, join, and readout. The projected fine flow and the retained flow give the same next retained state. Addition gives the same handoff state. Freshness and disjointness make the next extensive-sample law exactly `K_Pi`; composition with the same normalized `H_e` gives the same conditional next-record law. Multiplying this conditional kernel by the common preceding history law proves the induction step. No independent-marginal approximation is used: the entire same-batch response vector is retained before `H_e` is applied.

The argument remains valid if some query time is an adapted measurable stopping rule for the retained deterministic path and observed history, provided the rule is identical in the two descriptions and finite on the history in question. For countably many queries, equality of every finite cylinder follows by the same induction; a separate nonexplosion or endpoint convention is needed if query times accumulate.

Already observed records are carried by the controller through a join. A final aggregate state alone is not claimed to reconstruct the probability law of records made before that join. Exactness is equality of the processes initialized together and their future conditional kernels at each handoff. Past records may contain information about discarded shapes; that does not change the fact that every admitted future kernel depends only on the current aggregates and the carried controller history.

There is no repeatedly chosen hidden child in this protocol. Each query samples every participating primitive once and reports extensive sums; fresh repetitions use new samples. A protocol choosing one hidden child once and repeatedly sampling that child's law is different and is subject to the identification theorem in `response.md`.

## Overlapping primitive queries and why the scope matters

If one batch returns sums over arbitrary possibly overlapping primitive subsets `C_1,...,C_r` using shared primitive draws, its joint belief-sector Laplace transform is

\[
 \mathbb E\exp\left[-\sum_{a=1}^r\operatorname{tr}(U_aS_{C_a})\right]
 =\prod_{i=1}^N
 \left[\frac{\det P_1}
 {\det(P_1+\sum_{a:i\in C_a}U_a)}\right]^{\alpha_i}.
\]

Grouping equal membership patterns shows that this joint law is determined by the alpha-shape sums of every nonempty Venn atom; the model sector needs the beta sums. They need not be determined by the total shape of each queried subset alone. For example,

\[
 \operatorname{Cov}\bigl(\operatorname{tr}(US_C),\operatorname{tr}(VS_D)\bigr)
 =A_{C\cap D}\operatorname{tr}(P_1^{-1}UP_1^{-1}V).
\]

This follows either by two derivatives of the displayed logarithmic transform or by adding the covariances of shared independent primitive terms. It exposes the intersection shape. If every queried subset is a union of whole current blocks, all Venn atoms are also unions of whole current blocks, and the retained state determines these sums. This case is already included through `H_e`. If a query cuts through a current block, the theorem does not claim closure. Allowing all primitive subsets would recover all primitive shapes and remove this compression.

## Feedback and geometry limits

A separately prescribed common exponential tilt `q_i^+ proportional exp(-tr(HX))q_i` would give `P_1^+=P_1+H` for every child whenever the new precision is positive, and would descend through addition. That is an external state intervention, not a segment of the autonomous original flow, and is excluded from the base theorem. Its formula is not by itself a normalized observation model. Ordinary Bayesian conditioning of shared extensive observations generally correlates primitive contents and need not preserve the product recognition family. Separate child observations generally create child-specific precision updates and break common precision. Neither is included implicitly.

The response theorem does not establish the collective connection. A fixed addition channel permits applying the manuscript's score-projection result on an admitted smooth contextual family. The needed connection and residual conditions must still be checked for that family, with the common-precision and context-constant-shape assumptions made explicit. The geometry route handles that calculation.

The strongest established claim is exact normalized extensive-response and adaptive-history inheritance, including association-independent fixed addition joins and continuous model-shape information loss. The remaining local obligation is to verify that the actual proposed selection/handoff rule depends only on retained quantities while leaving at least one such shape-splitting fiber at both joins. Global formation, persistence, and nonzero retained geometry remain assigned to the other routes. Only source reads, one primary-source convention check, and this derivation were performed; no numerical experiment or simulation ran.
