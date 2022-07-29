import heapq


def solve(arr, k):
    h = []
    for i in range(len(arr)):
        heapq.heappush(h, -1 * arr[i])
        if len(h) > k:
            heapq.heappop(h)
    return - 1 * heapq.heappop(h)


print(solve([7, 10, 4, 3, 20, 15], 3))
