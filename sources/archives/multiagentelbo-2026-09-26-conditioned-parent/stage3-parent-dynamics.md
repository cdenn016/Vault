# Stage 3: an inherited parent learning from its own conditioned-start law

September 26, 2026. This note constructs the existing source-retaining parent from the selected late-coherence prefix and proves a separate retained-path bound when the parent continues source learning from its own actual law. It does not reset the retained activation law, impose the fine process's future row path on the parent, or claim unrestricted Markov closure.

The manuscript artifact is `Theory/ca_parent_dynamics.tex`, with proposition `prop:phil-actual-parent-dynamics`. The neighboring conditional-information result is owned by the separate static-law assignment and is not reproved or assumed to imply path convergence here.

## 1. Sources, model, and target

Source continuity was checked against the live `Research/manuscripts/pifb2/09_section.tex` and `13_section.tex`, the wiki concept `Meta-agents and hierarchical emergence`, `Theory/c13_formation.tex` parts (b) and (d) of `prop:rg-formation-endogenous-cycle`, its proof in `Theory/ca_formation_proofs.tex`, and Sections 2, 5, and 6 of `docs/derivations/2026-09-11-meta-agent-formation-frontier-and-locality/selective-interface-actual-parent.md`. The older selective-interface construction already keeps the complete source mark, initializes from a prefix-conditioned law, and separates conditional information from dynamic approximation. The present construction is its original scalar predecessor at the selected late window, with an additional own-law row evolution. No new external reference is needed.

Work at one base point in the unchanged four-cycle. The fine state is $(X,S)\in\mathbb R^{12}\times\{\pm1\}^4$. Both directions of each undirected edge use its one shared link translation. The continuous generator on sheet $S$ has drift $-A_SX$ and diffusion covariance $2TI$, where $A_S=H_S+T\Omega$, $\Omega=I+R_{\rm ev}$, and $0<T\le1/100$. A rate-one clock redraws the complete assignment from $b_p(S'\mid X)$. The fine rows continue to evolve from the fine process's original unconditional law.

Let $M$ be the selected matching. Put $s=t_L$, $\theta=s+1$, and let $E$ be the actual selected-coherence event of Stage 2 throughout $[s,\theta]$ at the existing Euclidean stacked-residual resolution $a$. Thus $E$ is measurable with respect to the history through $\theta$, including actual proposals; it contains no condition on the later interval. Assume

$$
\Pr(E^c)\le\rho<1,
\qquad \sup_{s\le t\le\theta+h}\operatorname{TV}(q_t,\nu_T^M)\le\delta,
\qquad \sup_{s\le t\le\theta+h}\max_i|p_i(t)-p_i^M|\le\delta,
$$

where the entire interval lies within the Stage 1 selection window and

$$
\nu_T^M=\mathcal N(0,T A_M^{-1})\otimes\delta_M.
$$

The new target is total variation between the parent path over a following duration $h$ and the fine retained path conditioned on $E$. The two laws live on the same source-stratified carrier and include the complete assignment history. The initial mean remains any fixed mean admitted by the Stage 1 diagonal theorem; this note does not strengthen its exceptional-set or mobility quantifiers.

The additional choices are $a(T)$, $h(T)$, and the Stage 1 tolerances and mobility caps. They will be displayed explicitly. None is substituted into the older first-formation horizon or the unrelated recursive-formation contract.

## 2. The existing channel and its exact inherited kernel

On each matching $M$, the three hidden unit directions are

$$
(n_e^+-n_f^+)/\sqrt2,\qquad n_e^-,\qquad n_f^-.
$$

Their span is $Z_M$, with orthogonal complement $W_M$ of dimension nine. The complement contains the full eight-dimensional kernel of $H_M$ and the fast common-normal coordinate. Off the two matchings, set $W_S=\mathbb R^{12}$. The channel is

$$
C(X,S)=(S,P_{W_S}X),
\qquad \mathcal Y=\coprod_S\{S\}\times W_S.
$$

It extends by the identity to observations and evaluator samples. The source label is never discarded. The loop covector annihilates both hidden spaces, so the loop is a function of $C$ on every stratum.

Both $H_M$ and $\Omega$ preserve $W_M\oplus Z_M$. In an orthonormal hidden basis $F_M$, the optimizing conditional lift is

$$
X=y+F_Mz,
\qquad z\sim\gamma_T^Z:=\mathcal N\left(0,T\operatorname{diag}(8+T,4+5T,4+5T)^{-1}\right).
$$

Write this kernel as $\kappa_M(dX\mid y)$. Off matching strata it is the point mass at $y$. The prior factor $\pi_S(p)$ cancels when conditioning on $(S,y)$, so $\kappa_S$ is independent of $p$.

At fixed rows the inherited proposal kernel is

$$
J_p((S,y),B)=\int\kappa_S(dX\mid y)
       \sum_{S'}b_p(S'\mid X)1_B(S',P_{W_{S'}}X).
