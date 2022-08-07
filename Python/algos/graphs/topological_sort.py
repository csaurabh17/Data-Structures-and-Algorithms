class Solution:

    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        stack = []
        visited = set()

        def DFS(i):
            visited.add(i)

            for j in adj[i]:
                if j not in visited:
                    DFS(j)
            stack.append(i)

        for i in range(V):
            if i not in visited:
                DFS(i)

        stack.reverse()
        return stack

