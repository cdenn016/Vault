<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 15 independent reconstruction: statistical-physics, RG, and effective-theory lens

## Frozen source, independence, and method

This memo is frozen to Research commit
`14551bb8d463f229a3b451d7222042d134c2c52d` on branch
`codex/gauge-vfe-rg-task15-adjudication-20260808`. The load-bearing source
hashes are:

| source | SHA-256 |
|---|---|
| `manuscripts/gauge_vfe_rg/SPEC.md` | `AB59A4D02E1C475B6384403013458D39F88F170D592EDF802D4C772DD7320571` |
| `manuscripts/gauge_vfe_rg/07_general_renormalization.tex` | `CEDA98A49F4122DE39D70F784288860AB727ABFA217A92B1230591E6CE76BCAD` |
| `manuscripts/gauge_vfe_rg/07b_agent_network_rg.tex` | `5EB159493EC727218E2EACA4CF47F3FDDEB090F6E193352846AD2A43181437CA` |
| `manuscripts/gauge_vfe_rg/09_coarsegraining.tex` | `7CAEDF0E2E5301B7F56FFEEE350CCD280BDA9C2119BA40D1619A5727FE161E80` |
| `manuscripts/gauge_vfe_rg/10_renormalization.tex` | `A19AE76E82EFF709C1BE7228B02B69558CC95A53AE4C064AB1AE459C6C134C49` |
| `manuscripts/gauge_vfe_rg/appendix_claim_ledger.tex` | `2AA6CB6D1B5A4FFC8B88D5BDF25642394FF351ACA81DA21633EEA9345FE39E90` |

I reconstructed the claims from the manuscript and its governing `SPEC.md`.
I did **not** read `construction-or-strongest-theorem.md`, any other Task 15
memo, or the Task 15 oracle packet. The ordinary rigorous-theory-search
scaffold and the repository `.verification` ledger were deliberately not
created or modified because this assignment authorizes exactly this one memo.
The claim states below apply the verification vocabulary locally; they are not
a substitute for a validated repository ledger.

Read-only wiki context was consulted at
`[[Renormalization-group flow of beliefs]]` and
`[[gauge-vfe-rg-pullback-geometry-2026-08-01]]`. It was used only to separate
the present abstract construction from the legacy exploratory MAgent blocking
pipeline; it is not proof evidence for any theorem below.

## Verdict

**Qualified affirmative.** The manuscript genuinely supplies a nonempty,
exact **finite-network effective VFE theory** at the level of normalized
measure pairs and fixed Markov coarse channels. On an additional
product-equivalent bounded-action tier, it supplies an exact full-interaction
Hoeffding coordinate system, a nonlinear coarse action map and its derivative
cocycle, all generated finite hyperedges, and an exact retained-projection
residual. With separately declared rescaling and comparison data, it also
supplies a correctly typed **conditional RG theory**: discrete beta data,
nonautonomous mode growth, fixed objects, and an explicit Gaussian tangent
realization.

The qualification is load-bearing. The manuscript does **not** derive a
canonical blocking rule, rescaling, common comparison space, autonomous flow,
nontrivial invariant retained ansatz, basin of attraction, universality class,
or infinite-volume/continuum limit. Its full finite interaction space has
`2^{|V|}-1` component function spaces and an extraction constant that grows as
`3^{|V|}-1`; it is finite-network exactness, not a dimension-free or
finite-parameter closure theorem. The unqualified proposition that these
finite results already constitute a universal or thermodynamic RG is refuted
by the manuscript's explicit scheme-change and noncommuting-limit witnesses.
The existential proposition that a nontrivial universal infinite-volume limit
might exist for some specified family remains **INCONCLUSIVE/OPEN**, not
negatively settled.

This verdict follows from the direct constructions and proofs reconstructed
below; it does not depend on a preferred conclusion.

## Memo-local claim ledger

| ID | atomic claim | state | direct closure evidence |
|---|---|---|---|
| RG-1 | A common normalized Markov pushforward gives an exact coarse VFE identity at unchanged evidence. | `EVIDENCE_VERIFIED` | Relative-entropy disintegration reconstructed below; source `07b_agent_network_rg.tex:16-73`, `thm:rg-exact-coarse-vfe`. |
| RG-2 | Every bounded action class on a finite product network has a unique full nonconstant Hoeffding interaction coordinate, with the stated finite norm bounds. | `EVIDENCE_VERIFIED` | Boolean-lattice projector proof and sharp biased-Rademacher family; source `07b_agent_network_rg.tex:1133-1255`, `thm:rg-hoeffding-action-isomorphism`. |
| RG-3 | The exact nonlinear interaction map, its tilted derivative, and its retained/action residual are correctly typed and exact under the stated product-equivalence hypotheses. | `EVIDENCE_VERIFIED` | Direct differentiation and inverse-map algebra; source `07b_agent_network_rg.tex:1367-1512`, `eq:rg-exact-nonlinear-interaction-map` through `eq:rg-interaction-residual-norm-control`. |
| RG-4 | Exact coarse closure generally generates hyperedges, marked attention data, and path memory rather than preserving a pairwise memoryless ansatz. | `EVIDENCE_VERIFIED` | Elimination/Mobius reconstruction, Ising-star counterexample, event-law pushforward, and exact projection-memory recurrence; source `07b_agent_network_rg.tex:1517-1565`, `1748-1907`, `1937-2119`. |
| RG-5 | Cross-scale modes, beta functions, and fixed objects are mathematically typed once their comparison, norm, scale, reference, and dynamical-type data are declared. | `EVIDENCE_VERIFIED` as a conditional framework | Chain rule, ordered products, exact residual, reference/scheme laws, and fixedness counterexamples; source `07_general_renormalization.tex:503-860` and `07b_agent_network_rg.tex:2124-2730`. No general mode splitting or attractor existence is proved. |
| RG-6 | The independent scalar Gaussian normalized-sum tangent has Hermite eigenvalues `b^{1-k/2}` and the stated relevance classes. | `EVIDENCE_VERIFIED` | Mehler regression plus diagonal-operator spectral proof; source `07b_agent_network_rg.tex:871-1048`, `thm:rg-gaussian-hermite-spectrum`. |
| RG-7 | The Gaussian block-factorization gap is the log-determinant expression stated in the manuscript and is monotone under block merging. | `EVIDENCE_VERIFIED` | Direct Gaussian-KL minimization and Fischer equality analysis; source `09_coarsegraining.tex:1002-1025`, `eq:cg-factorization-gap`. |
| RG-8 | The path-graph finite/maximal-depth limits differ, and regular variation of the zero-mode-excluded IDS implies the stated heat-susceptibility limit. | `EVIDENCE_VERIFIED` | Exact quotient/eigenvalue count and Abelian Karamata calculation; source `07_general_renormalization.tex:862-1062`, `prop:rg-noncommuting-limits`, `eq:rg-heat-susceptibility`. |
| RG-9 | The manuscript's complete finite law-level theorem is nonvacuous and exact under its enumerated hypotheses. | `EVIDENCE_VERIFIED`, conditional | Composition of RG-1 through RG-4 and explicit finite positive-law examples; source `07b_agent_network_rg.tex:2735-2811`, `thm:rg-complete-effective-theory` and `cor:rg-complete-analytic-tier`. |
| RG-10 | Finite exactness entails a blocking-scheme-independent universality class or an infinite-volume RG limit. | `REFUTED` | Moving-frame beta witness, correlated-Hermite dependence, exponentially nonuniform Hoeffding bound, and path noncommuting limits. The manuscript itself does not make this claim. |
| RG-11 | A specified nontrivial universal thermodynamic limit exists for this gauge-VFE family. | `INCONCLUSIVE` | No triangular family, DLR/projective-limit theorem, free-energy-density limit, diagonal-limit theorem, basin, or cross-scheme invariant is supplied; source `appendix_claim_ledger.tex:80-139` and `07b_agent_network_rg.tex:2813-2828`. |

