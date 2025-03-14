import unittest
from markdown_splitters import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestMarkdownSplitters(unittest.TestCase):
    
    # Tests for split_nodes_image
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL_TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL_TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )
    
    def test_single_image(self):
        node = TextNode(
            "Text ![img](https://example.com/image.png) more text",
            TextType.NORMAL_TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Text ", TextType.NORMAL_TEXT),
                TextNode("img", TextType.IMAGE, "https://example.com/image.png"),
                TextNode(" more text", TextType.NORMAL_TEXT),
            ],
            new_nodes,
        )
    
    def test_no_images(self):
        node = TextNode("Just plain text", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)
    
    def test_empty_text(self):
        node = TextNode("", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)
    
    def test_non_text_node(self):
        node = TextNode("already bold", TextType.BOLD_TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)
    
    # Tests for split_nodes_link
    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.NORMAL_TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.NORMAL_TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes,
        )
    
    def test_single_link(self):
        node = TextNode(
            "Text [link](https://example.com) more text",
            TextType.NORMAL_TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Text ", TextType.NORMAL_TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" more text", TextType.NORMAL_TEXT),
            ],
            new_nodes,
        )
    
    def test_no_links(self):
        node = TextNode("Just plain text", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)
    
    def test_mixed_content(self):
        node = TextNode(
            "Text ![img](https://img.com/a.png) and [link](https://link.com)",
            TextType.NORMAL_TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Text ![img](https://img.com/a.png) and ", TextType.NORMAL_TEXT),
                TextNode("link", TextType.LINK, "https://link.com"),
            ],
            new_nodes,
        )
    
    def test_multiple_nodes(self):
        nodes = [
            TextNode("First [link1](https://one.com)", TextType.NORMAL_TEXT),
            TextNode("Second [link2](https://two.com) text", TextType.NORMAL_TEXT),
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertListEqual(
            [
                TextNode("First ", TextType.NORMAL_TEXT),
                TextNode("link1", TextType.LINK, "https://one.com"),
                TextNode("Second ", TextType.NORMAL_TEXT),
                TextNode("link2", TextType.LINK, "https://two.com"),
                TextNode(" text", TextType.NORMAL_TEXT),
            ],
            new_nodes,
        )

if __name__ == '__main__':
    unittest.main()
