'''
Implementing Ford-Fulkerson method for Max. flow using BFS
'''

from collections import defaultdict, deque

def max_flow(edges, caps, n):
    source = 1
    sink = n
    # initiate flows with 0 
    flows = {}
    for (u, v) in edges:
        flows[u, v] = 0
        flows[v, u] = 0
    # initiate residual graph, by rules
    resid_adj = defaultdict(list)
    resid_caps = {}
    for (u, v) in edges:
        resid_caps[u, v] = caps[u, v] - flows[u, v]
        resid_caps[v, u] = flows[u, v] # cancellation
        if resid_caps[u, v] > 0:
            resid_adj[u].append(v)
        if resid_caps[v, u] > 0:
            resid_adj[v].append(u)
    for u in resid_adj.keys():
        resid_adj[u].sort(key = lambda v: -1*resid_caps[u, v])

    # find path from source to sink in resid_adj using BFS
    max_flow = 0
    while True:
        u = source
        v = resid_adj[source][0]
        queue = deque()
        queue.appendleft(((u, v), [])) # path = [] empty list
        while queue:
            (w, x), path = queue.pop()
            path.append((w, x))
            if x not in resid_adj.keys():
                continue
            for y in resid_adj[x]:
                if y == n: # reached sink
                    path.append((x, y))
                    a = path[0][0]
                    final = [a]
                    for e in path:
                        final.append(e[1])
                    queue = deque()
                    break
                elif (x, y) not in path:
                    tmp = [i for i in path]
                    queue.appendleft(((x, y), tmp))
        path = final.copy()
        final = []
        if not path:
            print('All augmenting paths found. Terminating search')
            break
        else: # there exists a path between source and sink
            u = path[0]
            min_ = float('inf')
            for v in path[1:]:
                min_ = min(min_, resid_caps[u, v])
                u = v
            f = min_
            prev = max_flow
            max_flow += f
            u = path[0]
            for v in path[1:]:
                if (u, v) in edges:
                    flows[u, v] += f
                    resid_caps[u, v] -= f
                else:
                    flows[v, u] -= f
                    resid_caps[v, u] -= f
                u = v
            # update residual graph, tracker
            resid_adj = defaultdict(list)
            for u, v in resid_caps.keys():
                if resid_caps[u, v] > 0:
                    resid_adj[u].append(v)
            for u in resid_adj.keys():
                resid_adj[u].sort(key = lambda v: -1*resid_caps[u, v])
            
    return max_flow, flows

def main():
    n = 6 # no. of vertices
    m = 9 # no. of edges
    data = [(1, 2, 16), (1, 3, 13),\
             (2, 4, 12),\
             (3, 2, 4), (3, 5, 14),\
             (4, 3, 9), (4, 6, 20),\
             (5, 4, 7), (5, 6, 4)]
    edges = []
    caps = {}
    for i in range(m):
        u, v, c = data[i]
        edges.append((u, v))
        caps[u, v] = c
    mf, flows = max_flow(edges, caps, n)
    print('Max Flow:', mf)
    print('Edge\tFlow')
    for e in edges:
        print(f'{e}\t{flows[e]}')

main()
