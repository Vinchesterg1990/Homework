import time
from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        self.Name = name
        self.power = power
        super().__init__()

    def run(self):
        enemies = 100
        count = 0
        print(f'{self.Name}, на нас напали!')
        while enemies > 0:
            time.sleep(1)
            count += 1
            enemies -= self.power
            if enemies > 0:
                print(f'{self.Name} сражается {count} день(дня)..., '
                      f'осталось {enemies} воинов.')
            else:
                print(f'{self.Name} одержал победу спустя {count} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
time.sleep(0.1)
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы окончились!')
