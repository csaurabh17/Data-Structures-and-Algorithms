# to find the longest common substring between 2 strings

def lc_substring(str1, str2, i, j, res):
    if i >= len(str1) or j >= len(str2):
        return res

    if str1[i] == str2[j]:
        return lc_substring(str1, str2, i + 1, j + 1, res + 1)
    else:
        return max(res, lc_substring(str1, str2, i + 1, j, 0), lc_substring(str1, str2, i, j + 1, 0))


print(lc_substring("acjkp", "abcjklp", 0, 0, 0))
