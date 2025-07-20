from enum import Enum

class TextType(Enum):
    TEXT = "text"
    CODE = "code"
    BOLD = "bold"
    ITALIC = "italic"
    LINK = "link"
    IMAGE = "image"

class TextNode:

    def __init__(self, text, text_type: TextType, url = None):
        self.text = text
        self.text_type: TextType = text_type
        self.url = url

    def __eq__(self, other):
        return (isinstance(other, TextNode)
                and self.text == other.text
                and self.text_type == other.text_type
                and self.url == other.url)

    def __repr__(self):
        displayed_url = self.url if self.url is not None else "None"
        return "TextNode(" + self.text + ", " + self.text_type.value + ", " + displayed_url + ")"


