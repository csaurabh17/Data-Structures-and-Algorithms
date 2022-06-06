# https://leetcode.com/problems/trapping-rain-water/
import sys


def get_suffix_arr(arr):
    suffix_arr = arr.copy()
    max_value = arr[len(suffix_arr) - 1]
    for i in reversed(range(len(suffix_arr))):
        max_value = max(max_value, suffix_arr[i])
        suffix_arr[i] = max_value
    return suffix_arr


def get_prefix_arr(arr):
    prefix_arr = arr.copy()
    max_value = arr[0]
    for i in range(len(prefix_arr)):
        max_value = max(max_value, prefix_arr[i])
        prefix_arr[i] = max_value

    return prefix_arr


def total_units_stored(arr):
    prefix = get_prefix_arr(arr)
    suffix = get_suffix_arr(arr)

    total_units = 0
    for i in range(len(arr)):
        total_units += min(prefix[i], suffix[i]) - arr[i]

    return total_units


print(total_units_stored([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
