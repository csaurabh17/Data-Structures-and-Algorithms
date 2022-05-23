# Check if an array is sorted or not


def is_sorted(arr, current_index):
    if len(arr) - 1 == current_index:
        return True
    elif arr[current_index] > arr[current_index + 1]:
        return False
    else:
        return is_sorted(arr, current_index + 1)


print(is_sorted([0, 1, 2, 3, 4, 4], 0))
