def naiveSearch(edges, n):
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
    # This loop is O[m]
    reachable = [set() for _ in range(n)]
    for u, v in edges:
        reachable[u].add(v)
    #print(reachable)
    
    # Expand reachable to vertices reachable in n steps
    # This loop is O[n^2]
    #     Since one can reach at most n vertices from each vertex
    for _ in range(n):
        prev = reachable.copy()
        for u in range(n):
            for v in reachable[u].copy():
                reachable[u] = reachable[u].union(reachable[v])
                # this operation (O[n])
        #print(reachable)
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
    
    # remove duplicates by making a set of tuples
    l_scc = set([tuple(scc) for scc in l_scc])

    # make a dictionary of sets
    l_scc = {i:set(scc) for i,scc in enumerate(l_scc)}

    # sccs is such that vertex/index i is the name of its scc
    #   this will help convert graph to metagraph
    # filling sccs is O[n]
    sccs = [None for _ in range(n)]
    for i in range(n):
        for s in l_scc.keys():
            if i in l_scc[s]:
                sccs[i] = s
                
    return max(l_scc.keys()) + 1, l_scc, sccs


def metaGraph(edges, sccs):
    # making meta_graph is O[m]
    meta_graph = set()
    for u, v in edges:
        if sccs[u] == sccs[v]:
            continue
        meta_graph.add((sccs[u], sccs[v]))
    return list(meta_graph)

    
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
##    n, m = 9, 9
##    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (3, 7), (4, 1), (4, 5), (6, 2), (8, 0)]
    ns, l_scc, sccs = naiveSearch(edges, n)
    print(f'Edges =\t{edges}')
    print(f'N_SCC =\t{ns}')
    print(f'L_SSC =\t{l_scc}')
    print(f'Metagraph =\t{metaGraph(edges, sccs)}')

    
main()
