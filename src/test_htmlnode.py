import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        # Test if the props_to_html method correctly converts props to HTML attributes
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_repr(self):
        # Test if __repr__ method correctly represents the HTMLNode object
        node = HTMLNode(tag="p", value="This is a paragraph.", children=[], props={})
        self.assertEqual(repr(node), "HTMLNode(tag=p, value=This is a paragraph., children=[], props={})")

    def test_empty_node(self):
        # Test an HTMLNode without any props, value, or children
        node = HTMLNode()
        self.assertEqual(repr(node), "HTMLNode(tag=None, value=None, children=[], props={})")

if __name__ == "__main__":
    unittest.main()
