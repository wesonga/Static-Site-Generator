from enum import Enum

# Enum for defining different types of inline text
class TextType(Enum):
    NORMAL_TEXT = "normal_text"
    BOLD_TEXT = "bold_text"
    ITALIC_TEXT = "italic_text"
    CODE_TEXT = "code_text"
    LINK = "link"
    IMAGE = "image"

# Class representing a text node with a specific text type
class TextNode:
    def __init__(self, text, text_type, url=None):
        """
        Initializes the TextNode with text content, type of text, and an optional URL.
        
        :param text: The text content of the node
        :param text_type: The type of text, which should be a member of the TextType enum
        :param url: The URL for links or images (default is None if not applicable)
        """
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        """
        Compares two TextNode objects to check if all properties are equal.
        
        :param other: The other TextNode object to compare against
        :return: True if both objects are equal, False otherwise
        """
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        """
        Returns a string representation of the TextNode object.
        
        :return: A string in the format: TextNode(TEXT, TEXT_TYPE, URL)
        """
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
