import unittest
from markdown_extractors import extract_markdown_images, extract_markdown_links

class TestMarkdownExtractors(unittest.TestCase):
    
    # Tests for extract_markdown_images
    def test_extract_single_image(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_multiple_images(self):
        text = "![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertListEqual(expected, matches)
    
    def test_empty_alt_text(self):
        text = "Image with empty alt ![](https://i.imgur.com/test.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("", "https://i.imgur.com/test.png")], matches)
    
    def test_no_images(self):
        text = "Just plain text with no images"
        matches = extract_markdown_images(text)
        self.assertListEqual([], matches)
    
    # Tests for extract_markdown_links
    def test_extract_single_link(self):
        text = "A link [to boot dev](https://www.boot.dev)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)
    
    def test_extract_multiple_links(self):
        text = "[to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        expected = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ]
        self.assertListEqual(expected, matches)
    
    def test_distinguish_image_from_link(self):
        text = "![image](https://i.imgur.com/test.png) and [link](https://www.example.com)"
        image_matches = extract_markdown_images(text)
        link_matches = extract_markdown_links(text)
        self.assertListEqual([("image", "https://i.imgur.com/test.png")], image_matches)
        self.assertListEqual([("link", "https://www.example.com")], link_matches)
    
    def test_no_links(self):
        text = "Just plain text with no links"
        matches = extract_markdown_links(text)
        self.assertListEqual([], matches)

if __name__ == '__main__':
    unittest.main()
