def find_pass(n):
    res = []
    for first in range(1, n // 2 + 1):
        for second in range(first + 1, n):
            if not n % (first + second):
                res.append([first, second])
    return res


print(find_pass(15))
print(find_pass(20))
