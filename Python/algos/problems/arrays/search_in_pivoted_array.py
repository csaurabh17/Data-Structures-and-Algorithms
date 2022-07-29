# An element in a sorted array can be found in O(log node) time via binary search. But suppose we rotate an ascending
# order sorted array at some pivot unknown to you beforehand. So for instance, 1 2 3 4 5 might become 3 4 5 1 2.
# Devise a way to find an element in the rotated array in O(log node) time. Microsoft Google Adobe Amazon D-E-Shaw
# Flipkart Hike Intuit MakeMyTrip Paytm

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


def find_peak_elem(arr, start, end):

    while start <= end:
        mid = int((start + (end - start) / 2))
        if arr[mid] > arr[mid + 1]:
            return mid
        if arr[mid] < arr[mid + 1]:
            start = mid + 1
        elif arr[mid] < arr[mid - 1]:
            return mid
    return -1


def search(arr, target):
    peak = find_peak_elem(arr, 0, len(arr) - 1)

    idx = binary_search(arr, target, 0, peak)

    if idx == -1:
        return binary_search(arr, target, peak + 1, len(arr) - 1)

    return idx


print(search([3, 4, 5, 1, 2], 2))

