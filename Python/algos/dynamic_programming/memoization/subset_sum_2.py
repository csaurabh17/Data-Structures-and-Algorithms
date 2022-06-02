# Google question -https://leetcode.com/discuss/interview-question/1279773/google-interview-question-array-subset-sum
# -equals-k


# using for loops
def subset_sum(arr, n):
    if n == 0:
        return True
    if not len(arr) and n != 0:
        return False

    for i in range(len(arr)):
        return subset_sum(arr[1:], n - arr[0]) or subset_sum(arr[1:], n)


# without using for loop
def subset_sum_without_looping(arr, n):
    if n == 0:
        return True
    if not len(arr) and n != 0:
        return False

    return subset_sum_without_looping(arr[1:], n - arr[0]) or subset_sum_without_looping(arr[1:], n)


print(subset_sum([2, 3, 7, 8, 10], 13))
print(subset_sum_without_looping([2, 3, 7, 8, 10], 13))
