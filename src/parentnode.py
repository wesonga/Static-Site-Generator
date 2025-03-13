from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("ParentNode must have a tag")
        if not children:
            raise ValueError("ParentNode must have children")
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")

        # Generate HTML for all children recursively
        children_html = "".join([child.to_html() for child in self.children])

        props_str = self.props_to_html()
        props_str = f" {props_str}" if props_str else ""

        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"
