# Wildcard string matching for * and ?

def match(w, s, i, j):
    if i < 0 and j < 0:
        return True
    if j < 0 <= i and w[j + 1] == '*':
        return True
    if j < 0:
        return False
    if i < 0 :
        return False

    if s[i] == w[j] or w[j] == "?":
        return match(w, s, i - 1, j - 1)
    elif s[i] != w[j] and w[j] == "*":
        return match(w, s, i, j - 1) or match(w, s, i - 1, j - 1) or match(w, s, i - 1, j)

    return False


print(match("?abc", "asfasfabc", 8, 2))
