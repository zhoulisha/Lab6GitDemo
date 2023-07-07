import unittest

from M4.numeric_conversion import *


class NumberTest(unittest.TestCase):
    def test_hex_string_decode(self):
        hex_str = "0x2A"
        # hex_str2 = "3B"
        expected = 45

        result = hex_string_decode(hex_str)
        self.assertEqual(expected, result)
