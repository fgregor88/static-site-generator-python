from textnode import TextNode, TextType
from htmlnode import HtmlNode
from leafnode import LeafNode

def main():
    test = TextNode("test", TextType.PLAIN, "more text")
    print(test)

    htmlnode = HtmlNode("test", "tets", "test", {"color":  "red", "size": "large"})
    print(htmlnode)
    html = htmlnode.props_to_html()
    print(html)

    leafnode = LeafNode("p", "test").to_html()
    print(leafnode)



if __name__ == "__main__":
    main()
