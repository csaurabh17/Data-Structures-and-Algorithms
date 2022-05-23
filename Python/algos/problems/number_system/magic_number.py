# determine nth magic number with base x (Amazon)

def magic_number(num, base):
    ans = 0
    base_initial = base
    while num > 0:
        value = num & 1
        num = num >> 1
        ans += value * base
        base *= base_initial

    return ans


print(magic_number(6, 5))
