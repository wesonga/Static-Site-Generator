from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Splits text nodes containing the specified delimiter into multiple nodes.
    
    Args:
        old_nodes (list): List of TextNode objects to process
        delimiter (str): Delimiter to split on (e.g., "`" for code, "**" for bold)
        text_type (TextType): Target text type for content between delimiters
    
    Returns:
        list: New list of TextNode objects with split content
    """
    new_nodes = []
    
    for node in old_nodes:
        # Only process text-type nodes
        if node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(node)
            continue
            
        # Split the text by delimiter
        parts = node.text.split(delimiter)
        
        # If no delimiters or odd number of parts (unclosed delimiter), keep as is
        if len(parts) == 1 or len(parts) % 2 == 0:
            new_nodes.append(node)
            continue
            
        # Process parts alternately as text and target type
        for i, part in enumerate(parts):
            if not part:  # Skip empty parts
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.NORMAL_TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))
                
    return new_nodes