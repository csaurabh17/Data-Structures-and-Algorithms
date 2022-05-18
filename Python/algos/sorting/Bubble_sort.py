def bubble_sort(ls):
    for i in range(len(ls) - 1, 0, -1):
        for j in range(i):
            if ls[j] > ls[j + 1]:
                temp = ls[j]
                ls[j] = ls[j+1]
                ls[j+1] = temp
    return ls


print(bubble_sort([4, 6, 2, 1, 2]))
