# Common-principal-bundle revision plan

## Mathematical contract

The ambient theory has one principal bundle \(\pi:P\to\mathcal C\) with structure group \(G\).  Belief and model laws inhabit the associated bundles
\[
\mathcal E_b=P\times_{\widehat\rho_b}\mathcal B_b,
\qquad
\mathcal E_m=P\times_{\widehat\rho_m}\mathcal B_m,
\]
where \(\rho_b\) and \(\rho_m\) may be inequivalent representations and may act on different-dimensional fibers.

Two local sections \(u_i^b,u_i^m:\mathcal C_i\to P\) determine a unique relative principal-frame field \(h_i:\mathcal C_i\to G\) by \(u_i^m=u_i^b h_i\).  This statement is representation-independent.  It does not supply a map between the associated fibers: \(\Phi:\mathcal E_b\to\mathcal E_m\) and \(\widetilde\Phi:\mathcal E_m\to\mathcal E_b\) are additional equivariant bundle morphisms and need not be inverses.

The same principal bundle may carry two connections \(\omega_b,\omega_m\), inducing distinct represented transports \(\Omega\) and \(\widetilde\Omega\).  A common frame and an equal connection are separate, stronger specializations.  Independent principal bundles with product gauge group \(G_b\times G_m\) are retained only as an optional extension.

## Execution

1. Rewrite the foundational geometry and levelwise RG state using the contract above.
2. Propagate it through the introduction, general generative theory, Gaussian realization, coarse-graining, notation appendix, claim ledger, and specification.
3. Remove stale statements that treat product gauge symmetry, two Cech classes, or common-frame assumptions as ambient.
4. Rebuild the PDF; check references, citations, labels, typography, and visual layout; run the numerical verification suite.
5. Record a derivation-backed verification claim and bind the ledger to the final source revision.

## Closure criteria

- No unexplained \(P_b,P_m,G_b,G_m\) notation remains outside the optional product-gauge extension or unrelated Gaussian precision symbols.
- The text distinguishes principal relative frames, represented frame operators, and cross-fiber intertwiners.
- General RG precedes the multivariate-Gaussian realization and uses one \(P_\ell\) at every scale.
- The compiled PDF contains no unresolved citation/reference markers and passes the numerical and ledger validators.
