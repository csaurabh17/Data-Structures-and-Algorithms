# solving the ninja problem

def ninja(day, last, matrix):
    if day == len(matrix) - 1:
        maxi = 0
        for i in range(len(matrix[day])):
            if i != last:
                maxi = max(maxi, matrix[day][i])
        return maxi

    maxi = 0
    for i in range(len(matrix[day])):
        if i != last:
            maxi = max(maxi, matrix[day][i] + ninja(day + 1, i, matrix))

    return maxi


print(ninja(0, -1, [[10, 50, 1], [5, 100, 11], [12, 10, 6]]))
