# https://www.geeksforgeeks.org/k-numbers-difference-maximum-minimum-k-number-minimized/
import sys


def solve(arr, k):
    arr.sort()
    min_diff = sys.maxsize
    for i in range(len(arr) - k - 1):
        min_diff = min(min_diff, arr[i + (k - 1)] - arr[i])

    return min_diff


print(solve([10, 100, 300, 200, 1000, 20, 30], 3))
