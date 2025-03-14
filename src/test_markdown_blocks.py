import unittest
from markdown_blocks import markdown_to_blocks

class TestMarkdownBlocks(unittest.TestCase):
    
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_single_block(self):
        md = "Just one paragraph with **bold** text"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["Just one paragraph with **bold** text"]
        )
    
    def test_multiple_newlines(self):
        md = """
# Heading


Paragraph with text

  
- List item 1
- List item 2
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Heading",
                "Paragraph with text",
                "- List item 1\n- List item 2",
            ]
        )
    
    def test_empty_input(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])
    
    def test_only_whitespace(self):
        md = "   \n\n  \n\n   "
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])
    
    def test_complex_document(self):
        md = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item

Another paragraph here
with multiple lines
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
                "- This is the first list item in a list block\n- This is a list item\n- This is another list item",
                "Another paragraph here\nwith multiple lines",
            ]
        )
    
    def test_trailing_newlines(self):
        md = "Paragraph one\n\nParagraph two\n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Paragraph one",
                "Paragraph two",
            ]
        )

if __name__ == '__main__':
    unittest.main()