## 1. Exact law-level VFE coarse-graining

The primary RG object is not an energy or coupling vector. At each level the
manuscript declares a standard-Borel space, a probability reference
`rho_l`, a finite positive measure `m_l << rho_l`, its mass `M_l`, and the
normalized law `pi_l=m_l/M_l`. A normalized, parameter-independent Markov
kernel `K_l` pushes **both** measures:

```
rho_{l+1}=rho_l K_l,       m_{l+1}=m_l K_l,
H_{l+1}=-log[d m_{l+1}/d rho_{l+1}].
```

This is defined at `07_general_renormalization.tex:76-109`,
`def:rg-measure-pair`, and exact composition and mass preservation are proved
at lines 111-137, `prop:rg-measure-pair-composition`. Absolute continuity at
the target is immediate: if `(rho K)(A)=0`, then `K(x,A)=0` `rho`-almost
everywhere and therefore `m`-almost everywhere.

For the VFE statement, let `Pi_o` be the fine posterior, `Q_o << Pi_o` the
recognition law, and attach the same coarse channel `C` to both. On the bridge
space define

```
Qhat(dy,dz)=Q_o(dy)C(y,dz),
Pihat(dy,dz)=Pi_o(dy)C(y,dz).
```

Attaching the same conditional kernel preserves relative entropy,
`KL(Q_o||Pi_o)=KL(Qhat||Pihat)`. Disintegrating the two bridge laws over `z`
gives

```
KL(Q_o||Pi_o)
 = KL(Q_o C || Pi_o C)
 + integral KL(Qhat(dy|z)||Pihat(dy|z)) (Q_o C)(dz).
```

The observation marginal is unchanged because `C(y,Z)=1`, so substituting
`F=KL(Q||posterior)-log p(o)` at the two levels yields exactly

```
F_P(Q_o)
 = F_{P^c}(Q_o C)
 + E_{Q_o C} KL(Qhat(.|Z)||Pihat(.|Z)).
```

This reconstructs `07b_agent_network_rg.tex:34-66`,
`thm:rg-exact-coarse-vfe`, including its extended-real convention. Equality
between fine and coarse VFE holds exactly when the conditional inference gap
vanishes, namely when the two conditional fine laws agree for `Q_o C`-almost
every `z`. The evidence has not improved; only unresolved conditional
information has been discarded.

The theorem fails outside its quantifiers. Different generative and
recognition channels need not preserve the fine KL; a fitted coarse generative
law need not preserve evidence; and coarsening the observation changes the
event being bounded. These are explicit exclusions at source lines 68-73.
Thus the VFE monotonicity is an exact data-processing identity, not a license
to compare arbitrary fitted models across scales.

**Falsification condition.** RG-1 would be false if one produced standard-Borel
spaces, a common fixed normalized channel, `Q_o << Pi_o`, and finite evidence
for which the relative-entropy chain rule above failed. Changing either
channel or the observation is not a falsifier because it violates a stated
premise.

## 2. Full finite-network Hoeffding interaction theory

### 2.1 Typed domain and the nonautomatic premise

At level `l`, take a finite vertex set `V_l`, standard-Borel coordinate spaces,
and a product probability reference

```
X_l = product_{i in V_l} X_{li},
nu_l = tensor_{i in V_l} nu_{li},
pi_l ~ nu_l.
```

Mutual absolute continuity makes `L^infinity(pi_l)` and
`L^infinity(nu_l)` the same normed equivalence-class space because they have
the same null sets. Product structure, not equivalence alone, makes the
coordinate integrations below well defined. The target premise
`pi_{l+1}=pi_l K_l ~ nu_{l+1}` is separately required
(`07b_agent_network_rg.tex:1133-1152`,
`eq:rg-interaction-product-reference`).

This premise is not preserved by an arbitrary Markov channel. The manuscript's
diagonal-cloning witness maps a uniform bit `x` to `(x,x)`. The target law is
supported on `(0,0)` and `(1,1)`. Any product measure charging both diagonal
atoms must charge both values in both marginals and hence both off-diagonal
atoms, so it cannot be equivalent to the target. This directly proves
`prop:rg-product-equivalence-not-preserved` at lines 1160-1180. In that case
the law-level pushforward remains exact, but the target product-reference
Hoeffding tier is unavailable.

### 2.2 Projectors, inverse theorem, bounds, and equality family

