'''
Создать класс Car.
Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5), стоп (сброс скорости на 0),
отображение скорости, задний ход (изменение знака скорости).
'''
import time
class Car:
    brand = None
    model = None
    year = None
    speed = None

    def __init__(self, brand, model, year, speed):
        self.brand, self.model, self.year, self.speed = brand, model, year, speed

    def speed_increase(self):
        self.speed += 5
    def speed_decrease(self):
        self.speed -= 5
    def stop(self):
        self.speed = 0
    def link_speed(self):
        print(f'{self.speed} км/ч')
    def reverse(self):
        self.speed = -5
    def car_to_100(self):
        while self.speed != 100:  # "разгон" машины до 100 км/ч
            time.sleep(1)
            self.speed_increase()
            self.link_speed()