import unittest
from textnode import TextNode, TextType
from text_splitter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_single_code_block(self):
        node = TextNode("This is text with a `code block` here", TextType.NORMAL_TEXT)
        expected = [
            TextNode("This is text with a ", TextType.NORMAL_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" here", TextType.NORMAL_TEXT)
        ]
        result = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(result, expected)
    
    def test_single_bold(self):
        node = TextNode("This is **bold** text", TextType.NORMAL_TEXT)
        expected = [
            TextNode("This is ", TextType.NORMAL_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" text", TextType.NORMAL_TEXT)
        ]
        result = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(result, expected)
    
    def test_single_italic(self):
        node = TextNode("This is _italic_ text", TextType.NORMAL_TEXT)
        expected = [
            TextNode("This is ", TextType.NORMAL_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" text", TextType.NORMAL_TEXT)
        ]
        result = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        self.assertEqual(result, expected)
    
    def test_multiple_delimiters(self):
        node = TextNode("Text `code1` and `code2` here", TextType.NORMAL_TEXT)
        expected = [
            TextNode("Text ", TextType.NORMAL_TEXT),
            TextNode("code1", TextType.CODE_TEXT),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode("code2", TextType.CODE_TEXT),
            TextNode(" here", TextType.NORMAL_TEXT)
        ]
        result = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(result, expected)
    
    def test_no_delimiter(self):
        node = TextNode("Plain text here", TextType.NORMAL_TEXT)
        expected = [node]
        result = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(result, expected)
    
    def test_unclosed_delimiter(self):
        node = TextNode("Text with `unclosed code", TextType.NORMAL_TEXT)
        expected = [node]
        result = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(result, expected)
    
    def test_non_text_node(self):
        node = TextNode("code", TextType.CODE_TEXT)
        expected = [node]
        result = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(result, expected)
    
    def test_empty_text(self):
        node = TextNode("", TextType.NORMAL_TEXT)
        expected = [node]
        result = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(result, expected)
    
    def test_multiple_nodes(self):
        nodes = [
            TextNode("First **bold** text", TextType.NORMAL_TEXT),
            TextNode("Second _italic_ text", TextType.NORMAL_TEXT)
        ]
        expected = [
            TextNode("First ", TextType.NORMAL_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" text", TextType.NORMAL_TEXT),
            TextNode("Second _italic_ text", TextType.NORMAL_TEXT)
        ]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD_TEXT)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()