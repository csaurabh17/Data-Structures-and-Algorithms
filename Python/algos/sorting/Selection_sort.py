def selection_sort(lst):
    for i in range(len(lst) - 1):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
        if i != min_index:
            temp = lst[i]
            lst[i] = lst[min_index]
            lst[min_index] = temp
    return lst


print(selection_sort([4, 6, 2, 1, 2]))

