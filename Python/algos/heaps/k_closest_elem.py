# program to figure out the k closest element to a value x in list
import heapq


def solve(arr, k, x):
    h = []
    for i in arr:
        heapq.heappush(h, (-abs(x - i), i))
        if len(h) > k:
            heapq.heappop(h)
    return h


print(solve([5, 6, 7, 8, 9], 3, 7))
