from gear import build_graph

def onehot_path(mm):
    nn, sizes, offs, edges, motor = build_graph(mm)
    walls = {frozenset(e) for e, k in edges.items() if k == "wall"}
    adjs = {frozenset(e) for e, k in edges.items() if k == "adj"}
    tuples = []

    def rec(g, cur):
        if g == mm:
            tuples.append(tuple(cur))
            return
        for r in range(sizes[g]):
            x = offs[g] + r
            if not cur or frozenset((cur[-1], x)) not in walls:
                rec(g + 1, cur + [x])

    rec(0, [])
    tset = set(tuples)
    nb = {t: [] for t in tuples}
    for t in tuples:
        for g in range(mm):
            for r in range(sizes[g]):
                x = offs[g] + r
                if frozenset((t[g], x)) in adjs:
                    t2 = t[:g] + (x,) + t[g + 1:]
                    if t2 in tset:
                        nb[t].append(t2)
    ends = [t for t in tuples if len(nb[t]) == 1]
    assert len(ends) == 2 and max(len(v) for v in nb.values()) == 2
    path = [ends[0]]
    prev = None
    while True:
        nx = [u for u in nb[path[-1]] if u != prev]
        if not nx:
            break
        prev = path[-1]
        path.append(nx[0])
    assert len(path) == len(tuples)
    mot = set(motor)

    def steps(pp):
        sc = [0]
        for a, c in zip(pp[:-1], pp[1:]):
            g = [i for i in range(mm) if a[i] != c[i]][0]
            sc.append(sc[-1] + (1 if (a[g], c[g]) in mot else (-1 if (c[g], a[g]) in mot else 0)))
        return sc

    if steps(path)[-1] < 0:
        path = path[::-1]
    return nn, path, steps(path)


