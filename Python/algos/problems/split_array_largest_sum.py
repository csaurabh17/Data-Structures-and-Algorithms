# split array into m pieces, minimizing the largest sum of all the combinations
# [7, 2, 5, 8, 10] m =2

def binary_search(lst, partitions):
    start = 0
    end = 0
    for i in range(len(lst)):
        start = max(start, lst[i])
        end += lst[i]

    while start < end:
        mid = int(start + (end - start) / 2)
        total = 0
        chunks = 1

        for i in lst:
            if i + total > mid:
                chunks += 1
                total = i
            elif i + total <= mid:
                total += i

        if chunks > partitions:
            start = mid + 1
        else:
            end = mid

    return end


print(binary_search([7, 2, 5, 8, 10], 2))
