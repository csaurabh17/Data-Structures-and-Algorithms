# https://www.geeksforgeeks.org/find-maximum-sum-possible-equal-sum-three-stacks/

def solve(s1, s2, s3):
    sum1, sum2, sum3 = 0, 0, 0
    # find sum of 3 stacks
    for i in s1:
        sum1 += i
    for i in s2:
        sum2 += i
    for i in s3:
        sum3 += i

    while True:
        if sum1 == sum2 == sum3:
            print(sum1)
            return
        if len(s1) == 0 or len(s2) == 0 or len(s3) == 0:
            print("No equal sum")
            return
        if max(sum1, sum2, sum3) == sum1:
            sum1 -= s1[0]
            s1 = s1[1:]
        elif max(sum1, sum2, sum3) == sum2:
            sum2 -= s2[0]
            s2 = s2[1:]
        elif max(sum1, sum2, sum3) == sum3:
            sum3 -= s3[0]
            s3 = s3[1:]


solve([3, 2, 1, 1, 1], [4, 3, 2], [2, 5, 4, 1])
solve([3, 2, 1, 1, 1], [4, 3, 2], [1, 1, 4, 1])
solve([3, 10], [4, 5], [2, 1])
