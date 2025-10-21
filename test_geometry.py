import unittest
from geometry import Circle, Triangle, calculate_area
import math

class TestGeometry(unittest.TestCase):
    def test_circle_area(self):
        c = Circle(2)
        self.assertAlmostEqual(c.area(), math.pi * 4)
    def test_triangle_area(self):
        t = Triangle(3, 4, 5)
        self.assertAlmostEqual(t.area(), 6)
    def test_right_triangle(self):
        t = Triangle(3, 4, 5)
        self.assertTrue(t.is_right())
    def test_calculate_area(self):
        c = Circle(1)
        t = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(c), math.pi)
        self.assertAlmostEqual(calculate_area(t), 6)

if __name__ == "__main__":
    unittest.main()
