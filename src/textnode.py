from enum import Enum


class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    ANCHOR = "anchor"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, textNode):
        if (
            self.text == textNode.textNode
            and self.text_type.value == textNode.text_type.value
            and self.url == textNode.url
        ):
            return True
        return False

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
