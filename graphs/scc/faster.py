def topological_ordering(edges, n, m):
    '''
    Iterative DFS to find a reverse postorder.
    
    Time complexity: O[m].
    
    Input:
        edges:  list of tuples such as (u, v) which represets a
                directed edge from vertex u to vertex v.
        n:      int, no. of vertices with names range(n).
        m:      int, no. of edges.
        
    Output:
        r_postorder:    list of vertices in reverse postorder
                        
    '''
    # Step 1
    # make adj, adj_r
    adj = {i:[] for i in range(n)}
    adj_r = {i:[] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj_r[v].append(u)
        
    # Step 2
    # initiate r_postorder, visited, and n_left (n not in postoder)
    r_postorder = []
    visited = [0 for i in range(n)]
    n_left = n
    
    #Step 3:
    # DFS to fill r_postorder
    while n_left:
        for u in range(n):
            if visited[u] == 0:
                break
        stack = [u]
        while stack:
            a = stack.pop()
            visited[a] = 1
            go_on = True
            for b in adj_r[a]:
                if not visited[b]:
                    go_on = False
                    stack.append(a)
                    stack.append(b)
                    break
            # if all neighbors have been visited
            if go_on:
                r_postorder.append(a)
                n_left -= 1
                
    r_postorder.reverse()
    
    return r_postorder, adj


def gatherSCCs(edges, n, m):
    '''
    This function takes a graph as edges, finds and returns the
    strongly connected components (SCC).
    
    Time Complexity: O[n + m]
    
    Input:
        edges:  list of tuples
        n:      int, no. of vertices.
                    Implied names of vetices: range(n)
    Output:
        n_scc:  int, no. of SCC
        l_scc:  list of lists; list of SCCs where
                    each SCC is represented as a list.
    '''
    
    # Step 1: find reverse post-order and adj
    # O[m]
    ordered, adj = topological_ordering(edges, n, m)
    #print(ordered)
    
    # Step 2: Collect all SCCs by DFS in reverse post-order
    # O[n]
    visited = [0 for _ in range(n)]
    n_left = n
    sccs = [0 for _ in range(n)]
    s = -1
    while n_left:
        u = None
        stack = []
        for u in ordered:
            if not visited[u]:
                stack = [u]
                break
        s += 1
        while stack:
            x = stack.pop()
            sccs[x] = s
            visited[x] = 1
            n_left -= 1
            for y in adj[x]:
                if not visited[y]:
                    stack.append(y)
                    
    # Step 3: make a dictionary of SCC keyed by name
    # O[n]                
    l_scc = {i:set() for i in range(max(sccs)+1)}
    for i, s in enumerate(sccs):
        l_scc[s].add(i)
    
    return len(l_scc), l_scc, sccs


def metaGraph(edges, sccs):
    # making metagraph is O[m]
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
    # find SCCs
    ns, l_scc, sccs = gatherSCCs(edges, n, m)
    print(f'Edges =\t{edges}')
    print(f'N_SCC =\t{ns}')
    print(f'L_SSC =\t{l_scc}')
    # make and print metagraph
    print(f'Metagraph =\t{metaGraph(edges, sccs)}')
    
main()
    
