# implement bubble sort using recursion

def bubble_sort(arr, i, end):
    if end == 0:
        return arr
    if i == end:
        bubble_sort(arr, 0, end - 1)
    elif i < end:
        if arr[i] > arr[i + 1]:
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp
        bubble_sort(arr, i + 1, end)
    return arr


print(bubble_sort([7, 3, 5, 6, 1, 0], 0, 5))
