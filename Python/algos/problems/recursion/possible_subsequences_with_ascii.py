# print all possible subsequences of a string and ascii values

def subseq(processed, unprocessed):
    if not unprocessed:
        print(processed)
        return

    c = unprocessed[0]

    subseq(processed + c, unprocessed[1:])
    subseq(processed, unprocessed[1:])
    subseq(processed + str(ord(c)), unprocessed[1:])


print(subseq("", "abc"))
