from enum import Enum

class TextType(Enum):
      PLAIN = "text"
      BOLD = "**Bold text**"
      ITALIC = "_Italic text_"
      CODE = "'Code text`"
      LINKS = "[anchor text](url)"
      IMAGES = "![alt text](url)"

class TextNode():   
   def __init__(self, text, text_type, url=None):
      self.text = text
      self.text_type = TextType[text_type]
      self.url = url

   def __eq__(self, other):
       return self == other

   def __repr__(self):
       return (f"{self.text}, {self.text_type.value}, {self.url}")
