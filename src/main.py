from textnode import TextNode, TextType


def main():
    test = TextNode("test", TextType.PLAIN, "more text")
    print(test)


if __name__ == "__main__":
    main()
