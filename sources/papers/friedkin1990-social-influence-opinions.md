---
type: paper
title: "Social Influence and Opinions"
aliases:
  - Friedkin Johnsen 1990
  - Friedkin-Johnsen model
  - FJ model
  - friedkin-johnsen-1990
  - Friedkin 1990
  - Friedkin & Johnsen 1990
authors:
  - Friedkin, Noah E
  - Johnsen, Eugene C
year: 1990
arxiv: null
url: https://doi.org/10.1080/0022250x.1990.9990069
tags:
  - cluster/social-physics/opinion-dynamics
  - cluster/social-physics/social-influence
  - cluster/social-physics/networks-and-contagion
  - project/social-physics
  - project/multi-agent
  - field/sociology
  - field/mathematics
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Social Influence and Opinions

> [!info] Citation
> Friedkin, Noah E. and Johnsen, Eugene C. (1990). "Social Influence and Opinions." *Journal of Mathematical Sociology*, 15(3-4), pp. 193-205. https://doi.org/10.1080/0022250x.1990.9990069

## TL;DR
Friedkin and Johnsen derive the foundational Friedkin-Johnsen (FJ) model of opinion dynamics from elementary process assumptions about iterative interpersonal influence. They show that the equilibrium $Y_\infty = [I - \alpha W]^{-1} \beta X B$ unifies a large family of prior social influence models (French, DeGroot, peer effects, linear discrepancy) as special cases, and demonstrate that the same model is consistent with both social conformity and persistent social conflict, showing the distinction between these two research traditions to be artificial.

## Problem & setting
The paper addresses how a network of interpersonal influences shapes the content of individuals' opinions. Prior work (Duncan et al. 1971, Doreian 1981, Erbring and Young 1979) had treated the equilibrium model $Y = WY + XB + U$ empirically, without grounding it in a principled theory of process or exploring its deducible implications. The paper seeks to provide that theoretical foundation and to unify the scattered literature on social conformity and conflict.

## Method
Starting from a network paradigm with three foundational assumptions — determinism (opinions are fully accounted for by causal variables), decomposability (the process unfolds in discrete periods governed by simultaneous linear equations), and continuance (the process runs until opinions settle) — the authors derive the basic social influence model. For fixed conditions, the iterative process

$$Y_t = \alpha W Y_{t-1} + \beta X B, \quad t = 2, 3, \ldots$$

with $Y_1 = XB$, converges when $|\alpha| < 1$ and $|W^k| < mJ$ for some constant $m > 0$, yielding the reduced-form equilibrium

$$Y_\infty = [I - \alpha W]^{-1} \beta Y_1 = [I - \alpha W]^{-1} \beta X B.$$

Here $W$ is the $n \times n$ interpersonal influence matrix, $\alpha$ weights endogenous (social) influences, $\beta$ weights exogenous conditions, and $X B$ encodes initial opinions from exogenous variables. The paper then derives the total-influence matrix $V = [I - \alpha W]^{-1} \beta$, whose row-$i$ entries $v_{ij}$ give the total (direct plus indirect) relative effect of member $j$ on member $i$'s final opinion. Individual settled opinions are

$$y_{i\infty} = \delta[(1 - v_{ii})m + v_{ii} y_i] + \delta \sum_{j \neq i} v_{ij}(y_j - m),$$

where $m$ is the mean of other members' initial opinions. The authors prove a convergence theorem (Appendix) showing $\lim_{\alpha \to 1^-} (1-\alpha)(I - \alpha W)^{-1} = W^\infty$ for stochastic $W$, connecting the basic model to French/Harary/DeGroot consensus models.

## Key results
The equilibrium model $Y_\infty = [I - \alpha W]^{-1} \beta X B$ subsumes as special cases: (1) the linear discrepancy model (change is proportional to the opinion gap between two actors); (2) the peer effects model (mean opinion of direct influencers predicts individual outcome); (3) the group consensus models of French (1956), Harary (1959), and DeGroot (1974), recovered in the limit $\alpha \to 1^-$. The decomposition of $y_{i\infty}$ into a conformity term (weighted average of $i$'s initial opinion and the group mean) and a conflict term (weighted sum of deviations from the mean) shows that a single model simultaneously generates conformity and conflict dynamics depending on the variance of initial opinions and the structure of $W$ — these are not competing processes requiring separate theories.

## Relevance to this research
The Friedkin-Johnsen model is structurally analogous to iterative belief-updating in the VFE transformer: the weight matrix $W$ parallels the attention matrix $\beta_{ij}$ (normalized influence weights between agents/tokens), and the equilibrium $Y_\infty = [I - \alpha W]^{-1} \beta Y_1$ mirrors the fixed-point structure of VFE E-step iterations where beliefs $\mu_i$ are updated as weighted combinations of neighbor beliefs transported via $\Omega_{ij}$. In the multi-agent active inference setting, the $\alpha$/$\beta$ decomposition (endogenous vs. exogenous weight) corresponds to the self-coupling $\alpha \cdot \mathrm{KL}(q_i \| p_i)$ and observation likelihood terms in the free energy functional. The FJ convergence theorem (stochastic $W$, $|\alpha|<1$ implies unique equilibrium) gives a classical precedent for the convergence analysis of the VFE message-passing dynamics. The peer-effects cautionary note — that a noteworthy effect of the mean of influential opinions does not imply conformance to a norm — is relevant to interpreting softmax attention averages in the GL(K) attention mechanism.

In the equivalent *susceptibility form* of the model, each agent updates as $y_i \leftarrow \lambda_i \sum_j W_{ij}\, y_j + (1-\lambda_i)\, y_i^{(0)}$, where the anchoring term $(1-\lambda_i)\,y_i^{(0)}$ encodes a stubbornness/attachment to the agent's own initial opinion. This fixed anchoring is the sociological precursor to the project's [[Belief inertia]]: where Friedkin–Johnsen impose a constant susceptibility $\lambda_i$, the project recasts the resistance to belief change geometrically as [[Mass as Fisher information]] (curvature of the local statistical manifold via the [[Fisher information metric]]). The model thus serves as the flat, no-gauge-curvature limit against which the gauge-theoretic extension — beliefs as [[Agents as fibre-bundle sections]] propagated by [[Parallel transport]] — is positioned, situating the project within the [[Renormalization-group flow of beliefs]] and [[Meta-agents and hierarchical emergence]] picture.

> [!note] Editorial: the exact parameterization (agent-specific vs. scalar $\lambda$, and the precise normalization of $W$) varies across presentations; the susceptibility form above follows the standard linear influence-process reading of the 1990 paper.

## Cross-links
- Concepts: [[Opinion Dynamics]], [[friedkin-johnsen-2011-social-influence-network|Social Influence Networks]], [[Belief Propagation]], [[Attention Mechanism]]
- Related sources: [[degroot-1974-consensus|degroot1974-reaching-consensus]], [[french-1956-formal-theory-social-power|french1956-formal-theory-social-power]]
- Manuscript/Project: [[VFE Transformer Program]], [[Collective active inference|Multi-Agent Active Inference]]

## BibTeX
```bibtex
@article{friedkin1990,
  author  = {Friedkin, Noah E. and Johnsen, Eugene C.},
  title   = {Social Influence and Opinions},
  journal = {Journal of Mathematical Sociology},
  year    = {1990},
  volume  = {15},
  number  = {3-4},
  pages   = {193--205},
  doi     = {10.1080/0022250x.1990.9990069},
}
```
