# -*- coding: utf-8 -*-
import math
from abc import ABC, abstractmethod
import sys
sys.stdout.reconfigure(encoding='utf-8')

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        # Формула Герона для площади треугольника
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def is_right(self):
        # Проверка на прямоугольный треугольник (теорема Пифагора с учетом сортировки сторон)
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[2] ** 2, sides[0] ** 2 + sides[1] ** 2, rel_tol=1e-9)

def calculate_area(shape: Shape) -> float:
    # Вычисляет площадь фигуры "без знания типа в compile-time"
    return shape.area()

# Примеры
if __name__ == "__main__":
    c = Circle(3)
    t = Triangle(3, 4, 5)
    print(f"Площадь круга: {c.area()}")
    print(f"Площадь треугольника: {t.area()}")
    print(f"Треугольник прямоугольный? {t.is_right()}")
    print(f"Общая функция: {calculate_area(c)}, {calculate_area(t)}")
