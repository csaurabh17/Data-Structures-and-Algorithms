# Prims algo for MST


class Solution:

    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        # init 3 arrays
        key = [sys.maxsize] * V
        mst = [False] * V
        parent = [-1] * V

        # first elem is 0
        key[0] = 0

        for i in range(V):

            # iterating the key array to find min index
            min_index = 0
            min_val = sys.maxsize
            for i in range(V):
                if key[i] < min_val and mst[i] == False:
                    min_index = i
                    min_val = key[i]

            # mark mst index of min element
            mst[min_index] = True
            # run a loop of all adj nodes of min key
            for node, weight in adj[min_index]:
                if not mst[node] and key[node] > weight:
                    key[node] = weight
                    parent[node] = min_index

        total_weight = 0
        for i in range(len(key)):
            if mst[i]:
                total_weight += key[i]
        return total_weight