For `A subset V_l`, define conditional integration against the product
complement,

```
(C_A f)(x_A) = integral f(x_A,y_{A^c}) nu_{A^c}(dy_{A^c}).
```

Product Fubini gives `C_A C_B=C_{A intersect B}`. Define the Boolean Mobius
projectors

```
P_A = sum_{B subset A} (-1)^{|A|-|B|} C_B.
```

Because the `C_A` commute and obey the intersection law,

```
P_A P_B = 1_{A=B} P_A,       sum_{A subset V_l} P_A = I.
```

The range `H_A=P_A L^infinity(nu_l)` consists of functions of `x_A` whose
product-reference mean vanishes in every active coordinate. Let

```
G_l = l1-direct-sum_{empty != A subset V_l} H_A,
||g||_G = sum_A ||g_A||_infinity,
E_l g = [sum_A g_A],
H_l[f] = (P_A f)_{A != empty},
```

where brackets quotient by constants. The projector identities immediately
give

```
H_l E_l = I_G,       E_l H_l = I_{L^infinity/R1}.
```

Assembly obeys `||E_l||<=1`. Since `P_A` is an alternating sum of `2^{|A|}`
conditional contractions,

```
||H_l|| <= sum_{A != empty} 2^{|A|} = 3^{|V_l|}-1.
```

This reconstructs `07b_agent_network_rg.tex:1182-1255`,
`thm:rg-hoeffding-action-isomorphism`.

The worst-case constant is genuinely sharp across product measures. For
independent biased Rademacher variables with `P(X_i=1)=p` and
`f=product_i X_i`, set `m=2p-1`. Direct expansion gives

```
P_A f = m^{n-|A|} product_{i in A}(X_i-m),
sum_{A != empty} ||P_A f||_infinity
 = (4p-1)^n-(2p-1)^n -> 3^n-1 as p -> 1.
```

For every `p<1`, both signs occur and `||[f]||=1`, so the ratio approaches the
upper bound. This also exposes the thermodynamic boundary: the exact finite
isomorphism has no dimension-free stability constant.

### 2.3 Gauge covariance is conditional, not automatic

If a gauge re-expression is realized by a coordinate permutation and
componentwise Borel isomorphisms that transport the product reference, then
Fubini intertwines every `C_A`, hence every `P_A`, `E_l`, and `H_l`. This is
`eq:rg-hoeffding-gauge-covariance` at source lines 1257-1290. The realization
hypothesis is necessary for preserving hyperedge degree. The
Haar-measure-preserving shear `(x_1,x_2)->(x_1,x_1+x_2)` on the two-torus sends
a singleton function of `x_2` to a genuine two-coordinate function. Product
measure preservation alone therefore does not preserve the grading.

For the nonlinear step, the manuscript additionally transports the complete
measure pair and intertwines the Markov kernel. Covariance of Radon--Nikodym
derivatives then proves covariance of the nonlinear interaction map and, if
the retained projections also intertwine, both residuals
(`07b_agent_network_rg.tex:1292-1362`,
`prop:rg-interaction-rn-gauge-covariance`). Almost-everywhere kernel
equivariance yields covariance of equivalence classes, not pointwise covariance
of an arbitrarily chosen conditional version.

**Falsification condition.** RG-2 would be false if the Boolean projectors
failed to resolve a bounded action class uniquely on a finite product
probability space. A gauge transformation that mixes coordinate scopes is not
a falsifier of the covariance theorem; it violates the grading-intertwining
hypothesis and is instead the manuscript's reason for stating that hypothesis.

## 3. Exact nonlinear coarse action and derivative cocycle

Fix the normalized evidence law `pi` and a reverse conditional `Pi(z,dy)` for
the joint `pi(dy)K(y,dz)`. For a bounded action increment `phi`, the exact
coarse increment is the Radon--Nikodym-first map

```
Q(phi)(z) = -log integral exp[-phi(y)] Pi(z,dy).
```

It is finite for every bounded `phi`, is additively homogeneous
`Q(phi+c)=Q(phi)+c`, and is nonexpansive in sup norm. At a general bounded
center, define the tilted reverse law

```
Pi^phi(z,dy)
 = exp[-phi(y)] Pi(z,dy) / integral exp[-phi] dPi(z).
```

Direct differentiation gives the exact Frechet derivatives

```
DQ(phi)[h](z) = E_{Pi^phi(.|z)} h,
D^2Q(phi)[h,k](z) = -Cov_{Pi^phi(.|z)}(h,k).
```

The denominator is bounded between `exp(-||phi||_infinity)` and
`exp(||phi||_infinity)`, so the maps are bounded. The Banach-algebra log series
proves local real analyticity at every bounded center. These statements and
their complete proof are at `07b_agent_network_rg.tex:149-365`,
`thm:rg-bounded-action-calculus` and
`prop:rg-action-bounded-recentering`.

Conjugating this action map by the exact Hoeffding isomorphisms yields

```
T_l^G = H_{l+1} o Qbar_l o E_l : G_l -> G_{l+1},
g_{l+1}^{ex}=T_l^G(g_l).
```

This is an exact nonlinear action-coordinate change, not a claim that a
pairwise ansatz closes. Its derivative at `g` is

```
D T_l^G(g)
 = H_{l+1} o U_l^{phi_g}bar o E_l,
```

where `U_l^{phi_g}` is conditional expectation under the tilted reverse law.
Replacing it by the untilted `U_l` is valid only at `g=0`. This reconstructs
`07b_agent_network_rg.tex:1367-1413`,
`eq:rg-exact-nonlinear-interaction-map` and
`eq:rg-nonlinear-interaction-derivative`.

Along an exact orbit the maps

```
D_l=D T_l^G(g_l):G_l -> G_{l+1},
D_{n<-l}=D_{n-1} ... D_l
```

form a typed derivative cocycle by the Frechet chain rule. A compatible mode
is a line satisfying

```
D_l v_{l,a} = lambda_{l,a} v_{l+1,a},
lambda_{n<-l,a}=product_{k=l}^{n-1} lambda_{k,a}.
```

