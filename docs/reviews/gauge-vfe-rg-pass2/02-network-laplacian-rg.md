# Pass 2: network, graph-Laplacian, and renormalization-group review

## Scope and verdict

This memo reviews the network-RG claims in Chapters 9--11 against the executable mathematics of the manuscript and the primary papers, without reopening the remediated R1--R21 findings. It separates:

- **general network/RG statements**, which can and should precede the multivariate-Gaussian (MVG) realization; and
- **MVG/gauge specializations**, which depend on matrix-weighted Laplacians, positive-semidefinite weights, generalized matrix pencils, and local \(\mathrm{GL}(K)\) reframings and therefore belong after that realization.

I found **six findings: one high, four medium, and one low**. The strongest defect is a missing bridge, not a defect in Proposition 11.9 itself: generalized eigenvalues are gauge invariant, but the real-space heat-kernel entries used to form Villegas et al.'s blocks are not. A two-node exact counterexample changes the blocking decision under a legal frame congruence while leaving the generalized spectrum unchanged.

Primary sources checked:

- P. Villegas, T. Gili, G. Caldarelli, and A. Gabrielli, “Laplacian renormalization group for heterogeneous networks,” *Nature Physics* **19**, 445--450 (2023), [doi:10.1038/s41567-022-01866-8](https://doi.org/10.1038/s41567-022-01866-8), especially Eqs. (1)--(3), the real-space construction, and the subsequent \(k\)-space construction.
- E. Garuccio, M. Lalli, and D. Garlaschelli, “Multiscale network renormalization: Scale-invariance without geometry,” *Physical Review Research* **5**, 043101 (2023), [doi:10.1103/PhysRevResearch.5.043101](https://doi.org/10.1103/PhysRevResearch.5.043101), especially Eqs. (1)--(7), Appendix A, and Sec. IV.A.
- A. Catanzaro, D. Garlaschelli, and S. P. Patil, “Renormalization of interacting random graph models,” *Physical Review E* **113**, 024314 (2026), [doi:10.1103/34n8-pw8x](https://doi.org/10.1103/34n8-pw8x).
- A. Gabrielli, D. Garlaschelli, S. P. Patil, and M. Á. Serrano, “Network renormalization,” *Nature Reviews Physics* **7**, 203--219 (2025), [doi:10.1038/s42254-025-00817-5](https://doi.org/10.1038/s42254-025-00817-5).

## Findings

### 1. The generalized-spectrum repair does not make the imported LRG blocking rule gauge invariant

**Location:** `manuscripts/gauge_vfe_rg/10_renormalization.tex:629-633`
**Severity:** high
**Layer:** MVG/gauge specialization, not general network RG
**Literal manuscript status and plain-English category:** The claim at line 629 has no status macro. Line 633 invokes Proposition 11.9, whose literal status is `ESTABLISHED`, but that proposition establishes invariance only of the roots of a regular pencil. The proposed passage from that invariant spectrum to a node partition is unsupported.
**Inflation verdict:** yes. Calling the diffusion-equivalence rule a “principled replacement” in this gauge-carrying setting goes beyond the established pencil theorem.

**Evidence:** Villegas et al. define the scalar density matrix
\[
\rho(\tau)=\frac{e^{-\tau L}}{\operatorname{Tr}e^{-\tau L}}
\]
and their real-space metagraph by thresholding
\[
\frac{\rho_{ij}(\tau)}{\min(\rho_{ii}(\tau),\rho_{jj}(\tau))}\geq 1.
\]
Those are entries in a distinguished node basis. Proposition 11.9 instead covers a pair of bilinear forms under
\[
(L,R)\longmapsto (G^\top L G,G^\top R G).
\]
Congruence does not commute with the ordinary matrix exponential. In general,
\[
e^{-\tau G^\top L G}\neq G^{-1}e^{-\tau L}G,
\]
so neither the Euclidean heat-kernel spectrum nor its entries define a local-\(\mathrm{GL}(K)\) invariant block rule.

The failure already occurs for \(K=1\) and two nodes. Set
\[
L=\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad
R=I,\qquad
G=\operatorname{diag}(2,1),
\]
and \(L'=G^\top LG,\ R'=G^\top RG\). A SciPy probe at \(\tau=1\) returned:

```text
eig(L)= [0. 2.]
eig(Lg)= [0. 5.]
gen_eig(L,R)= [0. 2.]
gen_eig(Lg,Rg)= [0. 2.]
original rho= [[0.5         0.380797078]
 [0.380797078 0.5        ]] threshold= 0.761594156 S= 0.527065341 C= 0.605894900
congruent rho= [[0.204015711 0.394645719]
 [0.394645719 0.795984289]] threshold= 1.934388867 S= 0.057966914 C= 0.239777960
```

The generalized spectrum is unchanged, exactly as Proposition 11.9 says, but the Villegas threshold changes from “do not join” to “join.” The ordinary entropy and susceptibility also change. This is a direct counterexample to treating the scalar density-matrix blocker as a gauge-admissible consequence of generalized spectral invariance.

There is a viable starting point, but it is not yet in the manuscript. If \(R\succ0\), define the \(R\)-self-adjoint generator
\[
\mathcal A=R^{-1}L.
\]
Then
\[
\mathcal A'=(G^\top RG)^{-1}(G^\top LG)=G^{-1}\mathcal A G,
\qquad
e^{-\tau\mathcal A'}=G^{-1}e^{-\tau\mathcal A}G,
\]
so the heat trace and entropy of its generalized eigenvalues are frame invariant. Its off-diagonal blocks still transform as \(K_{ij}\mapsto g_i^{-1}K_{ij}g_j\), however, and are not scalar node affinities. A second construction is required to turn those blocks into an equivariant partition.

The scalar source also assumes a connected graph to obtain its one-dimensional equilibrium kernel. In the manuscript's flat connected matrix-weighted case the Laplacian kernel is generally \(K\)-dimensional; rank-deficient weights add modes, and nontrivial connection holonomy can change the parallel-section space. A gauge-LRG definition therefore also owes a declared reference form, treatment of the zero-mode atom, and an entropy normalization based on the actual state-space dimension.

**Falsification condition:** Supply a density operator and a scalar block affinity whose induced partition is unchanged under every allowed block-diagonal \(G\), and show on the displayed pair that both frames produce the same decision; alternatively restrict the gauge group to a declared orthogonal subgroup and prove the restriction is part of the model rather than a convenient gauge choice.

**Fix:** Replace the claimed gauge-setting blocker with an open bridge, define the generalized heat generator \(R^{-1}L\), and defer any MVG block selector until a local-\(\mathrm{GL}(K)\)-invariant scalarization and kernel treatment are proved.

### 2. “Principled replacement” reverses the primary paper's classification of its real-space blocker

**Location:** `manuscripts/gauge_vfe_rg/10_renormalization.tex:629`
**Severity:** medium
**Layer:** general scalar network RG and source fidelity
**Literal manuscript status and plain-English category:** no status macro; this is a source-backed interpretive claim.
**Inflation verdict:** yes.

**Evidence:** Villegas et al. explicitly distinguish two constructions.

1. Their introduction calls the real-space version heuristic.
2. The threshold \(\rho_{ij}/\min(\rho_{ii},\rho_{jj})\geq1\) is chosen “for the sake of simplicity.”
3. At the start of the \(k\)-space section they state that the preceding assumptions lack justification and describe the real-space definition as a practical approximation.
4. The more rigorous \(k\)-space construction removes modes with \(\lambda\geq1/\tau^\ast\), chooses exactly \(N-n\) clusters by ordering heat-kernel affinities, constructs a reduced weighted Laplacian, and rescales time. Even there, the assignment of nodes to clusters is an algorithmic choice; the paper does not prove uniqueness, scheme independence, or optimality of the real-space threshold.

The manuscript correctly treats peak existence as inconclusive at line 631, but that epistemic caution is inconsistent with calling the associated blocking rule “principled” two lines earlier. Scale selection from the heat trace and real-space node assignment are separate claims with different support.

**Falsification condition:** Identify a theorem in the primary paper proving that the threshold rule is uniquely induced by the \(k\)-space integration, or proving an invariant optimality/equivalence property for it across admissible coarse-grainings.

**Fix:** Describe the entropy/susceptibility construction as a principled scalar scale diagnostic and the real-space threshold as the authors' heuristic blocker or practical approximation, with scheme independence left open.

### 3. The susceptibility is missing its minus sign and its normalization convention

**Location:** `manuscripts/gauge_vfe_rg/10_renormalization.tex:629`
**Severity:** medium
**Layer:** general spectral network RG
**Literal manuscript status and plain-English category:** no status macro; definitional/source-backed.
**Inflation verdict:** not an inflation issue; it is a sign and typing error in the operative definition.

**Evidence:** The manuscript calls “the derivative” of entropy with respect to \(\log\tau\) the entropic susceptibility. The primary paper defines the positive quantity
\[
C(\tau)=-\frac{dS}{d\log\tau}.
\]
The sign is forced by the canonical calculation. For eigenvalues \(\lambda_a\), probabilities \(p_a=e^{-\tau\lambda_a}/Z\), and ordinary von Neumann entropy \(S_{\rm vN}=-\sum_a p_a\log p_a\),
\[
S_{\rm vN}=\log Z+\tau\langle\lambda\rangle_\tau,
\qquad
\frac{dS_{\rm vN}}{d\log\tau}
=-\tau^2\operatorname{Var}_\tau(\lambda)\leq0,
\]
and hence
\[
C_{\rm vN}(\tau)=\tau^2\operatorname{Var}_\tau(\lambda)\geq0.
\]
If the entropy is normalized as in Villegas et al.,
\[
S=S_{\rm vN}/\log D,
\]
where \(D=N\) for their scalar graph and would be \(D=NK\) for an \(N\)-node, \(K\)-fiber realization, then
\[
C=C_{\rm vN}/\log D.
\]
This normalization does not move finite-\(D\) peaks, but it changes plateau amplitudes and any claimed relation to spectral dimension. In the two-node probe above, the normalized derivative is \(-0.605894900\), while the positive susceptibility is \(+0.605894900\).

Zero modes must also be typed. If their multiplicity is \(m_0>1\), \(S_{\rm vN}(\tau)\to\log m_0\) rather than zero as \(\tau\to\infty\). The derivative still tends to zero, but the entropy range and finite-size normalization differ from the connected scalar source.

**Falsification condition:** Declare a signed susceptibility convention in which negative extrema, rather than positive peaks, select scales, and show that it is the convention used by all downstream numerical claims; or show that the cited paper defines \(+dS/d\log\tau\).

**Fix:** Write \(C(\tau)=-dS/d\log\tau=\tau^2\operatorname{Var}_\rho(L)\) and state whether \(S\) is normalized by \(\log D\), including how the zero-mode atom is handled.

### 4. Infinite divisibility gives stochastic refinement, not a two-sided inverse of aggregation

**Location:** `manuscripts/gauge_vfe_rg/10_renormalization.tex:643` and `manuscripts/gauge_vfe_rg/10_renormalization.tex:721`
**Severity:** medium
**Layer:** general RG principle, followed by an MVG/\(\mathrm{PSD}^K\) specialization
**Literal manuscript status and plain-English category:** `OPEN`; conjectural/open.
**Inflation verdict:** yes. The phrase “makes the network flow invertible” and the listed settlement condition identify a stochastic section with a two-sided inverse.

**Evidence:** Let the simplest additive coarse map be
\[
Q(x_1,x_2)=x_1+x_2.
\]
It is not injective: \(Q(1,2)=Q(2,1)=3\). Therefore no deterministic \(F\) can satisfy both \(Q\circ F=\mathrm{id}\) and \(F\circ Q=\mathrm{id}\). The OR map on fine edges is even more many-to-one.

Infinite divisibility supplies convolution roots. Equivalently, it can supply a refinement kernel \(K(c,d\mathbf x)\) such that
\[
Q_\#K(c,\cdot)=\delta_c,
\]
so coarsening a sampled refinement returns the coarse value. It cannot also satisfy
\[
K(Q(\mathbf x),\cdot)=\delta_{\mathbf x}
\]
for both \(\mathbf x=(1,2)\) and \((2,1)\). A conditional split redraws a compatible microstate; it does not recover the discarded one. Thus it is a stochastic right inverse or refinement in distribution, not a group inverse on realized states.

Garuccio et al. call the annealed construction a group because stable fitness laws are infinitely divisible and allow indefinite top-down sampling. Their Sec. IV.A supports scale-consistent refinement of the ensemble family. It does not undo a realized OR aggregation or reconstruct a discarded fine graph. The manuscript is already cautious in labeling its own matrix extension open, but its proposed closure test—an infinitely divisible family on \(\mathrm{PSD}^K\) plus family preservation—would establish only distributional refinability. It is insufficient to establish a two-sided flow.

The distinction is reinforced by Catanzaro, Garlaschelli, and Patil (2026): even in their exactly closed maximum-coordination-two interacting model, inversion is described as local and partial under known-parameter assumptions; higher coordination generates additional interactions and leaves inverse level sets requiring priors.

**Falsification condition:** Exhibit an explicitly declared state space and coarse map on which aggregation is injective, or construct forward and reverse Markov kernels satisfying both identity compositions on the claimed object rather than merely matching one family of marginals.

**Fix:** Rename the target “scale-consistent stochastic refinement in distribution,” or add the two kernel identities to the open problem and prove a no-go on realized populations before seeking \(\mathrm{PSD}^K\) convolution roots.

### 5. Positivity already removes the Cauchy pathologies, while the Garuccio proof gap is elsewhere

**Location:** `manuscripts/gauge_vfe_rg/09_coarsegraining.tex:678`, `manuscripts/gauge_vfe_rg/09_coarsegraining.tex:692-704`, and `manuscripts/gauge_vfe_rg/09_coarsegraining.tex:929-930`
**Severity:** medium
**Layer:** general network RG, the matrix-valued bi-additive analogue, and source fidelity
**Literal manuscript status and plain-English category:** The bi-additive proposition and source reading are `ESTABLISHED`; the register says measurability is load-bearing and that Hamel-basis counterexamples otherwise survive.
**Inflation verdict:** yes. Measurability is sufficient for the displayed theorem over arbitrary symmetric-matrix-valued maps, but it is not load-bearing in the declared model, where every \(w(x,y)\) and \(\alpha(x)\) is positive semidefinite.

**Evidence:** Fix \(y>0\) and set \(F_y(x)=w(x,y)\). Bi-additivity gives
\[
F_y(x_1+x_2)=F_y(x_1)+F_y(x_2).
\]
Because admissible edge weights satisfy \(F_y(x)\succeq0\), for \(x_2>x_1\),
\[
F_y(x_2)-F_y(x_1)=F_y(x_2-x_1)\succeq0.
\]
Thus \(F_y\) is Loewner-monotone. For every \(v\), the scalar function \(v^\top F_y(x)v\) is nonnegative, additive, and therefore monotone on \(\mathbb R_+\); a monotone additive function is linear. Hence \(F_y(x)=xF_y(1)\) without measurability. Repeating in \(y\) gives
\[
w(x,y)=xyM,\qquad M=w(1,1)\succeq0.
\]
The same argument gives \(\alpha(x)=xA\) with \(A\succeq0\). A non-linear Hamel additive function cannot remain nonnegative on all of \(\mathbb R_+\), so it cannot define admissible PSD weights. The manuscript's Hamel warning becomes relevant only after dropping the cone-valued hypothesis.

The source-fidelity issue is related but distinct. Appendix A of Garuccio et al. does prove the product over fine dyads. For two distinct coarse blocks, edge independence gives
\[
1-p_{IJ}
=\prod_{i\in I}\prod_{j\in J}(1-p_{ij}),
\]
their Eq. (A1); taking logarithms gives the double-additive Eq. (A2). Those steps are explained directly from independent Bernoulli edges.

The unproved rigidity step comes next. The paper states that the only form compatible with Eq. (A2) is
\[
\log(1-p_{IJ})=-\delta\,g(x_I)g(x_J),
\]
their Eq. (A3), with additive positive \(g\), and then reparameterizes to \(g(x)=x\). This is where separable rank-one dependence on the two node factors is asserted rather than derived. Once that form and positivity are granted, positivity itself supplies the regularity needed to make additive \(g\) linear.

The wording “the step that separates the block product into a product over dyads” points to Eq. (A1), which is proved. The register's shorter wording, “separability asserted,” is closer to the primary record; “no regularity condition stated” is not the right residual concern because the positive range already rules out Hamel pathologies.

**Falsification condition:** Exhibit a non-linear additive \(F:\mathbb R_+\to\mathrm{PSD}^K\), or show that admissibility in the proposition permits indefinite \(w(x,y)\) and \(\alpha(x)\) for some positive arguments; separately, identify a derivation of Eq. (A3) from Eq. (A2) in the primary source.

**Fix:** Remove the claim that measurability is load-bearing under PSD admissibility, prove product form by cone monotonicity, and say that the source proves the dyadic survival-product identity but asserts the rank-one separable ansatz for the resulting bi-additive log-survival kernel.

### 6. The 2026 interacting-random-graph RG result is missing, but it does not overturn the Garuccio uniqueness claim

**Location:** `manuscripts/gauge_vfe_rg/09_coarsegraining.tex:676-678` and `manuscripts/gauge_vfe_rg/10_renormalization.tex:635-637`
**Severity:** low
**Layer:** general network RG and literature scope
**Literal manuscript status and plain-English category:** line 678 is `ESTABLISHED` as a source reading; line 637 has no status macro.
**Inflation verdict:** no inflation in the scoped Garuccio uniqueness claim; the surrounding literature picture is incomplete as of 2026.

**Evidence:** The exact update is:

> Alessio Catanzaro, Diego Garlaschelli, and Subodh P. Patil, “Renormalization of interacting random graph models,” *Physical Review E* **113**, 024314 (2026), doi:10.1103/34n8-pw8x.

The paper introduces nonfactorizing graph Hamiltonians in which link probabilities are conditioned on other links. For pairwise interactions whose line graph has maximum coordination number two, it derives a closed-form decimation RG by mapping to a one-dimensional disordered spin chain. Adding coordination-three interactions destroys that closed operator form under repeated decimation and drives the effective Hamiltonian toward heterogeneous all-to-all couplings; general higher coordination requires approximation or enlarged theory space. It also derives flows of disorder distributions and identifies their continuum description with time-reversed anisotropic drift diffusion on the statistical manifold.

This result does **not** refute Garuccio et al.'s uniqueness theorem:

- Garuccio et al. assume independent links, arbitrary **node partitions**, and the “at least one link”/OR coarse map.
- Catanzaro et al. study dependent links and decimate **edge variables on the line graph**.
- Catanzaro et al.'s exact closure is limited to maximum coordination two; it is not a competing uniqueness theorem under every node partition.

It does change what the manuscript should say around the independent-edge result: interacting random-graph RG is no longer merely an unaddressed outside class. It is an adjacent, differently typed construction with a sharply limited exact-closure theorem.

**Falsification condition:** Show that the 2026 paper uses the same independent-dyad law, arbitrary node-partition OR map, and additive-fitness functional equation as Garuccio et al.; or show that its result supplies a counterexample within that exact class.

**Fix:** Add the 2026 paper after the Garuccio comparison and state explicitly that it broadens the network-RG landscape without changing the independent-edge uniqueness theorem.

## Architectural split required by the new ordering

The requested ordering—abstract/general theory and RG before the MVG realization—works for this material only if the network discussion is split at its actual dependency seam:

| Material that is genuinely general and can precede MVG | Material that is an MVG/gauge specialization and must follow MVG |
|---|---|
| Coarse-graining as a many-to-one map; semigroup versus inverse; blocking-scheme dependence; invariance versus attraction; universality as a basin statement | \(\Lambda=\operatorname{blkdiag}(A_i)+L\), \(S^\top\Lambda S\), matrix-weighted cut sums, and the PSD matrix cone |
| Scalar LRG definitions \(e^{-\tau L}/Z\), \(C=-dS/d\log\tau\), heat-trace scale diagnostics, and the source's heuristic-versus-\(k\)-space distinction | Regular generalized pencils \((L,\Lambda)\) or \((L,R)\), mass pencils, local-\(\mathrm{GL}(K)\) congruence, and the gauge heat operator \(R^{-1}L\) |
| Garuccio's independent-edge OR theorem, its assumptions, scale-free versus scale-invariant, and Catanzaro et al.'s interacting edge-Hamiltonian RG | Matrix-valued bi-additive fixed rays, \(\mathrm{PSD}^K\) infinite divisibility, connection holonomy, matrix-kernel multiplicity, and a gauge-invariant block selector |
| General obligations for nested partitions, scheme independence, thermodynamic limits, and two-sided versus stochastic refinement | Claims that positive self terms regularize a particular Gaussian pencil or that a measured MVG operator supplies an admissible spectral diagnostic |

In particular, the current line 633 cannot remain in the pre-Gaussian general RG chapter as written: Proposition 11.9, positive self terms, \(\Lambda\), and the matrix pencil are all MVG realization objects. The general chapter can state the abstract obligation—an RG observable must descend to the declared quotient/symmetry class. The later MVG chapter can instantiate that obligation with common-congruence pencils and then confront Finding 1's missing block rule.

## Theorem-level open directions

### A. General spectral-dimension/heat-capacity theorem

**Target theorem:** For a declared thermodynamic sequence of positive self-adjoint generators with normalized counting measures \(N_n\to N\), prove under Tauberian hypotheses that
\[
N(\lambda)-N(0)\sim C\lambda^\alpha
\quad\Longleftrightarrow\quad
\int e^{-\tau\lambda}\,dN(\lambda)-N(0)
\sim C\Gamma(\alpha+1)\tau^{-\alpha},
\]
and derive the corresponding plateau of \(\tau^2\operatorname{Var}_\tau(\lambda)\).

**Proof obligations:** specify convergence mode and uniformity; remove or retain the zero-mode atom explicitly; state whether entropy is divided by \(\log D_n\); prove the Tauberian converse rather than infer it from a fitted log-log line; show which rescaling of \(\tau\) makes the exponent flow invariant. This belongs in general RG before MVG.

### B. Gauge-covariant heat-kernel and block-selector theorem

**Target theorem:** Given \(L\succeq0\), \(R\succ0\), and local congruence covariance, construct a diffusion from \(\mathcal A=R^{-1}L\) and a permutation-equivariant scalar affinity \(a_{ij}(\tau)\) whose induced partition is invariant under every block-diagonal \(G\).

**Proof obligations:** prove similarity covariance of the heat operator; prove positivity/self-adjointness in the \(R\)-inner product; classify the zero-mode space; construct a block scalar (for example, from invariant closed products such as \(K_{ij}K_{ji}\), not raw entries); prove that thresholding followed by connected components is gauge invariant; test the exact two-node counterexample above. This belongs after MVG.

### C. Nested-blocking and scheme-independence theorem

**Target theorem:** Characterize heat-kernel block rules for which partitions are nested in \(\tau\) and repeated blocking defines a semigroup independent, up to a declared equivalence, of admissible tie-breaking and threshold choices.

**Proof obligations:** show monotonicity or supply a counterexample; handle eigenvalue crossings and degenerate eigenspaces; prove that the number and identity of blocks do not depend on basis choices inside eigenspaces; compare the heuristic real-space threshold with the \(N-n\)-cluster \(k\)-space algorithm; state the topology in which two schemes have the same limit. The abstract obligations are general; the matrix-valued test is an MVG specialization.

### D. Refinement-versus-inverse theorem on additive cones

**Target theorem:** First prove a no-go: a noninjective sum/OR aggregation admits no two-sided deterministic or Markov inverse on realized populations. Then classify convolution semigroups on \(\mathrm{PSD}^K\) that yield scale-consistent stochastic refinement.

**Proof obligations:** declare whether the object is a state, parameter tuple, or law; distinguish \(Q_\#K=\mathrm{id}\) from \(KQ=\mathrm{id}\); characterize matrix subordinators/Lévy measures whose increments remain PSD; include edge/topology data rather than only node weights; prove compatibility with the declared family and with gauge congruence. The no-go is general; the cone classification follows MVG.

### E. Interacting graph-to-bundle closure theorem

**Target theorem:** Place independent-node aggregation and interacting-edge decimation in one typed diagram, then determine which graph-exponential Hamiltonians with matrix-valued/gauge-carrying sufficient statistics are closed under each coarse map.

**Proof obligations:** distinguish original nodes from line-graph sites; state whether links are independent; track all generated higher-order operators; prove when maximum-coordination-two closure survives a fiber representation; establish gauge covariance of the decimation; identify whether any exact subfamily survives both node aggregation and edge decimation. Catanzaro et al. supply the scalar interacting baseline; the bundle lift follows MVG.

## Plain-language summary for a physicist

The scalar Laplacian-RG idea is useful, but it contains two different ingredients. Its heat spectrum gives a defensible way to look for scales. Its rule for deciding which nodes become one block is a heuristic. The manuscript currently treats the latter as though the former had proved it.

That distinction becomes decisive once every node has its own frame. Generalized eigenvalues survive a frame change, but heat-kernel entries do not. In the smallest possible example, changing only the local frame changes the LRG decision from “keep the nodes separate” to “merge them.” A gauge-covariant heat generator can be built from \(R^{-1}L\), but a gauge-covariant node affinity still has to be invented and proved.

The susceptibility also needs the conventional minus sign: entropy decreases with diffusion time, so the positive detector is \(-dS/d\log\tau=\tau^2\operatorname{Var}(\lambda)\). Its normalization and zero modes must be declared before connecting a plateau to spectral dimension.

On inverse RG, infinitely divisible weights let one sample finer constituents whose sum has the right law. They do not reconstruct the constituents that were discarded. That is stochastic refinement, not a two-sided inverse.

Finally, the 2026 Catanzaro--Garlaschelli--Patil paper now gives an exact RG for a limited interacting random-graph class. It does not weaken Garuccio's independent-edge uniqueness result because it uses a different state space and a different coarse map. It should nevertheless be cited so the manuscript's literature boundary is current.
