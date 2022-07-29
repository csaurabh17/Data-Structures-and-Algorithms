# find duplicate number in  list in O(node) from range 1 to node
# [3,5,2,1,4]

def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp
    return lst


def cyclic_sort(lst):
    start = 0
    while start < len(lst):
        if lst[start] != start + 1:
            if lst[start] != lst[lst[start] - 1]:
                swap(lst, start, lst[start] - 1)
            else:
                return lst[start]
        else:
            start += 1
    return -1


print(cyclic_sort([1, 3, 2, 1, 4, 6]))
