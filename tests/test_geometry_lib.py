import math
import unittest

from circle import area as CircleArea, perimeter as CirclePerimeter
from square import area as SquareArea, perimeter as SquarePerimeter
from rectangle import area as RectangleArea, perimeter as RectanglePerimeter
from triangle import area as TriangleArea, perimeter as TrianglePerimeter


# Circle Tests
class CircleTestCase(unittest.TestCase):
    # Area
    def test_area(self):
        self.assertEqual(CircleArea(5), math.pi * 25)

    def test_zero_area(self):
        self.assertEqual(CircleArea(0), 0)

    def test_area_negative_1(self):
        with self.assertRaises(ValueError):
            CircleArea(-5)

    def test_area_negative_2(self):
        with self.assertRaises(ValueError):
            CircleArea(-10)

    def test_area_string(self):
        self.assertEqual(CircleArea("3"), math.pi * 9)

    def test_area_string_negative(self):
        with self.assertRaises(ValueError):
            CircleArea("-2")

    # Perimeter
    def test_perimeter(self):
        self.assertEqual(CirclePerimeter(13), 2 * math.pi * 13)

    def test_zero_perimeter(self):
        self.assertEqual(CirclePerimeter(0), 0)

    def test_perimeter_negative_1(self):
        with self.assertRaises(ValueError):
            CirclePerimeter(-3)

    def test_perimeter_negative_2(self):
        with self.assertRaises(ValueError):
            CirclePerimeter(-5)

    def test_perimeter_string(self):
        self.assertEqual(CirclePerimeter("3"), 2 * math.pi * 3)

    def test_perimeter_string_negative(self):
        with self.assertRaises(ValueError):
            CirclePerimeter("-14")


# Square Tests
class SquareTestCase(unittest.TestCase):
    # Area
    def test_area(self):
        self.assertEqual(SquareArea(5), 25)

    def test_zero_area(self):
        self.assertEqual(SquareArea(0), 0)

    def test_area_negative_1(self):
        with self.assertRaises(ValueError):
            SquareArea(-5)

    def test_area_negative_2(self):
        with self.assertRaises(ValueError):
            SquareArea(-10)

    def test_area_string(self):
        self.assertEqual(SquareArea("3"), 9)

    def test_area_string_negative(self):
        with self.assertRaises(ValueError):
            SquareArea("-2")

    # Perimeter
    def test_perimeter(self):
        self.assertEqual(SquarePerimeter(5), 20)

    def test_zero_perimeter(self):
        self.assertEqual(SquarePerimeter(0), 0)

    def test_perimeter_negative_1(self):
        with self.assertRaises(ValueError):
            SquarePerimeter(-3)

    def test_perimeter_negative_2(self):
        with self.assertRaises(ValueError):
            SquarePerimeter(-5)

    def test_perimeter_string(self):
        self.assertEqual(SquarePerimeter("3"), 12)

    def test_perimeter_string_negative(self):
        with self.assertRaises(ValueError):
            SquarePerimeter("-4")


# Rectangle Tests
class RectangleTestCase(unittest.TestCase):
    # Area
    def test_area(self):
        self.assertEqual(RectangleArea(5, 10), 50)

    def test_zero_area(self):
        self.assertEqual(RectangleArea(0, 10), 0)

    def test_area_negative_1(self):
        with self.assertRaises(ValueError):
            RectangleArea(-5, 10)

    def test_area_negative_2(self):
        with self.assertRaises(ValueError):
            RectangleArea(5, -10)

    def test_area_string(self):
        self.assertEqual(RectangleArea("3", "4"), 12)

    def test_area_string_negative(self):
        with self.assertRaises(ValueError):
            RectangleArea("-3", "4")

    # Perimeter
    def test_perimeter(self):
        self.assertEqual(RectanglePerimeter(5, 10), 30)

    def test_zero_perimeter(self):
        self.assertEqual(RectanglePerimeter(0, 0), 0)

    def test_perimeter_negative_1(self):
        with self.assertRaises(ValueError):
            RectanglePerimeter(-5, 10)

    def test_perimeter_negative_2(self):
        with self.assertRaises(ValueError):
            RectanglePerimeter(5, -10)

    def test_perimeter_string(self):
        self.assertEqual(RectanglePerimeter("3", "4"), 14)

    def test_perimeter_string_negative(self):
        with self.assertRaises(ValueError):
            RectanglePerimeter("3", "-4")


# Triangle Tests
class TriangleTestCase(unittest.TestCase):
    # Area
    def test_area(self):
        self.assertEqual(TriangleArea(3, 4), 6)

    def test_zero_area(self):
        self.assertEqual(TriangleArea(5, 0), 0)

    def test_area_negative_1(self):
        with self.assertRaises(ValueError):
            TriangleArea(-3, 4)

    def test_area_negative_2(self):
        with self.assertRaises(ValueError):
            TriangleArea(3, -4)

    def test_area_string(self):
        self.assertEqual(TriangleArea("3", "4"), 6)

    def test_area_string_negative(self):
        with self.assertRaises(ValueError):
            TriangleArea("-3", "4")

    # Perimeter
    def test_perimeter(self):
        self.assertEqual(TrianglePerimeter(3, 10, 2), 15)

    def test_zero_perimeter(self):
        self.assertEqual(TrianglePerimeter(0, 0, 0), 0)

    def test_perimeter_negative_1(self):
        with self.assertRaises(ValueError):
            TrianglePerimeter(-3, 10, 2)

    def test_perimeter_negative_2(self):
        with self.assertRaises(ValueError):
            TrianglePerimeter(3, -10, 2)

    def test_perimeter_string(self):
        self.assertEqual(TrianglePerimeter("3", "4", "5"), 12)

    def test_perimeter_string_negative(self):
        with self.assertRaises(ValueError):
            TrianglePerimeter("3", "-4", "5")