$$

It is normalized, has proposal rate one, and retains self proposals. For $S'=S$, the projection satisfies $P_{W_S}X=y$, so a self proposal leaves the parent state unchanged. A proposal to a different assignment uses the target projection, including the identity when the new stratum is nonmatching. The hidden Gaussian in this generator is an optimizing conditional integral, not a replacement for the actual retained initial law.

The stratum diffusion has generator

$$
\mathcal L_{p,S}^{C,\rm diff}f(y)
=-A_Sy\cdot\nabla_{W_S}f+T\Delta_{W_S}f.
$$

This is an exact projection of each held-sheet diffusion. At fixed rows, $\mu_p^C=C_\#\mu_{T,p}$ is invariant and reversible: each diffusion is Gaussian reversible, and the fine measure $\mu_{T,p}(dX,S)b_p(S'\mid X)$ is symmetric in $S,S'$. Push its two endpoints through $C$ to get detailed balance for $\mu_p^C(dy,S)J_p((S,y),d(S',y'))$. The finite-dimensional spaces can have different dimensions; the identity is an equality of measures on the disjoint union and needs no common Lebesgue density across strata.

## 3. Actual activation and autonomous own-law learning

At relative time $u=0$, initialize

$$
q_0^C=C_\#\operatorname{Law}(X_\theta,S_\theta\mid E),
\qquad p^C(0)=p(\theta).
$$

The retained law is used exactly, with all its surviving correlations and loop/source information. For $u>0$ the parent uses its own law:

$$
\dot p_i^C(u)=\epsilon_L\{q_u^C(\sigma_i=+1)-p_i^C(u)\}.
$$

The indices are the inherited source-row indices carried by the retained assignment mark. The fine comparator remains the original fine process conditioned on the prefix $E$; its future deterministic row path is the original fine row path. Conditioning does not rerun the fine learning equation with a new conditional marginal. The parent, by contrast, does solve its own learning equation above. This is the distinction the comparison must control.

### Existence, uniqueness, and row constraints

For a prescribed continuous interior row path, construct the parent successively between its Poisson clock rings. The stratum drift is linear. At each ring, sample the fixed hidden Gaussian kernel when needed and then the four receiver choices. A finite interval has finitely many rings, so the process is nonexplosive. Its second moments are finite: a target projection does not increase norm, and a matching lift adds expected squared hidden norm

$$
\frac{T}{8+T}+\frac{2T}{4+5T}\le\frac{5T}{8}.
$$

The diffusion generator applied to $|y|^2$ is at most $24T-2T|y|^2$ on any stratum. The full generator is therefore at most $25T-2T|y|^2$. The activation law has finite moment because it is a projection of a finite-moment fine law conditioned on an event of positive probability.

If two prescribed row paths lie in $[c,1-c]^4$, couple them with common initial state, Brownian increments, proposal clock, hidden Gaussian samples, and receiver uniforms until their first different assignment. The derivative of one posterior receiver probability in its prior entry is bounded by $1/[4c(1-c)]$. Summing four coordinates and integrating the mismatch intensity gives

