def get_matrix(*, n: int = 0, m: int = 0, value: int = 0) -> list:
    matrix = []
    if n > 0 and m > 0:
        for row in range(n):
            rows = []
            for col in range(m):
                rows.append(value)
            matrix.append(rows)
    return matrix


result1 = get_matrix(n=2, m=2, value=10)
result2 = get_matrix(n=3, m=5, value=42)
result3 = get_matrix(n=4, m=2, value=13)
print(result1)
print(result2)
print(result3)