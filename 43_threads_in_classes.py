from time import sleep
from threading import Thread

class Knight(Thread):
    def __init__(self, name, power):
        self.__name = name
        self.__power = power
        super().__init__()

    def run(self):
        enemy = 100
        day = 0
        print(f"{self.__name}, на нас напали!")
        while enemy:
            enemy -= self.__power
            day += 1
            print(f"{self.name} сражается {day} дней(дня)..., осталось {enemy} воинов.")
            sleep(1)
        print(f"{self.__name} одержал победу спустя {day} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")
