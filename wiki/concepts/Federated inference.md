---
type: concept
title: "Federated inference"
aliases:
  - "Belief sharing"
  - "Federated inference and belief sharing (concept)"
tags:
  - cluster/multi-agent
  - cluster/vfe
  - project/multi-agent
  - project/social-physics
status: draft
created: 2026-11-13
updated: 2026-11-13
---

# Federated inference

## Definition

Federated inference is the name that [[friston-2024-federated-inference]] gives to belief updating in which each agent of an ensemble assimilates messages from the other agents while it infers the latent states of a world that all of them observe. The agents are discrete-state [[Active Inference|active inference]] agents with a common generative model, and the messages carry their posterior beliefs about those latent factors that all of them represent in a common frame of reference. Belief sharing is the mechanism: every agent broadcasts its posterior over a shareable factor through an outcome modality, and every other agent reads the broadcast through a likelihood mapping that the agents hold in common. The paper identifies this likelihood mapping from beliefs to their overt expression with language, and it studies in turn the use of the mapping during inference, its acquisition by an agent that lacks it, and its emergence among agents none of whom has it (Introduction and Sections 3 to 5).

The term is borrowed from federated learning in machine learning; the paper cites Kairouz et al. (2021) and compares the two in its Section 6.3. The object is different. In federated learning, parties exchange gradient or parameter information about a common model without exchanging raw data. Here agents exchange full posterior distributions over hidden states, and the exchange changes state inference at every time step. The page [[Decentralized Bayesian inference]] covers the statistical literature on distributed posteriors, which uses the word in the machine-learning sense.

## Why it matters here

The paper is the active-inference construction nearest to the peer coupling of the [[Gauge-Theoretic Multi-Agent VFE Model]], and three places in the vault depend on what it says: the source note, whose relevance section overstates the relation; the correction recorded in [[Collective active inference]]; and the related-work passages of the collective-agents manuscript, which until November 13, 2026 stated that the paper was known there through its abstract and secondary accounts and now cite the full text. This page records a reading of the full published article ([published PDF](../../sources/pdfs/friston2024federated.pdf), 23 pages), with the equations checked against the printed pages, so that comparisons can rest on what the paper derives, what it simulates and what it asserts.

## Details

### The generative model and message passing

Each agent is a partially observed Markov decision process over discrete states (Section 2.1, Fig. 1). A likelihood tensor $\mathbf{A}$ maps hidden-state factors $f$ to outcome modalities $g$, a transition tensor $\mathbf{B}$ moves each factor under a path $u$, and further tensors $\mathbf{C}$, $\mathbf{D}$ and $\mathbf{E}$ give priors over paths, initial states and initial paths. The tensors are generally parameterized as Dirichlet distributions whose concentration parameters, written in lowercase, count how often a combination of states or outcomes has been observed, and the paper focuses on learning the likelihood counts $\mathbf{a}$. The approximate posterior factorizes over states, paths and likelihood parameters, $Q(s,u,a)=Q(s)Q(u)Q(a)$, and its sufficient statistics, written in bold, are expected probabilities. Inference minimizes the [[Variational free energy|variational free energy]] of the paper's Eq. 1, and controllable paths receive a prior that is a softmax of the negative [[Expected Free Energy|expected free energy]] of Eq. 2, which decomposes into expected information gain about parameters and about states plus an expected cost.

Belief updating is variational message passing on a factor graph (Section 2.3, Fig. 2). For a single agent, the posterior expectation over the states of factor $f$ at time $\tau$ is given by Eq. 4,

$$
\mathbf{s}^{f}_{\tau} = \sigma\big( \mu^{f}_{\uparrow\mathbf{A}} + \mu^{f}_{\rightarrow\mathbf{B}} + \mu^{f}_{\leftarrow\mathbf{B}} \big),
$$

in which the likelihood message is a sum over the outcome modalities that the factor generates,

$$
\mu^{f}_{\uparrow\mathbf{A}} = \sum_{g\in ch(f)} \mu^{g,f}_{\uparrow\mathbf{A}},
$$

and each summand is

$$
\mu^{g,f}_{\uparrow\mathbf{A}} = \mathbf{o}^{g}_{\tau} \odot \varphi(\mathbf{a}^{g}) \odot_{i\in pa(g)\setminus f} \mathbf{s}^{i}_{\tau}.
$$

