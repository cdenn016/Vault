"""Independent reconstruction of the gear-train model of open_agy_uniform_bound.md (written from the note's text)."""
import mpmath as mp


def v_of_I(I):
    K = mp.e ** (2 * mp.mpf(I))
    return (K - 1) + mp.sqrt(K * (K - 1))


def build_graph(m):
    sizes = [4] + [8] * (m - 2) + [3]
    offs = [0]
    for s in sizes:
        offs.append(offs[-1] + s)
    n = offs[-1]
    node = lambda g, r: offs[g] + r
    edges = {}
    for g, sz in enumerate(sizes):
        cyc = g < m - 1
        for i in range(sz):
            for j in range(i + 1, sz):
                isadj = (j - i == 1) or (cyc and j - i == sz - 1)
                edges[(node(g, i), node(g, j))] = "adj" if isadj else "wall"
    motor = [(node(0, i), node(0, (i + 1) % 4)) for i in range(4)]
    for g in range(m - 1):
        fsz, ssz = sizes[g], sizes[g + 1]
        alo, ahi = (0, 2) if g == 0 else (1, 5)
        arc1 = {(alo + t) % fsz for t in range(fsz // 2 + 1)}
        arc2 = {(ahi + t) % fsz for t in range(fsz // 2 + 1)}
        for r in range(ssz):
            allowed = (arc1, {ahi}, arc2, {alo})[r % 4]
            for s in range(fsz):
                if s not in allowed:
                    edges[(node(g, s), node(g + 1, r))] = "wall"
    return n, sizes, offs, edges, motor


class Model:
    """Linear-Gaussian slot model: one independent coordinate per edge, unit-SNR slot at each endpoint."""

    def __init__(self, m, delta, c, Iadj=1, Iwall=5, control=False):
        self.m = m
        self.n, self.sizes, self.offs, self.edges, self.motor = build_graph(m)
        n = self.n
        self.elist = list(self.edges)
        self.c = [mp.mpf(x) for x in c]
        vC = {e: v_of_I(Iadj if self.edges[e] == "adj" else Iwall) for e in self.elist}
        vmem = [dict(vC) for _ in range(n)]
        delta = mp.mpf(delta)
        for (u, w) in self.motor:
            e = (u, w) if (u, w) in self.edges else (w, u)
            vmem[u][e] = v_of_I(Iadj + delta)  # outgoing motor edge
            vmem[w][e] = v_of_I(Iadj + delta if control else Iadj - delta)  # incoming motor edge
        self.vC, self.vmem = vC, vmem
        # L[b][e][k] = 0.5*ln(1+k v_e) under belief b (0..n-1 members, n = declared belief)
        self.L = []
        for b in range(n + 1):
            vv = vC if b == n else vmem[b]
            self.L.append([(mp.mpf(0), mp.log(1 + vv[e]) / 2, mp.log(1 + 2 * vv[e]) / 2) for e in self.elist])
        self.N = 1 << n
        self._I = {}

    def info(self, b, s):
        """I_{q_b}(eta; o_{B(s)}) for bitmask s."""
        key = (b, s)
        if key not in self._I:
            tot = mp.mpf(0)
            Lb = self.L[b]
            for idx, (x, y) in enumerate(self.elist):
                k = ((s >> x) & 1) + ((s >> y) & 1)
                if k:
                    tot += Lb[idx][k]
            self._I[key] = tot
        return self._I[key]

    def psi(self, u):
        return self.c[u] + self.info(u, 1 << u)

    def dG(self, u, s):
        """G_u(s with u on) - G_u(s with u off)."""
        s0 = s & ~(1 << u)
        s1 = s | (1 << u)
        return -(self.info(u, s1) - self.info(u, s0)) + self.psi(u)

    def Phi(self, s):
        n = self.n
        M = sum(self.info(n, 1 << u) for u in range(n) if (s >> u) & 1) - self.info(n, s)
        return sum(self.c[u] for u in range(n) if (s >> u) & 1) + M

    def R(self, u, s):
        if not (s >> u) & 1:
            return mp.mpf(0)
        n = self.n
        s0 = s & ~(1 << u)
        red_u = self.info(u, 1 << u) + self.info(u, s0) - self.info(u, s)
        red_C = self.info(n, 1 << u) + self.info(n, s0) - self.info(n, s)
        return red_u - red_C

    def rates(self, gamma):
        """q[s][t] = T(s,t), s != t (uniform habits, binary policies)."""
        n, N = self.n, self.N
        gamma = mp.mpf(gamma)
        q = [[mp.mpf(0)] * N for _ in range(N)]
        for s in range(N):
            for u in range(n):
                d = self.dG(u, s)
                if (s >> u) & 1:
                    q[s][s ^ (1 << u)] = 1 / (n * (1 + mp.exp(-gamma * d)))  # turn off: G change = -d
                else:
                    q[s][s ^ (1 << u)] = 1 / (n * (1 + mp.exp(gamma * d)))  # turn on: G change = +d
        return q


def gth(q, order, n_keep=1):
    """Subtraction-free (GTH) elimination. States late in 'order' are eliminated first.
    Returns (stationary law over all states, pivots, reduced rate matrix on the first n_keep states)."""
    N = len(order)
    a = [[q[order[i]][order[j]] for j in range(N)] for i in range(N)]
    piv = {}
    red = None
    for k in range(N - 1, 0, -1):
        if k == n_keep - 1:
            red = [row[:n_keep] for row in a[:n_keep]]
        rk = a[k]
        s = mp.fsum(rk[:k])
        piv[order[k]] = s
        nz = [j for j in range(k) if rk[j]]
        for i in range(k):
            f = a[i][k] / s
            a[i][k] = f
            if f:
                ri = a[i]
                for j in nz:
                    if j != i:
                        ri[j] += f * rk[j]
    p = [mp.mpf(1)] + [mp.mpf(0)] * (N - 1)
    for k in range(1, N):
        p[k] = mp.fsum(p[i] * a[i][k] for i in range(k))
    Z = mp.fsum(p)
    pi = {order[k]: p[k] / Z for k in range(N)}
    return pi, piv, red


def tree_weight(q, states, root):
    """Sum over spanning in-trees rooted at 'root' of the chain q restricted to 'states' (matrix-tree theorem via pivots)."""
    order = [root] + [s for s in states if s != root]
    _, piv, _ = gth(q, order)
    w = mp.mpf(1)
    for s in order[1:]:
        w *= piv[s]
    return w
