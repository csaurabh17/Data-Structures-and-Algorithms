# doing binary search using recursion

def binary_search(lst, start, end, target):
    mid = int(start + (end - start) / 2)

    if start >= end and mid >= len(lst):
        return -1

    if target == lst[mid]:
        return mid
    else:
        if target < lst[mid]:
            return binary_search(lst, start, mid - 1, target)
        elif target > lst[mid]:
            return binary_search(lst, mid + 1, end, target)


print(binary_search([0, 1, 2, 3, 4], 0, 5, 2))
