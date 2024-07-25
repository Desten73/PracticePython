def get_multiplied_digits(number):
    return int(str(number)[0]) * get_multiplied_digits(int(str(number)[1:])) \
        if number > 9 else max(number, 1)


result = get_multiplied_digits(40203)
print(result)

