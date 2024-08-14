from threading import Thread
import time

class Knight(Thread):
    def __init__(self, name, power, enemies = 100):
        self.Name = name
        self.power = power
        self.enemy = enemies
        super().__init__()

    def run(self):
        print(f'{self.Name}, на нас напали!')
        count = 0
        while self.enemy != 0:
            self.enemy = self.enemy - self.power
            count = count + 1
            print(f'{self.Name} сражается {count} дней, осталось {self.enemy} воинов.')
            time.sleep(1)
        print(f'{self.Name} одержал победу спустя {count} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились')

