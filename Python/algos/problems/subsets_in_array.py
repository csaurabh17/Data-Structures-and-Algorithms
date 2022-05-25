# determine all possible subsets in array

def subsets(arr):
    outer = [[]]

    for elem in arr:
        length = len(outer)
        for i in range(len(outer)):
            internal = list.copy(outer[i])
            internal.append(elem)
            outer.append(internal)

    return outer


def subsets_with_duplicates(arr):
    outer = [[]]
    arr.sort()
    for idx in range(len(arr)):
        length = len(outer)
        start = 0
        end = 0
        if idx > 0 and arr[idx] == arr[idx - 1]:
            start = end + 1
        end = len(outer) - 1
        for i in range(start, len(outer)):
            internal = list.copy(outer[i])
            internal.append(arr[idx])
            outer.append(internal)

    return outer


print(subsets([1, 2, 3]))
print(subsets_with_duplicates([1, 3, 2, 3]))
