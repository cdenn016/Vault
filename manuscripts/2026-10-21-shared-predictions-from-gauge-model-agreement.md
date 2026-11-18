# Shared predictions from approximate model agreement across gauge frames

October 21, 2026

This note investigates a conditional mechanism for shared predictive structure among agents whose generative models approximately agree after transport. Its foundation is general probability laws and normalized kernels. No Gaussian family, probability distribution over agents, external observer, or prescribed hierarchy is required for the main result. The information-theoretic identities are established below. Formation of a population satisfying their hypotheses, persistence of that population, and identification of its shared predictions with physical laws remain separate dynamical and empirical questions.

The main result is quantitative. If two transported model laws have relative entropy at most \(\epsilon\) nats and use corresponding predictive mechanisms, their probabilities for every common record event differ by at most \(\sqrt{\epsilon/2}\). Imperfect correspondence adds an explicit kernel error. A common mechanism for an entire history preserves the initial bound at every finite horizon; genuinely different mechanisms at successive steps instead contribute successive conditional divergences. This distinction determines when approximate agreement can support persistent shared predictions.

## Probability without an external observer

An agent can be a local section whose value is a probability law. At a fixed context, the section value is already the agent's statistical state. In the current PIFB2 notation, a joint state–model section can be written

\[
\zeta_i(dk,dm)=q_i(dk\mid m)s_i(dm).
\]

Here \(s_i\) is the agent's law over model presentations, and a presentation \(m\) becomes predictive through a normalized record kernel. This is the construction in [PIFB2, “One statistical bundle”](<C:/Users/chris and christine/Desktop/Research/manuscripts/pifb2/04_section.tex:66>). A distribution over entire section configurations would be another mathematical object. It is not introduced in the agreement theorem.

There are two distinct uses of probability in an observer-free cosmology. A stochastic process law can be a constitutive part of the proposed dynamics: it specifies probabilities of internally generated histories without representing anybody's ignorance. Interpreting those probabilities as objective chances would be a physical postulate, not a consequence of measure theory. An epistemic law instead belongs to a specified agent and is conditional on that agent's accessible records. These roles should be declared rather than interchanged. A deterministic evolution of law-valued sections is also possible; uncertainty inside an agent's model does not force stochastic evolution of the section itself.

“Observer-free” here means that every observer, record, and comparison mechanism is internal to the modeled system and that no distinguished observer outside it is postulated. Writing a global process law does not assert that any internal agent possesses or computes it. Likewise, an expectation in a mathematical inequality does not require an actual observer averaging over multiple universes.

The kernels below may describe interactions between agents, subagents, and environmental agents. Their common output space specifies which internally available records are being compared. It does not add an external measurement apparatus. A model presentation can describe possible interactions without being a separately postulated material object. The theorem requires an interpretation of those possibilities and their readout; it does not decide their ontology.

## Typed comparison and predictive compatibility

Fix a context, a preparation or interaction protocol, and the information on which the predictions are conditioned. Let \(\mathsf M_i,\mathsf M_j\) be standard Borel spaces of model presentations, with probability laws \(s_i,s_j\). Let

\[
\Theta_{ij}:\mathsf M_j\longrightarrow\mathsf M_i,
\]

be a fixed bimeasurable bijection. This assumption describes an invertible comparison of model presentations. Selective, noisy, or dimension-changing communication is represented by a kernel rather than by calling a noninvertible map a gauge transformation.

Choose a common standard Borel record space \(\mathsf O\), including any declared translation of the agents' record labels. Let \(K_i:\mathsf M_i\rightsquigarrow\mathsf O\) and \(K_j:\mathsf M_j\rightsquigarrow\mathsf O\) be normalized predictive kernels. In agent \(i\)'s presentation define

