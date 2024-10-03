def is_prime(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        if n % 2 == 0:
            print("Составное")
            return n
        d = 3
        while d * d <= n and n % d != 0:
            d += 2
        res = d * d > n
        print("Простое" if res else "Составное")
        return n
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
