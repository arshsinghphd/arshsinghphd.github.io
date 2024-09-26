def brute_force(maze, start, end):
    paths = [[start]]
    while paths:
        path = paths.pop()
        (x, y) = path[-1]
        for (a, b) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if (a, b) == end:
                return 1
            elif (0 <= a < len(maze) and 0 <= b < len(maze[0]) and
                  (a, b) not in path and maze[a][b] == ' '):
                path.append((a, b))
                paths = [path] + paths
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
    print(brute_force(maze, start, end))

main()
