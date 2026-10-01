import unittest
from gencontent import extract_title


class TestDelimiter(unittest.TestCase):
    def test_h1_extraction(self):
        markdown = """
# This is the title

this is a paragraph

        
""".strip()
        result = extract_title(markdown)

        self.assertEqual(
            result,
            'This is the title'
        )

    def test_h2_first(self):
        markdown = """
## This is a misplaced h2 title

# This is the target title

this is a paragraph


""".strip()
        result = extract_title(markdown)

        self.assertEqual(
            result,
            'This is the target title'
        )


    def test_multi_h1(self):
        markdown = """
# This is the target title

# This is another h1 title which should not exist

this is a paragraph

""".strip()
        result = extract_title(markdown)

        self.assertEqual(
            result,
            'This is the target title'
        )

    def test_no_heading(self):
        markdown = """
This is not the target title

This is another paragraph which should exist

this is a paragraph

""".strip()

        with self.assertRaises(Exception):
            extract_title(markdown)