\[
s=s_i,\qquad
\widetilde s=\Theta_{ij\#}s_j,\qquad
K=K_i,\qquad
L(m,A)=K_j(\Theta_{ij}^{-1}m,A).
\]

For a law \(s\) and kernel \(K\), the notation \(sK\) means \((sK)(A)=\int K(m,A)s(dm)\). The compared predictive laws are

\[
\rho_i=sK,\qquad
\rho_{j\to i}=\widetilde sL.
\]

Exact predictive compatibility means \(K=L\), up to the null sets relevant to the laws being compared. Thus corresponding model presentations predict corresponding record events. This is additional content: closeness of distributions over model coordinates cannot constrain unconstrained readout mechanisms.

The conditioning matters. Agents with different private histories can reasonably make different predictions even when they share a generative architecture. A comparison must declare whether the histories are matched, transported, restricted to common information, or included among the model variables. Agreement for one such comparison is not a statement about every possible preparation.

All logarithms below are natural. Relative entropy is \(D(s\Vert t)=\int\log(ds/dt)ds\) when \(s\ll t\), and infinity otherwise. Total variation uses the convention

\[
\operatorname{TV}(s,t)=\sup_A|s(A)-t(A)|.
\]

## The shared-prediction theorem

Assume exact predictive compatibility and finite transported model disagreement

\[
D(s\Vert\widetilde s)\leq\epsilon<\infty.
\]

Define two joint laws on model presentations and records,

\[
\mu(dm,do)=s(dm)K(m,do),\qquad
\nu(dm,do)=\widetilde s(dm)K(m,do).
\]

Their conditional record mechanisms coincide, so their joint density ratio is \(ds/d\widetilde s\), evaluated at \(m\). Consequently \(D(\mu\Vert\nu)=D(s\Vert\widetilde s)\). Disintegrating instead over the record coordinate gives

\[
D(s\Vert\widetilde s)
=D(\rho_i\Vert\rho_{j\to i})
+\int
D\bigl(\mu(dm\mid o)\Vert\nu(dm\mid o)\bigr)\rho_i(do).
\tag{1}
\]

Standard Borel spaces ensure the required regular conditional laws. Finiteness of the left side ensures that the two nonnegative terms on the right are finite. This proof uses the relative-entropy chain rule in two orders; it does not use a density with respect to Lebesgue measure or a parametric family.

Nonnegativity of the conditional term and Pinsker's inequality imply

\[
D(\rho_i\Vert\rho_{j\to i})\leq\epsilon,
\qquad
\operatorname{TV}(\rho_i,\rho_{j\to i})
\leq\min\{1,\sqrt{\epsilon/2}\}.
\tag{2}
\]

Thus, for every measurable record event \(A\),

\[
\left|\rho_i(A)-\rho_{j\to i}(A)\right|
\leq\min\{1,\sqrt{\epsilon/2}\}.
\tag{3}
\]

The constant follows directly from a binary calculation. Mapping a record to the indicator of an event contracts KL. For binary relative entropy \(d(a\Vert b)\), the second derivative with respect to \(a\) is \(1/[a(1-a)]\geq4\), while the value and first derivative vanish at \(a=b\). Integrating twice gives \(d(a\Vert b)\geq2(a-b)^2\); endpoint cases follow by limits. Taking the supremum over events proves the stated normalization of Pinsker's inequality. Standard references for the contraction and binary inequality are [Polyanskiy and Wu, Theorems 7.2 and 7.7](https://people.lids.mit.edu/yp/homepage/data/LN_fdiv.pdf).

The result also controls every bounded measurable observable \(f\):

\[
\left|\mathbb E_{\rho_i}f-\mathbb E_{\rho_{j\to i}}f\right|
\leq
(\sup f-\inf f)\min\{1,\sqrt{\epsilon/2}\}.
\tag{4}
\]

Subtract \(\inf f\), divide by its range, and express the resulting \([0,1]\)-valued function through its superlevel events. Integrating Equation (3) proves Equation (4). Unbounded observables require additional tail or moment assumptions.

Equation (1) identifies exactly what the predictive mechanism conceals. Contraction is an equality if and only if \(\mu(dm\mid o)=\nu(dm\mid o)\) for \(\rho_i\)-almost every record. All disagreement relevant to distinguishing this pair then survives in the output. At the other extreme, a constant kernel \(K(m,\cdot)=\rho_0\) produces identical predictions for arbitrarily different model laws. Predictive agreement is therefore weaker than complete internal-model agreement.

A finite-state example makes the split explicit. Let \(M=(A,B)\in\{0,1\}^2\), let \(s=\operatorname{Ber}(1/2+a)\otimes\operatorname{Ber}(1/2+b)\), and let \(\widetilde s=\operatorname{Ber}(1/2)\otimes\operatorname{Ber}(1/2)\), with \(|a|,|b|<1/2\). The kernel reports \(A\). Define

\[
d(u)=(1/2+u)\log(1+2u)+(1/2-u)\log(1-2u).
\]

Then model KL is \(d(a)+d(b)\), record KL is \(d(a)\), and the conditional remainder is \(d(b)\). Setting \(a=0\) hides all disagreement; setting \(b=0\) makes KL contraction an equality. Since \(d(a)=2a^2+O(a^4)\) and record TV is \(|a|\), the small-disagreement constant in Equation (3) cannot be uniformly improved.

## Imperfectly compatible predictive mechanisms

Model agreement is insufficient when \(K\neq L\). Define

\[
\delta(m)=\operatorname{TV}\bigl(K(m,\cdot),L(m,\cdot)\bigr),
\qquad
\kappa(m)=D\bigl(K(m,\cdot)\Vert L(m,\cdot)\bigr).
\]

The functions are measurable for the standard Borel kernels under consideration. Insert \(\widetilde sK\) between \(sK\) and \(\widetilde sL\). Kernel contraction and convexity of TV give

\[
\operatorname{TV}(sK,\widetilde sL)
\leq\operatorname{TV}(s,\widetilde s)
+\mathbb E_{\widetilde s}\delta.
\]

Inserting \(sL\) instead gives the analogous bound weighted by \(s\). Therefore

\[
\operatorname{TV}(\rho_i,\rho_{j\to i})
\leq
\min\left\{
1,\sqrt{\epsilon/2}
+\min\{\mathbb E_s\delta,\mathbb E_{\widetilde s}\delta\}
\right\}.
\tag{5}
\]

Either expectation is valid because it comes from a different intermediate comparison. A uniform kernel discrepancy \(\delta(m)\leq\delta_0\) yields the simpler bound \(\min\{1,\sqrt{\epsilon/2}+\delta_0\}\).

There is a different, exact accounting in KL. For the joint laws \(\mu(dm,do)=s(dm)K(m,do)\) and \(\nu(dm,do)=\widetilde s(dm)L(m,do)\), the two chain decompositions give

\[
D(s\Vert\widetilde s)+\mathbb E_s\kappa
=D(\rho_i\Vert\rho_{j\to i})
+\mathbb E_{\rho_i}
D\bigl(\mu(dm\mid O)\Vert\nu(dm\mid O)\bigr).
\tag{6}
\]

When the displayed input and conditional divergences are finite,

\[
D(\rho_i\Vert\rho_{j\to i})
\leq\epsilon+\mathbb E_s\kappa,
\qquad
\operatorname{TV}(\rho_i,\rho_{j\to i})
\leq\min\left\{1,\sqrt{\frac{\epsilon+\mathbb E_s\kappa}{2}}\right\}.
\tag{7}
\]

The kernel KL is averaged under the first model law \(s\). Substituting an average under \(\widetilde s\) would require an additional argument. Reversing the whole comparison gives a different conditional divergence, \(D(L\Vert K)\), averaged under \(\widetilde s\).

A singleton model space exposes the necessary assumption: the two model laws are identical, but \(K=\delta_0\) and \(L=\delta_1\) give maximally different record laws. Their model KL is zero, predictive TV is one, and predictive KL is infinite. This is why model agreement must include compatible meaning for the model presentations.

## Gauge covariance and comparison around a network

Let \(g_i,g_j\) be bimeasurable changes of model presentation and \(h\) a common bimeasurable re-expression of records. The transformed objects obey

\[
s_i'=g_{i\#}s_i,\qquad
s_j'=g_{j\#}s_j,\qquad
\Theta_{ij}'=g_i\Theta_{ij}g_j^{-1},
\]

\[
K_i'(g_i m,hA)=K_i(m,A),\qquad
K_j'(g_j m,hA)=K_j(m,A).
\]

Thus \(\rho_i'=h_\#\rho_i\) and \(\rho_{j\to i}'=h_\#\rho_{j\to i}\). KL, TV, and the averaged kernel discrepancies are unchanged. The theorem is gauge invariant as a statement about predictions, although the laws and kernels transform covariantly. This agrees with [PIFB2's distinction between coordinate consistency and empirical symmetry](<C:/Users/chris and christine/Desktop/Research/manuscripts/pifb2/23_section.tex:6>).

At a fixed context consider a directed path \(i_0\leftarrow i_1\leftarrow\cdots\leftarrow i_r\) with typed invertible comparisons. Put

\[
e_{ij}=\operatorname{TV}(s_i,\Theta_{ij\#}s_j),
\qquad
\Theta_{\mathrm{path}}=
\Theta_{i_0i_1}\cdots\Theta_{i_{r-1}i_r}.
\]

Insert the successive transported intermediate laws. The TV triangle inequality and invariance under invertible pushforward give

\[
\operatorname{TV}
\left(s_{i_0},\Theta_{\mathrm{path}\#}s_{i_r}\right)
\leq\min\left\{1,\sum_{k=0}^{r-1}e_{i_ki_{k+1}}\right\}.
\tag{8}
\]

Directional edge bounds \(D(s_i\Vert\Theta_{ij\#}s_j)\leq\epsilon_{ij}\) imply \(e_{ij}\leq\sqrt{\epsilon_{ij}/2}\). KL itself is not being given a triangle inequality. A common endpoint record kernel contracts the resulting TV bound.

For a closed path based at \(i\), with composite \(H_\gamma\), Equation (8) becomes

\[
\operatorname{TV}(s_i,H_{\gamma\#}s_i)
\leq\min\left\{1,\sum_{e\in\gamma}e_e\right\}.
\tag{9}
\]

This bounds the action of the loop on the specified law. It does not bound the loop map's distance from the identity. A uniform finite-state law is invariant under every permutation, including nontrivial ones. Exact edge agreement therefore puts the loop in the shared law's stabilizer, without forcing trivial holonomy.

A direct link and a composite route can differ. When both are available, their actions on the endpoint law differ in TV by at most the path error plus the direct-edge error. No cocycle identity or flatness has been assumed. Selective interfaces that expose different information at different edges do not automatically satisfy the full-model comparison hypotheses of Equation (8); composable kernels and their retained conditional information must be specified.

## A shared public law and residual variation within a species

A population statement needs all predictions in one common record space for the same comparison. For this section assume that a common model presentation has been chosen, with aligned laws \(\bar s_i\), and that all agents use the same predictive kernel \(K\). Such a presentation is additional compatibility data; arbitrary independent network links do not guarantee it. Suppose

\[
D(\bar s_i\Vert\bar s_j)\leq\epsilon_{ij},
\]

for every ordered pair being used. Then \(D(\rho_i\Vert\rho_j)\leq\epsilon_{ij}\), where \(\rho_i=\bar s_iK\).

Choose fixed weights \(w_i>0\), \(\sum_iw_i=1\), for a finite population, and define the comparison law \(\bar\rho=\sum_iw_i\rho_i\). This is a mathematical reference. If it is given a physical sampling interpretation, the weights must describe an internal source-selection mechanism. No external observer is required in either reading.

Convexity of KL in its second argument gives

\[
D(\rho_i\Vert\bar\rho)
\leq\sum_jw_jD(\rho_i\Vert\rho_j).
\]

Indeed, take densities with respect to the finite dominating mixture and apply convexity of \(-\log\) pointwise before integrating. With the joint law \(\Pr(I=i,O\in A)=w_i\rho_i(A)\),

\[
I(I;O)=\sum_iw_iD(\rho_i\Vert\bar\rho)
\leq\sum_{i,j}w_iw_j\epsilon_{ij}.
\tag{10}
\]

Under uniform pairwise error \(\epsilon_{ij}\leq\epsilon\), at most \(\epsilon\) nats about the selected agent's identity are carried by this record. This is a precise sense in which a public prediction becomes approximately independent of which member supplies it. It concerns the declared protocol and mixture weights.

For one event \(A\), write \(p_i=\rho_i(A)\) and \(\bar p=\sum_iw_ip_i\). The exact identity

\[
\operatorname{Var}_w(p_I)
=\frac12\sum_{i,j}w_iw_j(p_i-p_j)^2,
\]

and Pinsker's inequality imply

\[
\operatorname{Var}_w(p_I)
\leq\frac14\sum_{i,j}w_iw_j\epsilon_{ij}.
\tag{11}
\]

If every pair is bounded by the same \(\epsilon\), the probabilities lie in an interval of width at most \(\min\{1,\sqrt{\epsilon/2}\}\). The variance of a variable in an interval of width \(d\) is at most \(d^2/4\), so a second bound is

\[
\operatorname{Var}_w(p_I)\leq\min\{1/4,\epsilon/8\}.
\tag{12}
\]

For completeness, if \(a\leq p_I\leq b\), then \(\mathbb E[(p_I-a)(b-p_I)]\geq0\) gives \(\operatorname{Var}(p_I)\leq(b-\bar p)(\bar p-a)\leq(b-a)^2/4\).

Variation between agents' predicted probabilities is distinct from variability of the records themselves. Under the source-selection interpretation, for the indicator \(B=1_{\{O\in A\}}\),

\[
\bar p(1-\bar p)
=\sum_iw_ip_i(1-p_i)+\operatorname{Var}_w(p_I).
\tag{13}
\]

Exact predictive agreement sets the second term to zero while leaving the first nonzero whenever the common event probability lies strictly between zero and one. Nor does a cross-sectional variance assert that any agent's probabilities fluctuate in time.

A binary channel illustrates selective agreement. Let \(\bar s_i=\operatorname{Ber}(1/2+a_i)\), and let the record flip the modeled bit with a common probability \(\eta\in[0,1/2]\). Then \(p_i=1/2+(1-2\eta)a_i\), and the population variance of predicted probabilities is multiplied by \((1-2\eta)^2\). At \(\eta=1/2\), all disagreement disappears because the channel erases the bit. Public agreement can therefore result from useful shared models or from loss of discriminating information; agreement alone does not distinguish these mechanisms.

## Repeated interactions and conditional disagreement

There are two different ways to extend the theorem through time. Their distinction is necessary when discussing persistent shared physics.

First, suppose that a model presentation \(m\) is retained throughout the record history. Conditional on \(m\), both agents use the same normalized kernel \(K_T(m,dh)\) for the entire finite history \(H_T\). This is the probabilistic construction \(s(dm)K_T(m,dh)\), not a requirement that an outside observer physically samples a model. A normalized mechanism can include internal actions and adaptive record gathering, for example

\[
K_T(m,dh)=
\prod_{t=1}^{T}
\pi_t(da_t\mid h_{t-1})
K_t(do_t\mid m,h_{t-1},a_t).
\]

The policy must be the same function of the same history in both compared models. Policies separately recomputed from different current model laws need not satisfy that condition.

Applying Equation (1) to the whole history gives, for every finite \(T\),

\[
D(s\Vert\widetilde s)
=D(sK_T\Vert\widetilde sK_T)
+\mathbb E_{sK_T}
D\bigl(s(dm\mid H_T)\Vert\widetilde s(dm\mid H_T)\bigr).
\tag{14}
\]

The notation for the conditional laws refers to the two stated model–history joints. Their predictive-history KL is at most \(\epsilon\), with no factor of \(T\). The initial difference can become visible through records but cannot gain KL through a common conditional mechanism. Bayesian posterior disagreement is controlled in expectation under the first history law, not uniformly after every realized history.

A three-state example shows the limitation. For \(0<r<1/2\), take

\[
s=(1-r,r(1-r),r^2),\qquad
\widetilde s=(1-r,r^2,r(1-r)),
\]

on \(\{a,b,c\}\). Their divergence is

\[
D(s\Vert\widetilde s)
=r(1-2r)\log\frac{1-r}{r}\longrightarrow0,
\]

as \(r\downarrow0\). A first record reports whether \(m\in\{b,c\}\), an event with probability \(r\) under both laws. Conditional on that event, the two probabilities of \(m=b\) are \(1-r\) and \(r\). Thus the next record can have conditional predictive TV \(1-2r\), arbitrarily close to one. There is no contradiction with Equation (14): this disagreement occurs on an increasingly rare history.

Second, consider different conditional record mechanisms at successive steps. Write

\[
\mathbb P_T(do_{1:T})=
\prod_{t=1}^{T}p_t(do_t\mid h_{t-1}),\qquad
\mathbb Q_T(do_{1:T})=
\prod_{t=1}^{T}q_t(do_t\mid h_{t-1}).
\]

Under finite conditional divergences and the corresponding absolute continuity, the logarithm of the path-density ratio is the sum of conditional log ratios. Hence

\[
D(\mathbb P_T\Vert\mathbb Q_T)
=\sum_{t=1}^{T}
\mathbb E_{\mathbb P_{H_{t-1}}}
D\bigl(p_t(\cdot\mid H_{t-1})
\Vert q_t(\cdot\mid H_{t-1})\bigr).
\tag{15}
\]

If the expected term at step \(t\) is at most \(\epsilon_t\), path KL is at most \(\sum_t\epsilon_t\), and path TV is at most \(\min\{1,\sqrt{\sum_t\epsilon_t/2}\}\). The expectations must use the actual first path law. Bounds checked on selected histories do not establish this statement. Equation (15) also applies to the retained-model construction of Equation (14); there its entire sum is bounded by the initial model KL. The chain rule itself does not imply growth proportional to the horizon. Such growth requires further properties of the conditional mechanisms.

For independent repeated Bernoulli records with parameters \(1/2+a\) and \(1/2-a\), where \(0<a<1/2\),

\[
D(\mathbb P_T\Vert\mathbb Q_T)
=2Ta\log\frac{1/2+a}{1/2-a}.
\tag{16}
\]

Their empirical record frequencies converge to different values, so path TV tends to one. This construction has a discrepancy at every draw. It is not the single-retained-model construction of Equation (14). Equivalently, independent resampling of the model at every step gives a product input law whose KL already grows with \(T\).

## A conditional mechanism for maintaining agreement

The previous inequalities transfer an assumed model agreement to records. They do not make model agreement stable. One explicit sufficient update condition can nevertheless be stated without selecting a Gaussian family.

Work in common model coordinates and let \(T_n\) be a normalized Markov kernel on those coordinates with total-variation contraction coefficient at most \(\alpha<1\). This means

\[
\operatorname{TV}(sT_n,tT_n)
\leq\alpha\operatorname{TV}(s,t),
\]

for all model laws \(s,t\). A sufficient characterization is \(\sup_{m,m'}\operatorname{TV}(T_n(m,\cdot),T_n(m',\cdot))\leq\alpha\). This is the Dobrushin coefficient discussed in [Polyanskiy and Wu, Section 2](https://arxiv.org/html/1508.06025v4).

Suppose the actual pair updates are \(s_{n+1}=s_nT_n\) and \(\widetilde s_{n+1}=\widetilde s_n\widetilde T_n\), with \(\mathbb E_{\widetilde s_n}\operatorname{TV}(T_n(m,\cdot),\widetilde T_n(m,\cdot))\leq\eta_n\). Then Equation (5)'s triangle argument yields

\[
d_{n+1}\leq\alpha d_n+\eta_n,\qquad
d_n=\operatorname{TV}(s_n,\widetilde s_n).
\]

Iteration gives

\[
d_n\leq\alpha^n d_0+
\sum_{k=0}^{n-1}\alpha^{n-1-k}\eta_k.
\tag{17}
\]

For \(\eta_k\leq\eta\), the bound is \(\alpha^nd_0+\eta(1-\alpha^n)/(1-\alpha)\), capped at one. A common predictive kernel transfers this bound to record TV; a mismatched readout adds its own error as in Equation (5).

This is a conditional stability result for a specified class of updates. Fisher descent, interacting nonlinear belief dynamics, and normalized Bayesian conditioning are not automatically linear Markov-kernel updates with a uniform contraction coefficient. The rare-record example already shows why conditioning can expand disagreement. A constant update kernel also satisfies strong contraction by erasing the previous model. Thus applying Equation (17) to a species hypothesis requires both a derivation of the update condition and evidence that the retained predictions carry nontrivial information.

## What the result establishes, and the next obligation

The theorem gives a possible mathematical meaning to shared physics within a population: members supply nearly the same probabilities for corresponding internally generated records, despite differences in their coordinate presentations and private information. Equations (10)–(13) quantify identity dependence and residual variation. They require no external observer and no probability law over the agents' section configurations.

The statement is conditional on the actual predictive kernels. If the model-law comparison ignores differences in likelihoods, preparations, action policies, or available history, its small value can coexist with large predictive disagreement. Conversely, a selective kernel can produce identical records while concealing substantial differences in internal models. None of the bounds proves calibration against the process that generates the records, selects a particular physical gauge group, or establishes a law of nature.

The bounds concern values of probability laws. They do not control their derivatives across the base or automatically identify a shared information geometry. [PIFB2's explicit counterexample](<C:/Users/chris and christine/Desktop/Research/manuscripts/pifb2/20_section.tex:58>) uses laws that are uniformly close in KL while their pullback Fisher tensors differ without a uniform bound. No derivative or geometric conclusion is imported here.

The next concrete obligation is to take one existing model-sector interaction from PIFB2, identify its normalized predictive evaluator, and establish a compatibility residual of the form in Equation (5) or (7). Then determine whether the specified dynamics preserve a useful bound on the transported model disagreement over a declared interval. Equation (17) supplies one sufficient route if its update hypotheses can actually be derived; it is not assumed to describe the current population dynamics.

An internal record protocol should separate loss of predictive distinctions from stable agreement about informative records. Comparing only a finite collection of record events can test those predictions, but it does not estimate the supremum over every event without further assumptions. The finite-history theorem offers a stronger analytic target whenever a common full-history kernel can be established.

These are standard information-theoretic consequences applied to the existing gauge-model construction. They extend the current operational-agreement discussion rather than introduce a new probability ontology. The unresolved scientific question is whether the chosen agent dynamics generate and sustain the compatibility and agreement whose observable consequences have been derived.

## Sources and scope of checking

The live source starting points were [PIFB2's statistical sections and model evaluators](<C:/Users/chris and christine/Desktop/Research/manuscripts/pifb2/04_section.tex:66>), [public agreement and private variation](<C:/Users/chris and christine/Desktop/Research/manuscripts/pifb2/20_section.tex:46>), [gauge covariance and empirical symmetry](<C:/Users/chris and christine/Desktop/Research/manuscripts/pifb2/23_section.tex:4>), and [cross-scale prediction and record accounting](<C:/Users/chris and christine/Desktop/Research/manuscripts/pifb2/10_section.tex>). The wiki notes “Agents as fiber-bundle sections” and “Meta-agents and hierarchical emergence” supplied the historical species interpretation. Their older Gaussian implementation language was not imposed on these general-law results.

For standard background, Polyanskiy and Wu's [lecture on f-divergences](https://people.lids.mit.edu/yp/homepage/data/LN_fdiv.pdf), Theorems 7.2 and 7.7, gives data processing and Pinsker's inequality with explicit logarithm conventions. Their [“Strong data-processing inequalities for channels and Bayesian networks”](https://arxiv.org/html/1508.06025v4), Section 2 and Appendix A, treats channel contraction and general-space extensions. The proofs specific to the present comparisons, mismatch accounting, population bounds, and temporal cases are given above.

Two bounded source-based derivations developed the predictive and temporal comparisons. A separate mathematical reconstruction checked Equations (1)–(17), the finite-state counterexamples, and the observer interpretation. Its clarification that Equations (14) and (15) are compatible was incorporated. This check concerns the statements and assumptions in this note; it does not certify the rest of PIFB2.

The work is an analytical investigation with finite-state examples, not a simulation or a physical experiment. No claim is made that the derived sufficient conditions hold in a trained model, biological population, or cosmological realization.
