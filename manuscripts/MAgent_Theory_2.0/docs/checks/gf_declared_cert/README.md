# Certificate for the declared instance of chapters/05_global_formation.tex

These scripts certify the classification of the declared instance
(`gf:declared`, `gf:instance`, the controls paragraph after it, and the
`gf:regrouping` remark) at the declared center. Trajectories, inverses,
determinants and quadratic forms use exact rational arithmetic
(`fractions.Fraction`). Log determinants, square roots and exponentials use
`mpmath.iv` interval enclosures at 60 digits, with widths below 1e-55. The
infinite tails are covered by persistence balls (`gf:persistence`), whose
radii are rigorous lower bounds from the bound f0 - |Dc| r - (1/2)|D|_F r^2.

## Files

- `certify_gf.py` certifies the full flow (Pi_perp, Pi_sep, Pi_join; smallest
  gap 0.0141798 at sweep 1), the label-preserving null (same sequence; tail
  ball of radius at least 0.261127 around kappa o), the renormalized null
  (Pi_perp, then Pi_join; gap 0.0397836), the full-flow tail ball (radius at
  least 0.114450 around m*_join, entered at sweep 3), the parent sweep (fixed
  points, self-consistency, and a ball of radius at least 0.627499 around the
  Pi_sep fixed point on which Pi_join is preferred), the exact reproduction (D)
  at sweeps 3 and 4, the posterior masses, and the frozen-environment control
  under (N3) of `inh:null-flow`, with each private copy holding m^0_{-i} in
  both its selection and its update. It also runs the `gf:regrouping`
  selection sequences and a few negative controls. Its output is in
  `certify_gf_output.txt`.
- `regroup_tail.py` (imports `certify_gf.py`) gives the tail balls for the
  `gf:regrouping` data: radius at least 0.3272 for the full flow and at least
  0.0991 for the label-preserving null, both entered at sweep 3. Its output
  is in `regroup_tail_output.txt`.

The fixed-structure contraction factor 0.188 is a floating-point eigenvalue
and is not used by the certificate. The radius of the open set U is not
certified; only its existence follows, by continuity from the strict margins.

The m = 0 negative control prints "unexpected". That label is wrong in the
script: m = 0 is not a tie, because the log determinants differ.

## Commands

Run from this folder (requires `mpmath`):

    OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python certify_gf.py certify_gf_output.txt
    OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python regroup_tail.py > regroup_tail_output.txt

Single-threaded runtimes: about 0.6 s and 0.2 s. A rerun on 2026-11-21
reproduced both output files byte for byte.
