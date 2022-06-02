# solving equal sum partition problem
# [1,5,5,11,5]

def equal_sum(p_arr, u_arr):
    print(p_arr, ":", u_arr)
    if not u_arr:
        return False
    if sum(p_arr) == sum(u_arr):
        return True

    return equal_sum(p_arr + [u_arr[0]], u_arr[1:]) or equal_sum([u_arr[0]], u_arr[1:])


# print(equal_sum([], [2, 5, 3, 3, 1]))
print(equal_sum([], [1, 5, 5, 11]))
# print(equal_sum([], [1, 2, 3, 5]))
