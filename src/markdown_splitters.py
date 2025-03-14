from markdown_extractors import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    """
    Splits TextNodes containing markdown images into separate nodes for text and images.
    Returns a list of new TextNodes.
    """
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT or not node.text:
            new_nodes.append(node)
            continue
            
        text = node.text
        images = extract_markdown_images(text)
        
        if not images:
            new_nodes.append(node)
            continue
            
        remaining_text = text
        for alt_text, url in images:
            image_markdown = f"![{alt_text}]({url})"
            before, after = remaining_text.split(image_markdown, 1)
            
            if before:
                new_nodes.append(TextNode(before, TextType.NORMAL_TEXT))
                
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            remaining_text = after
            
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.NORMAL_TEXT))
            
    return new_nodes

def split_nodes_link(old_nodes):
    """
    Splits TextNodes containing markdown links into separate nodes for text and links.
    Returns a list of new TextNodes.
    """
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT or not node.text:
            new_nodes.append(node)
            continue
            
        text = node.text
        links = extract_markdown_links(text)
        
        if not links:
            new_nodes.append(node)
            continue
            
        remaining_text = text
        for anchor_text, url in links:
            link_markdown = f"[{anchor_text}]({url})"
            before, after = remaining_text.split(link_markdown, 1)
            
            if before:
                new_nodes.append(TextNode(before, TextType.NORMAL_TEXT))
                
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            remaining_text = after
            
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.NORMAL_TEXT))
            
    return new_nodes
