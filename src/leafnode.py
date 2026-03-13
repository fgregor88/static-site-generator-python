class LeafNode:
    def __init__(self, tag=None, value=None, props=None):
        self.tag = tag
        self.value = value
        self.props = props

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        output = ""
        for prop in self.props:
            output += f' {prop}="{self.props[prop]}"'
        return output

    def __eq__(self, node: object) -> bool:
        if not isinstance(node, LeafNode):
            return NotImplemented
        if (
            self.tag == node.tag
            and self.value == node.value
            and self.props == node.props
        ):
            return True
        return False
