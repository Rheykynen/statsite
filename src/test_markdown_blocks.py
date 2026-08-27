import unittest

from markdown_blocks import markdown_to_blocks
from src.markdown_blocks import block_to_block_type, BlockType


class TestDelimiter(unittest.TestCase):
    def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

    def test_markdown_to_blocks2(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

This is **bolded** paragraph

"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "This is **bolded** paragraph",

            ],
        )

    def test_markdown_to_blocks_with_wrong_linebreaks(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line


- This is a list
- with items

This is another paragraph with _italic_ text and `code` here

This is the same paragraph on a new line


This is **bolded** paragraph

"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
                "This is another paragraph with _italic_ text and `code` here",
                "This is the same paragraph on a new line",
                "This is **bolded** paragraph",

            ],
        )

    def deactivated_test_markdown_to_blocks4(self):
            md = """
This is **bolded** paragraph

   This is another paragraph with _italic_ text and `code` here
   This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_blocktype_paragraph(self):
            block = "This is **bolded** paragraph"

            blocks = block_to_block_type(block)
            self.assertEqual(
                blocks, BlockType.PARAGRAPH
                ,
            )

    def test_block_to_blocktype_heading1(self):
            block = "# This is a Heading"
            blocks = block_to_block_type(block)

            self.assertEqual(
                blocks, BlockType.HEADING,
            )

    def test_block_to_blocktype_heading3(self):
            block = "### This is a Heading"
            blocks = block_to_block_type(block)

            self.assertEqual(
                blocks, BlockType.HEADING,
            )

    def test_block_to_blocktype_heading8(self):
            block = "######## This is a Heading"

            with self.assertRaises(Exception):
                block_to_block_type(block)

    def test_block_to_blocktype_h2_no_space(self):
            block = "##This is a Heading if it weren't for the missing space"
            blocks = block_to_block_type(block)

            self.assertEqual(
                blocks, BlockType.PARAGRAPH,
            )

if __name__ == "__main__":
    unittest.main()