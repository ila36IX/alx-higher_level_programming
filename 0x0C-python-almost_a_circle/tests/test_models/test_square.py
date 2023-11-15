# #!usr/usr/bin/python3
# from models.square import Square
# import unittest
#
# """
#
# Testing the square model
#
# """
#
#
# class TestSquare(unittest.TestCase):
#     """
#
#     Units to test the square class
#
#     """
#
#     def setUp(self):
#         """Units for testing"""
#         self.sqr1 = Square(3, 2, 3, 69)
#         self.sqr2 = Square(6, id=369)
#         self.sqr3 = Square(6, 3, 3)
#         self.sqr4 = Square(3, 6, 6)
#
#     def tearDown(self):
#         """Reset units"""
#         Square.reset()
#
#     def test_1(self):
#         """test when all arguments are given"""
#         self.assertEqual(self.sqr1.id, 69)
#         self.assertEqual(self.sqr1.width, 3)
#         self.assertEqual(self.sqr1.height, 3)
#         self.assertEqual(self.sqr1.x, 2)
#         self.assertEqual(self.sqr1.y, 3)
#
#     def test_2(self):
#         """key-worded argument case"""
#         self.assertEqual(self.sqr2.id, 369)
#         self.assertEqual(self.sqr2.width, 6)
#         self.assertEqual(self.sqr2.x, 0)
#         self.assertEqual(self.sqr2.y, 0)
#
#     def test_3(self):
#         """display method"""
#         self.assertEqual(self.sqr1.__str__(), "[Square] (69) 2/3 - 3")
#         self.sqr1.display()
#
#     def test_3(self):
#         """Test the size property"""
#         self.sqr1.size = 69
#         self.assertEqual(self.sqr1.width, 69)
#         self.assertEqual(self.sqr1.height, 69)
#         self.assertEqual(self.sqr1.size, 69)
#         with self.assertRaises(TypeError):
#             self.sqr1.size = "9"
#         with self.assertRaises(ValueError):
#             self.sqr1.size = 0
#
#     def test_4(self):
#         """Test the update method (No-keyworded args)"""
#         self.sqr1.update(33, 66, 99, 369)
#         self.assertEqual(self.sqr1.id, 33)
#         self.assertEqual(self.sqr1.size, 66)
#         self.assertEqual(self.sqr1.x, 99)
#         self.assertEqual(self.sqr1.y, 369)
#
#     def test_5(self):
#         """Test the update method (No-keyworded args)"""
#         self.sqr1.update(size=5, x=12)
#         self.assertEqual(self.sqr1.id, 69)
#         self.assertEqual(self.sqr1.size, 5)
#         self.assertEqual(self.sqr1.x, 12)
#         self.assertEqual(self.sqr1.y, 3)
#
#     def test_6(self):
#         """Test to_dictionery method"""
#         # self.sqr1 = Square(3, 2, 3, 69)
#         typle1 = {"size": 3, "x": 2, "y": 3, "id": 69}
#         self.assertDictEqual(self.sqr1.to_dictionary(), typle1)
#
#     def test_7(self):
#         """test object to string method"""
#         str_sqr1 = '[{"id": 69, "size": 3, "x": 2, "y": 3}, \
# {"id": 369, "size": 6, "x": 0, "y": 0}, {"ali": 2}]'
#         sqrs_list = [self.sqr1, self.sqr2, {"ali": 2}]
#         self.assertEqual(Square.to_json_string(sqrs_list), str_sqr1)
#
#     def test_7(self):
#         """test save to json mehtod"""
#
#         sqr_list = [self.sqr1, self.sqr2, self.sqr3, self.sqr4]
#         Square.save_to_file(sqr_list)
#
#     def test_8(self):
#         """Deserialize string to list"""
#
#         list_sqrs = [self.sqr1, self.sqr2]
#         list_sqrs_exp = [
#             {"size": 3, "x": 2, "y": 3, "id": 69},
#             {"size": 6, "x": 0, "y": 0, "id": 369}
#         ]
#         string = Square.to_json_string(list_sqrs)
#         self.assertEqual(Square.from_json_string(string), list_sqrs_exp)
