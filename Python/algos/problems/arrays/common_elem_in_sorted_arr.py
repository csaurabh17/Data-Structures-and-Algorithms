# to find common element in 3 sorted arrays

def find(arr1, arr2, arr3):
    n1 = len(arr1)
    n2 = len(arr2)
    n3 = len(arr3)
    i, j, k = 0, 0, 0
    ans = []
    while i < n1 and j < n2 and k < n3:
        if arr1[i] < arr2[j]:
            i += 1
        if arr2[j] < arr3[k]:
            j += 1
        elif arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            ans.append(arr1[i])
            elem = arr1[i]
            while i < n1 and arr1[i] == elem:
                i += 1
            while j < n2 and arr2[j] == elem:
                j += 1
            while k < n3 and arr3[k] == elem:
                k += 1
        else:
            k += 1

    return ans


ar1 = [1, 5, 10, 20, 40, 80, 80]
ar2 = [6, 7, 20, 80, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 80, 120]

print(find(ar1, ar2, ar3))
