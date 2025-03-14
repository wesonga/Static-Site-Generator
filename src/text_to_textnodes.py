from textnode import TextNode, TextType
from markdown_splitters import split_nodes_image, split_nodes_link

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """Helper function to split nodes based on a delimiter for bold, italic, and code."""
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT or not node.text:
            new_nodes.append(node)
            continue
            
        parts = node.text.split(delimiter)
        if len(parts) == 1:
            new_nodes.append(node)
            continue
            
        for i, part in enumerate(parts):
            if i % 2 == 0:  # Even indices are normal text
                if part:
                    new_nodes.append(TextNode(part, TextType.NORMAL_TEXT))
            else:  # Odd indices are the formatted text
                if part:
                    new_nodes.append(TextNode(part, text_type))
    return new_nodes

def text_to_textnodes(text):
    """
    Converts raw markdown text into a list of TextNodes.
    Handles bold (**), italic (_), code (`), images (![]()), and links ([]()).
    """
    # Start with a single normal text node
    initial_node = TextNode(text, TextType.NORMAL_TEXT)
    nodes = [initial_node]
    
    # Apply splitting in sequence
    # Order matters: do inline formatting before images/links to avoid splitting markup
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD_TEXT)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC_TEXT)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE_TEXT)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    return nodes
