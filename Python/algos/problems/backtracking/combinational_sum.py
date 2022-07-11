# Given an array of positive integers arr[] and a sum x, find all unique combinations in arr[] where the sum is equal
# to x. The same repeated number may be chosen from arr[] unlimited number of times. Elements in a combination (a1,
# a2, …, ak) must be printed in non-descending order. (ie, a1 <= a2 <= … <= ak). The combinations themselves must be
# sorted in ascending order, i.e., the combination with smallest first element should be printed first. If there is
# no combination possible the print “Empty” (without quotes).


def solve(arr, n, res):
    if sum(res) == n:
        print(res)
        return
    if sum(res) > n:
        return
    if len(arr) == 0:
        return

    solve(arr, n, res + [arr[0]])
    solve(arr[1:], n, res)


solve([2, 4, 6, 8], 8, [])
