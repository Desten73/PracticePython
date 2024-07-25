def sum_numbers_and_string_len(*args):
    summa = 0
    for data in args:
        if isinstance(data, list):
            for i in range(len(data)):
                summa += sum_numbers_and_string_len(data[i])
        if isinstance(data, tuple):
            for elem in data:
                summa += sum_numbers_and_string_len(elem)
        if isinstance(data, set):
            summa += sum_numbers_and_string_len(*data)
        if isinstance(data, dict):
            summa += sum_numbers_and_string_len(*data.keys())
            summa += sum_numbers_and_string_len(*data.values())
        if isinstance(data, int):
            summa += data
        if isinstance(data, str):
            summa += len(data)
    return summa


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(sum_numbers_and_string_len(*data_structure))
