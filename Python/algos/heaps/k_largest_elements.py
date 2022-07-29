# https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/

import heapq


def solve(arr, k):
    h = []
    for i in range(len(arr)):
        heapq.heappush(h, arr[i])
        if len(h) > k:
            heapq.heappop(h)
    return h


print(solve([7, 10, 4, 3, 20, 15], 3))
