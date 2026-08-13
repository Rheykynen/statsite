from enum import Enum
from src.htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
   def __init__(self, text, text_type, url=None):
      self.text = text
      self.text_type = text_type
      self.url = url

   def __eq__(self, other):
    if not isinstance(other, TextNode): # Wenn es nicht gleiche Typen sind, kann ich sie nicht vergleichen
       return False
    return ( # es soll jedes Element miteinander vergleichen werden
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

   def __repr__(self) -> str:
       return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node : TextNode) -> LeafNode:
    if text_node.text_type is None:
        raise Exception(f"node has no text_type")
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        if text_node.url is None:
            raise ValueError(f"node has no url")
        return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
    elif text_node.text_type == TextType.IMAGE:
        if text_node.url is None:
            raise ValueError(f"invalid URL")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"invalid text type: {text_node.text_type}")

def main():
    text_node_to_html_node(TextNode("Das ist ein Text", TextType.LINK, "https://www.boot.dev"))

if __name__ == "__main__":
    main()