$$
\operatorname{TV}(q_u^{C,p},q_u^{C,\widetilde p})
\le\frac1{c(1-c)}\int_0^u\|p(v)-\widetilde p(v)\|_\infty dv.
$$

Insert this in the variation-of-constants map

$$
\mathcal T(p)_i(u)=e^{-\epsilon_Lu}p_i^C(0)
 +\epsilon_L\int_0^u e^{-\epsilon_L(u-v)}q_v^{C,p}(\sigma_i=+1)dv.
$$

Its Lipschitz constant on a time interval of length $u_*$ is at most $\epsilon_Lu_*^2/[2c(1-c)]$. On a short interval it is a contraction on continuous paths in an interior cube; the map remains in that cube after reducing the interval if necessary because row velocities are bounded by $\epsilon_L$. This gives a local unique solution. Every solution satisfies

$$
p_i^C(u)\ge p_i^C(0)e^{-\epsilon_Lu},
\qquad1-p_i^C(u)\ge(1-p_i^C(0))e^{-\epsilon_Lu}.
$$

On any prescribed finite horizon these lower bounds provide one interior cube and a positive contraction step length, so finitely many successive constructions yield a unique solution on that horizon. Hence the coupled law exists globally and keeps every prior entry positive at finite times. The bounded jump rate makes source marginals continuous and the rows continuously differentiable. No Gaussian assumption on $q_u^C$ enters this construction.

For the matching's wrong-source row entry $\zeta_i^C(u)$, the own-law equation also implies

$$
0\le\zeta_i^C(u)\le\zeta_i^C(0)+\epsilon_Lu\le\delta+\epsilon_Lu.
$$

Set $d=\delta+\epsilon_Lh$ and assume $d<1/4$.

## 4. An averaged departure estimate for the inherited kernel

Let $\overline\nu_T^M$ be the nine-dimensional optimizing Gaussian on $W_M$. It is the retained conditional law of $\mu_{T,p}$ given $S=M$, independently of $p$. Define the parent departure probability at a proposal by

