from collections import deque


class Solution:

    # Function to detect cycle in an undirected graph.
    def isCycle(self, V, adj):
        # Code here
        visited = set()

        def bfs(i):
            q = deque()
            q.append([i, -1])
            visited.add(i)

            while len(q) > 0:
                node, prev = q.popleft()
                for j in adj[node]:
                    if j not in visited:
                        visited.add(j)
                        q.append([j, node])
                    else:
                        if j != prev:
                            return True
            return False

        for i in range(V):
            if i not in visited:
                if bfs(i):
                    return 1
        return 0

    def isCycleDFS(self, V, adj):
        visited = set()

        def dfs(node, prev):
            visited.add(node)
            if node not in adj:
                return
            for k in adj[node]:
                if k not in visited:
                    dfs(k, node)
                elif k in visited:
                    if k != prev:
                        return True
                    # else:
                    #     dfs(k, node)
            return False

        for i in range(V):
            if i not in visited:
                if dfs(i, -1):
                    return 1
        return 0

# graph = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1], 3: [0], 4: [2]}
graph = {0: {1}, 1: {0, 2, 4}, 2: {1, 3}, 3:{2, 4}, 4:{1, 3}}
graph = {0: {}, 1: {2}, 2: {1, 3}, 3:{2}}
# print(Solution().isCycle(5, graph))
print(Solution().isCycleDFS(5, graph))