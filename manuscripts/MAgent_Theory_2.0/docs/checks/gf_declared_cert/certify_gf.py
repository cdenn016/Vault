r"""Rigorous certification of the declared instance gf:declared / gf:instance
(MAgent_Theory_2.0/chapters/05_global_formation.tex, lines ~587-715).

Exact rational arithmetic (fractions.Fraction) for trajectories, inverses,
determinants and quadratic forms; mpmath.iv interval arithmetic only for
log det and square roots.  Score (uniform prior, common constants dropped):
    s(Pi, m) = -1/2 m^T C_Pi^{-1} m - 1/2 log det C_Pi .
"""
from __future__ import annotations
import sys
from fractions import Fraction as Fr
from itertools import combinations
from mpmath import iv, mp

iv.dps = 60
mp.dps = 60

# ---------------------------------------------------------------- linear algebra
def mat_inv(A):
    n = len(A)
    M = [list(map(Fr, row)) + [Fr(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [row[n:] for row in M]

def det(A):
    n = len(A); M = [list(map(Fr, r)) for r in A]; d = Fr(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return Fr(0)
        if p != c:
            M[c], M[p] = M[p], M[c]; d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return d

def mv(A, v): return [sum(a * x for a, x in zip(row, v)) for row in A]
def dot(u, v): return sum(a * b for a, b in zip(u, v))
def sub(u, v): return [a - b for a, b in zip(u, v)]
def quad(A, v): return dot(v, mv(A, v))
def ivq(q: Fr): return iv.mpf(q.numerator) / iv.mpf(q.denominator)
def ivlog(q: Fr): return iv.log(ivq(q))
def ivsqrt(q: Fr): return iv.sqrt(ivq(q))

# ---------------------------------------------------------------- catalog
def set_partitions(items):
    items = list(items)
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for p in set_partitions(rest):
        for k in range(len(p)):
            yield p[:k] + [[first] + p[k]] + p[k + 1:]
        yield [[first]] + p

def catalog(N):
    cat = []
    for P1 in set_partitions(range(N)):
        P1 = [tuple(sorted(b)) for b in P1]
        for P2 in set_partitions(range(len(P1))):
            cat.append((tuple(sorted(P1)), tuple(sorted(tuple(sorted(sum((list(P1[j]) for j in c), []))) for c in P2))))
    return cat

def name(P):
    f = lambda bl: "{" + ",".join("".join(str(i + 1) for i in b) for b in bl) + "}"
    return "(" + f(P[0]) + "|" + f(P[1]) + ")"

class Model:
    def __init__(self, s2, rho2, tau2, sig2, N=4):
        self.N = N; self.s2, self.rho2, self.tau2, self.sig2 = s2, rho2, tau2, sig2
        self.a = s2 / (s2 + rho2); self.b = 1 - self.a
        self.v = s2 + tau2 + sig2; self.k = (tau2 + sig2) / self.v
        self.kappa = self.v / (self.v + rho2)
        self.cat = catalog(N)
        assert len(self.cat) == len(set(self.cat))
        self.C, self.Ci, self.logdet, self.K = {}, {}, {}, {}
        for P in self.cat:
            C = [[Fr(0)] * N for _ in range(N)]
            for i in range(N):
                C[i][i] += s2
            for B in P[0]:
                for i in B:
                    for j in B: C[i][j] += tau2
            for G in P[1]:
                for i in G:
                    for j in G: C[i][j] += sig2
            self.C[P] = C; Ci = mat_inv(C); self.Ci[P] = Ci
            self.logdet[P] = ivlog(det(C))
            self.K[P] = [[Fr(int(i == j)) - s2 * Ci[i][j] for j in range(N)] for i in range(N)]

    def score(self, P, m):
        return -ivq(quad(self.Ci[P], m)) / 2 - self.logdet[P] / 2

    def select(self, m, cat=None):
        """Return (winner, runner-up, certified gap interval). Raises if not separated."""
        cat = cat or self.cat
        sc = {P: self.score(P, m) for P in cat}
        order = sorted(cat, key=lambda P: float(sc[P].mid), reverse=True)
        W = order[0]
        for P in order[1:]:
            g = sc[W] - sc[P]
            if not (g.a > 0):
                raise RuntimeError(f"selection not certified: {name(W)} vs {name(P)} gap {g}")
        gap = sc[W] - sc[order[1]]
        return W, order[1], gap

    def sweep(self, P, m, o):
        Km = mv(self.K[P], m)
        return [self.a * oi + self.b * zi for oi, zi in zip(o, Km)]

    def ball_radius(self, W, c, cat=None):
        r"""Largest certified r: for all P != W and ||u||<=r,
        s(W,c+u)-s(P,c+u) >= f0 - ||D c|| r - 1/2 ||D||_F r^2 > 0, D = C_W^{-1}-C_P^{-1}.
        Returns a rational lower bound r_cert (min over P) and the binding P."""
        cat = cat or self.cat
        best = None
        for P in cat:
            if P == W: continue
            D = [[x - y for x, y in zip(rw, rp)] for rw, rp in zip(self.Ci[W], self.Ci[P])]
            f0 = self.score(W, c) - self.score(P, c)
            g = ivsqrt(sum(x * x for x in mv(D, c)))
            h = ivsqrt(sum(x * x for row in D for x in row))
            # root of f0 - g r - h/2 r^2 = 0  -> r = (-g + sqrt(g^2 + 2 h f0)) / h ; take lower endpoint
            rr = (-g + iv.sqrt(g * g + 2 * h * f0)) / h
            rl = Fr(float(rr.a)) if rr.a > 0 else Fr(0)
            # step down to be safe and re-verify the bound at rl with interval arithmetic
            rl = rl * Fr(999999, 1000000)
            bound = f0 - g * ivq(rl) - h * ivq(rl) ** 2 / 2
            assert bound.a > 0, (name(P), bound)
            if best is None or rl < best[0]:
                best = (rl, P)
        return best

def F(x): return Fr(str(x))

def main() -> None:
    out = []
    def pr(*a):
        s = " ".join(str(x) for x in a); print(s); out.append(s)

    M = Model(Fr(1), Fr(1, 4), Fr(1, 10), Fr(4))
    pr("catalog size", len(M.cat), "| a,b,k,kappa =", M.a, M.b, M.k, M.kappa, "| a/kappa =", M.a / M.kappa)
    o = [F(x) for x in (2.9, 3.1, 4.4, 4.6)]
    m0 = [F(x) for x in (-9.2, -3.0, 4.2, 10.4)]
    perp = ((( 0,), (1,), (2,), (3,)), ((0,), (1,), (2,), (3,)))
    sep = (((0, 1), (2, 3)), ((0, 1), (2, 3)))
    join = (((0, 1), (2, 3)), ((0, 1, 2, 3),))
    assert perp in M.cat and sep in M.cat and join in M.cat

    def hist(label, traj):
        pr(f"--- {label}")
        sels = []
        for n, m in enumerate(traj):
            W, R, gap = M.select(m)
            sels.append(W)
            pr(f"  sweep {n}: sel={name(W)} runner-up={name(R)} gap in [{'%.10g' % float(gap.a)}, {'%.10g' % float(gap.b)}]")
        return sels

    # ---- full flow: exact rational trajectory, sweeps 0..4
    traj = [m0]
    for n in range(4):
        W, _, _ = M.select(traj[-1]); traj.append(M.sweep(W, traj[-1], o))
    sf = hist("FULL flow (expected: perp, sep, join, join, join)", traj)
    mstar = mv(M.C[join], mv(mat_inv([[M.C[join][i][j] + (M.rho2 if i == j else 0) for j in range(4)] for i in range(4)]), o))
    pr("  m*_join =", ['%.6f' % float(ivq(x).mid) for x in mstar])
    r_full, Pb = M.ball_radius(join, mstar)
    pr(f"  certified persistence radius (Euclidean = S-norm, S=I) r >= {float(r_full):.6f}, binding competitor {name(Pb)}")
    for n, m in enumerate(traj):
        d2 = sum(x * x for x in sub(m, mstar))
        pr(f"  ||m^({n}) - m*||^2 = {float(d2):.6e}  in ball: {d2 <= r_full**2}")
    # contraction factor of b K_join (symmetric, S=I): spectral radius
    import numpy as np
    Kj = np.array([[float(x) for x in r] for r in M.K[join]])
    pr("  b*lambda_max(K_join) (float) =", float(M.b) * max(np.linalg.eigvalsh(Kj)), " (lemma uses bound b = 0.2)")
    for n in (2, 3, 4):
        m = traj[n]
        pr(f"  sweep {n} contrasts exact: m1-m2 == a(o1-o2): {m[0]-m[1] == M.a*(o[0]-o[1])}, m3-m4 == a(o3-o4): {m[2]-m[3] == M.a*(o[2]-o[3])}")

    # ---- label-preserving null: m' = a o + b k m  (structure-independent)
    lp = [m0]
    for n in range(4):
        lp.append([M.a * oi + M.b * M.k * mi for oi, mi in zip(o, lp[-1])])
    pr("  lp m^(1) == full m^(1):", lp[1] == traj[1])
    sl = hist("LABEL-PRESERVING null (expected: perp, sep, join, ...)", lp)
    ko = [M.kappa * x for x in o]
    pr("  kappa o =", ['%.6f' % float(ivq(x).mid) for x in ko])
    r_lp, Pb = M.ball_radius(join, ko)
    pr(f"  certified radius around kappa*o: r >= {float(r_lp):.6f}, binding {name(Pb)}")
    for n, m in enumerate(lp):
        d2 = sum(x * x for x in sub(m, ko))
        pr(f"  ||m_lp^({n}) - kappa o||^2 = {float(d2):.6e}  in ball: {d2 <= r_lp**2}")
    pr("  tail: m_lp^(n)-kappa o = (bk)^(n)(m0-kappa o), bk =", M.b * M.k, "<1, so distance is nonincreasing")

    # ---- renormalized null: m^(n) = kappa o for n>=1
    sr = hist("RENORMALIZED null (expected: perp, join)", [m0, ko])

    # ---- parent sweep
    pr("--- PARENT sweep, A={12,34}")
    lamB = Fr(2); bB = M.b; aB = 1 - bB
    oh = [(o[0] + o[1]) / 2, (o[2] + o[3]) / 2]
    def Cc(P2):
        if P2 == "sep": return [[1 / lamB + M.tau2 + M.sig2, Fr(0)], [Fr(0), 1 / lamB + M.tau2 + M.sig2]]
        return [[1 / lamB + M.tau2 + M.sig2, M.sig2], [M.sig2, 1 / lamB + M.tau2 + M.sig2]]
    class PM: pass
    P = Model.__new__(Model)
    P.cat = ["sep", "join"]; P.C = {q: Cc(q) for q in P.cat}; P.Ci = {q: mat_inv(P.C[q]) for q in P.cat}
    P.logdet = {q: ivlog(det(P.C[q])) for q in P.cat}
    P.K = {q: [[Fr(int(i == j)) - (1 / lamB) * P.Ci[q][i][j] for j in range(2)] for i in range(2)] for q in P.cat}
    P.a, P.b = aB, bB
    rhoB2 = (1 / lamB) * bB / aB
    pr("  rho_B^2 =", rhoB2, " o_hat =", oh)
    fps = {}
    for q in P.cat:
        Cq = P.C[q]; fp = mv(Cq, mv(mat_inv([[Cq[i][j] + (rhoB2 if i == j else 0) for j in range(2)] for i in range(2)]), oh))
        fps[q] = fp
        # verify fixed point exactly
        assert P.sweep(q, fp, oh) == fp
        W, R, gap = P.select(fp)
        pr(f"  fixed point under {q}: {['%.6f' % float(ivq(x).mid) for x in fp]} -> selects {W} with gap [{'%.10g' % float(gap.a)}, {'%.10g' % float(gap.b)}]; self-consistent: {W == q}")
    r_s, _ = P.ball_radius("join", fps["sep"])
    pr(f"  certified ball around sep fixed point where join strictly preferred: r >= {float(r_s):.6f}")
    pr("  under sep the parent map is x -> aB oh + bB K_sep x, K_sep =", P.K["sep"], " contraction factor bB*K =", bB * P.K["sep"][0][0])
    # reproduction: fine block means vs parent sweep from handoff (sweep 2) on
    mh = [(traj[2][0] + traj[2][1]) / 2, (traj[2][2] + traj[2][3]) / 2]
    ok = True
    for n in range(2, 4):
        W, _, _ = P.select(mh); mh = P.sweep(W, mh, oh)
        fine = [(traj[n + 1][0] + traj[n + 1][1]) / 2, (traj[n + 1][2] + traj[n + 1][3]) / 2]
        ok &= (fine == mh) and W == "join"
    pr("  exact reproduction of fine block means and selection (sweeps 3,4):", ok)
    # (iv) symmetry / eigenvector
    Kj = P.K["join"]; pr("  K^c_join symmetric:", Kj[0][1] == Kj[1][0], " (1,1) eigvec:", mv(Kj, [1, 1])[0] == mv(Kj, [1, 1])[1])

    # ---- posterior masses and MAP of the records
    pr("--- posterior masses at the limit")
    def softmax_mass(scores, target):
        ref = scores[target]
        tot = sum((iv.exp(scores[q] - ref) for q in scores), iv.mpf(0))
        return 1 / tot
    sc_lim = {q: M.score(q, mstar) for q in M.cat}
    pr("  structure factor mass of join at m*_join:", "[%.6f, %.6f]" % (float(softmax_mass(sc_lim, join).a), float(softmax_mass(sc_lim, join).b)))
    CR = {q: [[M.C[q][i][j] + (M.rho2 if i == j else 0) for j in range(4)] for i in range(4)] for q in M.cat}
    sc_rec = {q: -ivq(quad(mat_inv(CR[q]), o)) / 2 - ivlog(det(CR[q])) / 2 for q in M.cat}
    pr("  record-posterior mass of join:", "[%.6f, %.6f]" % (float(softmax_mass(sc_rec, join).a), float(softmax_mass(sc_rec, join).b)))
    best = sorted(M.cat, key=lambda q: float(sc_rec[q].mid), reverse=True)
    g = sc_rec[best[0]] - sc_rec[best[1]]
    pr(f"  MAP of records = {name(best[0])} (join? {best[0]==join}), runner-up {name(best[1])}, gap [{'%.10g' % float(g.a)}, {'%.10g' % float(g.b)}]")

    # ---- frozen-environment control (N3): agent i copy reads (m_i, m0_{-i})
    pr("--- FROZEN-environment control")
    fr = [m0]; copysel = []
    for n in range(12):
        cur = fr[-1]; nxt = []; cs = []
        for i in range(4):
            x = list(m0); x[i] = cur[i]
            Wi, _, _ = M.select(x); cs.append(Wi)
            nxt.append(M.sweep(Wi, x, o)[i])
        copysel.append(cs); fr.append(nxt)
    sfr = hist("frozen joint-selector history (sweeps 0..12)", fr)
    pr("  copy selections per sweep:", [[name(w) for w in cs] for cs in copysel[:4]], "... last:", [name(w) for w in copysel[-1]])
    # 1-D certificate per agent: copy selection fixed = W_i on an interval around its fixed point
    xs, ok_all = [], True
    for i in range(4):
        Wi = copysel[-1][i]
        Kii = M.K[Wi][i][i]
        alpha = M.a * o[i] + M.b * sum(M.K[Wi][i][j] * m0[j] for j in range(4) if j != i)
        beta = M.b * Kii; xstar = alpha / (1 - beta); xs.append(xstar)
        # certify: on |x - xstar| <= r, Wi strict winner of copy selector along the e_i line
        rmin = None
        for Q in M.cat:
            if Q == Wi: continue
            c = list(m0); c[i] = xstar
            D = [[x - y for x, y in zip(rw, rq)] for rw, rq in zip(M.Ci[Wi], M.Ci[Q])]
            f0 = M.score(Wi, c) - M.score(Q, c)
            g1 = abs(mv(D, c)[i]); h1 = abs(D[i][i])
            assert f0.a > 0
            if h1 == 0 and g1 == 0:
                continue  # difference constant along the e_i line and positive
            rr = (-ivq(g1) + iv.sqrt(ivq(g1) ** 2 + 2 * ivq(h1) * f0)) / ivq(h1) if h1 != 0 else f0 / ivq(g1)
            rl = Fr(float(rr.a)) * Fr(999999, 1000000)
            assert (f0 - ivq(g1) * ivq(rl) - ivq(h1) * ivq(rl) ** 2 / 2).a > 0
            rmin = rl if rmin is None or rl < rmin else rmin
        inside = abs(fr[-1][i] - xstar) <= rmin
        ok_all &= inside
        pr(f"  agent {i+1}: copy sel {name(Wi)}, slope b*K_ii={float(beta):.5f}, x*={float(xstar):.6f}, cert. half-width {float(rmin):.4e}, m^(12) inside: {inside}")
    pr("  x* =", ["%.6f" % float(x) for x in xs], " x* == kappa o:", xs == ko)
    rfr, _ = M.ball_radius(join, xs)
    d2 = sum(x * x for x in sub(fr[-1], xs))
    pr(f"  joint ball around x*: r >= {float(rfr):.6f}; ||m_fr^(12)-x*||^2={float(d2):.3e} in ball: {d2 <= rfr**2}; all agents in invariant intervals: {ok_all}")

    # ---- negative controls
    pr("--- negative controls")
    W, _, _ = M.select(traj[1]); pr("  claim 'full sweep 1 selects join' ->", "REFUTED" if W != join else "accepted")
    try:
        M.select([Fr(0)] * 4); pr("  m=0 selection certified (unexpected)")
    except RuntimeError as e:
        pr("  m=0 (expected uncertifiable tie? no: distinct logdets) ->", e)
    W, _, _ = M.select([Fr(0)] * 4); pr("  m=0 selects", name(W), "(smallest det wins)")
    # a radius of 3x the certified one must fail the bound for some competitor
    Dfail = False
    for Q in M.cat:
        if Q == join: continue
        D = [[x - y for x, y in zip(rw, rq)] for rw, rq in zip(M.Ci[join], M.Ci[Q])]
        f0 = M.score(join, mstar) - M.score(Q, mstar)
        g = ivsqrt(sum(x * x for x in mv(D, mstar))); h = ivsqrt(sum(x * x for row in D for x in row))
        R = ivq(3 * r_full)
        if not (f0 - g * R - h * R * R / 2).a > 0: Dfail = True
    pr("  3x radius certificate fails (expected True):", Dfail)

    # ---- regrouping remark (gf:regrouping): tau^2 = 1/20
    pr("--- REGROUPING remark data (tau^2=1/20)")
    M2 = Model(Fr(1), Fr(1, 4), Fr(1, 20), Fr(4))
    o2 = [F(x) for x in (2.9, 3.1, 5.65, 5.85)]; m02 = [F(x) for x in (-4, 2, -9, -1)]
    tr = [m02]
    for n in range(4):
        W, _, _ = M2.select(tr[-1]); tr.append(M2.sweep(W, tr[-1], o2))
    for n, m in enumerate(tr):
        W, R, gap = M2.select(m); pr(f"  full sweep {n}: {name(W)} gap [{'%.10g' % float(gap.a)},{'%.10g' % float(gap.b)}]")
    lp2 = [m02]
    for n in range(5):
        lp2.append([M2.a * oi + M2.b * M2.k * mi for oi, mi in zip(o2, lp2[-1])])
    for n, m in enumerate(lp2):
        W, R, gap = M2.select(m); pr(f"  lp sweep {n}: {name(W)} gap [{'%.10g' % float(gap.a)},{'%.10g' % float(gap.b)}]")
    ko2 = [M2.kappa * x for x in o2]
    W, R, gap = M2.select(ko2); pr(f"  rn sweep>=1 (kappa o): {name(W)} gap [{'%.10g' % float(gap.a)},{'%.10g' % float(gap.b)}]")

    with open(sys.argv[1] if len(sys.argv) > 1 else "certify_gf_output.txt", "w") as fh:
        fh.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()
