import math
import unittest

from circle import area as CircleArea, perimeter as CirclePerimeter
from square import area as SquareArea, perimeter as SquarePerimeter
from rectangle import area as RectangleArea, perimeter as RectanglePerimeter
from triangle import area as TriangleArea, perimeter as TrianglePerimeter

# Circle Tests
class CircleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(CircleArea(5), math.pi * 25)

    def test_perimeter(self):
        self.assertEqual(CirclePerimeter(13), 2 * math.pi * 13)

    def test_zero_area(self):
        self.assertEqual(CircleArea(0), 0)

    def test_zero_perimeter(self):
        self.assertEqual(CirclePerimeter(0), 0)

# Square Tests
class SquareTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(SquareArea(5), 25)

    def test_perimeter(self):
        self.assertEqual(SquarePerimeter(5), 20)

    def test_zero_area(self):
        self.assertEqual(SquareArea(0), 0)

    def test_zero_perimeter(self):
        self.assertEqual(SquarePerimeter(0), 0)

# Rectangle Tests
class RectangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(RectangleArea(5, 10), 50)

    def test_perimeter(self):
        self.assertEqual(RectanglePerimeter(5, 10), 30)

    def test_zero_area(self):
        self.assertEqual(RectangleArea(0, 10), 0)

    def test_zero_perimeter(self):
        self.assertEqual(RectanglePerimeter(0, 0), 0)

# Triangle Tests
class TriangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(TriangleArea(3, 4), 6)

    def test_perimeter(self):
        self.assertEqual(TrianglePerimeter(3, 10, 2), 15)

    def test_zero_area(self):
            self.assertEqual(TriangleArea(5, 0), 0)

    def test_zero_perimeter(self):
        self.assertEqual(TrianglePerimeter(0, 0, 0), 0)
