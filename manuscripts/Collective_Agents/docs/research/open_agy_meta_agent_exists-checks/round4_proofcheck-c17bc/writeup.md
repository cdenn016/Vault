# Claims C17a (used), C17b and C17c: statements and arguments (cleaned write-up)

## Setting G

World: $\eta'=F\eta+Ba+w$. Agents' stacked internal state $x'=Ax+(\text{terms in the conditioned path})+E\xi$, where $\xi$ collects the private inputs: sensing noise, receiver-specific channel noise, computation noise, and act noise read by the actor itself. Acts: $a=\Gamma x+(\text{path terms})+\Gamma_\xi\xi+\nu$, with $\nu$ read by no filter. Shared broadcast noises $\beta$ are conditioned on and independent of $(\xi,\nu,w)$. All noises are Gaussian and independent across rounds. $A$ and the full closed loop are stable, and $F$ has no eigenvalue on the unit circle. Let $z$ be the stationary solution of $z'=Az+E\xi$, and let $\tilde y_t=B\Gamma z_t+B\Gamma_\xi\xi_t+B\nu_t+w_t$. $S$ maps the internal state to the agents' contrast coordinates. $N_{\mathrm{eff}}$ replaces each act's effect on $\eta$ by exogenous forcing with the law of the act path and keeps every agent's update rule.

## C17a (Lemma M; given, may be used)

$\Sigma^c=S\Cov(z_0\mid\tilde y)S^\top$ and $\Sigma^c_{\mathrm{eff}}=S\Cov(z_0)S^\top$, hence $\Sigma^c_{\mathrm{eff}}-\Sigma^c=S\Cov(\E[z_0\mid\tilde y])S^\top\succeq0$, and if $\Sigma^c\succ0$, $\Pi^c\succeq\Pi^c_{\mathrm{eff}}$.

## C17b (claim to check)