Here $\sigma$ is the softmax, $\mu_{\uparrow\mathbf{A}}$ is the ascending log-likelihood message from the modalities $ch(f)$, $\mu_{\rightarrow\mathbf{B}}$ and $\mu_{\leftarrow\mathbf{B}}$ are the forward and backward log-prior messages from beliefs about the preceding and following states, $\mathbf{o}^{g}_{\tau}$ is the observation in modality $g$, $\varphi(a)=\psi(a)-\psi(a_0)$ is the expected logarithm of a Dirichlet-distributed column (with $\psi$ the digamma function and $a_0$ the column sum), and $\odot$ is a sum-product contraction over one tensor dimension (footnote 4 of the paper). The transition subscript is printed in italic in Eq. 4 and in bold in Eqs. 6 to 8; the same messages are meant. By Jensen's inequality the likelihood message has the upper bound of Eq. 5, stated for a single parent,

$$
\mu^{g}_{\uparrow\mathbf{A}} = \mathbf{o}^{g}_{\tau} \odot \varphi(\mathbf{a}^{g}) \le \ell\big( \mathbf{o}^{g}_{\tau} \odot \mu(\mathbf{a}^{g}) \big),
$$

where $\ell$ is the logarithm and $\mu(a)=a/a_0$ is the expected likelihood. The paper uses the bounded form for communication and says that it is the message of belief propagation.

The simulated world (Section 3, Figs. 3 and 4) has three agents seated back to back, each seeing about a third of the horizon, and a subject that stands still or circles them. Each agent models four factors: the location of the subject among nine allocentric positions, its proximity (two levels), its pose (friend or foe) and the agent's own direction of gaze (three levels). There are eight outcome modalities, four visual, one proprioceptive and three auditory, the last with one modality for each of location, proximity and pose. Only the gaze factor is controllable (Fig. 4 caption), so the only action selected by expected free energy is where to look.

### The belief-sharing update and the joint free energy

Outcomes generated by the environment are caused by hidden states that are the same for all agents, whereas the outcomes that carry communication are caused by an agent's beliefs about those states (Section 3.1). The paper first writes belief sharing as if agents exchanged messages directly on a common factor graph. For agent $n$ and a shared factor $f$, Eq. 6 reads

$$
\mathbf{s}^{n,f}_{\tau} = \sigma\Big( \mu^{n,f}_{\uparrow\mathbf{A}} + \mu^{n,f}_{\rightarrow\mathbf{B}} + \mu^{n,f}_{\leftarrow\mathbf{B}} + \sum_{m\in pa(n)} \big( \mu^{m,f}_{\uparrow\mathbf{A}} + \mu^{m,f}_{\rightarrow\mathbf{B}} + \mu^{m,f}_{\leftarrow\mathbf{B}} \big) \Big).
$$

The superscripts $n$ and $m$ index agents, and $pa(n)$ is the set of agents whose beliefs about factor $f$ reach agent $n$; the paper does not define this set in words, and in the simulations it is the other two agents. The sum of an agent's three messages is the logarithm, up to normalization, of the posterior that the agent's own likelihood and prior messages support (Eq. 4). Eq. 6 therefore adds the log posteriors of the other agents to the receiver's own likelihood and prior messages. In terms of distributions, the receiver's belief is the product of its own posterior with the posteriors of the other agents, renormalized, and every agent enters with coefficient one. The paper describes this as the exchange of log posteriors among the agents that share beliefs about the factor.

Eq. 7 presents the update as the stationary point of a joint free energy $F$ over agents:

$$
\begin{aligned}
\frac{\partial F}{\partial \mathbf{s}^{n,f}_{\tau}} &= \frac{\partial}{\partial \mathbf{s}^{n,f}_{\tau}} \Big[ \mathbf{s}^{n,f}_{\tau} \odot \ell\big(\mathbf{s}^{n,f}_{\tau}\big) - \mathbf{s}^{n,f}_{\tau} \odot \sum_{m} \big( \mu^{m,f}_{\uparrow\mathbf{A}} + \mu^{m,f}_{\rightarrow\mathbf{B}} + \mu^{m,f}_{\leftarrow\mathbf{B}} \big) \Big] = 0 \\
&\Rightarrow \ell\big(\mathbf{s}^{n,f}_{\tau}\big) = \sum_{m} \big( \mu^{m,f}_{\uparrow\mathbf{A}} + \mu^{m,f}_{\rightarrow\mathbf{B}} + \mu^{m,f}_{\leftarrow\mathbf{B}} \big) \\
&\Rightarrow \mathbf{s}^{n,f}_{\tau} = \sigma\Big( \mu^{n,f}_{\uparrow\mathbf{A}} + \mu^{n,f}_{\rightarrow\mathbf{B}} + \mu^{n,f}_{\leftarrow\mathbf{B}} + \sum_{m\in pa(n)} \big( \mu^{m,f}_{\uparrow\mathbf{A}} + \mu^{m,f}_{\rightarrow\mathbf{B}} + \mu^{m,f}_{\leftarrow\mathbf{B}} \big) \Big).
\end{aligned}
$$

