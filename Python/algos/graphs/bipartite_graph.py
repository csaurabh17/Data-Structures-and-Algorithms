# User function Template for python3

from collections import deque

graph = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1], 3: [0], 4: [2]}


def BFS(adj, V):
    vis_arr = [-1] * V
    res = []
    color = 0
    vis_arr[0] = color
    q = deque()
    q.append(0)

    while len(q) > 0:
        elem = q.popleft()
        color = 1 if color == 0 else 0
        for i in adj[elem]:
            if vis_arr[i] == -1:
                q.append(i)
                vis_arr[i] = color
            else:
                if vis_arr[i] == vis_arr[elem]:
                    return 0
    return 1


def DFS(i, adj, visited, color=0):
    if visited[i] == color:
        return True
    elif visited[i] == -1:
        visited[i] = color
    for elem in adj[i]:
        if visited[i] == -1:
            DFS(elem, adj, visited, 1 if color == 0 else 0)
    return False


def solve_DFS(graph, V):
    visited = [-1] * V
    for i in range(len(visited)):
        if visited[i] == -1:
            if DFS(i, graph, visited):
                return 1
    return 0


print(BFS(graph, 5))

print(solve_DFS(graph, 5))

# before bfs starts , color first node with 0
# while q > 0
# pick first node, traverse aj list, color with alternate number
