def print_params(a=1, b="строка", c=True):
    print(f"{a=}, {b=}, {c=}")


print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [False, [2, 5, 8], 3.5]
values_dict = {'a': 5.7,
               'b': None,
               'c': [3, 6, 5]}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [None, "Test"]
print_params(*values_list_2, 42)
