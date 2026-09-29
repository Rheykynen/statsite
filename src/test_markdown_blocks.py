import unittest

from markdown_blocks import (
    block_to_block_type,
    BlockType,
    markdown_to_html_node,
    markdown_to_blocks
)



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

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_list(self):
        md = """
1. How to get kicked in the todger
2. Having been kicked in the todger
3. How to cope with being kicked in the todger
4. Grief
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div>"
            "<ol>"
            "<li>How to get kicked in the todger</li>"
            "<li>Having been kicked in the todger</li>"
            "<li>How to cope with being kicked in the todger</li>"
            "<li>Grief</li>"
            "</ol>"
            "</div>",
        )

    def test_ulist(self):
        md = """
- silliness
- silliness continues
- silliness: reckoning
- silliness but **bold** this time
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div>"
            "<ul>"
            "<li>silliness</li>"
            "<li>silliness continues</li>"
            "<li>silliness: reckoning</li>"
            "<li>silliness but <b>bold</b> this time</li>"
            "</ul>"
            "</div>",
        )

    def test_mixed_contents(self):
        md = """
# Heading

## Subheading

This is a paragraph with _italic_ text and `code` here

> this is a very fancy quote one needs to have a very high intelligence

this should be a normal paragraph

- oh
- a list
- how wonderful

1. How to get kicked in the balls
This is a guide how to fuck up a ordered list and subsequent _consequences_.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div>"
            "<h1>Heading</h1>"
            "<h2>Subheading</h2>"
            "<p>This is a paragraph with <i>italic</i> text and <code>code</code> here</p>"
            "<blockquote>this is a very fancy quote one needs to have a very high intelligence</blockquote>"
            "<p>this should be a normal paragraph</p>"
            "<ul>"
            "<li>oh</li>"
            "<li>a list</li>"
            "<li>how wonderful</li>"
            "</ul>"
            "<p>1. How to get kicked in the balls This is a guide how to fuck up a ordered list and subsequent <i>consequences</i>.</p>"
            "</div>",
        )

    def test_md_chars_in_text(self):
        md = """
# Heading about # Heading

## Subheading about C#

> Blockquote which is > than you
         
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div>"
            "<h1>Heading about # Heading</h1>"
            "<h2>Subheading about C#</h2>"
            "<blockquote>Blockquote which is > than you</blockquote>"
            "</div>"
        )


if __name__ == "__main__":
    unittest.main()