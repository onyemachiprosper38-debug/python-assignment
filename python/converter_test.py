import unittest
from converter import convert_usd_to_naira


class TestConverter(unittest.TestCase):

    def test_convert_1_dollar(self):
        result = convert_usd_to_naira(1)
        self.assertEqual(result, 1550)

    def test_convert_10_dollars(self):
        result = convert_usd_to_naira(10)
        self.assertEqual(result, 15500)

    def test_convert_zero(self):
        result = convert_usd_to_naira(0)
        self.assertEqual(result, 0)

    def test_convert_decimal(self):
        result = convert_usd_to_naira(2.5)
        self.assertEqual(result, 3875)


if __name__ == '__main__':
    unittest.main()
