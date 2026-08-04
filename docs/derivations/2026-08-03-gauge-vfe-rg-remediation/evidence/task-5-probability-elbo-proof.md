<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 5 probability and extended-ELBO derivation

## Scope

This artifact proves the probability interfaces used by the general finite-network theory: family-level domination, jointly measurable kernel Radon--Nikodym versions, measurable extended KL, the arbitrary-law extended ELBO and VFE, extended total correlation, restriction and frame invariance, exact coordinate updates, and extended data processing under a normalized coarse channel. It also records the interfaces used by the separate local/collective and observation-node construction. No continuum-limit or physical-time claim is made.

## Assumptions

- Latent and observation spaces used by the kernel RN and kernel-KL theorems are standard Borel.
- A selected observation has a declared slice measure (M_o) of mass (z\in(0,\infty)), with posterior (\Pi_o=M_o/z).
- Parameterized density calculations use one fixed family-level sigma-finite reference and finite jointly measurable density versions. In the local network construction the context-dependent baseline and every record law are normalized kernels, and one measurable baseline RCP version is fixed as model data.
- Classical split expectations additionally satisfy absolute continuity and separate log-integrability; the extended functional does not.
- Every coarse map is a normalized, measurable, parameter-independent Markov kernel.

## P1: exact common-domination criterion for a mixed family

Write each family member as

\[
\mu_t=f_t\lambda+\sum_{a\in A_t}p_t(a)\delta_a,
\qquad A_t=\{a:\mu_t(\{a\})>0\}.
\]

There is one sigma-finite dominator for the family if and only if (A_*=\bigcup_tA_t) is countable. If (A_*=\{a_n\}), then

\[
\nu_{\rm mix}=\lambda+\sum_{n\ge1}2^{-n}\delta_{a_n}
\]

dominates every member. Conversely, a common sigma-finite dominator must give positive mass to each (a\in A_*), while a sigma-finite measure has only countably many positive-mass point atoms. The family (\frac12N(0,1)+\frac12\delta_t), (t\in\mathbb R), is the sharp moving-atom obstruction. Singular-continuous components are not intrinsically excluded, but require a separately declared common singular reference.

## P2: finite jointly measurable kernel RN version

For probability kernels (K_x\ll L_x), choose finite refining partitions (\mathcal P_n) generating the target sigma-algebra and define

\[
r_n(x,y)=\sum_{A\in\mathcal P_n}\frac{K(x,A)}{L(x,A)}1_A(y),
\]

with (0/0=0). Each (r_n) is jointly measurable. For fixed (x), it is the conditional expectation of (dK_x/dL_x) on the partition sigma-algebra, so martingale convergence identifies its limit with the derivative (L_x)-almost everywhere. Defining (r) as the finite limsup and setting it to zero where the limsup is infinite changes only an (L_x)-null set. Thus (K(x,dy)=r(x,y)L(x,dy)) for every (x), with one finite jointly measurable version. A fixed sigma-finite reference (\nu) reduces to this theorem through an equivalent probability (w\nu), (0<w<\infty), (\int w,d\nu=1).

For two probability kernels (\kappa,\eta), put (\Lambda=(\kappa+\eta)/2) and use the preceding theorem to choose finite jointly measurable densities (a=d\kappa/d\Lambda) and (b=d\eta/d\Lambda). On (\mathscr G_n=\sigma(\mathcal P_n)), let

\[
a_n=E_\Lambda[a\mid\mathscr G_n],\qquad
b_n=E_\Lambda[b\mid\mathscr G_n],
\]

and define the nonnegative lower-semicontinuous convex perspective

\[
\Phi(u,v)=u\log(u/v)-u+v,
\]

with (\Phi(0,v)=v), (\Phi(u,0)=+\infty) for (u>0), and (\Phi(0,0)=0). The finite-partition relative entropies

\[
D_n(x)=\sum_{A\in\mathcal P_n}\kappa(x,A)
\log\frac{\kappa(x,A)}{\eta(x,A)}
=\int\Phi(a_n,b_n)\,d\Lambda_x
\]

are measurable. Conditional Jensen makes (D_n) nondecreasing, and the log-sum inequality gives (D_n\leq\mathrm{KL}(\kappa_x\Vert\eta_x)). Martingale convergence gives ((a_n,b_n)\to(a,b)) almost everywhere, while Fatou gives

