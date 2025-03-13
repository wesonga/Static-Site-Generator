import unittest
from textnode import TextNode, TextType
from textnode_to_htmlnode import text_node_to_html_node
from leafnode import LeafNode

class TestTextNodeToHtmlNode(unittest.TestCase):
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold_text(self):
        node = TextNode("This is bold", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")
    
    def test_italic_text(self):
        node = TextNode("This is italic", TextType.ITALIC_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic")
    
    def test_code_text(self):
        node = TextNode("This is code", TextType.CODE_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code")
    
    def test_link(self):
        node = TextNode("Click here", TextType.LINK, "https://www.example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props, {"href": "https://www.example.com"})
    
    def test_image(self):
        node = TextNode("An image", TextType.IMAGE, "https://www.example.com/image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "https://www.example.com/image.jpg", "alt": "An image"})
    
    def test_invalid_link(self):
        node = TextNode("Invalid link", TextType.LINK)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)
    
    def test_invalid_image(self):
        node = TextNode("Invalid image", TextType.IMAGE)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()
