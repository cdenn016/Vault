<!-- rigorous-theory-search-metadata {"schema_version":"rigorous-theory-search/v1","contract_id":"contract-sha256-cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e","target_digest":"cde4ab884a8d0a0dcd5187eadc4d2c23c79b2c04306227f230e9b12b59f8cf4e"} -->

# Analytic finite-time behavior and the meaning of selection

This lemma separates selecting an available exact quotient from dynamically creating a new future-response equivalence. It does not exclude state-dependent hierarchy selection, and it does not apply to all smooth channels in the frozen target.

Let \(M\) be a real-analytic manifold, \(V\) an analytic vector field with local flow \(\Phi_t\), and \(\mathcal H\) a family of analytic real-valued test functions for a declared observation protocol. A test function may be a finite-cylinder response probability, provided its analyticity is actually established. Assume that waiting is admitted: \(h\circ\Phi_s\) is also an admitted test for every nonnegative waiting time on the common domain. Work on a connected interval of common existence containing the times in the argument. Every fixed test used below must remain analytic along both trajectories on that interval.

Define \(x\sim y\) when all admitted future tests agree. If \(x\sim y\), waiting closure immediately gives \(\Phi_t x\sim\Phi_t y\) for any admitted finite \(t\ge0\). Conversely, suppose \(\Phi_t x\sim\Phi_t y\). For every \(h\in\mathcal H\), waiting closure gives
\[
h(\Phi_{t+s}x)-h(\Phi_{t+s}y)=0
\]
for an open interval of nonnegative \(s\). The left side is analytic in \(t+s\). The one-variable identity theorem extends zero throughout the connected common interval, in particular to time zero. This holds for every \(h\), hence \(x\sim y\).

The same argument applies to the observable annihilator
\[
N_x=\{v\in T_xM:dh_x(v)=0\text{ for every completed future test }h\}.
\]
For \(v\in T_xM\), the function \(s\mapsto d(h\circ\Phi_s)_x(v)\) is analytic. Forward waiting closure and backward analytic continuation therefore give
\[
D\Phi_t(N_x)=N_{\Phi_t x}
\]
on the same common domains. This equality uses the invertibility of the local flow map; it does not assume a globally complete flow. No smooth quotient manifold or constant-rank theorem follows without further hypotheses.

Thus an analytic regular system with one fixed waiting-closed analytic protocol does not acquire a new future-behavior equivalence at a finite interior time along its invertible flow. A membership rule may nevertheless select a quotient that was already mathematically available. Changing the protocol, reaching an infinite-time limit or a singular stratum, or leaving the analytic category is outside the conclusion.

Analyticity is substantive. On \(\mathbb R^2\), take \(\dot x=1,\dot y=0\) and the smooth output \(h(x,y)=b(x)y\), where \(b(x)=\exp(-1/x^2)\) for \(x<0\) and \(b(x)=0\) for \(x\ge0\). Two states with the same negative \(x\) and different \(y\) initially have different outputs but become future-output equivalent after crossing zero. This is a counterexample to extending the lemma to arbitrary smooth outputs. It is deliberately not an admissible formation witness for this task, because its flat output function is an imposed erasure gate.

The Wishart hierarchy studied in this run selects exact additive quotients using a declared threshold criterion. Those quotients already exist before the events. Its finite-time joins should not be described as annihilation of new distinctions by the fine dynamics.

Related source: Horstmeyer and Atay, [Characterization of Exact Lumpability for Vector Fields on Smooth Manifolds](https://arxiv.org/html/1607.01237), Proposition 1, identifies local smooth descent with \(DR V=\bar V\circ R\). The proof here uses only local flow uniqueness and elementary analytic continuation; it does not import a global lifetime assertion or the stronger control-theoretic realization theorems.

