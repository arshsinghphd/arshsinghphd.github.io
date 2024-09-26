from itertools import product
from collections import deque

def reachability_1(maze, start, end):
    notreached = set([(i, j) for i, j in
                       product(range(len(maze)), range(len(maze[0])))
                       if maze[i][j] == ' '])
    notreached.remove(start)
    reached = {start}
    unexplored = deque([start])
    while unexplored:
        (x, y) = unexplored.pop()
        for (a, b) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if (a, b) == end:
                return 1
            if (a, b) in notreached:
                notreached.remove((a, b))
                reached.add((a, b))
                unexplored.appendleft((a, b))
    return 0

def main():
    start = (0, 1)
    end = (4, 4)
    maze =  [
             'X XXX',
             'X  XX', 
             'XX  X', 
             'XXX X',
             'XXX  ',
             ]
    # convert list of strings to list of list of characters
    maze = [list(maze[i]) for i in range(len(maze))]
    print(reachability_1(maze, start, end))

main()
