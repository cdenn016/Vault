## Conclusion

**No computable fixed power is justified by the results stated in the question.**  The estimate with `a>3.5` proves tracking, not selection.  For selection one still needs a quantitative small-`T` lower bound for the actual unstable imprint on one common full-measure set of fixed means.  That bound is not a consequence of fixed-`T` analyticity/nonvanishing or of the large-`s` ray argument.

What *is* available is:

1. a genuinely joint initial-layer coupling bound;
2. a conditional, conservative power criterion once an imprint floor is supplied; and
3. unconditionally, a nonconstructive diagonal schedule with mean-independent thresholds and summable exceptional sets.

### 1. What can be made joint

Put `z=p-(1/2)1`, and denote by `b_i(p,x)` the conditional `+` probability in row `i`.  On `p_i in [1/4,3/4]`,

`∂_{p_i} b_i = b_i(1-b_i)/(p_i(1-p_i)) <= 4/3`.

Consequently the 16-state product redraw kernel is Lipschitz in total variation, uniformly in `x` and `T`.  Couple the adaptive process and the frozen-`p=1/2` process using the same initial state, Brownian motion, rate-one clock, and redraw uniforms.  Since `|z_i(t)|<=eps t`, the probability of a mismatched whole-assignment redraw by time `t` is at most `C eps t^2`.  Thus the row-marginal discrepancy is `O(eps t^2)`.  Integrating

`z'=eps(a-1/2-z)`

and retaining the `-eps z` term gives, at `t1=eps^(-1/4)`,

`z(t1)=eps ∫_0^t1 (a^0(s)-1/2)ds + R_c`,

`|R_c| <= C eps^2 t1^3 + C eps^2 t1^2 <= C eps^(5/4)`.                 (1)

This constant is independent of `T` and of the initial mean.  The estimate is valid on the stated interior cube, which contains the trajectory during this layer because `eps t1=eps^(3/4)=o(1)`.

For the frozen process, `a_i'=E b_i-a_i`, with `a_i(0)=a_i(infinity)=1/2`; hence the improper integrals of `a_i-1/2` and `E b_i-1/2` coincide.  If `U` denotes the unstable coordinate with the normalization used in the question, its supplied leading coefficient is therefore

`U(t1)=eps j_T(m)/2 + R_init`.                                           (2)

Let `L_T=1+log(1/T)` and `lambda_T=c T^(5/2)/L_T`.  On every bounded mean set `|m|<=R`, the quadratic Gaussian formula gives active initial entropy `H_0=O_R(T^-1)`.  Provided the stated active entropy rate controls the same conditional entropy that controls the row observable, Pinsker and entropy decay yield

`|∫_t^infinity E[b(X_s)-1/2]ds|`
` <= C_R T^(-1/2) lambda_T^(-1) exp(-lambda_T t/2)`
` <= C_R T^(-3)L_T exp[-cT^(5/2)t/L_T]`.                                (3)

Using the minimum of this decay bound and the trivial bound `1` also gives

`|J_T(m)| <= C_R lambda_T^(-1)[1+log(1/T)]`
`          <= C_R T^(-5/2)L_T^2`                                       (4)

for the full vector frozen imprint.  Combining (1)--(3),

`|R_init| <= C eps^(5/4)`
` + C_R eps T^(-3)L_T exp[-cT^(5/2)eps^(-1/4)/L_T]`.                     (5)

For `eps=T^a`, the second term in (5) is smaller than every power of `T` whenever `a>10`.  Thus the initial-layer coupling remainder can be controlled jointly; it is not the fundamental obstruction.  If the supplied entropy statement has not already established the active-entropy/observable identification used in (3), that identification is an additional exact obligation.

The averaged saddle itself is also locally nondegenerate.  If `B_sigma` is the residual matrix, then `H_sigma=B_sigma'B_sigma`.  With one shared scalar translation per undirected edge, row reduction gives

* `rank H_sigma=6` for the two alternating perfect-match assignments;
* `rank H_sigma=7` for the other fourteen assignments.

