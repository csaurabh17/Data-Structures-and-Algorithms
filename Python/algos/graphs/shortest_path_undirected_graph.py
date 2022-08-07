# Shortest Path in Undirected Graph with Unit Weights
import collections

import sys


def solve_bfs(graph, V, src):
    path_arr = [sys.maxsize] * V
    q = collections.deque()

    q.append(src)
    path_arr[src] = min(path_arr[src], 0)

    while len(q) > 0:
        elem = q.popleft()
        path_from_src = path_arr[elem]
        for i in graph[elem]:
            if path_from_src + 1 < path_arr[i]:
                path_arr[i] = path_from_src + 1
                q.append(i)

    return path_arr


graph = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 4], 3: [0], 4: [2]}
print(solve_bfs(graph, 5, 0))
