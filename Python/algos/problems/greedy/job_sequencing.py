# Given an array of jobs where every job has a deadline and associated profit if the job is finished before the deadline. It is also given that every job takes a single unit of time, so the minimum possible deadline for any job is 1. How to maximize total profit if only one job can be scheduled at a time.

def solve(arr, n):
    arr.sort(reverse=True, key=lambda x: x[2])
    job_sequence_arr = [-1] * n

    for i in range(len(arr)):
        job_seq_idx = arr[i][1] - 1
        while job_sequence_arr[job_seq_idx] != -1:
            job_seq_idx -= 1
        if job_seq_idx >= 0:
            job_sequence_arr[job_seq_idx] = arr[i][0]

    print(job_sequence_arr)


solve([['a', 2, 100],
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]], 3)