The right side and left side live at the same target level. The usual equation
`D_l v=lambda v` is ill typed until level spaces have been identified. The
general definitions and proof are at
`07_general_renormalization.tex:556-678`,
`def:rg-derivative-cocycle`, `def:rg-mode-line`, and
`prop:rg-mode-product`; their interaction instantiation is at
`07b_agent_network_rg.tex:1415-1431`, `def:rg-interaction-modes`.

This establishes a cocycle and defines compatible modes **if they exist**. It
does not prove a complete mode decomposition. An Oseledets splitting would
need a measure-preserving base flow, cocycle measurability and log-integrability,
and finite dimension or suitable compactness; the manuscript correctly
declines that extension at `07_general_renormalization.tex:813-823`.

## 4. Retained projections, exact residual, and generated operators

Let `R_l:G_l->G_l` be a bounded idempotent retained projection. Define

```
g_{l+1}^{ret}=R_{l+1}T_l^G(g_l),
r_{l+1}^G=(I-R_{l+1})T_l^G(g_l),
rbar_{l+1}^Q=E_{l+1}r_{l+1}^G.
```

Because `E_{l+1}` and `H_{l+1}` are inverse,

```
rbar_{l+1}^Q=0  iff  r_{l+1}^G=0,
T_l^G(Ran R_l) subset Ran R_{l+1}
 iff r_{l+1}^G(g)=0 for every g in Ran R_l.
```

For a nonempty target network,

```
||r^G||/(3^{|V_{l+1}|}-1)
 <= ||rbar^Q|| <= ||r^G||.
```

These are exact identities, not error estimates inferred from a small sample
(`07b_agent_network_rg.tex:1468-1512`,
`eq:rg-interaction-coordinate-residual` through
`eq:rg-interaction-residual-norm-control`). The lower constant again degrades
exponentially with network size.

The full generated operator content is explicit:

1. **Hyperedges.** Marginalizing an internal variable integrates the product
   of all incident nonnegative factors and creates one factor on the union of
   their remaining scopes. For any finite-valued coarse action, anchored
   Mobius inversion reconstructs it from all subsets. An extended-valued action
   remains exact as one top-order factor. Pairwise closure fails: eliminating
   the center of a three-leaf Ising star yields
   `2 cosh(h_0+sum_r J_r s_r)`, whose negative log has nonzero cubic coefficient
   `2 sech^2(h_0)tanh(h_0)J_1J_2J_3+O(J^5)` for small nonzero couplings and
   `h_0 != 0`. Source:
   `07b_agent_network_rg.tex:1517-1565`,
   `eq:rg-full-hypergraph-action` and `eq:rg-hidden-star-factor`.

2. **Cross-scale bridge kernels.** Disintegrating the full posterior bridge
   gives exact pair-marginal agent/meta kernels, but those pair kernels do not
   reconstruct the full fine posterior. Posterior-local refinement additionally
   needs `Y_I independent of Z_{-I} given (Z_I,o)` or another sufficient
   condition. Source: lines 1570-1616,
   `eq:rg-agent-meta-bayes-adjoint`.

3. **Gauge/holonomy data.** Exact coarse state retains a component root, the
   full based holonomy representation, and every dressed marked boundary edge.
   Separately quotienting conjugacy classes loses their relative orientation;
   a naive noncompact conjugacy quotient may not even be standard Borel.
   Source: lines 1621-1673,
   `eq:rg-full-holonomy-representation` and
   `eq:rg-dressed-boundary-edge`.

4. **Attention.** The exact object is the joint marked event law
   `eta_{ij}=alpha_i beta_{ij}`. Coarsening pushes `eta`, then recovers
   `alpha^c` and `beta^c` by disintegration. Pushing `beta` alone is not
   associative because it omits receiver occupancy. An averaged transported
   operator need not lie in the group and separate averages of marks and
   features need not recover their product; exact closure retains the marked
   operator-feature kernel. Source: lines 1748-1883,
   `eq:rg-meta-attention` and `eq:rg-attention-hom-operator`.

5. **Memory.** Pushing a full finite path law is exact but need not preserve
   first-order Markov structure. On the linear observable tier, with
   `Pi_res=PC` and `Q=I-Pi_res`, elimination gives memory operators

   ```
   C T Q (Q T Q)^m Q T P,      m>=0,
   ```

   plus an unresolved initial-state term. The exact recurrence is proved at
   `07b_agent_network_rg.tex:2027-2111`,
   `thm:rg-projection-memory`. Markov/autonomous closure requires those total
   corrections to vanish; `QTP=0` is sufficient on resolved initial data but
   is not necessary, as the manuscript's two-dimensional witness shows.

Thus the manuscript does what an effective-theory audit requires: it names
the generated terms and makes a restricted ansatz pay an explicit residual.
It does not make the residual small, uniformly controlled, or dynamically
stable unless additional estimates are supplied.

**Falsification condition.** RG-3 or RG-4 would fail if an admitted finite
product-equivalent bounded action had a coarse action outside the full
Hoeffding image, if the derivative differed from the tilted conditional mean,
or if the displayed coordinate and action residuals disagreed. A generated
higher-body term outside a pairwise ansatz confirms, rather than falsifies,
the full-interaction theorem.

## 5. Cross-scale growth, beta data, and scheme dependence

### 5.1 Growth rates

For block ratios `b_k>1`, the manuscript declares cumulative log scale

```
s_{n<-l}=sum_{k=l}^{n-1} log b_k.
```

For a mode line, the scalar exponent is

```
upsilon_{n<-l,a}
 = [sum_k log|lambda_{k,a}|]/s_{n<-l}.
```

The norm growth differs by the endpoint normalization term

```
[log||v_{n,a}||_n-log||v_{l,a}||_l]/s_{n<-l}.
```

Hence scalar and norm growth agree only for normalized or tempered mode
sections. Bounded isomorphisms `J_l:X_*->X_l` preserve asymptotic rates only
when both `J_l` and `J_l^{-1}` grow subexponentially relative to cumulative
scale. The witness `J_k=e^{k^2}` applied to an identity cocycle changes an
apparent exponent from zero to `-infinity`. Source:
`07_general_renormalization.tex:680-811`,
`def:rg-mode-exponents`, `thm:rg-tempered-comparison`, and
`prop:rg-superexponential-distortion`.

