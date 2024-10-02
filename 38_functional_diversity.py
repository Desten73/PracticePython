import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

res = list(map(lambda x, y: x == y, first, second))
print(res)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding="utf-8") as file:
            for words in data_set:
                file.write(str(words)+'\n')
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.__words = words

    def __call__(self):
        from random import choice
        return choice(self.__words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
