# Claim C17 and its argument (cleaned write-up for a reconstruction check)

## Claim (exact statement)

(Lemma M) $N_{\mathrm{eff}}$ keeps the members' act feedback and removes only what the world path tells about their private inputs: $\Sigma^c_{\mathrm{eff}}-\Sigma^c=S\Cov(\E[z_0\mid\tilde y])S^\top\succeq0$.

(Theorem O) If $C$ ($n\ge2$, scalar coordinates) is uncorrelated with $V\setminus C$ and exchangeable under $N_{\mathrm{eff}}$, with act loadings of disagreement rank below $n-1$, then either $\Pi^c$ is not diffusive or $r(C)\le r_{\mathrm{eff}}(C)$, so $C$ never differs from $N_{\mathrm{eff}}$.

(Proposition E) Acts consistent with expected free energy under a common preference load all members' errors about one component with one sign.

(Proposition D) A null that keeps the acts gives uncorrelated interchangeable members with nonzero loadings $\Sigma^c_{ij}<0$, so that null is not diffusive.

## Definitions (live source; read these sections)

- World-conditional law: `Collective_Agents/sections/04_collectives.tex`, lines 130-141 (`def:col-world-conditional`, `prop:col-world-conditional`).
- Diffusive precision, couplings, leaks: same file, lines 143-151.
- Contrast $r(C)=\xi_{\mathrm{in}}/\xi_{\mathrm{out}}$, $\xi_{\mathrm{out}}=\phi_C^\top\Pi\phi_C$, $\xi_{\mathrm{in}}$: same file, lines 182-188 (`def:col-contrast`).
- Collective and baseline: same file, lines 197-221.
- Nulls, including $N_{\mathrm{eff}}$ ("each act's effect on $\eta$ replaced by exogenous forcing with the law of the act path, added to $\mathcal X_{\mathrm{sh}}$"): `Collective_Agents/sections/05_agency.tex`, lines 332-360. "Differs" is defined at line 333.
- Group model with joint performative acts (setting of Proposition E): `Collective_Agents/sections/s05_agency.tex`, lines 146-181.

## Conventions

| Key | Choice | Test value |
| --- | --- | --- |
| World-conditional law | condition on the whole world path, every component, including acted ones; relay noise is receiver-specific; an agent's own sensing noise is private even when relayed | level-0 scalar network: $\Sigma^c=\sum_nW^nQ^\zeta W^{n\top}$ |
| Diffusive precision | $\Pi=\mathrm{diag}(\varepsilon)+L$, couplings $a_{ij}=-\Pi_{ij}\ge0$, leaks $\varepsilon_i=(\Pi\mathbf 1)_i\ge0$ | $\Pi=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$: $a_{12}=1$, $\varepsilon=(1,1)$ |
| Contrast | $r(C)=\xi_{\mathrm{in}}/\xi_{\mathrm{out}}$, $\xi_{\mathrm{out}}=\phi_C^\top\Pi\phi_C$, $\xi_{\mathrm{in}}=\min_{f\perp\mathbf 1_C}f^\top(\mathrm{diag}(\varepsilon)+L_C)f/f^\top f$ | compound-symmetric block $\Sigma=\alpha I_n+\beta\mathbf 1\mathbf 1^\top$ with no cut: $r=1+n\beta/\alpha$; at $\alpha=1,\beta=0.5,n=4$, $r=3$ |
| Contrast coordinates | prior errors | |

## Results used from elsewhere (cited, not part of this claim)

- (C1) If the world-conditional errors of a set $C$ of $n$ scalar agents have covariance $\alpha I_n+\beta\mathbf 1\mathbf 1^\top$, $\alpha>0$, $\beta\ge0$, and are uncorrelated with every other agent's, and the rest of the population's precision is diffusive, then $\Pi^c$ is diffusive, with coupling $\beta/(\alpha(\alpha+n\beta))$ and leak $1/(\alpha+n\beta)$ on $C$, no cut, and $r(C)=1+n\beta/\alpha$; for $-\alpha/n<\beta<0$ the off-diagonal entries are positive.
- (C4, "Z1") If $\Pi$ is a positive definite Z-matrix, then $\Sigma=\Pi^{-1}\ge0$ entrywise, $\Sigma_{ij}>0$ exactly within connected components of the coupling graph, $\Sigma_{ij}\Sigma_{jk}\le\Sigma_{ik}\Sigma_{jj}$, and every principal submatrix of $\Sigma$ has a Z-matrix inverse.

## Argument

**Setting G.** World: $\eta'=F\eta+Ba+w$. Agents' stacked internal state $x'=Ax+(\text{terms in the conditioned path})+E\xi$, where $\xi$ collects the private inputs: sensing noise, receiver-specific channel noise, computation noise, and act noise read by the actor itself. Acts: $a=\Gamma x+(\text{path terms})+\Gamma_\xi\xi+\nu$, with $\nu$ read by no filter. All noises are Gaussian and independent across rounds. $A$ and the full closed loop are stable. Let $z$ be the stationary solution of $z'=Az+E\xi$, and let $\tilde y_t=B\Gamma z_t+B\Gamma_\xi\xi_t+B\nu_t+w_t$. $S$ is the linear map from the internal state to the members' contrast coordinates.

**Lemma M.** $\Sigma^c=S\Cov(z_0\mid\tilde y_Z)S^\top$ and $\Sigma^c_{\mathrm{eff}}=S\Cov(z_0)S^\top$. Hence $\Sigma^c_{\mathrm{eff}}-\Sigma^c=S\Cov(\E[z_0\mid\tilde y])S^\top\succeq0$, and $\Pi^c\succeq\Pi^c_{\mathrm{eff}}$.

