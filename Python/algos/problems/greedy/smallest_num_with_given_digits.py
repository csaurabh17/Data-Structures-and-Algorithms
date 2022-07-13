# https://www.geeksforgeeks.org/find-smallest-number-with-given-number-of-digits-and-digit-sum/

def solve(total, digits):
    arr, i = [1] * digits, digits - 1
    total -= 1
    while i > 0:
        if total > 9:
            arr[i] = 9
            i -= 1
        else:
            arr[i] = total
            print(arr)
            return


solve(9, 2)
