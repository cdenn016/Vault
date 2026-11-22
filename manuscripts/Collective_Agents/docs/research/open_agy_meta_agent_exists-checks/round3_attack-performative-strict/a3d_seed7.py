r"""a3d: the candidate's declared decision-state set (300 draws, numpy seed 7, from the
stationary law of the act means) rebuilt from MY act-mean covariance; and the
negative-control tie tolerance of a5.
Declared expectation: if my act-mean covariance equals the candidate's, the
seed-7 set reproduces index 0.2772 and mean KL(P||E) 1.474; otherwise it does not."""
import io, contextlib
import numpy as np
with contextlib.redirect_stdout(io.StringIO()):
    import a3b_agency_variants as V
Vv = np.vstack([V.zb, V.zs])
Cmu = V.kap ** 2 * (Vv @ V.SYX @ Vv.T)
print("my act-mean covariance Cmu =\n", Cmu)
MU = np.random.default_rng(7).multivariate_normal(np.zeros(2), 0.5 * (Cmu + Cmu.T), size=300)
idx, den = V.idx_sample(MU)
print("seed-7 300-state set on my Cmu: index %.4f, mean KL(P||E) %.4f (candidate: 0.2772, 1.474)" % (idx, den))
