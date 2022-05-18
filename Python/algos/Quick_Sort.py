def swap(lst, i1, i2):
    temp = lst[i1]
    lst[i1] = lst[i2]
    lst[i2] = temp
    return lst


def pivot(lst, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if lst[i] < lst[pivot_index]:
            swap_index += 1
            swap(lst, swap_index, i)
    swap(lst, pivot_index, swap_index)
    return swap_index


def quick_sort(lst, left, right):
    if left < right:
        pivot_index = pivot(lst, left, right)
        quick_sort(lst, left, pivot_index - 1)
        quick_sort(lst, pivot_index + 1, right)
    return lst


# print(quick_sort([4, 3, 6, 1, 2], 0, 5))

print(min(max(True,-3,-4),2,7))
print(min(max(False,0,0),2,7))
print(all([3,0,4,2]))