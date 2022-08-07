# User function Template for python3

from collections import deque

graph = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1], 3: [0], 4: [2]}


def solve(adj, V):
    vis_arr = set()
    res = []

    for i in range(V):
        if i not in vis_arr:
            queue = deque()
            queue.append(i)
            while len(queue) > 0:
                elem = queue.popleft()
                res.append(elem)
                vis_arr.add(elem)
                for j in range(len(adj[elem])):
                    if j not in vis_arr:
                        queue.append(adj[elem][j])
    return res


print(solve(graph, 5))
