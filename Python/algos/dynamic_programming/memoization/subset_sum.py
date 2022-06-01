# Google question -https://leetcode.com/discuss/interview-question/1279773/google-interview-question-array-subset-sum
# -equals-k

matrix = [[[[None] * (9 + 1) for i in range(5 + 1)]]]


def subset_sum(arr, total):
    n = len(arr)
    if n == 0 and total == 0:
        return True
    if n == 0 and total > 0:
        return False

    # if arr[n - 1] == total:
    #     return True

    if arr[n - 1] <= total:
        matrix[n][total] = subset_sum(arr[:-1], total - arr[n - 1]) or subset_sum(arr[:-1], total)
    else:
        matrix[n][total] = subset_sum(arr[:-1], total)


print(subset_sum([2, 3, 7, 8, 10], 9))
