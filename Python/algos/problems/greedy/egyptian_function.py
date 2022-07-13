# https://www.geeksforgeeks.org/greedy-algorithm-egyptian-fraction/

import fractions
import math


def solve(fr):
    fr1 = fractions.Fraction(fr[0], fr[1])
    while fr1 > 0:
        ceiling = math.ceil(fr1.denominator / fr1.numerator)
        fr_ceil = fractions.Fraction(1, ceiling)
        print(fr_ceil, end=" + ")
        fr1 = fr1 - fr_ceil
    print(0)


solve((2, 3))
solve((6, 14))
solve((12, 13))
