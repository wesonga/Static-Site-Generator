import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextnodes(unittest.TestCase):
    
    def test_mixed_markdown(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.NORMAL_TEXT),
            TextNode("text", TextType.BOLD_TEXT),
            TextNode(" with an ", TextType.NORMAL_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word and a ", TextType.NORMAL_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" and an ", TextType.NORMAL_TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL_TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(expected, result)
    
    def test_plain_text(self):
        text = "Just some plain text"
        result = text_to_textnodes(text)
        expected = [TextNode("Just some plain text", TextType.NORMAL_TEXT)]
        self.assertListEqual(expected, result)
    
    def test_only_bold(self):
        text = "**bold text**"
        result = text_to_textnodes(text)
        expected = [TextNode("bold text", TextType.BOLD_TEXT)]
        self.assertListEqual(expected, result)
    
    def test_multiple_bold(self):
        text = "This **is** some **bold** text"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This ", TextType.NORMAL_TEXT),
            TextNode("is", TextType.BOLD_TEXT),
            TextNode(" some ", TextType.NORMAL_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" text", TextType.NORMAL_TEXT),
        ]
        self.assertListEqual(expected, result)
    
    def test_image_and_link(self):
        text = "![img](https://example.com/img.png) then [link](https://example.com)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("img", TextType.IMAGE, "https://example.com/img.png"),
            TextNode(" then ", TextType.NORMAL_TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
        ]
        self.assertListEqual(expected, result)
    
    def test_empty_string(self):
        text = ""
        result = text_to_textnodes(text)
        expected = [TextNode("", TextType.NORMAL_TEXT)]
        self.assertListEqual(expected, result)
    
    def test_complex_mixed(self):
        text = "A **bold** word _italic_ `code` ![img](https://img.com/a.png)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("A ", TextType.NORMAL_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" word ", TextType.NORMAL_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" ", TextType.NORMAL_TEXT),
            TextNode("code", TextType.CODE_TEXT),
            TextNode(" ", TextType.NORMAL_TEXT),
            TextNode("img", TextType.IMAGE, "https://img.com/a.png"),
        ]
        self.assertListEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
