# finding missing number in [0,n] array using cyclic sort
# [3, 0, 1]

def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp
    return lst


def cyclic_sort(lst):
    i = 0
    while i < len(lst):
        if lst[i] >= len(lst):
            i += 1
        elif lst[i] != lst[lst[i]]:
            swap(lst, i, lst[i])
        else:
            i += 1

    for i in range(len(lst)):
        if i != lst[i]:
            return i


print(cyclic_sort([3, 0, 1]))
