<!-- rigorous-theory-search-metadata {"contract_id":"contract-sha256-b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b","schema_version":"rigorous-theory-search/v1","target_digest":"b6f7aeefd57a2cac70495af4744dd3e3f58dccfe630d6407e3e277f34dac526b"} -->
# Task 5 probability and ELBO adversarial audit

## Attack matrix

| Attack | Target | Witness or check | Outcome |
| --- | --- | --- | --- |
| Moving atoms | One reference measure for a parameter family | (\mu_t=\frac12N(0,1)+\frac12\delta_t) over uncountable (t) | Defeats per-law reference selection; repaired by the exact countable-union iff criterion. |
| Singular-continuous overreach | Claim that Cantor components are intrinsically nondominable | A singleton Cantor law is dominated by itself | Defeats that wording; repaired by requiring a declared common singular reference. |
| Nonmeasurable RN selection | Pointwise density choices imply a kernel density | Modify versions on parameter-dependent null sections using a non-Borel selector | Defeats pointwise selection; repaired by the finite jointly measurable partition-limit version for (K_x\ll L_x). |
| False partition cofinality | One refining generating sequence is cofinal among all finite measurable partitions | Dyadic partitions of ([0,1]) never refine (\{C,C^c\}) for a Borel (C) that is not a finite union of dyadic cells | The cofinality claim is false; repaired by (\Lambda=(\kappa+\eta)/2), conditional expectations, the convex perspective (\Phi), Fatou's lemma, and the log-sum upper bound. |
| Infinite-measure complement step | Rectangle closure extends directly by a monotone-class argument for sigma-finite (\nu) | For counting measure on (\mathbb N), the sets (C_n=\{n,n+1,\ldots\}) decrease to empty while (\nu(C_n)=+\infty) does not decrease to zero | The naive finite-complement/decreasing-limit proof is invalid; repaired by a disjoint finite-measure partition, a (\pi)--(\lambda) proof on each piece, and a countable sum. |
| Singular recognition law | Classical split is the ELBO definition | (Q\not\ll\Pi_o) | Classical expression is unavailable, while the extended ELBO is exactly (-\infty); repaired by defining the measure-level functional first. |
| Infinite-entropy cancellation | Expected complete log likelihood defines parameter acceptance | Countable (q_n\propto[n(\log n)^2]^{-1}) with bounded density tilt | Both expected log likelihoods are (-\infty) while relative-log ELBOs differ; acceptance now uses (\mathcal L^{\rm ext}). |
| Infinite total correlation | Entropy-subtraction proof covers all joints | (Q=\operatorname{law}(U,U)) with uniform (U) | Joint is singular to product marginals and TC is infinite; repaired by finite-partition KL limits. |
| Unsafe extended rearrangement | (\log z=\mathcal L^{\rm ext}+\mathrm{KL}) for all (Q) | Singular (Q) gives (-\infty+\infty) | Formula rejected; only the two finite-constant gap identities remain. |
| Infinite DPI equality | Equality of fine/coarse KL implies recovery without finiteness | Three-point (a,b,c) erasure witness | Both KLs are infinite but no common reverse kernel exists; equality/recovery remains finite-KL only. |
| Exceptional RCP rebinding | An almost-sure identity may be evaluated at an arbitrarily fixed observation | For independent uniform (O,X), both the uniform kernel and the version changed to (\delta_0) at (o=0) are RCPs; their pushed values at (o=0) differ under a nonconstant channel | Repaired by fixing the fine measurable RCP and declaring (\bar P_o:=P_oK) pointwise, then proving that declared kernel is an RCP of the pushed joint. |
| Block-to-evidence overclaim | Any exact block E update plus M acceptance raises evidence | A block conditional replacement need not equal the full posterior | Repaired: block steps raise the common objective; evidence monotonicity requires full old-posterior exactness. |
| Additive incident overcounting | Summing singleton incident objectives reconstructs the collective record energy | For two agents and one record factor (a) with (\partial a=\{1,2\}) and selected energy (E_{a,o}=1), each singleton incident energy is (H_{1,o}=H_{2,o}=1), so their sum is (2) while the collective record energy is (1) | Repaired by counting each actual record once globally. In general, if (H_{i,o}=\sum_{a:i\in\partial a}E_{a,o}), then (\sum_iH_{i,o}=\sum_a|\partial a|E_{a,o}); naïve singleton summation overcounts every multi-agent record by its incidence multiplicity. |
| Observation erasure | Recasting observations as agents removes the environment | Any nontrivial observation kernel has an output sample space and normalization | Only a typed environment-node equivalence is proved; ontology is not erased. |
| Deterministic attention coefficient | (\beta_{ij}) alone is an ELBO recognition law | A fixed coefficient has no categorical sample variable or entropy | Repaired by a normalized latent source label and separate posterior/recognition rows. |
| Extra label-reading record | The displayed source-energy factor alone determines the posterior attention row | Let (J\in\{0,1\}) have prior ((1/2,1/2)) and (D_0=D_1=0), but add a normalized binary record with (P(R=1\mid J=0)=1/4) and (P(R=1\mid J=1)=3/4). Given (R=1), the displayed row is ((1/2,1/2)) while Bayes gives ((1/4,3/4)). | Repaired exactly by the complete augmented-likelihood factorization: (L_o^Y) is label independent and no other record or generative factor reads (J). |