The interaction Hoeffding bound yields one conditional tempering result:
comparison maps assembled with no worse than `O(3^{|V_l|})` coordinate
distortion are tempered if `|V_n|/s_{n<-l}->0`. This is automatic along a
strictly shrinking finite blocking tower, but not along a thermodynamic family
whose network size grows rapidly with depth
(`07b_agent_network_rg.tex:1433-1466`,
`cor:rg-interaction-tempered`). The existence of the comparison isomorphisms
themselves remains a separate premise; spaces of different finite dimension
need not be isomorphic.

### 5.2 Measure-pair and action beta functions

A genuine common-space RG step requires a coarse channel `C_b` and a declared
rescaling/identification kernel `I_b`, with endokernel `K_b=C_b I_b`. Autonomy
requires

```
K_{b_1 b_2}=K_{b_1}K_{b_2}.
```

Only then do the measure-pair maps form a semigroup. Without it they form a
typed nonautonomous cocycle. Source:
`07b_agent_network_rg.tex:2124-2145`,
`eq:rg-kernel-semigroup` and `eq:rg-measure-pair-map`.

On a finite-valued vector space closed under the reference-dependent action
map, the discrete action beta is

```
B_b^H[H;rho] = (R_b^H[H;rho]-H)/log b.
```

It is undefined at extended-valued points where subtraction would form
`infinity-infinity`. It is also reference dependent. If
`rho'=e^{-Delta}rho`, `H'=H-Delta`, and `rho(e^{-Delta})=1`, then direct
Radon--Nikodym algebra gives

```
B_b^H[H';rho']
 = B_b^H[H;rho]-B_b^H[Delta;rho].
```

This is an inhomogeneous reference law, not ordinary coordinate conjugacy
(`07b_agent_network_rg.tex:2147-2222`,
`prop:rg-action-beta-reference-change`).

For full interactions, comparison isomorphisms
`J_l:G_*->G_l` are required before subtraction. The exact, retained, and
residual beta terms obey

```
T_hat_l = J_{l+1}^{-1} T_l^G J_l,
beta_l^ex(g)=(T_hat_l(g)-g)/Delta s_l,
delta beta_l(g)
 = J_{l+1}^{-1} r_{l+1}^G(J_l g)/Delta s_l.
```

The retained beta is exact on its whole sector exactly when
`T_l^G(Ran R_l) subset Ran R_{l+1}`. Bounded idempotence alone does not imply
this. With `R(x,y)=(x,0)` and `T(x,y)=(x,x)`, the retained beta vanishes on
every `(x,0)` while the exact beta generates `(0,x)`. This is an explicit
false-fixed-point witness at source lines 2224-2323,
`prop:rg-retained-beta-residual`.

Changing comparison maps by `J_l'=J_l S_l` gives

```
T_hat_l'=S_{l+1}^{-1} T_hat_l S_l,
beta_l'(g)
 =[S_{l+1}^{-1}T_hat_l(S_l g)-g]/Delta s_l.
```

For scale-dependent `S_l` this is not the usual pushforward of a vector field.
Even a native identity step on `R` has apparent beta
`(a_l/a_{l+1}-1)g` in the moving frame `J_l u=a_l u`. This directly refutes
any claim that raw beta components are scheme-independent
(`07b_agent_network_rg.tex:2325-2341`,
`eq:rg-interaction-beta-scheme-change`).

### 5.3 Continuous beta data are extra structure

A continuous beta requires a `C^1` scale manifold, a Banach coupling bundle,
and a scale connection. In a local trivialization,

```
I_s beta^scale = partial_s g_tilde + A_s g_tilde,
A_s' = S_s A_s S_s^{-1}-(partial_s S_s)S_s^{-1}.
```

For differentiable positive densities satisfying the same forward generator,
the exact action formula is

```
dot H_t
 = -A^*(r_t e^{-H_t})/(r_t e^{-H_t}) + A^*r_t/r_t,
```

on the declared ratio and generator domain. A component beta additionally
needs a complete Schauder/Riesz basis and a justified differentiation/extraction
interchange. Source: `07b_agent_network_rg.tex:2343-2417`,
`def:rg-scale-connection` and `eq:rg-continuous-beta-functional`.

Discrete endpoints do not determine this structure. The evolution families

```
V^(0)(s,t)=1,
V^(epsilon)(s,t)=exp{epsilon[sin(2 pi s)-sin(2 pi t)]}
```

agree at every integer endpoint but have generators `0` and
`2 pi epsilon cos(2 pi s)`. This exact witness
(`prop:rg-continuous-beta-underdetermined`, source lines 2419-2461) rules out
deriving a unique continuous beta from a discrete blocking sequence.

## 6. Fixed objects and nonautonomous flows

At the normalized measure-pair tier, a fixed theory satisfies

```
R_b(rho_*,m_*)=(rho_*,m_*) for every declared b.
```

On the dominated tier this is equivalent to simultaneous reference invariance
and action invariance. A projective fixed ray `R_b^H H_*=H_*+c(b)` is weaker;
it represents the tracked fixed pair only when reference invariance and mass
normalization force `c(b)=0`. A fixed attention row is likewise insufficient:
the fixed object is the joint event law `eta=alpha beta`, so both occupancy and
the row must be fixed. Source:
`07b_agent_network_rg.tex:2489-2516`,
`thm:rg-fixed-point-equations`.

For a general nonautonomous tier, the invariant object is a section
`y_{l+1}=F_l(y_l)`. With declared isomorphisms to a common object, a reference
fixed object is fixed by every transported step. For a period-`p` family, the
appropriate fixed object may instead be a monodromy fixed point and its
`p`-cycle; its points need not be fixed by any one-step map. These typed
definitions are at lines 2582-2650, `def:rg-typed-fixed-objects`.

