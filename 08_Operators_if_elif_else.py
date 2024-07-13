# На вход программе подаются 3 целых числа и записываются в переменные
# first, second и third соответственно.
# Ваша задача написать условную конструкцию (из if, elif, else),
# которая выводит кол-во одинаковых чисел среди 3-х введённых.

first, second, third = input("Введите 3 целых числа: ").split()

print("Количество одинаковых чисел: ", end="")

if first == second and second == third:
    print("3")
elif first == second or second == third or first == third:
    print("2")
else:
    print("0")
