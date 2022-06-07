# Find Minimum Number of Merge Operations to Make an Array Palindrome
# Amazon

def merge(arr, start_index, end_index):
    arr[start_index] = arr[start_index] + arr[end_index]
    arr.pop(end_index)
    return arr


def make_arr_palindrome(arr):
    i = 0
    j = len(arr) - 1
    count = 0
    while i < j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        elif arr[i] > arr[j]:
            arr = merge(arr, j - 1, j)
            i += 1
            count += 1
        elif arr[i] < arr[j]:
            arr = merge(arr, i, i + 1)
            j -= 1
            count += 1
    return count


print(make_arr_palindrome([1, 4, 5, 1]))
print(make_arr_palindrome([11, 14, 15, 99]))
print(make_arr_palindrome([15, 4, 15]))
