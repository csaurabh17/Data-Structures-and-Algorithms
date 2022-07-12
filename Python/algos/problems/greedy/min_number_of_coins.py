# Given a value V, if we want to make a change for V Rs, and we have an infinite supply of each of the denominations
# in Indian currency, i.e., we have an infinite supply of { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes,
# what is the minimum number of coins and/or notes needed to make the change?


def solve(denominations, target):
    denominations.sort(reverse=True)

    min_number_of_coins = 0
    for i in denominations:
        if i <= target:
            target -= i
            min_number_of_coins += 1
        if target <= 0:
            print(min_number_of_coins)
            return


solve([1, 2, 5, 10, 20, 50, 100, 500, 1000], 70)
solve([1, 2, 5, 10, 20, 50, 100, 500, 1000], 121)