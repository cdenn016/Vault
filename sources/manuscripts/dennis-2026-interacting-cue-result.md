---
type: manuscript
title: "Interacting cue/result agents: exact records, inference, and retention"
aliases: ["Interacting cue-result manuscript", "Posterior-sampling cue-result communication"]
authors: ["Robert C. Dennis"]
year: 2026
tags: [cluster/multi-agent, cluster/vfe, cluster/attention, project/multi-agent, project/transformer, field/statistics, field/mathematics]
created: 2026-10-28
---

# Interacting cue/result agents: exact records, inference, and retention

> [!info] Citation
> Robert C. Dennis (2026). *Interacting cue/result agents: exact records, inference, and retention*. Research derivation for MAgent Theory 2.0, October 28, 2026.

## Target and assumptions

The result constructs one normalized two-agent communication protocol extending the local model in [[dennis-2026-cue-result-memory]]. It establishes exact inference for every admitted finite message history before moment projection. A common preparation law, its cross-agent coupling, the private-record mechanisms, the posterior-sampling policy, a fixed alternating speaker schedule, and reliable sharing of the delivered transcript are supplied assumptions. Sharing the parameters of a local bank alone does not supply this coupling or protocol. The construction does not identify the transformer stack with the interacting process.

For agent $i\in\{0,1\}$, let $Z_i=(A_i,X_i,Y_i)$ denote its presentation, cue, and result on standard Borel spaces, with local bank

$$
\pi_i(da,dx,dy)=r_i(da)\mu_{i,a}(dx)K_{i,a}(x,dy).
$$

Choose a normalized coupling $P_0(dz_0,dz_1)$ of these banks and normalized private-record kernels $L_i(x_i,dd_i)$. With $D=(D_0,D_1)$, the preparation is

$$
\Lambda_0(dz,dd)=P_0(dz_0,dz_1)L_0(x_0,dd_0)L_1(x_1,dd_1).
$$

The private records are conditionally independent given the represented variables. Agent $i$ observes only its own $D_i$ and the common transcript $H_{1:t}$. Its local recognition remains the joint law $s_{i,t}(da_i)q_{i,t}(dx_i,dy_i\mid a_i)$; presentation and content need not be independent. Regular conditional laws are fixed measurably on the admitted family, with normalized extensions on null histories. Density formulas apply where the predictive evidence is positive and finite. General statements about conditional laws hold almost surely.

## The actual message law

The next speaker $j$ draws a fresh $\widetilde Y$ from $P(Y_j\in dy\mid D_j,H_{1:t})$ and applies a fixed normalized encoder $C_j(y,dh)$. Conditional on the speaker's information, this randomization is independent of the prepared variables. Thus the common posterior $\Gamma_t=P(Z,D\mid H_{1:t})$ determines the message kernel

$$
\kappa_j(\Gamma_t,d_j;dh)
=\int C_j(y,dh)P(Y_j\in dy\mid D_j=d_j,H_{1:t}).
$$

The new sample is not a measurement of the already represented $Y_j$. Those two experiments can have equal unconditional message marginals and different receiver posteriors. In the dominated case, with message density $k_j$, the exact update is

