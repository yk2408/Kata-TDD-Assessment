import unittest
from string_calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(StringCalculator().add(""), 0)

    def test_single_number(self):
        self.assertEqual(StringCalculator().add("100"), 100)

    def test_multiple_numbers(self):
        self.assertEqual(StringCalculator().add("23,45"), 68)
        self.assertEqual(StringCalculator().add("23,21,98,45,34"), 221)
        self.assertEqual(StringCalculator().add("210,29,38"), 277)

    def test_newline_delimiter(self):
        self.assertEqual(StringCalculator().add("11\n12,13"), 36)
        self.assertEqual(StringCalculator().add("11\n12\n13"), 36)

    def test_custom_delimiter(self):
        # Custom delimiter ";"
        self.assertEqual(StringCalculator().add("//;\n1;2"), 3)
        # Custom delimiter "!"
        self.assertEqual(StringCalculator().add("//!\n4!10!23"), 37)
        # Custom delimiter "|"
        self.assertEqual(StringCalculator().add("//|\n2|3|4"), 9)

    def test_multiple_delimiters(self):
        # Multiple delimiters "*", "%"
        self.assertEqual(StringCalculator().add("//[*][%]\n1*2%3"), 6)
        # Multiple delimiters "!", "@"
        self.assertEqual(StringCalculator().add("//[!][@]\n1!2@3"), 6)
        # Multiple delimiters "***", "@@@"
        self.assertEqual(StringCalculator().add("//[***][@@@]\n1***2@@@3"), 6)

    def test_long_multiple_delimiters(self):
        # Multiple long delimiters "$$", "^^"
        self.assertEqual(StringCalculator().add("//[$$][^^]\n1$$2^^3"), 6)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            StringCalculator().add("-1,-2,3")
        self.assertEqual(str(context.exception), "negative numbers not allowed: -1, -2")

    # Test for ignoring large numbers
    def test_ignore_large_numbers(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("2,2001"), 2)  # Should ignore 2001
        self.assertEqual(calc.add("1000,3011,2020,5"), 1005)  # Only 1000 and 5 should be summed


if __name__ == '__main__':
    unittest.main()
