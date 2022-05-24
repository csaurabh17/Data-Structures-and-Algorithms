# return array list of a target number using recursion

def check_occurrence(arr, target, index, result_list: list):
    if index == len(arr):
        return result_list
    if arr[index] == target:
        result_list.append(arr[index])

    return check_occurrence(arr, target, index + 1, result_list)


print(check_occurrence([1, 2, 3, 4, 5, 4], 3, 0, []))