$$
\Gamma_{t+1}(dz,dd)
=\frac{k_j(h_{t+1}\mid d_j,\Gamma_t)\Gamma_t(dz,dd)}
{\int k_j(h_{t+1}\mid d_j',\Gamma_t)\Gamma_t(dz',dd')}.
$$

Successive integration of the normalized message kernels proves normalization and consistency of every finite-history law. Bayes' rule under that law gives the displayed recursion. The speaker's own private posterior is unchanged by its transmission because the likelihood factor is constant after conditioning on its $D_j$. The receiver instead integrates over the unknown peer record under $P(dd_j\mid Z_i,D_i,H_{1:t})$. Its local marginal generally does not determine that conditional law.

## Exact retention by a fixed reconstruction

Disintegrate the preparation as

$$
\Lambda_0(dz,dd)=W(d,dz)\lambda_0(dd),
\qquad W(d,dz)=P(Z\in dz\mid D=d).
$$

Every message likelihood at a fixed transcript is a function of $D$ alone. It reweights $\lambda_0$ without changing the conditional factor $W$, giving the exact identity

$$
\Gamma_t(dz,dd)=W(d,dz)\lambda_t(dd),
\qquad \lambda_t=P(D\in\cdot\mid H_{1:t}).
$$

Define the fixed encoded-result kernel $V_j(d,dh)=\int C_j(y,dh)W^{Y_j}(d,dy)$. The closed message and assimilation equations are

$$
\kappa_j^{\lambda_t}(d_j,dh)
=\int V_j(d,dh)\lambda_t(dd\mid D_j=d_j),
$$

$$
\lambda_{t+1}(dd)
=\frac{k_j^{\lambda_t}(h_{t+1}\mid d_j)\lambda_t(dd)}
{\int k_j^{\lambda_t}(h_{t+1}\mid d_j')\lambda_t(dd')}.
$$

The $Z_i$ posterior is reconstructed by integrating the corresponding marginal of $W$ against $\lambda_t(dd\mid D_i=d_i)$. Keeping the fixed model and encoders, $W$, the joint law $\lambda_t$, the agent's private value, and the next speaker preserves every finite future message and assimilation law of this protocol. The actual transcript must also remain registered when past-record queries belong to the interface. The statistical state need not reconstruct its literal entries.

On the admitted family $\{W\lambda\}$, marginalization to $\lambda$ and reconstruction by $W$ are inverse descriptions. This is a sufficient retention, with no minimality or lossy-parent claim. The fixed kernel can be large, and an exact continuous law need not have a finite description. Its two private-record marginals cannot generally replace the joint law.

For a fixed observed history, let $\mathcal L_t(D)$ be its likelihood under the historically specified policies and $Z_t$ its evidence. Under the absolute-continuity and finiteness hypotheses for the displayed terms,

$$
\mathcal F_t^D(\nu)
=\operatorname{KL}(\nu\Vert\lambda_0)-\mathbb E_\nu\log\mathcal L_t(D)
=\operatorname{KL}(\nu\Vert\lambda_t)-\log Z_t.
$$

The full-law free energy adds the $\nu$-average conditional KL to $W$; minimizing that conditional recovers $W$ exactly. Recomputing past policies from a candidate variational law would change the objective. These identities do not establish a reciprocal Fisher potential or a monotone sum of the agents' private free energies during communication.

## An exact four-weight exchange

Take binary variables, a fair $X_0$, and $P(X_1=X_0)=3/4$. Conditional on the cues, independently prepare $P(A_i=X_i)=3/4$, $P(Y_i=1-X_i)=3/4$, and $P(D_i=X_i)=3/4$. The encoder transmits the fresh result sample itself. If $p_i=P(X_i=1\mid D_i,H_{1:t})$, then

$$
P(A_i=1\mid D_i,H_{1:t})=\frac14+\frac12p_i,
\qquad
P(Y_i=1\mid D_i,H_{1:t})=\frac34-\frac12p_i.
$$

The local presentation/cue covariance is $p_i(1-p_i)/2>0$, while the result/cue covariance is its negative. With private values $D_0=1,D_1=0$, agent 1 speaking first, and messages $H_1=H_2=1$, agent 0's cue probability changes from $3/4$ to $45/62$. Its probability of replying with one changes from $3/8$ to $12/31$. Agent 1's cue probability changes from $1/4$ to $437/1918$ upon receiving that reply. Each local posterior uses only its own private value and the transcript.

In the order $(D_0,D_1)=(00,01,10,11)$, the joint private-record weights are exactly

$$
\lambda_0=\frac1{32}(9,7,7,9),
\qquad
\lambda_1\bigm|_{H_1=1}=\frac1{128}(45,21,35,27),
$$

$$
\lambda_2\bigm|_{H_1=H_2=1}
=\left(\frac{105}{242},\frac{49}{242},\frac{70}{341},\frac{54}{341}\right).
$$

The fixed reconstruction is $P(X_0=1\mid D)=(1/6,5/14,9/14,5/6)$; exchange the two private coordinates for agent 1. Conditional averaging and normalized reweighting give the stated fractions. Four weights evolve regardless of the number of exchanges; $W$ and the persistent registers remain part of the retained data.

A direct measurement $Y_1=1$ instead gives agent 0 the cue probability $9/14$. Two fresh samples from agent 1 before a reply give $45/64$; multiplying two independently marginalized cue likelihoods incorrectly gives $171/244$. The samples share the inaccessible $D_1$ and are independent conditional on that record, not conditional only on $X_1$. A deterministic echo is a third protocol and adds no evidence after the first message is registered. These are analytical probability identities.

## Gaussian closure and a retention obstruction

With one component per agent, a jointly Gaussian cue preparation, affine Gaussian result kernels, additive nondegenerate Gaussian private records, and linear Gaussian encoders, the common joint private-record law remains Gaussian at every finite step. Indeed $W$ has an affine conditional mean and constant covariance; reconstructing $W\lambda_t$ and conditioning on the speaker's coordinate gives an affine Gaussian result prediction. Posterior sampling and encoding then give an affine Gaussian likelihood in that coordinate. Gaussian conditioning closes the induction. This exact specialization retains the joint private-record covariance.

Finite-component Gaussian banks do not universally preserve a finite Gaussian-mixture posterior. A two-component sender can have a logistic private-record-dependent weight. The resulting receiver likelihood has different positive finite limits at the two cue tails. Multiplying its pre-message Gaussian by this likelihood yields a posterior whose ratio to that Gaussian has unequal positive finite tail limits. No finite positive Gaussian mixture has this property: wider components diverge relative to the baseline, shifted equal-variance components diverge in one tail, narrower components vanish in both tails, and identical components contribute equal limits. The obstruction concerns this closure family, while the normalized general-law update remains available.

A separate fixed binary preparation provides two reachable common histories with identical local joint recognition laws and different next assimilation. Let $X_0$ be fair, $B$ independent with $0<P(B=0)<1$, $X_1=X_0\mathbin{\mathrm{xor}}B$, and register the parity $C=B$ publicly. Use the same presentation and result kernels as above, an uninformative receiver record, and a sender record correct with probability $3/4$. For either fixed sender-private value, the local recognition laws are identical at $C=0$ and $C=1$. The same posterior-sampled message $H=1$ nevertheless gives

$$
P(X_0=1\mid C=0,H=1)=\frac7{16},
\qquad
P(X_0=1\mid C=1,H=1)=\frac9{16}.
$$

Deleting the parity and its cross-agent dependence therefore prevents an exact update from descending to the pair of local recognition laws, even if every local presentation/content correlation is retained. Retaining $C$, or its effect in a reconstruction $W_C=P(Z\mid D,C)$, resolves this particular collision. The example does not prove that the complete common posterior is minimal.

## Relevance to this research and remaining scope

For [[Cue-result generative memory]] and the [[Gauge-Theoretic Multi-Agent VFE Model]], the construction supplies a normalized case in which a received prediction changes a later transmitted prediction while correlated local recognition is preserved. It makes the dependence needed by [[Decentralized Bayesian inference]] explicit. A local moment projection can be introduced only after specifying the joint experiment; local means and covariances do not reconstruct the peer-evidence conditional consumed by the receiver.

The scope is communication about a fixed preparation under one supplied common model. New private measurements, learned banks or policies, differing agent models, unreliable transcript sharing, minimal retained state, efficient multi-component approximation, and endogenous formation remain separate obligations. No equivalence to reciprocal law dynamics, implementation claim for the [[VFE Transformer Program]], or performance claim follows. The next approximation problem is to control errors in the joint private-record law by their effects on future message and assimilation laws.

## BibTeX

```bibtex
@unpublished{dennis2026interactingcueresult,
  author = {Dennis, Robert C.},
  title = {Interacting Cue/Result Agents: Exact Records, Inference, and Retention},
  year = {2026},
  note = {Research derivation for MAgent Theory 2.0, October 28}
}
```
