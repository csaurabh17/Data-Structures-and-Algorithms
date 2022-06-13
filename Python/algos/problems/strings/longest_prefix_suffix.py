# Given a string of characters, find the length of the longest proper prefix which is also a proper suffix.

def find_prefix_suffix(s):
    first_letter = s[0]

    occurrence = 1
    i = 0
    res = ""
    try:
        j = s.index(first_letter, occurrence)
        while j <= len(s) - 1:
            if s[i] == s[j]:
                res += s[j]
                i += 1
                j += 1
            else:
                occurrence += 1
                j = s.index(first_letter, occurrence)
                i = 0
                res = ""
        return res
    except ValueError:
        return res


print(find_prefix_suffix("abcdab"))
print(find_prefix_suffix("aaaa"))





