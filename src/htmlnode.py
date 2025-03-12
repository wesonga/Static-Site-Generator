class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # Set default values if not provided
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        """
        To be overridden by child classes to render HTML.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")

    def props_to_html(self):
        """
        Convert the properties (attributes) dictionary into a string suitable for HTML rendering.
        Example: {"href": "https://www.google.com", "target": "_blank"} becomes
                 'href="https://www.google.com" target="_blank"'
        """
        return " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        """
        Provide a string representation for debugging.
        """
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
