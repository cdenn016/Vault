# Pass 2: variational and coarse-scale semantics

**Review baseline:** `f568b7b18973268fc1febafd3805f3cce64f933d`
**Lens:** exact ELBO semantics, recognition restrictions, Markov coarse maps,
law pushforwards versus energy precomposition, changing latent inventories,
attainment, and independent belief/model gauge actions
**Scope:** `03_probability.tex`, `04_generative.tex`, `05_elbo.tex`,
`05a_expfamily.tex`, `07_restrictions.tex`, `09_coarsegraining.tex`, and
`10_renormalization.tex`
**Verdict:** two high findings and two medium findings; no R1--R21 regression

## Bottom line

The exact fixed-model ELBO in Chapters 3--8 is sound under its declared
absolute-continuity and log-integrability hypotheses. The Gaussian restriction
optima are attained where the text says they are, and the text correctly
withholds attainment in the general exponential-family projection problem.

The strongest new problem is a quantifier error in the cross-inventory
discussion. A change of latent inventory does **not** by itself make two ELBOs
incomparable. If the coarse joint is the Markov pushforward of the fine joint,
the observation marginal and evidence are exactly the same, relative entropy
contracts, and the coarse ELBO is at least the fine ELBO. The manuscript proves
this for exact marginalization in `09_coarsegraining.tex:42-81`, then denies it
for inventory changes in general at `07_restrictions.tex:339` and
`09_coarsegraining.tex:797`. The correct dividing line is not “same inventory
versus different inventory”; it is “one fixed joint connected by a normalized
channel versus separately declared models with no evidence-preserving
relation.”

The second high issue is the general gauge type. The current construction makes
the belief and model actions two representations of the same local group
element. The author's required general theory instead has separate principal
bundles and connections whose independent gauge changes induce automorphisms
\(U^b\) and \(U^m\) of the associated belief and model bundles. The notation
\(\Phi:\mathcal E_b\to\mathcal E_m\) and
\(\widetilde\Phi:\mathcal E_m\to\mathcal E_b\) is reserved for cross-fiber
associated-bundle morphisms covering \(\mathrm{id}_{\mathcal C}\), while
\(\Omega\) and \(\widetilde\Omega\) denote the same-channel transports induced
by the two connections. One exact ELBO remains invariant under the resulting
product action. The current shared-frame construction is a valid diagonal
specialization, not the general statement.

## Claim ledger

| Claim checked | State | Closure |
|---|---|---|
| Different latent inventories automatically imply different evidences and block any ordered ELBO comparison | `REFUTED` | Exact Markov-pushforward derivation and the manuscript's own marginalization theorem |
| A normalized Markov coarse map applied to both posterior and recognition law preserves the evidence and cannot lower the ELBO | `EVIDENCE_VERIFIED` | Conditional-Jensen proof below; finite-space KL chain-rule residual checked symbolically as exactly zero |
| Finite KL equality under a Markov map is equivalent to fiberwise measurability of the likelihood ratio and gives pairwise Bayes recovery | `EVIDENCE_VERIFIED` | Strict conditional Jensen plus explicit regular-conditional recovery proof |
| Pairwise equality automatically gives one recovery kernel for every model parameter | `REFUTED` | The Bayes reverse kernel is reference-law dependent; experiment-level recovery requires one parameter-independent kernel |
| The current one-group action is the required general belief/model covariance | `REFUTED` relative to the authorial type requirement | Source fixes a diagonal action; the product-action theorem below works with separate associated-bundle actions, connections, and cross morphisms |
| One exact ELBO remains invariant under independent belief and model frame changes | `EVIDENCE_VERIFIED` | Common product-pushforward proof below |
| Excluding the posterior from a recognition family forces a strictly positive optimized KL gap | `REFUTED` | Gaussian open-half-line counterexample; exact SymPy derivative and boundary limit |
| The declared RG recursion already supplies a cross-scale ELBO | `REFUTED` | It flows only an operator sector, omits a rescaling law for \(h\), and declares no sequence of normalized generative joints or recognition channels |

## Findings

### 1. “Different inventory” is used as the wrong boundary for comparable ELBOs

**Location:** `manuscripts/gauge_vfe_rg/07_restrictions.tex:304-339`;
`manuscripts/gauge_vfe_rg/09_coarsegraining.tex:42-81,797`

**Severity:** high

**Claim status:** `REFUTED` by an exact derivation and by a theorem already
present in the manuscript.

