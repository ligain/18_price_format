import unittest
from format_price import format_price


class FormatPriceTest(unittest.TestCase):

    def test_null(self):
        self.assertIsNone(format_price())
        self.assertIsNone(format_price(' '))
        self.assertIsNone(format_price(None))
        self.assertIsNone(format_price(False))
        self.assertIsNone(format_price(True))
        self.assertIsNone(format_price([]))

    def test_float_number(self):
        self.assertEqual('0', format_price('.499999999999999'))
        self.assertEqual('3 245', format_price('3245.000000'))
        self.assertEqual('3 234 534 556 745', format_price('3234534556745.02'))
        self.assertEqual('0', format_price('000000.324'))

    def test_bad_string_argument(self):
        self.assertIsNone(format_price('sdf.90'))
        self.assertEqual('34 091', format_price('+34090.9000000000001'))
