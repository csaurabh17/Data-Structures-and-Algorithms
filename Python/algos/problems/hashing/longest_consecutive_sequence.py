# program to find longest conesecutive sequence in an arr


def solve(arr):
    max_val = -1
    arr_dict = {}

    for i in arr:
        arr_dict[i] = 0

    for i in range(len(arr)):
        if arr[i] - 1 in arr_dict:
            continue
        else:
            counter = 1
            while True:
                if arr[i] + counter in arr_dict:
                    counter += 1
                else:
                    max_val = max(max_val, counter)
                    break
    return max_val


print(solve([102, 4, 100, 1, 101, 3, 2]))