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


def main():
    n, m = 9, 9
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (3, 7), (4, 1), (4, 5), (6, 2), (8, 0)]
    ordered, adj = topological_ordering(edges, n, m)
    print(f'ordered = \t{ordered}')
    
main()
