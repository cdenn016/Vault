---
type: manuscript
title: "MultiAgentELBO exact Gaussian source moment bounds, October 3, 2026"
aliases: ["Exact Gaussian source moment transfer limits"]
authors: ["MultiAgentELBO project"]
year: 2026
tags: [cluster/multi-agent, cluster/info-geometry, cluster/vfe, project/multi-agent, field/mathematics, field/statistics]
created: 2026-10-03
---

# Exact Gaussian source moment bounds

MultiAgentELBO project (2026). *Exact Gaussian source moments: sharp growth bound and transfer limits*. Code commit [56f73c0](https://github.com/cdenn016/MultiAgentELBO/commit/56f73c084ceff3a833e10f257a42799957d24422), [PR 128](https://github.com/cdenn016/MultiAgentELBO/pull/128). Immutable archives retain the [research record](../archives/multiagentelbo-2026-10-03-binary-moment-bounds/research-record.md.txt), [executed scalar script](../archives/multiagentelbo-2026-10-03-binary-moment-bounds/check_scalars.py.txt) and [saved output](../archives/multiagentelbo-2026-10-03-binary-moment-bounds/scalar-checks.json). The method context is Thomas P. Minka, *Expectation Propagation for Approximate Bayesian Inference*, UAI 2001, section 2, equations (4)-(6), [author's corrected paper](https://tminka.github.io/papers/ep/minka-ep-uai.pdf); the archived note derives the bounds independently.

At fixed finite dimension and fixed positive quadratic-softmax logits, exact tilting of a positive-definite Gaussian preserves positive-definite covariance, finite polynomial moments at every state and local smoothness of the update map. Writing M=1+|R| squared+|m| squared+trace(S), the selected physical second moment is at most a fixed-model constant times M squared. An entropy argument proves the bound without an imposed probability floor, and moment matching gives the Gaussian projection Pythagorean identity. Candidate-probability-weighted entropy identities are explicitly distinguished from native weighting.

Two exact scalar counterexamples show why stronger uniform estimates fail. With beta=sigma(y-t squared), incoming variance t squared/2 and retained coordinates (1,t), the selected mean grows like t squared/2 and its second moment like t to the fourth/4. Thus a linear bound, any power below two and a fixed standardized mean-shift constant fail over the declared class. With beta=sigma(y squared-R squared) and incoming variance one, the selected variance grows like R squared, disproving a fixed covariance multiplier. Positive-definite quadratic sheet energies realize both likelihoods. Dominated-convergence arguments establish these limits; one SymPy/SciPy scalar calculation grounds the formulas but is neither a proof of the limits nor network evidence.

## Relevance to this research

The existing cubature integrability proof depends on precisely the two state-independent reset constants that fail here. This does not establish divergence under native histories, reachability in the saved GL(2) runs or an obstruction to formation. The next obligation is a native-probability-weighted Lyapunov or entropy estimate for the reset operator together with the continuous filter generator. Candidate-law estimates cannot be substituted for it. Practical O1 accuracy and O4 remain open. No complete continuous admission extension, production behavior change, model run or GPU job is claimed.

The preceding [[multiagentelbo-2026-10-03-projection-parity-diagnosis]] remains a non-reproduction of an unexplained failure; no failed-study retry occurred. See [[Staged hierarchy formation and RG composability]] and [[Gauge-Theoretic Multi-Agent VFE Model]].
