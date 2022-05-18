def binary_search(lst, item):
    start = 0
    end = int(len(lst) - 1)
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


# for ascending list
print(binary_search([3, 4, 6, 7, 10], 4))

# for descending list
print(binary_search([10, 9, 8, 7, 6], 6))

# for item not in list
print(binary_search([10, 9, 8, 7, 6], 12))
