import unittest
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_repr(self):
        node = LeafNode(
            "p",
            "Das ist ein Absatz",
            {'font-style': 'bold'},
        )
        self.assertEqual(
            node.__repr__(),
            "LeafNode(p, Das ist ein Absatz, {'font-style': 'bold'})")

    def test_leaf_to_html_a(self):
        node = LeafNode(
            "a",
            "www.google.com",
            {'href': 'https://www.google.com', 'target': '_blank'},
        )
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">www.google.com</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")