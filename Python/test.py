
def char_count(s):
    if len(s) == 0:
        print(0)
        return
    if len(s) == 1:
        print(s + str(1))
        return
    output = ""
    i = 0
    while i < len(s):
        curr_char = s[i]
        c = 0
        break_flag = False
        while not break_flag and i < len(s):
            if s[i] == curr_char:
               c += 1
               i += 1
            else:
                break_flag = True
        output += curr_char + str(c)
    print(output)


char_count("aaaa")
# char_count("a")
char_count("aabaaa")
# char_count("aa")

'''
* For a string input the function returns output encoded as follows:
 *
 * "a"     -> "a1"
 * "aa"    -> "a2"
 * "aabbba" -> "a2b3a1"
 '''

