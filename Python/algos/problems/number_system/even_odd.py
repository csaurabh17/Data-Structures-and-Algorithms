# determine whether a number is even or odd using number systems

def even_odd(num):
    if num & 1 == 0:
        return "even"
    else:
        return "odd"


print(even_odd(24))
