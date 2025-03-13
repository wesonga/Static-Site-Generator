import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        # Test equality of two TextNode objects with identical properties
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_equal_text(self):
        # Test when text is different
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a different text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def test_not_equal_text_type(self):
        # Test when text_type is different
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)

    def test_not_equal_url(self):
        # Test when the URL is different
        node = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.LINK, "https://www.different-url.com")
        self.assertNotEqual(node, node2)

    def test_url_is_none(self):
        # Test if URL is None (default value)
        node = TextNode("This is a text node", TextType.LINK)
        self.assertEqual(node.url, None)

    def test_repr(self):
        # Test the __repr__ method of the TextNode class
        node = TextNode("This is a text node", TextType.CODE_TEXT)
        self.assertEqual(repr(node), "TextNode(This is a text node, code, None)")

if __name__ == "__main__":
    unittest.main()