Fixedness does not transfer between tiers. The manuscript supplies finite
witnesses: a fixed law with alternating reference has alternating actions; a
fixed action class can change evidence mass; a projected fixed interaction can
have nonzero exact residual; a constant law extraction can hide a fixed-point-free
antipodal configuration map; a fixed attention row can accompany alternating
occupancy; and period-two maps `x->x+1`, `x->x-1` have identity monodromy while
neither one-step map has a fixed point
(`07b_agent_network_rg.tex:2652-2687`,
`prop:rg-fixed-object-nonimplication`).

Uniform projective contraction also does not force one scale-independent ray.
The alternating strictly positive matrices at
`07_general_renormalization.tex:522-542`,
`prop:rg-contraction-no-fixed-ray`, forget initial data but approach a two-cycle.
Thus an ordinary zero of one beta vector field is the right object only in an
autonomous common-space scheme.

## 7. Gaussian/Hermite realization

Let `X_1,...,X_b` be independent standard Gaussians and

```
Z=b^{-1/2} sum_i X_i.
```

The output is again standard Gaussian, so the extensive score operator

```
L_b h = E[sum_i h(X_i) | Z]
```

is an endomorphism of `L^2_0(gamma)`. For the normalized probabilists' Hermite
basis `e_k=He_k/sqrt(k!)`, the pair `(X_i,Z)` has correlation `b^{-1/2}`.
The conditional generating function is

```
E[exp(tX_i-t^2/2)|Z=z]
 = exp((t/sqrt b)z-t^2/(2b)),
```

so coefficient comparison gives

```
E[He_k(X_i)|Z]=b^{-k/2}He_k(Z),
L_b e_k=b^{1-k/2}e_k.
```

The Hermite basis is complete, hence this is the complete diagonal operator.
Its eigenvalues are positive, distinct, and tend to zero. Their squared sum is
`sum_{k>=1} b^{2-k}=b^2/(b-1)`, so the operator is Hilbert--Schmidt and compact.
Its norm and spectral radius are `sqrt b`. The zero value is not an eigenvalue
because the kernel is zero; it lies in the continuous spectrum because the
range is dense but nonclosed. The source gives the same proof at
`07b_agent_network_rg.tex:871-946`,
`thm:rg-gaussian-hermite-spectrum`.

With cumulative scale `log b`, the declared mode exponents are

```
y_k=1-k/2.
```

Degree one is relevant, degree two marginal, and degrees at least three
irrelevant. The growth is not a violation of data processing: conditional
expectation is contractive, but the separately declared independent-block
replication lift has norm `sqrt b`. The extensive normalization creates the
relevant direction.

The equality and boundary cases are explicit:

- If the block channel retains the extensive score as a measurable function,
  the Fisher defect is zero; if it maps the entire block to a point, all scores
  vanish.
- For equicorrelated unit Gaussians with correlation
  `rho>-1/(b-1)` and unit-variance normalized sum, the eigenvalue becomes
  `b^{1-k/2}[1+(b-1)rho]^{k/2}`. Thus the independent spectrum is not
  correlation universal.
- In dimension `d`, degree `k` has multiplicity
  `binomial(d+k-1,k)`. General `GL(d)` re-expression changes the reference
  covariance and requires transported law/norm data; it is not covered by the
  scalar theorem.
- The operator is only the derivative at the Gaussian law. No nonlinear basin,
  remainder bound, or control of the marginal degree-two direction follows.

These boundaries are proved at `07b_agent_network_rg.tex:973-1024`,
`prop:rg-hermite-scope`, and are recorded as open obligations at
`appendix_claim_ledger.tex:100-114`.

The separate MVG operator chapter has a different, finite-dimensional exact
sector. Hard aggregation sends `A->bA`, `W->b^2W` on a homogeneous complete
graph; dense rescaling fixes the coupling ray and contracts self terms by
`1/b`. This produces a singular boundary operator, not a normalized Gaussian
fixed law (`10_renormalization.tex:146-188`). Sum-only aggregation preserves
matrix faces and cannot select a matrix direction; Sylvester congruence reduces
one PSD coupling matrix to its rank but does not classify graphs, basins,
spectral measures, or schemes (`10_renormalization.tex:215-287`). The exact
finite sector therefore does not upgrade the Hermite tangent calculation into
universality.

**Falsification condition.** RG-6 would be false if the conditional Hermite
regression at the independent normalized Gaussian fixed law produced any
coefficient other than `b^{-k/2}`, or if the resulting complete diagonal
operator had the wrong spectrum. Correlated, anisotropic, non-Gaussian, or
nonlinearly iterated laws are outside the theorem and require new proofs.

## 8. Gaussian factorization gap

Let `p=N(mu,Lambda^{-1})` with `Lambda` positive definite and impose only that
the recognition covariance be block diagonal for a partition. The Gaussian
KL is

```
KL(N(nu,Sigma)||p)
 = 1/2[(nu-mu)^T Lambda(nu-mu)
       +tr(Lambda Sigma)-log det Lambda-log det Sigma-d].
```

The mean optimum is `nu=mu`. For block-diagonal `Sigma=directsum Sigma_I`, the
trace separates as `sum_I tr(Lambda_II Sigma_I)` and
`log det Sigma=sum_I log det Sigma_I`. Each strictly convex block problem has
optimum `Sigma_I=Lambda_II^{-1}`. Substitution gives

```
G_fact
 = 1/2[sum_I log det Lambda_II-log det Lambda].
```

This directly proves `09_coarsegraining.tex:1002-1011`,
`eq:cg-factorization-gap`, whose source text states the result without the
intermediate optimization.

Fischer's determinant inequality gives
`det Lambda <= product_I det Lambda_II`, so the gap is nonnegative. Merging two
blocks replaces `log det Lambda_II+log det Lambda_JJ` by
`log det Lambda_{I union J,I union J}`, which cannot increase the gap. For a
positive-definite matrix, equality in that merge holds exactly when
`Lambda_IJ=0`. The full gap is zero exactly when `Lambda` is block diagonal in
the chosen partition. The coarsest one-block partition therefore has zero gap;
the gap is generally positive at the finest singleton partition.

This monotonic endpoint behavior does not select an intrinsic scale. The
mean-tie cost is minimized at the finest partition while the factorization gap
is minimized at the coarsest; combining them needs an externally supplied
coefficient or a new nonmonotone functional. The manuscript correctly leaves
the existence of a nondegenerate selector open at
`09_coarsegraining.tex:1013-1025` and
`appendix_claim_ledger.tex:216-220`.

