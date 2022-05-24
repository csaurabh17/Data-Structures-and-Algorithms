# skip a target character in the string using recursion

def skip_char(text, index, target, ans):
    arr = list(text)

    if index == len(arr) - 1:
        return ans
    if index < len(arr):
        if arr[index] != target:
            ans += arr[index]
        return skip_char(arr, index + 1, target, ans)


print(skip_char("Saurabh", 0, 'a', ""))
