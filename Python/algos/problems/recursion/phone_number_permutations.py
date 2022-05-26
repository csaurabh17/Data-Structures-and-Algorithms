# (Google) given a number combination eg "1,2" print all possible permutations
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

nums = {
    "1": ["a", "b", "c"],
    "2": ["d", "e", "f"]
}


def phone_number_permute(p, up):
    if not up:
        print(p)
        return

    processed_num = up[0]
    letters = nums[processed_num]
    for i in letters:
        phone_number_permute(p + i, up[1:])


phone_number_permute("", "12")
