class Horse:
    _x_distance = 0
    _sound = "Frrr"

    def run(self, dx):
        self._x_distance += dx


class Eagle:
    _y_distance = 0
    _sound = "I train, eat, sleep, and repeat"

    def fly(self, dy):
        self._y_distance += dy


class Pegasus(Eagle, Horse):
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self._x_distance, self._y_distance

    def voice(self):
        print(self._sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
