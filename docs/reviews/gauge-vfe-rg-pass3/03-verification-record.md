# Coarse-graining investigation verification record

Date: 2026-08-01

- Report:
  docs/reviews/gauge-vfe-rg-pass3/01-holonomy-kl-coarsegraining-investigation.md
- Report SHA-256:
  29499322007E07852B365922ABF942B51E1513E26BC169FB057D398A0D0BD339
- Claim ledger:
  docs/reviews/gauge-vfe-rg-pass3/02-claim-ledger.json
- Claim-ledger SHA-256:
  4213F201C5F20F256C28425BD2C4AFC33124D24A570FD694F5590DD5F38DC3E0

The manuscript worktree already had an active verification marker for the preceding pass-2 audit.
That marker was preserved. The new ledger was copied into an isolated temporary Git gate, rebound
only in that temporary copy to the gate's concrete revision, and validated with:

    python verification_gate.py validate ledger.json --cwd C:\tmp\gauge-coarse-verification-20260801

Result: exit code 0 with no validation errors.

Closure summary:

- COARSE-01 through COARSE-04: EVIDENCE_VERIFIED.
- COARSE-05: REFUTED.
- COARSE-06: INCONCLUSIVE with four explicit open obligations.

No numerical check is used as proof of a mathematical claim. The closure evidence is the stated
derivation, exact counterexamples, and independently challenged source integration.
