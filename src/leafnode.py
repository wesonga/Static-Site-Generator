from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        
        if self.tag is None:
            return self.value  # Return raw text if no tag

        props_str = self.props_to_html()
        props_str = f" {props_str}" if props_str else ""

        # Return the HTML formatted element
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
