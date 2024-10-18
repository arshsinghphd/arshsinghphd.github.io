from itertools import permutations

def naive_search(edges, n, m):
    reachable = [set() for _ in range(n)]
    for u, v in edges:
        reachable[u].add(v)
        
    # This loop is O[n^3]
    #print(reachable)
    for _ in range(n):
        prev = reachable.copy()
        for u in range(n):
            for v in reachable[u].copy():
                reachable[u] = reachable[u].union(reachable[v])
                # this operation (O[n])
        #print(reachable)
        if prev == reachable:
            break
        
    # This loop is O[n^2 log n]
    l_scc = [set([i]) for i in range(n)]
    for i in range(n, -1, -1):
        for j in range(i):
            if i in reachable[j] and j in reachable[i]:
                l_scc[i] = l_scc[i].union(l_scc[j])
                l_scc[j] = l_scc[j].union(l_scc[i])
                # this operation (O[n])

    # remove duplicates by making a set of tuples
    l_scc = set([tuple(scc) for scc in l_scc])

    # make a list of lists
    l_scc = [list(scc) for scc in l_scc]
    
    return len(l_scc), l_scc

def main():
    n, m = 12, 16
    edges = [(0, 2), (0, 5),
             (1, 0), (1, 7),
             (2, 1), (2, 4),
             (3, 1), (3, 8),
             (4, 0),
             (6, 5), (6, 7),
             (7, 6),
             (8, 7),
             (9, 10),
             (10, 11),
             (11, 9)]
    n_scc, l_scc = naive_search(edges, n, m)
    print(n_scc, l_scc)
main()
