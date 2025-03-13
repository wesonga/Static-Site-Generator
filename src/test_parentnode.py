import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_with_multiple_children(self):
        children = [
            LeafNode("b", "Bold"),
            LeafNode(None, " Normal "),
            LeafNode("i", "Italic")
        ]
        parent_node = ParentNode("p", children)
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>Bold</b> Normal <i>Italic</i></p>"
        )

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(parent_node.to_html(), '<div class="container"><span>child</span></div>')

    def test_missing_tag_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "Text")])

    def test_missing_children_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)

    def test_nested_parent_nodes(self):
        grandchild = LeafNode("em", "deep")
        child = ParentNode("span", [grandchild])
        parent = ParentNode("section", [child])
        self.assertEqual(parent.to_html(), "<section><span><em>deep</em></span></section>")

if __name__ == "__main__":
    unittest.main()
