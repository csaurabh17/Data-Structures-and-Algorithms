# Searching an element in a rotated sorted array
# [3,4,5,6,0,1,2]

def search_elem(lst, target):
    peak = peak_elem(lst)
    if lst[peak] == target:
        return peak

    res = binary_search(lst, target, peak + 1, len(lst) - 1)
    if res != -1:
        return res
    else:
        return binary_search(lst, target, 0, peak - 1)


def peak_elem(lst):
    start = 0
    end = int(len(lst) - 1)
    while start <= end:
        mid = int(start + (end - start) / 2)
        if mid < end and lst[mid] > lst[mid + 1]:
            return mid
        elif mid > start and lst[mid] < lst[mid + 1]:
            return mid - 1
        elif lst[mid] <= lst[start]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def binary_search(lst, item, start, end):
    is_asc = True
    if lst[start] < lst[end]:
        is_asc = True
    else:
        is_asc = False

    if is_asc:
        while start <= end:
            mid = int(start + (end - start) / 2)
            if item < lst[mid]:
                end = mid - 1
            elif item > lst[mid]:
                start = mid + 1
            else:
                return mid
    else:
        while start <= end:
            mid = int(start + (end - start) / 2)
            if item < lst[mid]:
                start = mid + 1
            elif item > lst[mid]:
                end = mid - 1
            else:
                return mid
    return -1


print(search_elem([3, 4, 5, 6, 0, 1, 2], 4))
print(search_elem([3, 4, 5, 6, 0, 1, 2], 2))
print(search_elem([3, 4, 5, 6, 0, 1, 2], 6))
