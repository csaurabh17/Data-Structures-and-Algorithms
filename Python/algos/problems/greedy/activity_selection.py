# You are given n activities with their start and finish times. Select the maximum number of activities that can be
# performed by a single person, assuming that a person can only work on a single activity at a time.


def solve(arr):
    # sort the array of tuples according to finish time
    arr.sort(key=lambda x: x[1])

    total_activities = 1
    print("First activity picked : ", arr[0])
    finish_time_to_compare = arr[0][1]
    for i in range(1, len(arr)):
        if arr[i][0] >= finish_time_to_compare:
            print("Next activity picked : ", arr[i])
            total_activities += 1
            finish_time_to_compare = arr[i][1]

    print("total number of activities picked : ", total_activities)


solve([(5, 9), (1, 4), (3, 5), (0, 6), (5, 7), (3, 8),
       (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)])

