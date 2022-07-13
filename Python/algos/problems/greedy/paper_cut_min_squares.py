# https://www.geeksforgeeks.org/paper-cut-minimum-number-squares/


def solve(a, b):
    number_of_cuts = 0
    while a > 1 or b > 1:
        curr = min(a, b)
        max_cut = max(a, b)

        cut_size = max_cut % curr
        number_of_cuts += int(max_cut/curr)

        a = cut_size
        b = curr

    return number_of_cuts


print(solve(13, 29))
print(solve(4, 5))
