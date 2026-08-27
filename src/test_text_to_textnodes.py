import unittest

from textnode import TextNode, TextType
from inline_markdown import text_to_textnodes

class TestDelimiter(unittest.TestCase):
    def test_text_to_textnode1(self):
        node = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertEqual(
            node,
            [
                TextNode("This is ", TextType.TEXT),
                 TextNode("text", TextType.BOLD),
                 TextNode(" with an ", TextType.TEXT),
                 TextNode("italic", TextType.ITALIC),
                 TextNode(" word and a ", TextType.TEXT),
                 TextNode("code block", TextType.CODE),
                 TextNode(" and an ", TextType.TEXT),
                 TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                 TextNode(" and a ", TextType.TEXT),
                 TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )

    def test_text_to_textnode2(self):
        node = text_to_textnodes("This is **text** with an _italic_ word, another **bold word** and a teeny tiny `code block` with a [link](https://boot.dev)")
        self.assertEqual(
            node,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word, another ", TextType.TEXT),
                TextNode("bold word", TextType.BOLD),
                TextNode(" and a teeny tiny ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )