from enum import Enum

class BlockType(Enum):
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    PARAGRAPH = "paragraph"

def block_to_block_type(block):
    """
    Determines the type of Markdown block based on its content.
    
    :param block: A single block of Markdown text (whitespace already stripped)
    :return: BlockType enum value representing the block type
    """
    # Split into lines for multi-line block types
    lines = block.split("\n")
    
    # Heading: starts with 1-6 # characters followed by space
    if lines[0].startswith("#") and len(lines) == 1:
        if len(lines[0].split(" ")[0].strip("#")) == 0 and 1 <= lines[0].count("#") <= 6:
            return BlockType.HEADING
    
    # Code: starts and ends with triple backticks
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    # Quote: every line starts with >
    if all(line.startswith(">") for line in lines if line):
        return BlockType.QUOTE
    
    # Unordered list: every line starts with "- " and no empty lines
    non_empty_lines = [line for line in lines if line]
    if (non_empty_lines and 
        all(line.startswith("- ") for line in non_empty_lines) and 
        len(non_empty_lines) == len(lines)):  # No empty lines allowed
        return BlockType.UNORDERED_LIST
    
    # Ordered list: every line starts with number followed by ". "
    if non_empty_lines:  # Ensure non-empty lines
        numbered_lines = [line.split(". ")[0] for line in lines]
        if (all(line.isdigit() for line in numbered_lines) and 
            all(line.startswith(f"{i+1}. ") for i, line in enumerate(lines)) and 
            len(non_empty_lines) == len(lines)):  # No empty lines allowed
            return BlockType.ORDERED_LIST
    
    # Default to paragraph if no other conditions met
    return BlockType.PARAGRAPH