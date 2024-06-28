# Реализуйте класс House, объекты которого будут создаваться следующим образом:
# House('ЖК Эльбрус', 30)
# Объект этого класса должен обладать следующими атрибутами:
# self.name - имя, self.number_of_floors - кол-во этажей
# Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
# Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
# Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".
# Пункты задачи:
# Создайте класс House.
# Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
# Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
# Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
# Создайте объект класса House с произвольным названием и количеством этажей.
# Вызовите метод go_to у этого объекта с произвольным числом.
class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors


    def __len__(self):
        return self.numbers_of_floors


    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.numbers_of_floors}')


    def __eq__(self, other):
        return self.numbers_of_floors == other.numbers_of_floors


    def __add__(self, values):
        self.numbers_of_floors = self.numbers_of_floors + values
        return self


    def __iadd__(self, values):
        self.numbers_of_floors += values
        return self
        

    def __radd__(self, values):
        self.numbers_of_floors = values + self.numbers_of_floors
        return self


    def __gt__(self, other):
        return self.numbers_of_floors > other.numbers_of_floors
        

    def __ge__(self, other):
        return self.numbers_of_floors >= other.numbers_of_floors


    def __lt__(self, other):
        return self.numbers_of_floors < other.numbers_of_floors


    def __le__(self, other):
        return self.numbers_of_floors <= other.numbers_of_floors


    def __ne__(self, other):
        return self.numbers_of_floors != other.numbers_of_floors


    def go_to (self, new_floor):
        for i in range(1, new_floor + 1):
            if new_floor <= self.numbers_of_floors and new_floor > 0:
                print(i)
            else:
                print('Такого этажа не существует')
                break


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
