import unittest
from format_price import format_price


class FormatPriceTest(unittest.TestCase):

    def test_null_price(self):
        self.assertIsNone(format_price())
        self.assertIsNone(format_price(None))

    def test_empty_string(self):
        self.assertIsNone(format_price(' '))

    def test_bool_type_as_price(self):
        self.assertIsNone(format_price(False))
        self.assertIsNone(format_price(True))

    def test_empty_obj(self):
        self.assertIsNone(format_price([]))

    def test_small_price(self):
        self.assertEqual('0.50', format_price('.499999999999999'))
        self.assertEqual('0.32', format_price('000000.32'))
        self.assertEqual('0.35', format_price('0.345'))

    def test_long_price(self):
        self.assertEqual('3 234 534 556 745.02', format_price('3234534556745.02'))
        self.assertEqual('34 090.90', format_price('+34090.9000000000001'))
        self.assertEqual('3 245', format_price('3245.000000'))

    def test_bad_string_argument(self):
        self.assertIsNone(format_price('sdf.90'))
