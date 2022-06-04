# to find the minimum and maximum element in an array using minimal comparisons
import sys


def find_min_max(arr):
    min_ele = sys.maxsize
    max_ele = -sys.maxsize - 1
    for i in range(len(arr)):
        min_ele = min(min_ele, arr[i])
        max_ele = max(max_ele, arr[i])
    return min_ele, max_ele


print(find_min_max([-1, 3, 2, 9]))
