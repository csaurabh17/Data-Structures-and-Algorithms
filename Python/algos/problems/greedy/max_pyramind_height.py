# Find maximum height pyramid from the given array of objects
# Given n objects, with each object has width wi. We need to arrange them in a pyramidal way such that :
#
#
# Total width of ith is less than (i + 1)th.
# Total number of objects in the ith is less than (i + 1)th.

def solve(arr):
    levels = 0
    counter = 0
    while levels < len(arr):
        levels += 2
        counter += 1
    print(counter)


solve([40, 100, 20, 30])
solve([10, 20, 30, 50, 60, 70])
