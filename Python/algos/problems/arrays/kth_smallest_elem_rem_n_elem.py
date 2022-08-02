# K-th smallest element after removing some integers from natural numbers

n = 10000


def solve(arr, k):
    res_arr = [0] * n
    for i in arr:
        res_arr[i] = 1

    for i in range(len(res_arr)):
        if res_arr[i] != 1:
            k -= 1
        if k == 0:
            return i + 1


print(solve([1, 3], 4))
