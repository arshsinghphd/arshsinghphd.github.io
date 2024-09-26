from itertools import product
from collections import deque
import numpy as np

def reachability(maze, start, end):
    find = np.zeros(len(maze) * len(maze[0])).reshape((len(maze),
                                                       len(maze[0])))                                      
    unexplored = deque([start])
    while unexplored:
        (x, y) = unexplored.pop()
        find[x][y] = 1
        for (a, b) in [(x + 1, y), (x - 1, y),
                       (x, y + 1), (x, y - 1)]:
            if (a, b) == end:
                find[a][b] = 1
                return 1
            if (0 <= a < len(maze) and 0 <= b < len(maze[0]) and
                maze[a][b] == ' ' and find[a][b] != 1):
                find[a][b] = 1
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
    print(reachability(maze, start, end))
        
main()
