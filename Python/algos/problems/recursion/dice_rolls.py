# Number of dice rolls with target sum  (Amazon)
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/


def dice_rolls(p, up):
    if up == 0:
        print(p)

    for i in range(1, 7):
        if i <= up:
            dice_rolls(str(p) + str(i), up - i)


dice_rolls("", 4)