*Proof.* By superposition, $x=\bar x+z$, with $\bar x$ a causal linear functional of the conditioned path. In the full model, $\tilde y_t=\eta_{t+1}-F\eta_t-B(\Gamma\bar x_t+\text{path terms})$ is a causal function of the path. Conversely, $\eta$ is the stationary solution of the closed loop driven by $\tilde y$, so the two generate the same sigma-algebra. Since $\bar x_0$ is conditioned on, $\Cov(x_0\mid\eta)=\Cov(z_0\mid\tilde y)$. Under $N_{\mathrm{eff}}$, $\eta$ is a function of inputs independent of $\xi$, and $z$ is the same process (same $A$, $E$, $\xi$), so $\Cov(x_0\mid\eta)=\Cov(z_0)$. The Gaussian law of total covariance finishes the proof. $\square$

Reading adopted for Lemma M: $N_{\mathrm{eff}}$ keeps every agent's update rule, including the use of acts it knows.

**Theorem O.** Let $C$ have $n\ge2$ members with scalar contrast coordinates, and assume:
- (O1) isolation: $C$ is uncorrelated with $V\setminus C$ under $N_{\mathrm{eff}}$.
- (O2) exchangeability: the law of $z$ is invariant under the action of each permutation of $C$ on its agents' local states.
- (O3) rank: $\tilde y$ loads on $(z_C,\xi_C)$ through coefficient vectors $\kappa^{(r)}$ applied to agent-canonical patterns, and $W=\mathrm{span}\{P_{D_C}\kappa^{(r)}\}$ has $\dim W<n-1$, where $D_C=\mathbf 1_C^\perp\subset\mathbb R^n$ and $P_{D_C}$ is the orthogonal projection onto it. Equal loadings give $W=\{0\}$.

Then $\xi_{\mathrm{out}}(C)\ge\xi^{\mathrm{eff}}_{\mathrm{out}}(C)$, and if $\Pi^c$ is diffusive then $\xi_{\mathrm{in}}(C)\le\xi^{\mathrm{eff}}_{\mathrm{in}}(C)$. Hence either $\Pi^c$ is not diffusive or $r(C)\le r_{\mathrm{eff}}(C)$. If $\Pi^c_{\mathrm{eff}}$ is diffusive, $C$ is a collective under $N_{\mathrm{eff}}$ at every level at which it is one in the full model (leak ratio 1, baseline fixed), so $C$ never differs from $N_{\mathrm{eff}}$.

*Proof.* By Schur's lemma for $S_n$ on $\mathbb R^n\otimes\mathbb R^d$, the standard component $D_C\otimes\mathbb R^d$ evolves as i.i.d. copies along any orthonormal basis of $D_C$, independent of the trivial part and, by (O1), of $V\setminus C$. For a unit $f$ in $D_C$ orthogonal to $W$, the $f$-copy enters $\tilde y$ through neither states nor noises. For the noise terms, equivariance gives $\Cov((f\otimes I)z_t,m^\top\xi_s)=(h_0-h_1)(\kappa^\top f)=0$. The $f$-copy is therefore independent of $\tilde y$ and of every other direction, so $f$ is an eigenvector of both $\Sigma^c$ and $\Sigma^c_{\mathrm{eff}}$ with the same eigenvalue $\alpha$. Then:
- $\xi_{\mathrm{in}}(C)\le f^\top\Pi^cf-\sum_ia^\partial_if_i^2\le\alpha^{-1}=\xi^{\mathrm{eff}}_{\mathrm{in}}$ when $\Pi^c$ is diffusive ($a^\partial_i$ the couplings of member $i$ to agents outside $C$).
- $\xi_{\mathrm{out}}=\phi^\top\Pi^c\phi\ge\phi^\top\Pi^c_{\mathrm{eff}}\phi$ by Lemma M. $\square$

**Proposition E.** Setting: `def:agy-joint-acts` with additive effects on a scalar acted component, a common outcome map $h$, common $\Lambda$, true effect models and Gaussian habits. The world's mean act input is $-\sum_jw_jz_j/h_Z$ with weights $w_j\ge0$, where $z_j=h^\top Fm_j+(\text{terms without }m_j)$:
- under rule D2 (each member draws its act from its own policy posterior, treating the other members' acts as habit draws): $w_j=\gamma\Lambda\mu_j^2s_j^2$;
- under rule D1 (the tilted-habit group posterior): $w_j=\gamma\Lambda\sigma_j^2\mu_j^2/(1+\gamma\Lambda\sum_k\sigma_k^2\mu_k^2)$, from Sherman-Morrison.

So member $j$'s belief about component $k$ loads with sign $-\mathrm{sign}(h_Z(h^\top F)_k)$, common to all members.

**Proposition D.** Under a null that keeps the acts, let members $i$ and $j$ be uncorrelated and interchangeable in the private law, with $k_i\ne0$. Then $\Sigma^c_{ij}=-\lvert k_i\rvert^2<0$. By C4 (Z1), the null's precision is then not diffusive.

The original argument does not define $k_i$ beyond this. Notation gloss added by the record keeper (not part of the argument; check it rather than assume it): $k_i$ is read as member $i$'s row in a factorization $S\Cov(\E[z_0\mid\tilde y])S^\top=KK^\top$ of the correction of Lemma M.
