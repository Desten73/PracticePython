from math import pi
from math import sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if self.__is_valid_color(*color):
            self.__color = color
        else:
            self.__color = (1, 1, 1)

        if self.__is_valid_sides(sides):
            self.__sides = [*sides]
        else:
            self.__sides = [1 for i in range(self.sides_count)]

        self.filled = False

    def get_filled(self):
        return self.filled

    def set_filled(self):
        return self.filled

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, *color):
        if self.__is_valid_color(*color):
            self.__color = color

    def __is_valid_sides(self, *new_sides):
        if self.sides_count == 1 and isinstance(new_sides, int):
            return True
        elif not isinstance(new_sides, int) and self.sides_count == len(*new_sides):
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = [*new_sides]


class Circle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = sides[0] / (pi * 2)
        self.sides_count = 1

    def get_square(self):
        return pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        from functools import reduce
        from operator import mul
        p = len(self) / 2
        return sqrt(p * reduce(mul, [p - self.get_sides()[i] for i in range(self.sides_count)]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.__sides = [sides[0] for i in range(self.sides_count)]

    def get_sides(self):
        return self.__sides

    def get_volume(self):
        return pow(self.__sides[0], 3)


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
