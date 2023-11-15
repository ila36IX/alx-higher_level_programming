#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square 
import unittest


class Test_base(unittest.TestCase):
    """
    Test the Base class

    """

    def test_1(self):
        """Test in case id is None"""
        base1 = Base()
        base2 = Base()
        base3 = Base()
        base4 = Base()
        base5 = Base()
        self.assertAlmostEqual(base1.id, 1)
        self.assertAlmostEqual(base2.id, 2)
        self.assertAlmostEqual(base3.id, 3)
        self.assertAlmostEqual(base4.id, 4)
        self.assertAlmostEqual(base5.id, 5)

    def test_2(self):
        """Test in case id is not None"""
        base1 = Base(1)
        base2 = Base(2)
        base3 = Base(3)
        base4 = Base(4)
        base5 = Base(5)
        self.assertAlmostEqual(base1.id, 1)
        self.assertAlmostEqual(base2.id, 2)
        self.assertAlmostEqual(base3.id, 3)
        self.assertAlmostEqual(base4.id, 4)
        self.assertAlmostEqual(base5.id, 5)

    def test_3(self):
        """Test in case id is None again"""
        base1 = Base()
        base2 = Base()
        base3 = Base()
        base4 = Base()
        base5 = Base()
        self.assertAlmostEqual(base1.id, 6)
        self.assertAlmostEqual(base2.id, 7)
        self.assertAlmostEqual(base3.id, 8)
        self.assertAlmostEqual(base4.id, 9)
        self.assertAlmostEqual(base5.id, 10)

    def test_4(self):
        """Test to_json_string method"""
        junk_l = [{"key1": 1, "key2": 2}, {"key1": 1, "key2": 2}]
        junk_str = '[{"key1": 1, "key2": 2}, {"key1": 1, "key2": 2}]'
        json_str = Base.to_json_string(junk_l)
        self.assertEqual(json_str, junk_str)
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

        # Square.create(**{ 'size': 2 }) creates a new Square instance
    def test_5(self):
        print(Rectangle.load_from_file())

