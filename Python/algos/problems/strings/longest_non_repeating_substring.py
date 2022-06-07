# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def longest_sub(s):
    max_val = 0
    str_to_eval = ""
    current_max = 0
    for a in s:
        if a not in str_to_eval:
            str_to_eval += a
            current_max += 1
        else:
            max_val = max(max_val, current_max)
            current_max = 0
            str_to_eval = ""
    return max(current_max, max_val)


print(longest_sub("pwwkew"))
print(longest_sub("bbbbb"))
print(longest_sub("abcabcbb"))