import re

def extract_markdown_images(text):
    """
    Extracts markdown images from text in the format ![alt text](url)
    Returns list of tuples containing (alt_text, url)
    """
    pattern = r'!\[(.*?)\]\((https?://.*?)\)'
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    """
    Extracts markdown links from text in the format [anchor text](url)
    Returns list of tuples containing (anchor_text, url)
    """
    pattern = r'(?<!\!)\[(.*?)\]\((https?://.*?)\)'
    # Negative lookbehind (?<!\!) ensures we don't match image syntax
    matches = re.findall(pattern, text)
    return matches
