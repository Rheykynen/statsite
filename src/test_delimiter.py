import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter


class TestDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_split_nodes_code_in_front(self):
        node = TextNode("`Code block` comes first, the rest afterwards.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("Code block", TextType.CODE),
            TextNode(" comes first, the rest afterwards.", TextType.TEXT),
        ])

    def test_bold_delimiter(self):
        node = TextNode("This is text with a **bold** marker", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" marker", TextType.TEXT),
        ])

    def test_dont_split_no_delimiter(self):
        node = TextNode("This is text with links and no delimiter", TextType.LINK)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with links and no delimiter", TextType.LINK),
        ])

    def test_missing_delimiter(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_wrong_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "#", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a `code block` word", TextType.TEXT),
        ])

    def test_no_delimiter(self):
        node = TextNode("This is text with a type #h1# header", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "", TextType.TEXT)

    def test_multiple_delimiters(self):
        node = TextNode("This is text with a `code block` word and also some `more` code", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word and also some ", TextType.TEXT),
            TextNode("more", TextType.CODE),
            TextNode(" code", TextType.TEXT),
        ])

if __name__ == '__main__':
    unittest.main()