The frozen stationary label weights are proportional to

`w_p(sigma) det(Omega+H_sigma/T)^(-1/2)`.

They are therefore `Theta(T^3)` for the two matchings and `Theta(T^(7/2))` otherwise.  On compact subsets of the interior of the row cube, the averaged field `F_T(p)=E_{pi_p}[1_{sigma_i=+}]-p` converges in `C^2` to the two-matching field.  At `p=1/2`,

`DF_0=vv'-I`,

so the limiting eigenvalues are `3` along `v` and `-1` transversely.  This proves uniform *local* hyperbolicity of the averaged field; it neither creates nor lower-bounds the transient imprint.

For moving rows, while `p` remains in a fixed compact interior cube, the strongest direct entropy estimate has a history supremum.  With `h=sqrt(H(q_t|pi_{p_t}))`, bounded centered `p`-scores give, for the active entropy just described,

`D^+h <= -lambda_T h/2 + C eps(|z|+h)`,

`h(t) <= exp[-c lambda_T(t-s)]h(s)`
`       + C(eps/lambda_T) sup_{u in [s,t]}|z(u)|`.                       (6)

Replacing the history supremum by `|z(t)|` without a cone bootstrap would be invalid.  From (4)--(6), the initial transverse displacement is at most
`O_R(eps T^(-5/2)L_T^2)`, while the entropy forcing after the initial layer is at most `O_R(eps^2T^(-5)L_T^3)` plus a super-polynomial tail.  Symmetry makes `span(v)` an exact invariant linear eigenspace of the averaged field, so the transverse displacement does not enter the unstable equation linearly; its deterministic contribution is quadratic, `O_R(eps^2T^(-5)L_T^4)`.  A rigorous use of this last statement requires the usual history-supremum cone bootstrap for (6).

### 2. Exact condition that would yield a power

A convenient sufficient hypothesis is: there is one finite exponent `r>=0` and one common full-measure set of means such that, for each mean in that set,

`|j_T(m)| >= c(m)T^r` for all sufficiently small `T`.                    (7)

Together with the active-entropy identification and the uniform local cone bootstrap above, (7) makes every

`eps=T^a`,  `a>max{10,4r}`,                                               (8)

a conservative sufficient selection schedule.  Indeed:

* `eps^(5/4)=o(eps T^r)` is exactly `a>4r`;
* the entropy and transverse-quadratic terms are `o(eps T^r)` if `a>r+5`, which follows from (8);
* the frozen tail is super-polynomial if `a>10`;
* the supplied global tracking error is `O(T^(a-3.5)[1+(1+a)log(1/T)])=o(1)`;
* escape from a seed of order `T^(a+r)` needs at most `((a+r)/alpha+o(1))log(1/T)` slow time, whereas `eps t_L=2a log(1/T)` and `alpha>=7/5`; under `r<a/4` there is ample time.

More generally, for a specified `a>10`, a direct sufficient imprint condition is

`T^(a/4)=o(|j_T(m)|)` for a.e. fixed `m`,                                (9)

on a common full-measure set.  It controls not only the coupling remainder: under (9), the entropy/transverse ratio is bounded by `o(T^(3a/4-5)L_T^4)`, which also vanishes for `a>10`.  Conditions (7) or (9) have **not** been proved for the actual imprint.  Formula (8) is therefore a conditional theorem, not a resolution by an explicit power.

The missing result is a singular small-temperature theorem for the signed infinite-time resolvent defining `j_T`: it must control the long-time frozen semigroup, the boundary layers where edge costs tie, and cancellation in the `v` projection.  The scaling `X=sqrt(T)Y` does not turn this into regular perturbation theory, because `Y_0` has law `N(m/sqrt(T),T^(-1)I)`.  Fixed-`T` entirety only makes the zero set null separately for each `T`; it gives no common quantitative floor as `T downarrow0`.

### 3. Why the fixed-`T` facts alone cannot imply a power

This is a logical example only, not a counterexample to the model.  Let `ell` be linear with `ell(su)=s` on the ray used in the nonvanishing proof, and set

