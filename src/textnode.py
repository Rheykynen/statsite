from enum import Enum

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
