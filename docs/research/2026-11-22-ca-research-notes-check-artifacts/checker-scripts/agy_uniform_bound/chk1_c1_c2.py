"""C1 (n=2) reconstruction and C2 (topology, harmonicity, landscape) checks. Own code; mpmath 40 digits."""
import mpmath as mp
import numpy as np
from gear import build_graph, Model, gth, tree_weight

mp.mp.dps = 40

print("== C1: n=2 ==")
IC, de, h, ep0 = mp.mpf("0.5"), mp.mpf("0.01"), mp.mpf("0.4"), mp.mpf("0.015")


def n2(gamma, ep=ep0):
    c1, c2 = -h - ep, -h
    I1, I2 = IC + de, IC - de
    sig = lambda x: 1 / (1 + mp.exp(-x))
    # states: 0=(0,0),1=(1,0),2=(0,1),3=(1,1); member 1 flips bit0, member 2 flips bit1
    q = [[mp.mpf(0)] * 4 for _ in range(4)]

    def dG(u, s):  # G_u(on)-G_u(off) given the other's bit
        other = (s >> (1 - u)) & 1
        return (c1 + I1 * other) if u == 0 else (c2 + I2 * other)

    for s in range(4):
        for u in range(2):
            d = dG(u, s)
            q[s][s ^ (1 << u)] = sig(-gamma * d) / 2 if not (s >> u) & 1 else sig(gamma * d) / 2
    pi, _, _ = gth(q, [0, 1, 2, 3])
    return q, pi, (c1, c2)


# (i) validate tree_weight against explicit enumeration of the 4 trees per root on the 4-cycle
q, pi, _ = n2(mp.mpf(7))
cyc = [0, 1, 3, 2]


def brute(root):
    tot = mp.mpf(0)
    for cut in range(4):  # delete the cycle edge between cyc[cut] and cyc[cut+1]
        line = [cyc[(cut + 1 + t) % 4] for t in range(4)]
        j = line.index(root)
        w = mp.mpf(1)
        for i, a in enumerate(line):
            if a == root:
                continue
            nxt = line[i + 1] if j > i else line[i - 1]
            w *= q[a][nxt]
        tot += w
    return tot


Ws = [brute(r) for r in range(4)]
errs = [abs(tree_weight(q, [0, 1, 2, 3], r) / Ws[r] - 1) for r in range(4)]
print("tree_weight vs brute 4-tree enumeration, max rel err:", mp.nstr(max(errs), 3),
      "| MCTT pi vs GTH pi max err:", mp.nstr(max(abs(Ws[r] / sum(Ws) - pi[r]) for r in range(4)), 3))
assert max(errs) < mp.mpf(10) ** -30

# (ii) asymptotics
print(" gamma    P(0,1)         [P01/P10]/e^{g(2d-e)}   TV(P,P_Phi)      TV(P,P_Hodge)   P_Phi(0,1)<=e^{-g e}")
for g in [1, 100, 2000, 20000, 200000]:
    g = mp.mpf(g)
    q, pi, (c1, c2) = n2(g)
    EPhi = [0, c1, c2, c1 + c2 + IC]
    EH = [0, c1 + de / 2, c2 - de / 2, c1 + c2 + IC]

    def gibbs(E):
        w = [mp.exp(-g * (e - min(E))) for e in E]
        Z = sum(w)
        return [x / Z for x in w]

    pP, pH = gibbs(EPhi), gibbs(EH)
    tvP = sum(abs(pi[s] - pP[s]) for s in range(4)) / 2
    tvH = sum(abs(pi[s] - pH[s]) for s in range(4)) / 2
    print(f" {int(g):7d} {mp.nstr(pi[2], 10):>14} {mp.nstr(pi[2] / pi[1] / mp.exp(g * (2 * de - ep0)), 10):>16} "
          f"{mp.nstr(tvP, 10):>16} {mp.nstr(tvH, 10):>16}   {pP[2] <= mp.exp(-g * ep0)}")

# (iii) Hodge projection of the perturbation flow computed by least squares (not hard-coded)
d = 0.01
R = lambda u, s: (d if u == 0 else -d) * ((s & 1) * ((s >> 1) & 1))
E = [(s, s | (1 << u), u) for s in range(4) for u in range(2) if not (s >> u) & 1]
X = np.array([R(u, t) - R(u, s) for (s, t, u) in E])
Gm = np.zeros((len(E), 4))
for k, (s, t, u) in enumerate(E):
    Gm[k, t] = 1
    Gm[k, s] = -1