**Falsification condition.** RG-7 would be false if the stated
`KL(q||p)` optimum over block-product Gaussians were not
`Sigma_I=Lambda_II^{-1}`, or if an SPD merge increased the log-determinant
gap. The opposite KL orientation, a non-Gaussian or singular family, or a
mean-tied problem is a different optimization and is not a falsifier.

## 9. Path graph, Karamata, and the two-index boundary

### 9.1 Exact path quotient and noncommuting limits

For `m=b^n`, partition the unweighted path into consecutive blocks of size
`b^l`. With the unnormalized block indicator `S`, the quadratic form identity

```
z^T S^T L_m S z
 = sum_j (z_{j+1}-z_j)^2
 = z^T L_{m/b}z
```

proves `S^T L_m S=L_{m/b}`. Iteration gives the path on `b^{n-l}` vertices.
Orthonormal indicators introduce the declared factor `b^{-l}`. This is a
direct proof of `07_general_renormalization.tex:882-925`,
`eq:rg-path-galerkin-quotient`.

The path eigenvalues are

```
lambda_{m,k}=2-2 cos(pi k/m),      0<=k<=m-1.
```

Therefore the zero-mode-excluded normalized count converges at every fixed
depth to

```
U_infinity(lambda)
 = pi^{-1} arccos(1-lambda/2),       0<=lambda<=4,
U_infinity(lambda) ~ pi^{-1} sqrt(lambda) as lambda down to 0.
```

At maximal depth `l=n`, however, the quotient is always `Path_1`; its full
spectral law is `delta_0` and its zero-mode-excluded count is identically zero.
Thus fixed-depth thermodynamic and maximal-depth limits disagree. The exact
count, endpoints, Riemann-sum proof, and limiting formula are at source lines
927-1021, `prop:rg-noncommuting-limits`.

This is a direct counterexample to any inference that an exact finite
coarse-operator identity determines a unique thermodynamic RG limit. A
triangular family and diagonal scaling `l(n)` must be stated.

### 9.2 Abelian Karamata calculation

Let `U(lambda)=N(lambda)-N(0)` be nondecreasing and right-continuous with
`U(0+)=0`, and suppose

```
U(lambda) ~ c lambda^alpha L(1/lambda),
```

where `alpha>0`, `L` is slowly varying, and the positive heat trace is finite
at some `t_0>0`. Define

```
M_k(t)=integral_{(0,infinity)} lambda^k e^{-t lambda} dU(lambda).
```

The Abelian Stieltjes-Karamata theorem gives

```
M_k(t) ~ c alpha Gamma(alpha+k) t^{-(alpha+k)} L(t),
k=0,1,2.
```

Consequently

```
M_1/M_0 ~ alpha/t,
M_2/M_0 ~ alpha(alpha+1)/t^2.
```

For `S_+(t)=log M_0+tM_1/M_0`, differentiation under the exponentially
damped integral gives

```
-dS_+/d log t
 = t^2[M_2/M_0-(M_1/M_0)^2] -> alpha.
```

This reconstructs `07_general_renormalization.tex:1029-1057`,
`eq:rg-heat-susceptibility`, including its coefficient. It is the forward
Abelian implication only; a plateau does not by itself prove regular variation.

For the fixed-depth path limit, `alpha=1/2`, `c=1/pi`, and `L=1`, so the
zero-mode-excluded thermodynamic susceptibility tends to `1/2`. For every
fixed finite path with at least one positive mode, by contrast, the heat law
concentrates on its smallest positive eigenvalue and the susceptibility tends
to zero; at `Path_1` the zero-mode-excluded heat normalization is absent
altogether. This is another explicit order-of-limits warning.

Dividing the entropy by `log|V_n|` also divides the susceptibility by that
factor and destroys a nonzero plateau. Zero-mode treatment and normalization
are therefore part of the observable, not cosmetic conventions
(`07_general_renormalization.tex:1059-1062`).

**Falsification condition.** RG-8 would be false if the exact path spectrum or
quotient identity were wrong, or if a regularly varying count satisfying the
stated integrability hypotheses produced a different Abelian heat limit.
Failure of regular variation, changing the zero-mode convention, reversing the
limit order, or normalizing entropy differently changes the theorem rather
than falsifying it.

## 10. What the complete finite theorem does and does not establish

The closure theorem at `07b_agent_network_rg.tex:2735-2772`,
`thm:rg-complete-effective-theory`, assumes:

- a finite standard-Borel agent hypergraph and the already-defined common
  principal/associated statistical bundle data;
- normalized gauge-covariant baseline and interaction-record kernels with
  positive finite evidence;
- normalized recognition laws with the required absolute continuity and
  log-integrability;
- recognition-independent, gauge-equivariant structural coarse channels;
- globally gauge-equivariant measurable versions of every displayed
  disintegration;
- pushed references, full root-framed holonomy and boundary data, joint marked
  attention events, every generated hyperedge, and full path laws or exact
  memory kernels; and
- rescaling kernels satisfying the declared semigroup law.

Under those assumptions, normalization is preserved by Markov pushforward,
the VFE identities follow from relative-entropy disintegration, hypergraph
closure follows from Mobius inversion/top-order retention, bridge and attention
kernels follow from disintegration, holonomy dressing preserves covariance,
path closure follows by path-law pushforward, and semigroup composition is
typed on the measure pair. That is a valid finite composition proof. The
analytic corollary at lines 2774-2811 adds, rather than hides, the dominators,
bounded/finite action spaces, comparison isomorphisms, residuals, smooth scale
bundle, generator domain, basis/interchange, fixed-reference, and positive
likelihood hypotheses required for beta and linearization.

The theorem is nonvacuous. For example, on finite binary coordinate spaces,
take a strictly positive Gibbs density relative to the uniform product law and
a surjective block statistic. Its pushed law has full support on the finite
target, hence is equivalent to the uniform target product reference; every
action is bounded, the Hoeffding theorem applies, and generated interactions
are exactly represented. The trivial gauge group satisfies the gauge premises,
and any nontrivial componentwise equivariant realization satisfying the stated
kernel intertwining does as well. The Gaussian normalized-sum construction is
a separate inhabited tangent/fixed-law sector. Thus the assumptions do not
make the finite theorem vacuous.

