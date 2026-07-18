# VFE 4.0 Zero-Dimensional Population White Paper Revision Design

## Purpose

The July 17 white paper correctly constructs a normalized latent-variable language model and an exact ELBO, but it places the causal token graph in the role of bundle base. That choice conflicts with the established general theory in which agents are smooth local sections defined on open domains of a noumenal or contextual base manifold and with the V3 reduction in which the base is a single point. The revision must preserve the exact probabilistic construction while replacing the graph-base interpretation.

## Authoritative geometric distinction

The general theory begins with a smooth base manifold \(\mathcal C\), a principal \(G\)-bundle \(P\to\mathcal C\), associated sample bundles \(E_z=P\times_{\rho_z}V_z\) and \(E_m=P\times_{\rho_m}V_m\), and associated statistical bundles \(\mathscr B_z=P\times_{\rho_{z\#}}\mathcal F_z\) and \(\mathscr B_m=P\times_{\rho_{m\#}}\mathcal F_m\). An agent \(i\) is represented by statistical sections \(q_i\in\Gamma(U_i,\mathscr B_z)\) and \(s_i\in\Gamma(U_i,\mathscr B_m)\) defined on an open domain \(U_i\subseteq\mathcal C\). The base is a modeling domain and is not inferred from text by the construction.

The language-model specialization is the zero-dimensional reduction \(\mathcal C_0=\{\ast\}\). Every nonempty agent support is then the same open set \(\{\ast\}\), but the agents remain distinct labeled section values. The sequence index set \(I_T=\{0,\ldots,T\}\) labels a population of token agents stacked over \(\ast\). The causal directed acyclic graph \(D_T=(I_T,E_T)\) records dependencies among those agents. It is not the bundle base, a Cech nerve, or a discretization of the noumenal manifold.

The continuous latent sample space for the finite population is the labeled product fiber

\[
\mathcal Y_T=\bigoplus_{t\in I_T}
\left(E_{z,\ast}^{(t)}\oplus E_{m,\ast}^{(t)}\right).
\]

The exact recognition object is one normalized, generally correlated law \(Q_\psi\) on \(\mathcal Y_T\) together with the discrete source variables. Its persistent agent beliefs are pushforward marginals; full conditionals are distinct update objects. Local marginal sections do not determine the global joint. An agent-first alternative therefore requires an additional copula, correlation field, or compatible family of conditional kernels. Mean-field is only the optional block-diagonal precision restriction.

## Gauge data in the reduction

A smooth connection on \(P\to\mathcal C\) remains part of the general theory. Its base-direction curvature vanishes in the zero-dimensional reduction because \(T_\ast\mathcal C_0=0\). V3-style links \(\Omega_{tj}=U_tU_j^{-1}\) compare independently chosen agent frames at the same base point and form a flat coboundary. They are not parallel transport between distinct base points.

Independent edge links on the internal interaction graph are a separate discrete inter-agent connection. They transform by endpoint gauge actions and can carry cycle holonomy only when a declared undirected interaction complex supplies closed paths. Such holonomy is not curvature of the zero-dimensional base. The paper must keep the smooth-base connection, same-point frame comparison, and optional graph connection as three distinct objects.

## Probabilistic core

The normalized causal joint, target-blind prior-predictive recursion, categorical emission, and evidence identity remain the exact core. Their variables are retyped as labeled elements of the population product fiber rather than sections over graph vertices. The categorical cross-entropy remains the expected negative log emission inside the ELBO. Training recognition may condition on the observed target because it approximates a posterior, but the generative source priors, transitions used for prediction, and held-out evaluation must remain prefix measurable.

The preferred computational coordinates are conditional Gaussian natural parameters \((h,-J/2)\) on the global population law. Off-diagonal blocks of \(J\) encode cross-agent and cross-channel conditional dependence. Expectation coordinates are \((\mu,M)\), with \(M=\Sigma+\mu\mu^\top\); \((\mu,\Sigma)\) remain a reporting and sampling view. Natural coordinates do not themselves make an optimizer a natural-gradient method.

## Hierarchical scope

The general \(h\to s\to p\to q\to o\) hierarchy can be represented by additional statistical associated bundles and, in an exact generative model, by additional normalized latent factors. The minimal V4 white-paper core retains state and model channels and absorbs omitted levels into declared initial laws or fixed parameters. It must not imply that naming the hierarchy or adding pairwise divergences between moving beliefs creates an ELBO.

## Required manuscript changes

The title, executive summary, claim-status table, graphical abstract, geometry chapter, factor-graph caption, structured-recognition chapter, ELBO reference measure, transformer crosswalk, hypotheses, limitations, appendices, and notation table must use the general-theory/zero-dimensional-reduction distinction consistently. The rewrite must explicitly state the joint-first choice and the agent-first consistency obligation. All graph-base terminology must be removed except when describing the superseded July 17 formulation or an optional future extension.

## Verification contract

The revised document must compile with LuaLaTeX and BibTeX. Every citation key must resolve, every label must be unique, every reference must resolve, and no placeholder may remain. The manuscript must contain no banned LaTeX spacing macros, banned prose patterns, British spellings in touched prose, or unsupported equation-level claims. Independent reviewers must audit differential geometry, variational inference, and language-model causality before final compilation.
