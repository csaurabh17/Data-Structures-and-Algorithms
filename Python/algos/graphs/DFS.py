from collections import deque

res = []


def dfs(i, vis, graph):
    res.append(i)
    vis.add(i)
    for j in graph[i]:
        if j not in vis:
            dfs(j, vis, graph)


def solve(graph, V):
    vis = set()

    for i in range(V):
        if i not in vis:
            dfs(i, vis, graph)

    return res

graph = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1], 3: [0], 4: [2]}
print(solve(graph, 5))
