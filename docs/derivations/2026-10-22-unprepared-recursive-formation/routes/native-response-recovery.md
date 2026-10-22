<!-- rigorous-theory-search-metadata {"schema_version":"rigorous-theory-search/v1","contract_id":"contract-sha256-b542fc3173c340f7c3430dc4795f9964d742d9047e059add3a8949d73f3bbcbe","target_digest":"b542fc3173c340f7c3430dc4795f9964d742d9047e059add3a8949d73f3bbcbe"} -->
# Finite response recovery inside the native binary clique model

## Scope and relation to the prior result

The live manuscript, Chapter 9, Proposition `prop:public-gibbs-identifies`, already proves that an unrestricted identity-channel Gibbs interface identifies the distinct exposed source laws. This note gives a finite local reconstruction for the actual binary channel used by the new clique construction. Its content is the explicit reconstruction and the resulting obstruction to continuous local compression on an open set. It does not claim a new general identifiability principle, and it does not refute the frozen existential formation target over other admissible channels and protocols.

Let a source law on the fixed physical alphabet {-1,1} be q_x(k)=(1+kx)/2, with -1<x<1. Fix the homogeneous channel

\[
K_\rho(\ell\mid k)=\frac{1+\rho k\ell}{2},\qquad 0<\rho\leq1.
\]

For rho<1 every channel entry is positive, and for rho=1 this is the identity. The transmitted law has mean rho x. The map x to rho x is injective. Source priors and T>0 are fixed. No source label has to be exposed to the receiving agent.

For a block I of two sources with means x_1,x_2 and fixed positive prior weights w_1,w_2, define its contribution to the receiver's Gibbs normalizer by

\[
Z_I(r)=\sum_{j=1}^2w_j\exp\{-D(q_r\Vert q_{\rho x_j})/T\},\qquad -1<r<1.
\tag{R1}
\]

If the exterior offers another source contribution Z_o(r)>0 whose state is retained, the block-selection probability is Z_I/(Z_I+Z_o). Consequently it determines Z_I exactly. The result applies to the native nonself row of the four-agent clique example: for an exterior receiver, the two members of I are candidate sources, and the remaining exterior agent is the known competitor. Positivity makes division legitimate.

## An explicit two-source inverse

Put

\[
\psi(r)=\frac{1+r}{2}\log(1+r)+\frac{1-r}{2}\log(1-r),\qquad
 a_j=\operatorname{atanh}(\rho x_j),\quad v_j=a_j/T.
\]

Direct substitution of log q_t(k)=k atanh(t)-log(2 cosh(atanh(t))) gives

\[
D(q_r\Vert q_{\rho x_j})=\psi(r)-r a_j+\log\cosh a_j.
\]

Hence the known entropy factor removes the receiver-only term:

\[
F(r):=e^{\psi(r)/T}Z_I(r)=\sum_{j=1}^2b_j e^{v_jr},\qquad
 b_j=w_j(\cosh a_j)^{-1/T}>0.
\tag{R2}
\]

Fix any r_0 in the admitted open receiver interval, and set m_k=F^{(k)}(r_0), k=0,1,2,3. These are finite sums, so differentiation is immediate. With c_j=b_j e^{v_j r_0}>0,

\[
m_k=c_1v_1^k+c_2v_2^k,\qquad
H=m_0m_2-m_1^2=c_1c_2(v_1-v_2)^2.
\tag{R3}
\]

For x_1 different from x_2, H>0. Let s_1=v_1+v_2 and s_2=v_1v_2. Each root satisfies v_j^2=s_1v_j-s_2, so

\[
m_2=s_1m_1-s_2m_0,\qquad m_3=s_1m_2-s_2m_1.
\]

Solving this two-by-two system gives the explicit inverse

\[
s_1=\frac{m_0m_3-m_1m_2}{H},\qquad
s_2=\frac{m_1m_3-m_2^2}{H}.
\tag{R4}
\]

The two distinct real roots of z^2-s_1z+s_2 recover the unordered pair {v_1,v_2}. Finally,

\[
x_j=\rho^{-1}\tanh(Tv_j),\qquad
c_1=\frac{m_1-v_2m_0}{v_1-v_2},\qquad c_2=m_0-c_1.
\tag{R5}
\]

The inferred roots belong to (-atanh(rho)/T,atanh(rho)/T) when rho<1 because the original sources do. No analytic continuation, infinite receiver range, or Gaussian closure enters this calculation. Equality of the response function on an arbitrarily small open receiver interval implies equality of its first four derivatives and therefore equality of the unordered source laws. This is mathematical identifiability; it is not a claim that derivatives can be estimated without measurement error from finitely many samples.

## Consequence for an open class of local parent states

Suppose R_I depends on the block's own public law configuration and retained local history, while the remaining receiver and competitor laws can vary independently through an open set. Assume the same parent response kernel reproduces the native block-selection probability for every such exterior state. Whenever R_I(x)=R_I(x'), equation (R1) agrees on an open receiver interval, so (R3)-(R5) identify the unordered belief pair. Applying the same argument with the model temperature and model rows identifies the unordered model pair.

On a local chart where the two belief means and the two model means are separately distinct, ordering each pair removes the finite permutation ambiguity. The response has a smooth local inverse onto all four public scalar coordinates. There may remain a discrete ambiguity about which model mean is attached to which belief mean, but this cannot provide a continuous information-loss direction. Further evaluator or dynamical requirements can resolve that discrete ambiguity; it does not weaken the present conclusion.

Thus any retention preserving these open native exterior responses has no nonconstant continuous fiber in the four public coordinates on this chart. Adding formation timestamps or memory cannot rescue a proposed continuous compression: the argument applies to equality of the complete retained state, including those data. If the added data reconstruct the child coordinates, the retention has ceased to compress those coordinates.

This is a controlled-response statement. It does not assume arbitrary interventions on the actual trajectory. An open product neighborhood of initial laws permits exterior variations independently of the block. At a fixed finite regular time, the flow is a local diffeomorphism, so its image is open and contains product neighborhoods as well. To apply the argument at a state-dependent handoff, one must separately establish an open neighborhood of accessible retained exterior probes on that event stratum. The theorem does not silently identify a fixed-time open image with an event-conditioned preparation.

## Exactness, near equality, and escape routes

The Hankel determinant tends to zero quadratically in the source-logit separation. Near a strongly coherent pair, reconstructing its constituents is ill-conditioned, but H remains positive whenever the two exposed means are distinct. A small within-clique divergence is therefore an approximation opportunity, not exact redundancy. At exact equality the two atoms in (R2) merge and only their total weight remains; the inverse is then correctly singular.

The statement is not a no-go result for every parent. A noninjective original channel, a restricted exterior receiver family, a joint state-dependent alignment protocol, an exterior-dependent global retention, or a controlled approximation changes a premise. Each alternative still needs its own full-force projectability, joint-history response, geometry, and next-join proof. Merely replacing rho by a value close to one does not change the obstruction, since the channel remains injective.

No numerical experiment was used. Equations (R1)-(R5) are direct finite-sum identities. The underlying broad Gibbs-identification argument is already present in the live local manuscript; this explicit finite inverse supplies the interface test for the new native-clique construction.