\[
\mathrm{KL}(\kappa_x\Vert\eta_x)
=\int\Phi(a,b)\,d\Lambda_x
\leq\liminf_nD_n(x).
\]

Hence (D_n\uparrow\mathrm{KL}(\kappa_x\Vert\eta_x)). This proves KL measurability without the false assertion that the selected generating sequence is cofinal among all finite partitions.

For integration against a fixed sigma-finite (\nu), first choose a disjoint partition (\mathsf F=\bigsqcup_mF_m) with (\nu(F_m)<\infty). For each (m), the sets (C) for which (x\mapsto\nu(C_x\cap F_m)) is measurable form a Dynkin system containing the measurable rectangles: finite mass makes the complement identity legitimate, and disjoint unions give pointwise sums. The (\pi)--(\lambda) theorem handles indicators on each piece, and

\[
\nu(C_x)=\sum_m\nu(C_x\cap F_m).
\]

Simple approximation and monotone convergence then handle every nonnegative integrand. Applying this result separately to positive and negative parts proves the signed case wherever they are not both infinite.

## E1: arbitrary-law extended ELBO and relative-log form

For every probability (Q), define

\[
\mathcal L^{\rm ext}(Q)=\log z-\mathrm{KL}(Q\Vert\Pi_o),
\qquad
\mathcal F^{\rm ext}(Q)=-\log z+\mathrm{KL}(Q\Vert\Pi_o).
\]

These are defined in the extended reals even when (Q\not\ll\Pi_o). The safe gap identities are

\[
\log z-\mathcal L^{\rm ext}=\mathrm{KL}(Q\Vert\Pi_o),
\qquad
\mathcal F^{\rm ext}+\log z=\mathrm{KL}(Q\Vert\Pi_o).
\]

The equation (\log z=\mathcal L^{\rm ext}+\mathrm{KL}) is not formed when the two summands would be (-\infty) and (+\infty).

If (Q\ll M_o) and (r=dQ/dM_o), then (dQ/d\Pi_o=zr) and

\[
\mathcal L^{\rm ext}(Q)=-\int\log r,dQ.
\]

This extended integral is well defined because

\[
\int_{r<1}-\log r,dQ=\int_{r<1}-r\log r,dM_o\le z/e.
\]

If (Q\not\ll M_o), the extended ELBO is (-\infty). Only under the separate classical support and log-integrability hypotheses does this reduce to (E_Q[\log p(o,Y)-\log q(Y)]).

## E2: extended total correlation

For a finite block product, arbitrary (Q), marginals (Q_b), and references (\rho_b), finite product partitions obey the exact discrete identity

\[
D(Q_n\Vert\otimes_b\rho_{b,n})
=D(Q_n\Vert\otimes_bQ_{b,n})+\sum_bD(Q_{b,n}\Vert\rho_{b,n}).
\]

All terms are nonnegative. Refining-partition convergence of KL gives

\[
\mathrm{KL}(Q\Vert\otimes_b\rho_b)
=\mathrm{TC}(Q)+\sum_b\mathrm{KL}(Q_b\Vert\rho_b)
\]

in [0,+\infty], without entropy subtraction. If (Q\not\ll\otimes_b\rho_b), either a marginal KL is infinite or every marginal is dominated and (Q\not\ll\otimes_bQ_b), so total correlation is infinite. The law of ((U,U)), (U\sim\mathrm{Unif}[0,1]), realizes the infinite-TC branch despite matching uniform marginals.

The separate finite-density entropy identity requires finite joint and marginal entropies. Its further free-energy and pseudo-ELBO sign formulas also require (E_Q|\log p_\theta(o,Y\mid X)|<\infty), so the common energy term is defined; entropy finiteness alone does not supply that premise.

## E3: restriction, frame invariance, and coordinates

