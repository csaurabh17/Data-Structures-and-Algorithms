# Smallest Window in a String Containing all the Characters of Another String
# WIP

def solve(s, sub_s):
    # storing substring count
    count_s = len(sub_s)
    res = s
    map_s = {}
    i = 0
    j = 0
    # adding count in dict
    for sub in sub_s:
        if sub not in map_s:
            map_s[sub] = 1
        else:
            map_s[sub] += 1

    if s[i] in sub_s:
        map_s[s[i]] = 1

    inner_map = map_s.copy()
    while i < len(s) or j < len(s):
        if count_s == 0:
            res = min(res, s[i : j], key=len)
            if s[i] in inner_map:
                if inner_map[s[i]] < 0:
                    inner_map[s[i]] += 1
                    i += 1
                    count_s += 1
                    continue
                else:
                    res = min(res, s[i : j], key=len)
                    count_s = len(sub_s)
                    continue
            else:
                i += 1
                continue

        if s[j] in inner_map:
            inner_map[s[j]] -= 1
            if inner_map[s[j]] >= 0:
                count_s -= 1
            j += 1
        else:
            j += 1

    return res

print(solve("timetopractice", "toc"))
