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
        output = ""
        for prop in self.props:
            output += f"{prop}={self.props[prop]} "
        return output

    def dict_to_string(self):
        print(self.props)
        formated_props_string = "{\n"
        for prop in self.props:
            value = self.props[prop]
            formated_props_string = formated_props_string + f"\t\"{prop}\": \"{value}\",\n"
        formated_props_string = formated_props_string + "}"
        return formated_props_string

    #tag value children props

    def __eq__(self, node):
        if (
            self.tag == node.tag
            and self.value == node.value
            and self.children == node.children
            and self.props == node.props
        ):
            return True
        return False
