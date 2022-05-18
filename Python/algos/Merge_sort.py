def merge(l1, l2):
    new_arr = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            new_arr.append(l1[i])
            i += 1
        else:
            new_arr.append(l2[j])
            j += 1

    while i < len(l1):
        new_arr.append(l1[i])
        i += 1
    while j < len(l2):
        new_arr.append(l2[j])
        j += 1
    return new_arr


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    mid = int(len(lst) / 2)
    left = lst[:mid]
    right = lst[mid:]
    return merge(merge_sort(left), merge_sort(right))


print(merge_sort([4, 3, 1, 6, 2, 2]))
