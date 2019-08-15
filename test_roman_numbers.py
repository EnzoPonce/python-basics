import unittest
from Roman_numbers import roman_to_decimal


class testRomanNumbers(unittest.TestCase):
    def test_I_roman_to_decimal(self):
        decimal_numbers = roman_to_decimal('I')
        self.assertEqual(decimal_numbers,1)


if __name__=='__main__':
    unittest.main()