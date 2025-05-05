"""
Sample Test
"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtracting_numbers(self):
        """test subtracting numbers together"""
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
