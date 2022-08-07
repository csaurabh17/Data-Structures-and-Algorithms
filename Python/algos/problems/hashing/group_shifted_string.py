# https://www.geeksforgeeks.org/group-shifted-string/

def appendkey(s):
    key = "0"
    for i in range(1, len(s)):
        diff = ord(s[i]) - ord(s[i - 1])
        if diff < 0:
            diff += 26
        key += str(diff)
    return key


def solve(arr):
    d = {}
    for i in arr:
        key = appendkey(i)
        if key in d:
            d[key].append(i)
        else:
            d[key] = [i]
    for i in d:
        print(d[i])


solve(["acd", "dfg", "wyz", "yab", "mop",
       "bdfh", "a", "x", "moqs"])