**Evidence:**

`07_restrictions.tex:304-312` proves only the valid no-order statement for two
arbitrary normalized joints:

> “Let \(P_\theta\) and \(P_{\theta'}\) be normalized joints over the same
> observation but different latent inventories ... [the difference] combines
> an evidence difference ... with a tightness difference.”

The prose then strengthens that conditional result into a universal claim at
`07_restrictions.tex:339`:

> “As soon as the comparison replaces one latent inventory by another ... the
> two bounds bound different numbers and their difference is not a cost.”

`09_coarsegraining.tex:797` repeats the universal form:

> “Comparing partitions with different numbers of clusters means comparing
> models with different latent inventories, and a bound on one model's
> evidence stands in no order relation to a bound on another's; both are lower
> bounds on different numbers.”

But `09_coarsegraining.tex:42-81` has already constructed the counterexample to
that universal statement. Exact marginalization deletes \(Y_2\), changes the
latent inventory from \((Y_1,Y_2)\) to \(Y_1\), preserves the evidence by
Fubini, and proves
\[
\sup_{Q_1}\mathcal L^1(Q_1)\geq \sup_Q\mathcal L(Q)
\]
by KL data processing.

**Derivation and counterexample:** Let \(P(do,dx)\) be the fixed normalized
joint, \(K:x\rightsquigarrow z\) a normalized Markov kernel independent of
the recognition law, and
\[
\bar P(do,dz)=\int K(x,dz)P(do,dx).
\]
Then \(\bar P^O=P^O\), because integrating \(K(x,\mathsf Z)=1\) leaves the
observation marginal unchanged. For every regular observation \(o\),
\(\bar P_o=P_oK\). Given \(Q_o\), set \(\bar Q_o=Q_oK\). Hence
\[
\begin{aligned}
\bar{\mathcal L}(\bar Q_o;o)
&=\log p(o)-D(Q_oK\Vert P_oK)\\
&\geq \log p(o)-D(Q_o\Vert P_o)
=\mathcal L(Q_o;o).
\end{aligned}
\]
The inventories differ, but the two bounds are ordered because they bound one
fixed evidence. Taking \(K\) to be the coordinate projection
\((Y_1,Y_2)\mapsto Y_1\) is exactly the manuscript's Operation Two. Taking
\(Q_o=P_o\) makes both bounds equal to the same evidence, which is already a
one-line counterexample to “different inventory implies different bounded
number.”

This is not R21. R21 concerned a generative family indexed by the recognition
law. Here \(P\) is fixed and \(K\) is recognition-independent.

**Minimal rigorous repair:** Replace every inventory-based prohibition by:
“ELBOs on different latent spaces are comparable when the coarse joint is an
evidence-preserving Markov pushforward of the fine joint and the recognition
laws are related by the same channel; absent such a relation, their difference
mixes evidence and tightness.”

**Falsification condition:** Produce a normalized Markov kernel \(K\) for which
\((\mathrm{id}_{O}\otimes K)_\#P\) has a different observation marginal, or a
pair \(Q\ll P_o\) for which
\(D(QK\Vert P_oK)>D(Q\Vert P_o)\). Either would falsify the repair. Neither can
occur under the stated hypotheses.

### 2. The general covariance hardwires a diagonal action instead of independent belief and model gauge systems

**Location:** `manuscripts/gauge_vfe_rg/04_generative.tex:298-337`;
`manuscripts/gauge_vfe_rg/05a_expfamily.tex:38-49`;
`manuscripts/gauge_vfe_rg/05_elbo.tex:207-217`

**Severity:** high

**Claim status:** `EVIDENCE_VERIFIED` as a source/type mismatch; the current
one-group theorem remains valid as a specialization.

**Evidence:** `04_generative.tex:306-313` chooses one \(g_i\in G\), sends it
through two representations, and states:

> “The two matrices ... are images of the same group element under two
> representations; choosing them independently would declare a different
> geometric model.”

The general kernel action in `05a_expfamily.tex:43-47` likewise uses one \(g\)
simultaneously on source and target. Corollary 5.8 then proves ELBO invariance
only for the assembled single latent map \(g\).

The author's required general type has two independent principal gauge
systems. Their actions and smooth connections induce:

\[
U_i^b:\mathcal E_i^b\to\mathcal E_i^b,\qquad
U_i^m:\mathcal E_i^m\to\mathcal E_i^m
\]

as independent associated-bundle gauge automorphisms, and

\[
\Omega_{ij}:\mathcal E_j^b\to\mathcal E_i^b,\qquad
\widetilde\Omega_{ij}:\mathcal E_j^m\to\mathcal E_i^m
\]

as parallel transports along a base curve. By contrast, the reserved symbols

\[
\Phi_i:\mathcal E_i^b\to\mathcal E_i^m,\qquad
\widetilde\Phi_i:\mathcal E_i^m\to\mathcal E_i^b
\]

are morphisms of the associated bundles covering
\(\mathrm{id}_{\mathcal C}\), not principal-bundle morphisms and not
same-channel frame changes.

**Derivation:** Under the independent product gauge change
\((U^b,U^m)\), the typed covariance laws are
\[
\begin{aligned}
\Omega'_{ij}
  &=U_i^b\Omega_{ij}(U_j^b)^{-1},&
\widetilde\Omega'_{ij}
  &=U_i^m\widetilde\Omega_{ij}(U_j^m)^{-1},\\
\Phi_i'
  &=U_i^m\Phi_i(U_i^b)^{-1},&
\widetilde\Phi_i'
  &=U_i^b\widetilde\Phi_i(U_i^m)^{-1}.
\end{aligned}
\]
A parallel cross morphism obeys the associated-bundle intertwining identities
\[
\widetilde\Omega_{ij}\Phi_j=\Phi_i\Omega_{ij},
\qquad
\Omega_{ij}\widetilde\Phi_j
=\widetilde\Phi_i\widetilde\Omega_{ij}.
\]
If parallelness is not imposed, the two differences are covariant defects;
smoothly, for example,
\(D\Phi=\nabla^m\!\circ\Phi-\Phi\circ\nabla^b\).

For a cross-fiber generative kernel \(K_i^{b\leftarrow m}\), product
covariance is the measure-level condition
\[
K_i^{b\leftarrow m\,\prime}
  \bigl(\,\cdot\mid U_i^m m\bigr)
=(U_i^b)_\#
K_i^{b\leftarrow m}(\,\cdot\mid m).
\]
If the kernel also reads belief or model parents, every argument is transformed
by its corresponding \(U_j^b\) or \(U_j^m\). In a linear-Gaussian factor
\[
b_i\mid m_i\sim
\mathcal N(B_im_i+\eta_i,\Sigma_i),
\]
where \(B_i\) is a section of
\(\operatorname{Hom}(\mathcal E_i^m,\mathcal E_i^b)\) (and may instantiate
\(\widetilde\Phi_i\) when that is the intended cross morphism), covariance is
\[
B_i'=U_i^bB_i(U_i^m)^{-1},\qquad
\eta_i'=U_i^b\eta_i,\qquad
\Sigma_i'=U_i^b\Sigma_i(U_i^b)^\top.
\]
Observation loadings out of both fibers obey
\[
H_i^{b\prime}=H_i^b(U_i^b)^{-1},\qquad
H_i^{m\prime}=H_i^m(U_i^m)^{-1}.
\]
These relations make every factor, and hence the joint, transform by
\[
P'=(\mathrm{id}_{O}\times T_{U^b,U^m})_\#P,
\qquad
T_{U^b,U^m}=\bigoplus_{a,i}(U_i^b\oplus U_i^m).
\]
Transport the recognition law by the same map,
\(Q'=T_{U^b,U^m\#}Q\). The observation marginal is unchanged, the posterior
obeys \(P'_o=T_{U^b,U^m\#}P_o\), and invariance of KL under a common
bimeasurable bijection gives
\[
D(Q'\Vert P'_o)=D(Q\Vert P_o),\qquad
\mathcal L'(Q';o)=\mathcal L(Q;o).
\]
Thus there is still one exact ELBO, not one per channel. For an optimized
restricted ELBO, the recognition family must also be carried into its
product-action image; invariance of one law does not imply invariance of a
coordinate-defined restricted family.

The current construction is recovered by the optional diagonal
specialization
\[
U_i^b=\rho_b(g_i),\qquad U_i^m=\rho_m(g_i)
\]
for one \(g_i\). That belongs in the later MVG realization.

**Minimal rigorous repair:** State the product-action kernel and ELBO theorem
in the general part; type \(\Phi,\widetilde\Phi\) as cross morphisms of the
associated bundles, \(\Omega,\widetilde\Omega\) as connection-induced
same-channel transports, and the parallel/intertwining condition or its
covariant defect; then relabel the current same-element construction as the
diagonal MVG specialization.

**Falsification condition:** Exhibit an existing theorem in the scoped files
that permits arbitrary independent \((U^b,U^m)\), types the cross morphisms
and transports as above, transforms every generative factor, and proves the
joint, posterior, recognition, and ELBO pushforward identities. No such
theorem is present. Mathematically, a counterexample to the displayed
common-pushforward KL identity under bimeasurable \(U^b,U^m\) would falsify
the proposed repair.

### 3. Excluding the posterior does not imply a positive optimized gap

**Location:** `manuscripts/gauge_vfe_rg/05_elbo.tex:195-205`;
contrast `manuscripts/gauge_vfe_rg/07_restrictions.tex:18-35`

**Severity:** medium

**Claim status:** `REFUTED` by an exact Gaussian counterexample.

**Evidence:** After correctly proving pointwise equality only at the posterior,
`05_elbo.tex:205` says:

> “over a family that does not [contain the posterior], a positive gap
> remains”

and then immediately says that no minimizer over a restricted family is
asserted. Proposition 8.1 later correctly uses an infimum and explicitly says
it need not be attained. Those two statements are inconsistent if “gap
remains” means the optimized gap.

**Counterexample and symbolic check:** Let
\[
P^\star=\mathcal N(0,1),\qquad
\mathcal Q=\{\mathcal N(\mu,1):\mu>0\}.
\]
Every member is mutually absolutely continuous with \(P^\star\), satisfies the
Gaussian log-integrability hypotheses, and differs from \(P^\star\). Yet
\[
D\!\left(\mathcal N(\mu,1)\Vert\mathcal N(0,1)\right)
=\frac{\mu^2}{2},
\qquad
\inf_{\mu>0}D=0,
\]
with no minimizer. The optimized ELBO supremum equals the evidence although no
member attains it.

The exact SymPy check returned:

```text
gaussian_gap= mu**2/2
d_gap_d_mu= mu
inf_boundary_limit= 0
```

This is the standard distinction between a variational family containing the
posterior and having the posterior only in its KL closure. The fixed-model
identity itself is unaffected.

**Minimal rigorous repair:** Replace the sentence by: “every member distinct
from the posterior has a positive pointwise gap; the optimized infimum is
strictly positive only under a KL-separation condition, and it may be zero
without attainment.”

**Falsification condition:** Prove that every posterior-excluding recognition
family satisfying H1--H4 is separated from the posterior by a positive KL
radius. The displayed open-half-line Gaussian family disproves that statement.

### 4. The finite-stage RG recursion has no declared variational lift

**Location:** `manuscripts/gauge_vfe_rg/10_renormalization.tex:54-93`,
especially `:72-83`; status consequence at `:670,687`

**Severity:** medium

**Claim status:** `EVIDENCE_VERIFIED` that the lift is absent;
`INCONCLUSIVE` whether a suitable lift exists.

**Evidence:** The chapter correctly says that the flowed Gaussian object is
only
\[
\pi=((A_i),(W_{ij})).
\]
At `10_renormalization.tex:83` it states:

> “The information vector \(h\) is another natural coordinate ... it is not
> part of the RG state declared in this chapter and no rescaling law for it is
> claimed. ... [This] prevents the operator flow from being read as a flow of
> complete Gaussian laws without a further declaration.”

Lines 85--93 add that each scale needs a coarse reference measure and finite
normalizer, and that the source and target generally have different
dimensions. The status table at line 687 separately asks for “compatible
bases, measures, normalizers and bounds across scales.”

This is not R1. R1 concerned the singular limiting ray. The present gap exists
at every finite interior stage: a precision-sector map is not yet a
generative-joint map, does not specify an observation kernel, does not specify
the flow of \(h\), and does not specify a recognition channel. Therefore no
finite-stage comparison in the declared RG recursion is currently licensed by
one fixed evidence.

**Derivation:** To obtain an ELBO chain one must provide, at each level,
\[
P_{\ell+1}
=(\mathrm{id}_{O}\otimes K_\ell)_\#P_\ell,
\qquad
Q_{\ell+1}=Q_\ell K_\ell,
\]
with normalized \(K_\ell\), a common observation marginal, posterior
disintegration, absolute continuity, and either the separated H4 conditions
or the extended relative-log definition. The existing energy precomposition
\(\Lambda\mapsto\zeta_\ell^{-1}S_\ell^\top\Lambda S_\ell\) does not supply
such a \(K_\ell\). It defines a new coarse energy after choosing a reference
measure and normalizer. Equality with a law pushforward is an additional
theorem, not a consequence of congruence.

**Minimal rigorous repair:** Keep all current operator results, but add a boxed
statement that they imply no cross-scale ELBO until a complete
observation-preserving Markov lift is constructed; if such a lift is intended,
declare \(h_\ell\), the observation kernels, \(K_\ell\), \(Q_\ell\), reference
measures, and regularity hypotheses.

**Falsification condition:** Supply a complete sequence
\((P_\ell,Q_\ell,K_\ell)\) satisfying the displayed pushforward equations and
show that its induced full natural-parameter recursion is exactly the declared
rescaled operator recursion, including \(h_\ell\) and the observation model.

## The general Markov-coarse ELBO theorem

The following theorem is safe for the general part. It states precisely when a
cross-inventory comparison is licensed by one fixed evidence.

### Theorem (fixed-evidence Markov coarse map)

Let \((\mathsf X,\mathscr X)\) and \((\mathsf Z,\mathscr Z)\) be standard
Borel spaces. Fix one normalized joint \(P(do,dx)\) on
\(\mathsf O\times\mathsf X\), a regular observation \(o\) with
\(0<p(o)<\infty\), posterior \(P_o\), and recognition law \(Q_o\).
Let \(K:\mathsf X\rightsquigarrow\mathsf Z\) be a normalized Markov kernel
that does not read \(Q_o\). Define
\[
\bar P(do,dz)=\int K(x,dz)P(do,dx),\qquad
\bar Q_o=Q_oK.
\]
Then:

1. \(\bar P^O=P^O\), so \(\bar p(o)=p(o)\), and
   \(\bar P_o=P_oK\) for \(P^O\)-almost every \(o\).
2. \(Q_o\ll P_o\) implies \(Q_oK\ll P_oK\).
3. In the extended nonnegative reals,
   \[
   D(Q_oK\Vert P_oK)\leq D(Q_o\Vert P_o).
   \]
4. Defining the extended ELBO by
   \[
   \mathcal L^{\rm ext}(Q_o;o)
   :=\log p(o)-D(Q_o\Vert P_o),
   \]
   gives
   \[
   \bar{\mathcal L}^{\rm ext}(\bar Q_o;o)
   \geq \mathcal L^{\rm ext}(Q_o;o).
   \]
   If H4 holds at both scales, these are the separately integrated ELBOs of
   Chapter 5. H4 at the fine scale alone does not imply H4 after
   coarse-graining; `09_coarsegraining.tex:71-81` gives a correct witness.
5. If \(D(Q_o\Vert P_o)<\infty\), put
   \(r=dQ_o/dP_o\) and let
   \[
   \mathbb P_o(dx,dz)=P_o(dx)K(x,dz),\qquad
   \bar r(z)=\mathbb E_{\mathbb P_o}[r(X)\mid Z=z].
   \]
   Then \(d(Q_oK)/d(P_oK)=\bar r\), and equality in data processing holds
   exactly when
   \[
   r(X)=\bar r(Z)\qquad \mathbb P_o\text{-almost surely}.
   \]
6. Let \(R_{P_o}(z,dx)\) be a regular conditional law of \(X\) given \(Z=z\)
   under \(\mathbb P_o\). Then \(P_oKR_{P_o}=P_o\); under the equality
   condition also \(Q_oKR_{P_o}=Q_o\). Conversely, any one kernel \(R\) that
   recovers both \(P_o\) and \(Q_o\) forces equality by applying data
   processing through \(K\) and then \(R\).

**Proof:** The observation-marginal statement is normalization of \(K\).
Absolute continuity follows because \(P_oK(B)=0\) implies
\(K(x,B)=0\) for \(P_o\)-almost every \(x\), hence also for
\(Q_o\)-almost every \(x\). For bounded measurable \(f\),
\[
\int f(z)(Q_oK)(dz)
=\mathbb E_{\mathbb P_o}[f(Z)r(X)]
=\mathbb E_{\mathbb P_o}[f(Z)\bar r(Z)],
\]
which proves the Radon--Nikodym formula. Conditional Jensen for the strictly
convex \(\phi(t)=t\log t\) gives
\[
\mathbb E[\phi(\bar r(Z))]
\leq \mathbb E[\phi(r(X))].
\]
Finite divergence and strictness give the equality condition. For recovery,
\[
\begin{aligned}
(Q_oKR_{P_o})(A)
&=\int \bar r(z)R_{P_o}(z,A)(P_oK)(dz)\\
&=\iint \mathbf1_A(x)\bar r(z)\,\mathbb P_o(dx,dz)\\
&=\iint \mathbf1_A(x)r(x)\,\mathbb P_o(dx,dz)
=Q_o(A).
\end{aligned}
\]
The converse is the two-sided data-processing sandwich.

This is the Markov-kernel extension of the information/sufficiency relation
introduced by [Kullback and Leibler
(1951)](https://doi.org/10.1214/aoms/1177729694). Experiment-level
equivalence is the stronger [Blackwell
(1953)](https://doi.org/10.1214/aoms/1177729032) condition: one
parameter-independent recovery kernel must work for the whole family.

### What must remain fixed

For one fine/coarse ELBO comparison:

- the fine normalized joint \(P\), structural data, and selected observation;
- the observation marginal, preserved because the coarse joint is the
  pushforward of \(P\), not a separately normalized model;
- one recognition-independent normalized channel \(K\);
- the same channel applied to the posterior and recognition law; and
- the relevant absolute-continuity and integrability domains.

For a statistical experiment \(\{P_\theta\}_{\theta\in\Theta}\), \(K\) must be
parameter independent if it is to define one experiment morphism. Equality
for one pair \((Q_o,P_o)\) gives a pairwise recovery kernel. A sufficient
experiment requires one \(R\), independent of \(\theta\), with
\(P_{\theta,o}KR=P_{\theta,o}\) for every \(\theta\). Pair-specific recovery
kernels do not establish that statement.

Along a chain \(K_0,K_1,\ldots\) applied to one joint and one recognition law,
KL is nonincreasing and the fixed-evidence extended ELBO is nondecreasing.
This is not EM evidence monotonicity. The evidence is constant along the
channel chain; an exact E-step plus accepted M-step instead changes the model
parameter while ascending the same variational objective. [Dempster, Laird,
and Rubin (1977)](https://doi.org/10.1111/j.2517-6161.1977.tb01600.x)
is the primary EM source, and [Beal
(2003), Chapter 2](https://discovery.ucl.ac.uk/id/eprint/10101435/)
is the primary variational-Bayes treatment used here.

### Why energy precomposition is different

Given an injection \(\iota:\mathsf Z\to\mathsf X\), the operation
\[
\bar E(z)=E(\iota z),\qquad
\bar P(dz)\propto e^{-\bar E(z)}\bar\nu(dz)
\]
is not a channel \(K:\mathsf X\rightsquigarrow\mathsf Z\). It chooses a new
reference measure, samples a fine energy on an image that may be fine-measure
null, and introduces a new normalizer. No data-processing inequality or fixed
evidence follows. To compare its ELBO with the fine ELBO, one must prove a
separate identity
\[
\bar P=(\mathrm{id}_{O}\otimes K)_\#P
\]
for some normalized \(K\), or accept that the difference contains an
uncontrolled evidence difference. Parameter closure
\(S^\top\Lambda S\), by itself, proves neither.

## Product-action covariance theorem

Let principal gauge systems \(\mathcal P_b\) and \(\mathcal P_m\) induce
associated bundles \(\mathcal E_b\) and \(\mathcal E_m\), with independent
gauge changes inducing bimeasurable associated-bundle automorphisms \(U^b\)
and \(U^m\). Let their separate smooth connections induce the same-channel
parallel transports \(\Omega\) and \(\widetilde\Omega\). Let
\[
\Phi:\mathcal E_b\to\mathcal E_m,\qquad
\widetilde\Phi:\mathcal E_m\to\mathcal E_b
\]
be cross morphisms of the associated bundles covering
\(\mathrm{id}_{\mathcal C}\). They need not be parallel; when they are, they
intertwine the two induced transports, and otherwise their covariant defects
must transform tensorially under \((U^b,U^m)\).

Suppose:

1. transports and cross morphisms transform under the typed laws
   \[
   \begin{aligned}
   \Omega'_{ij}
     &=U_i^b\Omega_{ij}(U_j^b)^{-1},&
   \widetilde\Omega'_{ij}
     &=U_i^m\widetilde\Omega_{ij}(U_j^m)^{-1},\\
   \Phi_i'
     &=U_i^m\Phi_i(U_i^b)^{-1},&
   \widetilde\Phi_i'
     &=U_i^b\widetilde\Phi_i(U_i^m)^{-1};
   \end{aligned}
   \]
2. every cross-fiber generative kernel intertwines the product action, as in
   \[
   K_i^{b\leftarrow m\,\prime}
   (\cdot\mid U_i^m m)
   =(U_i^b)_\#K_i^{b\leftarrow m}(\cdot\mid m);
   \]
3. root laws and same-channel transition kernels obey the analogous
   pushforward identities;
4. the observation space is inert and its kernels satisfy
   \[
   L_i'(do\mid U_i^b b,U_i^m m)=L_i(do\mid b,m);
   \]
5. recognition transforms by the full product map,
   \(Q'=T_{U^b,U^m\#}Q\).

Then factorwise covariance and uniqueness of the iterated joint give
\[
P'=(\mathrm{id}_{O}\times T_{U^b,U^m})_\#P.
\]
Consequently \(P'^O=P^O\),
\(P'_o=T_{U^b,U^m\#}P_o\), and common-pushforward invariance of relative
entropy gives the exact product-action ELBO identity
\[
\begin{aligned}
\mathcal L'(Q';o)
&=\log p(o)-D\!\left(
T_{U^b,U^m\#}Q\,\middle\Vert\,
T_{U^b,U^m\#}P_o\right)\\
&=\log p(o)-D(Q\Vert P_o)
=\mathcal L(Q;o).
\end{aligned}
\]
This is one ELBO on the joint latent space. It does not require identifying
the two gauges. An optimized restricted ELBO is invariant only when its
recognition family is carried into the product-action image.

No cross-fiber morphism is needed merely to form the product latent space. A
cross morphism is required when a generative factor compares or predicts
between the two associated bundles. A fixed numerical cross map under
independent frame changes is generally not covariant: it must transform as a
section of \(\operatorname{Hom}(\mathcal E_b,\mathcal E_m)\) or
\(\operatorname{Hom}(\mathcal E_m,\mathcal E_b)\), as appropriate, or the
model must restrict the product action to its stabilizer. The shared action
\(U_i^b=\rho_b(g_i)\), \(U_i^m=\rho_m(g_i)\) is an optional diagonal MVG
specialization.

## Symbolic checks

The requested symbolic pass checked three algebraic seams:

```text
gaussian_gap= mu**2/2
d_gap_d_mu= mu
inf_boundary_limit= 0
em_d_elbo_d_theta= m - theta
em_entropy_derivative= 0
em_stationary_theta= [m]
kl_chain_rule_residual= 0
```

The first three lines close Finding 3. The next three verify the M-coordinate
separation used in Chapter 5 on a generic quadratic expected complete log
joint: with \(Q\) fixed, its entropy contributes zero derivative in the model
parameter, and stationarity is determined only by the expected complete log
joint. The final line expands a generic binary joint into marginal and
conditional probabilities and verifies exactly
\[
D(Q_{XZ}\Vert P_{XZ})
=D(Q_Z\Vert P_Z)
+\mathbb E_{Q_Z}D(Q_{X\mid Z}\Vert P_{X\mid Z}),
\]
the finite-space chain-rule form of the Markov equality/recovery analysis.

## Semantic consolidation and placement

The general semantic core is currently repeated in three locations:

- `05a_expfamily.tex:277-333` defines identification, a separate coarse
  normalizer, and energy/parameter closure;
- `09_coarsegraining.tex:96-206` restates the same law-versus-energy split and
  parameter map; and
- `10_renormalization.tex:54-100` states it a third time before specializing
  to the Gaussian operator recursion.

The fixed-model versus changing-model warning is likewise proved in
`07_restrictions.tex:263-342` and repeated with a stronger, false quantifier in
`09_coarsegraining.tex:792-821`. This is semantic repetition, not harmless
recapitulation: the copies have already drifted into the contradiction in
Finding 1.

The dependency-clean placement is:

1. **General Part I:** measurable fibers; one fixed normalized joint;
   recognition law; H1--H4; exact ELBO; restriction principle with infimum
   versus attainment; E/M separation; and the product-action covariance
   theorem.
2. **General Part II:** Markov coarse maps; fixed-evidence ELBO data
   processing; equality and recovery; experiment-level sufficiency; arbitrary
   model replacement; energy precomposition as a separately typed
   construction; and graph-exponential parameter closure.
3. **MVG realization:** linear-Gaussian kernels and bridges; covariance and
   precision charts; Gaussian restriction optima; determinant and Schur
   formulas; \(S^\top\Lambda S\); matrix-weighted transports; and the
   precision-sector RG recursion.

The later chapters should cite the general theorem and add only
family-specific hypotheses. The Gaussian example should not be the place
where independent product covariance is first defined.

## Theorem-grade open directions

1. **A law-level RG lift.** Construct normalized kernels \(K_\ell\) and full
   joints \(P_\ell\) for which
   \(P_{\ell+1}=(\mathrm{id}_{O}\otimes K_\ell)_\#P_\ell\), and prove that the
   induced full natural-parameter recursion, including \(h_\ell\) and the
   observation model, agrees with the intended rescaled operator flow.
   Success would give a genuine fixed-evidence ELBO monotone; failure would
   prove that the operator RG is model replacement rather than data
   processing.

2. **Gauge-equivariant recovery under a product action.** Characterize when
   the Bayes reverse kernel supplied by KL equality can be chosen equivariant
   under independent \((U^b,U^m)\), while respecting the associated-bundle
   cross morphisms \(\Phi,\widetilde\Phi\) and their covariant defects. The
   target theorem requires one parameter-independent and product-equivariant
   recovery kernel for the entire experiment, not pairwise almost-everywhere
   versions.

3. **Approximate sufficiency across scale.** Define a gauge-invariant Le Cam
   deficiency or uniform recovery error for the fine/coarse experiment and
   prove a composition bound along \(K_0K_1\cdots K_{\ell}\). This is the
   quantitative replacement when exact KL equality and recovery fail.

4. **Attainment and variational closure.** Give coercivity, tightness, or
   compactness conditions under which scale-dependent recognition families
   attain their reverse-KL projections, and characterize when a posterior lies
   only in their KL closure. A \(\Gamma\)-convergence or epi-convergence result
   could separate convergence of optimal values from convergence of
   optimizers as inventories change.

5. **When trace laws equal pushforwards.** Classify the energies, reference
   measures, and identification maps for which the normalized trace law from
   energy precomposition coincides with a Markov pushforward of the fine joint.
   Outside that class, cross-scale ELBO differences must be decomposed into an
   evidence/model-selection term and a recognition-tightness term.

## Concise physicist summary

A larger-scale latent space can be compared with a microscopic one if it is
obtained by passing the same joint distribution through a normalized noisy
channel. Then the experimental evidence is literally unchanged, KL
distinguishability can only decrease, and the coarse ELBO can only rise. It
rises because information was discarded, not because the model improved.
Equality means the discarded variables can be reconstructed for the laws in
question.

Restricting an energy to block-constant configurations is different. It is a
new model with a new measure and normalizer unless someone proves that it is a
pushforward of the old joint. The present RG is of this operator/energy type
and does not yet define an ELBO flow.

Independent belief and model frames do not split the variational principle
into two bounds. They enlarge the gauge action to a product action. Their
separate connections induce \(\Omega\) and \(\widetilde\Omega\);
\(\Phi:\mathcal E_b\to\mathcal E_m\) and
\(\widetilde\Phi:\mathcal E_m\to\mathcal E_b\) are cross morphisms of the
associated bundles, not frame changes or principal-bundle maps. If the joint
kernels, recognition law, cross morphisms, and any covariant defects transform
under the product action, the same single ELBO remains exactly invariant. The
current same-element construction is the diagonal Gaussian example of that
more general theorem.

## Primary sources used

- S. Kullback and R. A. Leibler, “On Information and Sufficiency,” *Annals of
  Mathematical Statistics* 22 (1951), 79--86,
  [doi:10.1214/aoms/1177729694](https://doi.org/10.1214/aoms/1177729694).
- D. Blackwell, “Equivalent Comparisons of Experiments,” *Annals of
  Mathematical Statistics* 24 (1953), 265--272,
  [doi:10.1214/aoms/1177729032](https://doi.org/10.1214/aoms/1177729032).
- A. P. Dempster, N. M. Laird, and D. B. Rubin, “Maximum Likelihood from
  Incomplete Data via the EM Algorithm,” *JRSS B* 39 (1977), 1--22,
  [doi:10.1111/j.2517-6161.1977.tb01600.x](https://doi.org/10.1111/j.2517-6161.1977.tb01600.x).
- M. J. Beal, *Variational Algorithms for Approximate Bayesian Inference*,
  PhD thesis, University College London (2003), Chapter 2,
  [UCL record](https://discovery.ucl.ac.uk/id/eprint/10101435/).
