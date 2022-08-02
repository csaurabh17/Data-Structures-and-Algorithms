# https://www.geeksforgeeks.org/count-distinct-elements-in-every-window-of-size-k/

def solve(arr , k):
    d = {}
    n = len(arr)
    for i in range(k):
        d[arr[i]] = d.get(arr[i], 0) + 1
    print(len(d), end = " ")
    for i in range(k, n):
        if d.get(arr[i - k], 0) > 0:
            d[arr[i - k]] -= 1
        else:
            d.pop(arr[i - k])

        d[arr[i]] = d.get(arr[i], 0) + 1
        print(len(d), end = " ")


solve([1, 2, 1, 3, 4, 2, 3], 4)