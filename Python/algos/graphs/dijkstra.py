# Shortest path using dijkstra algorithm
import heapq
import sys

adj = {1: [(2, 2), (4, 1)], 2: [(1, 2), (5, 5), (3, 4)], 3: [(2, 4), (4, 3), (5, 1)], 4: [(1, 1), (3, 3)],
         5: [(2, 5), (3, 1)]}


def solve(adj ,V, src):
    h = []
    heapq.heappush(h, (0, src))
    visited = [sys.maxsize] * (V + 1)

    while len(h) > 0:
        dist, node = heapq.heappop(h)
        for i in adj[node]:
            curr_dist, curr_node = i
            if dist + curr_dist < visited[curr_node]:
                visited[curr_node] = dist + curr_dist
                heapq.heappush(h, (dist, curr_node))
    return visited

print(solve(adj, 5, 1))



