# program to print longest substring without repeating characters


def solve(arr):
    l,r = 0,0
    max_len = 0
    set1 = set()
    n = len(arr)
    while l < n - 1 and r < n - 1:
        if arr[r] not in set1:
            max_len = max(max_len, r - l + 1)
            set1.add(arr[r])
            r += 1
        else:
            while arr[r] in set1:
                if arr[l] in set1:
                    set1.discard(arr[l])
                l += 1
            max_len = max(max_len, r - l + 1)
            set1.add(arr[r])
            r += 1
    return max_len

print(solve("abcaabcdba"))