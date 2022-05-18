# to find the greatest number smaller or equal to a specific number in a sorted arr

def find_num(lst, target):
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = int(start + (end - start) / 2)
        if target < lst[mid]:
            end = mid - 1
        elif target > lst[mid]:
            start = mid + 1
        else:
            break

    return lst[end]


print(find_num([2, 3, 5, 9, 14, 16, 18], 14))
print(find_num([2, 3, 5, 9, 14, 16, 18], 4))
print(find_num([2, 3, 5, 9, 14, 16, 18], 15))
