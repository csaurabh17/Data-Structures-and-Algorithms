# https://www.geeksforgeeks.org/fractional-knapsack-problem/

def solve(arr, v):
    for i in range(len(arr)):
        arr[i].append(arr[i][0]/arr[i][1])

    arr.sort(reverse=True, key=lambda x:x[2])

    total_profit = 0
    for i in range(len(arr)):
        if v >= arr[i][1]:
            total_profit += arr[i][0]
            v = v - arr[i][1]
        elif 0 < v < arr[i][1]:
            total_profit += int(v/arr[i][1] * arr[i][0])
            v = v - ((v/arr[i][1]) * arr[i][1])
    print(total_profit)


solve([[100, 20], [60, 10], [120, 30]], 50)