The bracket holds the terms of $F$ that depend on agent $n$'s expectation: its negative entropy, and minus its inner product with the summed messages of the agents. The claim attached to the equation is that federated inference of this kind brings the agents to the posterior that minimizes the joint free energy, where the gradients vanish.

> [!note] Editorial: Eq. 7 is the only place where the joint free energy is written, and only the terms that depend on $\mathbf{s}^{n,f}_{\tau}$ are printed. The sum over $m$ in the first two lines carries no index set, and the last line splits it into agent $n$ and the agents in $pa(n)$. The derivative of $\mathbf{s}\odot\ell(\mathbf{s})$ contributes a constant vector of ones that the printed second line omits; the softmax normalization absorbs it, so the conclusion is unaffected. The paper does not write $F$ in full and gives no convergence argument for simultaneous updates by all agents. A later footnote (footnote 10) says that the total free energy is the sum of local free energies.

The paper states that this update is formally distinct from Bayesian belief updating. Bayesian updating assimilates the likelihoods of conditionally independent observations, and it would leave agents with different posteriors that depend on their priors. Belief sharing assimilates posteriors, so that each agent inherits both the likelihoods and the priors of the others and the agents reach a consensus, which the paper likens to a "hive mind" (text after Eq. 7). The distinction is offered as a description of the form of Eqs. 6 and 7 and has no separate proof.

Beliefs are shared only when they concern the same states of the world under a shared frame of reference, a condition for which the paper cites [[fields-2022-neurons-as-hierarchies-of-quantum-reference-frames]]. In the model the location, proximity and pose of the subject are shared, and the direction in which each agent looks is private.

### Why sharing must pass through observations

The paper then argues that the direct exchange of Eq. 6 cannot be the mechanism for distinct agents. Federated inference defined as the direct assimilation of other agents' messages "dissolves the notion of an individual agent" (text after Eq. 7), because an agent is defined by its [[Markov Blanket|Markov blanket]] and the blanket precludes reciprocal message passing with other agents. If two agents are to be individuated, neither can be a parent or a child of the other in the graph, so they cannot pass messages to each other directly. To keep the agents conditionally independent, they must communicate through a blanket that they hold in common, which is their observations. The argument is verbal, with citations to the Markov blanket literature (among them [[heins-2023-spin-glass-active-inference]]), and its conclusion is that individuated agents need a likelihood mapping from beliefs to observations that can be exchanged. The paper associates this exchange of sufficient statistics with communication in general and with language in particular.

Each agent is therefore given an outcome modality for each shareable factor, and Eq. 8 shows that the direct update is recovered when the likelihood of that modality is the identity:

$$
\begin{aligned}
\mu^{n,f}_{\uparrow\mathbf{A}} &= \ell\big( \mathbf{o}^{n,f}_{\tau} \odot \mu(\mathbf{a}^{f}) \big), \\
\ell\big( \mathbf{o}^{n,f}_{\tau} \big) &= \sum_{m\in pa(n)} \ell\big( \mu(\mathbf{a}^{f}) \odot \mathbf{s}^{m,f}_{\tau} \big) \\
\Rightarrow \mu^{n,f}_{\uparrow\mathbf{A}} &= \sum_{m\in pa(n)} \ell\big( \mathbf{s}^{m,f}_{\tau} \big) : \mu(\mathbf{a}^{f}) = \mathbf{I}^{f} \\
&= \sum_{m\in pa(n)} \big( \mu^{m,f}_{\uparrow\mathbf{A}} + \mu^{m,f}_{\rightarrow\mathbf{B}} + \mu^{m,f}_{\leftarrow\mathbf{B}} \big).
\end{aligned}
$$

