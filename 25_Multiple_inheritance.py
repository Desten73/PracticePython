class Horse:
    def __init__(self):
        self._x_distance = 0
        self._sound = "Frrr"
        super().__init__()

    def run(self, dx):
        self._x_distance += dx


class Eagle:
    def __init__(self):
        self._y_distance = 0
        self._sound = "I train, eat, sleep, and repeat"
        super().__init__()

    def fly(self, dy):
        self._y_distance += dy


class Pegasus(Horse, Eagle):
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