$$
k_p(y)=J_p((M,y),\{S'\ne M\}).
$$

The matching has maximal sheet weight for $T\le1/100$. If each wrong-source row entry is at most $d$, then

$$
\mu_{T,p}(M)\ge\pi_M(p)\ge1-\sum_i\zeta_i\ge1-4d.
$$

Detailed balance of the inherited kernel bounds total stationary outgoing flux from $M$ by the stationary mass of its complement. Dividing by the matching mass gives

$$
\boxed{\int k_p(y)\overline\nu_T^M(dy)
\le\frac{1-\mu_{T,p}(M)}{\mu_{T,p}(M)}
\le\frac{4d}{1-4d}.}
$$

This is an average under a comparison law. It does not say that the actual parent law, or its survival-conditioned law, is Gaussian.

## 5. Causal conditioning and the retained-path estimate

Write $O_{T,h}^{C,M}$ for the stationary held-$M$ Ornstein–Uhlenbeck path on $W_M$, with the source label retained. The split $W_M\oplus Z_M$ makes it the exact path projection of the Stage 2 stationary full held-matching comparison.

Conditioning a full probability law on an event of probability $1-r$ changes its total variation by $r$. After projection to any future path segment the change is at most $r$. The Stage 2 native-path estimate on $[\theta,\theta+h]$ therefore yields

$$
\operatorname{TV}\left(\operatorname{Law}(C(X_{\theta+u},S_{\theta+u})_{0\le u\le h}\mid E),O_{T,h}^{C,M}\right)
\le\rho+(h+2)\delta.
$$

At the activation time the same argument gives

$$
\operatorname{TV}(q_0^C,\overline\nu_T^M\otimes\delta_M)\le\rho+\delta.
$$

Because $E$ uses only the prefix through $\theta$, future Brownian increments and proposal noise have their original laws. Neither displayed comparison conditions on future success.

Now maximally couple the parent activation law to $\overline\nu_T^M\otimes\delta_M$, and run the parent and stationary retained reference with common Brownian increments and clock. Before the first parent departure, the paths agree; same-assignment proposals leave the retained state unchanged. The parent's row path $p^C(u)$ is deterministic once its unique own-law problem has been solved. At each $u$ its wrong entries are at most $d$.

In the first-departure compensator keep the indicator that the initial coupling succeeded and no departure has yet occurred. The native parent then equals the held reference. Dropping that indicator bounds the probability by the integral over the whole stationary reference path:

$$
\begin{aligned}
\Pr(\text{parent departure before }h\text{ while initially coupled})
&\le\int_0^h\mathbb E[k_{p^C(u)}(Y_u^{\rm ref})]du\\
&\le\frac{4hd}{1-4d}.
\end{aligned}
$$

Here $Y_u^{\rm ref}\sim\overline\nu_T^M$ at every time. Stationarity is used only for the unconditioned reference after dropping the stopped indicator; it is not incorrectly imposed on the initially coupled subevent or on a survival-conditioned parent.

Thus the parent path law is within $\rho+\delta+4hd/(1-4d)$ of this same reference. The triangle inequality proves

$$
\boxed{
\operatorname{TV}\left(
\operatorname{Law}(C(X_{\theta+u},S_{\theta+u})_{0\le u\le h}\mid E),
\operatorname{Law}((Y_u^C,S_u^C)_{0\le u\le h})\right)
\le2\rho+(h+3)\delta+\frac{4h(\delta+\epsilon_Lh)}{1-4(\delta+\epsilon_Lh)}.
}
$$

This is a total-variation comparison of joint retained trajectories and assignment histories. It therefore also controls their loop histories and every measurable functional of the retained path. It makes no path claim for discarded variables or dynamically refreshed evaluator samples, which are not part of this process definition.

## 6. A vanishing bound on the selected joint schedule

Take the already proved implicit common schedule with tolerances at most $\delta\le T$ and mobility cap $\epsilon_L\le T^2$. Choose

$$
a=T^{1/4},\qquad h=T^{-1/4},\qquad
\rho=3\delta+b(T,a,1),
$$

where Stage 2 gives

$$
b(T,a,1)=8\sqrt{2/\pi}a+3408T/a^2.
$$

For sufficiently small temperatures $\rho<1$, and $\rho=O(T^{1/4})$. Also $d\le T+T^{7/4}\le2T$, $h\delta\le T^{3/4}$, and

$$
\frac{4hd}{1-4d}\le\frac{8T^{3/4}}{1-8T}=O(T^{3/4}).
$$

Since $1+T^{-1/4}\le t_L$ eventually under the mobility cap, the whole prefix and following interval fit inside the selected window. The retained-path error is consequently $O(T^{1/4})$.

The activation law in this result is the exact conditioned pushforward, and the parent rows evolve from its own actual law. Gaussian reference paths and frozen-row detailed balance were proof devices for the error bounds. They were not initialization or row-update replacements.

## 7. Scope, executed work, and remaining obligation

The strongest result is a well-defined inherited source-retaining parent, with its own coupled row dynamics, activated causally from the late selected-coherence prefix, and a separate vanishing retained/source path-TV bound over the following growing duration $T^{-1/4}$. The stated channel, block splitting, normalized jump kernel, and source/loop retention are exact. Its agreement with the native conditioned future is approximate and quantified.

This does not turn the late coherence into first formation, prove a second coalescence, certify R14 recursion, or establish exact closure under arbitrary switching. The approximation succeeds because both native and inherited processes make few departures from the selected matching during the stated following window. A further formation episode needs its own in-model event, inherited interaction, and comparison; the present bound cannot substitute for those obligations.

Work performed was source reading, the displayed analytical construction, and writing this report plus `Theory/ca_parent_dynamics.tex`. No external source, scientific simulation, symbolic numerical calculation, GPU workload, Lean work, tamper check, or broad test suite was used. The parent task performs the integration, independent proof check, and LaTeX validation. No vault file or other worker's file was changed.