Here $\mathbf{o}^{n,f}_{\tau}$ is the outcome that agent $n$ hears in the modality attached to factor $f$, $\mathbf{a}^{f}$ holds the Dirichlet counts of that auditory likelihood and $\mu(\mathbf{a}^{f})$ is its expected likelihood matrix. The first line is the bounded likelihood message of Eq. 5. The second line says that the logarithm of the heard outcome is the sum, over the other agents, of the logarithm of the outcome that each of them predicts from its posterior. The colon in the third line introduces the condition under which that line holds: when the expected likelihood is the identity matrix $\mathbf{I}^{f}$, the ascending auditory message is the sum of the other agents' log posteriors, which is the peer term of Eq. 6. The listener treats what it hears as an observation, and the result is formally the direct update. The paper adds that the likelihood can be any permutation matrix, a statement it illustrates later by the code that emerges in Section 5, and that the tensors for broadcasting are matrices that tie one outcome modality to one hidden factor.

> [!note] Editorial: The text after Eq. 8 says that each agent hears a probabilistic mixture of the outputs of the others, while the second line of Eq. 8 sets the logarithm of the heard outcome equal to a sum of logarithms, which makes the heard outcome an elementwise product of the speakers' predicted outcome distributions. The paper does not say whether that product is normalized before it is supplied as an observation. For a likelihood matrix that is neither the identity nor a permutation, the reduction to a sum of log posteriors does not hold in general.

### What is communicated and when

In the simulations communication follows Eq. 8. Each kind of belief is sent in its own auditory modality, and the outcome is a probability distribution over the levels of the factor in place of a one-hot vector (footnote 6). A broadcast therefore carries the sender's confidence along with the content: an uncertain agent contributes a flat distribution, which changes little, and an agent with a precise belief dominates what the others hear. Speaking is a readout of the posterior and is not a selected action. The paper names two alternatives that it does not use, a lower hierarchical level that would turn beliefs into word sequences, and the sampling of a token in proportion to the negative expected free energy of communicative acts (the latter with a citation to [[albarracin-2022-epistemic-communities]]).

Agents do not hear themselves. The paper says that this precludes double counting of an agent's own log posterior, with a pointer to Jardri and Deneve (2013) on circular inference, and that it can be read neurobiologically as [[Sensory attenuation|sensory attenuation]] of self-generated sensations. There is no turn taking and no attribution of agency; the paper contrasts this with turn-taking models such as [[friston-frith-2015-hermeneutics]] and imagines the sentinels reporting continuously. Because the environment generates observations and the agents broadcast at the same moment, a broadcast belief rests on the observations of the previous time step. What is communicated is therefore a posterior predictive distribution over the latent states, and its accuracy depends on the transitions the sender has inferred, for example the direction in which the subject moves (Section 3.1, final paragraph).

### Learning the communication code

Section 4 treats the acquisition of the auditory likelihood as active learning. The candidate update of the Dirichlet counts after an observation is the outer product $\Delta\mathbf{a}=\mathbf{o}_{\tau}\otimes_{i\in pa}\mathbf{s}^{i}_{\tau}$ (Eq. 9), and the agent chooses between two policies, to leave the counts as they are ($u_0$) or to apply the update ($u_1$). The prior over the two policies is a softmax of the expected free energy of the counts that would result (Eq. 10),

$$
P(u) = \sigma\big( -\alpha \cdot G(\mathbf{a} \mid u) \big),
$$

with

$$
G(\mathbf{a}) = -\mathbb{E}_{Q_a}\big[ D_{KL}[ Q(s,o \mid \mathbf{a}) \| Q(s \mid \mathbf{a}) P(o \mid \mathbf{a}) ] \big] - \mathbb{E}_{Q_a}\big[ \ln P(o \mid c) \big],
$$

so that $G$ is minus the mutual information between states and outcomes encoded by the counts, minus the expected log preference for outcomes, and $\alpha$ is a precision. The learning rule is the Bayesian model average over the two policies (Eq. 11),

$$
\mathbf{a}^{g}_{\tau+1} = \mathbf{a}^{g}_{\tau} + P(u_1) \Delta\mathbf{a}^{g}_{\tau},
$$

and a forgetting factor caps the total count (Eq. 12),

$$
\mathbf{a}^{g}_{\tau+1} = \big( \mathbf{a}^{g}_{\tau} + P(u_1) \Delta\mathbf{a}^{g}_{\tau} \big) \Big( \frac{\eta}{\eta + P(u_1)} \Big).
$$

