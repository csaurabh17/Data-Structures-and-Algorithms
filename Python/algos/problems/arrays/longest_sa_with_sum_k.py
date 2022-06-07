# Longest subarray with sum divisible by K
# Amazon

def longest_subarr(arr, i, j, k):
    if i == j:
        return -1
    summation = sum(arr[i:j + 1])
    if summation % k == 0:
        return len(arr[i:j+1])
    # max_val = 0

    if summation % k > 0:
        max_value = max(longest_subarr(arr, i + 1, j, k), longest_subarr(arr, i, j - 1, k))
    return max_value


print(longest_subarr([2, 7, 6, 1, 4, 5], 0, 5, 3))
print(longest_subarr([-2, 2, -5, 12, -11, -1, 7], 0, 5, 3))

