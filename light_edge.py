"""Third independent reconstruction of the r = 7 finite lemma 'Weighted light edge'
(Sneiderman, r7-r8/main.tex, Lemma 3.2). Route: the networkx atlas of all unlabelled graphs on
7 vertices; labelled counts as 7!/|Aut|; for each graph and weight budget Z, the maximum over
weights z (sum Z) of the minimum over edges of d(y) + d(y') + z_y + z_y'.
Usage: python3 light_edge.py      (about one second; requires networkx)"""
import math
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher

def alpha(G):
    return max(len(c) for c in nx.find_cliques(nx.complement(G)))

def comps(total, k):
    if k == 1:
        yield (total,)
        return
    for x in range(total + 1):
        for rest in comps(total - x, k - 1):
            yield (x,) + rest

table, counts, ntypes = {}, {}, {}
for G in nx.graph_atlas_g():
    if G.number_of_nodes() != 7:
        continue
    m = G.number_of_edges()
    if not 6 <= m <= 9 or alpha(G) > 5:
        continue
    aut = sum(1 for _ in GraphMatcher(G, G).isomorphisms_iter())
    counts[m] = counts.get(m, 0) + math.factorial(7) // aut
    ntypes[m] = ntypes.get(m, 0) + 1
    deg = dict(G.degree())
    E = list(G.edges())
    for Z in range(0, 10 - m):
        best = max(min(deg[a] + deg[b] + z[a] + z[b] for a, b in E) for z in comps(Z, 7))
        table[(m, Z)] = max(table.get((m, Z), 0), best)

print("unlabelled types  :", ntypes)     # expected {6: 40, 7: 65, 8: 97, 9: 131}
print("labelled graphs   :", counts)     # expected {6: 54257, 7: 116280, 8: 203490, 9: 293930}
for k in sorted(table):
    print("(m, Z) =", k, " largest possible minimum =", table[k])
print("(i)  m+Z <= 8 => some edge <= 6 :", all(v <= 6 for (m, Z), v in table.items() if m + Z <= 8))
print("(ii) m+Z <= 9 => some edge <= 7 :", all(v <= 7 for (m, Z), v in table.items() if m + Z <= 9))
