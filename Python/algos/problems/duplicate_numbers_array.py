# Finding duplicate numbers in array [1,node] using cycle sort

def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp
    return lst


def cycle_sort(lst):
    start = 0
    duplicate_lst = []

    while start < len(lst):
        if lst[start] != lst[lst[start] - 1]:
            swap(lst, start, lst[start] - 1)
        else:
            start += 1

    for i in range(len(lst)):
        if i + 1 != lst[i]:
            duplicate_lst.append(lst[i])

    return duplicate_lst


print(cycle_sort([4, 3, 2, 7, 8, 2, 3, 1]))
