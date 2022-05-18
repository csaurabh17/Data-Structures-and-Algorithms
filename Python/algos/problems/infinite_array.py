# finding element in an infinite array

def find_chunk(lst, target):
    start = 0
    end = 1

    while target > lst[end]:
        temp = end + 1
        end = end + (end - start + 1) * 2
        start = temp

    return [start, end]


def search_infinite_array(lst, item):
    start, end = find_chunk(lst, item)
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


print(search_infinite_array([1, 3, 5, 6, 7, 56, 123, 1245, 15321, 21425151, 77777777, 88888888, 99999999 , 999999999999 ], 1245))