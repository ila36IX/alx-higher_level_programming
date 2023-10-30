import unittest
max_integer = __import__('6-max_integer').max_integer

class max_integer_test(unittest.TestCase):

    """
    Test the max_integer function

    """

    def test_1(self):
        test_unit1 = [1, 5 , 6 , 10, 16]
        self.assertAlmostEqual(max_integer(test_unit1), 16)
        test_unit1 = [100, 5 , 6 , 10, 16]
        self.assertAlmostEqual(max_integer(test_unit1), 100)
        test_unit1 = [-100, -5 , -6 , -10, 0]
        self.assertAlmostEqual(max_integer(test_unit1), 0)