Since each candidate update sums to one, the total count stops changing once it equals $\eta$, which the paper reads as a hyperprior for Bayes-optimal forgetting in a changing world. An update is thus applied in proportion to the mutual information it is expected to add, and counts older than about $\eta$ observations fade. The closed tensor form of $G$ in Eq. 10 and the optimality claim for the forgetting factor are stated without derivation. The simulations set $\eta=32$; the paper gives no value for $\alpha$.

### Structure learning and selection

Section 5 moves from posteriors over parameters to priors over parameters. Bayesian model reduction scores a reduced prior against the full one after the data have been assimilated. With $\mathrm{B}$ the beta function, bold $\mathbf{a}$ the posterior counts, $a$ the prior counts and $a'$ the prior counts of the reduced model, Eq. 13 gives the change in free energy as

$$
\Delta F = \ln P(o \mid a) - \ln P(o \mid a') = \ln \mathrm{B}(\mathbf{a}) + \ln \mathrm{B}(a') - \ln \mathrm{B}(a) - \ln \mathrm{B}(\mathbf{a} + a' - a),
$$

with reduced posterior $\mathbf{a}'=\mathbf{a}+a'-a$; the paper cites Friston, Parr and Zeidman (2018) for the result and shows no steps. The space of reduced priors is explored by what the paper calls active model selection. A candidate prior $\hat a$ is formed by a unit step of the logarithm of the current prior counts down the gradient of $G$ with respect to the log counts, $\ell(\hat a)=\ell(a)-\partial G/\partial \ell(a)$, which the paper describes as new log priors that decrease expected free energy by one natural unit (Eq. 14), and old and candidate priors are then averaged with the weights of Eq. 15,

$$
P(u) = \sigma\big( -\alpha \cdot F(u) \big) \text{ with } F(u) = [0, \Delta F],
$$

so that the candidate gains weight when the reduced prior has the greater evidence. The paper states that learning and selection complement each other: posterior counts change to lower variational free energy if, and only if, expected free energy is reduced, and prior counts change to lower expected free energy if, and only if, variational free energy is reduced, as scored by Bayesian model reduction. It also states that this selection is guaranteed to find structures with precise mappings. That statement is asserted as a consequence of Eqs. 14 and 15 and has no proof.

### What the simulations show

All results are simulations of the three-agent world. The figures display single runs, and the paper reports no statistics over repeated random initializations.

In Section 3.2 the subject starts at the first location and circles the agents for eight time steps, once with communication and once with the auditory likelihoods made imprecise. With communication the second and third agents adopt the first agent's broadcast predictions before they see the subject themselves; without it the third agent holds a precise belief about location only from the fifth time step (Fig. 5). The free-energy differences favor communication with one exception, the first agent at the third time step. Gaze follows the inferred location and is driven by the information-gain term of expected free energy. Simulated electrophysiological responses for the third agent show larger belief updates when the broadcasts can be used (Fig. 6).

In Section 4.1 a child agent with uniform auditory counts sees and hears what her parent does. Over 32 episodes of 16 time steps her three auditory mappings approach the identity, the divergence from the parent's mappings falls and the mutual information of the mappings rises (Fig. 7). When each child then replaces her parent and the next parent receives a new child, the mappings of the final generation are almost the same as the original ones, with slightly imprecise mappings for proximity and pose (Fig. 8). No child's priors or structure encoded the parents' language.

In Section 5 all auditory counts start at one plus the absolute value of a Gaussian random number, and three agents run for 512 episodes with active learning and active selection. A sparse mapping emerges that is nearly the same in all three agents by about 128 episodes, and the mutual information of the location mapping saturates near two nats (Fig. 9). The emergent code assigns words to states differently from the identity code of the earlier sections, so an agent from this run could not communicate with one from the earlier runs, and it reports two of the nine locations with the same word. The paper attributes the convergence to selection by Bayesian model reduction; it reports no run of the same simulation without the selection step. In Section 5.2 an agent with intact auditory mappings and untrained visual mappings learns a visual likelihood that makes her inferences indistinguishable from those of the others in about 64 episodes when she can hear them, and does not reach that level in 512 episodes when she cannot (Fig. 11).

### Limits stated by the paper

The paper names several restrictions. The agents' generative models have a common allocentric frame for location; the paper says that egocentric frames with agent-specific likelihood mappings should work in principle and does not simulate them (end of Section 5). Communication is auditory, synchronous and continuous, with no turn taking; the agents do not move; and what is exchanged is a full probability vector for each factor, with no token sequences. The acquisition simulations assume that a language already exists, and all runs are small, about two minutes of simulated time for Section 4. Section 6.3 adds that belief sharing needs a channel that preserves the integrity of the broadcast outcomes. Section 6.6 notes that fixed points of individual free energies need not coincide with fixed points of a group free energy, citing [[heins-2023-spin-glass-active-inference]], and leaves open how agents should update their models to minimize collective as opposed to individual free energy. Whether communication and growing structural complexity arise in any loosely coupled system with identifiable subsystems is posed as a question for larger simulations (Section 6.1), and Section 6.8 says that the analysis stops short of linguistics. The remarks on privacy in Section 6.3 and on a duality between communication and space in Section 6.2 are interpretations without analysis or simulation.

## In this work

The comparisons in this section are made on this page. The paper does not make them, and each is marked as editorial.

> [!note] Editorial: Relation to the transported peer-KL energy. The immutable note [[friston-2024-federated-inference]] calls the coupling $\sum_{ij}\beta_{ij}D_{\mathrm{KL}}(q_i\|\Omega_{ij\#}q_j)$ of [[Multi-agent variational free energy]] federated inference written as one functional, and it presents federated inference as the flat-connection case $\Omega_{ij}=I$. The wiki has already withdrawn that reading in [[Collective active inference]], and the full text supports the withdrawal.
>
> The update of Eq. 6 is a sum of log posteriors with unit coefficients, that is, a renormalized product of the agents' posteriors over a factor that all agents represent in one frame. Let $r_m$ denote the normalized exponential of agent $m$'s own messages and let $M$ be the number of agents in the sum of Eq. 7, the receiver included. Up to a constant, the bracket of Eq. 7 is
>
> $$
> -H[\mathbf{s}] - \sum_{m} \mathbb{E}_{\mathbf{s}}[\ln r_m] = \sum_{m} D_{\mathrm{KL}}[\mathbf{s} \| r_m] + (M-1) H[\mathbf{s}],
> $$
>
> where $H$ is the Shannon entropy; the identity is the definition of the relative entropy applied $M$ times. The federated functional therefore differs from a sum of unit-weight divergences to the agents' posteriors by $M-1$ entropies of the receiver. Its minimizer is the renormalized product $\prod_m r_m$, which sharpens as agents are added, whereas a weighted sum of divergences alone is minimized by the geometric pool $\prod_m r_m^{w_m/\sum_k w_k}$ recorded in [[Probabilistic opinion pooling]], whose exponents sum to one. The same holds for the receiver-side stationarity of the gauge energy at fixed peers and fixed weights, leaving aside the terms in which the receiver's belief is the reference density of another agent's divergence: the self terms and the peer terms give a geometric pool of the receiver's prior and the transported peer beliefs with exponents that sum to one. Setting $\Omega_{ij}=I$ and $\beta_{ij}=1$ does not turn one functional into the other.
>
> A reduction would need all of the following to be matched: a common frame for the shared factors, which the paper assumes and the gauge model replaces by transport; unit coefficients for every speaker, where the gauge model has optimized attention rows with an entropy term; the entropy accounting above, in which a peer enters as a likelihood factor (a cross-entropy term) where the gauge energy has a divergence; the object that is compared, which in the paper is a posterior predictive broadcast read through a declared likelihood; the variational family, which in the paper is categorical with Dirichlet-distributed likelihoods; and a treatment of evidence that the agents hold in common. [[Multi-agent variational free energy]] records that the social block is an engineered consensus energy whose exact generative reading exists only on an enlarged inventory with a source label. On the evidence of this paper, federated inference is a comparator with a declared message likelihood, and neither construction is a special case of the other.

> [!note] Editorial: Relation to the collective-agents manuscript. That manuscript defines interpretation levels for a receiver and calls a reading literal when the receiver models a message as conditionally independent of its own information given the state of the world. The paper's receivers fit this definition. A broadcast posterior enters the listener's model as an outcome of the shared factor through an identity or permutation likelihood, and the listener assimilates it by the ascending likelihood message of Eq. 8, in the same way as a visual observation. The manuscript first made this classification with the qualification that it knew the paper through its abstract and secondary accounts, and it now makes it from the full text. Section 3.1 and Eq. 8 of the full text support it, with the refinement that what is read as an observation is a full posterior predictive distribution, so the sender's stated confidence is taken at face value.
>
> The paper excludes an agent's own broadcast from what the agent hears and says that this precludes double counting of the agent's own log posterior. That removes the direct self term. The paper does not discuss evidence that returns through other agents across rounds. As the scheme is described, agent $m$'s broadcast at time $\tau$ is a prediction built on its belief at $\tau-1$, which had assimilated agent $n$'s broadcast at $\tau-1$, and agent $n$'s own forward message at $\tau$ carries the same earlier evidence. The update of Eq. 6 also adds each agent's prior messages, so the prior messages computed from the common transition model enter once per agent; the paper affirms that agents inherit priors as well as likelihoods and applies no correction of the kind written in [[Decentralized Bayesian inference]]. These are observations about what the paper does not address. They are not results of the paper, which contains no analysis or simulation that isolates recirculated evidence and whose demonstrations use agents with complementary fields of view. [[catal-2025-belief-sharing-blessing]], a later paper read in the vault only through its abstract and introduction, argues that sharing posteriors in this way produces echo chambers and proposes sharing likelihoods.

> [!note] Editorial: Frames, codes and weights. The freedom that the paper finds in the code is a permutation of the words of one auditory modality, fixed by learning to be the same for all agents, and it acts on outcome labels. It is a different object from the transport $\Omega_{ij}$ between agents' belief frames in the gauge model ([[Gauge transformation]]), for which the paper's assumed allocentric frame leaves no role. The paper's remark that egocentric frames with agent-specific likelihood mappings should work is the nearest point of contact and is not developed. The paper has no partner selection and no [[Precision weighting|precision weighting]] of sources beyond what the broadcast distributions carry: every speaker has coefficient one, and a speaker's influence is set by how concentrated its broadcast is. The description in the belief-inertia manuscript, that federated inference treats communicated posteriors as evidence for a shared model and supplies no transport between frames, agrees with the full text. [[Active inference communication and collective boundaries]] places the paper beside models in which expression or the choice of partner is a policy.

The pages [[Collective active inference]], [[Multi-agent variational free energy]], [[Decentralized Bayesian inference]], [[Markov Blanket]], [[Active inference communication and collective boundaries]] and [[Chris Fields and physics as communication]] carry sections dated November 13, 2026 that point here.

## Sources

- [[friston-2024-federated-inference]]: source note for Friston, Parr, Heins, Constant, Friedman, Isomura, Fields, Verbelen, Ramstead, Clippinger and Frith (2024), Neuroscience and Biobehavioral Reviews 156, 105500, open access under CC BY. This page was written from the [published PDF](../../sources/pdfs/friston2024federated.pdf). The relevance section of the note is superseded by the first editorial note above.
- [[fields-2022-neurons-as-hierarchies-of-quantum-reference-frames]]: cited by the paper for the shared frame of reference under which beliefs are shared.
- [[fields-2022-a-free-energy-principle-for-generic-quantum-systems]]: cited by the paper, as a 2021 preprint, for self-evidencing and for the frame-of-reference reading of common ground.
- [[heins-2023-spin-glass-active-inference]]: cited for blankets that preclude reciprocal message passing and for individual versus group fixed points.
- [[albarracin-2022-epistemic-communities]]: cited for communicative acts sampled by expected free energy, an alternative the paper does not use.
- [[friston-frith-2015-hermeneutics]]: cited as a turn-taking model of communication.
- [[kaufmann-2021-active-inference-model]]: cited for endogenous alignment of agents' free-energy minima.
- [[constant-2019-regimes-expectations-active]] and [[veissiere-2020-thinking-through-other]]: cited for shared worlds and cultural niche construction.
- [[catal-2025-belief-sharing-blessing]]: later comparator on sharing posteriors versus sharing likelihoods; not cited by the paper.

## See also

- [[Collective active inference]]
- [[Multi-agent variational free energy]]
- [[Decentralized Bayesian inference]]
- [[Probabilistic opinion pooling]]
- [[Markov Blanket]]
- [[Expected Free Energy]]
- [[Sensory attenuation]]
- [[Quantum reference frames]]
- [[Echo chambers and polarization]]
- [[Cultural evolution and social learning]]
- [[Active inference communication and collective boundaries]]
- [[Chris Fields and physics as communication]]
- [[Collective agents literature map]]
- [[friston-2024-supervised-structure-learning]]: a separate paper on structure learning with expected-free-energy model priors, not cited by this one.
