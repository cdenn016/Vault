r"""Follow-up checks for blind_recompute.py (same folder).

(a) Monte Carlo of the actual filters (not the error recursion): twin runs share the world path and
    the initial filter means and differ in all private noises (v, nu, c). Then
    e^{(1)}(t) - e^{(2)}(t) has covariance 2 Sigma^c once the private transient has decayed.
(b) Exact ties of the substitute selector at 1.5: automorphism group of the attention pattern
    (member relabelings fixing S that preserve every J_i) acting transitively on members.
(c) Full list of distinct largest-regional-contrast values over diffusive orbits.
(d) Whether the family-2 patterns with {C : r(C) >= 4.45} = {A} are exactly the
    'S + one co-member' patterns.
"""
from __future__ import annotations

import os

for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[_v] = "1"

import itertools
import sys
import time

import mpmath as mp
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import blind_recompute as br  # noqa: E402

OUT = os.path.dirname(os.path.abspath(__file__))
LINES: list[str] = []


def log(s: str = "") -> None:
    print(s, flush=True)
    LINES.append(s)


def mc_twin(p, n_chains: int, T: int, seed: int) -> np.ndarray:
    r"""Run the steady-state filters on simulated data; return 0.5 * Cov(e^(1)(T-1) - e^(2)(T-1))."""
    F, Q, qc, Rc = 0.9, 0.05, 1e-4, 0.002
    Rs = [0.01, 1.0, 1.0, 1.0, 1.0]
    rng = np.random.default_rng(seed)
    filts = []
    for a in range(5):
        msgR = sorted(Rs[j] + Rc for j in p[a])
        f = br.filt_np(Rs[a], tuple(msgR), F, Q, qc)
        cols = [1 + msgR.index(Rs[j] + Rc) for j in p[a]]
        filts.append((f, cols))
    A = np.array([[F, 0.0], [1.0, 0.0]])
    var_eta = Q / (1 - F * F)
    eta_prev = rng.standard_normal(n_chains) * np.sqrt(var_eta)  # eta_{-1}
    eta = F * eta_prev + rng.standard_normal(n_chains) * np.sqrt(Q)  # eta_0
    # previous-round readings s_j(-1) per twin
    s_prev = [np.stack([eta_prev + rng.standard_normal(n_chains) * np.sqrt(Rs[j]) for j in range(5)]) for _ in range(2)]
    mminus = [np.zeros((5, n_chains, 2)) for _ in range(2)]
    e_last = None
    for t in range(T):
        s_now = []
        e_t = []
        for tw in range(2):
            s = np.stack([eta + rng.standard_normal(n_chains) * np.sqrt(Rs[j]) for j in range(5)])
            s_now.append(s)
            e_t.append(mminus[tw][:, :, 0] - eta[None, :])
            new_m = np.zeros_like(mminus[tw])
            for a in range(5):
                f, cols = filts[a]
                K = f["K"]
                mm = mminus[tw][a]  # (n, 2)
                innov_own = s[a] - mm[:, 0]
                m_post = mm + innov_own[:, None] * K[:, 0][None, :]
                for j, col in zip(p[a], cols):
                    y = s_prev[tw][j] + rng.standard_normal(n_chains) * np.sqrt(Rc)
                    m_post = m_post + (y - mm[:, 1])[:, None] * K[:, col][None, :]
                new_m[a] = m_post @ A.T + rng.standard_normal((n_chains, 2)) * np.sqrt(qc)
            mminus[tw] = new_m
        e_last = e_t
        for tw in range(2):
            s_prev[tw] = s_now[tw]
        w = rng.standard_normal(n_chains) * np.sqrt(Q)
        eta = F * eta + w
    d = e_last[0] - e_last[1]  # (5, n)
    return 0.5 * np.cov(d), d


