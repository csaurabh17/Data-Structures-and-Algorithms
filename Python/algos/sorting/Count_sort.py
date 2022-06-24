# to perform counting sort on an array


def count_sort(arr):
    # store the array value frequencies in a new array of range 0-9 (simplicity)
    freq_arr = [0] * 10
    places_arr = [0] * len(arr)

    for i in range(len(arr)):
        freq_arr[arr[i]] += 1

    # summation of previous elements in freq array
    for i in range(1, len(freq_arr)):
        freq_arr[i] += freq_arr[i - 1]

    # storing value in places arr
    for i in range(len(arr)):
        places_arr[freq_arr[arr[i]] - 1] = arr[i]
        freq_arr[arr[i]] -= 1

    return places_arr


print(count_sort([1, 4, 1, 2, 7, 5, 2]))
