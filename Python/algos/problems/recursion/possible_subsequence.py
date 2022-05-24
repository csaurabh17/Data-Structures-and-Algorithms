# print all possible subsequences of a string

def subseq(processed, unprocessed):
    if not unprocessed:
        final_list = [processed]
        return final_list

    c = unprocessed[0]

    left_list = subseq(processed + c, unprocessed[1:])
    right_list = subseq(processed, unprocessed[1:])

    return left_list + right_list


print(subseq("", "abc"))
