import unittest
from block_types import BlockType, block_to_block_type

class TestBlockTypes(unittest.TestCase):
    
    def test_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        
    def test_multi_level_heading(self):
        block = "#### Level 4 heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        
    def test_invalid_heading(self):
        block = "####### Too many hashes"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_code_block(self):
        block = "```\ncode here\nmore code\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        
    def test_single_line_code(self):
        block = "```\nsingle line\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        
    def test_quote_block(self):
        block = "> This is a quote\n> Another line"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        
    def test_single_line_quote(self):
        block = "> Single line quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        
    def test_unordered_list(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        
    def test_single_item_unordered_list(self):
        block = "- Single item"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        
    def test_ordered_list(self):
        block = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        
    def test_single_item_ordered_list(self):
        block = "1. Single item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        
    def test_invalid_ordered_list(self):
        block = "2. Wrong start\n3. Second item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
    def test_paragraph(self):
        block = "This is a normal paragraph with **bold** text"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
    def test_multi_line_paragraph(self):
        block = "First line\nSecond line with _italic_"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
    def test_mixed_content(self):
        block = "Text with > quote-like line\nSecond line"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
    def test_empty_lines_in_list(self):
        block = "- Item 1\n\n- Item 2"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
    def test_code_not_closed(self):
        block = "```\ncode here\nnot closed"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
