import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(
            "p",
            "Das ist ein Absatz",
            None,
            {"font-style": "bold"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, Das ist ein Absatz, children: None, {'font-style': 'bold'})")

    def test_values(self):
        node = HTMLNode(
            "h1",
            "Das ist eine Hauptüberschrift."
        )
        self.assertEqual(
            node.tag,
            "h1"
        )
        self.assertEqual(
            node.value,
            "Das ist eine Hauptüberschrift."
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )




if __name__ == "__main__":
    unittest.main()