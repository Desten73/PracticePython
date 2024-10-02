first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(res) for res in first_strings if not len(res) < 5]
print(first_result)

second_result = [(res1, res2) for res1 in first_strings for res2 in second_strings if len(res1) == len(res2)]
print(second_result)

third_result = {res: len(res) for res in first_strings + second_strings if not len(res) % 2}
print(third_result)
