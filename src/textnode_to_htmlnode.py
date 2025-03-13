from leafnode import LeafNode  # Assuming you already have this class
from textnode import TextNode, TextType

def text_node_to_html_node(text_node):
    """
    Converts a TextNode to a corresponding LeafNode.
    
    :param text_node: A TextNode object to be converted to a LeafNode.
    :return: A LeafNode object representing the HTML equivalent of the TextNode.
    :raises ValueError: If the TextNode has an invalid text_type.
    """
    if text_node.text_type == TextType.NORMAL_TEXT:
        return LeafNode(None, text_node.text)
    
    if text_node.text_type == TextType.BOLD_TEXT:
        return LeafNode("b", text_node.text)
    
    if text_node.text_type == TextType.ITALIC_TEXT:
        return LeafNode("i", text_node.text)
    
    if text_node.text_type == TextType.CODE_TEXT:
        return LeafNode("code", text_node.text)
    
    if text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("Link TextNode must have a URL.")
        return LeafNode("a", text_node.text, {"href": text_node.url})
    
    if text_node.text_type == TextType.IMAGE:
        if not text_node.url:
            raise ValueError("Image TextNode must have a URL.")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    
    # If the text type is invalid, raise an exception
    raise ValueError(f"Invalid TextType: {text_node.text_type}")
