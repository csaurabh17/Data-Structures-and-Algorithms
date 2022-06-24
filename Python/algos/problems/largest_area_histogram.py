# https://leetcode.com/problems/largest-rectangle-in-histogram/

def find(arr):
    max_area = 1
    for i in range(len(arr)):
        # get current height
        current_height = arr[i]
        current_area = current_height
        summation = current_area
        # run loop from index to end checking for rectangles <= equal area
        for j in range(i + 1, len(arr)):
            if arr[j] >= arr[i]:
                summation += current_area
            else:
                break

        # run loop from index to 0 checking for rectangles <= equal area
        for j in reversed(range(i)):
            if arr[j] >= arr[i]:
                summation += current_area
            else:
                break

        max_area = max(max_area, summation)
    return max_area


print(find([2, 1, 5, 6, 2, 3]))
print(find([2, 4]))
