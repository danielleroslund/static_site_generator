import unittest
from extract_title import extract_title

class TestExtraTitle(unittest.TestCase):
    
    def test_extract_simple_title(self):
        result = extract_title("# Hello")
        self.assertEqual(result, "Hello")

    def test_extract_title_with_whitespace(self):
        result = extract_title("#  Hello World   ")
        self.assertEqual(result, "Hello World")


if __name__ == "__main__":
    unittest.main()