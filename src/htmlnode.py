class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        print(self.props)
        formated_props_string = "{\n"
        for prop in self.props:
            value = self.props[prop]
            formated_props_string = formated_props_string + f"\t\"{prop}\": \"{value}\",\n"
        formated_props_string = formated_props_string + "}"
        return formated_props_string
