class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""
        output = ""
        for prop in self.props:
            output += f"{prop}={self.props[prop]} "
        return output

    def __eq__(self, node):
        if (
            self.tag == node.tag
            and self.value == node.value
            and self.children == node.children
            and self.props == node.props
        ):
            return True
        return False
