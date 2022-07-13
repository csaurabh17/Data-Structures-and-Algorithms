# https://www.spoj.com/problems/CHOCOLA/

def solve(h_length, v_length, horizontal, vertical):
    horizontal.sort()
    vertical.sort()
    h_count, v_count = 1, 1
    ans = 0
    i, j = h_length - 2, v_length - 2
    while i >= 0 and j >= 0:
        if horizontal[i] >= vertical[j]:
            ans += horizontal[i] * h_count
            v_count += 1
            i -= 1
        elif horizontal[i] < vertical[j]:
            ans += vertical[j] * v_count
            h_count += 1
            j -= 1

    while i >= 0:
        ans += horizontal[i] * h_count
        i -= 1
    while j >= 0:
        ans += vertical[j] * v_count
        j -= 1
    return ans


print(solve(6, 4, [2, 1, 3, 1, 4], [4, 1, 2]))
