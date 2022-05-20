# sort a list in O(n) from range 1 to n
# [3,5,2,1,4]

def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp
    return lst


def cyclic_sort(lst):
    start = 0
    while start < len(lst):
        if lst[start] != lst[lst[start] - 1]:
            swap(lst, start, lst[start] - 1)
        else:
            start += 1
    return lst


print(cyclic_sort([3, 5, 2, 1, 4]))
