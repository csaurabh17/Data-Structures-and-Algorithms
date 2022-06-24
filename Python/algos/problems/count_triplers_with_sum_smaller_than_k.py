# Count triplets with sum smaller than a given value

def count(up, p, k):
    if sum(up) >= k:
        return
    if len(up) == 3:
        print(up)
        return
    if len(p) < 1:
        return

    count(up + [p[0]], p[1:], k)
    count(up, p[1:], k)


count([], [-2, 0, 1, 3], 2)
print("------------")
count([], [5, 1, 3, 4, 7], 12)
