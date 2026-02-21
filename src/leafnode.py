class LeafNode:
    def __init__(self, tag=None, value=None, props=None):
        self.tag = tag
        self.value = value
        self.props = props

    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.props})"

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        output = ""
        for prop in self.props:
            output += f"{prop}={self.props[prop]} "
        return output

    def __eq__(self, node):
        if (
            self.tag == node.tag
            and self.value == node.value
            and self.props == node.props
        ):
            return True
        return False