## Reconstruction checks

1. Re-derived common domination in both directions; the necessity uses countability of positive-mass atoms of a sigma-finite measure.
2. Reconstructed the varying-kernel RN density from refining partitions and verified that the infinite-limsup replacement changes only a kernel-null set.
3. Replaced the false finite-partition cofinality step by (a_n=E[a\mid\mathscr G_n]), (b_n=E[b\mid\mathscr G_n]), conditional Jensen for (\Phi(a_n,b_n)), the log-sum upper bound, martingale convergence, and Fatou's lower bound; these force (D_n\uparrow\mathrm{KL}).
4. Localized the fixed sigma-finite integration theorem to disjoint finite-measure pieces, where finite complements make the Dynkin-system proof valid, and summed the measurable section integrals before simple approximation.
5. Re-derived the relative-log ELBO and bounded its negative part by (z/e).
6. Re-derived total correlation first on finite product partitions and then passed through monotone KL limits, so no signed entropy subtraction occurs.
7. Re-derived arbitrary-law DPI with the nonnegative generator (t\log t-t+1), and separately checked the non-AC branch.
8. Checked the coarse evidence theorem by fixing one measurable fine RCP, declaring (\bar P_o=P_oK) at every observation, and verifying its disintegration integral on rectangles before a (\pi)--(\lambda) extension.
9. Checked the repaired local construction from the context-indexed normalized baseline and record kernels, family-level jointly measurable densities, one fixed baseline RCP version, the posterior-full regular set, and the conditional KL chain; exceptional-point formulas are version declarations, not joint-law invariants.
10. Reconstructed additive incident counting exactly: with (H_{i,o}=\sum_{a:i\in\partial a}E_{a,o}), finite-sum interchange gives

    \[
    \sum_iH_{i,o}
    =\sum_i\sum_{a:i\in\partial a}E_{a,o}
    =\sum_a|\partial a|E_{a,o}.
    \]

    Hence the collective energy is (\sum_aE_{a,o}), not the naïve sum of singleton incident energies; equality holds only after explicit multiplicity correction or when every contributing record has singleton scope.
11. Recomputed the attention posterior in the full augmented joint. The exact binary-record witness above changes the row unless the selected complete likelihood is label exclusive; under exclusivity, Bayes cancels every label-free factor, and a general correlated recognition law retains conditional total correlation.
12. Checked that every evidence-ascent chain uses only (\mathcal L^{\rm ext}\le\log z), accepted nondecrease, and equality at the exact old posterior.

## Conclusion

The attacks falsify the broader formulations listed above but not the repaired claims under their declared hypotheses. The probability and extended-ELBO interfaces in the Task 5 source now cover singular laws, infinite KL, infinite total correlation, fixed sigma-finite integration, and kernel-KL measurability without undefined extended arithmetic or false cofinality. Local/observation claims remain conditional on the typed context-indexed normalized joint and fixed regular-conditional versions, and singleton incident objectives are coordinate objectives rather than additive pieces of the collective energy. The attention row additionally requires the full label-exclusive augmented likelihood; the binary extra-record witness proves that this premise cannot be dropped.
