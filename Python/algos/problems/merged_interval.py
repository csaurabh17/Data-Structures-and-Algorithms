def merge_interval(arr):
    arr.sort()

    temp_interval = arr[0]
    final_arr = []

    for i in range(1, len(arr)):
        if arr[i][0] <= temp_interval[1]:
            temp_interval[1] = arr[i][1]
            final_arr.append(temp_interval)
        else:
            final_arr.append(arr[i])

    return final_arr


print(merge_interval([[1, 3], [2, 4], [5, 8]]))
