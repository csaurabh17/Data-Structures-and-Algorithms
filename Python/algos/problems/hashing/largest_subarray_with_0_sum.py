# program to find the largest subarray with 0 sum
import sys


def solve(arr):
    s = 0
    max_val = -sys.maxsize
    d = {}

    for i in range(len(arr)):
        s += arr[i]
        if s == 0:
            if max_val == -sys.maxsize:
                max_val = i + 1
        elif s not in d:
            d[s] = i
        elif s in d:
            max_val = max(max_val, abs(d[s] - i))
    return max_val


print(solve([1, -1, 3, 2, -2, -8, 1, 7, 10, 23]))
