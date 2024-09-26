from itertools import product
from collections import deque
import numpy as np

def backTrack(find, start, end):
    unexplored = [end]
    path = []
    while unexplored:
        (x, y) = unexplored.pop()
        path.append((x, y))
        find[x][y] = 2
        for (a, b) in [(x + 1, y), (x - 1, y),
                       (x, y + 1), (x, y - 1)]:
            if (a, b) == start:
                path.append((a, b))
                find[x][y] = 2
                path.reverse()
                return path
            if (0 <= a < len(find) and 0 <= b < len(find[0]) and
                find[a][b] == 1):
                unexplored.append((a, b))
                break

    
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
                path = backTrack(find, start, end)
                return 1, path
            if (0 <= a < len(maze) and 0 <= b < len(maze[0]) and
                maze[a][b] == ' ' and find[a][b] != 1):
                find[a][b] = 1
                unexplored.appendleft((a, b))
    return 0, None

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
    ans, path = reachability(maze, start, end)
    print('Reached!' if ans else 'Not reachable')
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) in path:
                if (i, j) in [start, end]:
                    print('*', end=' ')
                else:
                    print('#', end=' ')
            else:
                print(maze[i][j], end=' ')
        print('')

main()