They do, however, make its scope conditional:

- The law-level construction survives when product equivalence fails; the
  Hoeffding coordinate tier does not.
- `L^infinity` action calculus covers bounded perturbations. Extended-valued
  actions remain measure-pair objects but do not inherit differential beta
  data.
- Retaining the full power set is exact but exponentially large and generally
  infinite dimensional inside each component when coordinate spaces are
  continuous.
- A nontrivial finite retained ansatz has not been shown invariant. Every such
  flow must carry the residual.
- The semigroup/rescaling and common comparison data needed for an autonomous
  RG are supplied as hypotheses, not selected by the VFE.
- Equivariant versions of regular conditionals are assumed where needed; plain
  standard-Borel disintegration supplies only almost-everywhere versions.

The strongest accurate one-sentence theorem is therefore:

> For each admitted finite gauge-VFE network and fixed equivariant Markov
> coarse channel, exact pushforward yields a normalized effective VFE law; if
> equivalent product references and bounded perturbations are available, the
> entire induced action is represented exactly by all finite Hoeffding
> hyperedges, and every retained truncation has an exact residual; RG beta,
> mode, and fixed-object statements become exact only after their declared
> reference, rescaling, norm, and dynamical-type data are supplied.

## 11. Universality and infinite-volume exclusions

The manuscript does not prove any of the following:

1. a canonical or nondegenerate partition selector;
2. an invariant nonzero proper retained interaction subspace;
3. existence of a complete cross-scale mode/Oseledets splitting;
4. nonlinear attraction to the Gaussian or MVG candidate;
5. a scheme-independent beta function or blocking-independent critical data;
6. completeness of rank plus any spectral exponent as a universality label;
7. a projectively consistent infinite interaction coordinate with uniform
   Hoeffding bounds;
8. existence or uniqueness of a DLR/thermodynamic state;
9. convergence of free-energy densities;
10. commutation of volume and RG-depth limits or a nontrivial diagonal limit;
11. a continuum physical law or empirical universality class.

For a countable agent/time index, projectively consistent normalized cylinder
laws on standard-Borel coordinates do yield a full joint law by Kolmogorov
extension. That only extends finite-cylinder identities. An infinite record
can still have probability zero; conditioning then requires a selected
almost-everywhere regular conditional or a proved DLR, Doob-transform, or
finite-volume posterior limit. Infinite-law KL additionally needs compatible
absolute continuity and an infinite coarse channel. These exact boundaries are
stated at `07b_agent_network_rg.tex:2813-2828`.

The finite theorem is said to be uniform in the number and arrangement of
agents in the logical sense that the same proof applies to every finite
network. It is not analytically uniform in volume: the Hoeffding inverse bound
is `3^{|V|}-1`. The path graph proves that even exact closure at every finite
stage does not determine the diagonal thermodynamic limit. The moving-frame
beta witness proves that raw beta components can change without changing the
native step. The correlated Gaussian formula proves that the explicit
relevance spectrum changes with dependence and normalization. These are direct
obstructions to promoting finite exactness to universality.

The manuscript's open-obligation ledger accurately records these exclusions
at `appendix_claim_ledger.tex:80-139` and `194-232`. The positive existence of
some future universality theorem is not refuted. To close it one would need, at
minimum, a specified triangular family and boundary conditions; projective or
DLR existence; uniform residual/tightness estimates; convergence of intensive
free energies and chosen invariant observables; a proved diagonal or
limit-exchange theorem; an autonomous map or a fully specified cocycle; a basin
or invariant-section theorem; and robustness under a declared class of
blocking and comparison schemes.

## 12. Oracle erasure, decisive attacks, and final adjudication

The affirmative-existence preference was removed from the logical premises.
The reconstruction still produces RG-1 through RG-9 from explicit definitions
and direct proofs. The following adversarial attacks were decisive in fixing
the scope:

- **Product-reference attack — sustained as a boundary.** Diagonal cloning
  destroys equivalence to every product target reference. It blocks the
  Hoeffding tier, not the primary law-level theory.
- **Pairwise-closure attack — sustained.** The hidden Ising star generates a
  cubic interaction. Exactness requires the full hypergraph or a residual.
- **Projected-fixed-point attack — sustained.** The two-dimensional `R,T`
  witness gives zero retained beta and nonzero exact beta.
- **Autonomous-flow attack — sustained.** Semigroup, reference-space, and
  rescaling data are premises; a general sequence is a cocycle. A continuous
  beta is underdetermined by discrete endpoints.
- **Universality attack — sustained.** Hermite eigenvalues change with
  correlation and normalization; raw beta changes under moving comparison
  frames; one rank or exponent is not a complete universality invariant.
- **Thermodynamic attack — sustained.** Exact path quotients have different
  fixed-depth and maximal-depth limits, and the finite Hoeffding constants are
  not uniform.
- **Finite-theory nonexistence attack — rejected.** The finite discrete
  strictly positive example inhabits all product/action hypotheses, and the
  law-level pushforward exists on every admitted finite standard-Borel model.

### Final status

- **Exact finite-network effective VFE theory:** `EVIDENCE_VERIFIED`, under the
  explicit law, channel, gauge, support, integrability, and disintegration
  hypotheses.
- **Exact finite-network full-interaction action theory:**
  `EVIDENCE_VERIFIED`, additionally conditional on equivalent product
  references and bounded perturbations.
- **Autonomous finite-network RG with beta/modes/fixed points:**
  `EVIDENCE_VERIFIED` only as a conditional construction after rescaling,
  comparison, reference, norm, and closure/residual data are supplied; no
  canonical instance is inferred.
- **Universality or infinite-volume/continuum theory:** `INCONCLUSIVE/OPEN` as
  an existential program. The inference from finite exactness to such a theory
  is `REFUTED`.

This is precisely an **effective finite-network gauge-VFE/RG framework**, not a
completed Wilsonian universality theorem or thermodynamic field theory.