For any family (\mathcal Q'),

\[
\sup_{Q\in\mathcal Q'}\mathcal L^{\rm ext}(Q)
=\log z-\inf_{Q\in\mathcal Q'}\mathrm{KL}(Q\Vert\Pi_o).
\]

Nested families give monotonicity of the suprema. A difference of optimized losses is stated only when both KL infima are finite. Under a bimeasurable frame map (R), push (M_o,\Pi_o,Q) simultaneously. Slice mass and KL are invariant in both the absolutely continuous and singular branches, so the extended ELBO is invariant; the classical formula follows only on its finite split domain.

For a latent block with fixed complement marginal (R_-), attach a completed posterior conditional (C(dy_B\mid y_-)). The law (C R_-) attains the minimum (\mathrm{KL}(R_-\Vert\Pi_-)). If that value is finite, the KL chain rule makes the minimizer unique; if it is infinite, data processing makes every candidate have infinite KL, so the optimum exists at value (-\infty) but is nonunique. Generalized parameter acceptance is therefore stated directly as nondecrease of (\mathcal L^{\rm ext}). Full old-posterior exactness plus acceptance implies evidence monotonicity; a block update alone does not.

## E4: extended data processing and fixed-evidence coarse ELBO

For (P\ll Q), under the joint law (Q(dx)K(x,dy)), the coarse density ratio is (\bar r(Y)=E[r(X)\mid Y]). Conditional Jensen for the nonnegative convex generator (\phi_0(t)=t\log t-t+1) gives

\[
\mathrm{KL}(PK\Vert QK)\le\mathrm{KL}(P\Vert Q)
\]

even when the right side is infinite. If (P\not\ll Q), the inequality is immediate. The finite-KL condition remains necessary for the usual equality/recovery characterization: on (X=\{a,b,c\}), let (K(a)=u), (K(b)=K(c)=v), (P=(\delta_a+\delta_b)/2), and (Q=(\delta_b+\delta_c)/2). Fine and coarse KL are both infinite, but no common reverse kernel recovers both laws.

For a fixed measurable fine posterior kernel (o\mapsto P_o), declare the compatible coarse version pointwise by (\bar P_o:=P_oK). Kernel integration makes it measurable, and for measurable (A\subseteq\mathsf O), (B\subseteq\mathsf Y),

\[
\int_A\bar P_o(B)\,P^O(do)
=\int_A\int K(x,B)P_o(dx)\,P^O(do)
=\bar P(A\times B).
\]

Thus (\bar P_o) is an RCP of the pushed joint, including its declared exceptional-point values. Using the same selected evidence-density representative for the fine and coarse slice, applying the inequality to (Q_o,P_o) under a normalized, parameter-independent channel yields

\[
\bar{\mathcal L}^{\rm ext}(Q_oK)
=\log p(o)-\mathrm{KL}(Q_oK\Vert P_oK)
\ge\mathcal L^{\rm ext}(Q_o)
\]

for arbitrary (Q_o), while normalization preserves the observation marginal and therefore the selected evidence representative. No almost-sure RCP identity is applied at an arbitrarily fixed exceptional observation.

## Local and observation-node interfaces

Before fixing context, the normalized baseline is a kernel (P_0:X\rightsquigarrow Y), every record is a normalized kernel (K_a:X\times Y_{\partial a}\rightsquigarrow O_a), and its density (\ell_a(X,y_{\partial a},o_a)) is finite and jointly measurable against one fixed family-level reference (\nu_a). After fixing one context (X), let

\[
L_o(y)=\prod_{a\in\mathcal A}\ell_a(o_a\mid y_{\partial a}),
\]

and put

\[
Z(o)=\int L_o,dP_0,
\qquad
\Pi_o=Z(o)^{-1}L_oP_0.
\]

For a nonempty block (B), first fix one measurable baseline RCP version and disintegrate

\[
P_0(dy)=P_{0,B^c}(db)P_{0,B}(dy_B\mid b).
\]

All pointwise formulas below are relative to this selected version; alternate RCP versions agree only almost everywhere. Let (g_{B,o}) be the product of precisely those record factors whose scopes intersect (B), and define the incident slice mass

\[
Z_B(b)=\int g_{B,o}(y_B;b)P_{0,B}(dy_B\mid b).
\]

The full outside likelihood is defined directly as

\[
w_B(b)=\int L_o(y_B,b)P_{0,B}(dy_B\mid b),
\]

so no formal (0\cdot\infty) product is used. On the posterior-full regular set where the required slice and outside factors are positive and finite,

\[
\Pi_{o,B}(dy_B\mid b)=Z_B(b)^{-1}g_{B,o}(y_B;b)P_{0,B}(dy_B\mid b).
\]

After an arbitrary measurable probability-kernel extension off that regular set, this is a posterior RCP version. Its joint-law invariance, and that of the pointwise local VFE, is only (\Pi_{o,B^c})-almost everywhere; downstream integration uses (Q_{B^c}\ll\Pi_{o,B^c}). For every conditional recognition law (r_B(\cdot\mid b)), the local extended VFE is

\[
\mathcal F_{B,o}^{\rm ext}(r_B;b)
=-\log Z_B(b)+\mathrm{KL}(r_B(\cdot\mid b)\Vert\Pi_{o,B}(\cdot\mid b)).
\]

Thus the singleton block is an agent VFE and an arbitrary nonempty block is a meta-agent VFE. If (Q=Q_{B^c}r_B), posterior disintegration gives the nonnegative extended chain

\[
\mathrm{KL}(Q\Vert\Pi_o)
=\mathrm{KL}(Q_{B^c}\Vert\Pi_{o,B^c})
+E_{Q_{B^c}}\mathrm{KL}(r_B\Vert\Pi_{o,B}).
\]

For two finite-posterior-KL laws with the same outside marginal, subtracting these finite identities cancels the outside term and the pointwise (-\log Z_B) term, proving

\[
\mathcal F_o^{\rm ext}(Q')-\mathcal F_o^{\rm ext}(Q)
=E_{Q_{B^c}}[\mathcal F_{B,o}^{\rm ext}(r'_B)-\mathcal F_{B,o}^{\rm ext}(r_B)].
\]

This is the local-global potential identity. It does not sum overlapping local objectives: each actual record factor occurs once in (L_o), even though it can occur in every incident block coordinate objective.

For attention, introduce finite categorical labels (J_i) with positive priors (\pi_i), independently of the baseline state. The complete selected-record augmented likelihood must have the exclusive factorization

\[
L_o^{\rm aug}(y,j)=L_o^Y(y)\prod_i\ell_i(o_i\mid y,J_i=j_i),
\qquad
\ell_i(o_i\mid y,j)=c_i(o_i,y)e^{-D_{ij}(y)/\tau_i},
\]

where (L_o^Y) is label independent and no other record or generative factor may read any (J_i). Normalization over the full record space remains declared model data. Bayes' formula then gives the exact conditional posterior row

\[
\beta^P_{ij}(y)
=\frac{\pi_{ij}e^{-D_{ij}(y)/\tau_i}}
{\sum_k\pi_{ik}e^{-D_{ik}(y)/\tau_i}}.
\]

Under the separately declared constant-row recognition factorization (Q(dy,dj)=Q_Y(dy)\prod_i\beta_i^Q(dj_i)), expansion of categorical KL gives, up to the source-independent term,

\[
\mathcal F_i^{\rm att}(\beta_i^Q)
=\mathrm{KL}(\beta_i^Q\Vert\pi_i)
+\tau_i^{-1}\sum_j\beta^Q_{ij}E_{Q_Y}D_{ij}.
\]

Lagrange multiplication on the positive-prior simplex gives the unique constant-row optimum proportional to (\pi_{ij}\exp[-E_{Q_Y}D_{ij}/\tau_i]). For a general correlated conditional label law, the extended total-correlation chain instead yields

\[
E_{Q_Y}\mathrm{TC}(Q_{J\mid Y})
+\sum_iE_{Q_Y}\left[
\mathrm{KL}(Q_{J_i\mid Y}\Vert\pi_i)
+\tau_i^{-1}E_{Q_{J_i\mid Y}}D_{iJ_i}(Y)
\right],
\]

plus the label-independent likelihood term. Therefore row marginals do not determine the collective attention ledger.

Finally, every normalized standard-Borel observation kernel has a measurable randomization (O=F(Y,U)) with (U\sim\operatorname{Unif}[0,1]), and marginalizing any normalized environment state and message policy produces such a kernel. This proves an operational environment-node interaction representation, while preserving the conditioning sigma-algebra generated by (O). The Bernoulli witness (O=Y) shows why deleting the record is not equivalent: conditioning gives a point mass and deletion returns the prior.

## Boundaries

- The construction is finite-design and standard-Borel; it does not prove a continuum section-space law.
- Exponential-family coordinates exist only on the natural domain where the normalizer is finite. The classical split additionally requires its own H4-type integrability.
- Evidence monotonicity requires a full exact old-posterior E phase; local/block ascent alone proves ascent of the common objective, not of evidence.
- A normalized coarse channel preserves evidence but discards information; the resulting ELBO increase is not model improvement.
