import heapq as hq


def solve(arr, k):
    h = []
    res = []

    for i in arr:
        hq.heappush(h, i)
        if len(h) > k:
            res.append(hq.heappop(h))

    return res + h


print(solve([6, 5, 3, 2, 8, 10, 9], 3))
print(solve([6, 7, 8, 2, 3, 4, 5], 3))
