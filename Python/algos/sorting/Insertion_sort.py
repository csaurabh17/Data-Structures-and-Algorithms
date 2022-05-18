def insertion_sort(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while temp < lst[j] and j > -1:
            lst[j + 1] = lst[j]
            lst[j] = temp
            j -= 1
    return lst


print(insertion_sort([4, 6, 2, 1, 2]))