Statement. Let $C$ have $n\ge2$ members with scalar contrast coordinates and assume:
- (O1) $C$ is uncorrelated with $V\setminus C$ under $N_{\mathrm{eff}}$;
- (O2') the joint law of $(z,\xi)$ is invariant under each simultaneous permutation of the members of $C$ acting on their local states and local private inputs; the contrast map on $C$ is $S_C=I_n\otimes s^\top$; and the noise loadings of $\tilde y$ on $\xi_C$ have the form $\kappa\otimes m$ in those coordinates;
- (O3) $\tilde y$ loads on $(z_C,\xi_C)$ through coefficient vectors $\kappa^{(r)}\in\mathbb R^n$ applied to agent-canonical patterns, and $W=\mathrm{span}\{P_{D_C}\kappa^{(r)}\}$ has $\dim W<n-1$, where $D_C=\mathbf 1_C^\perp$;
- $\Pi^c_{\mathrm{eff}}$ is diffusive.

Then $\xi_{\mathrm{out}}(C)\ge\xi^{\mathrm{eff}}_{\mathrm{out}}(C)$, and if $\Pi^c$ is diffusive, $\xi_{\mathrm{in}}(C)\le\xi^{\mathrm{eff}}_{\mathrm{in}}(C)=1/\alpha$, so $r(C)\le r_{\mathrm{eff}}(C)$.

Argument.
1. For $n\ge2$, $\mathbb R^n$ splits under $S_n$ into $\mathrm{span}\{\mathbf 1\}$ and $D_C$, non-isomorphic and absolutely irreducible, so every matrix (or spectral density) commuting with all $P_\sigma\otimes I_d$ has the form $I\otimes M_0+\mathbf 1\mathbf 1^\top\otimes M_1$. By (O2') this applies to the auto- and cross-covariances of $z_C$ at every lag and to $\Cov(z_{C,t},\xi_{C,s})=I\otimes(h_0-h_1)+\mathbf 1\mathbf 1^\top\otimes h_1$. Invariance with $V\setminus C$ held fixed puts the columns of the cross-spectrum between $z_C$ and $V\setminus C$ in $\mathbf 1\otimes\mathbb R^d$.
2. For a unit $f\in D_C$ with $f\perp W$, the copy $u_f=(f\otimes I)z_C$ satisfies: its covariance with the state-loading part of $\tilde y$ is $(f^\top\kappa)(R_0-R_1)p=0$; its covariance with the noise part is $(f\otimes I)^\top\Cov(z_{C,t},\xi_{C,s})(\kappa\otimes m)=(f^\top\kappa)(h_0-h_1)m=0$; and it is uncorrelated with the trivial part, with the other directions of $D_C$ orthogonal to it, and with $V\setminus C$. Being jointly Gaussian, $u_f$ is independent of $\tilde y$, so conditioning on $\tilde y$ leaves its covariance unchanged and $f$ (extended by zero) is an eigenvector of both $\Sigma^c$ and $\Sigma^c_{\mathrm{eff}}$ with the same eigenvalue $\alpha$.
3. On $C$, $\mathrm{diag}(\varepsilon)+L_C=\Pi_{CC}-\mathrm{diag}(a^\partial)$, with $a^\partial_i\ge0$ the couplings of member $i$ to $V\setminus C$ when $\Pi^c$ is diffusive. So $\xi_{\mathrm{in}}(C)\le f^\top\Pi^cf-\sum_ia^\partial_if_i^2\le f^\top\Pi^cf=1/\alpha$.
4. Under $N_{\mathrm{eff}}$, (O1) makes $\Pi^c_{\mathrm{eff}}$ block-diagonal between $C$ and $V\setminus C$, so $a^{\partial,\mathrm{eff}}=0$, and (O2') gives $\Sigma^{\mathrm{eff}}_{CC}=aI+b\mathbf 1\mathbf 1^\top$, whose inverse has $D_C$ as an eigenspace with eigenvalue $1/a$; by step 2, $a=\alpha$. With $\Pi^c_{\mathrm{eff}}$ diffusive, $\xi^{\mathrm{eff}}_{\mathrm{in}}(C)=1/\alpha$.
5. $\xi_{\mathrm{out}}=\phi^\top\Pi^c\phi\ge\phi^\top\Pi^c_{\mathrm{eff}}\phi=\xi^{\mathrm{eff}}_{\mathrm{out}}$ by C17a. Hence $r(C)=\xi_{\mathrm{in}}/\xi_{\mathrm{out}}\le\xi^{\mathrm{eff}}_{\mathrm{in}}/\xi^{\mathrm{eff}}_{\mathrm{out}}=r_{\mathrm{eff}}(C)$.

## C17c (claim to check)

Statement. Under a null that keeps the acts (so C17a applies to the null's own conditioning process $\tilde y$), let members $i$ and $j$ be uncorrelated in the private law, $(S\Cov(z_0)S^\top)_{ij}=0$; let the joint law of $(z,\tilde y)$ be invariant under the swap $i\leftrightarrow j$ of the two members' local states with $\tilde y$ held fixed, with $S$ equivariant on the pair; write $KK^\top=S\Cov(\E[z_0\mid\tilde y])S^\top$ and let $k_i$ (row $i$ of $K$) be nonzero. Then $k_i=k_j$, $\Sigma^c_{ij}=-\lvert k_i\rvert^2<0$, and the null's precision is not diffusive.

Argument. The swap invariance with $\tilde y$ fixed gives $\Cov((Sz_0)_i,\tilde y_s)=\Cov((Sz_0)_j,\tilde y_s)$ for every $s$, so $\E[(Sz_0)_i\mid\tilde y]=\E[(Sz_0)_j\mid\tilde y]$ and the rows of a factor $K$ built from the projection coefficients coincide: $k_i=k_j$. By C17a, $\Sigma^c_{ij}=(S\Cov(z_0)S^\top)_{ij}-k_i^\top k_j=-\lvert k_i\rvert^2<0$. By the cited result C4 (if $\Pi$ is a positive definite Z-matrix then $\Pi^{-1}\ge0$ entrywise), a negative entry of $\Sigma^c$ excludes a diffusive $\Pi^c$.
