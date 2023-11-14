#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

"""

Testing the Rectangle class

"""
class Test_rectangle(unittest.TestCase):
    """Test rectange"""

    def test_1(self):
        """Test of the case of valid arguments"""
        rec = Rectangle(1, 1)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 1)
        self.assertEqual(rec.x, 0)

    def test_2(self):
        """Test of the case of valid arguments"""
        rec = Rectangle(5, 10, 6, 9, id=None)
        self.assertEqual(rec.width, 5)
        self.assertEqual(rec.height, 10)
        self.assertEqual(rec.x, 6)
        self.assertEqual(rec.y, 9)

    def test_3(self):
        rec = Rectangle(5, 10, id=20)
        self.assertEqual(rec.width, 5)
        self.assertEqual(rec.height, 10)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)

    def test_4(self):   
        rec = Rectangle(6, 15)
        self.assertEqual(rec.width, 6)
        self.assertEqual(rec.height, 15)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)

    def test5(self):
        """Negative cases"""
        with self.assertRaises(ValueError):
            rec = Rectangle(-5, 3)
        with self.assertRaises(ValueError):
            rec = Rectangle(5, -3)
        with self.assertRaises(ValueError):
            rec = Rectangle(5, 3, 3, -5)
        with self.assertRaises(ValueError):
            rec = Rectangle(5, -3, -3, 5)

    def test_6(self):
        """Zero cases"""
        with self.assertRaises(ValueError):
            rec = Rectangle(0, 3, 6, 5)
        with self.assertRaises(ValueError):
            rec = Rectangle(5, 0, 6, 5)
        rec = Rectangle(5, 3, 0, 5)
        rec = Rectangle(5, 3, 5, 0)

    def test_7(self):
        """Test Non-integer cases"""
        with self.assertRaises(TypeError):
            rec = Rectangle("not_integer", 10)
        with self.assertRaises(TypeError):
            rec = Rectangle(10, "not_integer")
        with self.assertRaises(TypeError):
            rec = Rectangle(10, 15, "test")
        with self.assertRaises(TypeError):
            rec = Rectangle(10, 15, 0, "test")

    def test_8(self):
        """Test the area method"""
        R = Rectangle(5, 10)
        self.assertEqual(R.area(), 50)
        R = Rectangle(4, 4)
        self.assertEqual(R.area(), 16)
        R = Rectangle(8, 8)
        self.assertEqual(R.area(), 64)
