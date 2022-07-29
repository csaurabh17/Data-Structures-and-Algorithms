# (Google) given a number combination eg "1,2" print all possible permutations
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Method 1 - using global number reference
nums = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "node", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


# Method 2 - without using global number reference
def phone_number_permute_with_global(p, up):
    if not up:
        return [p]

    output = []
    digit = int(up[0])
    for i in range((3 * (digit - 1)), 3 * digit):
        output.extend(phone_number_permute_with_global(p + chr(ord("a") + i), up[1:]))
    return output


# phone_number_permute("", "3")
print(phone_number_permute_with_global("", "12"))
# print(chr(ord("b") + 1))
