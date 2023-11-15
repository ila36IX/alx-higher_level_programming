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
        with self.assertRaises(ValueError):
            rec = Rectangle(1, 2, -3)

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


class Test_rectangle2(unittest.TestCase):
    """

    New tests

    """

    @classmethod
    def setUpClass(self):
        """Reset the Rectangle id"""
        Rectangle.reset()

    def setUp(self):
        """Setup units to test with"""
        self.R1 = Rectangle(1, 1)
        self.R2 = Rectangle(2, 2, 3, 3, 5)
        self.R3 = Rectangle(4, 2, 4, 3)
        self.R4 = Rectangle(4, 2, 1, 0)

    def tearDown(self):
        """Delete the units"""
        del self.R1
        del self.R2
        del self.R3
        Rectangle.reset()
    
    def test_1(self):
        """Test __str__"""
        self.R1_str = "[Rectangle] (1) 0/0 - 1/1"
        self.R2_str = "[Rectangle] (5) 3/3 - 2/2"
        self.R3_str = "[Rectangle] (2) 4/3 - 4/2"
        self.R4 = Rectangle(10, 12)
        self.assertMultiLineEqual(self.R1.__str__(), self.R1_str)
        self.assertMultiLineEqual(self.R2.__str__(), self.R2_str)
        self.assertMultiLineEqual(self.R3.__str__(), self.R3_str)

    def test_2(self):
        # self.R1 = Rectangle(1, 1)
        # self.R2 = Rectangle(2, 2, 3, 3, 5)
        # self.R3 = Rectangle(4, 2, 4, 3)
        # self.R4 = Rectangle(4, 2, 1, 0)
        self.R3.update(666)
        self.assertEqual(self.R3.id, 666)
        """update method"""
        self.R1.update(1, 2, 3, 4, 5)
        self.R2.update(3, 6, 9, 36, 69)
        """R1 test"""
        self.assertEqual(self.R1.id, 1)
        self.assertEqual(self.R1.width, 2)
        self.assertEqual(self.R1.height, 3)
        self.assertEqual(self.R1.x, 4)
        self.assertEqual(self.R1.y, 5)
        """R2 test"""
        self.assertEqual(self.R2.id, 3)
        self.assertEqual(self.R2.width, 6)
        self.assertEqual(self.R2.height, 9)
        self.assertEqual(self.R2.x, 36)
        self.assertEqual(self.R2.y, 69)

    def test_3(self):
        """R1 with kwargs"""
        # self.R2 = Rectangle(2, 2, 3, 3, 5)
        self.R2.update(width=6, x=15)
        self.assertEqual(self.R2.id, 5)
        self.assertEqual(self.R2.width, 6)
        self.assertEqual(self.R2.height, 2)
        self.assertEqual(self.R2.x, 15)
        self.assertEqual(self.R2.y, 3)
        """MIx between args and kwargs"""
        self.R1.update(1, 2, 3, 4, 5, width=1000, id=69)
        self.assertEqual(self.R1.width, 2)
        self.assertEqual(self.R1.id, 1)

    def test_4(self):
        """Test the to_dictionary method"""
        tuple1 = {"width": 2, "height": 2, "x": 3, "y": 3, "id": 5}
        self.assertDictEqual(self.R2.to_dictionary(), tuple1)

    def test_5(self):
        self.R1 = Rectangle(1, 1)
        self.R2 = Rectangle(2, 2, 3, 3, 5)
        self.R3 = Rectangle(4, 2, 4, 3)
        self.R4 = Rectangle(4, 2, 1, 0)
        rect_list = [self.R1, self.R2, self.R3, self.R4]
        Rectangle.save_to_file(rect_list)

    def test_6(self):
        junk = Rectangle.create(**{ 'id': 89 })
        self.assertEqual(junk.id, 89)
        junk = Rectangle.create(**{ 'id': 89, 'width': 1 })
        self.assertEqual(junk.id, 89)
        self.assertEqual(junk.width, 1)
        junk = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })
        self.assertEqual(junk.id, 89)
        self.assertEqual(junk.width, 1)
        self.assertEqual(junk.height, 2)
        junk = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        self.assertEqual(junk.id, 89)
        self.assertEqual(junk.width, 1)
        self.assertEqual(junk.height, 2)
        self.assertEqual(junk.x, 3)
        junk = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(junk.y, 4) 
    
    def test_7(self):
        """Test writing to csv file"""
        Rectangle.save_to_file_csv([self.R1, self.R2, self.R4]) 
    
    def test_8(self):
        """Read from csv file"""
        lll = Rectangle.load_from_file_csv()
        for l in lll:
            print(l)
