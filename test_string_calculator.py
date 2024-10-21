import unittest
from string_calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(StringCalculator("").add(), 0)

    def test_single_number(self):
        self.assertEqual(StringCalculator("100").add(), 100)

    def test_multiple_numbers(self):
        self.assertEqual(StringCalculator("23,45").add(), 68)
        self.assertEqual(StringCalculator("23,21,98,45,34").add(), 221)
        self.assertEqual(StringCalculator("210,29,38").add(), 277)

    def test_newline_delimiter(self):
        self.assertEqual(StringCalculator("11\n12,13").add(), 36)
        self.assertEqual(StringCalculator("11\n12\n13").add(), 36)

    def test_custom_delimiter(self):
        # Custom delimiter ";"
        self.assertEqual(StringCalculator("//;\n1;2").add(), 3)
        # Custom delimiter "!"
        self.assertEqual(StringCalculator("//!\n4!10!23").add(), 37)
        # Custom delimiter "|"
        self.assertEqual(StringCalculator("//|\n2|3|4").add(), 9)

    def test_multiple_delimiters(self):
        # Multiple delimiters "*", "%"
        self.assertEqual(StringCalculator("//[*][%]\n1*2%3").add(), 6)
        # Multiple delimiters "!", "@"
        self.assertEqual(StringCalculator("//[!][@]\n1!2@3").add(), 6)
        # Multiple delimiters "***", "@@@"
        self.assertEqual(StringCalculator("//[***][@@@]\n1***2@@@3").add(), 6)

    def test_long_multiple_delimiters(self):
        # Multiple long delimiters "$$", "^^"
        self.assertEqual(StringCalculator("//[$$][^^]\n1$$2^^3").add(), 6)


if __name__ == '__main__':
    unittest.main()
