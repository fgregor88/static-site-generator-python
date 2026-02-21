from textnode import TextNode, TextType
from htmlnode import HtmlNode

def main():
    test = TextNode("test", TextType.PLAIN, "more text")
    print(test)

    htmlnode = HtmlNode("test", "tets", "test", {"color":  "red", "size": "large"})
    print(htmlnode)
    html = htmlnode.props_to_html()
    print(html)



if __name__ == "__main__":
    main()
