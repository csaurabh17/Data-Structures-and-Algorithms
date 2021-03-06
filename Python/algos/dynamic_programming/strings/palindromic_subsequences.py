# determine max of all palindromic subsequences of a string

def palindromic_subsequences(p, up):
    if not up:
        if p == p[::-1]:
            return len(p)
        return 0

    return max(palindromic_subsequences(p + up[0], up[1:]), palindromic_subsequences(p, up[1:]))


print(palindromic_subsequences("", "aabbbaa"))
