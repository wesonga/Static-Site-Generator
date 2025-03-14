def markdown_to_blocks(markdown):
    """
    Splits a raw Markdown string into a list of block strings.
    
    Blocks are separated by double newlines. Leading and trailing whitespace
    is stripped from each block, and empty blocks are removed.
    
    :param markdown: Raw Markdown string representing a full document
    :return: List of block strings
    """
    # Split on double newlines and filter out empty blocks
    blocks = [block.strip() for block in markdown.split("\n\n") if block.strip()]
    return blocks
