# determine the unique element in array using number systems

def unique(lst):
    unique_elem: int = 0
    for l in lst:
        unique_elem ^= l
    return unique_elem


print(unique([2, 4, 2, 4, 3, 6, 6, 8, 8]))
