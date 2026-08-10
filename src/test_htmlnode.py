import unittest
from htmlnode import HTMLNode


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

    def test_props_to_html(self):
        node = HTMLNode(
            "div",
            "Das ist ein div Container mit einem tollen Inhalt.",
            None,
            {"href": "https://www.google.com", "class": "boots"},
        )

        self.assertEqual(
            node.props_to_html(),
            'href="https://www.google.com" class="boots"',
        )


if __name__ == "__main__":
    unittest.main()