f, *_ = np.linalg.lstsq(Gm, X, rcond=None)
f -= f[0]
print("least-squares potential part f(00,10,01,11) =", np.round(f, 12), " claimed (d/2)(p1-p2) =", [0, d / 2, -d / 2, 0])
print("divergence of the raw n=2 perturbation:", np.round(Gm.T @ X, 12), "(nonzero: the raw n=2 perturbation has a potential part)")
print("divergence of residual X - grad f:", np.round(Gm.T @ (X - Gm @ f), 12))
# negative control: eps > 2 delta
q, pi, _ = n2(mp.mpf(2000), ep=mp.mpf("0.025"))
print("control eps=0.025>2delta, gamma=2000: P(0,1) =", mp.nstr(pi[2], 6))

print("\n== C2: topology via hypercube energies (own construction) ==")


def analyze(m, drop=None):
    n, sizes, offs, edges, motor = build_graph(m)
    if drop is not None:
        edges = dict(edges)
        edges.pop(drop)
    N = 1 << n
    s = np.arange(N, dtype=np.int64)
    bits = ((s[:, None] >> np.arange(n)[None, :]) & 1).astype(np.int64)
    hh, Iadj, Iwall = 0.9, 1.0, 5.0
    Phi = -hh * bits.sum(1).astype(float)
    for (x, y), kind in edges.items():
        Phi += (Iadj if kind == "adj" else Iwall) * bits[:, x] * bits[:, y]
    E0 = -m * hh
    P = np.where(np.abs(Phi - E0) < 1e-9)[0]
    B = np.where(np.abs(Phi - (E0 + 0.1)) < 1e-9)[0]
    V0 = set(P.tolist()) | set(B.tolist())
    assert Phi.min() > E0 - 1e-9
    mask = np.ones(N, bool)
    mask[list(V0)] = False
    gapV1 = Phi[mask].min() - E0
    nb = {a: [a ^ (1 << i) for i in range(n) if (a ^ (1 << i)) in V0] for a in V0}
    degs = sorted(len(v) for v in nb.values())
    ends = [a for a in V0 if len(nb[a]) == 1]
    ok = len(ends) == 2 and degs[-1] <= 2
    path = None
    if ok:
        path = [ends[0]]
        prev = None
        while True:
            nx = [b for b in nb[path[-1]] if b != prev]
            if not nx:
                break
            prev = path[-1]
            path.append(nx[0])
        ok = len(path) == len(V0)
    # min Phi increase on edges P->V1 and B->V1 (uniform costs)
    minPV1 = min(Phi[a ^ (1 << i)] - Phi[a] for a in P.tolist() for i in range(n) if (a ^ (1 << i)) not in V0)
    minBV1 = min(Phi[a ^ (1 << i)] - Phi[a] for a in B.tolist() for i in range(n) if (a ^ (1 << i)) not in V0) if len(B) else None
    return dict(n=n, nE=len(edges), nP=len(P), nB=len(B), gapV1=gapV1, ok=ok, degs=(degs[0], degs[-1]), path=path,
                Phi=Phi, motor=motor, sizes=sizes, offs=offs, edges=edges, V0=V0, minPV1=minPV1, minBV1=minBV1)