def main() -> None:
    t0 = time.time()
    model = br.MPModel([mp.mpf("0.01")] + [mp.mpf(1)] * 4, mp.mpf("0.002"), mp.mpf("0.9"), mp.mpf("0.05"),
                       mp.mpf("0.0001"))
    # (a) Monte Carlo
    log("(a) Monte Carlo of the running filters, twin runs sharing the world path.")
    log("    expectation: |MC - Sigma^c| within about 3 standard errors for every entry.")
    tests = [("family-1 all-source", ((), (0,), (0,), (0,), (0,))),
             ("family-1 chain S->1->2->3->4", ((), (0,), (1,), (2,), (3,))),
             ("family-2 S + mutual mate", ((), (0, 2), (0, 1), (0, 4), (0, 3)))]
    for name, p in tests:
        S5 = np.array(br.first_components(model.sigma_blocks(p)).tolist(), dtype=float)
        n = 60000
        C, d = mc_twin(p, n, 60, seed=12345)
        # SE of 0.5*Cov(d_a, d_b): d has covariance 2 S5; Var(d_a d_b) = D_aa D_bb + D_ab^2
        D = 2 * S5
        se = 0.5 * np.sqrt((np.outer(np.diag(D), np.diag(D)) + D ** 2) / n)
        z = (C - S5) / se
        log(f"  {name}: {br.pat_str(p)}; chains {n}, T=60 (rho(M) <= 0.71 so transient < 1e-17)")
        log("    Sigma^c (exact)   diag: " + ", ".join(f"{x:.6g}" for x in np.diag(S5)))
        log("    MC estimate       diag: " + ", ".join(f"{x:.6g}" for x in np.diag(C)))
        iu = np.triu_indices(5, 1)
        log("    exact off-diag (S1,S2,S3,S4,12,13,14,23,24,34): " + ", ".join(f"{x:.5g}" for x in S5[iu]))
        log("    MC    off-diag                                 : " + ", ".join(f"{x:.5g}" for x in C[iu]))
        log(f"    max |z| over 15 entries = {np.abs(z[np.triu_indices(5)]).max():.2f}")
    log(f"    MC wall {time.time() - t0:.1f}s")

    # (b), (c), (d) need per-pattern records; recompute the light quantities here
    def records(pats):
        out = []
        for p in pats:
            S5 = br.first_components(model.sigma_blocks(p))
            Pi = br.precision_mp(S5)
            dinfo = br.diffusive_info(Pi)
            sel, _, MI = br.selector_mp(S5, br.support_sets(p))
            rec = dict(p=p, Pi=Pi, diff=dinfo["diffusive"], sel=sel, MI=MI)
            if rec["diff"]:
                Pin = np.array(Pi.tolist(), dtype=float)
                rec["r"] = {C: br.contrast_np(Pin, C)[0] for C in br.REGIONS}
                rec["rmax"] = max(rec["r"].values())
            out.append(rec)
        return out

    fam1 = records(br.family_patterns(1))
    fam2 = records(br.family_patterns(2))

    def aut_transitive(p) -> tuple[int, bool]:
        auts = []
        for perm in itertools.permutations(br.MEMBERS):
            m = {0: 0}
            for o, nw in zip(br.MEMBERS, perm):
                m[o] = nw
            ok = all(set(m[j] for j in p[i]) == set(p[m[i]]) for i in br.MEMBERS)
            if ok:
                auts.append(m)
        orbit1 = {m[1] for m in auts}
        return len(auts), orbit1 == set(br.MEMBERS)

    log("\n(b) exact selector ties at 1.5 (family 1 and 2): S isolated and a member-transitive automorphism group")
    log("    expectation: every tie is S-isolated with a member-transitive automorphism group.")
    for fname, recs in (("family 1", fam1), ("family 2", fam2)):
        ties = [r for r in recs if (not mp.isinf(r["sel"])) and abs(r["sel"] - mp.mpf("1.5")) < mp.mpf("1e-30")]
        s_iso = [r for r in recs if all(0 not in r["p"][i] for i in br.MEMBERS)]
        log(f"  {fname}: ties {len(ties)}; S-isolated patterns {len(s_iso)}; "
            f"min selector over S-isolated = {br.fmt(min((r['sel'] for r in s_iso), default=mp.nan), 15)}")
        for r in ties:
            na, tr = aut_transitive(r["p"])
            iso = all(0 not in r["p"][i] for i in br.MEMBERS)
            # weighted MI degree of each member (S has zero MI with everyone when isolated)
            deg = [sum(r["MI"][tuple(sorted((i, j)))] for j in br.MEMBERS if j != i) for i in br.MEMBERS]
            spread = max(deg) - min(deg)
            log(f"    {br.pat_str(r['p'])}: S isolated={iso}, |Aut|={na}, member-transitive={tr}, "
                f"MI-degree spread={mp.nstr(spread, 3)}")
        # non-tied S-isolated: strictly above 1.5 with a gap
        above = [r["sel"] for r in s_iso if r["sel"] - mp.mpf("1.5") > mp.mpf("1e-30")]
        if above:
            log(f"    smallest S-isolated selector strictly above 1.5: {br.fmt(min(above), 15)}")

    log("\n(c) distinct largest-regional-contrast values over diffusive patterns (value: #patterns)")
    for fname, recs in (("family 1", fam1), ("family 2", fam2)):
        vals: dict[float, int] = {}
        for r in recs:
            if r["diff"]:
                key = round(r["rmax"], 9)
                vals[key] = vals.get(key, 0) + 1
        items = sorted(vals.items(), key=lambda kv: -kv[0])
        log(f"  {fname}: {len(items)} distinct values; top 8: " + "; ".join(f"{k:.9f}: {c}" for k, c in items[:8]))

    log("\n(d) family-2 patterns whose regions with r >= 4.45 are exactly {A} vs 'S + one co-member' patterns")
    exactA = {r["p"] for r in fam2 if r["diff"] and {C for C, v in r["r"].items() if v >= 4.45} == {br.A_TUP}}
    smate = {r["p"] for r in fam2 if all(0 in r["p"][i] for i in br.MEMBERS)}
    log(f"  |exactly {{A}}| = {len(exactA)}, |S + co-member| = {len(smate)}, equal sets: {exactA == smate}")
    # range of r(A) and the second-largest regional contrast over those patterns
    rA = [r["r"][br.A_TUP] for r in fam2 if r["p"] in smate]
    second = [sorted(r["r"].values())[-2] for r in fam2 if r["p"] in smate]
    log(f"  over S + co-member patterns: r(A) in [{min(rA):.10g}, {max(rA):.10g}], largest other region <= {max(second):.10g}")
    exactA1 = [r["p"] for r in fam1 if r["diff"] and {C for C, v in r["r"].items() if v >= 4.5} == {br.A_TUP}]
    log(f"  family 1 (r0=4.5) exactly {{A}}: {[br.pat_str(p) for p in exactA1]}")
    # family 1 at r0 = 4.5: second-largest region of the all-source pattern
    rs = [r for r in fam1 if r["p"] == ((), (0,), (0,), (0,), (0,))][0]["r"]
    log(f"  family-1 all-source: r(A) = {rs[br.A_TUP]:.12g}, next region = {sorted(rs.values())[-2]:.12g}")
    log(f"\ntotal wall {time.time() - t0:.1f}s")
    with open(os.path.join(OUT, "blind_followup_output.txt"), "w") as fh:
        fh.write("\n".join(LINES) + "\n")


if __name__ == "__main__":
    main()
