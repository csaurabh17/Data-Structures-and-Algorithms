# https://leetcode.com/problems/search-insert-position/

def binary_search(lst, item):
    start = 0
    end = int(len(lst) - 1)
    is_asc = True

    if lst[start] <= lst[end]:
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
            elif item != lst[mid] and start == end:
                if item < lst[mid]:
                    return 0
                else:
                    return 1
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
    return end + 1

# [1,3,5,6] target = 2


print(binary_search([1], 0))
print(binary_search([1, 3, 5, 6], 5))
