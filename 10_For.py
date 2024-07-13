numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []

for number in numbers[1:]:
    is_prime = True
    for div in range(2, number):
        if (number / div).is_integer():
            is_prime = False
            break
    if is_prime:
        prime.append(number)
    else:
        not_prime.append(number)

print("Prime:", prime)
print("Not Prime:", not_prime)
