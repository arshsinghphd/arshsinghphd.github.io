def naive_search(edges, n):
    '''
    This function takes a graph as edges, finds and returns the
    strongly connected components (SCC).
    
    Time Complexity:
        O[n^2]
    Input:
        edges:  list of tuples
        n:      int, no. of vertices.
                    Implied names of vetices: range(n)
    Output:
        n_scc:  int, no. of SCC
        l_scc:  list of lists,
                list of SCCs, where
                    each SCC is represented as a list.
    '''
    # make a set of vertices reachable from each vertex in one step
    # This loop is O[n]
    reachable = [set() for _ in range(n)]
    for u, v in edges:
        reachable[u].add(v)
    print(reachable)
    
    # Expand reachable to vertices reachable in n steps
    # This loop is O[n^2]
    #     Since one can reach at most n vertices from each vertex
    for _ in range(n):
        prev = reachable.copy()
        for u in range(n):
            for v in reachable[u].copy():
                reachable[u] = reachable[u].union(reachable[v])
                # this operation (O[n])
        print(reachable)
        # an early stop switch, we do not always need all n steps
        if prev == reachable:
            break
        
    # This loop is O[n^2]
    #    Since we perform at most n^2 successful comparisons
    l_scc = [set([i]) for i in range(n)]
    for i in range(n, -1, -1):
        for j in range(i):
            if i in reachable[j] and j in reachable[i]:
                l_scc[i] = l_scc[i].union(l_scc[j])
                l_scc[j] = l_scc[i]
                
    print(l_scc)
    
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
    n_scc, l_scc = naive_search(edges, n)
    print(n_scc, l_scc)
    
main()
