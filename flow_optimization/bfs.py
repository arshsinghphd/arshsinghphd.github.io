'''
Implementing BFS to gather all paths in a network
'''

from collections import deque

def bfs(edges, n):
    adj = {}
    for (u, v) in edges:
        if u not in adj.keys():
            adj[u] = [v]
        else:
            adj[u].append(v)
        
    # find all paths from source (1) to sink (n) in adj using BFS
    all_paths = []
    for v in adj[1]:
        queue = deque()
        queue.append(((1, v),[]))
        while queue:
            (w, x), path = queue.pop()
            path.append((w, x))
            if x not in adj.keys():
                continue
            for y in adj[x]:
                if y == n: # reached sink
                    path.append((x, y))
                    a = path[0][0]
                    final = [a]
                    for e in path:
                        final.append(e[1])
                    if final not in all_paths:
                        all_paths.append(final)
                    continue
                elif (x, y) not in path:
                    tmp = [i for i in path]
                    queue.appendleft(((x,y), tmp))
                    
    return all_paths

def main():
    n = 6 # no. of vertices
    m = 9 # no. of edges
    data = [(1, 2), (1, 3),\
             (2, 4),\
             (3, 2), (3, 5),\
             (4, 3), (4, 6),\
             (5, 4), (5, 6)]
    edges = []
    for i in range(m):
        u, v = data[i]
        edges.append((u, v))

    all_path = bfs(edges, n)
    for path in all_path:
        print(path)

main()
