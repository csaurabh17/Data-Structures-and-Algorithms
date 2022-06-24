# Searching in an array where adjacent differ by at most k
import math


def search(arr, k, x):
    i = 0

    while i < len(arr):
        step_count = math.ceil(abs((x - arr[i]) / k))
        if arr[i] == x:
            return i
        i += step_count


print(search([4, 5, 6, 7, 6], 1, 6))
print(search([20, 40, 50, 70, 70, 60], 20, 60))
