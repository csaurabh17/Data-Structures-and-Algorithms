# A Maze is given as N*N binary matrix of blocks where source block is the upper left most block i.e., maze[0][0] and
# destination block is lower rightmost block i.e., maze[N-1][N-1]. A rat starts from source and has to reach the
# destination. The rat can move only in two directions: forward and down.

res = [[0] * 4 for i in range(4)]


def solve(maze, i, j):
    if i == len(maze) - 1 and j == len(maze[len(maze) - 1]):
        res[i][j] = 1
        return res
    if maze[i][j] == 0:
        return False
    if maze[i][j] == 1:
        res[i][j] = 1
        
    if i < len(maze) - 1:
        solve(maze, i + 1, j)
    if j < len(maze[i]) - 1:
        solve(maze, i, j + 1)


solve([[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]], 0, 0)
print(res)
