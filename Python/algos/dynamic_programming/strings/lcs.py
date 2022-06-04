# to find the longest common subsequence between 2 strings
# 2. print the longest common subsequences between 2 strings


def lcs(i, j, str1, str2):
    if i < 0 or j < 0:
        return 0

    if str1[i] == str2[j]:
        return 1 + lcs(i - 1, j - 1, str1[:i], str2[:j])

    return 0 + max(lcs(i - 1, j, str1[:i], str2), lcs(i, j - 1, str1, str2[:j]))


def print_lcs(i, j, str1, str2):
    if i < 0 or j < 0:
        return ""

    if str1[i] == str2[j]:
        return str1[i] + print_lcs(i - 1, j - 1, str1[:i], str2[:j])

    return max(print_lcs(i - 1, j, str1[:i], str2), print_lcs(i, j - 1, str1, str2[:j]))


print(lcs(2, 2, "abc", "abcd"))
print(print_lcs(2, 2, "abc", "abcd"))