for m in [2, 3]:
    r = analyze(m)
    n = r["n"]
    path = r["path"]
    assert r["ok"] and all((bin(a).count("1") == m) == (k % 2 == 0) for k, a in enumerate(path))
    mot = set(r["motor"])
    Pst = path[::2]

    def steps(Pst):
        sc = [0]
        for a, b in zip(Pst[:-1], Pst[1:]):
            off = (a & ~b).bit_length() - 1
            on = (b & ~a).bit_length() - 1
            sc.append(sc[-1] + (1 if (off, on) in mot else (-1 if (on, off) in mot else 0)))
        return sc

    sc = steps(Pst)
    if sc[-1] < 0:
        Pst = Pst[::-1]
        sc = steps(Pst)
    mono = all(y >= x for x, y in zip(sc[:-1], sc[1:]))
    ntop = sum(1 for x in sc if x == 2 ** m)
    offs = r["offs"]
    lo = (0, 2) if m == 2 else (1, 5)
    u1, u2 = offs[m - 2] + lo[0], offs[m - 2] + lo[1]
    w1, w2 = offs[m - 1], offs[m - 1] + 2
    cps = [(k, sc[k]) for k, a in enumerate(Pst) if (((a >> u1) | (a >> u2)) & 1) and (((a >> w1) | (a >> w2)) & 1)]
    low = {Pst[k] & ((1 << offs[m - 2]) - 1) for k, _ in cps}
    bonus = {u1, u2, w1, w2}
    cnt5 = 0
    for k, a in enumerate(Pst):
        nbrs = [Pst[j] for j in (k - 1, k + 1) if 0 <= j < len(Pst)]
        if any(((b & ~a).bit_length() - 1) in bonus for b in nbrs):
            cnt5 += 1
    print(f" m={m} n={n} dim_eta={r['nE']} |P|={r['nP']} (3*2^m-5={3 * 2 ** m - 5}) |B|={r['nB']} induced-V0-is-path={r['ok']} "
          f"deg(min,max)={r['degs']} V1gap={r['gapV1']:.3f} min dPhi(P->V1)={r['minPV1']:.3f} min dPhi(B->V1)={r['minBV1']:.3f}")
    print(f"      s(vL)={sc[-1]} monotone={mono} n_top={ntop} checkpoints(pos,s)={cps} shared_low_subset={len(low) == 1} "
          f"P-states adjacent to a bonus-node bridge={cnt5}")
    assert r["nP"] == 3 * 2 ** m - 5 and sc[-1] == 2 ** m and mono and ntop == m - 1 and len(cps) == 4 and cnt5 <= 5
    if m == 2:
        M = Model(m, "0.01", [-0.9] * n)
        div = max(abs(mp.fsum(M.R(u, s ^ (1 << u)) - M.R(u, s) for u in range(n))) for s in range(M.N))
        ssum = max(abs(mp.fsum(M.R(u, s) for u in range(n))) for s in range(M.N))
        sig = [max(abs(M.R(u, s | (1 << u)) - M.R(u, s & ~(1 << u))) for s in range(M.N)) for u in range(n)]
        dec = max(abs(M.dG(u, s) - ((M.Phi(s | (1 << u)) + M.R(u, s | (1 << u))) - M.Phi(s & ~(1 << u))))
                  for u in range(n) for s in range(M.N))
        Mc = Model(m, "0.01", [-0.9] * n, control=True)
        divc = max(abs(mp.fsum(Mc.R(u, s ^ (1 << u)) - Mc.R(u, s) for u in range(n))) for s in range(Mc.N))
        PhiErr = max(abs(float(M.Phi(s)) - r["Phi"][s]) for s in range(M.N))
        print(f"      LG model m=2 (R from mutual informations, all 128 states): max|delta^*R|={mp.nstr(div, 3)} max|sum_u R_u|={mp.nstr(ssum, 3)}")
        print(f"      sigma_u={[mp.nstr(x, 6) for x in sig]}  decomposition residual={mp.nstr(dec, 3)}  |Phi_LG-pairwise Phi|max={PhiErr:.1e}  "
              f"[control (+d,+d): max|delta^*R|={mp.nstr(divc, 6)}]")

n, sizes, offs, edges, motor = build_graph(2)
inter = [e for e in edges if e[0] < 4 <= e[1]]
bad = [analyze(2, drop=e)["ok"] for e in inter]
print(" control: dropping each of the", len(inter), "inter-gear walls at m=2 still gives a path?", bad)

for m in [4, 5]:
    n, sizes, offs, edges, motor = build_graph(m)
    walls = {frozenset(e) for e, k in edges.items() if k == "wall"}
    cnt = [0]

    def rec(g, prev):
        if g == m:
            cnt[0] += 1
            return
        for rr in range(sizes[g]):
            x = offs[g] + rr
            if prev is None or frozenset((prev, x)) not in walls:
                rec(g + 1, x)

    rec(0, None)
    print(f" m={m}: n={n} (8m-9={8 * m - 9}), |E|={len(edges)} (68m-138={68 * m - 138}), one-hot wall-free tuples={cnt[0]} (3*2^m-5={3 * 2 ** m - 5})")
