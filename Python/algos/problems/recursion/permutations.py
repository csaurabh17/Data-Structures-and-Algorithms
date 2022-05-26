# determine all permutations of a string using recursion

def permutations(processed, unprocessed):
    if not unprocessed:
        print(processed)
        return

    for i in range(len(processed) + 1):
        c = unprocessed[0]
        f = processed[:i]
        l = processed[i:]
        permutations(f + c + l, unprocessed[1:])


def permutations_count(processed, unprocessed):
    if not unprocessed:
        return 1

    count = 0

    for i in range(len(processed) + 1):
        c = unprocessed[0]
        f = processed[:i]
        l = processed[i:]
        count += permutations_count(f + c + l, unprocessed[1:])

    return count


permutations("", "abcd")
print(permutations_count("", "abcd"))
