#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_list(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_variables(self):
        var = 6
        result = max_integer([1, 4, 3, var, 2, 5])
        self.assertEqual(result, var)

    def test_float(self):
        result = max_integer([0.1, 100, 5, 157.6, 666, 789.125, 20])
        self.assertEqual(result, 789.125)

    def test_unsorted_list(self):
        result = max_integer([5, 90, 2, 70, 954, 6, 0.8, -25])
        self.assertEqual(result, 954)

    def test_negative(self):
        result = max_integer([-5, -95, -7, -6, -36, -2])
        self.assertEqual(result, -2)

    def test_large_int(self):
        result = max_integer([56874, 666, 9445236644895, 5658, 587788, 2100000230015563, 98756687465, 88888888888888888, 56666])
        self.assertEqual(result, 88888888888888888)

    def test_mix_int(self):
        result = max_integer([546, -485, 0.56, 1987.256, -45964, - 7995455, 79942145,  89645333455656934])
        self.assertEqual(result, 89645333455656934)

    def test_str(self):
        result = max_integer("I am in love with a beautiful woman")
        self.assertEqual(result, "w")

    def test_tuple(self):
        result = max_integer((1, 99, -68, 67.2))
        self.assertEqual(result, 99)

    def test_matrix(self):
        result = max_integer([[-98, 0, 68.1], [8, 7.5, -100], [-1.124, 69, 6]])
        self.assertEqual(result, [8, 7.5, -100])

    def test_list_tuple(self):
        result = max_integer([(28, 6.3, -6), (7.3, -89, 2), (-1.2, 4, -52)])
        self.assertEqual(result, (28, 6.3, -6))

    def test_unequal_matrix(self):
        result = max_integer([[-96, 6.32], [100], [89.3, -8, -15.3]])
        self.assertEqual(result, [100])

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_no_args(self):
        result = max_integer()
        self.assertIsNone(result)



class TestMaxIntegerError(unittest.TestCase):

    def test_str_list(self):
        self.assertRaises(TypeError, max_integer, [25, -10.3, 68.6, "school", -6])
        self.assertRaises(TypeError, max_integer, ("Best", -7.3, 9, 9.6, -9))
        self.assertRaises(TypeError, max_integer, ([24, "damy"], [-63, 6, 0.3, -9.4], ["pretty"]))
        self.assertRaises(TypeError, max_integer, [("Rose", "Mary"), (56), (-9, 0, -9.3, 58)])

    def test_none_list(self):
        self.assertRaises(TypeError, max_integer, [25, -10.3, None, 68.6, "school", -6])
        self.assertRaises(TypeError, max_integer, (None, -7.3, 9, 9.6, -9))
        self.assertRaises(TypeError, max_integer, ([24, "damy"], [-63, 6, 0.3, None, -9.4], ["pretty"]))
        self.assertRaises(TypeError, max_integer, [("Rose", "Mary"), (None), (-9, 0, -9.3, 58)])
        self.assertRaises(TypeError, max_integer, (None))