`Ein(z)=∫_0^z (1-e^(-w))/w dw`,

`j_T^*(m)=(2T)^(-1) Ein(e^(-1/T^2)ell(m))`.

For each fixed `T`, this is a nonzero real-entire function; its real zero set is null.  For fixed `T` and `s to infinity`,

`j_T^*(su)=log(s)/(2T)-1/(2T^3)+O(1/T)`.

Hence it satisfies the analogous ray bound

`j_T^*(su)>=log(s)/(2T)-5loglog(s)/T-O_T(1)`

for all sufficiently large `s`.  But for every fixed `m`,

`j_T^*(m)=ell(m)e^(-1/T^2)/(2T)+O_m(e^(-2/T^2)/T)`,

which is smaller than every power of `T`.  The abstract unstable amplitude

`A(T,eps,m)=eps j_T^*(m)-eps^(5/4)`

has the stated fixed-`T` leading term and remainder: for fixed `T` and `ell(m)>0`, its leading sign eventually wins as `eps downarrow0`.  Along every `eps=T^a`, however, the adverse remainder wins for small `T` on that half-space.  This shows only that the fixed-`T` statements and ray growth do not logically imply any polynomial schedule.

### 4. Strongest unconditional diagonal schedule

Choose any predetermined sequence `T_n downarrow0` lying eventually in the fixed-temperature regime.  Choose a measurable representative of `M_T(m)` and define

`Phi_T(eps,m)=sup_{t in [2eps^(-1)log(1/eps),4eps^(-1)log(1/eps)]}`
`             q_t^{T,eps,m}(S != M_T(m))`.

This is the exact interval `[t_L,2t_L]` with `C=2`.  The finite-dimensional dynamics make `Phi_T` jointly measurable; alternatively, the existential projections below are analytic and hence Lebesgue measurable.  The fixed-`T` theorem says `Phi_T(eps,m) to 0` for a.e. `m` as `eps downarrow0`.

Let `B_n={|m|<=n}`, `delta_n=2^(-n)`, and

`E_{n,k}={m in B_n: some 0<eps<=1/k has Phi_{T_n}(eps,m)>delta_n}`.

As `k` increases these sets decrease.  Their intersection is contained in the fixed-`T_n` exceptional set, hence has measure zero.  Since `B_n` has finite measure, continuity from above gives a `k_n` such that

`|E_{n,k_n}|<=2^(-n)`.

Set

`eta_n <= min{1/k_n,2^(-n)}`,

and, if desired, also impose any predetermined positive cap and make `eta_n` decreasing.  The corresponding bad sets only shrink.  Since their measures are summable, the set of means belonging to infinitely many bad sets is null.  After also removing the countable union of the fixed-`T_n` null sets, the quantifiers are:

**For every predetermined `T_n downarrow0`, there are numbers `eta_n>0`, independent of `m`, such that for every sequence `0<eps_n<=eta_n`,**

`Phi_{T_n}(eps_n,m)<=2^(-n)` eventually for a.e. fixed `m`.

Thus selection holds along the diagonal.  These thresholds are nonconstructive: fixed-`T` convergence supplies no effective modulus, so they need not be computable and no relation `eta_n=T_n^a` follows.

This conclusion permits the selected matching `M_{T_n}(m)` to vary with `n`.  Finiteness of the matching set gives, after fixing `m`, some constant-matching subsequence; that subsequence may depend on `m`.  It does not yield a fixed matching along the full schedule, or even a deterministic constant-matching subsequence valid for a.e. `m`.  A fixed limiting matching requires a separate eventual-stabilization or uniform branch-gap theorem.

## Final answer

The strongest unconditional consequence is the summable-exception diagonal theorem above, with nonconstructive mean-independent epsilon thresholds and a matching allowed to vary with temperature.  A fixed power for the exact model remains unresolved.  The decisive unresolved obligation is the common-full-measure imprint floor (7), or equivalently a condition such as (9); the initial-layer coupling remainder itself admits the joint bound (5).
