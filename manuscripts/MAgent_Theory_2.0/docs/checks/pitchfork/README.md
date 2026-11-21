# Pitchfork coefficient check (chapter 18, section it2:ch-critical-mode)

Exact rational recomputation (sympy) of the cubic coefficient of the local pitchfork in
`chapters/18_link_dynamics.tex`, at the declared reference data (dictionary reference precision 3/4).

`pitchfork_check.py` reconstructs the model from eq. `it2:threshold-objective` and computes, in exact
rationals: the base point and gradient `g`, positive definiteness of `H`, `H^{-1} g` and
`T_c = 3269/10118`; the Lyapunov-Schmidt quartic `Phi_ssss(0, T_c)` by order-by-order solution of the
stationary curve and, independently, by the tensor formula `it2:critical-quartic`; the contractions of
`it2:critical-contractions`; the straight-line value (negative control); `D`; and the center-manifold
cubic coefficients of the Gibbs-reduced and full-relaxation flows, which equal `-c/D` and `-c/(D+4)`.
Result: `c = -657534393590529472/6223404588394626861 ~ -0.1056551 < 0` (subcritical); every constant
matches the text. Output: `pitchfork_check_output.txt`.

`control_Pa1.py [Pa]` evaluates `c` and `T_c` by the tensor formula at 40-digit mpmath precision (not
interval validated) for dictionary reference precision `Pa`. `Pa = 3/4` reproduces the exact value;
`Pa = 1` gives `c ~ +0.0229364`, `T_c ~ 0.3190910` (supercritical). Output: `control_output.txt`.
`pitchfork_check_defs.py` holds the model definitions used by the control script.

Commands (run from this folder, single-threaded):

    OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python pitchfork_check.py
    python control_Pa1.py 3/4
    python control_Pa1.py 1

Runtime: about 17 s for `pitchfork_check.py` on one thread; the control runs take a few seconds each.
`pitchfork_check.py` was rerun after copying here and reproduced `pitchfork_check_output.txt` exactly.

Not covered: the center-manifold existence theorem cited, uniformity of the remainder, and the global
claims; the precision-1 supercritical value is numerical only.
