# Given a valid sentence without any spaces between the words and a dictionary of valid English words,
# find all possible ways to break the sentence into individual dictionary words.

def solve(word, dictionary, output):
    if output in dictionary:
        print(output)
    if len(word) == 0:
        return

    c = word[0]

    solve(word[1:], dictionary, output + c)
    solve(word[1:], dictionary, output)


solve("ilovesamsungmobile", ["i", "love", "samsung", "mobile"], "")
