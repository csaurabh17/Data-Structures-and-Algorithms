# https://www.codingninjas.com/codestudio/problem-details/frog-jump_3621012
# additionally with 1 till k steps

import sys


def jump(arr, current_index, prev_index, k):
    if current_index == len(arr) - 1:
        return abs(arr[current_index] - arr[prev_index])

    min_value = sys.maxsize
    for i in range(1, k + 1):
        if prev_index + i <= len(arr) - 1:
            min_value = min(min_value, jump(arr[i:], prev_index + i, prev_index, k))

    return min_value


print(jump([10, 20, 30, 10], 0, 0, 2))
